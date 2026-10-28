SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T04:57:04Z.
attacking: QFORM-PUNCTURED-NO-SECOND-FRESH-RELAY-v1 by extracting the exact nonzero-pivot Schur/range-leverage normal form and locating the source information that the positive discriminant trace deletes.

# account03/B16 r41 — nonzero-pivot Schur leverage and the exact majority-sign root-numerator debt

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260924T045704Z-account03-B16-QFORM-r41`  
**Role:** Projection-product interaction  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW EXACT STRUCTURAL COMPILER + QUANTITATIVE HARD-COLLAR REDUCTION / FULL QFORM OPEN`  
**Regularity:** the new results below prove structural identities and a scoped essential-density estimate. They do not prove full-target continuity.

## 1. Source boundary

The owner target remains unrestricted: independent original-coordinate real inputs with scalar probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, moment, support, log-concavity, connected-support, iid, or independence-after-rotation hypothesis is introduced.


The immediate B16 predecessor is r40:

- `yspennstate/math-open-problems@0cb21304c563591f2fd01a9f67efb5449a14b6fc`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B16/20260924T042138Z-account03-B16-QFORM-r40/REPORT.md`.

It showed that an arbitrary nonzero outer physical square is harmless whenever a second source-separated zero-pivot crossing survives. The remaining exact-rank-three state is therefore the small nonzero physical pivot for which the useful third direction is trapped in the same residual source bank.

Two source inputs used below are:

1. account02/B16's exact physical-hub discriminant calculation and its hyperbolic cap barrier, `yspennstate/math-open-problems@390bf6a9ad30195ba4011927c8218245d0e014be`;
2. the designated partner account04/B16 r4, `yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`, whose two-dimensional projected-plane theorem gives `2*pi/sqrt(|det H|)` for a definite projected quadratic plane while retaining arbitrary affine translations from disjoint outside sources.

The new point of this run is an exact nonzero-pivot counterpart of the zero-pivot Witt leverage identity: it tells exactly how much determinant, physical-star energy, and hidden same-bank leakage remain after Schur complementation, and it exposes why the positive hub-root majorant loses the dominant near-coloop resource.

## 2. Exact nonzero-pivot Schur/range-leverage normal form

Let `A` be real symmetric of **exact rank three**, with nonzero eigenvalues `mu_1,mu_2,mu_3`. Choose an ORIGINAL coordinate `h` with

`a=A_hh != 0`.

Write, with `J=[n]\{h}`,

`A = [[a,b^T],[b,C]]`,

and define the physical Schur complement

`S=C-bb^T/a`.                                                     (2.1)

Since congruence by the usual pivot elimination preserves rank,

`rank S=2`.                                                        (2.2)

Let `R=ran S`, decompose the physical star

`b=b_R+b_0`, `b_R=P_R b`, `b_0=P_(ker S)b`,                       (2.3)

and put

`rho=||b_R||`, `tau=||b_0||`.                                     (2.4)

Let

`q_h=||P_(ran A)e_h||^2`                                          (2.5)

be the spectral-range leverage of the literal physical hub.

### Theorem `QFORM-NONZEROPIVOT-SCHUR-LEVERAGE-v1`

The following identities hold exactly:

`boxed: q_h = a^2/(a^2+tau^2).`                                   (2.6)

If `Delta_A=mu_1 mu_2 mu_3` and `Delta_S` is the product of the two nonzero eigenvalues of `S`, then

`boxed: a Delta_S = q_h Delta_A.`                                 (2.7)

If every `|mu_j|>=s`, then

`boxed: rho^2 >= s^2 q_h - a^2/q_h.`                              (2.8)

In particular, in the live near-coloop/small-pivot collar

`q_h>=63/64`, `0<|a|<=s/64`,                                     (2.9)

one has the fully explicit bounds

`boxed: rho^2 >= (62/63)s^2,`                                     (2.10)

`boxed: tau <= |a|/sqrt(63),`                                     (2.11)

and

`boxed: |Delta_S| >= 63 s^2.`                                     (2.12)

Thus more than `62/63` of one unit of squared physical-star scale is forced into the **rank-two Schur range**, while the star component in the Schur kernel is only of order the already-small pivot.

### Proof

Set

`T=[[1,b^T/a],[0,I]]`.

Then

`A=T^T diag(a,S) T`.                                               (2.13)

Let `E=span(e_h) direct_sum R`, the three-dimensional range of `diag(a,S)`. Under `T^T`,

`e_h -> e_h+b/a`, while `R` is fixed. Subtracting the `b_R/a` component inside `R`, one obtains

`ran A = R direct_sum span(e_h+b_0/a)`,                            (2.14)

with an orthogonal direct sum. Projecting `e_h` onto the last line gives (2.6).

For (2.7), choose an orthonormal basis `u_1,u_2` of `R` diagonalizing `S`. The three columns

`e_h+b/a, u_1,u_2`

span `ran A`. Their Gram determinant is the squared distance of `e_h+b/a` from `R`, namely

`1+tau^2/a^2 = 1/q_h`.                                            (2.15)

Writing the rank-three matrix as the corresponding nonorthogonal frame times `diag(a,lambda_1,lambda_2)` times its transpose, Sylvester's nonzero-eigenvalue identity gives

`Delta_A = a Delta_S (1+tau^2/a^2)=a Delta_S/q_h`,                 (2.16)

which is (2.7).

For (2.8), using a spectral decomposition of `A`,

`a^2+||b||^2=(A^2)_hh=sum_j mu_j^2 |<e_h,r_j>|^2 >= s^2 q_h`.      (2.17)

From (2.6),

`tau^2=a^2(1-q_h)/q_h`.                                           (2.18)

Therefore

`rho^2=||b||^2-tau^2 >= s^2 q_h-a^2-a^2(1-q_h)/q_h
       =s^2q_h-a^2/q_h`,                                         (2.19)

proving (2.8). Under (2.9), the right side is minimized at `q_h=63/64`, `|a|=s/64` and equals

`s^2(63/64-1/4032)=s^2(62/63)`,                                  (2.20)

which gives (2.10). Equation (2.11) is immediate from (2.18). Finally (2.7) and `|Delta_A|>=s^3` give

`|Delta_S|>=q_h s^3/|a| >=63 s^2`,                               (2.21)

proving (2.12). QED.

## 3. Canonical four-variable source form and conditional hub cap

When `rho>0`, choose a unit vector `ell=b_R/rho` in `R` and a unit `v in R` orthogonal to `ell`. When `tau>0`, put `p=b_0/tau`. Define the residual projections

`L=<ell,X_J>`, `V=<v,X_J>`, `P=<p,X_J>`.                          (3.1)

These are orthogonal coefficient directions, but they are generally **dependent** because they come from the same original-coordinate product bank. The literal hub `H=X_h` remains genuinely independent of the entire residual bank.

Let `S_2` be the `2x2` matrix of `S` on the orthonormal basis `(ell,v)`. Then the full exact-rank-three quadratic form has the identity

`boxed:
 Q = a ( H + (rho L+tau P)/a )^2 + (L,V) S_2 (L,V)^T.
