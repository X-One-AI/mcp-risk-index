# mcp-risk-index

Languages: English | [中文](./README.zh-CN.md)

An open risk index for common MCP servers, permissions, commands, and maintenance signals.

## Status

`v0.3.1` - evidence-backed catalog rendering with reviewer questions, strict review checks, and refreshed public sample metadata.

## Purpose

Convert `mcp-audit` rule experience into a reusable public data asset without unsupported claims.

## First Production Surface

Versioned data catalog with evidence-backed entries and a deterministic local CLI.

From PyPI:

```bash
python3 -m pip install xone-mcp-risk-index
mcp-risk-index init --output mcp-risk-index.catalog.yml
mcp-risk-index validate --catalog mcp-risk-index.catalog.yml --strict
mcp-risk-index render --catalog mcp-risk-index.catalog.yml --format markdown --output mcp-risk-index.md
mcp-risk-index render --catalog mcp-risk-index.catalog.yml --format json --output mcp-risk-index.json
```

From Homebrew:

```bash
brew install x-one-ai/tap/mcp-risk-index
mcp-risk-index --version
```

From a source checkout, you can also validate the bundled catalog:

```bash
mcp-risk-index validate --catalog data/catalog.yml --strict
mcp-risk-index render --catalog data/catalog.yml --format markdown --output mcp-risk-index.md
mcp-risk-index render --catalog data/catalog.yml --format json --output mcp-risk-index.json
```

For local development:

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest tests -q
```

## Catalog Contract

The bundled catalog uses `mcp-risk-index.catalog.v1`. Each entry records identity, package, launch command, permissions, maintenance facts, review-level risk signals, evidence, and limitations. Rendered Markdown and JSON also include reviewer questions derived from the evidence-backed signals.

Review levels are prompts for human inspection:

- `info`: useful context
- `review`: inspect before adoption
- `high-review`: require explicit owner approval

They are not safety scores.

Strict validation requires production review governance fields such as `maintenance.source_checked_at` and a GitHub repository source.

## Required Evidence

- server identity
- permission profile
- command/package signals
- maintenance signals
- evidence links

## Non-Goals

- no subjective ranking without evidence
- no broad repo health clone
- no security claims without criteria
- no absolute safe/unsafe labels

## OPT Operating Model

This project references the shared One Person Team workflow through [ops/opt-overlay.md](./ops/opt-overlay.md). Project-specific constraints live under [ops/constraints](./ops/constraints), and evolvable local skills live under [ops/skills](./ops/skills).

## Blocked Inputs

Inputs that require user or real-world data are recorded in `../x-one-skipped-inputs.md` and should not block foundation work.

Real-user feedback should be classified as false-positive, false-negative, adapter-request, scenario-request, or catalog-update when it applies; portfolio-level handling is tracked in X-One portfolio health docs.

## Docs

- [Product Foundation](./docs/product-foundation.md)
- [Catalog Governance](./docs/catalog-governance.md)
- [MCP Audit Adoption Review](./docs/mcp-audit-adoption-review.md)
- [Risk Context Note](./docs/risk-context-note.md)
- [Publishing](./docs/publishing.md)
- [Homebrew Packaging](./docs/homebrew.md)
- [Catalog Design](./docs/superpowers/specs/2026-06-13-catalog-design.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [Production Constraints](./ops/constraints/production.md)
- [Main Entry Constraints](./ops/constraints/main-entry.md)
- [Skill Evolution](./ops/skills/evolution.md)
