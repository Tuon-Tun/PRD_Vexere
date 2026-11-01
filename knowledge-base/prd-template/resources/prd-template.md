# [Product Name] - [Feature Name] PRD

<!--
  Product-first PRD, read top to bottom like any document. It hands over the rules, the logic, and
  the core value of the feature in business language that PO, BA, Dev, and QC all read the same way.
  It describes WHAT and WHY, never HOW: architecture, APIs, data model, and configuration belong to
  the Dev team's technical design document, linked in 1.2 References.
  No codes in the text: rules, messages, screens, and metrics are named in words. The only
  identifiers are story IDs in story headings and acceptance criterion numbers within a story.
  Labels inside the PRD (Rules, Acceptance Criteria, table headers) are written in the PRD's language.
  Optional sections (Success Metrics, Process Diagrams, Non-Functional Requirements, Screens) appear
  only when the user chose them; drop an excluded section and renumber the ones after it.
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

---

## 2. Feature Overview

<!-- The first thing a new reader meets. Plain prose a reader understands before any rule:
     no codes, no rule values, no jargon the Glossary has not defined yet. -->

### 2.1 Problem Statement / Context

**Context**

- Current behavior: [How it works today, from the user's point of view]
- Existing gap:
- Business motivation:

<!-- Only constraints on how or when the feature is delivered that the user explicitly stated, as stated.
     Remove this block when there are none. -->

**Known constraints**

-

**Problem Statement**

- **User problem:**
- **Business problem:**

---

### 2.2 Job to Be Done (JTBD)

<!--
  One block per distinct actor type, role, or usage context. Each block is the actor in bold and
  exactly one job story sentence. No IDs, no status, no dimension tables.
-->

**[User type / scenario]**

When [situation], I want to [motivation], so I can [expected outcome].

---

### 2.3 Goals

<!-- The outcomes the feature is for, in a few plain sentences. No codes, no targets
     (targets live in 2.4 when it is included). -->

1.

---

### 2.4 Success Metrics

<!-- Optional: only when the user asked for it in Step 0. "How it is measured" is the business
     definition: what is counted, for whom, over which period, not a tracking implementation.
     Type: Primary (the outcome the feature is for), Secondary, or Guardrail (what must not get worse
     while the primary metric improves; its target is a limit, e.g. "≤ 1%" or "no worse than baseline").
     Owner: the role who reports the number and judges the result. -->

| Type | Metric | How it is measured | Baseline | Target | Owner |
|------|--------|--------------------|----------|--------|-------|
| Primary | | | | | |

---

### 2.5 Glossary

<!--
  One term per concept, used identically in every section. Business terms, status names, and role
  names a new reader could misread, each with a one-line meaning in plain words. A term a rule defines
  (e.g. cancellation cutoff) gets its meaning without the value.
-->

| Term | Meaning in this PRD | Not to be confused with |
|------|---------------------|-------------------------|

---

## 3. Feature Specifications

### 3.1 General Rules

<!--
  Only what is the foundation of the whole feature and applies across epics: for example the payment
  currency, how amounts are written, a status lifecycle several epics depend on, and situations that
  behave the same in every story (session expired, connection lost, repeated tap, system unavailable).
  Everything else sits with its epic or story in 3.3. If nothing qualifies, write
  "None: every rule sits with the epic or story that uses it."
  Group rules under short plain headings. Each rule: concrete values, the condition that triggers it,
  and a worked example with real numbers for every calculation ("—" when an example adds nothing).
  An open value is "TBD" with who decides; an assumed one is "[value] (assumed)".
  A rule several PRDs of the domain share lives in domain-knowledge/[Domain_Name]/rules.md: here,
  say its effect in words and name that file.
  Launch policy: when the feature changes how existing bookings, tickets, vouchers, or accounts behave,
  a rule says how records that exist before launch, and actions in progress at launch, are treated.
-->

**[Group name]**

| Rule | Example |
|------|---------|
| | |

**[Lifecycle name], e.g. Booking status**

<!-- Only for a status lifecycle several epics depend on; otherwise it sits at the top of its epic.
     One row per event that changes the status, with only what that event causes.
     "When it enters" holds what happens however the status is reached, written once per status. -->

| From | When | Condition | To | Also happens |
|------|------|-----------|----|--------------|

| Status | When it enters |
|--------|----------------|

**Same in every story**

<!-- Situations that behave the same way everywhere. Exact message copy in quotes. -->

| Situation | What the user sees / what happens |
|-----------|-----------------------------------|

---

### 3.2 Process Diagrams

<!-- Optional: only the types the user chose in Step 0. Use the diagram-writer skill. Business-level
     diagrams only: actors, the system as one participant, and partners named in the input. Labels are
     short business questions and outcomes in words, never codes or values.
     Available types: BPMN (bpmn.io XML), Activity Diagram (PlantUML), Sequence Diagram (PlantUML). -->

---

### 3.3 Feature Epics & User Stories

<!--
  Follow the `user-story-skill` rules STRICTLY. Read top to bottom: epic, its rules, then each story.

  Epic: a heading, one plain sentence on what it gives the user, and "Rules for this epic" only when
  several of its stories use a rule (a status lifecycle only this epic uses sits here too).

  Story:
  - Heading: "##### US-01 - [Story name]". The Jira ticket summary starts with the same ID and name.
  - Statement: As a [persona], I want to [action], so that [value]. (In the PRD's language.)
  - Rules: the rules only this story uses, including who may take this story's action. Omit the block
    when the story has none.
  - Acceptance Criteria, numbered AC1, AC2, ... and labelled (Happy), (Alternative), or (Error):
    "- AC1 (Happy): ...". UI/UX behavior, how a broken rule or a failure is shown (toast / inline error /
    popup, with the message's copy in quotes where it is shown first), and side-effects of this story's
    own action. One outcome per criterion: split it when its outcomes can pass or fail separately (a
    disabled control and the inline message explaining it count as one). When it depends on a situation
    or state beyond "the user is on this screen", open with "If" (something happens) or "While" (a state
    holds). It reads on its own: a rule from the story's own block or its epic is applied in plain words;
    a rule from General Rules or another epic is stated by its effect in a few words, with a sample
    labelled e.g. when useful. No codes; another AC of the same story may be named ("as in AC3").
-->

#### Epic 1: [Epic Name]

[One sentence: what this epic gives the user.]

**Rules for this epic**

| Rule | Example |
|------|---------|
| [rule several stories of this epic use] | [worked example] |

##### US-01 - [Story Name]

As a [user role], I want to [action], so that [benefit].

**Rules**

| Rule | Example |
|------|---------|
| [rule only this story uses] | [worked example] |

**Acceptance Criteria**

- AC1 (Happy): [situation and outcome in plain words]
- AC2 (Alternative): While [state in words], [what the user can do or sees].
- AC3 (Error): If [business situation], [what happens, in plain words], and a [toast / inline error / popup] says "[copy]".

---

### 3.4 Non-Functional Requirements

<!--
  Optional. Only cross-cutting quality targets, as users or the business experience them: response time
  as the user perceives it, availability (e.g. 24/7, peak seasons), supported platforms and channels,
  information freshness, expected volume. A target that is the outcome of one story lives in its
  acceptance criterion instead. No infrastructure. An unknown target is "TBD" with who decides.
-->

| Expectation | Target |
|-------------|--------|

---

### 3.5 Screens

<!-- Optional: only when the user asked for it in Step 0. One row per screen: its name and what the
     user does there, in one sentence. Design: the frame link, filled by the designer or PM (Step 5.5
     writes it for frames it creates); never generated. What each screen shows lives in the acceptance
     criteria; colours, sizes, and assets live in the design tool. -->

| Screen | Purpose | Design |
|--------|---------|--------|

---

*Document generated using the PRD template renderer.*
