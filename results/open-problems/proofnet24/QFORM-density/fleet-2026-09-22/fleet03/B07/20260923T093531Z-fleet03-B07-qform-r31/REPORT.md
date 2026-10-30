SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T09:35:31Z.
attacking: the designated partner's diffuse row/column-star survivor — resolve overlap/misalignment by a dimension-free disjoint-innovation selection, then force either determinant-balanced mixed-minor mass or a quantitative rank-one/common-bank tube.

# fleet03/B07 r31 — diffuse two-star overlap compiler

## Status

`NEW_SUPPORTING_COORDINATE_SELECTION_THEOREMS / DESIGNATED_PARTNER_APPLIED / ONE_STRONGLY_TRANSVERSE_LOW-CURVATURE_SUBBRANCH_CONTINUOUSLY_PAID / FULL_QFORM_OPEN / FULL_CONTINUITY_OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains open. Nothing below assumes Gaussianity, moments, log-concavity, compact or connected support, post-rotation independence, a uniformly good individual minor, or law-uniform pointwise quadratic-phase decay.

The main new point is structural and exactly matches the B07 assignment: a pair of physically diffuse stars cannot remain an amorphous overlap obstruction. Without selecting or reciprocating a single small coordinate minor, it has a dimension-free original-coordinate compiler into (i) two genuinely disjoint innovations, and more sharply (ii) a determinant-balanced transverse two-frame, (iii) a positive aggregate mixed-minor bank, or (iv) a quantitative rank-one tube with four common physical banks.

## 1. Sources actually used

### 1.1 Designated partner fleet04/B07

For the first time in this slot's current-QFORM sequence, the designated partner has a completed current artifact:

`yspennstate/math-open-problems@842652e93680813d356fde0f15f12ab70b59c3c3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B07/20260923T091740Z-fleet04-B07-actual-core-diffuse-banks-r1/REPORT.md`.

Its unpaid N3 rank-four survivor gives an actual physical row star and an actual physical column star, with norms exceeding

`h=(2 sqrt(2)-1)/1572864
  =1.1624826588606455e-6`,                                    (1.1)

and, after its fixed choice `tau_0=h^2/128`, every physical coefficient is at most

`delta_tau0 <= h/8`.                                          (1.2)

The partner itself identifies the remaining geometric obstruction: its row-bank and column-bank systems may overlap or be misaligned, so one may not simply declare the two systems independent.

This report attacks exactly that obstruction.

### 1.2 Two-hub Pluecker smoothing

For the strongly transverse subbranch I also use the completed fleet02/B09 theorem

`QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`,

canonical source

`yspennstate/math-open-problems@bc348aa1a3631b0a0a3a9939cbb6b023578e9abc`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T064043Z-fleet02-B09-QFORM-r13/REPORT.md`.

For two literal physical hubs whose two coupling rows into a leaf bank have Gram determinant `Delta`, if the leaf principal block is diagonal (`r=0` in that theorem) and the whitened two-frame has determinant-weighted disjoint-basis probability `rho>0`, then the full ambient quadratic form, including an arbitrary actual 2x2 hub core and arbitrary conditioned outside couplings/affine terms, has a continuous density satisfying

`||p_Q||_infinity <= 2 sqrt(e) [rho Delta]^(-1/4)`.            (1.3)

I apply (1.3) only at that exact scope. The general partner survivor has arbitrary same-side leaf curvature, so (1.3) is not silently promoted to the full branch.

## 2. Abstract two-star notation

Let `r=(r_j)` and `c=(c_j)` be two real physical coefficient vectors on one common coordinate ground set; padding a vector by zeros is allowed. Write

`R=||r||_2`, `C=||c||_2`, `delta=max(||r||_infinity,||c||_infinity)`. (2.1)

The mixed second-compound/wedge currency is

`W^2 := sum_{j<k}(r_j c_k-r_k c_j)^2
      = R^2 C^2-(r dot c)^2`.                                 (2.2)

Equivalently, if `V` is the matrix with rows `r,c`, then

`W^2=E_2(V)=s_1(V)^2 s_2(V)^2`.                               (2.3)

This is aggregate determinant weight; no individual `2x2` coordinate minor is distinguished.

## 3. New theorem A — disjoint innovation selection

### Theorem `QFORM-TWOSTAR-DISJOINT-INNOVATION-v1`

Assume

`delta <= min(R,C)/8`.                                        (3.1)

