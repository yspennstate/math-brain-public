SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-23T08:55:55Z.
attacking: balanced positive-kernel modes — replace the arbitrary output center by an exact Laplace-mode one-sided identity and a compact tent-mode two-sided balance condition.

# fleet03/B15 auto17 — balanced-mode regularity compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Absolute continuity and regularity  
**Run:** `20260923T085555Z-fleet03-B15-qform-auto17`  
**Status:** `ESSENTIAL_STEP_APPLIED / BALANCED_MODE_ONE_SIDED_NORMAL_FORM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and result

For independent real `X_i` with probability densities `0<=f_i<=1` and real symmetric `A`, put

\[
Q_A=X^TAX,
\]

and let `s_3(A)` denote the third largest singular value.  It is convenient to use the homogeneous sharp constant

\[
C_*:=\sup_{\operatorname{rank}A\ge3}
  s_3(A)\,\|p_{Q_A}\|_\infty .
\tag{1.1}
\]

This is finite exactly when the owner's conjecture is true; normalizing by `s_3(A)` converts (1.1) to the original `s_3(A)>=1` formulation.

The full conjecture remains **OPEN**.  The new result is an exact restriction of the only center that needs to be studied.

### Theorem A — exact one-sided Laplace-mode normal form

Let

\[
\ell(u)=\frac12e^{-|u|},\qquad
L_A(y)=\mathbb E\,\ell(Q_A-y).
\]

For every target instance, `L_A` is continuous, vanishes at infinity, and has a global maximizer.  Let `\mathcal M_L(A)` be the set of its global maximizers.  Then

\[
\boxed{
C_*=\sup_{A,f}\ s_3(A)\max_y L_A(y)
}
\tag{1.2}
\]

and, because every target law is atomless, every `y_* in \mathcal M_L(A)` satisfies the exact balance identity

\[
\boxed{
\int_{(y_*,\infty)}e^{-(q-y_*)}\,d\mu_A(q)
=\int_{(-\infty,y_*)}e^{-(y_*-q)}\,d\mu_A(q)
=L_A(y_*).
}
\tag{1.3}
\]

Consequently

\[
\boxed{
C_*=\sup_{A,f}\ \sup_{y_*\in\mathcal M_L(A)}
 s_3(A)
 \int_{(y_*,\infty)}e^{-(q-y_*)}\,d\mu_A(q),
}
\tag{1.4}
\]

and the same formula holds with the left side of the mode.  Thus the full conjecture is **exactly equivalent, with no constant loss**, to a one-sided exponentially weighted estimate, but only at centers satisfying the opposite-side balance (1.3).

This directly removes the completely free output center from the remaining positive-kernel problem.

### Theorem B — compact tent-mode balance

Let

\[
\tau(u)=(1-|u|)_+,
\qquad T_A(y)=\mathbb E\,\tau(Q_A-y),
\]

and let `\mathcal M_T(A)` be its global maximizers.  Again

\[
\boxed{
C_*=\sup_{A,f}s_3(A)\max_y T_A(y).
}
\tag{1.5}
\]

For every `y_* in \mathcal M_T(A)`, atomlessness gives

\[
\boxed{
\Pr(y_*-1<Q_A<y_*)
=\Pr(y_*<Q_A<y_*+1).
}
\tag{1.6}
\]

Define the balanced one-sided unit-window constant

\[
B_*:=\sup_{A,f}\sup_{y_*\in\mathcal M_T(A)}
  s_3(A)\Pr(y_*<Q_A<y_*+1).
\tag{1.7}
\]

Then

\[
\boxed{B_*\le C_*\le2B_*.}
\tag{1.8}
\]

Hence finiteness of the full QFORM constant is equivalent, within factor two, to bounding **one adjacent unit interval at a tent mode whose opposite adjacent interval has exactly the same mass**.  This improves the previous Gaussian-mode compiler factor `<2.073` and replaces its infinite-tail posterior condition by the compact condition (1.6).

The significance is structural, not a claim that (1.7) is already bounded.  The live corrections show that arbitrary-center interval/fiber arguments can fail.  Equations (1.3) and (1.6) show that a full proof never needs an arbitrary center: the relevant center can be required to carry an exact self-balancing condition.

## 2. Absolute continuity needed for the mode derivatives

The mode identities require that the output has no atoms.  This part is unconditional and does not use the disputed bounded-density steps.

Let `A!=0` and `q(x)=x^TAx`.  For a Lebesgue-null set `N subset R`, set

\[
E_m=\{x:|x|\le m,\ |\nabla q(x)|\ge1/m\}.
\]

By coarea,

\[
\int_{E_m\cap q^{-1}(N)}|\nabla q(x)|\,dx
=\int_N \mathcal H^{n-1}(E_m\cap q^{-1}(t))\,dt=0.
\]

Thus `Leb(E_m cap q^{-1}(N))=0`.  Outside `union_m E_m`, the only possible non-null obstruction is the critical set `ker A`, which is a proper linear subspace and therefore null.  Hence `q^{-1}(N)` is null.  Since the input product law is absolutely continuous with respect to Lebesgue measure, `Q_A` is absolutely continuous.  In particular `\mu_A({y})=0` for every `y`.

This proves only absolute continuity, not the universal height bound.

## 3. One-scale kernel identity

The completed assigned partner fleet04/B15 proved the Gaussian heat-height theorem:

\[
\sup_{\varepsilon>0,y}
(\mu*\gamma_\varepsilon)(y)=\|p_\mu\|_\infty,
\tag{3.1}
\]

with `+infinity` if no bounded density exists.  Its canonical source is

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T211430Z-fleet04-B15-heat-regularity-r4/REPORT.md`.

