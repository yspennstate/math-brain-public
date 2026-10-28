SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T04:21:38Z.
attacking: QFORM-PUNCTURED-FRESH-HUB-SQUARE-STABILITY-v1 by a second-fresh-hub conditioning relay; close the r39 absolute-TT* barrier family and lift the designated account04/B16 receiver through an arbitrary outer square.

# account03/B16 r40 — outer-square relay and closure of the r39 mixed-frame barrier family

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T042138Z-account03-B16-QFORM-r40`  
**Role:** Projection-product interaction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW SOURCE-FIRST STRUCTURAL COMPILER + PREVIOUS BARRIER FAMILY CLOSED / FULL QFORM OPEN`  
**Regularity:** the new arguments below prove absolute continuity and an essential density bound in their stated scopes. They do **not** prove continuity there. Full-target continuity remains open.

## 1. Source boundary and mechanism change

The owner target remains unrestricted: independent original-coordinate real inputs with scalar probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of `A` of modulus at least one. No Gaussianity, moments, compact support, log-concavity, connected support, iid assumption, or independence after spectral rotation is used.


This run deliberately changes mechanism after the preceding mixed-volume/absolute-TT* attempts. The new step is source-first: condition an *outer* physical square before invoking a completed zero-pivot receiver on a **different** genuinely fresh source. This preserves original-coordinate independence and never deletes the outer square.

The completed inputs used are:

1. `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1`, account02/B16,
   `yspennstate/math-open-problems@be8062b160868bcc71aff45a77c56ff2d0501a9a`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T203140Z-account02-B16-QFORM-r36/REPORT.md`.
   If `H` is cap-one and independent of a light object `W`, `(L,V)` are light functions with joint density cap `M`, `T=T(W)` is arbitrary, and
   `Q=2 gamma H L+2LT+alpha L^2+2 delta LV+kappa V^2`, `gamma*kappa!=0`, then
   
   `||p_Q||_infinity <= 3*2^(2/3) M^(2/3)|gamma^2 kappa|^(-1/3)`.

2. The designated partner account04/B16 theorem `QFORM-FRESH-OR-TRANSVERSE-PAIRCAP-DICHOTOMY-v1`,
   `yspennstate/math-open-problems@c1bf7fd07ac10b105686d96c96344a1a2274f5d9`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260924T021703Z-account04-B16-QFORM-r3/REPORT.md`.
   With the source-valid pair construction in that theorem,
   
   `||p_Q||_infinity <= 3*2^(2/3) min{sqrt(2)/|sigma|,4/sqrt(G)}^(2/3)|gamma^2 kappa|^(-1/3)`,
   
   with an unavailable term omitted. In particular the transverse branch is
   
   `||p_Q||_infinity <=12 [G|gamma^2 kappa|]^(-1/3)`.

3. The immediately preceding B16 r39 report,
   `yspennstate/math-open-problems@3272887eaefad259aefc2e13a42d7699e74862cb`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260924T025219Z-account03-B16-QFORM-r39/REPORT.md`.
   It exhibited a strict target family with order-one mixed Pluecker mass for which the old *absolute* TT* kernel is infinite. That was a mechanism obstruction, not an output-density counterexample.

A fresh account01/B11 result, `yspennstate/math-open-problems@22373d23a5a18f91627d8849017beb38a2169f23`, independently closes the exact-rank-three zero-pivot near-coloop same-bank puncture by a Witt leverage identity. Therefore this run does not duplicate that zero-pivot work; it addresses how a nonzero outer physical square can be made harmless when a second source-separated zero-pivot crossing survives.

## 2. New compiler: an arbitrary outer square is free once a second fresh crossing survives

### Theorem `QFORM-OUTER-SQUARE-PAIRCAP-RELAY-v1`

Let `R,H` be independent real random variables with densities at most one. Let `W` be an arbitrary random object independent of `(R,H)`. Let `L=L(W)`, `V=V(W)`, and `T=T(W)` be measurable real functions and assume

`||p_(L,V)||_infinity <= M`.                                      (2.1)

For arbitrary real `A,r,alpha,delta`, and nonzero `gamma,kappa`, define

`Q = A R^2 + 2 r R L
     +2 gamma H L+2LT+alpha L^2+2delta LV+kappa V^2`.              (2.2)

Then `Q` is absolutely continuous and

`boxed:
 ||p_Q||_infinity
 <=3*2^(2/3) M^(2/3)|gamma^2 kappa|^(-1/3).
