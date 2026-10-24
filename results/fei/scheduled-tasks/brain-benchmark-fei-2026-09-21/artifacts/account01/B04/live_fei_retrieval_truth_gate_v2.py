#!/usr/bin/env python3
"""Fresh-main witness wrapper for the FEI retrieval semantic truth gate.

This gate does not perform retrieval and cannot establish brain acceptance. It
closes a replay gap in v1: an immutable but stale ORDER/RESEARCH_STATE snapshot
must not be accepted as "live" merely because its Git blob IDs are internally
consistent. v2 requires a same-invocation fresh-main witness, binds the result
payload to that witness, and delegates the semantic checks to the exact pinned
v1 gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

V1_GATE_GIT_BLOB = "aa9f7d808a023afed49f11c9271ee54bf43e3d89"
POINTER_ID = "FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z"
WITNESS_SCHEMA = "b04-live-truth-witness-v1"
WITNESS_SOURCE = "authorized_connector_fresh_main"
DEFAULT_MAX_AGE_SECONDS = 900
MAX_FUTURE_SKEW_SECONDS = 60


class GateError(RuntimeError):
    pass


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def load_regular(path: Path, *, max_bytes: int) -> bytes:
    if path.is_symlink():
        raise GateError(f"symlink rejected: {path.name}")
    if not path.is_file():
        raise GateError(f"not a regular file: {path.name}")
    st = path.stat()
    if st.st_size < 0 or st.st_size > max_bytes:
        raise GateError(f"input size rejected: {path.name}")
    return path.read_bytes()


def parse_json(raw: bytes, label: str) -> dict[str, Any]:
    try:
        obj = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise GateError(f"invalid {label} JSON") from exc
    if not isinstance(obj, dict):
        raise GateError(f"{label} must be a JSON object")
    return obj


def is_hex40(value: Any) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value) is not None


def parse_utc(value: Any) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise GateError("witness observed_utc must be RFC3339 UTC ending in Z")
    try:
        dt = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError as exc:
        raise GateError("witness observed_utc is invalid") from exc
    if dt.tzinfo is None:
        raise GateError("witness observed_utc lacks timezone")
    return dt.astimezone(timezone.utc)


def validate_witness(
    witness: dict[str, Any], *, now: datetime, max_age_seconds: int
) -> None:
    if witness.get("schema") != WITNESS_SCHEMA:
        raise GateError("witness schema mismatch")
    if witness.get("source") != WITNESS_SOURCE:
        raise GateError("witness source mismatch")
    if witness.get("fresh_main_resolved") is not True:
        raise GateError("witness does not assert fresh main resolution")
    if witness.get("joint_pointer_id") != POINTER_ID:
        raise GateError("witness joint pointer mismatch")
    for key in ("control_commit", "readme_git_blob", "order_git_blob", "research_state_git_blob"):
        if not is_hex40(witness.get(key)):
            raise GateError(f"witness invalid {key}")
    rev = witness.get("control_revision")
    if not isinstance(rev, str) or not rev.strip():
        raise GateError("witness control_revision missing")
    observed = parse_utc(witness.get("observed_utc"))
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    now = now.astimezone(timezone.utc)
    age = (now - observed).total_seconds()
    if age < -MAX_FUTURE_SKEW_SECONDS:
        raise GateError("witness timestamp is too far in the future")
    if age > max_age_seconds:
        raise GateError("witness is stale")


def validate(
    *,
    v1_gate: Path,
    order_path: Path,
    state_path: Path,
    results_path: Path,
    witness_path: Path,
    max_age_seconds: int = DEFAULT_MAX_AGE_SECONDS,
    now: datetime | None = None,
    expected_v1_blob: str = V1_GATE_GIT_BLOB,
) -> dict[str, Any]:
    if max_age_seconds <= 0 or max_age_seconds > 3600:
        raise GateError("max witness age must be in 1..3600 seconds")
    now = now or datetime.now(timezone.utc)

    v1_before = load_regular(v1_gate, max_bytes=2_000_000)
    order_before = load_regular(order_path, max_bytes=2_000_000)
    state_before = load_regular(state_path, max_bytes=4_000_000)
    results_before = load_regular(results_path, max_bytes=4_000_000)
    witness_before = load_regular(witness_path, max_bytes=32_000)

    if git_blob_sha(v1_before) != expected_v1_blob:
        raise GateError("v1 gate Git blob mismatch")

    witness = parse_json(witness_before, "witness")
    validate_witness(witness, now=now, max_age_seconds=max_age_seconds)

    if git_blob_sha(order_before) != witness["order_git_blob"]:
        raise GateError("ORDER does not match fresh-main witness")
    if git_blob_sha(state_before) != witness["research_state_git_blob"]:
        raise GateError("RESEARCH_STATE does not match fresh-main witness")

    results = parse_json(results_before, "results")
    witness_digest = sha256(witness_before)
    required_top = {
        "joint_pointer_id": POINTER_ID,
        "control_commit": witness["control_commit"],
        "control_revision": witness["control_revision"],
        "readme_git_blob": witness["readme_git_blob"],
        "order_git_blob": witness["order_git_blob"],
        "research_state_git_blob": witness["research_state_git_blob"],
        "truth_witness_sha256": witness_digest,
    }
    for key, expected in required_top.items():
        if results.get(key) != expected:
            raise GateError(f"results/witness binding mismatch: {key}")
    if results.get("full_brain_connected") is not False:
        raise GateError("results must not promote full_brain_connected")

    cmd = [
        sys.executable,
        "-B",
        str(v1_gate),
        "--order",
        str(order_path),
        "--research-state",
        str(state_path),
        "--results",
        str(results_path),
        "--expected-order-git-blob",
        witness["order_git_blob"],
        "--expected-state-git-blob",
        witness["research_state_git_blob"],
    ]
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    try:
        child = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
            check=False,
            env=env,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GateError(f"v1 gate execution failed: {type(exc).__name__}") from exc
    try:
        child_obj = json.loads(child.stdout.strip())
    except json.JSONDecodeError as exc:
        raise GateError("v1 gate emitted invalid JSON") from exc
    if (
        child.returncode != 0
        or not isinstance(child_obj, dict)
        or child_obj.get("status") != "PASS_LIVE_FEI_TRUTH_BOUND"
        or child_obj.get("full_brain_connected") is not False
    ):
        raise GateError("v1 semantic truth gate did not pass")
    if child_obj.get("order_git_blob") != witness["order_git_blob"]:
        raise GateError("v1 output ORDER binding mismatch")
    if child_obj.get("research_state_git_blob") != witness["research_state_git_blob"]:
        raise GateError("v1 output RESEARCH_STATE binding mismatch")
    if child_obj.get("results_sha256") != sha256(results_before):
        raise GateError("v1 output results digest mismatch")

    after = {
        "v1": load_regular(v1_gate, max_bytes=2_000_000),
        "order": load_regular(order_path, max_bytes=2_000_000),
        "state": load_regular(state_path, max_bytes=4_000_000),
        "results": load_regular(results_path, max_bytes=4_000_000),
        "witness": load_regular(witness_path, max_bytes=32_000),
    }
    before = {
        "v1": v1_before,
        "order": order_before,
        "state": state_before,
        "results": results_before,
        "witness": witness_before,
    }
    if after != before:
        raise GateError("acceptance inputs changed during validation")

    return {
        "status": "PASS_LIVE_FEI_TRUTH_BOUND_V2",
        "joint_pointer_id": POINTER_ID,
        "control_commit": witness["control_commit"],
        "control_revision": witness["control_revision"],
        "readme_git_blob": witness["readme_git_blob"],
        "order_git_blob": witness["order_git_blob"],
        "research_state_git_blob": witness["research_state_git_blob"],
        "truth_witness_sha256": witness_digest,
        "results_sha256": sha256(results_before),
        "v1_gate_git_blob": expected_v1_blob,
        "v1_output_sha256": sha256(child.stdout.encode("utf-8")),
        "acceptance_scope": "fresh-main semantic truth binding only; not production retrieval acceptance",
        "full_brain_connected": False,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--v1-gate", required=True, type=Path)
    p.add_argument("--order", required=True, type=Path)
    p.add_argument("--research-state", required=True, type=Path)
    p.add_argument("--results", required=True, type=Path)
    p.add_argument("--live-witness", required=True, type=Path)
    p.add_argument("--max-witness-age-seconds", type=int, default=DEFAULT_MAX_AGE_SECONDS)
    args = p.parse_args(argv)
    try:
        out = validate(
            v1_gate=args.v1_gate,
            order_path=args.order,
            state_path=args.research_state,
            results_path=args.results,
            witness_path=args.live_witness,
            max_age_seconds=args.max_witness_age_seconds,
        )
    except (GateError, OSError, UnicodeError) as exc:
        print(json.dumps({"status": "FAIL_CLOSED", "error": str(exc), "full_brain_connected": False}, sort_keys=True))
        return 2
    print(json.dumps(out, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
