SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-24T13:33:00Z.
attacking: B13 definite-pair/hyperbolic audit, complete dependency recheck, and the nine-eigenvalue product-Fourier improvement.

# fleet03/B13 fixed-multiplicity audit r4

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, source blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 790 lines.
Current source tree inspected before publication: `d2ae3d3878703809e7d7b70cf47f0db7a6740553`.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent B13 recheck; no fatal defect found.** The previously noted local wording issue in the product-projection proof remains a nonfatal repair. The earlier repository-package gap is now resolved: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are present and readable. The current finite checker reports PASS but, correctly, is not treated as proof.

A separate improvement artifact from this same run proves the stronger candidate theorem

` s_9(A)>=s > 0  =>  ||p_(X^TAX+b^TX+c)||_infinity < 3078 K^2/s.`

This audit does not self-award independent-validation or release status to that improvement.

## Line/label audit against proof_map.csv

### Lines 1-160: theorem, scaling, Fourier and Riesz — PASS

- `thm:main` / `cor:33`: quantifiers are arbitrary independent real coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine `b,c`; no moments or support assumptions are present.
- `lem:fourier`: the convention gives the stated `2pi` Plancherel constant; Gaussian regularization justifies the rough-law limiting argument. `phi in L1` is invoked only in branches where an integrable envelope was proved.
- `lem:envelope`: direct integration of `min(1,(a/|t|)^p)` gives `2ap/(p-1)` and hence the stated density constant.
- `lem:riesz`: the gamma/Gaussian representation and the Fourier normalization yield the stated half-potential factor. The order-three determinant envelope is used here with the additional `|t|^-1/2` weight, not incorrectly as an `L1` characteristic-function bound.

### Lines 169-217: singular values, Schur counting, diagonal dominance — PASS

- `lem:rank`: valid for nonsymmetric auxiliaries because it is stated in singular values via best-rank approximation.
- `lem:schur`: the principal-pivot Schur complement loses at most the pivot size in the count of eigenvalue magnitudes above a threshold. The singular case is correctly obtained by an `A+epsilon I` limit while preserving the chosen invertible pivot.
- `lem:dd`: standard strict row diagonal dominance; no symmetry required.

### Lines 221-301: geometric BL, product projections, scalar Fourier powers — PASS with one local wording repair

- `thm:bl`: heat-flow proof, frame identity, Gaussian limiting argument, and rough-function monotone approximation are consistent.
- `lem:projection`: after rows with `b_i=0` are dropped, the displayed sentence `sum_i(1-b_i)=d` should be read as

  `sum_{b_i>0}(1-b_i) <= d`.

  Indeed over all rows `sum_i(1-b_i)=d`; omitted zero-`b_i` rows each contribute one to the latter sum. The required conclusion is unchanged:

  `log p(y) <= (1/2) sum_{b_i>0}(1-b_i) <= d/2`.

  Status: **GAP, local wording only; theorem remains proved.**
- `lem:scalar-fourier`: the even power is a density-at-zero calculation for a sum of independent signed coordinates; the projection cap is applied before any deterministic rotation could threaten independence.

### Lines 310-400: decoupling, regularized determinant, crossing volumes — PASS

- `lem:decoupling`: copies are introduced only in the selected original-coordinate bank. The difference coordinates are independent and their densities are bounded by one.
- `thm:determinant`: the graph-frame weights satisfy the required identity; the scalar Fourier-power exponents are `2/d_i>=2`; the cancellation of the `d_i` powers and choice `alpha=(2pi e)^2` give the determinant exponent `-1/8` after taking fourth roots.
- `cor:vol-fourier`: order five yields exponent `5/4>1` and hence density; order three yields exponent `3/4` and is used only through the half-Riesz estimate.

### Lines 404-525: square, definite pair, hyperbola, quarter concentration — PASS

- `lem:square`: the two inverse branches give the `|a|^-1/2 |z-v|^-1/2` envelope. The conditional formula is a measure-domination statement and does not assert independence between the completed square and its Schur remainder.
- `lem:definite`: the deterministic orthogonal diagonalization occurs inside a two-dimensional integral after conditioning on two original independent coordinates; it does not rotate the random vector and reassert independence.
- `lem:hyperbola`: direct differentiation gives Jacobian `1/(2 sqrt D)`. On each positive/negative tail a physical coordinate with coefficient at least `rho0/sqrt2` exists; the coordinate used on the two tails need not be the same. The pre-rounding branch bound is `(15/2)log2 + log_+(32/(delta Lambda))`, and `Lambda>=2/sqrt D` gives the claimed envelope.
- `lem:quarter`: the scalar-pivot and off-diagonal branches cover all nonzero symmetric matrices. The Gaussian smoothing argument is integrated in frequency and does not use the refuted pointwise van-der-Corput shortcut.

