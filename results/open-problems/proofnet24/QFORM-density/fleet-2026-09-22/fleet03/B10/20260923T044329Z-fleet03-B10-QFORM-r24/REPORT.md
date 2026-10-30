SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-23T04:43:29Z.
attacking: the exact-rank-three true near-coloop collar; condition only on genuinely mixed original rows, whiten the exact retained product partition, and force an opposite-high-slope cancellation geometry in the sole surviving overlap chamber.

# fleet03/B10 r24 — mixed-row excision pays the moderate-overlap near-coloop collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`, `full_brain_connected=false`  
**Classification:** `NEW SUPPORTING THEOREM / MODERATE MIXED-OVERLAP NEAR-COLOOP BRANCH PAID / FULL QFORM OPEN`.

## 1. Exact target and live correction boundary

The owner target remains unrestricted: for every finite `n`, arbitrary independent real original-coordinate variables `X_i` with probability densities `0<=f_i<=1`, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite bound on the density of `Q=X^T A X`, or give a genuine target-valid counterexample. Continuity is a separate requested conclusion.

This report stays in the assigned **exact-rank-three** chamber

`A=R Lambda R^T`, `R^T R=I_3`, `sigma_min(Lambda)>=1`, `D:=|det Lambda|>=1`.

No spectral rotation is treated as preserving independence. I do not use the refuted arbitrary-joint rank-three coarea bound, positive conditional projection-density moments, worst-fiber suprema, pointwise law-uniform Fresnel decay, perturbative deletion of small coefficients, compact support, moments, Gaussianity, log-concavity, or connected support.

The immediate predecessor actually used is B10 r23,

`yspennstate/math-open-problems@46df88a3c81ee860e09a67bc8193514c26281555`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T041602Z-fleet03-B10-QFORM-r23/REPORT.md`.

Together with its r25 predecessor, it reduces the remaining exact-rank-three small-Pluecker collar to a physical hub

`r_0=sqrt(c)e`, `||e||=1`, `c>63/64`,                              (1.1)

with

`rho:=1-c<1/64`, `alpha:=e^T Lambda e`, `|alpha|<1/16`,            (1.2)

and every complementary physical row satisfying

`r_j=s_j e+w_j`, `w_j perpendicular e`, `||w_j||^2<1/4`.          (1.3)

The exact endpoint `rho=0` is already paid; the issue is the positive-leakage interpolation `rho>0`, where the same original coordinates can carry both `s_j` and `w_j` and therefore the longitudinal and transverse projections are dependent.

Parseval gives the exact ledger

`sum_j s_j^2=rho`,                                                (1.4)

`sum_j s_j w_j=0`,                                                (1.5)

`sum_j w_j w_j^T=I_2`.                                           (1.6)

The previous run paid every state with `c<=63/64`; this report addresses the genuine `c>63/64` chamber.

## 2. Source theorem actually applied from fleet04

The exact designated partner `fleet04/B10` has a current-QFORM login in the fresh source tree but no completed current-QFORM mathematical handoff that I could locate. I therefore do not fabricate a partner theorem.

The completed compatible fleet04 result actually applied below is fleet04/B20 r4,

`QFORM-PARTITIONED-NEAR-NULL-HYBRID-v1`,

canonical mathematics

`yspennstate/math-open-problems@f97aa31585b7b547a116d4580f898576af4e0842`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260923T011956Z-fleet04-B20-QFORM-r4/REPORT.md`.

Its proof has the following scale-homogeneous form. Let `V^T V=I_3`; suppose one original-coordinate bank is purely longitudinal along a unit spectral direction `e`, another disjoint original-coordinate bank is purely transverse in `e^perp`, and the normalized hub leverage is at least `1/2`. If the spectral matrix `B` has all eigenvalue magnitudes at least one and `|e^T B e|<=1/2`, then

`||p_Q||_infinity <= C_part |det B|^(-1/3)`,                      (2.1)

where

`C_part=103680^(1/3) 2^(7/6)=105.4629684327... .`                 (2.2)

