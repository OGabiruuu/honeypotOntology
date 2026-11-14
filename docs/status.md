# Ontology's Status

## Current architecture

The first six items of the [first delivery checklist](./first-delivery-checklist.md) are implemented. The shared structure, reuse decisions, identity policy, and [observation model](./observation-model.md) now support the [interaction vocabulary](./interaction-vocabulary.md): captured event reports, session/network context, authentication, command submissions and outcomes, client attributes, ordered protocol parameters, fingerprints, forwarding, errors, and detector labels. File-transfer/recording artifacts and GeoIP remain tracked by the subsequent checklist items.

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

## Interaction and protocol vocabulary verification

Checked on 14 November 2026 with the same temporary RDF.rb/RDF::Turtle validation environment.

- Parsed the five documents: 718 local triples, 39 classes, 27 object properties, and 50 datatype properties.
- Rechecked local imports/catalog resolution, documented local terms, references to versioned UCO/PROV declarations, and named-superclass disjointness.
- Checked that all report specializations retain informational entity semantics, while the optional interaction specializations remain UCO observable actions.
- Checked that command outcomes do not imply submission reports, credential-change reports do not require a command interface, and public keys do not imply a login/password credential pair.
- Checked that client-variable descriptors retain the UCO EnvironmentVariable range without inheriting the incompatible ObservableObject description range.
- Checked that source-reported outcomes do not imply actual action status and that ordered parameter values retain integer positions without identity constraints on repeated values.
- Checked that durations can retain fractional seconds, that source/report vocabularies remain open, and that no observation/demo instances or required session context were introduced.
- Rechecked namespace substitution and relative documentation links. Reviewed the field-level reference-source coverage documented in the interaction vocabulary.

No mappings or competency queries were executed. Full OWL reasoning, SHACL, complete transitive-import resolution, and source-data validation remain outside these checks.
