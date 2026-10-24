SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T23:07:27Z.
attacking: the exact-match/high-rank same-bank third-curvature survivor by forcing one simultaneous physical cut before any near-singular hub inversion.

# account02/B08 r29 — compound simultaneous-cut identity and a quantified aligned survivor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / complementary constructions and source-valid counterexamples  
Designated partner: `account03/B08`  
Owner continuation: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
Owner control at startup and pre-write refresh: revision `2026-09-22.15`, QFORM only  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING STRUCTURAL ROUTER + QUANTIFIED LOCALIZED/ALIGNED SPLIT + TARGET-VALID MECHANISM OBSTRUCTION / FULL TARGET OPEN**.

The unrestricted QFORM conjecture remains OPEN. All stochastic coordinates below are ORIGINAL independent coordinates with one-dimensional densities bounded by one. No moments, bounded support, log-concavity, identical laws, post-rotation independence, arbitrary-joint coarea bound, conditional projection-height bound, or deletion of a small quadratic perturbation is used. Essential boundedness is the target; continuity is asserted only on branches whose Fourier majorant is integrable.

## 1. First unpaid implication after this run

The first unpaid B08 implication is now

`QFORM-ALIGNED-TWOBANK-CARRIER-PLUS-DIAGONAL-COMPILER-v1`.

The preceding B08 run already supplied the **actual physical spectral gate**

`any physical 2x2 principal block with sigma_min >= L/64  ==>  ||p_Q||_infinity < 619/L`,      (1.1)

for every full ambient matrix with at least three eigenvalues of modulus at least `L`.

The newest account03/B08 result then isolated the remaining common-plane/same-bank third-curvature problem. The new result below solves its previously unpaid **simultaneous cut-selection** step for an arbitrary high-rank same-bank residual. In the current arm-area chamber, after excluding explicit localized witnesses, every still-unpaid same-bank residual is quantitatively aligned with its two-dimensional arm carrier: its total leave-one-out distance is `<0.005373 L`; at exact zero distance it is **exactly**

`M^T R M + physical diagonal`,                                    (1.2)

with `R` symmetric. The next receiver must consume this aligned carrier plus arbitrary physical diagonal twists and any small nonzero alignment/crossing without paying a reciprocal near-singular hub factor.

## 2. Pinned inputs actually used

### 2.1 Required fixed source

The owner-required source was read at the exact commit

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`:

- `RESULTS.md`;
- `FOURIER_ROUTE_REPORT.md`;
- `COUNTEREXAMPLE_SEARCH.md`.

The completed result actually applied to a new target-valid obstruction in Section 8 is **Theorem H (hub coordinates)**. With two original hubs, no light Fresnel square (`r=0`), a diagonal light block, and augmented arm Gram `G`, it gives

`|phi_Q(t)| <= (2|t|)^(-2) (4pi)^2 det(G)^(-1/2)`.               (2.1)

This is used below at an explicit matrix for which every physical pair misses the `L/64` gate and the new compound currency is identically zero.

### 2.2 Newest designated partner

The newest compatible account03/B08 report at pre-write refresh is

`yspennstate/math-open-problems@2dc8a71902532a4e28c15b86346d758f004bfab3`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260923T222118Z-account03-B08-qform-diffuse-r44/REPORT.md`.

Its analytic engine is the independently reviewed grouped projected-crossing theorem

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`,
`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

For two literal original hub coordinates and one projected crossing direction, write

`A_K = sqrt(det(M_K M_K^T))`,
`F_K = ||C_K||_F`,                                                 (2.2)

where `M_K` is the two-row hub arm on a physical light subset `K` and `C_K` is the residual crossing after projecting off `row(M_K)`. If every physical row of `C_K` has squared marginal at most `1/2`, the full ambient form satisfies

`||p_Q||_infinity <= C0 (A_K F_K)^(-1/3)`,
`C0=3*2^(5/6)=5.345392308842036...`,                              (2.3)

