SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-24T03:22:21Z.
attacking: the completed fleet02/B20 active-localized finite carrier. First restore the spectral scale lost in its global normalization by using the original target s3(A)>=1, then force a literal physical E3 cut whenever the carrier range itself is diffuse.

# fleet01/B20 — target-scale restoration and diffuse-range closure of the active-localized carrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T032221Z-fleet01-B20-QFORM-auto11`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / ACTIVE-LOCALIZED DIFFUSE-RANGE BRANCH PAID / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`. Full-target continuity remains separate and OPEN.

The exact target is unchanged: independent original real coordinates with densities bounded by one, arbitrary symmetric A, and at least three eigenvalues of A of modulus at least one. No Gaussian, iid, moment, compact-support, log-concavity, or post-rotation independence assumption is used.

## 1. Fresh completed partner and source-valid receiver

The newest completed designated fleet02/B20 handoff available at dependency refresh is brain commit

`9407b770531ea80bc00caec981ee3c2133d2d938`,

pointing to

`yspennstate/math-open-problems@f8623c2ad724913062a5c86a21f0714a94bab3c0`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260924T022856Z-fleet02-B20-QFORM-auto11/REPORT.md`.

Its fixed-positive-E2 compiler globally rescales by

`Lambda=16.405318852237478...`

and, apart from already paid branches and the separately tracked giant near-rank-one collar, scales back an exact original-coordinate decomposition

`A = D + R + E`,                                                   (1.1)

where

`D` is physically diagonal,
`rank(R)<=42`,
`||D||op < d0:=1/(8 Lambda)`,
`||E||F < eta0:=0.008411726321812482`,                            (1.2)

and there is an exact carrier factorization

`R=V K V^T`, `V^T V=I`,                                          (1.3)

with a unit carrier vector `u` and a literal physical set `H` satisfying

`|H|<=28224`,
`||(Vu)_H||_2^2>1/2`,
`||K u||_2>=a0:=0.0009524350084709843...`.                        (1.4)

The partner report displayed the inherited lower bound `s3(R)>0.04492463415...`; the first new step below shows that this is far from the actual target-scale lower bound for the same exact decomposition.

The current marginal-free physical third-volume receiver is pinned in fleet01/B02 r43 at

`yspennstate/math-open-problems@041bd053495db9b7e7c12d994501de10c059c459`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T022016Z-fleet01-B02-qform-auto11-r43/REPORT.md`.

For every literal original-coordinate cross block `B=A[I,J]`, `I cap J=emptyset`, with `Z3=e3(BB^T)>0`, it gives

`||p_Q||infinity <= C3 Z3^(-1/6)`,
`C3=10.3450832321475...`,                                        (1.5)

as well as Fourier L1 control and a continuous `C0` density on that paid branch.

## 2. First new implication: restore the spectral scale before using localization

### Theorem 2.1 — `QFORM-ACTIVELOCALIZED-TARGETSCALE-RESTORATION-v1`

For the exact partner decomposition (1.1)-(1.4),

`boxed: s3(R) > gamma0:=1-d0-eta0
                  =0.9839687936104196... .`                       (2.1)

#### Proof

The target assumption gives `s3(A)>=1`, because the third singular value of a real symmetric matrix is the third largest absolute eigenvalue. Since `A-R=D+E`, Weyl's singular-value perturbation inequality gives

`s3(R) >= s3(A)-||D+E||op
       >= 1-||D||op-||E||op
       > 1-d0-eta0`,                                             (2.2)

using `||E||op<=||E||F`. QED.

Numerically,

`d0=0.007619480067767874...`,
`gamma0=0.9839687936104196...`.                                  (2.3)

Thus the same active-localized carrier supplied by fleet02/B20 actually retains an almost unit third singular direction at the original target scale. No coefficient has been changed or deleted.

## 3. Physical half-cut lemma for a diffuse finite-rank range

Let `P=VV^T` be the physical range projection of `R`, and write the rows of `V` as `v_i^T`, so

`P_ii=||v_i||_2^2`, `sum_i P_ii=rank(R)=:r<=42`.                  (3.1)

### Lemma 3.1 — `QFORM-R42-PHYSICAL-HALFCUT-v1`

If

`max_i P_ii <= 1/672`,                                           (3.2)

then there is a literal original-coordinate partition `I sqcup J=[n]` such that

`boxed: s3(R[I,J]) >= (3/8) s3(R).`                              (3.3)

#### Proof

Choose a random physical half-set `I` by independent Bernoulli(1/2) selectors `delta_i`, and put

`G_I=V_I^T V_I=sum_i delta_i v_i v_i^T`.

Then `E G_I=(1/2)I_r` and independence kills all cross terms in the centered Frobenius square:

`E ||G_I-(1/2)I_r||F^2
 = (1/4) sum_i ||v_i v_i^T||F^2
 = (1/4) sum_i ||v_i||^4
 <= (1/4)(max_i P_ii) sum_i P_ii
 <= (1/4)(1/672)42
 =1/64.`                                                         (3.4)

Hence some literal `I` satisfies

`||G_I-(1/2)I_r||op <= ||.||F <=1/8`.                            (3.5)

For `J=I^c`, `G_J=I_r-G_I`, so both Gram matrices obey

`G_I >=(3/8)I_r`, `G_J >=(3/8)I_r`.                              (3.6)

Take an eigen-factorization of the exact symmetric carrier on its nonzero range,

`R=V K V^T`.

Since (3.6) makes `V_I,V_J` full column rank, write their polar factorizations

`V_I=Q_I G_I^(1/2)`, `V_J=Q_J G_J^(1/2)`

