# Extended Session Handout

## Goal

In this extended session, your group will first research a public architecture.
You will then act as AI Project Managers and use Claude Code to prototype the
same small product twice: once as a monolith and once as a distributed,
multi-service system.

Claude Code writes the implementation. Your role is to frame the product,
approve the scope, test both versions, compare evidence, make an architecture
decision, and record why. Do not build the application manually.

## Recommended Implementation Stack

For this exercise, we recommend a deliberately lightweight stack. It lets Claude
Code produce a working application quickly and keeps the comparison about
architecture rather than about learning several frameworks at once.

| Layer | Recommended choice | Why this helps the comparison |
|---|---|---|
| Frontend | Plain HTML, CSS, and JavaScript | The form, browser behavior, and API request stay visible. React would introduce components, state management, and build tooling that are outside this session. |
| API | FastAPI | Claude Code can generate small Python routes quickly, and the local `/docs` page lets the group inspect and test the API in a browser. |
| Database | SQLite via Python's `sqlite3` module | It creates a real persistent database in a local file, without a database server, cloud account, or credentials. |

This is not a universal recommendation. A production team may choose React for
a richer frontend, PostgreSQL for concurrent or production-scale data, another
API framework, or a managed database for good reasons. If your group chooses an
alternative, ask Claude Code to explain the reason and keep that same stack for
both prototypes. Here, the recommended stack makes frontend, API, database, and
service boundaries easy to observe.

## Timebox

This version assumes roughly twice the normal activity time: about 6-7 hours
including breaks and presentations.

| Time | Activity | Output |
|---|---|---|
| 30 min | Choose company, product scope, and sources | Source list and research question |
| 45 min | Manual architecture snapshot | First hypothesis with confidence labels |
| 45 min | Source validation and evidence matrix | Known / Likely / Possible / Unknown claims |
| 30 min | Architecture critique and product choice | Evidence-backed architecture snapshot |
| 35 min | Prototype brief and Claude Code plan | Approved brief and acceptance criteria |
| 60 min | Monolith prototype with Claude Code | Running monolith and test evidence |
| 75 min | Multi-service prototype with Claude Code | Running multi-service prototype and contracts |
| 45 min | Compare data flow, failure modes, and delivery cost | Architecture comparison table and risk list |
| Optional, 45-90 min | Product extensions with Claude Code | One or more verified extensions in both versions |
| 40 min | ADR and final synthesis | One ADR plus recommendation |
| 30 min | Presentation preparation | 5-slide outline |
| 5-7 min per group | Presentation | Architecture story and PM implications |

## Deliverables

Submit these five core items:

1. Architecture snapshot using [templates/architecture-brief.md](templates/architecture-brief.md)
2. Prototype brief using [templates/prototype-brief.md](templates/prototype-brief.md)
3. A working monolith prototype
4. A working multi-service prototype
5. One ADR using [templates/adr-template.md](templates/adr-template.md)

## Part 1: Choose a Company

Pick a company with public engineering material. Start with the list in
[02 - Reverse-Engineer Public Architecture](02-reverse-engineer-public-architecture.md)
or choose your own.

Write down:

- company
- core product
- product scope you will focus on
- at least five source URLs
- why this architecture is interesting for PMs

Good scopes:

- Slack message delivery and notifications
- Figma real-time collaboration
- Stripe API reliability
- Netflix streaming reliability
- Shopify storefront and checkout
- Airbnb search and booking data flow

## Part 2: Manual Snapshot

Before using an AI assistant, fill in a rough architecture snapshot yourself.
Keep it imperfect. The point is to have your own mental model before delegating.

Use confidence labels:

- Known
- Likely
- Possible
- Unknown

## Part 3: Evidence Matrix

Create a table with your strongest claims.

| Claim | Source | Confidence | What would make it stronger? |
|---|---|---|---|
|  |  | Known / Likely / Possible / Unknown |  |

Reject claims that have no source and no clear inference path.

## Part 4: Ask Claude Code to Challenge You

Prompt:

```text
You are my architecture research partner.

I am preparing a PM-facing architecture brief for <company> and focusing on
<product scope>.

Here is my first hypothesis:

<paste your snapshot>

Challenge it.
Mark unsupported claims, missing sources, likely overclaims, and important PM
risks I have missed. Do not invent facts. Ask for better evidence where needed.
Separate Known, Likely, Possible, and Unknown.
```

Update the brief based on what you accept. Note rejected suggestions directly
in the brief.

## Part 5: Select the Prototype Product

Use the shared office room-booking tool. This common scope makes comparison
between groups easier and keeps implementation time under control.

The product must support only this journey:

1. Browse rooms and available slots.
2. Create a booking with a name, room, date, and time.
3. Reject a conflicting booking.
4. Keep confirmed bookings after browser refresh.
5. Show a confirmation after a successful booking.

Do not add user accounts, external calendars, email delivery, payments, cloud
deployment, or a design system. Those are valid product decisions, but they
would obscure the architecture comparison.

Complete [templates/prototype-brief.md](templates/prototype-brief.md). Keep the
same brief and acceptance criteria for both variants.

## Part 6: Prototype the Monolith

