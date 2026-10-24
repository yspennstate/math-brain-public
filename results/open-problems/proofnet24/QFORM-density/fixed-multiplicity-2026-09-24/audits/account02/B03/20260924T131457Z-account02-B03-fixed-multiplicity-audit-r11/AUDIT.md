# account02/B03 independent fixed-multiplicity audit — 2026-09-24 r11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and verdict

- Repository/branch resolved at audit start: `yspennstate/math-open-problems` / `master` at `126eb0e75770fb9e814092f610e1e67ad0412afe`; final pre-write refresh reached `624d810437d72a71987d64578bfd559e40f93743`.
- Pinned baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- `manuscript.tex` git blob at both refreshed master states: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Package-declared SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Source size/range: 47,883 bytes, 790 lines.

**Mathematical verdict:** PASS for the stated 17-singular-value theorem. I found no fatal mathematical gap in the 790-line baseline. This is one independent worker audit, not formal verification or a release certificate. The unrestricted three-eigenvalue QFORM conjecture remains OPEN.

**Threshold verdict:** no multiplicity reduction is proved in this run. The current determinant/decoupling route gives order-4 Fourier decay exactly `|t|^{-1}`, a logarithmically non-integrable endpoint, so the manuscript's order-5 receiver cannot simply be replaced by order 4. A genuine `17 -> 13` theorem needs a new endpoint gain, a stronger structural count retaining order 5, or a different complete density receiver with constants and a closed dependency map.

## Package audit

| Item | Status | Reason / impact |
|---|---|---|
| `README.md` | PASS | Current candidate, source pins, scope and limitations agree with the manuscript. |
| `SOURCE_MANIFEST.json` | PASS | Present now; source blob/bytes/lines/hash agree with the current unchanged manuscript. |
| `manuscript.tex` | PASS | Read lines 1–790 end to end and checked every stated lemma/proof dependency below. |
| `AUDIT.md` | PASS AS SELF-REPORT / UNCHECKED HISTORICAL COUNTS | Correctly labels itself an authoring-agent self-audit. Its older finite-test counts are a different historical suite and were not reproduced here. No mathematical dependency. |
| `proof_map.csv` | PASS | Statement/proof ranges agree with the source labels inspected. |
| `verify.py` | PASS AS FINITE CHECKER | Logic matches the algebraic identities it claims to test. I independently re-ran the same exact/numerical algorithm and obtained `(534,18,9,240,30,297/2800)` for seeds, volume cases, strict cases, Schur cases, graph cases, and slack. This is not a universal proof. |
| `checks.json` | PASS | Matches that independent re-run: 534 exact interpolation seeds, 18 volume cases, 9 strict cases, 240 Schur threshold cases, 30 graph-weight cases, slack `297/2800`. |
| compiled PDF/render statement | UNCHECKED | Binary PDF is explicitly not stored in this GitHub root. This has no impact on the analytic theorem in `manuscript.tex`. |

A previous B03 audit had reported the support files missing at an earlier master snapshot. That packaging/reproducibility gap is repaired at the current source: all requested support files are now present. The baseline manuscript blob itself did not change.

## End-to-end mathematical audit

### Lines 1–82: definitions, theorem quantifiers, architecture — PASS

