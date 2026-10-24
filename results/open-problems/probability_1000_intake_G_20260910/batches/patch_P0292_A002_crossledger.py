"""2026-09-10: cross-ledger partial-result row for P0292 (Codex tree, Leskela Problem 4: a necessary and sufficient
condition for the supermodular time ordering (2)). Appended to intake G attempts.jsonl; the Codex tree is not
edited. Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
MEMO = ("~/<private-repo>/06_math_research/prob1000_lean_20260908/"
        "REPORT_P0291_Leskela_problem_3_nonmonotone_chain_with_supermodular_time_ordering_2026-09-10.md")
row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "P0292-A002",
    "problem_id": "P0292",
    "cross_ledger": "Codex tree Downloads/Probability_1000_20h_20260906 (row P0292, Leskela 2022 Problem 4 journal / Problem 3 arXiv)",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": ("Restrict to the star family on 1<2<3 (1->2 at a2, 1->3 at a3, 2->1 at b2, 3->1 at b3; always reversible, "
               "never monotone). Spectral one-gap reduction of the P0291 memo. Necessity from the two-point (concordance) "
               "condition via Cauchy interlacing of the arrowhead generator; sufficiency for b2 = b3 via the biased-coin "
               "version of the block certificate (S_p = sum_k p^k q^{3-k} T_k, each T_k an exact certificate)."),
    "key_identity": ("slow-mode coefficient of P_s(1,3) is c1 = pi3 b3 v1(1)^2 / ((b3 - mu1) <v1,v1>_pi), with "
                     "min(b2,b3) < mu1 < max(b2,b3) strictly when b2 != b3; bivariate condition for ANY reversible 3-state "
                     "chain: l1(1) l1(3) <= 0 for the slow left eigenvector l1 = pi v1."),
    "result": ("PARTIAL, on the star family: (2) FAILS whenever b3 > b2 (already for n = 2: P_s(1,3) overshoots, so "
               "P(X_0<=1, X_s<=2) eventually increases) and HOLDS whenever b2 = b3, for all arrival rates a2, a3 > 0 "
               "(Theorem 2 of the memo). Conjecture: on stars (2) <=> b2 >= b3; the b2 > b3 case passed the exact LP dual "
               "test of >=_sm at n = 3, 4 at every point tried (p0292_star_family_map.out) but is unproved. So the "
               "characterisation Leskela asks for is neither monotonicity nor symmetry; on three states the two-point "
               "condition is the sign condition l1(1) l1(3) <= 0 on the slow left eigenvector, and whether it is also "
               "sufficient beyond stars is being mapped on random reversible 3-state chains (p0292_random_3state_map.py)."),
    "result_status": "partial_result",
    "obstruction": ("For b2 > b3 the leaf-period length depends on the label, so the centre/leaf skeleton is not an "
                    "autonomous Markov chain and the finite block reduction does not apply; a proof needs either a new "
                    "coupling of the three prefix laws or a different route to the two spectral inequalities."),
    "independent_check": "",
    "artifact": MEMO,
}
with (HERE / "attempts.jsonl").open("a", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
print("appended P0292-A002 (cross-ledger, partial)")
