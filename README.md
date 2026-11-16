# honeypotOntology

An application ontology for integrating collected data, observations and analyses from independently operated honeypots using Semantic Web standards and Linked Data principles.

The ontology's vocabulary is expressed in OWL using Turtle and organized into four implementation-independent vocabularies. It reuses UCO 1.5.0 and PROV-O (30 April 2013). The current namespace (`https://example.org/honeypot`) is provisional.


### Usage and therms guide

- [Requirements and objectives](./docs/modeling/orsd.md)
- [Module structure, term inventory, and namespaces](./docs/modeling/architecture.md)
- [UCO and PROV-O reuse decisions](./docs/modeling/vocabulary-reuse.md)
- [Interactions, observations, source records, and observed objects](./docs/guides/observation-model.md)
- [Traceability to deployments, source records, and enrichment sources](./docs/guides/traceability.md)
- [Identifiers, duplicate handling, and identity limits](./docs/modeling/identity-policy.md)
- [Event, authentication, command, client, and protocol vocabulary](./docs/guides/interaction-vocabulary.md)
- [Transfers, captured files, and terminal recordings](./docs/guides/artifact-vocabulary.md)
- [Country/ASN enrichments, sources, and lookup times](./docs/guides/geoip-vocabulary.md)
- [Ontology entry point](./ontology/honeypot.ttl) and [local import catalog](./ontology/catalog-v001.xml)

This draft establishes the shared structure; it does not include executable source mappings, observation datasets, federation services, or SHACL validation. Detailed domain coverage remains tracked in the checklist.

### How to implement at your honeypot

Published ontology-compeling honeypot instances use persistent HTTP(S) IRIs under a controlled publication domain, with UUID-based paths for named resources originating from each installation. Isolated local tests can use `urn:uuid:...`. Instance identity, vocabulary namespaces, and domain migration are distinguished in the [identity policy](./docs/modeling/identity-policy.md)
