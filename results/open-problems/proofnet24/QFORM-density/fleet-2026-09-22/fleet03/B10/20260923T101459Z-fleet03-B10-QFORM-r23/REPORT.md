SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-23T10:14:59Z.
attacking: single-null-hub mixed-row survivor; convert the exact product-frame cancellation into a constant hub-star / principal-triple packet, then apply the completed fleet04/B10 three-bank theorem to an actual quantitative inequality.

# fleet03/B10 r23 — constant star curvature and a partner three-bank packet in the single-null-hub survivor

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `NEW_EXACT_STRUCTURAL_IDENTITY / DESIGNATED_PARTNER_APPLIED / UNIFORM_SUBCRITICAL_ANTICONCENTRATION / FULL_TARGET_OPEN`.

The full conjecture remains OPEN. This report works only in the exact-rank-three chamber left by fleet03/B10 r22. It proves that the apparent mixed-row obstruction cannot lose all physical curvature: the single null hub has a dimension-free aggregate off-diagonal row norm and a dimension-free aggregate principal-triple packet. The newly completed designated partner `fleet04/B10` then splits a fixed positive fraction of that packet into two disjoint transverse original-coordinate banks while retaining a fixed positive fraction of the longitudinal leakage in a third disjoint bank. A completed product-projection theorem converts the whole hub star into a uniform square-root small-ball / quarter-Riesz bound. The final `L^infinity` receiver combining these currencies is still unpaid.

No Gaussianity, moment, bounded-support, connected-support, log-concavity, diagonal-basis, post-rotation independence, arbitrary-joint coarea, conditional-density supremum, or perturbative deletion of small coefficients is used. Continuity is not newly proved in the surviving branch.

## 1. Fresh sources and correction boundary


The immediate B10 predecessor is

`yspennstate/math-open-problems@36d17401e6c910bd4ef856fcd4082b95d0f5c23d`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T011306Z-fleet03-B10-QFORM-r22/REPORT.md`.

Its surviving exact-rank-three state is recalled in Section 2.

The designated partner is now genuinely available and was read at its canonical proof source:

`yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B10/20260923T061725Z-fleet04-B10-QFORM-r4/REPORT.md`.

Its theorem `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1` is applied in Section 5.

The product-projection and scalar-star inputs are read from

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`

and

`yspennstate/math-open-problems@e8bd09a6e9c8dbe964b87f52ff9b5b6d13421958`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260923T052643Z-e284cc399d47/REPORT.md`.

The live corrections consumed include `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1`, `QFORM-CONDITIONAL-PROJECTION-POSITIVE-MOMENT-FALSE-v1`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, and the local-minor/cross-rank extraction failures in the current correction inbox. Nothing below invokes a challenged premise.

## 2. Exact survivor from r22

Write the exact-rank-three form as

`A = R M R^T`, `R^T R = I_3`,                                      (2.1)

where the physical rows of `R` are `u_i in R^3`. Since the three nonzero eigenvalues of `A` have modulus at least one,

`D:=|det M| >= 1`, `sigma_min(M)>=1`.                              (2.2)

The r22 survivor contains one ORIGINAL physical coordinate, indexed by `0`,

`u_0=sqrt(h) r`, `||r||=1`, `h>55/64`, `r^T M r=0`.              (2.3)

There may be additional rows exactly collinear with `r`, of total leverage less than `1/64`. All remaining rows form a complementary bank `C` and have the unique decomposition

`u_j=t_j r+y_j`, `y_j in r^perp`, `j in C`,                         (2.4)

with the exact Parseval ledger

`sum_(j in C) t_j^2 =: rho = 1-L <=1/8`,                            (2.5)

`sum_(j in C) y_j y_j^T = I_(r^perp)`,                              (2.6)

`sum_(j in C) t_j y_j =0`,                                          (2.7)

`||y_j||^2<=1/2`.                                                     (2.8)

The still-unpaid r22 branch has at least one genuinely mixed row, hence `rho>0`.

Set

`b:=M r`.                                                             (2.9)

Because `r^TMr=0`, `b` lies in `r^perp`. By (2.2),

`||b||=||Mr||>=1`.                                                    (2.10)

## 3. The null hub has a constant aggregate physical star

### Theorem 3.1 — `QFORM-SINGLE-NULL-HUB-STAR-IDENTITY-v1`

In the state (2.1)-(2.10),

`boxed: sum_(j!=0) A_(0j)^2 = h ||M r||^2 >= h >55/64.`             (3.1)

Consequently, if

`sigma_0 := (sum_(j!=0) A_(0j)^2)^(1/2)`,                            (3.2)

then

`boxed: sigma_0 >= sqrt(h) > sqrt(55/64).`                            (3.3)

#### Proof

For a complementary row (2.4), using the nullity in (2.3),

`A_(0j)=u_0^T M u_j
        =sqrt(h) r^T M(t_j r+y_j)
        =sqrt(h) b dot y_j`.                                         (3.4)

Every additional row collinear with `r` has zero coupling to the hub, again by `r^TMr=0`. Therefore (2.6) gives

`sum_(j!=0) A_(0j)^2
 = h sum_(j in C)(b dot y_j)^2
 = h b^T (sum_j y_jy_j^T)b
 = h||b||^2`.                                                         (3.5)

Equation (2.10) proves (3.1)-(3.3). QED.

This identity is important because no individual physical edge need be large. The entire off-diagonal row is aggregated before any reciprocal exponent is paid.

## 4. The same hub carries a constant aggregate principal-triple packet

### Theorem 4.1 — `QFORM-SINGLE-NULL-HUB-TRIPLE-PACKET-v1`

The complete fixed-hub principal-triple packet satisfies

`boxed:
 sum_(j<k; j,k in C) |det A_{ {0,j,k} }| = D h >= h >55/64.
