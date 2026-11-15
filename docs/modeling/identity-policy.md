# Identity and Duplicate Handling

## Scope

This policy defines the meaning and scope of identifiers before source mappings are implemented. It applies to any honeypot implementation. It does not execute ingestion, reconcile historical records, or claim that JSON and SQL occurrences can always be matched.

Vocabulary IRIs identify classes and properties. Instance IRIs identify installations, records, observations, and other resources. Changing the provisional vocabulary namespace must not rewrite already assigned instance IRIs. The publication convention applies to named instances of local or reused classes; existing external resource IRIs can be reused without reminting them.

## Resource identity

| Resource | Identity policy | Insufficient evidence |
|---|---|---|
| Deployment | Assign a persistent installation IRI under a controlled publication domain and retain its registry association. Preserve it across restarts or machine changes that retain installation continuity; assign a new identity when that continuity is intentionally broken. | A bare domain/hostname, sensor label, public IP, software name, or unverified producer UUID alone. |
| Source dataset version | Identify a particular dataset version or immutable capture segment and preserve that identity across copies. Record its deployment associations separately. | A mutable path, database name, or export filename alone. |
| Source record | Identify the record within its dataset version using a documented locator and preserve the identifier on repeated processing. | A row key without table/source scope, or a timestamp/event-type combination. |
| Observation information | Assign an identifier to an informational account. Reuse it only when processing the same account under the same interpretation; version changed interpretations. | Shared values or simultaneous timestamps alone. |
| Interaction | Assign an identity when the occurrence can be distinguished using source evidence. Retain multiple records supporting it where justified. | Treating each representation or matching command string as a unique physical occurrence. |
| Session | Scope the source-native session identifier by deployment and the producer's identifier lifecycle. Document collisions or uncertain lifecycle boundaries. | A session string alone, even if it is a primary key in one database. |
| Captured artifact | Identify a retained artifact or capture occurrence separately from its content digest and local storage path. | Equal digests alone do not prove the same capture or storage occurrence. |
| Derived information | Identify the result separately from its inputs; preserve the method/version context and issue a new identity for changed results. | Equal labels or overlapping inputs alone. |

No OWL key, functional property, inverse-functional property, or automatic `owl:sameAs` assertion implements these policies. They are publishing and ingestion responsibilities. The ontology preserves the relevant descriptions and relationships without inferring identity from nonunique values.

## Publication identifiers

Use persistent HTTP(S) instance IRIs under a domain controlled by the publisher, normally HTTPS. This can be the honeypot's domain or a shared publication domain serving several installations. `infra:HoneypotDeployment` identifies an installation, not the domain itself or necessarily a physical machine. Assign each installation a stable path; do not reuse it for an unrelated installation later.

Use UUID-based path identifiers for newly named resources originating from that installation, including dataset versions, records, observations, sessions, interactions, artifacts, and derived information when individually identified. The following are complete illustrative identifiers, not an observation dataset or an active publication service:

| Resource | Example instance IRI |
|---|---|
| Installation | `https://data.example.org/deployments/hp-01` |
| Dataset version | `https://data.example.org/deployments/hp-01/datasets/bd644b3c-ea16-46b3-b998-0becc79e8d26` |
| Observation | `https://data.example.org/deployments/hp-01/observations/550e8400-e29b-41d4-a716-446655440000` |

Paths distinguish resource kinds, while separate publication namespaces distinguish full IRIs even when local UUID strings coincide. UUID generation and registry management must still avoid collisions within a namespace. The ontology does not infer origin from paths: assert `evidence:observedAtDeployment`, `evidence:sourceDeployment`, `inter:sessionAtDeployment`, or other appropriate relationships. A dataset version and its originating installation always retain separate identities. Combined datasets or results with several origins can use a publisher-level path without inventing a single originating deployment.

