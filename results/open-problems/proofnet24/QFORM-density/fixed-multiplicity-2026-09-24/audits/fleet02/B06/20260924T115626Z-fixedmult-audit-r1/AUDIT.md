# fleet02/B06 independent audit — graph determinant, weights, regularizer, and full manuscript

Run: `20260924T115626Z-fixedmult-audit-r1`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Pinned git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent B06 audit.** I read the complete 790-line pinned `manuscript.tex` end to end and reconstructed every dependency used by the main theorem. I found no fatal mathematical defect in the theorem

` s_17(A)>=s > 0  ==>  ||p_(X^T A X+b^T X+c)||_infinity <= 10000 K^2/s `

for arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent coordinate densities bounded by `K`.

This is one independent worker audit, not formal verification and not by itself the two-review validation gate. The unrestricted three-large-eigenvalue conjecture remains open.

I found two nonfatal gaps:

1. **LOCAL WORDING GAP, projection lemma (source roughly lines 256–287):** after rows with `b_i=0` are omitted, the proof writes `sum_i(1-b_i)=d`. Over the retained positive-`b_i` rows the correct relation is `sum_{b_i>0}(1-b_i)<=d`. This is exactly the direction needed for the upper bound, so changing `=` to `<=` repairs the sentence with no change to the theorem or constants.
2. **REPOSITORY PACKAGE GAP:** the current manuscript root listed `manuscript.tex`, `README.md`, `AUDIT.md`, and `audits/`, while `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` named by the README were absent at the snapshot inspected. The symbolic proof in the pinned manuscript is complete without them; the gap is reproducibility/release packaging, not a mathematical failure.

No lower multiplicity is certified in this run. In particular, I give below a source-valid obstruction showing that the natural attempt to combine the order-four `1/|t|` endpoint with the already available half-potential bound cannot work as an abstract analytic lemma.

## Audit ledger

### A1. Statement, quantifiers, architecture and scaling — source lines 1–80 — PASS

The theorem retains arbitrary dimension, arbitrary independent coordinate densities bounded only by `K`, arbitrary signature and remaining spectrum, and arbitrary affine terms. The normalization `Y=KX` gives cap-one coordinates and

`tilde Q = (K^2/s) Q`,

with quadratic matrix `A/s`; rescaling back yields the factor `K^2/s`. No hidden moment, support, centering, regularity or log-concavity hypothesis appears.

### A2. Fourier inversion and negative half moments — source lines 81–161 — PASS

The convention `fhat(t)=int exp(itx) f(x) dx` is used consistently. Gaussian inversion, Plancherel, and the `L^1` characteristic-function density criterion have the correct `2pi` factors. The Riesz computation gives

`E|Z-a|^(-1/2) <= (2pi)^(-1/2) int |t|^(-1/2)|phi_Z(t)| dt`.

For an envelope `min(1,(u/|t|)^(3/4))`, the weighted integral is `12 sqrt(u)`, yielding the displayed constant. The manuscript never promotes this `3/4` envelope directly to an `L^1` Fourier bound.

### A3. Singular-value perturbation and Schur spectral count — source lines 162–223 — PASS

The approximation characterization of singular values applies to nonsymmetric matrices and yields both perturbation inequalities used later. The Schur count

`N_S(t) >= N_A(t)-k`

is correct: in the invertible case `S^(-1)` is a principal compression of `A^(-1)`, and interlacing applied separately to the positive and negative tails gives the absolute-eigenvalue count. The singular case follows from `A+epsilon I` and continuity. I also stress-tested this count numerically on random symmetric matrices and found no counterexample; the proof, not the diagnostic, is the certification.

### A4. Geometric Brascamp--Lieb heat flow — source lines 224–255 — PASS

The frame condition makes the column operator with columns `sqrt(c_i)u_i` a contraction, so

`sum c_i v_i^2 - |sum c_i u_i v_i|^2 >= 0`.

The heat-flow monotonicity, large-time Gaussian limit, and monotone approximation from bounded compactly supported inputs to general nonnegative integrable functions are valid at the stated level of detail.

