# fleet03/B20 independent release-gate audit — fixed multiplicity 17

Run: `20260924T114442Z-fleet03-B20-fixedmult-audit-r1`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Audited source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
Audited source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Audited theorem: for independent real coordinates with densities at most `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`, and `s_17(A)>=s>0`, the law of `X^T A X+b^T X+c` has an essentially bounded density with `||p||_infty <= 10000 K^2/s`.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent scheduled-worker audit; NOT independently validated yet.** I found no fatal mathematical gap in the complete 790-line source after checking the dependency chain from the Fourier preliminaries through the main theorem. I found two nonfatal gaps/repairs below: one inequality/equality wording issue in the projection lemma and one repository-package reproducibility mismatch. Neither changes the theorem as written after the stated local repair.

This is one independent audit, not peer review or formal verification. The source's own requirement of two genuinely separate complete reviews remains in force. The full three-large-eigenvalue conjecture is not proved by this manuscript.

## End-to-end audit ledger

### A1. Main quantifiers and scaling — PASS

The theorem preserves arbitrary dimension, arbitrary independent coordinate laws with only `0<=f_i<=K`, arbitrary signature, arbitrary extra spectrum, and arbitrary affine terms. The normalization `Y=KX`, `A -> A/s`, followed by `Q=(s/K^2) \widetilde Q`, correctly converts the normalized `K=s=1` estimate to `10000 K^2/s`.

### A2. Fourier normalization / inversion / negative half moment — PASS

The transform convention is used consistently. Gaussian regularization gives the stated inversion identities. The Riesz calculation

`E|Z-a|^{-1/2} <= (2pi)^(-1/2) int |t|^{-1/2}|phi_Z(t)| dt`

has the correct power and constant under the manuscript convention. The `3/4` Fourier envelope is used only after multiplication by `|t|^{-1/2}`; it is not incorrectly promoted to an `L^1` characteristic-function bound.

### A3. Geometric rank-one Brascamp--Lieb proof — PASS

For the heat-flow proof, the frame condition makes the column operator a contraction, so

`sum c_i v_i^2 - |sum c_i u_i v_i|^2 >= 0`.

The large-time Gaussian limit gives the correct product of masses, and the bounded-compact-support-to-general nonnegative-integrable passage by monotone approximation is legitimate.

### A4. Product projection density — PASS WITH LOCAL WORDING GAP

The proof of `||p_{U^T X}||_infty <= e^{d/2}` is sound. However, after factors with `b_i=0` are omitted, the text says

`sum_i (1-b_i)=d`.

For the remaining positive-`b_i` indices the correct relation is

`sum_{b_i>0}(1-b_i) <= d`.

This is all the proof needs, since it appears on an upper-bound line. Replacing the displayed equality by `<= d` repairs the wording without changing the result or any later constant.

### A5. Integrated scalar Fourier powers — PASS

For `p>=2`, choosing `m=floor(p/2)` and using `|fhat|<=1` gives the stated comparison with the `2m`-power. The latter is the characteristic function of a sum of independent signed coordinate differences; the one-dimensional product-projection bound yields the correct `p^{-1/2}` integral estimate.

### A6. Decoupling and regularized crossing determinant — PASS

