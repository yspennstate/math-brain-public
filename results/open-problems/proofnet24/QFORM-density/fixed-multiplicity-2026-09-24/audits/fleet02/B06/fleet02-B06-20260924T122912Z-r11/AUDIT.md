# fleet02/B06 independent audit r11 — full manuscript, graph weights, Jacobian and optimal regularizer

Run: `fleet02-B06-20260924T122912Z-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Canonical manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Recorded source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Master recheck before publication: manuscript blob still `183ccd294763214e6a707e8d4749ff9a8cf7006d` at `d7660965a035bfe7aab10db0699b764f91a96b2d`.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent B06 audit.** I reread the entire 790-line manuscript and reconstructed every dependency used by the main theorem. I found no fatal mathematical defect in

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary real symmetric `A`, arbitrary affine terms, and independent coordinate densities bounded by `K`. This remains one worker audit, not formal verification and not a claim about the unrestricted three-eigenvalue problem.

**GAP (repository packaging only):** at the inspected master snapshots the root contains `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`, but not `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, or `checks.json`, although README names them. Their advertised finite-test counts are therefore **UNCHECKED in this run**. The symbolic manuscript is self-contained and does not depend on those files.

**Correction to my preceding B06 audit:** I withdraw the earlier claimed local wording gap in the product-projection proof. The displayed sum `sum_i(1-b_i)=d` is valid if `i` ranges over all original rows, including `b_i=0`; the immediately following sentence explicitly assigns zero contribution to `-b log b` at `b=0`. Equivalently one may write `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`. There is no mathematical defect or needed source patch there.

No lower multiplicity is certified here. Instead I prove a stronger obstruction for the B06 mechanism: **the manuscript's fixed regularizer `alpha=(2*pi*e)^2` is the exact pointwise global minimizer of the entire free-alpha graph-BL majorant for every `t` and every cross block `M`.** Thus scalar retuning of this regularizer cannot improve the order-four endpoint at all, not merely asymptotically.

## Complete audit ledger

Every source line 1–790 is covered by the contiguous ranges below. `PASS` means I independently reconstructed the argument and checked the hypotheses of every invocation in that range; numerical claims are separated from symbolic proof.

### A1 — lines 1–80 — theorem, quantifiers, architecture, normalization — PASS

Definitions of singular values, essential supremum, `eta=1/100`, `kappa=1/80^2`, pivot alternatives and the `9,17` accounting are consistent. No moment, support, smoothness, centering, log-concavity or post-rotation independence assumption enters. For general `K,s`, `Y=KX` has cap-one coordinate densities and `tilde Q=(K^2/s)Q`, so rescaling gives exactly `10^4 K^2/s`.

### A2 — lines 81–161 — Fourier inversion, Gaussian regularization, Riesz half-potential — PASS

With `fhat(t)=int e^{itx}f(x)dx`, Plancherel has factor `2*pi`; Gaussian inversion has `1/(2 sqrt(pi v))`; the density inversion bound has `1/(2*pi)`. The gamma/Tonelli computation gives

\[
\mathbb E|Z-a|^{-1/2}\le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|dt.
\]

The `3/4` power envelope gives weighted integral `12 sqrt(u)`. Extended-valued Tonelli is used legitimately, so no a priori density or moment hypothesis is hidden.

### A3 — lines 162–223 — singular-value perturbation, Schur count, diagonal dominance — PASS

The approximation formula for singular values is valid for nonsymmetric matrices and yields both perturbation statements. For the Schur count, when `A` is invertible, `S^{-1}` is the complementary principal compression of `A^{-1}`; applying eigenvalue interlacing separately to positive and negative tails gives `N_S(t)>=N_A(t)-k`. The `A+epsilon I` limiting argument handles singular `A`. Strict row diagonal dominance is valid without symmetry.

### A4 — lines 224–255 — geometric rank-one Brascamp–Lieb heat flow — PASS

The frame matrix with columns `sqrt(c_i)u_i` has `WW^T=I`, hence operator norm one. Therefore