### A5. Product projections — source lines 256–287 — PASS WITH LOCAL WORDING GAP

The marginal density is integrated over the orthogonal complement, and geometric BL is applied to the original-coordinate factors. For `b_i=|w_i|^2`, the positive-`b_i` frame is correct and `int h_i <= b_i^(-1/2)`. The entropy bound then gives `||p_(U^T X)||_infinity <= e^(d/2)`.

The only defect is the equality noted in the verdict: after zero-`b_i` factors are omitted, the retained sum is at most `d`, not necessarily equal to `d`. Since this occurs on an upper-bound line, the proof remains valid after the one-symbol repair.

### A6. Integrated scalar Fourier powers — source lines 288–300 — PASS

With `m=floor(p/2)`, `|fhat|<=1` gives `int|fhat|^p <= int|fhat|^(2m)`. The latter is the Fourier transform of a sum of `m` independent differences at zero; the scalar projection bound yields

`int |fhat|^p <= 2pi sqrt(2e)/sqrt(p)`.

The use of a continuous inversion representative at zero is justified because the `2m`-power is integrable by the derived estimate.

### A7. Decoupling — source lines 301–328 — PASS

Cauchy--Schwarz in the original `X_I` law followed by an independent copy of `X_J` gives the two-copy product formula. Jensen yields the fourth-power version. The difference coordinates remain independent with cap-one densities by convolution. No post-rotation independence is asserted.

### A8. Regularized crossing determinant — source lines 329–379 — PASS; B06 primary lens

This was reconstructed independently. Put

`a=2t`, `alpha=(2pi e)^2`, `H=alpha I+a^2 M^T M`,

`c_j=alpha e_j^T H^(-1)e_j`, `d_i=a^2 m_i^T H^(-1)m_i`.

The vectors `sqrt(alpha)H^(-1/2)e_j` and `aH^(-1/2)m_i` form a rank-one geometric frame. Their weights satisfy `sum_i d_i=sum_j(1-c_j)=theta`.

After `x=H^(-1/2)z`, geometric BL gives exactly the manuscript's product of one-dimensional norms. Since the difference densities satisfy `g_j<=1`, their `L^(1/c_j)` norms are at most one. The scalar Fourier-power estimate at `p=2/d_i` gives

`||h_i||_(1/d_i) <= (2pi sqrt(e d_i))^(d_i)`,

so the `d_i` powers cancel. The entropy inequality contributes at most `e^(theta/2)`. Factoring `alpha^d` from `det H` leaves

`det(I+a^2M^TM/alpha)^(-1/2) (2pi e/sqrt(alpha))^theta`.

The selected `alpha=(2pi e)^2` cancels the second factor. Taking the fourth root of the fourth-power decoupling bound yields exactly

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

All Jacobians, weights and exponents are consistent. This theorem keeps arbitrary measurable same-bank terms and does not condition on a rotated spectral basis.

### A9. Crossing volumes and Fourier exponents — source lines 380–400 — PASS

Cauchy--Binet gives

`det(I+z M^TM)=sum_k z^k Z_k(M)`.

Keeping only the order-`k` term in the positive polynomial gives the envelope exponent `k/4`. The manuscript correctly uses `k=5` for an integrable `5/4` decay and `k=3` only after the Riesz weight. The constants `5e Z_5^(-1/10)` and the displayed `Z_3` half-potential bound are consistent.

### A10. Scalar, definite-pair, and hyperbolic-pair changes of variables — source lines 401–493 — PASS

The scalar-square profile is a conditional measure domination statement; it does not require independence of the completed square from its Schur remainder. The definite-pair Jacobian is `1/(2 sqrt(det B))` in quadratic polar coordinates and gives `pi M/sqrt(|det B|)`. The indefinite-pair hyperbolic parameterization has Jacobian `1/(2 sqrt(D))`; the tail proof uses only a single original coordinate density cap and total mass. The logarithmic envelope is valid away from the null critical level, sufficient for measure domination.

### A11. Quarter-power concentration — source lines 494–536 — PASS

