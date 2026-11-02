---
name: user-story-skill
description: >-
  Systematically create INVEST-standard User Stories with comprehensive Acceptance Criteria. Use when the user mentions "user story", "acceptance criteria", "AC", "INVEST", "story splitting", "story hierarchy", or asks for help writing or reviewing user stories. Also trigger when the user wants to decompose a feature into stories, ensure testable conditions, or align stories with business value. Do NOT use for general requirements gathering, feature specifications without a user-centric focus, or technical task breakdowns that don't follow the user story format.
---

# SKILL: User Stories & Acceptance Criteria

**Trigger:** Write / draft / review / decompose / check User Stories or AC.
**Rule:** Read fully before producing any output.

---
 
## 1 · STORY FORMAT (Non-Negotiable)

```text
As a [specific Actor/Persona],
I want to [Action + Object],
so that [Value/Reason].
```

| Part | Guidance |
|------|----------|
| **WHO** (Actor) | Specific named persona — never "user", "system", or "developer". Represents how the person works, thinks, feels. One actor per story. |
| **DOES + WHAT** (Action) | Outcome-focused, implementation-free. No UI elements, no technical prescriptions. Use "I want to [do X]" — avoid "I need a [feature]". |
| **WHY** (so that) | Genuine user/business value — never a system requirement. Always present. Ask "Why?" 5× to reach true motivation. |
| **AC** | Testable conditions confirming the story is complete. See Section 3. |

---

## 2 · INVEST (validate before every story)

| | Criterion | Check |
|-|-----------|-------|
| **I** | Independent | Stands alone; no dependency on incomplete stories |
| **N** | Negotiable | Starting point for discussion, not a locked contract |
| **V** | Valuable | Delivers real value to user or business |
| **E** | Estimable | Team can size it; if not → clarify or split |
| **S** | Small | Built + tested within one sprint (≤ 3 dev days) |
| **T** | Testable | Every AC has a clear pass/fail condition |

---

## 3 · ACCEPTANCE CRITERIA (AC)

**Format:** `- AC1 (Happy): [testable condition — pass/fail verifiable]`
**Prefer** one plain sentence per AC over Gherkin (Given/When/Then) — simpler to read and test.

- **One outcome per AC.** Split an AC when its outcomes can pass or fail separately (for example a status change and the toast that confirms it). A disabled or hidden control and the inline message that explains it count as one outcome.
- **Name the precondition.** When the AC depends on a situation or a state beyond "the user is on this screen", open with `If` (something happens) or `While` (a state holds): `- AC1 (Happy): While the seat hold is active, the remaining time is visible.`
- **Label the path.** Tag each AC `(Happy)`, `(Alternative)`, or `(Error)` so QC sees the coverage at a glance.

### Standalone story vs. story inside a PRD

- **Standalone** (a story written on its own, with no PRD): write the values directly in the AC, as in the examples.
- **Inside a PRD** (the PRD pipeline): the reader reads the PRD top to bottom, so each fact sits where it is needed, as defined in `knowledge-base/product-language/SKILL.md`. A rule only this story uses sits under the story in its Rules block, just above the AC; a rule several stories of the epic use sits at the top of the epic; only the foundation of the whole feature sits in General Rules. Rules, messages, screens, and metrics are named in words; the only codes are the job IDs on the epic's Serves line, the story ID in its heading, and the AC numbers. Each AC reads on its own: it applies the story's or epic's rules in plain words, states the effect of a rule from elsewhere in a few words (with a sample labelled e.g. when useful), and quotes a message's exact copy where it is shown first — `- AC2 (Error): If the cancellation cutoff has passed, the Cancel button is disabled and an inline note says "Online cancellation closes 24 hours before departure."` It never copies another story's whole rule table. What a status change causes lives in its lifecycle row; the AC only states that the change happens. Number AC within the story (`AC1`, `AC2`). Check INVEST, but do not print the check, a priority, or other metadata lines in the PRD.

### Must cover all of these

| Type | Rule |
|------|------|
| **Happy path** | At least one AC for the main successful flow |
| **Negative/edge flows** | `- ACn (Error): If [X], then [Y]` — at least one error/edge case. Inside a PRD, a situation in "Same in every story" counts for its situation |
| **Role-based** | Separate AC per role if multiple actors — only combine if buildable + testable together. Inside a PRD, who may act is a rule under the story where the action is taken; the AC states what an allowed or a refused role sees |
| **Error display** | For each broken rule or failure the story can hit: how it is shown (toast, inline error, popup) and which message |
| **Side-effects** | After the story's own action succeeds: what is recorded and for which metric, which notification is sent, what a partner is informed of — WHAT, never event names or how data is synced |
| **NFRs** | Performance, capacity, security — use exact thresholds, never vague quantifiers, and express them as the user or business experiences them (e.g., "results appear within 3 seconds"), not as infrastructure. Inside a PRD, a cross-cutting target lives in Non-Functional Requirements; a target that is this story's outcome is written in its AC |
| **Observable** | Every AC describes what the user sees or what result the business gets — never status codes, error codes, or internal system behavior |
| **Design hints** | Framed as preference: `- AC4 (Happy): Report is exportable. (Customer prefers Excel.)` |

### NFR placement

