# fleet02 / B03 independent fixed-multiplicity audit

Run: `20260924T121241Z-fleet02-B03-fixed-multiplicity-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Lens: decoupling, copies, conditional independence, Fourier exponents; fleet02 counterexample stress-testing.

## Source pin and scope

I froze the mathematical source at the master snapshot observed at audit start:

- repository: `yspennstate/math-open-problems`
- branch: `master`
- audit-start master commit: `a0cdb4f53dfbbec72979d5c7c0c95da061c283c6`
- manuscript initial source commit named by the package: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
- `manuscript.tex` git blob at both commits: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- package-declared manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

The blob equality was independently checked through GitHub. The SHA-256 above is the package-declared value; this connector run did not independently recompute SHA-256 from local bytes.

I read `manuscript.tex` in full, lines 1--790, plus the package `README.md` and `AUDIT.md`. Direct retrieval of `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` returned 404 at the frozen master snapshot; `SOURCE_MANIFEST.json` and `proof_map.csv` also returned 404 at the initial source commit. Accordingly, the mathematical manuscript was audited end-to-end, but claims depending on those absent supplementary files are UNCHECKED.

## Verdict

**PASS for the written 17-eigenvalue theorem at this B03 review.** I found no mathematical gap in the manuscript's proof that independent real coordinate densities bounded by `K`, arbitrary symmetric `A` with `s_17(A)>=s>0`, and arbitrary affine `b,c` give `||p_Q||_infty <= 10000 K^2/s`.

This is one worker review, not a release certificate. It does not by itself satisfy the owner's requirement for two genuinely separate complete reviews, and it does **not** prove the unrestricted three-eigenvalue conjecture.

**GAP in package reproducibility:** the README/AUDIT describe four supplementary files that are not present at the pinned source. This does not invalidate the self-contained proof in `manuscript.tex`, but it prevents independent execution of the advertised finite checks and prevents line-map verification from `proof_map.csv`.

No threshold reduction is claimed in this run. The most immediate attempted reduction, replacing order five by order four, hits an exact Fourier endpoint: the determinant theorem gives only `|phi(t)| <= C |t|^{-1}` at order four, which is not integrable. Therefore the existing argument does not lower 17 to 13 without an additional source of decay or a different structural/analytic receiver.

## Complete manuscript line coverage

Every source line 1--790 was read. The block table below is exhaustive; detailed sensitive checks follow it.

| Source lines | Content | Status | Audit result / next obligation |
|---|---|---|---|
| 1--80 | preamble, definitions, Theorem 1, Corollary, parameters, proof architecture | PASS | Quantifiers, essential-supremum formulation, arbitrary affine terms, signs and rough laws are stated consistently. Threshold accounting `9=4*3-3`, `17=4*5-3` matches later proof. |
| 81--160 | Fourier conventions, Plancherel/inversion, Gaussian identity, power envelope, half-Riesz bound | PASS | Fourier normalization and constants re-derived; no smoothness or moment assumption is introduced. |
| 161--240 | singular values/rank perturbation, Schur spectral count, diagonal dominance, start of geometric BL heat flow | PASS | Schur count checked including singular limiting case; nonsymmetric singular-value perturbation is used legitimately. |
| 241--320 | completion of geometric BL, product-projection bound, scalar Fourier powers, cross-form and decoupling statement | PASS | Heat-flow limits and rough-function truncation are sound. Projection proof is an integral change of variables, not post-rotation independence. |
| 321--400 | decoupling proof, regularized determinant theorem, crossing volumes and Fourier envelopes | PASS | Copy dependence and all square/fourth-root exponent transfers checked in detail below. |
| 401--480 | scalar square profile, definite pair, first part of hyperbolic-pair proof | PASS | Conditioning is on original coordinates. Deterministic rotations are not treated as independent random coordinates. |
| 481--560 | hyperbolic tails, quarter-power concentration, pivot/volume definition, start of sampled interpolation | PASS | Hyperbolic Jacobian and tail change of variables checked; random-sign split is deterministic after the existence argument. |
| 561--640 | sampling completion, `A=D+R+E`, global/restricted ranks, spectral-to-volume, random cut, no-pivot consequences statement | PASS | Ordered-minor multiplicity, nonsymmetric support, `rank R<=3r`, `rank R[L,L]<=r`, `D=0` on seed and diagonal-dominance contradiction all checked. |
| 641--720 | no-pivot constants, truncated half potential, singular kernels, pivot half-potential, start of nine-eigenvalue proposition | PASS | Full versus truncated half potentials are kept distinct; conditional Tonelli use is valid. |
| 721--790 | nine-eigenvalue completion, main theorem, scaling, dependency table, limitations and references | PASS | Main branching and `K,s` scaling checked. Continuity is not overclaimed. References are attribution rather than hidden proof dependencies. |

## B03 decoupling / copy / independence audit

### `lem:decoupling`, `eq:decouple2`, `eq:decouple4` — PASS

For
`Z=F(X_I)+2 X_I^T M X_J+G(X_J)`, the proof first applies Cauchy--Schwarz in the genuine product law of `X_I`, then expands the squared inner expectation with an independent copy `X'_J`. Integration over the genuinely independent original coordinates `X_i`, `i in I`, produces the product of scalar Fourier transforms at `2t(MD)_i`, where `D=X_J-X'_J`.

The residual phase `exp(it(G(X_J)-G(X'_J)))` is **not** claimed to depend only on `D`, and is **not** claimed independent of `D`; it is removed only after taking absolute values. This is the correct dependence-preserving step.

The vector `D` has independent coordinates because its coordinate pairs `(X_j,X'_j)` are independent across `j`. Each difference density satisfies
`g_j(d)=int f_j(x)f_j(x-d) dx <= ||f_j||_infty <=1`.

The fourth-power step is also exact: writing the nonnegative product as `P(D)`,
`|phi|^2 <= E P`, hence `|phi|^4 <= (E P)^2 <= E P^2` by Jensen. There is no hidden independence inserted between factors of `P`.

**Counterexample stress:** if `X,X'` are independent uniform variables on `[-1/2,1/2]`, then `D=X-X'` and `S=X+X'` have joint support `|D|+|S|<=1`, so they are not independent. Any derivation that separated a copy difference from its conjugate sum would be false for the allowed laws. The manuscript never makes that separation.

### `lem:scalar-fourier` — PASS

`|fhat|^(2m)` is the characteristic function of a sum of `m` independent whole differences, built from `2m` genuinely independent original/copy coordinates. The projection lemma is applied to those original coordinates, not to rotated differences. Integrability follows from `|fhat|^(2m)<=|fhat|^2` and Plancherel. The exponent comparison `m=floor(p/2)>=p/4` gives the stated constant.

### `thm:determinant` — PASS

The regularized frame uses
`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`, with `alpha=(2*pi*e)^2` and `H=alpha I+a^2M^TM`.
The outer products sum exactly to the identity; `0<c_j<=1`, `0<=d_i<=1`, and `theta=sum d_i=sum(1-c_j)`.

After the BL step, `g_j<=1` gives `||g_j||_(1/c_j)<=1`, while the scalar Fourier power bound at `p=2/d_i` gives
`||h_i||_(1/d_i) <= (2*pi*sqrt(e d_i))^(d_i)`.
The `d_i` powers cancel; the entropy term is at most `e^(theta/2)`; and the choice of `alpha` makes `(2*pi*e/sqrt(alpha))^theta=1`. Thus the BL integral has determinant power `-1/2`. Taking the fourth root dictated by `eq:decouple4` gives exactly the final determinant exponent `-1/8`. No factor of two or square root is missing.

### Crossing-volume exponent transfer — PASS, with a sharp barrier to the naive 13-direction reduction

Keeping the order-`k` term in
`det(I+zM^TM)` yields
`|phi_Z(t)| <= min(1,(u_k/|t|)^(k/4))`.

- `k=5`: exponent `5/4>1`, so direct Fourier inversion is legitimate and gives the bounded density estimate.
- `k=3`: exponent `3/4`; it is not enough for direct inversion, but after multiplying by the half-Riesz weight `|t|^-1/2`, the tail exponent is `5/4>1`, giving the full negative-half potential.
- `k=4`: exponent is **exactly 1**. `int_1^infty t^-1 dt` diverges. Therefore the existing determinant-envelope route cannot replace `k=5` by `k=4`. Since the structural lemma would give order four from `s_13`, this is a genuine endpoint obstruction to the immediate `17 -> 13` reduction, not a proof that 13 is impossible.

**Next obligation for lowering 17:** supply extra decay/cancellation at the order-four endpoint, or a replacement structural/analytic route. A lower threshold must retain arbitrary affine terms, arbitrary rough product laws, all signatures and arbitrary residual spectrum.

## Conditioning and independence elsewhere

- **Product projections — PASS.** Completing `U` to an orthogonal matrix is used only as a deterministic Jacobian in the marginal integral. The proof never asserts that `U^TX` and `W^TX` are independent.
- **Scalar pivot profile — PASS.** Conditioning on `X_-i` leaves the original coordinate `X_i` independent of the conditioning sigma-field. The displayed profile is a conditional measure domination; the manuscript explicitly does not claim independence of the completed square and Schur-complement residual.
- **Definite pair — PASS.** The pair consists of two original independent coordinates after conditioning on the complement; orthogonal diagonalization is inside the two-dimensional deterministic integral only.
- **Hyperbolic pair — PASS.** The original two coordinates remain independent; the eigenbasis parameterizes a level set but is never assigned a product law. Tail control deliberately returns to one original coordinate density `f_i<=1`.
- **Indefinite pair in the main theorem — PASS.** The critical value depends on the conditioned complement. The argument averages conditional measure bounds by Tonelli and never requires the critical value to be independent of the pair or to have a conditional density inherited from an unconditional projection.
- **Random coordinate cut — PASS.** The random cut is a deterministic/probabilistic existence device for the coefficient matrix. Once a cut is fixed, the two banks are disjoint original-coordinate blocks and therefore independent.

## Other sensitive proof checks

### Fourier normalization and half-Riesz constant — PASS

With `fhat(t)=int e^(itx) f(x)dx`, Plancherel is `int |fhat|^2=2*pi int|f|^2` and inversion is `(2*pi)^-1 int e^-itx fhat(t)dt`. The Gaussian regularization in `eq:gaussian-inversion` is consistent with this normalization. The gamma representation of `|z|^-1/2`, followed by the Gaussian identity, yields the factor `1/sqrt(2*pi)` in `eq:riesz`.

### Geometric BL heat flow — PASS

The heat-flow differentiation gives
`d_t F-Delta F = F(sum c_i v_i^2-|sum c_i u_i v_i|^2)>=0`, because the matrix with columns `sqrt(c_i)u_i` is a coisometry. Compact support supplies Gaussian domination for differentiation/integration by parts. The `t->infinity` scaling uses `sum c_i=d`; the `t->0` step uses Lebesgue points and Fatou. Truncation/monotone convergence extends to arbitrary nonnegative integrable functions.

### Schur spectral count — PASS

For invertible `A`, the complementary principal block of `A^-1` is `S^-1`. Positive and negative interlacing for principal compressions bounds the number of inverse eigenvalues outside `[-1/t,1/t]`, which is equivalent to `N_S(t)>=N_A(t)-k`. The singular case is correctly obtained from `A+epsilon I` with threshold `t-|epsilon|`; equality-at-threshold is retained in the limit.

### Hyperbolic envelope — PASS

The `(delta,t)` Jacobian on each branch is `1/(2 sqrt(D))`. The tail argument chooses a large component of the deterministic coefficient `u` in an **original coordinate**, obtains monotonicity and `|w_i'(t)|>=|w_i(t)|/3`, and spends only the original cap and unit mass. The two tails and middle interval lead to the stated logarithm; `Lambda>=2/sqrt(D)` converts it to the final `16 sqrt(D)/|z-v|` scale. Exceptional critical levels are handled at the measure/test-function level.

### Nonsymmetric interpolation and rank accounting — PASS

The sampled interpolant `P=A[:,T] B^-1 A[S,:]` need not be symmetric. The bordered determinant identity is exact for nonsingular seeds; sorting signs disappear after squaring. An ordered `(r+1,r+1)` disjoint minor is counted at most `(r+1)^2` times, so the claimed inequality (not equality) is correct.

In `A=D+R+E`, `E` is supported only on the off-diagonal part of the seed complement and has zero diagonal; `D` is diagonal and vanishes on `S union T`. The support of `R-P` is contained in rows `T` or columns `S`, giving the global `rank R<=3r`; simultaneously `R[L,L]=P[L,L]`, giving the sharper `rank R[L,L]<=r`. Neither estimate uses symmetry of `R` or `E`.

### Spectral-to-volume contradiction — PASS

If `V_{r+1}<kappa V_r`, then `||E||<=||E||_F<=(r+1)/80<=1/16`. With `m=4k-3` and `r<=k-1`, `m>=4r+1`. Rank perturbation by the global rank `3r` forces at least `r+1` diagonal entries of `D` of size at least `1-epsilon`; they lie in `L` because `D` vanishes on the seed. On those coordinates,
`|R_ii|>=371/400`, while each off-diagonal entry is `<1/7+1/16`, so even for `r=4` the off-diagonal row sum is `<23/28<371/400`. Strict diagonal dominance gives rank `r+1`, contradicting the restricted rank bound `<=r`.

### Full versus truncated half potentials — PASS

`prop:pivot-H` proves only the truncated potential `H(Q)<=600`. `prop:nine` combines the pivot branch with the no-pivot **full** potential estimate and then adds at most one for the tail `|Q-a|>1`, giving the full `<=601`. The scalar-pivot branch of the main theorem invokes this full `601` bound, not the truncated `600` bound. No truncation mismatch was found.

## Independent constant checks

The loose numerical inequalities used in the manuscript have comfortable slack. Independently recomputed values include:

- `12*sqrt(80e) = 176.959336187... < 200`;
- `800e = 2174.625462767... < 2400`;
- `L0=4+4 log 16 = 15.090354889...`;
- scalar-pivot truncated bound `10*(8+3L0) = 532.710646669... < 560`;
- indefinite-pivot truncated bound from the displayed estimate is `432.375066654... < 444`;
- main indefinite-pair bound from the displayed estimate is `238.997315553... < 251`;
- the diagonal-dominance slack is `371/400-23/28=297/2800>0`.

These arithmetic checks support, but do not replace, the proof audit.

## Package-file audit

| Package item | Status | Reason / impact / repair |
|---|---|---|
| `README.md` theorem/source-pin description | PASS | Matches the manuscript theorem and source blob. |
| `README.md` statement that `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json` are canonical package contents | **FALSE as a repository-state claim at the pinned source** | Direct fetches return 404. Repair by adding the promised immutable files or amending the package description. |
| `AUDIT.md` mathematical self-audit narrative | UNCHECKED as author-review evidence; not used as proof | I independently checked the manuscript instead of inheriting its verdict. |
| `AUDIT.md` claims about finite test counts and `verify.py`/`checks.json` | **UNCHECKED / GAP** | Supporting checker and result files are absent, so these diagnostics are not reproducible in this run. |
| `SOURCE_MANIFEST.json` | GAP / missing | Cannot independently audit its claimed hashes/review state. |
| `proof_map.csv` | GAP / missing | Cannot verify package-provided statement-to-line mapping. This review supplies exhaustive line-block coverage instead. |
| `verify.py` | GAP / missing | Cannot execute advertised finite checker. |
| `checks.json` | GAP / missing | Cannot compare recorded numerical results to checker output. |
| `manuscript.tex` | PASS | Full 790-line end-to-end proof audit completed. |

The missing supplementary files are a **reproducibility/package-integrity defect**, not a mathematical counterexample to Theorem 1, because every specialized mathematical dependency needed by the proof is actually proved in `manuscript.tex`.

## Dependency closure and lower-threshold status

The checked proof dependency chain is closed at 17:

`product densities -> geometric BL/product projection -> scalar Fourier powers -> copy-safe decoupling -> regularized crossing determinant -> crossing-volume envelopes`, together with
`sampled disjoint minors -> nonsymmetric completion with global/restricted rank -> no-pivot volume`, and the pivot side
`square/definite/hyperbolic conditional envelopes -> quarter concentration/log potential -> nine-eigenvalue full half potential -> scalar-pivot closure`.

The main no-pivot density branch specifically requires order five because the determinant theorem contributes `k/4` Fourier decay. The structural theorem at order five costs `4*5-3=17`. At order four the direct density exponent is exactly one and fails absolute integrability. I therefore do **not** publish a 13-, 16-, 9-, or 3-eigenvalue replacement theorem from this run.

Next proof obligation for a genuine reduction: either (i) gain any uniform positive amount beyond `|t|^-1` at the order-four endpoint while preserving arbitrary product laws and self-blocks, (ii) improve the structural interpolation/rank count while retaining a fifth-volume receiver, or (iii) replace the fifth-volume density inversion with a different complete receiver. Any such change needs a full replacement proof, constants, and dependency map before the threshold is changed.

## Final audit status

- manuscript mathematical baseline: **PASS in this independent B03 review**;
- fatal mathematical gap found: **none**;
- package reproducibility: **GAP** because four advertised supplementary files are absent;
- threshold improvement below 17: **not proved**;
- unrestricted three-eigenvalue QFORM: **OPEN / not claimed solved**.
