# Architecture Snapshot: LinkedIn

**Company and core product**
LinkedIn is a professional network and B2B platform. Member features include the feed, profiles, jobs, and messaging. Analytics features include "Who's Viewed Your Profile", ads reporting, and A/B testing.

**Sources used**
- [A Brief History of Scaling LinkedIn](https://engineering.linkedin.com/architecture/brief-history-scaling-linkedin) (2015, partly verified)
- [Kafka Ecosystem at LinkedIn](https://www.linkedin.com/blog/engineering/open-source/kafka-ecosystem-at-linkedin) (2016)
- [Open Sourcing Venice](https://www.linkedin.com/blog/engineering/open-source/open-sourcing-venice-linkedin-s-derived-data-platform) (2022)
- [Real-time Analytics at Massive Scale with Pinot](https://engineering.linkedin.com/analytics/real-time-analytics-massive-scale-pinot) (2014)

**Inferred tech stack**
- **Known:** Kafka with Avro and a schema registry, Venice (derived data), Pinot (real-time analytics), Hadoop and Gobblin (batch), Apache Helix, and Samza.
- **Likely (snippets only):** Espresso as the main data store and Rest.li as the service API framework.

**Architecture style and confidence level**
- **Known:** LinkedIn started as the monolith Leo. The member graph was split out as its first service.
- **Likely:** The architecture today is service-oriented and event-driven, with Kafka as the backbone.
- **Unknown:** Current service count and ownership model.

**Data flow hypothesis**
```text
Member action -> services (Rest.li) -> source-of-truth DB (Espresso)
                                    -> Kafka events (Avro)
Kafka -> Venice: derived data and AI features (async, eventually consistent)
Kafka -> Pinot: real-time analytics (+ Hadoop batch backfill)
```

**Non-functional priorities**
- Throughput: 1.4T Kafka messages/day, and Venice ingests about 14 GB/s on average.
- Latency: Pinot answers in tens of milliseconds.
- Eventual consistency, chosen on purpose to allow high write throughput.
- Reliability: audit trails detect data loss, and Burrow monitors consumer lag.

**Product trade-offs**
- Eventual consistency gives scale, but scores and counts can be briefly stale.
- Venice accepts async writes only, so a feature can't show a derived result instantly after an action.
- Many specialized systems fit each use case, but operations get complex.
- Services let teams release independently, but add cross-team dependencies.

**PM role in this environment**
- Decide per feature whether strong or eventual consistency is needed.
- Treat event schemas as shared contracts, because changes affect analytics and AI features.
- Set data-freshness requirements for AI features.
- Include cross-team dependencies when scoping.

**Open questions for engineering**
1. Who governs event schemas, and how are breaking changes handled?
2. Which features tolerate stale Venice data, and which don't?
3. Is Espresso still the main source-of-truth store?
4. How much of the 2014–2016 architecture still applies?

*Caveat: three of four sources are from 2014–2016. The Rest.li, Espresso, and Leo-migration claims come from search snippets or a partial article, so they are labeled Likely.*
