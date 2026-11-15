# Country and ASN Enrichment Vocabulary

## Independent results

[enrichment.ttl](../../ontology/enrichment.ttl) adds two informational subclasses of `enrich:EnrichmentResult`:

| Class | Meaning |
|---|---|
| `enrich:CountryEnrichmentResult` | Source-reported country code and/or name for an IP address. |
| `enrich:ASNEnrichmentResult` | Source-reported autonomous-system association and/or organization label for an IP address. |

Each result uses existing `enrich:enrichesObject` to identify its UCO IP-address subject. Results can exist independently, reference different sources/times, and coexist with other results for the same IP. They do not establish actor location, address ownership, or attribution; matching addresses do not merge results.

Reuse UCO `observable:AutonomousSystem` and `observable:AutonomousSystemFacet` via `core:hasFacet`, with integer `observable:number`. Keep descriptions scoped to results unless shared identity is justified. Organization labels remain on results, without creating verified organizations. Country fields remain reported values: document their code scheme and name language. UCO `location:SimpleAddressFacet` describes a place's address; these reports do not require asserting a place or a person's location.

## Properties

The nine properties below add two object properties and seven datatype properties. All fields, sources, and process descriptions remain optional.

| Property | Domain → range | Meaning |
|---|---|---|
| `enrich:autonomousSystem` | ASN result → UCO `AutonomousSystem` | System associated with the address by this result. |
| `enrich:lookupSource` | Enrichment result → PROV `Entity` | Identified reference dataset, service response, or other lookup source. |
| `enrich:countryCode` | Country result → `xsd:string` | Code in a documented scheme. |
| `enrich:countryName` | Country result → `xsd:string` | Source-reported country name. |
| `enrich:asnOrganizationName` | ASN result → `xsd:string` | Source-reported organization label. |
| `enrich:lookedUpAtTime` | Enrichment result → `xsd:dateTime` | Documented actual lookup time. |
| `enrich:cacheRecordedAtTime` | Enrichment result → `xsd:dateTime` | Documented cache-write/update timestamp. |
| `enrich:sourceVersion` | PROV `Entity` → `xsd:string` | Version/release label on the lookup source. |
| `enrich:providerName` | PROV `Entity` → `xsd:string` | Provider label on the lookup source. |

## Provenance and interpretation

Name source entities with `rdfs:label` or UCO `core:name`; retain known version/provider labels separately. File-backed sources may reuse UCO File. Use `evidence:SourceDataset` when an identified dataset version is established. An intermediate cache is not automatically the original lookup source. Unknown source identities, versions, providers, and release dates remain absent.

Known processes reuse `enrich:EnrichmentActivity`, PROV `used` for inputs, and `wasGeneratedBy` for results. Use `wasDerivedFrom` for justified derivation and `wasAssociatedWith` for established agent responsibility. The lookup-source relation alone asserts neither process. Known activity boundaries use PROV start/end properties; entity-generation time uses `prov:generatedAtTime`.

Lookup time, cache-write time, entity-generation time, and historical validity are distinct. A shared cache timestamp does not prove that all fields share a lookup. Independent country/ASN results preserve known differences; splitting already merged information cannot recover missing field-level provenance. No identity constraints, required sessions, or automatic derivation links are added.

See the [traceability guide](./traceability.md) for distinct paths to supporting capture observations, located cache records, and external reference sources. Matching IP subjects alone do not establish support or the deployment that performed the lookup.
