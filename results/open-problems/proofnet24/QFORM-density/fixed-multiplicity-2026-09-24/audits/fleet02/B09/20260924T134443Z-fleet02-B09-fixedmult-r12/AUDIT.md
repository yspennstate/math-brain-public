# fleet02/B09 r12 — independent full audit, with spectral-rank stress test

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Run: `20260924T134443Z-fleet02-B09-fixedmult-r12`.

Mathematical source pin: initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 790 lines / 47,883 bytes. The full package was read from master snapshot `4cff3d69361219127ce00e43434fa1b50e6bfd3d`; a later master refresh at `30025107d98a7aae3a0d1abda74424bc68e45ced` still returned exactly the same manuscript blob.

## Verdict

**PASS for the complete mathematical manuscript under this independent textual audit.** I found no mathematical GAP or FALSE statement in the 17-eigenvalue proof. In particular, the B09-sensitive nonsymmetric perturbation / global-rank / restricted-rank / diagonal-dominance chain is correct and the index `4r+1` is used exactly where claimed.

This is one worker review, not formal verification and not an independent-validation certificate. The unrestricted three-eigenvalue conjecture is not solved here.

No multiplicity reduction is claimed. A new exact finite family, recorded separately in this run's improvement artifact, shows that the rank-perturbation count itself is sharp: `4r` large singular values can coexist with `rank R=3r`, `rank R[L,L]=r`, and only `r` large diagonal entries of `D`. Thus `17 -> 16` cannot follow merely by tightening the existing rank arithmetic; any complete 16-eigenvalue replacement proof must use additional no-pivot/interpolation geometry or a new analytic receiver.

## End-to-end line audit

Statuses below concern the pinned 790-line `manuscript.tex`.

