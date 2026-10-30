SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B14, 2026-09-22T23:35:21Z.
attacking: rough-input localization for the ruled one-sheet rank-three estimate, retaining range-compatible affine shifts and arbitrary unbounded fragmented supports.

# fleet03/B14 r21 — rough-input one-sheet localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `ESSENTIAL_STEP_APPLIED / FULL_CONJECTURE_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`  

## 1. Result

This run closes the rough-input / localization gap explicitly flagged in the newest owner-directed Claude source for its ruled-hyperboloid Theorem C. It does **not** close the convex/two-sheet side or the full QFORM conjecture.

Let `A` be real symmetric of exact rank three and indefinite. Choose `sigma in {+1,-1}` so that `sigma A` has eigenvalues

\[
  \lambda_1>0,\qquad \lambda_2>0,\qquad -\mu<0,
\]

with `lambda_1,lambda_2,mu>0`. Let

\[
 F(x)=x^TAx+2b^Tx+c,\qquad b\in\operatorname{Ran}A,
\]

and define the affine critical value

\[
 c_*:=c-b^T A^+b,
\]

where `A^+` is the Moore-Penrose inverse. For arbitrary independent real `X_i` with probability densities `0<=f_i<=1`, the restriction of the law of `F(X)` to the majority-sign / one-sheet half-line

\[
 \sigma(t-c_*)\ge0
\]

is absolutely continuous and its density obeys

\[
 \boxed{
 \|p_F\|_{L^\infty(\{\sigma(t-c_*)\ge0\})}
 \le C(\lambda_1,\lambda_2,\mu)
 \le \pi\sqrt2,
 }
\]

provided `lambda_1,lambda_2,mu>=1`, where the sharper eigenvalue-sensitive constant is

\[
 C(\lambda_1,\lambda_2,\mu)
 =\frac1{\sqrt{\lambda_1\lambda_2\mu}}
 \int_0^{2\pi}
 \frac{d\theta}{
 \sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}.
 \tag{1}
\]

Equivalently, for every `a>=0` and `h>0`,

\[
 \Pr\{\sigma(F(X)-c_*)\in[a,a+h]\}
 \le C(\lambda_1,\lambda_2,\mu)h.
 \tag{2}
\]

The conclusion has **no** support-radius, moment, fragment-count, fragment-separation, connected-support, smoothness, or centering hypothesis.

Continuity is **not** proved for the arbitrary rough inputs by this argument. Smooth compact approximants have continuous projected densities, but total-variation limits of continuous bounded densities need not have continuous representatives.

## 2. Source result consumed

The newest required source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its `COUNTEREXAMPLE_SEARCH.md`, Theorem C, gives the ruled-hyperboloid calculation on the one-sheet side for signature `(+,+,-)`. The current owner continuation expressly warned that the line-trace step has to be justified for rough marginal densities: an a.e. two-dimensional projection-density bound cannot simply be evaluated pointwise on a prescribed curve. The proof below supplies that missing bridge by first proving the estimate for smooth compact product inputs, where the relevant marginal density is continuous, and then passing to arbitrary cap-one products in total variation with no constant loss.

## 3. Cap-preserving smooth compact approximation with no moments

### Lemma 1
For every probability density `0<=f<=1` on `R`, there exist `f_k in C_c^infinity(R)` such that

\[
 0\le f_k\le1,\qquad \int f_k=1,\qquad \|f_k-f\|_1\to0.
 \tag{3}
\]

### Proof
Choose `R` and put

\[
 m_R=\int_{|x|>R}f(x)\,dx.
\]

Define

\[
 g_R(x)=f(x)1_{[-R,R]}(x)+1_{[R+1,R+1+m_R]}(x).
\]

Then `g_R` is a compactly supported probability density and `0<=g_R<=1`. Moreover

\[
 \|g_R-f\|_1
 \le \int_{|x|>R}f(x)dx + m_R
 =2m_R\to0.
\]

