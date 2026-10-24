SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T12:37:31Z.
attacking: QFORM-GRADIENT-TO-LEVEL-PRODUCT-TRACE-v1 — test whether the kappa-free Schur-gradient/coarea budget can imply a pointwise level trace, and identify the minimum additional product-projection invariant when it cannot.

# account03/B05 r25 — gradient-to-level shell obstruction and the missing product-projection factor

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Quadratic coarea bound.  
**Status:** rigorous obstruction to an intermediate proof interface; precise missing factor sharpened; full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** not proved for the full target.  
**Execution:** WITHOUT_VERIFIED_BRAIN. Repository retrieval is not native learned-memory ingestion.

## 1. First unpaid implication and conclusion of this run

The preceding B05 theorem `QFORM-SCHUR-GRADIENT-DENSITY-v1` gives, in the grouped ratio-packet normal form,

\[
\|p_{(\partial_SQ,\partial_YQ,\partial_ZQ)}\|_\infty
 \le {L_SL_YL_Z\over 8|a\det B|}
\]

and hence a dimension-free reciprocal-gradient budget

\[
\mathbb E\|\nabla Q\|_2^{-1}
\le {3\over2}\left({L_SL_YL_Z\over |a\det B|}\right)^{1/3}.
\]

For the live ratio packet this is `<3.993 mu^(-1/3)` and, crucially, has no `kappa=sigma_min(B)` loss. The unpaid step was to turn this ambient estimate into a uniform pointwise coarea trace

\[
\sup_t\int_{Q=t}{f\over\|\nabla Q\|}\,d\mathcal H.
\]

This run proves that **no such upgrade can follow from the gradient-density bound, reciprocal-gradient expectation, a cap on the grouped joint density, and one-dimensional marginal caps alone**. In fact, even uniform caps for *every one-dimensional linear projection* of an arbitrary joint law do not suffice. The missing factor is therefore genuinely the nonlinear interaction between the quadratic level geometry and the **actual original-coordinate product-projection provenance**.

This is not a counterexample to QFORM. Both constructions below deliberately leave the class of independent original-coordinate product laws at the point where they refute the proposed intermediate interface.

## 2. A block-product parabolic-shell obstruction inside the exact Schur normal form

Fix `0<delta<=1/4`. Define a pair `(S,R)` with joint probability density

\[
h_\delta(s,r)
 =\mathbf 1_{\{0\le s\le\delta^{-1}\}}
  \mathbf 1_{\{|r+s^2|\le\delta/2\}}.                  \tag{2.1}
\]

The support has area `delta^{-1}*delta=1`, so `h_delta` is a probability density and

\[
\|h_\delta\|_\infty=1.                                  \tag{2.2}
\]

Its `S` marginal is

\[
p_S(s)=\delta\mathbf 1_{[0,\delta^{-1}]}(s),
\qquad \|p_S\|_\infty=\delta\le1.                       \tag{2.3}
\]

For fixed `r`, the allowed values of `s^2` lie in an interval of length at most `delta`. Since for `0<=a<=b`,

\[
\sqrt b-\sqrt a\le\sqrt{b-a},
\]

we also have

\[
\|p_R\|_\infty\le\sqrt\delta\le1.                      \tag{2.4}
\]

Let `Y,Z` be independent `Uniform[0,1]` variables, independent of the whole pair `(S,R)`. Consider

\[
Q_\delta=S^2+R+Y^2-Z^2.                                  \tag{2.5}
\]

This is exactly a grouped quadratic-plus-affine Schur normal form with

\[
C=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
P=0,\quad
B=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad a=1.      \tag{2.6}
\]

Thus it is a direct stress test for the proposed ambient-gradient-to-level implication. The affine `+R` is allowed in conditional normal forms generated after conditioning outside original coordinates; however, the specially engineered pair `(S,R)` is **not asserted to be a linear projection of independent cap-one original variables**, so (2.5) is not a global QFORM counterexample.

### 2.1 Exact shell coordinate

Set

\[
F=S^2+R.                                                  \tag{2.7}
\]

