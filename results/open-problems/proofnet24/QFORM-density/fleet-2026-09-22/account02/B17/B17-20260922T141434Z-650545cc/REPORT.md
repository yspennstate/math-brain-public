# account02/B17 — first-order no-escape theorem around the sharp diffuse witness

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Run:** `B17-20260922T141434Z-650545cc`  
**Assignment:** Sharp constant and witnesses  
**Status:** `NEW SUPPORTING THEOREM / FULL CONJECTURE OPEN`  

## 1. Full target and correction status

The full target remains open: for every dimension, every product law with independent real coordinate densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal finite bound on the density of `X^T A X`, or give a valid source-valid counterexample.

This run uses none of the refuted pointwise-Fresnel, fiber-supremum, conditional-density-cap, single-minor, single-Schur, local-cross-rank3, absolute phase-Wiener, or bounded-diameter-localization mechanisms. Product aggregation is kept until the actual three-bank quadratic output is formed.

A fresh partner result arrived during this run. `account03/B17`, canonical report `yspennstate/math-open-problems@3d0926c161ba4cbea4016bff63d89e34f87cb0e6`, independently closed the noncentral Gaussian branch by Poisson-mixture contraction, using the preceding `account02/B17` centered-Gaussian theorem. I therefore make no novelty claim for that noncentral closure. I apply it below and change the witness mechanism to the partner's next suggested stress: unequal/mixed first-order perturbations of the exact diffuse Boolean-free product source.

## 2. Exact source-valid stress family

Let the three banks be independent. For `j=1,2,3`, let

`U_{j,k} ~ Unif[-1/2,1/2]`, `k=1,...,m_j`,

and fix bounded real parameters `d_j` and bounded nonnegative parameters `u_j`. Put

`X_{j,k}=U_{j,k}+d_j/m_j`,

`S_j=m_j^{-1/2} sum_{k=1}^{m_j} X_{j,k}`,

`lambda_j=1+u_j/m_j`,

and

`Q=lambda_1 S_1^2 + lambda_2 S_2^2 - lambda_3 S_3^2`.

Every physical input density is exactly one on an interval of length one. The corresponding physical matrix is

`A=diag(lambda_1 J_{m_1}/m_1, lambda_2 J_{m_2}/m_2, -lambda_3 J_{m_3}/m_3)`,

so its nonzero spectrum is exactly `{lambda_1,lambda_2,-lambda_3}` and all three absolute eigenvalues are at least one. This is therefore an actual target family, not a Gaussian replacement.

The parameters test simultaneously:

1. unequal bank sizes;
2. source-valid `O(1/m_j)` mean shifts;
3. admissible `O(1/m_j)` outward perturbations of the three large eigenvalues.

## 3. The first-order no-escape theorem

Let

`rho = 1/m_1 + 1/m_2 + 1/m_3`.

As `min(m_1,m_2,m_3) -> infinity`, uniformly for `(d_j,u_j)` in any fixed compact set with `u_j>=0`, the density of `Q` at zero satisfies

\[
\boxed{
\frac{p_Q(0)}{3\sqrt2}
=1-
\frac{\frac{57}{640}+\frac92d_1^2+\frac38u_1}{m_1}
-
\frac{\frac{57}{640}+\frac92d_2^2+\frac38u_2}{m_2}
-
\frac{\frac3{80}+3d_3^2+\frac14u_3}{m_3}
+O(\rho^2).
}
\]

Every displayed first-order coefficient is strictly positive. Consequently **none of unequal bank counts, bounded mesoscopic translations of the unit intervals, or admissible outward `1/m` eigenvalue perturbations can push this diffuse three-bank saddle above `3 sqrt(2)` at first order.**

For `m_1=m_2=m_3=m`, `d_j=u_j=0`, the coefficient reduces exactly to

`2*(57/640)+3/80 = 69/320`,

recovering the completed `account03/B17` coefficient. Thus the theorem genuinely extends that partner result rather than replacing it.

This is a supporting local asymptotic theorem. It does **not** show that `3 sqrt(2)` is the global universal sharp constant.

## 4. Proof from the partner's exact Edgeworth expansion

Write `T_m=m^{-1/2} sum U_k` and let `f_m` be its density. The completed partner report `d7b6ac18a1dc1374de0ed902a110262d5061b1d0` proves the uniform expansion

\[
f_m(x)=\gamma(x)\left[1-\frac{H_4(z)}{20m}+O(m^{-2}P(z))\right],
\quad
\gamma(x)=\sqrt{6/\pi}e^{-6x^2},\quad z=\sqrt{12}x,
\]

with a Gaussian-dominated remainder strong enough for the polar saddle integral.

Only the even part of the translated density enters a square. With `delta=d/sqrt(m)`, define

\[
g_{m,d}(x)=\frac12\{f_m(x-\delta)+f_m(x+\delta)\}.
\]

Taylor expansion of the Gaussian term, together with symmetry cancellation of the odd derivative and the partner's uniform remainder, gives

\[
g_{m,d}(x)=\gamma(x)\left[
1+\frac1m\left(-\frac{H_4(z)}{20}+6d^2(z^2-1)\right)
+O(m^{-2}P_d(z))
\right].
\]

Indeed `gamma''/gamma=12(z^2-1)`, so the symmetric translation contributes `(d^2/(2m)) gamma''`.

At unit coefficients, the exact three-square saddle identity is the partner's polar formula. Under its normalized Gaussian baseline measure,

`E H_4(z_1)=E H_4(z_2)=57/32`, `E H_4(z_3)=3/4`,

and

`E z_1^2=E z_2^2=1/4`, `E z_3^2=1/2`.

Therefore one positive bank contributes

