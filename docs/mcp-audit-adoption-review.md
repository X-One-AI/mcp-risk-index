# MCP Audit Adoption Review

`mcp-risk-index` supports `mcp-audit` by explaining MCP server risk signals during adoption review. It should help reviewers ask better questions after a scan, not replace the scan or become a standalone ranking.

## mcp-audit adoption review path

1. Run mcp-audit first on the repository or team MCP config:

   ```bash
   mcp-audit scan --config ./mcp.json --profile starter --format markdown --output mcp-audit-report.md
   ```

2. Identify server names, launch commands, package managers, permissions, and broad filesystem or network access in the report.
3. Render catalog notes for related MCP servers:

   ```bash
   mcp-risk-index validate --catalog data/catalog.yml --strict
   mcp-risk-index render --catalog data/catalog.yml --format markdown --output mcp-risk-notes.md
   ```

4. Map catalog signals to audit findings. Treat catalog entries as review context, not as allow/deny decisions.
5. Write the adoption decision in the `mcp-audit` baseline review PR or policy exception PR.

## Support asset, not a scoring product

The catalog must remain:

- evidence-backed;
- limited to review prompts;
- explicit about limitations;
- free of safe/unsafe labels, global trust claims, or numeric security scores.

## Product gate

This support asset is production-ready only when:

- it helps explain at least one `mcp-audit` finding or adoption decision;
- every catalog signal has evidence and limitations;
- reviewers can trace a catalog note back to source metadata;
- catalog changes do not create a separate product narrative outside Safe Agent Operations.