and has a continuous `C_0` density. Arbitrary hub self-curvature, arbitrary internal same-bank curvature, every diagonal and every affine term are retained.

The partner proved this currency could be forced for a diffuse rank-one same-bank residual, and left the arbitrary-high-rank **simultaneous arm-area / projected-volume cut** as the precise next structural step. Sections 3-6 solve that step in terms of an intrinsic compound alignment energy.

### 2.3 Inherited arm scale

In the live common-plane descendant, each two-row arm obeys

`S_M := s_1(M)s_2(M) > s_* L^2`,
`s_* = 1/(64 sqrt(896)) = 0.0005219946131102039... .`             (2.4)

The preceding account02/B08 physical-pair theorem at

`math-open-problems@34c64bff0ddefd088c372ef60e7a1e1266a18a43`

supplies (1.1). No inverse of the near-singular hub block is used anywhere in the new router below.

## 3. Exact compound identity for one physical cut

Work in one physical light bank of size `m`. Let

`M in R^(2 x m)`                                                   (3.1)

be its two-row hub arm, with row rank two, and let

`S=S^T in R^(m x m)`                                               (3.2)

be an arbitrary same-bank residual. In the common-plane state the full light matrix may also contain arbitrary common-plane terms and an arbitrary crossing tail to the other bank; they will be retained in Section 5.

For a literal physical subset `K subset {1,...,m}`, let `P_K` be the orthogonal projection in `R^K` onto `row(M_K)`. Put

`A_K^2 = det(M_K M_K^T)`,                                        (3.3)

`C_K^S = S[K^c,K](I-P_K)`,
`F_K^S = ||C_K^S||_F`.                                           (3.4)

For `i in K^c`, append the row `S[i,K]` to the two arm rows. The Gram Schur-complement identity gives

`det([M_K;S[i,K]][M_K;S[i,K]]^T)
 = A_K^2 ||S[i,K](I-P_K)||_2^2`.                                 (3.5)

Cauchy--Binet on the `3 x |K|` matrix on the left gives

`det([M_K;S[i,K]][M_K;S[i,K]]^T)
 = sum_{T subset K, |T|=3} det([M_T;S[i,T]])^2`.                  (3.6)

Summing over `i in K^c` yields the exact identity

`boxed:
 A_K^2 (F_K^S)^2
 = sum_{i in K^c} sum_{T subset K, |T|=3}
     det([M_T;S[i,T]])^2 .`                                      (3.7)

This remains valid when `M_K` has rank `<2`: then both sides are zero. Thus no good minor or invertible local pivot is assumed.

## 4. Bernoulli cut solves the simultaneous-selection problem

Define the global compound currency

`Xi(M,S)
 = sum_i sum_{T subset [m]\{i}, |T|=3}
     det([M_T;S[i,T]])^2`.                                      (4.1)

Choose `K` by retaining each physical coordinate independently with probability `p`. For a fixed ordered pair `(i,T)` with `i notin T`, its term in (3.7) survives exactly when `T subset K` and `i notin K`, of probability

`p^3(1-p)`.                                                       (4.2)

Hence

`boxed:
 E[A_K^2 (F_K^S)^2]
 = p^3(1-p) Xi(M,S).`                                            (4.3)

The coefficient is maximized at `p=3/4`, where

`c := p^3(1-p)=27/256`.                                          (4.4)

Therefore some **literal original-coordinate cut** satisfies

`boxed:
 A_K F_K^S >= sqrt(c) Xi(M,S)^(1/2).`                            (4.5)

If `Xi>0`, that cut automatically has `A_K>0` and `F_K^S>0`, so `M_K` has row rank two. This proves the high-rank simultaneous-selection step left open by account03/B08; the remaining issue is only whether the selected projected volume is diffuse across physical rows or localized on one row.

## 5. Full-ambient router: diffuse projected rows pay, heavy rows localize

