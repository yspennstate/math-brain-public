# fleet01/B14 end-to-end audit — rough-law / measurable-kernel lens

Run: `20260924T124247Z-fleet01-B14-fixedmult-audit-r1`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner/objective-reported SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69` (not independently recomputed in this connector-only run).  
Current `master` at the final pre-write refresh still used the same manuscript blob as the baseline.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Executive verdict

**Mathematical manuscript verdict: PASS on this complete review; no fatal proof gap found.** I read all 790 source lines from the pinned blob and independently re-derived every substantive analytic/algebraic step, with particular attention to arbitrary rough densities, measurable versions, conditional kernels, Tonelli/Fubini, exceptional slices, weak limits, approximate identities, unbounded supports, and arbitrary translations. I found no hidden bounded-support, moment, smoothness, rotated-independence, or conditional-density-cap assumption.

**Release-package verdict: GAP / UNCHECKED.** The current manuscript root contains only `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`. The files that README/AUDIT describe as part of the reproducible package — `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` — are absent from the current root, and they were also absent at the pinned baseline commit. Therefore the manuscript proof can be audited directly, but the claimed finite-check package cannot presently be independently rerun or checked from this repository root. This does **not** invalidate the symbolic proof; it does prevent treating the package-level computational claims as independently verified.

**Multiplicity:** this review does not justify a reduction below 17. I independently confirmed that the present proof spends 17 only in the no-pivot order-five branch. The terminal `r=4` interpolation count saturates at 16: rank `R<=12` plus `s_16` forces four large diagonal entries, while the restricted rank is four, so the manuscript's diagonal-dominance contradiction needs the seventeenth direction. Order four gives the endpoint Fourier tail `|t|^{-1}` without an additional structural input. A fresh peer leverage-interpolated determinant result gives useful conditional 13- and 9-direction branches, but explicitly does not close the high-leverage endpoint, so I do not promote it to an unconditional lower threshold.

No statement here grants independent-validation status; the owner requires two genuinely separate complete reviews and release-gate synthesis.

## Complete line coverage

Every line of the pinned 790-line source was read. The following eight contiguous ranges cover the source without gaps.

| Source range | Verdict | Independent check |
|---|---|---|
| L1–L100 | PASS | Definitions, theorem quantifiers, singular-value convention, normalization architecture, Fourier convention, Gaussian kernel and beginning of inversion. The theorem has the advertised arbitrary dimension/sign/affine/rough-law scope. |
| L101–L200 | PASS | Plancherel via Gaussian approximate identity, Fourier inversion by weak identification, Gaussian inversion, power envelope, Riesz/negative-half-moment representation, singular-value rank perturbation, start of Schur count. Constants and Tonelli uses checked. |
| L201–L300 | PASS | Completion of singular Schur count including singular approximation, nonsymmetric diagonal dominance, full heat-flow proof of geometric rank-one Brascamp–Lieb, product-projection density bound, scalar Fourier-power estimate. No rotated-coordinate independence is used. |
| L301–L400 | PASS | Cross-block decoupling, copied-coordinate independence, regularized geometric determinant inequality, graph weights/Jacobians, determinant expansion, order-five density and order-three negative-half-moment envelopes. Fubini is protected by bounded phase integrands; no moments needed. |
| L401–L500 | PASS | Square pushforward, scalar conditional domination, definite pair, hyperbolic pair and logarithmic envelope, exceptional critical level handling, beginning of quarter-power concentration. Conditional arguments are valid as measure domination, not pointwise selection of environment-dependent versions. |
| L501–L600 | PASS | Quarter-power concentration and no-atoms/log potential, disjoint-volume definition, no-pivot entry bounds, sampled nonsymmetric interpolation, support and global/restricted rank bookkeeping, beginning of spectral-to-volume proposition. |
| L601–L700 | PASS | Terminal diagonal-dominance contradiction, random cut, no-pivot order-three/order-five consequences, truncated half-potential definition, singular-kernel estimates, beginning of pivot half-potential proof. The `4r+1` arithmetic and nonsymmetric singular-value use are correct. |
| L701–L790 | PASS | Completion of all pivot branches, nine-eigenvalue full half-potential, main 17-eigenvalue theorem, scaling in `K,s`, interval/density equivalence, threshold accounting, limitations and bibliography. Main constants are conservative but valid. |

No source range is left `UNCHECKED` in this review.

## Detailed rough-law and measure-theory audit

### 1. Density representatives and product measures — PASS

The theorem assumes `0<=f_i<=K` almost everywhere. Whenever pointwise caps are needed (notably the projection proof), one may redefine each density on its null set to obtain a Borel/Lebesgue-measurable representative bounded everywhere, without changing the law. Finite products are measurable and define the original product law. This is explicitly done in the projection lemma and is harmless everywhere else.

Suggested exposition-only strengthening: state once near the conventions that all coordinate densities are replaced by measurable representatives satisfying the cap everywhere. This would remove repeated version bookkeeping. No proof step currently fails without this sentence.

### 2. Gaussian regularization / approximate identity / weak limit — PASS

The Plancherel argument correctly starts with the integrable Gaussian multiplier. `f*g_eps -> f` in `L^2` follows from translation continuity in `L^2`, proved first on compactly supported continuous functions and then by density. Monotone convergence applies to the nonnegative Fourier integrand as `eps downarrow 0`.

For a general law `mu`, `mu*g_eps` has the displayed nonnegative density. Under `phi in L^1`, dominated convergence gives uniform convergence to the inverse-Fourier candidate. Weak convergence `mu*g_eps => mu` and convergence against `C_c` identify that candidate with the law. This avoids any assumption that the original law already has a continuous density.

### 3. Riesz half-potential / Tonelli — PASS

The gamma representation is nonnegative, so the first interchange with expectation is Tonelli even if the expectation is infinite. Gaussian inversion at fixed `v>0` is absolutely controlled by its Gaussian multiplier. After taking absolute values, the second interchange is again Tonelli on a nonnegative majorant. The explicit `v`-integral produces the manuscript constant. There is no hidden integrability assumption on `Z`.

### 4. Heat-flow Brascamp–Lieb limiting steps — PASS

The compactly supported bounded approximation gives Gaussian tails and polynomially controlled logarithmic derivatives on compact time intervals; the frame identity converts these into an integrable Gaussian majorant in `x`, justifying differentiation and integration by parts. At large time, the frame trace gives `sum c_i=d` and the quadratic frame identity gives the limiting `exp(-|z|^2/4)` profile. At small time, pullbacks of one-dimensional null sets under nonzero linear functionals are null by rotation/Fubini, and Fatou is sufficient. General nonnegative `L^1` data follows by monotone truncation. No finite moment or bounded original support assumption survives the limiting argument.

### 5. Product projection and rough coordinate laws — PASS

The orthogonal map in the proof is only a deterministic change of variables in Lebesgue integration. The proof never declares rotated coordinates independent. The rank-one BL frame uses the rows of the orthogonal complement and the original product factors. The pointwise cap `f_i<=1` and probability mass are exactly enough for `f_i^{1/b_i}<=f_i`; no smoothness or support condition is used. The scalar linear-form density cap follows by deterministic scaling.

### 6. Scalar Fourier powers — PASS

The text says the `2m`-power is integrable; this is justified because `2m>=2`, `|hat f|<=1`, and Plancherel gives `|hat f|^2 in L^1`, so `|hat f|^{2m}<=|hat f|^2`. Fourier inversion then supplies the continuous density value at zero. The projection lemma applies to the original independent signed coordinates, not to a rotated random vector.

### 7. Decoupling and determinant theorem — PASS

All integrations before Fourier majorization have modulus at most one, so Fubini/Tonelli needs no moments. The copied difference bank is coordinatewise independent because each difference uses a disjoint independent coordinate pair. Its density is the convolution `f*tilde f`, bounded by one.

The regularized determinant calculation was independently re-derived: the `c_j,d_i` vectors form an exact geometric frame; `0<c_j<=1`, `0<=d_i<=1`; the scalar Fourier exponent is `2/d_i>=2`; all `d_i` powers cancel; `prod c_j^{-c_j/2}<=e^{theta/2}`; and `alpha=(2 pi e)^2` cancels the residual scalar factor. Fourth-rooting gives exactly the stated determinant exponent `-1/8` and scale `t^2/(pi^2 e^2)`. Rank deficiency causes no problem because `H` is positive definite.

### 8. Scalar square profile and conditional kernels — PASS

For fixed environment, the two monotone inverse branches yield the square density envelope. The subsequent scalar-pivot formula is best interpreted as a measure inequality: for every nonnegative Borel test `psi`, the conditional expectation of `psi(Q)` is bounded by integration of `psi(z)` against the displayed square-root kernel. Integrating this inequality over the outside product law by Tonelli gives the unconditional domination. This avoids selecting a conditional density version simultaneously for uncountably many environments.

The Schur-complement remainder is a polynomial in the original outside coordinates with arbitrary affine term; it is not asserted independent of the square variable after completion, and the proof does not need such independence.

### 9. Definite and hyperbolic two-coordinate changes of variables — PASS

For a definite pair, orthogonal diagonalization is again only a deterministic integral change; the joint input density remains bounded by the original product cap, and independence after rotation is never invoked.

For an indefinite pair, the hyperbolic parametrization has Jacobian `1/(2 sqrt D)`. Tail control uses one original coordinate on each tail; on the negative tail one may choose a possibly different original coordinate for the `w` vector, with the same norm lower bound. The manuscript's phrase “both cutoffs” is terse but the argument is valid. The exceptional critical output level is null for a fixed fiber, and the proof explicitly permits use through nonnegative test-function domination. Hence an environment-dependent critical value does not create a Fubini “union of null slices” error.

### 10. Quarter-power concentration / no-atoms / logarithms — PASS

The diagonal branch is a direct square-preimage estimate. The off-diagonal branch uses a sign cut of the zero-diagonal part, obtains a physical crossing block with operator norm at least `L/4`, and applies the determinant theorem without discarding rough within-bank phases incorrectly. Gaussian smoothing of the small-ball indicator gives the stated quarter exponent; the gamma integral and elementary constant bound are consistent. Sending `rho downarrow 0` excludes atoms; layer cake then gives the logarithmic potential. No density of the quadratic output is assumed beforehand.

### 11. Sampled interpolation and nonsymmetric auxiliaries — PASS

The bordered determinant identity is correct with the nonsymmetric interpolant `P=A[:,T] B^{-1} A[S,:]`. Squaring removes ordering signs. Under determinant-square sampling, an order-`r+1` disjoint minor is counted at most `(r+1)^2` times; singular seeds can have nonsingular extensions, so an inequality rather than equality is the correct statement.

In the completion, `R-P` has possible support only in rows `T` or columns `S` after the exactly interpolated rows/columns and the `L x L` block are removed. Splitting this support gives two rank-`<=r` terms in addition to `P`, hence global rank `<=3r`; restriction to `L x L` equals `P[L,L]` and has rank `<=r`. Symmetry is never assumed for `R,E,P`.

### 12. Spectral-to-volume conversion — PASS

At `r=0`, off-diagonal Frobenius norm `<1/80` plus diagonal operator norm `<1/100` contradicts a singular value at least one. For `1<=r<=4`, Weyl singular-value perturbation and global rank `<=3r` force `m-3r` large diagonal entries of `D`; because `D` vanishes on the seed, they lie in `L`. With `m=4k-3>=4r+1`, there are `r+1` of them. The zero diagonal of `E`, the no-pivot physical entry bound, and `||E||_F<=1/16` yield strict row diagonal dominance on an `(r+1)` block of `R[L,L]`, contradicting its rank `<=r`. This remains valid though `A-E` and `R` need not be symmetric because only singular-value perturbation and ordinary rank are used there.

### 13. Random cut and volume receivers — PASS

Each ordered disjoint `k,k` seed crosses a fair coordinate cut in the prescribed orientation with probability `4^{-k}`. The resulting physical cross block preserves original-coordinate product provenance. The determinant theorem applies with arbitrary within-bank functions, including all self quadratic and affine terms. Order five gives an integrable `|t|^{-5/4}` envelope; order three with the `|t|^{-1/2}` Riesz weight gives the required half-potential. No output moment is used.

### 14. Singular kernels and pivot averaging — PASS

The `J(d)` estimate separates the two singularities and is finite for `d!=0`; the prior no-atom lemma makes the `d=0` environment event null in the scalar-pivot use. The logarithmic kernel estimate is a nonnegative layer-cake/overlap argument, so Tonelli is legitimate.

The scalar, definite-pair, and indefinite-pair pivot cases all yield inequalities uniform in arbitrary induced affine terms. In the indefinite branch, averaging the hyperbolic measure domination before selecting pointwise density versions correctly handles environment-dependent critical values.

### 15. Main theorem scaling and unbounded translations/supports — PASS

With `Y=KX`, each coordinate density is capped by one. The normalized polynomial satisfies `tilde Q=(K^2/s)Q`; therefore density scaling gives the factor `K^2/s`. Every earlier argument is translation invariant or uniform in affine terms. None integrates `|X_i|^p`, truncates the original law by support radius, or assumes a common center. Thus arbitrary unbounded support and arbitrary translations are genuinely covered.

## Package-level findings

### PKG-1 — FALSE as a current-repository inventory statement

`README.md` says the canonical source includes `proof_map.csv`, `verify.py`, `checks.json`, and `SOURCE_MANIFEST.json`. The fresh current-root listing contains none of these. The baseline commit root contains only `manuscript.tex`.

Impact: the README's package inventory is currently inaccurate. The manuscript itself remains available and pinned.

Repair: either upload the named supplementary files at the manuscript root or revise README/AUDIT to say they are not currently stored there.

### PKG-2 — UNCHECKED finite-check claims

`AUDIT.md` reports exact/numerical counts (504 interpolation seeds, 10 aggregate comparisons, 192 cut/order cases, 800 Schur cases, 1040 nonsymmetric perturbation inequalities, 160 graph-weight cases) and says all checks in `verify.py` passed. Because `verify.py` and `checks.json` are absent, this review cannot reproduce or inspect those computations. They remain `UNCHECKED` here. They are not used as premises in my symbolic proof audit.

### PKG-3 — UNCHECKED manifest/PDF hash provenance

The root does not contain `SOURCE_MANIFEST.json`, and the connector listing contains no compiled PDF blob. Accordingly the reported PDF hash and manifest review state were not independently verified in this run. Again, this has no effect on the mathematical proof in the `.tex` source.

## Threshold audit: why 17 remains the lowest unconditional theorem established here

The pivot branches consume substantially fewer directions: a scalar pivot needs nine directions after deleting one coordinate (so ten at entry), an indefinite pair needs one surviving Schur direction (three at entry), and a definite pair needs no residual spectrum. The bottleneck is solely the no-pivot order-five receiver.

At order five, the sampled interpolation can land at `r=4`. The present decomposition gives global rank `<=12` and restricted rank `<=4`. With `s_16>=1`, the singular-value/rank step forces **four** large diagonal entries of `D`, exactly matching the restricted-rank allowance; the row diagonal-dominance contradiction requires five. With `s_17>=1`, it forces five, producing the contradiction. Thus the manuscript's same structural mechanism does not lower by simply changing `17` to `16`.

The analytic side has the matching endpoint obstruction: order-four crossing volume yields only `|phi(t)|=O(|t|^{-1})` from the leverage-free determinant theorem, which is not absolutely integrable. The fresh fleet01/B04 leverage-interpolated determinant theorem validly improves order four whenever the volume-producing physical crossing has maximum row leverage `h<1`, and order three when `h<3/4`; however it explicitly loses its integrable gain as `h->1`. I checked that this is a conditional improvement, not an unconditional replacement proof. Therefore it does not lower the theorem's global multiplicity.

A previous B14 run also proved a quantitative terminal good-seed/heavier-neighbor fact under `s_16`, but the neighbor need not inherit the small residual-ratio certificate and the exchange graph has no dimension-free indegree bound. I found no valid transfer/charging argument that closes this terminal case.

**Rigorous threshold after this run: 17.** Statements with 16 or fewer spectral directions remain `GAP` absent a new high-leverage/terminal-saturation receiver or a genuinely integrable order-four endpoint estimate.

## Review status

This file is one complete end-to-end review by `fleet01/B14`. It is not a second identity and is not a self-awarded peer certificate. I have not used configuration, commit existence, or another worker's title as evidence of mathematical correctness. Any independently-validated status still requires the owner's two genuinely separate complete reviews and synthesis gate.