`                                                                     (2.3)

The bound is completely independent of the outer-square coefficient `A` and the outer crossing coefficient `r`.

#### Proof

Condition on the *outer* source `R=s`. The first two terms in (2.2) become a constant `A s^2` and the light-divisible term `2L(rs)`. Hence, up to the harmless constant shift,

`Q | {R=s}
 =2 gamma H L
  +2L[T(W)+rs]
  +alpha L^2+2delta LV+kappa V^2`.                                (2.4)

For each fixed `s`, this is exactly the completed account02/B16 theorem with the same fresh source `H`, the same pair `(L,V)`, and the new arbitrary twist

`T_s(W)=T(W)+rs`.                                                   (2.5)

The source theorem is uniform in the entire measurable twist, so its right side is independent of `s`. Thus every conditional law has a density bounded by the right side of (2.3). Averaging these conditional densities over `R` gives a density for `Q` with the same essential supremum. No moment of `R` is used, and `A R^2` is never treated as a small perturbation. QED.

### Why this matters for the punctured-hub problem

The small nonzero physical hub square is therefore **not intrinsically** the obstruction. It is harmless whenever, after conditioning that hub, there remains a second genuinely source-separated zero-pivot crossing whose partner pair can be controlled. The hard punctured collar must therefore be a state where the useful third direction is carried only through shared-bank curvature/overlap, not through such a second fresh relay.

This is exactly the distinction suggested by r39's phase-aware comparison: scalar mixed volume alone did not decide the issue; the location of the zero-pivot crossing inside the original source factorization does.

## 3. Designated account04/B16 theorem lifted through the outer square

The same conditioning gives a direct lift of the designated partner theorem.

Let `X` be the partner's product bank, let `Z,H` be its two fresh sources, put

`L=<ell,X>`, `S=<v,X>`, `V=sigma Z+S`,
`G=det Gram(ell,v)`,                                               (3.1)

and assume the partner's row-leverage gate when `G>0`. Add a further independent outer source `R` and define

`Q_tilde = A R^2+2rRL
          +2gamma HL+2LT+alpha L^2+2delta LV+kappa V^2`.           (3.2)

Conditioning on `R=s` merely replaces `T` by `T+rs`, so account04/B16 applies without any change in its pair cap. Therefore

`boxed:
 ||p_(Q_tilde)||_infinity
 <=3*2^(2/3)
   min{sqrt(2)/|sigma|,4/sqrt(G)}^(2/3)
   |gamma^2 kappa|^(-1/3).
`                                                                     (3.3)

In particular, under `|gamma|>=1`, `|kappa|>=1`, the partner's live gates survive an **arbitrary** outer square and crossing:

`|sigma|>=1/64  => ||p_(Q_tilde)||_infinity <=96`,                 (3.4)

`G>=2^(-12)     => ||p_(Q_tilde)||_infinity <=192`.                (3.5)

This is a target-relevant splice: a nonzero outer pivot does not reopen either completed partner branch if a second fresh source remains available after conditioning.

## 4. The r39 absolute-TT* barrier family is actually uniformly bounded by 3

Recall the r39 sharp mixed frame, for independent cap-one original sources `H_0,X_1,...,X_4`:

`L=(X_1-X_3)/sqrt(2)`,
`S=(X_2+X_4)/sqrt(2)`,
`P=(X_1+X_3)/sqrt(2)`.                                             (4.1)

Its mixed Pluecker masses are `M_JJK=M_JKK=1/2`, but r39 showed that the old absolute two-bank TT* kernel can nevertheless be infinite for interval laws. Consider exactly the former barrier family

`Q_bar,theta
 =theta H_0^2+2sqrt(2)H_0L+2P^2+4LS`.                           (4.2)

### Theorem `QFORM-R39-BARRIER-FAMILY-RELAY-CLOSURE-v1`

For every real `theta` and **arbitrary** independent original-coordinate probability densities bounded by one,

`boxed: ||p_(Q_bar,theta)||_infinity <=3.`                          (4.3)

Thus the infinite absolute-TT* kernel from r39 is purely a proof-mechanism failure; the actual output density of that same target family is uniformly bounded with a small constant.

#### Proof

Expand only the `S` term:

`4LS=2sqrt(2)LX_2+2sqrt(2)LX_4`.                                  (4.4)

Condition on `H_0=h`. Use `X_2` as the new genuinely fresh scalar and take the light object to be

`W=(X_1,X_3,X_4)`.                                                 (4.5)

The pair `(L,P)` depends only on `(X_1,X_3)`. The map

`(x_1,x_3) -> ((x_1-x_3)/sqrt(2),(x_1+x_3)/sqrt(2))`               (4.6)

is orthogonal, hence has Jacobian one. Therefore its joint density is exactly the product of the two pulled-back scalar densities and

`||p_(L,P)||_infinity <=1`.                                       (4.7)

For fixed `h`, (4.2) is, up to the constant `theta h^2`,

`2sqrt(2)X_2L
 +2L[sqrt(2)h+sqrt(2)X_4]
 +2P^2`.                                                           (4.8)

Apply `QFORM-FRESH-HUB-DIVISIBLE-TWIST-ABSORPTION-v1` with

`H=X_2`, `V=P`, `M=1`,
`gamma=sqrt(2)`, `kappa=2`,
`T=sqrt(2)h+sqrt(2)X_4`, `alpha=delta=0`.                           (4.9)

Since `|gamma^2 kappa|=4`,

`||p_(Q_bar,theta | H_0=h)||_infinity
 <=3*2^(2/3)*4^(-1/3)=3`.                                         (4.10)

The estimate is uniform in `h` and `theta`; average over `H_0`. QED.

### Strict owner-target check

In the orthonormal carrier `(H_0,L,P,S)`, the matrix of (4.2) is

`[[theta,sqrt(2),0,0],
  [sqrt(2),0,0,2],
  [0,0,2,0],
  [0,2,0,0]]`.                                                     (4.11)

The `P` direction is an eigenvector with eigenvalue `2`. The `(L,S)` principal block inside the remaining three-dimensional block is `[[0,2],[2,0]]`, with eigenvalues `+2,-2`. Cauchy interlacing therefore gives one eigenvalue of the `(H_0,L,S)` block at least `2` and one at most `-2`. Hence (4.2) has at least three eigenvalues of modulus at least `2` for every real `theta`. This is a strict instance of the owner target, not an easy off-target model.

No continuity conclusion is claimed from (4.3); the source theorem supplies absolute continuity and essential boundedness.

## 5. Concrete designated-partner application with the outer square present

To exercise (3.3) at an actual inequality satisfying the account04/B16 row-leverage gate, use six independent leaf sources and define

`L=(X_1+X_2-X_3-X_4)/2`,
`V=(X_1+X_2+X_3+X_4)/2`,
`S=(X_5+X_6)/sqrt(2)`.                                             (5.1)

Let `H_0` be one further independent cap-one original source and set

`Q_dist,theta
 =theta H_0^2+2sqrt(2)H_0L+2V^2+4LS`.                           (5.2)

Condition on `H_0=h`. Use partner fresh source `H=X_5`; include `X_6` in the light bank with zero coefficients in `(L,V)`; and take

`gamma=sqrt(2)`, `kappa=2`, `sigma=0`,
`T=sqrt(2)(h+X_6)`.                                                 (5.3)

The coefficient vectors of `(L,V)` are orthonormal. On each of `X_1,...,X_4`, their normalized two-frame row leverage is

`(1/2)^2+(1/2)^2=1/2`,                                             (5.4)

while the `X_6` row leverage is zero. Thus the designated partner's gate is met exactly and `G=1`. Its transverse estimate gives the actual all-target inequality

`boxed:
 ||p_(Q_dist,theta)||_infinity
 <=12*4^(-1/3)
 =7.559526299369239...<7.56,
