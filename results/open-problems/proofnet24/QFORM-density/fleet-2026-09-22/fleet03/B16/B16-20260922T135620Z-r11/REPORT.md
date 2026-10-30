# fleet03/B16 — fractional-trace product smoothing for every scalar Schur branch

**Run:** `B16-20260922T135620Z-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** projection-product interaction  
**Status:** `ESSENTIAL_SUPPORTING_STEP / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction-aware mechanism

The full target remains open: for independent real `X_i` with probability densities `0<=f_i<=1` and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal dimension/matrix/law-independent `L^infinity` density bound for `X^T A X`.

This run does **not** use the false law-uniform one-dimensional pointwise Fresnel estimate, does not replace product provenance by a bounded projection density, and does not take a fiberwise supremum of an indefinite trace. The live correction `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1` shows why that receiver-only route cannot work. Instead, the nonlinear trace is integrated jointly with the original two-coordinate product law.

The exact assigned partner `fleet04/B16` had no completed QFORM handoff visible at the final source refresh, so no result is attributed to it. A compatible completed partner theorem from `fleet04/B18` is applied below: `QFORM-SCHUR-PIVOT-SMOOTHING-v1`, canonical source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, proves the definite-Schur branch with constant `2 sqrt(pi)(|a det B|)^(-1/4)`. The new work closes its explicitly stated **indefinite-Schur / majority-sign pivot** boundary for every physical scalar pivot.

## 2. A one-dimensional bathtub kernel

For a probability density `f` on `R` satisfying `0<=f<=1`, set

`J_f(A)= integral_R f(x) |A-x^2|^(-1/2) dx`,

and `J_*(A)=sup_f J_f(A)`. Define

`Psi(A)= 1+log(1/|A|)` for `0<|A|<=1`, and `Psi(A)=|A|^(-1/4)` for `|A|>=1`.

(At `A=0`, allow `Psi(0)=+infinity`; later root loci have Lebesgue measure zero.)

### Lemma 2.1

For every `A!=0`,

`J_*(A) <= 8 Psi(A)`.

### Proof

By layer cake, for `K_A(x)=|A-x^2|^(-1/2)`,

`J_f(A) <= integral_0^infinity min(1,m_A(s)) ds`,

where `m_A(s)=|{x:K_A(x)>s}|`.

Write `epsilon=s^(-2)`. If `A>=0` and `epsilon>=A`, then

`m_A(s)=2 sqrt(A+epsilon) <= 2 sqrt(2)/s`.

If `A>=0` and `epsilon<A`, then

`m_A(s)=2[sqrt(A+epsilon)-sqrt(A-epsilon)] <= 4/(sqrt(A)s^2)`.

If `A<0`, then `m_A(s)=2 sqrt(epsilon-|A|)` when `epsilon>|A|` and zero otherwise, hence `m_A(s)<=2/s`.

For `0<|A|<=1`, split at `s=1` and `s=|A|^(-1/2)`; the displayed bounds give at most `8[1+log(1/|A|)]`. For `|A|>=1`, split where the `s^(-2)` bound crosses one; this gives at most `8|A|^(-1/4)`. QED.

## 3. The logarithmic ridge has a uniform weak-L2 trace

The elementary quadratic sublevel estimate

`|{z: |z^2+a|<R}| <= 4 sqrt(R)`                                          (3.1)

holds for every real `a` and `R>0`: for `a>=0` it is immediate; for `a<0` it follows from the difference of the two square roots around `sqrt(-a)`.

### Lemma 3.1

Uniformly in `a in R`,

`|| Psi(a+z^2) ||_(L^{2,infinity}(dz)) <= sqrt(15)`.

### Proof

For `0<t<1`, the event `Psi(a+z^2)>t` implies

`|a+z^2|<t^(-4)`;

by (3.1) its measure is at most `4t^(-2)`. For `t>=1`, only the logarithmic branch contributes and