Then there is a partition of the physical coordinates into disjoint sets `S,T` such that

`||r_S||_2^2 ||c_T||_2^2 >= (63/256)R^2C^2`.                 (3.2)

Consequently

`||r_S||_2 >= (sqrt(63)/16)R`,
`||c_T||_2 >= (sqrt(63)/16)C`.                                (3.3)

### Proof

Color each physical coordinate independently into `S` with probability `1/2` and put the remaining coordinates in `T`. Define

`U=sum_j 1_{j in S} r_j^2`,
`Z=sum_k 1_{k in T} c_k^2`.                                  (3.4)

The same-coordinate product never appears, while for `j!=k`,

`P(j in S,k in T)=1/4`.                                      (3.5)

Therefore

`E[UZ]
 =(1/4)(R^2C^2-sum_j r_j^2c_j^2)`.                           (3.6)

Using the physical coefficient cap,

`sum_j r_j^2c_j^2
 <= ||r||_infinity^2 C^2
 <= delta^2 C^2
 <= R^2C^2/64`.                                               (3.7)

Hence

`E[UZ]>=63R^2C^2/256`.                                       (3.8)

Some deterministic coloring achieves at least the expectation, proving (3.2). Since `U<=R^2` and `Z<=C^2`, (3.2) separately implies (3.3). QED.

### Partner application

By (1.1)-(1.2), the designated partner's two stars satisfy (3.1), so there are **disjoint original-coordinate innovation banks** with

`||r_S||_2,||c_T||_2
 > (sqrt(63)/16)h
 =5.766825035194508e-7`.                                      (3.9)

Thus the partner's overlap/misalignment obstruction is completely removed at the level of two linear innovations. This is not yet a curved quadratic receiver: arbitrary quadratic terms involving the same banks are still present and are not conditioned away.

## 4. New theorem B — transverse minor bank or rank-one/common-bank tube

The previous theorem always produces disjoint innovations, but it does not reveal whether the *pair* of stars has genuine two-dimensional determinant content. The next result gives an exhaustive dimension-free structural alternative.

### Theorem `QFORM-TWOSTAR-WEDGE-OR-RANKONE-BANKS-v1`

Assume (3.1). Then the star pair falls into one of the following three quantitative regimes.

#### T1: strongly transverse

If

`W >= RC/2`,                                                  (4.1)

then the whitened physical two-frame is determinant-balanced in the precise sense proved in Section 5: its determinant-weighted disjoint-basis probability satisfies

`rho>=1/2`.                                                    (4.2)

#### T2: moderately transverse

If

`RC/9 <= W < RC/2`,                                           (4.3)

there is a physical bipartition `S union T` for which the aggregate mixed-minor mass crossing the cut obeys

`sum_{j in S,k in T}(r_j c_k-r_k c_j)^2
 >= W^2/2
 >= R^2C^2/162`.                                             (4.4)

#### T3: strongly aligned / quantitative rank-one tube

If

`W < RC/9`,                                                   (4.5)

then, for a suitable sign `sigma in {+1,-1}` and normalized stars `u=r/R`, `v=c/C`,

`||u-sigma v||_2
 < d_0:=sqrt(2-2sqrt(80)/9)
 =0.11128351180739575 <1/8`.                                  (4.6)

Moreover the two-row coefficient matrix is quantitatively close to rank one:

`dist_F(V,rank<=1)=s_2(V)
 < ||V||_F/(9sqrt(2))
 <0.078568 ||V||_F`.                                          (4.7)

Finally there are four pairwise disjoint original-coordinate banks `B_1,...,B_4` on each of which **both** stars remain large:

`||r_(B_q)||_2 >= R/4`,
`||c_(B_q)||_2 > C/8`, `q=1,...,4`.                           (4.8)

### Proof of T2

For a random half-coloring, every unordered coordinate pair `{j,k}` is separated with probability exactly `1/2`. Therefore the expected cut mixed-minor mass equals `W^2/2`; some cut achieves at least that amount. Equation (4.4) follows from `W>=RC/9`.

### Proof of T3

From (2.2) and (4.5),

`|(r dot c)/(RC)| > sqrt(1-1/81)=sqrt(80)/9`.                 (4.9)

Choose `sigma` to make the normalized inner product positive. Then

`||u-sigma v||_2^2
 =2-2|u dot v|
 <2-2sqrt(80)/9`,                                             (4.10)