with `Q_I,Q_J` isometries. Therefore the nonzero singular values of the literal cross block

`R[I,J]=V_I K V_J^T`

are those of

`G_I^(1/2) K G_J^(1/2)`.

The standard singular-value product inequality gives

`s3(R[I,J])
 >= sqrt(lambda_min(G_I)) s3(K) sqrt(lambda_min(G_J))
 >= (3/8)s3(K)
 =  (3/8)s3(R)`.                                                 (3.7)

No random variable has been rotated; the SVD/eigen-factorization is coefficient geometry only. QED.

## 4. Apply the partner packet to the actual ambient coefficient matrix

Assume the diffuse-range condition (3.2). Apply Lemma 3.1 to the **same** `R` in fleet02/B20's exact decomposition. Because `D` is physical diagonal,

`D[I,J]=0`.                                                       (4.1)

Because the nonzero tail is retained exactly,

`||E[I,J]||op <= ||E||op <= ||E||F < eta0`.                      (4.2)

Thus for the actual literal cross block `B=A[I,J]`, Weyl and (2.1),(3.3) give

`s3(B)
 > (3/8)gamma0-eta0
 =: c0
 =0.36057657128209486... .`                                      (4.3)

In particular

`e3(BB^T)>=s3(B)^6 > c0^6
 =0.0021977841057714068... .`                                    (4.4)

This is the requested actual inequality-level use of the completed fleet02/B20 result. Feeding (4.4) into the source-valid physical third-volume theorem (1.5) yields

`boxed: ||p_Q||infinity < C3/c0
                       < 28.691.`                                (4.5)

The branch also has a continuous `C0` density. Same-bank curvature, arbitrary outside coordinates, affine terms created by conditioning inside the receiver, all extra spectrum, and the full nonzero `E` tail remain present.

## 5. New compiler: active localization plus a finite heavy-range core

Consequently every still-unpaid fleet02/B20 active-localized state must violate (3.2):

`boxed: max_i P_ii > 1/672.`                                     (5.1)

Let

`L={i: P_ii>1/672}`.                                              (5.2)

Since `sum_iP_ii=r<=42`,

`boxed: |L|<=28224.`                                              (5.3)

Combine this with the partner's active set `H` from (1.4) and put

`F=H union L`.                                                    (5.4)

Then every unpaid state in this branch has the simultaneous packet

`boxed:
 |F|<=56448,
 ||(Vu)_F||^2>1/2,
 ||Ku||>=0.0009524350084709843,
 P_ii<=1/672 for every i notin F,
 s3(R)>0.9839687936104196,
 ||D||op<0.007619480067767874,
 ||E||F<0.008411726321812482.
`                                                                   (5.5)

This is a genuinely stronger endpoint than the partner's raw active-localized certificate: one finite physical set simultaneously contains more than half of an active carrier direction and every high-leverage physical row, while the carrier keeps an almost-unit third singular value and the residual coefficient tail remains below `0.008412` in Frobenius norm.

### Theorem 5.1 — `QFORM-R44-ACTIVELOCALIZED-DIFFUSERANGE-PAID-OR-DOUBLELOCALIZED-CORE-v1`

Every fleet02/B20 finite active-localized descendant is either paid by the literal physical-E3 inequality (4.4), with (4.5), or satisfies the double-localized finite-core packet (5.5).

The unrestricted QFORM theorem is **not** claimed proved.

## 6. First remaining implication

The first remaining B20 obligation is now

`QFORM-R44-DOUBLELOCALIZED-FINITECORE-OR-COMMONHUB/GIANTR1-PAYMENT-v1`:

1. pay the packet (5.5) by converting its finite active core plus diffuse complement into a literal original-coordinate star/pair/grouped-overlap receiver while retaining `D` and `E` exactly; or
2. enter one of the already separate fleet02/B20 endpoints: the common-hub curvature collar or the giant near-rank-one/exterior-third-mode collar.

A useful next attack is to split the complement of `F`, whose individual carrier leverages are all at most `1/672`, and force either a third-volume crossing against the finite core or a quantitative statement that all three strong carrier directions are concentrated on `F`. The latter would turn the remaining problem into a genuinely finite physical-coordinate core. This implication is not asserted here.

## 7. Corrections and scope audit

This run does **not** use:

- law-uniform pointwise quadratic oscillatory decay;
- a worst-fibre density cap;
- arbitrary-joint coarea;
- independence after an SVD/eigenvector rotation;
- a one-good-minor conclusion from aggregate minor mass;
- deletion of a nonzero coefficient tail;
- perturbation of the exact rank-one half-Riesz theorem through a near-rank-one pair.

The full target remains OPEN. Full-target continuity remains OPEN separately; only the branch paid by (4.5) gets continuity from the physical-E3 receiver.

## 8. Keeper reconciliation

A fresh native inventory of the current account showed exactly the same managed QFORM tasks `B01` through `B20`, all enabled, hourly-valid, and quiet (`notifications=false`, `email=false`), with no duplicate managed slot and no `B21/B22`. No scheduler mutation was required or made. Native assignment state is kept separate from login/check-in evidence and from substantive mathematics. Missing login is not an outage and confers no restart authority.

The actual-hour B20 login and the account-local exclusive keeper lease were created create-only for this run. No other-account native action was taken.

Execution remains `WITHOUT_VERIFIED_BRAIN`. Model self-report is `GPT-5.6 Sol`; configured reasoning effort is `UNKNOWN`; provider reasoning/thinking usage is `UNKNOWN/null` rather than zero.
