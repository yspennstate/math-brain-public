# fleet02/B02 independent fixed-multiplicity audit

Run: `20260924T120609Z-fleet02-B02-fixedmult-audit-r11`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Lens: scalar Fourier powers, convolution and projection constants; counterexample/adversarial exact-law checks.

## Source pin

- Repository: `yspennstate/math-open-problems`, branch `master`.
- Fresh master observed before publication: `2886aaea3eb2cf55fff7b70e878fd175efb705fc`.
- Canonical manuscript path: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.
- Manuscript git blob read in full: `183ccd294763214e6a707e8d4749ff9a8cf7006d` (unchanged from owner-specified initial source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`).
- Owner README/AUDIT declare source SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`; this run verified the git blob identity, not an independently recomputed SHA-256.

## Verdict

**Mathematical verdict: PASS for the written 17-eigenvalue theorem.** I found no fatal mathematical defect in an independent end-to-end reading and rederivation of the complete 790-line manuscript. The theorem audited is exactly

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for arbitrary dimension, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, arbitrary affine `b,c`, and independent real coordinates with densities bounded by `K`.

There are two nonfatal gaps: (i) one projection-proof line is ambiguous about the index set of a sum, although either correct interpretation gives the asserted bound; (ii) the canonical repository root still lacks the four supplemental files named by its README (`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`). The latter blocks independent rerunning of the advertised finite checks but does not affect the self-contained symbolic proof in `manuscript.tex`.

This review does not claim the unrestricted three-eigenvalue conjecture and does not alter release/validation status. A release gate should apply the owner's separate-review rule independently.

## Complete source ledger

### Lines 1-100 — PASS

Definitions of singular values, essential density norm, theorem quantifiers, the `s_17` hypothesis, affine terms, and the `K^2/s` scale are coherent. The normalization `Y=KX` gives coordinate caps at most one and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c=(K^2/s)Q,
\]

so the final density rescales by `K^2/s` exactly. Fourier convention `\widehat f(t)=\int e^{itx}f(x)dx`, Gaussian `g_\varepsilon=(4\pi\varepsilon)^{-1/2}e^{-x^2/(4\varepsilon)}`, and inversion factor `1/(2\pi)` are mutually consistent.

### Lines 101-200 — PASS

Plancherel has factor `2\pi`. Gaussian inversion

\[
E e^{-v(Z-a)^2}=(2\sqrt{\pi v})^{-1}\int e^{-t^2/(4v)}e^{-ita}\phi_Z(t)dt
\]

has the correct normalization. The power-envelope integral is exactly `2ap/(p-1)`, hence density `ap/[\pi(p-1)]`. The half-Riesz calculation is also normalized correctly: after Tonelli,

\[
\int_0^\infty v^{-5/4}e^{-t^2/(4v)}dv
=\sqrt2\,\Gamma(1/4)|t|^{-1/2},
\]

giving coefficient `(2\pi)^{-1/2}`. The `3/4` envelope produces weighted integral `12\sqrt u`, hence `12\sqrt{u/(2\pi)}`. Singular-value perturbation and the Schur-count argument are used with the correct inequality directions.

### Lines 201-300 — PASS, with one presentation GAP at the projection summation line

The singular Schur-complement limit is valid. Strict diagonal dominance is stated correctly for nonsymmetric matrices. The geometric rank-one Brascamp-Lieb heat-flow proof has the right sign:

\[
\partial_tF-\Delta F=F\bigl(\sum c_iv_i^2-|\sum c_iu_iv_i|^2\bigr)\ge0,
\]

and its large-time Gaussian limit, small-time Fatou step and monotone truncation close the rough-input case.

For product projections, `b_i=|w_i|^2=1-|U^Te_i|^2`, the normalized `w_i` form the required frame, and `f_i^{1/b_i}\le f_i` because `0\le f_i\le1`. The entropy estimate gives `\|p_{U^TX}\|_\infty\le e^{d/2}`. **GAP (presentation only):** after rows with `b_i=0` are dropped from the Brascamp-Lieb product, the displayed equality `\sum_i(1-b_i)=d` must be understood as summing over all physical rows; over only retained rows it is merely `\le d`. The asserted upper bound remains valid either way. Recommended repair: write `\sum_{b_i>0}(1-b_i)\le\sum_i(1-b_i)=d`.

