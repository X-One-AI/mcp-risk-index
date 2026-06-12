# mcp-risk-index Product Foundation

## Intake

- Priority: P2
- Status: v0.1.0 local catalog CLI
- Positioning: An open risk index for common MCP servers, permissions, commands, and maintenance signals.
- Primary route: Product -> Architecture -> Expert/Security -> QA -> Implementation -> Completion readiness

## PRD

### Problem

Convert mcp-audit rule experience into a reusable public data asset without unsupported claims.

### Users

- Developers adopting AI agents or MCP tools
- Platform, DevTools, Security, and AI infrastructure teams
- Maintainers who need reviewable evidence rather than vague AI automation claims

### Goals

- server identity
- permission profile
- command/package signals
- maintenance signals
- evidence links

### Non-Goals

- no subjective ranking without evidence
- no broad repo health clone
- no security claims without criteria

### Acceptance Criteria

- The project can explain its place in Safe Agent Operations in one sentence.
- The first production surface is local-first or review-first, not a hosted dashboard by default.
- Reports, packets, indexes, or labs must be redaction-safe by design.
- Every risky claim links to evidence, rule logic, or an explicit limitation.
- The first catalog design is documented in `docs/superpowers/specs/2026-06-13-catalog-design.md`.
- Review levels are prompts for human review, not safety scores.
- `mcp-risk-index validate --catalog data/catalog.yml` validates the bundled catalog.
- `mcp-risk-index render` produces Markdown and JSON outputs.
- Invalid unknown signals, missing evidence, and safe/unsafe labels fail validation.

## Architecture Brief

### Boundaries

- Keep shared workflow knowledge in OPT; keep project-specific decisions in this repository.
- Keep the main entrypoint small and explicit.
- Prefer file-based artifacts over hidden services for the first production surface.

### Data Flow

```text
input evidence -> normalize -> redact -> evaluate -> render reviewable artifact
```

### Risks

- Overclaiming safety guarantees.
- Creating generic tooling that weakens the Agentic DevSecOps signal.
- Accepting real secrets or private user data into fixtures.
- Publishing unsupported safe/unsafe claims as if they were verified security facts.

## QA Plan

- Unit-test redaction and normalization before rule or report expansion.
- Add positive and negative fixtures for every behavior boundary.
- Verify generated artifacts do not include raw secrets.
- Keep bilingual README guidance aligned.

## Implementation Plan

1. Keep the first executable surface local-first and deterministic.
2. Use a versioned `mcp-risk-index.catalog.v1` data contract.
3. Require evidence links for every risk signal.
4. Render Markdown and JSON before adding hosted or automated scraping workflows.
5. Use feature branches named `feat/<scope>` or `docs/<scope>`.
6. Use Conventional/Angular commits such as `feat: add catalog schema` or `docs: clarify deferred scope`.
7. Never push directly to `main`; open a pull request from the feature branch.

## Skipped Inputs

- governance model
- initial review group
- usage frequency data
- broader real-world MCP server sample set
