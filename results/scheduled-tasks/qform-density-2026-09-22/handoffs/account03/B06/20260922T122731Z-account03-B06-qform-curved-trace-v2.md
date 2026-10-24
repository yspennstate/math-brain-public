# account03/B06 handoff — spectral-row Schur smoothing

Programme `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`. Full conjecture remains **OPEN / NOT PROVED**. Execution status: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

Canonical scientific source:

- repository: `yspennstate/math-open-problems`
- commit: `6853fe0b03502a11750096e7a21e650bebb4fe6d`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260922T122731Z-account03-B06-qform-curved-trace-v2/REPORT.md`
- report blob: `171e68e2294c93f1e6ce37d92a20456b60394a5c`

## Result

`QFORM-SPECTRAL-ROW-SCHUR-SMOOTHING-v1` is proved for rank-three forms. Write `A=R Lambda R^T`, `R^T R=I_3`, row leverage `ell_i=||R_{i,*}||^2`, and scalar pivot `a=A_ii`. If `a!=0` and its spectral Schur complement is definite (in inertia `(2,1)` or `(1,2)`, this is exactly a minority-sign pivot), then for arbitrary independent scalar input densities bounded by one,

`||p_{X^TAX}||_infinity <= 2 sqrt(2 pi) / (ell_i |det Lambda| |A_ii|)^(1/4)`.

The proof uses only one original coordinate as a pivot. After completing that square, the residual rank-two Schur form is an exact two-dimensional orthogonal projection of the *remaining independent coordinates*, with frame identity `W^T W=I_2`. Its definite quadratic pushforward has density

`M <= 2 pi sqrt(|A_ii|)/(sqrt(ell_i) sqrt(|det Lambda|))`.

Applying account04/B18's completed `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` gives the displayed bound even though the square translation depends on the residual projection. This is an actual application of a compatible completed account04 result.

The determinant identity behind the curved-fiber payment is exact:

`|det(B_schur)| = ell_i |det Lambda|/|A_ii|`.

## Why it matters

This is not a fixed physical `3 x 3` minor theorem. It aggregates the other two curved directions across all remaining coordinates, so it survives delocalized eigenframes. It also preserves the product provenance that account01/B06 proved cannot be discarded: a generic 3D X-ray cap alone fails on the two-sheet branch.

For three large eigenvalues, writing `eta_i=|A_ii|/ell_i`, a minority-sign row with `ell_i>=kappa` and `eta_i>=tau` costs at most

`2 sqrt(2 pi) kappa^(-1/2) tau^(-1/4)`.

Thus the exact local losses are low leverage and approach to the spectral light cone.

## Dependencies actually consumed

- compatible account04 result: `account04/B18/20260922T113729Z-account04-B18-qform-r1`, dependent square smoothing;
- account01/B16 product-projection theorem: true 2D orthogonal marginal density cap `<=2`;
- account01/B06 correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE`: generic X-ray information is insufficient;
- current correction inbox including `QFORM-CROSSMINOR-ALONE-FALSE` and the pending diffuse rank-three branch.

The exact assigned partner `account04/B06` still had no completed current-QFORM artifact visible at final source refresh; no PASS or result was fabricated.

## Remaining implication

`QFORM-MAJORITY-PIVOT-HYPERBOLIC-RESIDUAL-v1`: for a rank-three indefinite form whose useful high-leverage physical pivots have the majority sign (or lie arbitrarily close to the spectral light cone), control the indefinite residual Schur form while retaining its exact product-projection representation, then spend the third square. A generic 2D density/X-ray cap is not enough.

For the full higher-rank theorem there is a second debt: preserve a paid rank-three spectral mechanism in the presence of correlated additional spectral components, without treating them as independent noise.

Do not use the refuted pointwise oscillatory-decay route or unrestricted spectral-fiber supremum.
