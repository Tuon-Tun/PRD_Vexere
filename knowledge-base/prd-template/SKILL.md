---
name: prd-template-renderer
description: >
  Render a full product-first PRD from an approved structured brief and domain context. Use when
  the orchestrator has already collected and approved the feature JSON and needs the standard PRD
  filled end-to-end without re-interviewing the user.
---

# PRD Template Renderer

Produce a complete PRD from an approved structured brief, then fill `resources/prd-template.md`.
Scope: PRD drafting only. Review and export are separate steps in the pipeline.

The PRD is product first. It hands over the rules, the logic, and the core value of the feature so that PO, BA, Dev, and QC understand them the same way. It describes WHAT and WHY, never HOW. Every sentence follows `knowledge-base/product-language/SKILL.md`.

---

## Phase 1 - Inputs

Before drafting, confirm you have:

1. The approved JSON brief from Step 1
2. The approved Product Framing Pack from Step 2, including JTBD statements, Epics, User Stories, Acceptance Criteria, and open questions
3. Domain context from `domain-knowledge/[Domain_Name]/rules.md` when running in `IDE_FULL_PIPELINE`
4. Relevant domain history from prior PRDs or inputs, if present
5. Standards from:
   - `knowledge-base/product-language/SKILL.md`
   - `knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
   - `knowledge-base/knowledge/user-story-skill/SKILL.md`

Do not re-interview the user if the orchestrator already completed the JSON and Product Framing approval steps. Only stop and request clarification if a critical field remains blocked after Step 2 approval.
If JTBD research is not provided in the approved brief, Product Framing Pack, or domain context, label JTBD outputs as hypothesized and needing validation.

---

## Phase 2 - Draft

Load `resources/prd-template.md`. Fill every section listed in `Active_Sections` from the approved JSON. For any section **not** in `Active_Sections`, replace its entire content with `_Section excluded at user's request._` and keep the heading so the document structure stays intact. Use `TBD` only when the approved brief still contains an unresolved gap.

**Always included:** Section 1 Document Info (1.1 and 1.2 stay as empty tables for the PM; 1.3 is kept as is, translated) and Section 2.1 Summary. They are not part of `Active_Sections` and are never excluded.

**Section mapping:**

| `Active_Sections` value | Template section |
|-------------------------|------------------|
| `"Problem Statement"` | 2.2 |
| `"JTBD"` | 2.3 |
| `"Goals & Success Metrics"` | 2.4 |
| `"Scope"` | 2.5 |
| `"Glossary"` | 2.6 |
| `"Feature Epics & User Stories"` | 3.1 |
| `"Business Rules"` | 3.2 |
| `"Process Diagrams"` | 3.3 |
| `"Use Case Specifications"` | 3.4 |
| `"Functional Requirements"` | Functional Requirements table in 3.5 |
| `"Non-Functional Requirements"` | Non-Functional Requirements table in 3.5 |
| `"UI/UX Specifications"` | 3.6 |
| `"Dependencies & Impacted Areas"` | 3.7 |
| `"Assumptions & Open Questions"` | 4 |

**Product-first rules:**

- Write for four readers: PO, BA, Dev, and QC. Every sentence must be understandable without technical background.
- Never write technical detail: endpoints, HTTP methods or status codes, payloads, JSON, error codes, database tables or fields, internal services or modules, frameworks, code, configuration keys, or infrastructure. The system is one black box.
- Translate technical wording from the brief into business meaning instead of copying it. User-stated constraints go once, as stated, into 3.7 Known Constraints (from `Known_Constraints`).
- Be specific: every business rule has concrete values, a trigger condition, and what the user sees. Every calculation has a worked example with real numbers.
- Where a requirement needs a technical decision, state the business need and add an Open Question in Section 4 with Owner `Dev / Tech Lead`. Do not answer it.
- Use the terms defined in 2.6 Glossary consistently. Add any business term, status, or role a new reader could misread.

**Content rules:**

- Acceptance Criteria must follow the `Done when` standard from `user-story-skill` and describe observable outcomes. Reference the business rule an AC verifies, for example `(BR-02)`.
- Apply JTBD and user-story standards strictly; do not shortcut them to save tokens.
- Use the approved Product Framing Pack as the source of truth for Section 2.3 and Section 3.1.
- If `Epic_Candidates` or `User_Story_Candidates` are present in the brief, use them only as seeds already resolved by the approved Product Framing Pack.
- Build 2.5 Scope from `Scope`. Never invent Out of scope items; if none were confirmed, write `TBD` and add an Open Question.
- Build 2.6 Glossary from `Glossary` plus the business terms used in the PRD. Define terms from the input context only; mark unclear terms `TBD`.
- Build 3.2 from `Business_Logic_and_Rules`. Give every rule an ID (`BR-01`, `BR-02`, ...). Fill Statuses & Transitions and Roles & Permissions only when the feature has statuses or more than one role; otherwise remove those blocks.
- Build 3.7 from `Dependencies_and_Impacted_Areas` and `Known_Constraints`, in business terms.
- Surface `Assumptions`, `Missing_Information`, and unresolved `[NEEDS_CLARIFICATION]` items in Section 4 Assumptions & Open Questions.
- Functional Requirements must include a `High / Medium / Low` priority and the related story or rule ID.
- Non-Functional Requirements are business-level expectations. If no target is given, write `TBD` and add an Open Question for Dev / Tech Lead.
- Use Case tables must include Actor, Precondition, Postcondition, Main Flow, Alternative Flow, and Exception Flow. Exception flows describe what happens and what the user sees, never technical causes.
- List every user-facing message in 3.6 User-facing Messages with an ID (`MSG-01`, ...). Mark copy you wrote yourself as `(proposed copy)`.
- Section 3.3 must include only the diagram types explicitly approved by the user.
- Preserve the selected `Delivery_Mode`; drafting does not decide whether to save files or export DOCX.

---

## Phase 3 - Section 3.3 Diagrams

**Critical rule:** Only generate diagrams for the types explicitly approved by the user in Step 0 or Step 1. Do not substitute plain text or Mermaid when BPMN, Activity Diagram, or Sequence Diagram is requested.

When Section 3.3 needs one or more diagrams, **delegate entirely to `knowledge-base/prd-template/diagram-writer/SKILL.md`** using its Input Contract. Do not generate diagram code inline here.

Pass to `diagram-writer`:
- The diagram type(s) from `Diagram_Requirements` in the approved JSON
- The feature name and description
- The actors involved, from `Target_Users`
- The partners, teams, or existing features involved, from `Dependencies_and_Impacted_Areas`
- The happy path steps from `User_Flow`
- Key edge cases and error scenarios from `Business_Logic_and_Rules`

After `diagram-writer` returns the output, embed it verbatim in Section 3.3 of the PRD.

---

## Phase 4 - Versioning

Do not pre-fill Version History by default; the PM owns it. Keep the table format empty unless the workflow explicitly requests a starting row. If a starting row is explicitly requested, use `0.1`, today's date, `PRD pipeline`, and `Initial draft`.

---

## Quality Checklist

- All template section headers are present, including 1.3 and 2.1.
- Sections absent from `Active_Sections` contain only `_Section excluded at user's request._`.
- Section 3.3 contains only the diagrams explicitly requested by the user.
- No blank sections remain; use `TBD` when information is still pending.
- No technical detail appears anywhere (run the self-check in `knowledge-base/product-language/SKILL.md`).
- Every rule, story, use case, requirement, and message has an ID, and AC reference the rules they verify.
- Terms match the Glossary throughout.
- The language matches the user's language.
