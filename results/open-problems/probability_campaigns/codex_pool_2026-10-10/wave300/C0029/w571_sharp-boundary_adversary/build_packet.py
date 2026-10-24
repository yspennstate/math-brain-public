"""Build local C0029 correction and DRAFT material; never write a live store."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INTAKE = Path("~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907")
LIMIT_SOURCE = "https://websites.umich.edu/~rudelson/papers/rv-ICM2010.pdf"
SSS_SOURCE = "https://arxiv.org/html/2405.20308v2"
OP_LOGICAL = "math:probability.random-matrices:open-problem-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr"
AT_LOGICAL = "math:probability.random-matrices:attempt-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr"


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_claim(claim: dict) -> None:
    path = ROOT / "CLAIMS.jsonl"
    existing = {json.loads(line)["id"] for line in path.read_text(encoding="utf-8").splitlines() if line}
    if claim["id"] not in existing:
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(claim, ensure_ascii=False) + "\n")


def main() -> None:
    measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
    assert measurements["verdict"] == "PASS" and "B04" in measurements
    snapshot = json.loads((ROOT / "POPULATION_C0029_SNAPSHOT.json").read_text(encoding="utf-8"))
    target = next(r for r in snapshot if r["id"].startswith("claim_cbd6e1bc"))
    assert "Edelman's exact law" in target["body"]

    for number, statement, assumptions, proof, gap in [
        ("B03", "For every even n>=2 there is a full-row-rank (n-1) by n sign matrix A with kernel spanned by the perfectly flat unit vector (1,...,1)/sqrt(n), for which an independent iid Rademacher row X has P(dist(X,rowspan(A))=0)=binom(n,n/2)/2^n>=1/(n+1).", ["n even and >=2", "fixed A built from independent balanced sign rows", "X independent iid uniform signs"], "Balanced rows span the zero-sum hyperplane: differences include 2(e_i-e_j). Select a basis. The projection vanishes exactly when X is balanced. See ATTEMPT.md B03.", "Independent w572 review pending. Conditional obstruction only; no averaged or parent-problem refutation."),
        ("B04", "H(t)=1-exp(-t-t^2/2) is not the exact finite-n least-singular-value CDF of real iid standard Gaussian matrices. At n=1 the CDF is erf(t/sqrt(2)), with derivative sqrt(2/pi) at zero instead of one.", ["real iid N(0,1) matrix", "unnormalised entries", "n=1 counterexample", "t>=0"], "The single singular value of [Z] is |Z|. Integrate the standard Gaussian density. The finite-n versus limit distinction is explicitly stated in Rudelson-Vershynin ICM 2010 Theorem 3.1 and (3.2), p.9.", "Independent correction review and coordinator application pending; no live store change made.")
    ]:
        append_claim({"id": f"w571-C0029-{number}", "statement": statement,
                      "assumptions": assumptions, "source": "ATTEMPT.md" if number == "B03" else LIMIT_SOURCE,
                      "proof_or_counterexample": proof,
                      "independent_reviewer": {"agent": "w572", "state": "pending"},
                      "remaining_gap": gap, "status": "proved special case",
                      "draft": True, "created": "2026-10-10"})

    corrections_path = ROOT / "SOURCE_CORRECTIONS.jsonl"
    correction = json.loads(corrections_path.read_text(encoding="utf-8").strip())
    correction["primary_source"] = {"url": LIMIT_SOURCE, "locator": "Theorem 3.1 and equation (3.2), printed p.9, PDF page index 8", "source_quote": "This approach leads to the following asymptotic result:", "formula_evidence": "Theorem 3.1 explicitly uses convergence to H(epsilon) as n tends to infinity; (3.2) is the separate all-n upper bound.", "finite_n_source": SSS_SOURCE + "#S9", "finite_n_locator": "Theorem 9.4"}
    correction["population_store_readonly_confirmed"] = True
    correction["target_snapshot_digest"] = target["digest"]
    corrections_path.write_text(json.dumps(correction, ensure_ascii=False) + "\n", encoding="utf-8")

    # Read only the named record; preserve its exact line for a zero-context patch.
    found = []
    with (INTAKE / "attempts.jsonl").open(encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, 1):
            if '"attempt_id": "C0029-A001"' in raw:
                found.append((line_no, raw.rstrip("\r\n"), json.loads(raw)))
    assert len(found) == 1
    line_no, old_line, record = found[0]
    original_record = dict(record)
    record["key_identity"] = "Real Gaussian hard-edge LIMIT: for each fixed t>=0, lim_{n->infinity} P(sqrt(n)*s_min(G_n)<=t)=1-exp(-t-t^2/2). The finite-n Gaussian CDF is distinct and satisfies P(sqrt(n)*s_min(G_n)<=t)<=t."
    old_phrase = "For the Gaussian matrix Edelman's exact law gives P(sqrt n s_n <= t) = 1 - e^{-t^2/2 - t} ~ t as t -> 0, so the constant 1 is exactly the Gaussian density at zero of sqrt n s_n;"
    assert old_phrase in record["result"]
    record["result"] = record["result"].replace(old_phrase, "For real Gaussian matrices the hard-edge LIMIT as n tends to infinity has CDF 1-exp(-t-t^2/2), whose right derivative at zero is one; this is not an exact finite-n CDF;")
    record["review_note"] = "DRAFT correction w571 2026-10-10, independent review pending: do not replace the finite-n Gaussian CDF by its limit. Rudelson-Vershynin ICM 2010 Theorem 3.1 and (3.2) distinguish them; n=1 gives erf(t/sqrt(2)). The historical attempt's universality discussion must also be read with SSS 2405.20308v2 Theorems 1.1/1.2, which achieve 1+O_xi((log n)^(-1/16)) with an exponential remainder, not exact coefficient one."
    record["review_note_sources"] = [LIMIT_SOURCE, SSS_SOURCE]
    new_line = json.dumps(record, ensure_ascii=False, sort_keys=True)
    live_relative = "06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl"
    patch = f"--- a/{live_relative}\n+++ b/{live_relative}\n@@ -{line_no},1 +{line_no},1 @@\n-{old_line}\n+{new_line}\n"
    patch_path = ROOT / "patches/01_c0029_gaussian_limit.diff"
    patch_path.parent.mkdir(parents=True, exist_ok=True)
    patch_path.write_text(patch, encoding="utf-8")
    write_json(ROOT / "source_snapshots/C0029-A001.original.json", original_record)
    write_json(ROOT / "source_snapshots/C0029-A001.corrected.json", record)
    write_json(ROOT / "PATCH_CHECK.json", {"verdict": "PASS", "target_line": line_no,
               "old_line_matches_named_current_intake_record": True,
               "corrected_record_is_valid_json": True,
               "patch_changes": 1, "applied": False,
               "note": "No live file or git state modified; coordinator must apply-check after review."})

    status = json.loads((ROOT / "SOURCE_STATUS.json").read_text(encoding="utf-8"))
    status["canonical_intake_target"] = {"statement": "There exist rho in (0,1), n0>=1 and t0>0 such that for all n>=n0 and all 0<=t<=t0, P(sqrt(n)*s_min(B_n)<=t)<=t+rho^n.", "locator": "C0029 problems.jsonl:29; Bordenave-Chafai Section 7, printed p.53 (PDF index52)", "url": "https://arxiv.org/pdf/1109.3343", "scope_note": "This is the large-n/small-t candidate in the intake. Finite-n obstructions in this packet test auxiliary statements, not this target."}
    status["exact_target"]["remainder_convention"] = "Modern exponential-remainder formulation. Original Spielman-Teng ICM 2002 Conjecture 2, printed p.605, concerns iid sign matrices and inverse norm: P(||A^-1||>T)<=sqrt(n)/T+alpha^n. Original printed dimension/exponent notation mixes d and n; use consistent n via the modern statement. Closed singular-value endpoints follow by threshold limits."
    status["original_source"] = {"url": "https://arxiv.org/pdf/math/0212413", "locator": "Conjecture 2, p.605, PDF index8", "verified": True}
    status["prior_records"] = {"C0029": "problems.jsonl:29", "attempt": "attempts.jsonl:23, C0029-A001", "ranking": "RANKING_2026-09-07.csv:428, tier4 attempted_un", "H_I_lean": "Targeted C0029 searches found the ranking annotation, no separate C0029 proof in named H/I attempt directories.", "Team_O": "Targeted C0029/Spielman/Teng search found no matching Team O row.", "owner_solved_retired_status": "Not certified by this bounded search; current openness remains UNKNOWN."}
    status["gaussian_distinction_source"] = correction["primary_source"]
    status["population_readonly_check"] = {"store": "~/math-brain-build/local/population/brain.sqlite3", "matched_exact_claim_ids": [r["id"] for r in snapshot], "snapshot": "POPULATION_C0029_SNAPSHOT.json", "wrote_to_store": False}
    status["checks_pending"] = ["Named independent mathematical review", "Response-side served-model provenance gate", "Coordinator integration and retrieval receipt", "Complete current owner solved/retired-status certification"]
    write_json(ROOT / "SOURCE_STATUS.json", status)

    source = {"source_id": "owner-own-work:probability300:C0029:w571:20261010", "url": "file:///~/brain_workers/w571/ATTEMPT.md", "revision": "draft-unreviewed-2026-10-10", "license": "owner-own-work", "excerpt": None}
    entry_specs = [
        ("cdf-transfer-obstruction", "multiplicative-hard-edge-comparison-does-not-imply-coefficient-one", "Draft: multiplicative hard-edge comparison obstruction", "DRAFT author proof, independent review pending. Put H(t)=1-exp(-t-t^2/2), delta_n=(log(n+e))^(-1/16), p_n=exp(-n), and F_n(t)=p_n+(1-p_n)H((1+delta_n)t) for t>=0, with F_n(t)=0 for t<0. These are scalar CDFs with H(t)<=F_n(t)<=(1+delta_n)H(t)+p_n, and the same weak limit H. Yet at t=sqrt(delta_n)/2, F_n(t)-t>=delta_n^(3/2)/6, too large for any C exp(-c n). This refutes an abstract error-removal bridge only; it is not an iid matrix law or a refutation of C0029 or finite-n Gaussian comparison.", ["scalar CDFs", "n>=1", "t>=0", "no iid-matrix realization asserted"]),
        ("flat-kernel-atom", "full-row-rank-flat-kernel-does-not-give-exponential-small-ball-error", "Draft: flat kernel vectors retain arithmetic atoms", "DRAFT author proof, independent review pending. For every even n>=2, balanced sign rows span {x:sum x_i=0}. Select n-1 independent rows as A; its unit kernel vector is (1,...,1)/sqrt(n), perfectly flat. For an independent iid uniform sign row X, P(dist(X,rowspan(A))=0)=binom(n,n/2)/2^n>=1/(n+1). Thus full row rank and coordinate flatness alone do not give a uniform conditional small-ball estimate C epsilon+C exp(-c n). At n=4 the three rows (1,1,-1,-1), (1,-1,1,-1), (1,-1,-1,1) have Gram matrix 4I and zero-projection probability 3/8. These row blocks may be rare; no averaged estimate or parent conjecture is refuted.", ["even n>=2", "deterministic full-row-rank balanced sign block A", "independent iid uniform sign row X", "pointwise conditional statement, not an average"]),
        ("gaussian-finite-limit-correction", "gaussian-hard-edge-limit-is-not-the-finite-dimension-cdf", "Draft correction: Gaussian finite-dimensional law versus hard-edge limit", "DRAFT source correction, independent review pending. For an n by n real matrix G_n with iid N(0,1) entries, Rudelson-Vershynin ICM 2010 Theorem 3.1 states convergence, for each fixed t>=0 as n tends to infinity, of P(sqrt(n)*s_min(G_n)<=t) to H(t)=1-exp(-t-t^2/2). Their separate equation (3.2) gives the all-n upper bound by t. H is not the exact finite-n CDF: at n=1 the CDF is erf(t/sqrt(2)) and its right derivative at zero is sqrt(2/pi), not one. Preserve finite-n Gaussian CDFs in comparisons; the limiting-law identity in the existing C0029 attempt card needs this qualifier.", ["real iid N(0,1)", "variance-one unnormalised entries", "fixed t in the limit statement", "finite-n comparison distinct from its limit"]),
    ]
    entries = [{"key": key, "namespace": "probability.random-matrices", "logical_name": logical,
                "kind": "concept", "title": title, "statement": statement, "proof_text": None,
                "assumptions": assumptions, "domain": "probability theory", "source": dict(source)}
               for key, logical, title, statement, assumptions in entry_specs]
    relations = [
        {"from_key": "cdf-transfer-obstruction", "to_existing_logical": OP_LOGICAL, "kind": "semantic_association", "rationale": "C0029's coefficient-one target is stronger than approximate universality. The scalar counterexample isolates why a relative error cannot be discarded; it does not refute the target."},
        {"from_key": "flat-kernel-atom", "to_existing_logical": OP_LOGICAL, "kind": "semantic_association", "rationale": "A uniform full-rank flat-normal conditional bridge for iid sign matrices fails on balanced row blocks; an averaged arithmetic estimate would require additional work."},
        {"from_key": "gaussian-finite-limit-correction", "to_existing_logical": AT_LOGICAL, "kind": "semantic_association", "rationale": "The existing attempt claims H is a finite-n exact Gaussian law. The n=1 Gaussian CDF and the explicitly asymptotic primary source identify the missing limit qualifier; other contents of the attempt are not refuted."},
    ]
    bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w571", "bundle_slug": "c0029-sharp-boundary-route-obstructions-w571-20261010", "entries": entries, "relations": relations}
    assert len(entries) <= 200 and all(e["kind"] == "concept" and e["proof_text"] is None for e in entries)
    assert all(r["kind"] in {"semantic_association"} for r in relations)
    write_json(ROOT / "drafts/bundle_001.json", bundle)
    write_json(ROOT / "DRAFT_VALIDATION.json", {"verdict": "PASS", "entries": len(entries), "relations": len(relations), "all_new_results_concepts": True, "all_statement_guards_draft": True, "source_license": "owner-own-work", "live_ingestor_run": False, "note": "Local structural checks only; not a theorem/provenance review or integration receipt."})

    hook = {"id": "c0029-error-removal-w571-01", "area": "math", "event": "stage-start", "cue": "coefficient[- ]one|constant[- ]one", "fire_when": "A coefficient-one proof discards a relative 1+o(1) probability error by passing to the limit while retaining a uniform exponential remainder.", "silent_when": "The target itself permits 1+o(1), or a separate estimate bounds the coefficient excess uniformly by C exp(-c n).", "text": "Carry the relative error through the target quantifiers. A 1+o(1) factor can leave excess far above an exponential remainder; identify the extra estimate that removes it before claiming coefficient one.", "evidence": "w571/ATTEMPT.md B02 and MEASUREMENTS.json B02; perceptron_proof_open_gaps_fleet_2026_07_12", "proposer": "w571"}
    assert len(hook["text"]) <= 300
    (ROOT / "HOOK_PROPOSAL.jsonl").write_text(json.dumps(hook) + "\n", encoding="utf-8")
    print(json.dumps({"claims": 4, "corrections": 1, "draft_entries": 3, "draft_relations": 3,
                      "patch": str(patch_path), "live_writes": False}))


if __name__ == "__main__":
    main()