`                                                                      (3.2)

No term has been discarded; the fourth projected coordinate `P` appears only inside the translated physical square.

Put

`eta=tau/a`, `q=q_h=1/(1+eta^2)`,

and define the normalized range-hub variable

`Y=sqrt(q)(H+eta P)`.                                              (3.3)

Its coefficient vector is a unit vector orthogonal to `ell,v`, and `(Y,L,V)` is an orthonormal basis of the spectral range of `A`. In these coordinates,

`Q=(a/q)(Y+sqrt(q)rho L/a)^2+(L,V)S_2(L,V)^T`.                    (3.4)

Consequently its `3x3` coefficient matrix is

`B_range = [[a/q, rho/sqrt(q), 0],
            [rho/sqrt(q), rho^2/a+(S_2)11, (S_2)12],
            [0, (S_2)12, (S_2)22]],`                              (3.5)

and has exactly the three nonzero eigenvalues of `A`.

The probabilistic point is source-valid and stronger than a bare joint-density assertion. Conditional on the **entire residual original-coordinate bank**,

`p_(Y|X_J)(y|X_J) <= q^(-1/2)`,                                   (3.6)

because (3.3) is just a translate of `sqrt(q)H`. Hence the same cap remains true after conditioning only on `(L,V)`:

`boxed: ||p_(Y|L,V)||_infinity <= q^(-1/2).`                       (3.7)

Meanwhile the actual two-dimensional bounded-density projection theorem gives

`boxed: ||p_(L,V)||_infinity <= 2.`                               (3.8)

Equations (3.7)-(3.8) are the exact projection-product interface in this nonzero-pivot collar. They do **not** assert independence of `Y,L,V`.

## 4. Exact hub-root formula and cancellation of the dominant star

The same normal form exposes the central failure of the positive-root strategy.

Write the range matrix (3.5) as

`B_range=[[a_tilde,u^T],[u,C_2]]`,

where

`a_tilde=a/q`, `u=(rho/sqrt(q),0)`.                                (4.1)

For a target level `t`, the quadratic discriminant in the conditional `Y` equation has quadratic matrix

`K=u u^T-a_tilde C_2`.                                            (4.2)

A direct substitution from (3.5) gives the exact identity

`boxed: K=-(a/q) S_2.`                                            (4.3)

In particular,

`boxed: det K=(a/q) Delta_A.`                                     (4.4)

The large source-aligned coupling `rho`, which by (2.10) is at least `s sqrt(62/63)` in the hard collar, cancels **completely** from the positive discriminant matrix.

More explicitly, returning to the literal hub and writing `x=X_J`, let

`D_t(x)=(b^T x)^2-a(x^T Cx-t)=a(t-x^T Sx)`.                        (4.5)

For almost every `t`, conditioning on `X_J=x` gives the exact density formula

`p_Q(t)= E[ 1_{D_t>0}/(2 sqrt(D_t))
             * { f_H((-b^T X_J+sqrt(D_t))/a)
                +f_H((-b^T X_J-sqrt(D_t))/a) } ].`                 (4.6)

Replacing the two displayed hub-density values by their cap `1` yields the positive majorant

`p_Q(t) <= E [D_t(X_J)]_+^(-1/2).`                                (4.7)

But by (4.5), this majorant depends only on `aS`; it no longer contains `rho` at all. Thus the hub-root supremum step erases precisely the physical-star quantity that remains order one as `a->0`.

This is the exact algebraic reason the r38 positive trace can diverge logarithmically while the true density stays bounded: the numerator in (4.6), not the discriminant denominator by itself, must participate in the cancellation/source averaging.

### Corollary `QFORM-POSITIVE-DISCRIMINANT-STAR-ERASURE-v1`

In the live collar (2.9), every proof that passes from (4.6) to (4.7) before using original-product structure loses an order-one source coupling `rho>=s sqrt(62/63)`. On the majority-sign branch `a Delta_A<0`, `K` is indefinite by (4.4), and the existing fixed-determinant hyperbolic-cap counterexample shows that no estimate based only on `||p_(L,V)||_infinity` and `|det K|` can repair that loss.

This is a barrier for that proof interface, not a counterexample to QFORM.

## 5. Minority-sign scoped bound with hidden same-bank leakage retained

For completeness, when

`a Delta_A>0`,                                                     (5.1)

`K` in (4.3) is definite. The account02/B16 ellipse/layer-cake argument still works with the conditionally capped range hub (3.7): the root contribution receives the factor `q^(-1/2)`, while the pair density cap is at most `2`. Hence

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(2 pi) q^(-1/4) |a Delta_A|^(-1/4).
`                                                                      (5.2)

