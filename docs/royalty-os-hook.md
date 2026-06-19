# Royalty OS Hook

## Overview

Royalty OS Hook defines how trace receipts, contribution graphs, and memory breathing records can prepare for future value circulation.

In v0.1, Kazene Trace Receipt Protocol defined the minimal trace receipt.

In v0.2, the protocol added lifecycle-aware trace management.

In v0.3, the protocol connected trace receipts into contribution graphs.

In v0.4, the protocol connected trace and graph structures to memory metabolism.

In v0.5, the protocol adds a preliminary hook for Royalty OS integration.

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
v0.3 connects receipts into contribution graphs.
v0.4 teaches trace how to breathe.
v0.5 prepares trace for value circulation.
```

Royalty OS Hook does **not** calculate final payment.

It does **not** decide legal ownership.

It does **not** silently assign economic entitlement.

Its role is to prepare clean, reviewable routing signals for future attribution, royalty, pool, dispute, and human review systems.

---

## Why Royalty OS Hook Matters

AI-assisted work creates complex chains of contribution.

A single output may involve:

* original human ideas,
* prompts,
* source references,
* AI-generated drafts,
* edits,
* validations,
* release decisions,
* memory compaction,
* and downstream reuse.

Without a value-routing hook, contribution graphs remain descriptive only.

With a Royalty OS Hook, trace structures can indicate:

* whether attribution may be required,
* whether value routing is pending,
* whether a direct route is possible,
* whether a pool route is more appropriate,
* whether human review is required,
* whether dispute preparation is needed,
* and whether the record should remain non-monetized.

---

## Core Principle

```text
Royalty routing is not payment calculation.
It is value-circulation readiness.

Attribution is not ownership.
It is a review signal.

Influence is not entitlement.
It is a graph hint.

A royalty hook is not a verdict.
It is a bridge to human-reviewed value routing.
```

v0.5 must remain cautious.

The protocol may prepare routing signals.

It must not silently decide final payment, ownership, legal authorship, or economic allocation.

---

## Royalty Hook Object

v0.5 introduces a top-level `royalty_os_hook` object.

Recommended structure:

```yaml
royalty_os_hook:
  hook_id: "royalty-hook-2026-06-19-001"
  version: "0.5.0"
  created_at: "2026-06-19T09:30:00Z"

  target:
    target_type: "contribution_graph"
    target_id: "graph-2026-06-19-001"

  routing:
    royalty_route: "pending"
    route_basis: "contribution_graph"
    attribution_required: true
    monetization_status: "not_calculated"

  allocation:
    allocation_mode: "not_assigned"
    allocation_hint: "pool_candidate"
    estimated_value_weight: "high"

  review:
    human_review_required: true
    reason: "royalty_preparation"

  dispute:
    dispute_status: "none"
    dispute_preparation_required: false

  links:
    trace_receipt_ids:
      - "trace-2026-06-19-001"
      - "trace-2026-06-19-005"
    contribution_graph_ids:
      - "graph-2026-06-19-001"
    memory_breathing_ids:
      - "memory-2026-06-19-001"
```

---

## Target Types

Allowed target types:

```text
trace_receipt
contribution_graph
trace_chain
graph_edge
graph_node
memory_breathing_record
release_record
publication_record
```

### trace_receipt

Use when the value-routing signal applies to one trace receipt.

### contribution_graph

Use when value-routing readiness is based on an entire contribution graph.

### trace_chain

Use when the relevant contribution path is a sequence of trace receipts.

### graph_edge

Use when one relationship between two trace receipts may affect attribution or value routing.

### graph_node

Use when one node in the contribution graph may require attribution or value review.

### memory_breathing_record

Use when the value-routing decision depends on prior memory compaction, retention, or archive status.

### release_record

Use when the hook applies to a versioned release.

### publication_record

Use when the hook applies to an external publication, article, dataset, code release, or public artifact.

---

## Routing Fields

The `routing` object describes the direction of possible value circulation.

Recommended structure:

```yaml
routing:
  royalty_route: "pending"
  route_basis: "contribution_graph"
  attribution_required: true
  monetization_status: "not_calculated"
```

---

## Royalty Route

Allowed values:

```text
none
pending
direct
pool
human_review
blocked
```

### none

No royalty or value-routing action is expected.

Use when:

* the contribution has no value-routing relevance,
* the record is purely internal,
* or attribution is not required.

### pending

Value-routing relevance exists but has not been decided.

Use when:

* the graph suggests possible future attribution,
* release or monetization has not occurred,
* or more review is needed.

### direct

A direct route to a contributor or origin may be possible.

Use when:

* the contribution path is clear,
* the source identity is known,
* and human review confirms the route.

### pool

A shared pool route may be more appropriate.

Use when:

* many contributors are involved,
* influence is distributed,
* exact allocation is difficult,
* or the project uses pooled value circulation.

### human_review

The route cannot be determined automatically.

Use when:

* attribution is sensitive,
* value allocation may be disputed,
* legal interpretation is needed,
* or authorship boundaries are unclear.

### blocked

Value routing should not proceed.

Use when:

* consent is denied,
* legal restrictions apply,
* privacy risk is unresolved,
* safety concerns exist,
* or human review blocks the route.

---

## Route Basis

Allowed values:

```text
trace_receipt
trace_lifecycle
contribution_graph
memory_breathing
manual_review
external_policy
```

### trace_receipt

The routing signal is based on a single trace receipt.

### trace_lifecycle

The routing signal is based on lifecycle state, retention, archive, or review status.

### contribution_graph

The routing signal is based on graph nodes, edges, influence weights, or trace lineage.

### memory_breathing

The routing signal is based on memory layer, memory action, compaction, retention, or archive status.

### manual_review

The routing signal is based on human review.

### external_policy

The routing signal is based on license, organization policy, platform terms, law, or other external governance.

---

## Monetization Status

Allowed values:

```text
not_applicable
not_calculated
eligible
ineligible
pending_review
blocked
```

### not_applicable

The record is not connected to monetization.

### not_calculated

The record may later connect to value circulation, but no calculation has been performed.

### eligible

The record appears eligible for future value routing, pending review.

### ineligible

The record appears ineligible for value routing.

### pending_review

Eligibility cannot be determined without human review.

### blocked

Monetization or royalty routing should not proceed.

---

## Allocation Fields

The `allocation` object does not assign final payment.

It only describes allocation readiness.

Recommended structure:

```yaml
allocation:
  allocation_mode: "not_assigned"
  allocation_hint: "pool_candidate"
  estimated_value_weight: "high"
