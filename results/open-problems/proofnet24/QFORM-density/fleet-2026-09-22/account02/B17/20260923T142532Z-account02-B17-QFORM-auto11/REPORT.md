# Unequal opposite rank-one cube banks: a global sharp-constant barrier

Run: `20260923T142532Z-account02-B17-QFORM-auto11`  
Assignment: account02/B17, sharp constant and witnesses.  
Status: `SUPPORTING_ANALYTIC_WITNESS_THEOREM`; the unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Continuity for the full target is separate.  
Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication and theorem

The previous account02/B17 theorem controlled **identical** opposite rank-one uniform banks. The first unpaid witness variation was unequal opposite banks. This note closes that whole cube-bank class, globally in the output level and with an arbitrary cap-one law on the macroscopic coordinate.

Let `a in R^m`, `b in R^n` satisfy
\[
\|a\|_2=\|b\|_2=1.
\]
Let `U_i,V_j` be mutually independent `Unif[-1/2,1/2]` variables and set
\[
S_a=\sum_{i=1}^m a_iU_i,\qquad T_b=\sum_{j=1}^n b_jV_j.
\]
Let `X_f` be independent of the banks, with an arbitrary probability density `0<=f<=1`; no support, moment, connectedness, centering or log-concavity condition is imposed on `f`.

Define the physical symmetric matrix
\[
A_{a,b}=\operatorname{diag}(1,aa^T,-bb^T).
\]
Because `aa^T` and `bb^T` are rank one with nonzero eigenvalue one,
\[
\boxed{\operatorname{spec}_{\ne0}(A_{a,b})=\{1,1,-1\}.}
\]
All physical inputs are independent and have density at most one, so every finite member is source-valid for QFORM. Its output is
\[
Q_{a,b,f}=X_f^2+S_a^2-T_b^2.
\]

### Theorem

For every `m,n`, every unit coefficient profiles `a,b`, and every cap-one heavy density `f`,
\[
\boxed{
\|p_{Q_{a,b,f}}\|_\infty
\le K_*:=\frac\pi2\left(\sqrt2+2^{1/4}\right)
<3\sqrt2.
}
\tag{1.1}
\]
Numerically, only as a check,
\[
K_*=4.089443637123813\ldots,
\qquad
3\sqrt2=4.242640687119285\ldots.
\]
Thus arbitrary **unequal** redistribution of leverage in the two opposite rank-one cube banks cannot produce a witness above the current `3sqrt(2)` obstruction, even when the singleton law is arbitrarily fragmented, translated or unbounded in support.

## 2. Bank shape and the cap-one envelope

Write `h_a,h_b` for the densities of `S_a,T_b`. Each nonzero summand `a_iU_i` has an even interval density, hence is log-concave; convolution preserves log-concavity. Therefore `h_a,h_b` are even and nonincreasing on `[0,infinity)`. This is a property of the explicit cube-bank witness class, not an assumption on general QFORM inputs.

For `y>0`, the density of `T_b^2` is
\[
g_b(y)=\frac{h_b(\sqrt y)}{\sqrt y}.
\tag{2.1}
\]
Conditioning on `(X_f,S_a)` gives, for almost every output `t`,
\[
p_{Q_{a,b,f}}(t)
=\int_{\mathbb R}f(x)\int_{\mathbb R}h_a(s)
 g_b(x^2+s^2-t)\,\mathbf 1_{\{x^2+s^2>t\}}\,ds\,dx.
\tag{2.2}
\]
Since `f<=1`,
\[
p_{Q_{a,b,f}}(t)\le P_{a,b}(t),
\tag{2.3}
\]
where
\[
P_{a,b}(t):=
\iint_{x^2+s^2>t}
h_a(s)\frac{h_b(\sqrt{x^2+s^2-t})}{\sqrt{x^2+s^2-t}}\,ds\,dx.
\tag{2.4}
\]
The advantage of (2.4) is that it no longer contains the arbitrary heavy law.

## 3. New global output-level monotonicity

The earlier identical-bank argument used symmetry of the residual density. That symmetry is lost when `a != b`. The replacement is a direct monotonicity of the cap-one envelope `P_{a,b}`.

### Negative outputs

Let `t=-tau<=0`. Then
\[
P_{a,b}(-\tau)
=\iint h_a(s)
\frac{h_b(\sqrt{x^2+s^2+\tau})}{\sqrt{x^2+s^2+\tau}}\,ds\,dx.
\]
Because `r -> h_b(r)` is nonincreasing and nonnegative on `(0,infinity)`, so is `r -> h_b(r)/r`. Hence pointwise
\[
\boxed{P_{a,b}(-\tau)\le P_{a,b}(0).}
\tag{3.1}
\]

