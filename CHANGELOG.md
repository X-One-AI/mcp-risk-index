# Changelog

## 0.3.1

- Add generated reviewer questions to Markdown and JSON catalog renders so risk signals translate into concrete review actions.
- Refresh bundled public sample metadata on 2026-06-14 using public GitHub repository metadata.
- Correct publishing documentation to reflect the existing PyPI and TestPyPI package status.

## 0.3.0

- Expand the bundled catalog to twelve evidence-backed real-world MCP server entries.
- Add high-impact samples covering browser automation, hosted documentation, coding-agent project access, n8n workflow management, database access, and offensive security tooling.

## 0.2.0

- Expand the bundled catalog to six evidence-backed real-world MCP server entries.
- Add strict catalog validation for production review governance fields.
- Add catalog governance and contribution guidance.
- Improve install-to-first-catalog flow with `mcp-risk-index init`.

## 0.1.0

- Add the first `mcp-risk-index.catalog.v1` catalog schema and bundled catalog.
- Add local `mcp-risk-index validate` and `mcp-risk-index render` commands.
- Add Markdown and JSON renderers with non-score, evidence-backed output.
- Add invalid catalog fixtures for unknown signals, missing evidence, and unsupported absolute judgment fields.
- Add bilingual README usage and CI package smoke checks.
