# Interaction and Protocol Vocabulary

## Scope and interpretation

[interaction.ttl](../ontology/interaction.ttl) and [evidence.ttl](../ontology/evidence.ttl) cover event reports, session/network context, authentication, commands, protocol metadata, and detections independently of source schemas.

Following the [observation model](./observation-model.md), reports are information (`evidence:Observation` / PROV `Entity`); independently identified actions use `inter:Interaction` / UCO `ObservableAction`. A log entry does not require a separate action. Fields remain optional, and source labels do not define ontology classes or resource identity.

## Modeling rules

| Area | Representation and interpretation |
|---|---|
| Events and time | Retain source labels/messages and source-reported timestamps. Observation time differs from PROV entity-generation time. Record positions are local to a dataset version; database keys and timestamps do not establish causality or globally synchronized order. |
| Sessions | Separate session summaries from lifecycle reports. Preserve available boundaries and normalize known durations to decimal seconds, documenting conversions. Missing events or exact agreement between duration and timestamps are not required. |
| Network | Reuse UCO `NetworkConnection`, `NetworkConnectionFacet`, address classes/facets, and `core:hasFacet`. Use `src`/`dst`, `sourcePort`/`destinationPort`, and `addressValue`. Link reports, sessions, and actions through their respective connection properties. Endpoint equality alone does not establish shared connection identity; preserve the capture perspective across redirection. |
| Protocol labels | `evidence:protocolName` retains a source string. UCO `observable:protocols` requires a `types:ControlledDictionary`. Protocols are not inferred from ports. |
| Authentication | Retain presented values, method/realm, and scoped outcomes. Empty and absent passwords differ. UCO `Credential` requires a login/password pair, so generic reports do not require it; public-key material is separate. |
| Commands and outcomes | Separate submission and outcome reports; preserve compound/subcommand text. Equal text, time proximity, or shared sessions do not uniquely pair them. Credential changes are independent of interface, with additional command typing when justified. Outcomes describe the honeypot's response within a documented scope, not necessarily UCO `actionStatus` or effects on a real host. Ambiguous defaults do not establish failure. |
| Client attributes | Banners are claims; terminal dimensions use characters. Reported architecture describes session context. Client variables reuse UCO `EnvironmentVariable` with `core:name` and `observable:value`; these descriptors are inherent characterizations, so they do not use `describesObject` or establish process effects. |
| Parameters | Use one `ProtocolParameter` and separate `ParameterValue` resources. Preserve known roles, directions, lexical forms, encodings, zero-based positions, and repeated entries. A known count of zero preserves an explicit empty list; absence does not. Offered values are distinct from selected values. |
| Fingerprints and keys | Preserve fingerprint kind/value and available algorithm/input separately from key type/data/encoding. HASSH, JA4, JA4H, and key fingerprints remain distinguishable. They are not file hashes or actor identities; their presence does not establish validation, ownership, or authentication acceptance. |
| Forwarding and fragments | Distinguish the reported forwarding origin from the enclosing connection. Scope channel identifiers to their capture context. Preserve supplied fragments, known encoding, and reported byte length without evaluating serialized bytes, assuming Base64, or inferring complete delivery. |
| Errors and detections | Retain messages, codes, message numbers, detector labels, vulnerability identifiers, and trigger parameters. These reports alone do not establish successful exploitation, target vulnerability, or actor attribution. |

See [vocabulary reuse](./vocabulary-reuse.md) for UCO/PROV alignment rationale.

See the [artifact vocabulary](./artifact-vocabulary.md) for transfers, captured contents, and terminal recordings, and the [GeoIP vocabulary](./geoip-vocabulary.md) for country/ASN enrichments.


## Domain class inventory