The theorem quantifies over arbitrary dimension, arbitrary independent real coordinate laws with density caps `<=K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, all signatures and remaining spectrum, and assumes only `s_17(A)>=s>0`. The normalized parameters are exactly `eta=1/100`, `kappa=1/80^2`. The later scaling `Y=KX`, `A/s` correctly converts the normalized `K=s=1` result back to `10^4 K^2/s`. No support, moment, smoothness, log-concavity, identical-law, or diagonal-basis assumption appears.

### Lines 84–160: Fourier normalization, inversion, negative half moment — PASS

With `hat f(t)=int exp(itx)f(x)dx`, Plancherel has factor `2pi`, Fourier inversion has factor `1/(2pi)`, and the Gaussian regularization identity is consistent. The Riesz calculation yields

`E|Z-a|^{-1/2} <= (2pi)^(-1/2) int |t|^(-1/2)|phi_Z(t)|dt`.

For the envelope `min(1,(u/|t|)^(3/4))`, the weighted integral is exactly `12 sqrt(u)`, producing the stated `12 sqrt(u/(2pi))`. Tonelli is applied only to nonnegative majorants; no hidden moment assumption is needed.

### Lines 161–217: singular values, Schur counts, diagonal dominance — PASS

The nonsymmetric singular-value perturbation and rank inequalities follow from the approximation-number characterization. For an invertible principal pivot, the Schur complement is the complementary block of `A^{-1}` after inversion; positive and negative eigenvalue counts are controlled separately by principal compression. In the singular case the `A+epsilon I` argument with threshold `t-|epsilon|` is adequate; continuity of ordered eigenvalue moduli closes the limit. Strict row diagonal dominance is used correctly for a not-necessarily-symmetric matrix.

### Lines 221–255: geometric rank-one Brascamp--Lieb — PASS

The heat-flow computation has the correct sign. The frame identity makes the column map a contraction; compact-support Gaussian tails justify differentiation/integration by parts; the large-time limit has the right normalization because `sum c_i=d`; the small-time Fatou and monotone truncation steps handle rough nonnegative integrable inputs. No probabilistic independence is introduced here.

### Lines 258–301: product projections and scalar Fourier powers — PASS

The orthogonal completion is used only for a deterministic change of variables in the density integral. It never asserts that the rotated coordinates are independent. The row weights `b_i=1-|U^T e_i|^2` form the required geometric frame and give `||p_{U^T X}||_infty <= e^(d/2)`.

For `p>=2`, putting `m=floor(p/2)>=p/4` and using `|hat f|<=1` gives `int|hat f|^p <= int|hat f|^(2m)`. The latter is the characteristic function of a sum of **independent copies of differences**. Applying the scalar projection bound to the `2m` original signed coordinates gives exactly `2pi sqrt(2e)/sqrt(p)`.

### Lines 303–324: decoupling, copies, conditional independence — PASS

This is the primary B03 check. In

`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`, 

one first integrates in the genuine original block `X_J`, then applies Cauchy--Schwarz in `X_I`. Expanding the square introduces an independent whole copy `X'_J`. The phase `G(X_J)-G(X'_J)` is retained until an absolute value is taken; it is **not** treated as a function of `D=X_J-X'_J`, and it is never asserted independent of `D`.

After that absolute value, integration in the mutually independent original coordinates `X_i`, `i in I`, gives the product `prod_i |hat f_i(2t(MD)_i)|`. The coordinates `D_j` are independent because the coordinate pairs `(X_j,X'_j)` are independent across `j`; each difference density is `f_j * tilde f_j <=1`. The fourth-power estimate is exactly Jensen on the nonnegative product: `|phi|^2<=E P` implies `|phi|^4 <= (EP)^2 <= E(P^2)`.

**Counterexample stress test:** the tempting stronger assertion that `X-X'` is independent of `X+X'` is FALSE in the allowed class. For iid `Uniform[-1/2,1/2]`, the pair `(D,S)=(X-X',X+X')` has diamond support `|D|+|S|<=1`, so it cannot be independent. The manuscript never uses this false assertion.

### Lines 326–400: regularized determinant and exponent transfer — PASS

The graph/frame weights are `c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`, with `sum d_i=sum(1-c_j)`. The Brascamp--Lieb factors have the stated one-dimensional Jacobians. Substituting the scalar Fourier-power bound with `p=2/d_i` cancels the `d_i` powers. With `alpha=(2pi e)^2`, the exponential `c_j` loss cancels exactly, leaving a fourth-power majorant with determinant exponent `-1/2`; the fourth root gives the theorem's determinant exponent `-1/8`.

Retaining an order-`k` term in `det(I+zM^TM)` gives `|phi(t)| <= min(1,(u_k/|t|)^(k/4))`. Therefore:
- `k=5`: exponent `5/4>1`, so direct `L^1_t` inversion works and gives `5e Z_5^{-1/10}`.
- `k=3`: exponent `3/4`; multiplying by the half-Riesz weight gives tail exponent `5/4>1`, so the negative-half potential is finite.
- `k=4`: exponent exactly `1`; direct `L^1_t` inversion has a logarithmic divergence. This is a **GAP FOR THRESHOLD REDUCTION ONLY**, not a gap in the 17-direction theorem.

### Lines 404–525: scalar/definite/hyperbolic pivots and quarter concentration — PASS

All conditional arguments condition only on complementary **original coordinates**. The retained original coordinate(s) keep their genuine density cap and mutual independence. Completing a square only translates an original coordinate by a deterministic value after conditioning. Orthogonal diagonalization in the definite and hyperbolic pair arguments is used only to parametrize deterministic integrals; it does not create an independence claim.

