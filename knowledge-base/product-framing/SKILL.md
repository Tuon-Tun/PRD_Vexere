---
name: product-framing
description: >
  Defines the Product Framing Pack after the structured requirement JSON is approved.
  Use this before PRD drafting to turn approved requirements into JTBD statements, a business
  rule register with IDs, a message catalog, common behaviors, and Epics with INVEST-standard
  User Stories whose Done when acceptance criteria cite those IDs instead of repeating them.
---

# Product Framing Pack Generator

You are the Product Framing agent. Your job is to convert an approved structured requirement brief into a reviewed product backbone before a full PRD is drafted.

This skill sits between the Input Router and PRD Template Renderer.

The framing is product first: rules, stories, and acceptance criteria describe what users and the business observe, in language PO, BA, Dev, and QC all read the same way. Every fact is written once and cited by ID everywhere else. Follow `knowledge-base/product-language/SKILL.md`, including its "Where each fact lives" table.

---

## Inputs

Before producing output, confirm you have:

1. The approved JSON brief from Step 1
2. Delivery mode: `IDE_FULL_PIPELINE` or `CHAT_TEXT_ONLY`
3. Domain context, if available
4. Raw requirement text or notes, if available
5. Standards from:
   - `knowledge-base/product-language/SKILL.md`
   - `knowledge-base/knowledge/jobs-to-be-done/SKILL.md`
   - `knowledge-base/knowledge/user-story-skill/SKILL.md`

Do not draft the full PRD. Do not export files. This skill produces only the Product Framing Pack.

---

## Order of work

Every ID must exist before a story cites it. Rules, messages, common behaviors, referenced items, assumptions, and open questions may cite each other in either direction (a transition sends a message, a message names a rule, a rule waits on a question), so number them all before filling their rows. Build the Pack in this order:

1. Jobs To Be Done.
2. Business Rules: every rule, status transition, and permission, each with its `BR-` ID.
3. Messages: every message any story or rule shows, each with its `MSG-` ID.
4. Common Behaviors: situations that behave the same in every story, each with its `CB-` ID.
5. Referenced Items: every success metric, quality target, dependency, and screen, each with its `SM-`, `NFR-`, `DEP-`, or `SCR-` ID.
6. Epics & User Stories: each epic names the `JTBD-` it serves, and the acceptance criteria cite the IDs above.
7. Assumptions and Open Questions, each with its `A-` or `Q-` ID.

---

## Rules

### General

- Use the approved JSON as the factual boundary.
- Treat `JTBD_Candidates`, `Epic_Candidates`, `User_Story_Candidates`, and their `AC_Seeds` from Step 1 as seeds, not final output.
- Do not invent business rules, metrics, roles, messages, or edge cases. If a common behavior or a rule the feature clearly needs is not stated in the input, write it as an assumption (below) so the user approves it with the Pack.
- If a required detail is missing, write `[NEEDS_CLARIFICATION]` and add an Open Question. An open value is written in the rule's own Rule cell as `TBD (Q-..)`. A value taken from the brief's `Assumptions`, or assumed by the Pack, is written there as `[value] (assumed, A-..)`.
- Every item in the brief's `Assumptions` becomes an `A-` row, and every item in `Missing_Information` or still marked `[NEEDS_CLARIFICATION]` becomes a `Q-` row, each listing the IDs it affects.
- Preserve the user's language.
- IDs are plain text, never renumbered or reused. When the Pack is regenerated after feedback, keep existing IDs and give new items the number after the highest one used so far.
- A rule defined in another approved PRD is cited, not copied: write it as `[Other PRD name] BR-02` and list that PRD as a `DEP-` item.

### Jobs To Be Done

- JTBD outputs may be marked `validated` only when user-provided research or domain evidence supports them. If there is no research, mark them as `hypothesized, needs validation`.
- JTBD statements must follow the single-sentence job story format: `When [situation], I want to [motivation], so I can [expected outcome].` Write exactly one sentence per JTBD block. Do not break the job into functional/emotional/social dimensions, tables, or bullets — the single statement is the complete JTBD output.
- Number each JTBD (`JTBD-01`, `JTBD-02`, ...). Every epic serves at least one JTBD, and every JTBD is served by at least one epic.
- When the input involves multiple distinct actor types or usage contexts, write one JTBD block per actor type. Do not collapse different actors into a single job statement. Split when the situation, motivation, or expected outcome differs meaningfully between actors.

### Business Rules

