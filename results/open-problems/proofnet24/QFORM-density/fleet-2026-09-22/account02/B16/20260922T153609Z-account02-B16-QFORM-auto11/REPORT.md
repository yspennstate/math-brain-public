# account02/B16 — determinant-scaled binary Frostman bound and arbitrary indefinite Schur closure

**Run:** `20260922T153609Z-account02-B16-QFORM-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Projection-product interaction  
**Classification:** `PROVED SUPPORTING THEOREM / COMPLETED PARTNER RESIDUAL / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, live corrections, and partner result actually applied

The full target remains OPEN: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `X^T A X`, or give a target-level counterexample.

Fresh owner control was read from `yspennstate/math-research-brain` at `754c1ba61da9a4ef6cef9e23e7133c10a3cad275`; the last pre-write refresh was `6e3f90aa14e046d79a5ab2d2375e616aacf8475b`. The live corrections used here include the failures of projection-coordinate independence, conditional-cap substitution, fiberwise trace control, single-local-minor extraction, and absolute phase-Wiener control. None is used as a premise.

The completed designated partner result actually applied is **account03/B16**, run `20260922T150329Z-account03-B16-qform-r12`, canonical mathematics `yspennstate/math-open-problems@aee79a848b8d1a5ee1187ce01056b31de32f9505`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260922T150329Z-account03-B16-qform-r12/REPORT.md`, report blob `23cee7df2597df3700859473cc51de2b809b477f`. That report proves a conditional-product `L^3` theorem, an `L^3`-to-square `L^infinity` smoothing theorem, and a physical light-cone Schur branch. Its explicitly stated next missing implication is an arbitrary nondegenerate **indefinite binary quadratic polynomial** in two independent cap-one physical coordinates when both physical Schur diagonals may be nonzero.

This run closes exactly that missing local implication by a different mechanism: a determinant-scaled interval-concentration/Frostman estimate, followed by direct square-kernel potential integration. It never rotates the two input coordinates.

## 2. Binary interval-concentration theorem

Let `Y,W` be independent real random variables with probability densities `f,g` satisfying `0<=f,g<=1`. Let

`R(y,w)=a y^2+2b y w+c w^2+ell_1 y+ell_2 w+ell_0`

and assume the quadratic part is indefinite and nondegenerate:

`D := ac-b^2 < 0`,  `d:=|D|>0`.

For `x>0` define

`Psi(x)=x(1+log(1/x))` for `0<x<1`, and `Psi(x)=1` for `x>=1`.

### Theorem 2.1 — `QFORM-INDEFINITE-BINARY-FROSTMAN-v1`

For every interval `I` of length `h>0`,

`boxed( P(R(Y,W) in I) <= Psi( 2 sqrt(5) h / sqrt(d) ) ).`        (2.1)

Consequently

`boxed( P(R(Y,W) in I) <= M_* (h/sqrt(d))^(2/3) ),`              (2.2)

where

`M_* = 3 e^(-2/3) (2 sqrt(5))^(2/3)
     = 4.1808854176904156... .`                                  (2.3)

The constants are independent of the linear terms, interval location, laws of `Y,W`, and all support/moment information.

### Proof

Because `D!=0`, a translation of `y` and a separate translation of `w` remove `ell_1,ell_2`; this preserves independence and the two density caps. The resulting additive constant can be absorbed into the interval. Thus it suffices to treat the homogeneous quadratic part.

Let `I=[t-epsilon,t+epsilon]`, so `h=2epsilon`.

First suppose `a!=0`. Multiplying the polynomial and interval by `-1` if necessary, assume `a>0`. For fixed `w`, translate only the `y` variable and write

`a y^2+2b y w+c w^2
 = a (y+(b/a)w)^2 - (d/a) w^2.`                                  (2.4)

After `x=sqrt(a)(y+(b/a)w)`, the relevant one-dimensional set has length

`a^(-1/2) L_epsilon(T)`,

where

`L_epsilon(T)=|{x: |x^2-T|<=epsilon}|`,
`T=t+(d/a)w^2`.                                                   (2.5)

Two elementary bounds are enough:

`L_epsilon(T) <= 2 sqrt(2 epsilon)`,                              (2.6)

and for `T>epsilon`,

`L_epsilon(T)
 =2( sqrt(T+epsilon)-sqrt(T-epsilon) )
 <= 2 epsilon/sqrt(T-epsilon).`                                  (2.7)

Fix `0<s<1`. Let `m(w)` be the conditional probability, over `Y`, that `R(Y,w)` lies in `I`. Since `f<=1` and has total mass one,

`m(w) <= min(1, a^(-1/2)L_epsilon(T)).`                           (2.8)

If `m(w)>s`, then `L_epsilon(T)>s sqrt(a)`. By (2.6),

`a epsilon < 8 epsilon^2/s^2`.                                   (2.9)

Also `T>-epsilon`; and if `T>epsilon`, (2.7) gives

`T < epsilon + 4 epsilon^2/(a s^2).`                             (2.10)

Thus every `w` with `m(w)>s` satisfies

`d w^2` lying in one real interval of length at most

`2 a epsilon + 4 epsilon^2/s^2
 < 20 epsilon^2/s^2.`                                             (2.11)

For every interval `J` of length `H`,

`|{w: d w^2 in J}| <= 2 sqrt(H/d)`.                              (2.12)

Indeed, after intersecting `J` with `[0,infinity)`, this is just
`2(sqrt((u+H)/d)-sqrt(u/d)) <= 2 sqrt(H/d)`.

Combining (2.11)-(2.12), and using `h=2epsilon`, gives

`|{w:m(w)>s}| <= 2 sqrt(5) h/(s sqrt(d)).`                        (2.13)

If `a=0`, then `b!=0` and `d=b^2`. For fixed `w!=0`, the admissible `y` set is an interval of length exactly `h/(2|b w|)`, so

`|{w:m(w)>s}| <= h/(s sqrt(d))`,                                 (2.14)

which is stronger than (2.13).

Finally use the original second-coordinate product structure rather than any projected-coordinate independence. Since `0<=g<=1` and `int g=1`, layer cake gives, with `x=2 sqrt(5) h/sqrt(d)`,

`P(R in I)
 = int g(w)m(w)dw
 <= int_0^1 min(1,x/s) ds
 = Psi(x).`                                                       (2.15)

This proves (2.1).

For `0<x<1`, write `x=e^(-u)`. Then

`Psi(x)/x^(2/3)=e^(-u/3)(1+u) <= 3e^(-2/3)`,                     (2.16)

with equality at `u=2`; for `x>=1`, `1<=x^(2/3)`. Substituting `x=2sqrt(5)h/sqrt(d)` yields (2.2)-(2.3). QED.

## 3. Curved-pushforward consequence: inverse-square-root potential is uniformly finite

Let `mu_R` be the law of the binary polynomial above. From (2.2), every interval `J` of length `h` obeys

`mu_R(J) <= M_* (h/sqrt(d))^(2/3).`                               (3.1)

For every `t`, layer cake for the singular kernel gives

`int |t-r|^(-1/2) dmu_R(r)
 = int_0^infinity mu_R( |t-r| < lambda^(-2) ) dlambda.`           (3.2)

The interval inside (3.2) has length `2lambda^(-2)`, so

`mu_R( |t-r| < lambda^(-2) )
 <= min(1, A lambda^(-4/3)),`                                    (3.3)

where

`A=M_* 2^(2/3) d^(-1/3).`                                       (3.4)

Splitting at `lambda_0=A^(3/4)` gives the exact elementary integral

`int_0^infinity min(1,A lambda^(-4/3)) dlambda
 =4 A^(3/4).`                                                     (3.5)

Hence

`boxed(
 sup_t int |t-r|^(-1/2)dmu_R(r)
 <= 4 sqrt(2) M_*^(3/4) d^(-1/4).
 )`                                                               (3.6)

This is the requested connection between original-coordinate product structure and the **curved quadratic pushforward**. A bounded two-dimensional projection density by itself is not used and would not supply (3.1); the product cap is consumed before the curved trace through the physical one-coordinate slices.

## 4. Arbitrary indefinite physical Schur complement is now paid

Consider three independent original coordinates `(Z,Y,W)` and, after conditioning on every outside coordinate, a physical `3x3` principal block in scalar-pivot form

`B=[[alpha,r^T],[r,C]]`,  `alpha!=0`,

with physical two-coordinate Schur complement

`S=C-r r^T/alpha`.                                                (4.1)

Assume `S` is nondegenerate indefinite, so `det S<0`. Completing the square only in the physical pivot coordinate gives

`Q = alpha (Z+m(Y,W))^2 + R(Y,W)`,                               (4.2)

where the quadratic part of `R` is exactly `S`. Outside conditioning creates only linear and constant terms in `R`, which Theorem 2.1 already allows.

For fixed `(Y,W)`, the variable `Z+m(Y,W)` is a translate of the original cap-one density of `Z`. Therefore the conditional square pushforward has density bounded by

`|alpha|^(-1/2) |t-R(Y,W)|^(-1/2)`                               (4.3)

on the appropriate one-sided half-line. Averaging (4.3), and then using the stronger symmetric estimate (3.6), yields

`||p_Q||_infinity
 <= C_ind |alpha|^(-1/2) |det S|^(-1/4),`                        (4.4)

where

`C_ind=4sqrt(2)M_*^(3/4)
     = 8 * 3^(3/4) * 5^(1/4) / sqrt(e)
     = 16.53964516612327... .`                                   (4.5)

Since `det B=alpha det S`,

`boxed(
 ||p_Q||_infinity
 <= 16.539646 (|alpha det B|)^(-1/4).
 )`                                                               (4.6)

The bound is uniform in the outside coordinates, so averaging the conditional densities proves the same ambient bound with arbitrary outside couplings.

### Theorem 4.1 — `QFORM-ARBITRARY-INDEFINITE-SCHUR-FROSTMAN-v1`

Every invertible physical `3x3` pivot block having a nonzero physical scalar pivot and an arbitrary nondegenerate indefinite physical Schur complement is controlled by (4.6), with no rotation of the residual coordinates, no conditional-cap substitution after a sum/difference change of variables, no support or moment assumptions, and no receiver-only projection argument.

This strictly contains the newest account03/B16 light-cone residual `S=[[0,s],[s,c]]` as a special case (with a worse constant than that partner's sharper `8/(|alpha det B|)^(1/4)` special-case estimate). It closes the partner report's explicitly named remaining branch where both physical Schur diagonals are nonzero.

## 5. Relation to the previous B16 obstruction and remaining global problem

The theorem does **not** contradict the earlier `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1` correction. That counterexample shows that after replacing product coordinates by a dependent low-dimensional spectral projection, a fiberwise indefinite trace can diverge. Here the proof never makes that replacement: it conditions on one **original independent coordinate**, spends the actual cap `f<=1` on its physical quadratic slice, then spends the other original cap and probability normalization by layer cake before applying the curved square kernel.

Combining this run with the completed definite-Schur branch cited in account03/B16 and with account02/B16's prior all-zero-diagonal triple theorem removes the local sign-form hole for invertible physical triples without relying on rotated independence. But this is still not the full conjecture. The exact global obstruction remains that three large spectral eigenvalues do not force a physical triple with determinant bounded below. The live family

`(J_m/m) direct_sum (J_m/m) direct_sum (-J_m/m)`

has spectrum `{1,1,-1}` while every useful local reciprocal-minor payment deteriorates with `m`. A full proof must aggregate independent coordinate banks/diffuse pieces **before** paying reciprocal local minors, or provide a different global mechanism.

## 6. Status

- `QFORM-INDEFINITE-BINARY-FROSTMAN-v1`: **PROVED**.
- `QFORM-ARBITRARY-INDEFINITE-SCHUR-FROSTMAN-v1`: **PROVED supporting target branch**.
- Newest completed account03/B16 missing binary-indefinite-Schur branch: **CLOSED in the stated local scope**.
- Full arbitrary-dimension three-large-eigenvalue theorem: **OPEN / NOT PROVED**.
- No continuity claim, novelty claim, or target-level counterexample is made.