`Psi(a+z^2)>t  =>  |a+z^2|<exp(1-t)`.

Thus the measure is at most `4 exp((1-t)/2)`. Since

`sup_{t>=1} 4 t^2 exp((1-t)/2) = 64 exp(-3/2) < 15`,

the weak-`L^2` claim follows. QED.

Scaling yields, for `delta>0`,

`||J_*(a+delta y^2)||_(2,infinity) <= 8 sqrt(15) delta^(-1/4)`.            (3.2)

If `g` is any probability density with `0<=g<=1`, then for every nonnegative weak-`L^2` function `h`, layer cake gives

`integral g h <= integral_0^infinity min(1, |{h>t}|)dt <= 2 ||h||_(2,infinity)`.

Combining with (3.2),

`integral g(y) J_*(a+delta y^2)dy <= 16 sqrt(15) delta^(-1/4)`.            (3.3)

This is the key product-trace payment: the logarithmic ridge is not bounded pointwise, but it is uniformly weak-`L^2`, and the second cap-one marginal pays that ridge exactly once.

## 4. New theorem: two-dimensional indefinite fractional trace

### Theorem 4.1 — `QFORM-INDEFINITE-PRODUCT-FRACTIONAL-TRACE-v1`

Let `X,Y` be independent real variables with densities bounded by one. Let

`R(x,y) = (x,y) S (x,y)^T + linear(x,y) + constant`,

where `S` is an invertible indefinite real symmetric `2x2` matrix and `D=|det S|`. Then

`sup_z E |z-R(X,Y)|^(-1/2) <= 16 sqrt(15) D^(-1/4)`.                      (4.1)

No moment, support, continuity, or sign assumption is imposed on the input densities.

### Proof

Because `S` is invertible, a deterministic translation removes the linear term. This translates the two input densities separately and preserves independence and the cap-one property.

First suppose the first diagonal entry `r=S_11` is nonzero. Writing the off-diagonal entry as `s`, complete the square:

`R = r(x+(s/r)y)^2 - (D/r)y^2 + constant`

because `det S<0`. Set `delta=D/r^2`. For fixed `y`, translating `x` by `(s/r)y` preserves its density cap and mass, so

`E_X |z-R|^(-1/2)
 <= |r|^(-1/2) J_*( z/r + delta y^2 + constant' )`.

Average over `Y` and apply (3.3):

`E |z-R|^(-1/2)
 <= 16 sqrt(15) |r|^(-1/2) delta^(-1/4)
 = 16 sqrt(15) D^(-1/4)`.

If `S_11=0` but `S_22!=0`, swap the coordinates.

If both diagonal entries vanish, `S=[[0,c],[c,0]]`, `D=c^2`. For every cap-one probability density `h`, the bathtub principle gives

`sup_a integral h(v)|v-a|^(-1/2)dv <= 2 sqrt(2)`.

Condition first on `Y` and then integrate `Y`; this yields the sharper bound

`sup_z E |z-2cXY|^(-1/2) <= 4 sqrt(2) |c|^(-1/2)
 =4 sqrt(2)D^(-1/4)`.

This is below the constant in (4.1). QED.

## 5. New local three-coordinate theorem

Consider any ambient symmetric matrix `A` and three **original independent coordinates** whose physical principal block, after ordering one pivot first, is

`B=[[a,b^T],[b,C]]`, with `a!=0` and `det B!=0`.

Let `S=C-bb^T/a`; then `det B=a det S`, so `S` is invertible. Condition on every coordinate outside this triple. Outside couplings become only linear and constant terms. Completing the square in the pivot variable `Z` gives

`Q_w(Z,U)=a(Z+m_w(U))^2+R_w(U)`,

where the quadratic matrix of `R_w` is exactly `S`.

For each fixed `U=u`, the translated pivot variable still has a density bounded by one, so the square-pushforward kernel gives

`p_{Q_w}(t) <= |a|^(-1/2) E_U |t-R_w(U)|^(-1/2)`.                         (5.1)

