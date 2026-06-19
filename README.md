# Kazene Trace Receipt Protocol

**Kazene Trace Receipt Protocol** is a minimal standard for recording structured receipts of AI-assisted creation, transformation, routing, and derivative events without storing raw content by default.

It is designed as a lightweight trace layer for future attribution, memory metabolism, contribution graphs, and royalty circulation systems.

This protocol does **not** start with payment distribution.

It starts with a simpler question:

> What happened, what was referenced, what was transformed, and what should be preserved, compacted, forgotten, or reviewed?

## Current Version

```text
Version: v0.4.0-candidate
Layer: Memory Breathing Integration
Status: Draft protocol candidate
Validation: Passing
```

Kazene Trace Receipt Protocol is currently at **v0.4.0-candidate**.

This version extends the protocol by connecting trace receipts and contribution graphs to memory metabolism.

v0.4 introduces:

* memory layers:

  * `short_term`
  * `working`
  * `long_term`
  * `implicit`
  * `archive`
* memory actions:

  * `retain`
  * `compact`
  * `forget`
  * `archive`
  * `review`
  * `implicit`
  * `convert_to_rule`
* memory weights:

  * `low`
  * `medium`
  * `high`
  * `critical`
* target types for memory decisions,
* retention policy,
* compaction policy,
* human review boundary,
* and integration with 風の記憶丸, 構造反芻丸, and Royalty OS.

The goal of v0.4 is not to remember everything.

The goal is to remember less, but better.

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
v0.3 connects receipts into contribution graphs.
v0.4 teaches trace how to breathe.
```

---

## Validation Status

The current examples have been validated against their JSON Schemas.

```text
schemas/trace-receipt.schema.json
schemas/contribution-graph.schema.json
schemas/memory-breathing.schema.json

examples/trace-receipt.example.yaml
examples/trace-receipt-lifecycle.example.yaml
examples/contribution-graph.example.yaml
examples/memory-breathing.example.yaml

scripts/validate_examples.py
.github/workflows/validate-examples.yml
```

Validation status:

```text
GitHub Actions: Passing
Trace Receipt Core example: Passing
Trace Receipt Lifecycle example: Passing
Contribution Graph Seed example: Passing
Memory Breathing Integration example: Passing
Schema validation: Passing
```

To validate locally, run:

```bash
python scripts/validate_examples.py
```

A successful validation confirms that all current examples conform to their corresponding schemas.


## Why This Exists

AI-assisted work is becoming faster, denser, and more derivative.

A single workflow may now involve:

* human ideas,
* prompts,
* AI-generated drafts,
* code changes,
* design revisions,
* repository updates,
* memory compaction,
* agent routing,
* and downstream publications.

Without a minimal trace standard, these events become difficult to audit, attribute, compress, or reuse.

However, storing everything as raw logs creates a different problem:

> A trace system can easily become a surveillance system.

Kazene Trace Receipt Protocol avoids that by treating trace as a **structured receipt**, not a warehouse.

The default design is:

```text
hash over raw content
structure over full logs
retention over permanent storage
review boundary over silent automation
contribution hints over final royalty decisions
```

---

## Core Concept

A **Trace Receipt** is a minimal record of an event.

It describes:

* when the event happened,
* what type of event it was,
* who or what acted,
* what sources were referenced,
* what transformation occurred,
* what output was produced,
* what permission or usage scope applies,
* what contribution hint exists,
* what privacy and retention rules apply,
* whether future royalty routing may be needed,
* and whether human review is required.

It does **not** need to store the raw source or output content.

---

## Design Principles

```text
Trace is not surveillance.
Trace is structured accountability.

A receipt is not a verdict.
It records an event before value distribution is decided.

Contribution is not yet royalty.
It is a seed for future contribution graphs.

Forgetting is not loss.
It is part of healthy trace lifecycle management.

Raw content should not be stored by default.
Hashes, references, and lifecycle rules should be preferred.