| Source lines / label | Status | Independent check and impact |
|---|---|---|
| 1–46, front matter / abstract / conventions | PASS | The abstract matches the actual theorem and makes no continuity or unrestricted-three-eigenvalue claim. Singular values of symmetric matrices are correctly identified with ordered absolute eigenvalues. |
| 47–61, `thm:main`, `cor:33` | PASS | Quantifiers are unrestricted in dimension, signature, remaining spectrum, affine terms and rough product laws. The conclusion is essential boundedness, not continuity. The corollary follows from `s_17 >= s_33`. |
| 63–89, parameters and architecture | PASS | `eta=1/100`, `kappa=1/80^2`; the two counts `9=4*3-3`, `17=4*5-3` match the later algebra and Fourier exponents. |
| 91–120, `lem:fourier` | PASS | Plancherel normalization, Gaussian regularization, approximate identity, inversion and Gaussian identity are consistent with `fhat(t)=int e^{itx}f(x) dx`. |
| 122–130, `lem:envelope` | PASS | `int min(1,(a/|t|)^p)=2ap/(p-1)`, hence density bound `ap/[pi(p-1)]`. |
| 132–160, `lem:riesz` | PASS | Gamma/Tonelli calculation gives the exact prefactor `1/sqrt(2pi)` and the weighted envelope integral `12 sqrt(u)`. No hidden moment assumption. |
| 169–181, `lem:rank` | PASS | Best low-rank approximation gives both singular-value Lipschitz continuity and `s_{j+q}(D+R)<=s_j(D)` for arbitrary nonsymmetric matrices. The shift by exactly `q` is necessary; see the improvement artifact. |
| 183–207, `lem:schur` | PASS | For invertible ambient `A`, the complementary principal block of `A^{-1}` is `S^{-1}`; positive and negative variational counts give `N_S(t)>=N_A(t)-k`. In the singular limit, if `q=N_A(t)-k`, the moving threshold gives `s_q(S_epsilon)>=t-|epsilon|`; continuity yields `s_q(S)>=t`. The terse limit is valid. |
| 209–217, `lem:dd` | PASS | Standard max-coordinate proof works without symmetry. Strictness is essential: equality permits singular examples such as `[[1,-1],[-1,1]]`. |
| 221–255, `thm:bl` | PASS | Heat-flow derivative has the correct sign from the geometric frame identity. Gaussian domination justifies differentiation/integration by parts, the large-time limit gives the product of masses, and Fatou plus monotone truncation covers rough nonnegative integrable factors. |
| 258–282, `lem:projection` | PASS | Orthogonal completion is used only as a deterministic change of variables. The BL exponents are `b_i=1-|U^T e_i|^2`; `-b log b <=1-b` gives `e^{d/2}`. No rotated-coordinate independence is asserted. |
| 284–301, `lem:scalar-fourier` | PASS | With `m=floor(p/2)>=p/4`, `|fhat|^p<=|fhat|^{2m}`; inversion at zero plus the scalar projection bound gives `2pi sqrt(2e)/sqrt(p)`. Integrability follows already from the `L^2` bound. |
| 302–324, cross-form setup / `lem:decoupling` | PASS | Conditioning and Cauchy–Schwarz are on original independent banks. Expanding with an independent copy gives the stated product Fourier factors; Jensen produces the fourth-power version. Difference coordinates remain independent with cap-one densities. |
| 326–373, `thm:determinant` | PASS | The regularized frame, BL Jacobian scales, `c_j,d_i` trace identity and scalar Fourier powers cancel exactly for `alpha=(2pi e)^2`. Taking fourth roots gives `det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}`. |
| 375–400, crossing volumes / `cor:vol-fourier` | PASS | Cauchy–Binet expansion is correct. Retaining the order-`k` term gives exponent `k/4`; `k=5` yields `5e Z_5^{-1/10}`, while `k=3` is used only with the negative-half-moment weight. |
| 404–414, `lem:square` | PASS | Two inverse branches give the density profile and the inverse-image length estimate. |
| 416–434, scalar profile / `lem:definite` | PASS | Conditional domination is a Tonelli statement, not independence of the square and remainder. The two-dimensional polar Jacobian is `1/(2 sqrt(det B))`, giving `pi M/sqrt(|det B|)`. |
| 437–482, `lem:hyperbola` | PASS | Hyperbolic parametrization and Jacobian are correct. The tail cutoff `3 log 2/4` is sufficient; mass-one/cap-one tails give `3 log 2`; the middle length and `Lambda>=2/sqrt(D)` produce the displayed logarithmic envelope. Exceptional critical levels are handled measure-theoretically. |
| 485–525, `lem:quarter` | PASS | Diagonal case is immediate from the square profile. The random-sign cut forces a cross block of norm at least `L/4`; the determinant theorem, Gaussian smoothing and `Gamma(3/8)` estimate give the quarter-power bound. Layer cake gives `L_0=4+4 log 16`. |
| 528–544, `def:pivot-volume`, no-pivot entry bound | PASS | Ordered disjoint volumes are unambiguous. No pivot implies `|a_ij|^2<eta+eta^2`, hence the convenient strict bound `<1/7`. |
| 545–564, `lem:sampling` | PASS | The bordered determinant identity is exact. Squaring removes sorting signs. An ordered disjoint `(r+1)` pair has at most `(r+1)^2` parents; singular seeds may have nonsingular extensions, correctly making the aggregate relation an inequality, not an equality. |
| 566–580, `lem:completion` | PASS | `E` is only the off-diagonal `LxL` residual, `D` is diagonal and vanishes on the seed, and `R[L,L]=P[L,L]`. Since `R-P` is supported in rows `T` or columns `S`, `rank R<=3r`; restricted rank is `<=r`. Symmetry of the auxiliaries is neither asserted nor used. |
| 582–619, `prop:volume` | PASS | For a bad ratio, `epsilon<= (r+1)/80<=1/16`. With `m=4k-3`, perturbation gives `s_m(D+R)>=1-epsilon`; global rank gives `s_{m-3r}(D)>=1-epsilon`. Since `m>=4r+1`, there are `r+1` large diagonal entries, all in `L`. On them `|R_ii|>=371/400` and `|R_ij|<23/112`; for `r<=4` the row sum is `<23/28`, with exact slack `297/2800`. This contradicts restricted rank `<=r`. The `r=0` norm contradiction is also correct. |
| 621–645, `lem:cut`, `cor:no-pivot` | PASS | Each ordered disjoint pair survives the fair cut with probability `4^{-k}`. The volume lower bound gives `Z_k^{-1/(2k)}<=160`; constants `<200` and `<2400` follow. |
| 647–674, truncated potential / `lem:kernels` | PASS | The two singular integrals are bounded as stated. The logarithmic overlap is maximized by aligning interval superlevel sets. |
| 676–714, `prop:pivot-H` | PASS | Scalar-pivot Schur count supplies a nonzero spectral direction for the log potential. Definite and indefinite pair estimates are conditioned only on original coordinates. Constants and the scalar maximum `sup D^{-1/2} log_+ D=2/e` are correct. |
| 716–724, `prop:nine` | PASS | Pivot and no-pivot alternatives exhaust the matrix. The tail of the full half-potential costs at most one, giving `601`. |
| 726–749, proof of `thm:main` | PASS | No-pivot branch `<2400`; scalar pivot leaves at least 16 large Schur directions and uses the nine-direction bound to get `6010`; definite pair `<40`; indefinite pair leaves at least 15 large directions and gives `<251`. Scaling `Y=KX`, `Q=(s/K^2) Qtilde` yields `10000 K^2/s`. |
| 751–776, threshold accounting / limitations | PASS | The text accurately distinguishes global `3r` from restricted `r`, and order-five density from order-three half-potential use. It correctly disclaims a three-eigenvalue theorem and continuity in all branches. |
| 778–790, acknowledgments / bibliography | UNCHECKED | Bibliographic attribution/prior-art metadata was not independently verified in this B09 run. These citations are explicitly non-dependencies of the self-contained proof, so there is no downstream correctness impact on the theorem. |

