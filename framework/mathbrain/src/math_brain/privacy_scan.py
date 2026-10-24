"""Context-aware scanner for material considered for publication.

The scanner accepts an explicit list of repository-relative files.  It never
recurses on its own, never accepts an absolute input filename, and reports only
finding classes and locations so a detected credential is not echoed into logs.
"""

from __future__ import annotations

import fnmatch
import re
import tomllib
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

from .privacy import (
    DEFAULT_DENIED_CONTENT_TOKENS,
    DEFAULT_DENIED_PATH_TOKENS,
    PrivacyViolation,
    has_link_component,
    has_unsafe_path_syntax,
    is_within,
    read_stable_file,
    resolve_without_missing,
)

DEFAULT_POLICY_CATEGORY_CONTEXTS = frozenset(
    {
        "AGENTS.md",
        "README.md",
        "config/privacy.toml",
        "docs/design-brief.md",
        "docs/local-audit-protocol.md",
        "docs/privacy-boundary.md",
        "docs/threat-model.md",
        "src/math_brain/privacy.py",
        "src/math_brain/privacy_scan.py",
        "tests/test_privacy.py",
        "tests/test_privacy_scan.py",
        "tests/test_publication.py",
    }
)

_WINDOWS_ABSOLUTE_RE = re.compile(
    r"(?<![A-Za-z0-9_])(?:[A-Za-z]:[\\/](?:[^\s'\"`<>|]+))"
)
_UNC_PREFIX = chr(92) * 2
_UNC_ABSOLUTE_RE = re.compile(
    r"(?<!\\)"
    + re.escape(_UNC_PREFIX)
    + r"[A-Za-z0-9](?:[A-Za-z0-9._-]{0,252})[\\/]"
    + r"[A-Za-z0-9_$.-]+(?=[\\/\s'\"`<>]|$)"
)
_FILE_URI_RE = re.compile(r"\bfile://(?:localhost/)?[^\s'\"`<>]+", re.IGNORECASE)
_POSIX_ABSOLUTE_RE = re.compile(
    r"(?<![:/A-Za-z0-9_])/(?!/)(?:[A-Za-z0-9._~-]+/)+[A-Za-z0-9._~+-]+"
)

_SECRET_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{24,}\b")),
    ("provider-token", re.compile(r"\bsk-(?:proj-|ant-)?[A-Za-z0-9_-]{20,}\b")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    (
        "jwt",
        re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"),
    ),
    (
        "assigned-secret",
        re.compile(
            r"\b(?:api[_-]?key|access[_-]?token|secret|password|credential)\b"
            r"\s*[:=]\s*['\"]?[^\s,'\";]{8,}",
            re.IGNORECASE,
        ),
    ),
    (
        "bearer-token",
        re.compile(r"\bauthorization\s*:\s*bearer\s+[A-Za-z0-9._~-]{16,}", re.IGNORECASE),
    ),
)


@dataclass(frozen=True, slots=True)
class ScanPolicy:
    forbidden_categories: frozenset[str] = (
        DEFAULT_DENIED_PATH_TOKENS | DEFAULT_DENIED_CONTENT_TOKENS
    )
    policy_category_contexts: frozenset[str] = DEFAULT_POLICY_CATEGORY_CONTEXTS
    max_file_bytes: int = 5_000_000


DEFAULT_SCAN_POLICY = ScanPolicy()


@dataclass(frozen=True, slots=True)
class ScanFinding:
    code: str
    path: str
    line: int
    column: int
    message: str


def _is_policy_category_context(relative_path: str, policy: ScanPolicy) -> bool:
    normalized = PurePosixPath(relative_path).as_posix()
    return any(
        fnmatch.fnmatchcase(normalized, pattern)
        for pattern in policy.policy_category_contexts
    )


def _finding(
    code: str,
    path: str,
    line: int,
    column: int,
    message: str,
) -> ScanFinding:
    return ScanFinding(code, path, line, column, message)


