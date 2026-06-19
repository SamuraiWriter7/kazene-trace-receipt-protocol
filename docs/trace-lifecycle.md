# Trace Lifecycle

## Overview

Trace Lifecycle defines how a trace receipt is created, validated, linked, compacted, retained, forgotten, archived, and reviewed.

In v0.1, Kazene Trace Receipt Protocol defined the minimal receipt structure.

In v0.2, the protocol begins to describe how that receipt moves through time.

A trace receipt is not only a static record.

It has a lifecycle.

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

The goal of Trace Lifecycle is to prevent trace records from becoming permanent surveillance logs while preserving the minimum structure needed for accountability, attribution, memory metabolism, and future value circulation.

---

## Why Lifecycle Matters

AI-assisted events are not isolated.

A single event may become part of a longer chain:

```text
read
  ↓
reference
  ↓
generate
  ↓
edit
  ↓
review
  ↓
release
  ↓
archive / forget / royalty review
```

Without lifecycle rules, trace receipts can accumulate as raw historical burden.

With lifecycle rules, trace receipts can be:

* validated,
* linked to parent and child traces,
* compacted after use,
* retained when structurally important,
* forgotten when no longer needed,
* archived for accountability,
* or returned to human review.

This allows trace to breathe.

---

## Lifecycle Principle

```text
Trace should be durable enough for accountability,
but light enough to avoid surveillance.
```

The protocol should preserve:

* event structure,
* source/output hashes,
* permission boundaries,
* privacy settings,
* lifecycle state,
* value-routing hints,
* and human review triggers.

The protocol should avoid preserving:

* unnecessary raw content,
* redundant logs,
* obsolete intermediate chatter,
* sensitive content without need,
* and permanent records without lifecycle justification.

---

## Lifecycle States

v0.2 introduces an explicit lifecycle state.

Recommended field:

```yaml
lifecycle:
  state: "created"
  expires_at: null
  forgetting_action: "compact_after_use"
```

Allowed lifecycle states:

```text
created
validated
linked
compacted
retained
forgotten
archived
reviewed
```

---

## State Definitions

### created

The trace receipt has been created but not yet validated.

Use this state when:

* a new receipt is generated,
* the event has just occurred,
* schema validation has not yet completed,
* or downstream linkage has not yet been confirmed.

Example:

```yaml
lifecycle:
  state: "created"
  expires_at: null
  forgetting_action: "compact_after_use"
```

---

### validated

The trace receipt has passed schema validation.

Use this state when:

* the receipt conforms to the active JSON Schema,
* required fields are present,
* enum values are valid,
* and the receipt can safely enter a trace chain.

Example:

```yaml
lifecycle:
  state: "validated"
  expires_at: null
  forgetting_action: "compact_after_use"
```

---

### linked

The trace receipt has been connected to a parent or child trace.

Use this state when:

* `parent_trace_id` is present,
* `child_traces` contains downstream trace references,
* or the receipt has become part of a trace chain.

Example:

```yaml
parent_trace_id: "trace-2026-06-18-001"
child_traces:
  - "trace-2026-06-18-002"

lifecycle:
  state: "linked"
  expires_at: null
  forgetting_action: "retain"
```

---

### compacted

The trace receipt has been reduced to its useful structural elements.

Use this state when:

* raw or temporary context has been released,
* only hashes and structural metadata remain,
* redundant details have been removed,
* or the receipt has been prepared for long-term retention.

Example:

```yaml
privacy:
  raw_content_stored: false
  reversible: false
  retention: "working"

lifecycle:
  state: "compacted"
  expires_at: null
  forgetting_action: "retain"
```

---

### retained

The trace receipt should be kept because it has durable value.

Use this state when the trace affects:

* authorship,
* attribution,
* safety,
* recurring workflow,
* project architecture,
* value routing,
* or future review.

Example:

```yaml
privacy:
  retention: "long_term"

lifecycle:
  state: "retained"
  expires_at: null
  forgetting_action: "retain"
```

---

### forgotten

The trace receipt has been intentionally released or removed from active memory.

Forgetting does not always mean deletion.

It may mean:

* raw content was deleted,
* temporary metadata was removed,
* the receipt was compacted into a higher-level summary,
* or the trace was downgraded from active use.

Example:

```yaml
privacy:
  retention: "forget_after_use"

lifecycle:
  state: "forgotten"
  expires_at: "2026-07-01T00:00:00Z"
  forgetting_action: "forget_after_use"
```

---

### archived

The trace receipt has been moved to a lower-access archive.

Use this state when:

* the receipt is no longer active,
* but may be needed for future accountability,
* dispute resolution,
* audit,
* or historical reconstruction.

Example:

```yaml
privacy:
  retention: "archive"

lifecycle:
  state: "archived"
  expires_at: null
  forgetting_action: "archive"
```

---

### reviewed

The trace receipt has passed through human review.

Use this state when a human has reviewed the receipt for:

* authorship,
* attribution,
* privacy risk,
* safety boundary,
* legal interpretation,
* value allocation,
* physical-world action,
* or irreversible publication.

Example:

```yaml
review:
  human_review_required: true
  reason: "authorship_and_value"

lifecycle:
  state: "reviewed"
  expires_at: null
  forgetting_action: "retain"
```

---

## Read / Ingest / Reference Events

v0.2 extends `event_type` to include upstream information actions.

Recommended additions:

```text
read
ingest
reference
```

These events are important because AI systems often create value before generation occurs.

The act of reading, ingesting, or referencing a source may affect:

* attribution,
* permission,
* memory routing,
* privacy,
* and future contribution graphs.

---

## Event Type Semantics

### read

Use `read` when a human, AI agent, or tool accesses content without necessarily storing or transforming it.

Example:

```yaml
event_type: "read"
```

