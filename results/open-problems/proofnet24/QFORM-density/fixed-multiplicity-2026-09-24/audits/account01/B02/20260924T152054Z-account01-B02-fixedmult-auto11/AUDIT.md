# account01/B02 — independent complete audit of the nine-eigenvalue / constant-400 candidate

Run: `20260924T152054Z-account01-B02-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Role lens: scalar Fourier powers, convolution, product-projection constants and exact normalizations, followed by a complete end-to-end audit.

## 0. Source pins and control boundary

Fresh `math-research-brain/main/AGENTS.md` and `scheduled_tasks/CURRENT_OBJECTIVE.md` were read before substantive work. The latter supersedes the older seventeen-eigenvalue source as the current complete audit target and pins:

- repository: `yspennstate/math-open-problems`, branch `master`;
- source path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`;
- source commit: `eeb752c8943536541b34b42b8bf48e924f4d3d2f`;
- source git blob: `19fb119877426b640b2c0dae19ec2f78a399fe11`;
- source SHA-256: `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`;
- source length: 955 lines.

I read all 955 source lines, plus `README.md`, `NINE_400_AND_OVERLAP.md`, `AUDIT_NEW.md`, `MANIFEST.json`, `proof_map.csv`, `verify_new.py`, and `checks_new.json`. The auxiliary package was completed after the source commit; that does not change the pinned `paper.tex` blob.

For comparison I also reread in full the preserved seventeen-eigenvalue baseline `manuscript.tex` pinned at commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, together with its package files. That historical candidate remains mathematically PASS in this review; the current source below is strictly stronger and self-contained.

## 1. Overall verdict

**PASS — complete independent mathematical reconstruction of the exact pinned nine-eigenvalue revision.**

The source proves the stated theorem