## Support-package audit

`README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, `checks.json`, and `DELIVERY_STATUS.md` were all present and read in the package snapshot. This repairs the package-availability gap noted in the preceding B09 run.

- **PASS:** `proof_map.csv` line ranges agree with the source sections used above.
- **PASS by code inspection:** `verify.py` checks the pinned SHA, exact interpolation support/ranks, the volume-sampling inequality and exact diagonal-dominance slack, plus scoped floating diagnostics. It correctly labels itself non-verifying.
- **READ / not independently rerun:** committed `checks.json` reports `PASS`, 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict sampling cases, 240 floating Schur cases and 30 graph-weight cases.
- **UNCHECKED historical diagnostics:** `AUDIT.md` contains older finite-test counts (504/10/192/800/1040/160). `SOURCE_MANIFEST.json` and `DELIVERY_STATUS.md` explicitly state that the new checker is a different suite and does not reproduce those historical counts. I therefore do not treat the historical numbers as independently reproduced. No theorem step depends on them.
- **UNCHECKED delivery-only claim:** I did not independently rebuild or visually inspect the separately delivered 16-page PDF. The mathematical source itself is complete and source-pinned.

## B09 rank/eigenvalue stress tests

No counterexample was found to any stated rank/eigenvalue lemma. Nearby strengthenings fail sharply:

1. **Rank-`q` shift is sharp.** Let `D=diag(I_{j-1},0_q)` and `R=diag(0_{j-1},I_q)`. Then `rank R=q`, `D+R=I_{j+q-1}`, so replacing `j+q` by `j+q-1` in `lem:rank` would assert `1<=0`.
2. **Schur loss `k` is sharp.** For block diagonal `A=diag(B,S)` with all `k` eigenvalues of `B` above threshold, `N_S(t)=N_A(t)-k` exactly.
3. **Strict diagonal dominance cannot be weakened to non-strict:** `[[1,-1],[-1,1]]` is singular at equality.
4. **The `4r+1` spectral count is rank-theoretically sharp.** The separate improvement artifact gives an exact symmetric direct-sum family with `s_{4r}=1`, `E=0`, `rank R=3r`, `rank R[L,L]=r`, and exactly `r` nonzero/large diagonal entries in `D`. Hence `4r` cannot force `r+1` large `D` entries from the manuscript's rank data alone.

## Threshold-lowering status and next obligation

Current completed improvements on master isolate the attempted `s_16` theorem to the terminal no-pivot `r=4` chamber and produce quantitative four-bank/three-bank determinant structure there. I independently checked that this is compatible with the baseline audit, but it is not a complete replacement proof: the sampled seed determinant can be arbitrarily small, and a single-seed reciprocal determinant estimate is not dimension-free.

Therefore the next obligation remains a **source-coordinate aggregate receiver for the terminal `r=4` chamber**: use the no-pivot geometry beyond the rank count—e.g. aggregate the determinant escalation / overlap-one bordered minors or obtain an order-four-plus-one smoothing mechanism—without paying the reciprocal of one tiny sampled seed. Until that is proved with explicit constants and a closed dependency map, the valid theorem threshold remains **17**.
