# [Product Name] - [Feature Name] PRD

<!--
  Product-first PRD. It hands over the rules, the logic, and the core value of the feature
  in business language that PO, BA, Dev, and QC all read the same way.
  It describes WHAT and WHY, never HOW: architecture, APIs, data model, and configuration
  belong to the Dev team's technical design document, linked in 1.2 References.
  Every fact is written once, in its home section, and cited by ID everywhere else.
  Wording and placement rules: knowledge-base/product-language/SKILL.md.
-->

---

## 1. Document Info

### 1.1 Version History

<!-- PM fills this section. Do not generate. -->

| Version | Last Updated | Modified By | Change Summary |
|---------|--------------|-------------|----------------|

### 1.2 References

<!-- PM fills the links. Do not generate them. Keep the four rows below and add others as needed. -->

| Document | Link | PIC |
|----------|------|-----|
| Jira Epic | | |
| Figma (master file) | | |
| Technical design (Dev) | | |
| Tracking plan (Data) | | |

### 1.3 How to Read This PRD

<!-- Keep this table and the ID line as is (translated into the PRD language). Drop references to excluded sections. -->

| Reader | Start with | Use it to |
|--------|------------|-----------|
| PO | 2. Feature Overview, 2.5 Scope | Confirm the value, the goals, and what is in or out |
| BA | 3.1 Business Rules, 3.3 User Stories, 3.4 Use Cases, 3.5 Traceability Matrix | Check that every rule and flow is complete and consistent |
| Dev | 3.1 Business Rules, 3.3 Acceptance Criteria and Rules applied, 3.6 Screens and Messages, 3.7 Dependencies | Understand the logic to build, then design the technical solution separately |
| QC | 3.1 Business Rules, 3.3 Acceptance Criteria and Common Behaviors, 3.5 Traceability Matrix, 3.6 Messages | Derive test cases and trace each one to a criterion or rule ID |

Every fact appears once. Other places cite its ID: `JTBD-` job, `US-` story, `US-01-AC2` acceptance criterion, `CB-` common behavior, `BR-` business rule, `MSG-` message, `SCR-` screen, `UC-` use case, `SM-` success metric, `NFR-` quality target, `DEP-` dependency, `A-` assumption, `Q-` open question.

---

## 2. Feature Overview

### 2.1 Summary

<!--
  Always filled, even when other sections are excluded.
  A reader should understand the feature in 30 seconds. Plain language, no jargon.
  No rule values or metric targets here: name them and cite their IDs.
-->

| | |
|-|-|
| **What** | [The feature in one sentence] |
| **For whom** | [Primary users or actors] |
| **Why** | [The problem or opportunity it addresses] |
| **Core value** | [The most important outcome for users and for the business] |
| **Success looks like** | [The primary metric and its guardrail, by name and ID, e.g. "Booking completion rate (SM-01), without more payment failures (SM-03)"] |

---

### 2.2 Problem Statement / Context

**Context**

