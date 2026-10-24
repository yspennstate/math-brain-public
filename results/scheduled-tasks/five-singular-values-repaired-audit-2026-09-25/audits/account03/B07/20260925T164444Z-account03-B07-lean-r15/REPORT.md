# account03/B07 Lean verification run 20260925T164444Z-account03-B07-lean-r15

Exact target: math-open-problems commit 4e530247ec0ef4101a6e5ecf621bd35a969c42aa,
repaired source blob 98e45d53d106db9a205051a4dd4917fc39dc2e3a.

Fresh coordination: Lemma 2.6 is already compiled in FiveS2Schur.lean and Lemma 2.7(a,b)
are already compiled in FiveS2Minors.lean / FiveS2Gram.lean. The next uncovered
finite-linear-algebra dependency remains the exact bridge from the compiled ApproxGE proxy in
FiveS2Weyl.lean to Mathlib's padded LinearMap.singularValues.

New result: the exact equivalence is needed only on ambient-live indices
1 <= j <= card(domain), and it remains valid there even when s_j=0 from rank deficiency.
Only j > card(domain) needs separate padded handling: singularValues(j-1)=0 and
ApproxGE j sigma A implies sigma<=0 by choosing R=A. The reverse padded equivalence must not be
stated without a nontrivial-domain hypothesis because ApproxGE requires a nonzero witness.

Thus the paper's exact three Lemma 2.5 inequalities can be completed by an ambient-index case
split, using the live bridge together with the already compiled approx_perturb_symm,
approx_rank_perturb, and approx_of_compress.

Pinned Mathlib 5e932f97 was inspected directly and supplies the required singular-value support,
rank, toEuclideanLin and toLpLin APIs. An independent EYM formalization was inspected only as a
blueprint, not as target evidence.

Status: UNCOMPILED WIP. This runtime has no lean/lake; no installation or remote workflow was
attempted. No compile or #print axioms credit is claimed. No sorry/admit/new axiom was inserted
into executable proof code. Execution remains WITHOUT_VERIFIED_BRAIN; unexposed settings UNKNOWN.
