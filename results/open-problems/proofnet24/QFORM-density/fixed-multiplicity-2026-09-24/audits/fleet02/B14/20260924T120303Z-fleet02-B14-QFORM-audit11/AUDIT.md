# fleet02/B14 independent end-to-end audit — fixed multiplicity 17

Run: `20260924T120303Z-fleet02-B14-QFORM-audit11`

Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned mathematical source: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`. The same blob remained on fresh master during this review.

## Verdict

**Mathematical verdict: PASS.** I read the full 790-line manuscript independently and reconstructed every specialized analytic/algebraic step used by the theorem. I found no fatal mathematical gap in the statement: independent real coordinate densities `<=K`, arbitrary real symmetric `A` with `s_17(A)>=s>0`, arbitrary affine `b,c` imply an essentially bounded density with the manuscript's bound `10000 K^2/s`.

This is one independent review, not a self-awarded validation certificate and not a proof of the unrestricted three-eigenvalue conjecture.

**Packaging verdict: GAP, non-mathematical.** On fresh master the advertised `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` were absent from the manuscript root, although README/AUDIT refer to them. I therefore did not treat the advertised finite checks as independently rerun evidence. The theorem proof itself is self-contained in `manuscript.tex`.

**Rough-law presentation patch: GAP-PRESENTATION / theorem unaffected.** The statement assumes density caps only almost everywhere, while some later formulas write pointwise values of one-dimensional density representatives along inverse branches/level curves. A global convention suffices: for each marginal choose a Borel representative equal a.e. to the given density and truncate it pointwise into `[0,K]`. This leaves the law unchanged and gives the pointwise cap used later. The manuscript already makes this choice locally in the projection lemma; making it global removes representative ambiguity.

## End-to-end source audit

### Lines 41–80: statement, normalization and architecture — PASS

The quantifiers retain arbitrary dimension, signature, affine terms, rough independent laws and the remaining spectrum. For `Y=KX`, the coordinates of `Y` have density cap one and `Q=(s/K^2) \widetilde Q` with quadratic matrix `A/s`, so the final density scales by `K^2/s`. No continuity is claimed outside the integrable-Fourier branch.

### Lines 81–160: Fourier identities, inversion and negative half moments — PASS

The Gaussian approximate-identity proof of Plancherel is valid for `L1 cap L2` inputs. The inversion argument passes through the convolved laws and weak convergence, so it does not presuppose a density for the original law. The power-envelope integral is `2ap/(p-1)`, hence the density bound `ap/[pi(p-1)]`. The gamma/Gaussian derivation of

`E|Z-a|^{-1/2} <= (2pi)^(-1/2) int |t|^{-1/2}|phi_Z(t)| dt`

is Tonelli-safe; the `3/4` envelope gives the exact weighted integral `12 sqrt(u)`.

### Lines 161–220: singular values, Schur counts and diagonal dominance — PASS

The nonsymmetric singular-value approximation/rank inequalities are used with the right index direction. For invertible ambient `A`, `S^{-1}` is the complementary principal block of `A^{-1}`, and positive/negative interlacing gives `N_S(t)>=N_A(t)-k`.

I specifically rechecked the manuscript's short singular-ambient paragraph. It is mathematically sufficient as written. From

`N_{S_epsilon}(t-|epsilon|) >= N_A(t)-k`,

let `q=N_A(t)-k`. The `q`-th ordered eigenvalue modulus of `S_epsilon` is at least `t-|epsilon|`; because `S_epsilon -> S`, continuity of the ordered moduli gives the `q`-th ordered modulus of `S` at least `t`. Thus `N_S(t)>=q`. A separately posted fixed-`delta` replacement proof is a valid clarity patch, but the moving-threshold passage is not a mathematical failure once this ordered-modulus sentence is made explicit.

Strict row diagonal dominance is correctly applied to nonsymmetric matrices.

### Lines 221–282: geometric Brascamp–Lieb and product projections — PASS

The heat-flow sign is correct:

`partial_t F - Delta F = F(sum c_i v_i^2 - |sum c_i u_i v_i|^2) >=0`.

The frame identity makes the relevant map a contraction. The large-time scaling uses `sum c_i=d`, and compact support supplies a Gaussian dominating function. The `t downarrow 0` step uses Lebesgue points and Fatou, followed by monotone approximation.

In the projection lemma, rows with zero complementary weight are legitimately discarded using the pointwise density cap. For the rest, `f_i^(1/b_i)<=f_i`, and `-b log b<=1-b` gives `||p_{U^T X}||_infty<=e^(d/2)` without probabilistic rotation.

### Lines 283–400: scalar Fourier powers, decoupling and crossing determinant — PASS

For real `p>=2`, reduction to the even exponent `2 floor(p/2)` is valid because `|hat f|<=1`; the density-at-zero estimate for a sum of independent differences gives `2pi sqrt(2e)/sqrt(p)`.

The decoupling identities retain original product structure. All pre-estimate integrands have modulus at most one, so Fubini uses no moments. The regularized graph Brascamp–Lieb proof has consistent frame weights `c_j,d_i`; scalar Fourier exponents are `2/d_i>=2`; the entropy factor cancels the regularizer exactly. The final determinant bound

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`

