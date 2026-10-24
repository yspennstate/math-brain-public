# B09 addendum — consume latest B20 nested-cut reduction

After the main B09 report was committed, account03/B20 completed `QFORM-NESTED-CUT-THREE-RESOURCE-v1` at `yspennstate/math-open-problems@06ef7346c08f41c3fac240e1acdeb1b42dc2995d`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T165009Z-account03-B20-QFORM-r13/REPORT.md`.

In the current unresolved target branch, B20 proves a product-preserving original-coordinate cut with one of three quantitative resources:

1. `s_2(C)>=3/160` in one cross bank;
2. `s_1(C)>9/160` plus a physical square pivot on one side with `|A_ii|>=157/320`;
3. `s_1(C)>9/160` plus a nested same-side physical cross bank with `s_1>157/640`.

This is source-compatible with the B09 theorem. It changes the first unpaid implication from an abstract low-stable-rank extraction to the more concrete **`QFORM-NESTED-BANK-ANALYTIC-PAYMENT-v1`** already named by B20.

B09 now pays a precise subbranch of alternatives 2--3: whenever the physical pivot/nested-bank structure reduces, after the genuine scalar Schur completion, to a nondegenerate grouped rank-two quotient

`S_PP=alpha uu^T`, `S_TT=gamma vv^T`, `S_PT=beta uv^T`,
`S_PW=u r^T`, `S_TW=v s^T`,

with arbitrary `S_WW`, the main report gives

`||p_Q||_infinity <= sqrt(2) C_* |a|^(-1/2) Delta_grp^(-1/4)`,

`Delta_grp=|alpha gamma-beta^2| ||u||^2 ||v||^2`.

For the isolated hyperbolic subcase the sharper bound is `8/sqrt(|a| sigma)`. Thus the remaining B20 payment problem is specifically the **arbitrary-self-block** case: preserve the outer/nested bilinear resources while the same physical banks also carry unrestricted quadratic curvature. The account02/B09 same-square counterexample shows that this curvature cannot simply be absorbed into the pivot square.

No full-solution claim is made. The full conjecture remains OPEN; continuity also remains unproved on the new B09 branch.
