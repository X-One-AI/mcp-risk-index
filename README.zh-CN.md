# mcp-risk-index

语言： [English](./README.md) | 中文

常见 MCP server 的权限、启动命令、维护状态和风险说明索引。

## 状态

`v0.2.0` - 本地 catalog 校验、strict review 检查和渲染 CLI。

## 目的

把 `mcp-audit` 的规则经验转成可复用的公共数据资产，同时避免没有证据支撑的安全断言。

## 第一生产化表面

版本化 data catalog：每个条目都需要证据支撑，并提供确定性的本地 CLI。

PyPI 发布后：

```bash
python3 -m pip install xone-mcp-risk-index
mcp-risk-index init --output mcp-risk-index.catalog.yml
mcp-risk-index validate --catalog mcp-risk-index.catalog.yml --strict
mcp-risk-index render --catalog mcp-risk-index.catalog.yml --format markdown --output mcp-risk-index.md
mcp-risk-index render --catalog mcp-risk-index.catalog.yml --format json --output mcp-risk-index.json
```

Homebrew tap 更新后：

```bash
brew install x-one-ai/tap/mcp-risk-index
mcp-risk-index --version
```

如果在源码仓库中，也可以直接校验内置 catalog：

```bash
mcp-risk-index validate --catalog data/catalog.yml --strict
mcp-risk-index render --catalog data/catalog.yml --format markdown --output mcp-risk-index.md
mcp-risk-index render --catalog data/catalog.yml --format json --output mcp-risk-index.json
```

本地开发：

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest tests -q
```

## Catalog 契约

内置 catalog 使用 `mcp-risk-index.catalog.v1`。每个条目记录 server 身份、package、启动命令、权限、维护事实、review 级别的风险信号、证据和限制。

Review level 是给人工检查的提示：

- `info`：有用上下文
- `review`：采用前需要检查
- `high-review`：需要明确 owner 审批

它们不是安全评分。

Strict validation 会要求生产 review 治理字段，例如 `maintenance.source_checked_at` 和 GitHub repository 来源。

## 必要证据

- server 身份
- 权限画像
- 命令/package 信号
- 维护状态信号
- 证据链接

## 非目标

- 不做没有证据的主观排名
- 不做泛 repo health clone
- 不做没有标准支撑的安全声明
- 不做绝对 safe/unsafe 标签

## OPT 运行模型

本项目通过 [ops/opt-overlay.md](./ops/opt-overlay.md) 引用共享 One Person Team 工作流。项目自己的约束放在 [ops/constraints](./ops/constraints)，可演进 skill 放在 [ops/skills](./ops/skills)。

## 暂缺输入

需要用户或真实世界数据补充的内容记录在 `../x-one-skipped-inputs.md`，不阻塞基础建设。

## 文档

- [产品基础](./docs/product-foundation.md)
- [Catalog Governance](./docs/catalog-governance.md)
- [Publishing](./docs/publishing.md)
- [Homebrew Packaging](./docs/homebrew.md)
- [Catalog Design](./docs/superpowers/specs/2026-06-13-catalog-design.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [生产约束](./ops/constraints/production.md)
- [主入口约束](./ops/constraints/main-entry.md)
- [Skill 演进](./ops/skills/evolution.md)