The two-copy Cauchy--Schwarz/Jensen decoupling uses only original-coordinate independence. In the regularized determinant proof, the frame weights

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`

satisfy the required frame identity. The `d_i` powers cancel against the integrated scalar Fourier estimate; the `c_j` entropy factor contributes at most `e^{theta/2}`. With `alpha=(2pi e)^2` and `a=2t`, the remaining determinant is exactly

`det(I+t^2 M^T M/(pi^2 e^2))^{-1/8}`.

No rotational independence is used.

### A7. Crossing volumes and analytic exponents — PASS

Cauchy--Binet gives the coefficient identity for `Z_k`. Retaining the order-`k` term yields exponent `k/4`. The resulting constants are consistent:

- `k=5`: `||p_Z||_infty <= 5e Z_5^{-1/10}`;
- `k=3`: the weighted Fourier integral gives the stated negative-half-moment estimate.

This distinction is essential and is handled correctly.

### A8. Coordinate pivot kernels — PASS

The scalar-square conditional domination is a measure-domination statement and does not assert independence between the completed square and the Schur remainder. The definite-pair bound follows from deterministic two-dimensional change of variables. The indefinite-pair hyperbolic parameterization is applied in original coordinates; its tail estimate uses only individual density caps and total mass. The logarithmic singularity is subsequently averaged against a surviving quadratic direction using the quarter-power concentration lemma.

### A9. Quarter-power concentration — PASS

If a diagonal coefficient is large, the scalar-square small-ball estimate suffices. Otherwise a sign partition produces an original-coordinate cross block with operator norm at least one quarter of the quadratic-part norm. Retaining one singular factor in the determinant theorem yields the `|t|^{-1/4}` envelope. Gaussian smoothing then produces the stated `rho^{1/4}` concentration and the uniform logarithmic-potential bound. No false uniform pointwise quadratic-phase estimate over arbitrary cap-one laws is invoked.

### A10. Volume-sampled interpolation / support / ranks — PASS

For a nonsingular disjoint seed `B=A_{S,T}`, the interpolant

`P=A_{.,T} B^{-1} A_{S,.}`

has rank at most `r` and agrees with `A` on rows `S` and columns `T`. The bordered determinant identity controls the off-diagonal residual on `L x L`. Singular seeds are correctly omitted, so the aggregate count is an inequality rather than a false equality.

In the completion `A=D+R+E`, `D` vanishes on `S union T`, `E` is zero-diagonal and supported only on `L x L`, and `R_{L,L}=P_{L,L}` has rank at most `r`. Globally, `R-P` is supported in rows `T` or columns `S`, giving `rank R<=3r`. I also checked that this global `3r` phenomenon is not merely an artifact: already for `r=1` a generic three-coordinate symbolic instance can attain rank three.

### A11. No-pivot spectral-to-volume implication — PASS

Assuming `V_k<kappa^k`, telescoping produces a ratio `V_{r+1}/V_r<kappa` (or the first vanishing volume). For `1<=r<=4`, the completion gives `||E||<=1/16`. Since `m=4k-3>=4r+1`, rank perturbation by a global rank-`3r` matrix forces at least `r+1` diagonal entries of `D` of modulus at least `1-epsilon`; these lie in `L` because `D` vanishes on the seed. On an `(r+1)`-subset the manuscript's explicit diagonal/off-diagonal bounds give strict row diagonal dominance, contradicting `rank R_{L,L}<=r`. The arithmetic slack is positive.

The `r=0` case is separately and correctly disposed of by the Frobenius norm of the off-diagonal part.

### A12. Random cut, nine-direction half potential, and final pivot proof — PASS

A fair coordinate cut retains each ordered disjoint `k`-minor with probability `4^{-k}`, so the expected crossing volume is `4^{-k}V_k`. This gives the manuscript's `k=3` half-potential and `k=5` density consequences. The pivot half-potential proposition correctly uses Schur spectral counts; the main scalar-pivot branch removes one coordinate from seventeen and still has enough directions for the nine-eigenvalue half-potential bound. The two-coordinate pivot branches remove two directions and use only what remains. The final normalized constants (`2400`, `6010`, and the pair bounds) all remain below `10000`.

## Independent Schur-count check

I separately stress-tested the Schur spectral-count statement numerically on random real symmetric matrices in dimensions 3 through 7 and all admissible pivot sizes, comparing the count of eigenvalues of absolute value above random thresholds before and after Schur complementation. No counterexample appeared in 5000 random trials per tested dimension/pivot pattern. This is diagnostic only; the proof itself is the interlacing argument through the complementary principal block of `A^{-1}`, followed by the manuscript's singular perturbation limit.

## Repository-package GAP (nonmathematical but release-relevant)

At the audited master snapshot, the manuscript root exposed `manuscript.tex`, `README.md`, and `AUDIT.md`, but the README refers to `proof_map.csv`, `verify.py`, `checks.json`, and `SOURCE_MANIFEST.json` as canonical package members. Those files were not present in the root listing I inspected. Therefore the repository should not presently be described as containing the complete reproducibility package unless those files are restored or the README is corrected. This does not by itself undermine the symbolic proof in `manuscript.tex`.

## Threshold accounting: why this audit does not lower 17

The current interpolation mechanism naturally gives the count `4k-3`: the correction has global rank as large as `3r`, while the contradiction needs `r+1` large diagonal coordinates in the seed complement where the restricted correction has rank only `r`. The global `3r` rank can genuinely be attained, so a reduction obtained merely by replacing `3r` with `2r` is not justified.

The next direct multiplicity is `k=4`, which would correspond to thirteen large singular directions in the same algebraic scheme. But the present determinant theorem then yields Fourier exponent exactly

`k/4 = 1`,

so the resulting `|t|^{-1}` envelope is borderline non-integrable and does not imply an `L^infty` density by absolute Fourier inversion. Consequently **no 17->13 improvement is claimed here**. A 13-eigenvalue theorem through this architecture requires a genuinely stronger endpoint analytic step (for example, an order-four small-ball/density estimate not based solely on absolute `L^1` Fourier integrability), or a new structural reduction.

## Release gate

- Mathematical baseline at multiplicity 17: **PASS in this audit**.
- Fatal mathematical defect found: **none**.
- Local repair required: projection-lemma equality `=` should be `<=` after zero-`b_i` rows are omitted.
- Reproducibility/package gap: four files named by README were absent from the root listing inspected.
- Multiplicity improvement established: **none**; 17 remains the best theorem certified by this audit.
- Full three-eigenvalue target: **OPEN**.
- Continuity: the no-pivot Fourier branch has continuous density; the manuscript deliberately claims only an essentially bounded density globally.
- Independent validation: **not yet asserted**. This report supplies one independent complete scheduled-worker review; a second genuinely separate complete review is still required under the owner objective before marking the manuscript independently validated.

## Next proof target

Attack the `k=4` endpoint directly: under a physical crossing block with fourth crossing volume bounded below, prove a dimension-free `L^infty` density bound without demanding absolute integrability of the crude `|t|^{-1}` envelope. A successful endpoint theorem would combine with the already-audited interpolation argument to lower the multiplicity threshold from 17 to 13 while preserving arbitrary signs, affine terms, rough cap-one laws, and all extra spectrum.
