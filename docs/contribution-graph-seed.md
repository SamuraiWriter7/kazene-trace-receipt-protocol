# Contribution Graph Seed

## Overview

Contribution Graph Seed defines how multiple trace receipts can be connected into a lightweight contribution graph.

In v0.1, Kazene Trace Receipt Protocol defined the minimal receipt structure.

In v0.2, the protocol added lifecycle-aware trace management.

In v0.3, the protocol begins to connect trace receipts into contribution relationships.

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
v0.3 connects receipts into contribution graphs.
```

The purpose of v0.3 is not to calculate royalties.

The purpose is to describe how trace receipts relate to one another.

---

## Why Contribution Graphs Matter

AI-assisted creation rarely happens in a single step.

A typical workflow may include:

```text
human idea
  ↓
prompt
  ↓
AI reading
  ↓
source reference
  ↓
draft generation
  ↓
human edit
  ↓
schema update
  ↓
validation
  ↓
release
```

Each step may produce a trace receipt.

Individually, each receipt records an event.

Together, they form a contribution graph.

A contribution graph helps answer:

* which trace receipts influenced this output,
* which sources were upstream,
* which outputs became downstream,
* which human or AI actors contributed,
* which links require review,
* which contribution paths are strong or weak,
* and which traces may later connect to value routing.

---

## Core Principle

```text
A contribution graph is not a royalty engine.
It is a structured map of influence, lineage, and review boundaries.
```

v0.3 should remain lightweight.

It should not attempt to decide:

* final ownership,
* final attribution score,
* final payment allocation,
* legal authorship,
* or economic entitlement.

Those belong to later layers, especially Royalty OS and human review.

---

## Contribution Graph Model

A contribution graph is made of:

```text
nodes
edges
paths
weights
review triggers
```

### Nodes

A node represents a trace receipt.

Each node should reference an existing `trace_receipt.id`.

Example:

```yaml
nodes:
  - trace_id: "trace-2026-06-18-001"
    node_type: "origin"
    contribution_hint: "idea"
```

### Edges

An edge represents a relationship between two trace receipts.

Example:

```yaml
edges:
  - from_trace_id: "trace-2026-06-18-001"
    to_trace_id: "trace-2026-06-18-002"
    relation_type: "influenced"
    influence_weight: "high"
```

### Paths

A path represents a meaningful route through multiple trace receipts.

Example:

```text
origin idea
  → prompt
  → AI draft
  → human edit
  → release
```

### Weights

Weights are provisional hints.

They help describe influence, but they are not final scores.

Allowed values:

```text
low
medium
high
critical
```

### Review Triggers

Some graph relationships should return to human review.

This is especially important when the graph involves:

* authorship,
* attribution,
* value allocation,
* privacy-sensitive sources,
* high-impact derivative outputs,
* disputed contribution,
* cross-agent delegation,
* or irreversible public release.

---

## Graph Object

v0.3 introduces an optional `contribution_graph` object.

Recommended structure:

```yaml
contribution_graph:
  graph_id: "graph-2026-06-18-001"
  graph_type: "trace_lineage"
  root_trace_id: "trace-2026-06-18-001"
  terminal_trace_ids:
    - "trace-2026-06-18-005"

  nodes:
    - trace_id: "trace-2026-06-18-001"
      node_type: "origin"
      contribution_hint: "idea"

    - trace_id: "trace-2026-06-18-002"
      node_type: "reference"
      contribution_hint: "source_reference"

    - trace_id: "trace-2026-06-18-003"
      node_type: "generation"
      contribution_hint: "draft"

  edges:
    - from_trace_id: "trace-2026-06-18-001"
      to_trace_id: "trace-2026-06-18-003"
      relation_type: "influenced"
      influence_weight: "high"
      review_required: false

    - from_trace_id: "trace-2026-06-18-002"
      to_trace_id: "trace-2026-06-18-003"
      relation_type: "referenced_by"
      influence_weight: "medium"
      review_required: true

  review:
    graph_review_required: true
    reason: "attribution"
