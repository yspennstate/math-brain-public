# account02/B15 auto11 — full fixed-multiplicity audit

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T140615Z-account02-B15-fixedmult-auto11`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned `manuscript.tex` blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Source length: 47,883 bytes / 790 lines.  
Execution class: `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval/use was real; native brain receiver ingestion was not verified).

I read the fresh owner controls, then the complete package: `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. I then independently reconstructed the analytic and algebraic dependencies rather than adopting the historical self-audit verdict.

## Verdict

**Baseline theorem: PASS, with one nonfatal notation GAP and no FALSE mathematical claim found.**

The pinned manuscript proves, as stated,

` s_17(A) >= s > 0  =>  ||p_(X^TAX+b^TX+c)||_infinity <= 10000 K^2/s `

for arbitrary real symmetric `A`, arbitrary affine terms, arbitrary dimension/signature/remaining spectrum, and arbitrary independent real coordinate laws with densities bounded by `K`.

The only manuscript defect I found is at the indefinite-pair part of the main proof (within lines 726–749): after explicitly defining the remainder quadratic matrix as the Schur complement, the text writes `||A/B||>=1`, but `A/B` is nowhere defined. **Repair:** replace it by `||S||>=1`, where `S=D-C^T B^{-1}C` is the Schur complement from Lemma `lem:schur`. **Impact:** none on the argument; the preceding Schur-count statement leaves at least fifteen eigenvalues of `S` of modulus at least one, so `||S||>=1` follows immediately. Status: **GAP (notation only, locally repairable)**.

No unrestricted three-eigenvalue theorem is proved or claimed here.

## Complete source-line coverage ledger

Every source line 1–790 is covered by one of the following ranges. `PASS` means the mathematical claim was reconstructed or, for metadata, checked not to add a hidden hypothesis. `UNCHECKED` is reserved only for external priority/binary-build facts that are not proof premises.

| Source lines | Item | Status | Reconstruction / issue / downstream impact |
|---|---|---|---|
| 1–46 | LaTeX setup, abstract, definitions of singular values/density notation | **PASS** | Abstract matches the theorem and does not add smoothness/support/moment assumptions. |
| 47–57 | `thm:main` | **PASS** | Quantifiers are complete; conclusion is essential `L^infinity`, not continuity. Interval domination is equivalent to the density cap. |
| 58–61 | `cor:33` | **PASS** | Follows because singular values are decreasing: `s_17>=s_33`. |
| 62–90 | Architecture, parameters, Fourier convention | **PASS** | `eta=1/100`, `kappa=1/80^2`; pivot/no-pivot dichotomy is exhaustive. Conditioning is explicitly on original coordinates. |
| 91–120 | `lem:fourier` | **PASS** | Plancherel normalization, Gaussian inversion, and `L^1` Fourier inversion are correct; Gaussian regularization starts from an arbitrary probability law, not a pre-existing density. |
| 121–130 | `lem:envelope` | **PASS** | Splitting at `|t|=a` gives `int min(1,(a/|t|)^p)=2ap/(p-1)` and the stated density constant. |
| 131–160 | `lem:riesz` | **PASS** | Mellin/Gaussian representation and two Tonelli steps give exactly `1/sqrt(2 pi)`; the `3/4` envelope gives weighted integral `12 sqrt(u)`. Extended values correctly cover atoms. |
| 161–168 | Norm/spectral-count conventions | **PASS** | Used consistently. |
| 169–181 | `lem:rank` | **PASS** | Approximation-number characterization gives singular-value Lipschitz perturbation and the rank shift for nonsymmetric matrices. |
| 182–207 | `lem:schur` | **PASS** | Invertible case follows from `S^{-1}` as a principal compression of `A^{-1}` and positive/negative min-max counts. The singular case with threshold `t-|epsilon|` passes to the limit and preserves `>=t`. |
| 208–217 | `lem:dd` | **PASS** | Standard max-coordinate kernel-vector proof; symmetry unnecessary. |
| 218–255 | `thm:bl` geometric rank-one inequality | **PASS** | Heat-flow derivative has correct sign from the frame contraction; integration by parts, large-time normalization, small-time Fatou and truncation are justified at the stated scope. |
| 256–282 | `lem:projection` | **PASS** | Deterministic rotation only; no rotated independence. For `b_i=0`, the corresponding factor is dropped and one may extend `-b log b` continuously by zero; summing `1-b_i` over all rows gives `d`. No mathematical repair is needed. |
| 283–301 | `lem:scalar-fourier` | **PASS** | Difference density is cap one; even-power inversion is legitimate because `|hat f|^2` is integrable; projection of `2m` literal independent coordinates gives the stated `p`-power constant. |
| 302–324 | Cross-form setup and `lem:decoupling` | **PASS** | Copy is introduced only in the `J` bank; product Fourier factors arise from original independent `I` coordinates. No moments are used. |
| 325–373 | `thm:determinant` | **PASS** | Frame weights, graph Jacobian, scalar Fourier powers, `alpha=(2 pi e)^2`, and fourth root reconstruct exactly; determinant exponent is `-1/8`. |
| 374–400 | Crossing-volume identities and `cor:vol-fourier` | **PASS** | Cauchy–Binet is exact. Order five gives `|t|^-5/4` and direct inversion; order three gives only `|t|^-3/4`, used with the Riesz weight, not falsely as a density theorem. |
| 401–414 | `lem:square` | **PASS** | Two inverse branches give the square-root density envelope and interval-preimage length. |
| 415–422 | Conditional scalar profile | **PASS** | It is a test-function/Tonelli domination formula; it does not assert independence between the completed square and the Schur remainder. |
| 423–434 | `lem:definite` | **PASS** | Polar/elliptic Jacobian is `1/(2 sqrt(|det B|))`; rotation is only in deterministic integration. |
| 435–482 | `lem:hyperbola` | **PASS** | Hyperbolic Jacobian, tail monotonicity, one-dimensional bathtub bound and AM–GM reduction reconstruct. Exceptional critical level is handled measure-theoretically. |
| 483–525 | `lem:quarter` | **PASS** | Diagonal branch and random-sign off-diagonal crossing branch are valid; Gaussian small-ball smoothing gives the stated coefficient and layer cake gives `L_0=4+4 log 16`. |
| 526–544 | Pivot/volume definition and no-pivot entry estimates | **PASS** | Failure of diagonal and principal-pair pivots gives the displayed entry bounds. |
| 545–564 | `lem:sampling` | **PASS** | Bordered determinant identity is exact; singular seeds correctly make the aggregate count an inequality, not an equality. |
| 565–580 | `lem:completion` | **PASS** | `D` vanishes on the seed, `E` has zero diagonal, global `rank R<=3r`, and restricted `rank R[L,L]<=r`; nonsymmetry is correctly retained. |
| 581–619 | `prop:volume` | **PASS** | Bad successive-volume ratio gives `||E||_F<=(r+1)/80<=1/16`; singular-value rank subtraction forces `r+1` large diagonal residuals; row dominance contradicts restricted rank. Exact slack is `371/400-23/28=297/2800>0`. |
| 620–630 | `lem:cut` | **PASS** | Every ordered disjoint `k`-minor survives a fair cut with probability `4^-k`. |
| 631–645 | `cor:no-pivot` | **PASS** | `k=3` gives full half-potential `<200`; `k=5` gives density `<800e<2400`. Correctly distinct conclusions. |
| 646–674 | Truncated potential and `lem:kernels` | **PASS** | Both singular integrals are finite with the advertised coarse constants; layer-cake overlap argument is valid. |
| 675–714 | `prop:pivot-H` | **PASS** | Scalar, definite, and indefinite pivots exhaust the definition; every branch is uniform in induced affine terms and rough laws. Constants reconstruct below. |
| 715–724 | `prop:nine` | **PASS** | Pivot/no-pivot dichotomy gives truncated potential `<=600`; the outside-unit tail costs at most one, so full half-potential `<=601`. |
| 725–749 | Main proof, scaling, corollary/equivalence | **PASS with one notation GAP** | No-pivot `<2400`, scalar `6010`, definite `<40`, indefinite `<251`. Scaling `Y=KX`, `Q=(s/K^2)Qtilde` gives `K^2/s`. Undefined `A/B` must be `S`, as described above. |
| 750–790 | Threshold accounting, limitations, acknowledgments, bibliography | **PASS mathematically / UNCHECKED priority** | Threshold accounting correctly distinguishes order-three half-potential from order-five density inversion and explicitly declines the unrestricted three-eigenvalue theorem/global continuity. Exhaustive bibliographic priority was not re-researched; citations are not proof dependencies. |

No source line remains mathematically `UNCHECKED`.

## B15 reconstruction: Gaussian inversion

With the manuscript convention

`hat f(t)=int exp(i t x) f(x) dx`, `phi_Z(t)=E exp(i t Z)`,

the exact identity is

`exp(-v x^2) = [1/(2 sqrt(pi v))] int exp(-t^2/(4v)) exp(-i t x) dt`.

Hence for **any** probability law of `Z`, without assuming a density,

`E exp(-v(Z-a)^2) = [1/(2 sqrt(pi v))] int exp(-t^2/(4v)) exp(-i t a) phi_Z(t) dt`.

The sign follows after `t -> -t`. The Gaussian factor makes Fubini absolute. If `phi_Z in L^1`, the Gaussian-regularized densities converge uniformly to the inverse Fourier integral, so this branch genuinely produces a bounded **continuous** density. This continuity conclusion is tied to the common `L^1` Fourier majorant; it is not available from weak/TV approximation alone.

## B15 reconstruction: Riesz half-potential

For extended nonnegative values,

`|z|^-1/2 = Gamma(1/4)^-1 int_0^infinity v^-3/4 exp(-v z^2) dv`.

After Gaussian inversion, Tonelli, and `w=t^2/(4v)`,

`int_0^infinity v^-5/4 exp(-t^2/(4v)) dv = sqrt(2) Gamma(1/4) |t|^-1/2`.

Therefore

`E|Z-a|^-1/2 <= (2 pi)^-1/2 int |t|^-1/2 |phi_Z(t)| dt`.

For `|phi_Z(t)|<=min(1,(u/|t|)^(3/4))`, the weighted integral is exactly

`2 int_0^u t^-1/2 dt + 2 u^(3/4) int_u^infinity t^-5/4 dt = 12 sqrt(u)`,

which gives `12 sqrt(u/(2 pi))`. There is no hidden density, moment, support or continuity premise.

## Constant recheck

The baseline constants have real slack:

- quarter-power Gaussian coefficient: `2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)=3.995259...<16`;
- no-pivot nine-direction full half-potential: `12 sqrt(80e)=176.959...<200`;
- no-pivot seventeen-direction density: `800e=2174.625...<2400`;
- scalar-pivot truncated half-potential: `10(8+3L_0)=532.711...<560`;
- definite-pair truncated half-potential: `40 pi=125.664...<160`;
- indefinite-pair truncated half-potential: `432.376...<444`;
- main scalar branch: `6010<10000`;
- main indefinite-pair branch: `238.998...<251`.

## Rough-law approximation: what it proves and what it does not

A cap-preserving mollification in the **original coordinates** has

`f_i^(eps)=f_i*rho_eps`, `0<=f_i^(eps)<=1`, and `||f_i^(eps)-f_i||_1 ->0`.

For finite dimension,

`|| product_i f_i^(eps) - product_i f_i ||_1 <= sum_i ||f_i^(eps)-f_i||_1 ->0`.

Deterministic quadratic pushforward contracts total variation. Therefore a smooth-input interval inequality

`mu_eps(I)<=C |I|`

with `C` independent of `eps` passes with **zero loss** to the rough law and gives an essentially bounded density.

It does **not** by itself pass continuity of density representatives. Counterexample to that inference: `f=1_[0,1]` and `f_eps=f*rho_eps` are cap-one smooth probability densities with `f_eps->f` in `L^1`; every `f_eps` is continuous while the limiting density has jump discontinuities. Thus TV/L1 convergence plus a uniform `L^infinity` cap is insufficient for continuity. A common integrable Fourier envelope, a uniform modulus, or another separate regularity theorem is required.

This is exactly the scope respected by the manuscript: the no-pivot order-five branch has an integrable characteristic function and hence a continuous density; pivot branches are proved directly as measure domination and claim only essential boundedness.

## Counterexample stress test: why order four alone cannot replace order five by absolute inversion

A `C/|t|` characteristic-function envelope is not enough for bounded density. Let `G,H` be independent standard Gaussians (their densities are below one) and put `Z=GH`. Conditioning gives

`phi_Z(t)=(1+t^2)^(-1/2) ~ |t|^-1`,

while the density is `p_Z(z)=pi^-1 K_0(|z|)` and has a logarithmic singularity at zero. Equivalently, `2GH` is the indefinite rank-two quadratic form with matrix `[[0,1],[1,0]]`.

So the naive order-four endpoint (`|phi|=O(1/|t|)`) cannot, by absolute Fourier inversion alone, lower the manuscript threshold. This is an obstruction to that proof interface, not a counterexample to a lower fixed-multiplicity theorem.

## Package/support-file audit

- `README.md`: **PASS**. It identifies the 17-direction baseline as a candidate and explicitly says the unrestricted three-eigenvalue theorem is not solved.
- `DELIVERY_STATUS.md`: **PASS as status metadata**. It accurately separates source delivery, native assignment observations, and mathematical validation.
- `SOURCE_MANIFEST.json`: **PASS** for the source pin/size/hash metadata. The compiled-PDF binary itself was not independently re-downloaded in this run: **UNCHECKED binary reproduction**, with no proof impact because the complete source is present.
- `AUDIT.md`: **PASS as historical self-report, not evidence of independent correctness**. Its older finite-test counts are explicitly distinguished from the newer checker.
- `proof_map.csv`: **PASS**; statement/proof ranges agree with the source and were used only as navigation, not as a substitute for reading the source.
- `verify.py`: **PASS at its stated finite-check scope**. The source-hash guard, interpolation/rank/support identities, volume comparison, Schur diagnostics and graph-weight diagnostics match the written proof. It is not a universal certificate.
- `checks.json`: **PASS as the recorded output of the new scoped checker** (`534` interpolation seeds, `18` volume cases, `240` Schur threshold cases, `30` graph-weight cases, exact slack `297/2800`). I did not independently rerun that exact script/environment here, so execution reproduction is **UNCHECKED**, with no effect on the symbolic proof audit.

## Next proof obligation after the baseline

The baseline is secure enough to attempt multiplicity reduction. A lower threshold must replace the no-pivot order-five density endpoint rather than pretending the order-four `1/|t|` envelope is integrable. I separately reconstructed the current grouped order-three density receiver and order-two half-potential receiver and assembled a complete nine-eigenvalue replacement proof; that proof and its constants are saved in this run's immutable improvement artifact. Threshold eight remains open and requires genuinely new overlap/cycle product structure rather than a rank-two density endpoint.
