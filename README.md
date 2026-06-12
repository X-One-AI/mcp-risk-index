# mcp-risk-index

Languages: English | [中文](./README.zh-CN.md)

An open risk index for common MCP servers, permissions, commands, and maintenance signals.

## Status

`P2` - catalog design ready for v0.1.0 planning.

## Purpose

Convert mcp-audit rule experience into a reusable public data asset without unsupported claims.

## First Production Surface

Versioned data catalog with evidence-backed entries and review workflow.

The first executable surface is specified in [Catalog Design](./docs/superpowers/specs/2026-06-13-catalog-design.md).

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
