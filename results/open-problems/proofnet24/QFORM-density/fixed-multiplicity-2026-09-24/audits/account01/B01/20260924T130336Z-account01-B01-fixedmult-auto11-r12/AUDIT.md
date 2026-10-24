# account01/B01 fixed-multiplicity full audit — r12

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `account01/B01`  
Run: `20260924T130336Z-account01-B01-fixedmult-auto11-r12`  
Audited repository snapshot: `yspennstate/math-open-problems@b7eb3da660dfbe32fef8c4d9295863cb3f2caf28`  
Canonical manuscript initial commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Canonical manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Declared manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Fresh brain control read before publication: `yspennstate/math-research-brain@6aaf4cdf3f5f7f68b84a7063ca11dd5cf8ab47ed`.

## Executive verdict

**Literal pinned 790-line manuscript: GAP (repairable), not PASS.** The only mathematical source defect I found is the singular-ambient limiting sentence in `lem:schur`, line 205. The moving threshold `t-|epsilon|` cannot be passed to the limit merely by continuity. A fixed-threshold `delta` argument repairs the lemma with no change of statement or constants; I independently rederived that repair below.

**Mathematical 17-eigenvalue theorem after inserting that repair: PASS in this end-to-end reconstruction.** I found no other fatal defect. This corrects my own earlier B01 immutable report that labelled the literal baseline PASS; that earlier artifact is preserved but its literal-source verdict is superseded by this report.