`                                                                         (4.1)

#### Proof

For every physical triple `I` in an exact-rank-three representation,

`|det A_I|=D det(R_I)^2`.                                             (4.2)

For `I={0,j,k}`, multilinearity and (2.4) give

`det(u_0,u_j,u_k)^2
 =h det(r,y_j,y_k)^2`.                                                (4.3)

By the two-dimensional Cauchy--Binet identity and (2.6),

`sum_(j<k) det(r,y_j,y_k)^2
 =det_(r^perp)(sum_j y_jy_j^T)
 =1`.                                                                 (4.4)

Summing (4.2)-(4.4) proves (4.1). QED.

Thus the single-null-hub survivor is not a vanishing-curvature state. Its difficulty is solely that the constant packet may be diffuse over many original-coordinate triples.

## 5. Actual application of the designated partner fleet04/B10

Apply fleet04/B10's completed `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1` to the complementary bank `C`, with distinguished direction `r`, longitudinal coefficients `t_j`, and transverse rows `p_j=y_j`.

Here the transverse Gram is exactly

`G=sum_j y_jy_j^T=I_2`.                                               (5.1)

The regression vector in the partner notation is

`w=G^(-1)sum_j t_jy_j=0`                                              (5.2)

by (2.7), so its regression residuals are exactly

`e_j=t_j`, `rho=sum_j e_j^2`.                                        (5.3)

The partner theorem therefore supplies a partition of ORIGINAL coordinates

`C=S disjoint_union Y disjoint_union Z`                               (5.4)

such that, with

`rho_S=sum_(i in S)t_i^2`,
`G_Y=sum_(j in Y)y_jy_j^T`,
`G_Z=sum_(k in Z)y_ky_k^T`,                                          (5.5)

and

`M_2(G_Y,G_Z):=tr(adj(G_Y)G_Z)
              =sum_(j in Y,k in Z) det(y_j,y_k)^2`,                  (5.6)

one has the actual inequality

`boxed: rho_S M_2(G_Y,G_Z) >= (2/81) rho.`                            (5.7)

Because `rho_S<=rho` and the total pair-volume in (4.4) is one,

`M_2(G_Y,G_Z)<=1`.                                                    (5.8)

Since `rho>0`, (5.7)-(5.8) separately force

`boxed: rho_S >= (2/81)rho,`                                         (5.9)

`boxed: M_2(G_Y,G_Z) >= 2/81.`                                       (5.10)

This is the required inequality-level use of the **designated** partner result.

Combining (5.10) with the fixed-hub determinant identity gives a dimension-free, disjoint-bank subpacket:

`sum_(j in Y,k in Z)|det A_{ {0,j,k} }|
 =D h M_2(G_Y,G_Z)
 >=(2D h)/81
 >55/2592
 =0.0212191358... .`                                                  (5.11)

Moreover the leakage and curvature currencies coexist quantitatively:

`boxed:
 rho_S * sum_(j in Y,k in Z)|det A_{ {0,j,k} }|
 >= (2D h/81) rho
 > (55/2592) rho.
`                                                                         (5.12)

The source groups `S`, `Y`, and `Z` are disjoint original-coordinate banks, and the hub coordinate is disjoint from all three. Thus (5.9)-(5.12) preserve genuine product provenance. No spectral-coordinate independence is asserted.

## 6. Whole-star product aggregation gives uniform square-root anti-concentration

The completed weighted product-projection theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` says that a normalized one-dimensional linear form of independent cap-one variables has density cap at most `sqrt(e)`.

Define, using all original coordinates other than the hub,

`Z_0:=sum_(j!=0) A_(0j)X_j`.                                         (6.1)

By (3.2), `Z_0/sigma_0` is a normalized product projection, hence

`||p_(Z_0)||_infinity <= sqrt(e)/sigma_0`.                            (6.2)