I apply it here to an actual equality for the sharp target constant.

For a nonnegative probability kernel `K` with the standard dilates

\[
K_\varepsilon(u)=\varepsilon^{-1}K(u/\varepsilon),
\]

both `K=ell` and `K=tau` are approximate identities.  Every fixed target instance has an individually bounded `C_0` density by the completed B15 regularity chain, so

\[
\sup_{\varepsilon>0,y}(p_Q*K_\varepsilon)(y)=\|p_Q\|_\infty.
\tag{3.2}
\]

Now use scalar homogeneity.  If `Q_A=X^TAX` and `A'=A/\varepsilon`, then

\[
Q_{A'}=Q_A/\varepsilon,
\qquad s_3(A')=s_3(A)/\varepsilon,
\]

and

\[
s_3(A)(p_{Q_A}*K_\varepsilon)(y)
=s_3(A')\,\mathbb E K(Q_{A'}-y/\varepsilon).
\tag{3.3}
\]

Taking the supremum over all rank-at-least-three matrices, all product laws, all scales and all centers gives

\[
\boxed{
C_*=\sup_{A,f}s_3(A)\sup_y\mathbb E K(Q_A-y)
}
\tag{3.4}
\]

for `K=ell` and `K=tau`.

Combining the partner Gaussian identity (3.1) with (3.4) gives the actual target-level equality

\[
\boxed{
\sup_{A,f}s_3(A)\sup_y\mathbb E\gamma_1(Q_A-y)
=
\sup_{A,f}s_3(A)\sup_y\frac12\mathbb E e^{-|Q_A-y|}
=
\sup_{A,f}s_3(A)\sup_y\mathbb E(1-|Q_A-y|)_+
=C_*.
}
\tag{3.5}
\]

Thus the partner heat theorem and the balanced-mode kernels encode exactly the same optimal universal constant.

## 4. Proof of Theorem A

For a fixed target law `\mu`, put

\[
L(y)=\frac12\int e^{-|q-y|}\,d\mu(q).
\]

Since `ell in C_0` and `\mu` is finite, `L in C_0`; hence a global maximizer `y_*` exists.  Since `\mu` is atomless, dominated differentiation gives

\[
L'(y)=\frac12\left[
\int_{(y,\infty)}e^{-(q-y)}\,d\mu(q)
-
\int_{(-\infty,y)}e^{-(y-q)}\,d\mu(q)
\right].
\tag{4.1}
\]

At a global maximizer `L'(y_*)=0`.  Write

\[
R_*:=\int_{(y_*,\infty)}e^{-(q-y_*)}\,d\mu(q),
\qquad
J_*:=\int_{(-\infty,y_*)}e^{-(y_*-q)}\,d\mu(q).
\]

Equation (4.1) gives `R_*=J_*`, while by definition

\[
L(y_*)=\frac12(R_*+J_*).
\]

Therefore

\[
R_*=J_*=L(y_*),
\]

which proves (1.3).  Combining this identity with the fixed-scale equality (3.4) for `K=ell` proves (1.4).

There is also an absolutely convergent Fourier representation

\[
L_A(y)=\frac1{2\pi}\int_{\mathbb R}
 e^{-ity}\frac{\phi_A(t)}{1+t^2}\,dt,
\tag{4.2}
\]

