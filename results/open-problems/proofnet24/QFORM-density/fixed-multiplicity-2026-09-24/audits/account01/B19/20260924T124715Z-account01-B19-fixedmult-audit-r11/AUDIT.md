# account01/B19 independent end-to-end audit — fixed multiplicity 17

Run: `20260924T124715Z-account01-B19-fixedmult-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Lens: independent full proof reconstruction, then guarded integration of proved repairs/improvements.

## Source pin and fatal-gap-first verdict

Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.  
Audited file: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.  
Observed git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Package-recorded SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`; this connector-only run did **not** independently recompute the raw-byte SHA-256, so only the git blob is independently pinned here.  
Fresh master head observed during the audit: `7e2bfa6deed6d8a3e8e1c8a08fd4afb490f46f81`; `manuscript.tex` on that head still had the same blob `183ccd...`.

**Fatal mathematical gaps: NONE FOUND.** My independent reconstruction gives **PASS** for the complete written 17-eigenvalue candidate

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for independent arbitrary real coordinate laws with densities bounded by `K`, arbitrary real symmetric `A`, all signatures and remaining spectra, and arbitrary affine `b,c`.

This is one independent audit. It is **not** a self-awarded independent-validation certificate and it does not prove the unrestricted three-eigenvalue conjecture.

## Package defects / omissions

**FALSE (current README inventory):** on fresh `master`, direct retrieval of `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` from the manuscript root returned 404, although `README.md` lists all four as canonical package members. The root files actually retrievable in this run included `README.md`, `AUDIT.md`, `manuscript.tex`, and audit/improvement directories.

**UNCHECKED:** the finite-test counts and recorded `verify.py` results quoted in `AUDIT.md` cannot be independently rerun or inspected here because `verify.py` and `checks.json` are absent. They are not used as proof evidence in this audit.

**GAP-PRESENTATION, theorem unaffected:** the theorem assumes density caps a.e., while several inverse-branch/coarea formulas later display pointwise values of rough densities. A uniform convention fixes this: replace each marginal density by a Borel representative equal a.e. to the original and clipped pointwise to `[0,K]`. This does not change any law and makes every later pointwise bound literal. The projection proof already makes this choice locally. Conditional domination can equivalently be stated only against nonnegative Borel test functions, avoiding exceptional-slice choices entirely.

## Complete line-by-line audit ledger

Every source line 1–790 is covered below. `PASS` means I reconstructed the argument and checked each invoked hypothesis; `UNCHECKED` means the stated evidence was unavailable rather than false.

