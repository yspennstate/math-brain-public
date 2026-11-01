SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T11:43:27Z.
attacking: QFORM-TRIANGLE-PAIR-TRANSFER-RECONDITIONING-v1 — move the guaranteed TRIANGLE physical pair into the source bank, preserve the rank-two cross determinant quantitatively, and use the completed uniform near-null receiver before any generic interpolation.

# fleet03/B19 r33 — TRIANGLE pair transfer, source reconditioning, and a <65 density exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / quantitative inequalities and rigorous computations  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/writes are not native learned-memory ingestion  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW TARGET-LEVEL PAID SUBBRANCH + SHARPER RESIDUE / FULL QFORM OPEN`.

The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open. The theorem below advances the exact-rank-three rank-two-cross TRIANGLE chamber only. It uses original-coordinate repartitioning and arbitrary cap-one product laws; no Gaussianity, moments, compact support, log-concavity, post-rotation independence, arbitrary-joint coarea, fiber supremum, or law-uniform pointwise quadratic-phase decay is used.

## 1. Source-pinned incoming state

The live TRIANGLE packet is the completed fleet03/B19 result at

`yspennstate/math-open-problems@63e569420a83b6a9f073c2158e3b5f46214535d7`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T093525Z-fleet03-B19-QFORM-r28/REPORT.md`.

Its exact-rank-three setup is

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`,                  (1.1)

with an ORIGINAL-coordinate split `I union J`, source and receiver Grams

`G=R_I^T R_I`, `H=R_J^T R_J=I-G`,                                (1.2)

`rank(G)=3`, `rank(H)=2`, and cross block

`C=A[I,J]`, `rho=s_1(C)s_2(C)>=rho_0:=sqrt(29/3072)`.             (1.3)

Put `W=range(H)`. For receiver rows `s_j` define the normalized Parseval frame

`v_j=(H|_W)^(-1/2)s_j`, `sum_(j in J) v_jv_j^T=I_W`.              (1.4)

The TRIANGLE compiler furnishes an actual physical pair `T={j,k}` with

`d_T:=det(v_j,v_k)^2>d_0:=377/1344`.                              (1.5)

Equivalently its pair-to-source cross singular product is

`Delta_T=rho sqrt(d_T)>0.0514587738859587`.                       (1.6)

The completed uniform receiver used below is fleet01/B19
`QFORM-RANK2-CROSS-TRANSVERSE-UNIFORM-NEARNULL-v1`, canonical

`yspennstate/math-open-problems@d72be34399b8d0325c715973e7af3a37df7ce227`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260923T060843Z-fleet01-B19-QFORM-auto11/REPORT.md`.

For an exact-rank-two physical cross block with singular product `rho'`, a three-dimensional source self range, and transverse source action scale

`R'=(lambda^2+delta^2)^(1/2)=||B'r||`,                            (1.7)

it gives a continuous density with

`||p_Q||_infinity <= C_* (R')^(-1/4) (rho')^(-3/8)`,              (1.8)

where

`C_*=2^(15/4)3^(-3/8)=8.9113194670...`.                           (1.9)

This theorem is uniform through the exact/punctured near-null transition and does not delete a small coefficient.

## 2. Transfer the physical TRIANGLE pair to the source

Let `S_T` be the `2 x 3` matrix of the two spectral rows `s_j,s_k`. Define the normalized pair covariance on `W`

`K:=v_jv_j^T+v_kv_k^T`.                                          (2.1)

Because `(v_l)` is Parseval,

`0<=K<=I_W`.                                                      (2.2)

Moreover

`det K=det(v_j,v_k)^2=d_T=:d`.                                   (2.3)

Let the eigenvalues of `K` be `k_1>=k_2>=0`. Since `k_1<=1`,

`k_2=d/k_1>=d`; hence

`boxed: K>=d I_W.`                                                (2.4)

Now literally move the two ORIGINAL coordinates in `T` from receiver to source:

`I'=I union T`, `J'=J\T`.                                        (2.5)

The new Grams are

`G'=G+S_T^T S_T`, `H'=H-S_T^T S_T=I-G'`.                         (2.6)

On `W`, using `S_T^T S_T=H^(1/2) K H^(1/2)`,

`G'|_W=I_W-H|_W+H^(1/2) K H^(1/2)`
`      >=I_W-(1-d)H|_W`
`      >=d I_W`.                                                  (2.7)