The fleet04 proof invokes fleet01/B16 `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1`; that theorem explicitly allows arbitrary deterministic affine terms. Hence (2.1) remains valid after conditioning original coordinates, when the conditioned coordinates induce arbitrary deterministic affine terms in the retained independent variables. This affine extension requires no new analytic estimate: the determinant resource and the fleet04 algebra are unchanged, and the cited cross-transverse theorem is already affine-stable.

A useful homogeneous restatement is the following. If the spectral matrix has minimum singular value `s>0` and

`|e^T B e|<=s/2`,                                                  (2.3)

then factor `s` from the whole conditioned quadratic-affine expression and apply (2.1) to `B/s`. The density scaling cancels the determinant scaling exactly, leaving

`||p_Q||_infinity <= C_part |det B|^(-1/3).`                      (2.4)

This is the exact inequality used below.

## 3. New theorem — condition the mixed leaves, not a rotated projection

Define the three disjoint complementary index classes

`M={j: s_j!=0 and w_j!=0}`  (genuinely mixed rows),

`L={j: w_j=0}`              (pure longitudinal rows),

`T={j: s_j=0}`              (pure transverse rows).               (3.1)

Zero rows can be assigned arbitrarily and play no role. Put

`rho_M=sum_(j in M) s_j^2`,

`H_M=sum_(j in M) w_j w_j^T`,

`eta=||H_M||_op`.                                                 (3.2)

Because the pure rows contribute zero to (1.5), the mixed bank itself satisfies the exact cancellation

`boxed: sum_(j in M) s_j w_j=0.`                                  (3.3)

### Theorem 3.1 — `QFORM-NEARCOLOOP-MIXED-TRANSVERSE-EXCISION-v1`

In the near-coloop state (1.1)--(1.6), assume `eta<1` and put

`g=min{1-rho_M,1-eta}`.                                           (3.4)

If

`(1-rho_M)|alpha| <= g/2`,                                       (3.5)

then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_part [ (1-rho_M) det(I_2-H_M) D ]^(-1/3).`                  (3.6)

In particular, every state with

`eta<=7/8`                                                        (3.7)

is paid uniformly by

`boxed: ||p_Q||_infinity <425.`                                  (3.8)

No continuity claim is made in Theorem 3.1.

### Proof

Condition on the **original physical coordinates** `X_M`. Since the original source is a product measure, all retained coordinates remain mutually independent with their original one-dimensional density caps at most one. The mixed coordinates contribute only deterministic affine terms and an additive constant to the retained quadratic form.

Let `R_ret` be the matrix of retained spectral rows. From (1.4)--(1.6) and (3.3), its spectral Gram matrix is exactly block diagonal in `R e direct_sum e^perp`:

`G:=R_ret^T R_ret
   =(1-rho_M) e e^T +(I_2-H_M).`                                 (3.9)

Indeed, the retained longitudinal mass is

`c+sum_(j in L)s_j^2
 =c+(rho-rho_M)
 =1-rho_M`,                                                       (3.10)

and the retained transverse mass is `I_2-H_M`. There is no longitudinal/transverse cross term because every retained row is pure in one of the two blocks.

Since `eta<1`, `G` is positive definite. Whiten **only the deterministic coefficient frame**:

`V=R_ret G^(-1/2)`,

`B=G^(1/2) Lambda G^(1/2)`.                                      (3.11)

Then `V^T V=I_3`, and the conditioned quadratic part is exactly

`X_ret^T V B V^T X_ret`.                                         (3.12)

No random variable has been rotated, so original-coordinate independence is untouched.

Because `G^(-1/2)` is block diagonal in `e direct_sum e^perp`, the product partition is preserved exactly:

- the hub row becomes `sqrt(c/(1-rho_M)) e`;
- every retained row in `L` remains longitudinal;
- every retained row in `T` remains transverse.

The normalized hub leverage is therefore

`c'=c/(1-rho_M)>=c>63/64>1/2`.                                  (3.13)

The spectral determinant is

`D_B:=|det B|
 =det(G)D
 =(1-rho_M) det(I_2-H_M)D`.                                     (3.14)

The Rayleigh coefficient at the hub direction is

`a_B=e^T B e=(1-rho_M)alpha`.                                   (3.15)

