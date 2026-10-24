# QFORM B01 — signed Fejer replacement and conditional definite-plane gate

Run: `20260922T141507Z-b01-qform-fejer-r1`  
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
Initial control commit: `e41a73e3fed32b4c1e834fd3e0b918d3d3682bf7`; pre-publication refresh: `1d935d68cdb77685d8bb95d79638862585bc34ca`  
Status: `ESSENTIAL_STEP_APPLIED`; the full conjecture remains `OPEN`; execution label `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and the correction that must survive

The target is the full arbitrary-product-law quadratic-form conjecture: the coordinates are independent, each density is at most one, the real symmetric matrix has at least three eigenvalues of modulus at least one, and the desired density bound is universal in the dimension, matrix and laws. Rotating the inputs is not allowed because it destroys independence.

The false pointwise Fresnel claim remains explicitly refuted. Fix `s != 0` and `delta > 0`. The set

    E(s,delta)={x: dist(s x^2,2 pi Z)<=delta}

has infinite Lebesgue measure. Choose a measurable subset `E` of measure one and take `f=1_E`. Then

    Re int exp(i s x^2) f(x) dx >= cos(delta).

Thus no law-uniform positive power decay can hold at every frequency, even in one dimension; three independent copies also refute the proposed pointwise `|t|^{-3/2}` product envelope. The newer correction `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1` must also survive: even a bounded continuous quadratic output can have a characteristic function outside `L^1`. Accordingly, every result below keeps the signed time cancellation before taking an absolute value.

## 2. Exact signed Fejer interface

Let `mu` be any probability law on the real line, with characteristic function

    phi(t)=int exp(i t x) dmu(x).

For `T>0` define

    F_T(u)=(1/(2 pi)) int_{-T}^T (1-|t|/T) exp(i t u) dt
          =(T/(2 pi)) (sin(Tu/2)/(Tu/2))^2

and

    D_T mu(y)=int F_T(x-y) dmu(x).

The Fourier formula is

    D_T mu(y)
    =(1/(2 pi)) int_{-T}^T (1-|t|/T)
       Re(exp(-i t y) phi(t)) dt.                    (2.1)

The right side is phase-sensitive and may contain large positive and negative pieces, but its total is nonnegative because it equals the convolution with `F_T`.

### Theorem 2.1 (exact bounded-density equivalence)

The following are equivalent for a finite probability law `mu` and a constant `C`:

1. `mu` has a density `p` with `||p||_infinity<=C`.
2. `D_T mu(y)<=C` for every `T>0` and every real `y`.

Moreover, whenever `mu` has a bounded density,

    ||p||_infinity = sup_{T>0,y in R} D_T mu(y).       (2.2)

#### Proof

The kernels `F_T` are nonnegative and have integral one. If `dmu=p dx` and `p<=C`, then `D_T mu=p*F_T<=C`.

Conversely, suppose `D_T mu<=C`. The absolutely continuous probability measures `(D_T mu)(y)dy` converge weakly to `mu` as `T` tends to infinity, because `F_T` is an approximate identity. For every nonnegative compactly supported continuous `g`,

    int g dmu = lim_T int g(y) D_T mu(y) dy
               <= C int g(y) dy.

Hence `mu<=C dy`, so `mu` has a density at most `C`. Finally, if `p` is bounded, at every Lebesgue point `y` one has `(p*F_T)(y)->p(y)`. Taking Lebesgue points arbitrarily close to the essential supremum proves the reverse inequality in (2.2).

This is the correct averaged-in-frequency replacement for a pointwise oscillatory estimate. It is also strictly weaker than absolute Fourier integrability.

### Interval form

Put

    s_0=(sin(1/2)/(1/2))^2=4 sin(1/2)^2.

For an interval `I=[y-ell/2,y+ell/2]`, choose `T=2/ell`. On `I-y`,

    F_T(u)>=s_0/(pi ell).

Therefore

    mu(I) <= (pi ell/s_0) D_{2/ell} mu(y).             (2.3)

Thus a universal bound for the signed Fejer averages gives the required `O(ell)` small-ball estimate immediately, without assuming that `phi` is in `L^1`.

### Continuity is a separate statement

If `p` belongs to `C_0(R)`, then `D_T mu=p*F_T` converges uniformly to `p`. Conversely, local-uniform convergence of `D_T mu` to a function `p` implies that `p` is a continuous density of `mu`. A mere uniform bound in Theorem 2.1 only proves an essentially bounded density; it does not prove continuity.

## 3. A fully coupled distribution-function gate

The Fejer interface becomes useful without any separation of the remainder.

### Theorem 3.1 (one physical scalar gate)

Let `Q=X^T A X` under the full product-law assumptions, and suppose `a=A_ii!=0` for one original coordinate. Then for every interval `I` of length `ell`,

    P(Q in I) <= min(1, 2 sqrt(ell/|a|)).              (3.1)

#### Proof

Condition all coordinates except `X_i`. The conditional polynomial is

    a X_i^2+b X_i+c=a(X_i+b/(2a))^2+c'.

For every interval of output length `ell`, its inverse image under this scalar quadratic has total Lebesgue length at most `2 sqrt(ell/|a|)`. The conditional density of `X_i` is its original density and is at most one. This proves the conditional bound uniformly in the random affine tilt `b` and constant `c`; averaging proves (3.1).

This is a direct, fully coupled replacement for the false scalar pointwise estimate. It is scale-correct for one quadratic direction, but it is only `O(sqrt(ell))`, not the linear estimate needed for the full theorem.

### Theorem 3.2 (definite physical two-plane gate)

Let `S={i,j}` and let `B=A[S,S]`. If `B` is positive or negative definite, then for every interval `I` of length `ell`,

    P(Q in I) <= min(1, pi ell/sqrt(det B)).            (3.2)

Consequently `Q` has a density satisfying

    ||p_Q||_infinity <= pi/sqrt(det B),                (3.3)

and its signed Fejer averages satisfy

    D_T law(Q)(y) <= pi/sqrt(det B)                    (3.4)

for every `T,y`.

#### Proof

Condition all coordinates outside `S`. Independence leaves the conditional joint density `f_i(x_i)f_j(x_j)<=1`. The conditional polynomial is

    z^T B z+l^T z+c.

After translating by `-B^{-1}l/2` and applying `w=|B|^{1/2}z`, the Jacobian is `1/sqrt(det B)`, and the interval preimage is a circular annulus (possibly truncated at radius zero). Its area is at most `pi ell`. This proves (3.2) uniformly in every outside value. Averaging gives the same estimate. Interval domination yields (3.3), and Theorem 2.1 gives (3.4). Negative definite `B` is reduced to the positive case by changing the sign of the polynomial.

The theorem permits arbitrary self-quadratic terms and arbitrary couplings from the two selected coordinates to every conditioned coordinate. It assumes no moment, support, sign pattern outside the two-plane, or diagonal basis. It is a genuine target-level branch, but the three-large-eigenvalue hypothesis does not force a uniformly conditioned definite physical principal pair, so it does not close the parent conjecture.

## 4. Assigned-partner result applied to an actual Fejer inequality

I apply the completed account01/B01 theorem from run `20260922T133732Z-b01-qform-auto11`, canonical report `yspennstate/math-open-problems@e58461e07b19315b290cb4b397929090ec6f48b9`.

For `a=A_ii!=0`, that theorem proves for every frequency interval of length `L`

    int_I |phi_Q(t)|^2 dt <= B_a(L),

where

    B_a(L)=L,                                           if |a|L<1,
    B_a(L)=|a|^{-1}[8+4 pi(1+log(|a|L))],              if |a|L>=1.

It already includes all off-diagonal couplings through a random affine tilt. Applying Cauchy-Schwarz directly to (2.1), and using

    int_{-T}^T (1-|t|/T)^2 dt=2T/3,

gives the actual phase-sensitive inequality

    0<=D_T law(Q)(y)
      <=(1/(2 pi)) sqrt((2T/3) B_a(2T)).               (4.1)

Combining (4.1) with (2.3), for `ell<=4|a|`, gives

    P(Q in [y-ell/2,y+ell/2])
    <=min(1,
      s_0^{-1} sqrt{ ell/(3|a|)
      [8+4 pi(1+log(4|a|/ell))] }).                    (4.2)

This is weaker asymptotically than the direct square-root estimate (3.1), but it is a concrete transfer of the partner's fully coupled local-`L^2` theorem into the exact Fejer interface. More importantly, it identifies what is still missing on the Fourier side: the partner controls the absolute energy, while the full theorem needs the signed average in (2.1) to remain `O(1)` as `T` grows.

## 5. Strictness against the newest absolute-Wiener correction

For `A=I_3` and iid `Uniform[-1/2,1/2]`, the live correction `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1` proves that the relevant absolute Fourier integral diverges. Nevertheless the established diagonal theorem gives a bounded continuous density with norm at most `pi`. Theorem 2.1 therefore yields

    D_T law(Q)(y)<=pi

for every `T,y`, and the Fejer averages converge uniformly to the density. Thus the signed Fejer obligation survives a source-valid case in which the absolute Wiener obligation fails maximally. This is not merely a different notation for `int |phi|`: it retains exactly the time cancellation that the correction requires.

## 6. What remains for the full conjecture

The full QFORM conjecture is not proved here. The exact remaining Fourier implication can now be stated without a false intermediate claim:

    prove sup_{T>0,y in R} D_T law(X^T A X)(y)<=C

under the three-large-eigenvalue hypothesis, uniformly over all cap-one product laws.

By Theorem 2.1 this is equivalent to the desired essentially bounded density and by (2.3) it directly gives the linear interval estimate. The new definite-plane gate pays this obligation whenever a uniformly conditioned definite physical principal pair exists. The difficult residual consists of matrices for which every useful physical pair is indefinite or poorly conditioned, including dense zero-diagonal configurations and the high-cardinality aggregate families in the live corrections. In that residual, the next mechanism must combine original-coordinate product aggregation with the signed Fejer average before taking absolute values; local energy bounds such as (4.1) alone cannot remove the square-root/logarithmic scale loss.

Continuity remains separate: after the uniform Fejer bound, one still needs local-uniform convergence of `D_T` (or another regularity argument). No continuous-density claim is made for the unrestricted target.

## 7. Status and dependencies

New proved results:

* `QFORM-SIGNED-FEJER-EXACT-INTERFACE-v1`: exact equivalence between the target `L^infinity` density bound and a uniform signed triangular frequency average, with the explicit interval majorant (2.3).
* `QFORM-CONDITIONAL-DEFINITE-PLANE-GATE-v1`: the fully coupled bound `pi/sqrt(det B)` from any definite physical principal two-plane.
* `QFORM-COUPLED-FEJER-L2-ENVELOPE-v1`: the assigned partner's local-`L^2` estimate applied to (4.1) and (4.2).

Corrections preserved: pointwise phase-aligned support; absolute ambiguity/Hölder logarithmic loss; absolute phase-Wiener failure; no forced uniformly good local principal block or rank-three cross cut. No numerical histogram, centered-support extremality, moment hypothesis, rotation-preserved independence, or absolute Fourier integrability is used.

Outcome: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.
