SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-22T22:37:41Z.
attacking: direct coarea for the double-star / aggregate-bank survivor, with the goal of paying an internal rank-two product bank before selecting any physical triple.

# account03/B05 r19 — aggregate rank-two bank + two scalar-bank coarea

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Quadratic coarea bound  
**Live owner control:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** supporting theorem proved; full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Continuity:** not proved by the theorem below; only essential boundedness is claimed.

## 1. Source-valid starting point

The target remains the full owner statement: independent original coordinates with one-dimensional probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, compact-support, log-concavity, Gaussian, connected-support, diagonal-basis, or post-rotation independence assumption is introduced.

The live corrections are enforced. In particular this report does **not** use law-uniform pointwise Fresnel/van-der-Corput decay, an arbitrary-joint rank-three coarea bound, a positive moment of a conditional projection-density height, an unrestricted fiber supremum, or the false principle that a bounded conditional density can replace genuine independence.

The preceding B05 run isolated a same-bank leakage obstruction: aggregate star arms can be large even while their supplier banks also carry quadratic curvature, so conditioning those banks away loses the useful curvature. Fresh B10/B19 work sharpened the same issue to `QFORM-O3-INTERNAL-RANK2-ROUTING-v1`: a three-bank aggregate determinant packet is already paid if all three banks are spectral rank one, while a bank of genuine spectral rank two was still an unpaid endpoint.