Ask Claude Code to propose a minimal monolith. Review the proposal, then approve
the build.

Prompt:

```text
Use our approved prototype brief to propose a monolith implementation.

The browser interface, booking API, conflict rule, persistence, and confirmation
behavior should run as one small local application. Keep dependencies minimal.
Do not implement anything outside the brief.

We recommend plain HTML, CSS, and JavaScript, FastAPI, and SQLite via Python's
sqlite3 module. If you choose another stack, explain why and use it for both
prototypes.

Before writing files, show the stack, file structure, local run command, and the
five acceptance tests. Wait for approval.
```

After approval, run it and test every acceptance criterion yourself. Note where
the booking rule lives, where data is stored, and what you would monitor.

## Part 7: Prototype the Multi-Service Version

Create a second implementation using exactly the same product brief with Claude
Code. It should have at least these responsibilities:

```text
Browser frontend -> Booking API -> Booking data store
                         |
                         -> Notification component -> confirmation log or feed
```

Prompt:

```text
Use the same approved prototype brief and acceptance criteria to propose a
multi-service implementation.

Separate the frontend, booking API, and notification component. The booking API
owns booking data and conflict rules. The notification component may receive a
local HTTP call or a simple local event and write a confirmation log or feed in
its own SQLite database. It must not read or write the booking database directly.

We recommend plain HTML, CSS, and JavaScript, FastAPI for both APIs, and SQLite
via Python's sqlite3 module. If you choose another stack, explain why and use it
for both prototypes.

Do not add cloud infrastructure, authentication, email providers, or a message
broker. Before writing files, show the component map, data ownership, API or
event contract, local run commands, and acceptance tests. Wait for approval.
```

Run it and apply the same five acceptance tests. Test one extra failure case:
what does the user experience when the notification component is unavailable?

## Part 8: Compare Data Flow and Non-Functional Risks

Map one user journey through the system:

- user action
- frontend or client
- backend/API layer
- services or modules
- storage
- analytics or events
- monitoring and alerts
- failure points

Then identify risks:

| Risk area | Example question |
|---|---|
| Reliability | What happens if a dependency is unavailable? |
| Scalability | What part of the flow grows fastest with usage? |
| Performance | Where might users notice latency? |
| Data quality | Which metrics depend on correct event capture? |
| Privacy/compliance | Which data needs consent, retention, or access control? |
| AI readiness | Which data or feedback loops would AI features need? |

Complete this table from what you observed, not from generic assumptions.

| Question | Monolith | Multi-service |
|---|---|---|
| How many components must run locally? | | |
| Who owns the booking rule and booking data? | | |
| How does confirmation happen? | | |
| What changes to add cancellation notifications? | | |
| What fails when one component is unavailable? | | |
| What logs or metrics would you need first? | | |
| What is easier for Claude Code to change safely? | | |

Record the three most meaningful risks or open engineering questions directly in
your architecture brief.

## Optional: Extend the Product With Claude Code

Only start this part after both base prototypes pass all five acceptance
criteria. It is optional. Groups that are still finishing the core comparison
should not rush into it.

Choose one extension at a time. Ask Claude Code to add it to both versions,
update the database and API when needed, and propose a new acceptance test. Test
the extension in both versions before choosing another one.

Suggested extensions, from smaller to richer:

1. Cancel a booking and make the room available again.
2. Filter rooms by capacity or equipment.
3. Show a participant's upcoming bookings.
4. Add a room capacity and reject bookings above it.
5. Show a daily room-usage dashboard.
6. Add a booking status: pending, confirmed, or cancelled.
7. Add a simple activity history for bookings and cancellations.

Prompt:

```text
Both prototypes pass the base acceptance criteria. Add this one extension to
both versions: <chosen extension>.

Before editing, explain:
- the user behavior we are adding;
- which frontend, API, database, and notification changes are needed;
- one new acceptance test;
- whether the architecture trade-off changes.

Keep the existing behavior working. Do not add unrelated features. After the
change, run the old tests and the new test, then summarize the result.
```

Do not treat "more features" as automatically better. Stop when the group can
still explain what changed and why it matters architecturally.

## Part 9: Make an ADR

Use [templates/adr-template.md](templates/adr-template.md) to record one
architecture decision.

Example ADR topics:

- Start the product as a monolith rather than multi-service.
- Extract notifications only after a measurable need appears.
- Keep booking data owned by one component.
- Require the same acceptance tests for any architecture comparison.
- Let Claude Code create local prototype files while retaining approval for
  commits and external actions.

## Part 10: Final Presentation

Prepare five slides:

1. Product brief and the five acceptance criteria
2. Monolith: component map, demo, and evidence from testing
3. Multi-service version: component map, demo, and evidence from testing
4. Trade-offs, failure mode, and PM recommendation
5. Recommendation and, if completed, one optional extension

## Review Checklist

Before submitting, check:

- The two versions implement the same approved user journey.
- Both prototypes pass the same five acceptance criteria.
- The multi-service version has explicit component responsibilities and data
  ownership.
- The comparison cites observed behavior, file paths, or logs.
- The ADR captures a real trade-off and a recommendation for this product stage.
- No sensitive data was pasted into an AI tool.
- The final output is short enough to present clearly.
