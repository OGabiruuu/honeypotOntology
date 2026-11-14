# honeypotOntology

An application ontology for integrating collected data, observations and analyses from independently operated honeypots using Semantic Web standards and Linked Data principles.

The ontology's vocabulary is expressed in OWL using Turtle and organized into four implementation-independent vocabularies. It reuses UCO 1.5.0 and PROV-O (30 April 2013). The current namespace (`https://example.org/honeypot`) is provisional.

### Usage and therms guide

- [Requirements and objectives](./docs/orsd.md)
- [Module structure, term inventory, and namespaces](./docs/architecture.md)
- [UCO and PROV-O reuse decisions](./docs/vocabulary-reuse.md)
- [Event, authentication, command, client, and protocol vocabulary](./docs/interaction-vocabulary.md)
- [Interactions, observations, source records, and observed objects](./docs/observation-model.md)
- [Identifiers, duplicate handling, and identity limits](./docs/identity-policy.md)
- [Ontology entry point](./ontology/honeypot.ttl) and [local import catalog](./ontology/catalog-v001.xml)

This draft establishes the shared structure; it does not include executable source mappings, observation datasets, federation services, or SHACL validation. Detailed domain coverage remains tracked in the checklist.