The hyperbolic Jacobian `1/(2 sqrt(D))`, tail monotonicity estimates, and logarithmic envelope are consistent. The critical level is handled through measure domination/nonnegative test functions, so no exceptional-slice value of a rough density is selected. The quarter-concentration argument uses either a genuine scalar coordinate pivot or a deterministic sign partition exposing a cross block; its Fourier smoothing exponent transfers correctly to the `rho^(1/4)` small-ball bound and then to the logarithmic potential.

### Lines 528–645: disjoint-minor skeleton, nonsymmetric interpolation, spectral-to-volume, random cut — PASS

The sampled interpolation `P=A_{.,T}B^{-1}A_{S,.}` may be nonsymmetric. The bordered determinant identity is exact after squaring. Singular seeds can have nonsingular extensions, hence the aggregate step is correctly an inequality rather than an equality.

In `A=D+R+E`, `D` is zero on the seed, `E` has zero diagonal, `rank(R)<=3r` globally, while `R[L,L]=P[L,L]` has rank at most `r`. The support argument for `R-P` justifies the two extra rank-`r` pieces. The proof correctly uses singular values for the nonsymmetric perturbation `A-E`.

The count `m=4k-3` is sharp for this argument: since the bad ratio may occur at `r=k-1`, one needs `m>=4r+1` to force `r+1` large diagonal entries outside the seed. The diagonal-dominance contradiction uses the restricted rank, not the global rank. Random cutting captures each ordered disjoint seed with probability exactly `4^{-k}`. Constants give `k=3` half potential `<200` and `k=5` density `<=800e<2400`.

### Lines 647–724: kernels, pivot half potentials, nine-direction bridge — PASS

The distinction between truncated and full half potentials is maintained. Scalar pivots use the square-root profile against the Schur-complement output; quarter concentration first excludes atoms, then the kernel/log potential bound is legal. Definite and indefinite pairs are conditioned on their original complement and averaged. Proposition `nine` uses the pivot result for the truncated part and adds at most one from the tail `|Q-a|>1`, while the no-pivot branch already controls the full potential. Thus the main scalar-pivot branch legitimately uses `<=601`, not merely the truncated `<=600`.

### Lines 726–749: main theorem — PASS

No-pivot: order 5 yields density `<=2400`. Scalar pivot: Schur count loses one of 17 and therefore leaves at least 16, enough for Proposition `nine`; the profile gives `10*601=6010`. Definite pair: uniform conditional density `<=10pi`. Indefinite pair: Schur count loses two; one surviving spectral direction is sufficient for the logarithmic-potential bound. Averaging is through measure domination/Tonelli, so the conditioning-dependent critical value causes no independence or exceptional-slice problem. Final `K,s` scaling is correct.

### Lines 751–790: threshold accounting, limitations, references — PASS / UNCHECKED attribution only

The threshold-accounting paragraph correctly distinguishes order-5 density from order-3 half-Riesz. The limitation explicitly says the proof does not give `s_3`. The no-continuity/no-independence-shortcut remark matches the actual argument. Bibliographic entries are attribution only and are **UNCHECKED for historical priority** in this run; no theorem depends on them.

## Hypothesis-invocation map

Every substantive invocation was checked against its stated hypotheses:

- `lem:fourier` is used with either an explicitly integrable envelope or Gaussian damping.
- `lem:projection` is used only on genuine independent coordinate collections, never on a rotated vector asserted independent.
- `lem:scalar-fourier` is applied to genuine one-dimensional coordinate densities or their independent-copy differences.
- `lem:decoupling` is invoked only after a literal original-coordinate partition.
- `thm:determinant` retains arbitrary same-bank functions `F,G`; no hidden separability is imposed.
- `lem:schur` is invoked only for invertible scalar or two-coordinate principal pivots.
- pivot density/profile lemmas are applied conditionally on disjoint original coordinates.
- `prop:nine` is used only when the Schur complement retains at least nine eigenvalues of modulus `>=1`.

## Reproducibility repair and current-master note

The previously missing `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are now present and internally consistent, so the prior package reproducibility GAP is closed. Current master also contains a separate account04/B12 constant-only improvement, derived from the same baseline, giving `2010+1200 log 16 < 5338` in place of `10000`; it does not modify `manuscript.tex` and does not reduce the eigenvalue multiplicity. I do not count it as a threshold improvement by this B03 run.

## Next obligation

A complete reduction below 17 must overcome the order-4 `|t|^{-1}` endpoint or improve the structural count while preserving an integrable receiver. Any replacement must retain arbitrary affine terms, arbitrary rough product laws, arbitrary signature/dimension/remaining spectrum, give explicit constants, and close every dependency. No such complete replacement was found here, so no improvement artifact is created.
