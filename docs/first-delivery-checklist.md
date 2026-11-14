# First Delivery Checklist

Implementation checklist for the [ORSD](./orsd.md). Check items as they are completed and validated.

## Agreed scope

This delivery covers the ontology structure and its documentation. Executable mappings, data generation or selection, demonstration datasets, federation execution, and SHACL validation are excluded. The choice between materialized and virtual RDF remains open.

The ontology will be organized into four vocabularies:

1. Honeypot infrastructure.
2. Observable interactions.
3. Evidence and observations.
4. Enrichment and analysis.

Use UCO 1.5.0 and the [PROV-O Recommendation of 30 April 2013](https://www.w3.org/TR/2013/REC-prov-o-20130430/). Use a documented provisional namespace with stable local term names and a documented procedure for replacing its base IRI.

## Implementation

- [x] Define classes, properties, and relationships across the four vocabularies, keeping them independent of honeypot implementations. See [module structure and initial verification](./architecture.md).
- [x] Document UCO 1.5.0 reuse and PROV-O provenance, including the rationale for application-specific terms. See [vocabulary reuse](./vocabulary-reuse.md).
- [x] Define deployment, observation, and source-record identifiers; document duplicate handling and identity limits. See [identity policy](./identity-policy.md).
- [ ] Distinguish interactions, observations, source records, and observed objects; keep session membership optional.
- [ ] Represent captured events, available session and network context, authentication, commands, and reported outcomes.
- [ ] Represent available client/protocol metadata, fingerprints, forwarding observations, errors, and detector labels.
- [ ] Represent file transfers and failures, captured contents, terminal recordings, paths, and hash algorithms.
- [ ] Represent country/ASN enrichments with available lookup times and source metadata.
- [ ] Document the conceptual correspondence with JSON and PostgreSQL, coverage differences, transformations, unavailable information, and ambiguous ingestion history.
- [ ] Preserve traceability from represented observations and enrichments to deployments and source records.
- [ ] Provide SPARQL query templates for CQ1–CQ6, CQ8, and CQ13–CQ15; document prerequisites without claiming validation against data.
- [ ] Check ontology syntax, module references, and structural coverage of the selected competency questions.
