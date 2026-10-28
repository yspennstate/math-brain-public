SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-24T10:49:31Z.
attacking: scalar-pivot rank-two currency forcing or paid routing for the bilinear block mechanism.

# account03/B09 r49 — regularized two-volume half-Riesz compiler

Programme: `QFORM-DENSITY-3EIG-20260922`
Role: Bilinear block mechanism / quantitative inequalities and rigorous computations
Run: `20260924T104931Z-account03-B09-QFORM-r49`
Status: **NEW SUPPORTING THEOREMS PENDING INDEPENDENT REVIEW; FULL QFORM OPEN; FULL-TARGET CONTINUITY OPEN**
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN. Every stochastic conditioning below is on ORIGINAL coordinates. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, or post-rotation independence assumption is introduced.

## 1. Fresh sources and exact predecessor debt


The immediate predecessor is

`yspennstate/math-open-problems@1701e5a05a12b35a3c5100ff343d02c75d5c9a84`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T094653Z-account03-B09-QFORM-r48/REPORT.md`.

That run proved a scalar-pivot plus exact grouped-rank-two crossing bound but left the structural debt: force or route the currency after the scalar pivot. The present run changes mechanism. It uses the completed regularized-determinant cross estimate to aggregate **all two-volume before selecting singular directions**, thereby remaining stable when a rank-two crossing is contaminated by arbitrarily many tiny extra singular directions.

The main dependency is the complete supporting proof

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`

