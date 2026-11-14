# Vocabulary Reuse

## Pinned references

The application imports the **1.5.0 version IRIs** of UCO modules, while using UCO's stable term namespaces. The source reviewed is the [UCO 1.5.0 release](https://github.com/ucoProject/UCO/tree/1.5.0/ontology/uco), not an unversioned development branch.

| Dependency | Imported version IRI | Reference source |
|---|---|---|
| UCO Core | `https://ontology.unifiedcyberontology.org/uco/core/1.5.0` | [core.ttl](https://github.com/ucoProject/UCO/blob/1.5.0/ontology/uco/core/core.ttl) |
| UCO Observable | `https://ontology.unifiedcyberontology.org/uco/observable/1.5.0` | [observable.ttl](https://github.com/ucoProject/UCO/blob/1.5.0/ontology/uco/observable/observable.ttl) |
| UCO Action | `https://ontology.unifiedcyberontology.org/uco/action/1.5.0` | [action.ttl](https://github.com/ucoProject/UCO/blob/1.5.0/ontology/uco/action/action.ttl) |
| UCO Analysis | `https://ontology.unifiedcyberontology.org/uco/analysis/1.5.0` | [analysis.ttl](https://github.com/ucoProject/UCO/blob/1.5.0/ontology/uco/analysis/analysis.ttl) |
| PROV-O | `http://www.w3.org/ns/prov-o-20130430` | [30 April 2013 Recommendation](https://www.w3.org/TR/2013/REC-prov-o-20130430/) |

PROV-O term IRIs retain the namespace `http://www.w3.org/ns/prov#`. Importing a dated ontology document does not change its term IRIs.

UCO modules have their own transitive imports. Applications must resolve the versioned import closure when relying on its semantics. This repository does not copy, simplify, or redefine external terms. UCO contains SHACL shapes alongside its OWL axioms; importing that vocabulary does not mean application data has been SHACL-validated.

The transitive UCO collections wrapper, `https://ontology.unifiedcyberontology.org/co/1.5.0`, imports the unversioned Collections Ontology IRI `http://purl.org/co`. Pinning UCO's version IRIs therefore does not by itself freeze every transitive dependency. That external ontology was not retrieved in the initial structural checks. A complete reproducible import closure requires a separately managed, identified copy of it; no application term currently directly references its namespace.

## UCO alignment and extension rationale

Every relationship below is a subclass alignment, not a claim of equivalence with an entire external concept.

| Application term | Reused superclass | Rationale |
|---|---|---|
| `infra:HoneypotDeployment` | `core:UcoObject` | A managed installation identity is domain-specific and may span several digital components; it is not necessarily a device or software instance. |
| `infra:PresentedEnvironment` | `core:UcoObject` | The description distinguishes an advertised persona from the underlying infrastructure. |
| `inter:Interaction` | `observable:ObservableAction` | The described digital interaction is an action; logging or observing it is a separate process. |
| `inter:Session` | `core:ContextualCompilation` | A session supplies shared context, without equating that context with a same network transport connection. |
| `evidence:Observation` | `core:UcoObject` | The application term denotes information. UCO `Observation` instead denotes an observing action, so it is not an appropriate superclass for this result. |
| `evidence:ObservationActivity` | `observable:Observation` | This term specifically denotes the temporal act of observing. |
| `evidence:TransformationActivity` | `action:Action` | Translation and normalization are performed processes. |
| `evidence:SourceDataset` | `core:UcoObject` | A versioned record-location scope can be a file, capture segment, database snapshot, or another source representation. |
| `evidence:SourceRecord` | `core:UcoObject` | Source rows can describe accumulated state. They are not universally an event record or one event occurrence. |
| `evidence:CapturedArtifact` | `observable:ObservableObject` | Retained digital material fits the generic UCO object concept without assuming a file format or transfer direction. |
| `enrich:DerivedInformation` | `core:UcoObject` | A shared informational superclass covers enrichment and analysis without asserting that every lookup is analysis. |
| `enrich:EnrichmentResult` | Through `enrich:DerivedInformation` | Additional characterization is kept distinct from raw observation information and the object it describes. |
| `enrich:AnalyticalResult` | `analysis:AnalyticResult` | This is specifically a characterization resulting from examination. |
| `enrich:EnrichmentActivity` | `action:Action` | An enrichment may be a lookup rather than detailed examination. |
| `enrich:AnalysisActivity` | `analysis:Analysis` | This specifically represents detailed examination, following UCO's definition. |

`infra:hasSoftware` references `observable:Software` directly. No local synonym for software is introduced. Publishers can similarly reuse relevant UCO classes and facets as detailed domain modeling develops.

`evidence:describesObject` likewise uses `observable:ObservableObject` directly as its range. Being an observed object is a relational role, so a redundant application class is not introduced. `evidence:describesInteraction` instead targets the local specialization of UCO `ObservableAction`. Both specialize the general description property, without equating objects, actions, observation information, or source records. See the [observation model](./observation-model.md).

UCO 1.5.0 declares `core:Event` disjoint with `action:Action`. Therefore, `inter:Interaction`, observation activities, transformation activities, and analysis activities must not also be classified as `core:Event`. A Cowrie event-type label does not justify assigning that UCO class. There is no global equivalence between UCO actions or events and PROV activities.

Application properties are introduced for meanings absent from the selected reused properties: installation association, presented environments, optional session context, source location, and evidential support. For example, `evidence:supportedByRecord` is not a subproperty of `prov:wasDerivedFrom`: a supporting record does not prove a specific derivation.

## Interaction and protocol extensions

The [interaction vocabulary](./interaction-vocabulary.md) adds source-report specializations while preserving the established UCO/PROV boundaries:

- Connection attempts, authentication attempts, command submissions, credential-change attempts, protocol negotiations, and forwarding requests inherit `inter:Interaction` and therefore UCO `observable:ObservableAction`. These optional action resources do not assert success or require a session.
- Event, session, authentication, command, client, negotiation, forwarding, error, and detection observation classes inherit informational `evidence:Observation` and `prov:Entity`. They are not subclasses of UCO `core:Event`, `action:Action`, or the observing activity.
- Protocol fingerprints, presented public-key material, and traffic fragments specialize UCO `observable:ObservableObject`. They are distinct concepts rather than aliases for a file, a credential pair, or an actor.
- Named protocol parameters and individual ordered values specialize `core:UcoObject`. Their application-specific role preserves source parameter names, repeated values, optional ordering, and explicit empty lists without requiring one vendor's protocol schema.
- Credential-change reports are not restricted to command reports. An established command context can be represented through additional typing; other honeypot interfaces are not forced to model credential changes as shell commands.

Direct reuse includes `observable:NetworkConnection`, `observable:NetworkConnectionFacet`, appropriate IP-address classes/facets, `core:hasFacet`, `observable:src`, `observable:dst`, `observable:sourcePort`, `observable:destinationPort`, and `observable:addressValue`. These represent available network characteristics without introducing local synonyms. UCO `observable:protocols` expects a controlled dictionary; the local `evidence:protocolName` instead explicitly preserves a source-reported string.

UCO `observable:EnvironmentVariable` is an inherent characterization, not an ObservableObject. `evidence:clientVariable` points to that descriptor directly, with `core:name` and `observable:value`; it is not a specialization of `evidence:describesObject`. This respects UCO's separation of inherent characterizations and content objects.

Local report-scoped properties avoid stronger or different meanings of existing terms:

| Local representation | Reuse boundary |
|---|---|
| Presented authentication fields and public-key material | UCO `observable:Credential` specifically denotes a login/password combination; a generic authentication report need not contain such a pair or a verified account. |
| `evidence:reportedOutcome` with its scope | UCO `action:actionStatus` characterizes an action's state; an ambiguous source flag is not automatically that state. |
| `evidence:observedAtTime` | PROV `generatedAtTime` describes entity generation, not automatically the source-reported observation time. |
| `evidence:reportedDurationSeconds` | UCO `observable:duration` is defined for phone-call duration with an integer range; it is not a generic fractional observation-duration field. |
| Original event types, messages, and detector labels | These are reported metadata, not identity keys, universal class names, exploit actions, or confirmed system effects. |


## PROV-O alignment

| PROV-O superclass | Application subclasses | Interpretation |
|---|---|---|
| `prov:Entity` | Deployments, presented environment descriptions, observation information, source datasets, source records, captured artifacts, and derived information | Identifiable things or informational descriptions whose provenance can be recorded. |
| `prov:Activity` | Observation, transformation, enrichment, and analysis activities | Processes occurring over time that may use or generate entities. |

The entity and process descriptions refer to distinct resources. No class is made both a PROV entity and a PROV activity. `inter:Interaction` is not automatically a PROV activity: describing an interaction does not require a provenance-process representation of it. A publisher may provide one when appropriate and supported.

Use these existing properties directly when the corresponding facts are known:

| Property | Intended use | Evidence boundary |
|---|---|---|
| `prov:wasGeneratedBy` | Entity → process that generated it | Requires a known generation relationship, not merely a matching timestamp. |
| `prov:used` | Activity → entity used by it | Does not imply that the entity is the sole input. |
| `prov:wasDerivedFrom` | Resulting entity → source entity | Requires justified derivation; it is stronger than general evidential support. |
| `prov:hadPrimarySource` | Entity → its primary-source entity | Use only where the primary-source relationship is established. |
| `prov:generatedAtTime` | Entity → generation time | Distinct from interaction time, ingestion time, and lookup time. |
| `prov:wasAssociatedWith` | Activity → responsible agent | The agent must be represented as such; a deployment identifier alone does not establish agent responsibility. |

An actual observing process may generate both JSON and SQL records. In that case, the records can share a generation origin without either being derived from the other. Importing JSON into SQL can establish a different derivation path when that execution is known. The ontology accommodates both descriptions without selecting a source pipeline.

UCO `analysis:originatingAnalysis` may connect an analytical result to its UCO analysis activity. `prov:wasGeneratedBy` can additionally describe the known generation relationship. These external properties are not globally declared equivalent, and no new inverse or wrapper property is needed.

## Compatibility limits

- The alignments preserve the semantic difference between observations as information and observing as an activity.
- UCO facets retain their original meanings; the application does not flatten every UCO property onto every resource.
- No external class or property is given a stronger global domain, range, equivalence, or cardinality by this ontology.
- Imported SHACL rules have not been executed. Syntactic checks and structural inspection do not establish full OWL consistency or UCO shape conformance.
