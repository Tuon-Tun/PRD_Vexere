---
name: product-language-guide
description: >
  The single source of truth for how every PRD pipeline output is worded and where each fact
  lives. Product first: describe WHAT the feature does and WHY, in business language that PO, BA,
  Dev, and QC all read the same way, with every fact defined once and cited by ID everywhere else.
  Apply it in every step that writes or reviews PRD content.
---

# Product-First Language Guide

A PRD is a shared language between four readers: **PO, BA, Dev, and QC**. Its job is to hand over the rules, the logic, and the core value of a feature so that all four understand them the same way, without a meeting to explain the document.

The PRD describes **WHAT** the feature does and **WHY**. It does not describe **HOW** it is built.

## Why the PRD stays non-technical

Whoever writes the PRD, a person or an AI, usually does not have the full technical context: the company's tech stack, its engineering rules, its internal systems, the SaaS tools and configuration systems already in place. Technical detail written without that context is guesswork. It misleads Dev, it cannot be checked by PO, BA, or QC, and it hides the business rules that actually matter.

The Dev team owns the technical design (architecture, APIs, data model, configuration) in a separate document, linked from the PRD's References section.

## Why every fact is written once

When the same rule appears in a user story, a business rule, a use case, and a screen description, readers have to read it four times and still cannot tell which copy is the real one. When the policy changes, one copy gets updated and the others do not, and Dev and QC end up building and testing different numbers. So every fact has exactly **one home**. Every other place **cites its ID** instead of repeating it.

## What each reader needs

| Reader | Needs from the PRD |
|--------|--------------------|
| PO | The problem, the value, the goals, and what is in or out of scope |
| BA | Complete, consistent business rules, statuses, and flows |
| Dev | Unambiguous logic: conditions, limits, calculations, statuses, and what happens when something goes wrong |
| QC | Observable, testable outcomes with IDs to trace every test case back to a rule or an acceptance criterion |

## Rules

1. **Describe behavior, not implementation.** Write what the user, the operator, or the business observes. Never write how the system achieves it.
2. **Treat the system as one black box.** Call it "the system" or the product name. Do not split it into internal services, modules, or components. External parties (partners, other teams) may be named only when the input names them.
3. **Do not write technical detail.** No endpoints, HTTP methods or status codes, request or response payloads, JSON, error codes, database tables or fields, caches, queues, scheduled jobs, service or module names, frameworks, programming languages, code or pseudo-code, configuration keys, tracking event names or properties, or infrastructure.
4. **Translate, never drop.** When the input contains technical wording, keep its business meaning and rewrite it in product language (see the table below). If the meaning is unclear, ask in business terms.
5. **Be specific.** Non-technical does not mean vague. Every business rule states concrete values (amounts, time windows, counts, limits, roles) and the condition that triggers it, once, in its own row. Words such as "fast", "valid", "appropriate", "optimal", "flexible", or "etc." are allowed only when the PRD defines them.
6. **Make every outcome testable.** Acceptance criteria state a result QC can check by using the product, without reading code.
7. **One term per concept.** Use the same word for the same thing in every section. Define business terms, status names, and role names in the Glossary, and never switch to a synonym later.
8. **Adjustable values: say who, not how.** If the business needs to change a value without a new release (a fee, a limit, a time window), state that it is adjustable and by which role. If the value is set per partner or per campaign, give the rule's shape, who sets the value, the default if any, and a worked example labelled as sample values. Do not describe how it is configured.
9. **Route technical decisions to questions.** If a requirement depends on a technical decision, write the business need and add an Open Question owned by Dev / Tech Lead. Do not answer it in the PRD.
10. **Keep user-provided delivery constraints, do not expand them.** If the user explicitly states a constraint on how or when the feature is delivered (for example "must reuse the current payment partner", "launch before Tet"), record it once, as stated, under Known Constraints. A limit on what users or data may do (a count, a time window, an amount) is a business rule, not a constraint.
11. **Write plainly.** Short sentences, active voice, one idea per sentence. Tables for rules, numbered steps for flows.
12. **Define once, cite by ID.** Every fact lives in exactly one home (table below). Everywhere else, including other sections, diagrams, and messages, cite its ID and never repeat its value, formula, condition, or copy. IDs are plain text so they survive being copied into Jira. IDs are never renumbered or reused once approved; a removed item keeps its row, marked "No longer applies".

## Where each fact lives

Ask what a sentence is about. If it is about **money, seats or other inventory, a status, a voucher or other entitlement, or who may act**, it is a business rule. If it is about **what the user sees or what this story triggers**, it is an acceptance criterion that cites the rule.