### Positive outputs

Let `t>=0`. In polar coordinates `x=r cos(theta), s=r sin(theta)`, (2.4) becomes
\[
P_{a,b}(t)
=\int_0^{2\pi}\int_{\sqrt t}^{\infty}
 h_a(r\sin\theta)
 \frac{h_b(\sqrt{r^2-t})}{\sqrt{r^2-t}}r\,dr\,d\theta.
\]
Put `q=sqrt(r^2-t)`, so `r dr=q dq`. Then
\[
P_{a,b}(t)
=\int_0^{2\pi}\int_0^\infty
h_a(\sqrt{q^2+t}\sin\theta)h_b(q)\,dq\,d\theta.
\tag{3.2}
\]
Evenness and monotonicity of `h_a` give
\[
h_a(\sqrt{q^2+t}\sin\theta)\le h_a(q\sin\theta),
\]
so
\[
\boxed{P_{a,b}(t)\le P_{a,b}(0),\qquad t\ge0.}
\tag{3.3}
\]
Combining (2.3), (3.1), and (3.3),
\[
\boxed{\|p_{Q_{a,b,f}}\|_\infty\le P_{a,b}(0).}
\tag{3.4}
\]
This is the key step allowing unequal banks.

## 4. Two cube-projection norms

The Ball/Rogozin cube-projection theorem gives, for every unit coefficient vector,
\[
\boxed{\|h_a\|_\infty\le\sqrt2,
\qquad \|h_b\|_\infty\le\sqrt2.}
\tag{4.1}
\]
The constant is sharp for the two-coordinate diagonal projection. This is the same cube-slicing input used in the required pinned Claude source; its rank-three ruled theorem uses the corresponding two-dimensional product-measure marginal bound.

