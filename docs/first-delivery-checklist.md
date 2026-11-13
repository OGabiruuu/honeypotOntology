# First Delivery Checklist

Implementation checklist for the [ORSD](./orsd.md). Check items as they are completed and validated.

- [ ] Define shared concepts and document UCO reuse and PROV-O provenance, without requiring Cowrie-specific structures.
- [ ] Define deployment, observation, and source-record identifiers; document duplicate handling and identity limits.
- [ ] Represent captured events, available session and network context, authentication, commands, and reported outcomes.
- [ ] Represent available client/protocol metadata, fingerprints, forwarding observations, errors, and detector labels.
- [ ] Represent file transfers and failures, captured contents, terminal recordings, paths, and hash algorithms.
- [ ] Represent country/ASN enrichments with available lookup times and source metadata.
- [ ] Document JSON and PostgreSQL mappings, coverage differences, transformations, and unavailable information.
- [ ] Preserve traceability from represented observations and enrichments to deployments and source records.
- [ ] Provide SPARQL examples for CQ1–CQ6, CQ8, and CQ13–CQ15, within available evidence.
- [ ] Validate integration and federation across at least two deployments, returning origins and testing local identifier collisions and duplicate handling.