which is (4.6).

For the rank-one tube, (2.3) gives `s_1s_2=W`. Since

`s_1>=||V||_F/sqrt(2)`                                       (4.11)

and

`RC<=(R^2+C^2)/2=||V||_F^2/2`,                               (4.12)

we obtain

`s_2=W/s_1
 < [||V||_F^2/18]/[||V||_F/sqrt(2)]
 =||V||_F/(9sqrt(2))`.                                       (4.13)

For the common-bank statement, `||u||_infinity<=1/8`. Apply the designated partner's elementary greedy four-bank lemma to `u`, obtaining disjoint banks with

`||u_(B_q)||_2>=1/4`.                                        (4.14)

Then by (4.6),

`||v_(B_q)||_2
 >=||u_(B_q)||_2-||u-sigma v||_2
 >1/4-d_0
 >1/8`.                                                      (4.15)

Rescaling proves (4.8). QED.

### Partner-scale consequence

For the designated partner, T2 gives the explicit cancellation-free physical minor bank

`sum_cross det^2 > h^4/162
 =1.1272777052964666e-26`.                                   (4.16)

T3 instead gives a genuine relative `1/(9sqrt(2))` rank-one tube, plus four common banks each carrying row-star norm `>h/4` and column-star norm `>h/8`. This is a substantially sharper low-tail statement than merely saying that the two bank systems overlap.

## 5. New theorem C — physical diffusion forces Pluecker disjointness in T1

The strongly transverse branch can be sharpened to the exact determinant-balanced currency required by current mixed-hub Fourier theorems.

Let the physical coefficient frame be the `m x 2` matrix

`Cmat_j=(r_j,c_j)`,                                           (5.1)

with Gram matrix

`G=Cmat^T Cmat
  =[[R^2,r dot c],[r dot c,C^2]]`.                            (5.2)

Assume the more general transversality bound

`W>=eta RC`.                                                  (5.3)

Whiten deterministically,

`U=Cmat G^(-1/2)`, so `U^TU=I_2`.                             (5.4)

Let `ell_j=||U_j||_2^2` be the physical leverage and let

`w_{jk}=det(U[{j,k},:])^2`                                   (5.5)

be the Pluecker basis law. If two iid basis pairs drawn from `w` are `S,T`, denote

`rho=P(S cap T=empty)`.                                       (5.6)

### Theorem `QFORM-DIFFUSE-2FRAME-PLUCKER-DISJOINT-v1`

Under (3.1) and (5.3),

`max_j ell_j <= 1/(16 eta^2)`,                               (5.7)

and therefore

`rho >= 1-1/(8 eta^2)`.                                      (5.8)

In particular, in T1 (`eta=1/2`),

`max_j ell_j<=1/4`, `rho>=1/2`.                              (5.9)

### Proof

Since `det G=W^2>=eta^2R^2C^2`,

`lambda_min(G)
 >= det(G)/tr(G)
 >= (eta^2/2) min(R,C)^2`.                                   (5.10)

Every physical row of `Cmat` has squared norm at most

`r_j^2+c_j^2<=2delta^2<=min(R,C)^2/32`.                      (5.11)

Hence

`ell_j=Cmat_j G^(-1) Cmat_j^T
 <= ||Cmat_j||^2/lambda_min(G)
 <=1/(16eta^2)`.                                              (5.12)

For a whitened two-frame, Cauchy-Binet gives `sum_{j<k}w_{jk}=1`, and the inclusion marginal satisfies

`ell_j=sum_{k!=j} w_{min(j,k),max(j,k)}`.                     (5.13)

For two iid basis pairs, inclusion-exclusion is exact:

`rho=1-sum_j ell_j^2+sum_{j<k}w_{jk}^2`.                     (5.14)

Since `sum_j ell_j=2`,

`sum_j ell_j^2 <= (max_j ell_j)sum_j ell_j
 <=1/(8eta^2)`.                                               (5.15)

Dropping the nonnegative final term in (5.14) proves (5.8). QED.

This is a determinant-weighted coordinate selection statement, not a leverage assertion about rotated random variables. The whitening is applied only to the deterministic coefficient frame used to define its Pluecker law; no random coordinate is rotated and called independent.

## 6. Actual full-ambient payment on the strongly transverse diagonal-leaf subbranch

This subsection is a scoped application, not the main novelty claim.