The scalar Fourier-power lemma is valid and noncircular. For `p\ge2`, `m=\lfloor p/2\rfloor\ge p/4`; since `|\widehat f|\le1`, `\int|\widehat f|^p\le\int|\widehat f|^{2m}`. Plancherel already makes the latter integrable. Fourier inversion at zero plus the scalar projection bound for the `2m` signed independent coordinates gives

\[
\int|\widehat f|^p\le {2\pi\sqrt{2e}\over\sqrt p}.
\]

The difference density `f*\widetilde f\le1` follows exactly from cap times unit mass.

### Lines 301-400 — PASS

The cross-form split retains all same-bank quadratic and affine terms. Two-copy decoupling uses only original-coordinate independence. Jensen correctly upgrades the nonnegative second-power majorant to the fourth-power estimate.

In the determinant theorem, with `a=2t`, `\alpha=(2\pi e)^2`, `H=\alpha I+a^2M^TM`, the `c_j,d_i` vectors form an exact weighted frame. For `h_i=|\widehat f_i|^2`, applying the scalar Fourier lemma with `p=2/d_i` yields

\[
\|h_i\|_{1/d_i}\le (2\pi\sqrt{e d_i})^{d_i}.
\]

The `d_i` powers cancel the Brascamp-Lieb scaling factors; `\prod c_j^{-c_j/2}\le e^{\theta/2}` and `\alpha=(2\pi e)^2` cancel the remaining regularizer factor. Fourth-rooting gives exactly

\[
|\phi_Z(t)|\le\det\left(I+{t^2\over\pi^2e^2}M^TM\right)^{-1/8}.
\]

Cauchy-Binet gives the stated `Z_k` expansion. Keeping one order-`k` term gives exponent `k/4`. For `k=5`, `5/4>1` and the density constant is exactly `5e Z_5^{-1/10}`. For `k=3`, `3/4` is not directly integrable, but after multiplication by the half-Riesz weight `|t|^{-1/2}` the tail is `|t|^{-5/4}`, yielding the stated half-potential bound.

### Lines 401-549 — PASS

The scalar square profile and inverse-interval estimate are correct. Conditioning gives the Schur-complement profile as a measure-domination statement, without claiming independence. The definite-pair Jacobian is `1/(2\sqrt{|\det B|})`, so integrating `\theta\in[0,2\pi)` gives the sharp factor `\pi`.

The hyperbolic parametrization has absolute Jacobian `1/(2\sqrt D)`. Its tail change of variables uses only one original-coordinate density cap and mass one; the middle interval length and `\Lambda\ge2/\sqrt D` give the displayed logarithmic envelope. The quarter-power lemma's random sign cut is a physical coordinate cut. Its Gaussian smoothing integral has coefficient

\[
2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8),
\]

which is safely below 16 by the manuscript's elementary estimates. Layer cake gives `L_0=4+4\log16`.

The definitions of pivots and ordered disjoint volumes are precise. No-pivot entry bounds follow from `\eta=1/100`.

### Lines 550-700 — PASS

The volume-sampling identity is a bordered determinant identity. Singular seeds have zero sampling weight, so counting extensions only gives an inequality, exactly as stated. The nonsymmetric interpolation

`P=A[:,T] A[S,T]^{-1} A[S,:]`

interpolates rows `S` and columns `T`. In `A=D+R+E`, `D` vanishes on the seed, `E` has zero diagonal, global `rank(R)\le3r`, and `rank(R[L,L])\le r`; these distinct rank bounds are used in the correct places.

In the spectral-to-volume proposition, a bad volume ratio gives `\|E\|_F\le(r+1)/80\le1/16`. Rank perturbation forces at least `r+1` large diagonal entries of `D` in the seed complement because `m=4k-3\ge4r+1`. There,

\[
|R_{ii}|\ge371/400,
\qquad
\sum_{j\ne i}|R_{ij}|<4(1/7+1/16)=23/28<371/400,
\]

so the `(r+1)` compression is invertible, contradicting restricted rank `\le r`. The random coordinate cut pays each ordered disjoint `(S,T)` with probability `4^{-k}`. Consequently `Z_k^{-1/(2k)}\le160`; `k=3` gives full half potential `<200`, `k=5` gives density `<2400`.

The singular-kernel estimates, truncated half-potential definition, and pivot reductions preserve the distinction between full and truncated potentials.

### Lines 701-790 — PASS

