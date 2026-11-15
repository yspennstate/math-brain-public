# FEIB27 final results

| Allowed terms | Local C, approximately | Summed C, approximately | Status beyond the census |
| --- | ---: | ---: | --- |
| Inf | 9.428632 | 3.606847 | local bound disproved; summed bound open |
| singleton + B | 9.428632 | 3.606847 | local bound disproved; summed bound open |
| M + B | 9.465607 | 4.028236 | local bound disproved; summed bound open |
| noise(0.95) + B | 9.465607 | 3.999338 | local bound disproved; summed bound open |
| degree cap 2 + B | 9.465607 | 4.067699 | local bound disproved; summed bound open |
| all linear terms except Inf | 9.428632 | 3.606847 | local bound disproved; summed bound open |
| B alone | 9.465607 | 4.093796 | local bound disproved; summed bound open |
| M alone | 42.511875 | 10.688295 | both forms disproved |
| degree cap 2 alone | 21.444786 | 5.930623 | both forms disproved |
| noise(0.5) alone | 209715.200000 | 9986.438095 | both forms disproved |
| noise(0.8) alone | 86.651553 | 12.134961 | both forms disproved |
| noise(0.95) alone | 14.063432 | 4.751033 | both forms disproved |
| perspective alone | 32.625678 | 8.598106 | both forms disproved |
| singleton alone; low-level truncation alone, r=1,2,3 | infeasible | infeasible | explicit zero-denominator witnesses |

PROVED. The entire per-coordinate dictionary fails universally by the explicit bent-hiding family. All summed directions using only variance-budget terms fail by balanced tribes. The step-by-step proofs, shared-budget calculation and refined local bound are in PROOFS.md.

CHECKED NUMERICALLY. 33,573,370 function instances, including two million directed proposals and one million provably distinct stress functions, with full restriction closure of the initial finite census as detailed in REPORT.md. 172,593,426 relevant-coordinate instances. Coefficient replay residual at most 5.642e-14.

CHECKED NUMERICALLY / INTERVAL CERTIFIED. Eight candidate potentials do not improve the finite delivered constant over Theta=0: the binding tribes witness has full step 6.0037460565590882514... bits/influence, with all potential-drop budget inequalities certified on every coordinate.

CHECKED NUMERICALLY. The main-census maximum best-coordinate positive-log moment is 1.851658579311; the structured larger stress family raises it to about 1.863061. The candidate bound of two remains open. Half-mass at p<=q is disproved; the strongest scanned counterexample has best mass 0.159481095679.

PROVED by exact integers. Half-mass at p<=4q is false even for a transitive monotone function: the eighteen-variable disjoint-pair tribes function with two complementary transversal clauses has mass 429970409/859963392 at every coordinate. The exact histogram and independent integer Walsh check are in transversal_certificate.json.

OPEN. No surviving universal summed or best-coordinate conjecture is proved; FEI remains open. REPORT.md is the complete report, with evidence and scope limits.
