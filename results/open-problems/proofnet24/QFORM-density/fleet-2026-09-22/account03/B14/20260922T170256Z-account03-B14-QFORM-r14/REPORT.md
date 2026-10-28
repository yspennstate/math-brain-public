# account03/B14 — singular-payoff localization and translation quotient

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Run:** `20260922T170256Z-account03-B14-QFORM-r14`  
**Status:** `TARGET_LEVEL_SUPPORTING_LEMMA / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and source state

The target remains the full arbitrary-dimensional statement: for independent real coordinates with densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove one universal finite `C` such that

\[
   \Pr\{X^TAX\in I\}\le C|I|
\]

for every interval `I`, or give a genuine counterexample. Continuity is separate and is not proved here.


The completed required partner input is account04/B14:

`yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`.

It proves the one-coordinate bathtub extremization for bounded payoffs and the no-loss approximation of measurable unit sets by compact finite unions of intervals. The present run extends that localization to *unbounded singular payoffs*, which the previous TV argument by itself did not cover.

A second compatible input is the completed interactive rank-two affine half-Riesz theorem:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

Its proved scope is

\[
 \sup_t\mathbb E\left| (U^TX)^T\Lambda(U^TX)+b^TX-t\right|^{-1/2}
 \le 128|\det\Lambda|^{-1/4}
\]

for any two-column orthonormal `U`, invertible symmetric `Lambda`, arbitrary original-coordinate affine vector `b`, and independent cap-one inputs. If `b` belongs to the quadratic range, the constant improves to `16 sqrt(30)`.

## 2. Main theorem: exact localization for arbitrary nonnegative payoffs

Let `D_n` be the class of product probability laws

\[
 d\mu(x)=\prod_{i=1}^n f_i(x_i)\,dx,
 \qquad 0\le f_i\le1,\quad \int f_i=1.
\]

Let `E_n` be the subclass whose marginals are `1_{E_i} dx` with measurable `|E_i|=1`, and let `F_n` be the further subclass in which every `E_i` is a compact finite union of intervals.

### Theorem 2.1 — singular-payoff extreme-product localization

For every measurable function

\[
 K:\mathbb R^n\to[0,\infty],
\]

possibly unbounded and possibly infinite on a null or positive-measure set,

\[
\boxed{
 \sup_{\mu\in D_n}\int K\,d\mu
 =\sup_{\mu\in E_n}\int K\,d\mu
 =\sup_{\mu\in F_n}\int K\,d\mu
 }
\]

as an equality in `[0,+infinity]`.

The same equality holds after an arbitrary outer supremum over a parameter family `K_theta`; no uniformity in `theta` is lost.

### Proof

The inclusions `F_n subset E_n subset D_n` give one direction. Fix `mu in D_n`, a truncation level `M<infinity`, and `epsilon>0`, and put

\[
 K_M=\min(K,M).
\]

Then `0<=K_M<=M`.

Hold all marginals except the first fixed. Conditional integration gives a measurable payoff `g_1(x_1)` with `0<=g_1<=M`. Divide by `M` and apply the account04/B14 bathtub lemma: replacing `f_1` by an indicator `1_{E_1}`, `|E_1|=1`, cannot decrease the expectation of `K_M`. Repeat this coordinate by coordinate. Thus there is a measurable extreme product `nu_E in E_n` with

\[
 \int K_M\,d\nu_E\ge \int K_M\,d\mu.
\]

Now use the partner finite-fragment approximation. For each `E_i` choose a compact finite union `F_i` with `|F_i|=1` and

\[
 \sum_i |E_i\triangle F_i|<\frac{2\epsilon}{M}
\]

(with the statement trivial if `M=0`). For the associated product law `nu_F`,

\[
 d_{TV}(\nu_E,\nu_F)
 \le \frac12\sum_i |E_i\triangle F_i|
 <\frac{\epsilon}{M}.
\]

Because `0<=K_M<=M`,

\[
 \left|\int K_M\,d\nu_E-\int K_M\,d\nu_F\right|
 \le M d_{TV}(\nu_E,\nu_F)<\epsilon.
\]

Hence

\[
 \sup_{\nu\in F_n}\int K\,d\nu
 \ge \sup_{\nu\in F_n}\int K_M\,d\nu
 \ge \int K_M\,d\mu-\epsilon.
\]

Let `epsilon downarrow 0` and then `M to infinity`. Monotone convergence gives

\[
 \sup_{\nu\in F_n}\int K\,d\nu\ge \int K\,d\mu.
\]

Taking the supremum over `mu in D_n` proves the theorem.

### Quantitative form

For every fixed bounded truncation `K_M` and every product law `mu in D_n`, there is a compact finite-fragment product `nu in F_n` satisfying

\[
 \int K_M\,d\nu\ge \int K_M\,d\mu-\epsilon,
\]

and it is enough to approximate the successive bathtub sets so that

\[
 \sum_i |E_i\triangle F_i|<2\epsilon/M.
\]

No support diameter, moment, connectedness, fragment-count or separation bound appears.

## 3. Half-Riesz corollary: the singular kernel localizes with no loss

For a real symmetric matrix `B`, vector `c`, exponent `alpha>0`, and parameter `t`, define

\[
 K_{B,c,t,\alpha}(y)=|y^TBy+c^Ty-t|^{-\alpha},
\]

with value `+infinity` on the zero set. Theorem 2.1 gives the exact equality

\[
\boxed{
 \sup_{\mu\in D_m}\sup_t
 \mathbb E_\mu |Y^TBY+c^TY-t|^{-\alpha}
 =
 \sup_{\mu\in F_m}\sup_t
 \mathbb E_\mu |Y^TBY+c^TY-t|^{-\alpha}.
}
\]

This is the localization statement needed by scalar-Schur arguments: total-variation localization can now be applied *after truncating the singular kernel*, and monotone convergence removes the truncation without any moment assumption.

For `alpha=1/2`, a universal half-Riesz estimate may therefore be proved entirely on compact finite-fragment product indicators, provided the constant is independent of fragment count, positions and separations.

## 4. Exact translation quotient for affine perturbations

Define the worst-case singular-potential constant

\[
 \mathcal H_\alpha(B,c)
 =\sup_{\mu\in D_m}\sup_t
   \mathbb E_\mu |Y^TBY+c^TY-t|^{-\alpha}.
\]

For every translation vector `s`, the change of variables `Y=Z+s` gives

\[
 (Z+s)^TB(Z+s)+c^T(Z+s)
 =Z^TBZ+(c+2Bs)^TZ+\mathrm{constant}.
\]

Translation is a bijection of `D_m` and also of the measurable-unit-set and compact-finite-fragment classes. The outer supremum over `t` absorbs the additive constant. Therefore

\[
\boxed{\mathcal H_\alpha(B,c)=\mathcal H_\alpha(B,c+2Bs).}
\]

Consequently `mathcal H_alpha(B,c)` depends only on the coset of `c` modulo `Range(B)`. Because `B` is symmetric, this is equivalently only the kernel component

\[
 P_{\ker B}c.
\]

In particular:

* if `B` is invertible, every affine term can be removed from the worst-case constant by translating the input laws;
* if `c in Range(B)`, the affine term is similarly removable;
* if `B` is singular, only the component of `c` in `ker(B)` is an essential affine obstruction.

This is an exact statement about the supremum over the target law class. It does **not** assert that a fixed individual input law is invariant under deleting its affine term.

Applied to the current rank-two theorem `B=U Lambda U^T`, the only genuinely essential arbitrary affine component is the projection of `b` onto `ker(B)=Range(U)^perp`. The completed theorem's stronger constant `16 sqrt(30)` corresponds precisely to the case where this kernel component vanishes.

## 5. Scalar-Schur density bridge with exact singular localization

Consider a general quadratic-affine expression in one physical coordinate `x` and the remaining vector `y`:

\[
 Q(x,y)=a x^2+2x u^Ty+d_0x+y^TBy+d^Ty+c,
 \qquad a\ne0.
\]

Completing the square gives the exact identity

\[
 Q(x,y)=a\left(x+\frac{u^Ty+d_0/2}{a}\right)^2+S(y),
\]

where

\[
 S(y)=y^T\left(B-\frac{uu^T}{a}\right)y
 +\left(d-\frac{d_0}{a}u\right)^Ty
 +c-\frac{d_0^2}{4a}.
\]

For each fixed `y`, the cap `f_x<=1` and the two inverse branches of the square map give the conditional density estimate

\[
 p_{Q\mid Y=y}(t)
 \le |a|^{-1/2}|t-S(y)|^{-1/2}.
\]

Indeed, whenever `(t-S(y))/a>0`, the two roots each contribute at most

\[
 \frac1{2\sqrt{|a|\,|t-S(y)|}},
\]

and otherwise there is no contribution. Integrating in `y` yields

\[
\boxed{
 p_Q(t)\le |a|^{-1/2}
 \mathbb E|t-S(Y)|^{-1/2}.
}
\]

Therefore, if the Schur quadratic-affine remainder has half-Riesz constant at most `K`, then

\[
 \|p_Q\|_\infty\le K/\sqrt{|a|}.
\]

By Theorem 2.1, proving that `K` for all arbitrary cap-one product laws of `Y` is **exactly equivalent** to proving it for compact finite-fragment indicator products. No localization penalty, no support diameter, and no moment term enters this scalar-Schur step.

This pays a previously implicit interface: the singular half-Riesz quantity used in the proof-first scalar-pivot route is now compatible with the finite-fragment localization, even though it is unbounded and TV convergence alone does not directly control it.

## 6. Actual inequality using the completed rank-two result

Suppose the Schur remainder quadratic matrix has exact rank two,

\[
 C=B-uu^T/a=U\Lambda U^T,
\]

with `U^TU=I_2` and invertible symmetric `Lambda`. Its affine vector is arbitrary. The completed rank-two theorem gives

\[
 \sup_t\mathbb E|S(Y)-t|^{-1/2}
 \le128|\det\Lambda|^{-1/4}.
\]

Hence the preceding scalar-Schur inequality gives

\[
\boxed{
 \|p_Q\|_\infty
 \le128 |a|^{-1/2}|\det\Lambda|^{-1/4}.
}
\]

If the Schur affine vector lies in `Range(C)`, equivalently has zero kernel component, the improved source constant gives

\[
\boxed{
 \|p_Q\|_\infty
 \le16\sqrt{30}\, |a|^{-1/2}|\det\Lambda|^{-1/4}.
}
\]

For a physical 3-by-3 block with Schur complement `C`, `det A_block=a det C`; thus the first bound can also be written

\[
 128\,|a\,\det A_{block}|^{-1/4}.
\]

This is not a full solution because the bare three-large-eigenvalue hypothesis does not force a uniformly good physical 3-by-3 block or a uniformly large outer pivot.

## 7. Why this is not already contained in the prior localization runs

The previous account03/B14 law-level convex-mixture theorem worked in total variation and was sufficient for interval indicators and bounded test functions. The half-Riesz kernel

\[
 |q-t|^{-1/2}
\]

is unbounded, so TV convergence alone does not justify passage of its expectation. The present proof uses bounded truncations, partner bathtub extremization, quantitative finite-fragment approximation, and monotone convergence. This closes that exact technical gap.

The result also identifies the translation-invariant affine quotient `c mod Range(B)`, which is useful in current rank-two and Schur synthesis: range-affine terms are bookkeeping translations, while kernel-affine terms are genuine.

## 8. Remaining implication toward full QFORM

Full QFORM is still OPEN. The present run does not solve the zero/near-zero physical-pivot or arbitrary higher-rank Schur-remainder branches.

A now-clean proof-first obligation is:

> establish a dimension-free half-Riesz bound for the relevant higher-rank Schur remainder, with arbitrary kernel-affine component, on compact finite-fragment product indicators; by Theorem 2.1 that bound automatically extends with the identical constant to all cap-one product laws and arbitrary fragment translations.

Alternatively a structural reduction may show that every matrix outside the ridge-certified diffuse branch has a physical pivot whose Schur remainder falls into a completed grouped/rank-two family. The singleton-plus-two-banks corrections rule out several naive minor/rank-cut dichotomies, so that structural step remains nontrivial.

Continuity of the final output density is not proved by this argument; the scalar-Schur estimate gives existence of an essentially bounded density only.

## 9. Computation / algebra check

A direct symbolic expansion verified the displayed square-completion identity exactly. A deterministic 1000-sample floating-point regression over random signs, pivots, couplings, affine terms and points gave maximum absolute reconstruction error `5.58e-14`, consistent with floating-point roundoff. This is diagnostic only; the proof is algebraic.

## 10. Source pins

- Fresh programme controls initially read at `yspennstate/math-research-brain@1836efdb710f84dd601889af6e09992e755e1cd1`; pre-publication main refresh observed `ba912a492619ee1a19dacff41a2ffefa1e1556aa` before the final control/correction reread.
- Required partner theorem: `yspennstate/math-open-problems@8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`, exact account04/B14 report path stated above.
- Rank-two affine half-Riesz theorem: `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, exact interactive report path stated above.
- The correction inbox was consumed before derivation and will be refreshed again before the handoff/receipt.

No scheduler mutation, task creation, email/Drive action, public release, remote workflow, paid model/API/Codex call, permission expansion or cross-account authentication is part of this result.