def scan_text(
    text: str,
    *,
    relative_path: str,
    policy: ScanPolicy = DEFAULT_SCAN_POLICY,
) -> tuple[ScanFinding, ...]:
    """Scan UTF-8 text without including the matched text in diagnostics."""

    normalized_path = PurePosixPath(relative_path).as_posix()
    findings: list[ScanFinding] = []
    category_context = _is_policy_category_context(normalized_path, policy)

    if not category_context:
        folded_parts = tuple(part.casefold() for part in PurePosixPath(normalized_path).parts)
        for category in sorted(policy.forbidden_categories):
            if any(category.casefold() in part for part in folded_parts):
                findings.append(
                    _finding(
                        "forbidden-category-path",
                        normalized_path,
                        0,
                        0,
                        "filename contains a forbidden category marker",
                    )
                )
                break

    absolute_patterns = (
        _WINDOWS_ABSOLUTE_RE,
        _UNC_ABSOLUTE_RE,
        _FILE_URI_RE,
        _POSIX_ABSOLUTE_RE,
    )
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern in absolute_patterns:
            for match in pattern.finditer(line):
                findings.append(
                    _finding(
                        "absolute-path",
                        normalized_path,
                        line_number,
                        match.start() + 1,
                        "absolute local path is not publishable",
                    )
                )
        for kind, pattern in _SECRET_PATTERNS:
            for match in pattern.finditer(line):
                findings.append(
                    _finding(
                        "secret",
                        normalized_path,
                        line_number,
                        match.start() + 1,
                        f"possible {kind} detected; matched value suppressed",
                    )
                )
        if category_context:
            continue
        for category in sorted(policy.forbidden_categories):
            pattern = re.compile(
                rf"(?<![A-Za-z0-9_]){re.escape(category)}(?![A-Za-z0-9_])",
                re.IGNORECASE,
            )
            for match in pattern.finditer(line):
                findings.append(
                    _finding(
                        "forbidden-category",
                        normalized_path,
                        line_number,
                        match.start() + 1,
                        "content contains a forbidden category marker",
                    )
                )
    return tuple(findings)


def load_scan_policy(
    config_path: str | Path,
    *,
    repository_root: str | Path,
) -> ScanPolicy:
    """Load the scanner subset of the public privacy policy."""

    repo_path = Path(repository_root)
    if has_unsafe_path_syntax(repo_path):
        raise PrivacyViolation("unsafe-path-syntax", "repository root uses disabled path syntax")
    if has_link_component(repo_path):
        raise PrivacyViolation("link-component", "repository root contains a link component")
    try:
        repo = resolve_without_missing(repo_path)
    except (FileNotFoundError, RuntimeError, OSError) as exc:
        raise PrivacyViolation("unresolvable", "repository root does not resolve safely") from exc
    config = Path(config_path)
    if not config.is_absolute():
        config = repo / config
    if has_link_component(config):
        raise PrivacyViolation("link-component", "scanner policy contains a link component")
    raw = read_stable_file(config, root=repo, max_file_bytes=1_000_000)
    try:
        document = tomllib.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as exc:
        raise PrivacyViolation("policy-parse", "privacy policy is not valid UTF-8 TOML") from exc
    hard_exclusions = document.get("hard_exclusions")
    scanner = document.get("scanner")
    if not isinstance(hard_exclusions, dict) or not isinstance(scanner, dict):
        raise PrivacyViolation("policy-schema", "privacy policy lacks scanner configuration")
    categories = hard_exclusions.get("path_tokens")
    content_categories = hard_exclusions.get("content_tokens", [])
    contexts = scanner.get("policy_category_contexts")
    maximum = scanner.get("max_file_bytes")
    if (
        not isinstance(categories, list)
        or not categories
        or not all(isinstance(item, str) and item for item in categories)
        or not isinstance(content_categories, list)
        or not all(isinstance(item, str) and item for item in content_categories)
        or not isinstance(contexts, list)
        or not contexts
        or not all(isinstance(item, str) and item for item in contexts)
        or not isinstance(maximum, int)
        or isinstance(maximum, bool)
        or not 1 <= maximum <= 100_000_000
    ):
        raise PrivacyViolation("policy-schema", "scanner policy fields are invalid")
    return ScanPolicy(
        frozenset(item.casefold() for item in categories + content_categories),
        frozenset(contexts),
        maximum,
    )