- Current behavior: [How it works today, from the user's point of view]
- Existing gap:
- Business motivation:

**Problem Statement**

- **User problem:**
- **Business problem:**

---

### 2.3 Job to Be Done (JTBD)

<!--
  One block per distinct actor type, role, or usage context — no upper limit.
  Write one JTBD block per actor when their situation, motivation, or expected outcome differs.
  Do not collapse different actors into a single statement.
  Each JTBD is exactly one job story sentence — no dimension tables or bullets.
  Keep the JTBD IDs from the approved Product Framing Pack; each epic in 3.3 names the job it serves.
-->

**JTBD-01 - [User Type / Scenario]** — Status: [validated / hypothesized, needs validation]

When [situation], I want to [motivation], so I can [expected outcome].

---

### 2.4 Goals & Success Metrics

**Goals:**

<!-- Name each outcome and cite its SM ID. A baseline or target appears only in its row of the table below. -->

1.

**Success Metrics:**

<!-- The home of every metric's baseline and target. "How it is measured" is the business definition: what is
     counted, for whom, over which period. Not a tracking implementation.
     Type: Primary (the outcome the feature is for), Secondary, or Guardrail (what must not get worse while
     the primary metric improves). A guardrail's target is a limit, e.g. "≤ 1%" or "no worse than baseline".
     Owner: the role who reports the number and judges the result. -->

| ID | Type | Metric | How it is measured | Baseline | Target | Owner |
|----|------|--------|--------------------|----------|--------|-------|
| SM-01 | Primary | | | | | |

---

### 2.5 Scope

<!--
  Out of scope matters as much as in scope: it tells Dev what not to build and QC what not to test.
  List capabilities at epic or story level and cite their IDs. Never repeat rule values here.
  List only items the user stated or confirmed. Otherwise write TBD and add an Open Question.
-->

**In scope**

-

**Out of scope**

-

---

### 2.6 Glossary

<!--
  One term per concept, used identically in every section of this PRD.
  Include business terms, status names, and role names a new reader could misread, each with a
  one-line meaning, using the names in 3.1. Transitions and permissions live in 3.1: cite their BR IDs,
  do not restate them. A term a rule defines (e.g. cancellation cutoff) gets its meaning without the
  value and cites the rule: "the latest time a ticket can be cancelled online (BR-01)".
-->

| Term | Meaning in this PRD | Not to be confused with |
|------|---------------------|-------------------------|

---

## 3. Feature Specifications

### 3.1 Business Rules

<!--
  The core of the PRD for Dev and QC, and the only place rule values live. One rule per row, each with
  its own BR ID (unique across all tables in this section), concrete values, and the condition that triggers it.
  A rule answers a question about money, seats or other inventory, a status, a voucher or other
  entitlement, or who may act. What the user sees when it applies lives in the citing acceptance criteria.
  - Example: a concrete case with real numbers, e.g. "Ticket 300,000 VND cancelled 30 hours before
    departure -> refund 270,000 VND". Every calculation needs a worked example.
  - Uses: IDs of other rules this rule depends on. In transition, status, and permission rows, the rules cited in
    the row play the same role.
  - An open or assumed value is written in the Rule cell itself: "TBD (Q-..)" or "[value] (assumed, A-..)".
  - Notes: the source of the rule; who may change the value without a new release; "No longer applies (vX)"
    for a removed rule, which keeps its ID and is no longer cited.
  - A rule defined in another approved PRD is not copied here: cite it as "[Other PRD name] BR-02".
  - Launch policy: when the feature changes how existing bookings, tickets, vouchers, or accounts behave,
    a rule says how records that exist before launch, and actions in progress at launch, are treated.
    How existing data is converted is an Open Question for Dev / Tech Lead.
-->

**Formulas, Policies & Limits**

| ID | Rule | Example | Uses | Notes |
|----|------|---------|------|-------|
| BR-01 | | | | |

**Statuses & Transitions**

<!-- Only if the feature has statuses (e.g. booking, ticket, refund). Otherwise remove these two blocks.
     Transitions: one row per event that changes a status, with only the side-effects of that event (e.g.
     "refund per BR-03"). An event names the action and cites the permission row that says who may take it,
     without repeating its roles or conditions. A condition that depends on another rule names it in words
     and cites its ID.
     On Entering a Status: side-effects that are the same however the status is reached (notifications by
     MSG ID, inventory released, partner informed), written once per status, never on each transition. -->

| ID | From status | Event | Condition | To status | Side-effects of this event |
|----|-------------|-------|-----------|-----------|----------------------------|

**On Entering a Status**

| ID | Status | Side-effects |
|----|--------|--------------|

**Roles & Permissions**

<!-- Only if more than one role acts in this feature. Otherwise remove this block. One row per action,
     including actions that change a status. The only place that says who may act. -->

| ID | Action | [Role 1] | [Role 2] | [Role 3] |
|----|--------|----------|----------|----------|

---

### 3.2 Process Diagrams

<!-- Use the diagram-writer skill. Business-level diagrams only: actors, the system as one
     participant, and partners named in the input. Labels name rules and cite their IDs, never values.
     Available types: BPMN (bpmn.io XML), Activity Diagram (PlantUML), Sequence Diagram (PlantUML). -->

---

### 3.3 Feature Epics & User Stories

<!--
  Taken from the approved Product Framing Pack. Follow the `user-story-skill` rules STRICTLY.

  Common Behaviors come first: situations that behave the same way in every story (login session
  expired, connection lost, repeated tap, system temporarily unavailable). Each is written once and
  cited by stories instead of being repeated in their acceptance criteria.

  Each epic names the job it serves (JTBD ID) and has a Jira line the PM fills after creating the epic.

  Each story:
  - Statement: As a [persona], I want to [action], so that [value/reason].
  - Priority: Must / Should / Could.
  - Screens: the SCR IDs from 3.6 the story is built on, or none.
  - Jira: filled by the PM after creating the ticket; never generated. The Jira ticket summary starts
    with the story ID and name (e.g. "US-03 Choose seats"), so the ticket and the PRD always match.
  - Common behaviors: the CB IDs that apply to the story.
  - Rules applied: every BR referred to by its acceptance criteria and its common behaviors, then every
    BR cited in any cell of those rules' rows, followed all the way down (a transition also brings in the
    "on entering" row of its new status; a cited message brings in its Rules column). Prefixed with the
    feature name so it still makes sense in a Jira ticket; rules from another PRD go in a second group
    prefixed with that PRD's name and are not followed further.
  - Acceptance criteria, numbered AC1, AC2, ... and labelled (Happy), (Alternative), or (Error): UI/UX
    behavior, how a broken rule or a failure is shown (toast / inline error / popup + MSG ID), and
    side-effects of this story's own action. One outcome per criterion: split it when its outcomes can
    pass or fail separately (a disabled control and the inline message explaining it count as one). When it depends on a situation or state beyond "the user is on this
    screen", open with "If" (something happens) or "While" (a state holds) and cite the rule.
    Side-effects of a status change live in 3.1 (on its transition or "on entering" row); the acceptance
    criterion only states that the transition happens. Cite rule and message IDs; never copy a rule value or message wording.
