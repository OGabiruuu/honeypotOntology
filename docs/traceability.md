# Observation and Enrichment Traceability

## Scope

This guide reviews the existing [evidence](../ontology/evidence.ttl), [interaction](../ontology/interaction.ttl), and [enrichment](../ontology/enrichment.ttl) relationships. Endpoint discovery and federation execution are separate publication concerns.

## Capture and source-record paths

| Relationship | Subject → object | Interpretation |
|---|---|---|
| `evidence:observedAtDeployment` | Observation → deployment | Explicit capture origin. |
| `evidence:supportedByRecord` | Observation → source record | Record supporting the account; not automatically derivation. |
| `evidence:inSourceDataset` | Source record → source dataset version | Scope in which the record is located. |
| `evidence:recordLocator` | Source record → string | Canonical location within that identified dataset version. |
| `evidence:sourceDeployment` | Source dataset → deployment | A deployment represented in the dataset, not necessarily the origin of every record. |
| `evidence:describesInteraction` | Observation → interaction | Known action described by the account. |
| `inter:atDeployment` | Interaction → deployment | Deployment involved in the action; separate from capture origin. |

For an observation with known capture origin and source support, publish its deployment link and supporting records, each with its dataset version and documented locator. Preserve multiple supports rather than arbitrarily selecting one. The optional `evidence:localIdentifier` retains a source key but does not replace the scoped locator. Follow the [identity policy](./identity-policy.md).

From a deployment, consumers can search subjects of `evidence:sourceDeployment`, `evidence:observedAtDeployment`, or `inter:atDeployment`. From a dataset they can find its records and supporting observations, then the observations' described interactions. No direct dataset-to-observation or dataset-to-interaction membership property is defined. These traversals need published statements; IRI paths do not supply them.

A mixed-origin dataset requires observation-level origin information. Even a single currently listed dataset deployment is not an exhaustive origin declaration under the open-world interpretation. Dataset membership, session context, and interaction descriptions do not automatically propagate capture origin. `inter:sessionAtDeployment`, `inter:inSession`, and `evidence:inSession` retain their separate meanings.

Artifacts are traced through observations that describe them using `evidence:describesObject` or cite them using `evidence:hasSupportingArtifact`. The latter relationship does not identify the process that generated an artifact. A shared artifact or digest does not merge capture records or installations.

## Enrichment paths and PROV-O reuse

| Relationship | Subject → object | Interpretation |
|---|---|---|
| `enrich:enrichesObject` | Enrichment result → UCO object | Subject characterized, not its source or capture origin. |
| `enrich:hasSupportingObservation` | Derived information → observation | Known evidential support; continue through the capture/source-record paths above. |
| `enrich:lookupSource` | Enrichment result → PROV entity | Reference dataset, response, or other lookup source, independently of capture records. |
| `prov:wasDerivedFrom` | Result entity → source entity | Justified derivation, including from a source record when established. |
| `prov:wasGeneratedBy` and `prov:used` | Result → generating activity → input entity | Known process and its documented inputs. |

Keep three roles distinct: the installation that captured input, the reference information source, and the activity/agent performing enrichment. A lookup can support several deployments without having been executed by all of them. `prov:wasAssociatedWith` identifies an established responsible agent; a deployment is not automatically a PROV agent.

Where a result has a supporting capture observation, `enrich:hasSupportingObservation` provides a path to that observation's deployment and source records. Shared IP values or even a shared subject resource alone do not justify this support relationship. Country and ASN results retain independent sources and times, as detailed in the [GeoIP guide](./geoip-vocabulary.md).

For information represented from a cache row, retain that row as `evidence:SourceRecord` in an identified dataset version. When conversion/derivation is known, the result can use `prov:wasDerivedFrom` to that record; a known conversion can also use `evidence:TransformationActivity` with PROV generation/usage. The cache row is not automatically the original `enrich:lookupSource`. Process-level input trace does not automatically prove that every output derives from every input.

Do not apply `evidence:supportedByRecord` or `evidence:observedAtDeployment` directly to a derived result merely to fill a gap: their domains infer observation typing. The vocabulary has no direct support-only result-to-record property. If neither a supporting observation nor justified PROV derivation/process is known, that part of the result's source-record trace remains incomplete. Preserve the available facts; adding a new support relationship would require a separate modeling decision.

## Completeness boundaries

- Capture origin, located source record, reference source, generating process, and responsible agent are independent questions. A complete path for one does not establish the others.
- A standalone interaction remains OWL-valid without a report. Observations, enrichments, and sessions can also retain partial information; absent links are not negative findings or automatic validation failures.
- Timestamp equality, source labels, paths, foreign-key similarity, or shared values do not establish generation, derivation, actor identity, or cross-source occurrence identity. The [source correspondence](../../honey-semantic-correspondence.md) records Honey's unrecoverable history and cache limits.
- Consumers must distinguish direct-origin retrieval from retrieval requiring a complete dataset/record chain. Mandatory joins can exclude partial but useful observations. Query prerequisites must state the published links and entailment assumptions they need; generation and support links are not inferred from one another.