Typical use:

```text
AI reads a document before summarizing it.
```

---

### ingest

Use `ingest` when content is absorbed into a system, index, memory layer, dataset, or workflow context.

Example:

```yaml
event_type: "ingest"
```

Typical use:

```text
A document is loaded into a project memory or retrieval context.
```

This event type may require stronger privacy review.

---

### reference

Use `reference` when content is used as a cited, linked, or structurally relevant source for a later transformation.

Example:

```yaml
event_type: "reference"
```

Typical use:

```text
A README section references a prior protocol document.
```

---

## Actor Authority Scope

v0.2 introduces `authority_scope` inside `actor`.

Recommended structure:

```yaml
actor:
  type: "ai_agent"
  id: "agent:example"
  role: "assistant"
  authority_scope: "delegated"
```

Allowed values:

```text
local_only
cloud
delegated
cross_agent
public_agent
restricted
```

---

## Authority Scope Definitions

### local_only

The actor operates only within a local or user-controlled environment.

Use when:

* no cloud execution is involved,
* no external system action is taken,
* and the action remains within the user’s local workspace.

---

### cloud

The actor operates through a cloud service.

Use when:

* a hosted AI model or external compute provider is used,
* data or metadata may leave the local environment,
* or provider-side policy boundaries apply.

---

### delegated

The actor acts with user-granted authority.

Use when:

* the user instructs an AI agent to perform a task,
* the agent has permission to execute bounded actions,
* or the action occurs on behalf of a human.

---

### cross_agent

The actor routes context, memory, or action to another AI agent.

Use when:

* multiple agents interact,
* one agent delegates to another,
* or trace authority crosses wing boundaries.

This should often trigger human review if the trace is sensitive.

---

### public_agent

The actor operates in a public or externally visible context.

Use when:

* outputs are published,
* public systems are affected,
* or downstream audiences may rely on the result.

---

### restricted

The actor operates under limited or sensitive authority.

Use when:

* access is constrained,
* data is sensitive,
* compliance rules apply,
* or action requires strict boundary enforcement.

---

## Source Influence Hint

v0.2 introduces an optional `influence_hint` inside each `source_refs` item.

Recommended structure:

```yaml
source_refs:
  - type: "prompt"
    ref_hash: "sha256:example-source-hash"
    visibility: "private"
    influence_hint: "high"
```

Allowed values:

```text
low
medium
high
critical
```

This is not a final attribution score.

It is only a provisional signal for future contribution graph analysis.

---

## Influence Hint Definitions

### low

The source was lightly consulted or had minimal effect.

### medium

The source informed the event but did not dominate the output.

### high

The source strongly shaped the output, structure, or decision.

### critical

The source was essential to the event and may require attribution, retention, or human review.

---

## Parent and Child Trace Links

Trace receipts can form chains.

Recommended fields:

```yaml
chain_id: "chain-2026-06-18-001"
parent_trace_id: "trace-2026-06-18-001"
child_traces:
  - "trace-2026-06-18-002"
  - "trace-2026-06-18-003"
```

These fields allow simple trace graph construction without requiring a full graph database.

---

## Trace Chain Example

```text
trace-001: read source document
  ↓
trace-002: reference source document
  ↓
trace-003: generate README draft
  ↓
trace-004: edit README
  ↓
trace-005: release v0.2.0-candidate
```

Each receipt remains small.

The chain creates meaning.

---

## Forgetting Actions

v0.2 continues to support lifecycle-aware forgetting.

Allowed values:

```text
retain
compact_after_use
forget_after_use
archive
human_review
```

---

## Forgetting Action Definitions

### retain

Keep the receipt in its current form.

Use when:

* the receipt is structurally important,
* it affects attribution,
* or it may be needed for future validation.

---

### compact_after_use

Reduce the receipt after the active workflow ends.

Use when:

* the trace is useful now,
* but raw or detailed context should not remain active,
* or only summary metadata should be retained later.

---

### forget_after_use

Release the receipt after use.

Use when:

* the trace is temporary,
* the event has no durable value,
* or retaining the receipt would create unnecessary privacy risk.

---

### archive

Move the receipt to archive.

Use when:

* it is no longer active,
* but may be needed for audit, dispute, or historical reconstruction.

---

### human_review

Return the lifecycle decision to a human.

Use when:

* authorship is unclear,
* value allocation may be affected,
* privacy risk exists,
* safety boundaries are involved,
* or the consequence is irreversible.

---

## Human Review Boundary

Trace lifecycle automation must not silently resolve critical matters.

Human review is required when lifecycle decisions involve:

* authorship,
* ownership,
* attribution,
* royalty routing,
* legal interpretation,
* financial consequence,
* privacy risk,
* safety boundary,
* physical-world action,
* cross-agent authority,
* irreversible publication,
* or disputed contribution.

The lifecycle system may recommend.

It must not silently decide.

---

## Relationship to Memory Breathing

Trace Lifecycle connects directly to memory metabolism.

```text
Trace Receipt
  ↓
Lifecycle State
  ↓
Retention / Compaction / Forgetting
  ↓
Memory Breathing
  ↓
Implicit Guidance or Archive
```

This makes Trace Lifecycle compatible with:

* Kazene Memory Breathing Protocol,
* 風の記憶丸,
* 構造反芻丸,
* and Royalty OS.

---

## v0.2 Summary

v0.2 extends Trace Receipt Core by adding:

* read/reference/ingest event semantics,
* explicit lifecycle states,
* actor authority scope,
* source influence hints,
* stronger parent-child trace semantics,
* and clearer forgetting actions.

In short:

```text
v0.1 records the receipt.
v0.2 gives the receipt a lifecycle.
```

Trace is not a static archive.

Trace is a living boundary between memory, attribution, privacy, and value circulation.
