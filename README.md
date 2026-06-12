# mcp-risk-index

Languages: English | [中文](./README.zh-CN.md)

An open risk index for common MCP servers, permissions, commands, and maintenance signals.

## Status

`v0.1.0` - local catalog validation and rendering CLI.

## Purpose

Convert `mcp-audit` rule experience into a reusable public data asset without unsupported claims.

## First Production Surface

Versioned data catalog with evidence-backed entries and a deterministic local CLI.

```bash
python3 -m pip install xone-mcp-risk-index
mcp-risk-index init --output mcp-risk-index.catalog.yml
mcp-risk-index validate --catalog mcp-risk-index.catalog.yml
mcp-risk-index render --catalog mcp-risk-index.catalog.yml --format markdown --output mcp-risk-index.md
mcp-risk-index render --catalog mcp-risk-index.catalog.yml --format json --output mcp-risk-index.json
```

From a source checkout, you can also validate the bundled catalog:

```bash
mcp-risk-index validate --catalog data/catalog.yml
mcp-risk-index render --catalog data/catalog.yml --format markdown --output mcp-risk-index.md
mcp-risk-index render --catalog data/catalog.yml --format json --output mcp-risk-index.json
```

For local development:

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest tests -q
```

## Catalog Contract

The bundled catalog uses `mcp-risk-index.catalog.v1`. Each entry records identity, package, launch command, permissions, maintenance facts, review-level risk signals, evidence, and limitations.

Review levels are prompts for human inspection:

- `info`: useful context
- `review`: inspect before adoption
- `high-review`: require explicit owner approval

They are not safety scores.

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

## Docs

- [Product Foundation](./docs/product-foundation.md)
- [Catalog Design](./docs/superpowers/specs/2026-06-13-catalog-design.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [Production Constraints](./ops/constraints/production.md)
- [Main Entry Constraints](./ops/constraints/main-entry.md)
- [Skill Evolution](./ops/skills/evolution.md)
