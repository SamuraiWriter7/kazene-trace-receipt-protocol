# Memory Breathing Integration

## Overview

Memory Breathing Integration defines how trace receipts and contribution graphs connect to memory metabolism.

In v0.1, Kazene Trace Receipt Protocol defined the minimal trace receipt.

In v0.2, the protocol added lifecycle-aware trace management.

In v0.3, the protocol connected multiple trace receipts into contribution graphs.

In v0.4, the protocol connects trace and graph structures to memory breathing.

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
v0.3 connects receipts into contribution graphs.
v0.4 decides how trace should be retained, compacted, forgotten, archived, or reviewed.
```

The purpose of v0.4 is not to remember everything.

The purpose is to remember less, but better.

---

## Why Memory Breathing Matters

Trace systems can easily become overwhelming.

If every prompt, read event, edit, reference, graph edge, validation, and release is preserved forever, the protocol becomes a burden.

A healthy trace system needs memory metabolism.

It must decide:

* what should be retained,
* what should be compacted,
* what should be forgotten,
* what should be archived,
* what should become implicit guidance,
* and what should return to human review.

Memory Breathing Integration prevents trace from becoming surveillance, clutter, or cognitive overload.

---

## Core Principle

```text
Memory is not storage.
Memory is metabolism.

Trace is not burden.
Trace is material for structured memory.

Forgetting is not loss.
Forgetting is lifecycle control.

Compaction is not erasure.
Compaction is transformation.

