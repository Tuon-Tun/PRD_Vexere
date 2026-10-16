---
name: product-language-guide
description: >
  The single source of truth for how every PRD pipeline output is worded. Product first:
  describe WHAT the feature does and WHY, in business language that PO, BA, Dev, and QC
  all read the same way. Apply it in every step that writes or reviews PRD content.
---

# Product-First Language Guide

A PRD is a shared language between four readers: **PO, BA, Dev, and QC**. Its job is to hand over the rules, the logic, and the core value of a feature so that all four understand them the same way, without a meeting to explain the document.

The PRD describes **WHAT** the feature does and **WHY**. It does not describe **HOW** it is built.

## Why the PRD stays non-technical

Whoever writes the PRD, a person or an AI, usually does not have the full technical context: the company's tech stack, its engineering rules, its internal systems, the SaaS tools and configuration systems already in place. Technical detail written without that context is guesswork. It misleads Dev, it cannot be checked by PO, BA, or QC, and it hides the business rules that actually matter.

The Dev team owns the technical design (architecture, APIs, data model, configuration) in a separate document, linked from the PRD's References section.

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
3. **Do not write technical detail.** No endpoints, HTTP methods or status codes, request or response payloads, JSON, error codes, database tables or fields, caches, queues, scheduled jobs, service or module names, frameworks, programming languages, code or pseudo-code, configuration keys, or infrastructure.
4. **Translate, never drop.** When the input contains technical wording, keep its business meaning and rewrite it in product language (see the table below). If the meaning is unclear, ask in business terms.
5. **Be specific.** Non-technical does not mean vague. Every rule states concrete values (amounts, time windows, counts, limits, roles), the condition that triggers it, and what the user sees. Words such as "fast", "valid", "appropriate", "optimal", "flexible", or "etc." are allowed only when the PRD defines them.
6. **Make every outcome testable.** Acceptance criteria and flows state a result QC can check by using the product, without reading code.
7. **One term per concept.** Use the same word for the same thing in every section. Define business terms, statuses, and roles in the Glossary, and never switch to a synonym later.
8. **Adjustable values: say who, not how.** If the business needs to change a value without a new release (a fee, a limit, a time window), state that it is adjustable and by which role. Do not describe how it is configured.
9. **Route technical decisions to questions.** If a requirement depends on a technical decision, write the business need and add an Open Question owned by Dev / Tech Lead. Do not answer it in the PRD.
10. **Keep user-provided constraints, do not expand them.** If the user explicitly states a technical constraint (for example "must reuse the current payment partner"), record it once, as stated, under Known constraints in Dependencies & Impacted Areas. Do not add technical detail around it.
11. **Write plainly.** Short sentences, active voice, one idea per sentence. Tables for rules, numbered steps for flows, and IDs for traceability: `US-`, `BR-`, `UC-`, `FR-`, `NFR-`, `MSG-`, `Q-`.

## Translation examples

The examples are illustrative. Write in the user's language and use only the rules the input actually supports.

| Technical wording (avoid) | Product wording (use) |
|---------------------------|-----------------------|
| `POST /bookings` returns `409 Conflict` | If the seat was just taken by another customer, the system tells the customer the seat is no longer available and asks them to choose another seat. |
| Request timeout 30s, retry 3 times | If the operator has not confirmed within 30 seconds, the system tries again, up to 3 times. After that, the customer is told the booking could not be confirmed. |
| `401 Unauthorized` | If the customer's login session has expired, they are asked to log in again and return to the step they were on. |
| `5xx` / service unavailable | If the system cannot process the request right now, the customer sees "Please try again in a few minutes" and is not charged. |
| Cron job runs at 00:00 daily | Every day at 00:00, the system automatically [action]. |
| Data cached for 5 minutes | The displayed [information] may be up to 5 minutes behind the latest update. |
| `UPDATE bookings SET status = 'CANCELLED'` | The ticket moves to the status "Cancelled". |
| Config key `max_seats_per_booking = 5` | A customer can book at most 5 seats per booking. The Operations team can change this limit. |
| Idempotency key on payment request | If the customer taps "Pay" more than once, they are charged only once. |
| Webhook from the payment gateway | When the payment partner reports the payment result, the system [action]. |
| Emit an analytics event | The system records each [action] so the team can measure [metric]. |
| Rate limit 3 requests / 10 min | A customer can request a new OTP at most 3 times within 10 minutes. |

## Self-check before output

- [ ] No forbidden technical detail (Rule 3) appears anywhere, including tables and diagrams.
- [ ] Every business rule has concrete values and a trigger condition.
- [ ] Every acceptance criterion and exception flow describes something a user or QC can observe.
- [ ] Every term matches the Glossary, with no synonyms.
- [ ] Every technical decision appears as an Open Question owned by Dev / Tech Lead, not as an answer.
- [ ] A PO, a BA, a Dev, and a QC would each read every sentence the same way.