Let `eta_epsilon` be a nonnegative compactly supported smooth mollifier of mass one. Then

\[
 f_{R,\epsilon}=g_R*\eta_\epsilon
\]

is smooth, compactly supported, nonnegative, has total mass one, and satisfies

\[
 \|f_{R,\epsilon}\|_\infty\le\|g_R\|_\infty\le1.
\]

For fixed `R`, choose `epsilon` so that `||f_{R,epsilon}-g_R||_1` is arbitrarily small, and diagonalize in `R`. No first or higher moment of `f` is used. QED.

For a fixed finite dimension, applying Lemma 1 coordinatewise gives product measures `mu_k` with

\[
 d_{TV}(\mu_k,\mu)
 \le \frac12\sum_i\|f_{i,k}-f_i\|_1\to0.
 \tag{4}
\]

Every measurable pushforward contracts total variation.

## 4. Why the line-trace bound is pointwise for smooth products

Assume now that all coordinate densities are `C_c^infinity`. Let `R` be the `n x 3` matrix whose columns are orthonormal eigenvectors corresponding to the three nonzero eigenvalues of `sigma A`, and let

\[
 Y=R^TX\in\mathbb R^3.
\]

The product density of `X` is smooth and compactly supported. After completing `R` to an orthogonal matrix and integrating the product density over the orthogonal complement, the density `rho` of `Y` is `C_c^infinity(R^3)`.

Fix any unit direction `v in S^2`. For `a in v^perp`,

\[
 L_v(a)=\int_{a+\mathbb Rv}\rho(y)\,d\ell(y)
\]

is the density at `a` of the two-dimensional orthogonal projection `P_{v^perp}Y`. If `eta_1,eta_2` is an orthonormal basis of `v^perp`, then

\[
 (\eta_1^TY,\eta_2^TY)
 =((R\eta_1)^TX,(R\eta_2)^TX),
\]

and `R eta_1,R eta_2` are orthonormal vectors in the original coordinate space. The two-dimensional product-projection density bound used in the source Theorem C therefore gives

\[
 \|L_v\|_\infty\le2.
 \tag{5}
\]

For rough laws that theorem is an essential-supremum statement. Here `rho` is smooth compact, hence `L_v` is continuous, so its essential bound is a genuine pointwise bound at every `a`. This is exactly what makes the prescribed ruling lines legitimate before the limiting step.

## 5. Exact ruled coarea calculation

After the affine translation in Section 6 below, it suffices to treat

\[
 q(y)=\lambda_1 y_1^2+\lambda_2 y_2^2-\mu y_3^2.
\]

Put

\[
 D=\operatorname{diag}(\sqrt{\lambda_1},\sqrt{\lambda_2},\sqrt\mu),
 \qquad z=Dy,
\]

so that

\[
 q(y)=q_0(z):=z_1^2+z_2^2-z_3^2.
\]

If `rho` is the density of `Y`, the density in `z` coordinates is

\[
 \widetilde\rho(z)=\frac{\rho(D^{-1}z)}{\sqrt{\lambda_1\lambda_2\mu}}.
\]

For `s>0`, write

\[
 e_\theta=(\cos\theta,\sin\theta,0),\qquad
 e_\theta^\perp=(-\sin\theta,\cos\theta,0),
\]

and parameterize `q_0=s` by

\[
 \Phi_s(\theta,t)=\sqrt{s}\,e_\theta+t(e_\theta^\perp+e_3).
 \tag{6}
\]

Directly,

\[
 q_0(\Phi_s(\theta,t))=s.
\]

More importantly,

\[
 \partial_\theta\Phi_s\times\partial_t\Phi_s
 =\frac12\nabla q_0(\Phi_s).
 \tag{7}
\]

Hence the coarea surface factor is **exactly**

\[
 \frac{d\sigma}{|\nabla q_0|}=\frac12\,d\theta\,dt.
 \tag{8}
\]

Therefore the smooth output density is