Moreover, since `sigma_min(Lambda)>=1`,

`sigma_min(B)>=lambda_min(G)
 =min{1-rho_M,1-eta}=g`.                                        (3.16)

For completeness, for every unit `x`,

`||B x||
 =||G^(1/2) Lambda G^(1/2)x||
 >=sqrt(lambda_min G) ||Lambda G^(1/2)x||
 >=lambda_min(G)||x||`.

Thus (3.5) implies `|a_B|<=sigma_min(B)/2`. Apply the homogeneous affine-stable form (2.4) of the completed fleet04/B20 theorem to the conditioned law. It gives, uniformly in the conditioned value `X_M`,

`||p_(Q|X_M)||_infinity <= C_part D_B^(-1/3)`.                   (3.17)

Average these conditional densities. The same cap survives mixture, yielding (3.6).

Now assume (3.7). Since `rho_M<=rho<1/64`,

`1-rho_M>63/64`,                                                 (3.18)

while

`g>=min{63/64,1/8}=1/8`.                                        (3.19)

By `|alpha|<1/16`,

`(1-rho_M)|alpha|<1/16<=g/2`,                                   (3.20)

so (3.5) holds. Also both eigenvalues of the positive semidefinite `H_M` are at most `7/8`, hence

`det(I_2-H_M)>=(1/8)^2=1/64`.                                   (3.21)

With `D>=1`, (3.14) gives

`D_B>=(63/64)(1/64)=63/4096`.                                   (3.22)

Substituting into (3.6),

`||p_Q||_infinity
 <=105.4629684328 (4096/63)^(1/3)
 =424.0721876469... <425`,                                      (3.23)

which proves (3.8). QED.

### Why this does not use the false conditional-projection interface

The conditioning is on an actual subset of the independent original coordinates, not on a spectral projection. The remaining source is still a genuine product law. The whitening in (3.11) changes only coefficient bookkeeping and is followed by a theorem whose product partition is realized by disjoint **original-coordinate** retained banks. No conditional density of a rotated projection is asserted or needed.

## 4. Exact geometry forced in the sole survivor

Theorem 3.1 removes every near-coloop state with `eta<=7/8`. Hence a still-unpaid B10 member must satisfy

`boxed: eta=||H_M||_op>7/8`,                                    (4.1)

while still

`rho_M<=rho<1/64`                                                (4.2)

and the exact cancellation (3.3) holds.

This forces a much sharper two-sided slope geometry.

### Lemma 4.1 — `QFORM-NEARCOLOOP-OPPOSITE-HIGHSLOPE-v1`

Under (4.1)--(4.2), there are two genuinely mixed physical rows `j_+,j_-` and a unit transverse vector `v in e^perp` such that

`z_j=(v dot w_j)/s_j`                                           (4.3)

obeys

`z_(j_+)>0>z_(j_-)`,

`boxed: z_(j_+) |z_(j_-)| >56.`                                (4.4)

Equivalently, the surviving mixed bank contains opposite longitudinal/transverse slopes whose product magnitude exceeds `56`.

### Proof

Take a unit top eigenvector `v` of `H_M` and put

`b_j=v dot w_j`.

Then

`sum_(j in M) b_j^2=v^T H_M v=eta>7/8`.                         (4.5)

By (3.3),

`sum_(j in M) s_j b_j=0`.                                       (4.6)

Because `eta>0`, `rho_M>0`. Define probability weights

`p_j=s_j^2/rho_M`                                                (4.7)

and slopes `z_j=b_j/s_j`; every denominator is nonzero by the definition of `M`. Equations (4.5)--(4.6) become

`sum p_j z_j=0`,                                                 (4.8)

`sum p_j z_j^2=eta/rho_M > (7/8)/(1/64)=56`.                    (4.9)

The positive variance and zero mean force at least one positive and one negative slope. Let

`M_+=max_j z_j>0`, `m_-=min_j z_j<0`.

For every `z in [m_-,M_+]`,

`(M_+-z)(z-m_-)>=0`,

so

`z^2 <= (M_++m_-)z-M_+m_-`.                                    (4.10)