\[
\partial_tF-\Delta F
=F\left(\sum_i c_i v_i^2-\left|\sum_i c_i u_i v_i\right|^2\right)\ge0.
\]

The large-time Gaussian limit uses `sum c_i=d`; compact support supplies the stated Gaussian domination, and monotone truncation extends to arbitrary nonnegative integrable inputs.

### A5 — lines 256–287 — product-projection density — PASS; previous B06 gap retracted

For `b_i=|w_i|^2`, rows with `b_i>0` give the geometric frame, while factors with `b_i=0` are at most one and may be dropped. The one-dimensional rescaling contributes `b_i^{-b_i/2}`. Then

\[
\log p(y)\le\frac12\sum_{b_i>0}[-b_i\log b_i]
\le\frac12\sum_{b_i>0}(1-b_i)
\le\frac12\sum_i(1-b_i)=d/2.
\]

Thus the manuscript's compressed notation is sound. The scalar consequence is `sqrt(e)/|a|`.

### A6 — lines 288–300 — integrated scalar Fourier powers — PASS

For `m=floor(p/2)`, `2m<=p` and `|fhat|<=1`, hence `int|fhat|^p<=int|fhat|^(2m)`. The latter is the characteristic function of a sum of `m` independent differences and is integrable (already dominated by the `L^2` power). Fourier inversion at zero plus the scalar projection bound gives `2*pi*sqrt(2e)/sqrt(p)`.

### A7 — lines 301–328 — cross-block decoupling — PASS

Cauchy–Schwarz in the original `X_I` law followed by an independent copy of `X_J` gives the two-copy product. Jensen gives the fourth-power inequality. Difference coordinates remain independent and cap one by convolution. All pre-estimate integrands have modulus at most one, so Fubini uses no moments.

### A8 — lines 329–379 — regularized crossing determinant — PASS; primary B06 reconstruction

Put `a=2t`, `alpha=(2*pi*e)^2`, `H=alpha I+a^2 M^T M`,

\[
c_j=\alpha e_j^TH^{-1}e_j,
\qquad d_i=a^2m_i^TH^{-1}m_i.
\]

The vectors `sqrt(alpha)H^{-1/2}e_j` and `aH^{-1/2}m_i` have outer products summing to `I`. Hence `0<c_j<=1`, `0<=d_i<=1` and

\[
\theta=\sum_i d_i=\sum_j(1-c_j).
\]

Rows with `d_i=0` have Fourier factor one and can be omitted; as `d_i downarrow0` the formula is continuous. After `x=H^{-1/2}z`, the full Jacobian is `det(H)^(-1/2)`. Normalizing the coordinate-frame vector gives

\[
x_j=\sqrt{c_j/\alpha}\,u_j\cdot z,
\]

so the BL one-dimensional change contributes exactly `alpha^{c_j/2}c_j^{-c_j/2}||g_j||_{1/c_j}`. The cross-row vector contributes exactly `d_i^{-d_i/2}||h_i||_{1/d_i}`. Since `g_j<=1`, its norm is at most one. The scalar Fourier-power lemma at `p=2/d_i` gives

\[
\|h_i\|_{1/d_i}\le(2\pi\sqrt{e d_i})^{d_i},
\]

and the `d_i` powers cancel. The entropy term obeys `prod c_j^{-c_j/2}<=e^{theta/2}`. Factoring `alpha^d` from `det H` leaves

\[
\det(I+a^2M^TM/\alpha)^{-1/2}
\left(\frac{2\pi e}{\sqrt\alpha}\right)^\theta.
\]

At `alpha=(2*pi*e)^2` the multiplier is one. Fourth roots give exactly

