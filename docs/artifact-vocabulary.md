# Artifact Vocabulary

## Classes and interpretation

[evidence.ttl](../ontology/evidence.ttl) adds five classes and eight properties. Reports remain informational PROV entities; retained material remains separate from the report and any independently identified action.

| Class | Superclass(es) | Meaning |
|---|---|---|
| `evidence:FileTransferObservation` | `evidence:EventObservation` | Transfer or attempted transfer, including reported failure. |
| `evidence:FileCaptureObservation` | `evidence:EventObservation` | Report concerning captured file contents, regardless of origin. |
| `evidence:TerminalRecordingObservation` | `evidence:EventObservation` | Recording state or characteristics. |
| `evidence:CapturedFile` | `evidence:CapturedArtifact`, UCO `observable:File` | Retained material represented as a file. |
| `evidence:TerminalRecording` | `evidence:CapturedArtifact` | Retained terminal recording, independent of storage format. |

A report can have several applicable types. A failed retrieval can have a URL without an artifact; redirected command output can produce an artifact without network transfer. None of these types implies another report, successful transfer, malware, or an independently identified action. Fields and session membership remain optional.

Use existing description, supporting-artifact, source-record, deployment, outcome, and duration properties. Description/support do not imply generation; use PROV generation/usage only for known processes, following the [observation model](./observation-model.md). Recording duration does not automatically equal session duration.

## Properties

All eight properties have domain `evidence:Observation`: one object property and seven datatype properties. No keys, cardinalities, or closed value lists are added.

| Property | Range | Meaning |
|---|---|---|
| `evidence:requestedURL` | UCO `observable:URL` | Requested resource, without asserting response or content origin. |
| `evidence:sourcePath` | `xsd:string` | Reported source-side path in documented endpoint context. |
| `evidence:targetPath` | `xsd:string` | Reported destination, including an emulated path. |
| `evidence:transferDirection` | `xsd:string` | Direction relative to the honeypot, when justified. |
| `evidence:captureMethod` | `xsd:string` | Documented mechanism, such as redirection or a transfer mechanism. |
| `evidence:reportedCaptureSource` | `xsd:string` | Original source description, separate from normalized fields. |
| `evidence:artifactState` | `xsd:string` | State at the report, such as open or finalized. |
| `evidence:reportedDuplicate` | `xsd:boolean` | Source-supplied duplicate flag; absence does not mean false. |

## Direct UCO reuse

| Characteristic | Representation |
|---|---|
| Stored file | `observable:FileFacet` via `core:hasFacet`, with `observable:filePath` and known `observable:fileName`. A file-backed recording can additionally be typed `evidence:CapturedFile`. |
| Requested URL | A separate `observable:URL` with `observable:URLFacet` and `observable:fullValue`. UCO File and URL are disjoint. |
| Content size/digest | `observable:ContentDataFacet` via `core:hasFacet`, using `observable:sizeInBytes` and singular `observable:hash` pointing to `types:Hash`. Use known `types:hashMethod` and valid hexadecimal `types:hashValue` (`xsd:hexBinary`). |

Keep retained storage paths separate from interaction paths and scope relative paths to their documented environment. Neither path equality nor matching digests establishes shared capture identity. Unknown/malformed digests remain available in source records; field names or lengths alone do not establish algorithms. Size describes the documented content or stored representation, which may differ under compression. No bytes must be embedded or decoded in RDF, and a report does not prove continued artifact availability.