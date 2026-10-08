# Final Review and Presentation

The final presentation is not a technical trivia contest. It is a product
architecture story: the same product, two working prototypes, observed
trade-offs, and a recommendation for what a PM should do next.

## Evidence Quality Review

Before presenting, review your strongest claims.

| Claim type | Good evidence | Weak evidence |
|---|---|---|
| Prototype behavior | A passing acceptance test, browser observation, API response, or log entry. | "The agent said it works." |
| Component boundary | Actual file paths, a running process list, API contract, or event payload. | A diagram with no implementation behind it. |
| Data ownership | Database schema, repository code, or a tested write path. | Assuming each service owns data because it sounds right. |
| Reliability priority | A tested failure mode and a concrete user impact. | Generic claim that reliability matters. |
| PM recommendation | A clear connection between observed delivery cost, risk, and product stage. | "Microservices are more scalable." |

## Final Artifact Checklist

Your final submission should include:

- the approved prototype brief
- a running monolith and evidence from the five acceptance tests
- a running multi-service version and evidence from the same tests
- a comparison table and three focused risks or open questions
- one ADR
- optionally, one extension implemented and tested in both versions
- a presentation outline or slide deck

## Presentation Structure

Use five slides or sections.

### 1. Product Scope and Test Contract

Answer:

- Which user problem did you choose?
- Which five acceptance criteria did both prototypes have to meet?
- Which features did you explicitly exclude to keep the comparison fair?

### 2. Monolith Prototype

Show:

- component map
- short demo of the core journey
- test result and evidence of persistence
- where the booking rule and data live

Use simple language. A PM should be able to understand the architecture without
knowing every framework.

### 3. Multi-Service Prototype

- component map and API or event contract
- short demo of the same core journey
- data ownership
- what happens when notification is unavailable

### 4. Recommendation and PM Implications

Translate architecture into product work:

- which version you would choose for the first release and why
- delivery dependencies and operational cost
- launch risks and first metrics or logs to add
- what condition would justify moving from one architecture to the other

### 5. What the Comparison Taught You

Explain:

- what Claude Code created and what you verified by testing;
- which architecture you recommend for the first product release;
- what evidence would make you reconsider that choice later.

Groups that completed an optional extension can also show what it changed in the
frontend, API, database, and multi-service boundary. This is extra evidence,
not a requirement for a strong presentation.

The goal is not to write every line manually. It is to use Claude Code to
produce something testable, then make a recommendation grounded in observed
behavior.

## Example Speaker Notes

```text
We chose a room-booking tool and used identical acceptance tests for both
versions. The monolith was faster to run and easier to change because the
booking rule, data store, and confirmation behavior lived in one application.
The multi-service version separated notification work, but introduced an API or
event contract and an additional failure mode. For a small first release, we
recommend the monolith. We would reconsider extraction when notification volume,
independent ownership, or reliability requirements become measurable.
```

## Peer Review

Use this checklist when another group presents:

| Question | Notes |
|---|---|
| Was the same product and test contract used twice? | |
| Did both demos show the core user journey? | |
| Were component boundaries and data ownership clear? | |
| Did they show a real failure mode or operational trade-off? | |
| Did the PM recommendation match the evidence? | |
| Did the group test the generated work rather than trust it blindly? | |

## Check Your Understanding

What is the strongest sign that a group used AI well in this activity?

<details>
<summary>Show answer</summary>

The strongest sign is not a polished deck. It is a clear trail of judgment: a
bounded brief, identical acceptance tests, observed prototype behavior, a
defensible recommendation, and evidence that the group tested the generated
work instead of simply trusting it.

</details>
