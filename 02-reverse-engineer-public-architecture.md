# Reverse-Engineer Public Architecture

The original Notion activity asks groups to investigate a real company's public
engineering information and infer its architecture. This module keeps that
activity, but makes the research method more explicit and more useful for AI PM
work.

![A practitioner connects public engineering clues to an architecture map](assets/architecture-research-workflow.png)

*Architecture research combines public sources, visible system signals, and
careful inference.*

## Research Goal

You are not trying to discover private implementation details. You are building
a reasoned public hypothesis:

> Based on public evidence, this is probably how the system is shaped, what
> trade-offs it creates, and what a PM should care about.

## Good Public Sources

Use at least three sources. Prefer primary sources when available.

| Source type              | What it can reveal                                                                     | Reliability                                               |
| ------------------------ | -------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Engineering blog         | Architecture evolution, scaling problems, incidents, data platforms, reliability work. | High when written by the company.                         |
| Public documentation     | APIs, integrations, data model concepts, platform boundaries.                          | High for current public surfaces.                         |
| Open-source repositories | Languages, frameworks, modules, contribution patterns.                                 | High for open components, incomplete for private systems. |
| Job descriptions         | Technology keywords, team boundaries, current hiring priorities.                       | Medium; may be aspirational or broad.                     |
| Conference talks         | Architecture decisions, migration stories, operating model.                            | Medium to high, depending on date.                        |
| Third-party articles     | Context and summaries.                                                                 | Medium to low unless they cite primary sources.           |

## Suggested Companies

Pick one company from the table or choose another company with enough public
technical material.

| Company  | Product type              | Useful starting point                                                           |
| -------- | ------------------------- | ------------------------------------------------------------------------------- |
| GitLab   | SaaS development platform | [GitLab Engineering Handbook](https://handbook.gitlab.com/handbook/engineering/) |
| Slack    | Collaboration SaaS        | [Slack Engineering](https://slack.engineering/)                                  |
| Shopify  | Commerce platform         | [Shopify Engineering](https://shopify.engineering/)                              |
| Airbnb   | Marketplace               | [Airbnb Tech Blog](https://airbnb.tech/)                                         |
| Spotify  | Streaming and media       | [Spotify Engineering](https://engineering.atspotify.com/)                        |
| Netflix  | Media platform            | [Netflix Technology Blog](https://netflixtechblog.com/)                          |
| Stripe   | Fintech and APIs          | [Stripe Engineering](https://stripe.com/blog/engineering)                        |
| Figma    | Collaboration design tool | [Figma Engineering](https://www.figma.com/blog/engineering/)                     |
| LinkedIn | Social and B2B platform   | [LinkedIn Engineering](https://engineering.linkedin.com/)                        |

## Evidence Matrix

Use this matrix while researching.

| Question                                     | Evidence to collect                                                        | PM interpretation                                        |
| -------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| What is the core product experience?         | Product pages, docs, API docs, user workflows.                             | Which user outcomes must the architecture protect?       |
| What are the main components?                | Blog posts, diagrams, docs, repositories.                                  | Which teams or services may become dependencies?         |
| What data is created and where does it flow? | Event posts, analytics posts, API docs, data platform notes.               | Which metrics, privacy risks, or AI opportunities exist? |
| What architecture style is likely?           | Mentions of monolith, services, events, queues, functions, data pipelines. | What trade-offs affect delivery and reliability?         |
| What quality attributes matter most?         | Reliability posts, incident posts, scale posts, compliance docs.           | What should be in acceptance criteria and launch plans?  |

## Responsible Inference

Do not overclaim. Use confidence language:

- **Known:** directly stated by a primary source.
- **Likely:** supported by several signals.
- **Possible:** reasonable, but needs validation.
- **Unknown:** not visible from public material.

Example:

> Known: the company describes using event streaming for analytics. Likely:
> product metrics depend on asynchronous pipelines. Unknown: the exact internal
> ownership model for event schema governance.

## AI Research Prompts

Use AI to speed up research, then verify sources manually.

```text
Summarize the public architecture signals for <company>.
Use only public sources. Separate known facts from likely inferences.
Return:
1. core product experience
2. likely tech stack
3. likely architecture style
4. data flow hypothesis
5. reliability/scalability concerns
6. PM implications
7. source URLs for every claim
```

```text
Review this architecture hypothesis for weak evidence or overclaiming.
Mark each claim as Known, Likely, Possible, or Unknown.
Suggest what source would strengthen the weak claims.
```

## Output: Architecture Snapshot

Create a one-page architecture snapshot before making slides:

- Company and core product
- Sources used
- Inferred tech stack
- Architecture style and confidence level
- Data flow hypothesis
- Non-functional priorities
- Product trade-offs
- PM role in this environment
- Open questions for engineering

## Check Your Understanding

Why should you separate known facts from inferences?

<details>
<summary>Show answer</summary>

Because public research is incomplete. Separating facts from inferences keeps
the work honest, makes the brief more useful for engineering review, and reduces
the risk of presenting speculation as truth.

</details>
