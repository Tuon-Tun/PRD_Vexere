---
name: product-language-guide
description: >
  The single source of truth for how every PRD pipeline output is worded and where each fact
  lives. Product first and human first: the PRD describes WHAT the feature does and WHY, in
  business language PO, BA, Dev, and QC read the same way, and a reader understands it top to
  bottom without looking anything up. Apply it in every step that writes or reviews PRD content.
---

# Product-First Language Guide

A PRD is a shared language between four readers: **PO, BA, Dev, and QC**. Its job is to hand over the rules, the logic, and the core value of a feature so that all four understand them the same way, without a meeting to explain the document.

The PRD describes **WHAT** the feature does and **WHY**. It does not describe **HOW** it is built.

## Why the PRD reads top to bottom, without codes

People read a PRD like any other document: from the top, one section at a time. A reader cannot hold a register of codes in their head. A sentence such as "per BR-26, show MSG-04 (CB-02)" forces them to open three other sections before they know what it says, and once a domain has several PRDs that cross-reference each other, nobody can follow it at all.

So the PRD is written for a reader who has only the page in front of them:

- **Each fact sits where the reader needs it.** A rule lives under the story that uses it, at the top of its epic when several stories of that epic use it, or in General Rules only when it is the foundation of the whole feature.
- **Codes only where they help.** A code stays when it labels an item the reader meets in a short list and that other parts point to at a high level, or that people use outside the PRD: jobs (`JTBD-01`, each epic names the jobs it serves), epics (`Epic 1`), stories (`US-01`, also the Jira ticket summary), and the numbers of a story's acceptance criteria (`AC1`, used by QC for test cases). Rules, messages, screens, metrics, and quality targets are named in words, never by an ID.
- **The overview comes first and is plain.** The Problem Statement, JTBD, and Goals are short prose a new reader understands before meeting any rule.

## Why the PRD stays non-technical

Whoever writes the PRD, a person or an AI, usually does not have the full technical context: the company's tech stack, its engineering rules, its internal systems, the SaaS tools and configuration systems already in place. Technical detail written without that context is guesswork. It misleads Dev, it cannot be checked by PO, BA, or QC, and it hides the business rules that actually matter.

The Dev team owns the technical design (architecture, APIs, data model, configuration) in a separate document, linked from the PRD's References section.

## What each reader needs

| Reader | Needs from the PRD |
|--------|--------------------|
| PO | The problem, the value, and the goals |
| BA | Complete, consistent business rules, statuses, and flows |
| Dev | Unambiguous logic: conditions, limits, calculations, statuses, and what happens when something goes wrong |
| QC | Observable, testable outcomes, numbered within each story so every test case points to one acceptance criterion |

## Rules

1. **Describe behavior, not implementation.** Write what the user, the operator, or the business observes. Never write how the system achieves it.
2. **Treat the system as one black box.** Call it "the system" or the product name. Do not split it into internal services, modules, or components. External parties (partners, other teams) may be named only when the input names them.
3. **Do not write technical detail.** No endpoints, HTTP methods or status codes, request or response payloads, JSON, error codes, database tables or fields, caches, queues, scheduled jobs, service or module names, frameworks, programming languages, code or pseudo-code, configuration keys, tracking event names or properties, or infrastructure.
4. **Translate, never drop.** When the input contains technical wording, keep its business meaning and rewrite it in product language (see the table below). If the meaning is unclear, ask in business terms.
5. **Be specific.** Non-technical does not mean vague. Every business rule states concrete values (amounts, time windows, counts, limits, roles) and the condition that triggers it. Words such as "fast", "valid", "appropriate", "optimal", "flexible", or "etc." are allowed only when the PRD defines them.
6. **Make every outcome testable.** Acceptance criteria state a result QC can check by using the product, without reading code.
7. **One term per concept.** Use the same word for the same thing in every section. Define business terms, status names, and role names in the Glossary, and never switch to a synonym later.
8. **Adjustable values: say who, not how.** If the business needs to change a value without a new release (a fee, a limit, a time window), state that it is adjustable and by which role. If the value is set per partner or per campaign, give the rule's shape, who sets the value, the default if any, and a worked example labelled as sample values. Do not describe how it is configured.
9. **Technical decisions are questions, not answers.** If a requirement depends on a technical decision, write the business need, mark the open point `TBD` with who decides in words ("TBD, Dev / Tech Lead decides"), and list it for the user at the approval step. Do not answer it in the PRD.
10. **Delivery constraints stay out of the PRD.** A constraint the user states on how or when the feature is delivered (for example "must reuse the current payment partner", "launch before Tet", "one shared formatter for every amount") belongs to the delivery plan or the Dev team's technical design, not to the PRD. List it for the user at the approval step so it reaches the Dev team. A limit on what users or data may do (a count, a time window, an amount) is a business rule, not a constraint.
11. **Write plainly.** Short sentences, active voice, one idea per sentence. Tables for rules, numbered steps for flows.
12. **Codes only where they help.** The PRD keeps four kinds of code: job IDs (`JTBD-01`) in each job's heading and in the line under each epic that names the jobs it serves; epic numbers (`Epic 1`); story IDs (`US-01`) in story headings; and acceptance criterion numbers within a story (an acceptance criterion may point to another of the same story, "as in AC3"). These label short lists the reader sees, or items Jira and QC use. Never write a rule, message, screen, metric, quality target, dependency, assumption, question, or common behavior by an ID (`BR-`, `MSG-`, `SCR-`, `SM-`, `NFR-`, `DEP-`, `A-`, `Q-`, `UC-`, `CB-`), and never copy source codes from the input ("CR-08", "Gốc: ..."). Name those things in words.
13. **Readable in place.** A reader understands each story from its epic and its own block, without opening another section. An acceptance criterion states the situation and the outcome in plain words. When the outcome depends on a rule that sits elsewhere (General Rules, or another story), it says that rule's effect in a few words and may add a sample labelled "e.g." (in Vietnamese "VD"). A message is described by what it says, and its exact copy is written in quotes where the message is shown.
14. **Unknowns stay visible but light.** An assumed value is written in its rule as `[value] (assumed)`, an unknown one as `TBD` with who decides in words. They are listed for the user in the chat at the approval step; the PRD has no assumptions or open-questions register.