is correct.

Cauchy–Binet gives the order-`k` volumes. Keeping `k=5` yields an integrable `5/4` envelope and density `<=5e Z_5^(-1/10)`; `k=3` yields the `3/4` envelope used only after the Riesz weight.

### Lines 401–526: square, definite pair, hyperbolic pair and quarter concentration — PASS

The scalar square inverse-branch formula and interval-preimage bound are correct. The conditional formula is measure domination, not an independence assertion.

The definite-pair proof is a deterministic change of variables in the two-dimensional integral and never assumes independence after diagonalizing the quadratic matrix.

For the hyperbolic pair, the `(delta,t)` Jacobian is `1/(2 sqrt(D))`. On each tail one original coordinate is monotone with derivative comparable to its magnitude; the cap-one/mass-one bathtub estimate gives the logarithmic tail. The two-tail plus middle calculation gives the displayed `6+log_+` envelope, and `Lambda>=2/sqrt(D)` produces the final scale. The proof's nonnegative-test-function formulation is exactly what is needed for rough laws.

The random-sign split in the quarter-power lemma produces a genuine original-coordinate cross block of norm at least `||S||/4`; one singular factor from the crossing determinant gives the `|t|^(-1/4)` majorant. Gaussian smoothing yields the stated small-ball exponent. Letting the radius decrease excludes atoms, and layer cake gives `L0=4+4 log 16`.

### Lines 527–651: sampled interpolation and spectral-to-volume step — PASS

The bordered determinant identity is exact. Singular deleted seeds can lose representations, so the sampling proof correctly uses an inequality. The completion satisfies simultaneously

`rank R<=3r`, `R[L,L]=P[L,L]`, `rank R[L,L]<=r`,

with `D=0` on the seed and `E` zero on the diagonal. The support decomposition of `R-P` into rows `T` plus remaining columns `S` proves the global `3r` bound without symmetry of the auxiliaries.

In the bad-ratio branch, `s_m(A-E)>=1-epsilon` and the rank inequality force at least `m-3r>=r+1` large diagonal entries of `D`, all in `L`. Their corresponding `R[H,H]` block is strictly row diagonally dominant because

`371/400 > 4(1/7+1/16)=23/28`.

That contradicts `rank R[L,L]<=r`. The fair random cut contributes exactly `4^(-k)` per ordered disjoint pair, giving the displayed `Z_3,Z_5` consequences.

### Lines 652–760: singular kernels, pivot half-potentials and main proof — PASS

The `J(d)` near/far split and logarithmic-kernel rearrangement are valid nonnegative Tonelli arguments. In the scalar-pivot half-potential estimate, the Schur remainder retains one large spectral direction and the quarter-power logarithmic potential is applied with its exact hypothesis. Definite and indefinite pairs are averaged through conditional measure domination.

For `s_9>=1`, the pivot branch supplies a truncated half-potential and the outside part of `|Q-a|^(-1/2)` costs at most one; the no-pivot branch already controls the full half-potential.

The main branches close: no pivot `<2400`; scalar pivot `<=6010`; definite pair `<40`; indefinite pair `<251`. The Schur counts lose exactly the pivot dimension and allow arbitrary induced affine terms.

### Lines 761–790: scope and limitations — PASS

The manuscript correctly distinguishes the order-five integrable Fourier envelope from the order-three half-potential use, and it does not claim the three-eigenvalue conjecture or continuity in the pivot branches.

## Rough-law compiler: measurable versions and conditional Tonelli

**Lemma (integrated conditional domination).** Let `nu` be a positive finite measure on an environment space, let `mu_y` be a measurable probability/subprobability kernel on `R`, and let `k(y,z)>=0` be jointly Borel. Suppose that for `nu`-a.e. `y` and every nonnegative Borel test function `h`,

`int h(z) mu_y(dz) <= int h(z) k(y,z) dz`.

Then the mixture `mu(B)=int mu_y(B) nu(dy)` is dominated by

`K(z) dz`,  `K(z)=int k(y,z) nu(dy)`.

Proof: integrate the displayed inequality in `y` and apply Tonelli. If `K(z)<=C` a.e., the mixture has an essentially bounded density `<=C`. No conditional-density version and no exceptional set common to all `y` is required.

Applications in the manuscript are immediate:

- scalar pivot: `k(y,z)=|a|^(-1/2)|z-R(y)|^(-1/2)` after dropping the favorable one-sided indicator;
- definite pair: `k` is the constant `pi/sqrt(|det B|)`;
- indefinite pair: `k(y,z)=D^(-1/2)[6+log_+(16sqrt(D)/|z-R(y)|)]`, with `+infinity` on the critical graph.

