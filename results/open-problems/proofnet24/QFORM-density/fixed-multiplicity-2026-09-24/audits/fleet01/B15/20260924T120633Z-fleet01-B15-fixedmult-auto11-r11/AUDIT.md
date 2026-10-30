# fleet01/B15 independent end-to-end audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T120633Z-fleet01-B15-fixedmult-auto11-r11`

## Source pin and package state

- Pinned initial source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
- The commit exists and records `manuscript.tex` as a 790-line added file.
- Pinned/current manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
- Declared manuscript SHA-256 in the current objective, README and self-audit: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
- Fresh `master` returned the same manuscript blob, so the mathematical source audited here is exactly the pinned baseline blob.

**Package GAP, non-mathematical:** fresh directory enumeration at the manuscript root contains `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`, but does **not** contain the four files named by README/AUDIT/current objective: `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`. Direct fetches of those paths returned 404. Therefore their contents and the finite-check claims depending on them are **UNCHECKED/MISSING** in this run. This does not by itself invalidate the self-contained proof in `manuscript.tex`, but the package is not presently reproducible exactly as README says.

## Overall mathematical verdict

**PASS for the complete written 17-eigenvalue theorem.** I independently read the full 790-line manuscript and re-derived every main analytic/algebraic step, including the starting B15 lens. I found no FALSE mathematical statement and no fatal proof gap in the theorem

`independent coordinate densities <= K`, `A=A^T`, `s_17(A)>=s>0`, arbitrary `b,c`  
`=> ||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s`.

This report is one complete independent audit only. It does not change release/validation status and does not claim the unrestricted three-eigenvalue conjecture.

## Fatal defects first

None found in the 790-line mathematical proof.

The only concrete GAP found is repository packaging/reproducibility: four supplementary files promised by the package are absent on fresh `master`; details above.

## End-to-end line audit

### Lines 1-83 — PASS

Definitions of singular values and essential density height, theorem quantifiers, affine terms, normalization plan, pivot/no-pivot architecture, and the distinction between order three and order five are consistent. No hidden support, moment, identical-law, positivity, or post-rotation independence assumption is introduced.

The scaling at the end is consistent with these lines: for `Y=KX`, the coordinate densities of `Y` are at most one, `\widetilde Q=(K^2/s)Q`, and density rescaling returns the factor `K^2/s`.

### Lines 84-120 — PASS (Gaussian Fourier identities and inversion)

With the convention `fhat(t)=int exp(itx)f(x) dx`, the heat kernel

`g_epsilon(x)=(4*pi*epsilon)^(-1/2) exp(-x^2/(4 epsilon))`

has transform `exp(-epsilon t^2)`. The regularized Plancherel identity has the correct factor `2*pi`. Approximate-identity convergence in `L^2` and monotone convergence justify passage to the limit.

If `phi_Z in L^1`, Gaussian smoothing produces densities converging uniformly to

`p_Z(x)=(2*pi)^(-1) int exp(-itx) phi_Z(t) dt`,

so `||p_Z||_infinity <= (2*pi)^(-1)||phi_Z||_1`. Weak convergence of `mu*g_epsilon` identifies that continuous inverse transform with the law of `Z`.

The Gaussian identity

`E exp(-v(Z-a)^2) = [2 sqrt(pi v)]^(-1) int exp(-t^2/(4v)) exp(-ita) phi_Z(t) dt`

has the correct normalization. No density of `Z` is assumed here.

### Lines 121-160 — PASS (power envelope and Riesz half-potential)

For the envelope `min(1,(a/|t|)^p)`, `p>1`, its exact `L^1` mass is `2ap/(p-1)`, giving the displayed density constant after division by `2*pi`.

The gamma representation

`|z|^(-1/2)=Gamma(1/4)^(-1) int_0^infinity v^(-3/4) exp(-v z^2) dv`

is exact. Combining it with Gaussian inversion gives the inner integral

`int_0^infinity v^(-5/4) exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4)|t|^(-1/2)`,

and therefore exactly

`E|Z-a|^(-1/2) <= (2*pi)^(-1/2) int |t|^(-1/2)|phi_Z(t)| dt`.

For the `3/4` Fourier envelope, the weighted integral is exactly

`2 int_0^u t^(-1/2)dt + 2u^(3/4) int_u^infinity t^(-5/4)dt = 12 sqrt(u)`,

so the stated half-potential constant is correct. Tonelli is used only for nonnegative majorants, including the infinite-value case.

### Lines 161-220 — PASS

The singular-value approximation formula and both nonsymmetric perturbation/rank consequences are correct. The Schur spectral-count lemma is valid: for invertible `A`, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative interlacing separately bounds the number of inverse eigenvalues with modulus `>1/t`, which is equivalent to `N_S(t)>=N_A(t)-k`. The singular case is correctly obtained through `A+epsilon I` and the weakened threshold `t-|epsilon|`. Strict row diagonal dominance is valid without symmetry.

### Lines 221-300 — PASS

The geometric rank-one Brascamp-Lieb heat-flow proof has the correct sign:

`partial_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`,