-->

**Common Behaviors**

| ID | Situation | What the user sees / what happens | Rules & Messages |
|----|-----------|-----------------------------------|------------------|
| CB-01 | | | |

**Epic 1: [Epic Name]** — Serves: JTBD-01 — Jira: [PM fills]

- **US-01 - [Story Name]**
  - **As a** [user role],
  - **I want to** [action],
  - **so that** [benefit].
  - **Priority:** [Must / Should / Could]
  - **Screens:** SCR-01
  - **Jira:** [PM fills]
  - **Common behaviors:** CB-01
  - **Rules applied (PRD [Feature Name]):** BR-01, BR-03
  - **Acceptance Criteria**
    - AC1 (Happy) Done when: [observable outcome, naming the rule in words] (BR-03)
    - AC2 (Alternative) Done when: While [state] (BR-03), [what the user can do or sees].
    - AC3 (Error) Done when: If [business situation] (BR-01), [toast / inline error / popup] shows MSG-01.

---

### 3.4 Use Case Specifications

<!--
  Write a use case only for a flow with several user actions and system responses in between, or
  that branches on a business condition. One use case may cover several stories; name them in its
  header. A single-step story gets no use case: its acceptance criteria are complete.
  If no flow qualifies, write "No use case needed: every story is single-step; see the acceptance
  criteria in 3.3." This is complete, not TBD.

  Use cases hold only the ORDER of steps, taken from the approved user flow. Every outcome cites where it is defined: the acceptance
  criterion or common behavior (what the user sees), the rule (BR), the message (MSG). Add a branch
  row only where the flow really branches; there is no minimum number of rows.
  Precondition and Postcondition name the condition or status and cite its BR ID, without values.
-->

**UC-01 - [Use Case Name]** (covers US-01, US-02)

| Field             | Detail |
|-------------------|--------|
| **Actor**         |        |
| **Precondition**  |        |
| **Postcondition** |        |

**Main Flow:**

| Step | Actor | Action | Result (cites AC / BR / MSG) |
|------|-------|--------|------------------------------|

**Branches:**

| Step | Trigger (business situation) | Handled by (AC / CB) | Rule |
|------|------------------------------|----------------------|------|

<!-- Repeat the UC block only for other flows that qualify. -->

---

