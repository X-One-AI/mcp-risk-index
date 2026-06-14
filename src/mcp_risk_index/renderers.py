from __future__ import annotations

import json
from typing import Any


REVIEW_QUESTIONS_BY_SIGNAL = {
    "filesystem-access": "Which filesystem paths can this server read or write?",
    "network-access": "Which network destinations, token scopes, or client policies limit this access?",
    "env-access": "Which environment variables or credentials are exposed to this server?",
    "process-exec": "Which local commands, containers, or subprocesses can this server start?",
    "unpinned-launch": "Can the launch command pin an exact package version, image tag, or digest?",
    "low-maintenance-signal": "What current maintenance or release evidence should be checked before adoption?",
    "sensitive-domain-access": "Could this server access logged-in browser sessions, private data, or sensitive domains?",
}


def render_json(catalog: dict[str, Any]) -> str:
    rendered = dict(catalog)
    rendered["entries"] = [
        {
            **entry,
            "review_questions": build_review_questions(entry),
        }
        for entry in catalog["entries"]
    ]
    return json.dumps(rendered, ensure_ascii=False, indent=2) + "\n"


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

    lines.extend(["", "### Reviewer Questions", ""])
    for question in build_review_questions(entry):
        lines.append(f"- {question}")

    lines.extend(["", "### Limitations", ""])
    for limitation in entry["limitations"]:
        lines.append(f"- {limitation}")
    lines.append("")
    return lines


def build_review_questions(entry: dict[str, Any]) -> list[str]:
    questions: list[str] = []
    for signal in entry["risk_signals"]:
        question = REVIEW_QUESTIONS_BY_SIGNAL.get(signal["id"])
        if question and question not in questions:
            questions.append(question)
    return questions
