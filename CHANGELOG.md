# Changelog

## [v0.5.0-candidate] - 2026-06-19

### Added

* Added `docs/royalty-os-hook.md`.
* Added `schemas/royalty-os-hook.schema.json`.
* Added `examples/royalty-os-hook.example.yaml`.
* Updated `scripts/validate_examples.py` to validate:

  * Trace Receipt Core
  * Trace Receipt Lifecycle
  * Contribution Graph Seed
  * Memory Breathing Integration
  * Royalty OS Hook
* Added the initial **Royalty OS Hook** layer.

### Defined

* Defined the top-level `royalty_os_hook` object.
* Defined royalty hook target types:

  * `trace_receipt`
  * `contribution_graph`
  * `trace_chain`
  * `graph_edge`
  * `graph_node`
  * `memory_breathing_record`
  * `release_record`
  * `publication_record`
* Defined royalty route values:

  * `none`
  * `pending`
  * `direct`
  * `pool`
  * `human_review`
  * `blocked`
* Defined route basis values:

  * `trace_receipt`
  * `trace_lifecycle`
  * `contribution_graph`
  * `memory_breathing`
  * `manual_review`
  * `external_policy`
* Defined monetization status values:

  * `not_applicable`
  * `not_calculated`
  * `eligible`
  * `ineligible`
  * `pending_review`
  * `blocked`
* Defined allocation modes:

  * `not_assigned`
  * `direct_candidate`
  * `pool_candidate`
  * `manual_review_required`
  * `blocked`
* Defined allocation hints:

  * `none`
  * `direct_candidate`
  * `pool_candidate`
  * `review_candidate`
  * `dispute_candidate`
  * `blocked`
* Defined estimated value weights:

  * `low`
  * `medium`
  * `high`
  * `critical`
* Defined dispute status values:

  * `none`
  * `possible`
  * `active`
  * `resolved`
  * `blocked`
* Defined optional dispute reasons:

  * `none`
  * `authorship`
  * `attribution`
  * `value_allocation`
  * `license_conflict`
  * `privacy_risk`
  * `consent_denied`
  * `external_policy`
  * `other`
* Defined links to:

  * trace receipts
  * contribution graphs
  * memory breathing records
  * release records
  * publication records

### Validation

* Confirmed that `examples/trace-receipt.example.yaml` passes validation.
* Confirmed that `examples/trace-receipt-lifecycle.example.yaml` passes validation.
* Confirmed that `examples/contribution-graph.example.yaml` passes validation.
* Confirmed that `examples/memory-breathing.example.yaml` passes validation.
* Confirmed that `examples/royalty-os-hook.example.yaml` passes validation.
* Confirmed GitHub Actions validation passes.

### Design Principles

* Established that Royalty OS Hook is not a payment engine.
* Established that royalty routing is value-circulation readiness, not final allocation.
* Established that attribution is a review signal, not automatic ownership.
* Established that influence is a graph hint, not entitlement.
* Established that monetization status is preliminary and reviewable.
* Established that dispute preparation must be explicit.
* Established that blocked routing must be representable.
* Established the rule: no final value allocation without human review.
* Connected Trace Receipt, Trace Lifecycle, Contribution Graph, Memory Breathing, and Royalty OS into one staged protocol path.

### Status

* Status: `v0.5.0-candidate`
* Layer: `Royalty OS Hook`
* Validation: Passing
* Maturity: Draft protocol candidate


## [v0.4.0-candidate] - 2026-06-19

### Added

* Added `docs/memory-breathing-integration.md`.
* Added `schemas/memory-breathing.schema.json`.
* Added `examples/memory-breathing.example.yaml`.
* Updated `scripts/validate_examples.py` to validate:

  * Trace Receipt Core
  * Trace Receipt Lifecycle
  * Contribution Graph Seed
  * Memory Breathing Integration
* Added the initial **Memory Breathing Integration** layer.

### Defined

* Defined memory layers:

  * `short_term`
  * `working`
  * `long_term`
  * `implicit`
  * `archive`
* Defined memory actions:

  * `retain`
  * `compact`
  * `forget`
  * `archive`
  * `review`
  * `implicit`
  * `convert_to_rule`
