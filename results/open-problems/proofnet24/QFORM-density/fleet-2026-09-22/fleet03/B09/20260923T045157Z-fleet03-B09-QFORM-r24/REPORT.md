SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T04:51:57Z.
attacking: the small-disjointness survivor in the grouped rank-two / mixed-hub Pluecker mechanisms, by extracting a quantitative disjoint physical-bank rank split instead of paying a vanishing reciprocal minor.

# fleet03/B09 r24 — quantitative Pluecker small-disjointness rank split

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **NEW STRUCTURAL SUPPORTING LEMMA / LARGE-DISJOINTNESS BRANCH PAID / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report does not claim a full density theorem. It proves the first missing implication left by r23: when determinant-weighted disjoint-basis mass is small, the failure cannot remain an amorphous high-dimensional obstruction. It forces one of exactly three quantitative original-coordinate geometries: a three-coordinate core, a two-dimensional core plus an outside line, or a one-dimensional core plus an outside plane. These alternatives retain a literal physical-coordinate partition and aggregate determinant volume; no spectral rotation is declared independent.

No Gaussianity, moments, compact support, connected support, log-concavity, identical distributions, or post-rotation independence is used. No pointwise law-uniform Fresnel decay, arbitrary-joint coarea estimate, conditional fiber supremum, or Monte Carlo extremality claim is used.

## 1. Inputs actually used

### 1.1 Previous B09 grouped-two-slope theorem

The completed fleet03/B09 r23 report is

`yspennstate/math-open-problems@13986bc9209e39eb885d7ad9e7bede9e426754aa`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T034845Z-fleet03-B09-QFORM-r23/REPORT.md`.

Its theorem `QFORM-GROUPED-TWOSLOPE-ONEFRESNEL-DISJOINT-v1` has disjoint original-coordinate banks `I,J,K`, a rank-two cross block `C=A[I,J]`, and

`A_II=lambda v v^T+D`,

with `D` diagonal. If `R` is an orthonormal basis of `range(C)`,

`delta=||(I-RR^T)v||_2`,

and `U=[v,R]G^(-1/2)` is the whitened three-dimensional active frame, define Pluecker weights

`w_S=det(U_S)^2`, `|S|=3`,

and

`rho=P(S cap T=empty)`

for iid bases from `w`. Then

`||p_Q||_infinity <= (5e/3)
 [ |lambda| delta^2 pdet(CC^T) rho ]^(-1/5)`.             (1.1)

The same coefficient times interval length bounds every interval, and the branch has a continuous density. The only remaining analytic gate in that packet is small `rho`.

### 1.2 Fresh compatible peer theorem

The completed fleet02/B09 report is

`yspennstate/math-open-problems@c5a57d1be0dc69e47bcb9fb52d5eaac77f4833c6`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T041423Z-fleet02-B09-QFORM-auto11/REPORT.md`.

Its `QFORM-MIXED-HUB-PLUCKER-SMOOTHING-v1` keeps one physical hub and an exact rank-two same-side curvature expansion. In its `r=2` case, with mixed-frame Gram matrix `G` and two nonzero curvature coefficients `lambda_1,lambda_2`, it gives

`||p_Q||_infinity
 <= 2 e^(3/4)
    [rho det(G)|lambda_1 lambda_2|]^(-1/4)`.             (1.2)

The density is continuous and the same coefficient multiplies interval length. I apply (1.2) quantitatively in Section 5.

The designated partner `fleet04/B09` still has no completed current-QFORM handoff/archive at the fresh repository check, so no theorem is attributed to that slot. The fleet02/B09 result is used as the available compatible completed B09 peer result.

## 2. Exact determinant identity

Let `U in R^(N x 3)` have orthonormal columns and rows `u_i^T`. For every physical triple `S`, define

`w_S=det(U_S)^2`.                                             (2.1)

Cauchy--Binet gives

`sum_S w_S=1`.                                                (2.2)

For a triple `S`, define the residual covariance on its physical complement

`R_S=sum_(i notin S) u_i u_i^T
    =I_3-U_S^T U_S`.                                         (2.3)

A second Cauchy--Binet identity gives

`det(R_S)=sum_(T subset S^c, |T|=3) w_T`.                    (2.4)

Hence the disjoint-basis mass is exactly

`rho=sum_(S cap T=empty) w_S w_T
    =sum_S w_S det(R_S).`                                    (2.5)

Thus `rho` is not merely a combinatorial overlap statistic. It is the Pluecker-weighted mean residual three-volume after deleting one physical triple.

## 3. New theorem: quantitative three-way rank split

### Theorem `QFORM-PLUCKER-SMALLRHO-RANKSPLIT-v1`

Let `U in R^(N x 3)` have orthonormal columns and let `rho` be (2.5). Fix any `eta in (0,1)`. Then at least one of the following holds.

**A. Balanced-disjointness branch**

`rho >= eta^3/2`.                                               (3.1)

**B. Quantitative physical rank-split branch**

