"""Bounded local diagnostics and draft-shape validation; never a proof certificate."""
from __future__ import annotations

import datetime as dt
import json
import math
import time
from decimal import Decimal, localcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def dump(name: str, value: object) -> None:
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def fresh_gate() -> dict:
    # Read only these local pressure fields, excluding process details and remote hosts.
    path = Path("~/.claude/compute/compute_state.json")
    raw = json.loads(path.read_text(encoding="utf-8"))
    fields = ("ts", "host", "status", "mode", "cpu_pct", "mem_avail_mb", "commit_eff_avail_mb", "commit_eff_used_pct")
    receipt = {k: raw.get(k) for k in fields}
    now = dt.datetime.now()
    observed = dt.datetime.strptime(str(raw["ts"]), "%Y-%m-%d %H:%M:%S")
    age = (now - observed).total_seconds()
    receipt.update(observed_at=now.isoformat(), age_seconds=age)
    # Ordinary tiny testing is permitted by the doctrine; a stale or distress gate is not.
    allowed = -5 <= age <= 60 and raw.get("status") in ("ok", "normal", "warn")
    receipt.update(allowed=allowed, workload="stdlib-only CDF diagnostics; no matrices, sampling, training, GPU, new workers or parallel compute", atomic_cpu_seconds_cap=2, extra_numeric_storage_bytes_cap=32768)
    dump("COMPUTE_GATE.json", receipt)
    return receipt


def diagnostics() -> dict:
    gate = fresh_gate()
    if not gate["allowed"]:
        return {"status": "SKIPPED_GATE", "gate": "COMPUTE_GATE.json", "mathematical_proof": False}
    start = time.process_time()
    witnesses = []
    for t in (0.1, 0.5, 1.0):
        true_n1 = math.erf(t / math.sqrt(2))
        false_finite_law = -math.expm1(-t - t*t/2)
        witnesses.append({"t": t, "real_gaussian_n1": true_n1, "stored_exact_formula": false_finite_law, "absolute_error": abs(true_n1-false_finite_law)})
    assert all(w["absolute_error"] > 0.01 for w in witnesses)
    checked = 0
    samples = []
    with localcontext() as context:
        context.prec = 100
        one = Decimal(1)
        two = Decimal(2)
        e = one.exp()
        for n in (16, 256, 1024):
            nd = Decimal(n)
            eta = (-(nd+e).ln().ln()/16).exp()
            a = (-nd.sqrt()).exp()
            q = two**(-n)

            def F(t: Decimal) -> Decimal:
                return one - (-t-t*t/2).exp()

            m = eta*F(a)/2

            def G(t: Decimal) -> Decimal:
                return q+(one-q)*((one-m)*F(t)+(m if t >= a else Decimal(0)))

            points = (Decimal(0), a/2, a, a*(one+Decimal("0.000001")), Decimal("0.01"), Decimal("0.1"), one, two)
            previous = Decimal(-1)
            for t in sorted(points):
                value = G(t)
                tolerance = Decimal("1e-90")
                assert -tolerance <= value <= one+tolerance
                assert value+tolerance >= previous
                assert abs(value-F(t)) <= eta*F(t)/2+q+tolerance
                assert value <= Decimal("1.5")*t+q+tolerance
                previous = value
                checked += 4
                if time.process_time()-start > 2:
                    raise RuntimeError("bounded diagnostic CPU budget exceeded")
            excess = G(a)-a
            assert excess >= eta*a/16
            checked += 1
            samples.append({"n": n, "a_n": str(a), "eta_n": str(eta), "excess_at_a_n": str(excess), "proved_lower_bound": str(eta*a/16), "ratio_to_exp_minus_0_1_n": str(excess/(-nd/10).exp())})
    return {"status": "PASS_DIAGNOSTICS", "mathematical_proof": False, "gate": "COMPUTE_GATE.json", "n1_false_identity_witnesses": witnesses, "old_formula_witness_failures": len(witnesses), "corrected_statement_finite_n_identity_assertions": 0, "sampled_inequality_checks": checked, "cdf_samples": samples, "cpu_seconds": time.process_time()-start, "scope": "Finite diagnostics support reproducibility only. The quantified proof is OBSTRUCTION_PROOF.md; no random-matrix experiment or asymptotic inference is made from these samples."}


def validate(path: Path) -> dict:
    b = json.loads(path.read_text(encoding="utf-8"))
    assert b["spec"] == "mathbrain-draft-v1" and b["author_agent"] == "w568"
    assert b["review_state"] == "DRAFT"
    keys = {e["key"] for e in b["entries"]}
    assert len(keys) == len(b["entries"]) <= 200
    required = {"key", "namespace", "logical_name", "kind", "title", "statement", "proof_text", "assumptions", "domain", "source"}
    for e in b["entries"]:
        assert required <= e.keys()
        assert e["kind"] == "concept" and e["proof_text"] is None
        assert e["statement"].startswith("DRAFT") and e["assumptions"]
        assert e["source"]["license"].startswith("owner-own-work")
        assert e["source"]["source_id"] and e["source"]["url"]
    kinds = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    for r in b["relations"]:
        assert r["from_key"] in keys and r["kind"] in kinds
        assert r["rationale"]
        assert r.get("to_key") in keys or r.get("to_existing_logical", "").startswith("math:")
        assert r["kind"] in {"cites", "semantic_association"}
    return {"status": "PASS_DRAFT_SHAPE", "entries": len(b["entries"]), "relations": len(b["relations"]), "theorem_or_lemma_entries": 0, "mathematical_proof": False, "canonical_integrator_run": False}


if __name__ == "__main__":
    result = {"diagnostics": diagnostics(), "draft_validation": validate(ROOT / "drafts/bundle_001.json")}
    dump("MEASUREMENTS.json", result)
    print(json.dumps({"diagnostics": result["diagnostics"]["status"], "checks": result["diagnostics"].get("sampled_inequality_checks", 0), "old_formula_witness_failures": result["diagnostics"].get("old_formula_witness_failures", 0), "draft": result["draft_validation"]}, ensure_ascii=False))
