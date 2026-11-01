"""2026-09-10: cross-ledger attempt row for P0291 (Codex tree, Leskela Problem 3), appended to the intake G
attempts.jsonl so that ledger scans find the result; problems.jsonl untouched (P0291 is not a G row). The Codex
tree itself is not edited (its owner was asked on the mesh to update the row). Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
MEMO = ("~/<private-repo>/06_math_research/prob1000_lean_20260908/"
        "REPORT_P0291_Leskela_problem_3_nonmonotone_chain_with_supermodular_time_ordering_2026-09-10.md")
row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "P0291-A002",
    "problem_id": "P0291",
    "cross_ledger": "Codex tree Downloads/Probability_1000_20h_20260906 (row P0291, Leskela 2022 Problem 3 journal / Problem 2 arXiv)",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": ("Candidate: symmetric 3-state star (1->2 and 1->3 at rate a, 2->1 and 3->1 at rate b); not monotone since "
               "P_t(1,{3}) = at + O(t^2) > P_t(2,{3}) = O(t^2). Proof of the supermodular time ordering (2): reduce to "
               "monotonicity in each gap; for a reversible 3-state chain E phi as a function of one gap is "
               "C + alpha e^{-bg} + beta e^{-(2a+b)g}, so gap-monotonicity <=> (C1) Phi22+Phi33 >= Phi23+Phi32 and "
               "(C2) 2Phi11+Phi22+Phi33 >= Phi12+Phi13+Phi21+Phi31 for the two-point conditional Phi; leaf labels are "
               "exchangeable fair coins per excursion; (C1) by block comonotonicity; (C2) via the order-preserving "
               "coupling of the centre-started and leaf-started skeletons (fair coin on the overlap excursion) reduces "
               "to S(psi) >= 0 for supermodular psi on {1,2,3}^4, which is an exact nonnegative combination of 11 "
               "elementary increasing-difference inequalities (rational-verified)."),
    "key_identity": ("F(g) = C + alpha e^{-bg} + beta e^{-(2a+b)g}; b alpha + (2a+b) beta = b pi_2 [2Phi11 + Phi22 + Phi33 - "
                     "Phi12 - Phi13 - Phi21 - Phi31]; S(psi) = sum of 11 weighted elementary supermodular inequalities."),
    "result": ("YES: a stationary ergodic CTMC on three ordered values that is not stochastically monotone but satisfies "
               "c1 <= c2 => lambda_{c1} >=_sm lambda_{c2}, for every a, b > 0 (and by Bauerle-Rolski a non-monotone "
               "environment obeying Ross's monotonicity (1)). Smallest possible state space (two-state chains are "
               "monotone). Controls: exact LP dual test of >=_sm on {1,2,3}^n passes for n = 3,4,5 and rate pairs "
               "(1,1),(1,3),(3,1),(1,4); the clockwise 3-cycle control fails; the birth-death control passes; (C1),(C2) "
               "computed directly from conditional expectations have minima 0 to 1e-15. Boundary (measured): the "
               "asymmetric star with return rates b2 < b3 fails (2); b2 > b3 and a2 != a3 pass."),
    "result_status": "candidate_full_solution",
    "obstruction": ("None mathematical. Owed: independent referee of the spectral step and of the coupling's marginal "
                    "correctness; citation search on Leskela 2022 / Bauerle-Rolski 1998 for a prior 3-state example; "
                    "the Codex ledger row should be updated by its owner."),
    "independent_check": "",
    "artifact": MEMO,
}
with (HERE / "attempts.jsonl").open("a", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
print("appended P0291-A002 (cross-ledger)")