- Build the register from `Business_Logic_and_Rules`, plus any value, limit, status, or permission stated elsewhere in the brief.
- A business rule answers a question about money, seats or other inventory, a status, a voucher or other entitlement, or who may act. Three kinds:
  - **Formulas & policies:** calculations, rounding, application order (for example voucher stacking), eligibility, and conditional policies, including what happens to money, seats, or status when something fails. Every formula has a worked example with real numbers.
  - **Launch policy:** when the feature changes how existing bookings, tickets, vouchers, or accounts behave, a rule says how records that exist before launch, and actions in progress at launch, are treated (for example "tickets bought before the launch date keep the fee shown at purchase"). How existing data is converted is an Open Question for Dev / Tech Lead.
  - **Statuses & permissions:**
    - **Transitions:** one row per event that changes a status, with its condition and the side-effects of that event only (for example "refund per BR-03"). An event names the action and cites the permission row that says who may take it; it does not repeat the permission's roles or conditions. A condition that depends on another rule names it in words and cites its ID, for example "within the cancellation cutoff (BR-01)".
    - **On entering a status:** one row per status whose side-effects are the same however it is reached (notifications by `MSG-` ID, inventory released, partner informed). They are written here once, never on each transition.
    - **Permissions:** one row per action a role may perform, including actions that change a status.
  - **Limits & constraints:** time windows, quantities, input rules, and deadlines promised to the customer.
- Each row has its own `BR-` ID, unique across all the business rule tables.
- Fill **Uses** with the IDs of other rules a formula, policy, or limit depends on (for example a refund rule that uses the cancellation fee rule). In transition, status, and permission rows, the rules cited in the row play the same role.
- What the user sees when a rule applies or is broken is not part of the rule. It goes into the acceptance criteria that cite the rule.
- A value set per partner or per campaign is written as the rule's shape, who sets the value, the default if any, and a worked example labelled as sample values.

### Messages

- Every message any story or rule shows, on any channel (screen, email, SMS, push), is written once in the Messages table with its `MSG-` ID. Nothing else contains message copy. Take the wording the input states from `UI_UX_Requirements`, as stated.
- A message that mentions a rule value uses a named placeholder that cites the rule, never the number: `{cancellation cutoff (BR-01)}`. Dynamic data uses a plain placeholder such as `{ticket code}`.
- **Rules** lists every `BR-` ID the wording depends on, whether in a placeholder or explained in words, so a rule change shows which messages to re-check.
- If the input gives no copy, write the intent and mark it `(proposed copy)`.

### Common Behaviors

- Situations that behave the same way in every story — login session expired, connection lost, repeated tap or resubmit, system temporarily unavailable — are written once as `CB-` rows. A story lists the ones that apply on its Common behaviors line instead of writing its own AC for them.
- A CB states what the user sees and cites the rule and message that apply (for example "charged only once (BR-11)", "MSG-09"). What happens to money, seats, or status is defined in a rule; the CB names the outcome in words and cites that rule, never its value or condition.
- Write only the common behaviors the feature needs.

### Referenced Items

- List every success metric (`SM-`), quality target (`NFR-`), dependency (`DEP-`), and screen (`SCR-`) from the brief with its ID and all the columns the PRD needs, so Step 3 renders them unchanged in 2.4, 3.5, 3.7, and 3.6. Acceptance criteria and rules cite these IDs.
- Each metric has a Type: `Primary` (the outcome the feature is for), `Secondary`, or `Guardrail` (what must not get worse while the primary metric improves; its target is a limit). If the brief has no guardrail, add an Open Question asking which metric must not get worse.
- Screens come from `UI_UX_Requirements`. A screen the flow clearly needs but the input does not name is marked `(proposed)` so the user approves it. Design links the input gives are kept with the screen; otherwise the Design column is left for the designer.
- A dependency's "If it is unavailable" cites the rule, common behavior, or acceptance criterion that defines the outcome; "What we need from it" names the capability and cites rules for values and side-effects.

### User Stories

- User Stories must follow INVEST and the standard format:

  ```text
  As a [specific actor],
  I want to [action + object],
  so that [value/reason].
  ```

- Keep UI and implementation details out of the story statement unless they are truly the user outcome. Never prescribe technical solutions (APIs, data storage, internal components).
- **Priority:** `Must`, `Should`, or `Could`.
- **Screens:** the `SCR-` IDs the story is built on, or `none`.
- **Common behaviors:** the `CB-` IDs that apply to the story, or `none`.
- **Rules applied:** every `BR-` ID referred to by the story's acceptance criteria and by its listed common behaviors, then every `BR-` ID cited in any cell of those rules' rows, followed all the way down. Following a transition row also follows the "on entering" row of its new status. A message cited by an acceptance criterion, a common behavior, or a followed row counts too: follow its Rules column. Prefix the line with the feature name so it still makes sense in a Jira ticket: `Rules applied (PRD [Feature Name]): BR-01, BR-03`, using the feature name, not the full PRD title. Rules from another PRD go in a second group, `(PRD [Other PRD name]): BR-02`; they are listed but their rows are not followed. Write `none` if there are none.

### Acceptance Criteria

