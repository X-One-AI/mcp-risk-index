from __future__ import annotations

import argparse
import sys
from importlib import resources
from pathlib import Path
from typing import Sequence

from . import __version__
from .catalog import CatalogValidationError, load_catalog
from .renderers import render_json, render_markdown


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "init":
            starter_catalog = resources.files("mcp_risk_index").joinpath("catalogs/starter.yml").read_text(
                encoding="utf-8"
            )
            args.output.write_text(starter_catalog, encoding="utf-8")
            print(f"wrote {args.output}")
            return 0

        if args.command == "validate":
            catalog = load_catalog(args.catalog)
            print(f"schema_version={catalog['schema_version']} entries={len(catalog['entries'])}")
            return 0

        if args.command == "render":
            catalog = load_catalog(args.catalog)
            output = render_markdown(catalog) if args.format == "markdown" else render_json(catalog)
            if args.output:
                Path(args.output).write_text(output, encoding="utf-8")
            else:
                print(output, end="")
            return 0

        parser.print_help()
        return 2
    except CatalogValidationError as exc:
        print(f"mcp-risk-index: {exc}", file=sys.stderr)
        return 1


def entrypoint() -> None:
    raise SystemExit(main())


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mcp-risk-index",
        description="Validate and render an evidence-backed MCP risk signal catalog.",
    )
    parser.add_argument("--version", action="version", version=f"mcp-risk-index {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    init = subparsers.add_parser("init", help="Write a starter catalog file.")
    init.add_argument("--output", required=True, type=Path, help="Path for the generated catalog YAML.")

    validate = subparsers.add_parser("validate", help="Validate a catalog file.")
    validate.add_argument("--catalog", required=True, type=Path, help="Path to catalog YAML.")

    render = subparsers.add_parser("render", help="Render a catalog as Markdown or JSON.")
    render.add_argument("--catalog", required=True, type=Path, help="Path to catalog YAML.")
    render.add_argument("--format", required=True, choices=("markdown", "json"), help="Output format.")
    render.add_argument("--output", type=Path, help="Output file. Writes to stdout when omitted.")

    return parser