because the frame map is a contraction. The large-time normalization uses `sum c_i=d`, and the compact-support heat tails justify integration by parts. Monotone truncation handles general nonnegative integrable inputs.

The product-projection lemma integrates the **original product density along orthogonal fibers**; it never treats the rotated coordinates as independent. The one-dimensional scaling factors and entropy bound `-b log b <=1-b` give `||p_(U^T X)||_infinity <= e^(d/2)`.

The scalar Fourier-power estimate is noncircular: `|fhat|^(2m)` is integrable already from Plancherel and `|fhat|<=1`, so inversion at zero is legitimate. Projection of the `2m` original signed coordinates gives the stated constant.

### Lines 301-360 — PASS

The two-copy decoupling is correct. Conditioning/integration over one original block, Cauchy-Schwarz, expansion with an independent copy, and integration over the other original coordinates produce the product Fourier factors. Jensen gives the fourth power. Difference coordinates remain independent and cap one.

The regularized frame `H=alpha I+a^2 M^TM` and weights `c_j,d_i` are correctly normalized. The one-dimensional changes of variables in the BL factors are correct.

### Lines 361-400 — PASS

Using `p=2/d_i` in the scalar Fourier-power bound yields

`||h_i||_(1/d_i) <= (2*pi*sqrt(e d_i))^(d_i)`;

the `d_i` powers cancel the geometric scale factors. The `c_j` entropy contributes `e^(theta/2)`. With `alpha=(2*pi*e)^2`, the remaining multiplier is exactly one. Taking fourth roots gives

`|phi_Z(t)| <= det(I+t^2 M^TM/(pi^2 e^2))^(-1/8)`.

Cauchy-Binet yields the crossing-volume expansion. For order five the tail exponent is `5/4>1`, so absolute Fourier inversion applies and gives `5e Z_5^(-1/10)`. For order three the tail exponent is only `3/4`, which is **not** integrable; multiplying by the Riesz weight `|t|^(-1/2)` changes the tail to `|t|^(-5/4)`, which is integrable. The manuscript keeps these conclusions separate correctly.

### Lines 401-428 — PASS

The square-profile formula and inverse-image length bound are correct. Its later use is a conditional domination statement, not an independence assertion. The definite `2x2` pair calculation has Jacobian `1/(2 sqrt(|det B|))`, hence density cap `pi M/sqrt(|det B|)` after angular integration. Orthogonal diagonalization is only a deterministic change of integration variables.

### Lines 429-484 — PASS

For the indefinite pair the hyperbolic parametrization has absolute `(delta,t)` Jacobian `1/(2 sqrt D)`. Writing a branch as `u e^t+w e^(-t)` gives `|u|=|w|=sqrt(delta Lambda)/2`. Selecting an **original** coordinate of `u` (and, independently, possibly another original coordinate for the negative tail) gives the monotonic-tail estimate. The cutoff `3/4 log 2` is sufficient because `|w_i|/|u_i|<=sqrt 2`. On a monotone tail, cap one plus mass one yields `<=3 log 2`; the middle interval supplies the logarithm. `Lambda>=2/sqrt D` converts the argument to `16 sqrt D/|z-v|`. Rough densities are handled against nonnegative tests, so exceptional critical slices are not selected after conditioning.

### Lines 485-530 — PASS

If no diagonal has modulus at least `||S||/2`, the random-sign split gives a physical cross block of norm at least `||S||/4`. Retaining one singular factor in the determinant theorem yields the quarter-power Fourier envelope. Gaussian smoothing with `v=1/8` gives coefficient

`2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8) = 3.9952593615... <16`.

Layer cake then gives the uniform logarithmic potential `L_0=4+4 log 16`. This step needs only one nonzero spectral direction and does not assert a pointwise quadratic Fourier bound outside the proved cross-block mechanism.

### Lines 531-584 — PASS

The disjoint-minor sampling count is correctly an inequality rather than an equality because singular seeds may admit nonsingular extensions. The nonsymmetric interpolant `P=A[:,T]B^(-1)A[S,:]` agrees with `A` on rows `S` and columns `T`. In the completion, `R-P` is supported in rows `T` or columns `S`, giving global `rank R<=3r`, while `R[L,L]=P[L,L]` gives restricted rank `<=r`; `D` vanishes on the seed exactly. No symmetry is silently imposed on `P,R,E`.

### Lines 585-652 — PASS

For a bad volume ratio, `||E||_F<=(r+1)/80<=1/16`. With `m=4k-3` and `r<=k-1`, singular-value perturbation plus global rank gives at least `m-3r>=r+1` large diagonal entries of `D`, all in `L`. On an `(r+1)`-set of them,

`|R_ii|>=371/400`, while each off-diagonal is `<1/7+1/16`, so the row sum is `<23/28<371/400`. Strict diagonal dominance makes that restricted block rank `r+1`, contradicting `rank R[L,L]<=r`.

The random cut contributes exactly `4^(-k)` per ordered disjoint minor. Thus order three gives `Z_3^(-1/6)<=160` and full half-potential `<200`; order five gives `Z_5^(-1/10)<=160` and density `<=800e<2400`.