The map `(s,r)->(s,f)` with `f=s^2+r` has Jacobian one. Under (2.1), its image is the rectangle

\[
0\le s\le\delta^{-1},\qquad |f|\le\delta/2,              \tag{2.8}
\]

with constant joint density one. Consequently

\[
F\sim \operatorname{Uniform}[-\delta/2,\delta/2],
\qquad \|p_F\|_\infty=\delta^{-1},                       \tag{2.9}
\]

and in fact `F` and `S` are independent. The curved `(S,R)` strip has converted into a thin interval under the quadratic-plus-affine map.

### 2.2 The surviving rank-two logarithm

Let

\[
T=Y^2-Z^2.                                                \tag{2.10}
\]

For `0<u<1`, using the density `(2sqrt x)^(-1)` of `Y^2`,

\[
p_T(u)={1\over4}\int_0^{1-u}{dv\over\sqrt{v(v+u)}}.     \tag{2.11}
\]

For `0<u<=1/4`, the interval `[u,1/2]` lies in the range of integration and `v+u<=2v`; therefore

\[
p_T(u)
\ge {1\over4\sqrt2}\int_u^{1/2}{dv\over v}
={1\over4\sqrt2}\log {1\over2u}.                        \tag{2.12}
\]

The law of `T` is symmetric. Since `Q_delta=F+T`, (2.9) gives

\[
\begin{aligned}
p_{Q_\delta}(0)
 &= {1\over\delta}\int_{-\delta/2}^{\delta/2}p_T(-v)\,dv\\
 &= {2\over\delta}\int_0^{\delta/2}p_T(u)\,du\\
 &\ge {1\over4\sqrt2}\left(1+\log{1\over\delta}\right).
\end{aligned}                                             \tag{2.13}
\]

Hence

\[
\boxed{\ \|p_{Q_\delta}\|_\infty
\ge {1\over4\sqrt2}\left(1+\log{1\over\delta}\right)
\longrightarrow\infty.\ }                               \tag{2.14}
\]

### 2.3 Yet the gradient data become better, not worse

The three derivatives used in the r23 Schur-gradient theorem are

\[
(\partial_SQ_\delta,\partial_YQ_\delta,\partial_ZQ_\delta)
=(2S,2Y,-2Z).                                             \tag{2.15}
\]

Because `S,Y,Z` are genuinely independent here, this triple has product density and

\[
\boxed{\
\|p_{(\partial_SQ_\delta,\partial_YQ_\delta,\partial_ZQ_\delta)}\|_\infty
={\delta\over8}.\ }                                      \tag{2.16}
\]

Moreover the full gradient in `(S,R,Y,Z)` is

\[
\nabla Q_\delta=(2S,1,2Y,-2Z),                            \tag{2.17}
\]

so pointwise `||nabla Q_delta||_2>=1` and therefore

\[
\boxed{\ \mathbb E\|\nabla Q_\delta\|_2^{-1}\le1.\ }   \tag{2.18}
\]

Thus a uniformly bounded reciprocal-gradient budget — even accompanied by a gradient-triple density cap tending to zero — does not control a single level trace.

We have proved the following proof-interface obstruction.

### Proposition `QFORM-BLOCKPRODUCT-PARABOLIC-SHELL-GRADIENT-TRACE-FAIL-v1`

There is a family of grouped laws satisfying

- `(S,R)` independent of `Y` independent of `Z`;
- `||h_(S,R)||_infinity<=1`;
- all four one-dimensional coordinate marginals have density cap at most one;
- the exact Schur normal form (2.6) has `|a det B|=1`;
- `||p_(partial_S Q,partial_Y Q,partial_Z Q)||_infinity<=1/8` and in fact tends to zero;
- `E||grad Q||^(-1)<=1`;

but `||p_Q||_infinity -> infinity`.

Therefore the r23 theorem cannot be upgraded to a pointwise trace through these summary quantities alone.

## 3. The same obstruction is visible as a tangent projection spike

The parabolic strip (2.1) is incompatible with a dimension-free cap on all adapted linear projections. This supplies one concrete invariant that true product projections have and the engineered shell does not.

Put