`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

Its Section 5 proves: for any original-coordinate cross block `C=A[I,J]`, arbitrary same-side measurable phases, and `1<=q<2`, if the maximum coordinate leverage of `range(C)` on one physical side is at most `q/2`, then

`|phi(t)| <= det(I + [2q/(pi^2 e^2)] t^2 C C^T)^(-1/(4q)).`   (1.1)

The source status is a complete supporting analytic argument with independent review still pending; this run does not upgrade that review status.

The fractional-potential representation used in r48 is also retained:

`E|R-w|^(-1/2) <= (2pi)^(-1/2) int_R |t|^(-1/2)|phi_R(t)| dt.` (1.2)

The live correction inbox was reread before publication. In particular nothing here uses law-uniform pointwise quadratic-phase decay, post-rotation independence, a bounded arbitrary-joint coarea theorem, fiberwise supremum integration, deletion of small quadratic terms, or a claim that one physical minor has universal scale.

## 2. Two-volume notation

For a real matrix C with singular values `s_1,s_2,...`, define the second elementary singular-value energy

`E_2(C) := sum_(i<j) s_i^2 s_j^2.`                         (2.1)

By Cauchy--Binet,

`E_2(C) = sum_(|I|=|J|=2) det(C[I,J])^2
        = || wedge^2 C ||_HS^2.`                           (2.2)

This is the aggregate physical two-volume. It is stable under adding arbitrarily small extra singular directions; unlike a product of all nonzero singular values it does not acquire a reciprocal tiny-singular-value loss.

## 3. New theorem: leverage-controlled aggregate half-Riesz bound

Let Y and Z be disjoint banks of ORIGINAL independent cap-one coordinates and let

`R = F(Y) + 2 Y^T C Z + G(Z)`                              (3.1)

where F and G are arbitrary measurable real functions, finite almost surely. Let `theta` be the maximum diagonal entry of the orthogonal projection onto `range(C)` in the Y-coordinate space. One may swap the two sides and use the smaller available leverage.

### Theorem 3.1 — `QFORM-REGDET-TWOVOLUME-HALFRIESZ-v1`

Assume `E_2(C)>0`. For every

`q in [1,2)` with `theta <= q/2`,                           (3.2)

one has

`boxed:
 sup_w E|R-w|^(-1/2) <= K_q E_2(C)^(-1/8),`                (3.3)

where

`K_q = sqrt(e) 2^(-7/4) q^(-1/4)
       B(1/8,(2-q)/(8q)).`                                  (3.4)

In particular

`K_1 = sqrt(e) 2^(-7/4) B(1/8,1/8)
     = 7.673759290384858...`                                (3.5)

when `theta<=1/2`, and

`K_(3/2)=14.065344806406538...`                             (3.6)

when `theta<=3/4`.

### Proof

Apply (1.1) to R. Put

`gamma_q = 2q/(pi^2 e^2).`

Expanding the determinant in elementary symmetric functions gives

`det(I + gamma_q t^2 C C^T)
 >= 1 + gamma_q^2 t^4 E_2(C).`                              (3.7)

Therefore

`|phi_R(t)| <= [1 + beta t^4]^(-1/(4q)),`
`beta = gamma_q^2 E_2(C).`                                  (3.8)

Insert (3.8) into (1.2). Since q<2, the resulting integral converges at infinity. Scaling `u=beta^(1/4)t` gives

`int_R |t|^(-1/2)[1+beta t^4]^(-1/(4q)) dt
 = beta^(-1/8) * (1/2)
   B(1/8,(2-q)/(8q)).`                                      (3.9)

Also

`beta^(-1/8)
 = pi^(1/2)e^(1/2)(2q)^(-1/4) E_2(C)^(-1/8).`              (3.10)

Multiplying by `(2pi)^(-1/2)` yields exactly (3.3)--(3.4). No density of R is assumed in advance. QED.

### Interpretation

At rank exactly two, r48 already gave a grouped half-Riesz estimate in terms of the product of the two nonzero singular values. The new point is robustness to **extra nonzero directions**. Equation (3.3) depends only on the aggregate two-volume `E_2(C)` and does not multiply or invert the additional small singular values. This is a genuine new interface for a near-rank-two Schur crossing.

## 4. Scalar pivot converts the two-volume half potential directly to O(length)

Choose a literal original coordinate h with `a=A_hh !=0` and condition on any original coordinates outside the retained banks. Complete only X_h:

`Q = a (X_h + ell/a)^2 + R,`                               (4.1)

where ell is affine in the remaining original variables and R is the exact Schur remainder. Let C be any cross block of R between disjoint original-coordinate banks Y,Z satisfying Theorem 3.1.

For every fixed value of the remaining variables, `X_h+ell/a` is only a translation of the original cap-one density. Hence the density of the square term obeys

`p_(a(X_h+ell/a)^2)(u) <= |a|^(-1/2)|u|^(-1/2)`            (4.2)

on the appropriate half-line. Averaging gives

`p_Q(t) <= |a|^(-1/2) E|t-R|^(-1/2).`                      (4.3)

Combining with Theorem 3.1 proves:

### Theorem 4.1 — `QFORM-SCALARPIVOT-REGDET-TWOVOLUME-v1`

Under (3.2),

`boxed:
 ||p_Q||_infinity
 <= K_q |a|^(-1/2) E_2(C)^(-1/8).`                         (4.4)

Consequently, for every interval I,

`boxed:
 P{Q in I}
 <= K_q |a|^(-1/2) E_2(C)^(-1/8) |I|.`                    (4.5)

This is the requested no-square-root-loss conversion: the bilinear bank is spent at inverse-half-potential scale, and the literal scalar square converts it directly into a linear interval bound. The proof establishes an essentially bounded density. It does **not** separately establish continuity.

## 5. Random disjoint partition identity and third-compound polynomial currency

Let S be the scalar Schur complement after the h-pivot, on the remaining original coordinates. Define the disjoint two-minor energy

`D_2^disj(S)
 := sum_{I,J: |I|=|J|=2, I cap J=emptyset}
       det(S[I,J])^2.`                                      (5.1)

Randomly color every remaining coordinate independently Y or Z with probability 1/2 and put `C=S[Y,Z]`. By (2.2), every ordered disjoint pair `(I,J)` contributes to `E_2(C)` precisely when `I subset Y` and `J subset Z`, which has probability `1/16`. Therefore

`boxed:
 E_partition E_2(S[Y,Z]) = D_2^disj(S)/16.`                (5.2)

Hence some physical disjoint partition satisfies

`E_2(S[Y,Z]) >= D_2^disj(S)/16.`                           (5.3)

This statement alone does not force the leverage condition; that is kept explicit rather than silently assumed.

The Schur minors polynomialize exactly. For disjoint two-subsets I,J excluding h,

`det A[{h} union I,{h} union J] = a det S[I,J].`            (5.4)

Define

`T_h(A) := sum_{I,J disjoint, |I|=|J|=2}
              det A[hI,hJ]^2.`                              (5.5)

Then

`T_h(A)=a^2 D_2^disj(S).`                                  (5.6)

Thus whenever a partition attaining (5.3) also has leverage at most `q/2`, Theorem 4.1 yields the fully polynomial certificate

`boxed:
 ||p_Q||_infinity
 <= sqrt(2) K_q [a^2 T_h(A)]^(-1/8).`                      (5.7)

No reciprocal physical 2x2 or 3x3 minor appears. The scaling is correct: `a^2 T_h` has coefficient degree eight, and the `-1/8` power has density scale degree minus one.

The checker verifies (5.2) by exhaustive averaging over all 64 bipartitions of a seeded 6x6 symmetric matrix and verifies (5.4) on 1000 seeded matrices.

## 6. Exact physical-row two-volume localization identity

For any C, set `M=C C^T`. For physical row i define

`W_i := sum_{j != i} sum_{|K|=2} det C[{i,j},K]^2.`         (6.1)

Using the squared area identity for two row vectors and summing j,

`boxed:
 W_i = M_ii tr(M) - (M^2)_ii.`                             (6.2)

Summing i gives

`boxed:
 sum_i W_i = 2 E_2(C).`                                    (6.3)

If C has exact rank two, write `C=U diag(s_1,s_2)V^T` with `U^T U=I_2` and let `ell_i=||U_{i,:}||^2`, the physical row leverage. Then (6.2) simplifies to

`boxed:
 W_i=(s_1 s_2)^2 ell_i.`                                   (6.4)

Therefore failure of the diffuse threshold `ell_i<=3/4` has a precise consequence: one literal physical row carries more than three quarters of the entire rank-two Pluecker energy. This does NOT by itself prove a density bound; the correction `QFORM-ONE-HEAVY-ROW-SAME-SQUARE-ABSORPTION-FALSE-v1` forbids treating one heavy coefficient plus a square as sufficient when arbitrary same-bank curvature is retained. Instead (6.4) identifies the exact next branch: keep the heavy row and the remaining two-volume jointly and apply conditional linear anti-concentration without deleting the coupled curvature.

## 7. Target-valid near-rank-two stress family with arbitrarily many tiny directions

Let r>=2 and m=2r. Put

`U = (1/sqrt(2)) [ I_r ; I_r ]`,                            (7.1)

so U has orthonormal columns and every physical row leverage equals `1/2`. Let

`Sigma_eps = diag(2,2,eps,...,eps)`                          (7.2)

with r-2 copies of eps, and define the m-by-m cross block

`C_eps = U Sigma_eps U^T.`                                 (7.3)

Use the full symmetric coefficient matrix

`A = [ 1   0    0
       0   0    C_eps
       0 C_eps^T 0 ].`                                     (7.4)

The literal first coordinate is a scalar pivot `a=1`. The bipartite block has eigenvalues plus/minus the singular values of C_eps, hence the full spectrum contains

`1, +2,-2,+2,-2`                                           (7.5)

for every r and eps>0. Thus the owner target hypothesis holds uniformly.

The cross range leverage is exactly 1/2, so q=1 applies. Moreover

`E_2(C_eps)
 = 16 + 8(r-2) eps^2 + binom(r-2,2) eps^4
 >=16.`                                                     (7.6)

Theorem 4.1 therefore gives the uniform bound

`boxed:
 ||p_Q||_infinity
 <= K_1 16^(-1/8)
 = 5.426167231424402...`                                    (7.7)

for every r and every eps>0.

By contrast, any exact-rank-r certificate based on the product of all nonzero singular values pays

`prod_j s_j = 4 eps^(r-2)`                                 (7.8)

and deteriorates as eps->0. Thus (7.7) genuinely removes the tiny-extra-direction product loss while retaining arbitrary same-side phases in the theorem.

The deterministic checker tested r=2,4,8 and eps=10^-2,10^-8. It verified leverage 1/2, the exact formula (7.6), and at least five eigenvalues of modulus at least one in every case.

## 8. Required account04/B09 partner result applied to an actual inequality

The designated partner result is

`yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.