### Lines 528-645: volume interpolation and no-pivot branches — PASS

- `def:pivot-volume`: ordered disjoint row/column sets are used consistently.
- `lem:sampling`: the bordered determinant identity is exact for a nonsingular seed; singular seeds can have nonsingular extensions, so the aggregate relation is correctly an inequality.
- `lem:completion`: `D` vanishes on the seed; `E` has zero diagonal; `R-P` is supported in rows `T` or columns `S`; therefore `rank R<=3r`, while on `LxL`, `R=P` and `rank R[L,L]<=r`.
- `prop:volume`: perturbation by `E` is in singular values, so nonsymmetry causes no issue. The forced large diagonal entries lie in `L`, and `m>=4r+1` supplies `r+1` of them. Strict diagonal dominance then contradicts the restricted rank, not the global rank.
- `lem:cut`: each ordered disjoint `k,k` minor crosses a fair cut with probability `4^-k`.
- `cor:no-pivot`: order three is a half-potential bound and order five an actual density bound, with the stated scaling.

### Lines 654-724: singular kernels and pivot half potentials — PASS

- `lem:kernels`: both singular integrals are locally integrable at the allowed exponents; the translated log-kernel bound is uniform in the translation.
- `prop:pivot-H`: scalar, definite pair, and indefinite pair alternatives are exhaustive for an `eta`-pivot. In the scalar case the Schur remainder has at least one large eigenvalue; the hyperbolic branch averages the moving critical value through Tonelli rather than choosing rough pointwise representatives.
- `prop:nine`: the distinction between truncated `H(Q)` and the full half potential is explicit; the outside kernel contributes at most one.

### Lines 726-790: main proof and scaling — PASS

- No-pivot `s_17` uses order five.
- A scalar pivot loses one spectral direction, leaving at least sixteen and hence the nine required by `prop:nine`.
- A pair pivot loses two directions. Definite pairs are paid directly; indefinite pairs retain a nonzero Schur direction for the logarithmic moment.
- The general scaling `Y=KX`, `Q=(s/K^2) Q_tilde` is correct and preserves all input-law hypotheses.
- The theorem asserts essential boundedness globally. Continuity is not silently inferred from non-Fourier pivot branches.

No source region in the pinned 790-line baseline is left `UNCHECKED` in this run.

## Support-file audit

- `README.md`: matches the pinned source identity and correctly distinguishes source from the conversation-delivered PDF.
- `SOURCE_MANIFEST.json`: source blob/SHA/size/line count agree with the pinned candidate; it explicitly labels the current review status.
- `proof_map.csv`: line ranges match the manuscript labels used above.
- `verify.py`: exact checks cover interpolation support/ranks, zero diagonals, bordered determinants, sampling aggregation, and rational diagonal-dominance slack; floating checks cover Schur counts and graph weights. It contains no network or model calls.
- `checks.json`: reports PASS for 534 exact interpolation seeds, 18 exact volume comparisons, 240 Schur threshold diagnostics and 30 graph-weight diagnostics. These diagnostics are not used as a substitute for the proofs.
- `AUDIT.md`: correctly labels itself an authoring-agent self-audit and not independent verification.

## Lower-threshold audit

The new fleet03/B04 grouped receiver supplies a density from aggregate order-three crossing volume and a half potential from aggregate order-two crossing volume. I independently rechecked the weighted Holder, Jacobian, entropy, and promotion interfaces needed for its application. Combining them with the baseline interpolation immediately lowers the no-pivot density threshold from seventeen to nine; the B13 sharpened pivot analysis lowers the resulting global constant further to `<3078 K^2/s`. The complete derivation is in the sibling improvement artifact.

An `s_8` theorem is not proved. The fleet03/B08 terminal theorem shows the remaining no-pivot state saturates a rank-six correction and three disjoint two-coordinate banks with only a determinant **ratio** lower bound. Because an indefinite rank-two quadratic can have a logarithmically unbounded density, paying one reciprocal two-minor cannot close this state. The next proof obligation is a product-preserving three-bank/cycle receiver that consumes the determinant ratio before local-minor inversion, or a different structural decomposition.

## Designated partner use

The completed fleet04/B13 no-attainment purification theorem was checked and applied to the actual slab kernel in the sibling improvement. It gives an exact zero-loss equivalence between the cap-one product-law supremum and bounded finite-union unit product sets. No interval, centering, bounded-diameter or fixed-fragment extremality is asserted.

## Final status

- Baseline 17 theorem: **PASS in this run**.
- Baseline projection wording: **GAP, nonfatal/local repair**.
- Support-file presence: **PASS; earlier package gap repaired**.
- Nine-eigenvalue improvement with constant 3078: **proved candidate; owner review gate still applies**.
- Eight-eigenvalue theorem: **OPEN**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
- Full-target continuity: **OPEN**.
