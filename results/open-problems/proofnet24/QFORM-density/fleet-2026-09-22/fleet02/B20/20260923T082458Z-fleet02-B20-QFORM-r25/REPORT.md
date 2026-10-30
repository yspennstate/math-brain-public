SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B20, 2026-09-23T08:24:58Z.
attacking: the designated-partner normalized-heavy finite-core survivor by a second exact whitening step and a source-coordinate finite-core compiler.

# fleet02/B20 r25 — finite-core whitening compiler and double-coloop reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Proof closure and keeper / SYNTHESIS / complementary constructions and source-valid counterexamples  
**Execution:** `WITHOUT_VERIFIED_BRAIN`: authenticated repository retrieval occurred, but no actual learned-memory receiver ingestion was exposed.  
**Status:** `ESSENTIAL_STEP_APPLIED / HC REDUCED TO FINITE DOUBLE-COLOOP / FULL QFORM OPEN`.

The unrestricted conjecture remains OPEN. No Gaussianity, log-concavity, moment, compact-support, connected-support, diagonal-basis, post-rotation-independence, arbitrary-joint coarea, worst-fiber, or perturbative-deletion hypothesis is introduced. Continuity is kept separate from essential boundedness.

## 1. Fresh source state and designated partner

The newest compatible completed designated partner found in this run is fleet03/B20 r29:

