# Good User Story Examples

---

## Example 1 — Claims & Permissions (Financial Services)

**Story:**

```text
As a Claims Supervisor,
I want to access payment permissions,
so that I can know which reps on my team are authorised to make digital payments.
```

**Why it works:**

- Actor is specific (Claims Supervisor — not "user" or "manager")
- Action is outcome-focused — gaining knowledge, not clicking a screen
- Value is clear — oversight and control of authorised digital payments

**Acceptance Criteria:**

```text
Done when: The Claims Supervisor can view a list of all reps on their team.
Done when: The list indicates which reps are authorised to make digital payments.
Done when: The list indicates which reps are not authorised to make digital payments.
Done when: A Customer Service Rep cannot access the payment permissions screen.
Done when: A change to a rep's payment permission appears in the list within 5 minutes.
```

---

## Example 2 — Project Management Visibility

**Story:**

```text
As a Project Manager,
I want to view team workload,
so that I can assign tasks more effectively and prevent team burnout.
```

**Why it works:**

- Actor is specific and relatable
- Action is outcome-focused — viewing workload, not "seeing a dashboard"
- Value covers both the manager's goal and the broader team benefit

**Acceptance Criteria:**

```text
Done when: The project manager can see a workload view showing all active tasks per team member.
Done when: Tasks are displayed with estimated effort and due date.
Done when: The view highlights team members exceeding 100% capacity in a visually distinct way.
Done when: The workload view updates in real time as tasks are assigned or completed.
Done when: If no tasks are assigned to a team member, the view shows 0% utilisation.
```

---

## Example 3 — Order Notifications (E-commerce)

**Story:**

```text
As a Customer,
I want to receive order notifications,
so that I stay updated on my delivery status without having to check manually.
```

**Why it works:**

- Actor is the direct end user
- Action focuses on the user's goal — staying informed, not the delivery mechanism
- Value solves a real frustration — not knowing where your order is

**Acceptance Criteria:**

```text
Done when: The customer receives a notification when their order is confirmed.
Done when: The customer receives a notification when their order is shipped.
Done when: The customer receives a notification when their order is out for delivery.
Done when: The customer receives a notification when their order is delivered.
Done when: If the customer has opted out of notifications, they receive no automated messages.
Done when: Notifications are sent within 5 minutes of the relevant status change. (Customer's preference is email.)
```

---

## Example 4 — Admin Password Reset (IT / Support)

**Story:**

```text
As an Admin,
I want to reset user passwords,
so that I can help users regain account access quickly and reduce support wait times.
```

**Why it works:**

- Actor is specific with a clear support role
- Action is outcome-focused — resetting passwords, not "clicking a button"
- Value ties to both the user's need (regain access) and the business benefit (reduce support time)

**Acceptance Criteria:**

```text
Done when: The admin can search for a user by name or email address.
Done when: The admin can trigger a password reset for any found user account.
Done when: The user receives a password reset email within 2 minutes of the admin triggering the reset.
Done when: The reset link expires after 24 hours.
Done when: If the user account is locked, the admin can unlock it alongside the password reset.
Done when: If the admin searches for a non-existent account, the system displays "No account found" and does not error.
Done when: All password reset actions are logged with the admin's ID and timestamp for audit purposes.
```

---

## Example 5 — Wishlist Functionality (E-commerce)

**Story:**

```text
As a Shopper,
I want to save products to a wishlist,
so that I can manage all items I'm interested in and purchase them at a convenient time.
```

**Why it works:**

- Actor is specific — a Shopper with a clear purchase intent context
- Action is outcome-focused — saving and managing interest, not "adding to a list"
- Value is concrete — deferred purchase on the shopper's own timeline

**Acceptance Criteria:**

```text
Done when: The shopper can add a product to their wishlist from the product detail page.
Done when: The shopper can view all items saved to their wishlist in one place.
Done when: The shopper can remove any item from their wishlist.
Done when: If an item in the wishlist goes out of stock, it is marked as "Out of Stock" but remains in the list.
Done when: The wishlist persists across sessions — items are still present when the user logs back in.
Done when: If the shopper is not logged in, they are prompted to log in or register before saving to wishlist.
```

---

## Example 6 — Community Safety Notification (Mobile App)

**Story:**

```text
As a Community Driver,
I want to warn my network about road hazards,
so that other drivers nearby can avoid the same danger I encountered.
```

**Why it works:**

- Actor is specific — Community Driver, not generic "user"
- Action is outcome-focused — warning the network, not "using voice commands" (mechanism removed)
- Value is immediate and personal — protecting peers from a hazard already experienced

**Acceptance Criteria:**

```text
Done when: The driver can create and publish a road hazard alert from within the app.
Done when: The app reads the alert back to the driver for confirmation before publishing.
Done when: The driver must confirm before the alert is sent to their network.
Done when: Upon confirmation, notifications are sent to all connected friends within 30 seconds.
Done when: If the driver cancels, no notification is sent and the draft is discarded.
Done when: If alert creation fails after 3 attempts, the app offers an alternative input method.
```

---

## Example 7 — Multi-Role Data Access

**Story:**

