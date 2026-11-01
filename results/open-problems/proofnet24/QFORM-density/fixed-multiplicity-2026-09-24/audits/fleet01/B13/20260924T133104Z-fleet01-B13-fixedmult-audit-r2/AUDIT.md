# fleet01/B13 independent full audit — fixed multiplicity candidate

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Run: `20260924T133104Z-fleet01-B13-fixedmult-audit-r2`.

Pinned mathematical baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `manuscript.tex` git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, package SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes / 790 lines. I read the complete 790-line baseline source and the current README, DELIVERY_STATUS, historical AUDIT, proof_map, SOURCE_MANIFEST, verify.py and checks.json. The source hash is mutually consistent across the manifest, checker and recorded check result; I did not independently recompute the SHA-256 from raw bytes in this connector run. The git blob and baseline commit were read directly.

## Verdict

**PASS** for the pinned seventeen-direction theorem at its exact stated scope. I found no fatal mathematical defect in the complete baseline argument. This is one independent worker audit, not a release certificate or journal peer review. The theorem remains a fixed-multiplicity result; it does **not** prove the unrestricted three-eigenvalue conjecture.

Candidate proved by the pinned source: independent arbitrary real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary signature/remaining spectrum and affine `b,c`; if `s_17(A)>=s>0`, then the law of `X^T A X+b^T X+c` has essential density at most `10000 K^2/s`.

No mathematical source range is left unchecked below. External bibliographic priority/metadata at lines 782--789 was read for internal consistency but not independently literature-verified; it is marked **UNCHECKED (external attribution only)** and is not a proof dependency.

## Package audit

- `README.md`: **PASS.** Correctly identifies the complete 790-line source, exact baseline, candidate scope, support files and nonvalidation status.
- `DELIVERY_STATUS.md`: **PASS as delivery/status evidence.** Correctly separates source delivery, PDF delivery, task activity and mathematical validation.
- `SOURCE_MANIFEST.json`: **PASS for internal source/hash consistency.** It records baseline commit, blob, SHA-256, source size/lines and support hashes consistently with the checker/result files.
- historical `AUDIT.md`: **PASS as a self-report only.** Its older finite-test counts are explicitly distinguished from the newer reproducibility suite.
- `proof_map.csv`: **PASS.** Statement/proof ranges match the baseline source ranges used below.
- `verify.py`: **PASS as a scoped finite diagnostic, not proof.** It pins the baseline SHA, checks exact interpolation identities/ranks and the exact diagonal-dominance slack, then performs numerical Schur/graph diagnostics. Its assertions do not purport to certify all dimensions.
- `checks.json`: **PASS as the recorded execution result.** It reports 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict-sampling cases, 240 Schur threshold cases and 30 graph-weight cases. I did not rerun the Python suite in this connector-only audit; independent runtime reproduction is **UNCHECKED**, with no effect on the symbolic proof below.

## End-to-end line audit

### Lines 35--83 — definitions, theorem, architecture

**PASS.** Singular values are correctly identified with ordered absolute eigenvalues for symmetric `A`. Quantifiers preserve arbitrary dimension, sign, affine terms and arbitrary independent cap-`K` densities. The normalization `eta=1/100`, `kappa=1/80^2` is used consistently. The architecture correctly distinguishes the order-three half-potential receiver from the order-five density receiver.

### Lines 91--160 — Fourier identities, power envelope, negative half moments

**PASS.** With `hat f(t)=int exp(itx)f(x)dx`, the `2pi` Plancherel and `1/(2pi)` inversion constants are correct. Gaussian regularization justifies inversion without smoothness. The gamma calculation gives

`int_0^infty v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`,

hence the Riesz prefactor `1/sqrt(2pi)`. For a `3/4` Fourier envelope the weighted integral is exactly `12 sqrt(u)`. Extended nonnegative values and Tonelli are used legitimately.

### Lines 169--217 — singular-value perturbation, Schur spectral count, diagonal dominance