```

---

## Allocation Mode

Allowed values:

```text
not_assigned
direct_candidate
pool_candidate
manual_review_required
blocked
```

### not_assigned

No allocation mode has been assigned.

### direct_candidate

A direct allocation may be possible after review.

### pool_candidate

A pooled allocation may be more appropriate.

### manual_review_required

Human judgment is required before allocation can proceed.

### blocked

Allocation should not proceed.

---

## Allocation Hint

Allowed values:

```text
none
direct_candidate
pool_candidate
review_candidate
dispute_candidate
blocked
```

This field is a signal only.

It does not allocate value.

---

## Estimated Value Weight

Allowed values:

```text
low
medium
high
critical
```

`estimated_value_weight` indicates the likely value relevance of the target.

It is not a final royalty weight.

---

## Review Boundary

Royalty OS Hook must return to human review when value-sensitive matters arise.

Recommended structure:

```yaml
review:
  human_review_required: true
  reason: "royalty_preparation"
```

Allowed review reasons:

```text
none
authorship
attribution
value_allocation
royalty_preparation
legal_interpretation
privacy_risk
safety_boundary
disputed_contribution
external_policy
irreversible_publication
other
```

Human review is required when the hook affects:

* authorship,
* attribution,
* value allocation,
* royalty routing,
* legal interpretation,
* privacy,
* safety,
* external publication,
* disputed contribution,
* blocked consent,
* or irreversible economic consequence.

---

## Dispute Preparation

v0.5 introduces lightweight dispute preparation.

Recommended structure:

```yaml
dispute:
  dispute_status: "none"
  dispute_preparation_required: false
```

Allowed dispute status values:

```text
none
possible
active
resolved
blocked
```

### none

No dispute signal is present.

### possible

A dispute may arise.

### active

A dispute is currently active.

### resolved

A dispute has been reviewed or resolved.

### blocked

Routing or allocation is blocked due to dispute risk.

---

## Links

Royalty OS Hook may link to related protocol objects.

Recommended structure:

```yaml
links:
  trace_receipt_ids:
    - "trace-2026-06-19-001"
  contribution_graph_ids:
    - "graph-2026-06-19-001"
  memory_breathing_ids:
    - "memory-2026-06-19-001"
```

Links should reference existing records by ID.

The hook should avoid duplicating full trace, graph, or memory records.

---

## Relationship to Trace Receipt

Trace Receipt records what happened.

Royalty OS Hook marks whether the event may later participate in value routing.

```text
Trace Receipt
  ↓
Royalty OS Hook
  ↓
pending / direct / pool / human_review / blocked
```

---

## Relationship to Contribution Graph

Contribution Graph maps influence and lineage.

Royalty OS Hook uses that graph as a basis for future attribution and value-routing review.

```text
Contribution Graph
  ↓
influence paths
  ↓
value-routing readiness
  ↓
human review
```

---

## Relationship to Memory Breathing

Memory Breathing decides what is retained, compacted, forgotten, archived, reviewed, made implicit, or converted into rules.

Royalty OS Hook should only operate on trace and graph structures that have passed memory hygiene.

```text
Memory Breathing
  ↓
clean retained structure
  ↓
Royalty OS Hook
```

This prevents value routing from being based on noisy, over-retained, or privacy-sensitive trace.

---

## Relationship to Royalty OS

Royalty OS Hook is not the full Royalty OS.

It is the adapter layer.

```text
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
Royalty OS
  ↓
Human Review / Dispute Layer
```

Royalty OS may later calculate, allocate, distribute, or record value circulation.

Royalty OS Hook only prepares the route.

---

## Human Review Rule

The central rule of v0.5 is:

```text
No final value allocation without human review.
```

Automated systems may propose:

* `royalty_route`,
* `allocation_hint`,
* `estimated_value_weight`,
* `dispute_status`,
* and `monetization_status`.

They must not silently decide final payment, ownership, or entitlement.

---

## Example Flow

```text
trace receipt created
  ↓
trace lifecycle validated
  ↓
contribution graph generated
  ↓
memory breathing compacted
  ↓
royalty hook created
  ↓
route marked as pending
  ↓
human review required
  ↓
Royalty OS may later process value circulation
```

---

## v0.5 Summary

v0.5 extends Kazene Trace Receipt Protocol by adding Royalty OS Hook.

It defines:

* target types,
* routing signals,
* royalty route values,
* route basis,
* monetization status,
* allocation readiness,
* allocation hints,
* estimated value weight,
* review boundary,
* dispute preparation,
* and links to trace, graph, and memory records.

In short:

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
v0.3 connects receipts into contribution graphs.
v0.4 teaches trace how to breathe.
v0.5 prepares trace for value circulation.
```

Royalty OS Hook is the bridge between structured trace and future value circulation.

It prepares the path.

It does not decide the payout.
