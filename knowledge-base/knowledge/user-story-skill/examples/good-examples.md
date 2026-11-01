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
- The Claims Supervisor can view a list of all reps on their team.
- The list indicates which reps are authorised to make digital payments.
- The list indicates which reps are not authorised to make digital payments.
- A Customer Service Rep cannot access the payment permissions screen.
- A change to a rep's payment permission appears in the list within 5 minutes.
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
- The project manager can see a workload view showing all active tasks per team member.
- Tasks are displayed with estimated effort and due date.
- The view highlights team members exceeding 100% capacity in a visually distinct way.
- The workload view updates in real time as tasks are assigned or completed.
- If no tasks are assigned to a team member, the view shows 0% utilisation.
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
- The customer receives a notification when their order is confirmed.
- The customer receives a notification when their order is shipped.
- The customer receives a notification when their order is out for delivery.
- The customer receives a notification when their order is delivered.
- If the customer has opted out of notifications, they receive no automated messages.
- Notifications are sent within 5 minutes of the relevant status change. (Customer's preference is email.)
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
- The admin can search for a user by name or email address.
- The admin can trigger a password reset for any found user account.
- The user receives a password reset email within 2 minutes of the admin triggering the reset.
- The reset link expires after 24 hours.
- If the user account is locked, the admin can unlock it alongside the password reset.
- If the admin searches for a non-existent account, the system displays "No account found" and does not error.
- All password reset actions are logged with the admin's ID and timestamp for audit purposes.
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
- The shopper can add a product to their wishlist from the product detail page.
- The shopper can view all items saved to their wishlist in one place.
- The shopper can remove any item from their wishlist.
- If an item in the wishlist goes out of stock, it is marked as "Out of Stock" but remains in the list.
- The wishlist persists across sessions — items are still present when the user logs back in.
- If the shopper is not logged in, they are prompted to log in or register before saving to wishlist.
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
- The driver can create and publish a road hazard alert from within the app.
- The app reads the alert back to the driver for confirmation before publishing.
- The driver must confirm before the alert is sent to their network.
- Upon confirmation, notifications are sent to all connected friends within 30 seconds.
- If the driver cancels, no notification is sent and the draft is discarded.
- If alert creation fails after 3 attempts, the app offers an alternative input method.
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
- A Customer Service Rep can update demographic data.
- An Admin can update demographic data.
- A Supervisor can update demographic data and view an audit log of all changes.
- Each role's access is verified by individual login credentials before updates are permitted.
- If a user attempts to access demographic data without the appropriate role, they receive an "Access Denied" message.
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
- The order page shows the order status, the estimated delivery date, and the time of the last update from the delivery partner.
- The order page loads within 2 seconds for 95% of visits.
- If the delivery partner has not sent an update for more than 24 hours, the order page shows "Delivery information is being updated" instead of an outdated date.
- If the order number does not exist, the shopper sees "Order not found."
- Only the shopper who placed the order can see its delivery information.
```

---

## Example 9 — Story Inside a PRD (Read Top to Bottom, No Codes)

Inside a PRD, the reader reads from the top and never looks anything up. A rule only this story uses sits right under the story; a rule several stories of the epic use sits at the top of the epic; only the foundation of the whole feature sits in General Rules. Nothing is named by a code: the only identifiers are the story ID in its heading and the AC numbers. A message's exact copy is quoted where it is shown.

**From the PRD's General Rules (3.1):**

```text
Same in every story
Repeated tap | Tapping a confirm button more than once performs the action only once.
```

**The epic and the story:**

```text
#### Epic 2: Manage my tickets

Passengers change or cancel their tickets without calling the hotline.

Rules for this epic
Ticket status | Confirmed -> Cancelled, when a cancellation is confirmed before the cancellation cutoff.
              | When a ticket enters Cancelled: the seat is returned to the operator and the passenger
              | gets the email "Cancellation confirmed for ticket {ticket code}".
Who may cancel | The passenger, for their own tickets; customer service, on the passenger's behalf.

##### US-04 - Cancel a ticket

As a passenger who changed my travel plans, I want to cancel my ticket in the app,
so that I get my money back without calling the hotline.

Rules
Rule                                                          | Example
A ticket can be cancelled online up to 24 hours before         | Departure 20:00 on 12 May -> online cancellation
departure (the cancellation cutoff).                           | closes at 20:00 on 11 May.
Cancellation fee = 10% of the ticket price.                    | Ticket 300,000 VND -> fee 30,000 VND.
Refund = amount paid - cancellation fee.                       | Paid 300,000 VND -> refund 270,000 VND.
```

**Acceptance Criteria:**

```text
- AC1 (Happy): While a ticket is still before its cancellation cutoff, "My tickets" shows a "Cancel ticket" button for it.
- AC2 (Error): If the cancellation cutoff has passed, the button is disabled and an inline note says "Online cancellation closes {cancellation cutoff} before departure."
- AC3 (Happy): Tapping "Cancel ticket" opens a popup showing the cancellation fee and the refund amount before the passenger confirms. E.g. ticket 300,000 VND -> fee 30,000 VND, refund 270,000 VND.
- AC4 (Happy): After the passenger confirms, the ticket moves to Cancelled and the refund is started.
- AC5 (Happy): After the passenger confirms, a toast says "Your ticket has been cancelled. Refund: {refund amount}."
- AC6 (Alternative): If the passenger closes the popup without confirming, they are back on "My tickets" and the ticket still shows as Confirmed.
```

**Why it works:**

- The reader meets the cutoff, fee, and refund rules right above the AC that apply them; nothing has to be memorized or looked up
- The ticket status and who may cancel sit at the top of the epic, because the customer-service story in the same epic uses them too; AC4 only states that the status changes
- Repeated taps are handled once in General Rules, so the story does not write its own AC for them
- Each message's exact copy is in the AC where it is shown; there is no message table to cross-check
- The only identifiers are "US-04" (also the start of the Jira ticket summary) and AC1 to AC6, which QC uses for test cases