\[
 p_q(s)=\frac12\int_0^{2\pi}\int_{\mathbb R}
 \widetilde\rho(\Phi_s(\theta,t))\,dt\,d\theta.
 \tag{9}
\]

For fixed `theta`, set

\[
 v_\theta=e_\theta^\perp+e_3,
 \qquad
 w_\theta=D^{-1}v_\theta
 =\left(-\frac{\sin\theta}{\sqrt{\lambda_1}},
 \frac{\cos\theta}{\sqrt{\lambda_2}},
 \frac1{\sqrt\mu}\right).
\]

The inner integral in (9), returned to `y` coordinates, is

\[
 \frac1{\sqrt{\lambda_1\lambda_2\mu}}
 \int_{\mathbb R}\rho(a_\theta+t w_\theta)\,dt
 =\frac1{\sqrt{\lambda_1\lambda_2\mu}\,|w_\theta|}
 \int_{a_\theta+\mathbb Rw_\theta}\rho(y)\,d\ell(y).
\]

Using (5),

\[
 p_q(s)
 \le\frac1{\sqrt{\lambda_1\lambda_2\mu}}
 \int_0^{2\pi}\frac{d\theta}{|w_\theta|},
 \tag{10}
\]

which is exactly (1).

Finally,

\[
 \frac{1}{\sqrt{\lambda_1\lambda_2\mu}\,|w_\theta|}
 =\frac1{\sqrt{
 \lambda_2\mu\sin^2\theta+
 \lambda_1\mu\cos^2\theta+
 \lambda_1\lambda_2}}.
\]

If `lambda_1,lambda_2,mu>=1`, the denominator is at least

\[
 \sqrt{\sin^2\theta+\cos^2\theta+1}=\sqrt2,
\]

so

\[
 C(\lambda_1,\lambda_2,\mu)\le\frac{2\pi}{\sqrt2}=\pi\sqrt2.
 \tag{11}
\]

This verifies both the coarea Jacobian and the exact source constant.

## 6. Range-compatible affine terms cost zero

Return to

\[
 F(x)=x^TAx+2b^Tx+c,
 \qquad b\in\operatorname{Ran}A.
\]

Take

\[
 h=-A^+b.
\]

Then `Ah=-b`. Writing `x=z+h`,

\[
 F(z+h)=z^TAz+c-b^TA^+b=z^TAz+c_*.
 \tag{12}
\]

Coordinate translation preserves independence and every marginal density cap. Thus (10)-(11) apply on the one-sheet side relative to `c_*`, with exactly the same constant.

This is the precise translation statement needed here. No assertion is made for an affine component outside `Ran A`; such a component cannot be removed by translating a singular quadratic form.

## 7. Passing from smooth compact inputs to arbitrary fragmented/unbounded inputs

Let `mu_k` be the smooth compact product approximants from Lemma 1 and let

\[
 \nu_k=F_\#\mu_k,\qquad \nu=F_\#\mu.
\]

By (4) and contraction of total variation,

\[
 d_{TV}(\nu_k,\nu)\to0.
 \tag{13}
\]

For every Borel set `E` in the one-sheet half-line

\[
 H_\sigma:=\{t:\sigma(t-c_*)\ge0\},
\]

Sections 4-6 give

\[
 \nu_k(E)\le C(\lambda_1,\lambda_2,\mu)|E|.
\]

Taking `k->infinity` in total variation yields

\[
 \nu(E)\le C(\lambda_1,\lambda_2,\mu)|E|.
 \tag{14}
\]

In particular `nu({c_*})=0`, and the restriction of `nu` to `H_sigma` has a Radon-Nikodym density bounded by the same constant. This proves (1)-(2) for the original arbitrary input laws.

No moment or support hypothesis entered the limiting argument.

## 8. Application of the completed designated partner result

The designated partner fleet04/B14 proved

`QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1`

at

