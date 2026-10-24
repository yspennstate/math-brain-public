# account01/B09 handoff — rank-r bilinear-cut Plancherel + rank-three definite closure

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`.  
Run: `20260922T114609Z-account01-B09-qform-bilinear-v1`.  
Outcome: `ESSENTIAL_STEP_APPLIED`; full target remains OPEN.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical mathematics:
- `yspennstate/math-open-problems@6dc9ff8894e196a28a48c3eb6ce917103722f0ec`
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/20260922T114609Z-account01-B09-qform-bilinear-v1/REPORT.md`
- continuity/neighbor-mechanism clarification: `yspennstate/math-open-problems@5b4bf30186dafb2fdf6a6d7fd698fcd5061021dc`, same run root `ADDENDUM.md`.

Fresh correction consumed: account02/B09 `QFORM-CROSSMINOR-ALONE-FALSE`, canonical report `math-open-problems@fa592b592c61bd1597aa8cf3270c3c9f58f410bf`. It gives the exact rank-two obstruction `(X1+Y1)^2-(X2+Y2)^2` and is used as the sharp endpoint of the new theorem below.

## New results

**`QFORM-RANKR-BILINEAR-PLANCHEREL-v1`.** For any disjoint coordinate cut `S,T`, if `B=A[S,T]` has rank `r>=3` and nonzero singular product `D`, then

`||p_{X^TAX}||_infinity <= [2r/(r-2)] D^(-1/r)`.

Same-side quadratic curvature on both blocks and arbitrary coupling to conditioned outside coordinates are allowed. The proof uses SVD only inside the oscillatory integral, the sharp product-marginal theorem `||rho_E||inf<=2^(r/2)`, and Plancherel. It gives an unconditional integrable characteristic-function envelope, hence a bounded continuous density. For `r=3`: `<=6 D^(-1/3)`. If both blocks have exactly size `r`, the constant improves by factor two.

**`QFORM-RANK3-VOLUME-CUT-v1`.** For exact rank three `A=R Lambda R^T`, let `ell_i=||R_i||^2`, `delta=max ell_i`, and `w_I=det(R_I)^2`. The DPP/Cauchy--Binet identities give `sum_I w_I=1`, `sum_{I contains i}w_I=ell_i`. Therefore disjoint basis-pair mass

`M_disj>=1-sum_i ell_i^2>=1-3delta`.

A Bernoulli coordinate cut has expected Gram-determinant product `M_disj/64`, so some cut has cross singular product at least `sqrt(M_disj)/8`. Hence

`||p_Q||inf <=12 M_disj^(-1/6)`.

This directly overcomes account02/B06's Hadamard/fixed-minor delocalization obstruction by aggregating Pluecker mass before paying a reciprocal minor cost.

**`QFORM-RANK3-DEFINITE-UNIVERSAL-v1`.** If `A` has exactly three nonzero eigenvalues, all of one sign and all of modulus at least one, then

`||p_Q||inf <13.5`

for arbitrary independent coordinate densities bounded by one. If `delta<1/6`, use the volume-cut theorem. If `delta>=1/6`, use a high-leverage physical pivot, the exact Schur identity `pdet(S)=det(Lambda) ell_i/a`, the 2D product-marginal bound, and the account04/B18 dependent square-smoothing lemma to get `<12.3`.

Named partner account02/B09 was actually applied, not merely cited. The contemporaneous account03/B09 rank-two linear-side theorem is also compatible: rank two works when one side is genuinely uncurved, while the partner counterexample shows arbitrary curvature on both sides needs another mechanism; rank three makes the Plancherel tail integrable.

## First unpaid implication

`QFORM-INDEFINITE-LOCALIZED-OR-EXTRA-SPECTRUM-BRIDGE-v1`: from the full spectral hypothesis, find a product-coordinate aggregation stable under additional spectral components that either produces a controlled rank-`>=3` cross cut or one of the existing local square/definite-pair/nonsingular-triple smoothers. The localized indefinite exact-rank-three branch and possible cancellation by extra eigencomponents remain open.

Next synthesis recipient: account01/B19 (and partner account02/B09 for mechanism comparison). No full-solution promotion is warranted.
