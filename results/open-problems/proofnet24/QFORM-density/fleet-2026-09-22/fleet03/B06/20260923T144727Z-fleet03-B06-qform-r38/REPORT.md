SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T14:47:27Z.
attacking: upgrade the low-disjointness aggregate E2 survivor by lifting the entire anchored cofactor bank into physical three-volume before inversion; otherwise force a quantitative recursive near-rank-two core.

# fleet03/B06 r38 — anchored cofactor -> three-volume lift or recursive rank-two core

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`, programme revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Status:** `NEW SUPPORTING DICHOTOMY / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and freshest proof-graph position

The unrestricted target remains open: for every dimension, independent ORIGINAL real coordinates with densities bounded by one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `Q=X^TAX`, or give a valid counterexample. No moment, support, Gaussian, log-concavity, iid, sign, finite-rank, or diagonal-basis assumption is introduced. A spectral rotation is never used to manufacture independence. Continuity remains a separate desired conclusion.

The fresh fleet04/B20 theorem actually used below is

`yspennstate/math-open-problems@3671f29afb89083947437ffc4ebbb037aba58a4d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T142031Z-fleet04-B20-QFORM-r10/REPORT.md`.

It supplies, in the no-moderate-diagonal `N3(1/64)` regime, a literal ORIGINAL-coordinate partition `[n]=J disjoint_union K` and cross block `N=A[J,K]` with

`E:=||N||_F^2 > c3:=11907/16384`.                                      (1.1)

Its later compiler leaves an absolute rank-two cross tube; in particular it never authorizes deleting the small nonzero tail.

The immediate local input is the concurrently completed B06 r37 packet

`yspennstate/math-open-problems@fa9d5dd3cc78a092484480b536872d332e22c90a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T141825Z-fleet03-B06-qform-r37/REPORT.md`.

In its low determinant-disjointness branch there is a physical row anchor `i in J` and column anchor `a in K`. After permuting only coefficient labels, write

`N = [[b, r^T], [c, D]]`,                                               (1.2)

and define the complete anchored cofactor matrix

`C := bD-c r^T`.                                                        (1.3)

R37 proves

`||C||_F > (sqrt(3937)/1024) E`.                                       (1.4)

Combining the *actual fleet04/B20 inequality* (1.1) with (1.4) gives the absolute currency

`L:=||C||_F > L0`,

`L0 := sqrt(3937)*11907/16777216
      =0.04453127861416368...`,                                        (1.5)

and hence

`L^2 > L0^2 = 558174667113/281474976710656
              =0.001983034775012271...`.                               (1.6)

The designated `fleet04/B06` current-QFORM directory still has no completed theorem at this run's source check; I do not fabricate one. The completed fleet04/B20 theorem above is the compatible fleet04 result actually applied at (1.1)->(1.5).

Consumed corrections include: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint 3D coarea is false; post-rotation independence is false; positive moments of worst conditional projected-density caps are false; unrestricted fiber suprema lose dimension; no single good minor need carry aggregate determinant mass; and a small nonzero quadratic tail cannot be deleted for arbitrary unbounded inputs.

## 2. Exact cofactor-to-three-volume identity

For a matrix `M`, write `e_k(M^TM)` for the sum of squares of all physical `k x k` minors. For the block (1.2), define the anchored third-volume

`W3(i,a)
 := sum_{j<k, alpha<beta}
    det N[{i,j,k},{a,alpha,beta}]^2`,                                  (2.1)

where `j,k` run over the non-anchor rows and `alpha,beta` over the non-anchor columns.

### Lemma 2.1 — `QFORM-ANCHOR-COFACTOR-E3-IDENTITY-v1`

If `b!=0`, then

`boxed: W3(i,a)=b^(-2) e_2(C^T C).`                                   (2.2)

Consequently

`e_3(N^T N) >= b^(-2)e_2(C^T C)`.                                    (2.3)

#### Proof

Fix two non-anchor rows `j,k` and columns `alpha,beta`. The corresponding anchored `3 x 3` minor is

`det [[b,r_alpha,r_beta],
      [c_j,D_jalpha,D_jbeta],
      [c_k,D_kalpha,D_kbeta]]`.

Taking the Schur complement of the scalar `b` gives

`= b det(D[{j,k},{alpha,beta}]
          - b^(-1)c_{j,k} r_{alpha,beta}^T)`
`= b det(b^(-1) C[{j,k},{alpha,beta}])`
`= b^(-1) det C[{j,k},{alpha,beta}].`                                 (2.4)