### Theorem 5.1 — `QFORM-ALL-SCHUR-PIVOT-PRODUCT-TRACE-v1`

Under the preceding hypotheses, the full quadratic form has an essentially bounded density. More precisely:

* if `S` is indefinite,

`||p_Q||_infinity <= 16 sqrt(15) (|a| |det B|)^(-1/4)`;                  (5.2)

* if `S` is definite, the completed `fleet04/B18` partner theorem gives

`||p_Q||_infinity <= 2 sqrt(pi) (|a| |det B|)^(-1/4)`.                   (5.3)

Hence every invertible physical `3x3` principal block with at least one nonzero diagonal pivot is controlled, regardless of Schur-complement signature, with the unified bound

`||p_Q||_infinity <= 16 sqrt(15) (|a| |det B|)^(-1/4)`.                  (5.4)

### Proof

For the indefinite branch, combine (5.1) with Theorem 4.1 and `|det S|=|det B|/|a|`. For the definite branch, apply the named fleet04/B18 theorem, which was proved precisely for this conditional fully coupled setting and allows arbitrary outside couplings. Averaging conditional densities over the outside coordinates preserves the same `L^infinity` bound. QED.

This theorem removes the exact sign boundary left by the partner result: **a majority-sign scalar pivot whose Schur complement is indefinite is no longer an unpaid local branch.**

The new argument proves absolute continuity plus an essentially bounded density. It does **not** prove a continuous representative; continuity remains separate.

## 6. Exact application to the partner's Hadamard boundary example

The partner report identified

`H=[[1,1,1],[1,1,-1],[1,-1,1]]`

as the basic inertia `(2,1)` example in which every diagonal pivot has the majority sign and every scalar Schur complement is indefinite.

Exact arithmetic gives

`det H=-4`,  `spec(H)={-1,2,2}`.

For the first pivot, `a=1` and

`S=[[0,-2],[-2,0]]`, `det S=-4`.

This is the pure off-diagonal subcase of Theorem 4.1, so (rather than the generic `16 sqrt(15)` constant) the sharper calculation gives

`boxed( ||p_{X^T H X}||_infinity <= 4 )`.                               (6.1)

Thus the exact Hadamard majority-sign obstruction in the fleet04/B18 report is fully paid for arbitrary independent cap-one input densities, without rotating the inputs or assuming a bounded conditional projection density.

## 7. What remains unpaid for the full conjecture

This is **not** a full solution. The three-large-eigenvalue hypothesis does not force one physical principal triple with `|a det B|` bounded below by a universal constant. Delocalized frames can make every individual scalar pivot/minor tiny. The live aggregate-minor theorem from fleet01/B07 shows that determinant mass can survive in an aggregate even when every fixed-cut leverage gate fails; the current theorem supplies a new local payment once a scalar-pivot triple is selected, but does not yet prove the required dimension-free selection/mixture.

The next target-relevant implication is:

> combine determinant-weighted heavy-coordinate stopping/mixture with (5.4), so that the sum of reciprocal local payments is controlled by aggregate third-minor mass rather than by the worst selected `|a det B|`; separately handle the all-zero-diagonal invertible triple or pay it through a two-coordinate pivot. The argument must retain arbitrary extra spectral components and original-coordinate product provenance.

This also explains why the generic bounded-projection-density interface remains insufficient: the logarithmic indefinite ridge is paid by the **source product law before normalization**, through the weak-`L^2` estimate (3.3), not by a receiver-only density cap.

## 8. Verification and scope

Exact symbolic checks for the Hadamard block give `det H=-4`, eigenvalues `-1,2,2`, first Schur complement `[[0,-2],[-2,0]]`, and the pure-bilinear constant `4`. These checks are diagnostics; the proof is the analytic derivation above.

Corrections consumed before publication include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`.

No claim of a full solution, universal final constant, continuity for the new branch, novelty, or independent review is made.