`yspennstate/math-open-problems@b1f862a5685a726b0eb2e3c348b22ee9eaf7a782`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T074211Z-fleet03-B20-QFORM-r29/REPORT.md`.

It works inside the current exact-rank-three/rank-two-cross chamber

`A = R M R^T`, `R^T R = I_3`,                                  (1.1)

with `M=M^T` invertible and `s_min(M)>=1`, and with an original-coordinate partition inherited from the rank-two-cross route. The preceding fleet02/B19 repartition theorem leaves the normalized-heavy branch with an original-coordinate set

`K0={j: ell_j>1/16}`, `|K0|<=31`.                               (1.2)

Write rows of `R` as `r_i`, and

`T0=sum_{j in K0} r_j r_j^T`,
`S0=I-T0`,
`delta0=lambda_min(S0)`.                                       (1.3)

The partner proves the following exhaustive alternatives.

(A) `delta0<1/64`, so some spectral unit direction has more than `63/64` of its squared physical mass on `K0`.

(B) `delta0>=1/64` and every residual row has `S0`-whitened leverage at most `1/32`; then the full law is paid by

`||p_Q||_infinity < 27/delta0 <=1728`.                          (1.4)

(C) `delta0>=1/64`, but the threshold fails. Then

`K1={i notin K0: r_i^T S0^{-1}r_i>1/32}`,                      (1.5)

obeys `1<=|K1|<=95`, so `|K0 union K1|<=126`, while every row outside `K0 union K1` obeys the `1/32` threshold relative to the exact retained Gram `S0`.

The required pinned interactive source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Two proved results from it are used below at equation level:

**Theorem F.** For an exact rank-three physical quadratic block whose normalized spectral-frame leverage is at most `1/2`, arbitrary linear terms allowed,

`||p||_infinity <= 12 |lambda_1 lambda_2 lambda_3|^{-1/3}`.     (1.6)

**Theorem B.** If a physical `m`-coordinate quadratic matrix has three eigenvalues of modulus at least one, then for zero linear term

`||p||_infinity <= 2 sqrt(2 pi) sum_{i=1}^m ||Pi e_i||`,        (1.7)

where `Pi` is projection onto the three-dimensional spectral range. For a rank-three matrix the sum is at most `sqrt(3m)`.

The source also confirms that no counterexample is known and that the unrestricted conjecture remains open; its shell example refutes replacing product structure by an arbitrary bounded three-dimensional joint density.

## 2. A source-coordinate finite-core compiler

### Theorem 2.1 — `QFORM-FINITE-PHYSICAL-CORE-RANK3-PAYMENT-v1`

Assume (1.1), with independent original coordinates having densities at most one. Let `K` be a set of `m` ORIGINAL coordinates, put `P=R_K`, and suppose

`T=P^T P >= kappa I_3`, `kappa>0`.                              (2.1)

Then the full ambient quadratic law has a density satisfying

`boxed: ||p_Q||_infinity <= 2 sqrt(6 pi m) / kappa.`            (2.2)

No condition is imposed on the values of the coordinates outside `K`.

### Proof

Condition on all original coordinates in `O=K^c`. The conditional quadratic polynomial in `x_K` is

`x_K^T B x_K + 2 d^T x_K + c`,
`B=P M P^T`,
`d=P M R_O^T x_O`.                                              (2.3)

Because `T>=kappa I`, `P` has column rank three. Let

`Q0=P T^{-1/2}`; then `Q0^T Q0=I_3`, and

`B=Q0 L Q0^T`, `L=T^{1/2} M T^{1/2}`.                          (2.4)

Hence the three nonzero eigenvalues of `B` have modulus at least

`s_min(L)>=lambda_min(T)s_min(M)>=kappa`.                       (2.5)

Also `range(B)=range(P)`, while `d` in (2.3) lies in `range(P)`. Therefore there is a deterministic vector `h=h(x_O)` with `Bh=d`. Completing the square gives

`x_K^T Bx_K+2d^Tx_K=(x_K+h)^T B(x_K+h)-h^TBh`.                 (2.6)

The translated variables `X_i+h_i`, `i in K`, are still independent and each has a density bounded by one. Apply the pinned Theorem B to `B/kappa`. If `Pi_B` is the orthogonal projection onto `range(B)`,

`||p_{(X_K+h)^T B(X_K+h)}||_infinity
 <= (2 sqrt(2pi)/kappa) sum_{i in K} ||Pi_B e_i||`.             (2.7)

Since `rank Pi_B=3`, Cauchy-Schwarz gives

`sum_{i in K}||Pi_B e_i||
 <= sqrt(m sum_i ||Pi_B e_i||^2)
 =sqrt(3m)`.                                                     (2.8)

This proves (2.2), uniformly in the conditioned outside values. Averaging the conditional laws preserves the same essential-supremum bound. QED.

Two values needed below are

`m<=31, kappa=1/64  => ||p_Q||_infinity <=128 sqrt(186 pi)<3095`, (2.9)

`m<=126, kappa=1/64 => ||p_Q||_infinity <=128 sqrt(756 pi)<6239`. (2.10)

This theorem uses a spectral decomposition only as deterministic matrix algebra. It never promotes a rotated random coordinate to an independent source.

## 3. Second whitening of the partner's case C

Retain case (C) of Section 1. For every residual original coordinate put

`u_i=S0^{-1/2}r_i`.                                             (3.1)

Because the residual rows sum exactly to `S0`,

`sum_{i notin K0} u_i u_i^T=I_3`.                              (3.2)

Let

`O=[n] \ (K0 union K1)`,
`U1=sum_{i in K1}u_i u_i^T`,
`UO=sum_{i in O}u_i u_i^T=I-U1`.                               (3.3)

Every `i in O` satisfies

`||u_i||^2<=1/32`.                                               (3.4)

### Theorem 3.1 — `QFORM-HC-SECOND-WHITENING-v1`

In case (C), either

`boxed: ||p_Q||_infinity <=12288`,                              (3.5)

or the finite original-coordinate core

`K=K0 union K1`, `|K|<=126`,                                   (3.6)

carries more than `15/16` of the squared physical mass of some spectral unit direction.

### Proof

First suppose

`lambda_min(UO)>=1/16`.                                        (3.7)

After conditioning exactly the original coordinates in `K`, the residual physical spectral Gram is

`S=R_O^T R_O
  =S0^{1/2} UO S0^{1/2}`.                                      (3.8)

Since `S0>=I/64`,

`S>=I/1024`.                                                     (3.9)

For `i in O`, the leverage in the *new exact residual frame* is

`r_i^T S^{-1}r_i
 =u_i^T UO^{-1}u_i
 <= (1/32)/(1/16)=1/2`.                                        (3.10)

Write `Q1=R_O S^{-1/2}`; then `Q1^TQ1=I_3` and

`A_OO=Q1 L1 Q1^T`,
`L1=S^{1/2} M S^{1/2}`.                                       (3.11)

Thus

`s_min(L1)>=lambda_min(S)s_min(M)>=1/1024`.                    (3.12)

Diagonalizing the deterministic `3x3` matrix `L1` changes only the spectral frame, not the source coordinates. The physical leverages remain those in (3.10). The pinned Theorem F, which already allows arbitrary affine terms created by conditioning, yields

`||p_Q||_infinity
 <=12 |det L1|^{-1/3}
 <=12*1024
 =12288`.                                                       (3.13)

Now suppose (3.7) fails. Choose a unit `z` with

`z^T UO z<1/16`,                                                (3.14)

and set

`w=S0^{-1/2}z`, `v=w/||w||`.                                   (3.15)

Since `S0<=I`, equation `w^T S0 w=1` implies `||w||>=1`. The physical Gram of the shell `O` is the matrix `S` in (3.8), so

`v^T S v
 = z^T UO z / ||w||^2
 <1/16`.                                                        (3.16)

Because the full spectral frame is Parseval, `I=R_K^T R_K+S`. Hence

`v^T R_K^T R_K v>15/16`.                                      (3.17)

Thus the at-most-126 original coordinates in `K` carry more than `15/16` of a genuine spectral direction. QED.

This argument does not delete the shell. The shell either supplies an exact rank-three conditioned frame to Theorem F, or its failure itself certifies concentration.

## 4. The partner HC branch collapses to a finite double-coloop

### Theorem 4.1 — `QFORM-HC-FINITECORE-DOUBLECOLOOP-COMPILER-v1`

Under the complete designated-partner HC hypotheses of Section 1, one of the following holds:

1. `boxed: ||p_Q||_infinity <12288`; or
2. there is a set `K` of at most `126` ORIGINAL coordinates such that, for

`T_K=R_K^T R_K`,                                                (4.1)

`boxed: lambda_max(T_K)>15/16,  lambda_min(T_K)<1/64.`          (4.2)

Equivalently there are orthogonal spectral unit vectors `v_+,v_-` satisfying

`sum_{i in K}<r_i,v_+>^2>15/16`,                               (4.3)

`sum_{i in K}<r_i,v_->^2<1/64`,                                (4.4)

so the complement carries

`sum_{i notin K}<r_i,v_+>^2<1/16`,
`sum_{i notin K}<r_i,v_->^2>63/64`.                            (4.5)

### Proof

Use the partner's alternatives.

**Case A.** `delta0<1/64`. Since `S0=I-T0`,

`lambda_max(T0)=1-delta0>63/64`.                               (4.6)

If `lambda_min(T0)>=1/64`, Theorem 2.1 with `m<=31` gives (2.9), hence alternative 1. Otherwise `K=K0` satisfies (4.2), in fact with `lambda_max(T0)>63/64`.

**Case B.** The partner gives `<1728`, so alternative 1 holds.

**Case C.** Apply Theorem 3.1. If (3.5) holds, alternative 1 holds. Otherwise, for `K=K0 union K1`, `|K|<=126` and (3.17) gives

`lambda_max(T_K)>15/16`.                                       (4.7)

If `lambda_min(T_K)>=1/64`, Theorem 2.1 and (2.10) give `<6239`; otherwise (4.2) holds.

Finally choose orthonormal eigenvectors of the symmetric matrix `T_K` at its largest and smallest eigenvalues to obtain (4.3)-(4.5). QED.

The constant `12288` is deliberately not optimized; the structural compression is the point.

## 5. A physical-row consequence from the same pinned source

The pinned Theorem F also says that if every physical rank-three leverage obeys

`||r_i||^2<=1/2`,                                               (5.1)

then already

`||p_Q||_infinity<=12 |det M|^{-1/3}<=12`.                     (5.2)

Hence every *unpaid* double-coloop state from Theorem 4.1 has an ORIGINAL coordinate `h` with

`||r_h||^2>1/2`.                                                (5.3)

If `h in K`, then (4.4) gives

`|<r_h,v_->|^2<1/64`,
`||Proj_{v_-^perp} r_h||^2>31/64`.                             (5.4)

If `h notin K`, then (4.5) gives

`|<r_h,v_+>|^2<1/16`,
`||Proj_{v_+^perp} r_h||^2>7/16`.                              (5.5)

Thus the next receiver is not facing an abstract rotated coloop. It has a physical source coordinate with transverse spectral component at least

`sqrt(7/16)=0.6614378277...`.                                  (5.6)

This is deterministic matrix geometry only; the spectral components are not declared independent random variables.

## 6. Why a tempting stronger shortcut is false

Finite cardinality of the core alone cannot pay the branch. For example, the Parseval frame can have one original row equal to `e_1` while the complement carries the `e_2,e_3` directions. Then the one-coordinate core has

`T_K=diag(1,0,0)`.                                              (6.1)

It captures an entire spectral direction but has `lambda_min(T_K)=0`, so Theorem 2.1 cannot be invoked. This is not a counterexample to QFORM; it is a source-valid counterexample to the shortcut “finite concentrated core automatically contains a robust physical rank-three core.”

Likewise the small shell mass in (4.5) cannot be discarded as a uniformly small quadratic perturbation: an unbounded spectral coefficient in `M` can compensate an arbitrarily small frame mass. The current correction against moment-free matrix-perturbation deletion is therefore essential.

## 7. Strongest conditional proof graph after this run

The source-pinned end-to-end graph currently contains the following paid exits.

- The pinned D5 theorem pays every genuine physical cross block with fixed fifth volume, with no marginal condition.
- The exact-rank-three diffuse physical-frame branch is paid by pinned Theorem F.
- The rank-two-cross balanced transverse-source branch is paid by the existing fleet01/fleet03 receiver chain.
- The fleet02/B19 diffuse repartition branch is paid by `<776`.
- The fleet02/B19 non-double near-rankdrop branch is paid by `<61`.
- Designated partner fleet03/B20 r29 pays its conditioned-whitened HC branch by `<1728` and reduces the rest to cases A/C.
- Theorem 3.1 here pays the second-whitened case-C shell by `<12288` unless a finite core captures `>15/16` of a spectral direction.
- Theorem 2.1 pays every such finite core that also spans all three spectral directions at scale `1/64`.

Therefore the entire normalized-heavy HC debt has been reduced to the fixed finite double-coloop packet (4.2)-(4.5). The separate B19 near-rankdrop alternative was already a complementary-bank double-coloop, so the two former structural debts now have the same qualitative geometry.

## 8. First unpaid implication

The first unpaid implication in this designated exact-rank-three/rank-two-cross route is now:

### `QFORM-RANK2CROSS-DOUBLECOLOOP-PAYMENT-v1`

Under the original independent cap-one product-source hypotheses, retain the exact-rank-three representation (1.1), the inherited rank-two-cross certificate and all arbitrary self/ambient couplings allowed by the route. Assume all previously listed paid exits fail. Then there is either the B19 complementary-bank double-coloop, or an original-coordinate set `K`, `|K|<=126`, with

`lambda_max(R_K^T R_K)>15/16`,
`lambda_min(R_K^T R_K)<1/64`,                                  (8.1)

and an original coordinate `h` of leverage `>1/2` satisfying the transverse lower bound (5.4) or (5.5).

Prove a universal linear small-ball / essential-density bound for this packet, or source-preservingly reduce it to the already-paid physical-pair, grouped-square/ridge, or mixed-hub receiver.

A promising next mechanism is **heavy-row plus orthogonal bank directions before inversion**: spend the physical row `h` together with the two orthogonal coloop directions, keeping every operation in original-coordinate conditioning. A bare second Cauchy-Schwarz that reproduces only a square-root collar is insufficient, and no rotated source coordinate may be treated as independent.

This implication would close the current exact-rank-three rank-two-cross structural chamber. It would not by itself close the unrestricted theorem: the arbitrary-extra-spectrum/N3 descent and other source-pinned structural packets remain, and a full candidate still requires every target quantifier plus two independent end-to-end reviews.

## 9. Status

- `QFORM-FINITE-PHYSICAL-CORE-RANK3-PAYMENT-v1`: **PROVED**.
- `QFORM-HC-SECOND-WHITENING-v1`: **PROVED**.
- `QFORM-HC-FINITECORE-DOUBLECOLOOP-COMPILER-v1`: **PROVED**.
- HC non-double-coloop branch: **PAID**, explicit universal bound `<12288`.
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**; no new unrestricted continuity claim is made.