**PASS.** The approximation-number formula proves both nonsymmetric singular-value claims. For invertible `A`, the complementary inverse block is `S^{-1}`; positive and negative principal-compression interlacing gives the absolute spectral count. The singular case follows from `A+epsilon I`, using threshold `t-|epsilon|` and continuity. Strict row diagonal dominance implies invertibility without symmetry.

### Lines 221--255 — geometric rank-one Brascamp--Lieb

**PASS.** The heat equation normalization is consistent with the chosen Gaussian. Direct differentiation gives

`partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`,

because the frame map is a contraction. Compact-support Gaussian bounds justify differentiation/integration by parts, the large-time normalization is exact since `sum c_i=d`, and the small-time passage uses Lebesgue points plus Fatou. Truncation gives the general nonnegative integrable case.

### Lines 258--301 — projection densities and scalar Fourier powers

**PASS.** The orthogonal-complement row weights `b_i=1-|U^T e_i|^2` form the needed geometric frame. The cap-one inequality `f_i^(1/b_i)<=f_i` yields the one-dimensional norms and `-b log b<=1-b` yields `||p_{U^T X}||_infinity<=e^(d/2)`. No independence of rotated coordinates is asserted. For Fourier powers, `m=floor(p/2)>=p/4`; `|hat f|^(2m)` is the characteristic function of a sum of literal independent differences, and the scalar projection cap gives the stated `2pi sqrt(2e)/sqrt(p)` bound.

### Lines 310--400 — decoupling, regularized determinant, crossing-volume envelopes

**PASS.** Squaring and introducing an independent copy only in the literal `J` bank yields the second-power decoupling; Jensen yields the fourth-power form; difference coordinates remain independent cap-one variables. In the determinant theorem, with `a=2t`, `alpha=(2pi e)^2`, the weights

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`

form the exact rank-one frame and satisfy `sum d_i=sum(1-c_j)`. The BL scaling factors are correct. Scalar Fourier powers at exponent `2/d_i` cancel the powers of `d_i`; `prod c_j^(-c_j/2)<=e^(theta/2)` and the chosen regularizer cancel the remaining `(2pi e)^theta`. Taking fourth roots gives exactly

`|phi_Z(t)|<=det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

Cauchy--Binet gives the `Z_k` expansion. Keeping one order yields `u_k=pi e Z_k^(-1/(2k))`; `k=5` gives density `5e Z_5^(-1/10)`, while `k=3` gives the stated full negative-half-moment bound.

### Lines 404--434 — scalar square and definite pair

**PASS.** The square profile has exactly two inverse branches and the interval-preimage bound follows from the square-root modulus. Conditional use is a measure-domination statement, not an independence assertion. For a definite two-coordinate block, completing the square and deterministic orthogonal diagonalization are legitimate. In elliptic polar variables `(delta,theta)` the absolute Jacobian is `1/(2 sqrt(|det B|))`, so a joint density cap `M` gives `pi M/sqrt(|det B|)`. No post-rotation independence is used.

### Lines 437--482 — hyperbolic pair, both signs, rough original-coordinate tails

**PASS.** This was the primary B13 lens and was reconstructed in full.

For `delta=z-v>0`, the two branches

`w_epsilon(t)=epsilon sqrt(delta/mu_+) cosh(t)e_+ + sqrt(delta/|mu_-|) sinh(t)e_-`

cover the complete level set. Direct determinant calculation of the two parameter derivatives gives absolute Jacobian `1/(2 sqrt(D))` on each branch, `D=|det B|`. Writing a branch as `u e^t+w e^(-t)` gives

`|u|=|w|=rho_0=sqrt(delta Lambda)/2`, `Lambda=mu_+^(-1)+|mu_-|^(-1)`.