1. In the **WHAT** clause (if it defines system behaviour)
2. In **AC** (preferred — for performance, capacity, security). Inside a PRD, a threshold that applies across the feature lives in Non-Functional Requirements (or in a rule, for a limit); the AC states it when it is the story's own outcome
3. As its **own story** if effort is sprint-sized

### MoSCoW for AC priority

**M**ust / **S**hould / **C**ould / **W**on't — if an AC is Could/Won't, break it into a separate "Nice to Have" story rather than mixing priorities.

---

## 4 · ACTOR RULES

- Single actor, single action, single outcome per story
- If multiple roles share the same functionality: one story + role-based AC **only if** buildable AND testable together; otherwise → separate stories

---

## 5 · WHEN TO SPLIT A STORY

Split when any of these are true:

- `and` / `or` / `/` in the story statement
- AC list spans more than one sprint
- Multiple actors need separate build + test paths
- NFR effort is significant enough to own a sprint slot
- Story points = XL

**Strategies:** Part 1/2/3 · Split by actor · Split by flow (positive vs. edge) · Split by CRUD scope (Create / Edit / Delete)

---

## 6 · HIERARCHY

```text
Epic → Feature → User Story
```

- Stories must connect to a Feature; Features to an Epic
- Each story's "Why" must be **self-contained** — the "so that" clause makes sense without reading the Epic; devs work from stories, not Epics. Inside a PRD, do not paste the Epic description or another story's rules into the story: the Jira ticket gets its context from the Epic link, the epic's rules, the story's own rules, and its AC

---

## 7 · SPECIAL CASES

**Integration / partner stories**

```text
As a [person who benefits from the exchange],
I want to [see / receive / send] [business information] [from / to] [partner or team],
so that [outcome].
```

Also define, in business terms: what information is exchanged, when, who owns it, and what the user sees if the partner is unavailable. Inside a PRD, the outcome when the partner is unavailable lives in a rule under the story; the AC states what the user sees. Do not define endpoints, payloads, status codes, or data formats — those belong to the Dev team's technical design.

**Reporting stories:** WHO = person who uses the report · WHAT = the business information the report shows · AC = what the user sees (default sort, empty state, export result) · WHY = business reason. Inside a PRD, limits and formats are rules under the story

**Non-collocated teams:** Add more AC detail; supplement with SRD or mockup; link all artifacts explicitly in the story. Inside a PRD, add detail in the story's rules and AC, where the reader already is, not in a separate document.

**Mockups:** Each mockup section → one or more stories. Developed collaboratively. Suggestion tool only — not a locked design.

---

## 8 · ANTI-PATTERNS

| ❌ Anti-Pattern | Problem | ✅ Fix |
|-----------------|---------|--------|
| "I need a [feature]" | Leads to design requirements | Use "I want to [action]" |
| "and/or/" in statement | Multiple outcomes | Split story |
| Multiple actors, one story | Can't build+test together | Separate stories |
| Prescribes UI/technical solution | Limits team creativity | Describe user goal only |
| Generic actor ("user", "system", "developer") | No empathy or end-user value | Use specific persona |
| AC list too long | Spans multiple sprints | Split story |
| Vague NFR ("more than X") | Untestable | Use exact threshold |
| Developer as actor | No end-user value | Reframe as technical task |
| Missing "so that" | Team doesn't know the why | Always include value clause |
| Inside a PRD, AC says only "per BR-01" or "show MSG-04", or copies another story's whole rule table | A code forces the reader to look it up; a copied table drifts when the policy changes | Put the rule under the story or at the top of its epic, and state a rule from elsewhere by its effect in a few words |

---

## 9 · OUTPUT FORMAT

```text
##### US-01 - [Short descriptive title]

As a [Actor], I want to [Action + Object], so that [Value].

**Rules**                                   ← inside a PRD, only when the story has its own rules
| Rule | Example |

**Acceptance Criteria**
- AC1 (Happy): [positive condition]
- AC2 (Alternative): While [state], [what the user can do or sees]
- AC3 (Error): If [X], then [Y], and a [toast / inline error / popup] says "[copy]"
- AC4 (Happy): [NFR with exact threshold]

Notes (optional, standalone only)
[Design suggestion — framed as preference, not requirement]
[Links: mockup / SRD / related story]

INVEST (standalone only; inside a PRD the check is done, not printed)
[ ] I  [ ] N  [ ] V  [ ] E  [ ] S  [ ] T
```

---

## 10 · PRE-OUTPUT SELF-CHECK

Fix any failure before outputting.

- [ ] Actor is specific — not "user", "system", or "developer"
- [ ] Action is outcome-focused — no UI/technical prescriptions
- [ ] "so that" is present with genuine user/business value
- [ ] No `and` / `or` / `/` in WHO/DOES/WHAT
- [ ] Every AC has a clear pass/fail condition
- [ ] Every AC describes an observable outcome in business language — no status codes, endpoints, or internal components
- [ ] Inside a PRD: no rule, message, or screen codes; every AC reads on its own; rules only this story uses are in its Rules block; message copy is quoted where it is shown first
- [ ] Happy path + at least one negative/edge case covered, by its own AC or, inside a PRD, by "Same in every story"
- [ ] All AC completable within one sprint
- [ ] All 6 INVEST criteria pass
- [ ] NFRs use exact thresholds — no vague quantifiers
