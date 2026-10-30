SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-24T12:25:12Z.
attacking: the current fixed-multiplicity candidate end-to-end, with emphasis on Gaussian inversion, the Riesz half-potential, rough-law regularity, and whether the order-four endpoint can lower 17 to 13.

# fleet03/B15 complete fixed-multiplicity audit

Run: `20260924T122512Z-fleet03-B15-fixed-multiplicity-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Initial manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Owner-supplied source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Publication-refresh master inspected before write: `0e09d541a8749be0b70a595cb5abaa4ab7559b2d`; manuscript blob unchanged.

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent fleet03/B15 audit.** I read the complete 790-line manuscript and reconstructed every dependency needed for the theorem

\[
s_{17}(A)\ge s>0 \quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4 K^2/s
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary signs and remaining spectrum, arbitrary affine terms, and arbitrary independent real coordinate densities bounded by `K`.

I found **no fatal mathematical defect**. I found one local wording gap in the projection lemma and one repository-package/reproducibility gap. Neither changes the theorem after the stated local repair. The unrestricted three-eigenvalue conjecture remains open. This report is an independent worker audit, not a self-awarded release or formal-verification certificate.

## B15 focal audit: Gaussian inversion and Riesz half-potential

### Lines 91–123: Fourier inversion and Gaussian regularization — PASS

The manuscript convention is

\[
\widehat f(t)=\int e^{itx}f(x)\,dx.
\]

For `g_epsilon(x)=(4 pi epsilon)^(-1/2) exp(-x^2/(4 epsilon))`, one has `g_hat=e^{-epsilon t^2}`. The regularized Plancherel identity has the correct `2 pi` factor, and the approximate-identity limit in `L^2` is legitimate. If `phi_Z in L^1`, the Gaussian-smoothed laws converge uniformly to

\[
p_Z(x)=\frac1{2\pi}\int e^{-itx}\phi_Z(t)\,dt,
\]

so this branch has a canonical bounded continuous density. The separate identity

\[
\mathbb E e^{-v(Z-a)^2}
=\frac1{2\sqrt{\pi v}}
\int e^{-t^2/(4v)}e^{-ita}\phi_Z(t)\,dt
\]

has the correct normalization.

### Lines 124–160: Riesz half-potential — PASS

The gamma representation

\[
|z|^{-1/2}=\Gamma(1/4)^{-1}\int_0^\infty v^{-3/4}e^{-vz^2}\,dv
\]

combined with Gaussian inversion gives, after Tonelli and the exact substitution `w=t^2/(4v)`,

\[
\int_0^\infty v^{-5/4}e^{-t^2/(4v)}\,dv
=\sqrt2\,\Gamma(1/4)|t|^{-1/2}.
\]

Therefore

\[
\boxed{
\mathbb E|Z-a|^{-1/2}
\le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|\,dt .
}
\]

The argument is valid with extended nonnegative values and does not require a pre-existing density for `Z`. If

\[
|\phi_Z(t)|\le \min\{1,(u/|t|)^{3/4}\},
\]

then

\[
2\int_0^u t^{-1/2}dt+2u^{3/4}\int_u^\infty t^{-5/4}dt=12\sqrt u,
\]

so the displayed manuscript constant `12 sqrt(u/(2 pi))` is exact.

### Completed partner result applied to an actual inequality — PASS

I independently derived the preceding Riesz identity before reading the completed `fleet04/B15` audit. I then applied that partner-checked identity to the manuscript's actual no-pivot nine-direction inequality.

For `s_9(A)>=1` and no `eta`-pivot, the sampled order-three crossing block satisfies

\[
Z_3^{-1/6}\le 160.
\]

The volume envelope has

\[
u_3=\pi e Z_3^{-1/6}\le160\pi e,
\qquad
|\phi_Q(t)|\le\min\{1,(u_3/|t|)^{3/4}\}.
\]

The partner-verified Riesz compiler therefore gives

\[
\boxed{
\sup_a\mathbb E|Q-a|^{-1/2}
\le12\sqrt{u_3/(2\pi)}
\le12\sqrt{80e}
=176.959336\ldots<200.
}
\]

This is the exact quantitative input used later in the scalar-pivot branch, not merely a qualitative citation.

## Full end-to-end audit ledger

### Lines 45–90: statement, quantifiers, and scaling architecture — PASS

The theorem retains all advertised hypotheses. No support, moment, log-concavity, smoothness, or sign assumption is introduced. The normalization `Y=KX`, `A -> A/s` and `Q=(s/K^2) Q_tilde` produces the final factor `K^2/s` correctly.

### Lines 162–220: singular values, Schur spectral count, diagonal dominance — PASS

The nonsymmetric singular-value perturbation inequality is used in its valid singular-value form. For an invertible principal pivot `B`, the complementary principal block of `A^{-1}` is `S^{-1}`; interlacing applied separately to positive and negative spectral thresholds gives `N_S(t)>=N_A(t)-k`. The singular case is correctly obtained by an `A+epsilon I` limit with a moving threshold. Strict row diagonal dominance is valid without symmetry.

### Lines 221–255: geometric Brascamp–Lieb heat flow — PASS

For `sum c_i u_i u_i^T=I`, the column operator with columns `sqrt(c_i)u_i` is a contraction, giving

\[
\sum_i c_i v_i^2-\left|\sum_i c_i u_i v_i\right|^2\ge0.
\]

The compact-support Gaussian tail argument justifies differentiation and integration by parts. The large-time Gaussian limit and the small-time Fatou passage are valid, followed by monotone approximation for general nonnegative integrable inputs.

### Lines 256–283: product projection density — PASS WITH WORDING GAP

The result `||p_{U^T X}||_infty <= e^{d/2}` is valid. The proof drops indices with `b_i=0`, then writes `sum_i(1-b_i)=d`. If that sum is read as only over retained indices, the correct statement is

\[
\sum_{b_i>0}(1-b_i)\le d.
\]

Alternatively, retain all indices in that final identity. The proof needs only the upper bound, so this is a local wording repair and changes no theorem or constant.

### Lines 284–301: integrated scalar Fourier powers — PASS

For `p>=2`, `m=floor(p/2)` and `|f_hat|<=1` reduce the integral to an even power. That even power is the characteristic function of a sum of independent signed differences. The one-dimensional product-projection estimate at zero gives the stated `2 pi sqrt(2e)/sqrt(p)` bound.

### Lines 303–400: decoupling, determinant theorem, crossing volumes — PASS

The two-copy decoupling uses only original-coordinate independence. The graph weights

`c_j=alpha e_j^T H^{-1}e_j`, `d_i=a^2 m_i^T H^{-1}m_i`

form the required geometric frame. With `alpha=(2 pi e)^2` and `a=2t`, the `d_i` powers cancel against the scalar Fourier-power estimate and the `c_j` entropy factor cancels the remaining regularizer scale, yielding exactly

\[
|\phi_Z(t)|\le
\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

Cauchy–Binet then gives the crossing-volume expansion. The order-five exponent is `5/4>1` and yields an `L^1` characteristic function; the order-three exponent `3/4` is used only after the Riesz weight. The manuscript does not confuse those conclusions.

### Lines 401–536: scalar, definite-pair, hyperbolic-pair, and quarter-power estimates — PASS

The scalar square profile is conditional measure domination, not an independence assertion. The definite-pair proof is a deterministic two-dimensional change of variables after conditioning. The indefinite-pair hyperbolic parameterization has Jacobian `1/(2 sqrt(D))`; its tails are paid using a single original coordinate density cap and total mass, not a rotated-coordinate cap. The quarter-power lemma correctly obtains a physical cross block from a sign partition and uses one singular factor from the determinant theorem. The resulting small-ball exponent and logarithmic-potential bound are consistent.

### Lines 537–621: sampled nonsymmetric interpolation and spectral-to-volume conversion — PASS

For a disjoint nonsingular seed `B=A_{S,T}`,

\[
P=A_{\cdot,T}B^{-1}A_{S,\cdot}
\]

has rank at most `r` and exactly interpolates rows `S` and columns `T`. The bordered determinant identity gives the expected residual bound. Singular seeds are omitted, so the extension count is correctly an inequality.

In `A=D+R+E`, `D` vanishes on `S union T`, `E` is zero-diagonal and supported in `L x L`, `rank R<=3r`, while `R_{L,L}=P_{L,L}` has rank at most `r`. The proof correctly distinguishes the global `3r` rank from the restricted `r` rank.

Assuming `V_k<kappa^k` yields a ratio `V_{r+1}/V_r<kappa`. With `m=4k-3`, rank perturbation forces at least `r+1` large diagonal entries of `D` in `L`; their principal submatrix of `R` is strictly row-diagonally dominant, contradicting `rank R_{L,L}<=r`. The explicit arithmetic slack is positive.

### Lines 622–651: random cut and no-pivot consequences — PASS

Each ordered disjoint `k`-minor survives a fair coordinate cut with probability `4^{-k}`, hence `E Z_k(A_{I,J})=4^{-k}V_k(A)`. For `k=3` this gives the full half-potential bound above; for `k=5` it gives

\[
\|p_Q\|_\infty\le800e=2174.625462\ldots<2400.
\]

### Lines 652–725: singular kernels, truncated versus full half potential — PASS

The manuscript correctly separates

\[
H(Z)=\sup_a\mathbb E[|Z-a|^{-1/2}{\bf1}_{|Z-a|\le1}]
\]

from the full half potential. The pivot proposition proves only the truncated bound `H<=600`. The nine-eigenvalue proposition then adds at most one from the region `|Z-a|>1`, obtaining the full bound `<=601`. The main scalar-pivot density estimate invokes this full bound. No truncation/full-potential swap occurs.

### Lines 726–790: final closure and regularity scope — PASS

The branches give, in the normalized case:

- no pivot: `<2400`;
- scalar pivot: `10*601=6010`;
- definite pair: `10 pi<40`;
- indefinite pair: `<251`.

All are below `10^4`. Conditioning is always on original coordinates and affine terms are retained.

For regularity, the manuscript is intentionally asymmetric. The no-pivot order-five branch has `phi in L^1`, hence a canonical continuous `C_0` density. The pivot branches establish measure domination and therefore an essentially bounded density, but the manuscript does **not** infer continuity from `L^infty` alone. The global theorem therefore correctly claims essential boundedness only.

## Threshold-lowering attempt

The same algebraic skeleton with order `k=4` would require `4k-3=13` large singular directions and would force a lower bound on the fourth crossing volume. However the determinant theorem then provides only the critical envelope

\[
|\phi(t)|\lesssim |t|^{-1},
\]

which is not absolutely integrable. This endpoint cannot by itself give an `L^infty` density. A concrete sanity check is the product `UV` of independent uniforms on `[-1,1]`:

\[
p_{UV}(x)=\tfrac12\log(1/|x|){\bf1}_{0<|x|<1},
\]

which is unbounded, while its characteristic function is `Si(t)/t=O(1/|t|)`. Thus **this run does not certify a 13-eigenvalue theorem**.

Nor does the current rank argument immediately give 16: at the worst `k=5,r=4` step, sixteen large singular values only force four large diagonal coordinates after the global rank-12 correction, whereas the restricted correction may itself have rank four; the contradiction requires five. The manuscript's global `3r` and restricted `r` roles cannot simply be merged or replaced by an unsupported `2r` estimate.

The next honest reduction target is therefore a genuinely structured order-four endpoint estimate, or a different structural argument that improves the spectral-to-volume count while preserving arbitrary signs, affine terms, all extra spectrum, and rough cap-one product laws.

## Repository/package gap — GAP, nonmathematical

At the inspected current master, the fixed-multiplicity root contains `manuscript.tex`, `README.md`, `AUDIT.md`, and the `audits/` and `improvements/` directories. The README advertises `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json`, but these supplementary files were absent; direct retrieval of `proof_map.csv` returned 404. This is a reproducibility/package-delivery gap, not a defect in the symbolic proof.

## Status

- Mathematical 17-eigenvalue baseline: **PASS in this audit**.
- Fatal mathematical defect found: **none**.
- Local mathematical wording repair: projection lemma final equality should be an inequality if restricted to retained indices.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity from this manuscript: **not proved**; no-pivot branch is continuous, pivot branches are only essentially bounded here.
- Multiplicity lower than 17 established in this run: **none**.
- Independent-validation/release status: **not self-awarded**; owner/release gate must synthesize genuinely separate complete reviews.
- Execution context: `WITHOUT_VERIFIED_BRAIN`; authenticated repository retrieval/readback occurred, but no native mathematical-receiver ingestion was verified.