Return to the two-bank common-plane geometry. Let the selected bank be `J_1`, with arm `M=M_1` and same-bank residual `S=S_1`; let `J_2` be the other bank. The light-light blocks may contain

`M_1^T R M_1 + S_1`,
`M_2^T R M_2 + S_2`,
`M_1^T R M_2 + T`,                                                (5.1)

with arbitrary symmetric `R`, arbitrary symmetric `S_2`, and arbitrary physical cross-tail `T` allowed by the ambient state.

Use the cut `K subset J_1` furnished by (4.5). Project the full crossing from

`I=(J_1\K) union J_2`

to `K` off `row(M_K)`. Every common-plane row dies under `I-P_K`, so the full projected crossing is

`C_K = [ S_1[J_1\K,K] ; T[J_2,K] ] (I-P_K)`                     (5.2)

(up to the harmless transpose convention for `T`). In particular

`F_K := ||C_K||_F >= F_K^S`.                                     (5.3)

Thus (4.5) implies

`A_K F_K >= sqrt(c) Xi(M,S)^(1/2).`                              (5.4)

No small cross-tail is discarded; it can only increase the available Frobenius crossing currency.

If every physical row of the **full** `C_K` has squared marginal at most `1/2`, apply the partner theorem (2.3):

`||p_Q||_infinity
 <= C0 c^(-1/6) Xi(M,S)^(-1/6)
 = 2^(13/6) sqrt(3) Xi(M,S)^(-1/6).`                             (5.5)

The exact numerical constant is

`C_* = 2^(13/6) sqrt(3)
     = 7.7766451889586605... .`                                  (5.6)

This branch has a continuous `C_0` density.

If instead a row marginal exceeds `1/2`, then some literal physical row `i` obeys

`||C_{K,i,*}|| > F_K/sqrt(2)`.                                   (5.7)

This is the complementary localized certificate. The theorem therefore retains an arbitrary product source and turns the previously unresolved high-rank cut selection into an exact **diffuse-or-localized** router.

### Theorem 5.1 — `QFORM-EXACTMATCH-HIGHRANK-COMPOUND-ROUTER-v1`

Under the common-plane two-hub geometry above, for every symmetric same-bank residual `S`, define `Xi(M,S)` by (4.1). If `Xi>0`, then either

1. the full ambient quadratic form has a continuous density satisfying (5.5), or
2. some physical row of a selected full projected crossing carries more than half of that crossing's squared Frobenius mass.

All same-bank curvature, the second bank, arbitrary common-plane curvature, the physical cross-tail, hub self-curvature and affine terms are retained.

## 6. Intrinsic form: weighted leave-one-out alignment energy

The currency `Xi` has a clean intrinsic interpretation. Let

`G=MM^T`,
`S_M=sqrt(det G)=s_1(M)s_2(M)`,                                  (6.1)

and for the `i`th physical arm column `m_i` define its leverage

`ell_i = m_i^T G^(-1)m_i`, `0<=ell_i<=1`, `sum_i ell_i=2`.        (6.2)

When `ell_i<1`, deleting coordinate `i` leaves a rank-two arm. Define

`d_i = dist(S[i,-i], row(M_{-i}))`.                              (6.3)

When `ell_i=1`, its contribution below is defined as zero. Matrix determinant lemma gives

`det(M_{-i}M_{-i}^T)=det(G)(1-ell_i)`.                           (6.4)

Applying the Gram Schur complement and Cauchy--Binet to the fixed `i` summand in (4.1) yields

`sum_{T subset [m]\{i}, |T|=3} det([M_T;S[i,T]])^2
 = det(G)(1-ell_i)d_i^2`.                                       (6.5)

Hence

`boxed:
 Xi(M,S)=S_M^2 D_M(S)^2,`                                       (6.6)

where

`D_M(S)^2 := sum_i (1-ell_i)d_i^2`.                              (6.7)