| Class | Superclass(es) | Meaning |
|---|---|---|
| `inter:ConnectionAttempt` | `inter:Interaction` | Attempt to establish network communication. |
| `inter:AuthenticationAttempt` | `inter:Interaction` | Presentation of authentication information. |
| `inter:CommandSubmission` | `inter:Interaction` | Submission of command text. |
| `inter:CredentialChangeAttempt` | `inter:Interaction` | Attempt to change authentication material. |
| `inter:ProtocolNegotiation` | `inter:Interaction` | Exchange of protocol parameters. |
| `inter:ForwardingRequest` | `inter:Interaction` | Request to forward traffic. |
| `inter:ProtocolFingerprint` | `observable:ObservableObject` | Protocol/authentication fingerprint, distinguished by kind. |
| `inter:ProtocolParameter` | `core:UcoObject` | Named parameter with optional role and direction. |
| `inter:ParameterValue` | `core:UcoObject` | Individual parameter value with optional position and encoding. |
| `inter:PublicKeyMaterial` | `observable:ObservableObject` | Public-key material presented by a client. |
| `inter:TrafficFragment` | `observable:ObservableObject` | Recorded portion of network or protocol data. |
| `evidence:EventObservation` | `evidence:Observation` | Source-reported information about an occurrence. |
| `evidence:SessionObservation` | `evidence:Observation` | Session state, parameters, or accumulated summary. |
| `evidence:SessionLifecycleObservation` | `evidence:SessionObservation`, `evidence:EventObservation` | Reported session lifecycle state. |
| `evidence:AuthenticationObservation` | `evidence:EventObservation` | Presented authentication data and reported outcome. |
| `evidence:CommandObservation` | `evidence:EventObservation` | Command text, processing, or result report. |
| `evidence:CommandSubmissionObservation` | `evidence:CommandObservation` | Report of command submission. |
| `evidence:CommandOutcomeObservation` | `evidence:CommandObservation` | Report of a command-processing result. |
| `evidence:CredentialChangeObservation` | `evidence:EventObservation` | Report of a credential-change attempt, through any interface. |
| `evidence:ClientAttributeObservation` | `evidence:EventObservation` | Client banner, terminal dimensions, variables, or key material. |
| `evidence:ProtocolNegotiationObservation` | `evidence:EventObservation` | Reported protocol parameters, options, or capability lists. |
| `evidence:ForwardingObservation` | `evidence:EventObservation` | Forwarding request, channel data, or traffic characteristics. |
| `evidence:ProtocolErrorObservation` | `evidence:EventObservation` | Reported processing error or malformed data. |
| `evidence:DetectionObservation` | `evidence:EventObservation` | Detector label, vulnerability identifier, or suspicious input. |

## Domain property inventory

These properties supplement the shared relationships listed in [Architecture](./architecture.md). None is functional, a key, or an existential completeness requirement.