If no diagonal coefficient has size `L/2`, a sign partition creates an original-coordinate cross block of norm at least `L/4`. Retaining one singular factor in the determinant theorem gives a `|t|^(-1/4)` envelope. Gaussian smoothing yields the stated `rho^(1/4)` small-ball estimate. The exact coefficient before the manuscript's simplification is about `3.995259362<16`, so the generous constant is sound. Layer cake then gives the uniform logarithmic potential.

### A12. Volume-sampled interpolation and completion — source lines 537–584 — PASS

For a sampled disjoint invertible seed `B=A[S,T]`,

`P=A[:,T] B^(-1) A[S,:]`

has rank at most `r` and agrees with `A` on rows `S` and columns `T`. The bordered determinant identity controls the off-diagonal residual on `L x L`. Singular seeds are absent from the sampling distribution, so the aggregate extension count is correctly an inequality rather than an equality.

In `A=D+R+E`, `D` vanishes exactly on `S union T`, `E` has zero diagonal, `R[L,L]=P[L,L]`, hence `rank R[L,L]<=r`. The difference `R-P` is supported in rows `T` or columns `S`, so `rank R<=3r`. Nonsymmetry of these auxiliaries causes no problem because the later perturbation statement is about singular values.

### A13. No-pivot spectral-to-volume proposition — source lines 585–621 — PASS

A bad telescoping ratio gives `||E||<=1/16`. With `m=4k-3` and a bad-ratio index `r<=k-1`, global rank `<=3r` forces at least `r+1` entries of the diagonal `D` to have magnitude at least `1-epsilon`. They lie in `L` because `D` vanishes on the seed. On the resulting `(r+1)`-set,

`|R_ii| >=371/400`, while each off-diagonal is `<1/7+1/16`; for `r<=4` the row sum is `<23/28`.

The strict diagonal-dominance slack is exactly

`371/400 - 23/28 = 297/2800 >0`.

Thus `R[H,H]` has rank `r+1`, contradicting the restricted rank `<=r`. The separate `r=0` Frobenius argument is also correct.

### A14. Random cut and no-pivot analytic consequences — source lines 622–651 — PASS

Each ordered disjoint `k`-minor survives a fair cut with probability `4^(-k)`, giving the exact expectation. With `kappa=1/80^2`, the resulting bound is `Z_k^(-1/(2k))<=160`. Substitution gives

`12 sqrt(80e)=176.959...<200`,

and

`800e=2174.625...<2400`.

### A15. Singular kernels, pivot half potential, and nine-direction bound — source lines 652–721 — PASS

The two kernel integrals have the stated crude constants. The scalar-pivot branch uses only a surviving Schur eigenvalue to average the logarithmic singularity; definite and indefinite pair branches are uniform after conditioning. The largest displayed truncated-half-potential constants are below `600`. The distinction between truncated `H(Q)` and the full half-potential is preserved: outside distance one the kernel is at most one, giving `601`.

### A16. Main theorem — source lines 722–790 — PASS

No pivot: the order-five branch gives density `<2400`. A scalar pivot removes one spectral direction and leaves enough for the nine-direction half-potential, giving `6010`. A definite pair is directly bounded. An indefinite pair removes two directions; one surviving Schur eigenvalue suffices for the logarithmic average. All constants are below `10000`. General `K,s` scaling is correct.

## B06 improvement analysis: the graph regularizer cannot by itself solve the order-four endpoint

Before specializing `alpha`, the same BL calculation gives the fourth-power majorant

`I_alpha(t) <= det(I+a^2 M^TM/alpha)^(-1/2) (2pi e/sqrt(alpha))^theta`,

where

`theta = tr[a^2 M^TM (alpha I+a^2 M^TM)^(-1)]`.

Let `M` have fixed rank `r` and nonzero singular values `sigma_l`. If `alpha/a^2 ->0`, then each nonzero singular direction contributes asymptotically

`(1+a^2 sigma_l^2/alpha)^(-1/2) (2pi e/sqrt(alpha))^(a^2 sigma_l^2/(alpha+a^2 sigma_l^2))
 ~ 2pi e/(|a| sigma_l)`.