| Fact | Its one home | ID |
|------|--------------|----|
| Who needs what, and why; priority | User Story (3.1) | `US-01` |
| Formulas, calculations, rounding, application order, with a worked example | Business Rules (3.2) | `BR-01` |
| Eligibility and conditional policies, including what happens to money, seats, or status when something fails | Business Rules (3.2) | `BR-01` |
| Limits and data constraints (time windows, quantities, input rules), and deadlines promised to the customer | Business Rules (3.2) | `BR-01` |
| Status transitions, their conditions, and their side-effects (notifications, inventory released, partner informed) | Business Rules (3.2), Statuses & Transitions | `BR-01` |
| Who may perform which action | Business Rules (3.2), Roles & Permissions | `BR-01` |
| What the user sees and can do in one story: UI behavior, loading and empty states, default sort order, what each button does, how an error or rule violation is shown (toast, inline error, popup), side-effects of this story's own action | Acceptance Criteria under its story (3.1) | `US-01-AC2` |
| Behavior that is the same in every story: login session expired, connection lost, repeated tap, system temporarily unavailable | Common Behaviors (3.1) | `CB-01` |
| The exact wording of every message, on any channel (screen, email, SMS, push) | Messages (3.6) | `MSG-01` |
| Quality targets: perceived speed, availability, supported platforms, information freshness, expected volume | Non-Functional Requirements (3.5) | `NFR-01` |
| Success metrics with their baselines and targets | Success Metrics table (2.4) | `SM-01` |
| Partners, teams, other PRDs, and existing features this feature relies on | Dependencies (3.7) | `DEP-01` |
| A rule defined in another approved PRD | That PRD, listed in Dependencies (3.7) | `[Other PRD name] BR-02` |
| The order of steps in a multi-step flow | Use Case (3.4), citing AC, CB, BR, and MSG IDs | `UC-01` |
| Unknown or assumed values | The rule's own row says `TBD (Q-03)` or `15 minutes (assumed, A-02)`; the question or assumption cites the rule ID | `Q-01`, `A-01` |

**Messages:** a message that mentions a rule value uses a named placeholder that cites the rule, never the number: "Tickets can be cancelled online up to {cancellation cutoff (BR-01)} before departure." Dynamic data uses a plain placeholder: `{ticket code}`. The message's Rules column lists every rule its wording depends on. Acceptance criteria and common behaviors say how a message is shown (toast, inline error, popup); transitions and use cases cite only its ID.

**Tracking and partners:** say WHAT, not HOW. Write "The system records each completed cancellation to measure SM-02" and "The operator is informed that the ticket is cancelled". Event names and properties belong to the Data team's tracking plan, and how data reaches a partner belongs to the technical design; both are linked in References.

## Translation examples

The examples are illustrative. Write in the user's language and use only the rules the input actually supports.

| Technical wording (avoid) | Product wording (use) |
|---------------------------|-----------------------|
| `POST /bookings` returns `409 Conflict` | BR: A seat held by one customer cannot be held by another. AC: If the seat was just taken (BR-04), the customer sees MSG-02 and is asked to choose another seat. |
| Request timeout 30s, retry 3 times | BR: The system waits up to 30 seconds for the operator to confirm and tries again up to 3 times; if there is still no confirmation, no money is taken. AC: If the booking is still unconfirmed after the retries (BR-07), a popup shows MSG-05. |
| `401 Unauthorized` | CB: If the login session has expired, the user is asked to log in again and returns to the step they were on. |
| `5xx` / service unavailable | CB: If the system cannot process the request right now, the user sees MSG-09 and can try again; BR: the customer is not charged. |
| Cron job runs at 00:00 daily | BR: Every day at 00:00, the system automatically [action]. |
| Data cached for 5 minutes | NFR: The displayed [information] may be up to 5 minutes behind the latest update. |
| `UPDATE bookings SET status = 'CANCELLED'` | BR (transition): Confirmed → Cancelled when [event and condition]. AC: the ticket moves to Cancelled (BR-08). |
| Config key `max_seats_per_booking = 5` | BR: A customer can book at most 5 seats per booking. The Operations team can change this limit. |
| Idempotency key on payment request | CB: If the customer taps "Pay" more than once, they are charged only once (BR-11). |
| Webhook from the payment gateway | BR (transition): When the payment partner reports success, the booking moves from Pending to Confirmed. |
| Emit an analytics event | AC: The system records each [action] to measure SM-01. |
| Rate limit 3 requests / 10 min | BR: A customer can request a new OTP at most 3 times within 10 minutes. AC: If the limit is reached (BR-12), the "Resend" button is disabled and MSG-06 is shown. |

## Self-check before output

- [ ] No forbidden technical detail (Rule 3) appears anywhere, including tables and diagrams.
- [ ] Every business rule has concrete values (or `TBD (Q-..)`) and a trigger condition, in its own row.
- [ ] No rule value, formula, condition, or message copy appears outside its home; every other mention cites the ID.
- [ ] Every acceptance criterion describes something a user or QC can observe.
- [ ] Every term matches the Glossary, with no synonyms.
- [ ] Every technical decision appears as an Open Question owned by Dev / Tech Lead, not as an answer.
- [ ] A PO, a BA, a Dev, and a QC would each read every sentence the same way.