A second consequence, crucial here, is
\[
\boxed{\|h_a\|_2^2\le1,
\qquad \|h_b\|_2^2\le1.}
\tag{4.2}
\]
Indeed, if `S_a'` is an independent copy and
\[
Z_a=\frac{S_a-S_a'}{\sqrt2},
\]
then `Z_a` is a projection of `2m` independent centered unit intervals with unit coefficient vector `(a,-a)/sqrt(2)`. By (4.1), `p_{Z_a}(0)<=sqrt(2)`. But scaling and convolution give
\[
p_{Z_a}(0)
=\sqrt2\,p_{S_a-S_a'}(0)
=\sqrt2\int_\mathbb R h_a(s)^2\,ds.
\]
Thus `||h_a||_2^2<=1`, and similarly for `b`.

## 5. Cone-tip integral and the universal constant

At zero, polar coordinates cancel the singular radial factor:
\[
\begin{aligned}
P_{a,b}(0)
&=\int_0^{2\pi}\int_0^\infty
 h_a(r\sin\theta)h_b(r)\,dr\,d\theta\\
&=4\int_0^1\frac{I(u)}{\sqrt{1-u^2}}\,du,
\end{aligned}
\tag{5.1}
\]
where
\[
I(u):=\int_0^\infty h_b(r)h_a(ur)\,dr.
\tag{5.2}
\]
The `L^infinity` projection bound and `int_0^infinity h_b=1/2` give
\[
I(u)\le\frac{\sqrt2}{2}.
\tag{5.3}
\]
By Cauchy-Schwarz, evenness, and (4.2),
\[
\begin{aligned}
I(u)
&\le
\left(\int_0^\infty h_b(r)^2dr\right)^{1/2}
\left(\int_0^\infty h_a(ur)^2dr\right)^{1/2}\\
&\le \frac1{2\sqrt u},\qquad u>0.
\end{aligned}
\tag{5.4}
\]
For `0<=u<=1/sqrt(2)` use (5.3). For `1/sqrt(2)<=u<=1`, (5.4) gives
\[
I(u)\le\frac{2^{1/4}}2.
\tag{5.5}
\]
Since
\[
\int_0^{1/\sqrt2}\frac{du}{\sqrt{1-u^2}}
=\int_{1/\sqrt2}^{1}\frac{du}{\sqrt{1-u^2}}
=\frac\pi4,
\]
(5.1) yields
\[
P_{a,b}(0)
\le4\left[
\frac{\sqrt2}{2}\frac\pi4
+\frac{2^{1/4}}2\frac\pi4
\right]
=\boxed{\frac\pi2(\sqrt2+2^{1/4})}.
\tag{5.6}
\]
Finally, `pi<22/7` and `2^{-1/4}<10/11` (equivalently `11^4<2*10^4`) imply
\[
\frac{K_*}{\sqrt2}
=\frac\pi2(1+2^{-1/4})
<\frac{11}{7}\left(1+\frac{10}{11}\right)
=3.
\]
Therefore
\[
\boxed{K_*<3\sqrt2.}
\tag{5.7}
\]
This proves (1.1).

## 6. Required application of the pinned Claude result

The required source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` proves, in `COUNTEREXAMPLE_SEARCH.md`, Theorem C: for an exact rank-three `(+, +, -)` form with eigenvalue magnitudes at least one,
\[
p_Q(s)\le\pi\sqrt2,\qquad s\ge0.
\tag{6.1}
\]
Our `A_{a,b}` has exactly that spectrum, so (6.1) is an immediate valid finite-source inequality for every member of this unequal-bank family. It rules out unbounded one-sheet escape but is not sharp enough for the proposed `3sqrt(2)` constant because `pi sqrt(2)>3sqrt(2)`. The new envelope argument upgrades this specific family from the source's one-sided `pi sqrt(2)` bound to the global strict inequality
\[
\boxed{\|p_{Q_{a,b,f}}\|_\infty\le K_*<3\sqrt2.}
\tag{6.2}
\]
Thus failure of Theorem C's constant to reach `3sqrt(2)` is a limitation of that proof constant, not evidence against QFORM.

The same pinned source also explicitly invokes Ball/Rogozin product-measure projection bounds; those are the source-valid ingredients used in (4.1)-(4.2).

## 7. Application of the latest designated partner result

The latest account03/B17 theorem, source-pinned at

`math-open-problems@f8070e3dd56d0f4f4fb3f4b4734c7bc65f3684fc`,

proves for three independent normalized uniform banks of arbitrary unequal sizes `m_j>=3` and arbitrary orthogonal orientation `O` that
\[
\frac{p_{\widetilde Q}(0)}{3\sqrt2}
=1-\sum_{j=1}^3\frac{h(O_{3j}^2)}{20m_j}
+O\!\left((\sum_jm_j^{-1})^2\right),
\]
where
\[
h(u)=\frac{57+6u-39u^2}{32}\ge\frac34.
\]
Hence
\[
\limsup_{\min m_j\to\infty}\sup_{O\in O(3)}p_{\widetilde Q}(0)\le3\sqrt2.
\tag{7.1}
\]
Combining (7.1) with the present global theorem gives the concrete two-architecture obstruction
\[
\boxed{
\max\left\{
\sup_{a,b,f}\|p_{Q_{a,b,f}}\|_\infty,
\ \limsup_{\min m_j\to\infty}\sup_O p_{\widetilde Q}(0)
\right\}
\le3\sqrt2,
}
\tag{7.2}
\]
with the first term in fact bounded by `K_*<3sqrt(2)`. Thus unequal bank scales do not create a sharp-constant overshoot either in the one-heavy/two-opposite-rank-one architecture or, at first order at the cone tip, in the fully diffuse three-bank architecture.

## 8. Scope and remaining witness class

This theorem does **not** assume anything extra in the full conjecture; rather, it analyzes one explicit source-valid adversarial subclass. Its bank variables are chosen to be centered unit intervals, while the heavy variable is arbitrary cap one.

The theorem does not control banks built from arbitrary fragmented/nonunimodal physical marginals, several shared or non-collinear intermediate-leverage rows, additional active spectrum, or other coupled multiscale structures. The proof of (3.1)-(3.3) uses the unimodality of the explicit cube-bank projection densities; if a future adversarial bank density is nonunimodal, this envelope mechanism can fail. Such a failure is a **failure of this mechanism**, not a counterexample to QFORM.

Likewise, an eventual valid example with peak above `3sqrt(2)` would disprove only the proposed sharp constant `3sqrt(2)`; it would not by itself disprove the existence of a larger universal QFORM constant.

The first B17 witness obligation after this result is therefore: construct or rule out **nonunimodal unequal opposite banks or genuinely shared-coordinate intermediate-leverage geometries**, always retaining cap-one physical marginals and verifying the actual spectrum.

## 9. Correction compatibility

The live correction inbox was reread before publication. This proof does not use uniform pointwise quadratic-phase decay, independence after spectral rotation, arbitrary-joint rank-three coarea, worst fiber suprema, positive moments of conditional projection caps, a universally conditioned physical minor, a rank-three cross-cut dichotomy, bounded fragment count, or near-zero half-Riesz interpolation. All independence used above is independence of the original physical variables in the explicit construction.

Full QFORM status remains **OPEN / NOT PROVED / NOT DISPROVED**.
