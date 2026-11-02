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

The PRD is product first and human first. It hands over the rules, the logic, and the core value of the feature so that PO, BA, Dev, and QC understand them the same way, reading it top to bottom without looking anything up. It describes WHAT and WHY, never HOW. Every sentence follows `knowledge-base/product-language/SKILL.md`, including its "Where each fact lives" table.

---

## Phase 1 - Inputs

Before drafting, confirm you have:

1. The approved JSON brief from Step 1
2. The approved Product Framing Pack from Step 2: JTBD, general rules, epics with their rules, user stories with their rules and acceptance criteria, and the optional parts the user chose
3. Domain context from `domain-knowledge/[Domain_Name]/rules.md` when running in `IDE_FULL_PIPELINE`
4. Relevant domain history from prior approved PRDs, if present
5. Standards from:
   - `knowledge-base/product-language/SKILL.md`
   - `knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
   - `knowledge-base/knowledge/user-story-skill/SKILL.md`

Do not re-interview the user if the orchestrator already completed the JSON and Product Framing approval steps. Only stop and request clarification if a critical field remains blocked after Step 2 approval.

---

## Phase 2 - Draft

Load `resources/prd-template.md`. Fill every section listed in `Active_Sections`. Drop every section that is **not** listed, heading included, and renumber the sections after it, so the reader never meets an empty or "excluded" section. Use `TBD` only when the approved inputs still contain an unresolved gap, with who decides in words.

**Always included:** Section 1 Document Info (1.1 stays an empty table for the PM; 1.2 keeps its four pre-seeded rows with empty Link and PIC cells). It is not part of `Active_Sections`.

**Section mapping:**

| `Active_Sections` value | Template section |
|-------------------------|------------------|
| `"Problem Statement"` | 2.1 |
| `"JTBD"` | 2.2 |
| `"Goals"` | 2.3 |
| `"Success Metrics"` | 2.4 |
| `"Glossary"` | 2.5 |
| `"General Rules"` | 3.1 |
| `"Process Diagrams"` | 3.2 |
| `"Feature Epics & User Stories"` | 3.3 |
| `"Non-Functional Requirements"` | 3.4 |
| `"Screens"` | 3.5 |

**Where each section comes from:**

- The approved Product Framing Pack is the source of truth for 2.2 JTBD, 3.1 General Rules, 3.3 (epics, epic rules, stories, story rules, acceptance criteria), 2.4 Success Metrics, 3.4 Non-Functional Requirements, and 3.5 Screens. Render them as approved. Do not re-derive them from the JSON, and do not reword them.
- 2.1 and 2.3 come from the JSON (`Problem_Statement`, `Core_Objective`), written as plain prose with no codes and no rule values. `Known_Constraints` is not rendered: the orchestrator lists it for the user at Step 5.
- 2.5 Glossary comes from the JSON `Glossary` plus every status and role named in the approved rules, using the names the rules use.
- 3.2 comes from diagram-writer (Phase 3).
- People fill the links: the 1.2 References rows and the Design column of 3.5 Screens (unless the input gave a link or Step 5.5 created the frame). Leave them empty; never generate a link or a ticket key.
- If drafting reveals an outcome no acceptance criterion defines, do not write it into another section. Tell the orchestrator, which raises it with the user at Step 5.

**Product-first rules:**

- Write for four readers: PO, BA, Dev, and QC. Every sentence must be understandable without technical background.
- Never write technical detail: endpoints, HTTP methods or status codes, payloads, JSON, error codes, database tables or fields, internal services or modules, frameworks, code, configuration keys, tracking event names, or infrastructure. The system is one black box.
- Translate technical wording from the brief into business meaning instead of copying it. User-stated delivery constraints are not written into the PRD.
- Where a requirement needs a technical decision, state the business need and mark the open point `TBD, Dev / Tech Lead decides`. Do not answer it.
- Use the terms defined in 2.5 Glossary consistently.

**Human-first rules:**

- Codes only where they help: job IDs (`JTBD-01`) in job headings and in each epic's Serves line, epic numbers, story IDs in story headings, and AC numbers within a story. No rule, message, screen, metric, quality target, dependency, assumption, question, or common-behavior IDs anywhere, and no source codes copied from the input.
- 2.1, 2.2, and 2.3 are short plain prose a new reader understands before meeting any rule.
- A rule sits under the one story that uses it, at the top of its epic when several stories of that epic use it, or in 3.1 only when it applies across epics. A status lifecycle sits with the epic that uses it, or in 3.1 when several epics depend on it. Who may take an action sits with the story where the action is taken.
- An acceptance criterion reads on its own. It applies a rule of its story or epic in plain words; it states the effect of a rule from 3.1 or another epic in a few words, with a sample labelled e.g. when useful. It shows a message by describing it and, where the message is shown first, quoting its exact copy.
- A rule several PRDs of the domain share is not copied: state its effect in words and name `domain-knowledge/[Domain_Name]/rules.md`.
- Open or assumed values are written in the rule itself: `TBD` with who decides, or `[value] (assumed)`.
- Section 3.2 includes only the diagram types explicitly approved by the user.
- Preserve the selected `Delivery_Mode`; drafting does not decide whether to save files or export DOCX.

---

## Phase 3 - Section 3.2 Diagrams

**Critical rule:** Only generate diagrams for the types explicitly approved by the user in Step 0 or Step 1. Do not substitute plain text or Mermaid when BPMN, Activity Diagram, or Sequence Diagram is requested.

When Section 3.2 needs one or more diagrams, **delegate entirely to `knowledge-base/prd-template/diagram-writer/SKILL.md`** using its Input Contract. Do not generate diagram code inline here.

Pass to `diagram-writer`:
- The diagram type(s) from `Diagram_Requirements` in the approved JSON
- The feature name and description
- The actors involved, from `Target_Users`
- The partners, teams, or existing features involved, from `Dependencies_and_Impacted_Areas`
- The happy path steps from `User_Flow`, each named in words
- The branches defined by the acceptance criteria, general rules, and status lifecycles, each named in words

After `diagram-writer` returns the output, embed it verbatim in Section 3.2 of the PRD.

---

## Phase 4 - Versioning

Do not pre-fill Version History by default; the PM owns it. Keep the table format empty unless the workflow explicitly requests a starting row. If a starting row is explicitly requested, use `0.1`, today's date, `PRD pipeline`, and `Initial draft`.

---

## Quality Checklist

- Every section in `Active_Sections` is present and filled; every other section is dropped and the rest renumbered.
- No codes appear anywhere except job IDs, epic numbers, story IDs, and AC numbers.
- Every epic has a Serves line naming the jobs it serves, and every job is served by at least one epic.
- No technical detail appears anywhere (run the self-check in `knowledge-base/product-language/SKILL.md`).
- 2.1 to 2.3 read as plain prose with no rule values.
- Every rule sits where its readers need it: under its one story, at the top of its epic, or in 3.1 only when it applies across epics.
- Every story has its heading with its ID, its statement, its Rules block when it has rules, and numbered, labelled acceptance criteria.
- Every acceptance criterion is labelled (Happy), (Alternative), or (Error), states one outcome, opens with If or While when it depends on a situation or state, and reads on its own.
- Every message the PRD shows has its exact copy (or "(proposed copy)") in quotes where it is shown first.
- A value written both in a rule and in an acceptance criterion's summary is the same in both places.
- Section 3.2 contains only the diagrams explicitly requested by the user.
- Terms match the Glossary throughout.
- The language matches the user's language.