It proves that a literal invertible 3x3 original-coordinate cross block K, with arbitrary same-side curvature and outside couplings retained, gives a continuous density satisfying

`||p_Q||_infinity <= 3 |det K|^(-1/3).`                    (8.1)

Apply it to

`K=diag(6,2,1),
 A_*=[0 K; K 0].`                                          (8.2)

The spectrum is `{-6,-2,-1,1,2,6}`, so the target hypothesis holds. Since `det K=12`,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= 3*12^(-1/3)
 = 1.310370697104448...`                                    (8.3)

and the same coefficient multiplies interval length. This partner branch has a continuous density.

## 9. What is and is not closed

Newly paid in this run:

* a scalar pivot plus a cross block with nontrivial aggregate two-volume and leverage strictly below one;
* stability through arbitrarily many tiny additional cross singular values;
* a direct O(interval length) conclusion with no square-root small-ball decoupling;
* an exact random-partition compiler for disjoint Schur two-volume;
* an exact polynomial third-compound form of that currency;
* an exact heavy-row localization identity for the complementary rank-two geometry.

Still open:

* the bare three-large-eigenvalue hypothesis does not yet force a scalar pivot and a disjoint partition satisfying both a universal lower bound on `a^2 T_h(A)` and a leverage threshold;
* the high-leverage complementary branch must keep the heavy physical row **and** the remaining two-volume/curvature jointly; one-heavy-row absorption alone is already refuted by the live corrections;
* zero scalar pivots require a separate off-diagonal or finite-core route;
* full-target continuity is not obtained from Theorem 4.1.

The next precise B09 debt is therefore

`QFORM-HEAVYROW-TWOVOLUME-CONDITIONAL-LINEAR-v1`:

when every useful two-volume partition has a physical leverage >3/4, use (6.2)--(6.4) to isolate the heavy original coordinate, retain the complementary Pluecker mass and arbitrary same-side curvature, and prove a translation-uniform inverse-half-potential bound by conditional linear anti-concentration. The bound must remain linear in interval length after the scalar pivot and must not reduce to the refuted one-heavy-coefficient shortcut.

Full unrestricted QFORM remains OPEN. Full-target continuity remains OPEN.

## 10. Deterministic verification

`CHECK.py` and `CHECK_OUTPUT.txt` are in this immutable run directory. Results:

* 1000 seeded Schur-minor identities: maximum relative error `7.675e-16`;
* 1000 Cauchy--Binet two-volume identities: maximum relative error `2.554e-15`;
* exhaustive 64-partition identity (5.2): absolute error `5.329e-15`;
* `B(1/8,1/8)=15.655373151252725`;
* `K_1=7.673759290384858`;
* `K_(3/2)=14.065344806406538`;
* stress-family uniform q=1 bound `5.426167231424402`;
* partner inequality (8.3): `1.310370697104448`;
* all assertions passed.

These computations check algebra/constants and finite stress instances only; the proofs above are analytic.