| Property | Domain → range | Meaning |
|---|---|---|
| `inter:sessionConnection` | `inter:Session` → `observable:NetworkConnection` | Known session-to-connection association; multiple connections are allowed. |
| `inter:relatedConnection` | `inter:Interaction` → `observable:NetworkConnection` | Known interaction-to-connection association. |
| `inter:hasParameterValue` | `inter:ProtocolParameter` → `inter:ParameterValue` | Parameter-to-value association; ordering uses explicit positions. |
| `inter:fingerprintKind` | `inter:ProtocolFingerprint` → `xsd:string` | Fingerprint family or scheme. |
| `inter:fingerprintValue` | `inter:ProtocolFingerprint` → `xsd:string` | Fingerprint value as supplied. |
| `inter:fingerprintHashAlgorithm` | `inter:ProtocolFingerprint` → `xsd:string` | Explicitly known fingerprint digest algorithm. |
| `inter:fingerprintInput` | `inter:ProtocolFingerprint` → `xsd:string` | Source-supplied fingerprint input. |
| `inter:parameterName` | `inter:ProtocolParameter` → `xsd:string` | Source or documented parameter name. |
| `inter:parameterRole` | `inter:ProtocolParameter` → `xsd:string` | Known role, such as offered capability or selected value. |
| `inter:parameterDirection` | `inter:ProtocolParameter` → `xsd:string` | Source-declared traffic direction or endpoint role. |
| `inter:parameterValueCount` | `inter:ProtocolParameter` → `xsd:nonNegativeInteger` | Known value count; zero records an explicitly empty list. |
| `inter:valueLexicalForm` | `inter:ParameterValue` → `xsd:string` | Supplied lexical representation. |
| `inter:valueEncoding` | `inter:ParameterValue` → `xsd:string` | Known value serialization or interpretation. |
| `inter:valuePosition` | `inter:ParameterValue` → `xsd:nonNegativeInteger` | Zero-based position within one parameter. |
| `inter:keyType` | `inter:PublicKeyMaterial` → `xsd:string` | Source-reported key type. |
| `inter:keyData` | `inter:PublicKeyMaterial` → `xsd:string` | Supplied public-key representation. |
| `inter:keyEncoding` | `inter:PublicKeyMaterial` → `xsd:string` | Known key serialization or encoding. |
| `inter:fragmentData` | `inter:TrafficFragment` → `xsd:string` | Supplied fragment representation. |
| `inter:fragmentEncoding` | `inter:TrafficFragment` → `xsd:string` | Known fragment serialization or encoding. |
| `inter:reportedByteLength` | `inter:TrafficFragment` → `xsd:nonNegativeInteger` | Source-reported byte length, independent of serialized character count. |
| `evidence:networkConnection` | `evidence:Observation` → `observable:NetworkConnection` | Report-to-connection association, with endpoint characteristics in UCO facets. |
| `evidence:hasFingerprint` | `evidence:Observation` → `inter:ProtocolFingerprint` | Report-to-fingerprint association. |
| `evidence:hasProtocolParameter` | `evidence:Observation` → `inter:ProtocolParameter` | Report-to-parameter association. |
| `evidence:clientVariable` | `evidence:Observation` → `observable:EnvironmentVariable` | Client-supplied UCO environment-variable descriptor. |
| `evidence:hasPublicKey` | `evidence:Observation` → `inter:PublicKeyMaterial` | Report-to-public-key association. |
| `evidence:hasTrafficFragment` | `evidence:Observation` → `inter:TrafficFragment` | Report-to-traffic-fragment association. |
| `evidence:forwardingOriginAddress` | `evidence:ForwardingObservation` → `observable:IPAddress` | Reported forwarding origin, distinct from the enclosing connection source. |
| `evidence:triggerParameter` | `evidence:DetectionObservation` → `inter:ProtocolParameter` | Named input identified by a detector. |
| `evidence:sourceEventType` | `evidence:EventObservation` → `xsd:string` | Original source event-type label. |
| `evidence:rawMessage` | `evidence:EventObservation` → `xsd:string` | Original human-readable source message. |
| `evidence:observedAtTime` | `evidence:Observation` → `xsd:dateTime` | Source-reported observation timestamp. |
| `evidence:sequencePosition` | `evidence:SourceRecord` → `xsd:nonNegativeInteger` | Zero-based record position within one source dataset version. |
| `evidence:reportedStartTime` | `evidence:SessionObservation` → `xsd:dateTime` | Explicitly reported session start. |
| `evidence:reportedEndTime` | `evidence:SessionObservation` → `xsd:dateTime` | Explicitly reported session end. |
| `evidence:reportedDurationSeconds` | `evidence:Observation` → `xsd:decimal` | Source-reported duration normalized to decimal seconds. |
| `evidence:lifecycleState` | `evidence:SessionLifecycleObservation` → `xsd:string` | Explicitly reported session lifecycle state. |
| `evidence:presentedUsername` | `evidence:Observation` → `xsd:string` | Username presented in the observed context. |
| `evidence:presentedPassword` | `evidence:Observation` → `xsd:string` | Presented password; an empty value differs from absence. |
| `evidence:authenticationMethod` | `evidence:AuthenticationObservation` → `xsd:string` | Explicitly known authentication method. |
| `evidence:reportedRealm` | `evidence:Observation` → `xsd:string` | Source-supplied realm or processing-context label. |
| `evidence:commandText` | `evidence:CommandObservation` → `xsd:string` | Original command or subcommand text. |
| `evidence:targetUsername` | `evidence:CredentialChangeObservation` → `xsd:string` | Username targeted by a credential-change attempt. |
| `evidence:reportedOutcome` | `evidence:Observation` → `xsd:string` | Source-justified reported outcome. |
| `evidence:outcomeScope` | `evidence:Observation` → `xsd:string` | Documented scope of the reported result. |
| `evidence:clientBanner` | `evidence:ClientAttributeObservation` → `xsd:string` | Client-supplied identification or version banner. |
| `evidence:terminalColumns` | `evidence:ClientAttributeObservation` → `xsd:nonNegativeInteger` | Reported terminal width in character columns. |
| `evidence:terminalRows` | `evidence:ClientAttributeObservation` → `xsd:nonNegativeInteger` | Reported terminal height in character rows. |
| `evidence:reportedArchitecture` | `evidence:SessionObservation` → `xsd:string` | Architecture/environment label for the session context. |
| `evidence:reportedChannelIdentifier` | `evidence:ForwardingObservation` → `xsd:string` | Channel identifier scoped to documented capture context. |
| `evidence:forwardingOriginPort` | `evidence:ForwardingObservation` → `xsd:integer` | Reported forwarding-origin port. |
| `evidence:errorMessage` | `evidence:ProtocolErrorObservation` → `xsd:string` | Source-reported error description. |
| `evidence:errorCode` | `evidence:ProtocolErrorObservation` → `xsd:string` | Source-reported error code or category. |
| `evidence:messageNumber` | `evidence:ProtocolErrorObservation` → `xsd:integer` | Source-reported protocol message number. |
| `evidence:detectorLabel` | `evidence:DetectionObservation` → `xsd:string` | Source-assigned detection label. |
| `evidence:vulnerabilityIdentifier` | `evidence:DetectionObservation` → `xsd:string` | Vulnerability identifier associated with a detection report. |
| `evidence:protocolName` | `evidence:Observation` → `xsd:string` | Source-reported protocol label. |
