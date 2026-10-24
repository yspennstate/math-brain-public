SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B10, 2026-09-22T21:46:31Z.
attacking: the small-residual / near-span exact-rank-three chamber by replacing reciprocal cross-rank payment with an exterior-volume stratification that stays nondegenerate as the leakage residuals tend to zero.

# account03/B10 r19 — near-span leakage compiles to a constant aggregate principal-triple bank

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Rank-three coupled case  
**Fresh owner control at start:** revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL TARGET OPEN`

## 0. Scope and correction boundary

The target remains the unrestricted statement for independent ORIGINAL-coordinate real inputs with densities `0<=f_i<=1` and symmetric `A` with at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, or diagonal-basis hypothesis is added. General spectral rotation is not treated as preserving independence. Continuity is recorded separately from essential boundedness.

The live corrections remain binding. In particular this report does **not** use the refuted arbitrary-joint rank-three coarea inequality, a positive conditional projection-density moment, law-uniform pointwise quadratic-phase decay, a worst fiber supremum, or perturbative deletion of small coefficients under unrestricted supports.

The exact designated partner `account04/B10` still has no completed current-QFORM report or handoff visible at the fresh lookup, so no partner result is invented. The completed compatible account04 result actually applied below is account04/B16,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T161909Z-account04-B16-QFORM-r2/REPORT.md`,

whose fixed-pair determinant-bank identity is used in Section 5 on the actual near-unit branch.

The principal earlier inputs are:

1. account03/B10 r18, `QFORM-THREE-CROSS-GEOMEAN-v1` and the remaining mechanism `QFORM-HEAVY-NULL-SMALLRESIDUAL-OR-DOUBLEHIGH-v1`;
2. account03/B19, `QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1`;
3. account02/B19, `QFORM-NULLROW-TWOBANK-SPAN-OR-CROSSRANK3-v1`, which pays the exact span endpoint and every leakage residual bounded away from zero, leaving `QFORM-NULLROW-TWOBANK-NEARSPAN-UNIFORMITY-v1`;
4. account03/B14, `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1`, which pays any one physical principal triple with determinant bounded below.

This run changes mechanism: rather than paying a reciprocal power of the small leakage residual, it keeps the whole exterior-volume bank and computes its exact four-stratum decomposition.

## 1. Exact compressed heavy-null state

Work in the exact-rank-three compressed state already reached by B10. Write

`A = R M R^T`, `R^T R = I_3`,

with `M` invertible symmetric, and let

`D=|det M|>=1/2`.

There is a distinguished ORIGINAL independent cap-one coordinate `X_0` whose spectral row is

`u_0=sqrt(c) r`, `c>=7/9`,

where `r` is a unit `M`-null vector. In the orthonormal spectral basis `(r,e,w)`, write each complementary row as

`u_j=(alpha_j,v_j)`, `v_j=(beta_j,gamma_j) in R^2`.

Parseval gives

`sum_j alpha_j^2 = 1-c`,
`sum_j alpha_j v_j = 0`,
`sum_j v_j v_j^T = I_2`.                                          (1.1)

Use the completed B19 original-coordinate partition into disjoint banks `J,K`. Put

`S_G=sum_(j in G) v_jv_j^T`, `G=J,K`.

Then

`S_J+S_K=I_2`,
`det S_J det S_K >=1/640`,

and in particular both `S_J,S_K` are positive definite. Let `V_G` be the matrix whose rows are `v_j`. Make the exact least-squares decompositions

`alpha_G=V_G p_G+eta_G`,
`V_G^T eta_G=0`,
`tau_G=||eta_G||^2`.                                               (1.2)

The near-span debt is precisely the regime where both `tau_J,tau_K` are positive but arbitrarily small.

## 2. New exact identity: the slope gap exhausts the non-residual longitudinal energy

Define

`delta=p_J-p_K`.                                                   (2.1)

### Theorem 2.1 — `QFORM-TWOBANK-SLOPEGAP-ENERGY-v1`

