SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-23T09:04:43Z.
attacking: the extreme normalized-coloop / thin-line / small-pivot-triangle residue by excising a globally light physical row through the spectral-window theorem, then collapsing every survivor to one quantitative small-pivot hub.

# account03/B19 r29 — row-excision ridge compiler and one-hub reduction

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / quantitative inequalities and rigorous computations  
**Fresh prepublication owner control:** `yspennstate/math-research-brain@4ac85fccb0633ca94a33d795a677c12598cc6b5f`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW TARGET-LEVEL STRUCTURAL REDUCTION / FULL QFORM OPEN`.

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. Global continuity also remains open. This report advances the exact-rank-three rank-two-cross branch only; arbitrary-extra-spectrum closure remains a separate global debt.

## 1. Source-pinned incoming state

The immediate B19 predecessor is account03/B19 r28,

`yspennstate/math-open-problems@4d5181180f8d5e9e14c9b1c5c5e44679c8c212b9`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T080333Z-account03-B19-QFORM-r28/REPORT.md`.

It reduces the exact-rank-three rank-two-cross near-coloop chamber to a normalized physical STAR or a three-row TRIANGLE after paying the disjoint normalized two-basis mass branch.

The newest complementary assembly input is account02/B19 r30,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260923T083941Z-account02-B19-QFORM-r30/REPORT.md`.

Its theorem `QFORM-NORMALIZED-COLOOP-ANGLE-COMPILER-v1` sharpens the r28 residue to three possibilities:

(A) an actual receiver row has normalized leverage `ell>63/64`;

(B) an actual receiver row has thick-whitened mass `<1/64`, thin-whitened mass `>23/32`, and **global spectral leverage** `c<1/32`;

(C) the r28 TRIANGLE residue: an actual row has global spectral leverage `c>21/64`, physical diagonal modulus `<1/64`, and off-diagonal physical star energy `>1343/4096`.

The analytic inputs used below were read at their complete source proofs:

1. `QFORM-SPECTRAL-WINDOW-DENSITY-v1`, canonical source
   `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
   `proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.
   If the spectral projection onto all eigenspaces `|lambda|>=1/64` has every diagonal at most `1/32`, then the quadratic form, even after arbitrary coordinate-separable measurable perturbations, has a continuous `C_0` density with
   `||p||_infinity <=288 sqrt(3e)/13<64`.

2. `QFORM-RANK3-ALL-RESIDUAL-ORIENTATIONS-v1`, canonical source
   `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`,
   `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
   In exact rank three, for physical row leverage `c_i`, nonzero physical pivot `a=A_ii`, and spectral core `M`,
   `||p_Q||_infinity <=128 [c_i |a| |det M|]^(-1/4)`.

