# Smoothing corollary: the full target reduces to smooth compact cap-one laws

This is a supplement to `REPORT.md` in the same run.

## Statement

The restricted hypothesis `(R)` in the main report can be weakened further: it is enough to prove the universal interval bound with constant `C` only when every input density lies in `C_c^infty(R)`, satisfies `0<=f<=1`, and the matrix has three eigenvalues of absolute value strictly greater than one.

Then the full owner target for arbitrary measurable cap-one densities and threshold `>=1` follows with exactly the same constant `C`. The affine extension also follows with the same constant.

## Proof

Start with an arbitrary cap-one density `f`. The main report constructs compactly supported cap-one densities `f^(R)` with

`||f^(R)-f||_1 <= 2 delta_R -> 0`.

Let `phi_epsilon` be a nonnegative `C_c^infty` probability mollifier. Put

`f^(R,epsilon)=f^(R) * phi_epsilon`.

Then

1. `f^(R,epsilon)>=0` and its integral is one;
2. convolution with a probability density is an `L^infinity` contraction, hence `||f^(R,epsilon)||_infinity <= ||f^(R)||_infinity <=1`;
3. the support is compact because both factors have compact support;
4. `f^(R,epsilon)` is smooth;
5. for fixed `R`, `||f^(R,epsilon)-f^(R)||_1 ->0` as `epsilon->0`.

Apply this independently coordinate by coordinate. Product total variation is at most the sum of the marginal total variations, and every quadratic pushforward contracts total variation. Therefore any interval inequality with constant `C` valid for the smooth compact product laws passes first as `epsilon->0` to the compact rough product laws and then as `R->infinity` to the original product law, with no constant loss.

The strict-to-threshold eigenvalue passage is Section 4 of the main report.

For the affine homogenization, if one wants to invoke only the smooth-input restricted theorem, replace the auxiliary uniform law on `[T,T+1]` by any fixed smooth compact cap-one probability density `g` translated by `T`: `Y_T=T+Y`, `Y~g`. Such `g` exists, for example by convolving the unit-interval density with a smooth compact probability mollifier; convolution preserves the cap `<=1`. Since `Y` is finite almost surely, `Y_T/T ->1` almost surely. The matrix perturbation and Weyl argument are unchanged. Thus the affine theorem also follows from the smooth restricted class.

## Consequence for proof design

A future proof of the remaining analytic core may freely use smooth compact one-dimensional densities and a strict spectral margin, provided every bound is uniform in the support geometry, the support diameter, the number/separation of fragments before smoothing, and the amount by which the third eigenvalue exceeds one. The exact compiler in `REPORT.md` then returns to arbitrary rough/unbounded laws and the threshold case without any tail or moment term.

This is a localization/regularization reduction only. It does not prove the missing analytic bound for the smooth compact class and does not establish full-target continuity.
