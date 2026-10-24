SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-24T08:00:24Z.
attacking: the account03/B20 r49 balanced four-cell rank-two survivor by converting any genuinely transverse same-bank curvature into a literal physical cross-E3 payment, and otherwise forcing a simultaneous two-sided rank-two alignment collar.

# account02/B20 r49 — four-cell E3-or-two-sided-alignment closure

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **ESSENTIAL STEP APPLIED / NEW FULL-AMBIENT BRANCH PAYMENT / TWO-SIDED CURVATURE COLLAR SHARPENED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval and publication are not native learned-memory receiver ingestion.

Regularity: the payment branch below uses the completed marginal-free physical cross-E3 theorem and therefore gives a continuous `C_0` density in that branch. The surviving alignment branch is structural only. Unrestricted target continuity remains separate and open.

All banks below are literal ORIGINAL-coordinate sets. No random variable is rotated. Orthogonal column changes appear only inside a deterministic exterior-volume identity. No Gaussian, log-concavity, moment, compact-support, connected-support, iid, post-rotation independence, arbitrary-joint coarea, worst-fibre cap, conditional-cap, or law-uniform pointwise quadratic-phase decay assumption is introduced. Every nonzero coefficient tail and every same-bank quadratic term stays in the ambient law.

## 1. Fresh source-pinned frontier

The newest compatible completed designated partner is account03/B20 r49:

`yspennstate/math-open-problems@4bf5217dace0129fcb6995727e1d8afa671c2435`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260924T065238Z-account03-B20-QFORM-auto11-r49/REPORT.md`.

Its exact balanced-grid expression is

`h = 1/2 - 1/(4 sqrt(2))`,

`boxed: s_grid = h/126 - 2^-16`
`              = 0.002550005533980064... .`                     (1.1)

It supplies four disjoint original-coordinate banks

`R_1, R_2, C_1, C_2`                                             (1.2)

such that for every `a,b in {1,2}` the actual physical cell

`M_ab := A[R_a,C_b]`                                             (1.3)

satisfies

`boxed: sigma_2(M_ab) > s_grid.`                                 (1.4)

The same source keeps the genuine `2^-16` rank-two-approximation tail and proves the normalized light-plane leverage gate `<=1/16`; neither is erased here.

The current account02/B20 predecessor additionally paid the branches with transverse third energy on both row banks and the one-sided-curvature endpoint. Its remaining debt was robust physical rank-two crossing with genuine quadratic curvature on both original-coordinate sides.

Two completed receivers are used below at their exact scopes.

### 1.1 Marginal-free physical cross-E3 receiver

Canonical source:

`yspennstate/math-open-problems@d0bda9f4e884eff19e5e7b0cf4cacab34d416c28`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`, theorem `QFORM-CROSS-E3-MARGINALFREE-L1-v1`.

For any literal disjoint physical cross block `K=A[U,V]`,

`V_3(K):=e_3(KK^T)>0`                                           (1.5)

implies for the complete ambient quadratic law

`boxed: ||p_Q||_infinity <= C_E3 V_3(K)^(-1/6),`                 (1.6)

where

`C_E3=3*2^(4/3)*exp(1/3)=10.550168831164775... .`                (1.7)

It retains arbitrary same-bank curvature, outside couplings, affine terms, extra spectrum and signs, and has no volume-marginal gate.

### 1.2 Required pinned D5 receiver

From the required pinned package

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Theorem `D_5` gives, for every literal disjoint physical cross block `K`,

`boxed: ||p_Q||_infinity <= 5 sqrt(2e) e_5(K^T K)^(-1/10)`       (1.8)

with no marginal condition. In particular

`e_5(K^T K)>=1/1024`

implies

`boxed: ||p_Q||_infinity <=10 sqrt(2e)`
`                           =23.316439815971...<23.317.`           (1.9)

This is applied below to the actual augmented cuts, not cited only as background.

## 2. Exterior-volume extension lemma

### Lemma 2.1 — `R2+TRANSVERSE-COLUMN => E3`

Let `M` be any real matrix with `sigma_2(M)>=s>0`, let `P` be the orthogonal projection onto the top-two left singular subspace of `M`, and let `D` be any matrix with the same row index set as `M`. Put