The critical values `R(y)` are Borel quadratic polynomials. Quarter-power concentration gives the required logarithmic integrability. This retains arbitrary translations, fragmented/unbounded supports, and conditioning-generated affine terms.

## Same-proof constant sharpening — independently confirmed

The scalar-pivot truncated half-potential actually gives

`H_* = 10(20+12 log 16) = 200+120 log 16`,

which dominates the other pivot and no-pivot nine-direction constants. Hence the full half-potential in the nine-direction remainder is at most `201+120 log 16`, and the main scalar branch is at most

`C_* = 2010+1200 log 16`.

All other branches are smaller. Thus the same proof gives

`||p_Q||_infinity <= (2010+1200 log 16) K^2/s`,

and using only the manuscript's `log 16<3`, the clean bound `<5610 K^2/s`.

## New terminal structure for the attempted 17 -> 16 reduction

The current rank-count proof fails naively at terminal `r=4` under only `s_16>=1`: global rank `<=12` forces four large diagonal entries, while restricted rank `<=4` is compatible with a `4x4` invertible block. There is nevertheless extra no-pivot structure.

Assume terminal `r=4`, no `eta`-pivot, `V_5<kappa V_4`, and `s_16(A)>=1`. For the sampled seed `(S,T)` supplied by the manuscript, put `B=A[S,T]` and choose four large diagonal indices `H subset L`. The same proof gives

`|P_ii|>=371/400`, `|P_ij|<23/112` for `i!=j` in `H`,

where `P[H,H]=A[H,T] B^{-1} A[S,H]`. Since `|H|=4`, both row and column diagonal-dominance margins are at least

`delta = 371/400 - 3(23/112) = 109/350`.

A max-coordinate argument gives `||P[H,H]^{-1}||_infinity<=1/delta`; applying it to the transpose gives the same `1`-norm bound. Hence

`s_min(P[H,H])>=delta`,  `|det P[H,H]|>=delta^4`.

Set `b=|det A[S,T]|`, `c=|det A[H,T]|`, `e=|det A[S,H]|`. The factorization gives

`c e / b = |det P[H,H]| >= delta^4`.

Every entry of every disjoint `4x4` cross minor is an off-diagonal entry of `A`, so `|a_ij|<1/7` and Hadamard give

`c,e <= (2/7)^4 = 16/2401`.

Therefore, separately,

`c >= alpha b`, `e >= alpha b`,

with

`alpha = delta^4/(16/2401) = (109/100)^4 = 1.41158161... >1`.

Thus every sampled-good terminal seed in the `s_16` chamber forces **two strictly heavier neighboring disjoint four-minors**. This does not yet prove the 16-eigenvalue theorem because the neighboring heavier seeds need not satisfy the same small residual bound. The sharpened unpaid implication is to control that good-seed/heavier-neighbor transfer globally, or construct a source-valid obstruction.

## Required legacy-source application to a real localization obstruction

I re-read `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed Theorem A gives, in dimension three with all eigenvalues of modulus at least `sigma` and arbitrary affine terms,

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`.

Apply it to `A=I_3`. For every `N`, let each marginal be the cap-one comb

`f_N = 1_{ union_{j=1}^N [4^j,4^j+1/N] }`.

The whole law satisfies

`||p_{X_1^2+X_2^2+X_3^2}||_infinity <= 6 sqrt(pi)`

uniformly in fragment count and separation. If instead one localizes each original coordinate to one tooth and normalizes before paying curvature, each normalized tooth has density cap `N`; scaling to cap one turns the matrix into `I_3/N^2`, and Theorem A gives a cellwise normalized certificate `6 sqrt(pi) N^2`. Averaging cellwise suprema does not recover that factor. Fragment-first active normalization therefore loses `N^2` on an unchanged exact-target law while the source-valid whole-law certificate stays constant.

## Partner compatibility

The latest compatible pre-audit fleet03/B14 theorem gives the exact fixed-matrix translation quotient after whole-law finite-fragment extreme localization: centering produces precisely affine vectors in `Range(A)`, with fragment count, diameter and location unbounded. The present manuscript is uniform in **all** affine vectors, so that quotient is automatically admissible wherever one passes to the centered extreme core. It is not used as a premise of the 17-eigenvalue proof.

## Final status and next obligation

- 17-eigenvalue theorem: **PASS** in this independent audit.
- `10000` constant: valid; same proof sharpens it to `2010+1200 log 16 <5610`.
- Missing advertised supplementary checker/manifest files: **GAP (packaging only)**.
- Global bounded-Borel representative convention: **GAP-PRESENTATION**, repaired by the convention plus conditional-Tonelli compiler above.
- Full 16-eigenvalue theorem: **GAP / not proved**. New terminal fact: a sampled-good `r=4` seed forces two neighboring four-minors larger by `(109/100)^4`.
- Full unrestricted three-eigenvalue QFORM: still **OPEN**.