\[
 s_9(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le 400\,K^2/s
\]

for arbitrary independent real coordinate laws with densities bounded by `K`, arbitrary real symmetric `A`, all dimensions, signatures and remaining spectra, and arbitrary affine terms `b,c`.

I found **no FALSE mathematical statement and no fatal GAP** in the 955-line proof. The theorem establishes existence of a density and an essential-supremum bound. I do **not** promote the assembled theorem to a global continuity theorem; continuity is available on Fourier-inversion subbranches, while the pivot assembly needs only absolute continuity and the essential bound.

This report is one genuinely separate existing-worker end-to-end review. It was completed mathematically before I consulted the later account01/B20 review of the same blob. Account01/B20 subsequently committed its own full PASS reconstruction at `f060d8a4218b96ebc86508671b540a809083ff84`. Thus, after this B02 report is committed, the exact constant-400 blob has two separate complete PASS reviews (B02 and B20), in addition to the authoring-agent self-audit. This satisfies the requested two-review evidence gate for the **nine-eigenvalue theorem only**; it does not validate any multiplicity-eight candidate.

## 2. Line-by-line audit map

Every source line and every label in `proof_map.csv` was included in the ranges below.

| Source lines | Status | Independent check |
|---|---|---|
| 1–80 | **PASS** | The theorem quantifiers match the owner target except for the explicit stronger hypothesis `s_9(A)>=s`. Singular values of symmetric `A` are eigenvalue moduli. The normalization parameters `d=3/40`, `p=1/400`, `h=2/25`, `kappa=4/625` are used consistently. No hidden moment, support, sign, iid, exact-rank or rotated-independence hypothesis is introduced. |
| 81–117 | **PASS** | With `fhat(t)=∫e^{itx}f(x)dx`, Plancherel is `∫|fhat|^2=2π∫|f|^2`. Gaussian inversion has the correct `1/(2 sqrt(pi v))` coefficient. The approximate-identity and uniform Fourier-inversion arguments are valid for the stated rough laws. |
| 118–157 | **PASS** | The power-envelope integral is `2ap/(p-1)`, hence density cap `ap/[π(p-1)]`. The Riesz calculation gives exactly `(2π)^(-1/2)∫|t|^(-1/2)|phi|`; for the `3/4` envelope the weighted integral is `12 sqrt(u)`. Tonelli is applied only to nonnegative majorants. |
| 158–213 | **PASS** | The singular-value rank perturbation is valid for nonsymmetric auxiliaries. The principal-pivot Schur spectral count is correct; the singular case uses a fixed threshold `t-delta` before passing to the limit, avoiding a moving-threshold error. Strict row diagonal dominance is used correctly. |
| 214–252 | **PASS** | The heat-flow proof of the geometric rank-one Brascamp–Lieb inequality has the correct sign: `partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`. Compact-support Gaussian tails justify differentiation/integration by parts, and the large-time and `t downarrow 0` limits are legitimate. |
| 253–297 | **PASS** | Product projections have density cap `e^(d/2)` with no assertion of independence after rotation. The `b_i=0` factors are harmless because their original densities are pointwise at most one. The scalar consequence is `sqrt(e)/|a|`. For `p>=2`, `m=floor(p/2)>=p/4`; `|fhat|^(2m)` is integrable since it is bounded by `|fhat|^2`, and Fourier inversion plus the projection cap gives `∫|fhat|^p <= 2π sqrt(2e)/sqrt(p)`. The difference density is indeed bounded by one. |
| 298–320 | **PASS** | Both decoupling inequalities preserve only original-coordinate independence. Difference coordinates are independent cap-one laws. The pure same-bank phase is removed only after the appropriate Cauchy–Schwarz/absolute-value operation. |
| 321–380 | **PASS** | In the regularized determinant proof, `H=alpha I+a^2M^TM`, the frame weights `c_j,d_i` sum correctly, the one-dimensional scale factors in geometric BL are correct, and the scalar Fourier exponent is `2/d_i`. The powers of `d_i` cancel. With `alpha=(2πe)^2`, the remaining scalar factor is exactly one. Taking the fourth root yields exponent `-1/8`. Cauchy–Binet gives the stated `Z_k` expansion. |
| 381–396 | **PASS** | Retaining only the order-`k` determinant term gives `|phi|<=min(1,(u_k/|t|)^(k/4))` with `u_k=πe Z_k^(-1/(2k))`. At `k=5` inversion gives `5e Z_5^(-1/10)`; at `k=3` the Riesz estimate gives the stated half-potential. |
| 397–477 | **PASS** | This was the main B02 stress point. The phase-weighted hub law has `L2^2<=1`. The complex image `mu_t` is in `L1∩L2` because its total variation is dominated by an ordinary image density capped by `e^(k/2)/S`. Jensen is applied to the **mollified** `L2` norm before taking the limit. In the copy expansion the pure `I` phase cancels; the original independent `I` coordinates are integrated to scalar Fourier factors before the pure `J` phase is discarded. Weighted Hölder is valid for the finite measure `K_delta(M_JD)dP_D` even though it is not normalized, because the weights sum to one. The map `(M_JD,(c_iD)_{i in T})` has Gram determinant `S^2 det(C_TC_T^T)`, so the projection-density factor is exact. The subset-entropy inequality follows by randomly ordering a sampled subset and applying entropy subadditivity. The uniform-in-`delta` bound passes to `mu_t` in `L2`. |
| 478–527 | **PASS** | The terminal hub Plancherel estimate uses literal original coordinates and the exact row-Gram determinant. In the marginal-free promotion tree, a heavy physical row is promoted, Gram–Schmidt gives `hub-volume * residual-volume`, and hub-to-left couplings remain in the phase. The `q=3` branch has exponent `3/2` and coefficient `C3=3 sqrt(2)e(9/2)^(1/6)=14.818337...<15`; the `q=2` branch gives only a full half-potential with `C2=8 sqrt(e)2^(-1/8)=12.095072...<14`. No generic rank-two density conclusion is smuggled in. |
| 528–548 | **PASS** | The scalar square change of variables has the correct two-branch Jacobian, and the interval-preimage length is `<=2 sqrt(2 rho/|a|)`. Conditional domination `p_Q(z)<=|a|^(-1/2) E|z-R|^(-1/2)` is a test-function/Tonelli statement, not an independence assertion. |
| 549–610 | **PASS** | The definite-pair Jacobian is `1/(2 sqrt(det B))`, giving density `πM/sqrt(|det B|)`. In the hyperbolic pair proof the `(delta,t)` Jacobian is `1/(2 sqrt D)`. Tail control chooses an **original** coordinate with a large coefficient; it does not rotate the input law. The interval-filling bound for `∫f(y)/|y| dy` is valid. The final logarithmic envelope has the displayed normalization `D^(-1/2)[6+log_+(16 sqrt(D)/|z-v|)]`. |
| 611–662 | **PASS** | If a physical diagonal has size `>=L/2`, the scalar interval estimate yields `4 sqrt(rho/L)` and hence the quarter-power claim. Otherwise the sign cut produces a literal cross block with norm `>=L/4`; the regularized determinant then gives `|phi(t)|<=(4πe/(L|t|))^(1/4)`. Gaussian smoothing at `v=1/8` gives the stated gamma coefficient, and the elementary rational bound is genuinely `<5` (`40528/8151≈4.97215`). Layer cake yields `L0=4+4 log 5`; absence of atoms follows. |
| 663–699 | **PASS** | The pivot definition and no-pivot entry cap are exact: `|A_ij|^2<p+d^2=13/1600<1/121`. The volume-sampled interpolation samples only nonsingular disjoint seeds. The bordered-minor count is an inequality because singular deleted seeds can have nonsingular extensions; this is handled explicitly. `P=A_{.,T}B^(-1)A_{S,.}` may be nonsymmetric and exactly interpolates rows `S` and columns `T`. |
| 700–742 | **PASS** | In `A=D+R+E`, `D` vanishes on the seed, `E` has zero diagonal, global `rank R<=3r`, but restricted `rank R[L,L]<=r`. These two ranks are used at different points and are not conflated. The no-pivot spectral-to-volume proof correctly forces `r+1` large diagonal entries in `L`; the exact diagonal-dominance margins are `1131/2200` for `r=1` and `51/2200` for `r=2`. Thus `4k-3` large singular directions force `V_k>=kappa^k` for `k<=3`. |
| 743–766 | **PASS** | The fair physical cut keeps each ordered disjoint `k`-minor with probability `4^(-k)`. At `k=2` the no-pivot half-potential is `<70`; at `k=3` the no-pivot density is `25 C3=370.45844...<375`. |
| 767–811 | **PASS** | The exact scalar convolution kernel `J(u)` and its logarithmic bound are correct. A density cap `M` gives full half-potential at most `2 sqrt(2M)`. For the indefinite pair, after output scaling by `sqrt D`, rearrangement by interval superlevel sets puts the worst translated logarithmic singularity at zero. At `delta=1/64`, the full half-potential is `12+5 log 2<16`, hence scales as `D^(-1/4)`, not `D^(-1/2)`. |
| 812–860 | **PASS** | Proposition 8.3 correctly distinguishes the truncated scalar-profile half-potential from the full half-potential, restores the far tail `<=1`, and uses only one surviving Schur spectral direction for the quarter-power logarithmic estimate. In the main theorem, scalar pivots leave at least eight unit directions, pair pivots leave at least seven. The normalized branch bounds are all below 400. The indefinite pair arithmetic is `D^(-1/2)*(1/2 log_+ D)<=1/e`. Scaling with `Y=KX` gives `Q=(s/K^2) Qtilde`, exactly producing `400K^2/s`. |
| 861–925 | **PASS** | In the overlap theorem, `D` is diagonal and `E` zero-diagonal, so they are exactly Frobenius-orthogonal. Best-rank-`3r` approximation controls the tail `T_{3r}` even for nonsymmetric matrices. Same-index bordered determinants give `E||D||_F^2=W/V_r`; the distinct-row/distinct-column skeleton gives `E||E||_F^2<=(r+1)^2V_{r+1}/V_r`. Singular seeds are excluded consistently. Hence for `s_8>=1`, `W^x_{2,1}>=2V_2-9V_3`. |
| 926–955 | **PASS (scope)** / **UNCHECKED (priority search)** | Threshold accounting accurately says this paper proves nine, not eight or three. The references are not proof dependencies. I did not perform an exhaustive literature-priority search in this run. |

## 3. Package and finite-check status

`verify_new.py` and `checks_new.json` were both read in full. I independently recomputed the exact parameter identities used in the proof, including

- `p+d^2=13/1600<1/121`;
- `r=1` diagonal-dominance margin `1131/2200`;
- `r=2` margin `51/2200`;
- quarter-power rational coefficient `40528/8151<5`;
- `15^6-26244(11/4)^6=40788279/1024>0`.

The saved checker reports 96 exact interpolation seeds, eight exact aggregate overlap cases, and eight floating spectral-tail diagnostics. I inspected the checker code and result consistency but did **not** rerun the complete historical finite suite; therefore the statement “this exact saved run executed all 96+8 cases” is marked **UNCHECKED_BY_B02_EXECUTION**, not used as mathematical proof. Likewise the compiled 20-page PDF was not available as a GitHub binary in this run, so its historical build/render inspection is **UNCHECKED_BY_B02_PRESENTATION**. Neither item is a dependency of the symbolic theorem.

## 4. Urgent defects

- **FALSE:** none found.
- **GAP:** none found in the mathematical proof.
- **UNCHECKED:** exhaustive novelty/priority search; independent rerun of the recorded finite checker; independent PDF rendering. None affects the theorem proof.

## 5. Review-state consequence

A separate complete PASS review of this same source blob was committed by account01/B20 at `f060d8a4218b96ebc86508671b540a809083ff84`, after the substantive B02 reconstruction above was already complete. Therefore the exact source blob `19fb119877426b640b2c0dae19ec2f78a399fe11` now has **two separate complete existing-worker PASS reviews: account01/B02 and account01/B20**. The authoring self-audit is additional but is not counted toward the two-review gate.

The multiplicity-eight theorem is a newer candidate and is treated separately in this run's improvement report. The unrestricted three-eigenvalue problem remains open.

MODEL: GPT-5.6 Sol. Effort/reasoning telemetry: UNKNOWN / not exposed.