| Source lines | Status | Independent check and reason | Downstream effect |
|---|---|---|---|
| 1–45 | PASS | Preamble/abstract state exactly the candidate: independent rough product laws, `s_17`, arbitrary affine terms, dimension/signature uniformity. No hidden moment/support/smoothness hypothesis. | None. |
| 46–83 | PASS | Singular-value convention, theorem quantifiers, `eta=1/100`, `kappa=1/80^2`, pivot definition and accounting `9=4*3-3`, `17=4*5-3` are consistent. Normalized proof target is `K=s=1`. | Main scope preserved. |
| 84–160 | PASS | Fourier convention, Gaussian approximate identity, Plancherel factor `2 pi`, inversion factor `1/(2 pi)`, Gaussian inversion factor `1/(2 sqrt(pi v))`, power-envelope integral and Riesz half-potential normalization all check. Extended Tonelli is only applied to nonnegative quantities. The `3/4` envelope gives weighted integral exactly `12 sqrt(u)`. | Supplies all rough-law Fourier/Riesz inputs. |
| 161–220 | PASS | Singular-value perturbation and low-rank inequalities are valid for nonsymmetric matrices. For an invertible symmetric pivot, `S^{-1}` is the complementary principal compression of `A^{-1}`; positive and negative interlacing separately yield `N_S(t)>=N_A(t)-k`. The `A+epsilon I` passage gives the singular case. Strict row diagonal dominance is valid without symmetry. | Every later Schur count has the correct loss. |
| 221–282 | PASS | Geometric rank-one Brascamp–Lieb heat flow has the correct sign because the frame map is a contraction; `sum c_i=d`, the large-time Gaussian limit and compact-support domination are correct, then monotone truncation handles general integrable inputs. Product projection integrates the original product density over deterministic orthogonal fibers; no rotated independence is asserted. Rows with `b_i=0` are harmless. Mathematically one may write `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`; this is the only wording point worth making explicit. | Projection density `<=e^{d/2}` is valid. |
| 283–300 | PASS | For `m=floor(p/2)`, `|fhat|<=1` gives the reduction to exponent `2m`; `|fhat|^{2m}` is integrable, Fourier inversion at zero is noncircular, and the product-projection scalar bound gives `2 pi sqrt(2e)/sqrt(p)`. Difference densities remain cap one by convolution. | Scalar Fourier-power input valid. |
| 301–328 | PASS | Cauchy–Schwarz in one physical bank plus an independent copy of the other gives the power-2 decoupling inequality; Jensen gives power 4. All pre-estimate integrands have modulus at most one, so no moments enter. | Product provenance preserved. |
| 329–379 | PASS | In the graph-BL proof, `H=alpha I+a^2M^TM`, weights `c_j,d_i` form a Parseval frame and `theta=sum d_i=sum(1-c_j)`. The Jacobian, one-dimensional rescalings, `p=2/d_i`, cancellation of `d_i` powers, entropy bound and `alpha=(2 pi e)^2` cancellation are all correct. Taking fourth roots gives exponent `-1/8` and coefficient `t^2/(pi^2 e^2)`. Zero rows/zero singular values are harmless by omission/continuity. | Determinant theorem valid without leverage/sign assumptions. |
| 380–400 | PASS | Cauchy–Binet gives `det(I+zM^TM)=sum z^k Z_k`; retaining order `k` gives exponent `k/4`. `k=5` is integrable and yields `5e Z_5^{-1/10}`; `k=3` is used only with the Riesz weight and yields the stated half-potential. | No improper direct density inference from order 3. |
| 401–428 | PASS after representative convention | Scalar square inverse branches and interval-preimage length are correct. The conditional profile is a domination of measures, not an independence assertion. The definite-pair polar change of variables has Jacobian `1/(2 sqrt(|det B|))` and integrates to `pi M/sqrt(|det B|)`. | Rough-law pivot branch valid. |
| 429–484 | PASS after representative convention | Hyperbolic coordinates have Jacobian `1/(2 sqrt D)`. Each branch is `u e^t+w e^{-t}` with `|u|=|w|=sqrt(delta Lambda)/2`; an original coordinate carries at least the stated amplitude. Beyond the cutoff it is one-sign monotone with derivative comparable to magnitude. The bathtub bound uses only density cap one plus total mass one. The middle interval yields the logarithm and `Lambda>=2/sqrt D` gives the final scale. Negative level handled by sign swap. | Uniform log envelope sound for arbitrary rough laws. |
| 485–530 | PASS | If no large diagonal, random signs isolate a literal physical cross block with norm at least `L/4`. Retaining one determinant singular-value factor yields `|t|^{-1/4}`; Gaussian smoothing gives the quarter-power concentration. The numerical coefficient is actually about `3.99526<16`. Layer cake gives `L0=4+4 log 16`; atoms are excluded by shrinking the radius. | One surviving spectral direction controls the log potential. |
| 531–584 | PASS | Ordered disjoint-minor definition is consistent. Volume-sampled interpolation uses exact bordered determinants. Singular seeds can have nonsingular extensions, so the aggregate count is correctly an inequality. `P=A[:,T]B^{-1}A[S,:]` can be nonsymmetric but has rank `<=r`, interpolates rows `S` and columns `T`; completion has `D=0` on the seed, zero-diagonal `E`, full `rank R<=3r`, and restricted `rank R[L,L]<=r`. | Both rank bounds are established with exact support. |
| 585–621 | PASS | A bad telescoping volume ratio gives `||E||_F<=(r+1)/80<=1/16`. With `m=4k-3` and `r<=k-1`, low-rank perturbation forces at least `r+1` diagonal entries of `D` of modulus `>=1-epsilon`, all in `L`. On that set `|R_ii|>=371/400`, while each off diagonal is `<1/7+1/16`; for `r<=4`, row sum `<23/28`. Exact slack `371/400-23/28=297/2800>0`, contradicting `rank R[L,L]<=r`. The `r=0` Frobenius branch is also correct. | Spectral-to-volume proposition valid through `k=5`. |
| 622–651 | PASS | Fair cut retains each ordered disjoint pair with probability `4^{-k}`. Thus `Z_k^{-1/(2k)}<=160`; `k=3` gives `12 sqrt(80e)<200`, and `k=5` gives `800e<2400`. All self/cross/affine terms remain in the actual cross-form functions. | No-pivot 9-half-potential and 17-density branches close. |
| 652–681 | PASS | Both singular-kernel bounds are correct by the stated near/far split and interval-overlap/Tonelli argument. | Kernel constants safe. |
| 682–721 | PASS | Scalar pivot plus one surviving Schur direction gives truncated half-potential; definite pair is direct; indefinite pair uses the log kernel and scalar maximum. The three pivot cases exhaust the pivot definition. For `s_9>=1`, the pivot case controls the truncated potential and the outside part costs `<=1`; no-pivot already controls the full potential. | Nine-direction full half-potential `<=601` is valid. |
| 722–763 | PASS | Main case split is exhaustive. No pivot: `<2400`. Scalar pivot: Schur count loses one and still leaves at least nine directions, giving `<=6010`. Definite pair: `<40`. Indefinite pair: pair removal leaves a nonzero Schur direction and the logarithmic potential closes. Conditional critical values are handled by integrated domination/Tonelli. | Normalized theorem closes. |
| 764–774 | PASS | Scaling `Y=KX` makes cap one and `tilde Q=(K^2/s)Q` with quadratic matrix `A/s`; density scaling gives `K^2/s`. `s_17>=s_33` proves the corollary. Interval domination and essential-density equivalence are standard. | General theorem closes. |
| 775–790 | PASS for mathematical scope; bibliography existence PASS, priority UNCHECKED | Threshold accounting accurately distinguishes order 5 density from order 3 half-potential. The manuscript explicitly does not claim the `s_3` theorem or global continuity. The two cited papers/titles/authors exist as stated, but this run is not a comprehensive novelty/priority review. | No proof dependency on external results because specialized inputs are reproved. |

