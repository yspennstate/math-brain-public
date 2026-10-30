# fleet01/B03 r11 — fixed-multiplicity manuscript audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer: `fleet01/B03`  
Run: `20260924T115227Z-fleet01-B03-fixed-multiplicity-audit-r11`  
Starting lens: decoupling, independent copies, conditional independence, powers two/four, Fourier exponents.  
Pinned manuscript commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256 from owner/source metadata: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Current-master manuscript blob read in this run: `183ccd294763214e6a707e8d4749ff9a8cf7006d` (same source as baseline).

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this complete textual audit.** I read the complete 790-line `manuscript.tex` and re-derived the proof chain rather than relying on the self-audit. I found no fatal mathematical gap and no false use of conditional independence, rotated-coordinate independence, or pointwise quadratic-phase decay. The theorem audited is exactly: independent real coordinates with densities at most `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, `s_17(A)>=s>0`, and

`||p_{X^TAX+b^TX+c}||_infty <= 10000 K^2/s`.

This report does **not** claim the unrestricted three-eigenvalue conjecture, optimality of 17, peer review, or formal verification.

There is one release/reproducibility **GAP**: the current manuscript root advertises `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but direct reads of each path returned not-found in this run. Thus the numerical/finite-check claims in the self-audit are **UNCHECKED here** and cannot presently be rerun from the advertised root. This does not break the self-contained symbolic proof in `manuscript.tex`.

The external bibliography attribution to BCCT/Rudelson--Vershynin is **UNCHECKED in this run**; it is attribution only and not a dependency, because the specialized inequalities used in the theorem are reproved in the manuscript.

## Exhaustive source ledger

The following eight ranges partition all 790 source lines, with no omitted source range.

| Source lines | Status | What was checked independently | Impact |
|---|---|---|---|
| 1--100 | PASS | Front matter, exact theorem quantifiers, singular-value convention, `K=s=1` normalization plan, pivot definition/architecture, Fourier convention, Gaussian regularizer, Plancherel and inversion statements. The theorem does not add support, moment, smoothness, sign, rank, or rotation hypotheses. | Main scope is correctly stated. |
| 101--200 | PASS | Gaussian inversion proof, power-envelope integral, Riesz/negative-half-moment representation and constants, singular-value perturbation/rank inequality, beginning of Schur spectral-count proof. The Riesz weight is `|t|^{-1/2}` and the `3/4` envelope is used only in the weighted integral. | Fourier constants and half-potential exponent are sound. |
| 201--300 | PASS (one wording clarification) | Singular Schur limit, strict diagonal dominance, complete geometric rank-one BL heat-flow proof and limiting passage, product-projection lemma, scalar Fourier powers. In the projection proof, after zero-`b_i` factors are dropped, the clean statement is `sum_{b_i>0}(1-b_i)<=d`; equivalently, if the sum is restored over all indices, `sum_i(1-b_i)=d`. The manuscript's conclusion `<=e^{d/2}` is unaffected. | No theorem repair beyond this harmless clarification. |
| 301--400 | PASS | Entire B03 core: cross-block representation, two-copy decoupling, square/fourth powers, independence of difference coordinates, regularized determinant theorem, graph-BL weights/scales, determinant expansion, crossing-volume exponents. I recomputed the fourth-root exponent `-1/8` and the `k/4` Fourier decay. | No hidden conditional-independence or recapping error. |
| 401--500 | PASS | Scalar-square profile and measure domination, definite two-coordinate change of variables, indefinite hyperbolic level-set parametrization/Jacobian and tail decomposition. Rotations occur only inside deterministic integrals; product density is retained in original physical coordinates. | Pivot local estimates are valid for rough cap-one laws. |
| 501--600 | PASS | Completion of hyperbolic tails, quarter-power concentration, random sign cut, no-atom/log-potential bound, disjoint-volume definition, no-pivot entry bounds, volume-sampled interpolation, bordered-minor count, nonsymmetric completion with global rank `<=3r` and restricted rank `<=r`. | Sensitive interpolation/support chain is sound. |
| 601--700 | PASS | Spectral-to-volume contradiction, `m=4k-3`, global `3r` rank loss versus restricted `r` contradiction, random coordinate cut, order-3 and order-5 analytic consequences, singular kernels, scalar/definite/indefinite pivot half-potential branches. | Nine- and seventeen-direction intermediate estimates close. |
| 701--790 | PASS mathematically; bibliography attribution UNCHECKED | Completion of pivot-H, nine-eigenvalue full half potential, all branches of main theorem, general `K,s` scaling, density-vs-interval equivalence, threshold accounting, continuity limitation. External reference descriptions were not independently source-verified. | Candidate theorem closes; full three-eigenvalue problem remains open. |

