# fleet01/B15 end-to-end fixed-multiplicity audit — r12

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run start: `2026-09-24T13:02:27Z`  
Pinned baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Manuscript source length: 790 lines.

## Fatal defects first

**No fatal mathematical defect found in the 17-eigenvalue baseline.** I read all 790 lines and independently checked every stated proof dependency. My mathematical verdict on the written theorem is **PASS**:

` s_17(A)>=s>0 => ||p_(X^T A X+b^T X+c)||_infinity <=10000 K^2/s `

for arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, and arbitrary affine `b,c`.

This is one worker audit and not a self-issued release/validation certificate. It does not prove the unrestricted three-eigenvalue conjecture.

There is one **package/reproducibility GAP**, not a theorem gap: the historical counts and high-precision diagnostics listed in the original `AUDIT.md` are not reproduced by the current `verify.py/checks.json`. `SOURCE_MANIFEST.json` now explicitly states that the newly added checker is a different executed suite and the original test counts have not been reproduced. The old counts therefore remain **UNCHECKED as historical computational claims**. The current checker itself is present and internally consistent with the pinned source.

## Complete source audit

| Source lines | Item | Verdict | Reason / downstream impact |
|---|---|---|---|
| 1--74 | Abstract, definitions, theorem/corollary, normalization, architecture | PASS | Quantifiers retain arbitrary dimension, signature, rough product laws, affine terms and remaining spectrum. `s_j` is correctly absolute eigenvalue order for symmetric `A`. The proof explicitly claims only essential `L^infinity`, not global continuity. |
| 75--120 | Fourier convention, Gaussian regularization, Plancherel, inversion | PASS | With `hat f(t)=int e^{itx}f(x)dx`, Plancherel has factor `2pi`, inversion `1/(2pi)`, and `g_epsilon=(4pi epsilon)^(-1/2)e^{-x^2/(4epsilon)}` has transform `e^{-epsilon t^2}`. The Gaussian identity coefficient `1/(2 sqrt(pi v))` is correct. Approximate-identity and weak-limit steps are adequate. |
| 122--130 | Power envelope | PASS | `int min(1,(a/|t|)^p)dt=2ap/(p-1)` for `p>1`; inversion gives `ap/[pi(p-1)]`. |
| 132--160 | Negative-half-moment / Riesz formula | PASS | Gamma representation plus Gaussian inversion and Tonelli yields exactly `1/sqrt(2pi) int |t|^{-1/2}|phi(t)|dt`. The inner `v` integral is `sqrt(2) Gamma(1/4)|t|^{-1/2}`. Under the order-three envelope the weighted integral is exactly `12 sqrt(u)`, so the stated `12 sqrt(u/(2pi))` is correct. |
| 162--181 | Singular values and rank perturbation | PASS | Approximation numbers justify both inequalities for nonsymmetric matrices. No eigenvalue argument is applied to nonsymmetric auxiliaries. |
| 183--207 | Schur spectral count, including singular `A` | PASS | For invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative variational counts give `N_S(t)>=N_A(t)-k`. The `A+epsilon I` limiting argument preserves the threshold with `t-|epsilon|` and closes equality-at-threshold cases. |
| 209--217 | Strict diagonal dominance | PASS | Standard maximal-coordinate proof, valid without symmetry. |
| 219--255 | Geometric rank-one Brascamp--Lieb | PASS | Heat-flow sign is correct: the frame map is a contraction. Gaussian tails justify integration by parts on compact positive time intervals. Large-time scaling uses `sum c_i=d` and the frame identity; the `t downarrow0` Fatou step handles Lebesgue points correctly. |
| 257--282 | Product projection density | PASS | Orthogonal completion is used only in deterministic integration. No independence after rotation is assumed. BL yields `prod b_i^{-b_i/2}` and `-b log b<=1-b` gives `e^{d/2}`. Scalar scaling gives `sqrt(e)/|a|`. |
| 284--301 | Integrated scalar Fourier powers | PASS | `m=floor(p/2)>=p/4`; `|hat f|^{2m}` is integrable and is the characteristic function of a sum of independent differences. The projection cap gives the displayed constant. |
| 303--324 | Cross-bank decoupling | PASS | Copying one original product bank is legitimate; pure same-bank phases have modulus one after expansion; difference coordinates remain independent with density cap one. Both powers 2 and 4 follow. |
| 326--373 | Regularized crossing determinant | PASS | The graph weights form the exact frame for `H=alpha I+a^2M^TM`. One-dimensional scale factors in BL are correct. The scalar Fourier-power estimate cancels the `d_i` powers; `prod c_j^{-c_j/2}<=e^{theta/2}` and `alpha=(2pi e)^2` cancel the entropy factor. Taking fourth roots gives exactly `det(I+t^2 M^TM/(pi^2e^2))^{-1/8}`. |
| 375--400 | Crossing volumes and order-three/order-five envelopes | PASS | Cauchy--Binet expansion is correct. Retaining the order-`k` term gives exponent `k/4`. **Order five:** `5/4>1`, so direct Fourier inversion pays a bounded continuous no-pivot density. **Order three:** `3/4<1`, so it does not pay density inversion; after multiplication by the Riesz weight `|t|^{-1/2}`, the tail exponent is `5/4>1`, which pays only the half-potential. This distinction is used correctly throughout. |
| 402--421 | Scalar square profile and conditional domination | PASS | Change of variables and interval-preimage constants are correct. The profile after conditioning is a measure-domination formula; the proof does not assert independence between the completed square and the Schur remainder. |
| 423--434 | Definite two-coordinate pivot | PASS | Deterministic orthogonal diagonalization is harmless; the `(delta,theta)` Jacobian is `1/(2sqrt(det B))`, giving `pi M/sqrt(det B)`. |
| 436--482 | Hyperbolic pair | PASS | Hyperbolic parametrization and Jacobian `1/(2sqrt D)` are correct. Tail estimates use a literal original coordinate and only its density cap/mass. The middle interval length and `Lambda>=2/sqrt D` conversion are valid. Exceptional critical levels are handled through nonnegative-test-function measure domination. |
| 484--525 | Quarter-power concentration and log potential | PASS | Random sign partition of the off-diagonal part gives a literal cross block with norm at least `L/4`. The determinant estimate gives the `|t|^{-1/4}` envelope. Gaussian smoothing yields the coefficient `2^(5/8) pi^(-1/4)e^(3/8)Gamma(3/8)<16`. Layer cake then gives `L_0=4+4log16`; atomlessness is proved before the logarithmic expectation is used. |
| 527--543 | Pivot/volume definitions and no-pivot entry bound | PASS | From absence of scalar and principal-pair pivots, `|a_ij|^2<eta^2+eta<1/49`; the stated `|a_ij|<1/7` follows. |
| 545--564 | Volume-sampled interpolation | PASS | The bordered determinant identity is correct. Singular seeds may possess nonsingular extensions, so the global counting is correctly an inequality rather than equality. `P=A[:,T]B^{-1}A[S,:]` is allowed to be nonsymmetric and interpolates rows `S` and columns `T`. |
| 566--580 | Diagonal + interpolation completion | PASS | `E` is supported only off diagonal in `LxL`, `D` vanishes on the seed, `R_LL=P_LL`, global `rank R<=3r`, restricted `rank R_LL<=r`. These two rank bounds are kept distinct. |
| 582--619 | No-pivot spectral-to-volume proposition | PASS | The `r=0` case contradicts `||A||>=1`. For `r>=1`, `epsilon<=1/16`; rank subtraction from `m=4k-3>=4r+1` forces `r+1` large diagonal entries in `L`. On the selected block, diagonal lower bound `371/400` exceeds off-row sum `23/28`, so strict diagonal dominance contradicts restricted rank `<=r`. Exact slack is `297/2800>0`. |
| 621--630 | Random coordinate cut | PASS | Every ordered disjoint `k,k` pair crosses a fair cut with probability exactly `4^{-k}`. |
| 632--645 | No-pivot analytic consequences | PASS | For `k=3`, `Z_3^{-1/6}<=160` and the Riesz bound is `<200`. For `k=5`, `Z_5^{-1/10}<=160` and density is `<=800e<2400`. |
| 647--674 | Truncated half-potential and singular kernels | PASS | The near-region `J(d)` integral is bounded by the stated elementary hyperbolic/trigonometric integrals; the far region gives the logarithm. The shifted logarithmic-kernel overlap is maximized at coincident centers and integrates to 8. |
| 676--714 | Pivot half-potential | PASS | Scalar pivot uses one surviving Schur direction, non-atomicity, the `J` kernel and log potential. Exact manuscript value is `200+120log16<560`, rounded to 600. Definite and indefinite pair estimates are both below 600. No conditional-cap shortcut is used. |
| 716--724 | Nine-eigenvalue half-potential | PASS | Pivot case uses the preceding truncated bound; no-pivot case has the stronger full half-potential. Outside distance one the kernel is at most one, yielding full bound 601. |
| 726--749 | Main theorem and scaling | PASS | No-pivot branch `<2400`. A scalar pivot leaves 16 unit-scale Schur directions, hence the nine-direction half-potential applies and gives `6010`. Definite pair `<40`; indefinite pair leaves 15 directions and only needs one for the logarithmic critical value. For general `K,s`, `Y=KX` has cap one and `Q=(s/K^2)Qtilde`, giving the required `K^2/s` scaling. |
| 751--790 | Threshold accounting, regularity scope, bibliography | PASS | The paper correctly states that order three only pays the Riesz quantity in the baseline determinant route, order five pays density, and only the no-pivot branch is asserted continuous. No full-theorem continuity shortcut appears. |