Because `A_00=h r^TMr=0`, the full quadratic form has the exact original-coordinate representation

`Q=2X_0 Z_0+W`,                                                       (6.3)

where `W` is an arbitrary measurable quadratic-plus-affine function of all variables other than `X_0`; importantly, `X_0` is genuinely independent of the pair `(Z_0,W)`.

The `a=0` part of fleet02/B06's completed `QFORM-NONNULL-STAR-QUARTER-RIESZ-v1` gives, for a scalar `X` of density cap `K`, a scalar `Z` of density cap `L`, and arbitrary dependence between `Z` and `W`,

`P(2XZ+W in I)<=2 sqrt(K L |I|)`.                                    (6.4)

Apply (6.4) with `K=1` and (6.2). For every interval `I` of length `eps`,

`P(Q in I)
 <=2 e^(1/4) sigma_0^(-1/2) eps^(1/2)
 <=2 e^(1/4) h^(-1/4) eps^(1/2)
 <2.668 eps^(1/2).`                                                   (6.5)

Thus the whole mixed-row survivor has a **dimension-free square-root small-ball bound** before any local edge or local triple is selected.

The same estimate gives a useful fractional-potential currency. If `0<alpha<1/2`, then from (6.4) on the interval `(t-rho,t+rho)`,

`P(|Q-t|<rho)<=min(1,2 sqrt(2KL rho))`.                               (6.6)

Layer cake gives

`boxed:
 H_alpha(Q):=sup_t E|Q-t|^(-alpha)
 <= (8KL)^alpha/(1-2alpha).
`                                                                         (6.7)

At `alpha=1/4`,

`H_(1/4)(Q)
 <=2^(7/4)e^(1/8)sigma_0^(-1/4)
 <=2^(7/4)e^(1/8)h^(-1/8)
 <3.885.`                                                              (6.8)

This does **not** imply an `L^infinity` density bound. The live B06 endpoint example shows that a general star estimate cannot simply be promoted to the half-Riesz exponent `alpha=1/2`; the third-direction packet (5.11) must be used before that endpoint.

## 7. What this removes, and the exact next implication

The r22 single-null-hub mixed-row survivor can no longer be described as suffering from vanishing local geometry in aggregate. Uniformly over dimension and all admissible input laws it has simultaneously:

1. a physical hub row with `sigma_0^2>55/64`, equation (3.1);
2. total hub principal-triple mass `>55/64`, equation (4.1);
3. after the designated partner's product-preserving partition, a disjoint `Y x Z` hub-triple subpacket `>55/2592`, equation (5.11);
4. a third disjoint bank `S` retaining at least `2/81` of the longitudinal leakage energy, equation (5.9);
5. an unconditional square-root small-ball bound `<2.668 sqrt(eps)` and quarter-Riesz bound `<3.885`, equations (6.5) and (6.8).

Every one of these statements is independent of the number of physical coordinates. Individual edges and individual principal triples may still tend to zero.

The first unpaid implication is therefore

`QFORM-NULL-HUB-THREEBANK-PACKET-TO-LINFINITY-v1`:

> Starting from the exact state above, combine the zero-diagonal hub `X_0`, the disjoint original-coordinate leakage bank `S`, and the two disjoint transverse banks `Y,Z` satisfying (5.9)-(5.12), to prove a universal `L^infinity` density bound without selecting one tiny edge/triple, taking a worst conditional-density supremum, or perturbatively discarding the same-bank longitudinal/transverse contamination.

A plausible receiver must use the `S/Y/Z` product provenance **before** collapsing these banks to dependent spectral projections. The natural endpoint is to upgrade the subcritical star currency (6.8) with the constant third-direction packet (5.11), rather than trying to prove the false universal half-Riesz star bound.

The full exact-rank-three theorem remains OPEN, and arbitrary additional spectrum remains a separate full-target debt. Essential boundedness and continuity are not claimed for this surviving branch in this report.

## 8. Integrity summary

- Target quantifiers: unchanged.
- Designated partner actually used: `fleet04/B10`, canonical commit `afdea9634d9e3f5fb09659da436292cf7dbe5b20`, at equations (5.7)-(5.12).
- Product projection source actually used: `fleet02/B06`, canonical commit `8dd33c1abd4fd64140f59032feda2b13d4351da5`.
- Star small-ball source actually used: `fleet02/B06`, canonical commit `e8bd09a6e9c8dbe964b87f52ff9b5b6d13421958`.
- Numerical decimals are evaluations of proved closed-form constants only; no Monte Carlo evidence is used as proof.
- Native brain ingestion was not authenticated or verified: `WITHOUT_VERIFIED_BRAIN`.
- No task/schedule, enabled/paused state, notification/email setting, public workflow, paid model/API/Codex call, or cross-account native action was changed.
