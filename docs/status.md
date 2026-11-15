# Ontology's Status

## Current architecture

The first ten items of the [first delivery checklist](./first-delivery-checklist.md) are complete at the ontology-structure/documentation level. The shared structure, reuse decisions, identity policy, and [observation model](./observation-model.md) support the [interaction vocabulary](./interaction-vocabulary.md), [artifact vocabulary](./artifact-vocabulary.md), and [GeoIP vocabulary](./geoip-vocabulary.md). Coverage includes event reports, session/network context, authentication, commands, protocol metadata, transfers/captured material, terminal recordings, and independently sourced country/ASN results.

No executable source mappings, observation datasets, analytical algorithms, federation services, or SHACL shapes are included. No competency question is claimed to have been validated against captured data.

The tenth checklist item is covered by the [traceability review](./traceability.md): existing capture/support/record paths, independent enrichment sources, justified PROV derivation/process paths, and explicitly documented incomplete-source cases. This is a structural/documentation result, not a claim of traceability validated against published records.

## Naming

| Prefix | Namespace |
|---|---|
| `infra:` | `https://example.org/honeypot/infrastructure/` |
| `inter:` | `https://example.org/honeypot/interaction/` |
| `evidence:` | `https://example.org/honeypot/evidence/` |
| `enrich:` | `https://example.org/honeypot/enrichment/` |

These are vocabulary namespaces. Published instances use persistent HTTP(S) IRIs under a controlled domain, with stable installation paths and UUID-based paths for named resources. Local tests without a publication domain can use UUID URNs. The [identity policy](./identity-policy.md) defines stable generation, explicit origin links, and migration; no final instance domain, registry, or dereferencing service has been configured.

To replace the provisional vocabulary base before publication:

1. Choose the final absolute ontology base IRI and preserve the module suffixes and local term names.
2. Replace the exact string `https://example.org/honeypot` throughout the Turtle documents, catalog entries, and ontology documentation.
3. Reload the entry ontology with the updated catalog and check all imports, version IRIs, term references, and annotations.
4. Update any separately maintained queries or mappings using these namespaces.

This vocabulary substitution must not rewrite assigned instance IRIs. Promoting local URNs or changing an instance publication domain requires the separate, documented migration process in the identity policy.


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

## Artifact and GeoIP vocabulary verification

Checked on 14 November 2026 with the same temporary RDF.rb/RDF::Turtle validation environment.

- Parsed the five documents: 857 local triples, 46 classes, 30 object properties, and 64 datatype properties.
- Added five artifact classes and eight properties, plus two country/ASN result classes and nine properties.
- Rechecked local imports/catalog targets, declarations and annotations, versioned UCO/PROV references, named-superclass disjointness, namespace substitution, and relative documentation links.
- Checked that transfer, capture, and recording reports remain informational entities without implying one another or retained material; retained artifacts do not become reports.
- Checked UCO File reuse for captured files, optional file storage for terminal recordings, and the separate URL range for requested resources.
- Checked independent country/ASN result hierarchies, direct UCO AutonomousSystem reuse, and organization labels scoped to ASN results.
- Checked distinct lookup/cache timestamp properties without automatic PROV generation-time semantics, source entities without forced derivation links, and the continued absence of identity/completeness constraints or demo instances.
- Reviewed reference coverage against the catalogue, schema, writer/importer, and GeoIP cache code. Cache timestamps and preserved older fields do not establish complete lookup history or field-level provenance.

These are syntax and targeted structural checks. Full OWL reasoning and the unresolved unversioned Collections Ontology import remain as documented above; no mappings, SHACL, source-data validation, or competency-query execution were performed.

## Source-correspondence review

The [external Honey correspondence document](../../honey-semantic-correspondence.md) was reviewed on 14 November 2026 against the catalogue, schema, direct writer, importer, and GeoIP cache implementation. Documentation checks verified relative links, 91 referenced local terms, 17 explicitly prefixed upstream terms, coverage of all 25 catalogued event types, 15 event types handled by the reviewed pipelines, and all ten SQL tables.

The review identifies incompatible command flags, lost/overwritten metadata, ingestion-history ambiguities, and normalized-field gaps for free-form session input and detailed campaign metrics. No ontology document was changed, and no application code, mapping, database query, or source-data validation was executed.

## Instance-publication policy revision

The identity policy now uses controlled-domain HTTP(S) IRIs for publication, with stable installation paths and UUID-based resource paths. UUID URNs are the convention for isolated local tests. Documentation distinguishes installation identity from machines/domains, dataset identity from deployment identity, and UUID generation namespaces from HTTP publication namespaces. Origin remains explicit in ontology relationships.

Promotion to publication or a publication-domain change requires verified continuity and an explicit old/new IRI mapping; vocabulary namespace replacement does not rename instances. The revision affects documentation only. No class/property definitions, UCO/PROV-O alignments, or OWL identity constraints were changed.

## Traceability review

The [traceability guide](./traceability.md) documents the existing paths from observations to capture deployments and located source records, from derived results to supporting observations, and from enrichment results to independent lookup sources. Known record derivations and process inputs reuse PROV-O directly, without equating evidential support with derivation or deployments with responsible agents.

Focused checks compared 16 local domain/range signatures and four pinned PROV-O signatures, verified 14 compatible typed paths, and checked local term references and 57 relative links across seven documents. File checksums confirmed that all five ontology documents and the import catalog were unchanged. The observation-model diagram was corrected to match the declared ObservableObject range of `evidence:describesObject`.

The review explicitly records that no direct support-only derived-result-to-record property exists. Without a known supporting observation or justified derivation/process, that part of the trace remains incomplete; matching subjects or IRI paths do not fill it. Query prerequisites must distinguish partial information from complete record chains. No mappings, RDF datasets, SHACL rules, endpoint discovery, or query execution were introduced, and actual data traceability has not been validated.