The exact repaired theorem checked is: for independent real `X_i` with densities bounded by `K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, and arbitrary `b,c`, the law of `X^T A X+b^T X+c` has an essentially bounded density with `||p||_infinity<=10000 K^2/s`. Global continuity is not proved by the pivot branches. The unrestricted three-eigenvalue conjecture remains open.

## Complete source-line audit

Every line of `manuscript.tex` was reread in this invocation. Status refers to the literal pinned source unless explicitly marked “after repair”.

| Source range / item | Status | Exact reasoning | Downstream impact / repair |
|---|---|---|---|
| 1–83: conventions, theorem, corollary, parameters, architecture | **PASS** | Quantifiers allow arbitrary dimension/signature/remaining spectrum, arbitrary affine `b,c`, and independent rough cap-`K` laws. Singular values are zero padded. No moments, support, log-concavity, diagonalization of random variables, or hidden exact-rank assumption enters. | Main scope is stated correctly. |
| 84–168: Fourier convention, Gaussian inversion, power envelope, Riesz identity | **PASS** | With `hat f(t)=int e^{itx}f(x)dx`, Plancherel and inversion constants are consistent. Gaussian regularization is Tonelli-safe. The half-Riesz constant and envelope integrals have the displayed powers. | Analytic normalization is sound. |
| 169–181: `lem:rank` | **PASS** | Approximation-number characterization gives both perturbation and rank-loss singular-value inequalities. | Used correctly in interpolation and Schur bookkeeping. |
| 183–204: `lem:schur`, statement and invertible-ambient proof | **PASS** | For invertible `A`, `S^{-1}` is the complementary principal block of `A^{-1}`. Positive and negative compression interlacing separately gives the absolute-eigenvalue count. The strict/weak threshold conversion in the inverse formulation is consistent with `N_T(t)=#{|lambda|>=t}`. | Correct for invertible ambient matrix. |
| 205: singular-ambient limit in `lem:schur` | **GAP (repairable)** | The manuscript applies the invertible result at the moving threshold `t-|epsilon|` and then says continuity gives the limit. A moving threshold can cross eigenvalues at exactly `t`; continuity alone does not justify the claimed count. | Every later Schur count should cite the fixed-`delta` repair below. The theorem survives unchanged after repair. |
| 209–301: diagonal dominance; geometric rank-one BL; product projection; scalar Fourier powers | **PASS** | Heat-flow derivative is `F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0` by the frame contraction; limits use nonnegative Fatou/Tonelli. Projection density uses deterministic SVD/Jacobian only, never post-rotation independence. Scalar Fourier power uses `m=floor(p/2)` and a genuine sum of signed independent copies. | All projection/Fourier inputs are internally proved. |
| 302–400: decoupling; regularized crossing determinant; volume envelopes | **PASS** | Independent-copy decoupling is product-preserving. In the determinant theorem the graph-BL frame is exact, the `c_j,d_i` Jacobians and scalar Fourier exponents cancel correctly, and `alpha=(2pi e)^2` removes the entropy factor. Cauchy–Binet gives the `Z_k` coefficients; `k=5` is integrable and `k=3` is used only through the Riesz weight. | No false scalar pointwise van-der-Corput input is used. |
| 401–482: scalar square, definite pair, hyperbolic pair | **PASS** | Scalar inverse branches give the square-root profile. The definite pair is bounded after a deterministic coordinate change in the integral, not by rotating random variables. Hyperbolic coordinates have Jacobian `1/(2 sqrt D)`; the tail is controlled in an original coordinate using cap one plus total mass one. | All pivot profiles remain valid for rough densities. |
| 483–525: quarter-power concentration and log potential | **PASS** | Large diagonal gives square-root concentration. Otherwise a random sign split creates an original-coordinate cross block with norm at least `||S||/4`; the determinant receiver supplies the quarter-power bound. Gaussian smoothing and layer cake give the logarithmic potential. | One surviving spectral direction is paid without moments. |
| 526–580: pivot volume; sampled interpolation; completion | **PASS** | The bordered determinant formula is exact. Singular seeds are omitted only in the direction that makes the sampling estimate weaker. For `P=A[:,T]A[S,T]^{-1}A[S,:]`, the completion has `D=0` on the seed, diagonal-free `E`, global `rank R<=3r`, and restricted `rank R[L,L]<=r`. Nonsymmetry of `P,R,E` is explicitly harmless because only singular values/rank and diagonal dominance are used. | Sensitive algebraic dependency closes. |
| 581–619: `prop:volume` | **PASS** | A bad ratio produces `||E||<=1/16`. For `m=4k-3` and `r<=k-1`, global rank loss `3r` leaves at least `r+1` large entries of diagonal `D`, all in `L`. On that block `|R_ii|>=371/400` while the off-diagonal row sum is `<23/28`, contradicting restricted rank `<=r` by strict diagonal dominance. | Proves the manuscript `4k-3 -> V_k` conversion. |
| 621–645: fair random cut and no-pivot consequences | **PASS** | Every ordered disjoint `k`-minor survives the fair cut with probability `4^{-k}`. Constants `12 sqrt(80e)<200` for the order-three half-potential and `800e<2400` for order-five density check. | No-pivot branches close. |
| 646–714: kernel integrals and `prop:pivot-H` | **PASS after Schur repair** | Kernel estimates are direct nonnegative layer-cake/Tonelli bounds. Scalar/definite/indefinite pivot branches keep truncated and full half-potentials distinct. The only challenged premise is the Schur spectral count; the fixed-`delta` proof below restores it. | Truncated half-potential bound is valid after repair. |
| 716–724: nine-eigenvalue half-potential proposition | **PASS after Schur repair** | Pivot/no-pivot is exhaustive; no-pivot uses `s_9` with `k=3`, while a pivot only needs the repaired surviving-direction count. Tail outside distance one is correctly added only when a full half-potential is needed. | This proposition is restored by the same local repair. |
| 726–790: main theorem, scaling, remarks | **PASS after Schur repair** | Under `s_17`, scalar pivot leaves 16 Schur directions, definite pair is directly bounded, indefinite pair leaves at least one direction for the logarithmic estimate, and no pivot uses `k=5`. With `Y=KX`, `Q=(s/K^2) Qtilde`, so density scales by exactly `K^2/s`. | Repaired 17-eigenvalue theorem closes with all advertised quantifiers. |

No source line is left **UNCHECKED** mathematically. The literal source has exactly the one labelled repairable gap above.

## Exact repair of line 205 (`lem:schur`)

Let