Human review is not a bottleneck.
It is the boundary that prevents memory automation from becoming unchecked authority.
```

---

## Memory Breathing Layers

v0.4 uses five memory layers.

```text
short_term
working
long_term
implicit
archive
```

---

## Layer Definitions

### short_term

Use for immediate task context.

Examples:

* current request,
* active prompt,
* current file,
* latest validation result,
* temporary trace chain,
* immediate decision.

Typical lifetime:

```text
minutes_to_hours
```

Recommended actions:

```text
retain_temporarily
compact_after_use
forget_after_use
```

---

### working

Use for active project or release-cycle context.

Examples:

* current repository state,
* current version,
* current schema/example/validator alignment,
* active contribution graph,
* unresolved issue,
* ongoing release workflow.

Typical lifetime:

```text
days_to_weeks
```

Recommended actions:

```text
retain
compact
review_later
archive_after_release
```

---

### long_term

Use for durable structures and recurring patterns.

Examples:

* core protocol architecture,
* stable design principles,
* recurring validation patterns,
* authorship or attribution boundaries,
* safety constraints,
* durable workflow decisions.

Typical lifetime:

```text
months_to_years
```

Recommended actions:

```text
retain
archive
convert_to_rule
human_review
```

---

### implicit

Use for behavioral posture rather than explicit recalled facts.

Examples:

* prefer hash over raw content,
* avoid surveillance-by-default,
* keep human review for critical decisions,
* preserve authorship boundaries,
* compact raw trace into reusable structure,
* avoid over-retention.

Recommended actions:

```text
convert_to_guidance
apply_as_response_posture
do_not_treat_as_hidden_authority
```

---

### archive

Use for inactive but accountability-relevant trace.

Examples:

* release records,
* validation-passing candidates,
* public publication trace,
* reviewed contribution graphs,
* dispute-preparation records,
* high-impact authorship or attribution chains.

Recommended actions:

```text
archive
retain_low_access
review_on_request
```

---

## Memory Actions

v0.4 introduces explicit memory actions.

Recommended values:

```text
retain
compact
forget
archive
review
implicit
convert_to_rule
```

---

## Action Definitions

### retain

Keep the trace or graph in active memory.

Use when:

* it is needed for ongoing work,
* it affects current release state,
* it supports validation,
* or it is part of active project context.

---

### compact

Reduce the trace or graph to its reusable structure.

Use when:

* raw detail is no longer needed,
* the important pattern has been extracted,
* the trace should remain useful without remaining bulky,
* or the graph should be summarized for future use.

---

### forget

Release the trace from active memory.

Use when:

* it was temporary,
* it has no durable value,
* retaining it creates privacy or cognitive burden,
* or the useful structure has already been extracted.

Forgetting should not erase accountability-sensitive records without review.

---

### archive

Move the trace or graph to low-access storage.

Use when:

* it is no longer active,
* but may be needed for audit,
* release history,
* attribution review,
* dispute preparation,
* or historical reconstruction.

---

### review

Return the memory decision to a human.

Use when memory decisions involve:

* authorship,
* attribution,
* royalty routing,
* legal interpretation,
* privacy risk,
* safety boundary,
* physical-world action,
* irreversible publication,
* disputed contribution,
* or cross-agent authority.

---

### implicit

Transform the trace into behavioral guidance.

Use when the specific event does not need to be remembered, but the lesson should shape future action.

Example:

```text
Do not preserve raw logs when hash-based receipt is sufficient.
```

---

### convert_to_rule

Convert a repeated pattern into an explicit recurrence rule.

Use when:

* an error repeats,
* a validation failure pattern is discovered,
* a release workflow rule is needed,
* or a structural lesson should become executable practice.

This action connects Memory Breathing Integration to structural rumination systems.

---

## Memory Breathing Object

v0.4 introduces an optional `memory_breathing` object.

Recommended structure:

```yaml
memory_breathing:
  memory_id: "memory-2026-06-19-001"
  version: "0.4.0"
  created_at: "2026-06-19T08:30:00Z"

  target:
    target_type: "contribution_graph"
    target_id: "graph-2026-06-19-001"

  memory_layer: "working"
  memory_action: "compact"
  memory_weight: "high"

  reason: "release_cycle_trace_should_be_compacted_after_validation"

  retention:
    retain_until: null
    review_after: "2026-07-19T00:00:00Z"
    archive_after: null

  compaction:
    compacted_summary_ref: "summary:trace-graph-v0.3"
    raw_trace_retained: false
    structural_pattern_retained: true

  review:
    human_review_required: false
    reason: "none"
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
release_record
validation_record
rumination_record
```

### trace_receipt

Use when the memory decision applies to one trace receipt.

### contribution_graph

Use when the memory decision applies to an entire contribution graph.

### trace_chain

Use when the memory decision applies to a sequence of linked trace receipts.

### graph_edge

Use when the memory decision applies to a relationship between two traces.

### graph_node

Use when the memory decision applies to one node in a contribution graph.

### release_record

Use when the memory decision applies to a release or candidate milestone.

### validation_record

Use when the memory decision applies to schema/example/CI validation evidence.

### rumination_record

Use when the memory decision applies to a failure analysis or recurrence-prevention record.

---

## Memory Weight

v0.4 uses four memory weights.

```text
low
medium
high
critical
```

### low

Use for temporary or one-time details.

Typical actions:

```text
forget
compact
```

### medium

Use for active project context.

Typical actions:

```text
retain
compact
archive_after_release
```

### high

Use for durable structures, repeated patterns, or important design decisions.

Typical actions:

```text
retain
archive
convert_to_rule
```

### critical

Use when memory affects authorship, attribution, safety, value routing, legal interpretation, privacy, or irreversible external action.

Typical actions:

```text
review
archive
retain_with_human_boundary
```

Critical memory should not be silently forgotten or rewritten.

---

## Retention Policy

Memory Breathing Integration supports retention timing.

Recommended fields:

```yaml
retention:
  retain_until: null
  review_after: "2026-07-19T00:00:00Z"
  archive_after: null
```

### retain_until

Optional timestamp until which the memory should remain active.

### review_after

Optional timestamp after which memory should be reviewed.

### archive_after

Optional timestamp after which memory should move to archive.

---

## Compaction Policy

Compaction should preserve structure while reducing burden.

Recommended fields:

```yaml
compaction:
  compacted_summary_ref: "summary:trace-graph-v0.3"
  raw_trace_retained: false
  structural_pattern_retained: true