## Detailed B03 audit: copies, conditioning and Fourier powers

### 1. Decoupling identities — PASS

Across an original-coordinate cut `I sqcup J`, write

`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`.

Cauchy--Schwarz in the probability law of `X_I` gives

`|phi_Z(t)|^2 <= E_{X_I} |E_{X_J} exp(itG(X_J)+2it X_I^T M X_J)|^2`.

Expanding this square introduces one independent copy `X'_J`, so `D=X_J-X'_J`. Before absolute values the extra phase is `exp(it(G(X_J)-G(X'_J)))`; integrating each original independent `X_i`, `i in I`, gives exactly

`prod_i fhat_i(2t(MD)_i)`.

Taking modulus produces (3.2). The variables `D_j` are independent because each uses a disjoint independent pair `(X_j,X'_j)`, and

`g_j=f_j*tilde f_j <= ||f_j||_infty ||tilde f_j||_1 <=1`.

No statement is made that a sum and difference from the same coordinate pair are independent, and no conditional law is re-capped.

For the fourth power, if

`B(D)=prod_i |fhat_i(2t(MD)_i)|`,

then `0<=B<=1` and `(E B)^2<=E B^2`, hence

`|phi_Z(t)|^4 <= E_D prod_i |fhat_i(2t(MD)_i)|^2`.

This is the exact power needed downstream.

### 2. Scalar Fourier power input — PASS

For `p>=2`, with `m=floor(p/2)>=p/4`, `|fhat|<=1` gives

`int |fhat|^p <= int |fhat|^{2m}`.

The last integral is finite already because `|fhat|^{2m}<=|fhat|^2` and Plancherel applies to `f` (`f<=1`, `int f=1` implies `f in L^2`). It is the characteristic function integral of a sum of `m` independent differences. The scalar projection lemma applied to the `2m` original signed independent coordinates yields

`int |fhat|^{2m} <= 2 pi sqrt(e)/(sqrt(2m)) <= 2 pi sqrt(2e)/sqrt(p)`.

Thus no circular use of Fourier inversion is present.

### 3. Regularized determinant theorem — PASS