The analytic input used below is the completed pair-log theorem

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`,

which proves the following dependence-safe statement for two **independent cap-one scalar inputs**. If their fixed quadratic matrix `B` is invertible indefinite, `D=|det B|`, `kappa=sigma_min(B)`, and after completing the pair the remaining random critical value `R` satisfies

`sup_t P(|R-t|<rho) <= H sqrt(rho)`,

then

`||p_Q||_infinity <= 4 sqrt(2H) (D kappa)^(-1/4)`.                    (1.1)

The rank-one affine small-ball theorem used there is also source-valid:

`sup_t P(|lambda (u dot X)^2 + b dot X + d - t|<rho)
 <= min(1,10 sqrt(rho/|lambda|))`,                                     (1.2)

for every unit coefficient vector `u`, arbitrary affine term, and the original cap-one product law.

The exact designated partner `account04/B05` has no completed current-QFORM artifact discoverable at the fresh source check. No result is fabricated for that slot. A compatible completed account04 theorem is applied in Section 6.

## 2. Geometry: one rank-two product bank and two rank-one product banks

Work first in an exact-rank-three active block

`A_S = R_S M R_S^T`,                                                   (2.1)

where `M` is an invertible real symmetric `3 x 3` matrix. The original-coordinate index set `S` is partitioned into three disjoint banks

`G_1 disjoint_union G_2 disjoint_union G_3`.

All original coordinates outside `S` may be conditioned; they create arbitrary affine terms and constants, which the theorem below permits uniformly.

Assume:

1. the rows in `G_1` have spectral span exactly two;
2. the rows in `G_2` are collinear: `r_j=c_j v_2`, `||v_2||=1`, and `lambda_2=sum_(j in G_2)c_j^2>0`;
3. the rows in `G_3` are collinear: `r_k=d_k v_3`, `||v_3||=1`, and `lambda_3=sum_(k in G_3)d_k^2>0`;
4. the union spans all three spectral dimensions.

Factor the first-bank row matrix as

`R_(G_1) = C T_1^T`,                                                   (2.2)

with `C^T C=I_2` and `T_1` a `3 x 2` full-rank matrix. Define the genuine original-coordinate two-dimensional projection

`L=C^T X_(G_1)`.                                                       (2.3)

No independence is asserted between the two components of `L`.

For the two rank-one banks define normalized scalar aggregates

`Y=lambda_2^(-1/2) sum_(j in G_2)c_j X_j`,
`Z=lambda_3^(-1/2) sum_(k in G_3)d_k X_k`.                             (2.4)

The banks are disjoint, hence `L`, `Y`, and `Z` are mutually independent as **blocks**. Rogozin--Ball gives

`||p_Y||_infinity, ||p_Z||_infinity <= sqrt(2)`.                       (2.5)

Put

`t_2=sqrt(lambda_2)v_2`, `t_3=sqrt(lambda_3)v_3`,
`T_23=[t_2,t_3]`,
`B=T_23^T M T_23`.                                                     (2.6)

Assume for the new theorem that `B` is invertible and indefinite, and write

`D=|det B|`, `kappa=sigma_min(B)>0`.                                  (2.7)

Finally define the **aggregate three-bank principal-determinant mass**

`mu = sum_(i in G_1, j in G_2, k in G_3)
        |det A_{ {i,j,k},{i,j,k} }|`.                                  (2.8)

For exact rank three every principal triple has

`det A_{ijk}=det(M) det(r_i,r_j,r_k)^2`,                               (2.9)

so all nonzero terms have the same sign before absolute values.

## 3. Exact aggregate Schur identity: no physical triple is selected

### Lemma 3.1 — `QFORM-RANK2BANK-AGGREGATE-SCHUR-IDENTITY-v1`

Let

`N=M-MT_23 B^(-1) T_23^T M`,                                          (3.1)

and

`S=T_1^T N T_1`.                                                       (3.2)

Then `S` has rank exactly one. If `lambda_S` denotes its nonzero eigenvalue, then

`boxed( D |lambda_S| = mu. )`                                         (3.3)

#### Proof

The `4 x 4` compressed quadratic matrix in variables `(L_1,L_2,Y,Z)` is

`K=[T_1,T_23]^T M [T_1,T_23]`.                                       (3.4)

Its rank is three because `M` is invertible and the four compressed columns span `R^3`. Since the lower-right pair block `B` is invertible, Schur complementation gives

`rank K = rank B + rank S =2+rank S`,

hence `rank S=1`.

For `ell=1,2`, the principal `3 x 3` minor using compressed coordinate `L_ell` and both scalar banks equals, on one hand,

`det B * S_(ell,ell)`.                                                 (3.5)

On the other hand, by Cauchy--Binet for a `3 x 3` spectral matrix,

`det([t_(1,ell),t_2,t_3]^T M [t_(1,ell),t_2,t_3])
 = det(M) det(t_(1,ell),t_2,t_3)^2`,                                  (3.6)

where `t_(1,ell)` is column `ell` of `T_1`. Summing (3.5)--(3.6) over `ell` gives

`det B * tr S
 = det(M) sum_(ell=1)^2 det(t_(1,ell),t_2,t_3)^2`.                   (3.7)

Because `R_(G_1)=CT_1^T` and `C^TC=I_2`,

`sum_(i in G_1) det(r_i,t_2,t_3)^2
 = sum_(ell=1)^2 det(t_(1,ell),t_2,t_3)^2`.                            (3.8)

Using `t_2=sqrt(lambda_2)v_2`, `t_3=sqrt(lambda_3)v_3`, and summing the collinear coefficients in `G_2,G_3`, the absolute value of the right side of (3.7) is exactly `mu` from (2.8)--(2.9). Since `S` has rank one, `tr S=lambda_S`. Taking absolute values proves (3.3). QED.

The identity is the key coarea currency: the curvature remaining after completing the two scalar banks is paid by the **whole aggregate determinant packet** `mu`; no reciprocal individual physical triple occurs.

## 4. Main theorem: the internal rank-two bank is paid away from scalar-pair isotropy

### Theorem 4.1 — `QFORM-ONE-RANK2-TWO-RANK1-BANK-COAREA-v1`

Under the hypotheses of Section 2,

`boxed(
 ||p_Q||_infinity
 <= 8 * 2^(3/4) * sqrt(5) * (kappa * mu)^(-1/4).
)`                                                                         (4.1)

Numerically the universal prefactor is

`8 * 2^(3/4) * sqrt(5) = 30.084824744691147...`.                       (4.2)

The estimate is uniform in every affine term produced by conditioning outside `S` and therefore applies to the full ambient quadratic form whenever the stated three-bank structure occurs inside an original-coordinate set.

#### Proof

Scale the rank-one-bank aggregates to cap-one variables

`Y'=sqrt(2)Y`, `Z'=sqrt(2)Z`.                                         (4.3)

They remain independent of each other and of the entire first bank. Their pair quadratic block is

`B'=B/2`, so

`D'=D/4`, `kappa'=kappa/2`.                                           (4.4)

Complete this pair. The Schur matrix on the first-bank projection `L` is still exactly `S` from (3.2): scaling the pair columns by `1/sqrt(2)` and the inverse pair block by `2` cancels in the Schur complement. Thus the remaining quadratic curvature is

`lambda_S (q dot L)^2`,                                               (4.5)

for a unit `q in R^2`, plus an arbitrary affine term in the original `G_1` coordinates and a constant. Since `C^TC=I_2`, the original-coordinate coefficient vector `Cq` has Euclidean norm one. Therefore the completed rank-one affine small-ball theorem (1.2) applies with

`H=10/sqrt(|lambda_S|)`.                                               (4.6)

