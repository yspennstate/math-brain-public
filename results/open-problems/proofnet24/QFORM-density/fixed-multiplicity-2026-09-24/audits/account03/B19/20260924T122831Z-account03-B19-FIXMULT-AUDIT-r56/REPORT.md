# account03/B19 independent end-to-end audit — fixed multiplicity 17

Run: `20260924T122831Z-account03-B19-FIXMULT-AUDIT-r56`  
Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Execution status: `WITHOUT_VERIFIED_BRAIN`  
Pinned manuscript source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Pinned manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Fresh master immediately before publication: `493563c7ef8d2deae4cc68d11855c3f732796b46`; the manuscript blob was still exactly the pinned blob.

## Verdict

**Mathematical verdict: PASS on the complete 790-line 17-eigenvalue argument.** I independently read and reconstructed the full manuscript before consulting peer verdicts. I found no fatal mathematical gap in the theorem

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, arbitrary affine `b,c`, and independent real coordinates whose densities satisfy only `0<=f_i<=K` a.e.

This is one independent worker review, not formal verification and not a self-awarded independent-validation certificate. The unrestricted three-large-eigenvalue conjecture remains open. The manuscript proves a globally essentially bounded density; continuity is automatic only on the no-pivot integrable-Fourier branch, not on all pivot branches.

I found one **nonfatal local wording gap** in the product-projection proof and one **repository-package reproducibility gap**. Neither changes the theorem. I also found a rigorous same-proof constant improvement from `10000` to `3910`, recorded separately under this run's improvement folder. I did not prove a reduction from 17 to 16 eigenvalues.

## End-to-end audit ledger

### Statement, quantifiers, normalization, Fourier inversion — PASS

The theorem keeps every advertised hypothesis and does not introduce Gaussianity, moments, compact support, connected support, log-concavity, or rotated-coordinate independence. The normalization is correct: with `Y=KX`, the coordinates of `Y` have density cap one and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\qquad Q=(s/K^2)\widetilde Q.
\]

Hence a normalized density constant rescales by exactly `K^2/s`.

The Gaussian regularization, Plancherel convention and Fourier inversion constants are mutually consistent. The inversion proof does not presuppose absolute continuity of the unsmoothed law.

### Negative half moments and spectral preliminaries — PASS

The gamma/Gaussian calculation gives

\[
\mathbb E|Z-a|^{-1/2}
\le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|\,dt.
\]

The `3/4` characteristic-function exponent is used only after multiplication by the Riesz weight and is never misused as an `L^1` Fourier bound.

The nonsymmetric singular-value approximation/rank inequalities have the correct index direction. For an invertible principal pivot, the complementary principal block of `A^{-1}` is the inverse Schur complement, and positive/negative interlacing yields `N_S(t)>=N_A(t)-k`. The singular ambient case follows by `A+epsilon I` and continuity of ordered eigenvalue moduli.

### Geometric Brascamp–Lieb and product projections — PASS with one wording repair

The heat-flow sign is correct: the frame identity makes the map with columns `sqrt(c_i)u_i` a contraction, so

\[
\left|\sum_i c_i u_i v_i\right|^2\le\sum_i c_iv_i^2.
\]

The large-time Gaussian limit and the `t downarrow 0` Fatou argument are adequate, and monotone truncation covers general nonnegative integrable inputs.

**GAP-NONFATAL (wording only):** in the product-projection lemma, after factors with `b_i=0` are dropped, the manuscript writes

`sum_i (1-b_i)=d`.

If this displayed sum is read as running only over the retained `b_i>0` indices, equality need not hold. The correct statement is

\[
\sum_{b_i>0}(1-b_i)\le d,
\]

or, equivalently, equality holds before dropping the zero-`b_i` rows. Since the line is used only as an upper bound, replacing `=` by `<=` repairs the proof with no constant or theorem change.

The proof correctly chooses representatives of the marginal densities bounded pointwise by one at this location. For maximum presentation robustness the same bounded-Borel representative convention should be declared globally once; this changes no law.

### Scalar Fourier powers, decoupling and graph determinant — PASS