Thus `I_alpha(t)` still has only `|a|^(-r)` decay, and after the fourth root `|phi|` has only `|t|^(-r/4)` decay. If `alpha` is comparable to `a^2`, every effective exponent is strictly below one per singular direction; if `alpha>>a^2`, the decay is weaker still. Therefore simply retuning this regularizer cannot turn the `r=4` endpoint into an absolutely integrable characteristic-function envelope. The threshold reduction 17 -> 13 needs a genuinely new endpoint mechanism, not a different scalar choice of `alpha` in the existing proof.

## Source-valid counterexample to an abstract `k=4 Fourier + half-potential => L-infinity` synthesis

This is a counterexample to an intermediate analytic compiler, not to the manuscript theorem.

Let `U,V` be independent `Uniform[-1/2,1/2]` variables and

`Q_0 = 2UV = (U,V) [[0,1],[1,0]] (U,V)^T`.

The input densities are exactly cap one and the two eigenvalues of the quadratic matrix are `+1,-1`. Direct product change of variables gives

`p_(Q_0)(q) = log(1/(2|q|)) 1_{|q|<1/2}`,

so `p_(Q_0)` diverges logarithmically at zero.

Nevertheless its characteristic function satisfies a borderline order-four-type envelope. Indeed

`phi_(Q_0)(t)=2 Si(t/2)/t`,

where `Si(x)=int_0^x sin(u)/u du`; in particular `|phi_(Q_0)(t)|<=min(1,C/|t|)` for an absolute `C`.

It also has a uniformly finite half potential. Since

`int p_(Q_0)^3 = int_0^1 (-log x)^3 dx = 6`,

Hölder with exponents `3` and `3/2`, together with the uniform translated bound on

`int_{-1/2}^{1/2}|q-a|^(-3/4)dq`,

gives

`sup_a E|Q_0-a|^(-1/2) < infinity`.

Therefore the two abstract pieces

`|phi(t)| = O(1/|t|)` and `sup_a E|Z-a|^(-1/2)<infinity`

do **not** imply an essentially bounded density. Since `s_13>=1` would already imply the manuscript's nine-direction half-potential estimate while the order-four crossing route supplies only `1/|t|`, a 13-eigenvalue proof cannot close by a black-box synthesis of just those two outputs. It must exploit additional quadratic/product structure at the endpoint.

This obstruction is source-valid and product-generated; it is not a fixed-multiplicity counterexample because it has only two large eigenvalues.

## Threshold status and first unpaid implication

- Certified theorem after this audit: multiplicity **17** with the manuscript's `10000 K^2/s` bound.
- Reduction to 16: not obtained. The current rank-count mechanism has a terminal `r=4` chamber where 16 directions force only four large diagonal entries against a restricted rank-four correction; a new structural input is needed.
- Reduction to 13: not obtained. The present order-four determinant endpoint is `1/|t|`, and the explicit `2UV` example above rules out upgrading it using only an abstract half-potential bound.

First unpaid implication:

**`QFORM-FIXEDMULT-K4-STRUCTURED-ENDPOINT-v1`.** Under the actual original-coordinate product provenance of the order-four crossing-volume branch, prove a dimension-free `L^infinity` output-density bound from `Z_4(M)>=c>0` while retaining arbitrary same-bank measurable quadratic/affine terms, or exhibit a source-valid obstruction within that exact branch. Any successful theorem here would combine with the already-audited interpolation argument to lower the spectral threshold from 17 to 13. It must use more than absolute `1/|t|` Fourier decay plus the nine-direction half-potential estimate.

## Review status

Mathematical 17-eigenvalue baseline: **PASS in this audit**.  
Fatal mathematical gap found: **none**.  
Local proof repair: projection-lemma equality should be an inequality after zero-weight rows are dropped.  
Repository-package reproducibility: **GAP**, supplementary files named by README were absent in the inspected root.  
Lower multiplicity proved here: **none**.  
Unrestricted three-eigenvalue conjecture: **OPEN**.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.