`yspennstate/math-open-problems@1250c776b3840b8494ace461b27541f8e156e9bf`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B14/20260922T182134Z-fleet04-B14-centered-affine-r3/REPORT.md`.

Its argument is matrix-by-matrix and therefore restricts to this exact-rank-three indefinite subclass. Moreover it preserves the relevant side of the critical value exactly.

Indeed, start with an arbitrary homogeneous input and a compact approximation having mean `m`. Center it by `Y=X-m`. Then

\[
 X^TAX=Y^TAY+2(Am)^TY+m^TAm.
\]

In the partner notation `b=Am`, `c=m^TAm`, so

\[
 c_*=c-b^TA^+b
 =m^TAm-m^TA A^+A m
 =0.
 \tag{15}
\]

Applying the present theorem to this **actual localized affine inequality** gives, for every `a>=0,h>0`,

\[
 \boxed{
 \Pr\{\sigma[\,Y^TAY+2(Am)^TY+m^TAm\,]\in[a,a+h]\}
 \le C(\lambda_1,\lambda_2,\mu)h.
 }
 \tag{16}
\]

There is no centering, tail, support-diameter, fragment-count, or fragment-separation loss.

Conversely, for a centered affine instance with `b in Ran A`, choose `m` with `Am=b` and set `X=Y+m`. Then

\[
 Y^TAY+2b^TY+c=X^TAX+c-m^TAm,
\]

and `m^TAm=b^TA^+b`, so

\[
 F(Y)-c_*=X^TAX.
 \tag{17}
\]

Thus the majority-sign half-line is preserved exactly under the partner's centering/uncentering equivalence. In particular the sharp one-sheet small-ball constant is the same over arbitrary homogeneous cap-one inputs, compact centered range-affine cap-one inputs, and centered compact finite-fragment extreme inputs.

This is the requested application of a completed partner result to an actual inequality, not merely a citation.

## 9. Numerical/algebraic checker

A deterministic checker for the two identities used in the geometry was run on 10,000 parameter samples. It checks

1. `q_0(Phi_s(theta,t))=s`;
2. `partial_theta Phi x partial_t Phi = (1/2) grad q_0(Phi)`;
3. the target-scale integrand is at most `1/sqrt(2)` whenever `lambda_1,lambda_2,mu>=1`.

Observed maximum floating residuals were

`cross_identity_error = 2.842170943040401e-14`,

`level_identity_error = 4.392659846974567e-12`.

The checker is only a diagnostic; the exact identities are proved algebraically above.

## 10. What this does and does not close

Closed in stated scope:

* the one-sheet side of every exact-rank-three indefinite form;
* arbitrary independent cap-one marginals, including unbounded supports and arbitrarily distant/many fragments;
* all range-compatible affine translations, with the exact critical value `c_*`;
* the pointwise-trace gap in applying the newest source Theorem C to rough input laws;
* the exact constant `C(lambda_1,lambda_2,mu)`, hence the universal `pi sqrt(2)` bound when all three magnitudes are at least one.

Still open:

* the two-sheet/convex side of an exact-rank-three indefinite form;
* definite exact-rank-three forms in a diffuse spectral orientation;
* higher-rank matrices with arbitrary additional eigenvalues/couplings;
* arbitrary conditioning-generated affine kernel components for a singular active block;
* a continuous density representative for the full rough-input theorem.

Therefore full QFORM remains `OPEN / NOT PROVED`.

## 11. Source pins

* Fresh control source used at start: `yspennstate/math-research-brain@cb13f8ef744550c0e1a1136dbaf95d617e95d638`.
* Newest Claude source required by the owner: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md`, Theorem C.
* Designated partner theorem actually applied: `yspennstate/math-open-problems@1250c776b3840b8494ace461b27541f8e156e9bf`, fleet04/B14 centered-affine localization report.
* Current correction discipline retained: pointwise quadratic-phase decay, arbitrary-joint coarea, worst conditional-density moments, universal single-minor/cross-rank-three gates, and fixed fragment-count/diameter localization remain unavailable.