* Defined memory weights:

  * `low`
  * `medium`
  * `high`
  * `critical`
* Defined memory target types:

  * `trace_receipt`
  * `contribution_graph`
  * `trace_chain`
  * `graph_edge`
  * `graph_node`
  * `release_record`
  * `validation_record`
  * `rumination_record`
* Defined retention policy fields:

  * `retain_until`
  * `review_after`
  * `archive_after`
* Defined compaction policy fields:

  * `compacted_summary_ref`
  * `raw_trace_retained`
  * `structural_pattern_retained`
* Defined memory review boundary fields:

  * `human_review_required`
  * `reason`
* Defined optional links to:

  * trace receipts
  * contribution graphs
  * rumination records
  * royalty hooks

### Validation

* Confirmed that `examples/trace-receipt.example.yaml` passes validation.
* Confirmed that `examples/trace-receipt-lifecycle.example.yaml` passes validation.
* Confirmed that `examples/contribution-graph.example.yaml` passes validation.
* Confirmed that `examples/memory-breathing.example.yaml` passes validation.
* Confirmed GitHub Actions validation passes.

### Design Principles

* Established that trace should not accumulate endlessly.
* Established that memory is not storage, but metabolism.
* Established that forgetting is not loss, but lifecycle control.
* Established that compaction is not erasure, but transformation.
* Established that critical memory decisions require human review.
* Established that low-value trace can be compacted or forgotten after useful structure is extracted.
* Established that high-value trace can be retained, archived, or converted into recurrence rules.
* Established that Memory Breathing Integration connects Trace Receipt, Trace Lifecycle, Contribution Graph, 風の記憶丸, 構造反芻丸, and Royalty OS.

### Status

* Status: `v0.4.0-candidate`
* Layer: `Memory Breathing Integration`
* Validation: Passing
* Maturity: Draft protocol candidate


## [v0.2.0-candidate] - 2026-06-19

### Added

* Added `docs/trace-lifecycle.md`.
* Added `examples/trace-receipt-lifecycle.example.yaml`.
* Updated `schemas/trace-receipt.schema.json` for v0.2 lifecycle support.
* Updated `scripts/validate_examples.py` to validate both:

  * Trace Receipt Core example
  * Trace Receipt Lifecycle example
* Added lifecycle-aware trace semantics.

### Extended

* Extended `event_type` with upstream information actions:

  * `read`
  * `ingest`
  * `reference`
* Extended `actor` with:

  * `authority_scope`
* Extended `source_refs` with:

  * `influence_hint`
* Extended `lifecycle` with:

  * `state`
* Extended `transformation.output_hash` to allow `null` for read-only events.
* Extended `transformation.derivative_level` with:

  * `none`
* Extended `contribution.contribution_type` with:

  * `source_reference`
  * `reading`
  * `ingestion`
* Extended `review.reason` with:

  * `source_ingestion`
  * `authority_scope`
  * `trace_lifecycle`
  * `memory_retention`

### Defined

* Defined explicit lifecycle states:

  * `created`
  * `validated`
  * `linked`
  * `compacted`
  * `retained`
  * `forgotten`
  * `archived`
  * `reviewed`
* Defined actor authority scopes:

  * `local_only`
  * `cloud`
  * `delegated`
  * `cross_agent`
  * `public_agent`
  * `restricted`
* Defined source influence hints:

  * `low`
  * `medium`
  * `high`
  * `critical`
* Defined trace lifecycle behavior for:

  * reading
  * ingestion
  * reference
  * validation
  * linking
  * compaction
  * retention
  * forgetting
  * archiving
  * human review

### Validation

* Confirmed that `examples/trace-receipt.example.yaml` passes validation.
* Confirmed that `examples/trace-receipt-lifecycle.example.yaml` passes validation.
* Confirmed GitHub Actions validation passes.

### Design Principles

* Established that AI trace begins before generation, at the point of reading, ingestion, or reference.
* Established that actor authority boundaries should be recorded explicitly.
* Established that source-level influence should be captured as a provisional hint, not a final attribution score.
* Established that trace receipts should have lifecycle states rather than remaining static records.
* Reinforced that forgetting, compaction, archive, and human review are first-class trace lifecycle operations.

