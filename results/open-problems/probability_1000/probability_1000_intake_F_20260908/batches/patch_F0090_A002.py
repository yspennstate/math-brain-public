"""2026-09-10: second attempt on F0090 (Kalai, Three puzzles, Conjecture 8; = GPS 2010 open problem 1).
Appends attempt row F0090-A002 to attempts.jsonl and sets result_status of F0090 to candidate_full_solution
in problems.jsonl (every other line byte-identical). Written by claude-prob1000-0910. Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
MEMO = ("~/<private-repo>/06_math_research/prob1000_lean_20260908/"
        "REPORT_F0090_Kalai_conjecture_8_entropy_influence_percolation_2026-09-10.md")

row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "F0090-A002",
    "problem_id": "F0090",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": ("Hierarchical (quadtree) coding bound on the entropy of a random subset of the square: "
               "H(A) <= 1 + 4 sum_{k>=1} E|A_{2^k}| + C_0 E|A_1|, where A_r is the set of dyadic r-squares hit by A "
               "(Shannon source coding for a uniquely decodable code). Applied to A = spectral sample S and A = "
               "pivotal set P of the crossing event f_R. One-scale sum bounded by the GPS Lemma 3.2 box estimate "
               "P[S cap B != 0] <= 4 alpha_box(B,Q) (and P[P cap B != 0] <= alpha_box(B,Q)), the boundary handled by "
               "alpha_box(B,Q) <= C alpha_4(r,d) (d/D)^2 (four arms in the disc of radius d/2, three half-plane arms "
               "from 2d to D/2, independent), giving E|A_r| <= C (R/r)^2 alpha_4(r,R) + C. Sum over dyadic r "
               "converges by quasi-multiplicativity and GPS (2.6), alpha_4(r,R) >= C^{-1}(r/R)^{2-eps}, to "
               "C R^2 alpha_4(1,R) <= C' I(f_R)."),
    "key_identity": ("P[S cap B != emptyset] = E[Var(f | bits outside B)] <= P[Lambda_B] = alpha_box(B,Q) "
                     "(GPS Lemma 3.2 (3.4)); H(A) <= E[code length] = 1 + 4 sum_k E|A_{2^k}| + C_0 E|A_1|; "
                     "sum_{r=2^k} (R/r)^2 alpha_4(r,R) <= C R^2 alpha_4(1,R) sum_k 2^{-eps k}."),
    "result": ("Both inequalities of Conjecture 8 hold for the crossing event of the square, on Z^2 and on the "
               "triangular lattice: H(S(f_R)) <= C I(f_R) and H(P(f_R)) <= C I(f_R), i.e. Ent(f_R) = O(R^2 alpha_4(R)), "
               "which is also GPS 2010 open problem 1. The obstruction named in F0090-A001 (whether GPS prove a "
               "spectral-sample box estimate) is removed: the box estimate is GPS Lemma 3.2 (3.4), one line from the "
               "conditional-variance identity, and needs no second-moment input. Inputs used: GPS Lemma 3.2, "
               "quasi-multiplicativity, GPS (2.6) lower bound (Reimer + 5-arm + RSW), the half-plane three-arm bound "
               "alpha_3^+(r,R) <= C (r/R)^2 (the two-arm bound alpha_2^+ <= C r/R also suffices), and E|P| >= c R^2 "
               "alpha_4(1,R). General principle: the entropy-influence inequality holds for every Boolean function on "
               "a planar array whose spectral sample satisfies sum_{k>=1} E|S_{2^k}| = O(E|S|)."),
    "result_status": "candidate_full_solution",
    "obstruction": ("None mathematical. Remaining: (a) independent referee of the memo; (b) prior-art citation check "
                    "(papers citing GPS 2010 / Kalai 2018 for 'spectral entropy'): the FEI literature to June 2026 "
                    "(1105.2651, 1110.4301, 1304.1347, 1806.03646, 2312.08271, 2606.00246) has no percolation case and "
                    "the 2024 Combinatorica bound gives only O(I log R) here; (c) general quads checked only in outline."),
    "independent_check": "",
    "artifact": MEMO,
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
    if r.get("problem_id") == "F0090":
        r["result_status"] = "candidate_full_solution"
        r["status_search"] = (r.get("status_search", "") + " UPDATE 2026-09-10: same question is GPS 2010 (arXiv:0803.3750) "
                              "Section 11 open problem 1 ('is Ent(f_R) = O(R^2 alpha_4(R))?'). Attempt F0090-A002 gives a "
                              "full argument (author-checked, unrefereed); see " + MEMO)
        out.append(json.dumps(r, ensure_ascii=False, sort_keys=True)); n += 1
    else:
        out.append(line)
pp.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("appended attempt; patched problem rows:", n)
