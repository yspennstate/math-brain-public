"""Lean authority is Windows-only, and a build elsewhere says so (fleet04/B18,
B18-R79-LEAN-POSIX-AUTHORITY-UNREACHABLE-20260929).

On every platform but Windows the executable lease is opened read-only and cannot be held against replacement, so
executable_lock_enforced is false and no result there is authority-eligible. That was already fail-closed; what was
missing was the explanation. A passing build on such a lease now says in its reason that it is a diagnostic only,
LeanResult.authority_blockers names the gates that are closed, and the docs state the platform contract. The lease
of a non-Windows host is its real branch: _lease_executable itself, run with os.name reading 'posix' for the call.
"""

import os
from dataclasses import replace
from pathlib import Path

import pytest

from math_brain import lean as lean_module

from test_lean import clean_run, sealed_eligible_result

_REAL_LEASE = lean_module._lease_executable


def test_the_non_windows_branch_of_the_lease_does_not_enforce_the_lock(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    binary = tmp_path / "lean.bin"
    binary.write_bytes(b"\x7fELF synthetic lean binary")   # a native header, as the snapshot requires
    with monkeypatch.context() as patch:
        patch.setattr(os, "name", "posix")
        lease = _REAL_LEASE(binary)
    try:
        assert lease.lock_enforced is False and lease.descriptor is not None
    finally:
        lease.close()


def test_a_passing_build_on_an_unlockable_executable_says_it_is_a_diagnostic(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    def posix_lease(path: Path):
        with monkeypatch.context() as patch:
            patch.setattr(os, "name", "posix")
            return _REAL_LEASE(path)

    monkeypatch.setattr(lean_module, "_lease_executable", posix_lease)
    result, *_ = clean_run(tmp_path)
    assert result.passed, result.reason
    assert not result.executable_lock_enforced
    assert not result.authority_eligible
    assert "authority unsupported on this platform" in result.reason
    assert "executable_lock_enforced" in result.authority_blockers


def test_a_locked_lease_passing_build_carries_no_platform_note(tmp_path: Path) -> None:
    if os.name != "nt":
        pytest.skip("the executable is held against replacement only on Windows")
    result, *_ = clean_run(tmp_path)
    assert result.passed, result.reason
    assert result.executable_lock_enforced
    assert "authority unsupported" not in result.reason
    assert "executable_lock_enforced" not in result.authority_blockers


def test_blockers_are_empty_exactly_when_eligible(tmp_path: Path) -> None:
    eligible = sealed_eligible_result(tmp_path)
    assert eligible.authority_eligible and eligible.authority_blockers == ()
    unlocked = replace(eligible, executable_lock_enforced=False)
    assert not unlocked.authority_eligible
    assert unlocked.authority_blockers == ("executable_lock_enforced",)


def test_every_blocker_name_is_one_gate_of_eligibility(tmp_path: Path) -> None:
    result, *_ = clean_run(tmp_path)
    names = [name for name, _ in result._authority_gates()]
    assert len(names) == len(set(names)) == 21
    assert set(result.authority_blockers) <= set(names)
    assert result.authority_eligible == (result.authority_blockers == ())


def test_the_docs_state_the_platform_contract() -> None:
    docs = (Path(__file__).resolve().parents[1] / "docs" / "formal-verification.md").read_text(encoding="utf-8")
    assert "Authority is Windows-only" in docs and "authority_blockers" in docs