`K=[M D]`.                                                       (2.1)

Then

`boxed: e_3(KK^T) >= sigma_1(M)^2 sigma_2(M)^2 ||(I-P)D||_F^2`
`                    >= s^4 ||(I-P)D||_F^2.`                     (2.2)

#### Proof

Take an SVD of `M`. Right-multiply the `M` columns by its right singular orthogonal matrix and leave the `D` columns fixed. This deterministic column rotation does not change `KK^T` and does not act on any random variable. In the rotated coefficient matrix the first two `M` columns are

`sigma_1 u_1`, `sigma_2 u_2`.                                    (2.3)

By Cauchy-Binet, `e_3(KK^T)` is the sum of squared Euclidean three-volumes of all triples of columns of `K`. Restrict this nonnegative sum to the triples consisting of the two columns in (2.3) and one physical column `d_j` of `D`. Their squared three-volumes are

`sigma_1^2 sigma_2^2 ||(I-P)d_j||_2^2`.                          (2.4)

Summing in `j` gives the first inequality in (2.2), and `sigma_1>=sigma_2>=s` gives the second. QED.

The useful point is that no individual physical 3x3 minor is selected. A complete rank-two packet is extended by the **aggregate transverse Frobenius energy**.

## 3. Main four-cell theorem

Write the two same-side cross-half curvature blocks as

`D_R := A[R_1,R_2]`,
`D_C := A[C_1,C_2]`.                                             (3.1)

For each cell `M_ab`, let

`P_ab` be its top-two left singular projection on `R_a`,
`Q_ab` be its top-two right singular projection on `C_b`.         (3.2)

Fix any `delta>0`.

### Theorem 3.1 — `QFORM-R49-FOURCELL-E3-OR-TWOSIDED-ALIGNMENT-COLLAR-v1`

Under (1.2)-(1.4), at least one of the following two alternatives holds.

### A. Full-law E3 payment

For some `a,b`, one of the two literal augmented original-coordinate cross blocks

`K^R_ab := A[R_a, C_b union R_(3-a)]`,

`K^C_ab := A[C_b, R_a union C_(3-b)]`                            (3.3)

has

`boxed: e_3(K K^T) >= s_grid^4 delta^2.`                         (3.4)

Consequently the complete ambient law satisfies

`boxed: ||p_Q||_infinity`
` <= C_E3 s_grid^(-2/3) delta^(-1/3).`                           (3.5)

### B. Simultaneous two-sided curvature alignment

For every `a,b`,

`||(I-P_ab) A[R_a,R_(3-a)]||_F < delta`,                         (3.6)

`||(I-Q_ab) A[C_b,C_(3-b)]||_F < delta`.                         (3.7)

In particular, for every `b,b' in {1,2}`,

`boxed: ||D_R - P_1b D_R P_2b'||_F < 2 delta,`                   (3.8)

and for every `a,a' in {1,2}`,

`boxed: ||D_C - Q_a1 D_C Q_a'2||_F < 2 delta.`                   (3.9)

Hence both same-side cross-half curvature blocks are simultaneously within `2 delta` of rank at most two maps whose input and output planes are the **actual singular planes of the four paid rank-two cells**. In addition,

`dist_F(D_R, rank<=2)<delta`,
`dist_F(D_C, rank<=2)<delta`,                                    (3.10)

and the cell planes obey the activity-weighted coherence identities

`||(P_11-P_12)D_R||_F<2 delta`,
`||D_R(P_21-P_22)||_F<2 delta`,                                  (3.11)

`||(Q_11-Q_21)D_C||_F<2 delta`,
`||D_C(Q_12-Q_22)||_F<2 delta`.                                  (3.12)

#### Proof

For the `R` side fix `a,b` and set

`D_a=A[R_a,R_(3-a)]`.                                            (3.13)

The columns `C_b` and `R_(3-a)` are disjoint from the row bank `R_a`, so `K^R_ab=[M_ab,D_a]` is a literal physical cross block. Lemma 2.1 and (1.4) give

