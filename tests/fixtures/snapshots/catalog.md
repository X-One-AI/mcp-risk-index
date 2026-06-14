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

### Reviewer Questions

- Which filesystem paths can this server read or write?
- Can the launch command pin an exact package version, image tag, or digest?

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

### Reviewer Questions

- Which network destinations, token scopes, or client policies limit this access?
- Can the launch command pin an exact package version, image tag, or digest?

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

### Reviewer Questions

- Which filesystem paths can this server read or write?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

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

### Reviewer Questions

- Which filesystem paths can this server read or write?
- Can the launch command pin an exact package version, image tag, or digest?

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

### Reviewer Questions

- Which network destinations, token scopes, or client policies limit this access?
- Which environment variables or credentials are exposed to this server?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

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

### Reviewer Questions

- Could this server access logged-in browser sessions, private data, or sensitive domains?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

### Limitations

- Sensitive-domain exposure depends on which browser profile, tabs, and targets the client allows.

## Playwright MCP

- ID: `playwright-mcp`
- Homepage: https://github.com/microsoft/playwright-mcp
- Package: `npx:@playwright/mcp`
- Launch: `npx @playwright/mcp@latest`
- Version pinned: `False`

### Risk Signals

- `sensitive-domain-access` (`high-review`)
  - Evidence: https://github.com/microsoft/playwright-mcp
- `network-access` (`high-review`)
  - Evidence: README documents browser navigation, network request inspection, allowed-origin options, and HTTP transport
- `filesystem-access` (`review`)
  - Evidence: README documents user data directories, storage state files, output directories, secrets files, init pages, and init scripts
- `env-access` (`review`)
  - Evidence: README lists PLAYWRIGHT_MCP_* environment variables for runtime options
- `process-exec` (`review`)
  - Evidence: README documents local browser automation and Docker launch modes
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses @latest rather than an exact package version

### Reviewer Questions

- Could this server access logged-in browser sessions, private data, or sensitive domains?
- Which network destinations, token scopes, or client policies limit this access?
- Which filesystem paths can this server read or write?
- Which environment variables or credentials are exposed to this server?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

### Limitations

- Actual exposure depends on browser profile choice, origin policy, enabled capabilities, and whether existing logged-in browser state is connected.

## Context7

- ID: `context7`
- Homepage: https://github.com/upstash/context7
- Package: `npx:ctx7`
- Launch: `npx ctx7 setup`
- Version pinned: `False`

### Risk Signals

- `network-access` (`review`)
  - Evidence: README documents the hosted MCP URL https://mcp.context7.com/mcp
- `env-access` (`review`)
  - Evidence: README documents passing an API key via the CONTEXT7_API_KEY header
- `filesystem-access` (`review`)
  - Evidence: README says ctx7 setup installs the appropriate skill or MCP configuration
- `process-exec` (`review`)
  - Evidence: launch.command runs setup through npx
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses npx without an exact package version

### Reviewer Questions

- Which network destinations, token scopes, or client policies limit this access?
- Which environment variables or credentials are exposed to this server?
- Which filesystem paths can this server read or write?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

### Limitations

- Hosted service behavior, API-key handling, and private backend components are not fully represented by public repository files.

## Serena

- ID: `serena`
- Homepage: https://github.com/oraios/serena
- Package: `uv:serena-agent`
- Launch: `uv tool install -p 3.13 serena-agent && serena init`
- Version pinned: `False`

### Risk Signals

- `filesystem-access` (`high-review`)
  - Evidence: README describes semantic retrieval and editing capabilities for coding workflows
- `process-exec` (`high-review`)
  - Evidence: README documents execute_shell_command for running builds, tests, and linters
- `unpinned-launch` (`review`)
  - Evidence: launch.command installs serena-agent without an exact version

### Reviewer Questions

- Which filesystem paths can this server read or write?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

### Limitations

