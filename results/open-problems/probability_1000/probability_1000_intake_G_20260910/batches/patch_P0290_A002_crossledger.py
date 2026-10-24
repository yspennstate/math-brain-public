"""2026-09-10: cross-ledger attempt row for P0290 (Codex tree, Leskela Problem 2: does Ross's workload monotonicity (1)
hold for lambda = f(X) with f Boolean/deterministic on a doubly stochastically monotone CTMC X?). Negative search
result at light traffic and at moderate load; recorded in intake G attempts.jsonl. Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
MEMO = ("~/<private-repo>/06_math_research/prob1000_lean_20260908/"
        "REPORT_P0291_Leskela_problem_3_nonmonotone_chain_with_supermodular_time_ordering_2026-09-10.md")
row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "P0290-A002",
    "problem_id": "P0290",
    "cross_ledger": "Codex tree Downloads/Probability_1000_20h_20260906 (row P0290, Leskela 2022 Problem 2 journal / Problem 1-related arXiv)",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": ("Two instruments. (i) Light traffic: by the campaign's uniform expansion (P0289 proof file) w(c) = eps a/2 + "
               "eps^2 J_f(c) + O(eps^3) with J_f(c) = int_0^1 (1-u) E[f(X_0) f(X_{cu})] du, so (1) fails for small eps iff "
               "J_f rises somewhere; J_f computed exactly from the eigendecomposition and, where ill-conditioned, by expm "
               "quadrature. The earlier attempt P0290-A001 only used reversible X, where every autocovariance is a "
               "nonnegative mixture of decaying exponentials and J_f is automatically monotone; doubly monotone chains "
               "need not be reversible (explicit 3-state example with a circulation: rates 1.2, 0.1 / 0.8, 1.2 / 0.5, 0.8), "
               "and 4-state doubly monotone chains with complex eigenvalues exist (7 of 40 sampled). (ii) Moderate load: "
               "exact mean workload of the MMPP/M/1 queue by the matrix-geometric QBD solution, scanned in c at loads "
               "0.2-0.85 (p0290_qbd_workload.py)."),
    "key_identity": ("J_f(c) = sum_l A_l h(lambda_l c), h(z) = (e^z - 1 - z)/z^2, A_l = ((pi f)^T V)_l (V^{-1} f)_l; "
                     "E[workload] = E[N] for exponential unit service; R solves A0 + R A1 + R^2 A2 = 0."),
    "result": ("NEGATIVE SEARCH, no counterexample: on 140 random doubly monotone non-reversible generators (3, 4, 5 states) "
               "times every Boolean f and 30 random nonnegative f, and in a 20-restart hill-climb inside the doubly monotone "
               "cone, J_f never rises (the one apparent rise was an eigen-decomposition artefact at eigenvalues -221/-64 "
               "and disappears under direct quadrature: J = 0.49932, 0.49928, 0.49924, 0.49920, 0.49915 at c = 10, 30, 49, 68, "
               "90). The AUTOCOVARIANCE itself can rise: a 4-state doubly monotone chain with f = 1_{2,3} has "
               "E f(X_0) f(X_t) = 0.060015 at t = 0.90 and 0.061145 at t = 10 (expm-verified), so the Codex observation that "
               "f(X) can violate (2) extends to a non-monotone autocovariance, yet the (1-u)-weighted second-order workload "
               "coefficient stays monotone. Exact QBD workload on the 3-state hand example is monotone in c for five Boolean f "
               "at loads 0.2, 0.5, 0.8; the random-chain QBD scan found no rise in the part completed before its time limit "
               "(a smaller rerun is in p0290_qbd_random.out). Contrast: the star chains of P0291 show that NON-monotone "
               "intensities can satisfy (1); Problem 2 asks the converse direction (monotone hidden chain, non-monotone image)."),
    "result_status": "attempted_unsolved",
    "obstruction": ("If Problem 2 is true it needs a proof that goes beyond the supermodular order (which f(X) violates); the "
                    "light-traffic coefficient's monotonicity for all f on doubly monotone chains is itself an unproved "
                    "empirical regularity here (R_f can rise but J_f did not in any case tried). If it is false, the "
                    "counterexample is not at light traffic and not among small random doubly monotone chains at moderate "
                    "load; a targeted construction (large circulation, service distribution other than exponential/deterministic) "
                    "is the next thing to try."),
    "independent_check": "",
    "artifact": MEMO,
}
with (HERE / "attempts.jsonl").open("a", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
print("appended P0290-A002 (cross-ledger)")