Squaring and summing over all physical leaf pairs gives (2.2) by Cauchy-Binet. Since (2.1) is a sub-sum of the full physical third-volume, (2.3) follows. QED.

This identity is the core curved-fiber replacement: the whole anchored two-cofactor bank is summed first, and only then is it converted into third curvature. No reciprocal individual `2 x 2` minor is selected.

## 3. Complementary rank-one stability is dimension-free

Let `y_1>=y_2>=...>=0` be the squared singular values of `C`, so

`L^2=sum_j y_j`,
`e_2(C^TC)=sum_{j<k} y_j y_k`.                                        (3.1)

### Lemma 3.1 — `QFORM-COFACTOR-E2-OR-RANK1-v1`

For every `tau>0`, if

`e_2(C^TC) < tau b^2 L^2`,                                            (3.2)

then

`boxed: dist_F(C, rank<=1)^2 < 2 tau b^2.`                            (3.3)

#### Proof

Since

`sum_j y_j^2 = L^4-2e_2(C^TC)`                                      (3.4)

and `sum_j y_j^2 <= y_1 sum_j y_j = y_1L^2`, (3.2) implies

`y_1 > L^2-2tau b^2`.                                                 (3.5)

The squared Frobenius distance to the best rank-one approximation is

`sum_{j>=2} y_j = L^2-y_1 <2tau b^2`.                                (3.6)

QED.

Thus failure of the three-volume lift is not an unstructured bad case: the *entire cofactor matrix* is forced close to rank one, independently of the number of physical coordinates.

Moreover, because `C=bD-cr^T`, if `b!=0` and `R1` is a best rank-one approximation to `C`, then

`D_2 := b^(-1)(cr^T+R1)`                                               (3.7)

has rank at most two and

`boxed: dist_F(D,rank<=2)
 <= ||C-R1||_F/|b|
 < sqrt(2tau).}`                                                       (3.8)

Again the whole residual cross core is retained; no random quadratic tail is dropped.

## 4. Third-volume receiver and a parametric dichotomy