For a scalar pivot, the Schur complement loses at most one large eigenvalue, leaving at least 16 and therefore enough for the nine-eigenvalue full half-potential theorem; the final constant is `10*601=6010`. A definite pair gives `<40`. An indefinite pair loses at most two large eigenvalues, leaving at least 15, in particular a norm-one surviving direction; the logarithmic-potential averaging gives `<251`. The no-pivot branch is `<2400`. The final `10^4` bound therefore closes all cases. The manuscript correctly limits continuity to the Fourier branch and explicitly does not claim the three-eigenvalue conjecture.

## B02 exact-law adversarial checks

1. **Scalar Fourier exponent is sharp.** The admissible cap-one Gaussian `f_G(x)=e^{-\pi x^2}` is a probability density with
   \[
   \widehat f_G(t)=e^{-t^2/(4\pi)},\qquad
   \int|\widehat f_G(t)|^pdt={2\pi\over\sqrt p}.
   \]
   Hence the universal `p^{-1/2}` power in the scalar Fourier lemma cannot be improved to `p^{-\alpha}` with any `\alpha>1/2`. The manuscript constant has only the factor `\sqrt{2e}` of slack on this exact family.

2. **Uniform law checks convolution constants.** For `f=1_{[-1/2,1/2]}`, `\widehat f(t)=2\sin(t/2)/t`, so
   \[
   \int|\widehat f|^2=2\pi,\qquad \int|\widehat f|^4={4\pi\over3}.
   \]
   Its difference density is `(1-|x|)_+`, whose supremum is exactly one. Thus the manuscript's difference cap `g\le1` is sharp.

3. **Projection homogeneity.** For independent cap-one Gaussians `e^{-\pi x_i^2}`, the scalar projection `a\cdot X` has peak exactly `1/\|a\|_2`. The manuscript's `\sqrt e/\|a\|_2` has safe constant slack and correct scaling. A one-coordinate uniform law saturates the basic `1/|a|` scale.

4. **Bilinear Fourier normalization.** For independent cap-one Gaussians `X,Y` and `Z=2mXY`, direct Gaussian integration gives
   \[
   \phi_Z(t)=\left(1+{m^2t^2\over\pi^2}\right)^{-1/2}.
   \]
   The manuscript determinant envelope for the one-by-one block is
   \[
   \left(1+{m^2t^2\over\pi^2e^2}\right)^{-1/8},
   \]
   which is a valid upper bound and confirms both the factor two in the cross term and the `\pi^2e^2` regularizer normalization.

5. **Pivot constants have exact extremizers/asymptotics.** For `Y` uniform on `[-1/2,1/2]`, `Y^2` has density `z^{-1/2}` on `(0,1/4)`, saturating the scalar square profile. For two independent such uniforms, `Y_1^2+Y_2^2` has density exactly `\pi` for sufficiently small positive output, saturating the definite-pair constant. For `Y_1^2-Y_2^2`, the density has a logarithmic singularity with leading coefficient one, confirming the necessity and correct scale of the hyperbolic logarithm.

## Endpoint obstruction and threshold-improvement verdict

The present B02 analytic route cannot lower 17 by tightening scalar Fourier, convolution, or projection constants alone. The scalar `p^{-1/2}` exponent is exact by the Gaussian example above. The determinant theorem then gives, from a single order-`k` crossing volume, only

\[
|\phi(t)|\lesssim |t|^{-k/4}.
\]

Direct Fourier inversion needs `k/4>1`; `k=4` is the exact logarithmically divergent endpoint `|t|^{-1}`, so order five is the first direct-density order. The structural proposition with order five has worst seed order `r=4` and requires `m-3r\ge r+1`, i.e. `m\ge17`. Therefore **no complete lower-threshold theorem follows from constant optimization within the current chain**. A genuine reduction below 17 needs a replacement argument: e.g. an endpoint order-four receiver using additional determinant degrees, a stronger decoupling/determinant exponent with all hypotheses closed, or a structural interpolation/rank improvement. No such complete replacement is asserted here.

## Repository-package GAP

Fresh root listings at both the initial source commit and current master do not contain `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, or `checks.json`, although the repository README/AUDIT name them as canonical artifacts. Status: **GAP (reproducibility/package, nonmathematical)**. Downstream impact: this run cannot independently rerun or source-map the advertised finite tests from the canonical root. The self-contained symbolic proof remains auditable from `manuscript.tex`. Next obligation: restore/publish those exact supplementary artifacts with source-pinned hashes, or amend the README/AUDIT to describe their actual location.

## Review status

This is a complete independent mathematical review by fleet02/B02. It is not formal verification and not a self-awarded release certificate. The owner-required multi-review/release gate remains a separate decision. No unrestricted three-eigenvalue QFORM claim is made.