### Lines 653-720 — PASS

The two singular-kernel bounds are valid. The near part of `J(d)` is bounded by

`2 asinh(sqrt 2)+pi+2 acosh(sqrt 2)=7.1967714971...<8`,

and the far part is at most `3 log_+(1/|d|)`. The shifted logarithmic kernel is maximized when the superlevel intervals are centered together, giving exactly `8` at center zero.

For a scalar pivot, the Schur complement retains one large eigenvalue under the two-large-eigenvalue hypothesis; quarter-power concentration excludes the exceptional atom and supplies the logarithmic expectation. The resulting scalar-pivot truncated half-potential is `532.7106...<560<600`. Definite and indefinite pair branches have the displayed uniform constants. The use of the full half-potential outside the unit interval contributes at most one, yielding `<=601` under nine large eigenvalues.

### Lines 721-790 — PASS

The main normalized case exhausts all possibilities: no pivot; scalar pivot; definite pair pivot; indefinite pair pivot. The scalar Schur complement retains at least sixteen large eigenvalues and therefore satisfies the nine-eigenvalue half-potential proposition. A principal pair loses at most two large eigenvalues. In the indefinite case the residual Schur complement has norm at least one, so the quarter-power/logarithmic lemma applies. The exact main indefinite numerical upper bound is about `238.9974`, well below `10^4`; the scalar branch is `6010` and is the largest displayed final branch.

General `K,s` scaling is correct, and interval domination is equivalent to an essential density bound by standard outer regularity/Radon-Nikodym domination. The limitations section accurately states that only the no-pivot branch obtains continuity from an integrable characteristic function; the full theorem claims only essential boundedness.

## B15 lens summary: exact analytic thresholds and regularity scope

1. **Gaussian normalization:** PASS. All `2*pi`, `sqrt(pi v)`, and heat-kernel constants are consistent.
2. **Riesz half-potential:** PASS. The coefficient is exactly `1/sqrt(2*pi)` and the order-three weighted tail is integrable because `3/4+1/2=5/4>1`.
3. **Order three:** does **not** give bounded density by absolute inversion; it gives the negative-half-potential estimate used at scalar pivots.
4. **Order four:** the same determinant receiver would give only a `|t|^(-1)` endpoint, which is not absolutely integrable. It cannot by itself justify an `L^infinity` density conclusion.
5. **Order five:** gives `|t|^(-5/4)`, hence an `L^1` characteristic function and a continuous density in the no-pivot branch.
6. **Regularity scope:** the manuscript correctly makes no continuity claim for the pivot branches. The theorem-level conclusion is only existence of an essentially bounded density.

## Numerical checks performed independently in this run

I recomputed, independently of the missing `verify.py/checks.json` package:

- quarter-power coefficient: `3.9952593615816134 < 16`;
- near-region `J` constant: `7.196771497190057 < 8`;
- `L_0=4+4 log 16 = 15.090354888959125`;
- scalar-pivot truncated-half-potential bound: `532.7106466687737 < 560`;
- indefinite-pivot truncated-half-potential bound from the displayed estimate: `432.375066654277 < 444`;
- no-pivot nine-direction full half-potential: `176.959336187295 < 200`;
- no-pivot seventeen-direction density: `2174.625462767236 < 2400`;
- main indefinite-pair branch: `238.997315553161 < 251`.

These numerical recomputations are diagnostics only; the symbolic proof above is the basis for PASS.

## GAP / FALSE / UNCHECKED ledger

- `manuscript.tex` lines 1-790: **PASS**.
- `README.md`: **GAP** in package description because it names four supplementary files absent from fresh `master`; theorem/status description otherwise consistent with source.
- package `AUDIT.md`: mathematical self-audit text is consistent with the source, but its finite-check coverage is **UNCHECKED** here because the checker/results it cites are absent.
- `SOURCE_MANIFEST.json`: **UNCHECKED/MISSING** (404; absent from fresh root listing).
- `proof_map.csv`: **UNCHECKED/MISSING**.
- `verify.py`: **UNCHECKED/MISSING**.
- `checks.json`: **UNCHECKED/MISSING**.
- FALSE mathematical claims found: **none**.

## Downstream impact and next obligations

The baseline 17-eigenvalue candidate is mathematically sound on this audit and can remain the proof baseline. The package should later restore or correct the four promised supplementary artifacts, but that is not a proof repair.

No multiplicity reduction is certified by this audit. The current proof's no-pivot bottleneck is precise: order four corresponds to thirteen spectral directions algebraically but reaches only the nonintegrable `1/|t|` Fourier endpoint. Any `17 -> 13` improvement needs an endpoint/cancellation argument or a different structural receiver; simply reusing absolute inversion is insufficient.

I supply a separate immutable B15 improvement artifact proving (i) a self-contained order-four `L^2` endpoint under thirteen large eigenvalues in the no-pivot chamber and (ii) explicit `C^{0,1/4}` regularity in the existing order-five no-pivot chamber. Neither is relabeled as a lower-multiplicity `L^infinity` theorem.
