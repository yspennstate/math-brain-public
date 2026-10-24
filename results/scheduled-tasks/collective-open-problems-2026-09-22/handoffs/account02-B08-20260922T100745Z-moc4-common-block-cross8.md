# account02/B08 MOC4 handoff — common-block external reduction

Source run: `B08-20260922T100745Z-81e721`  
Canonical report: `yspennstate/math-open-problems` / `proofnet24/collective-MOC4/account02/B08/B08-20260922T100745Z-81e721/REPORT.md`  
Report Git blob: `b77c219367bb3369e55a43d21b20361e7365a2a2`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains OPEN.

## Exact boundary reduction

Let `f(sigma)=L(prod_i(a_i+b_{sigma(i)}))`, `M=max f` and use account03/B09's exact Saxl external bound
`h_L(U)<=max(M,max e_{tau,rho'}(f))` for true unitaries.

For a **full-support exposed 1+3 common-block face**, the block determinant is a strictly positive convex combination of all six block-preserving permutation vertices. Hence all six have support M. Exact rational identities on the 53 standard Saxl_4 generators express **all 48 external functionals** as nonnegative combinations of off-face evaluations modulo face evaluations. Therefore every external value is <=M. If every off-face endpoint is strictly below M, all 48 external values are strictly below M and there is an open spectral/support collar.

For a **full-support exposed 2+2 common-block face**, the same argument pays **40 of 48** external functionals. The only eight not covered are

`((2,3,0,1),(1,2,0))`, `((2,3,0,1),(2,0,1))`,
`((2,3,1,0),(1,0,2))`, `((2,3,1,0),(2,1,0))`,
`((3,2,0,1),(1,0,2))`, `((3,2,0,1),(2,1,0))`,
`((3,2,1,0),(1,2,0))`, `((3,2,1,0),(2,0,1))`.

Their `tau` values are exactly the four permutations swapping the two 2-element blocks. Thus a generic 2+2 boundary approach can only fail through these eight cross-block antipodal Saxl atoms (or lower-support/off-face-tie degeneracies).

The newest named-partner report account03/B09 `20260922T094506Z-account03-B09-MOC4-r12`, `MOC4-B09-TWO-KNOT-CROSS-BLOSSOM-v1`, has unique dangerous atom `((2,3,0,1),(1,2,0))`, exactly one of the eight above, and pays it on a nontrivial support chamber by a genuine complementary-minor cofactor/blossom certificate.

## Next boundary implication

`MOC4-COMMON-BLOCK-CROSS8-PAYMENT-v1`: symbolically pay the eight cross-block-swap external functionals using genuine spinor/cofactor compatibility, or construct a true-unitary support violation. Do not treat external Saxl excess alone as a counterexample.

Exact verification files beside the source report:
- `CHECK.py` Git blob `2a880eba70ba962d9bdcbe2d5eaa8f5c7bbe65c2` — 40/48 for 2+2, residual eight classified exactly;
- `CHECK_13.py` Git blob `4955aa4be606e78a53c39bafebc3e300c6c9ec7f` — 48/48 for 1+3.

Both checkers use standard-library `Fraction` arithmetic and verify identities on all 53 Saxl_4 subset generators. No arbitrary bistochastic surrogate is used.