## Where each fact lives

Ask what a sentence is about. If it is about **money, seats or other inventory, a status, a voucher or other entitlement, or who may act**, it is a business rule. If it is about **what the user sees or what this story triggers**, it is an acceptance criterion.

| Fact | Where it lives |
|------|----------------|
| The jobs users hire the feature for | JTBD (2.2), one job story per actor, numbered `JTBD-01`; each epic names the jobs it serves |
| Who needs what, and why | The user story statement (3.3) |
| A rule only one story uses: formula, policy, limit, who may take this story's action | Rules, under that story (3.3) |
| A rule several stories of the same epic use, including a status lifecycle only that epic uses | Epic rules, at the top of that epic (3.3) |
| A rule that is the foundation of the whole feature and applies across epics (for example the payment currency, the number format, a status lifecycle several epics depend on), and situations that behave the same in every story (session expired, connection lost, repeated tap, system unavailable) | General Rules (3.1) |
| A rule several PRDs of the domain share | The domain rules file `domain-knowledge/[Domain_Name]/rules.md`; the PRD says the rule's effect in words and names the file |
| What the user sees and can do in one story: UI behavior, loading and empty states, default sort order, what each button does, how an error or rule violation is shown (toast, inline error, popup), side-effects of this story's own action | Acceptance Criteria under its story (3.3) |
| The exact copy of a message, on any channel (screen, email, SMS, push) | In quotes, in the acceptance criterion (or general behavior) where it is shown first; elsewhere it is described in a few words |
| A quality target that applies across the feature: perceived speed, availability, supported platforms, information freshness, expected volume | Non-Functional Requirements (3.4) |
| A quality target that is the outcome of one story | That story's acceptance criterion |
| Success metrics with their baselines, targets, and owners (only when the user asked for them) | Success Metrics (2.4) |
| Screens and their purpose, with design links (only when the user asked for them) | Screens (3.5) |
| Unknown or assumed values, technical decisions | In the rule itself: `TBD` with who decides, or `[value] (assumed)`; listed for the user in the chat at approval |

**A value in two places.** Saying a rule's effect in an acceptance criterion repeats a little of it. Keep the rule row as the source: the effect in the criterion stays short, and when a rule changes, every criterion of the same epic that mentions it is updated in the same edit. The reviewer checks that the two still match.

**Tracking and partners:** say WHAT, not HOW. Write "The system records the UI language of each session to measure the booking completion rate" and "The operator is informed that the ticket is cancelled". Event names and properties belong to the Data team's tracking plan, and how data reaches a partner belongs to the technical design; both are linked in References.

## Translation examples

The examples are illustrative. Write in the user's language and use only the rules the input actually supports.

| Technical wording (avoid) | Product wording (use) |
|---------------------------|-----------------------|
| `POST /bookings` returns `409 Conflict` | Rule: A seat held by one customer cannot be held by another. AC: If the seat was just taken, a popup says "This seat has just been booked. Please choose another seat." and the seat map reloads. |
| Request timeout 30s, retry 3 times | Rule: The system waits up to 30 seconds for the operator to confirm and tries again up to 3 times; if there is still no confirmation, no money is taken. AC: If the booking is still unconfirmed after the retries, a popup says the booking could not be confirmed and that no money was taken. |
| `401 Unauthorized` | General rule: If the login session has expired, the user is asked to log in again and returns to the step they were on. |
| `5xx` / service unavailable | General rule: If the system cannot process the request right now, the user sees "Something went wrong. Please try again." and is not charged. |
| Cron job runs at 00:00 daily | Rule: Every day at 00:00, the system automatically [action]. |
| Data cached for 5 minutes | NFR: The displayed [information] may be up to 5 minutes behind the latest update. |
| `UPDATE bookings SET status = 'CANCELLED'` | Rule (lifecycle): Confirmed → Cancelled when [event and condition]. AC: the ticket moves to Cancelled. |
| Config key `max_seats_per_booking = 5` | Rule: A customer can book at most 5 seats per booking. The Operations team can change this limit. |
| Idempotency key on payment request | General rule: If the customer taps "Pay" more than once, they are charged only once. |
| Webhook from the payment gateway | Rule (lifecycle): When the payment partner reports success, the booking moves from Pending to Confirmed. |
| Emit an analytics event | AC: The system records each [action] to measure [metric name]. |
| Rate limit 3 requests / 10 min | Rule: A customer can request a new OTP at most 3 times within 10 minutes. AC: If the limit is reached, the "Resend" button is disabled and an inline note says when they can try again. |

## Self-check before output

- [ ] No forbidden technical detail (Rule 3) appears anywhere, including tables and diagrams.
- [ ] No code other than job IDs, epic numbers, story IDs, and AC numbers appears anywhere, including tables and diagrams.
- [ ] Every business rule has concrete values (or `TBD` with who decides) and a trigger condition.
- [ ] Every rule sits where its readers need it: under its one story, at the top of its epic, or in General Rules only when it applies across epics.
- [ ] Every story can be understood from its epic and its own block without opening another section.
- [ ] Every acceptance criterion describes something a user or QC can observe.
- [ ] Every term matches the Glossary, with no synonyms.
- [ ] A PO, a BA, a Dev, and a QC would each read every sentence the same way.
