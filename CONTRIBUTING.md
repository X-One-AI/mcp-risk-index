# Contributing

Thanks for improving `mcp-risk-index`.

## Catalog Rules

- No safe/unsafe labels.
- No unsupported security claims.
- No secret, private, or customer-specific fixtures.
- Add evidence for every risk signal.
- Add a limitation whenever behavior depends on user configuration.
- Run strict validation before opening a pull request.

## Local Checks

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest tests -q
mcp-risk-index validate --catalog data/catalog.yml --strict
```

## OPT

This project references OPT through `ops/opt-overlay.md`. Do not modify shared OPT from this repository; add project-specific constraints or skills here when evidence shows they help.