There exists `k in {1,2,3}` and a family `G_k` of physical triples whose total Pluecker weight is at least `1/6`, such that for every `S in G_k` there is an orthogonal decomposition

`R^3=F_S direct_sum H_S`, `dim F_S=k`,                          (3.2)

with

`boxed: sigma_min(P_S U|_(F_S)) >= sqrt(1-eta),`                (3.3)

and, when `k<3`,

`boxed: sigma_min(P_(S^c) U|_(H_S)) > sqrt(eta).`               (3.4)

Equivalently, the squared `k`-volume carried by the three physical coordinates `S` is at least

`det[(P_S U|F_S)^T(P_S U|F_S)] >=(1-eta)^k`,                   (3.5)

while the squared complementary `(3-k)`-volume carried by the disjoint outside bank is strictly larger than

`det[(P_(S^c) U|H_S)^T(P_(S^c) U|H_S)] > eta^(3-k)`.           (3.6)

Moreover the outside rows are quantitatively close to the complementary subspace:

`sum_(i notin S)||P_(F_S)u_i||_2^2 <= k eta`.                  (3.7)

Thus the three cases have the literal source-coordinate meaning:

- `k=3`: a three-coordinate core carries all three active dimensions up to tail energy `3 eta`;
- `k=2`: three coordinates carry a two-dimensional core, while all outside rows are within total squared error `2 eta` of one line and that outside line has squared energy `>eta`;
- `k=1`: three coordinates carry one active direction, while all outside rows are within total squared error `eta` of one plane and that outside plane has squared two-volume `>eta^2`.

These are disjoint physical banks `S` and `S^c`; no random-coordinate rotation is involved.

### Proof

Assume (3.1) fails, so

`rho<eta^3/2`.                                                   (3.8)

Sample `S` from the Pluecker law `w`. By (2.5),

`E_w det(R_S)=rho`.                                              (3.9)

Markov's inequality gives

`P_w(det(R_S)>eta^3) <= rho/eta^3 <1/2`.                        (3.10)

Therefore the good set

`G={S:det(R_S)<=eta^3}`                                        (3.11)

has Pluecker weight greater than `1/2`.

Fix `S in G`. Let

`0<=mu_1<=mu_2<=mu_3<=1`                                      (3.12)

be the eigenvalues of `R_S`. Their product is at most `eta^3`, hence

`mu_1<=eta`.                                                    (3.13)

Let `k` be the number of `mu_j` which are at most `eta`; thus `k in {1,2,3}`. Let `F_S` be the span of the corresponding eigenvectors and `H_S=F_S^perp`.

For every unit `x in F_S`,

`||P_(S^c) U x||_2^2=x^T R_S x<=eta`.                          (3.14)

Since `U^T U=I`,

`||P_S U x||_2^2=1-x^T R_S x>=1-eta`.                          (3.15)

Hence every squared singular value of `P_S U|F_S` is at least `1-eta`, proving (3.3) and (3.5).

If `k<3`, every eigenvalue of `R_S` on `H_S` is strictly larger than `eta`. Therefore, for every unit `y in H_S`,

`||P_(S^c)U y||_2^2=y^T R_S y>eta`,                             (3.16)

which proves (3.4), and multiplying the relevant eigenvalues proves (3.6).

Finally,

`sum_(i notin S)||P_(F_S)u_i||_2^2
 =tr(P_(F_S)R_S)
 =sum_(j=1)^k mu_j
 <=k eta`,                                                       (3.17)

which is (3.7).

Partition `G` according to `k=1,2,3`. Since `w(G)>1/2`, one class has Pluecker weight at least `1/6`. QED.

## 4. Consequences for the grouped-two-slope B09 packet

Write the r23 aggregate resource as

`R_* = |lambda| delta^2 pdet(CC^T)`.                            (4.1)

Combining (1.1) with Theorem 3 gives, for every `eta in (0,1)`, the following exact dichotomy:

- either

`boxed:
 ||p_Q||_infinity
 <= (5e/3) 2^(1/5) eta^(-3/5) R_*^(-1/5),`                    (4.2)

with a continuous density and the identical coefficient times `|L|` for every interval;

- or a Pluecker subfamily of weight at least `1/6` has one of the three source-coordinate rank-split geometries (3.3)--(3.7).

This converts the vague phrase “small disjointness” into a finite exhaustive quantitative debt. There is no fourth high-dimensional small-rho geometry.

For the concrete scale

`eta=1/16`,                                                     (4.3)

balanced disjointness means

`rho>=eta^3/2=1/8192`.                                         (4.4)

If also `R_*>=1`, (4.2) gives

`boxed: ||p_Q||_infinity <27.468.`                              (4.5)

If (4.5) is unavailable solely because `rho<1/8192`, then at least one sixth of the determinant mass lies in triples for which the active frame has one of the following strong physical-bank certificates:

- three-core: all three active singular values into `S` are at least `sqrt(15/16)`;
- two-core plus line: the two core singular values are at least `sqrt(15/16)` and the disjoint outside line has norm `>1/4`;
- one-core plus plane: the core singular value is at least `sqrt(15/16)` and both singular values of the disjoint outside plane are `>1/4`.