In the state above,

`boxed: p_J=S_K delta,   p_K=-S_J delta,`                         (2.2)

and

`boxed:
 1-c = tau_J+tau_K + delta^T S_J S_K delta.
`                                                                     (2.3)

### Proof

The cross-column Parseval identity in (1.1) is

`0=sum_j alpha_jv_j = S_Jp_J+S_Kp_K`,                            (2.4)

because `V_G^T eta_G=0`. Since `p_J=p_K+delta` and `S_J+S_K=I`,

`0=p_K+S_Jdelta`,

which gives `p_K=-S_Jdelta` and then `p_J=S_Kdelta`.

The longitudinal Parseval identity and orthogonality in (1.2) give

`1-c=tau_J+tau_K+p_J^TS_Jp_J+p_K^TS_Kp_K`.                      (2.5)

Because `S_K=I-S_J`, the two matrices commute. Substituting (2.2),

`p_J^TS_Jp_J+p_K^TS_Kp_K`
`=delta^T(S_KS_JS_K+S_JS_KS_J)delta`
`=delta^T S_JS_K(S_J+S_K)delta`
`=delta^T S_JS_Kdelta`,

which is (2.3). QED.

Since the eigenvalues of `S_JS_K` are `lambda(1-lambda)`, one always has

`0 < S_JS_K <= (1/4)I_2`.                                        (2.6)

Therefore

`|delta|^2 >=4(1-c-tau_J-tau_K)`.                               (2.7)

For example, if `tau_J+tau_K<=1/32` and `c<=61/64`, then

`1-c-tau_J-tau_K >=1/64`,

so

`boxed: |delta|>=1/4.`                                           (2.8)

Conversely, if `tau_J+tau_K<=1/32` and `|delta|<1/4`, then (2.3),(2.6) imply

`1-c <1/32+1/64=3/64`,

hence

`boxed: c>61/64.`                                                (2.9)

Thus the apparent near-span discontinuity is forced either into a quantitative two-bank slope gap or into the near-unit heavy-null endpoint.

## 3. Exact four-stratum exterior-volume formula

Let `U_G` be the physical-row matrix on bank `G`, with rows `(alpha_j,v_j)`. Define the four spectral triple-volume strata

`E_30=sum_{i<j<k in J} det(u_i,u_j,u_k)^2`,
`E_21=sum_{i<j in J, k in K} det(u_i,u_j,u_k)^2`,
`E_12=sum_{i in J, j<k in K} det(u_i,u_j,u_k)^2`,
`E_03=sum_{i<j<k in K} det(u_i,u_j,u_k)^2`.                      (3.1)

### Theorem 3.1 — `QFORM-TWOBANK-MIXED-EXTERIOR-STRATA-v1`

One has the exact identities

`boxed: E_30=tau_J det S_J,`                                     (3.2)

`boxed:
 E_21=det S_J (tau_K+delta^T S_Kdelta)
      +tau_J det S_J tr(S_J^(-1)S_K),
`                                                                     (3.3)

`boxed:
 E_12=det S_K (tau_J+delta^T S_Jdelta)
      +tau_K det S_K tr(S_K^(-1)S_J),
`                                                                     (3.4)

`boxed: E_03=tau_K det S_K.`                                     (3.5)

Moreover

`boxed: E_30+E_21+E_12+E_03=1-c.`                              (3.6)

Every term displayed in (3.2)--(3.5) is nonnegative.

### Proof

Apply the determinant-one spectral shear

`(alpha,v) -> (alpha-p_J dot v, v)`.

It preserves every `3x3` row determinant. On bank `J`, the sheared Gram matrix is exactly

`K_J'=diag(tau_J,S_J)`.                                          (3.7)

On bank `K`, using `p_K-p_J=-delta`, it is

`K_K'=[[tau_K+delta^TS_Kdelta, -delta^TS_K],`
`      [-S_Kdelta, S_K]].`                                       (3.8)

Cauchy--Binet says that `E_21` is the coefficient of `t^2s` in