because `\widehat\ell(t)=1/(1+t^2)` and `|\phi_A(t)|<=1`.  Thus the exact one-sided physical-space mode formulation does not require the refuted law-uniform pointwise oscillatory decay or an undamped Wiener norm.

## 5. Proof of Theorem B

For a fixed target law define

\[
T(y)=\int(1-|q-y|)_+\,d\mu(q).
\]

Again `T in C_0` and has a global maximizer.  Because `\mu` is atomless, differentiation of the tent kernel gives

\[
T'(y)
=
\Pr(y<Q<y+1)-\Pr(y-1<Q<y).
\tag{5.1}
\]

At any global maximizer `y_*`, (5.1) is zero, proving the exact adjacent-window balance (1.6).

Let the common mass be

\[
m_*:=\Pr(y_*<Q<y_*+1)=\Pr(y_*-1<Q<y_*).
\]

Since `0<=tau<=1` and its support is `[-1,1]`,

\[
T(y_*)\le\Pr(|Q-y_*|<1)=2m_*.
\tag{5.2}
\]

Therefore (3.4) with `K=tau` gives

\[
C_*\le2B_*.
\tag{5.3}
\]

Conversely, every target instance has an individually bounded density and

\[
m_*\le\|p_Q\|_\infty
\]

because the interval has length one.  Hence

\[
B_*\le C_*.
\tag{5.4}
\]

Equations (5.3)-(5.4) prove (1.8).

The tent Fourier multiplier is

\[
\widehat\tau(t)=\left(\frac{\sin(t/2)}{t/2}\right)^2\in L^1(\mathbb R),
\tag{5.5}
\]

so this compact balanced-center formulation also has an absolutely convergent Fourier interface for every target law.

## 6. Relation to the previous Gaussian-mode compiler

The previous B15 run used Gaussian heat modes.  At a unit Gaussian heat mode, the posterior residual `U=Q-y_*` satisfies

\[
\mathbb E e^{vU}\le e^{v^2/2},
\]

and the resulting fixed-radius centered small-ball compiler had factor `<2.073`.

The present tent formulation improves the purely quantitative compiler to

\[
B_*\le C_*\le2B_*,
\]

while replacing a global subgaussian posterior condition by the compact exact balance

\[
\Pr(y_*-1<Q<y_*)=\Pr(y_*<Q<y_*+1).
\]

The Laplace formulation is stronger in another direction: it has **zero constant loss** and reduces the target to either one-sided exponentially weighted contribution, because the two sides are exactly equal at a Laplace mode.

These are not universal density bounds by themselves.  They are center restrictions that a future coarea, grouped-coordinate, ridge, or fractional-trace argument may exploit before taking any fiber supremum or reciprocal small-minor cost.

## 7. First unpaid implication after this run

A full proof now may target either of the following strictly restricted statements.

### Zero-loss weighted target

For every target instance and every Laplace mode `y_*`, prove

\[
\boxed{
\int_{(y_*,\infty)}e^{-(q-y_*)}\,d\mu_A(q)
\le\frac{C}{s_3(A)}.
}
\tag{7.1}
\]

Because of (1.4), this is **exactly** the full conjecture with the same constant.

### Compact target, factor two

For every target instance and every tent mode `y_*`, prove

\[
\boxed{
\Pr(y_*<Q_A<y_*+1)\le\frac{C}{s_3(A)},
\qquad
\Pr(y_*-1<Q_A<y_*)=\Pr(y_*<Q_A<y_*+1).
}
\tag{7.2}
\]

Then `C_*<=2C`.  Conversely, the full conjecture with constant `C_*` implies (7.2) with `C=C_*`.

The live correction that an arbitrary center can translate a dangerous interval into a punctured shell therefore does not apply unchanged to (7.2): the center is constrained by an equal-mass interval on the opposite side.  Whether the product-preserving two-sheet/ridge geometry can exploit this balance is the next mathematical question.

## 8. Scope and integrity

No Gaussianity, moments, centering, log-concavity, compact support, connected support, or independence after spectral rotation is assumed.  The only properties used are the original product absolute continuity, scalar homogeneity of the quadratic form, positivity of the kernels, and the completed fleet04/B15 heat-height theorem.  No pointwise van-der-Corput estimate, arbitrary-joint coarea bound, conditional density cap, or fiber-supremum argument is used.

The fixed-instance `C_0` theorem is used only to justify the already-completed target regularity endpoint and the easy inequality `m_*<=||p_Q||_infty`; the new balanced-mode identities themselves require only atomlessness.

The full universal constant remains open.