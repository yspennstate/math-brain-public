"""Prepare one local review bundle; --submit stages only the task-named inbox file."""
from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w376")
LIVE_REL = "math-brain-inbox/w376/bundle_001.json"


def entry(key: str, logical: str, title: str, statement: str, assumptions: list[str]) -> dict:
    return {
        "key": key, "namespace": "probability.fpp", "logical_name": logical,
        "kind": "concept", "title": title, "statement": statement,
        "proof_text": None, "assumptions": assumptions,
        "domain": "probability theory",
        "source": {
            "source_id": f"owner-probability-campaign-w376-20261010:{key}",
            "url": f"urn:probability-research:20261010:w376:{key}",
            "revision": "unreviewed-draft-v1",
            "license": "owner-own-work (w376 original audit; independent review pending)",
            "excerpt": None,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true")
    args = parser.parse_args()
    entries = [
        entry(
            "oscillation-obstruction",
            "oscillating-kpz-balance-does-not-imply-strong-exponent-existence",
            "Draft: exact KPZ balances can coexist with unequal exponent thresholds",
            "DRAFT, independent review pending. For integers n>=2, let a_n=1/4 on even n and 1/3 on odd n. Set X_n=n^(a_n) Z for a symmetric random sign Z, and D_n=n^((1+a_n)/2). Define chi_a as the infimum of q with some alpha>0 such that sup_n E exp(alpha |X_n|/n^q)<infinity; define chi_b as the supremum of q with some N such that inf_{n>=N} Var(X_n)/n^(2q)>0. Define xi_a and xi_b in the same way using D_n for upper moments and E D_n for lower bounds. Then chi_a=1/3, chi_b=1/4, xi_a=2/3, xi_b=5/8. At every scale sqrt(Var(X_n))=D_n^2/n; both endpoint identities chi_a=2xi_a-1 and chi_b=2xi_b-1 hold, but the threshold gaps are 1/12 and 1/24. This refutes an abstract inference from scale balances to common strong exponents. These observables are NOT an iid FPP model; no FPP nonexistence or exponent theorem follows.",
            ["Abstract integer-indexed observables, not FPP passage times or geodesics", "Upper bounds are uniform exponential moments; lower bounds allow a finite index cutoff", "The odd and even subsequences are both unbounded"],
        ),
        entry(
            "finite-endpoint-obstruction",
            "fpp-lower-wandering-premise-needs-its-finite-cutoff",
            "Draft: all-endpoint wandering lower bounds fail for a bounded positive iid law",
            "DRAFT, independent review pending. In nearest-neighbor undirected FPP on Z^d, d>=2, with iid Uniform[1,2] edge weights, the unique geodesic from 0 to e1 is the direct edge in every environment: its cost is at most 2, while every other self-avoiding path has odd length at least 3 and cost at least 3. Hence D(0,e1)=0, where D is maximum Euclidean deviation of the geodesic set from the joining segment. For every real r, inf_{v!=0} E D(0,v)/|v|^r=0. This is a finite-endpoint obstruction, not a statement about asymptotic wandering. The all-endpoint lower infimum printed in Auffinger-Damron equation (2.2), https://arxiv.org/pdf/1109.0523, differs from the tail-cutoff lower premise in Chatterjee Theorem 1.1, https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf. Preserve that distinction when invoking either theorem; changing a cited premise needs justification.",
            ["Nearest-neighbor undirected Z^d with d>=2", "Every edge weight lies in [1,2]", "The lower infimum includes the endpoint e1"],
        ),
        entry(
            "raw-coupling-drift-obstruction",
            "separated-fpp-marginal-drifts-obstruct-every-raw-sublinear-coupling",
            "Draft: changing a coupling cannot erase a raw linear FPP drift gap",
            "DRAFT, independent review pending. Suppose U_n/n has almost-sure limsup at most mu-c under its marginal sequence law, while V_n/n tends almost surely to mu under its marginal sequence law, for a deterministic c>0. Under any joint coupling at each n and any 0<epsilon<c/2, P((V_n-U_n)/n>=c-2epsilon) is at least 1-P(U_n/n>mu-c+epsilon)-P(V_n/n<mu-epsilon), and this tends to 1. No independence is required, and the coupling may vary with n. In bounded positive nondegenerate iid FPP, w375's audited connector-separated detour construction supplies this drift gap between unrestricted and directed axial passage times. For the Uniform[1,2] low=[1,5/4], high=[7/4,2], k=6 witness, the certified saving is at least 1/3758096384. A different coupling alone therefore cannot give a raw o_P(n) approximation. This does not exclude different deterministic centering or equality of centered fluctuation universality classes. The mathematical argument and exact input assumptions are in w376 ATTEMPT.md and PEER_AUDIT.md; novelty and target solution are not claimed.",
            ["Deterministic marginal drift separation c>0", "Original marginal sequence laws supply the stated almost-sure limits; arbitrary new couplings preserve each n's marginals", "The FPP application requires the exact bounded positive iid hypotheses of w375 L2, independently reviewed by w376 but awaiting final referee w377"],
        ),
        entry(
            "conditional-kpz-premise-audit",
            "p0110-conditional-kpz-relation-needs-an-exponent-existence-certificate",
            "Draft: P0110 law certificates must verify exponent existence",
            "DRAFT source-audit guidance, independent review pending. P0110 asks for a nondegenerate iid undirected lattice FPP law with well-defined fluctuation and wandering exponents satisfying chi=2xi-1; equation (4.19) and Question 22 of Auffinger-Damron-Hanson, https://arxiv.org/pdf/1511.03262, do not settle exponent existence or mandate only one definition. A proposed solution must state its exponent definition and prove existence for the exhibited law. If it uses Chatterjee Theorem 1.1, https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf, it must check iid nearest-neighbor weights on Z^d, d>=2, a nearly-gamma law, finite moment generating function near zero, the uniform upper exponential-moment and tail-uniform lower variance/mean-deviation premises, and chi_a=chi_b plus xi_a=xi_b. A scale balance or conditional theorem citation alone supplies none of the two coincidence certificates. Keep tail cutoffs and all-endpoint infima distinct. Directed-model transfers must account for deterministic centering and an error on the fluctuation scale; changing the coupling alone cannot erase separated raw marginal drifts. Current openness is UNKNOWN; this draft certifies no solved target or novelty.",
            ["The campaign's P0110 target is the survey's Question 22 in ordinary iid undirected lattice FPP", "Conditional-theorem hypotheses must be verified for the actual exhibited law", "Own audit concepts have not yet passed independent review"],
        ),
    ]
    relations = [
        {"from_key": "conditional-kpz-premise-audit", "to_key": "oscillation-obstruction", "kind": "depends_on",
         "rationale": "The explicit oscillating observables show why exact balances cannot replace the two exponent-coincidence certificates demanded by the audit guidance."},
        {"from_key": "conditional-kpz-premise-audit", "to_key": "finite-endpoint-obstruction", "kind": "cites",
         "rationale": "The guidance cites the Uniform[1,2] endpoint example to require accurate lower-infimum cutoffs when applying a primary theorem."},
        {"from_key": "conditional-kpz-premise-audit", "to_key": "raw-coupling-drift-obstruction", "kind": "cites",
         "rationale": "The guidance cites the coupling-independent raw drift separation to require correct deterministic centering before a directed-model fluctuation transfer."},
    ]
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w376",
              "bundle_slug": "p0110-exponent-premise-audit-w376-001",
              "entries": entries, "relations": relations}
    keys = {e["key"] for e in entries}
    assert len(entries) == len(keys) <= 200
    assert all(e["kind"] == "concept" and e["proof_text"] is None for e in entries)
    assert all(e["source"]["license"].startswith("owner-own-work") for e in entries)
    allowed = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
    assert all(r["from_key"] in keys and r["to_key"] in keys and r["kind"] in allowed for r in relations)
    # This specific dependency graph has one edge and hence no cycle.
    dependencies = [r for r in relations if r["kind"] == "depends_on"]
    assert len(dependencies) == 1 and dependencies[0]["from_key"] != dependencies[0]["to_key"]
    content = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
    local_bundle = ROOT / "bundle_001.json"
    local_bundle.write_text(content, encoding="utf-8")
    patch_dir = ROOT / "patches"
    patch_dir.mkdir(exist_ok=True)
    diff = "".join(difflib.unified_diff([], content.splitlines(keepends=True),
                   fromfile="a/" + LIVE_REL, tofile="b/" + LIVE_REL))
    (patch_dir / "01_p0110_draft_bundle.diff").write_text(diff, encoding="utf-8")
    validation = {"entries": len(entries), "relations": len(relations),
                  "all_entries_remain_unreviewed_concepts": True,
                  "allowed_licenses": True, "internal_relation_ends_resolved": True,
                  "dependency_graph_acyclic": True, "formal_proof_receipt": None}
    (ROOT / "DRAFT_VALIDATION.json").write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    evidence = []
    by_key = {e["key"]: e for e in entries}
    for relation in relations:
        evidence.append({**relation,
            "from_quote": by_key[relation["from_key"]]["statement"],
            "to_quote": by_key[relation["to_key"]]["statement"],
            "review_state": "DRAFT; independent review pending"})
    (ROOT / "RELATIONS_EVIDENCE.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in evidence), encoding="utf-8")
    if args.submit:
        INBOX.mkdir(parents=True, exist_ok=True)
        final = INBOX / "bundle_001.json"
        if final.exists():
            if final.read_text(encoding="utf-8") != content:
                raise RuntimeError("Existing inbox file differs; refusing to overwrite")
        else:
            part = INBOX / "bundle_001.part"
            if part.exists():
                raise RuntimeError("Existing partial file; refusing to overwrite")
            part.write_text(content, encoding="utf-8")
            part.rename(final)
    state = {"draft_created": True, "submitted": args.submit,
             "submitted_path": str(INBOX / "bundle_001.json") if args.submit else None,
             "reviewed": False, "ingested": False, "retrievable": False,
             "retrievability_check": "Not run; coordinator integration and independent review remain pending.",
             "live_store_writes": 0, "command": "python -X utf8 build_review_bundle.py" + (" --submit" if args.submit else "")}
    (ROOT / "SUBMISSION_STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validation": validation, "submission": state}, indent=2))


if __name__ == "__main__":
    main()
