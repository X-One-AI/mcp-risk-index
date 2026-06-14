# Homebrew Packaging

`mcp-risk-index` is distributed through the X-One tap.

## User Install

```bash
brew tap x-one-ai/tap
brew trust --formula x-one-ai/tap/mcp-risk-index
brew install x-one-ai/tap/mcp-risk-index
mcp-risk-index --version
```

## Tap Repository

```text
X-One-AI/homebrew-tap
```

Formula path:

```text
Formula/mcp-risk-index.rb
```

## Formula Requirements

- Install the Python CLI as `mcp-risk-index`.
- Use the released `xone-mcp-risk-index` source distribution.
- Vendor Python dependencies as Homebrew resources.
- Run `mcp-risk-index --version` and `mcp-risk-index init` in the formula test.

## Current Target

```text
xone-mcp-risk-index==0.3.1
```