**Unchecked mathematical manuscript ranges:** none. Every line of `manuscript.tex` was read in this run.

## B15 analytic reconstruction

The three normalization constants that are easiest to get wrong are all correct:

1. Gaussian inversion:
   `E exp(-v(Z-a)^2) = [1/(2 sqrt(pi v))] int exp(-t^2/(4v)) exp(-ita) phi_Z(t) dt`.
2. Riesz half-potential:
   `E|Z-a|^{-1/2} <= [1/sqrt(2pi)] int |t|^{-1/2}|phi_Z(t)|dt`.
3. For `|phi(t)|<=min(1,(u/|t|)^(3/4))`, the weighted integral is `12 sqrt(u)`, not an unweighted `L^1` integral. This is precisely why the baseline order-three result is a half-potential theorem and not a density theorem.

At order five the envelope is `|t|^{-5/4}`, genuinely in `L^1`, so Fourier inversion gives a `C_0` density. The manuscript's global theorem does not bootstrap continuity through the pivot cases; those branches are intentionally measure-domination/essential-height arguments only.

## Supplementary files

Fresh reads after the concurrent package repair found all requested support files on `master`:

- `proof_map.csv`, blob `bd52d705490437a1998d78d4d944d13d2186ff97`: **PASS** as a line map; the ranges match the source read in this run.
- `SOURCE_MANIFEST.json`, blob `72e16a87ecc6d8b865a1861d929c32609f79a545`: **PASS** for the source identity and current support-file metadata. It explicitly says the new checker does not reproduce the historical test counts.
- `verify.py`, blob `5755b77201a734080051a8ed7fee705850310466`: **PASS** as a finite reproducibility checker for what it actually tests. It pins the correct source SHA, exactly checks interpolation/rank/diagonal-dominance identities on its finite sample and performs explicitly labeled floating diagnostics.
- `checks.json`, blob `cd6a55e928d1a91d63fb17f5f6184a4cf0c5a937`: **PASS** as recorded output of the new suite: source hash matches, 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, slack `297/2800`, 240 Schur threshold diagnostics and 30 graph-weight diagnostics.