Following the [Linked Data principles](https://www.w3.org/DesignIssues/LinkedData.html), published HTTP(S) IRIs must allow clients to retrieve useful RDF descriptions. Having a domain in an IRI or exposing a SPARQL endpoint alone does not establish dereferenceability. The serving mechanism remains a publication responsibility; no service or final domain is configured in this delivery.

Retain source/identity lifecycle associations in a publisher-managed registry. The optional `infra:deploymentIdentifier` literal stores the registered installation identifier; descriptive source labels can use `core:name`. These values are not OWL keys. The SQL-to-RDF or other mapping/publication layer assigns instance IRIs, whether RDF is materialized or virtual. Federated queries use those identities rather than generating fresh identifiers.

## Stable generation and local tests

Generate and retain a UUID for each newly identified source dataset version. For records with a stable locator in that immutable version, a publisher may derive a UUIDv5 using the retained dataset UUID as namespace and the canonical locator as name, then embed the result in the record's HTTP(S) IRI. The UUID namespace is distinct from the HTTP publication namespace. Otherwise, assign a UUID once and persist the association; never generate a fresh UUID for the same account on every read or query.

A deterministic observation identifier may similarly be scoped to an identified source record and a versioned mapping rule plus a stable output discriminator. This identifies an informational representation, not a globally reconciled occurrence. A mapping that changes an interpretation must not silently reuse the old observation identity. When one account combines multiple records, assign or resolve its identity explicitly rather than selecting an arbitrary supporting record as its identity key.

For isolated local tests without a publication domain, use persistent UUID URNs, for example `urn:uuid:550e8400-e29b-41d4-a716-446655440000`. The `urn:uuid:` prefix is literal. These are valid RDF identifiers, but the URNs alone do not provide HTTP lookup. This is the local-test convention, not the publication identifier convention. Keep their assignments stable within the test environment.

No UUID generator, registry, mapping engine, or HTTP publication mechanism is implemented in this delivery. Instance-IRI syntax is a publication policy, not an OWL class restriction.

## Publication migration

When promoting local test resources to HTTP(S) publication, retain an explicit registry mapping from each old URN to its new public IRI after verifying resource continuity. Do not equate resources merely because their UUID suffixes match. An `owl:sameAs` assertion is appropriate only when exact identity has been established; generation, derivation, or revised interpretation is not identity.

A vocabulary namespace change is separate and must not alter instance IRIs. Moving data or changing a honeypot's machine address should preserve its established public IRIs where publication continuity can be maintained. If a publication domain must change, document a controlled IRI migration and retain mappings and resolvable aliases/redirects where possible. Do not silently rename resources during ingestion or query execution.

## Locator requirements

Store the documented canonical locator in `evidence:recordLocator`, with its scope supplied by `evidence:inSourceDataset`. Retain a source-native key in `evidence:localIdentifier` when present; that literal does not replace the full locator.

- For a relational snapshot, include schema, table, typed primary-key components, and any record-version discriminator required by that snapshot. Composite keys must preserve component order and type.
- For an immutable log segment, use an exact byte offset or a documented line-number convention within that segment. Paths and rotated filenames are location metadata, not the segment identity.
- For a stream, use its immutable partition/epoch and stable message offset, where supplied.
- Use an unambiguous, versioned encoding. Delimiter-based concatenation of unescaped values is insufficient. If UUIDv5 is used, the locator's exact UTF-8 bytes are part of the rule.
- Do not silently trim, case-fold, Unicode-normalize, strip NULs, or otherwise transform identifier components. Document any required transformation and its collision implications.

SQL rows may change as a session accumulates metadata. Identify each exported dataset version explicitly; a row in a later snapshot is a separately versioned source record. A known stable logical-row identity can be maintained in an external registry. Cross-version correspondence must not be invented from identical values.

## Duplicate and correspondence cases

| Case | Treatment |
|---|---|
| Same source record processed again | Reuse the source-record identity and unchanged observation identities; repeated ingestion must not create extra representations of the same account. |
| Same immutable source dataset copied or renamed | Preserve dataset and record identities when continuity is verified; retain the additional location separately. |
| Same content at different source locators | Keep distinct record identities. Equal record bytes may legitimately occur more than once. |
| JSON and SQL proven to describe the same occurrence | Keep both record identities. An identified interaction may be shared by their observation descriptions if the correspondence is justified. |
| JSON/SQL correspondence uncertain | Keep separate descriptions and document uncertainty. Do not assert `owl:sameAs` from session, time, type, or content similarity alone. |
| Importer reinserts an already captured event as a new SQL row | Preserve the distinct SQL records. Deduplicate occurrence counts only if evidence establishes the underlying correspondence. |
| Matching native keys across deployments | Keep identities separate through deployment/source scope. |
| Matching file hashes across captures | Record shared content characteristics when modeled; retain distinct artifact/capture identities and do not infer common authorship. |

One record may describe several interactions, and several records may support one interaction. A source record and the interaction it describes must never be equated merely to simplify counting.