`A=[[B,C],[C^T,D]]`, `det B !=0`, `S=D-C^T B^{-1}C`, and fix `t>0`. For arbitrary `0<delta<t`, choose `epsilon_m ->0` with `A_m=A+epsilon_m I` invertible and `|epsilon_m|<delta/2`. For all large `m`, `B+epsilon_m I` is invertible and

`S_m=D+epsilon_m I-C^T(B+epsilon_m I)^{-1}C -> S`.

Every eigenvalue of `A` with modulus at least `t` becomes an eigenvalue of `A_m` with modulus greater than `t-delta`, hence

`N_{A_m}(t-delta) >= N_A(t)`.

Apply the already valid invertible case at the **fixed** threshold `t-delta`:

`N_{S_m}(t-delta) >= N_{A_m}(t-delta)-k >= N_A(t)-k`.

Ordered eigenvalues of the symmetric matrices `S_m` converge to those of `S`, so

`N_S(t-delta) >= N_A(t)-k`.

Finally `N_S(t-delta) downarrow N_S(t)` as `delta downarrow0` in finite dimension. Therefore

`N_S(t)>=N_A(t)-k`.

This is a complete replacement proof for the singular paragraph; no constant or later hypothesis changes.

## Required support files and dependency closure

At the audited snapshot all files requested by the owner are present and were read in full.

- `README.md`: **PASS as current status metadata**; it correctly distinguishes written candidate, reviews, and release gate.
- `SOURCE_MANIFEST.json`: **PASS for internal metadata consistency** with the observed canonical manuscript blob, line/byte counts, and stated support-file roles. The declared SHA-256 is pinned here; this review did not independently recompute SHA-256 bytes outside the repository connector.
- `proof_map.csv`: **PASS**; the labelled statement/proof ranges match the manuscript structure, including `lem:schur` at 183–207 and the main proof at 726–749.
- `verify.py`: **PASS as a finite diagnostic script, not a proof**. It pins the manuscript SHA, checks exact interpolation identities/rank bounds and constants, and runs numerical Schur/graph-weight diagnostics. Its random Schur tests are generically invertible and therefore do not repair the singular limiting sentence.
- `checks.json`: **PASS as the recorded output of that finite suite**, reporting 534 exact interpolation seeds, 18 exact volume comparisons, 240 floating Schur threshold cases and 30 graph-weight cases. These finite tests do not establish universal analytic claims.
- `AUDIT.md`: **GAP as a validation verdict** because the historical self-audit missed line 205. Its other bookkeeping is useful evidence but is not an independent proof.
- `DELIVERY_STATUS.md`: **PASS as current delivery metadata**; it explicitly says the B18 Schur clarification and competing PASS reports must be reconciled.

The earlier package-absence issue observed in a previous B01 run is now **RESOLVED**: the four advertised support files are present at this snapshot. The canonical `manuscript.tex` itself remains byte-identical to the initial source, so the Schur repair is not yet incorporated into that literal blob.

## Quantifiers, scaling, and dependency closure

After the Schur repair, the complete specialized dependency graph is internal:

`Fourier/Gaussian/Riesz -> geometric BL -> product projections -> scalar Fourier powers -> decoupling/determinant -> crossing-volume envelopes -> interpolation/rank contradiction -> no-pivot receivers`,

plus

`square/definite/hyperbolic pivots -> quarter concentration/log kernels -> repaired Schur count -> pivot half-potential -> main theorem`.

The bibliography is attribution/background rather than an unproved mathematical dependency. No dimension-dependent quantity enters the final constant.

## Review-state correction

My prior B01 r11 report called the literal manuscript PASS. That label was too strong because it did not detect the moving-threshold issue at line 205. This immutable r12 report corrects that status:

- canonical literal blob `183ccd...`: **GAP (repairable)**;
- mathematical 17-eigenvalue theorem with the displayed fixed-`delta` repair inserted: **PASS in this review**;
- global continuity: **not proved**;
- full three-eigenvalue conjecture: **OPEN**.

A separate improvement artifact from this run gives an independent end-to-end reconstruction of the stronger nine-eigenvalue candidate and a precise eight-direction endpoint certificate/barrier. No self-awarded release or peer-review certificate is made here.