The quantity `D_M(S)` is exactly the weighted leave-one-out distance of the same-bank curvature from the two-dimensional physical arm carrier. Substitution in (5.5) gives the scale-transparent estimate

`boxed:
 ||p_Q||_infinity
 <= C_* (S_M D_M(S))^(-1/3)`                                    (6.8)

on the diffuse projected-row branch.

The localized alternative can also be given an absolute size. Since `A_K<=S_M`, (4.5)-(6.6) imply

`F_K >= sqrt(c) D_M(S)`.                                         (6.9)

Therefore a heavy row satisfies

`boxed:
 ||C_{K,i,*}||
 > sqrt(c/2) D_M(S)
 = (3 sqrt(6)/32) D_M(S)
 =0.22963966338592295... D_M(S).`                               (6.10)

This is an actual original-coordinate localized third-curvature witness, not a spectral-coordinate statement.

## 7. Quantified actual `619/L` hybrid gate

Apply Theorem 5.1 in the inherited arm chamber (2.4). Define

`eta_619
 := (C_*/619)^3 / s_*
 = 0.0037987340155334467... .`                                  (7.1)

If on either bank

`D_M(S) >= eta_619 L`,                                           (7.2)

then

`S_M D_M(S)
 > s_* eta_619 L^3
 = (C_*/619)^3 L^3`.                                             (7.3)

Consequently the diffuse projected-row branch is paid by

`boxed: ||p_Q||_infinity <619/L`,                                (7.4)

while the heavy-row branch gives an actual physical projected row of size

`boxed:
 ||C_{K,i,*}||
 > (3sqrt(6)/32) eta_619 L
 = 8.72340000619756*10^(-4) L.`                                 (7.5)

Now impose the newest localized/diffuse arm split explicitly. If some arm leverage satisfies

`ell_i>1/2`,                                                       (7.6)

there is already an actual localized arm coordinate. Otherwise every `1-ell_i>=1/2`. If neither (7.4) nor the localized projected-row alternative occurs, then on each unpaid bank

`D_M(S)<eta_619 L`,                                               (7.7)

and therefore

`boxed:
 (sum_i d_i^2)^(1/2)
 <=sqrt(2)D_M(S)
 <0.005372221164615409 L.`                                       (7.8)

Thus the still-unpaid nonlocalized high-rank hybrid is no longer an arbitrary same-bank matrix: row by row, after deleting its own physical diagonal entry, its entire curvature lies within total Euclidean error `<0.005373 L` of the two-row arm carrier.

This is the new explicit actual spectral/structural gate:

- physical pair scale `>=L/64`: paid by the preceding `<619/L` theorem;
- common-plane arm-localized leverage `>1/2`: actual localized coordinate;
- arm-diffuse but alignment energy `>=0.003799L`: either paid by `<619/L` or a projected row of size `>8.72e-4L` is localized;
- otherwise the same-bank curvature satisfies the quantified aligned condition (7.8).

Applying the last two bullets to both physical banks quantifies the remaining two-bank hybrid while retaining arbitrary product sources and all cross/same-bank terms.

## 8. Exact zero-alignment classification

The endpoint `D_M(S)=0` has a rigid algebraic form.

### Theorem 8.1 — `QFORM-ARMALIGNMENT-ZERO-CLASSIFICATION-v1`

Assume `M` has row rank two and every arm leverage obeys `ell_i<1` (in particular the diffuse gate `ell_i<=1/2` suffices). Then

`D_M(S)=0`

if and only if there exist a symmetric `2 x 2` matrix `R_0` and a physical diagonal matrix `D_0` such that

`boxed: S=M^T R_0 M + D_0.`                                      (8.1)

#### Proof

The reverse implication is immediate: after deleting coordinate `i`, every off-diagonal row of `M^T R_0 M` lies in `row(M_{-i})`, while `D_0` disappears.