```text
As a CSR System User,
I want to update customer demographic data,
so that customer records remain accurate and up to date.
```

**Why it works:**

- Actor is a unified persona covering multiple roles — valid when all roles share the same build + test path
- Action is singular and clear — update demographic data
- Roles are separated in AC, not the story — keeping the story statement clean

**Acceptance Criteria:**

```text
Done when: A Customer Service Rep can update demographic data.
Done when: An Admin can update demographic data.
Done when: A Supervisor can update demographic data and view an audit log of all changes.
Done when: Each role's access is verified by individual login credentials before updates are permitted.
Done when: If a user attempts to access demographic data without the appropriate role, they receive an "Access Denied" message.
```

---

## Example 8 — Integration / Partner Story

**Story:**

```text
As an Online Shopper,
I want to see my order's current status and estimated delivery date from the delivery partner,
so that I can plan to be home when the parcel arrives.
```

**Why it works:**

- Actor is the person who benefits from the integration, not the system
- Action names the business information exchanged and where it comes from — no endpoints or data formats
- Value traces to a real outcome for the shopper
- The technical design (how the partner's data is received) is left to the Dev team

**Acceptance Criteria:**

```text
Done when: The order page shows the order status, the estimated delivery date, and the time of the last update from the delivery partner.
Done when: The order page loads within 2 seconds for 95% of visits.
Done when: If the delivery partner has not sent an update for more than 24 hours, the order page shows "Delivery information is being updated" instead of an outdated date.
Done when: If the order number does not exist, the shopper sees "Order not found."
Done when: Only the shopper who placed the order can see its delivery information.
```

---

## Example 9 — Story Inside a PRD (Rules Cited by ID)

Inside a PRD, rule values, message wording, and shared behaviors are written once in their own tables. The story's AC name each rule in words and cite its ID, so a policy change is edited in one row only.

**From the PRD's Business Rules (3.1), Screens and Messages (3.6):**

```text
BR-01 | A ticket can be cancelled online up to 24 hours before departure.
BR-02 | Cancellation fee = 10% of the ticket price. Example: ticket 300,000 VND -> fee 30,000 VND.
BR-03 | Refund = amount paid - cancellation fee (BR-02). Uses: BR-02. Example: paid 300,000 VND -> refund 270,000 VND.
BR-04 | Permission: cancel a ticket. Passenger: own tickets. Customer service: on the passenger's behalf.
BR-05 | Transition: Confirmed -> Cancelled. Event: cancellation confirmed by a role allowed by BR-04.
        Condition: within the cancellation cutoff (BR-01). Side-effects of this event: refund per BR-03.
BR-06 | On entering Cancelled: seat returned to the operator; MSG-03 sent.
MSG-01 | Screen | "Tickets can be cancelled online up to {cancellation cutoff (BR-01)} before departure." | Rules: BR-01
MSG-02 | Screen | "Your ticket has been cancelled. Refund: {refund amount}."                              | Rules: BR-03
MSG-03 | Email  | "Cancellation confirmed for ticket {ticket code}..."                                    | Rules: —
CB-02  | Repeated tap: tapping "Confirm" more than once moves the ticket to Cancelled only once (BR-05).
SCR-01 | My tickets | Design: [Figma frame link, filled by the designer]
```

**Story:**

```text
As a Passenger who changed my travel plans,
I want to cancel my ticket in the app,
so that I get my money back without calling the hotline.

Priority: Must
Screens: SCR-01
Jira: [PM fills after creating the ticket "US-01 Cancel a ticket"]
Common behaviors: CB-02
Rules applied (PRD Ticket Cancellation): BR-01, BR-02, BR-03, BR-04, BR-05, BR-06
```

**Why it works:**

- No AC repeats "24 hours", "10%", or any message wording — changing the cutoff to 12 hours edits BR-01 only
- The email and the seat release are on the "on entering Cancelled" row (BR-06), written once however the ticket gets cancelled
- `Rules applied` lists BR-01, BR-02, BR-03, and BR-05 because the AC and CB-02 cite them, and BR-04 and BR-06 because the transition BR-05 names its permission and its new status. It stops there: a rule that BR-03 uses would be found in BR-03's Uses column, not added to the line
- Repeated taps are handled once by CB-02, which the story lists instead of writing its own AC for it
- MSG-02's Rules column names BR-03, so a change to the refund rule shows which message to re-check

**Acceptance Criteria:**

```text
AC1 (Happy) Done when: While a ticket is within the cancellation cutoff (BR-01), "My tickets" shows a "Cancel ticket" button for it.
AC2 (Error) Done when: If the cancellation cutoff has passed (BR-01), the button is disabled and an inline explanation shows MSG-01.
AC3 (Happy) Done when: Tapping "Cancel ticket" opens a popup with the fee (BR-02) and the refund amount (BR-03) before the passenger confirms.
AC4 (Happy) Done when: After the passenger confirms, the ticket moves to Cancelled (BR-05).
AC5 (Happy) Done when: After the passenger confirms, a toast shows MSG-02.
AC6 (Alternative) Done when: If the passenger closes the popup without confirming, they are back on "My tickets" and the ticket still shows as Confirmed.
```
