# fleet02/B11 — full fixed-multiplicity audit, Schur-count lens

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `fleet02-B11-20260924T134908Z-r11`  
Baseline manuscript commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Baseline SHA-256 recorded by the package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, 790 lines, 47,883 bytes.

## Verdict

**PASS** for the complete written 17-eigenvalue theorem in this independent worker audit. I found no fatal mathematical gap in the pinned manuscript. This is one review, not formal verification or a release certificate. The unrestricted three-eigenvalue QFORM conjecture is not solved by this manuscript.

The supplementary package is now complete on current master: `README.md`, `SOURCE_MANIFEST.json`, `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json` are present. I independently re-executed the mathematical logic of the current finite checker: 534 exact interpolation seeds, 18 exact volume comparisons, 9 strict sampling cases, 240 floating Schur threshold cases, and 30 graph-weight cases passed, with exact diagonal-dominance slack `297/2800`. These checks support but do not prove the theorem. I read the exact manuscript git blob. I did not independently recompute the package's external SHA-256 from raw repository bytes, so that one cryptographic rehash is **UNCHECKED** in this run; the git blob itself is pinned exactly.

## End-to-end source audit

| Source lines / label | Status | Independent check, impact, next obligation |
|---|---|---|
| 1–46, setup/abstract/architecture | PASS | Definitions of singular values, essential density, normalized parameters, pivot alternatives, and the announced `9=4*3-3`, `17=4*5-3` dependency structure agree with later proofs. No hidden moment/support/log-concavity/rotation-independence assumption appears. |
| 47–61, `thm:main`, `cor:33` | PASS | Quantifiers are uniform in dimension, signature, remaining spectrum, affine terms, and arbitrary independent density caps. Corollary follows from monotonicity `s_17>=s_33`. |
| 62–87, architecture/normalization | PASS | The proof really uses `K=s=1` first and later rescales. The claimed pivot/no-pivot split is exhaustive. |
| 88–120, `lem:fourier` | PASS | Fourier convention, Plancherel constant `2*pi`, Gaussian convolution, inversion, and continuity under `phi in L1` are consistent. Rough-law use is via convolution/Fubini, not point values on exceptional slices. |
| 122–130, `lem:envelope` | PASS | `int min(1,(a/|t|)^p)=2ap/(p-1)` for `p>1`; inversion yields the stated constant. |
| 132–160, `lem:riesz` | PASS | Gamma/Gaussian calculation gives coefficient `1/sqrt(2*pi)`. The `3/4` envelope weighted by `|t|^-1/2` integrates to `12 sqrt(u)`, hence (2.7) as stated. |
| 161–181, singular-value preliminaries / `lem:rank` | PASS | Approximation-number proof is valid for nonsymmetric matrices. Rank perturbation is used later on `D+R=A-E` without illicit eigenvalue language. |
| 183–207, `lem:schur` | PASS, with clarification below | The fixed-threshold spectral count `N_S(t)>=N_A(t)-k` is valid for invertible pivot `B`, including singular ambient `A`. The limit proof is sound; an explicit singular-value limit formulation is given below. Invertibility of `B` is essential. |
| 209–217, `lem:dd` | PASS | Standard nonsymmetric strict row diagonal dominance argument. |
| 218–255, `thm:bl` | PASS | Heat-flow derivative has the right sign from the Parseval-frame contraction. Tail domination, `t->infinity`, Lebesgue-point/Fatou `t->0`, and monotone approximation close the rough-law proof. |
| 258–282, `lem:projection` | PASS | Orthogonal complement frame and BL scaling give `exp(d/2)`. This controls a projected joint density but never asserts independence of projected coordinates. Scalar scaling gives `sqrt(e)/|a|`. |
| 284–301, `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`; inversion of `|fhat|^(2m)` at zero plus the scalar projection bound gives the stated `2*pi*sqrt(2e)/sqrt(p)`. Difference densities remain cap one. |
| 302–324, `lem:decoupling` | PASS | Cauchy–Schwarz and independent copy are used on original coordinate banks. Pure phases are discarded only after taking moduli. Powers two and four are correct. |
| 326–373, `thm:determinant` | PASS | The regularized frame, graph-BL Jacobians, weights `c_j,d_i`, trace identity, scalar Fourier powers and cancellation with `alpha=(2*pi*e)^2` reproduce determinant exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`. |
| 374–400, crossing volumes / `cor:vol-fourier` | PASS | Cauchy–Binet expansion is exact. Order five gives exponent `5/4>1` and density; order three gives exponent `3/4` and is used only with the half-Riesz weight, not directly for density. |
| 401–434, `lem:square`, profile, `lem:definite` | PASS | Square inverse branches and interval preimage constant are correct. Conditional profile is a measure-domination statement, not an independence claim. Definite pair uses only deterministic rotation of a joint density. |
| 437–482, `lem:hyperbola` | PASS | Hyperbolic parametrization has Jacobian `1/(2 sqrt(D))`; tail monotonicity and bathtub bound control each branch. `Lambda>=2/sqrt(D)` gives the final logarithmic scale. Exceptional critical level is handled in the test-function formulation. |
| 485–525, `lem:quarter` | PASS | Diagonal case and random-sign cross-block case both close. The determinant theorem supplies `|t|^-1/4`; Gaussian smoothing gives quarter-power concentration and layer cake gives `L0=4+4 log16`. |
| 528–535, `def:pivot-volume`, no-pivot entry bound | PASS | From no principal 2-pivot and small diagonal, `|a_ij|^2<eta^2+eta<1/49`, hence `|a_ij|<1/7`. |
| 545–564, `lem:sampling` | PASS | Bordered determinant identity is exact. Ordered disjoint extensions are counted at most `(r+1)^2`; singular seeds explain why the aggregate relation is an inequality. `P` is allowed nonsymmetric and interpolates the specified rows/columns. |
| 566–580, `lem:completion` | PASS | `E` has zero diagonal; `D` vanishes on the seed; `R_LL=P_LL`, so restricted rank is at most `r`. Globally `R-P` is supported on rows `T` or columns `S`, giving rank at most `2r` in addition to `rank P<=r`, hence `rank R<=3r`. No symmetry of auxiliaries is used. |
| 582–619, `prop:volume` | PASS | Telescoping/first-zero choice of `r` is exhaustive. For `r=0`, `||A||<eta+sqrt(kappa)<1`. For `r>=1`, singular-value perturbation and global `3r` rank force `r+1` large diagonal entries, all in `L`; restricted rank `<=r` then contradicts strict diagonal dominance. Exact row slack is `371/400-23/28=297/2800>0`. |
| 621–645, `lem:cut`, `cor:no-pivot` | PASS | Each ordered disjoint minor crosses a fair cut with probability `4^-k`. This yields `Z_k^-1/(2k)<=160`; constants `<200` for the full half potential and `800e<2400` for density are correct. |
| 646–674, `lem:kernels` | PASS | Both singular integrals are finite with the stated coarse constants. The logarithmic rearrangement is valid for interval superlevels. |
| 676–714, `prop:pivot-H` | PASS | Scalar-pivot branch uses one surviving Schur spectral direction and the log potential; definite pair is direct; indefinite pair uses hyperbolic envelope plus the log kernel and `sup D^-1/2 log_+ D=2/e`. All are uniform in induced affine terms. |
| 716–724, `prop:nine` | PASS | Pivot branch gives truncated half potential at most 600; no-pivot order-three gives full half potential below 200; outside the unit window costs at most one. |
| 726–749, proof of `thm:main` | PASS | No-pivot order five gives `<2400`; scalar pivot loses one direction and leaves at least 16, hence nine; definite pair is bounded directly; indefinite pair loses two and leaves at least 15, more than enough for the logarithmic critical-value control. Scaling gives exactly `10000 K^2/s`. |
| 750–790, accounting/limitations/references | PASS | Dependency table matches the proof. The manuscript expressly does not claim the three-eigenvalue theorem or global continuity. Classical citations are attribution only because the specialized inputs are reproved. |

No source range remains mathematically UNCHECKED in the 790-line baseline. The only UNCHECKED item in this run is independent raw-byte SHA-256 recomputation noted above.

## B11 focus: Schur spectral counts, singular matrices, and exact overcount counterexamples

The manuscript's lemma is

`A=[[B,C],[C^T,D]], det B != 0, S=D-C^T B^-1 C  =>  N_S(t)>=N_A(t)-k`.

For invertible `A`, block elimination implies that the complementary principal block of `A^-1` is `S^-1`. Principal-compression interlacing applied separately to `A^-1` and `-A^-1` bounds the numbers of eigenvalues of `S^-1` above `t^-1` in each sign, which is equivalent to the absolute-value count.

For singular ambient `A`, choose `epsilon_j -> 0` avoiding the finitely many values making either `A+epsilon_j I` or `B+epsilon_j I` singular. Put `tau_j=t-|epsilon_j|>0`. Weyl gives

`N_{A+epsilon_j I}(tau_j) >= N_A(t)`.

The invertible case gives

`N_{S_j}(tau_j) >= N_A(t)-k`,

where `S_j` is the Schur complement of `B+epsilon_j I` in `A+epsilon_j I`, and `S_j->S`. If `r=N_A(t)-k>0`, this says the `r`th largest eigenvalue modulus of `S_j` is at least `tau_j`; continuity gives `s_r(S)>=t`. This is exactly `N_S(t)>=r`. Thus there is no endpoint loss when an eigenvalue lies exactly at the threshold.

### Counterexample 1: singular pivot cannot be replaced by a Moore–Penrose Schur complement

Take

`A=[[0,1],[1,0]], B=[0]`.

The Moore–Penrose expression gives `S_dagger=0`. At `t=1`, `N_A(1)=2` and `N_{S_dagger}(1)=0`; a putative loss-one extension would require `0>=1`. Hence `det B !=0` is essential without additional range hypotheses.

**Status:** FALSE for the natural singular-pivot pseudoinverse extension.  
**Impact:** none on the manuscript, whose scalar and pair pivots are quantitatively invertible.  
**Next obligation for any improvement:** do not condition through a singular pivot merely by inserting `B^dagger`.

### Counterexample 2: a tiny invertible scalar pivot can consume one full large direction

For `0<epsilon<1`, let

`A_epsilon=[[epsilon,sqrt(epsilon)],[sqrt(epsilon),1]]`, `B=[epsilon]`.

Then `S=0` and

`spec(A_epsilon)={1+epsilon,0}`.

At `t=1`, `N_A=1` but `N_S=0`, while the pivot itself has no threshold-large eigenvalue: `N_B(1)=0`.

**Status:** FALSE for replacing the loss `k=1` by the number of threshold-large eigenvalues visible in the pivot.  
**Impact:** the manuscript's geometric loss one is sharp even for an arbitrarily small nonzero pivot and singular ambient matrix.  
**Next obligation:** any lower-count proof must obtain extra structure elsewhere; small pivot magnitude alone does not refund the spectral direction.

### Counterexample 3: the full loss two is sharp for an arbitrarily near-singular indefinite pair

Let

`B_epsilon=diag(epsilon,-epsilon)`, `C=sqrt(epsilon) I_2`, `D=diag(1,-1)`

and

`A_epsilon=[[B_epsilon,C],[C,D]]`.

Then `S=D-C^T B_epsilon^-1 C=0`, while

`det(lambda I-A_epsilon)=lambda^2 (lambda-(1+epsilon))(lambda+(1+epsilon))`,

so

`spec(A_epsilon)={1+epsilon,-(1+epsilon),0,0}`.

At `t=1`, `N_A=2`, `N_S=0`, yet `N_{B_epsilon}(1)=0`. Thus one positive and one negative large direction can both be consumed by an arbitrarily near-singular indefinite pivot.

**Status:** FALSE for any universal improvement from loss two to loss one based only on near-singularity, indefinite signature, or the count of large pivot eigenvalues.  
**Impact:** the pair-pivot spectral accounting in the manuscript is sharp at the level of hypotheses used.  
**Next obligation:** a threshold below the current structural bound cannot be obtained merely by sharpening Lemma `lem:schur` under its present assumptions.

## Package/reproducibility audit

- `README.md`: PASS. It now accurately names the complete package and distinguishes source from compiled PDF delivery.
- `SOURCE_MANIFEST.json`: PASS as metadata; source blob/line/byte values agree with the exact blob read in this run. Raw-byte SHA-256 recomputation: UNCHECKED.
- `AUDIT.md`: PASS as a historical self-audit, not independent evidence. Its older finite-test counts are explicitly distinct from the current suite.
- `proof_map.csv`: PASS. Statement/proof ranges agree with the manuscript labels and were used in this audit.
- `verify.py`: PASS as a finite diagnostic. Its assertions match the proof's algebraic invariants and do not overclaim universality.
- `checks.json`: PASS. Independent execution of the checker's logic reproduced 534/18/9 exact counts and 240/30 floating counts, with `297/2800` slack.

## Threshold impact

The Schur accounting itself is not what forces 17. Scalar and pair branches spend only one and two directions respectively, and the examples above show those losses cannot in general be reduced. The 17 threshold is driven by the no-pivot order-five crossing-volume endpoint through `4k-3` with `k=5`. A genuine threshold reduction therefore needs a stronger no-pivot analytic receiver or stronger structural interpolation, not wishful Schur overcounting.

A separate immutable improvement artifact from this run reviews a complete nine-eigenvalue replacement argument now present on master. This baseline audit does not alter the pinned 17-eigenvalue source.