`                                                                     (5.5)

uniformly for every real outer-square coefficient `theta`.

The family is again strict target-valid by the same carrier/interlacing argument as Section 4. For comparison only, the actual two-dimensional orthogonal projection theorem gives the pair cap `M<=2`, and the stronger source theorem from Section 2 yields `3*2^(2/3)=4.7622031559...`; (5.5) is recorded because it is the required **designated account04/B16 result applied to an actual inequality**.

## 6. What this resolves and what remains

The r39 family labeled as an absolute-TT* barrier is no longer an unresolved density family: (4.3) closes it by a source-first relay. The correct lesson is now sharper:

- order-one mixed Pluecker volume does **not** control the old absolute TT* kernel;
- nevertheless, if the phase exposes a second source-separated zero-pivot crossing after conditioning the outer square, the whole outer-square puncture is harmless;
- therefore the genuinely hard punctured near-coloop packet must be one in which every quantitatively useful third direction is trapped in the same source bank as its curvature, so that no relay of Theorems 2/3 is available.

The first B16 implication is consequently narrowed to

`QFORM-PUNCTURED-NO-SECOND-FRESH-RELAY-v1`:                         (6.1)

in the exact-rank-three small nonzero hub-pivot collar `0<|a|D<2^(-12)`, prove a universal bound in the complementary state where no source-separated secondary zero-pivot crossing satisfies either the fresh-innovation or shared-transverse account04/B16 gate. The next mechanism must keep cancellation/curvature inside that shared bank; replacing it by a marginal cap is forbidden by the live corrections.

This does **not** close arbitrary additional nonseparable spectrum, and it does not prove the full conjecture. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity remains OPEN.

## 7. Verification notes

A deterministic checker saved beside this report verifies:

1. the exact constant `3` in (4.10);
2. the designated-partner constant `12*4^(-1/3)=7.559526299369239...`;
3. the four active `(L,V)` row leverages in (5.4) are exactly `1/2`;
4. the conditional three-variable matrix in the sharp barrier closure has characteristic polynomial `(lambda-2)(lambda^2-2)` and determinant `-4`, consistent with the zero-pivot rank-three receiver;
5. the carrier target check uses an exact `+2` eigenvector and an exact principal `(+2,-2)` pair, so it is uniform in `theta`.

These finite checks are regression evidence; Sections 2--6 are the analytic argument.
