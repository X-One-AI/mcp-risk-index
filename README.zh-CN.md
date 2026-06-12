# mcp-risk-index

语言： [English](./README.md) | 中文

常见 MCP server 的权限、启动命令、维护状态和风险说明索引。

## 状态

`P2` - catalog 设计已准备进入 v0.1.0 规划。

## 目的

把 `mcp-audit` 的规则经验转成可复用的公共数据资产，同时避免没有证据支撑的安全断言。

## 第一生产化表面

版本化 data catalog：每个条目都需要证据支撑，并配套 review workflow。

第一可执行表面已在 [Catalog Design](./docs/superpowers/specs/2026-06-13-catalog-design.md) 中定义。

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
- [Catalog Design](./docs/superpowers/specs/2026-06-13-catalog-design.md)
- [OPT Overlay](./ops/opt-overlay.md)
- [生产约束](./ops/constraints/production.md)
- [主入口约束](./ops/constraints/main-entry.md)
- [Skill 演进](./ops/skills/evolution.md)