`-(1/20)*(57/32) + 6 d_j^2*(1/4-1) = -57/640 -(9/2)d_j^2`,

while the negative bank contributes

`-(1/20)*(3/4) + 6 d_3^2*(1/2-1) = -3/80 -3d_3^2`.

The three different `1/m_j` terms add at first order; their products and the individual second-order remainders are `O(rho^2)`.

It remains to differentiate the Gaussian saddle with respect to the coefficients. For standard Gaussians and signature `(2,1)`, the exact zero-density formula is

\[
p_G(0;a,b,c)=\frac1{4\pi}\int_0^{2\pi}
[A(\phi)(A(\phi)+c)]^{-1/2}\,d\phi,
\quad A(\phi)=a\cos^2\phi+b\sin^2\phi.
\]

At `a=b=c=1`, differentiation under the integral gives the relative derivatives

\[
\partial_a\log p_G(0)=\partial_b\log p_G(0)=-\frac38,
\qquad
\partial_c\log p_G(0)=-\frac14.
\]

Hence `lambda_1=1+u_1/m_1`, `lambda_2=1+u_2/m_2`, and `lambda_3=1+u_3/m_3` add precisely `-3u_1/(8m_1)`, `-3u_2/(8m_2)`, and `-u_3/(4m_3)` to the relative expansion. Cross-products with the Edgeworth/translation terms are again `O(rho^2)`. This proves the theorem.

The signs have a useful structural interpretation: because the target constraint is `|lambda_j|>=1`, all legal first-order spectral movement from the equality point is outward, and the Gaussian saddle strictly decreases in every such direction.

## 5. Applying the newest completed partner theorem: exact Gaussian-input sharp constant

The newest `account03/B17` report proves that arbitrary Gaussian mean translation cannot increase the centered sharp envelope: if `G~N(0,I)` and symmetric `B` has three eigenvalues of modulus at least `s`, then for every mean vector `m`,

`||(G+m)^T B(G+m)||_density,infinity <= 1/(2 sqrt(2) s)`.

This has an immediate source-valid sharp corollary for the original problem restricted to Gaussian product inputs.

If independent `X_i~N(mu_i,sigma_i^2)` have densities bounded by one, then

`1/(sqrt(2 pi) sigma_i) <= 1`, hence `sigma_i^2>=1/(2pi)`.

Writing `Sigma=diag(sigma_i^2)` and `B=Sigma^{1/2} A Sigma^{1/2}`, the singular-value inequality gives

`s_3(B) >= lambda_min(Sigma) s_3(A) >= 1/(2pi)`.

Therefore every Gaussian-input target instance satisfies

\[
\boxed{\|p_{X^TAX}\|_\infty\le \pi/\sqrt2.}
\]

The constant is sharp inside the Gaussian-input subclass: take `n=3`, `A=diag(1,1,-1)`, centered independent Gaussians with variance `1/(2pi)`. Their one-dimensional densities have peak exactly one, and scaling the partner's equality case gives density peak `pi/sqrt(2)` at zero.

Thus actual Gaussian product laws are substantially less dangerous than the global lower-bound family (`pi/sqrt(2) < 3sqrt(2)`). The obstruction at `3sqrt(2)` is created by **finite non-Gaussian product structure that Gaussianizes only after diffuse aggregation**, not by an intrinsically worst Gaussian input law.

## 6. Relation to the regularized-determinant branch

The owner-supplied regularized-determinant theorem gives a coarse but fully source-valid upper bound below 27 when the entire range projection has row leverage at most `1/32`. For the three-bank matrices above, the range leverage in bank `j` is `1/m_j`; hence once every `m_j>=32`, that theorem already proves a universal bounded density for this whole family even with additional small spectral directions if the same full-range leverage condition persists.

The present result is different: it calibrates the **sharp local constant** of this stress family and shows several plausible first-order escapes all move downward. It does not close the heavy-coordinate/nonseparable branch of the full conjecture.

## 7. Consequences for the sharp-constant search

The strongest current stress picture is now:

- `C=pi` is false globally; exact rotated witnesses exceed it.
- every candidate universal constant must satisfy `C>=3sqrt(2)`;
- centered and noncentered Gaussian diffuse limits cannot exceed `3sqrt(2)`;
- the exact equal-bank uniform family approaches `3sqrt(2)` from below;
- the new theorem shows unequal bank sizes, `O(1/m)` source translations, and legal `O(1/m)` eigenvalue anisotropy still approach from below at first order;
- Gaussian product inputs themselves have the strictly smaller sharp constant `pi/sqrt(2)`.

Therefore a witness beating `3sqrt(2)`, if it exists, must leave this perturbative diffuse basin. The next serious adversarial mechanisms are genuinely mesoscopic/non-Lindeberg arrays, mixed-leverage matrices with a finite heavy core coupled to a diffuse tail, or `m`-dependent cap-one densities whose deviation from the variance-minimizing interval is large enough to change the saddle beyond first order.

## 8. Scope and provenance

Partner mathematics actually applied:

1. `account03/B17`, report commit `d7b6ac18a1dc1374de0ed902a110262d5061b1d0`: exact uniform Edgeworth expansion and the coefficient `69/320` for the equal-bank source.
2. `account03/B17`, report commit `3d0926c161ba4cbea4016bff63d89e34f87cb0e6`: noncentral Gaussian contraction and fully mixed Walsh stress. The noncentral theorem overlapped a derivation begun in this run; the partner completed it first, so no priority/novelty claim is made here.
3. owner-supplied regularized-determinant report `a302aab3477c64757b511e80d3907f982e04873a`: used only at its stated low-full-range-leverage scope.

Fresh live correction inbox was reread immediately before publication; no refuted premise above is used. Full conjecture status remains `OPEN / NOT PROVED`.
