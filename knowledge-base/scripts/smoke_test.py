#!/usr/bin/env python3
import importlib.machinery
import importlib.util
import json
import os
import re
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

# Optional PRD sections, in template order. Document Info and Summary are always included.
ACTIVE_SECTIONS = [
    "Problem Statement",
    "JTBD",
    "Goals",
    "Success Metrics",
    "Glossary",
    "General Rules",
    "Process Diagrams",
    "Feature Epics & User Stories",
    "Non-Functional Requirements",
    "Screens",
]

# Codes a human reader would have to look up. A PRD names these things in words; only story IDs
# (US-01) and AC numbers within a story remain.
CODE = re.compile(r"\b(?:BR|MSG|CB|SCR|NFR|DEP|SM|JTBD|UC|RN|A|Q)-\d+\b")


def fail(message):
    print(json.dumps({"status": "error", "message": message}))
    sys.exit(1)


def load_json(relative_path):
    path = ROOT / relative_path
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as exc:
        fail(f"Could not read {relative_path}: {exc}")


def load_module(name, relative_path):
    path = ROOT / relative_path
    loader = importlib.machinery.SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    if spec is None:
        fail(f"Could not load module spec for {relative_path}")

    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def assert_true(condition, message):
    if not condition:
        fail(message)


def check_input_schema():
    schema = load_json("knowledge-base/input-router/resources/output_schema.json")
    required = set(schema.get("required", []))

    expected_required = {
        "Delivery_Mode",
        "Output_Artifacts",
        "Active_Sections",
        "Wireframes_Requested",
        "Clarification_Confirmed",
        "Domain_Name",
        "Feature_Name",
        "Input_Type",
        "Core_Objective",
        "Problem_Statement",
        "JTBD_Candidates",
        "Target_Users",
        "Scope",
        "Glossary",
        "Epic_Candidates",
        "User_Story_Candidates",
        "User_Flow",
        "Business_Logic_and_Rules",
        "Non_Functional_Requirements",
        "Success_Metrics",
        "UI_UX_Requirements",
        "Dependencies_and_Impacted_Areas",
        "Known_Constraints",
        "Diagram_Requirements",
        "Assumptions",
        "Missing_Information",
    }

    assert_true(schema.get("$schema"), "Input schema is missing $schema")
    assert_true(required == expected_required, "Input schema required fields drifted")

    assert_true(
        set(schema["properties"]["Delivery_Mode"].get("enum", []))
        == {"IDE_FULL_PIPELINE", "CHAT_TEXT_ONLY"},
        "Delivery_Mode enum is invalid",
    )
    assert_true(
        set(schema["properties"]["Output_Artifacts"]["items"].get("enum", []))
        == {"Text Response", "Markdown File", "DOCX File"},
        "Output_Artifacts enum is invalid",
    )

    diagram_items = schema["properties"]["Diagram_Requirements"]["items"]
    assert_true(
        set(diagram_items.get("enum", []))
        == {"None", "Activity Diagram", "Sequence Diagram", "BPMN"},
        "Diagram_Requirements enum is invalid",
    )

    active_sections_items = schema["properties"]["Active_Sections"]["items"]
    assert_true(
        active_sections_items.get("enum", []) == ACTIVE_SECTIONS,
        "Active_Sections enum is invalid",
    )
    assert_true(
        schema["properties"]["Clarification_Confirmed"].get("type") == "boolean",
        "Clarification_Confirmed must be a boolean",
    )

    domain_pattern = schema["properties"]["Domain_Name"]["pattern"]
    assert_true(
        re.match(domain_pattern, "payment-gateway") is not None,
        "Domain_Name pattern rejects a valid slug",
    )
    assert_true(
        re.match(domain_pattern, "Payment Gateway") is None,
        "Domain_Name pattern accepts an invalid slug",
    )


