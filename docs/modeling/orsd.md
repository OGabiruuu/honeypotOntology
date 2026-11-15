# Ontology Requirements Specification Document

## Definition

### Purpose

This application ontology aims to enable semantic interoperability between distributed honeypots. It must provide a shared vocabulary for integrating and querying captured data, observations, artifacts, enrichments, and analytical results while preserving their origins and remaining independent of source schemas and honeypot implementations.

### Scope

The ontology must support the integration of different kinds of honeypots through shared concepts and extensible representations of implementation-specific capabilities. The existing Cowrie-based application and its JSON logs and PostgreSQL schema provide reference sources for eliciting and validating requirements; they do not define structural requirements for other honeypots.

The covered concepts include:

- Honeypot deployments, their identifiers, software, network exposure, and presented environment or persona, where available.
- Observed source and destination endpoints, client characteristics, and submitted credentials, without assuming an identified actor.
- Captured observations and source records, their timestamps, and recorded ordering information.
- Sessions and network interactions, including SSH and Telnet where applicable, without requiring every observation to belong to a session.
- Authentication attempts, connection establishment and closure, and outcomes reported by the honeypot.
- Submitted commands, reported outcomes, and observed actions or effects in the honeypot environment.
- Client and protocol metadata, including banners, negotiation parameters, fingerprints, client variables, terminal dimensions, and session parameters.
- Forwarding requests, captured traffic fragments, protocol errors, malformed packets, and detector-reported possible exploit attempts.
- File transfer attempts and outcomes, uploads, captured file contents, emulated destination paths, storage paths, and hashes with their algorithms.
- Terminal recordings and their available metadata, distinguished from other captured files.
- IP-related country and autonomous system (ASN) enrichments, their lookup times, and their sources where known.
- Transformations, analytical results, behavioral profiles, and evidence supporting correlations or attribution hypotheses.

Representing analytical results and hypotheses does not require the ontology itself to compute similarity, detect campaigns, or identify actors. Such results must remain distinguishable from original observations.

### Standards and reused vocabularies

- [RDF](https://www.w3.org/TR/rdf11-concepts/) and [RDFS](https://www.w3.org/TR/rdf-schema/) for graph representation and vocabulary semantics.
- [OWL 2](https://www.w3.org/TR/owl2-overview/) for the formal ontology.
- [SPARQL](https://www.w3.org/TR/sparql11-overview/) for querying and federation.
- [SHACL](https://www.w3.org/TR/shacl/) for validating published data against explicit requirements.
- [UCO — Unified Cyber Ontology](https://ontology.unifiedcyberontology.org/documentation/) for semantically appropriate cybersecurity concepts.
- [PROV-O](https://www.w3.org/TR/prov-o/) for the provenance of source records, transformations, enrichments, and analytical results.

### Users

It aims to be used by programmers, and AI Agents who want to constuct federated and semantically rich honeypots, as well as cybersecurity professionals that would like to consult them


## Requirements

### Functional

- Support integrated and federated queries across independent deployments, retaining the originating honeypot and source traceability for each returned observation.
- Support representations derived from both JSON logs and the existing PostgreSQL schema, documenting coverage differences without requiring other honeypots to use either format.
- Distinguish an observed occurrence from its source records and derived representations, so multiple representations do not automatically imply multiple occurrences.
- Preserve original event types, observed values, and available source references, and document normalization, truncation, defaults, or other transformations affecting their interpretation.
- Distinguish submitted input, reported outcomes, captured artifacts, and inferred effects. A honeypot-accepted login or detector label must not imply a confirmed external compromise.
- Preserve available event times and ordering evidence without inventing missing boundaries, causal links, or a complete chronological order.
- Represent GeoIP/ASN as sourced enrichments of observed addresses, not as verified physical locations of actors. Preserve lookup time and dataset identity or version when available.
- Represent correlations and attribution as evidence-supported hypotheses, recording their method and confidence when supplied; shared identifiers alone must not establish actor identity.

### Non-functional

- Express the ontology in OWL 2, reuse RDF/RDFS semantics, and support Linked Data identification and linking practices.
- Reuse UCO concepts whenever semantically appropriate and comply with applicable constraints. Document the adopted version and the rationale for reuse or extension.
- Reuse PROV-O for provenance and document the selected terms and their interpretation in the application domain.
- Support additional honeypot implementations without requiring changes to shared core definitions. Cowrie event codes, protocols, session structures, and database fields must not become universal prerequisites.
- Support globally unique identifiers across independent deployments, with documented identity scopes and handling of repeated ingestion and cross-source duplicates.
- Use persistent, dereferenceable HTTP(S) IRIs under controlled publication domains for named instances, with UUID-based paths for resources originating from installations. Local tests without a publication domain may use UUID URNs; document promotion/migration separately from vocabulary namespace changes. See the [identity policy](./identity-policy.md).
- Support partial observations and heterogeneous source capabilities. Missing information must not be interpreted as a negative observation or fabricated from defaults.
- Provide SHACL validation requirements, competency-query examples, and documentation in English.


### Competency questions

#### 1. Data representation and retrieval

- **CQ1:** Which authentication attempts were observed by each honeypot, including their credentials, timestamps, and outcomes?
- **CQ2:** Which recorded events, observed actions, network interactions, and artifacts are associated with a given session?
- **CQ3:** What ordering of recorded events can be established within a given session from the available timestamps and ordering evidence?
- **CQ4:** Which honeypots observed a given IP address, command, fingerprint, or file hash within a specified time interval?

#### 2. Provenance and traceability

- **CQ5:** Which honeypot deployment, original observation, and source record support a given piece of information?
- **CQ6:** Which transformations, enrichments, and analyses contributed to the derivation of a given result?
- **CQ7:** Which original observations and artifacts were used to derive a given analytical conclusion?

#### 3. Cross-honeypot correlation

- **CQ8:** Which sessions observed by different honeypots share common credentials, commands, network identifiers, or file hashes?
- **CQ9:** Which sessions across different honeypots exhibit similar sequences of observed actions according to a specified comparison method?
- **CQ10:** Which analytical results suggest that observations from different honeypots are related, and what evidence supports these associations?

#### 4. Behavioral profiling and attribution hypotheses

- **CQ11:** What behavioral characteristics and supporting observations are associated with a given hypothesized intruder profile?
- **CQ12:** Which observations support the hypothesis that different sessions originated from the same actor or automated tool, and with what confidence?

#### 5. Integrated retrieval and IP enrichment

- **CQ13:** Which observations matching specified criteria were collected across different honeypots, and which deployment and source record does each observation originate from?
- **CQ14:** Which country and ASN enrichments are associated with an observed source IP, and when and from which data source were those enrichments obtained, where recorded?
- **CQ15:** Which source records or representations refer to the same observed occurrence, and what evidence supports that correspondence?