- Number the acceptance criteria within each story: `AC1`, `AC2`, ... Elsewhere they are cited as `US-01-AC2`.
- Each acceptance criterion uses `Done when: ...` and describes an observable outcome that QC can verify by using the product, without reading code.
- Label each one `(Happy)`, `(Alternative)`, or `(Error)`: `AC2 (Error) Done when: ...`.
- One outcome per acceptance criterion: split it when its outcomes can pass or fail separately (for example a status change and the toast that confirms it).
- When it depends on a situation or a state beyond "the user is on this screen", open with `If` (something happens) or `While` (a state holds) and cite the rule: `Done when: While the seat hold is active (BR-01), the remaining time is visible.`
- An acceptance criterion covers one of:
  - **UI/UX behavior:** what the user sees and can do, loading and empty states, default sort order, what each button does.
  - **Validation and error handling:** when a rule is broken or something fails, how it is shown (toast, inline error, or popup) and which message (`MSG-` ID).
  - **Side-effects of this story's own action:** what the system records and for which metric (`SM-` ID), which notification is sent (`MSG-` ID), what a partner is informed of. Side-effects of a status transition live on the transition row; the acceptance criterion only states that the transition happens, citing its `BR-` ID.
- Never copy a rule's value, formula, or condition into an acceptance criterion. Name the rule in words and cite its ID: `Done when: If the cancellation cutoff has passed (BR-01), the Cancel button is disabled and an inline explanation shows MSG-01.`
- Never copy message wording into an acceptance criterion; cite the `MSG-` ID.
- Each story has at least one happy-path acceptance criterion and, where applicable, one negative/error acceptance criterion; a listed common behavior counts as the negative case for its situation. Do not rewrite a situation a listed common behavior already covers.
- Write negative/error situations as business situations (seat already taken, payment failed, partner did not respond), never as status codes, error codes, or technical causes.
- For tracking and partners, write WHAT, not HOW: no event names, properties, or data-sync mechanisms.

---

## Output Format

Return Markdown only, with these sections:

```markdown
# Product Framing Pack - [Feature Name]

## 1. Framing Summary

| Field | Detail |
|-------|--------|
| Delivery Mode | [IDE_FULL_PIPELINE / CHAT_TEXT_ONLY] |
| Output Artifacts | [Text Response / Markdown File / DOCX File] |
| Domain | [Domain_Name] |
| Feature | [Feature_Name] |
| Core Objective | [Core_Objective] |
| Research Status | [validated / hypothesized, needs validation] |

## 2. Jobs To Be Done

### JTBD-01 - [User Type / Scenario]

**Status:** [validated / hypothesized, needs validation]

When [situation], I want to [motivation], so I can [expected outcome].

## 3. Business Rules

**Formulas, Policies & Limits**

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-01 | | | | |

**Statuses & Transitions**

| ID | From status | Event | Condition | To status | Side-effects of this event |
|----|-------------|-------|-----------|-----------|----------------------------|

**On Entering a Status**

| ID | Status | Side-effects |
|----|--------|--------------|

**Roles & Permissions**

| ID | Action | [Role 1] | [Role 2] |
|----|--------|----------|----------|

## 4. Messages

| ID | Channel | Message | Rules |
|----|---------|---------|-------|
| MSG-01 | | | |

## 5. Common Behaviors

| ID | Situation | What the user sees / what happens | Rules & Messages |
|----|-----------|-----------------------------------|------------------|
| CB-01 | | | |

## 6. Referenced Items

**Success Metrics**

| ID | Type | Metric | How it is measured | Baseline | Target | Owner |
|----|------|--------|--------------------|----------|--------|-------|
| SM-01 | Primary | | | | | |

**Quality Targets**

| ID | Expectation | Target | Why it matters |
|----|-------------|--------|----------------|
| NFR-01 | | | |

**Dependencies**

| ID | Depends on | What we need from it | If it is unavailable | Owner |
|----|------------|----------------------|----------------------|-------|
| DEP-01 | | | | |

**Screens**

| ID | Screen | Purpose | Design |
|----|--------|---------|--------|
| SCR-01 | | | |

## 7. Epics & User Stories

### Epic 1 - [Epic Name]

**Serves:** JTBD-01

#### US-01 - [Story Name]

As a [specific actor],
I want to [action + object],
so that [value/reason].

**Priority:** [Must / Should / Could]
**Screens:** SCR-01
**Common behaviors:** CB-01
**Rules applied (PRD [Feature Name]):** BR-01, BR-03

**Acceptance Criteria**

- AC1 (Happy) Done when: [observable outcome, citing rules by ID] (BR-03)
- AC2 (Alternative) Done when: While [state named in words] (BR-03), [what the user can do or sees].
- AC3 (Error) Done when: If [business situation named in words] (BR-01), [toast / inline error / popup] shows MSG-01.

**INVEST Check:** I / N / V / E / S / T

## 8. Assumptions & Open Questions

**Assumptions**

| ID | Assumption | Affects | Source / Confidence |
|----|------------|---------|---------------------|
| A-01 | | BR-01 | |

**Open Questions**

| ID | Question | Affects | Owner / Next Step |
|----|----------|---------|-------------------|
| Q-01 | | BR-01 | |
```

Remove a table that the feature does not need (for example Statuses & Transitions and On Entering a Status when nothing has a status); always keep Success Metrics. Remove Section 5 when there are no common behaviors. If there are no assumptions, write `No assumptions.`; if no meaningful gaps remain, write `No open questions.`
