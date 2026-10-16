# [Product Name] - [Feature Name] PRD

<!--
  Product-first PRD. It hands over the rules, the logic, and the core value of the feature
  in business language that PO, BA, Dev, and QC all read the same way.
  It describes WHAT and WHY, never HOW: architecture, APIs, data model, and configuration
  belong to the Dev team's technical design document, linked in 1.2 References.
  Wording rules: knowledge-base/product-language/SKILL.md.
-->

---

## 1. Document Info

### 1.1 Version History

<!-- PM fills this section. Do not generate. -->

| Version | Last Updated | Modified By | Change Summary |
|---------|--------------|-------------|----------------|

### 1.2 References

<!-- PM fills this section. Do not generate. Link the Dev team's technical design document here once it exists. -->

| Document | Link | PIC |
|----------|------|-----|

### 1.3 How to Read This PRD

<!-- Keep this table as is (translated into the PRD language). Drop references to excluded sections. -->

| Reader | Start with | Use it to |
|--------|------------|-----------|
| PO | 2. Feature Overview, 2.5 Scope | Confirm the value, the goals, and what is in or out |
| BA | 3.1 User Stories, 3.2 Business Rules, 3.4 Use Cases | Check that every rule and flow is complete and consistent |
| Dev | 3.2 Business Rules, 3.4 Use Cases, 3.7 Dependencies | Understand the logic to build, then design the technical solution separately |
| QC | Acceptance Criteria in 3.1, 3.2 Business Rules, exception flows in 3.4, messages in 3.6 | Derive test cases and trace each one to a rule or criterion ID |

---

## 2. Feature Overview

### 2.1 Summary

<!--
  Always filled, even when other sections are excluded.
  A reader should understand the feature in 30 seconds. Plain language, no jargon.
-->

| | |
|-|-|
| **What** | [The feature in one sentence] |
| **For whom** | [Primary users or actors] |
| **Why** | [The problem or opportunity it addresses] |
| **Core value** | [The most important outcome for users and for the business] |
| **Success looks like** | [The headline metric and its target] |

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
-->

**JTBD - [User Type / Scenario]**

When [situation], I want to [motivation], so I can [expected outcome].

---

### 2.4 Goals & Success Metrics

**Goals:**

1.

**Success Metrics:**

<!-- "How it is measured" is the business definition: what is counted, for whom, over which period. Not a tracking implementation. -->

| Metric | How it is measured | Baseline | Target |
|--------|--------------------|----------|--------|

---

### 2.5 Scope

<!--
  Out of scope matters as much as in scope: it tells Dev what not to build and QC what not to test.
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
  Include business terms, statuses, and roles a new reader could misread.
-->

| Term | Meaning in this PRD | Not to be confused with |
|------|---------------------|-------------------------|

---

## 3. Feature Specifications

### 3.1 Feature Epics & User Stories

<!--
  Structure all features using an Epic > User Story > Acceptance Criteria hierarchy.
  Follow the `user-story-skill` rules STRICTLY:
  - Epic groups related User Stories.
  - User Story format: As a [persona], I want to [action], so that [value/reason].
  - Acceptance Criteria: `Done when: [observable positive/negative condition]`.
  - Reference the business rule an AC verifies, e.g. (BR-02), so QC can trace it.

  Format example:
  **Epic 1: [Epic Name]**
  - **US-01 - [Story Name]**
    - **As a** [user role],
    - **I want to** [action],
    - **so that** [benefit].
    - **Acceptance Criteria**
      - Done when: [condition 1]
      - Done when: If [situation], then [what the user sees / what happens] (BR-01)
-->

### 3.2 Business Rules

<!--
  The core of the PRD for Dev and QC. One rule per row, one testable statement per rule, with
  concrete values: eligibility, limits, pricing, permissions, validation, sequencing, deadlines,
  timeouts, retries, and exception handling.
  - Example: a concrete case with real numbers, e.g. "Ticket 300,000 VND cancelled 30 hours before
    departure -> refund 270,000 VND". Every calculation needs a worked example.
  - Notes: the source of the rule, and who may change the value without a new release (if the
    business needs that). Never how it is configured.
-->

**Rules**

| ID | Rule | Example | Notes |
|----|------|---------|-------|
| BR-01 | | | |

**Statuses & Transitions**

<!-- Only if the feature has statuses (e.g. booking, ticket, refund). Otherwise remove this block. -->

| From status | Event | To status | Triggered by | What the user sees |
|-------------|-------|-----------|--------------|--------------------|

**Roles & Permissions**

<!-- Only if more than one role acts in this feature. Otherwise remove this block. -->

| Action | [Role 1] | [Role 2] | [Role 3] |
|--------|----------|----------|----------|

### 3.3 Process Diagrams

<!-- Use the diagram-writer skill. Business-level diagrams only: actors, the system as one
     participant, and partners named in the input.
     Available types: BPMN (bpmn.io XML), Activity Diagram (PlantUML), Sequence Diagram (PlantUML). -->

