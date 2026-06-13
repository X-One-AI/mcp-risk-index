# Publishing

`mcp-risk-index` uses GitHub Actions and PyPI Trusted Publishing.

Python distribution package:

```text
xone-mcp-risk-index
```

Installed CLI:

```text
mcp-risk-index
```

## Current Index Status

As of 2026-06-13, public API checks show:

- PyPI: `xone-mcp-risk-index` is not published yet.
- TestPyPI: `xone-mcp-risk-index` is not published yet.

## GitHub Environments

Create these GitHub environments:

- `testpypi`
- `pypi`

The `pypi` environment should require manual approval.

## Trusted Publisher Settings

```text
Project: xone-mcp-risk-index
Owner: X-One-AI
Repository: mcp-risk-index
Workflow: publish.yml
Environment: testpypi or pypi
```

## Publish Order

1. Merge and verify a green CI run on `main`.
2. Confirm the release tag exists, for example `v0.3.0`.
3. Run `Publish Python Package` with `repository = testpypi`.
4. Verify a clean TestPyPI install.
5. Run `Publish Python Package` with `repository = pypi` from a release tag after approval.
6. Verify a clean PyPI install.

## TestPyPI Install Check

```bash
python -m venv /tmp/mcp-risk-index-testpypi
/tmp/mcp-risk-index-testpypi/bin/python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  xone-mcp-risk-index
/tmp/mcp-risk-index-testpypi/bin/mcp-risk-index --version
```

## PyPI Install Check

```bash
python -m venv /tmp/mcp-risk-index-pypi
/tmp/mcp-risk-index-pypi/bin/python -m pip install xone-mcp-risk-index
/tmp/mcp-risk-index-pypi/bin/mcp-risk-index --version
```

## GitHub Release Install Path

```bash
python3 -m pip install https://github.com/X-One-AI/mcp-risk-index/releases/download/v0.3.0/xone_mcp_risk_index-0.3.0-py3-none-any.whl
mcp-risk-index --version
```
