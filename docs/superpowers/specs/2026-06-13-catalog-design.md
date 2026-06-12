# mcp-risk-index Catalog Design

## Status

Proposed for v0.1.0 implementation planning.

## Product Decision

`mcp-risk-index` is an evidence-backed catalog, not a subjective leaderboard. It should help teams understand common MCP server permission, command, package, and maintenance signals without claiming that a listed server is safe or unsafe in absolute terms.

## Problem

Teams adopting MCP servers need a reusable reference for risk-relevant facts: what the server can access, how it is launched, whether packages are pinned, what maintenance signals exist, and which evidence supports each statement. Raw opinions or unsupported scores would damage trust and create legal/security overclaim risk.

## Users

- Developers choosing MCP servers for local or team workflows.
- Platform and AI infrastructure teams curating allowed MCP configurations.
- Security and DevSecOps teams reviewing permissions and supply-chain exposure.
- Maintainers who want transparent, evidence-based notes rather than opaque labels.

## Goals

- Maintain a versioned catalog schema for MCP server entries.
- Require evidence for every risk-relevant signal.
- Separate factual signals from derived review notes.
- Provide local validation before entries are merged.
- Render a concise Markdown index and machine-readable JSON.
- Support future use by `mcp-audit` rules without coupling releases.

## Non-Goals

- No subjective overall ranking in v0.1.0.
- No hosted dashboard.
- No claim that a server is safe, unsafe, compliant, or malicious.
- No broad repository health scoring unrelated to MCP usage.
- No automated scraping until governance and source-of-truth policy are explicit.

## Catalog Schema

The first catalog file is `data/catalog.yml` with:

- `schema_version`: `mcp-risk-index.catalog.v1`
- `generated_at`: optional ISO timestamp for rendered artifacts
- `entries`: list of MCP server entries

Each entry contains:

- `id`: stable lowercase slug
- `name`: human-readable server name
- `homepage`: source URL
- `package`: package manager and package name when applicable
- `launch`: command and whether versions are pinned
- `permissions`: filesystem, network, environment, process, or custom access notes
- `maintenance`: repository activity and release signals as facts
- `risk_signals`: list of signal IDs with severity-like levels limited to `info`, `review`, or `high-review`
- `evidence`: URLs or local notes backing each signal
- `limitations`: what the catalog cannot conclude

## Signal Model

Allowed initial signal IDs:

- `filesystem-access`
- `network-access`
- `env-access`
- `process-exec`
- `unpinned-launch`
- `low-maintenance-signal`
- `sensitive-domain-access`

Signal levels are review prompts, not safety scores:

- `info`: useful context
- `review`: reviewer should inspect before adoption
- `high-review`: strong reason for explicit owner approval

## First Production Surface

Local CLI:

```bash
mcp-risk-index validate --catalog data/catalog.yml
mcp-risk-index render --catalog data/catalog.yml --format markdown --output mcp-risk-index.md
mcp-risk-index render --catalog data/catalog.yml --format json --output mcp-risk-index.json
```

## Architecture

```text
catalog.yml -> parse -> schema validate -> signal validate -> render Markdown/JSON
```

Modules for v0.1.0:

- `schema`: schema version and allowed signal validation.
- `catalog`: load entries into typed data structures.
- `renderers`: Markdown and JSON output.
- `cli`: `validate` and `render`.

## Security And Trust Gate

Decision: revise if implementation allows unsupported claims.

Required controls:

- Every `risk_signal` must reference evidence.
- Rendered output must include limitations and non-score language.
- Unknown signal IDs fail validation.
- Entries cannot use `safe`, `unsafe`, `score`, `critical`, or `trusted` as top-level judgment fields.
- Fixtures must avoid claims about real projects unless evidence URLs are present.

Residual risk:

- Evidence links can become stale.
- Maintenance signals can change after catalog publication.
- Review level is a prompt for human review, not a security guarantee.

## QA Plan

- Validate a good catalog fixture.
- Reject unsupported schema versions.
- Reject unknown signal IDs.
- Reject risk signals without evidence.
- Reject score-like or absolute safety fields.
- Snapshot Markdown rendering for a small catalog.
- Keep README and README.zh-CN aligned.

## Implementation Batches

1. Package scaffold and docs alignment tests.
2. Catalog fixtures and schema validation.
3. Markdown and JSON renderers.
4. CLI `validate` and `render` commands.
5. Bilingual README usage, changelog, manifest, CI package checks.
6. Release artifacts and post-release wheel verification.

## Acceptance Criteria

- `python3 -m pytest tests -q` passes.
- `mcp-risk-index validate --catalog data/catalog.yml` validates the bundled catalog.
- `mcp-risk-index render` produces Markdown and JSON.
- Invalid unsupported claims fail validation.
- README and README.zh-CN include aligned install, usage, non-goals, and limitations.
- CI installs the package and runs CLI smoke checks.
- A release can ship wheel and sdist artifacts.

## Open Inputs Recorded Elsewhere

The following should not block v0.1.0:

- Governance model for accepting public entries.
- Initial maintainer review group.
- Real-world usage frequency data.
- Automated source-of-truth policy for changing maintenance signals.