def scan_repository_files(
    *,
    repository_root: str | Path,
    relative_paths: Iterable[str | Path],
    policy: ScanPolicy = DEFAULT_SCAN_POLICY,
    home: str | Path | None = None,
) -> tuple[ScanFinding, ...]:
    """Scan only explicitly named files; directory inputs are refused."""

    repo_path = Path(repository_root)
    if has_unsafe_path_syntax(repo_path):
        return (
            _finding(
                "unsafe-path-syntax",
                "<repository>",
                0,
                0,
                "repository root uses disabled filesystem syntax",
            ),
        )
    if has_link_component(repo_path):
        return (_finding("unsafe-root", "<repository>", 0, 0, "repository root uses a link"),)
    try:
        repo = resolve_without_missing(repo_path)
        resolved_home = resolve_without_missing(Path(home) if home is not None else Path.home())
    except (FileNotFoundError, RuntimeError, OSError):
        return (_finding("unsafe-root", "<repository>", 0, 0, "repository root is unresolved"),)
    if repo == resolved_home or is_within(resolved_home, repo):
        return (
            _finding(
                "home-recursion",
                "<repository>",
                0,
                0,
                "scanner may not target the home tree or one of its ancestors",
            ),
        )

    findings: list[ScanFinding] = []
    paths = tuple(relative_paths)
    if not paths:
        return (
            _finding(
                "no-input-files",
                "<repository>",
                0,
                0,
                "scanner requires an explicit non-empty file list",
            ),
        )
    for raw_path in paths:
        relative = Path(raw_path)
        label = PurePosixPath(str(raw_path).replace("\\", "/")).as_posix()
        if (
            relative.is_absolute()
            or relative.drive
            or relative.root
            or ".." in relative.parts
        ):
            findings.append(
                _finding(
                    "absolute-input-path",
                    label,
                    0,
                    0,
                    "scanner inputs must be repository-relative files",
                )
            )
            continue
        if has_unsafe_path_syntax(relative):
            findings.append(
                _finding(
                    "unsafe-path-syntax",
                    label,
                    0,
                    0,
                    "input uses disabled filesystem syntax",
                )
            )
            continue
        candidate = repo / relative
        if has_link_component(candidate):
            findings.append(_finding("unsafe-path", label, 0, 0, "input contains a link component"))
            continue
        try:
            resolved = resolve_without_missing(candidate)
        except (FileNotFoundError, RuntimeError, OSError):
            findings.append(_finding("missing-file", label, 0, 0, "input file does not resolve"))
            continue
        if not is_within(resolved, repo):
            findings.append(_finding("unsafe-path", label, 0, 0, "input escapes repository"))
            continue
        if resolved.is_dir():
            findings.append(
                _finding(
                    "directory-input",
                    label,
                    0,
                    0,
                    "directory recursion is disabled; enumerate files explicitly",
                )
            )
            continue
        try:
            raw = read_stable_file(resolved, root=repo, max_file_bytes=policy.max_file_bytes)
        except PrivacyViolation as exc:
            findings.append(_finding(exc.code, label, 0, 0, "input failed stable-file checks"))
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            findings.append(
                _finding("non-utf8", label, 0, 0, "publication scanner accepts UTF-8 text only")
            )
            continue
        findings.extend(scan_text(text, relative_path=label, policy=policy))
    return tuple(findings)