The even-power reduction is valid because `|fhat|<=1`, while integrability of `|fhat|^{2m}` follows from Plancherel. The density-at-zero evaluation is therefore legitimate and gives the displayed `2*pi*sqrt(2e)/sqrt(p)` bound.

The two-copy decoupling uses only original-coordinate independence. The fourth-power inequality is a Jensen consequence of the nonnegative second-power majorant.

For `H=alpha I+a^2M^TM`, the physical coordinate vectors and rows of `M` form the exact frame used in graph Brascamp–Lieb. The factors `c_j,d_i`, the trace identity, the one-dimensional Jacobians, and the scalar Fourier exponents `2/d_i` all match. With `alpha=(2*pi*e)^2` and `a=2t`, fourth-rooting gives exactly

\[
|\phi_Z(t)|\le
\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
\]

Cauchy–Binet gives the `Z_k` expansion. Order five gives exponent `5/4>1` and direct density inversion; order three gives exponent `3/4` and is used only for the half-potential.

### Scalar, definite-pair, hyperbolic-pair and quarter-power estimates — PASS

The scalar square formula and interval-preimage estimate are deterministic one-dimensional changes of variables applied after conditioning. The definite-pair proof rotates only the deterministic integral, not the law.

The hyperbolic pair has Jacobian `1/(2 sqrt(|det B|))`. Each tail is controlled by one original marginal using its cap and total mass; the middle region produces the logarithm. The exceptional critical level is harmless in the nonnegative-test-function/Tonelli formulation.

The quarter-power dichotomy is correct. If no large physical diagonal exists, a random-sign physical partition extracts a genuine original-coordinate cross block with norm at least one quarter of the operator norm. The graph determinant theorem then supplies the `|t|^{-1/4}` input to Gaussian smoothing. This is not the refuted uniform quadratic van-der-Corput mechanism.

### Disjoint-minor sampling, completion and spectral-to-volume conversion — PASS

For a nonsingular disjoint seed `B=A[S,T]`, the bordered determinant identity

\[
\det A_{S\cup\{\ell\},T\cup\{m\}}^2
=
\det(B)^2(A_{\ell m}-P_{\ell m})^2
\]

is exact up to sorting signs, which disappear on squaring. Singular deleted seeds may have nonsingular extensions, so the proof correctly uses an inequality rather than equality when summing.

The completion `A=D+R+E` has simultaneously

\[
\|E\|_F\le(r+1)\sqrt{V_{r+1}/V_r},\qquad
\operatorname{rank}R\le3r,
\qquad R_{L,L}=P_{L,L},
\qquad \operatorname{rank}R_{L,L}\le r,
\]

and `D` vanishes on `S union T`. I independently checked the support statement: `R-P` vanishes on rows `S`, columns `T`, and the full `L x L` block, so its remaining support is contained in rows `T` or columns `S`; this gives the extra `2r` rank and hence the global `3r` bound. Symmetry of `R,E` is neither claimed nor needed.

In the bad-volume-ratio branch, `||E||_F<=1/16`. Rank perturbation forces `r+1` large diagonal entries of `D` on `L`. On those entries,

\[
|R_{ii}|\ge371/400,
\qquad
|R_{ij}|<1/7+1/16,
\]

and for `r<=4` the off-diagonal row sum is `<23/28<371/400`. Thus `R[H,H]` is invertible of rank `r+1`, contradicting `rank R[L,L]<=r`. The `r=0` case is separate and correct.

The fair coordinate cut retains each ordered disjoint `k`-minor with probability `4^{-k}`. Therefore the order-three and order-five analytic consequences follow exactly as stated.

### Pivot half-potentials and final proof — PASS

The scalar pivot is a conditional measure-domination statement, not an independence assertion. Its Schur remainder retains the required large spectral directions. Definite and indefinite pair bounds are averaged over the complement using Tonelli.

The nine-eigenvalue half-potential proposition correctly distinguishes a truncated pivot estimate from the full no-pivot estimate; outside distance one, the kernel contributes at most one.

The final normalized branches close:

- no pivot and `s_17>=1`: density `<2400`;
- scalar pivot: Schur leaves at least 16 large directions, hence the nine-direction half-potential applies;
- definite pair: density `<40`;
- indefinite pair: Schur leaves at least 15 directions, and one surviving direction controls the logarithmic critical-value potential.

The stated `10000` bound is therefore valid. The separate improvement file proves that exactly the same argument, with only elementary tightening of constants, gives `3910` instead.

## Fixed-multiplicity 16: exact terminal obstruction, no theorem claimed

I independently reran the rank count under the hypothetical assumption `s_16(A)>=1`. All ratio indices `r<=3` still close by the manuscript's contradiction. The only new obstruction is terminal `r=4`: global `rank R<=12` forces only four large entries of `D`, while restricted `rank R[L,L]<=4` is compatible with a nonsingular `4x4` block. Thus changing `17` to `16` in the present proposition is invalid.

The four forced indices `H subset L` nevertheless give a strongly diagonally dominant

\[
P_{H,H}=A[H,T]B^{-1}A[S,H].
\]

Using the sharper no-pivot entry estimate gives an invertible three-bank configuration `(S,T,H)`. I then applied the completed account02/B14 terminal-seed result at this exact `r=4` inequality: with

\[
\delta=109/350,
\quad b=|\det A[S,T]|,
\quad c=|\det A[H,T]|,
\quad e=|\det A[S,H]|,
\]

one has

\[
ce/b=|\det P_{H,H}|\ge\delta^4,
\]

while every disjoint `4x4` cross minor obeys Hadamard's bound `<=16/2401`. Consequently

\[
\boxed{c\ge(109/100)^4 b,\qquad e\ge(109/100)^4 b.}
\]

So a sampled-good terminal seed forces two strictly heavier neighboring order-four minors. This is real extra structure, but it does not yet imply the 16-eigenvalue theorem because the heavier neighboring seeds are not known to inherit the same small residual bound. The next threshold obligation is to control this good-seed/heavier-neighbor transfer globally, or to replace the borderline order-four `|t|^{-1}` absolute Fourier endpoint by a product-structure-sensitive endpoint estimate.

## Actual application of the designated account04/B19 result

The latest compatible account04/B19 finite-hub theorem says that a physical decomposition `D+K_r+F` with `rank K_r<=r`, `||F||op<delta`, and at least `r+3` physical coordinates satisfying `|D_ii|>=a>delta` has

\[
\|p_Q\|_\infty
\le
\frac{250(r+3)[8+\log(r+3)]}{a-\delta}.
\]

Apply it to the manuscript's terminal `r=4` completion, viewed with global low-rank parameter `r_global=12`, `F=E`, `||E||op<=1/16`, and `a=1/2`. Whenever that completion has at least fifteen such diagonal coordinates, the full ambient law is paid by

\[
\boxed{
\|p_Q\|_\infty
<
\frac{250\cdot15(8+\log15)}{1/2-1/16}
<91784.
}
\]

This is a scoped application, not a proof of the terminal `s_16` case: the rank count there guarantees only four large diagonal coordinates, not fifteen. It nevertheless cleanly removes the high-diagonal-multiplicity subbranch without dropping the error `E`.

## Packaging/reproducibility status

At fresh master `493563c7ef8d2deae4cc68d11855c3f732796b46`, the manuscript root still contains `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`, but the README-advertised `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are absent from the root listing. I therefore did not claim to rerun those advertised finite checks from the repository package. This is a reproducibility-package gap, not a mathematical gap in the self-contained manuscript.

## Final status

- 17-eigenvalue mathematical theorem: **PASS in this independent B19 audit**.
- Fatal mathematical defect: **none found**.
- Local proof wording repair: product-projection entropy sum should use `<=d` after zero-weight rows are dropped.
- Optional global rough-law presentation repair: declare bounded Borel density representatives once near the start.
- Valid same-proof constant: **3910 K^2/s** (proved in the companion improvement file).
- 16-eigenvalue theorem: **OPEN / not proved here**.
- Three-eigenvalue conjecture: **OPEN**.
- Global continuity: **not proved** by this manuscript; essential boundedness is the validated scope.
- Native learned-memory ingestion: **WITHOUT_VERIFIED_BRAIN**.