`det(tK_J'+sK_K')`.                                              (3.9)

For `tau_J>0`, that coefficient equals

`det(K_J') tr((K_J')^(-1)K_K')`,

which is exactly (3.3). The identity extends to `tau_J=0` by polynomial continuity. The same calculation after shearing by `p_K` gives (3.4). Equations (3.2),(3.5) are ordinary Cauchy--Binet on each bank.

Finally the Gram matrix of all complementary rows is, by (1.1),

`U_{J union K}^T U_{J union K}=diag(1-c,1,1)`.

A final Cauchy--Binet expansion over all complementary triples gives (3.6). QED.

This is the crucial nonperturbative point: as `tau_J,tau_K ->0`, the mixed strata need not collapse. The slope mismatch is stored as actual rank-three exterior volume across the two original-coordinate banks.

## 4. First unpaid implication converted to a constant aggregate O3 packet

Assume the genuine near-span region

`tau_J+tau_K <=1/32`.                                           (4.1)

If

`c<=61/64`,                                                       (4.2)

then (3.2),(3.5) and `det S_G<=1` give

`E_21+E_12`
`=1-c-E_30-E_03`
`>=1-c-tau_J-tau_K`
`>=1/64`.                                                         (4.3)

Therefore at least one mixed stratum satisfies

`boxed: max(E_21,E_12)>=1/128.`                                 (4.4)

For every physical triple `I` in exact rank three,

`det A_{I,I}=det(M) det(R_I)^2`,

so all principal-triple determinants have the sign of `det M` and

`|det A_{I,I}|=D det(R_I)^2`.                                   (4.5)

Combining (4.4) with `D>=1/2` gives the target-scale aggregate determinant packet

`boxed:
 max{
  sum_{i<j in J,k in K}|det A_{ {i,j,k} }|,
  sum_{i in J,j<k in K}|det A_{ {i,j,k} }|
 }
 >=1/256.
`                                                                     (4.6)

Thus the small-positive-residual branch away from the near-unit endpoint no longer loses a reciprocal power of `tau`. It carries a **constant aggregate principal-triple bank** on one of the two explicit mixed original-coordinate compositions.

This is not yet an `L^infinity` theorem. Diffuse frames can spread a constant principal-minor mass over arbitrarily many tiny triples, so selecting one triple would reintroduce a dimension loss. The correct remaining interface is aggregate-before-inversion.

As a local exit, if one triple in the bank has determinant at least `eta>0`, the completed account03/B14 theorem gives immediately

`||p_Q||_infinity <=32 sqrt(10) eta^(-1/3)`.                     (4.7)

Hence the only unclosed part of (4.6) is genuinely diffuse at whatever fixed atom threshold one chooses.

## 5. Compatible account04 theorem applied: the near-unit half of the dichotomy

Now suppose instead

`c>61/64`.                                                        (5.1)

The completed compatible account04/B16 fixed-pair theorem gives, for the heavy null row `0` and every complement row `j`,

`P_0j:=sum_{k ne 0,j}|det A_{ {0,j,k} }|=D c h_j`,
`h_j=||v_j||^2`.                                                  (5.2)

This is an actual theorem application. Summing (5.2) over every complement `j` and using `sum_j h_j=tr I_2=2`, while observing that each unordered triple `{0,j,k}` is counted twice, yields the exact aggregate identity

`boxed:
 sum_{j<k}|det A_{ {0,j,k} }|=D c.
`                                                                     (5.3)

Under `D>=1/2` and (5.1),

`boxed:
 sum_{j<k}|det A_{ {0,j,k} }| >61/128.
`                                                                     (5.4)

This is much stronger than the `1/256` mixed-bank resource in (4.6). It also remains nonzero at the exact unit-leverage endpoint `c=1`, consistently with the completed null-scalar endpoint theorem.

Because `A_00=0`, any single heavy-row triple atom of size at least `eta` is additionally paid by the one-zero-diagonal physical-triple theorem with

