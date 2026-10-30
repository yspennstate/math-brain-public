# fleet01/B06 complete audit — fixed multiplicity candidate

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T123830Z-fleet01-B06-fixedmult-audit-r11`  
Repository/branch: `yspennstate/math-open-problems`, `master`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Canonical recorded SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Model: GPT-5.6 Sol. Provider reasoning effort/counters: UNKNOWN / not exposed.

## Verdict

**PASS for the complete written 17-eigenvalue mathematical argument, in this independent review.** I found no FALSE statement and no unresolved mathematical GAP in `manuscript.tex`. No manuscript lines remain UNCHECKED in this review. This review does **not** turn the candidate into an independently validated theorem by itself; the owner requires two genuinely separate complete reviews before that status.

The exact scope I checked is the one in the source: arbitrary dimension; independent real coordinate laws with densities bounded by `K`; arbitrary real symmetric `A`; arbitrary signature, remaining spectrum, affine `b,c`; hypothesis `s_17(A)>=s>0`; conclusion `||p_Q||_infty <= 10000 K^2/s`. The full three-eigenvalue conjecture is not claimed or proved.

There is a **repository-package GAP**: at the fresh `master` snapshot, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are absent from the stated manuscript root (each direct fetch returned 404), although `README.md` describes them as canonical package members and `AUDIT.md` describes finite checks from them. Therefore those finite diagnostics and their claimed reproducibility are **UNCHECKED from this repository snapshot**. This is not a mathematical gap in the self-contained `manuscript.tex` proof.

## Exhaustive source-range audit

The seven exact source chunks below cover all 790 source lines without omission.

| Source range | Status | What was checked |
|---|---|---|
| 1--120 | PASS | Preamble/definitions; theorem and corollary quantifiers; normalization architecture; pivot/no-pivot split; Fourier convention; Gaussian kernel and inversion. Scaling target `K^2/s` is consistent with `Y=KX` and `Q=(s/K^2)\widetilde Q`. |
| 121--240 | PASS | Power-envelope integral; Riesz `1/2` identity and constant `1/sqrt(2*pi)`; singular-value perturbation/rank shift without symmetry; Schur spectral count including singular `A`; strict diagonal dominance; start of geometric BL heat-flow proof. |
| 241--360 | PASS | Completion of geometric BL including frame contraction, integration by parts, large-time Gaussian limit and small-time Fatou; product-projection density with no rotated-independence claim; scalar Fourier-power bound; two- and four-power decoupling; graph determinant definitions through the BL setup. |
| 361--480 | PASS | Graph determinant theorem constants/Jacobian/weights/trace/entropy cancellation; `alpha=(2*pi*e)^2`; determinant exponent `-1/8`; Cauchy--Binet crossing volumes; order-5 density and order-3 half-potential exponents; scalar-square profile; definite-pair Jacobian; hyperbolic parametrization and both tail bounds through the logarithmic envelope. |
| 481--600 | PASS | Completion of hyperbolic bound; quarter-power concentration; no-atom/log-potential consequence; pivot/volume definitions; no-pivot entry bound; volume-sampled interpolation; bordered determinant; nonsymmetric completion, support, global rank `<=3r`, restricted rank `<=r`; start of spectral-to-volume contradiction. |
| 601--720 | PASS | Spectral-to-volume contradiction including `D=0` on seed, `m>=4r+1`, forced large diagonal entries, exact diagonal-dominance slack; random cut factor `4^{-k}`; no-pivot order-3/order-5 consequences; kernel integrals; scalar/definite/indefinite pivot half-potentials; start of nine-direction receiver. |
| 721--790 | PASS | Nine-eigenvalue full half-potential; complete main case split; Schur survivor counts; density domination/averaging; general `K,s` scaling; interval equivalence; threshold accounting and limitations; continuity scope. |

## B06 lens: graph determinant theorem reconstructed

Write `a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^T M`. For each column-coordinate row `e_j` and each physical row `m_i^T` of `M`, define

`c_j = alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`.

The vectors `sqrt(alpha) H^{-1/2}e_j` and `a H^{-1/2}m_i` form a Parseval frame, hence `0<c_j<=1`, `0<=d_i<=1`, and

`theta=sum_i d_i=sum_j(1-c_j)`.

After fourth-power decoupling, the integral is

`int prod_j g_j(x_j) prod_i |fhat_i(a m_i.x)|^2 dx`.

The substitution `x=H^{-1/2}z` contributes `det(H)^(-1/2)`. Normalizing each frame vector and applying geometric BL gives the exact factors

`alpha^(c_j/2)c_j^(-c_j/2)||g_j||_(1/c_j)` and `d_i^(-d_i/2)||h_i||_(1/d_i)`, `h_i=|fhat_i|^2`.

Because `g_j<=1`, `||g_j||_(1/c_j)<=1`. The scalar Fourier lemma at exponent `2/d_i` gives

`||h_i||_(1/d_i) <= (2*pi*sqrt(e d_i))^(d_i)`.

Thus the `d_i` powers cancel. The entropy inequality `prod c_j^(-c_j/2)<=e^(theta/2)` combines with the Fourier factor to give `(2*pi*e)^theta`. Factoring `alpha^d` from `det H` contributes `alpha^(-theta/2)`, and the chosen `sqrt(alpha)=2*pi*e` cancels this exactly. Therefore

`|phi_Z(t)|^4 <= det(I + t^2 M^T M/(pi^2 e^2))^(-1/2)`,

hence

`|phi_Z(t)| <= det(I + t^2 M^T M/(pi^2 e^2))^(-1/8)`.

I found no missing Jacobian, wrong BL exponent, lost factor of two, or sign/symmetry assumption here. The use of `M^T M` is deterministic and does not rotate the random coordinates.

## Sensitive algebra checks

### Nonsymmetric interpolation and both rank bounds — PASS

For a sampled disjoint seed `(S,T)`, `P=A[:,T]B^{-1}A[S,:]` has rank at most `r`, agrees with `A` on rows `S` and columns `T`, and need not be symmetric. With `L=(S union T)^c`, defining `E_LL=off(A_LL-P_LL)` and `D_ii=A_ii-P_ii` on `L` gives `R=A-D-E` with `R_LL=P_LL` and hence `rank R_LL<=r`. Moreover `R-P` vanishes on rows `S`, columns `T`, and `LxL`; the only possible remainder is supported in rows `T` or columns `S`, giving `rank(R-P)<=2r` and `rank R<=3r`. No symmetry of `R,E` is used later.

### `D` vanishes on the seed and spectral-to-volume conversion — PASS

At a bad ratio `V_{r+1}<kappa V_r`, `||E||<=||E||_F<=(r+1)sqrt(kappa)<=1/16`. With `m=4k-3` and `r<=k-1`, `m>=4r+1`. Rank perturbation gives `s_{m-3r}(D)>=1-epsilon`, hence at least `r+1` diagonal entries of `D` have size `>=1-epsilon`; because `D=0` on `S union T`, they lie in `L`. On those `r+1` coordinates, `|R_ii|>=371/400`, while each off-diagonal is `<1/7+1/16`, so the row sum is `<23/28<371/400`. Strict diagonal dominance forces rank `r+1`, contradicting `rank R_LL<=r`.

### Singular Schur paragraph — PASS

For `A_epsilon=A+epsilon I`, the pivot remains invertible for small `epsilon`, `S_epsilon->S`, and `N_{A_epsilon}(t-|epsilon|)>=N_A(t)`. If `m=N_A(t)-k>0`, the invertible case gives `s_m(S_epsilon)>=t-|epsilon|`; continuity of ordered singular values of the symmetric Schur complements yields `s_m(S)>=t`. No rate comparison beyond convergence is required.

## Analytic endpoints and rough-law handling

**PASS.** The order-five determinant envelope has exponent `5/4>1`, so absolute Fourier inversion is legitimate. The order-three envelope has exponent `3/4`; it is used only after multiplication by `|t|^{-1/2}` in the Riesz estimate, giving an integrable `|t|^{-5/4}` tail. The manuscript does not infer a density directly from the order-three envelope.

The scalar-square, definite-pair and hyperbolic calculations are all used as domination statements after conditioning on original coordinates. Tonelli handles rough densities and avoids exceptional-slice choices. The hyperbolic Jacobian is `1/(2 sqrt(|det B|))`; the two branches cancel the factor `1/2` in the final envelope. The large-tail coordinate change uses only one original density at a time, bounded by one and with mass one. No conditional density cap is inferred from an unconditional projection.

## Threshold-reduction audit

I do **not** claim an unconditional reduction below 17 in this run. Within the current proof pipeline, the terminal `r=4` case is genuinely saturated at the bookkeeping level: `s_16` only forces four large diagonal entries after paying the global `3r=12` rank, while the restricted block is allowed rank four, so the strict-diagonal-dominance contradiction needs a fifth coordinate and therefore `s_17`. Separately, replacing order five by order four in the present fourth-power determinant receiver gives only `|phi(t)|=O(|t|^{-1})`, the non-integrable absolute-Fourier endpoint.

A new analytic improvement overcoming part of the endpoint, under a quantitative row-leverage gate, is recorded separately in this run's `IMPROVEMENT.md`. It recovers the manuscript theorem at `q=2` and gives an integrable order-four envelope whenever the crossing row leverage is uniformly `<1`; it does **not** establish that such a cut exists under only `s_13` or `s_16`, so it is not a lower-multiplicity theorem.

## Package/readback status

- `manuscript.tex`: FULL 790-line review; mathematical verdict PASS.
- `README.md`: FULL review; its canonical-package list conflicts with the current missing supplementary files.
- `AUDIT.md`: FULL review; self-audit claims are consistent with the manuscript mathematics I checked, but finite-check claims are not independently reproducible from the current root because the checker bundle is absent.
- `SOURCE_MANIFEST.json`: UNCHECKED / MISSING (404).
- `proof_map.csv`: UNCHECKED / MISSING (404).
- `verify.py`: UNCHECKED / MISSING (404).
- `checks.json`: UNCHECKED / MISSING (404).

No baseline source file was modified by this review.