## Equation-level dependency audit

The dependency-critical displayed statements were independently checked with their exact hypotheses: `eq:plancherel`, `eq:inversion`, `eq:gaussian-inversion`, `eq:envelope`, `eq:riesz`, `eq:riesz-power`, `eq:rank-perturb`, `eq:frame`, `eq:bl`, `eq:projection`, `eq:scalar-fourier`, `eq:decouple2`, `eq:decouple4`, `eq:determinant`, `eq:graph-bl`, `eq:Zk`, `eq:det-expand`, `eq:vol-envelope`, `eq:five-volume`, `eq:three-volume`, `eq:profile`, `eq:hyperbola`, `eq:quarter`, `eq:log-bound`, `eq:Vr`, `eq:small-entry`, `eq:P`, `eq:sampling`, `eq:completion`, `eq:completion-bounds`, `eq:volume-lower`, `eq:cut`, `eq:no-pivot-nine`, `eq:no-pivot-seventeen`, `eq:H`, `eq:J`, `eq:log-kernel`, `eq:pivot-H`, `eq:scalar-max`, `eq:nine-H`, and `eq:final-scalar`.

The most failure-sensitive points were checked explicitly:

1. **Nonsymmetric interpolation:** only singular-value/rank facts are used on `A-E`, `R`, `P`; no eigenvalue theorem is applied to them.
2. **Seed support:** forced large entries of `D` are in `L` because `D` vanishes on `S union T`, exactly where `rank R[L,L]<=r` applies.
3. **Schur counts:** all pivots used for Schur complements are genuinely invertible; loss is exactly pivot size.
4. **Rough laws:** conditioning remains on original coordinates; no density cap is inferred for an arbitrary rotated conditional law.
5. **Full vs truncated half-potential:** the proof adds the outside contribution `<=1`; it never silently identifies them.

## Independent constant check and same-proof strengthening

Direct recomputation gives

\[
L_0=4+4\log16=15.0903548889\ldots,
\]

and the scalar-pivot truncated half-potential actually satisfies

\[
H_* =10(20+12\log16)=532.7106466687\ldots .
\]

This dominates the other nine-direction branches. Therefore

\[
\sup_a \mathbb E|Q-a|^{-1/2}
\le 1+H_*=201+120\log16,
\]

and the main scalar branch is bounded by

\[
10(201+120\log16)
=2010+1200\log16
=5337.1064666877\ldots<5610.
\]

The no-pivot density branch is `800e=2174.62546...`; the definite and indefinite pair branches are smaller. Thus the **same proof, with no hypothesis change**, yields the stronger universal fixed-17 bound

\[
\boxed{\|p_Q\|_\infty\le(2010+1200\log16)K^2/s<5610K^2/s.}
\]

This strengthening is recorded separately in this run's improvement artifact; it does not lower multiplicity.

## Guarded peer integration only after independent baseline reconstruction

I then read current peer mathematics, treating it as input to check rather than validation. An account02/B19 construction gives an exact saturation of the manuscript completion already for `r=1`: with

\[
A_0=\begin{pmatrix}
-3&1&-3&-3\\
1&-3&-3&-3\\
-3&-3&10&9\\
-3&-3&9&9
\end{pmatrix},\quad S=\{1\},\ T=\{2\},
\]

the manuscript interpolation has `E=0`, `D=diag(0,0,1,0)`, `rank R=3=3r`, and `rank R[L,L]=1=r`. I independently recomputed these ranks and `det A_0=144`. Scaling preserves the rank saturation and can place the example inside the local no-pivot small-entry class. Hence simply improving the completion ranks is not a valid route to `17 -> 16`.

Applied to the actual attempted terminal inequality, under only `s_16(A)>=1` at `r=4`, the manuscript gives

\[
m-3r=16-12=4,
\]

so only four large diagonal residuals are forced, exactly matching the allowed restricted rank four. No contradiction follows. Current peer refinements produce additional terminal structure (an exact 8-versus-8 Schur saturation and strictly heavier neighboring four-minors), but do not establish the missing good-seed transfer. Therefore a full `s_16` theorem is still **GAP**, not a proved improvement.

## Final status

- Mathematical 17-eigenvalue manuscript: **PASS in this audit**.
- Fatal proof gap: **none found**.
- Current stated `10000 K^2/s`: **PASS**, with same-proof improvement `<5610 K^2/s`.
- README package inventory for four auxiliary files: **FALSE on fresh master**.
- Finite-test/checker evidence depending on absent files: **UNCHECKED**.
- Rough-density representative issue: **GAP-PRESENTATION**, repaired without changing theorem.
- Unconditional multiplicity 16 or 13: **GAP / not proved**.
- Full three-eigenvalue conjecture: **OPEN**.
- Independent-validation status: **not self-awarded by this run**; peer PASS assertions are not promoted into a certificate.
