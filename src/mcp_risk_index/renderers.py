from __future__ import annotations

import json
from typing import Any


def render_json(catalog: dict[str, Any]) -> str:
    return json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"


def render_markdown(catalog: dict[str, Any]) -> str:
    lines: list[str] = [
        "# MCP Risk Index",
        "",
        f"Schema: `{catalog['schema_version']}`",
        "",
    ]

    for entry in catalog["entries"]:
        lines.extend(_render_entry(entry))

    lines.extend(
        [
            "## Index Limitations",
            "",
            "- Review levels are prompts for human review, not security guarantees.",
            "- Entries are evidence-backed catalog facts, not safe/unsafe labels.",
            "- Maintenance and release signals can change after publication.",
        ]
    )
    return "\n".join(lines) + "\n"


def _render_entry(entry: dict[str, Any]) -> list[str]:
    package = entry["package"]
    launch = entry["launch"]
    lines = [
        f"## {entry['name']}",
        "",
        f"- ID: `{entry['id']}`",
        f"- Homepage: {entry['homepage']}",
        f"- Package: `{package['manager']}:{package['name']}`",
        f"- Launch: `{launch['command']}`",
        f"- Version pinned: `{launch['version_pinned']}`",
        "",
        "### Risk Signals",
        "",
    ]
    for signal in entry["risk_signals"]:
        lines.append(f"- `{signal['id']}` (`{signal['level']}`)")
        for evidence in signal["evidence"]:
            lines.append(f"  - Evidence: {evidence}")

    lines.extend(["", "### Limitations", ""])
    for limitation in entry["limitations"]:
        lines.append(f"- {limitation}")
    lines.append("")
    return lines
