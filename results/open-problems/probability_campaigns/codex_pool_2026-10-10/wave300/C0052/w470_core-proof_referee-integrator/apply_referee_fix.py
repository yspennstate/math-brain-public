"""Apply w473's exact-joint-law correction to this worker's claim row."""

import json
from pathlib import Path

path = Path(__file__).resolve().parent / "CLAIMS.jsonl"
rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
found = False
for row in rows:
    if row.get("id") == "C0052-reduction-03":
        row["statement"] = (
            "For beta<beta_c, let B={y:||y||_infinity<=floor(xi)} and draw "
            "(X,Y,Z) with joint mass P(X=x,Y=y,Z=z)=G(x)G(z-y)/(|B|chi^2) "
            "for y in B. Thus X is independent of (Y,Z). Let q_beta be the expected "
            "probability that two independent currents with respective source pairs "
            "(0,X) and (Y,Z) connect all four marked vertices in their union. "
            "Then -g(beta)>=2|B|q_beta/xi^3. If xi->infinity and liminf q_beta>0, "
            "C0052 follows in the source's coupling sense."
        )
        row["assumptions"] = (
            "The stated full joint endpoint mass; subcritical infinite-volume current identity "
            "of Exercise 61(1) and convergence of its finite-volume version; nearest-neighbor "
            "zero-field Ising on Z^3; xi>0, chi<infinity."
        )
        row["independent_reviewer"] = "w473: FIX exact joint law; corrected in ATTEMPT.md"
        row["remaining_gap"] = (
            "Prove a scale-uniform lower bound for q_beta and justify the assumed infinite-volume "
            "passage. Parent problem remains unsolved."
        )
        row["verdict"] = "FIX applied to endpoint law; conditional algebra KEEP"
        found = True
assert found
if not any(row.get("id") == "C0052-endpoint-tree-05" for row in rows):
    rows.append({
        "id": "C0052-endpoint-tree-05",
        "statement": "On degree-three ferromagnetic trees T_{H,m} formed by a depth-H binary bush and length-m handle at equal edge parameter log 3, sample endpoint X with law G(o,x)/chi and one current with sources o triangle X. Its bare hit probability k(v) at the handle tip satisfies k(v)/G(o,v)->0 along H=m^2 as m->infinity. Hence no graph-uniform positive linear lower bound k>=c G follows merely from endpoint averaging; this says nothing against a Z^3-specific bound.",
        "assumptions": "Finite zero-field free-boundary Ising trees, maximum degree three, all edge parameters log 3; current parity factorization on trees; X weighted by G/chi.",
        "source": "owner-own-work: ~/brain_workers/w470/ENDPOINT_TREE_OBSTRUCTION.md; current identity background Aizenman arXiv:2112.04248v2 (5.9)",
        "proof_or_counterexample": "Tree spin correlation gives tau=4/5 per edge; an even current edge is present with rho=2/5. With S_H=sum_h(2tau)^h and T_m=sum_j tau^j, exact k(v)=[S_H rho^m+sum_j tau^j rho^(m-j)]/[S_H+T_m]. For H=m^2, k(v)/tau^m <=2^(-m)+4(5/8)^(m^2)(5/4)^m ->0.",
        "independent_reviewer": "w473 requested, pending",
        "remaining_gap": "Independent referee check; no implication for the homogeneous critical Z^3 model or C0052.",
        "status": "proved special case",
        "verdict": "author proof, pending independent referee"
    })
path.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
print("updated C0052-reduction-03 after w473 FIX and saved endpoint-tree claim")
