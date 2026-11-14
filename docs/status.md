# Ontology's Status

## Current architecture

The first four items of the [first delivery checklist](./first-delivery-checklist.md) are implemented: shared classes and relationships, reuse decisions, identity policy, and the distinction between interactions, observation information, source records, and observed objects. The [observation model](./observation-model.md) defines the descriptive relationships and optional session context. Detailed authentication, command, protocol, artifact, and GeoIP modeling remains tracked by the subsequent checklist items.

No executable source mappings, observation datasets, analytical algorithms, federation services, or SHACL shapes are included. No competency question is claimed to have been validated against captured data.

## Naming

| Prefix | Namespace |
|---|---|
| `infra:` | `https://example.org/honeypot/infrastructure/` |
| `inter:` | `https://example.org/honeypot/interaction/` |
| `evidence:` | `https://example.org/honeypot/evidence/` |
| `enrich:` | `https://example.org/honeypot/enrichment/` |

To replace the provisional base before publication:

1. Choose the final absolute ontology base IRI and preserve the module suffixes and local term names.
2. Replace the exact string `https://example.org/honeypot` throughout the Turtle documents, catalog entries, and ontology documentation.
3. Reload the entry ontology with the updated catalog and check all imports, version IRIs, term references, and annotations.
4. Update any separately maintained queries or mappings using these namespaces.


## Initial structural verification

Checked on 14 November 2026 using RDF.rb 3.2.12 and RDF::Turtle 3.2.1 in a temporary validation environment. No runtime dependency was added to the application or ontology repository.

- Parsed all five Turtle documents: 247 local triples, 15 classes, 14 object properties, and 5 datatype properties.
- Checked catalog targets, ontology/version identities, resolution of local imports, and absence of local import cycles.
- Checked local term declarations and documentation, and verified referenced UCO/PROV terms against 12 versioned upstream ontology documents.
- Checked the local named-superclass hierarchies against retrieved explicit disjointness axioms, including UCO Event/Action and PROV Entity/Activity distinctions.
- Checked the absence of application identity keys, functional properties, forced equivalences, and minimum-cardinality constraints.
- Replaced the provisional namespace in memory, reparsed the documents, and verified preservation of their triples under the IRI substitution.
- Checked relative Markdown links.

These are targeted syntax and structural checks, not a complete OWL consistency proof. The unversioned transitive Collections Ontology import remains unresolved. No SHACL validation, source-data validation, competency-query execution, or federation demonstration was performed. The final checklist item also includes competency-question coverage and therefore remains open.

## Observation-model verification

Checked on 14 November 2026 with the same temporary RDF.rb/RDF::Turtle validation environment.

- Parsed the updated five documents: 261 local triples, 15 classes, 16 object properties, and 5 datatype properties.
- Checked the two specialized description properties, their domains and ranges, and their subproperty relationships to `evidence:describes`.
- Checked that observation information retains entity semantics and does not inherit observing-activity semantics, and that source records are not automatically typed as observations or interactions.
- Checked that supporting-record relationships are not description subproperties, that session properties retain distinct domains, and that no session restrictions or property chains introduce required or propagated context.
- Rechecked local import resolution, external term declarations, named-superclass disjointness, namespace substitution, and relative documentation links.

These checks operate on ontology structure and introduce no observation dataset. The import-closure and full-reasoning limits described above are unchanged.
