import json
import subprocess
import sys
from pathlib import Path

import pytest

from mcp_risk_index.catalog import CatalogValidationError, load_catalog
from mcp_risk_index.cli import main
from mcp_risk_index.renderers import render_json, render_markdown


CATALOG = Path("data/catalog.yml")


def test_load_catalog_validates_bundled_catalog():
    catalog = load_catalog(CATALOG)

    assert catalog["schema_version"] == "mcp-risk-index.catalog.v1"
    assert [entry["id"] for entry in catalog["entries"]] == [
        "filesystem-server",
        "fetch-server",
        "git-server",
        "memory-server",
        "github-mcp-server",
        "chrome-devtools-mcp",
        "playwright-mcp",
        "context7",
        "serena",
        "n8n-mcp",
        "mcp-toolbox",
        "hexstrike-ai",
    ]


def test_strict_catalog_validation_requires_review_governance_fields():
    catalog = load_catalog(CATALOG, strict=True)

    assert len(catalog["entries"]) >= 12
    assert all(entry["maintenance"]["source_checked_at"] == "2026-06-13" for entry in catalog["entries"])


@pytest.mark.parametrize(
    "fixture, message",
    [
        ("tests/fixtures/invalid-unknown-signal.yml", "Unknown signal id"),
        ("tests/fixtures/invalid-missing-evidence.yml", "must include evidence"),
        ("tests/fixtures/invalid-absolute-claim.yml", "Unsupported judgment field"),
    ],
)
def test_invalid_catalogs_fail_with_clear_errors(fixture, message):
    with pytest.raises(CatalogValidationError, match=message):
        load_catalog(Path(fixture))


def test_render_markdown_snapshot_stays_stable():
    expected = Path("tests/fixtures/snapshots/catalog.md").read_text(encoding="utf-8")

    assert render_markdown(load_catalog(CATALOG)) == expected


def test_render_json_outputs_machine_readable_catalog():
    data = json.loads(render_json(load_catalog(CATALOG)))

    assert data["schema_version"] == "mcp-risk-index.catalog.v1"
    assert data["entries"][0]["risk_signals"][0]["id"] == "filesystem-access"


def test_cli_validate_and_render(tmp_path, capsys):
    markdown = tmp_path / "index.md"
    json_output = tmp_path / "index.json"
    starter = tmp_path / "catalog.yml"

    validate_exit = main(["validate", "--catalog", str(CATALOG), "--strict"])
    init_exit = main(["init", "--output", str(starter)])
    markdown_exit = main(["render", "--catalog", str(CATALOG), "--format", "markdown", "--output", str(markdown)])
    json_exit = main(["render", "--catalog", str(CATALOG), "--format", "json", "--output", str(json_output)])

    captured = capsys.readouterr()
    assert validate_exit == 0
    assert "strict=true" in captured.out
    assert init_exit == 0
    assert load_catalog(starter, strict=True)["entries"]
    assert markdown_exit == 0
    assert json_exit == 0
    assert "# MCP Risk Index" in markdown.read_text(encoding="utf-8")
    assert json.loads(json_output.read_text(encoding="utf-8"))["entries"]


def test_package_module_entrypoint_outputs_version():
    result = subprocess.run(
        [sys.executable, "-m", "mcp_risk_index", "--version"],
        check=True,
        env={"PYTHONPATH": "src"},
        text=True,
        stdout=subprocess.PIPE,
    )

    assert result.stdout.strip() == "mcp-risk-index 0.3.0"