### Status

* Status: `v0.2.0-candidate`
* Layer: `Trace Lifecycle`
* Validation: Passing
* Maturity: Draft protocol candidate


All notable changes to this project will be documented in this file.

This project follows a candidate-based release flow for early protocol development.

---

## [v0.1.0-candidate] - 2026-06-18

### Added

* Added initial `README.md` defining **Kazene Trace Receipt Protocol**.
* Added `schemas/trace-receipt.schema.json`.
* Added `examples/trace-receipt.example.yaml`.
* Added `scripts/validate_examples.py`.
* Added `.github/workflows/validate-examples.yml`.
* Added GitHub Actions validation for schema/example consistency.
* Added the initial **Trace Receipt Core** model.

### Defined

* Defined a minimal structured receipt for AI-assisted creation, transformation, routing, and derivative events.
* Defined the top-level `trace_receipt` object.
* Defined core receipt metadata:

  * `id`
  * `version`
  * `timestamp`
  * `event_type`
  * `chain_id`
  * `parent_trace_id`
  * `child_traces`
* Defined actor metadata:

  * `type`
  * `id`
  * `role`
* Defined source reference metadata:

  * `type`
  * `ref_hash`
  * `visibility`
* Defined transformation metadata:

  * `intent`
  * `method`
  * `model_or_tool`
  * `model_version`
  * `compute_provider`
  * `output_hash`
  * `derivative_level`
* Defined contribution hints:

  * `contribution_type`
  * `weight_hint`
  * `estimated_influence`
* Defined permission fields:

  * `usage_scope`
  * `consent_status`
  * `license_ref`
* Defined privacy fields:

  * `raw_content_stored`
  * `reversible`
  * `retention`
  * `zero_knowledge_proof`
* Defined lifecycle fields:

  * `expires_at`
  * `forgetting_action`
* Defined future value-routing hook:

  * `royalty_route`
  * `attribution_required`
* Defined human review boundary:

  * `human_review_required`
  * `reason`

### Validation

* Added JSON Schema validation using Draft 2020-12.
* Added YAML example validation using `PyYAML`.
* Added validation script using `jsonschema`.
* Confirmed that `examples/trace-receipt.example.yaml` passes validation against `schemas/trace-receipt.schema.json`.
* Confirmed GitHub Actions validation passes.

### Design Principles

* Established that trace receipts should not store raw content by default.
* Established hash-based source and output references as the default pattern.
* Established trace lifecycle and forgetting as first-class protocol concerns.
* Established that contribution hints are not final royalty or legal judgments.
* Established human review as the boundary for authorship, attribution, privacy, safety, and value-sensitive decisions.

### Status

* Status: `v0.1.0-candidate`
* Layer: `Trace Receipt Core`
* Validation: Passing
* Maturity: Draft protocol candidate

---

## Roadmap

### v0.2 — Trace Lifecycle

Planned focus:

* Clarify trace lifecycle states.
* Strengthen `parent_trace_id` and `child_traces` semantics.
* Add more explicit expiration and forgetting behavior.
* Define lifecycle transition rules:

  * created
  * validated
  * linked
  * compacted
  * retained
  * forgotten
  * archived
  * reviewed

### v0.3 — Contribution Graph Seed

Planned focus:

* Define lightweight contribution graph structure.
* Connect multiple trace receipts into trace chains.
* Improve influence hints.
* Add source-output relationship mapping.
* Add review triggers for disputed or high-impact contribution chains.

### v0.4 — Memory Breathing Integration

Planned focus:

* Connect trace receipts to memory metabolism.
* Support retention, compaction, forgetting, archive, and implicit memory routing.
* Integrate with Kazene Memory Breathing Protocol and 風の記憶丸.

### v0.5 — Royalty OS Hook

Planned focus:

* Add preliminary value-circulation hooks.
* Connect trace receipts to Royalty OS.
* Prepare attribution and royalty routing review.
* Add dispute-preparation fields without calculating final payment.