- README notes shell/file overlap is often disabled by surrounding agent harnesses; verify enabled tools per client configuration.

## n8n MCP

- ID: `n8n-mcp`
- Homepage: https://github.com/czlonkowski/n8n-mcp
- Package: `docker:ghcr.io/czlonkowski/n8n-mcp`
- Launch: `docker run --rm -i -e N8N_API_URL -e N8N_API_KEY ghcr.io/czlonkowski/n8n-mcp`
- Version pinned: `False`

### Risk Signals

- `network-access` (`high-review`)
  - Evidence: README documents n8n API connectivity, hosted dashboard setup, and self-hosted deployment
- `env-access` (`high-review`)
  - Evidence: README says n8n management tools require N8N_API_URL and N8N_API_KEY
- `process-exec` (`review`)
  - Evidence: README documents Docker and self-hosted deployment options
- `unpinned-launch` (`review`)
  - Evidence: launch.command does not pin an image tag or digest

### Reviewer Questions

- Which network destinations, token scopes, or client policies limit this access?
- Which environment variables or credentials are exposed to this server?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

### Limitations

- Risk depends on n8n API permissions, workflow environment, and whether management tools are enabled.

## MCP Toolbox for Databases

- ID: `mcp-toolbox`
- Homepage: https://github.com/googleapis/mcp-toolbox
- Package: `npx:@toolbox-sdk/server`
- Launch: `npx @toolbox-sdk/server --config tools.yaml`
- Version pinned: `False`

### Risk Signals

- `network-access` (`high-review`)
  - Evidence: README says the server connects AI agents, IDEs, and applications directly to enterprise databases
- `env-access` (`high-review`)
  - Evidence: README says users must set appropriate environment variables to connect prebuilt database tools
- `filesystem-access` (`review`)
  - Evidence: README documents tools.yaml as the primary configuration file for sources and tools
- `process-exec` (`review`)
  - Evidence: README documents npm, binary, container, Homebrew, and source execution modes
- `unpinned-launch` (`review`)
  - Evidence: launch.command uses npx without an exact package version

### Reviewer Questions

- Which network destinations, token scopes, or client policies limit this access?
- Which environment variables or credentials are exposed to this server?
- Which filesystem paths can this server read or write?
- Which local commands, containers, or subprocesses can this server start?
- Can the launch command pin an exact package version, image tag, or digest?

### Limitations

- Database blast radius depends on configured sources, credentials, network access, and read/write tool definitions.

## HexStrike AI MCP Agents

- ID: `hexstrike-ai`
- Homepage: https://github.com/0x4m4/hexstrike-ai
- Package: `python:hexstrike-ai`
- Launch: `python3 hexstrike_server.py`
- Version pinned: `False`

### Risk Signals

- `process-exec` (`high-review`)
  - Evidence: README documents 150+ security tools and an /api/command endpoint to execute arbitrary commands
- `network-access` (`high-review`)
  - Evidence: README documents network scanning, web testing, vulnerability assessment, and reconnaissance tools
- `sensitive-domain-access` (`high-review`)
  - Evidence: README advises running in isolated environments and says AI agents can execute arbitrary security tools
- `filesystem-access` (`review`)
  - Evidence: README documents local installation and security-tool setup
- `unpinned-launch` (`review`)
  - Evidence: launch.command starts a local Python entry script without a released package version

### Reviewer Questions

- Which local commands, containers, or subprocesses can this server start?
- Which network destinations, token scopes, or client policies limit this access?
- Could this server access logged-in browser sessions, private data, or sensitive domains?
- Which filesystem paths can this server read or write?
- Can the launch command pin an exact package version, image tag, or digest?

### Limitations

- Catalog does not authorize scanning; production use requires explicit target ownership, network controls, and audit logging.

## Index Limitations

- Review levels are prompts for human review, not security guarantees.
- Entries are evidence-backed catalog facts, not safe/unsafe labels.
- Maintenance and release signals can change after publication.
