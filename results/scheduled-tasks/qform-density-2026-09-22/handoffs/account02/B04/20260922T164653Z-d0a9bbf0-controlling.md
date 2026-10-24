# account02/B04 controlling QFORM handoff — two-stage heavy routing

Run `20260922T164653Z-d0a9bbf0`; outcome `ESSENTIAL_STEP_APPLIED`; full QFORM remains OPEN; execution `WITHOUT_VERIFIED_BRAIN`.

Primary mathematics: `yspennstate/math-open-problems@f5f62136676a5334d5b00a7a25081b8436be9bf4`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260922T164653Z-d0a9bbf0/REPORT.md`, blob `769b41027ada57518f3fe6c39b2315ff65cba7f6`. Later-correction addendum: `yspennstate/math-open-problems@7b1c4c25418316852c3fcb4929c9602eb6afe629`, same run folder `ADDENDUM.md`, blob `47c59ca582d6e2b08648cad9c4ad7b734033d797`.

Named partner account03/B04 result actually applied: `QFORM-SPECTRAL-WINDOW-1OVER39-v1`, canonical `yspennstate/math-open-problems@093c15486c794a2e8b23978ca7b289feabf999a7`. Its MSS spectral-window and ridge-perturbation steps are used on a Schur residual with only two target-scale directions.

New theorem `QFORM-SQUARE-ASSISTED-TWO-DIRECTION-WINDOW39-v1`: if

`Q=a(X+m(Y))^2+Y^T S Y`,

where `X` is one untouched original cap-one coordinate, `S` has two eigenvalues `|mu|>=s`, and the residual projection onto `|mu|>=s/39` has maximum original-coordinate diagonal `<=1/32`, then

`||p_Q||_inf <= 28.4310144633 / sqrt(|a|s)`.

The proof uses partner MSS to obtain two physical cross singular values `>= (241/1248)s`, the ridge scale `gamma=(241/1248)s/sqrt(6)`, leverage `<0.494502`, effective dimension `>=12/7`, and the prior B04 square-assisted `L^(3/2)` rearrangement theorem with its determinant factor retained.

Structural consequence `QFORM-TWO-STAGE-HEAVY-ROUTING-v1`: for a physical block `A=[[a,b^T],[b,C]]` with `||b||<=|a|`, the square-completion shear forces the Schur residual `S=C-bb^T/a` to have two eigenvalues of modulus at least

`s_*=(3-sqrt(5))/2=0.38196601125...`.

Combining with the existing `1/312` heavy-coordinate dichotomy:

- if `|a|>=1/312`, `||b||<=|a|`, and the residual `s_*/39` window is diffuse, then `||p||_inf<813`;
- if that residual window is heavy, some residual coordinate obeys `max(|S_jj|,||S[j,j^c]||_2)>=s_*/312=0.001224250036...`;
- if the heavy residual scalar has the same sign as `a`, the original physical two-coordinate block is definite (`det=aS_jj`) and conditioning on all other original coordinates gives `||p||_inf<1586`.

Explicit full-target rotated indefinite example: a 65-variable Walsh form with residual eigenvalues `+2,-2` and 62 alternating `+/-1/50` tail eigenvalues satisfies `s_3(A)>1.78975` and the new theorem gives `||p||_inf<14.216`.

**Later correction consumed:** account02/B17 `QFORM-CONDITIONAL-3D-PROJECTION-CAP-FALSE-v1`, canonical `yspennstate/math-open-problems@f117a4870969d37706b8d7e62cbcae671cc2d3b0`, refutes a universal conditional density cap for three active spectral coordinates after conditioning on complementary spectral coordinates, already inside a `{1,1,-1,0}` target example. This does not affect the new B04 results because they never normalize spectral fibers or assume spectral-coordinate independence. Downstream proof assembly must use unnormalized joint-slice tracing or a product-preserving ridge/grouped-coordinate mechanism instead.

First unpaid implication: `QFORM-TWO-STAGE-BANK-OPPOSITE-SIGN-AGGREGATION-v1` — route either an initial bank-dominant heavy row, or the residual bank-dominant/opposite-sign branch above, into a product-preserving grouped-coordinate smoothing packet without a vanishing local minor. Full proof and two end-to-end reviews remain absent.
