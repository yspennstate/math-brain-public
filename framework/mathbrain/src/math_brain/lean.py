"""Narrow Lean adapter; kernel success and statement fidelity remain distinct."""

from __future__ import annotations

import hashlib
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


PLACEHOLDER = re.compile(r"\b(?:sorry|admit|sorryAx)\b")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return "sha256:" + digest.hexdigest()


def _within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


@dataclass(frozen=True, slots=True)
class LeanResult:
    available: bool
    passed: bool
    returncode: int | None
    stdout: str
    stderr: str
    reason: str
    source_hash: str
    toolchain_version: str
    command: tuple[str, ...]


def check_lean_file(
    path: str | Path,
    *,
    command: Sequence[str] = ("lean",),
    project_root: str | Path | None = None,
    timeout_seconds: int = 60,
) -> LeanResult:
    source = Path(path).resolve(strict=True)
    source_hash = sha256_file(source)
    normalized_command = tuple(command)
    if not normalized_command:
        raise ValueError("Lean command must not be empty")
    if source.suffix.casefold() != ".lean":
        raise ValueError("Lean checker accepts only .lean files")
    root = Path(project_root).resolve(strict=True) if project_root is not None else source.parent
    if not _within(source, root):
        raise ValueError("Lean source escapes the project root")
    text = source.read_text(encoding="utf-8-sig", errors="strict")
    if PLACEHOLDER.search(text):
        return LeanResult(
            True,
            False,
            None,
            "",
            "",
            "source contains a forbidden proof placeholder token",
            source_hash,
            "not queried",
            normalized_command,
        )
    version = "unknown"
    try:
        version_run = subprocess.run(
            [*normalized_command, "--version"],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=min(timeout_seconds, 20),
            check=False,
            shell=False,
        )
        if version_run.returncode == 0:
            version = (version_run.stdout or version_run.stderr).strip()[:500]
    except (FileNotFoundError, OSError):
        return LeanResult(
            False,
            False,
            None,
            "",
            "",
            "Lean command is unavailable",
            source_hash,
            "unavailable",
            normalized_command,
        )
    except subprocess.TimeoutExpired:
        return LeanResult(
            False,
            False,
            None,
            "",
            "",
            "Lean version query timed out",
            source_hash,
            "timeout",
            normalized_command,
        )

    try:
        completed = subprocess.run(
            [*normalized_command, str(source)],
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
            check=False,
            shell=False,
        )
    except FileNotFoundError:
        return LeanResult(
            False,
            False,
            None,
            "",
            "",
            "Lean command is unavailable",
            source_hash,
            version,
            normalized_command,
        )
    except subprocess.TimeoutExpired as exc:
        return LeanResult(
            True,
            False,
            None,
            exc.stdout or "",
            exc.stderr or "",
            "Lean check timed out",
            source_hash,
            version,
            normalized_command,
        )
    except OSError as exc:
        return LeanResult(
            False,
            False,
            None,
            "",
            "",
            f"Lean could not start: {exc}",
            source_hash,
            version,
            normalized_command,
        )

    combined = completed.stdout + "\n" + completed.stderr
    placeholder_warning = "declaration uses 'sorry'" in combined or "sorryAx" in combined
    passed = completed.returncode == 0 and not placeholder_warning
    if placeholder_warning:
        reason = "Lean accepted the file with a proof placeholder"
    elif passed:
        reason = "Lean kernel check passed"
    else:
        reason = "Lean reported an error"
    return LeanResult(
        True,
        passed,
        completed.returncode,
        completed.stdout,
        completed.stderr,
        reason,
        source_hash,
        version,
        normalized_command,
    )


FIDELITY_QUESTIONS = (
    "Do formal and prose quantifiers match?",
    "Do domains and typeclass assumptions match?",
    "Are all definitions extensionally equivalent to the prose definitions?",
    "Did the formal statement add assumptions or weaken the conclusion?",
    "Are boundary and degenerate cases represented?",
    "Does any trusted axiom or placeholder remain?",
)


@dataclass(frozen=True, slots=True)
class StatementFidelityReview:
    prose_claim_hash: str
    formal_statement_hash: str
    reviewer: str
    quantifiers_match: bool
    domains_match: bool
    definitions_match: bool
    assumptions_match: bool
    conclusion_match: bool
    boundary_cases_match: bool
    no_extra_axioms: bool
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.prose_claim_hash.startswith("sha256:"):
            raise ValueError("prose claim hash must be a sha256 digest")
        if not self.formal_statement_hash.startswith("sha256:"):
            raise ValueError("formal statement hash must be a sha256 digest")
        if not self.reviewer.strip():
            raise ValueError("fidelity review requires an identified reviewer")

    @property
    def passed(self) -> bool:
        return all(
            (
                self.quantifiers_match,
                self.domains_match,
                self.definitions_match,
                self.assumptions_match,
                self.conclusion_match,
                self.boundary_cases_match,
                self.no_extra_axioms,
            )
        )