Conversely `D_M(S)=0` and `ell_i<1` imply `d_i=0` for every `i`. Choose `a_i in R^2` so that

`S[i,-i]=a_i^T M_{-i}`.                                          (8.2)

Let `A=[a_1 ... a_m] in R^(2 x m)`. For `i!=j`,

`(A^T M)_{ij}=a_i^T m_j=S_ij=S_ji=(A^T M)_{ji}`.                 (8.3)

The diagonal of a skew-symmetric matrix is automatically zero, so (8.3) says

`A^T M=M^T A`.                                                    (8.4)

If `x in ker M`, then (8.4) gives `M^T A x=0`. Since `M^T` is injective, `Ax=0`. Hence `ker M subset ker A`, so every row of `A` lies in `row(M)` and

`A=R_0 M`                                                        (8.5)

for some `2 x 2` matrix `R_0`. Substitution in (8.4) gives

`M^T(R_0^T-R_0)M=0`;                                             (8.6)

multiplying by left and right inverses constructed from `G=MM^T` yields `R_0^T=R_0`. Equation (8.2) now says `S-M^T R_0M` has zero off-diagonal entries, proving (8.1). QED.

So the exact unpaid endpoint is not mysterious high-rank curvature: modulo arbitrary physical diagonal twists it is a quadratic form in the **same two aggregate arm coordinates** already seen by the hubs. This is why a third projected crossing direction need not exist.

## 9. Target-valid obstruction to forcing positive compound currency

The classification above raises a natural but false stronger structural hope: perhaps the target spectral hypothesis itself forces `D_M(S)>0` or a good physical pair. It does not.

Let `m=2^q>=4096` and let `U in R^(2 x m)` consist of two normalized Sylvester-Hadamard rows, so

`UU^T=I_2`,
`|U_hj|=m^(-1/2)`.                                                (9.1)

Use two original hub coordinates and two disjoint light banks of size `m`, with

`M_1=M_2=(L/sqrt(2))U`,                                          (9.2)

and define

`A_star =
 [[0_2, M_1, M_2],
  [M_1^T, 0, 0],
  [M_2^T, 0, 0]].`                                               (9.3)

The combined hub-to-light arm is `[M_1 M_2]` and has two singular values exactly `L`. Therefore

`spec(A_star)={+L,+L,-L,-L,0,...,0}`.                            (9.4)

This is an actual target matrix: it has four eigenvalues of modulus `L`.

Every physical `2 x 2` principal block is either singular or a hub-light block

`[[0, a],[a,0]]`,
`|a|=L/sqrt(2m)<L/64`                                            (9.5)

for `m>=4096`. Thus the physical-pair `L/64` gate fails everywhere.

On each light bank the same-bank residual is exactly zero, so

`D_M(S)=Xi(M,S)=0`.                                               (9.6)

The arm itself is diffuse: each bank leverage is exactly `2/m<=1/2`. The arm area is large,

`s_1(M_r)s_2(M_r)=L^2/2`.                                       (9.7)

Hence a large target spectrum plus diffuse arms does **not** force positive same-bank compound currency. This is a mechanism obstruction to strengthening Theorem 5.1 into a spectral lower bound for `Xi`; it is not a counterexample to QFORM.

### Required fixed-source result applied to the actual obstruction

The completed fixed-source Theorem H pays this same matrix uniformly for arbitrary cap-one product sources. Take the two literal hubs as `H`, all `2m` leaves as `I`, `J=empty`, and `r=0`. The light block is zero, hence diagonal. The augmented arm Gram is

`G=sum_{i in I} rho_i rho_i^T=L^2 I_2`,                           (9.8)

and every normalized physical leverage is exactly `1/m<=1/2`. Thus (2.1) gives

`|phi_Q(t)| <= min(1, 4pi^2/(L^2 t^2)).`                         (9.9)

Since

`int_R min(1,4pi^2/(L^2t^2)) dt = 8pi/L`,                       (9.10)

