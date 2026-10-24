"""2026-09-10, same session, self-correction: G0008-A001 claimed monotonicity of n -> P_p(0 <-> (0,n)) for ALL n
when p is small, by a ratio argument that only controls the series in the path length, not the dependence on n.
That claim is withdrawn; the large-n statement (Ornstein-Zernike) stands. Appends G0008-A002 only. Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "G0008-A002",
    "problem_id": "G0008",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": "Re-audit of G0008-A001 before reporting.",
    "key_identity": "",
    "result": ("CORRECTION. The small-p claim of A001 ('monotonicity holds for all n when p is below some p_0') is "
               "withdrawn: the crude bounds p^n <= P_p(0 <-> (0,n)) <= sum_{k>=n} mu^k p^k give P_p(0<->(0,n+1)) <= "
               "(mu p)^{n+1}/(1 - mu p), which is NOT below p^n once mu^{n+1} p > 1 - mu p, i.e. for all large n at any "
               "fixed p (mu = 2.64.. is the connective constant); the low-order expansion P = p^n (1 + a_n p^2 + ...) "
               "has coefficients a_n growing with n, so uniformity in n is exactly what is missing. What stands: for "
               "every fixed p < p_c, P_p(0 <-> x) = C(p, x/|x|) |x|^{-1/2} e^{-|x|/xi_p(x/|x|)} (1 + o(1)) (Campanino-Ioffe "
               "2002, Ornstein-Zernike for Bernoulli percolation), so the axis two-point function is eventually "
               "decreasing; for p > p_c the same holds for the truncated function in d = 2 (Campanino-Ioffe-Louidor "
               "2010). So the partial result is: eventual monotonicity at every p != p_c; nothing at p_c; nothing for "
               "small n."),
    "result_status": "partial_result",
    "obstruction": "As in A001, minus the withdrawn claim.",
    "independent_check": "",
}
# annotate A001 in place as well, so a sampled excerpt carries its own correction
ap = HERE / "attempts.jsonl"
out, n = [], 0
for line in ap.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    r = json.loads(line)
    if r.get("attempt_id") == "G0008-A001":
        r["corrected_by"] = ("G0008-A002 (same day): the 'all n for small p' claim is withdrawn; only the "
                             "large-n Ornstein-Zernike statement stands.")
        out.append(json.dumps(r, ensure_ascii=False, sort_keys=True)); n += 1
    else:
        out.append(line)
out.append(json.dumps(row, ensure_ascii=False, sort_keys=True))
ap.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("annotated A001 rows:", n, "; appended G0008-A002")
