"""2026-09-11: third attempt on E0064 (Rozikov Problem 11, Theorem 6 for m >= 4): the uniqueness clause fails for
m >= 5 (explicit rational two-fixed-point operator on 5 types; two-face construction for m >= 6); m = 4 uniqueness
numerically supported. Appends E0064-A003 to attempts.jsonl and sets the row's result_status to
candidate_partial_counterexample. Written by claude-prob1000-0910. Run once."""
import json
from pathlib import Path
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent.parent
MEMO = ("~/<private-repo>/06_math_research/prob1000_lean_20260908/"
        "REPORT_E0064_strictly_nonVolterra_fixed_point_uniqueness_fails_for_five_types_2026-09-11.md")
row = {
    "schema": "probability-attempt.v1",
    "attempt_id": "E0064-A003",
    "problem_id": "E0064",
    "author": "claude-prob1000-0910",
    "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "substantive": True,
    "method": ("Uniqueness clause of Theorem 6 in m >= 4. (i) Random search: 400 four-type, 150 five-type strictly "
               "non-Volterra operators (Dirichlet entries), fixed points by Newton from 120-150 starts: always exactly one. "
               "(ii) Structure: an invariant 3-face carries the unique fixed point of its 3-type restriction (Theorem 6 "
               "itself); two invariant triples must be disjoint (a shared pair would have to land in two third types), so "
               "m >= 6 admits two invariant faces and hence two fixed points; m = 4 admits at most one and a face-invariant "
               "4-type operator has V_4 == 0, so all its fixed points lie in the face; m = 5 admits one invariant face and a "
               "possible interior second point. (iii) Explicit m = 5 example found by the symmetric ansatz and verified in "
               "exact rational arithmetic."),
    "key_identity": ("m=5: face {1,2,3} symmetric (P_ii,k = 1/2, P_ij,third = 1); P_i4,5 = P_i5,4 = 1 (i <= 3), P_44,5 = "
                     "P_55,4 = 1, P_45,k = 1/3 (k <= 3). Fixed points p = (1/3,1/3,1/3,0,0) and q = (1/9,1/9,1/9,1/3,1/3): "
                     "V_k(q) = (1/81+1/81)/2 + 2/81 + (2/3)(1/9) = 1/9; V_4(q) = 2(1/3)(1/3) + 1/9 = 1/3."),
    "result": ("The uniqueness clause of Theorem 6 is FALSE for every m >= 5: the explicit 5-type operator above has two "
               "fixed points (both exact; tangent Jacobian eigenvalues (-2,-1,-1,2) at p, index -1, and (-4/3,-1/3,-1/3,0) "
               "at q, index +1; neither attractive), and for m >= 6 any operator with two disjoint invariant triples has two "
               "fixed points by Theorem 6 applied to each face (numerically 2 or 3 in 30/30 random such operators). "
               "Together with E0064-A002 (non-attractiveness fails from m = 4), Theorem 6 does not extend to m >= 4. "
               "At m = 4 uniqueness is UNRESOLVED and numerically supported: 700 operators including sparse (Dirichlet 0.1) "
               "and face-invariant ones all had exactly one fixed point (e0064_fixed_point_search.py, "
               "e0064_face_construction.py, e0064_m5_exact.out)."),
    "result_status": "candidate_partial_counterexample",
    "obstruction": ("m = 4 uniqueness: an index count would work if every fixed point had index +1, but the 5-type example "
                    "shows a saddle of index -1 can occur, so a proof must use the dimension; not attempted. The cycle clause "
                    "(2) of Theorem 6 in higher dimension is untouched. Prior art beyond the source and Jamilov-Ladra-"
                    "Mukhitdinov 2017 not searched."),
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
    if r.get("problem_id") == "E0064":
        r["result_status"] = "candidate_partial_counterexample"
        r["status_search"] = (r.get("status_search", "") + " UPDATE 2026-09-11: uniqueness clause refuted for m >= 5 "
                              "(E0064-A003, explicit 5-type example, exact); m = 4 open, numerically unique; see " + MEMO)
        out.append(json.dumps(r, ensure_ascii=False, sort_keys=True)); n += 1
    else:
        out.append(line)
pp.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("appended E0064-A003; patched problem rows:", n)
