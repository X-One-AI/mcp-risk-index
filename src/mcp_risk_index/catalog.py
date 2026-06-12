from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .schema import (
    ALLOWED_LEVELS,
    ALLOWED_SIGNAL_IDS,
    ENTRY_REQUIRED_FIELDS,
    SCHEMA_VERSION,
    UNSUPPORTED_JUDGMENT_FIELDS,
    CatalogValidationError,
)


def load_catalog(path: Path | str, *, strict: bool = False) -> dict[str, Any]:
    catalog_path = Path(path)
    try:
        raw = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise CatalogValidationError(f"Catalog not found: {catalog_path}") from exc
    except yaml.YAMLError as exc:
        raise CatalogValidationError(f"Catalog is not valid YAML: {catalog_path}") from exc

    if not isinstance(raw, dict):
        raise CatalogValidationError("Catalog root must be a mapping")

    validate_catalog(raw, strict=strict)
    return raw


def validate_catalog(catalog: dict[str, Any], *, strict: bool = False) -> None:
    if catalog.get("schema_version") != SCHEMA_VERSION:
        raise CatalogValidationError(f"Unsupported schema_version: {catalog.get('schema_version')!r}")

    entries = catalog.get("entries")
    if not isinstance(entries, list) or not entries:
        raise CatalogValidationError("Catalog entries must be a non-empty list")

    seen_ids: set[str] = set()
    for index, entry in enumerate(entries):
        _validate_entry(entry, index=index, seen_ids=seen_ids, strict=strict)


def _validate_entry(entry: Any, *, index: int, seen_ids: set[str], strict: bool) -> None:
    if not isinstance(entry, dict):
        raise CatalogValidationError(f"Entry at index {index} must be a mapping")

    unsupported = sorted(UNSUPPORTED_JUDGMENT_FIELDS.intersection(entry))
    if unsupported:
        raise CatalogValidationError(f"Unsupported judgment field on entry {index}: {unsupported[0]}")

    missing = sorted(ENTRY_REQUIRED_FIELDS.difference(entry))
    if missing:
        raise CatalogValidationError(f"Entry at index {index} is missing required field: {missing[0]}")

    entry_id = entry["id"]
    if not isinstance(entry_id, str) or not entry_id:
        raise CatalogValidationError(f"Entry at index {index} must include a non-empty id")
    if entry_id in seen_ids:
        raise CatalogValidationError(f"Duplicate entry id: {entry_id}")
    seen_ids.add(entry_id)

    for field in ("name", "homepage"):
        if not isinstance(entry[field], str) or not entry[field]:
            raise CatalogValidationError(f"Entry {entry_id} field {field} must be a non-empty string")

    if not isinstance(entry["package"], dict):
        raise CatalogValidationError(f"Entry {entry_id} package must be a mapping")
    if not isinstance(entry["launch"], dict):
        raise CatalogValidationError(f"Entry {entry_id} launch must be a mapping")
    if not isinstance(entry["permissions"], dict):
        raise CatalogValidationError(f"Entry {entry_id} permissions must be a mapping")
    if not isinstance(entry["maintenance"], dict):
        raise CatalogValidationError(f"Entry {entry_id} maintenance must be a mapping")
    if strict:
        _validate_strict_entry(entry, entry_id=entry_id)

    signals = entry["risk_signals"]
    if not isinstance(signals, list) or not signals:
        raise CatalogValidationError(f"Entry {entry_id} must include at least one risk signal")
    for signal_index, signal in enumerate(signals):
        _validate_signal(signal, entry_id=entry_id, signal_index=signal_index)

    limitations = entry["limitations"]
    if not isinstance(limitations, list) or not all(isinstance(item, str) and item for item in limitations):
        raise CatalogValidationError(f"Entry {entry_id} limitations must be a non-empty list of strings")


def _validate_signal(signal: Any, *, entry_id: str, signal_index: int) -> None:
    if not isinstance(signal, dict):
        raise CatalogValidationError(f"Entry {entry_id} risk signal {signal_index} must be a mapping")

    signal_id = signal.get("id")
    if signal_id not in ALLOWED_SIGNAL_IDS:
        raise CatalogValidationError(f"Unknown signal id on entry {entry_id}: {signal_id}")

    level = signal.get("level")
    if level not in ALLOWED_LEVELS:
        raise CatalogValidationError(f"Invalid signal level on entry {entry_id}: {level}")

    evidence = signal.get("evidence")
    if not isinstance(evidence, list) or not evidence or not all(isinstance(item, str) and item for item in evidence):
        raise CatalogValidationError(f"Risk signal {signal_id} on entry {entry_id} must include evidence")


def _validate_strict_entry(entry: dict[str, Any], *, entry_id: str) -> None:
    maintenance = entry["maintenance"]
    source_checked_at = maintenance.get("source_checked_at")
    if not isinstance(source_checked_at, str) or len(source_checked_at.split("-")) != 3:
        raise CatalogValidationError(f"Entry {entry_id} must include maintenance.source_checked_at in strict mode")
    if not isinstance(maintenance.get("repository"), str) or not maintenance["repository"].startswith("https://github.com/"):
        raise CatalogValidationError(f"Entry {entry_id} must include a GitHub repository URL in strict mode")
    if not isinstance(entry["homepage"], str) or not entry["homepage"].startswith("https://"):
        raise CatalogValidationError(f"Entry {entry_id} homepage must be an https URL in strict mode")