```

Compaction should preserve:

* root cause,
* contribution lineage,
* review boundary,
* validation status,
* durable design choice,
* recurrence pattern,
* and release significance.

Compaction should release:

* duplicate logs,
* temporary troubleshooting chatter,
* obsolete assumptions,
* raw prompt noise,
* redundant trace details,
* and nonessential intermediate state.

---

## Human Review Boundary

Memory decisions must return to human review when they involve:

* authorship,
* attribution,
* value allocation,
* royalty routing,
* legal interpretation,
* privacy risk,
* safety boundary,
* physical-world action,
* irreversible publication,
* disputed contribution,
* cross-agent authority,
* identity-sensitive context,
* or deletion of accountability-sensitive trace.

Recommended structure:

```yaml
review:
  human_review_required: true
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
legal_interpretation
physical_world_action
irreversible_publication
disputed_contribution
cross_agent_authority
memory_retention
trace_deletion
other
```

---

## Relationship to Trace Receipt

Trace Receipt records a single event.

Memory Breathing decides how that event should live in memory.

```text
Trace Receipt
  ↓
Memory Breathing
  ↓
retain / compact / forget / archive / review / implicit / convert_to_rule
```

---

## Relationship to Trace Lifecycle

Trace Lifecycle describes the state of a trace receipt.

Memory Breathing decides how the trace should be treated as memory.

```text
created / validated / linked / compacted / retained / forgotten / archived / reviewed
  ↓
memory action
  ↓
memory layer
```

---

## Relationship to Contribution Graph

Contribution Graph connects trace receipts.

Memory Breathing decides which parts of the graph matter.

```text
Contribution Graph
  ↓
critical nodes retained
  ↓
low-value edges compacted
  ↓
temporary nodes forgotten
  ↓
release-sensitive paths archived
  ↓
attribution-sensitive edges reviewed
```

---

## Relationship to 風の記憶丸

風の記憶丸 is the GPT-level execution layer for this protocol.

It helps decide:

* what to remember,
* what to compact,
* what to forget,
* what to archive,
* what to convert into implicit guidance,
* what to convert into recurrence rules,
* and what to return to human review.

```text
Kazene Trace Receipt Protocol
  ↓
Contribution Graph
  ↓
Memory Breathing Integration
  ↓
風の記憶丸
```

---

## Relationship to 構造反芻丸

構造反芻丸 connects to the `convert_to_rule` action.

When a trace or graph reveals a repeated failure, validation issue, mismatch, or structural error, it may become a recurrence-prevention rule.

```text
failure trace
  ↓
structural rumination
  ↓
recurrence pattern
  ↓
convert_to_rule
  ↓
future validation gate
```

---

## Relationship to Royalty OS

Memory Breathing does not calculate royalties.

However, it helps prepare clean inputs for Royalty OS by deciding which traces, graph nodes, and contribution paths should be preserved for future value review.

```text
Trace Receipt
  ↓
Contribution Graph
  ↓
Memory Breathing
  ↓
Royalty OS Hook
```

The cleaner the memory layer, the safer the value-routing layer becomes.

---

## Example Flow

```text
trace receipt created
  ↓
trace lifecycle validated
  ↓
contribution graph generated
  ↓
memory breathing applied
  ↓
low-value nodes compacted
  ↓
critical release path archived
  ↓
attribution-sensitive edge reviewed
  ↓
royalty preparation remains pending
```

---

## v0.4 Summary

v0.4 extends Kazene Trace Receipt Protocol by adding Memory Breathing Integration.

It defines:

* memory layers,
* memory actions,
* memory weights,
* retention policy,
* compaction policy,
* target types,
* human review boundaries,
* and integration with 風の記憶丸, 構造反芻丸, and Royalty OS.

In short:

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
v0.3 connects receipts into contribution graphs.
v0.4 teaches trace how to breathe.
```

Trace should not accumulate endlessly.

Trace should breathe.
