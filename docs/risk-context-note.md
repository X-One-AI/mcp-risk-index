# Risk Context Note

`mcp-risk-index` can support an agent review by turning catalog signals into a short risk context note. This is review context, not an allow/deny decision.

## Boundary

- A risk context note must not be used as a merge gate by itself.
- It does not replace `mcp-audit`, repository-specific policy, human review, or incident response.
- It does not score a PR as safe or unsafe.

## Note Format

```text
signal: <catalog signal or pattern>
evidence: <file, configuration, or behavior that triggered the concern>
reviewer question: <specific question the reviewer should answer>
limitations: <what this note cannot prove>
```

## Example

```text
signal: broad filesystem access
evidence: MCP configuration grants access to a large workspace directory
reviewer question: Is the path scope necessary for the intended task?
limitations: This note does not prove exploitation or policy violation.
```

## Use With Agent Evidence

When `agent-pr-evidence` reports MCP-related risk flags, attach the context note as supporting material. The reviewer still decides whether the PR needs more evidence, a baseline review, a failure packet, or a merge block.