This is a legitimate essential-density estimate through arbitrary hidden `P` leakage in (3.2); no conditional projection is declared independent. It is not uniform as `a->0`, so it is only a supporting branch, not the missing punctured-to-zero theorem.

## 6. Designated account04/B16 result applied to an actual target inequality

The newest completed designated-partner theorem is account04/B16 r4,

`yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`,

which gives

`||p_Q||_infinity <= 2*pi/sqrt(|det H_2|)`                          (6.1)

whenever a disjoint original-coordinate product bank enters through a two-dimensional projection with definite quadratic matrix `H_2`; arbitrary affine terms generated by the outside variables are retained.

Apply it to the strict target family

`Q_eta = -H^2 + 2 eta H U + 2U^2+2V^2`,                            (6.2)

where `H` is one original cap-one source and `(U,V)` is any orthonormal two-dimensional projection of a disjoint cap-one product bank. Conditional on `H=h`, the projected plane has

`H_2=diag(2,2)`, `det H_2=4`,                                     (6.3)

while `2 eta h U` is exactly an allowed affine translation. Thus the partner theorem gives, uniformly in every real `eta`,

`boxed: ||p_(Q_eta)||_infinity <= pi.`                             (6.4)

This is an actual owner-target inequality, not a two-eigenvalue control: the carrier matrix

`[[-1,eta,0],[eta,2,0],[0,0,2]]`

has eigenvalues

`2`, `(1+sqrt(9+4eta^2))/2`, `(1-sqrt(9+4eta^2))/2`,              (6.5)

so all three have modulus at least one for every `eta`.

The role of (6.4) here is a source-valid control showing what a definite projected plane can pay outright. It does not pretend that the general majority-sign shared-bank collar has such a definite plane.

## 7. First remaining implication

The first B16 debt is now more precise than r40's generic “no second fresh relay” label:

`QFORM-PUNCTURED-MAJORITY-ROOT-NUMERATOR-v1`.

> In the exact-rank-three collar `q_h>=63/64`, `0<|a|<=s/64`, `a Delta_A<0`, use the exact source formula (4.6) **before** replacing the two values of the untouched original hub density by `1`. The in-range physical star obeys `rho>=s sqrt(62/63)` and the hidden Schur-kernel leakage obeys `tau<=|a|/sqrt(63)`. Prove a uniform bound for (4.6), or force an already-paid source-preserving phase-aligned / three-crossing exit.

The point is quantitative: the positive discriminant denominator (4.5) forgets `rho` identically, while the numerator retains it through the translations `-b^T X_J/a`. A successful proof must keep that root numerator, or an equivalent Fourier/TT* cancellation, until after the original-product averaging. Retrying a bounded joint projection density, arbitrary-joint coarea, pointwise van der Corput, or the old absolute TT* kernel cannot close this branch.

Arbitrary additional nonseparable spectrum remains a separate interface after the exact-rank-three endpoint. Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**, and global continuity remains OPEN.