**GAP / UNCHECKED:** the original `AUDIT.md` historical claims of 504 exact interpolation seeds, 10 volume-sampling aggregates, 192 random-cut cases, 800 Schur cases, 1040 nonsymmetric rank-perturbation cases, 160 graph-weight cases, and the listed high-precision diagnostic values are not reproduced by the current checker. `SOURCE_MANIFEST.json` acknowledges this. These finite historical claims are not used as proof of the theorem. The compiled-PDF hash/render/no-warning claims are also **UNCHECKED in this run**, because the binary PDF is not stored in this repository root and no local build artifact was supplied through the connector.

## Lower-threshold status found and independently checked in this run

After completing the baseline audit, I read the complete fleet03/B04 immutable candidate at commit `8ff490c177d0cd7d6f33130f1431785e312a9d10` and independently reconstructed its new grouped product-Fourier compiler, physical-row promotion identities, `E_3` density receiver, `E_2` half-potential receiver, pivot assembly and scaling.

The only compressed point in the original B04 presentation is the rough-law passage from mollified conditional complex pushforwards back to the unsmoothed `L^2` norm. Fleet02/B04 subsequently supplied the correct repair at commit `f1e43c2b688013aed9ff00a3e5ceba398d34793b`: condition on the physical `I` bank, mollify the conditional pushforward, expand its square, establish the weighted-minor estimate uniformly in the mollifier, then remove smoothing with Plancherel/Fourier Fatou and a second Fatou step in the conditioning variable. I independently checked this repair and found it sufficient.