`e_3(K^R_ab (K^R_ab)^T)`
` >=s_grid^4 ||(I-P_ab)D_a||_F^2.                               (3.14)

Thus if the norm in (3.6) is at least `delta`, branch A holds. The transpose argument, applied to `M_ab^T` and `A[C_b,C_(3-b)]`, gives exactly the same conclusion from a failure of (3.7).

Assume no E3 payment occurs. Then all inequalities (3.6)-(3.7) hold. For `D_R=A[R_1,R_2]`, (3.6) with `a=1` gives

`||(I-P_1b)D_R||_F<delta`.                                       (3.15)

With `a=2`, symmetry of `A` gives

`||(I-P_2b')D_R^T||_F<delta`,

or equivalently

`||D_R(I-P_2b')||_F<delta`.                                      (3.16)

Therefore

`D_R-P_1b D_R P_2b'`
` =(I-P_1b)D_R + P_1b D_R(I-P_2b')`,                             (3.17)

so (3.8) follows by the triangle inequality. Taking only the first term in (3.15), `P_1bD_R` is rank at most two and proves the first half of (3.10). The identities in (3.11) follow by subtracting the two bounds with `b=1,2`; e.g.

`(P_11-P_12)D_R`
` =(I-P_12)D_R-(I-P_11)D_R`.                                    (3.18)

The `C` side is identical, giving (3.9), the second half of (3.10), and (3.12). Finally branch A is paid by (1.6), giving (3.5). QED.

## 4. Concrete r49 constants

Take the actual retained-tail scale

`delta=tau=2^-16=0.0000152587890625`.                            (4.1)

Using the exact partner expression (1.1), branch A yields

`V_3 >= s_grid^4 2^-32`                                         (4.2)

and hence

`boxed: ||p_Q||_infinity <22789.002 <22790.`                     (4.3)

Therefore every still-unpaid r49 four-cell state satisfies simultaneously

`boxed: ||D_R-P_1b D_R P_2b'||_F <2^-15`                         (4.4)

for all `b,b'`, and

`boxed: ||D_C-Q_a1 D_C Q_a'2||_F <2^-15`                         (4.5)

for all `a,a'`, as well as

`dist_F(D_R,rank<=2)<2^-16`,
`dist_F(D_C,rank<=2)<2^-16`.                                    (4.6)

This replaces the previous vague phrase “genuine two-sided curvature” by an explicit source-valid collar: **all cross-half curvature on both sides is itself almost rank two and locked to every relevant cell singular plane.** The remaining unrestricted curvature can only hide inside the four literal principal node blocks

`A[R_1,R_1], A[R_2,R_2], A[C_1,C_1], A[C_2,C_2]`                (4.7)

plus the retained aligned rank-two bridges.

## 5. Robust-second-mode refinement

The alignment alternative itself has a useful dichotomy. Let `D` denote either `D_R` or `D_C`, and let `P,P'` be the two output cell planes on the corresponding side. Assume (3.6) or (3.7), respectively.

For any `kappa>0`:

* if `sigma_2(D)<kappa`, then from `dist_F(D,rank<=2)<delta`,

  `boxed: dist_F(D,rank<=1)<sqrt(kappa^2+delta^2);`               (5.1)

* if `sigma_2(D)>=kappa` and `U_D` is a top-two left singular frame of `D`, then

  `boxed: ||(I-P)U_D||_op <= delta/kappa,`                        (5.2)

  and the same for `P'`, hence

  `boxed: ||P-P'||_op <=2 delta/kappa.`                           (5.3)

Indeed `(I-P)D V_2=(I-P)U_D Sigma_2`, whose Frobenius norm is at most `delta`; dividing by the least singular value `kappa` gives (5.2). Equation (5.1) is the identity

`dist_F(D,rank<=1)^2=sigma_2(D)^2+sum_(j>=3) sigma_j(D)^2`

combined with the rank-two tail bound in (3.10).

At the natural choice `kappa=s_grid`, an unpaid side is therefore either

`dist_F(D,rank<=1)<0.002550052`,                                 (5.4)

or its two cell planes differ in operator norm by less than

`2 delta/s_grid=0.011967652`.                                   (5.5)

So robust same-side two-dimensional curvature forces quantitative latent-plane coherence; otherwise that curvature itself collapses to an explicit near-rank-one tube.

## 6. Required pinned D5 applied to the same live cuts

For each of the eight actual augmented blocks in (3.3), the pinned no-marginal D5 theorem (1.8) applies directly. Thus if for any such `K`

`e_5(K^T K)>=1/1024`,                                            (6.1)

then the entire ambient quadratic law is already paid by

`boxed: ||p_Q||_infinity<23.317.`                                (6.2)

Consequently every state surviving Sections 3-5 may, in addition, assume

`boxed: e_5((K^R_ab)^T K^R_ab)<1/1024,`
`       e_5((K^C_ab)^T K^C_ab)<1/1024`                           (6.3)

for all `a,b`. This is an equation-level use of the required `e5f71d79...` source on the newly constructed physical cuts.

## 7. Exact obstruction: E3 cannot be forced after alignment

The surviving alignment branch is real, not a weakness of the inequality. Let `m>=32` and choose four disjoint physical banks of size `m`. On them choose orthonormal two-frames

`U_1,U_2,V_1,V_2`                                                (7.1)

with flat physical leverage `2/m<=1/16`. For constants `s,t>0`, define a symmetric coefficient matrix by

`A[R_a,C_b]=s U_a V_b^T` for all `a,b`,                          (7.2)

`A[R_1,R_2]=t U_1 U_2^T`,
`A[C_1,C_2]=t V_1 V_2^T`,                                       (7.3)

with transpose blocks imposed by symmetry and all four principal node blocks zero.

Every cell has exactly two nonzero singular values, both equal to `s`, while every augmented block in (3.3) has row space contained in the corresponding two-frame. Hence

`boxed: e_3(KK^T)=0`                                             (7.4)

for all eight augmented cuts, even though both same-side bridges can have arbitrarily large rank-two strength `t`.

On the eight-dimensional latent carrier the coefficient matrix is two identical copies of

`H(s,t)=`
`[[0,t,s,s],`
` [t,0,s,s],`
` [s,s,0,t],`
` [s,s,t,0]],                                                    (7.5)

whose eigenvalues are

`t+2s, t-2s, -t, -t`.                                            (7.6)

For the target-valid choice `s=t=1`, the full nonzero spectrum is

`{3,3,-1,-1,-1,-1,-1,-1}`.                                     (7.7)

Thus the three-large-eigenvalue hypothesis, the `1/16` diffuse planes, four robust rank-two cells, and even robust two-sided same-bank curvature do **not** force any transverse E3 currency. This refutes that stronger structural shortcut, not the QFORM conjecture. It shows that after (4.4)-(4.6) the correct next mechanism is the aligned latent-network/self-curvature endpoint, not another attempt to manufacture a third crossing direction.

## 8. First unpaid implication after this run

The sharpened first unpaid implication is

`QFORM-R49-ALIGNED-FOURNODE-R2-PLUS-SELF-CURVATURE-ENDPOINT-v1`:

> Under the full independent cap-one product hypotheses and `s_3(A)>=1`, retain the account03/B20 r49 four literal cells with `sigma_2>s_grid`, the genuine `2^-16` coefficient tail and `1/16` diffuse-plane provenance. Assume all eight augmented D5 currencies in (6.3) fail and the E3 payment in Section 3 fails. Then both same-side cross-half blocks satisfy the simultaneous rank-two collars (4.4)-(4.6), with the robust-second-mode alternatives (5.4)-(5.5). Pay the remaining form, whose only unrestricted quadratic curvature is in the four principal node blocks plus these plane-aligned bridges, or route one node/self-curvature component source-preservingly into an already completed physical pair, hub, ridge/window, Fresnel, E3 or E5 receiver.

The theorem has therefore removed **transverse two-sided curvature** from the live debt. The genuinely new endpoint is a four-node product system with plane-aligned rank-two bridges and arbitrary internal node curvature.

Full unrestricted QFORM status: **OPEN / NOT PROVED / NOT DISPROVED**.

Full unrestricted continuity status: **OPEN separately**.
