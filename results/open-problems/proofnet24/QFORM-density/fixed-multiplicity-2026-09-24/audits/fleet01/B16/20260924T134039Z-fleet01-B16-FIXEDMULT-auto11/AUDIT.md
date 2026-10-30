# fleet01/B16 independent full audit — 2026-09-24T13:40:39Z

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

## Source pin and method

I first read the fresh control files and then reconstructed the complete mathematical proof from the pinned manuscript before consulting peer improvement verdicts. The current repository moved during the run from `b8a78d6c67ec84e8f54d57c515561874da9db9ba` to `ea20a6ed5d41f63146d7763174e87effa996d336`, but `manuscript.tex` remained byte-identical to the baseline source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`: git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines.

I read all 790 source lines and the root `README.md`, `DELIVERY_STATUS.md`, `AUDIT.md`, `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json`. The finite checker reports 534 exact interpolation seeds, 18 volume comparisons, 240 numerical Schur threshold cases and 30 graph-weight cases; I treat these as diagnostics only, not proof.

## Baseline verdict

**PASS** for the written 17-eigenvalue theorem. I found no mathematical GAP or FALSE statement in the pinned manuscript. The exact theorem audited is

\[
s_{17}(A)\ge s>0,\quad 0\le f_i\le K
\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s,
\]

for arbitrary real symmetric `A`, arbitrary affine `b,c`, arbitrary dimension/signature/remaining spectrum, and independent arbitrary real coordinate densities. This audit does not imply the unrestricted three-eigenvalue conjecture.

## Continuous source-range ledger

| source lines | status | independent reconstruction |
|---|---|---|
| 1–46 | PASS | Setup/abstract preserve the stated rough-law, arbitrary-signature and affine quantifiers. No hidden support, moment, smoothness, or continuity hypothesis is introduced. |
| 47–61 | PASS | `thm:main` is exactly the 17-direction statement; `cor:33` follows from monotonicity of ordered singular values. |
| 62–90 | PASS | `eta=1/100`, `kappa=1/80^2`; pivot/no-pivot architecture is exhaustive. Auxiliary rotations are deterministic integral changes, not independence assertions. |
| 91–120 | PASS | Gaussian regularization gives Plancherel at the manuscript convention; `phi in L1` gives a bounded continuous density. Approximate-identity limiting arguments are justified in `L2`/weak convergence. |
| 121–130 | PASS | The power-envelope integral is `2ap/(p-1)` and inversion gives `ap/[pi(p-1)]`. |
| 131–160 | PASS | Gamma/Tonelli derivation of the negative-half Riesz bound has coefficient `1/sqrt(2pi)`; the `3/4` envelope contributes exactly `12 sqrt u`. |
| 161–181 | PASS | Singular-value perturbation and rank shift follow from the best low-rank approximation formula and do not require symmetry. |
| 182–207 | PASS | Schur spectral count is valid: for invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative interlacing give the absolute-value count. The `A+epsilon I` moving-threshold limit correctly handles singular `A`. |
| 208–217 | PASS | Strict row diagonal dominance gives invertibility also for nonsymmetric matrices. |
| 218–255 | PASS | Heat-flow Brascamp–Lieb sign is `sum c_i v_i^2-|sum c_i u_i v_i|^2>=0` from the frame contraction; the large-time Gaussian normalization uses `sum c_i=d`; rough inputs follow by Lebesgue points, Fatou, truncation and monotone convergence. |
| 256–282 | PASS | Product-projection density bound `e^{d/2}` is valid without post-rotation independence. Harmless wording note: after zero-`b_i` factors are dropped, `sum(1-b_i)=d` is literally over all original rows; over retained rows only `<=d` is needed. |
| 283–301 | PASS | Scalar Fourier-power estimate is valid: `m=floor(p/2)>=p/4`; the even power is the characteristic function of a sum of independent differences; the projection bound at zero is legitimate after inversion gives a continuous version. |
| 302–324 | PASS | Two/four-power decoupling uses one independent copy of the literal product bank; difference coordinates remain independent cap-one variables. No moment hypothesis is used. |
| 325–373 | PASS | Regularized determinant theorem checks completely: frame weights `c_j,d_i`, graph Jacobian, scalar Fourier powers and entropy factor cancel at `alpha=(2pi e)^2`; fourth root gives determinant exponent `-1/8` and scale `t^2/(pi^2e^2)`. |
| 374–400 | PASS | Cauchy–Binet crossing-volume expansion is exact. Order 5 gives `|t|^{-5/4}` and an `L1` Fourier density bound; order 3 is used only with the extra `|t|^{-1/2` Riesz weight. |
| 401–414 | PASS | Scalar-square inverse branches and interval preimage estimate are correct. The conditional profile is a measure-domination/Tonelli statement, not an independence claim. |
| 415–434 | PASS | Definite two-coordinate coarea gives `pi M/sqrt(|det B|)` after a deterministic orthogonal change; only the joint cap is used. |
| 435–482 | PASS | Hyperbolic Jacobian is `1/(2sqrt D)`; the two tails are paid in literal original coordinates by cap one plus mass one; middle length yields the logarithm; `Lambda>=2/sqrt D` produces the stated `16sqrt D/|z-v|`. Exceptional critical slices are handled in nonnegative-test-function form. |
| 483–525 | PASS | Quarter-power small-ball theorem: diagonal branch is direct; otherwise the sign cut produces a physical cross block of norm at least `L/4`; determinant decay is `|t|^{-1/4}`; the Gaussian integral coefficient is `<16`. Layer cake gives `4+4 log16` and excludes atoms. |
| 526–544 | PASS | No-pivot entry estimate gives `|a_ij|^2<eta^2+eta<2eta`, hence `|a_ij|<1/7`. |
| 545–564 | PASS | Volume sampling: bordered determinant identity is exact for nonsingular seeds; singular deleted seeds can have nonsingular extensions, so the manuscript correctly uses `<=`, not equality. Interpolant may be nonsymmetric and exactly matches rows `S` and columns `T`. |
| 565–580 | PASS | Completion has `E` only on off-diagonal `LxL`, diagonal `D` vanishing on the seed, `rank R<=3r`, while the crucial restriction satisfies `R_LL=P_LL`, `rank R_LL<=r`. |
| 581–619 | PASS | Spectral-to-volume contradiction is correct. For a bad ratio, `epsilon<=(r+1)/80<=1/16`; global rank subtraction forces `r+1` large diagonal entries in `L`; on the selected block diagonal magnitude is at least `371/400` while every row off-diagonal sum is `<23/28`; strict diagonal dominance contradicts restricted rank `<=r`. |
| 620–630 | PASS | Fair physical cut retains each ordered disjoint `k`-minor with probability `4^{-k}`. |
| 631–645 | PASS | `Z_k^{-1/(2k)}<=160`; constants are `12 sqrt(80e)<200` for the order-three full half potential and `800e<2400` for the order-five density. |
| 646–674 | PASS | Both singular kernels are correctly bounded. Simultaneous square-root singularities are integrable with logarithmic growth; interval-overlap rearrangement yields the uniform log-kernel bound `8`. |
| 675–714 | PASS | Pivot truncated-half-potential proposition is correct in all scalar/definite/indefinite branches. Exact scalar-branch value is `200+120 log16<533`; definite branch `<160`; indefinite branch `<444`, hence the displayed common `600`. |
| 715–724 | PASS | Under `s_9>=1`, pivot gives truncated half potential at most 600 and no-pivot gives the stronger full half potential `<200`; the tail outside distance one costs at most one. |
| 725–749 | PASS | Main split closes: no pivot `<2400`; scalar pivot `6010`; definite pair `<40`; indefinite pair `<251`. Schur counts are more than sufficient. Scaling with `Y=KX` gives exactly `K^2/s`. |
| 750–790 | PASS | Threshold accounting and limitations accurately separate density versus half-potential conclusions and make no full-three or global-continuity claim. |

## Degenerate/measure-theoretic cases explicitly checked

Zero crossing ranks are excluded exactly where a positive crossing volume is assumed; zero BL weights are dropped before reciprocal exponents are formed; singular `A` in the Schur lemma is covered by the moving-threshold regularization; atoms are excluded before logarithmic layer-cake use; critical hyperbolic/square levels are not assigned common pointwise conditional versions; all conditioning remains on literal independent source coordinates. The nonsymmetric interpolation matrices are used only for rank/singular-value algebra.

## UNCHECKED

No mathematical source range of `manuscript.tex` is left UNCHECKED. Non-proof metadata left UNCHECKED in this run: (i) comprehensive literature priority/novelty, and (ii) the conversation-only compiled PDF binary/render because that binary is not stored in this repository root. The source build claim is not needed for the theorem.

## Independent conclusion

Baseline manuscript classification: **PASS / no fatal gap found**. This is an independent mathematical review, not formal verification or journal peer review. The unrestricted three-eigenvalue theorem remains open.
