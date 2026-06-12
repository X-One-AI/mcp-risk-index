# MCP Risk Index

Schema: `mcp-risk-index.catalog.v1`

## Filesystem MCP Server

- ID: `filesystem-server`
- Homepage: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- Package: `npx:@modelcontextprotocol/server-filesystem`
- Launch: `npx -y @modelcontextprotocol/server-filesystem /workspace`
- Version pinned: `False`

### Risk Signals

- `filesystem-access` (`review`)
  - Evidence: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses npx without a pinned package version

### Limitations

- Catalog records command and permission signals only; verify current package release and allowed paths before production adoption.

## Fetch MCP Server

- ID: `fetch-server`
- Homepage: https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- Package: `uvx:mcp-server-fetch`
- Launch: `uvx mcp-server-fetch`
- Version pinned: `False`

### Risk Signals

- `network-access` (`review`)
  - Evidence: https://github.com/modelcontextprotocol/servers/tree/main/src/fetch
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses uvx without a pinned package version

### Limitations

- Network destinations depend on user prompts, client policy, and runtime configuration.

## Git MCP Server

- ID: `git-server`
- Homepage: https://github.com/modelcontextprotocol/servers/tree/main/src/git
- Package: `uvx:mcp-server-git`
- Launch: `uvx mcp-server-git`
- Version pinned: `False`

### Risk Signals

- `filesystem-access` (`review`)
  - Evidence: https://github.com/modelcontextprotocol/servers/tree/main/src/git
- `process-exec` (`review`)
  - Evidence: https://github.com/modelcontextprotocol/servers/tree/main/src/git
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses uvx without a pinned package version

### Limitations

- Actual repository scope depends on MCP client configuration and working directory.

## Memory MCP Server

- ID: `memory-server`
- Homepage: https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- Package: `npx:@modelcontextprotocol/server-memory`
- Launch: `npx -y @modelcontextprotocol/server-memory`
- Version pinned: `False`

### Risk Signals

- `filesystem-access` (`review`)
  - Evidence: https://github.com/modelcontextprotocol/servers/tree/main/src/memory
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses npx without a pinned package version

### Limitations

- Stored memory content can be sensitive; catalog does not inspect or classify user memory data.

## GitHub MCP Server

- ID: `github-mcp-server`
- Homepage: https://github.com/github/github-mcp-server
- Package: `docker:ghcr.io/github/github-mcp-server`
- Launch: `docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server`
- Version pinned: `False`

### Risk Signals

- `network-access` (`high-review`)
  - Evidence: https://github.com/github/github-mcp-server
- `env-access` (`high-review`)
  - Evidence: launch.command passes GITHUB_PERSONAL_ACCESS_TOKEN into the server environment
- `process-exec` (`review`)
  - Evidence: launch.command starts a Docker container
- `unpinned-launch` (`review`)
  - Evidence: launch.command does not pin an image digest or tag

### Limitations

- Risk depends heavily on GitHub token scopes and organization policy.

## Chrome DevTools MCP

- ID: `chrome-devtools-mcp`
- Homepage: https://github.com/ChromeDevTools/chrome-devtools-mcp
- Package: `npx:chrome-devtools-mcp`
- Launch: `npx chrome-devtools-mcp@latest`
- Version pinned: `False`

### Risk Signals

- `sensitive-domain-access` (`high-review`)
  - Evidence: https://github.com/ChromeDevTools/chrome-devtools-mcp
- `process-exec` (`review`)
  - Evidence: launch.command starts local Chrome DevTools integration
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses @latest rather than an exact package version

### Limitations

- Sensitive-domain exposure depends on which browser profile, tabs, and targets the client allows.

## Index Limitations

- Review levels are prompts for human review, not security guarantees.
- Entries are evidence-backed catalog facts, not safe/unsafe labels.
- Maintenance and release signals can change after publication.