The completed source-pinned D-prime theorem is in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`.

For an ORIGINAL-coordinate cross block with full third-volume

`Z=e_3(N^TN)>0`,                                                       (4.1)

if the canonical determinant-squared three-minor law has every row-inclusion marginal at most `h<3/4`, then the full ambient quadratic form, with arbitrary same-bank quadratic terms and outside couplings retained, has a continuous density satisfying

`||p_Q||_infinity
 <=6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) Z^(-1/6).`                         (4.2)

The same theorem applies to `N^T`, so either physical side can supply the diffuse marginal gate.

### Theorem 4.1 — `QFORM-ANCHORED-COFACTOR-E3-OR-RECURSIVE-RANK2-v1`

Assume the r37 anchored state (1.2)-(1.6), `b!=0`. Fix `tau>0`. Then at least one of the following holds.

**A. Three-volume diffuse payment.** If

`e_2(C^TC) >= tau b^2L^2`                                              (4.3)

and the canonical full three-volume law of `N` has maximum row marginal at most `2/3` on either the row side or the column side, then `Q` has a continuous density and

`boxed:
 ||p_Q||_infinity
 <=9 sqrt(3e) (tau L^2)^(-1/6)
 <9 sqrt(3e) (tau L0^2)^(-1/6).}`                                    (4.4)

**B. Nested three-volume anchors.** If (4.3) holds but (4.4)'s marginal hypothesis fails on both orientations, then there is a physical row and a physical column each contained in more than `2/3` of the canonical squared three-minor volume of `N`. This is a genuine nested double-anchor certificate, not a selected large minor.

**C. Recursive low-rank cofactor.** If (4.3) fails, then

`boxed: dist_F(C,rank<=1)<sqrt(2tau)|b|`,                              (4.5)

and

`boxed: dist_F(D,rank<=2)<sqrt(2tau).}`                                (4.6)

#### Proof

Under (4.3), Lemma 2.1 gives

`Z=e_3(N^TN)>=b^(-2)e_2(C^TC)>=tau L^2`.                              (4.7)

If one orientation has all three-volume inclusion marginals at most `2/3`, apply (4.2) with `h=2/3`; its coefficient is exactly `9sqrt(3e)`. This proves A. If neither orientation satisfies the gate, the definitions give B. If (4.3) fails, Lemma 3.1 and (3.8) give C. QED.

The theorem uses the complete aggregate cofactor volume before inversion. It never replaces a curved intersection by its fiber maximum.

## 5. Concrete `tau=1/64` collar in the live r37 state

Set

`tau=1/64`.                                                            (5.1)

### 5.1 Paid third-volume branch

From (1.6) and (4.7),

`Z > L0^2/64
   = 3.098491835956674e-5`.                                            (5.2)

Therefore any orientation with maximum third-volume row marginal at most `2/3` is continuously paid by

`boxed: ||p_Q||_infinity <145.019137684 <145.020.}`                   (5.3)

If not, both physical sides carry `>2/3` three-volume anchors, giving the nested-double-anchor branch.

### 5.2 Cofactor-near-rank-one branch

If (4.3) fails, then

`dist_F(C,rank<=1)
 < |b|/(4sqrt(2)).`                                                     (5.4)

R37's non-pair branch has `|b|<1/32`, hence

`boxed: dist_F(C,rank<=1)<1/(128sqrt(2))
       =0.005524271728... .}`                                          (5.5)

Because `L>L0`, the nonleading cofactor energy is at most

`dist_F(C,rank<=1)^2/L^2
 <0.015389331`,                                                        (5.6)

so

`boxed: sigma_1(C)^2/||C||_F^2 >0.984610669.}`                         (5.7)

Thus the cofactor obstruction is quantitatively one-dimensional in Frobenius energy.

For the r37 **large-core** survivor one additionally has

`||D||_F > (sqrt(3937)/64)E
          >0.7125004578266`.                                           (5.8)

Equation (4.6) becomes

`dist_F(D,rank<=2)<1/(4sqrt(2))=0.1767766953...`,                      (5.9)

and therefore

`boxed:
 dist_F(D,rank<=2)^2/||D||_F^2 <0.061557324,
 sum_{j<=2}s_j(D)^2/||D||_F^2 >0.938442676.}`                         (5.10)

This is a strict recursive product-coordinate reduction: after deleting only the already-designated physical anchor row and column from the *coefficient matrix*, the full residual cross core `D` is trapped within a dimension-free Frobenius tube around rank two. The quadratic form itself is never replaced by the rank-two approximation; the residual tail stays in the next receiver.

At the exact `b=0` endpoint, `C=-cr^T` is rank one identically. The present cofactor-to-E3 division by `b` is not used; that endpoint remains routed to the completed B06 zero-anchor double-star/wedge mechanism rather than being obtained by an illegal limit.

## 6. What this removes and what remains

Relative to r37, the low-disjointness small-edge branch is now split into much narrower outcomes:

1. a **continuous full-density payment `<145.020`** whenever the anchored cofactor has enough second exterior volume and one physical side of the resulting third-volume law is diffuse;
2. a **nested row/column three-volume anchor** if third curvature exists but is concentrated on both physical sides;
3. a **98.46%-energy rank-one cofactor** if that third curvature is absent;
4. and, on r37's large-core subbranch, a **93.84%-energy rank-two residual core** on strictly smaller original-coordinate banks.

The high determinant-disjointness r37 branch still has only the valid fractional credit

`sup_s E|Q-s|^(-1/2)<24.121`;                                         (6.1)

that estimate by itself does not imply an `L^infinity` density and is not promoted here.

The next exact B06 debt is

`QFORM-ABSOLUTE-RANK2-TUBE-TAIL-RETAINING-RECEIVER-v1`:

> On the recursive rank-two core produced by (5.9)-(5.10), retain its small but nonzero cross tail and arbitrary same-bank quadratic curvature, and either (i) combine a second independent aggregate curvature currency with the rank-two half-Riesz estimate to reach an actual density bound, or (ii) route the near-rank-two core into the existing nested-anchor / mixed-hub / physical-pair receivers without selecting a reciprocal local minor.

A parallel debt is to upgrade the high-disjointness half-Riesz branch (6.1) without assuming a fresh independent square.

## 7. Status and integrity

`QFORM-ANCHOR-COFACTOR-E3-IDENTITY-v1`: **PROVED supporting identity**.  
`QFORM-COFACTOR-E2-OR-RANK1-v1`: **PROVED supporting lemma**.  
`QFORM-ANCHORED-COFACTOR-E3-OR-RECURSIVE-RANK2-v1`: **PROVED supporting dichotomy**.  
Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.  
Universal continuity: **OPEN**; continuity is proved here only on branch A by D-prime.

No pointwise Fresnel shortcut, arbitrary-joint coarea, conditional-density moment, spectral-coordinate independence, unrestricted fiber supremum, one-good-minor extraction, or small-tail deletion is used.