In T1, `Delta=det G=W^2>=R^2C^2/4` and Section 5 gives `rho>=1/2`. If the actual leaf principal block on the star coordinates is diagonal, the completed fleet02/B09 two-hub theorem (1.3) therefore applies to the two literal physical hubs while retaining their entire actual 2x2 core. It yields

`||p_Q||_infinity
 <=2sqrt(e)[rho Delta]^(-1/4)
 <=2^(7/4)sqrt(e)(RC)^(-1/2)`.                                (6.1)

At the designated partner scale `R,C>h`,

`boxed:
 ||p_Q||_infinity
 < 2^(7/4)sqrt(e)/h
 = 4770492.861005282.`                                        (6.2)

The density is continuous on this subbranch. The numerical constant is intentionally not optimized; its role is to show that the determinant-balanced aggregate certificate is already strong enough for an existing full-ambient receiver once the same-side leaf curvature lies in that theorem's exact scope.

The general partner survivor does **not** assume a diagonal or determinant-balanced low-rank-plus-diagonal leaf principal block. Arbitrary high-rank same-bank curvature remains the genuine missing receiver.

## 7. Forbidden-coordinate robustness

If a particular downstream receiver insists that both hub coordinates be deleted from the star ground set before applying Sections 3-5, at most two coefficients of magnitude `h/8` are removed from each partner star. Thus the remaining star norms satisfy

`R_0,C_0 > h_0:=sqrt(31/32)h`.                                (7.1)

The disjoint-innovation calculation then has diagonal collision ratio at most `1/62`, giving

`||r_S||,||c_T||
 > sqrt(61/248) h_0
 =5.674549881008414e-7`.                                      (7.2)

In the strongly transverse `eta=1/2` branch, the same leverage proof gives

`max ell_j<=8/31`, `rho>=15/31`.                             (7.3)

Thus even this conservative deletion does not destroy determinant-balanced disjointness. The diagonal-leaf payment becomes

`||p_Q||_infinity
 < 2sqrt(e)(4096/465)^(1/4) h^(-1)
 =4886720.526794658`.                                         (7.4)

## 8. What this closes and what it does not

This run closes the designated partner's **pure bank-overlap/misalignment** issue: two diffuse physical stars always yield disjoint independent innovation banks, and their joint geometry is now quantitatively classified before any reciprocal minor payment.

It also produces the exact type of determinant-weighted currency requested by this slot:

- strong transverse: a whitened two-frame with `rho>=1/2`;
- medium transverse: a disjoint-bank aggregate mixed-minor packet of size at least `R^2C^2/162`;
- strong aligned: a relative `1/(9sqrt(2))` physical rank-one tube plus four common banks carrying both stars.

What remains unpaid is **not** bank overlap. It is nonlinear curvature: in the T2 and T3 branches, and in T1 outside the determinant-balanced low-rank-plus-diagonal leaf scope, the same original-coordinate banks may carry arbitrary dense quadratic self-couplings. A bounded density for the selected linear projections alone cannot be substituted for a curved pushforward estimate; the live correction ledger explicitly forbids that move. Likewise the T3 nonzero tail may not be discarded as a small random perturbation for arbitrary unbounded product laws.

The next precise obligation is therefore

`QFORM-DIFFUSE-TWOSTAR-CURVATURE-RECEIVER-v1`:

> Starting from the designated-partner N3 survivor, consume either (a) the determinant-balanced/transverse aggregate mixed-minor frame, (b) the medium transverse cut minor bank, or (c) the relative `1/(9sqrt(2))` rank-one/common-bank tube, while retaining the actual two-hub core, arbitrary same-bank quadratic curvature, all unused couplings and the full remaining spectrum. Route any failure into an already-paid volume, finite-core, ridge, grouped-square, pair-log, or exact-null endpoint without assuming independence after a spectral rotation.

Full QFORM remains **OPEN / not proved / not disproved**. Full-target continuity remains **OPEN**; continuity is proved here only on the explicitly scoped strongly-transverse diagonal-leaf two-hub subbranch.

## 9. Regression checks

`CHECKS.py` and captured `CHECKS.txt` are beside this report. They exhaustively enumerate all bipartitions for 210 deterministic small integer-vector cases to verify the averaging lower bounds, and check one deterministic 80-coordinate diffuse aligned configuration. The captured output ends `STATUS=PASS`. These are algebraic regression checks only; the proofs are the arguments above.