```

---

## Graph Types

Allowed graph types:

```text
trace_lineage
contribution_chain
derivative_chain
review_chain
memory_chain
royalty_preparation
```

### trace_lineage

Use when the graph describes the basic lineage of trace receipts.

### contribution_chain

Use when the graph emphasizes human, AI, tool, or source contributions.

### derivative_chain

Use when the graph describes how one output led to another derivative output.

### review_chain

Use when the graph is primarily used for human review or dispute preparation.

### memory_chain

Use when the graph is connected to memory retention, compaction, forgetting, or archive.

### royalty_preparation

Use when the graph may later connect to Royalty OS, without calculating payment yet.

---

## Node Types

Allowed node types:

```text
origin
source
prompt
reference
reading
ingestion
generation
edit
review
validation
release
memory
archive
```

### origin

The starting point of a contribution chain.

### source

A referenced file, repository, dataset, memory, URL, or other source.

### prompt

A prompt or instruction that shaped the output.

### reference

A trace receipt used as a cited or structurally relevant reference.

### reading

A trace receipt representing an AI or human read action.

### ingestion

A trace receipt representing absorption into a system, index, memory layer, or workflow context.

### generation

A trace receipt representing AI-assisted output generation.

### edit

A trace receipt representing human or AI editing.

### review

A trace receipt representing human or automated review.

### validation

A trace receipt representing schema, CI, or consistency validation.

### release

A trace receipt representing publication, release, or externalization.

### memory

A trace receipt connected to memory retention, compaction, or routing.

### archive

A trace receipt moved into long-term archive or low-access storage.

---

## Edge Relation Types

Allowed relation types:

```text
influenced
derived_from
referenced_by
generated_from
edited_from
validated_by
reviewed_by
released_as
compacted_into
archived_as
routed_to
```

### influenced

A source or trace shaped a later trace.

### derived_from

A later trace is derived from an earlier trace.

### referenced_by

A trace was used as a reference by another trace.

### generated_from

An output trace was generated from an earlier trace.

### edited_from

An edited trace was produced from an earlier trace.

### validated_by

A trace was validated by a schema, script, CI action, or review process.

### reviewed_by

A trace was reviewed by a human or review system.

### released_as

A trace became part of a public or external release.

### compacted_into

A trace was compressed into a smaller summary or memory form.

### archived_as

A trace was moved into archive.

### routed_to

A trace was routed to another wing, agent, system, or review layer.

---

## Influence Weight

`influence_weight` describes provisional influence between two trace receipts.

Allowed values:

```text
low
medium
high
critical
```

This is not a final attribution score.

It is a lightweight signal for future review, contribution graph analysis, or Royalty OS integration.

---

## Review Boundary

A contribution graph should trigger human review when:

* a critical source influences a public output,
* a disputed contribution exists,
* authorship may be affected,
* value allocation may be affected,
* sensitive source material appears in the graph,
* a cross-agent route influences downstream output,
* a trace is released externally,
* or the graph may later connect to royalty routing.

Recommended structure:

```yaml
review:
  graph_review_required: true
  reason: "attribution"
```

Allowed review reasons:

```text
none
authorship
attribution
value_allocation
privacy_risk
safety_boundary
cross_agent_authority
disputed_contribution
royalty_preparation
memory_retention
irreversible_publication
other
```

---

## Relationship to Trace Receipt

The contribution graph should not replace trace receipts.

It should connect them.

```text
Trace Receipt
  = records a single event

Trace Lifecycle
  = describes how that event moves through time

Contribution Graph
  = connects multiple receipts into influence and lineage relationships
```

A graph should reference trace receipts by `trace_id`.

It should avoid duplicating full receipt data.

---

## Relationship to Royalty OS

v0.3 prepares for Royalty OS but does not perform royalty calculation.

It may mark:

* influence paths,
* high-impact sources,
* attribution-required edges,
* disputed contribution areas,
* and value-sensitive review triggers.

But final value allocation belongs to a later layer.

```text
Contribution Graph Seed
  ↓
Royalty OS Hook
  ↓
Human Review / Dispute Layer
  ↓
Value Circulation
```

---

## Relationship to Memory Breathing

Contribution graphs may also support memory metabolism.

For example:

```text
long trace chain
  ↓
graph extraction
  ↓
critical nodes retained
  ↓
low-value nodes compacted
  ↓
temporary traces forgotten
  ↓
review-sensitive edges archived
```

This allows the protocol to preserve structural memory without keeping every raw intermediate trace.

---

## Minimal Example Flow

```text
trace-001: human idea
  ↓ influenced
trace-002: prompt
  ↓ generated_from
trace-003: AI draft
  ↓ edited_from
trace-004: human edit
  ↓ validated_by
trace-005: release
```

This flow can be represented as:

```yaml
contribution_graph:
  graph_id: "graph-2026-06-18-001"
  graph_type: "contribution_chain"
  root_trace_id: "trace-2026-06-18-001"
  terminal_trace_ids:
    - "trace-2026-06-18-005"

  nodes:
    - trace_id: "trace-2026-06-18-001"
      node_type: "origin"
      contribution_hint: "idea"

    - trace_id: "trace-2026-06-18-002"
      node_type: "prompt"
      contribution_hint: "prompt"

    - trace_id: "trace-2026-06-18-003"
      node_type: "generation"
      contribution_hint: "draft"

    - trace_id: "trace-2026-06-18-004"
      node_type: "edit"
      contribution_hint: "correction"

    - trace_id: "trace-2026-06-18-005"
      node_type: "release"
      contribution_hint: "publication"

  edges:
    - from_trace_id: "trace-2026-06-18-001"
      to_trace_id: "trace-2026-06-18-002"
      relation_type: "influenced"
      influence_weight: "high"
      review_required: false

    - from_trace_id: "trace-2026-06-18-002"
      to_trace_id: "trace-2026-06-18-003"
      relation_type: "generated_from"
      influence_weight: "high"
      review_required: false

    - from_trace_id: "trace-2026-06-18-003"
      to_trace_id: "trace-2026-06-18-004"
      relation_type: "edited_from"
      influence_weight: "medium"
      review_required: false

    - from_trace_id: "trace-2026-06-18-004"
      to_trace_id: "trace-2026-06-18-005"
      relation_type: "released_as"
      influence_weight: "critical"
      review_required: true

  review:
    graph_review_required: true
    reason: "irreversible_publication"
```

---

## v0.3 Summary

v0.3 extends Kazene Trace Receipt Protocol by introducing Contribution Graph Seed.

It defines:

* graph identity,
* graph type,
* root trace,
* terminal traces,
* graph nodes,
* graph edges,
* relation types,
* influence weights,
* and graph-level human review triggers.

In short:

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
v0.3 connects receipts into a contribution graph.
```

Contribution Graph Seed is the bridge between trace records and future attribution, memory breathing, and royalty circulation systems.