3. account03/B19 r23 `QFORM-ARBITRARY-HUB-SQRT-SMALLBALL-v1`, canonical report
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T030233Z-account03-B19-QFORM-r23/REPORT.md`.
   For a physical hub with off-diagonal star vector `m`, arbitrary hub diagonal and arbitrary residual curvature,
   `sup_z P(|Q-z|<=eps) <=4*2^(1/4)||m||^(-1/2) eps^(1/2)`.

The designated account04/B19 input used at an actual inequality is its completed r2 theorem
`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T222052Z-account04-B19-QFORM-r2/REPORT.md`.
Its exact scope is retained below.

## 2. New row-excision theorem

Work in the exact-rank-three representation

`A=R M R^T`, `R^T R=I_3`, `M=M^T`, `s_min(M)>=1`.               (2.1)

Let the physical spectral row at an original coordinate `j` be `s in R^3`, and write

`c=||s||^2`.                                                       (2.2)

Assume

`c<1/32`.                                                         (2.3)

Delete physical row `j` from `R`, writing the remaining `(n-1) x 3` matrix as `P`. Then

`G:=P^T P=I_3-s s^T`.                                            (2.4)

Since `c<1`, `G` is positive definite, with eigenvalues `1,1,1-c`.
Define the residual physical quadratic matrix

`B=P M P^T`.                                                      (2.5)

### Theorem 2.1 — `QFORM-LIGHT-ROW-EXCISION-RIDGE-COMPILER-v1`

Under (2.1)--(2.5), exactly one of the following target-safe conclusions holds:

1. **Diffuse residual payment.** The full original `Q=X^TAX` has a continuous `C_0` density satisfying

   `boxed: ||p_Q||_infinity <64.`                                (2.6)

2. **A second global physical row is quantitatively heavy.** There is `k!=j` with

   `boxed: c_k:=||r_k||^2 >31/1024.`                             (2.7)

   In that case either

   (a) `|A_kk|>=1/64`, and the full form is paid by

   `boxed: ||p_Q||_infinity <868;`                               (2.8)

   or

   (b) `|A_kk|<1/64`, and its off-diagonal physical star obeys

   `boxed: sum_(l!=k) A_kl^2 >123/4096.`                         (2.9)

No coefficient is deleted and no projected coordinate is declared independent.

### Proof

Put

`Q_0=P G^(-1/2)`.                                                 (2.10)

Then `Q_0^T Q_0=I_3`, `P=Q_0 G^(1/2)`, and therefore

`B=Q_0 [G^(1/2) M G^(1/2)] Q_0^T`.                              (2.11)

Hence the three nonzero eigenvalues of `B` are exactly the eigenvalues of the symmetric `3 x 3` matrix in brackets. Its smallest singular value satisfies

`s_min(G^(1/2) M G^(1/2))
 >=lambda_min(G) s_min(M)
 >=1-c
 >31/32`.                                                        (2.12)

Thus **all** nonzero eigenvalues of `B` have modulus `>31/32`; in particular the spectral projection of `B` onto `|lambda|>=1/64` is precisely its rank-three range projection

`Pi=Q_0 Q_0^T=P G^(-1)P^T`.                                     (2.13)

For a remaining physical row `r_k`, its diagonal leverage in this projection is

`q_k=r_k^T G^(-1) r_k`.                                         (2.14)

If `max_(k!=j) q_k<=1/32`, condition on the ORIGINAL scalar `X_j=x`. The conditional form is

`X_{-j}^T B X_{-j}
 +2x sum_(k!=j) A_jk X_k
 +A_jj x^2`.                                                      (2.15)

The linear term is a sum of coordinate-separable measurable perturbations. The spectral-window theorem therefore applies **uniformly in x** and gives a continuous `C_0` conditional density bounded by `288sqrt(3e)/13<64`. Averaging these conditional densities against the cap-one probability density of `X_j` preserves the same `L^infinity` bound. Dominated convergence, using the uniform bound, also preserves continuity and vanishing at infinity. This proves (2.6).

Suppose instead some `q_k>1/32`. Sherman--Morrison gives the exact inverse

`G^(-1)=I_3 + s s^T/(1-c)`.                                     (2.16)

Therefore

`q_k=c_k +(s dot r_k)^2/(1-c)`.                                 (2.17)

Cauchy--Schwarz yields `(s dot r_k)^2<=c c_k`, hence

`q_k<=c_k/(1-c)`.                                                (2.18)

Consequently

`c_k>(1-c)/32>31/1024`,                                         (2.19)

which is (2.7).

If `|A_kk|>=1/64`, the completed exact-rank-three scalar-pivot theorem gives, using `|det M|>=1`,

`||p_Q||_infinity
 <=128[c_k |A_kk| |det M|]^(-1/4)
 <128[(31/1024)(1/64)]^(-1/4)
 =128(65536/31)^(1/4)
 =867.939650...<868`,                                            (2.20)

proving (2.8).

Finally assume `|A_kk|<1/64`. Since `Ae_k=R M r_k` and `R^T R=I_3`,

`||Ae_k||^2=||M r_k||^2>=||r_k||^2=c_k`.                        (2.21)

Thus

`sum_(l!=k)A_kl^2
 =||Ae_k||^2-A_kk^2
 >31/1024-1/4096
 =123/4096`,                                                     (2.22)

which proves (2.9). QED.

## 3. Collapse the entire r30 STAR / thin-line / TRIANGLE residue to one hub

### Corollary 3.1 — `QFORM-EXTREME-COLOOP-TRIANGLE-TO-SMALLPIVOT-HUB-v1`

Every survivor (A), (B), or (C) from account02/B19 r30 is either already paid by an essentially bounded density with universal constant `<868`, or there exists an ORIGINAL physical coordinate `h` satisfying

`boxed:
 |A_hh|<1/64,
 sum_(l!=h) A_hl^2 >123/4096.}`                                 (3.1)

The diffuse-excision paid branch is actually continuous with bound `<64`.

### Proof

**Case (B).** r30 already gives global leverage `c_j<1/32`. Apply Theorem 2.1 directly.

**Case (A).** Let `j` be the extreme normalized-coloop row. If its global leverage `c_j<1/32`, apply Theorem 2.1. If instead `c_j>=1/32`, split on the physical pivot. When `|A_jj|>=1/64`, the scalar-pivot theorem gives

`||p_Q||_infinity
 <=128[(1/32)(1/64)]^(-1/4)
 =128*2048^(1/4)
 =861.077929...<862`.                                            (3.2)

When `|A_jj|<1/64`, exactly as in (2.21)--(2.22),

`sum_(l!=j)A_jl^2
 >=c_j-A_jj^2
 >1/32-1/4096
 =127/4096
 >123/4096`.                                                      (3.3)

**Case (C).** r30/r28 already gives `|A_jj|<1/64` and star energy `>1343/4096`, which is stronger than (3.1).

Hence every unbounded-density obligation left by the r30 exact-rank-three compiler now has the single physical form (3.1). QED.

This is a material simplification: the normalized Pluecker STAR, the globally-light thin-line row, and the small-pivot TRIANGLE no longer require separate analytic receivers.

## 4. Quantitative analytic currency of the remaining hub

Let

`m=A[h,-h]`.                                                      (4.1)

From (3.1),

`||m|| >sqrt(123)/64 =0.1732896329...`.                          (4.2)

Apply account03/B19 r23 `QFORM-ARBITRARY-HUB-SQRT-SMALLBALL-v1`, which permits an arbitrary hub diagonal and arbitrary residual quadratic function. For every `z` and `eps>0`,

`P(|Q-z|<=eps)
 <=4*2^(1/4)||m||^(-1/2) eps^(1/2)
 <11.427 eps^(1/2).`                                             (4.3)

The same source therefore gives the quarter-Hoelder small-ball and quarter-Riesz currencies

`sup_z P(|Q-z|<=rho)<3.381 rho^(1/4)`,                           (4.4)

`sup_z E|Q-z|^(-1/4)<6.761`.                                    (4.5)

These are **not** an `L^infinity` density conclusion. The latest account04/B19 r3 obstruction `QFORM-L3-PLUS-HALF-HOLDER-NOT-LINFINITY-v1` specifically warns that a square-root small-ball estimate plus an `L^3` density estimate cannot be converted to `L^infinity` by generic interpolation. Thus the next step must make the hub resource interact with a second original-product smoothing channel before the final singularity is inverted.

## 5. Designated partner account04/B19 applied at an actual inequality

The completed account04/B19 theorem `QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1` applies in its residual-diffuse **exact-null-coloop** normal form and gives, for `0<D_res<=1`, a continuous density with

`||p_Q||_infinity<34 sqrt(log(e/D_res))`.                        (5.1)

On the concrete assembly range

`e^(-8)<=D_res<=1`,                                              (5.2)

we have `log(e/D_res)<=9`, hence

`boxed: ||p_Q||_infinity<102.`                                  (5.3)

Its source separately pays the exact `D_res=0` endpoint by `<5.844` and `D_res>=1` by `<11.748`. This is retained as an actual paid endpoint in the universal proof graph. No near-coloop extension of (5.1) is inferred.

## 6. Compact conditional proof assembly after this run

Within the current exact-rank-three rank-two-cross route:

1. r27 pays balanced frame defect; r28 pays fixed disjoint normalized two-basis mass and reduces low-disjointness to STAR/TRIANGLE.
2. r30 pays the moderate-angle STAR and leaves only extreme normalized coloop, globally-light thin-line, and small-pivot TRIANGLE endpoints.
3. Theorem 2.1 above excises every globally-light row without deleting it probabilistically: either the exact residual rank-three spectral window is diffuse and gives a continuous `<64` bound, or another ORIGINAL row has leverage `>31/1024`.
4. Scalar pivots on that row pay `<868`; failure of that pivot forces star energy `>123/4096`.
5. Therefore all r30 residue collapses to the single quantitative physical-hub condition (3.1), which already has the uniform small-ball / quarter-Riesz bounds (4.3)--(4.5).

The first unpaid implication inside this exact-rank-three chamber is now

`QFORM-SMALLPIVOT-STAR123-COUPLED-SMOOTHING-v1`:

> Given an exact-rank-three target matrix and one ORIGINAL physical row `h` with `|A_hh|<1/64` and `||A[h,-h]||_2^2>123/4096`, use the same source-product geometry to expose a second smoothing channel (indefinite pair, grouped rank-two bank, square channel, ridge packet, or equivalent) and convert the already-proved hub quarter-Riesz currency to a universal `L^infinity` density bound. The mechanism must tolerate arbitrary residual self curvature and all signs.

The broad normalized-coloop/thin-line/triangle branching is therefore no longer the first local debt.

Globally, the unrestricted theorem is still OPEN. The arbitrary-extra-spectrum/N3 closure cannot be inferred from this exact-rank-three compiler, and two independent end-to-end reviews are not yet appropriate because a full candidate proof does not yet exist.

## 7. Scope and correction audit

- All random conditioning is on ORIGINAL independent coordinates. No spectral rotation is treated as preserving independence.
- The spectral-window theorem is used only after literal deletion/conditioning of one original coordinate; its allowed coordinate-separable perturbations cover the induced linear term exactly.
- `M` may have any signature and repeated eigenvalues. Only `s_min(M)>=1` is used.
- No Gaussianity, moments, compact support, log-concavity, connected support, arbitrary-joint coarea, positive conditional projection-density moment, worst-fiber supremum, local-minor extremality, or law-uniform pointwise Fresnel decay is used.
- Small coefficients are never discarded as random perturbations.
- The diffuse row-excision branch proves a continuous `C_0` density. The scalar-pivot branch and the surviving hub compiler are recorded only at the regularity actually supplied by their source theorems.
- Full-target continuity remains OPEN.

## 8. Arithmetic checks

The exact threshold arithmetic used above is

`31/1024-1/4096=123/4096=0.030029296875`,

`1/32-1/4096=127/4096=0.031005859375`,

`128(65536/31)^(1/4)=867.9396503859...`,

`128*2048^(1/4)=861.0779292198...`,

`sqrt(123)/64=0.1732896329...`,

`4*2^(1/4)*(sqrt(123)/64)^(-1/2)=11.4269729515...`.

The proof is analytic; these decimal evaluations are only checks.

## 9. Operational integrity

Fresh control/corrections were reread immediately before publication. The required account03/B19 status-login write was attempted at the current UTC hour but the repository connector blocked the write under its safety checks; no successful status-file receipt is claimed. The immutable mathematical bundle is written only under this worker's authorized math path. Repository access occurred, but no authenticated native brain receiver/ingestion was observed, so execution remains `WITHOUT_VERIFIED_BRAIN`. No scheduler, task-count, enabled/paused state, notification, email, permission, or public-release change was made.