Human review is not a bottleneck.
It is the boundary that prevents trace automation from becoming unchecked authority.
```

---

## Relationship to Kazene OS

Kazene Trace Receipt Protocol sits between creation, memory, attribution, and royalty circulation.

```text
Human / AI / Tool Event
  ↓
Trace Receipt
  ↓
Trace Lifecycle
  ↓
Contribution Graph
  ↓
Memory Breathing
  ↓
Royalty OS Hook
  ↓
Human Review / Dispute Layer
```

It can connect to:

* **Kazene Memory Breathing Protocol**
* **風の記憶丸**
* **構造反芻丸**
* **Royalty OS**
* **Contribution Graph systems**
* **AI-assisted GitHub workflows**
* **Enterprise trace gateways**
* **Public commons attribution layers**

---

## What This Protocol Is

Kazene Trace Receipt Protocol is:

* a minimal receipt format,
* a trace lifecycle seed,
* a contribution graph seed,
* a privacy-aware metadata structure,
* a bridge between AI workflows and future royalty systems,
* and a foundation for memory compaction and human review.

---

## What This Protocol Is Not

Kazene Trace Receipt Protocol is **not**:

* a payment system,
* a final royalty calculation engine,
* a surveillance log,
* a full provenance database,
* a license enforcement system,
* a blockchain requirement,
* or a replacement for human judgment.

Royalty routing may be added later, but v0.1 only records the structural conditions needed for future attribution and review.

---

## Repository Structure

```text
kazene-trace-receipt-protocol/
├─ README.md
├─ CHANGELOG.md
├─ docs/
│  ├─ trace-receipt-overview.md
│  ├─ trace-receipt-lifecycle.md
│  └─ privacy-and-forgetting.md
├─ schemas/
│  └─ trace-receipt.schema.json
├─ examples/
│  └─ trace-receipt.example.yaml
├─ scripts/
│  └─ validate_examples.py
└─ .github/
   └─ workflows/
      └─ validate-examples.yml
```

---

## Minimal Trace Receipt Example

```yaml
trace_receipt:
  id: "trace-2026-06-18-001"
  version: "0.1.0"
  timestamp: "2026-06-18T05:39:00Z"

  event_type: "generate"
  chain_id: null
  parent_trace_id: null
  child_traces: []

  actor:
    type: "human"
    id: "human:creator"
    role: "originator"

  source_refs:
    - type: "prompt"
      ref_hash: "sha256:example-source-hash"
      visibility: "private"

  transformation:
    intent: "article_draft"
    method: "ai_assisted_generation"
    model_or_tool: "chatgpt"
    model_version: "unknown"
    compute_provider: "openai"
    output_hash: "sha256:example-output-hash"
    derivative_level: "medium"

  contribution:
    contribution_type: "idea"
    weight_hint: "high"
    estimated_influence: 0.8

  permission:
    usage_scope: "public"
    consent_status: "explicit"
    license_ref: null

  privacy:
    raw_content_stored: false
    reversible: false
    retention: "working"
    zero_knowledge_proof: null

  lifecycle:
    expires_at: null
    forgetting_action: "compact_after_use"

  value_hook:
    royalty_route: "pending"
    attribution_required: true

  review:
    human_review_required: true
    reason: "authorship_and_value"
```

---

## Core Fields

### `id`

Unique identifier for the trace receipt.

Example:

```yaml
id: "trace-2026-06-18-001"
```

---

### `version`

Protocol version used by the receipt.

Example:

```yaml
version: "0.1.0"
```

---

### `timestamp`

Time when the trace event occurred.

Example:

```yaml
timestamp: "2026-06-18T05:39:00Z"
```

---

### `event_type`

Type of event being recorded.

Initial v0.1 event types:

```text
generate
edit
summarize
code_change
schema_change
example_change
review
compact
route
release
```

Future versions may extend this list to include:

```text
video_generation
design_change
robot_action
sensor_action
agent_execution
```

---

### `actor`

The human, AI agent, system, organization, or tool that performed the event.

Example:

```yaml
actor:
  type: "human"
  id: "human:creator"
  role: "originator"
