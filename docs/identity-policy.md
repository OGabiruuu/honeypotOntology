# Identity and Duplicate Handling

## Scope

This policy defines the meaning and scope of identifiers before source mappings are implemented. It applies to any honeypot implementation. It does not execute ingestion, reconcile historical records, or claim that JSON and SQL occurrences can always be matched.

Vocabulary IRIs identify concepts. Instance IRIs identify installations, records, observations, and other resources. Changing the provisional vocabulary namespace must not change instance identity.

## Resource identity

| Resource | Identity policy | Insufficient evidence |
|---|---|---|
| Deployment | Assign and persist a globally scoped identifier in a publisher-managed registry. Preserve it across restarts that retain installation continuity; assign a new identity when that continuity is intentionally broken. | Sensor labels, public IPs, hostnames, software names, or an unverified producer UUID. |
| Source dataset version | Identify a particular dataset version or immutable capture segment and preserve that identity across copies. Record its deployment associations separately. | A mutable path, database name, or export filename alone. |
| Source record | Identify the record within its dataset version using a documented locator and preserve the identifier on repeated processing. | A row key without table/source scope, or a timestamp/event-type combination. |
| Observation information | Assign an identifier to an informational account. Reuse it only when processing the same account under the same interpretation; version changed interpretations. | Shared values or simultaneous timestamps alone. |
| Interaction | Assign an identity when the occurrence can be distinguished using source evidence. Retain multiple records supporting it where justified. | Treating each representation or matching command string as a unique physical occurrence. |
| Session | Scope the source-native session identifier by deployment and the producer's identifier lifecycle. Document collisions or uncertain lifecycle boundaries. | A session string alone, even if it is a primary key in one database. |
| Captured artifact | Identify a retained artifact or capture occurrence separately from its content digest and local storage path. | Equal digests alone do not prove the same capture or storage occurrence. |
| Derived information | Identify the result separately from its inputs; preserve the method/version context and issue a new identity for changed results. | Equal labels or overlapping inputs alone. |

No OWL key, functional property, inverse-functional property, or automatic `owl:sameAs` assertion implements these policies. They are publishing and ingestion responsibilities. The ontology preserves the relevant descriptions and relationships without inferring identity from nonunique values.

## Identifier convention

Use persistent UUID-based instance IRIs of the form `urn:uuid:{uuid}` as the reference convention. The braces are placeholders, not literal IRI characters. Generate and store a UUID for each newly identified deployment and source dataset version. Keep registry associations with source descriptions and identity lifecycle decisions. The optional `infra:deploymentIdentifier` literal records the registered deployment identifier; source labels can use existing descriptive vocabulary such as `core:name`.

For records that have a stable locator in an identified immutable dataset version, a publisher may use UUIDv5 with that dataset UUID as the namespace and a canonical locator string as the name. Otherwise, assign a UUID once and persist the association in the registry. Do not generate a fresh random identifier each time the same record is read. UUID-based identity depends on correct generation and registry management; the ontology does not mathematically guarantee collision-free identifiers.

A deterministic observation identifier may similarly be scoped to an identified source record and a versioned mapping rule plus a stable output discriminator. This identifies an informational representation, not a globally reconciled occurrence. A mapping that changes an interpretation must not silently reuse the old observation identity. When one account combines multiple records, assign or resolve its identity explicitly rather than selecting an arbitrary supporting record as its identity key.

No UUID generator or mapping engine is prescribed or implemented in this delivery. The distinction between resource identity, source-local keys, and occurrence correspondence applies equally to other persistent IRI schemes.

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