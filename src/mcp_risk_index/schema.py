SCHEMA_VERSION = "mcp-risk-index.catalog.v1"

ALLOWED_SIGNAL_IDS = {
    "filesystem-access",
    "network-access",
    "env-access",
    "process-exec",
    "unpinned-launch",
    "low-maintenance-signal",
    "sensitive-domain-access",
}

ALLOWED_LEVELS = {"info", "review", "high-review"}

ENTRY_REQUIRED_FIELDS = {
    "id",
    "name",
    "homepage",
    "package",
    "launch",
    "permissions",
    "maintenance",
    "risk_signals",
    "limitations",
}

UNSUPPORTED_JUDGMENT_FIELDS = {"safe", "unsafe", "score", "critical", "trusted"}


class CatalogValidationError(ValueError):
    """Raised when a catalog does not satisfy the public schema contract."""