`||p_Q||_infinity <=3*2^(2/3) eta^(-1/3)`.                       (5.5)

If no such atom exists, (5.4) is an explicitly quantified diffuse heavy-null wedge bank, exactly the kind of aggregate packet that the current B11 line identifies as needing a product-preserving trace inequality.

## 6. Unified compiler for the near-span obstruction

Sections 4--5 prove the following theorem.

### Theorem 6.1 — `QFORM-NEARSPAN-TO-O3-AGGREGATE-v1`

In the compressed heavy-null exact-rank-three B10 state with `D>=1/2`, `c>=7/9`, and B19 two-bank partition, assume

`tau_J+tau_K<=1/32`.                                             (6.1)

Then at least one of the following **original-coordinate principal-triple banks** has aggregate absolute determinant mass at least `1/256`:

1. triples with two indices in `J` and one in `K`;
2. triples with one index in `J` and two in `K`;
3. triples containing the distinguished heavy null coordinate `0`.

More precisely, if `c<=61/64`, one of (1),(2) has mass at least `1/256`; if `c>61/64`, bank (3) has mass greater than `61/128`.

No reciprocal leakage residual, no moment/support bound, and no rotated-coordinate independence appears in this statement.

This directly resolves the **structural** part of `QFORM-NULLROW-TWOBANK-NEARSPAN-UNIFORMITY-v1`: the `tau ->0` limit cannot lose all rank-three curvature. What remains is one already-recognized analytic currency, namely a dimension-free payment for a diffuse aggregate principal-triple bank under the original product law.

The mechanism is materially different from B10 r18. r18 paid nonzero leakage through the third singular value of one cross block and therefore cost `(tau_J tau_K)^(-1/6)`. The present exterior-volume compiler keeps all four Cauchy--Binet strata and has **no inverse power of tau**.

## 7. Relation to the double-high branch

Theorem 6.1 does not by itself close B10 r18's separate `double-high` range-leverage branch when one residual norm is not small. The r18 geometric-mean three-cross gate and Witt row gate remain the correct paid exits there. The current result is specifically the first missing small-positive-residual implication requested by the near-span state.

It also does not solve arbitrary additional spectrum beyond exact rank three. The identity (4.5), and therefore the clean conversion of exterior volume into principal determinant mass, uses exact rank three.

## 8. Verification

A deterministic numerical checker samples random positive-definite `S_J` with `S_K=I-S_J`, random slope gaps, and random orthogonal residual vectors. It constructs the full Parseval frame satisfying (1.1), directly sums every squared `3x3` row determinant in the four strata, and checks (2.2)--(3.6). Over the recorded batch, the maximum absolute algebraic discrepancy was below `7e-16`. The checker is regression evidence only; the proof is the exact algebra above.

## 9. Status and next implication

**Proved in this run:**

- `QFORM-TWOBANK-SLOPEGAP-ENERGY-v1`;
- `QFORM-TWOBANK-MIXED-EXTERIOR-STRATA-v1`;
- `QFORM-NEARSPAN-TO-O3-AGGREGATE-v1`;
- compatible account04/B16 applied to the actual near-unit determinant-bank inequality (5.4).

**Not proved:**

- a universal `L^infinity` payment for an arbitrarily diffuse aggregate principal-triple bank;
- the separate double-high bank-range-leverage chamber outside the small-residual region;
- arbitrary extra spectrum;
- the full QFORM conjecture.

The exact next implication for this line is therefore

`QFORM-NEARSPAN-O3-AGGREGATE-PAYMENT-v1`:

> Starting from one of the three structured product-coordinate banks in Theorem 6.1 with total absolute principal-triple determinant mass at least `1/256`, prove a dimension-free output density bound **before** selecting reciprocal local minors, or give a target-valid counterexample.

The full QFORM conjecture remains **OPEN / NOT PROVED**. Essential boundedness is obtained only in the local-atom exits (4.7),(5.5) and previously paid branches. This run does not newly prove continuity; continuity remains only where a cited branch already establishes it.
