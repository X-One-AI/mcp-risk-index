# MCP Risk Index

Schema: `mcp-risk-index.catalog.v1`

## Filesystem MCP Server

- ID: `filesystem-server`
- Homepage: https://github.com/modelcontextprotocol/servers
- Package: `npx:@modelcontextprotocol/server-filesystem`
- Launch: `npx -y @modelcontextprotocol/server-filesystem /workspace`
- Version pinned: `False`

### Risk Signals

- `filesystem-access` (`review`)
  - Evidence: https://github.com/modelcontextprotocol/servers
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses npx without a pinned package version

### Limitations

- Example entry for schema validation; verify current repository state before production adoption.

## Fetch MCP Server

- ID: `fetch-server`
- Homepage: https://github.com/modelcontextprotocol/servers
- Package: `uvx:mcp-server-fetch`
- Launch: `uvx mcp-server-fetch`
- Version pinned: `False`

### Risk Signals

- `network-access` (`review`)
  - Evidence: https://github.com/modelcontextprotocol/servers
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses uvx without a pinned package version

### Limitations

- Network behavior depends on user prompts and runtime configuration.

## Index Limitations

- Review levels are prompts for human review, not security guarantees.
- Entries are evidence-backed catalog facts, not safe/unsafe labels.
- Maintenance and release signals can change after publication.