```

Allowed actor types:

```text
human
ai_agent
system
organization
tool
```

---

### `source_refs`

A list of sources referenced by the event.

Sources should be referenced by hash or structured identifier whenever possible.

Example:

```yaml
source_refs:
  - type: "prompt"
    ref_hash: "sha256:example-source-hash"
    visibility: "private"
```

Initial source types:

```text
prompt
file
url
repository
dataset
memory
design_asset
sensor
manual_input
```

Visibility levels:

```text
private
shared
public
restricted
```

---

### `transformation`

Describes what transformation occurred.

Example:

```yaml
transformation:
  intent: "article_draft"
  method: "ai_assisted_generation"
  model_or_tool: "chatgpt"
  model_version: "unknown"
  compute_provider: "openai"
  output_hash: "sha256:example-output-hash"
  derivative_level: "medium"
```

Derivative levels:

```text
low
medium
high
critical
```

The derivative level is only a hint.
It is not a final legal or economic judgment.

---

### `contribution`

Records a lightweight contribution hint.

Example:

```yaml
contribution:
  contribution_type: "idea"
  weight_hint: "high"
  estimated_influence: 0.8
```

Contribution types:

```text
idea
prompt
data
code
design
review
correction
action
context
memory
```

Weight hints:

```text
low
medium
high
critical
```

`estimated_influence` is optional and should be treated as a provisional signal, not a final attribution score.

---

### `permission`

Records usage scope, consent status, and optional license reference.

Example:

```yaml
permission:
  usage_scope: "public"
  consent_status: "explicit"
  license_ref: null
```

Usage scopes:

```text
personal
internal
commercial
public
training
no_training
research
archive
```

Consent status values:

```text
explicit
implied
unknown
denied
not_required
```

---

### `privacy`

Defines how sensitive content is handled.

Example:

```yaml
privacy:
  raw_content_stored: false
  reversible: false
  retention: "working"
  zero_knowledge_proof: null
```

Retention levels:

```text
temporary
working
long_term
forget_after_use
archive
```

The default recommendation is:

```yaml
raw_content_stored: false
```

---

### `lifecycle`

Defines trace lifecycle and forgetting behavior.

Example:

```yaml
lifecycle:
  expires_at: null
  forgetting_action: "compact_after_use"
```

Forgetting actions:

```text
retain
compact_after_use
forget_after_use
archive
human_review
```

---

### `value_hook`

Defines whether the trace may connect to future royalty or value routing systems.

Example:

```yaml
value_hook:
  royalty_route: "pending"
  attribution_required: true
```

Royalty route values:

```text
none
pending
direct
pool
human_review
```

This field does not calculate payment.
It only marks whether future value routing may be relevant.

---

### `review`

Defines whether human review is required.

Example:

```yaml
review:
  human_review_required: true
  reason: "authorship_and_value"
```

Human review should be required when trace decisions involve:

* authorship,
* attribution,
* value allocation,
* legal interpretation,
* privacy risk,
* safety boundary,
* physical-world action,
* irreversible publication,
* cross-agent authority,
* or disputed contribution.

---

## Trace Lifecycle

A trace receipt may move through the following lifecycle:

```text
created
  ↓
validated
  ↓
linked
  ↓
compacted
  ↓
retained / forgotten / archived
  ↓
reviewed if needed
```

The protocol supports future extension into parent-child trace chains:

```text
parent_trace_id
  ↓
current_trace_id
  ↓
