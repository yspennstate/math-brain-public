# fleet02/B15 auto11 — early mathematical checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Execution `WITHOUT_VERIFIED_BRAIN`.

## First unpaid implication, in exact positive form

Apply the completed assigned-partner result fleet03/B15 auto11 (`math-open-problems@a86bb095aac440bd79e2b2c26b23228ac952d2ab`). For every probability law `mu` on `R`, with `+infinity` if no bounded density exists,

`||p_mu||_infinity = sup_{r>0,y} mu({r<|z-y|<2r})/(2r)`.

Therefore the full QFORM theorem is exactly the universal shell estimate

`P(r<|X^T A X-y|<2r) <= 2 C r`

for all target instances, all `r>0`, and all `y`. No continuity assertion is used.

## Apply the completed ruled one-sheet theorem to a real shell inequality

From the required Claude source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, Theorem C gives, for

`q(z)=lambda_1 z_1^2+lambda_2 z_2^2-mu z_3^2`, `lambda_1,lambda_2,mu>=1`,

the majority-side density bound

`p_q(s) <= C_+ := (lambda_1 lambda_2 mu)^(-1/2) int_0^{2pi} [sin^2(theta)/lambda_1+cos^2(theta)/lambda_2+1/mu]^(-1/2) dtheta <= pi sqrt(2)`

for `s>=0`.

Hence for every `r>0,y`,

`P(r<|q-y|<2r, q>=0) <= 2 C_+ r <= 2 pi sqrt(2) r`.

For an affine translate `q+c`, replace `q>=0` by `q+c>=c`. For a physical invertible 3x3 indefinite block `B` with smallest absolute eigenvalue `kappa`, conditioning on all outside original coordinates and completing the square inside those three coordinates preserves their product cap-one laws; averaging yields a positive majority submeasure `nu_+` with

`nu_+({r<|z-y|<2r})/(2r) <= C_B <= pi sqrt(2)/kappa`.

Thus, within this branch, the first unpaid term is precisely the minority/two-sheet positive submeasure `nu_-`:

`sup_{r,y} nu_-({r<|z-y|<2r})/(2r)`.

By the finite-measure version of the partner annular lemma, any universal bound on this last quantity is exactly a bounded-density bound for `nu_-`; combining with `nu_+` gives the full conditional/ambient density bound. This isolates the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` obstruction without invoking continuity.

## Rough-input bridge check

The ruled estimate can be passed from smooth to arbitrary cap-one marginals without a continuity assumption on the output. Convolve each original-coordinate density with a Gaussian. This preserves independence and the cap `<=1`, and converges in `L^1`. For fixed finite dimension, the product densities converge in `L^1` by telescoping, hence the joint laws and all fixed measurable subevents converge in total variation. The smooth majority-side interval/shell inequality therefore passes to the original rough law. Interval domination then implies absolute continuity of the majority submeasure with essential density at most `C_B`; it does not imply a continuous representative.

Next: test whether the exact annular normal form permits a uniform small-scale limit. A phase-aligned target family should decide this without touching the full height conjecture.