Choose an **original physical coordinate** with `|u_i|>=rho_0/sqrt(2)`. For `t>=(3/4)log 2`, the decaying term is at most half the growing term, hence this original coordinate is monotone, has fixed sign, and obeys `|y'(t)|>=|y(t)|/3`. With `T=max((3/4)log2,log(2/|u_i|))`, its magnitude is at least one. Since the other original-coordinate density is at most one,

`int_T^infty f_1(w_1(t))f_2(w_2(t))dt <=3 int_{|y|>=m, one sign} f_i(y)/|y| dy`.

Here **both hypotheses are used**: cap `f_i<=1` and total mass at most one on the half-line imply the decreasing-weight integral is maximized by the nearest length-one interval, giving `<=3 log(1+1/m)<=3 log2`. The negative tail is identical using `w`; it may select a different original coordinate, which is harmless. The two cutoffs obey

`T,T' <= (3/4)log2 + (1/2)log_+(32/(delta Lambda))`.

Thus each branch integral is at most `(15/2)log2+log_+(32/(delta Lambda)) < 6+log_+(32/(delta Lambda))`. Since `Lambda>=2/sqrt(D)`, summing the two branches against the coarea factor gives exactly

`D^(-1/2)(6+log_+(16 sqrt(D)/|z-v|))`.

For `delta<0`, negating the form/interchanging the positive and negative eigendirections gives the same computation. The critical level `delta=0` is null. Conditional uses later are through nonnegative test-function domination and Tonelli, so a moving exceptional point for rough densities is never treated as a common pointwise exceptional set.

### Lines 485--525 — quarter-power concentration and logarithmic averaging

**PASS.** The diagonal branch gives the conditional square small-ball estimate. Otherwise the random-sign cut of the off-diagonal part produces a literal original-coordinate crossing block with norm at least `L/4`; the determinant theorem yields the `|t|^(-1/4)` envelope. Gaussian smoothing with `v=1/8` gives coefficient

`2^(5/8) pi^(-1/4)e^(3/8)Gamma(3/8)<16`.

Layer cake then yields `L_0=4+4 log16` and in particular atomlessness. This is exactly what is needed when averaging the moving hyperbolic critical value in the main indefinite-pair branch.

### Lines 528--645 — pivot volume, sampled interpolation, rank bounds, spectral-to-volume conversion

**PASS.** No pivot implies `|a_ii|<eta` and `|a_ij|<1/7`. For a nonsingular sampled seed, the bordered determinant identity is exact; singular seeds can have nonsingular extensions, so the manuscript correctly obtains an inequality rather than claiming equality. The interpolant `P=A[:,T]B^{-1}A[S,:]` can be nonsymmetric and has rank at most `r`; it agrees with `A` on rows `S` and columns `T`.

In the completion, `R-P` is supported in rows `T` or columns `S`, giving global `rank R<=3r`, while on `L` one has `R_LL=P_LL` and `rank R_LL<=r`. `D` vanishes on the seed and `diag E=0`. These are the two distinct rank facts needed later.

If `V_k<kappa^k`, a bad ratio occurs at some `r<=k-1`. For `r>=1`, `||E||<=1/16`. With `m=4k-3>=4r+1`, global rank subtraction forces at least `r+1` diagonal entries of `D` of modulus at least `1-epsilon`, all in `L`. On those rows,

`|R_ii|>=371/400`, while each off-diagonal is `<1/7+1/16`; for `r<=4` the row sum is `<23/28`, with exact slack `297/2800>0`. Hence the `(r+1)` restricted block is invertible, contradicting `rank R_LL<=r`. The fair physical-coordinate cut captures every ordered disjoint pair with probability `4^(-k)`, giving the stated order-three and order-five analytic consequences.

### Lines 654--674 — singular kernels

**PASS.** The near part of `J(d)` scales to a finite universal integral `<8`; on the far part `|x-d|>=|x|/2`, giving the logarithmic term. For the log kernel, superlevel sets are intervals; overlap is maximized at coincident centers and the exact centered integral is `8`.