\[
|\phi_Z(t)|\le
\det\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

Zero rows, zero singular values, `c_j` close to zero, and `c_j=1` are all harmless; no division by a zero weight is used.

### A9 — lines 380–400 — Cauchy–Binet crossing volumes and exponents — PASS

`det(I+zM^TM)=sum_k z^k Z_k(M)` follows from principal-minor expansion plus Cauchy–Binet. Keeping one positive coefficient gives exponent `k/4`. The `k=5` envelope is integrable and yields `5e Z_5^{-1/10}`. The `k=3` envelope is used only with the Riesz weight, not incorrectly as an `L^1` characteristic-function bound.

### A10 — lines 401–493 — scalar, definite-pair and hyperbolic Jacobians — PASS

The scalar inverse-image length is at most `2 sqrt(2 rho/|a|)`. In the definite pair, quadratic polar coordinates have Jacobian `1/(2 sqrt(|det B|))`, giving `pi M/sqrt(|det B|)`. In the indefinite pair, the hyperbolic coordinates have Jacobian `1/(2 sqrt(D))`. The two tails are controlled using one literal original-coordinate density and its mass, while the middle interval has bounded length. The AM–GM inequality `Lambda>=2/sqrt(D)` yields the final `16 sqrt(D)` logarithmic scale. Exceptional critical levels are handled at the measure-domination level.

### A11 — lines 494–536 — quarter-power concentration and logarithmic potential — PASS

If no diagonal coefficient has size `L/2`, sign decoupling yields a literal cross block of norm at least `L/4`. One determinant factor gives `|t|^{-1/4}`; Gaussian smoothing gives the `rho^{1/4}` small-ball estimate. Layer cake then gives `4+4 log 16`. This argument preserves arbitrary rough coordinate laws.

### A12 — lines 537–584 — sampled interpolation and completion — PASS

For sampled disjoint invertible `B=A[S,T]`, `P=A[:,T]B^{-1}A[S,:]` has rank at most `r` and interpolates rows `S` and columns `T`. Bordered determinants control the off-diagonal `LxL` residual; singular seeds are not sampled, so the extension count is correctly an inequality. In `A=D+R+E`, `D` vanishes on `S union T`, `E` has zero diagonal, `R[L,L]=P[L,L]`, and `rank R[L,L]<=r`. Since `R-P` is supported in rows `T` or columns `S`, `rank R<=3r`. Symmetry is not needed for these auxiliary rank estimates.

### A13 — lines 585–621 — no-pivot spectral-to-volume proposition — PASS

A bad telescoping ratio gives `||E||<=1/16`. With `m=4k-3` and `r<=k-1`, the global `3r` rank loss leaves at least `r+1` diagonal entries of `D` of size `1-epsilon`, all in `L`. On their `(r+1)`-set, diagonal entries of `R` are at least `371/400`, while the off-diagonal row sum is less than `23/28`. Exact slack is

\[
371/400-23/28=297/2800>0.
\]

Strict diagonal dominance contradicts the restricted rank `<=r`. The `r=0` Frobenius branch also contradicts `||A||>=1`.

### A14 — lines 622–651 — random cut and no-pivot analytic consequences — PASS

Each ordered disjoint `k`-minor survives a fair cut with probability `4^{-k}`. Hence `Z_k^{-1/(2k)}<=160`. For `k=3`, the half-potential constant is `12 sqrt(80e)<200`; for `k=5`, the density constant is `800e<2400`.

### A15 — lines 652–721 — singular kernels, pivot half-potential, nine-eigenvalue bound — PASS

The kernel bounds are valid with their generous constants. A scalar pivot leaves at least one Schur eigenvalue when only the truncated half potential is needed; definite and indefinite pair pivots are uniformly bounded after conditioning. The proof correctly distinguishes the truncated `H(Q)` from the full half potential; outside unit distance the kernel is at most one, yielding `601`.

### A16 — lines 722–790 — main theorem and limitations — PASS

No pivot uses order five. A scalar pivot removes one direction and still leaves enough for the nine-direction full half-potential bound, giving `6010`. A definite pair is directly bounded. An indefinite pair removes two directions and needs only one surviving Schur eigenvalue to average its logarithm. All branches lie below `10000`; the final `K,s` scaling is exact. The manuscript explicitly does not claim the unrestricted three-eigenvalue theorem or continuity in every branch.

## Package files outside manuscript

- `README.md`: **PASS** as a description of the mathematical candidate, but **GAP** as a reproducibility inventory because four named files are absent at the inspected master state.
- `AUDIT.md`: **PASS as author self-audit metadata, not independent evidence**. Its finite-test counts are not promoted to proof.
- `SOURCE_MANIFEST.json`: **UNCHECKED / absent**.
- `proof_map.csv`: **UNCHECKED / absent**.
- `verify.py`: **UNCHECKED / absent**.
- `checks.json`: **UNCHECKED / absent**.

The current master manuscript blob equals the pinned initial blob, so concurrent audit/improvement commits have not changed the mathematical source audited here.

## New B06 result: the chosen scalar regularizer is exactly optimal

The manuscript specializes the regularizer early. Keep it free: let `alpha=q^2>0`, `C=2*pi*e`, `a=2|t|`, and let `sigma_j` be the nonzero singular values of `M`. The same graph-BL proof gives the fourth-power majorant

\[
B_\alpha(t)^4=
\prod_j(1+x_j)^{-1/2}
\left(\frac Cq\right)^{x_j/(1+x_j)},
\qquad x_j=(a\sigma_j/q)^2.
\]

For one nonzero singular direction set `A=a sigma/C`. Since `C/q=sqrt(x)/A`, the logarithm of its factor is

\[
F_A(x)=-\tfrac12\log(1+x)+\frac{x}{1+x}
\left(\tfrac12\log x-\log A\right).
\]

A direct derivative calculation gives the exact identity

\[
F_A'(x)=\frac{\tfrac12\log x-\log A}{(1+x)^2}.
\]

Thus the unique minimum is at `x=A^2`. But

\[
x=A^2
\iff (a\sigma/q)^2=(a\sigma/C)^2
\iff q=C
\iff \alpha=(2\pi e)^2,
\]

independently of `sigma`. **Every nonzero singular factor is minimized by the same regularizer**, so their product is globally minimized there for every fixed `t` and `M`. At that minimum the factor equals

\[
(1+A^2)^{-1/2},
\]

and the fourth root is exactly the determinant bound in the manuscript.

Consequences:

1. The choice `alpha=(2*pi*e)^2` is not merely a convenient cancellation; it is pointwise optimal within this entire scalar-regularizer/entropy-majorant proof family.
2. Any `t`-dependent scalar retuning makes the available majorant weakly worse; if `t sigma_j !=0` for at least one direction and `alpha!=(2*pi*e)^2`, it is strictly worse.
3. For rank `r`, the optimally tuned bound still has large-`|t|` decay `|t|^{-r/4}`. In particular rank/order four remains exactly at the nonintegrable `1/|t|` endpoint. Therefore a `17 -> 13` reduction cannot come from scalar regularizer tuning inside this proof; it needs a genuinely stronger structured endpoint or a different structural reduction.

This sharpens my preceding run's asymptotic regularizer obstruction to an exact global optimization theorem.

## Counterexample status and next obligation

My previous run already supplied the source-valid route obstruction `Q_0=2UV` (independent cap-one uniforms): logarithmically unbounded density despite `|phi(t)|=O(1/|t|)` and uniformly finite half-potential. The exact optimizer above now closes the remaining possibility that a different scalar `alpha(t)` could strengthen the manuscript's order-four graph-BL output enough to bypass that obstruction.

The first unpaid threshold-lowering implication is therefore:

**`QFORM-FIXEDMULT-K4-STRUCTURED-ENDPOINT-v2`** — under the actual original-coordinate product provenance and a quantitative fourth crossing volume, prove a dimension-free `L^infinity` density bound while retaining arbitrary measurable same-bank quadratic/affine terms, or produce a counterexample in that exact structured branch. A black-box combination of `1/|t|` Fourier decay with the existing half-potential bound is insufficient, and scalar graph-regularizer retuning is now exactly ruled out.

No threshold below seventeen is claimed until that endpoint or an alternative complete dependency chain is proved with explicit constants.
