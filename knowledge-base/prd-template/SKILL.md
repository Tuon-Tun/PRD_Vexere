---
name: prd-template-renderer
description: >
  Render a full product-first PRD from an approved structured brief, an approved Product Framing
  Pack, and domain context. Use when the orchestrator has already collected and approved the feature
  JSON and the framing pack and needs the standard PRD filled end-to-end without re-interviewing the user.
---

# PRD Template Renderer

Produce a complete PRD from an approved structured brief and an approved Product Framing Pack, then fill `resources/prd-template.md`.
Scope: PRD drafting only. Review and export are separate steps in the pipeline.

The PRD is product first. It hands over the rules, the logic, and the core value of the feature so that PO, BA, Dev, and QC understand them the same way. It describes WHAT and WHY, never HOW. Every fact is written once, in its home section, and cited by ID everywhere else. Every sentence follows `knowledge-base/product-language/SKILL.md`, including its "Where each fact lives" table.

---

## Phase 1 - Inputs

Before drafting, confirm you have:

1. The approved JSON brief from Step 1
2. The approved Product Framing Pack from Step 2: JTBD, business rules, messages, common behaviors, referenced items, epics, user stories with acceptance criteria, assumptions, and open questions, all with their IDs
3. Domain context from `domain-knowledge/[Domain_Name]/rules.md` when running in `IDE_FULL_PIPELINE`
4. Relevant domain history from prior approved PRDs, if present
5. Standards from:
   - `knowledge-base/product-language/SKILL.md`
   - `knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
   - `knowledge-base/knowledge/user-story-skill/SKILL.md`

Do not re-interview the user if the orchestrator already completed the JSON and Product Framing approval steps. Only stop and request clarification if a critical field remains blocked after Step 2 approval.
If JTBD research is not provided in the approved brief, Product Framing Pack, or domain context, label JTBD outputs as hypothesized and needing validation.

---

## Phase 2 - Draft

Load `resources/prd-template.md`. Fill every section listed in `Active_Sections`. For any section **not** in `Active_Sections`, replace its entire content with `_Section excluded at user's request._` and keep the heading so the document structure stays intact. Use `TBD` only when the approved inputs still contain an unresolved gap.

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
| `"Traceability Matrix"` | Traceability Matrix in 3.5 |
| `"Non-Functional Requirements"` | Non-Functional Requirements table in 3.5 |
| `"UI/UX Specifications"` | 3.6 |
| `"Dependencies & Impacted Areas"` | 3.7 |
| `"Assumptions & Open Questions"` | 4 |

**Sections that define cited IDs:** a section that defines IDs other sections cite is never left empty while those IDs are cited. If one was excluded but its IDs are still cited, keep only its defining table, with a one-line note that it is kept because other sections cite it: 3.1 Common Behaviors and stories (`CB-`, `US-`, AC numbers), 3.2 Business Rules (`BR-`), 3.6 Messages (`MSG-`), 2.4 Success Metrics (`SM-`), the Non-Functional Requirements table (`NFR-`), 3.7 Dependencies (`DEP-`), and Section 4 (`A-`, `Q-`).

**Where each section comes from:**

- The approved Product Framing Pack is the source of truth for 2.3 JTBD, 3.1 (common behaviors, stories, priorities, Common behaviors and Rules applied lines, acceptance criteria), 3.2 Business Rules, 3.6 Messages, the `SM-`, `NFR-`, and `DEP-` tables, and the Assumptions and Open Questions. Render them with their IDs unchanged. Do not re-derive them from the JSON, and do not reword them.
- 2.1, 2.2, the goals in 2.4, 2.5, 3.6 Screens, 3.7 Impacted Areas, and Known Constraints come from the JSON, written so that they cite IDs instead of restating rules.
- 2.6 Glossary comes from the JSON `Glossary` plus every status and role named in the approved business rules, using the names the rules use.
- 3.3 comes from diagram-writer (Phase 3). 3.4 takes its step order from `User_Flow`, and each step cites the AC, CB, BR, or MSG that defines its outcome. The Traceability Matrix is built from the citations in 3.1, 3.4, the Rules column of 3.6 Messages, and the rules that cite other rules in 3.2.
- If drafting reveals an outcome no acceptance criterion defines, do not write it into another section. Add it as an Open Question so the user can approve it at Step 5.

**Product-first rules:**