### Lines 676--724 — pivot half-potential and nine-direction half-potential

**PASS.** Scalar pivot: Schur leaves a unit spectral direction and the square profile plus the `J` kernel gives the exact stronger estimate

`H(Q)<=10(20+12 log16)=532.710646...<600`.

Definite pair gives `<160`. Indefinite pair uses the hyperbolic envelope and the log-kernel directly, with `sup D^(-1/2)log_+D=2/e`; it is `<444`. Therefore the coarse uniform `H<=600` is valid. For `s_9>=1`, the pivot case uses this result and the no-pivot case has a full half-potential `<200`; outside distance one the half-kernel is at most one, so the full potential is `<=601` as printed.

### Lines 726--749 — main theorem and scaling

**PASS.** The no-pivot branch under `s_17>=1` has density `<2400`. A scalar physical pivot leaves at least sixteen Schur directions, hence enough for the nine-direction full half-potential; the printed `6010` is valid (though nonsharp). A definite pair is `<40`. An indefinite pair leaves at least fifteen Schur directions, hence in particular norm at least one; averaging the hyperbolic envelope uses the quarter-power logarithmic potential and gives `<251`. All conditioning remains in original coordinates.

For general `K,s`, `Y=KX` has cap-one coordinate densities and `A/s` has seventeenth singular value at least one. The identity `Q=(s/K^2) Qtilde` gives the final `K^2/s` factor exactly.

### Lines 750--781 — threshold accounting, limitations, acknowledgment

**PASS.** The stated proof dependencies and limitations accurately describe the baseline. The manuscript does not infer bounded density from the order-three envelope and does not claim the three-eigenvalue conjecture or continuity in the pivot branches.

### Lines 782--789 — bibliography

**UNCHECKED (external attribution only).** The references are internally consistent with the in-text attribution and no theorem depends on an unproved statement from them. I did not perform an external priority/bibliographic verification in this run. Lines 790/end-of-document: **PASS**.

## B13-specific downstream audit: definite/hyperbolic critical-value use

**PASS.** The definite-pair Jacobian is sign-insensitive after an overall sign change. The indefinite envelope treats both signs of the level set and uses only original-coordinate changes in the tails. The unit-density cap alone is not silently substituted for total mass: the tail estimate needs and correctly uses cap `<=1` **and** probability mass `=1`. In the main proof the hyperbolic critical value is a Schur-complement quadratic polynomial; the moving singularity is averaged via `E log_+(1/|R-z|)` and the conditional inequalities are interpreted through test functions/Tonelli. There is no illegal common exceptional slice.

## Baseline dependency map

`heat-flow BL -> projection cap -> scalar Fourier powers -> physical-bank decoupling -> regularized determinant -> volume envelopes`;

`sampled disjoint minors -> nonsymmetric completion -> global/restricted ranks -> diagonal dominance -> no-pivot V_3/V_5`;

`physical random cut -> order-three full half potential / order-five density`;

`square + definite pair + hyperbolic pair + Schur count + quarter-power log control -> pivot branches`;

`exhaustive pivot/no-pivot split + scaling -> s_17 theorem`.

## Threshold-lowering status

A separate immutable improvement note from this run reconstructs and audits the fresh complete `s_9` replacement. My conclusion is **PASS as a candidate replacement proof**, preserving arbitrary laws, signs, remaining spectrum and affine terms, with constant `<5338 K^2/s`. I found no rigorous route below nine in this run. The current method has a genuine `s_8` endpoint at the bad ratio `r=2`: global rank `<=6` and restricted rank `<=2` can force only two large residual diagonal coordinates, which is compatible with restricted rank two. Moreover a generic order-two indefinite quadratic can have a logarithmically unbounded density. This is an obstruction to the present proof interface, not a counterexample to an eight-eigenvalue theorem.

Release/validation status remains guarded: no self-awarded independent-validation label is made here, and the unrestricted three-eigenvalue conjecture remains open.
