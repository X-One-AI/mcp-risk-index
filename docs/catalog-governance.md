# Catalog Governance

## Purpose

`mcp-risk-index` publishes evidence-backed MCP server signals for review workflows. It does not publish security guarantees, trust labels, or global rankings.

## Entry Requirements

Every catalog entry must include:

- stable `id`
- server `name`
- `homepage`
- `package`
- `launch`
- `permissions`
- `maintenance.repository`
- `maintenance.source_checked_at`
- at least one `risk_signals` item
- evidence for every risk signal
- at least one limitation

## Strict Validation

Run strict validation before proposing catalog changes:

```bash
mcp-risk-index validate --catalog data/catalog.yml --strict
```

Strict mode requires `source_checked_at` and a GitHub repository URL so reviewers can reason about freshness and provenance.

## Review Policy

- No safe/unsafe labels.
- No overall security scores.
- No claims that a server is malicious, compliant, trusted, or approved.
- Use `info`, `review`, or `high-review` only as prompts for human inspection.
- Add limitations when runtime behavior depends on token scopes, client configuration, browser profile, filesystem path, network destination, or user prompts.

## Evidence Freshness

`source_checked_at` records when a maintainer checked public source metadata. It is not a freshness guarantee. Entries with stale evidence should be revised, weakened, or removed.

## OPT Link

This governance document is project-specific. Shared workflow and role practice remain in OPT; catalog policy and local review constraints live in this repository.
