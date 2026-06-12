from pathlib import Path


def test_docs_and_package_metadata_stay_aligned():
    english = Path("README.md").read_text(encoding="utf-8")
    chinese = Path("README.zh-CN.md").read_text(encoding="utf-8")
    foundation = Path("docs/product-foundation.md").read_text(encoding="utf-8")
    production = Path("ops/constraints/production.md").read_text(encoding="utf-8")
    ci = Path(".github/workflows/ci.yml").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")
    manifest = Path("MANIFEST.in").read_text(encoding="utf-8")
    changelog = Path("CHANGELOG.md").read_text(encoding="utf-8")

    assert "mcp-risk-index validate" in english
    assert "mcp-risk-index init" in english
    assert "mcp-risk-index render" in english
    assert "v0.1.0" in english
    assert "README.zh-CN.md" in english
    assert "mcp-risk-index validate" in chinese
    assert "mcp-risk-index init" in chinese
    assert "mcp-risk-index render" in chinese
    assert "v0.1.0" in chinese
    assert "README.md" in chinese
    assert "mcp-risk-index.catalog.v1" in foundation
    assert "safe/unsafe labels" in production
    assert "python3 -m pytest tests -q" in ci
    assert 'version = "0.1.0"' in pyproject
    assert "include README.zh-CN.md" in manifest
    assert "recursive-include data *.yml" in manifest
    assert "recursive-include tests/fixtures *.md" in manifest
    assert "## 0.1.0" in changelog