On `ker H`, `G'` is the identity. Therefore

`boxed: G'>=d I_3.`                                               (2.8)

This is the key source reconditioning: the actual physical TRIANGLE pair repairs the nearly singular source direction without rotating the product law.

## 3. Exact preservation of the rank-two cross determinant

Let

`r_T:=det(I_W-K)`.                                                (3.1)

If `r_T>0`, then `H'` still has rank two and range `W`. The exact rank-two cross determinant identity gives

`rho^2=det(H|_W) det((MGM)|_W)`,                                  (3.2)

and, for the repartitioned cross block `C'=A[I',J']`,

`(rho')^2=det(H'|_W) det((MG'M)|_W)`,
`rho'=s_1(C')s_2(C')`.                                           (3.3)

Because

`H'|_W=H^(1/2)(I_W-K)H^(1/2)`,                                   (3.4)

we have

`det(H'|_W)=det(H|_W) r_T`.                                      (3.5)

Also `G'>=G`, so

`MG'M-MGM=M(G'-G)M=(S_T M)^T(S_T M)>=0`.                         (3.6)

Compression to `W` preserves positive-semidefinite order, and determinant is monotone on positive-definite `2 x 2` matrices. Hence

`det((MG'M)|_W)>=det((MGM)|_W)`.                                 (3.7)

Combining (3.2)--(3.7),

`boxed: rho' >= rho sqrt(r_T).`                                  (3.8)

No inverse of a local physical minor appears. The old aggregate cross determinant is lost only by the **normalized determinant mass actually removed from the receiver**.

There is also an exact combinatorial interpretation. Since the remaining normalized frame covariance is `I_W-K`, Cauchy--Binet gives

`boxed:
 r_T=det(I_W-K)
    =sum_{U subset J\T, |U|=2} det(v_U)^2.}`                     (3.9)

Thus `r_T` is precisely the total normalized two-basis determinant mass left entirely outside the promoted physical pair.

## 4. Source self curvature after transfer

Let

`B'=A[I',I']=R_{I'} M R_{I'}^T`.                                 (4.1)

On its three-dimensional range it is orthogonally represented by

`(G')^(1/2) M (G')^(1/2)`.                                      (4.2)

Therefore, by (2.8) and `s_min(M)>=1`,

`s_min^+(B')>=lambda_min(G') s_min(M)>=d`.                       (4.3)

For the unit transverse source direction `r` in the uniform receiver (1.7),

`R'=||B'r||>=d`.                                                 (4.4)

This point is stronger than merely producing a nonzero transverse coefficient: all signatures, repeated eigenvalues, and zero/nonzero scalar transverse pivots are covered because the receiver spends the full norm `sqrt(lambda^2+delta^2)`.

## 5. New paid TRIANGLE branch

### Theorem 5.1 — `QFORM-TRIANGLE-PAIR-TRANSFER-RECONDITIONING-v1`

Under (1.1)--(1.5), if

`r_T=det(I_W-K)>=1/64`,                                          (5.1)

then the full quadratic form has a continuous density and

`boxed: ||p_Q||_infinity <65.`                                  (5.2)

#### Proof

Apply the completed uniform near-null receiver (1.8) to the literal ORIGINAL-coordinate repartition `(I',J')`. Equations (3.8) and (4.4) give

`||p_Q||_infinity
 <= C_* d^(-1/4) [rho sqrt(r_T)]^(-3/8)
 = C_* d^(-1/4) rho^(-3/8) r_T^(-3/16).`                        (5.3)

Use

`d>d_0=377/1344`,
`rho>=rho_0=sqrt(29/3072)`,
`r_T>=1/64`.                                                     (5.4)

Then

`C_* d_0^(-1/4) rho_0^(-3/8) 64^(3/16)
 =64.0187353229...<65`.                                         (5.5)

The receiver proves an integrable characteristic function in this scope, so the density is continuous and vanishes at infinity. QED.

This closes the coupled-third-source `L^infinity` problem for every TRIANGLE whose promoted pair leaves at least `1/64` of normalized two-basis determinant mass in the receiver. It does not use the invalid generic `L^3 + 2/3` interpolation route.

## 6. The surviving TRIANGLE geometry is now a two-coordinate near-coloop

If Theorem 5.1 does not apply, then

`r_T=det(I_W-K)<1/64`.                                           (6.1)

Since the eigenvalues of `K` lie in `[0,1]`,