child_traces
```

This allows trace receipts to become seeds for future contribution graphs without requiring a full graph system in v0.1.

---

## Privacy and Forgetting

This protocol treats forgetting as a first-class operation.

Forgetting may mean:

* deleting raw temporary data,
* retaining only hashes,
* compacting trace records,
* downgrading memory weight,
* moving records to archive,
* or returning the decision to human review.

The goal is to preserve accountability without creating permanent surveillance.

---

## Validation

The repository includes:

```text
schemas/trace-receipt.schema.json
examples/trace-receipt.example.yaml
scripts/validate_examples.py
```

The validation script checks that the example file conforms to the JSON Schema.

Expected command:

```bash
python scripts/validate_examples.py
```

## Version Roadmap

### v0.1 — Trace Receipt Core

Status: Completed as `v0.1.0-candidate`

Focus:

```text
record what happened
avoid raw content storage by default
define privacy and lifecycle fields
prepare future contribution graph linkage
```

v0.1 established the first executable receipt structure for AI-assisted creation, transformation, routing, and derivative events.

---

### v0.2 — Trace Lifecycle

Status: Completed as `v0.2.0-candidate`

Focus:

```text
read / ingest / reference event types
actor authority scope
source influence hints
explicit lifecycle state
parent-child trace semantics
retention / compaction / forgetting / archive / review
```

v0.2 extended Trace Receipt Core by adding lifecycle-aware trace management.

It introduced the idea that a trace receipt is not only a static record.

It can be created, validated, linked, compacted, retained, forgotten, archived, or reviewed.

---

### v0.3 — Contribution Graph Seed

Status: Completed as `v0.3.0-candidate`

Focus:

```text
trace chains
influence hints
source-output relationships
graph nodes
graph edges
review triggers
```

v0.3 connected multiple trace receipts into lightweight contribution graphs.

It established the first graph layer for mapping influence, lineage, memory actions, review boundaries, and future royalty-preparation routes.

---

### v0.4 — Memory Breathing Integration

Status: Current candidate

Focus:

```text
memory layers
memory actions
memory weights
retention policy
compaction policy
human review boundary
implicit guidance
convert_to_rule
```

v0.4 connects trace receipts and contribution graphs to memory metabolism.

It defines how trace should be retained, compacted, forgotten, archived, reviewed, made implicit, or converted into recurrence rules.

In short:

```text
Trace should not accumulate endlessly.
Trace should breathe.
```

---

### v0.5 — Royalty OS Hook

Planned focus:

```text
attribution_required
royalty_route
pool routing
review boundary
dispute preparation
value circulation readiness
```

v0.5 will add preliminary hooks for future value circulation and Royalty OS integration.

It will not calculate final payment.

It will prepare trace, graph, and memory records for attribution review, royalty routing, and dispute-aware value circulation.


## Example Use Cases

### AI-assisted article creation

```text
handwritten idea
  → prompt
  → AI draft
  → human edit
  → blog post
  → trace receipt
```

---

### GitHub specification work

```text
concept
  → README
  → schema
  → example
  → validator
  → release note
  → trace receipt
```

---

### Memory compaction

```text
long conversation
  → structural summary
  → useful memory retained
  → raw noise released
  → trace receipt
```

---

### Future royalty routing

```text
origin idea
  → derivative article
  → code implementation
  → public release
  → contribution graph
  → royalty review
```

---

## Integration with Memory and Rumination Systems

Kazene Trace Receipt Protocol can work with memory and rumination agents.

```text
Trace Receipt
  = records what happened

風の記憶丸
  = decides what to retain, compact, forget, or route

構造反芻丸
  = converts failure traces into recurrence prevention rules

Royalty OS
  = connects trace records to future value circulation
```

This allows the protocol to support both accountability and cognitive load reduction.

---

## Human Review Boundary

This protocol must not silently decide critical matters.

Human review is required when a trace affects:

* authorship,
* ownership,
* attribution,
* royalty routing,
* safety,
* privacy,
* legal interpretation,
* financial consequence,
* political interpretation,
* physical-world action,
* or irreversible external publication.

Trace receipts may assist review.

They must not replace it.

---

## License

This project is intended to be developed as an open standard.

Recommended license:

```text
MIT License for code
CC BY 4.0 for documentation
```

Final license selection should be confirmed by the repository owner.

---

## Status

```text
Version: v0.1.0-candidate
Status: Draft
Layer: Trace Receipt Core
```

Kazene Trace Receipt Protocol is an early-stage standard for creating structured, privacy-aware, lifecycle-conscious receipts for AI-assisted creation and transformation.

Its purpose is simple:

> Record enough structure to support future attribution, memory breathing, and value circulation — without turning trace into surveillance.

```
```