\[
s_0={1\over2\delta},\qquad
N=\sqrt{1+\delta^{-2}},\qquad
U={\delta^{-1}S+R\over N}.                               \tag{3.1}
\]

Write `S=s_0+x` and `e=R+S^2`. Restrict to

\[
|x|\le{\sqrt\delta\over2},\qquad
|e-x^2|\le{\delta\over4}.                               \tag{3.2}
\]

This set lies inside (2.1), has probability mass

\[
\sqrt\delta\,{\delta\over2}={\delta^{3/2}\over2}.       \tag{3.3}
\]

Since `delta^{-1}=2s_0`,

\[
\delta^{-1}S+R=s_0^2-x^2+e,                              \tag{3.4}
\]

which varies by at most `delta/2` on (3.2). Hence `U` lies in an interval of length at most `delta/(2N)`. By averaging its one-dimensional density over this interval,

\[
\boxed{\ \|p_U\|_\infty\ge N\sqrt\delta\ge\delta^{-1/2}.\ } \tag{3.5}
\]

So the parabolic shell has a large tangent linear projection. A genuine normalized one-dimensional linear projection of independent cap-one inputs enjoys the standard universal projection-density cap, so this particular shell cannot be substituted for such a product projection.

However, the next section shows that **linear projection caps by themselves still do not solve the coarea problem**.

## 4. Even caps for every one-dimensional projection are insufficient for an arbitrary joint law

Fix `R>=1` and define

\[
r_R=\left(R^3+{3\over4\pi}\right)^{1/3}.                \tag{4.1}
\]

Let `X in R^3` have density

\[
\rho_R(x)=\mathbf1_{\{R\le|x|\le r_R\}}.                \tag{4.2}
\]

Because

\[
{4\pi\over3}(r_R^3-R^3)=1,                              \tag{4.3}
\]

this is a probability density with `||rho_R||_infinity=1`.

By rotational symmetry, for every unit vector `theta`, the density of `theta dot X` is

\[
p_{\theta\cdot X}(z)
=\pi\big[(r_R^2-z^2)_+-(R^2-z^2)_+\big],                \tag{4.4}
\]

and hence

\[
\|p_{\theta\cdot X}\|_\infty=\pi(r_R^2-R^2).           \tag{4.5}
\]

Using

\[
r_R^2-R^2
=(r_R^3-R^3){r_R+R\over r_R^2+r_RR+R^2}                \tag{4.6}
\]

and, for `x>=1`, `(x+1)/(x^2+x+1)<=2/3`, we obtain

\[
\boxed{\ \sup_{|\theta|=1}\|p_{\theta\cdot X}\|_\infty
\le {1\over2R}.\ }                                      \tag{4.7}
\]

Thus every one-dimensional linear projection becomes *more* anti-concentrated as `R` grows.

Now take the quadratic form

\[
q(x)=|x|^2.                                               \tag{4.8}
\]

Coarea gives exactly

\[
p_{q(X)}(t)=2\pi\sqrt t\,
\mathbf1_{[R^2,r_R^2]}(t),                               \tag{4.9}
\]

so

\[
\boxed{\ \|p_{q(X)}\|_\infty=2\pi r_R\ge2\pi R\to\infty.\ } \tag{4.10}
\]

At the same time `nabla q(X)=2X`; its three-dimensional density is at most `1/8`, and

\[
\mathbb E\|\nabla q(X)\|_2^{-1}\le{1\over2R}.            \tag{4.11}
\]

Therefore:

### Proposition `QFORM-ALL-LINEAR-PROJECTION-CAPS-STILL-INSUFFICIENT-v1`

For arbitrary three-dimensional joint densities, even the simultaneous collection

\[
\|\rho\|_\infty\le1,
\qquad
\sup_{|\theta|=1}\|p_{\theta\cdot X}\|_\infty\le1,
\qquad
\|p_{\nabla q(X)}\|_\infty\le1,
\qquad
\mathbb E\|\nabla q(X)\|^{-1}\le1                     \tag{4.12}
\]

cannot imply a universal bound for `||p_(q(X))||_infinity`.