Now apply the pair-log coarea theorem (1.1) to the independent cap-one pair `(Y',Z')` and the independent first-bank remainder. It gives

`||p_Q||_infinity
 <=4 sqrt(2H) (D' kappa')^(-1/4)`

` =4 sqrt(20) |lambda_S|^(-1/4) (D kappa/8)^(-1/4)`

` =8 * 2^(3/4) * sqrt(5)
   (D kappa |lambda_S|)^(-1/4)`.                                     (4.7)

Finally Lemma 3.1 gives `D|lambda_S|=mu`, proving (4.1). Every conditioning step is on disjoint **original-coordinate banks**. No rotated spectral coordinate is declared independent. QED.

### What this theorem adds

The earlier three-rank-one-bank theorem scalarized all three banks. The present result allows one resource-carrying bank to have genuine spectral rank two and to carry arbitrary internal quadratic curvature. The determinant packet is still paid before any physical-triple inversion. The only new denominator is the smallest singular value `kappa` of the compressed quadratic form on the two rank-one scalar banks.

## 5. Actual application to the fresh B10 tripartite packet

Fresh account03/B10 work proves, in its exact-rank-three near-span branch, the existence of three disjoint original-coordinate banks with

`mu = sum_(i in B_1,j in B_2,k in B_3)|det A_{ijk}| >= 1/512`.          (5.1)

Suppose two of those banks are spectral rank one and the third is spectral rank two, and let `kappa` be the smallest singular value of the compressed quadratic matrix on the two rank-one-bank aggregates. If that pair is indefinite and invertible, Theorem 4.1 gives the concrete target-law inequality

`boxed(
 ||p_Q||_infinity
 <= 8*2^(3/4)*sqrt(5) * (512/kappa)^(1/4).
)`                                                                         (5.2)

Thus the B10/B19 `O3-INTERNAL-RANK2-ROUTING` debt is paid on the entire non-isotropic scalar-pair subbranch without selecting any of the potentially tiny `m^3` physical triples.

The exact remaining factor is now explicit:

`QFORM-RANK2BANK-NEAR-ISOTROPIC-SCALARPAIR-v1`:

> in the same aggregate three-bank packet, control the regime in which the two rank-one banks have a singular or arbitrarily small compressed pair `kappa`, or reroute the curvature by splitting/using the rank-two bank before any reciprocal `kappa` payment. A lower bound on `sigma_min(M)` alone does not force such a pair compression away from zero in an indefinite form, because a two-plane may be nearly isotropic.

If two or all three resource-carrying banks have spectral rank at least two, additional routing is also still required. No claim is made that (4.1) exhausts the B10 packet.

## 6. Compatible completed account04 theorem applied to an actual inequality

The exact designated `account04/B05` has no completed current-QFORM artifact at the fresh source check, so none is invented. The completed compatible account04/B18 theorem `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1` states that if a base random variable has density cap `M`, an original independent cap-one scalar supplies a possibly dependent translated square with coefficient `a!=0`, then

`||p_(R+aV_R^2)||_infinity <=2 sqrt(M/|a|)`.                           (6.1)

Apply it to the actual bound (4.1). If an additional disjoint original-coordinate scalar square pivot is present, with arbitrary translation depending on all three active banks, then

`||p_Q||_infinity
 <= 2 [8*2^(3/4)*sqrt(5)]^(1/2)
       |a|^(-1/2)(kappa mu)^(-1/8)`

` < 10.971 |a|^(-1/2)(kappa mu)^(-1/8).`                               (6.2)

This is a genuine application of completed account04 mathematics; it does not pretend the missing account04/B05 partner report exists.

## 7. Scope, continuity, and full-target status

Theorem 4.1 proves an essentially bounded density on the stated aggregate exact-rank-three bank geometry. It does **not** establish a continuous representative; continuity remains unproved in this branch.

It also does not prove the unrestricted owner conjecture. Remaining debts include the near-isotropic/singular compressed scalar-pair regime, configurations with multiple rank-two resource banks, arbitrary extra spectral directions, and the global structural routing that must force one of the already-paid branches from only the hypothesis of three eigenvalues with modulus at least one.

The full QFORM conjecture therefore remains **OPEN / NOT PROVED / NOT DISPROVED**.

## 8. Source pins

- pair-log theorem: `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md` (complete source read this run).
- rank-two affine / rank-one affine small-ball report: `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
- fresh B10 tripartite packet: account03/B10 commit `7acd371ee2ee83a7fae12d7bedb38bc99c051b6d`.
- compatible account04 theorem: account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

Repository transport is not native learned-memory ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.