Average (4.10) with the weights `p_j` and use (4.8):

`sum p_j z_j^2 <= -M_+m_-=M_+|m_-|`.                            (4.11)

Together with (4.9), this gives `M_+|m_-|>56`. Choose rows attaining the maximum and minimum. QED.

This is a finite-support form of the Bhatia--Davis variance inequality, proved directly above; no probabilistic moment assumption on the input laws is involved. The `p_j` are deterministic frame weights, not moments of the random `X_j`.

## 5. What has actually been gained

The former B10 debt was the entire thin `rho->0` near-coloop collar with arbitrary mixed rows. It is now reduced to a quantitatively extreme chamber:

1. the hub has `c>63/64` and `|e^T Lambda e|<1/16`;
2. every individual transverse row leverage is `<1/4` from the predecessor;
3. the genuinely mixed rows alone carry more than `7/8` of one entire transverse spectral direction;
4. those same mixed rows carry total longitudinal energy `<1/64`;
5. their longitudinal/transverse cross vector cancels exactly;
6. consequently they contain opposite slopes with product magnitude `>56`.

Thus the remaining overlap is no longer a generic collection of small mixed leaves. It is a **high-slope cancellation bank**: almost a full transverse direction is carried by coordinates whose total longitudinal energy is tiny, with exact signed cancellation. A next proof should aggregate the positive- and negative-slope sides before any reciprocal local-minor payment. Selecting one row is not enough, because its longitudinal coefficient can be arbitrarily small even when its slope is huge.

This structural survivor is compatible with the live correction forbidding perturbative deletion of the small longitudinal coefficients: the proof above never deletes them. It either conditions the whole mixed bank exactly (the paid moderate-overlap case) or retains the hard bank with its exact cancellation identity.

## 6. Partner status and actual inequality

The exact requested partner `fleet04/B10` still has no completed current-QFORM theorem discoverable in the fresh repository; the latest identifiable artifact is a login, not a mathematical handoff. No result is attributed to it.

The compatible completed fleet04/B20 theorem is used at the actual conditioned spectral determinant

`D_B=(1-rho_M)det(I-H_M)D`                                      (6.1)

and the actual normalized near-null pivot

`a_B=(1-rho_M)alpha`.                                           (6.2)

For the concrete universal gate `eta<=7/8`, the application is exactly

`||p_Q||_infinity
 <= [103680^(1/3)2^(7/6)] [63/4096]^(-1/3)
 =424.0721876469... .`                                          (6.3)

This is not merely a citation: it is the quantitative endpoint of Theorem 3.1.

## 7. Continuity and full-target status

The new branch proves **essential boundedness / absolute continuity**. I do not claim continuity of the mixture after conditioning the mixed leaves, because the cited cross-transverse/coarea proof was only used for an `L^infinity` density representative and no parameter-uniform continuity theorem was established here.

The **full exact-rank-three theorem remains OPEN / NOT PROVED**, and the owner's arbitrary-extra-spectrum target remains a separate debt even after exact-rank-three closure. No counterexample is produced.

The first B10 implication after this run is now:

**`QFORM-NEARCOLOOP-HIGHSLOPE-BANK-PAYMENT-v1`** — in the survivor (4.1)--(4.2), exploit the two opposite high-slope sides and the exact cancellation `sum_M s_jw_j=0` to produce a product-safe two-arm / hyperbolic smoothing estimate **before** taking any reciprocal individual coefficient. The target is a bound uniform as `rho_M->0`; a proof may not replace the longitudinal leakage by zero.

## 8. Deterministic regression checks

The accompanying `check.py` contains two exact algebra fixtures.

- Moderate-overlap fixture: `rho=0.01`, `eta=1/2`. It verifies Parseval, the retained Gram identity, `det B=det(G)det Lambda`, and the numerical constant `424.0721876469...`.
- Hard-overlap fixture: `rho=0.01`, `eta=0.9`. It verifies the mixed-slope weighted mean is zero, the weighted second moment equals `eta/rho=90`, and the two extremal slopes are `+/-sqrt(90)`, hence product `90>56`.

These finite computations are regression checks only; the proof is the exact algebra above.