Again, this spherical shell is not a product law and is not a QFORM counterexample. It proves that the required extra invariant is stronger than one-dimensional linear anti-concentration.

## 5. Exact missing factor after r23

The two constructions isolate the next B05 obligation much more sharply.

**`QFORM-PRODUCT-PROJECTION-CURVED-SHELL-EXCLUSION-v1`.** In the grouped packet arising from actual independent original coordinates, use the fact that `(S,R)` is a genuine **linear image of a product measure with its original-coordinate coefficient provenance**, together with the independent scalar banks `Y,Z`, to rule out concentration of mass in a thin translated quadratic shell at the level-set scale. The desired conclusion is a uniform interval estimate

\[
\Pr\{Q\in[t,t+\varepsilon]\}
\le C\,\mu^{-1/3}\varepsilon                            \tag{5.1}
\]

(or an equivalent coarea trace), uniformly in the pair condition number and all affine terms.

The next proof cannot depend only on any of the following already-insufficient summaries:

\[
\|h_{S,R}\|_\infty,\quad
\|p_S\|_\infty,\quad
\|p_R\|_\infty,\quad
\sup_\theta\|p_{\theta\cdot(S,R)}\|_\infty,\quad
\|p_{\text{gradient triple}}\|_\infty,\quad
\mathbb E\|\nabla Q\|^{-1}.                             \tag{5.2}
\]

A viable coarea proof must retain a genuinely multilinear/product-provenance quantity — for example an original-coordinate Brascamp--Lieb/fractional-trace inequality or an interval estimate before the physical product banks are compressed to an arbitrary joint law.

This is compatible with the current correction stream: arbitrary-joint shell/coarea bounds and conditional-density-moment gates are already known false. The present run shows precisely why the new kappa-free gradient theorem, although useful, does not by itself bypass that correction.

## 6. Required designated-partner application

The completed designated partner result is account04/B05 r2:

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`.

It proves, for an exact physical slope class of mass `m_*>0`,

\[
\|p_Q\|_\infty<51.6(\mu m_*)^{-1/3}.                    \tag{6.1}
\]

Applying it to the concrete branch

\[
\mu\ge1,\qquad m_*\ge{1\over4},                          \tag{6.2}
\]

gives the actual numerical inequality

\[
\boxed{\ \|p_Q\|_\infty
<51.6\,4^{1/3}
=81.909894\ldots<81.91.\ }                               \tag{6.3}
\]

Thus the dominant exact-slope branch is already paid by the designated partner. The obstruction in Sections 2--5 concerns the complementary attempt to replace missing exact slope mass by only ambient gradient/coarea summaries.

## 7. Scope, corrections, and next step

**Proved this run:**

1. `QFORM-BLOCKPRODUCT-PARABOLIC-SHELL-GRADIENT-TRACE-FAIL-v1`, an explicit Schur-normal-form counterexample to the inference from grouped density caps + gradient-density/reciprocal-gradient control to a pointwise output-density bound;
2. the tangent-projection lower bound (3.5), identifying one way that the engineered curved shell violates true product-projection structure;
3. `QFORM-ALL-LINEAR-PROJECTION-CAPS-STILL-INSUFFICIENT-v1`, showing that even all one-dimensional projection caps do not rescue an arbitrary-joint coarea theorem;
4. an equation-level application of account04/B05 r2 yielding (6.3).

**Not proved:**

- the interval estimate (5.1) for genuine product projections;
- the unrestricted exact-rank-three or higher-rank theorem;
- the full QFORM conjecture;
- the full continuity conclusion.

The decisive next mechanism is **not** to strengthen the ambient reciprocal-gradient estimate. It is to retain original-coordinate product structure through the curved shell trace, before replacing a bank by an arbitrary joint projected density. This should be attacked through a product-measure fractional trace/Brascamp--Lieb inequality or a direct interval estimate in the original coordinates.

No Gaussian, moment, compact-support, connected-support, log-concavity, or post-rotation independence assumption is used in any positive statement about the target class here. The two negative constructions are explicitly labelled as proof-interface counterexamples, not target counterexamples.
