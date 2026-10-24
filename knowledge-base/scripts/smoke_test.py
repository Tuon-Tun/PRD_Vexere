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
    "Goals & Success Metrics",
    "Scope",
    "Glossary",
    "Business Rules",
    "Process Diagrams",
    "Feature Epics & User Stories",
    "Use Case Specifications",
    "Traceability Matrix",
    "Non-Functional Requirements",
    "UI/UX Specifications",
    "Dependencies & Impacted Areas",
    "Assumptions & Open Questions",
]


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
    assert_true("Done when" in content, "Product framing skill is missing acceptance criteria guidance")
    assert_true("Rules applied" in content, "Product framing skill is missing the Rules applied line")
    # Rules applied lists direct citations only; a chain followed to the end lists most of the register.
    for rel in (
        "knowledge-base/product-framing/SKILL.md",
        "knowledge-base/prd-template/SKILL.md",
        "knowledge-base/prd-template/resources/prd-template.md",
        "knowledge-base/prd-reviewer.md",
        "knowledge-base/knowledge/user-story-skill/SKILL.md",
    ):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert_true("all the way down" not in text, f"{rel} still follows Rules applied all the way down")
    # Rules must get their IDs before the stories that cite them are written.
    rules_at = content.find("## 3. Business Rules")
    stories_at = content.find("## 7. Epics & User Stories")
    assert_true(
        0 <= rules_at < stories_at,
        "Product framing output must define Business Rules before Epics & User Stories",
    )


def check_prd_sections():
    guide = ROOT / "knowledge-base/product-language/SKILL.md"
    assert_true(guide.is_file(), "Product language guide is missing")

    skill = (ROOT / "knowledge-base/prd-template/SKILL.md").read_text(encoding="utf-8")
    mapped = re.findall(r'^\| `"([^"]+)"` \|', skill, flags=re.MULTILINE)
    assert_true(mapped == ACTIVE_SECTIONS, "prd-template/SKILL.md section mapping drifted from Active_Sections")

    template = (ROOT / "knowledge-base/prd-template/resources/prd-template.md").read_text(encoding="utf-8")
    for heading in ("### 1.3 How to Read This PRD", "### 2.1 Summary", "### 2.5 Scope", "### 2.6 Glossary",
                    "#### Traceability Matrix", "### 3.7 Dependencies & Impacted Areas",
                    "## 4. Assumptions & Open Questions"):
        assert_true(heading in template, f"PRD template is missing heading: {heading}")
    assert_true("API / Technical Specs" not in template, "PRD template still contains the technical specs section")
    # Rules are defined before the stories that cite them, in the PRD as in the framing pack.
    assert_true(
        0 <= template.find("### 3.1 Business Rules") < template.find("### 3.3 Feature Epics & User Stories"),
        "PRD template must place Business Rules (3.1) before Feature Epics & User Stories (3.3)",
    )
    assert_true(
        "#### Functional Requirements" not in template,
        "PRD template still contains the Functional Requirements table",
    )

    framing = (ROOT / "knowledge-base/product-framing/SKILL.md").read_text(encoding="utf-8")
    for name, text in (("PRD template", template), ("Product framing skill", framing)):
        # Shared side-effects of a status live once, on its "on entering" row.
        assert_true("**On Entering a Status**" in text, f"{name} is missing the On Entering a Status table")
    for path in sorted((ROOT / "knowledge-base").rglob("*.md")):
        assert_true(
            "Also cites" not in path.read_text(encoding="utf-8"),
            f"{path.relative_to(ROOT)} still uses the removed 'Also cites' line",
        )

    writer = (ROOT / "prd-writer.md").read_text(encoding="utf-8")
    agenda = re.findall(r"^  \d+\. (.+?) — ", writer, flags=re.MULTILINE)
    assert_true(agenda == ACTIVE_SECTIONS, "prd-writer.md Step 0 agenda drifted from Active_Sections")


def main():
    check_input_schema()
    check_export_schema()
    check_create_domain_helper()
    check_export_helper()
    check_product_framing_skill()
    check_prd_sections()
    print(json.dumps({"status": "success", "checks": 6}))


if __name__ == "__main__":
    main()