### 3.5 Traceability & Non-Functional Requirements

#### Traceability Matrix

<!--
  IDs only, no prose. One row per BR, built from the citations in 3.3 (acceptance criteria and common
  behaviors), 3.4 (use cases), 3.6 (the Rules column of each message), and 3.1 (rules citing other rules).
  Cited by: the AC and CB IDs that cite the rule, plus "via BR-.." for each rule that uses it.
  MSG: the messages whose Rules column lists the rule. A removed rule shows "No longer applies".
  A rule cited from another PRD gets its own row, named with that PRD, so a change there can be traced here.
  Add a row with "—" in the BR column for each story that applies no rule. Use "—" when nothing maps.
-->

| BR | Cited by (AC / CB) | UC | MSG |
|----|--------------------|----|-----|

#### Non-Functional Requirements

<!--
  The home of cross-cutting quality targets, expressed as users or the business experience them:
  response time as the user perceives it, availability (e.g. 24/7, peak seasons), supported platforms
  and channels, information freshness, expected volume.
  Who may see what is a permission rule in 3.1; recording a specific action is an acceptance criterion.
  No infrastructure. If the business has no target, write TBD and add an Open Question for Dev / Tech Lead.
-->

| ID | Expectation | Target | Why it matters |
|----|-------------|--------|----------------|

---

### 3.6 UI/UX Specifications

**Screens**

<!-- An inventory only. What each screen does lives in the acceptance criteria of the stories listed.
     Stories: built from the stories' Screens lines. Design: the Figma frame link, filled by the designer or
     PM (Step 5.5 writes it for frames it creates); never generated. Colours, sizes, and assets live in Figma. -->

| ID | Screen | Purpose | Stories | Design |
|----|--------|---------|---------|--------|

**Messages**

<!--
  The only place message wording lives, for every channel. Acceptance criteria and common behaviors
  cite the MSG ID and say how it is shown (toast, inline error, popup); transitions and use cases cite
  only the MSG ID.
  A message that mentions a rule value uses a named placeholder citing the rule, never the number:
  "{cancellation cutoff (BR-01)}". Dynamic data uses a plain placeholder: "{ticket code}".
  Rules: every BR the wording depends on, in a placeholder or explained in words.
  If no copy was provided, write the intent of the message and mark it (proposed copy).
-->

| ID | Channel | Message | Rules |
|----|---------|---------|-------|

---

### 3.7 Dependencies & Impacted Areas

<!--
  Business view only. The technical design (architecture, APIs, data model, configuration) is
  owned by the Dev team in a separate document, linked in 1.2 References.
-->

**Dependencies**

<!-- Teams, partners, other PRDs, or existing features this feature relies on. "What we need from it" names
     the capability and cites rules for values and side-effects. "If it is unavailable" cites the rule,
     common behavior, or acceptance criterion that defines the outcome; it does not restate it. -->

| ID | Depends on | What we need from it | If it is unavailable | Owner |
|----|------------|----------------------|----------------------|-------|

**Impacted Areas**

<!-- Existing features, screens, reports, or team processes that change because of this feature.
     "What changes" cites story and rule IDs instead of restating them. -->

| Area | What changes | What to re-check |
|------|--------------|------------------|

**Known Constraints**

<!-- Only constraints on how or when the feature is delivered that the user explicitly stated (e.g. reuse
     the current payment partner, launch before Tet), recorded once as stated. Limits on what users or
     data may do are business rules in 3.1. Write "None provided." if there are none. -->

-

---

## 4. Assumptions & Open Questions

**Assumptions**

<!-- An assumed value is written in its rule row as "(assumed, A-..)"; the assumption cites the rule. -->

| ID | Assumption | Affects | Source / Confidence |
|----|------------|---------|---------------------|

**Open Questions**

<!-- Missing business information, plus technical decisions routed to Dev / Tech Lead as questions.
     The PRD never answers technical questions itself. A question about a rule value cites the rule,
     whose row says "TBD (Q-..)". -->

| ID | Question / Missing Information | Affects | Owner / Next Step |
|----|--------------------------------|---------|-------------------|

---

*Document generated using the PRD template renderer.*
