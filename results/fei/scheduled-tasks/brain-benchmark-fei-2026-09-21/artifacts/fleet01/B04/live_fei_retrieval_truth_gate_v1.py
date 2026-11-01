#!/usr/bin/env python3
"""Fail-closed semantic gate for FEI retrieval against the live joint research state.

This component does not perform retrieval and cannot establish brain acceptance.  It
checks that already-produced *production* retrieval case records are semantically
compatible with an exact, immutable FEI ORDER/RESEARCH_STATE snapshot.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

POINTER_ID = "FEI-JOINT-FOUR-ACCOUNTS-2026-09-21-192650Z"
REQUIRED_CASES = {
    "full_fei_status",
    "positive_current_budget_status",
    "kernel_constants_scope",
    "subcube_peeling_scope",
}

class GateError(RuntimeError):
    pass


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _git_blob_sha(data: bytes) -> str:
    h = hashlib.sha1()
    h.update(f"blob {len(data)}\0".encode("ascii"))
    h.update(data)
    return h.hexdigest()


def _load_regular(path: Path) -> bytes:
    if path.is_symlink():
        raise GateError(f"symlink rejected: {path.name}")
    st = path.stat()
    if not path.is_file():
        raise GateError(f"not a regular file: {path.name}")
    if st.st_size > 4_000_000:
        raise GateError(f"input too large: {path.name}")
    return path.read_bytes()


def _truth(v: Any) -> bool:
    return v is True


def _norm(s: Any) -> str:
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def _require_anchor(text: str, needle: str, label: str) -> None:
    if _norm(needle) not in _norm(text):
        raise GateError(f"live state missing required anchor: {label}")


def _assert_common(case: dict[str, Any], state_blob: str, order_blob: str) -> None:
    if case.get("research_state_git_blob") != state_blob:
        raise GateError(f"{case.get('id')}: state blob binding mismatch")
    if case.get("order_git_blob") != order_blob:
        raise GateError(f"{case.get('id')}: order blob binding mismatch")
    if not _truth(case.get("evidence_verified")):
        raise GateError(f"{case.get('id')}: evidence not VERIFIED")
    if not _truth(case.get("citation_binding_checked")):
        raise GateError(f"{case.get('id')}: citation binding not checked")
    for k in ("query_digest", "database_digest"):
        v = case.get(k)
        if not isinstance(v, str) or not re.fullmatch(r"[0-9a-f]{64}", v):
            raise GateError(f"{case.get('id')}: invalid {k}")


def _validate_case(case: dict[str, Any]) -> None:
    cid = case["id"]
    claim = _norm(case.get("claim"))
    warnings = " ".join(_norm(x) for x in case.get("warnings", []))

    if cid == "full_fei_status":
        if case.get("status") != "OPEN_NOT_PROVED":
            raise GateError("full_fei_status: must be OPEN_NOT_PROVED")
        if "open" not in claim or ("not proved" not in claim and "not proven" not in claim):
            raise GateError("full_fei_status: claim must explicitly say open/not proved")
        if _truth(case.get("solved")):
            raise GateError("full_fei_status: solved=true is forbidden")

    elif cid == "positive_current_budget_status":
        if case.get("status") != "REFUTED_AT_STATED_SCOPE":
            raise GateError("positive_current_budget_status: refuted status required")
        if "refut" not in claim:
            raise GateError("positive_current_budget_status: claim must state refutation")
        if "refut" not in warnings and "supersed" not in warnings and "stale" not in warnings:
            raise GateError("positive_current_budget_status: supersession/refutation warning required")
        if _truth(case.get("accepted_as_theorem")):
            raise GateError("positive_current_budget_status: stale theorem acceptance forbidden")
        if case.get("counterexample_to_fei") is not False:
            raise GateError("positive_current_budget_status: must preserve NOT-a-counterexample-to-FEI scope")

    elif cid == "kernel_constants_scope":
        if case.get("status") != "PROVED_KERNEL_SCOPE":
            raise GateError("kernel_constants_scope: proved kernel scope required")
        required = ("s<=pi m", "p<=(pi^2/2-pi)m", "s+p<=(pi^2/2)m")
        compact = claim.replace("π", "pi").replace(" ", "")
        for token in required:
            if token.replace(" ", "") not in compact:
                raise GateError(f"kernel_constants_scope: missing {token}")
        if case.get("scope") != "KERNEL_CONSTANTS_NOT_FEI_CONSTANTS":
            raise GateError("kernel_constants_scope: kernel/FEI scope binding required")

    elif cid == "subcube_peeling_scope":
        if case.get("status") != "PROVED_RESTRICTED_SCOPE":
            raise GateError("subcube_peeling_scope: restricted proved status required")
        if case.get("coefficient") != "4(1+epsilon)":
            raise GateError("subcube_peeling_scope: coefficient mismatch")
        if case.get("physical_block_payment") != "12 I_Z":
            raise GateError("subcube_peeling_scope: payment mismatch")
        if case.get("universal_fei_constant") is not False:
            raise GateError("subcube_peeling_scope: 12 must not be promoted to universal FEI constant")
        if "not a universal fei constant" not in claim:
            raise GateError("subcube_peeling_scope: claim must preserve non-universal scope")


def validate(order_path: Path, state_path: Path, results_path: Path,
             expected_order_blob: str, expected_state_blob: str) -> dict[str, Any]:
    order_before = _load_regular(order_path)
    state_before = _load_regular(state_path)
    results_raw = _load_regular(results_path)

    if _git_blob_sha(order_before) != expected_order_blob:
        raise GateError("ORDER git blob mismatch")
    if _git_blob_sha(state_before) != expected_state_blob:
        raise GateError("RESEARCH_STATE git blob mismatch")

    order_text = order_before.decode("utf-8")
    state_text = state_before.decode("utf-8")
    _require_anchor(order_text, POINTER_ID, "joint pointer id")
    _require_anchor(state_text, "Full FEI remains OPEN", "FEI open status")
    _require_anchor(state_text, "positive-current O(J) budget are REFUTED", "latest positive-current refutation")
    _require_anchor(state_text, "kernel constants, not FEI constants", "kernel-vs-FEI scope")
    _require_anchor(state_text, "Twelve is NOT a universal FEI constant", "subcube constant scope")

    try:
        payload = json.loads(results_raw)
    except Exception as exc:
        raise GateError(f"invalid results JSON: {exc}") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("cases"), list):
        raise GateError("results must contain cases list")
    if payload.get("joint_pointer_id") != POINTER_ID:
        raise GateError("results pointer id mismatch")
    if payload.get("research_state_git_blob") != expected_state_blob:
        raise GateError("top-level state binding mismatch")
    if payload.get("order_git_blob") != expected_order_blob:
        raise GateError("top-level order binding mismatch")
    if payload.get("full_brain_connected") is not False:
        raise GateError("gate input must not promote full_brain_connected")

    seen: set[str] = set()
    for raw in payload["cases"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str):
            raise GateError("each case needs string id")
        cid = raw["id"]
        if cid in seen:
            raise GateError(f"duplicate case: {cid}")
        seen.add(cid)
        if cid not in REQUIRED_CASES:
            continue
        _assert_common(raw, expected_state_blob, expected_order_blob)
        _validate_case(raw)
    missing = sorted(REQUIRED_CASES - seen)
    if missing:
        raise GateError("missing required cases: " + ",".join(missing))

    order_after = _load_regular(order_path)
    state_after = _load_regular(state_path)
    if order_after != order_before or state_after != state_before:
        raise GateError("truth inputs changed during validation")

    return {
        "status": "PASS_LIVE_FEI_TRUTH_BOUND",
        "joint_pointer_id": POINTER_ID,
        "order_git_blob": expected_order_blob,
        "order_sha256": _sha256(order_before),
        "research_state_git_blob": expected_state_blob,
        "research_state_sha256": _sha256(state_before),
        "results_sha256": _sha256(results_raw),
        "required_cases": sorted(REQUIRED_CASES),
        "full_brain_connected": False,
        "acceptance_scope": "semantic_truth_binding_only_not_production_retrieval_acceptance",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--order", required=True, type=Path)
    p.add_argument("--research-state", required=True, type=Path)
    p.add_argument("--results", required=True, type=Path)
    p.add_argument("--expected-order-git-blob", required=True)
    p.add_argument("--expected-state-git-blob", required=True)
    args = p.parse_args(argv)
    try:
        out = validate(args.order, args.research_state, args.results,
                       args.expected_order_git_blob, args.expected_state_git_blob)
    except (GateError, OSError, UnicodeError) as exc:
        print(json.dumps({"status": "FAIL_CLOSED", "error": str(exc), "full_brain_connected": False}, sort_keys=True))
        return 2
    print(json.dumps(out, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