Let `a=2t`, `alpha=(2 pi e)^2`, `H=alpha I+a^2 M^TM`,

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`.

The rank-one frame identity is exact. Its trace gives

`theta=sum_i d_i=sum_j(1-c_j)`.

After `x=H^{-1/2}z`, geometric BL produces the displayed determinant/Jacobian factor. The difference densities satisfy `||g_j||_{1/c_j}<=1`. With `h_i=|fhat_i|^2`, the scalar power bound at `p=2/d_i` gives

`||h_i||_{1/d_i} <= (2 pi sqrt(e d_i))^{d_i}`.

The `d_i` powers cancel the BL scale. The entropy bound on the `c_j` weights supplies `e^{theta/2}`, and `sqrt(alpha)=2 pi e` cancels the remaining scalar factor. Consequently the right side for `|phi|^4` is

`det(I+t^2 M^TM/(pi^2 e^2))^{-1/2}`,

and taking the fourth root yields precisely

`|phi_Z(t)| <= det(I+t^2 M^TM/(pi^2 e^2))^{-1/8}`.

### 4. Crossing exponents — PASS

Retaining the `k`th Cauchy--Binet coefficient gives

`|phi_Z(t)| <= min(1,(u_k/|t|)^{k/4})`.

Hence order 5 gives exponent `5/4>1` and direct `L^1` inversion, while order 3 gives exponent `3/4`; after the Riesz weight `|t|^{-1/2}` its tail is `|t|^{-5/4}`, integrable. The manuscript never promotes the order-3 estimate to a direct bounded-density statement.

## Algebraic and measure-theoretic checks outside the B03 lens

- **Schur count — PASS.** For invertible `A`, the complementary principal block of `A^{-1}` is `S^{-1}`. Positive and negative interlacing applied to `A^{-1}` bounds the number of eigenvalues of `S^{-1}` outside `(-1/t,1/t)`, equivalent to `N_S(t)>=N_A(t)-k`. The `A+epsilon I` limiting argument handles singular `A` while keeping the pivot invertible for small epsilon.
- **Heat-flow limiting step — PASS.** The frame condition gives the contraction inequality in the sign needed for monotonicity. Compact support supplies Gaussian domination at fixed positive times and at infinity; Fatou plus monotone approximation handles general nonnegative integrable inputs.
- **Nonsymmetric interpolation — PASS.** `P=A[:,T]B^{-1}A[S,:]` agrees with `A` on rows `S` and columns `T`. With the manuscript `D,E,R`, `R[L,L]=P[L,L]` exactly. `R-P` is supported in rows `T` or columns `S`, so its rank is at most `2r`; therefore `rank R<=3r`, while `rank R[L,L]<=r`.
- **Spectral-to-volume — PASS.** If `V_{r+1}/V_r<kappa`, `||E||<=1/16`; after a global rank-`3r` loss, `m=4k-3>=4r+1` leaves `r+1` diagonal entries of `D` of size at least `1-epsilon`. They lie in `L`, where strict row diagonal dominance gives rank `r+1`, contradicting the restricted rank `<=r`.
- **Conditional rough-law steps — PASS.** The scalar square, definite pair and hyperbolic pair arguments are formulated as changes of variables/measure domination under conditioning on original coordinates. Exceptional critical levels are never substituted into arbitrary density versions; Tonelli with nonnegative test functions is sufficient.
- **Full versus truncated half potential — PASS.** `prop:pivot-H` controls only the truncated kernel. `prop:nine` adds at most one from the complement `|Q-a|>1`, yielding `<=601`; the main scalar-pivot density uses this full bound.

## Package audit

| Artifact | Status in this run | Reason |
|---|---|---|
| `README.md` | PASS WITH GAP | Read. It accurately states theorem scope/status, but advertises four supplementary root files that direct reads could not resolve. |
| `AUDIT.md` | READ; mathematical claims cross-checked independently | It is explicitly a self-audit, not independent validation. |
| `manuscript.tex` | PASS | All 790 lines read at the pinned source. |
| `SOURCE_MANIFEST.json` | GAP / unavailable | Direct path read returned not-found. |
| `proof_map.csv` | GAP / unavailable | Direct path read returned not-found. |
| `verify.py` | GAP / unavailable | Direct path read returned not-found. |
| `checks.json` | GAP / unavailable | Direct path read returned not-found. |
| Finite diagnostics listed in self-audit | UNCHECKED | Cannot rerun advertised checker from this root because checker/results are absent. They are not used as proof premises. |
| BCCT/RV bibliographic attribution | UNCHECKED | No external source verification performed in this run; theorem is self-contained with respect to specialized inputs. |

## Threshold reduction attempt from the B03 mechanism

I did not obtain a valid multiplicity improvement in this run. I did obtain a precise mechanism barrier, proved separately in the improvement artifact: the manuscript's fourth-power determinant bound is optimal **within the entire leverage-free Jensen/BL scheme that uses only uniform scalar Fourier `L^p` bounds for `p>=2`**. For every `q>=2`, the same argument gives

`|phi_Z(t)| <= det(I + q t^2 M^TM/(2 pi^2 e^2))^{-1/(4q)}`,

so an order-`k` crossing volume yields tail exponent only `k/(2q)<=k/4`. Thus order 4 remains at best `|t|^{-1}` in this method, exactly the nonintegrable endpoint. Higher even/Jensen powers make the exponent worse, not better. A `17 -> 13` theorem therefore needs a genuinely different endpoint receiver or additional structure, not more independent-copy powering.

The tempting `q<2` continuation would require dimension-free scalar Fourier control below `L^2` whenever a BL leverage `d_i` approaches one. Such a bound is not supplied by the manuscript hypotheses and cannot be silently assumed. I therefore do **not** claim a lower threshold.

## Review-status observations

Two separate complete PASS reports were visible during this run (`fleet03/B20`, commit `5b1f701981801423ac44b4d5db5d7fe1b2dacb9c`; `fleet03/B08`, commit `1cb1abecf56b73b8788d7e14a7bfcd6bcb75e963`). I used them only as cross-checks after my own source reading. I do not self-assign a new repository-wide `independently validated` label; that release-status transition belongs to the owner/release gate and should account for the local wording/package issues above.

## Final statuses

- Mathematical 17-eigenvalue theorem at pinned source: **PASS** in this audit.
- Fatal gap: **none found**.
- False theorem/lemma: **none found**.
- Projection-lemma wording: **PASS WITH CLARIFICATION**, no constant/theorem change.
- Advertised reproducibility package: **GAP**.
- Finite diagnostics and external attribution: **UNCHECKED** in this run.
- Multiplicity lower than 17: **NOT ESTABLISHED** here.
- Full three-eigenvalue conjecture: **OPEN / not claimed by this manuscript**.
- Global continuity: **not claimed/proved by this manuscript**; the no-pivot Fourier branch is continuous.