The last two statements use `sqrt(eta)=1/4` in (3.4). This is the scale needed for a later bilinear/linear anti-concentration payment; it does not depend on dimension.

A useful strengthening in the `k=3` branch is immediate: since

`U_S^T U_S=I-R_S`,

`w_S=det(U_S)^2=prod_j(1-mu_j)>=(1-eta)^3`.                     (4.6)

Thus the three-core branch is not merely “localized”; it contains an actually large physical triple minor of the active frame.

## 5. Fresh peer theorem applied to an actual inequality

Apply fleet02/B09's completed mixed-hub theorem (1.2) with the same threshold `eta`. Put

`H_* = det(G)|lambda_1 lambda_2|`.                              (5.1)

If

`rho>=eta^3/2`,                                                  (5.2)

then (1.2) gives the concrete inequality

`boxed:
 ||p_Q||_infinity
 <= 2^(5/4)e^(3/4) eta^(-3/4) H_*^(-1/4).`                     (5.3)

At `eta=1/16` and `H_*>=1`,

`boxed: ||p_Q||_infinity <40.281.`                              (5.4)

The density is continuous and every interval has probability `<40.281 |L|` in that normalized resource regime. If (5.4) fails solely because `rho<1/8192`, Theorem 3 again outputs the same three quantitative physical-bank rank splits for the mixed hub frame. Thus the new lemma simultaneously sharpens the remaining small-rho debt in both completed B09 packets.

This is an actual numerical application of a completed compatible peer result, not a bibliography-only reference.

## 6. Exact endpoint controls

The three alternatives are all necessary. They already appear when `rho=0`.

### 6.1 Three-core endpoint

Take `U=I_3`. The only Pluecker basis is all three coordinates, `rho=0`, and

`R_S=0`.

This is exactly `k=3`.

### 6.2 Two-core plus outside line

Take rows

`e_1, e_2, e_3/sqrt(2), e_3/sqrt(2)`.

The columns are orthonormal. Every nonzero Pluecker basis contains the first two coordinates, so two bases can never be disjoint and `rho=0`. For either basis,

`spec(R_S)={0,0,1/2}`.

This is exactly `k=2`: the complement is a line.

### 6.3 One-core plus outside plane

Take rows

`e_1/sqrt(2), e_1/sqrt(2), e_2/sqrt(2), e_2/sqrt(2), e_3`.

Again `U^TU=I`. Every nonzero basis contains the final coordinate, hence `rho=0`, and for every basis

`spec(R_S)={0,1/2,1/2}`.

This is exactly `k=1`: one core direction and an outside plane.

These are structural regression controls, not counterexamples to QFORM. They show why a small-rho proof cannot route every failure into only a single “near-coloop” form.

## 7. Why this advances the full proof map

The r23 debt was to convert small determinant-disjointness into a quantitative near-line, near-plane, or finite-core statement without throwing away original-coordinate product provenance. Theorem 3 does precisely that and additionally preserves a complementary determinant-volume lower bound on the disjoint bank.

What it does **not** yet prove is that each of the three approximate geometries is already paid by an existing target theorem under arbitrary residual curvature. Small coefficients cannot be treated as small random errors because the input laws need not have moments or bounded support. The perturbative step must therefore be done by conditioning/translation-invariant anti-concentration, not by moment estimates.

The next exact B09 implication is

`QFORM-RANKSPLIT-PHYSICAL-PAYMENT-v1`:

> Starting from (3.3)--(3.7), pay each of the three source-coordinate rank-split geometries without moment assumptions: route `k=3` to a finite physical-core theorem; route `k=2` by retaining the two-core variables and aggregating the disjoint line before reciprocal inversion; route `k=1` by retaining one core physical scalar and applying a rank-two disjoint-bank half-Riesz / conditional-linear anti-concentration estimate to the outside plane. The estimate must remain linear in interval length and allow arbitrary same-bank residual quadratic curvature.

The `k=1` case is especially aligned with this slot's bilinear mechanism: the outside plane already has both singular values `>sqrt(eta)`, so no fixed tiny two-column minor need be selected. The remaining issue is coupling that aggregate two-volume to the core scalar while retaining the exact original-product selectors.

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN**. Theorems (1.1) and (1.2) give continuity only on their paid large-disjointness branches.

## 8. Corrections respected

- No law-uniform pointwise van-der-Corput/Fresnel decay is used.
- No arbitrary-joint rank-three coarea estimate is used.
- No positive conditional projection-density moment is assumed.
- No independence is asserted after diagonalizing or whitening the coefficient frame.
- No fixed physical minor is required in the diffuse branch; determinant mass is aggregated first.
- No Monte Carlo or histogram is used as proof.

The checker beside this report verifies the complementary-minor identity numerically on a random orthonormal frame, the three exact `rho=0` endpoint spectra, and the constants at `eta=1/16`.
