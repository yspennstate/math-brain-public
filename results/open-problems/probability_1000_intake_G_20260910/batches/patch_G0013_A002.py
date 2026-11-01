"""2026-09-10: second attempt on G0013 (Catalano-Lavenant conjecture) - convexity reduction and an exhaustive
discrete check. Appends G0013-A002; sets G0013 result_status to partial_result. Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "G0013-A002",
    "problem_id": "G0013",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": ("(1) Convexity: pi -> W_2^2(pi, lambda (x) lambda) is convex and weakly continuous on the convex weakly "
               "compact set Pi(lambda, lambda), so by Bauer's maximum principle the supremum is attained at an EXTREME "
               "doubly stochastic measure. Deterministic couplings (id, T)_# lambda with T measure-preserving are "
               "extreme, but for nonatomic marginals not every extreme point is of that form (Lindenstrauss 1965, "
               "Losert's example), so this reduces the conjecture to extreme couplings, not all the way to maps. "
               "(2) Discretisation: marginals uniform on n equally spaced atoms, couplings = doubly stochastic "
               "matrices / n; there every extreme point IS a permutation (Birkhoff), so the discrete conjecture is "
               "'the identity and the reversal maximise W_2^2(pi_sigma, U_n (x) U_n) over permutations sigma', with "
               "each value a transportation LP (n^2 grid points to n atoms). Exhaustive search "
               "(prob1000_lean_20260908/g0013_permutation_search.py, scipy HiGHS)."),
    "key_identity": "W_2^2(., nu) convex => max over Pi(lambda,lambda) at an extreme point; Birkhoff in the discrete case",
    "result": ("MEASURED (exact LP values): for n = 3, 4, 5, 6, 7 (6, 24, 120, 720, 5040 permutations) the maximum is "
               "attained EXACTLY by the identity and the reversal and by nothing else; maxima 0.098765, 0.109375, "
               "0.102400, 0.103395, 0.101624; runner-ups are the identity or reversal with one adjacent transposition "
               "at an end (e.g. n=7: 0.096626 vs 0.101624). The discrete conjecture holds for n <= 7. The values "
               "hover near 0.10; for the continuous diagonal coupling the analogous quantity should be the limit."),
    "result_status": "partial_result",
    "obstruction": ("The continuous statement needs either (a) the extreme-point reduction pushed to maps, or (b) a "
                    "direct proof for the discrete permutation problem uniform in n plus a Gamma-convergence/"
                    "approximation step. For (b), the runner-up pattern suggests an exchange argument: uncrossing "
                    "two atoms of a non-monotone permutation should increase the transport cost to the product law; "
                    "not proved."),
    "independent_check": "",
}
ap = HERE / "attempts.jsonl"
with ap.open("a", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
pp = HERE / "problems.jsonl"
out, n = [], 0
for line in pp.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    r = json.loads(line)
    if r.get("problem_id") == "G0013":
        r["result_status"] = "partial_result"; n += 1
        out.append(json.dumps(r, ensure_ascii=False, sort_keys=True))
    else:
        out.append(line)
pp.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("appended G0013-A002; patched", n)