- Write for four readers: PO, BA, Dev, and QC. Every sentence must be understandable without technical background.
- Never write technical detail: endpoints, HTTP methods or status codes, payloads, JSON, error codes, database tables or fields, internal services or modules, frameworks, code, configuration keys, tracking event names, or infrastructure. The system is one black box.
- Translate technical wording from the brief into business meaning instead of copying it. User-stated delivery constraints go once, as stated, into 3.7 Known Constraints (from `Known_Constraints`).
- Where a requirement needs a technical decision, state the business need and add an Open Question in Section 4 with Owner `Dev / Tech Lead`. Do not answer it.
- Use the terms defined in 2.6 Glossary consistently.

**Single-home rules:**

- A rule's value, formula, or condition appears only in its 3.2 row. A message's wording appears only in 3.6 Messages. A metric's baseline and target appear only in its row of the 2.4 Success Metrics table; the Goals, 2.1, and 2.2 name the outcome and cite the `SM-` ID. A quality target appears only in the Non-Functional Requirements table. Everywhere else, cite the ID.
- A rule from another approved PRD is cited as `[Other PRD name] BR-02`, never copied, and that PRD is listed in 3.7 Dependencies.
- 2.1 Summary names the headline metric with its `SM-` ID, without its target.
- 2.5 Scope lists capabilities at epic or story level with their IDs, never rule values.
- 2.6 Glossary gives each status and role a one-line meaning; their transitions and permissions are cited by `BR-` ID. A term a rule defines gets its meaning without the value and cites the rule.
- 3.4 Use Cases: write one only for a flow with several user actions and system responses in between, or that branches on a business condition; one use case may cover several stories. Steps hold only the order and cite AC, CB, BR, and MSG IDs. Add a branch row only where the flow really branches; there is no minimum. If no flow qualifies, write the "No use case needed" line from the template.
- 3.5 Traceability Matrix: one row per BR, columns BR | Cited by (AC / CB) | UC | MSG, IDs only. Cited by lists the AC and CB IDs that cite the rule plus "via BR-.." for each rule that uses it. MSG lists the messages whose Rules column names the rule. A removed rule shows "No longer applies". A rule cited from another PRD gets its own row, named with that PRD. Each story that applies no rule gets a row with "—" in the BR column.
- 3.6 Screens lists screens and the stories shown on each; behavior lives in the acceptance criteria.
- 3.7 Dependencies: "If it is unavailable" cites the rule, common behavior, or acceptance criterion that defines the outcome. Impacted Areas cite story and rule IDs.
- Open or assumed values: the rule's Rule cell says `TBD (Q-..)` or `[value] (assumed, A-..)`; the question or assumption cites the rule ID and states only the open point.
- Non-Functional Requirements are business-level expectations. If no target is given, write `TBD` and add an Open Question for Dev / Tech Lead.
- Section 4 renders the Pack's assumptions and open questions with their IDs unchanged. Add a new `Q-` item only for a gap found while drafting, numbered after the highest ID used so far.
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
- The partners, teams, or existing features involved, from the `DEP-` items
- The happy path steps from `User_Flow` (the 3.4 main flow when one exists), each with its AC or BR ID
- The branches defined by the acceptance criteria, common behaviors, and status transitions, each with its AC, CB, or BR ID

After `diagram-writer` returns the output, embed it verbatim in Section 3.3 of the PRD.

---

## Phase 4 - Versioning

Do not pre-fill Version History by default; the PM owns it. Keep the table format empty unless the workflow explicitly requests a starting row. If a starting row is explicitly requested, use `0.1`, today's date, `PRD pipeline`, and `Initial draft`.

---

## Quality Checklist

- All template section headers are present, including 1.3 and 2.1.
- Sections absent from `Active_Sections` contain only `_Section excluded at user's request._`, except the defining table of a section whose IDs are still cited.
- Section 3.3 contains only the diagrams explicitly requested by the user.
- No blank sections remain; use `TBD` when information is still pending.
- No technical detail appears anywhere (run the self-check in `knowledge-base/product-language/SKILL.md`).
- No rule value, formula, condition, message wording, or target appears outside its home section.
- Every story has Priority, Common behaviors, and Rules applied lines; Rules applied follows the definition in `knowledge-base/product-framing/SKILL.md` exactly (acceptance criteria and common behaviors, then every BR cited in those rules' rows all the way down, the "on entering" row of each transition's new status, and the Rules column of every cited message; rules from another PRD listed but not followed).
- Every cited ID exists in this PRD or carries the name of a PRD listed in 3.7; every BR is cited or used by another rule, except rows marked "No longer applies", which nothing cites; and the Traceability Matrix holds IDs only.
- IDs match the approved Product Framing Pack.
- Terms match the Glossary throughout.
- The language matches the user's language.
