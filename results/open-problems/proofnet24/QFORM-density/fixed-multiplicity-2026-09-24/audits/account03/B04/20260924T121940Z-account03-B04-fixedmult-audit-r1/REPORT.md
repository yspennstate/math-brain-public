SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T12:19:40Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924, with the B04 lens on the geometric Brascamp--Lieb heat-flow proof and all limiting steps, followed by the lowest rigorous multiplicity reduction supported by a complete product-Fourier compiler.

# account03/B04 — independent fixed-multiplicity manuscript audit

## Source and verdict

Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline manuscript:
- repository: `yspennstate/math-open-problems`
- initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- stated SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`

**Mathematical verdict on the 790-line baseline: PASS, with one nonfatal wording GAP and no fatal gap found.** This is one independent worker review, not formal verification and not a self-awarded release certificate. The unrestricted three-eigenvalue conjecture remains open.

Repository-package verdict: **GAP (nonmathematical/reproducibility)**. At the root observed in this run, `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/` were present, while the README/AUDIT referenced `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` that were not present at that root. This does not invalidate the self-contained symbolic manuscript, but the repository package was incomplete relative to its own reproducibility description.

## End-to-end audit map

Every source interval below was read from the pinned blob, and every displayed equation/proof step in the interval was checked. Labels are included so that minor later line drift does not obscure the scope.

| Source lines | Material | Verdict | Reasoning / issue |
|---|---|---|---|
| 1--79 | abstract, definitions, `thm:main`, normalization and architecture | PASS | Quantifiers, singular-value formulation, affine terms, and the `K=s=1` normalization are consistent with the final rescaling. |
| 80--130 | Gaussian regularization, Plancherel/inversion, power envelope | PASS | Fourier normalization is internally consistent; approximate-identity and weak-limit steps justify the density conclusion. |
| 131--166 | `lem:riesz` negative-half-potential formula | PASS | Gamma representation, Gaussian inversion, Tonelli, and the `|t|^{-1/2}` constant all check. |
| 167--206 | singular-value perturbation, Schur spectral count, diagonal dominance | PASS | Nonsymmetric singular-value use is legitimate. The inverse-compression argument yields the stated loss of at most the pivot size. |
| 207--260 | `thm:bl` geometric rank-one Brascamp--Lieb heat flow | PASS | Independently reconstructed in detail below. No hidden smoothness assumption survives the truncation/heat-flow limit. |
| 261--315 | product projection densities; integrated scalar Fourier powers | PASS with wording GAP | The projection theorem is correct. After zero-leverage rows are dropped, the displayed text should read `sum_{b_i>0}(1-b_i) <= d`, not equality with `d`. The final cap `e^{d/2}` remains valid. Scalar Fourier powers then follow. |
| 316--390 | decoupling and regularized crossing determinant | PASS | Difference coordinates retain independent cap-one densities; graph-BL weights form an exact frame; the `alpha=(2 pi e)^2` choice cancels the entropy/Fourier factors and gives exponent `-1/8`. |
| 391--420 | determinant expansion and order-3/order-5 volume envelopes | PASS | Cauchy--Binet and the resulting `5e Z_5^{-1/10}` density / order-3 half-potential constants check. |
| 421--451 | scalar square and definite-pair profiles | PASS | Changes of variables are measure-dominating statements in original coordinates; no rotated-coordinate independence is used. |
| 452--520 | hyperbolic pair and quarter-power concentration | PASS | Hyperbolic Jacobian, both exponential tails, middle interval, AM--GM reduction in `Lambda`, signed-cut construction, Gaussian regularization, and layer-cake logarithmic bound check. |
| 521--585 | disjoint volumes, `lem:sampling`, `lem:completion` | PASS | Bordered determinant identity and the `(r+1)^2` overcount are correct; singular seeds only make the sampling relation an inequality. `rank R<=3r` and `rank R[L,L]<=r` follow from the actual support decomposition. |
| 586--650 | `prop:volume`, random coordinate cut, no-pivot consequences | PASS | The key count is `m-3r >= r+1`; forced large diagonal entries lie in `L`; exact diagonal-dominance slack is positive. The cut probability is `4^{-k}`. |
| 651--690 | two singular kernels | PASS | Near/far split for `J(d)` and interval-superlevel argument for the logarithmic kernel are valid. |
| 691--735 | pivot half potential and nine-eigenvalue half-potential proposition | PASS | Scalar, definite-pair and indefinite-pair alternatives exhaust pivots; truncated-to-full half-potential costs at most one. |
| 736--770 | proof of `thm:main` | PASS | No-pivot `s_17`, scalar-pivot Schur `s_16`, pair-pivot Schur `s_15`, and all constants are used within their stated scopes. |
| 771--790 | scaling, threshold accounting, limitations | PASS | `Y=KX` gives cap-one coordinates and `Q=(s/K^2)\widetilde Q`; final factor is `K^2/s`. Continuity is correctly not claimed in the pivot branches. |

## B04 lens: independent reconstruction of geometric Brascamp--Lieb

For `f_i(t,.)=g_t*h_i`, set `v_i=partial_s log f_i` and
`F(t,x)=prod_i f_i(t,u_i.x)^{c_i}`. Since the heat kernel convention satisfies `partial_t f_i=partial_s^2 f_i`, direct differentiation gives

`(partial_t F-Delta F)/F = sum_i c_i v_i^2 - |sum_i c_i u_i v_i|^2`.

The frame identity `sum_i c_i u_i u_i^T=I` says that the matrix with columns `sqrt(c_i)u_i` is a coisometry, so the final expression is nonnegative. For compactly supported bounded inputs and time in a compact subset of `(0,infinity)`, Gaussian tails dominate the product and its derivatives, hence integration by parts gives monotonicity of `int F(t,x)dx`.

Taking traces of the frame identity gives `sum c_i=d`. Under `x=sqrt(t) z`, each heat convolution has the asymptotic

`sqrt(t) f_i(t,sqrt(t) u_i.z) -> (4pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`.

The frame identity also gives `sum c_i(u_i.z)^2=|z|^2`, so the limiting integral is exactly `prod M_i^{c_i}`. Compact support supplies a uniform Gaussian majorant for `t>=1`. At `t downarrow 0`, each `u_i.x` is a Lebesgue point for almost every `x`; preimages of one-dimensional null sets under a nonzero linear functional are null by rotation/Fubini. Fatou therefore gives the inequality. Monotone truncation removes boundedness/support assumptions. I find no missing limiting step here.

## Nonfatal projection wording gap

In `lem:projection`, put `b_i=|w_i|^2`. The proof correctly drops factors with `b_i=0`, and for the remaining rows obtains

`log p(y) <= (1/2) sum_{b_i>0}[-b_i log b_i]
          <= (1/2) sum_{b_i>0}(1-b_i)`.

The manuscript then writes the last sum as `d`. That equality need not hold after the zero-`b_i` rows were dropped. The correct statement is

`sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`.

Thus the claimed bound `p(y)<=e^{d/2}` is unchanged. Status: **GAP in wording only; theorem remains PASS**.

## Algebraic threshold check

The key no-pivot interpolation argument was re-derived. If the sampled seed has order `r`, then `rank R<=3r` globally but `rank R[L,L]<=r`. From `s_m(A)>=1` and `||E||<=epsilon`, the diagonal part must have at least `m-3r` entries of modulus at least `1-epsilon`. Since it vanishes on the seed, the contradiction needs `m-3r>=r+1`, i.e. `m>=4r+1`. With `r<=k-1` this gives `m=4k-3`. The forced `(r+1)x(r+1)` block is strictly diagonally dominant because

`371/400 - 4(1/7+1/16) = 297/2800 >0`.

This confirms the manuscript's 9 and 17 structural counts. It also explains why lowering the density theorem requires a stronger analytic endpoint at lower crossing order, rather than merely relabeling the existing rank argument.

## Improvement generated by this audit

A separate immutable improvement from this same run gives a self-contained product-Fourier compiler, using only analytic inputs reproved in the manuscript plus an explicit weighted-subset argument, and combines it with the already-audited structural proposition to obtain a **candidate nine-eigenvalue density theorem** with bound `6010 K^2/s`. It is saved under the corresponding `improvements/account03/B04/...` run directory. It does not alter the pinned 17-eigenvalue baseline and needs independent end-to-end review before promotion.

Execution status: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval/writeback occurred; no authenticated native brain receiver was used. No scheduler state, task identity, notification/email setting, public release, paid API/model, permission, or cross-account authentication was changed.