`(1-k_1)(1-k_2)<1/64`.                                          (6.2)

Therefore at least one factor is below `1/8`, so

`boxed: k_1>7/8.`                                                (6.3)

At the same time (2.4) and (1.5) give

`boxed: k_2>=d>d_0=377/1344>0.2805.`                             (6.4)

Thus the unpaid TRIANGLE endpoint is no longer an arbitrary three-row concentration or generic high-star state. An **actual pair of original physical coordinates** carries more than `7/8` of one normalized receiver direction and at least `d_0` in the orthogonal direction, while the complete normalized two-basis determinant mass of every receiver pair disjoint from it is below `1/64` by (3.9).

Call the new residue

`QFORM-TRIANGLE-PHYSICAL-PAIR-NEARCOLOOP-v1`:

> In the exact-rank-three rank-two-cross TRIANGLE chamber, after promoting the actual pair `T` with `det K>d_0`, pay the remaining state `det(I-K)<1/64` using its two-coordinate near-coloop structure, or route it to the existing grouped/rank-one/ridge/null-coloop payments without deleting the nonzero remainder.

The exact endpoint `det(I-K)=0` leaves a rank-at-most-one receiver after promotion; the punctured interval `0<det(I-K)<1/64` must not be inferred from that endpoint by coefficient continuity.

## 7. Designated partner fleet04/B19 applied at an actual inequality

The completed designated-partner theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` is source-pinned at

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`.

In its residual-diffuse **exact-null-coloop** scope it proves

`||p_Q||_infinity <34 sqrt(log(e/D_res))`, `0<D_res<=1`.         (7.1)

Hence on the concrete interval

`e^(-8)<=D_res<=1`,                                              (7.2)

`log(e/D_res)<=9`, and therefore

`boxed: ||p_Q||_infinity<102.`                                  (7.3)

The source separately pays `D_res=0` by `<5.844` and `D_res>=1` by `<11.748`. This is retained as an actual paid endpoint in the proof graph. I do **not** infer that (7.1) automatically extends to the new punctured pair-near-coloop state (6.1).

The partner's later obstruction `QFORM-L3-PLUS-HALF-HOLDER-NOT-LINFINITY-v1` is also respected: Theorem 5.1 reaches `L^infinity` by preserving and repartitioning the common quadratic-form geometry before Fourier inversion, not by generic interpolation of the prior TRIANGLE `2/3` small-ball estimate.

## 8. Compact conditional proof assembly after this run

Within the current exact-rank-three rank-two-cross route, the prior balanced-frame and disjoint-basis branches are paid. TRIANGLE supplies an actual pair with `d>d_0` and `rho>=rho_0`. The present theorem literally transfers that pair into the source, forces the new source Gram to satisfy `G'>=dI`, and preserves the cross singular product by the exact factor `sqrt(det(I-K))`. Therefore every TRIANGLE state with `det(I-K)>=1/64` is paid continuously by `<65`.

The first local TRIANGLE debt is now the sharply quantified physical-pair near-coloop state (6.1)--(6.4). The parallel deep-STAR/two-channel leaf-curvature debt from fleet02/B19 remains separate. Globally, strict `N3(tau)` and arbitrary-extra-spectrum descent remain unresolved; no exact-rank-three result here is promoted silently to general rank.

## 9. Signs, degeneracies, and regularity audit

`M` may have any signature; only `s_min(M)>=1` is used. Repeated eigenvalues are harmless. No quantity is divided by when `r_T=0`; that endpoint is left in the explicit residue. The selected physical pair has `d>d_0`, so its normalized covariance is genuinely positive definite. All repartitions move literal original coordinates and therefore preserve the product law between banks. The paid branch proves a continuous `C_0` density. Full-target continuity remains OPEN.

## 10. Arithmetic regression

`d_0=377/1344=0.2805059523809524`,

`rho_0=sqrt(29/3072)=0.09716019846967515`,

`C_*=2^(15/4)3^(-3/8)=8.911319467025024`,

and the bound in (5.5) is

`64.01873532293244<65`.

The deterministic check file for this run records these values and the exact algebraic implications `K<=I, det K=d => K>=dI` and `det(I-K)<1/64 => lambda_max(K)>7/8`.

No scheduler/task-count, enabled/paused state, notification, email, permission, paid API/model, public release, Drive, installation, cross-account authentication, or remote-workflow action was taken.