def check_export_schema():
    schema = load_json("knowledge-base/docx-converter/resources/export_tool_schema.json")
    input_schema = schema.get("input_schema", {})
    one_of = input_schema.get("oneOf", [])

    assert_true(schema.get("script_path") == "knowledge-base/scripts/export_docx.py", "Export script path drifted")
    assert_true(
        {"input_path", "output_path"}.issubset(input_schema.get("properties", {})),
        "Export schema is missing file-based arguments",
    )
    assert_true(len(one_of) == 2, "Export schema must support file and inline modes")


def check_create_domain_helper():
    create_domain = load_module("create_domain", "knowledge-base/scripts/create_domain.py")

    assert_true(
        create_domain.normalize_domain_name("Payment Gateway") == "payment-gateway",
        "Domain normalization failed",
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        result = json.loads(
            create_domain.create_domain_files(
                "Payment Gateway",
                "# Domain Rules\nSmoke test domain.",
                project_root=temp_dir,
            )
        )

        assert_true(result["status"] == "success", "Domain creation did not succeed")
        assert_true(Path(result["inputs_path"]).is_dir(), "inputs directory was not created")
        assert_true(Path(result["prds_path"]).is_dir(), "PRDs directory was not created")
        assert_true(Path(result["rules_path"]).is_file(), "rules.md was not created")


def check_export_helper():
    export_docx = load_module("export_docx", "knowledge-base/scripts/export_docx.py")

    assert_true(
        export_docx.sanitize_filename('PRD: Feature/Name?.docx')
        == "PRD_ Feature_Name_.docx",
        "Filename sanitization failed",
    )
    assert_true(
        export_docx.default_docx_path("domain-knowledge/demo/PRDs/demo_PRD.md").endswith(
            os.path.join("domain-knowledge", "demo", "PRDs", "demo_PRD.docx")
        ),
        "Default DOCX path failed",
    )
    stripped = export_docx.strip_reviewer_notes(
        "# PRD\n\n## Overview\nIntro.\n\n"
        "> [!WARNING] REVIEWER'S NOTE (RN-01)\n"
        "> **Risk:** Gap.\n"
        "> **Option A:** Fix A.\n"
        "> **Option B:** Fix B.\n\n"
        "## Requirements\nKeep me.\n\n"
        "> [!WARNING] REVIEWER'S NOTE (RN-02)\n"
        "> **Risk:** Gap two.\n"
        "> **Option A:** Fix A2.\n"
        "> **Option B:** Fix B2.\n\n"
        "## Next\nContent\n"
    )
    assert_true("REVIEWER'S NOTE" not in stripped, "Reviewer note stripping failed")
    # Content between and after notes must survive: a DOTALL regex would greedily
    # consume everything from the first note to end of file.
    assert_true(
        "## Requirements" in stripped and "Keep me." in stripped,
        "Reviewer note stripping removed content between notes",
    )
    assert_true(
        "## Next" in stripped and "Content" in stripped,
        "Reviewer note stripping removed content after the note block",
    )


def check_product_framing_skill():
    path = ROOT / "knowledge-base/product-framing/SKILL.md"
    assert_true(path.is_file(), "Product framing skill is missing")

    content = path.read_text(encoding="utf-8")
    assert_true("Product Framing Pack" in content, "Product framing skill is missing its output contract")
    assert_true("**Rules for this epic**" in content, "Product framing skill is missing the epic rules block")
    # Readers never memorize codes: no skill asks for rule lists, "Done when", or cross-reference tables.
    for rel in (
        "knowledge-base/product-framing/SKILL.md",
        "knowledge-base/prd-template/SKILL.md",
        "knowledge-base/prd-template/resources/prd-template.md",
        "knowledge-base/prd-reviewer.md",
        "knowledge-base/knowledge/user-story-skill/SKILL.md",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        for phrase in ("Rules applied", "Done when", "Traceability Matrix", "Rules by Story", "Story rules"):
            assert_true(phrase not in text, f"{rel} still mentions '{phrase}'")
    # General rules come before the stories that apply them.
    rules_at = content.find("## 3. General Rules")
    stories_at = content.find("## 4. Epics & User Stories")
    assert_true(
        0 <= rules_at < stories_at,
        "Product framing output must put General Rules before Epics & User Stories",
    )


def check_prd_sections():
    guide = ROOT / "knowledge-base/product-language/SKILL.md"
    assert_true(guide.is_file(), "Product language guide is missing")

    skill = (ROOT / "knowledge-base/prd-template/SKILL.md").read_text(encoding="utf-8")
    mapped = re.findall(r'^\| `"([^"]+)"` \|', skill, flags=re.MULTILINE)
    assert_true(mapped == ACTIVE_SECTIONS, "prd-template/SKILL.md section mapping drifted from Active_Sections")

    template = (ROOT / "knowledge-base/prd-template/resources/prd-template.md").read_text(encoding="utf-8")
    for heading in ("### 1.2 References", "### 2.1 Problem Statement / Context", "### 2.2 Job to Be Done (JTBD)",
                    "### 2.3 Goals", "### 2.4 Success Metrics", "### 2.5 Glossary", "### 3.1 General Rules",
                    "### 3.3 Feature Epics & User Stories", "### 3.4 Non-Functional Requirements", "### 3.5 Screens"):
        assert_true(heading in template, f"PRD template is missing heading: {heading}")
    # Sections readers found useless or impossible to follow are gone.
    for removed in ("How to Read This PRD", "### 2.1 Summary", "Scope", "Use Case", "Traceability", "Rules by Story",
                    "**Messages**", "Dependencies & Impacted Areas", "Assumptions & Open Questions", "INVEST",
                    "Priority", "Common behaviors", "Why it matters", "API / Technical Specs"):
        assert_true(removed not in template, f"PRD template still contains '{removed}'")
    assert_true(not CODE.search(template), "PRD template still uses codes")
    assert_true(
        0 <= template.find("### 3.1 General Rules") < template.find("### 3.3 Feature Epics & User Stories"),
        "PRD template must place General Rules (3.1) before Feature Epics & User Stories (3.3)",
    )

    framing = (ROOT / "knowledge-base/product-framing/SKILL.md").read_text(encoding="utf-8")
    for name, text in (("PRD template", template), ("Product framing skill", framing)):
        # What happens however a status is reached is written once, on its "when it enters" row.
        assert_true("When it enters" in text, f"{name} is missing the 'When it enters' table")
    for path in sorted((ROOT / "knowledge-base").rglob("*.md")):
        assert_true(
            "Also cites" not in path.read_text(encoding="utf-8"),
            f"{path.relative_to(ROOT)} still uses the removed 'Also cites' line",
        )

    writer = (ROOT / "prd-writer.md").read_text(encoding="utf-8")
    agenda = re.findall(r"^  \d+\. (.+?) — ", writer, flags=re.MULTILINE)
    assert_true(agenda == ACTIVE_SECTIONS, "prd-writer.md Step 0 agenda drifted from Active_Sections")


def check_domain_prds():
    # Every approved PRD in the repository reads without codes.
    for path in sorted((ROOT / "domain-knowledge").glob("*/PRDs/*_PRD.md")):
        text = path.read_text(encoding="utf-8")
        found = sorted(set(CODE.findall(text)))
        assert_true(not found, f"{path.relative_to(ROOT)} still uses codes: {', '.join(found[:10])}")
        assert_true("Done when" not in text, f"{path.relative_to(ROOT)} still uses 'Done when'")


def main():
    check_input_schema()
    check_export_schema()
    check_create_domain_helper()
    check_export_helper()
    check_product_framing_skill()
    check_prd_sections()
    check_domain_prds()
    print(json.dumps({"status": "success", "checks": 7}))


if __name__ == "__main__":
    main()