---

### 3.4 Use Case Specifications

<!--
  One UC block per User Story (UC-01 mirrors US-01, UC-02 mirrors US-02, and so on).
  Describe what the actor does and what the system does in response, as the user or the
  business observes it.

  For EACH UC, exhaustively enumerate before writing:

  ALTERNATIVE FLOWS - every valid deviation from the happy path:
    - User cancels or goes back at any step
    - User chooses a different option or path
    - User skips an optional step
    - User changes input before confirming
    -> Each distinct trigger = one row (A1, A2, A3, and so on). Do not stop at A1.

  EXCEPTION FLOWS - every situation where something goes wrong, written as what happens
  and what the user sees (never HTTP codes, error codes, or technical causes):
    - User is not logged in, or the login session expired mid-way
    - User loses connection mid-way
    - Input is missing or breaks a rule (name the rule ID)
    - Nothing is found / empty state
    - The item is no longer available (taken by someone else, sold out, expired)
    - A partner does not respond in time or rejects the request
    - The system cannot process the request right now: what the user sees, and whether money and data are safe
    - User repeats the action (double tap, resubmit): no duplicate result
    - A limit is reached
    -> Each distinct situation = one row (E1, E2, E3, and so on). Do not stop at E1.

  CRITICAL MANDATE: YOU MUST WRITE OUT ALL NECESSARY USE CASES FOR EVERY USER STORY.
  A SINGLE USER STORY MAY REQUIRE MULTIPLE USE CASES TO COVER ALL FUNCTIONALITIES.
-->

**UC-01 - [Use Case Name]**

| Field             | Detail |
|-------------------|--------|
| **Use Case ID**   |        |
| **Use Case Name** |        |
| **Actor**         |        |
| **Precondition**  |        |
| **Postcondition** |        |

**Main Flow (Happy Path):**

| Step | Actor | Action | System Response (what the user sees / what happens) |
|------|-------|--------|------------------------------------------------------|

**Alternative Flows:**

| Step | Trigger | Actor Action | System Response |
|------|---------|--------------|-----------------|

**Exception Flows:**

| Step | Situation | System Handling (what happens + what the user sees) | Related Rule |
|------|-----------|-----------------------------------------------------|--------------|

<!-- Repeat the full UC block above for UC-02, UC-03, and so on until coverage is complete. -->

---

### 3.5 Feature Requirements

#### Functional Requirements

<!--
  Derive from all User Stories, Acceptance Criteria, and Business Rules. No fixed upper limit.
  Write each requirement as a capability in business terms: "The system allows [actor] to ..."
  or "The system [does X] when [condition]".
-->

| ID | Requirement | Related Story / Rule | Priority |
|----|-------------|----------------------|----------|

#### Non-Functional Requirements

<!--
  Business-level expectations only, expressed as users or the business experience them:
  response time as the user perceives it, availability (e.g. 24/7, peak seasons), supported
  platforms and channels, privacy (who may see which information), traceability (which actions
  must be recorded and who reviews them), expected volume.
  No infrastructure. If the business has no target, write TBD and add an Open Question for Dev / Tech Lead.
-->

| ID | Expectation | Target | Why it matters |
|----|-------------|--------|----------------|

---

### 3.6 UI/UX Specifications

**Screens & Elements**

| Screen / Element | What the user sees and can do | Rules |
|------------------|-------------------------------|-------|

**User-facing Messages**

<!-- Every message the user can see: confirmations, warnings, errors, empty states.
     If no copy was provided, write the intent of the message and mark it (proposed copy). -->

| ID | When it appears | Message |
|----|-----------------|---------|

---

### 3.7 Dependencies & Impacted Areas

<!--
  Business view only. The technical design (architecture, APIs, data model, configuration) is
  owned by the Dev team in a separate document, linked in 1.2 References.
-->

**Dependencies**

<!-- Teams, partners, or existing features this feature relies on. -->

| Depends on | What we need from it | If it is unavailable | Owner |
|------------|----------------------|----------------------|-------|

**Impacted Areas**

<!-- Existing features, screens, reports, or team processes that change because of this feature. -->

| Area | What changes | What to re-check |
|------|--------------|------------------|

**Known Constraints**

<!-- Only constraints the user explicitly stated, recorded once as stated. Do not expand or add
     technical detail. Write "None provided." if there are none. -->

-

---

## 4. Assumptions & Open Questions

**Assumptions**

| ID | Assumption | Source / Confidence |
|----|------------|---------------------|

**Open Questions**

<!-- Missing business information, plus technical decisions routed to Dev / Tech Lead as questions.
     The PRD never answers technical questions itself. -->

| ID | Question / Missing Information | Owner / Next Step |
|----|--------------------------------|-------------------|

---

*Document generated using the PRD template renderer.*