With that repair, the nine-eigenvalue replacement proof is mathematically **PASS in this B15 review**:

` s_9(A)>=s > 0  =>  ||p_Q||_infinity <= 6010 K^2/s `.

The no-pivot branch uses the baseline `V_3>=kappa^3`, a fair physical cut, and the new marginal-free third-crossing receiver. The scalar-pivot branch leaves eight Schur directions; if the Schur complement has a pivot, the baseline half-potential applies, while if it has no pivot then `s_5>=1`, the order-two volume theorem plus the new `E_2` receiver pays the full half-potential. Pair pivots are cheaper. All assumptions of the 17 theorem are retained.

There are now at least two separate recorded full PASS reconstructions of this nine-eigenvalue theorem (fleet01/B16 at commit `54ec2a651d854563f8db0d92c4c3426f76551786` and fleet03/B08 at `c02a08f19d010e508578695a5906744fdbcfcd70`), plus the fleet02/B04 repaired derivation. I record this evidence but do **not** self-promote release/validation status; that remains a release-gate decision.

The current structural route does not prove eight eigenvalues: for order-three volume the worst bad-ratio seed has `r=2`; the completion has global rank `<=6` and restricted rank `<=2`. Under `s_8>=1`, rank subtraction forces only two large diagonal residual entries, which is compatible with restricted rank two. Under `s_9`, three are forced and strict diagonal dominance gives the contradiction. This is a proof-route barrier, not a counterexample to an eight-eigenvalue theorem.

## Final verdict ledger

- Baseline 17-eigenvalue mathematical theorem: **PASS**.
- Baseline manuscript mathematical ranges left unchecked: **none**.
- Current support-file source identity / new finite checker: **PASS**.
- Historical finite-check counts and compiled-PDF/render claims from the original self-audit: **UNCHECKED / package provenance GAP**; no theorem impact.
- Nine-eigenvalue replacement proof after explicit rough-law limit repair: **PASS in this B15 reconstruction**; multiple separate PASS reviews are recorded, but no release status is self-awarded here.
- Eight or fewer eigenvalues by the present interpolation/order-three route: **GAP / not proved**.
- Unrestricted three-eigenvalue conjecture: **not claimed solved**.