Fourier inversion yields the real target-level inequality

`boxed: ||p_(X^T A_star X)||_infinity <=4/L`.                    (9.11)

Moreover `phi in L^1`, so the density is continuous and vanishes at infinity.

This is the required `e5f71d79...` result applied to a source-valid obstruction: whole-arm aggregation succeeds exactly where every physical pair is weak and the new third-curvature compound currency vanishes identically.

## 10. Deterministic checks

`CHECKS.py` and `CHECKS.txt` in this run directory verify:

1. (3.7) for every subset in 40 seeded random `2 x 6` / symmetric `6 x 6` tests, maximum error `8.527e-14`;
2. the Bernoulli identity (4.3), maximum error `1.421e-14`;
3. the intrinsic formula (6.6), maximum error `1.990e-13`;
4. `Xi=0` for 40 seeded matrices of the exact aligned form `M^T R M + diagonal`, maximum numerical residue `1.764e-28`;
5. the constants
   `c=27/256`,
   `C_*=7.776645188958661`,
   `eta_619=0.003798734015533447`, and
   the localized-row threshold `0.0008723400006197561 L`.

The output terminates

`QFORM_B08_R29_CHECK_PASS`.

These calculations are regression checks only; Sections 3-9 are analytic arguments.

## 11. What is and is not solved

### Proved here

- `QFORM-EXACTMATCH-COMPOUND-CUT-IDENTITY-v1`: exact formula (3.7) and Bernoulli expectation (4.3), solving simultaneous physical cut selection for arbitrary high-rank same-bank curvature.
- `QFORM-EXACTMATCH-HIGHRANK-COMPOUND-ROUTER-v1`: the full ambient diffuse-or-localized router (5.5)/(5.7), retaining arbitrary cross-tail and same-bank terms.
- The intrinsic identity `Xi=S_M^2 D_M(S)^2`, yielding the dimensionally exact density scale `C_*(S_M D_M)^(-1/3)`.
- In the current arm chamber, the actual `619/L` gate: `D_M>=0.003799L` is paid or creates a physical projected row `>8.72e-4L`; otherwise the diffuse arm has total leave-one-out misalignment `<0.005373L`.
- `QFORM-ARMALIGNMENT-ZERO-CLASSIFICATION-v1`: zero alignment is exactly `M^T R M + physical diagonal` under the diffuse arm gate.
- `QFORM-ALIGNED-DIFFUSE-STAR-OBSTRUCTION-v1`: a target-valid four-large-eigenvalue Hadamard star has every physical pair below `L/64` and `Xi=0`, yet fixed-source Theorem H gives `||p_Q||infinity<=4/L` continuously for every cap-one product source.

### Still open

The unrestricted QFORM conjecture is **OPEN**. The new structural router does not by itself pay the aligned carrier state (8.1) when nontrivial carrier curvature and arbitrary physical diagonal twists interact with a near-singular hub. It also does not convert every localized arm/projected-row witness into a global density bound inside this report. Small nonzero departures from exact alignment must be retained rather than deleted as random perturbations.

The next precise B08 implication is therefore

`QFORM-ALIGNED-TWOBANK-CARRIER-PLUS-DIAGONAL-COMPILER-v1`:

> In the common-plane two-hub state after the `L/64` physical-pair gate, assume both arms are diffuse and both same-bank residuals satisfy the quantified alignment bound (7.8), with exact zero limit `S_r=M_r^T R_r M_r+D_r`. Prove a universal `O(L^-1)` full-ambient density bound that retains arbitrary physical diagonal twists, arbitrary cross-tail, induced affine terms and original product provenance, and is stable as the alignment errors tend to zero. It must recover the fixed-source `4/L` mechanism on the zero-carrier Hadamard star family without asserting independence after rotation.

Continuity remains separate globally; the new projected-crossing paid branch and the fixed-source star family have continuous `C_0` densities.
