# Modular Ontology Structure

## Documents and dependencies

The [entry ontology](../ontology/honeypot.ttl) imports four vocabularies. Its role is composition; it introduces no additional domain classes.

| Vocabulary | Document | Local dependencies | Responsibility |
|---|---|---|---|
| Infrastructure | [infrastructure.ttl](../ontology/infrastructure.ttl) | None | Deployment identity, software components, and presented environment descriptions. |
| Observable interactions | [interaction.ttl](../ontology/interaction.ttl) | Infrastructure | Described actions involving a honeypot and optional session contexts. |
| Evidence and observations | [evidence.ttl](../ontology/evidence.ttl) | Infrastructure, interactions | Observation information, source records, retained material, and observation/transformation processes. |
| Enrichment and analysis | [enrichment.ttl](../ontology/enrichment.ttl) | Evidence and its dependencies | Derived information and the activities that produce it. |

The dependency direction is acyclic. Infrastructure and interactions do not depend on observation records or analytical results. A consumer may load only the lower-level vocabularies it needs; the entry ontology loads all four.

The [XML catalog](../ontology/catalog-v001.xml) resolves local ontology and version IRIs to their Turtle documents. Use it with a catalog-aware ontology loader, or explicitly load the documents with the same IRI mappings. A plain Turtle parser does not automatically apply catalogs or follow imports. The provisional namespace is not a hosted ontology service.

Direct external dependencies are versioned OWL imports. Their versions, semantics, and transitive-dependency limits are documented in [Vocabulary Reuse](./vocabulary-reuse.md). Loading the full import closure requires access to those external documents or a separately maintained local cache; such a cache is not bundled here.

## Class inventory

The prefixes below abbreviate the provisional module namespaces, not source formats or software implementations.

Domain specializations and their additional properties are listed in the [interaction and protocol vocabulary](./interaction-vocabulary.md), [artifact vocabulary](./artifact-vocabulary.md), and [country/ASN enrichment vocabulary](./geoip-vocabulary.md).

| Class | Meaning and boundary |
|---|---|
| `infra:HoneypotDeployment` | An installation with its own managed identity; it need not be a physical host or PROV agent. |
| `infra:PresentedEnvironment` | An environment/persona description exposed by the installation; it does not identify the underlying host. |
| `inter:Interaction` | A digital action involving the honeypot, independently identified when evidence permits. |
| `inter:Session` | A context grouping related interactions; it need not equal one network connection. |
| `evidence:Observation` | Informational content describing an observed interaction, object, or state. |
| `evidence:ObservationActivity` | The temporal act of observing, distinct from its informational output. |
| `evidence:TransformationActivity` | A process converting or normalizing information. |
| `evidence:SourceDataset` | An identified dataset version or immutable capture segment used to locate records. |
| `evidence:SourceRecord` | A record within that version; a record may summarize multiple events or accumulated state. |
| `evidence:CapturedArtifact` | Retained digital material, independently of its capture and storage mechanisms. |
| `enrich:DerivedInformation` | Information produced through transformation, enrichment, or analysis. |
| `enrich:EnrichmentResult` | Additional sourced information about an object. |
| `enrich:AnalyticalResult` | A characterization resulting from analysis, with no implied certainty of attribution. |
| `enrich:EnrichmentActivity` | A process obtaining additional information, without automatically claiming detailed analysis. |
| `enrich:AnalysisActivity` | A detailed examination of information. |

## Property inventory

| Property | Subject → object or literal | Interpretation |
|---|---|---|
| `infra:hasSoftware` | Deployment → UCO software | A component used by the installation. |
| `infra:presentsEnvironment` | Deployment → presented environment | The advertised environment description. |
| `infra:deploymentIdentifier` | Deployment → string | Publisher-managed persistent deployment identifier. |
| `inter:atDeployment` | Interaction → deployment | Installation involved; it does not identify the performer. |
| `inter:inSession` | Interaction → session | Optional known context. |
| `inter:sessionAtDeployment` | Session → deployment | Installation providing the session namespace. |
| `inter:sessionIdentifier` | Session → string | Source-native session key. |
| `inter:sessionScope` | Session → string | Documented lifecycle or namespace interpreting the key. |
| `evidence:describes` | Observation → UCO object | The interaction or object described by the observation. |
| `evidence:describesInteraction` | Observation → interaction | A specialized description of an independently identified interaction. |
| `evidence:describesObject` | Observation → UCO digital object | A specialized description of an object; uses UCO object classes directly. |
| `evidence:observedAtDeployment` | Observation → deployment | Capture origin. |
| `evidence:supportedByRecord` | Observation → source record | Supporting evidence, without automatic derivation. |
| `evidence:hasSupportingArtifact` | Observation → captured artifact | Retained supporting material. |
| `evidence:inSourceDataset` | Source record → dataset version | Record-location scope. |
| `evidence:sourceDeployment` | Dataset version → deployment | A deployment represented by the dataset; there may be several. |
| `evidence:inSession` | Observation → session | Known context even when no interaction can be individually identified. |
| `evidence:recordLocator` | Source record → string | Documented locator within the dataset version. |
| `evidence:localIdentifier` | Source record → string | Original source key retained for traceability. |
| `enrich:enrichesObject` | Enrichment result → UCO object | The object receiving additional characterization. |
| `enrich:hasSupportingObservation` | Derived information → observation | Evidence supporting a derived description. |

Use existing UCO and PROV-O properties directly where appropriate. In particular, generation, usage, and derivation do not require application-specific synonyms.

The [observation model](./observation-model.md) explains the distinction between described subjects, supporting records, and optional session context.

## Interpretation rules

- An observation can describe several subjects and have several supporting records. A record can support several observations. Neither relation is one-to-one.
- A record does not require a separately identified interaction. This accommodates SQL summaries, state observations, and honeypots without event-level identifiers.
- Session membership is optional. No property requires protocol, database, or a Honeypot application specific data and structures.
- A known session context can be attached to observation information without creating an unsupported action or command execution.
- Specialized descriptions entail `evidence:describes`, while support and session membership remain separate relationships. Session membership is not automatically propagated between observations and their subjects.
- `inter:Interaction` specializes UCO `ObservableAction`. Other observed occurrences need not be forced into this class; the broader `evidence:describes` relationship can reference other UCO objects, including UCO events when appropriate.
- This ontology follows OWLs open word concept. Therefore, domain and range axioms only infer types; they are not completeness checks. Reusing a property on an unrelated subject can cause unintended typing, so publishers must follow the documented meanings.
- There are no application-level minimum cardinalities, functional properties, inverse-functional properties, identity keys, or equivalence assertions.
- Supporting evidence, dataset containment, and capture origin are separate from provenance derivation and PROV agent responsibility.
- A dataset containing several deployments must retain observation-level origins. Membership in the dataset alone cannot identify which deployment captured an individual observation.

## Namespaces

The table lists vocabulary namespaces for classes and properties. Published instances of ontology-compeling honeypots must use separate, persistent HTTP(S) IRIs under a controlled domain, with a stable installation path and UUID-based paths for its named resources. The domain may serve one or several installations. Local tests without a publication domain use `urn:uuid:...` identifiers. See the [identity and migration policy](./identity-policy.md); neither IRI paths nor UUID suffixes imply origin or identity automatically.

| Prefix | Namespace |
|---|---|
| `infra:` | `https://example.org/honeypot/infrastructure/` |
| `inter:` | `https://example.org/honeypot/interaction/` |
| `evidence:` | `https://example.org/honeypot/evidence/` |
| `enrich:` | `https://example.org/honeypot/enrichment/` |
