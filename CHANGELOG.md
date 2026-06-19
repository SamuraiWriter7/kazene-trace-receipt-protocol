# Changelog

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
