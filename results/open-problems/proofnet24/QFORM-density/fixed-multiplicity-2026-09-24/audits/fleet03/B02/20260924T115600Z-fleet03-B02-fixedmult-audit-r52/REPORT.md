# fleet03/B02 independent full audit — fixed multiplicity 17

Run: `20260924T115600Z-fleet03-B02-fixedmult-audit-r52`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`  
Manuscript: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`

## Verdict

**PASS for the mathematical 17-eigenvalue baseline in this independent fleet03/B02 audit.** I read the complete 790-line source at the pinned commit and re-derived the dependency chain rather than relying on prior audit verdicts. I found no fatal mathematical gap and no hypothesis loss. The theorem retains arbitrary dimension, arbitrary independent real coordinate laws with only density cap `K`, arbitrary real symmetric `A`, arbitrary signature and remaining spectrum, and arbitrary affine `b,c`.

I do **not** mark the manuscript independently validated; that status is a release-gate decision requiring genuinely separate complete reviews and synthesis. The full three-large-eigenvalue conjecture is still open. Global continuity is not proved by the manuscript; continuity is supplied only on the no-pivot Fourier branch.

There is a **repository-package GAP**: the current root listing contains `manuscript.tex`, `README.md`, `AUDIT.md`, `audits/`, and `improvements/`, while the README names `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` as package members. They were not present in the root listing inspected in this run. This is a reproducibility/package issue, not a defect in the symbolic manuscript proof.

A new quantitative improvement follows from the manuscript as written: the final constant `10000` can be replaced, without changing any lemma or assumption, by

\[
\boxed{C_* = 2010+1200\log 16 = 5337.106466687737\ldots.}
\]

The proof of this sharpening is given below and in the companion improvement artifact.

## End-to-end audit ledger

The source-line ranges below refer to the pinned 790-line `manuscript.tex`. Every labeled statement and invocation in these ranges was checked against the hypotheses available at the call site.

### Lines 1–100 — theorem, quantifiers, normalization architecture — PASS

Checked `thm:main`, `cor:33`, the definitions of singular values/density norm, and the fixed parameters `eta=1/100`, `kappa=1/80^2`. The claimed normalized theorem is exactly the one needed after scaling. No bounded-support, smoothness, moment, log-concavity, diagonal-basis, or rotated-independence assumption is inserted.

### Lines 101–200 — Fourier identities, power envelope, Riesz half-potential, rank perturbation, Schur count start — PASS

With the convention `fhat(t)=int exp(itx)f(x)dx`, Plancherel carries the factor `2pi`, Fourier inversion carries `(2pi)^-1`, and Gaussian inversion has the stated normalization. The negative-half-moment calculation gives

\[
\mathbb E|Z-a|^{-1/2}\le (2\pi)^{-1/2}\int |t|^{-1/2}|\phi_Z(t)|dt.
\]

The `3/4` envelope is correctly used only after the `|t|^{-1/2}` weight. The singular-value perturbation statements are valid for nonsymmetric matrices.

### Lines 201–300 — Schur count completion, diagonal dominance, geometric BL, projection densities, scalar Fourier powers — PASS

The singular Schur-complement case is legitimately obtained by `A+epsilon I` and spectral continuity. Strict row diagonal dominance is applied to a possibly nonsymmetric matrix, for which the stated elementary proof is valid.

The heat-flow proof of geometric rank-one Brascamp–Lieb is correct: the frame identity makes the relevant column operator a contraction, giving

\[
\partial_tF-\Delta F=F\left(\sum c_i v_i^2-\left|\sum c_i u_i v_i\right|^2\right)\ge0.
\]

The large-time limit and monotone truncation passage to rough nonnegative `L1` inputs are valid.

For the product-projection lemma, after writing `b_i=1-|U^Te_i|^2`, factors with `b_i=0` may be dropped. The entropy inequality may then be summed over all indices by extending `-b log b` continuously at zero; equivalently the positive-`b_i` sum is at most the all-index sum. Thus `||p_{U^T X}||_infty<=e^{d/2}` is valid. I classify the sentence `sum_i(1-b_i)=d` as mathematically harmless under the all-index convention, though an explicit convention would improve clarity.

The B02 focal scalar Fourier-power lemma is correct. For `p>=2`, `m=floor(p/2)>=p/4` and `|fhat|<=1` give

\[
\int|\widehat f|^p\le\int|\widehat f|^{2m}.
\]

The latter is the characteristic function of the sum of `m` independent signed differences. Its density at zero is bounded by the one-dimensional projection theorem applied to `2m` original independent coordinates with coefficient norm `sqrt(2m)`, hence

\[
\int|\widehat f|^{2m}\le 2\pi\frac{\sqrt e}{\sqrt{2m}}
\le\frac{2\pi\sqrt{2e}}{\sqrt p}.
\]

Also `f*tilde f<=1` follows directly from `||f||_infty<=1` and mass one.

### Lines 301–400 — decoupling, regularized determinant, crossing volumes — PASS

The two-copy Cauchy–Schwarz step uses only independence of the original coordinate blocks. Jensen yields the fourth-power form with no conditional-density cap.

For `H=alpha I+a^2M^TM`, `alpha=(2pi e)^2`, `a=2t`, the weights

\[
c_j=\alpha e_j^TH^{-1}e_j,\qquad d_i=a^2m_i^TH^{-1}m_i
\]

form the stated geometric frame and satisfy `theta=sum d_i=sum(1-c_j)`. Applying the scalar Fourier-power lemma at exponent `2/d_i` gives

\[
||h_i||_{1/d_i}\le(2\pi\sqrt{e d_i})^{d_i}.
\]

The powers of `d_i` cancel, the `c_j` entropy factor is at most `e^{theta/2}`, and the remaining scalar multiplier is exactly one because `sqrt(alpha)=2pi e`. Taking fourth roots gives

\[
\boxed{|\phi_Z(t)|\le\det(I+t^2M^TM/(\pi^2e^2))^{-1/8}.}
\]

Cauchy–Binet gives the crossing-volume coefficients. Retaining order `k` yields Fourier exponent `k/4`. The manuscript correctly distinguishes `k=5` (absolute Fourier inversion, density bound) from `k=3` (weighted half-potential only).

### Lines 401–500 — scalar square, definite pair, hyperbolic pair, quarter-power concentration start — PASS

The scalar-square density profile is a conditional measure-domination statement, not an independence assertion. The definite two-coordinate bound is a deterministic change of variables after conditioning on original coordinates. The indefinite hyperbolic parameterization has Jacobian `1/(2sqrt(D))`; the tail estimate uses only one original marginal density at a time and total mass one, so it does not silently use independence after an orthogonal rotation.

### Lines 501–600 — quarter concentration, disjoint minors, sampling, completion, spectral-to-volume start — PASS

In the no-large-diagonal branch, a sign partition produces an original-coordinate cross block with operator norm at least `L/4`; one determinant factor then gives the `|t|^-1/4` envelope. Gaussian smoothing gives the manuscript coefficient

\[
2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8)<16,
\]

and layer cake yields `L0=4+4 log16`.

For volume sampling, the nonsymmetric interpolant

\[
P=A_{\cdot,T}A_{S,T}^{-1}A_{S,\cdot}
\]

has rank at most `r`, agrees with `A` on rows `S` and columns `T`, and the bordered determinant identity gives the squared residual. Singular seeds are omitted, so the aggregate multiplicity statement is correctly an inequality.

In `A=D+R+E`, `D` is diagonal and vanishes on the seed, `E` is zero-diagonal and supported in `LxL`, `R_{L,L}=P_{L,L}` has rank at most `r`, while globally `rank R<=3r` because `R-P` is supported in rows `T` or columns `S`. No symmetry of the auxiliary `R,E` is required by the later singular-value argument.

### Lines 601–700 — spectral-to-volume completion, random cut, no-pivot consequences, singular kernels, pivot half-potential start — PASS

If `V_k<kappa^k`, telescoping (or first vanishing volume) produces `V_{r+1}/V_r<kappa`. For `1<=r<=4`,

\[
||E||\le||E||_F\le(r+1)/80\le1/16.
\]

With `m=4k-3>=4r+1`, rank perturbation by global rank `3r` forces at least `r+1` diagonal entries of `D` of magnitude `>=1-epsilon`; they lie in `L`. On an `(r+1)`-subset `H`,

\[
|R_{ii}|\ge371/400,
\qquad
\sum_{j\ne i}|R_{ij}|<4(1/7+1/16)=23/28<371/400,
\]

so `R_{H,H}` is invertible, contradicting `rank R_{L,L}<=r`. The `r=0` case is separately correct.

A fair coordinate cut retains an ordered disjoint `k`-minor with probability `4^-k`; hence `E Z_k=4^-kV_k`. Combining with the determinant theorem gives the manuscript no-pivot `k=3` and `k=5` consequences.

The two singular-kernel integrals are correctly bounded. In particular the near part of `J(d)` is finite and the far part is logarithmic; the log-kernel estimate follows by interval-superlevel overlap and Tonelli.

### Lines 701–790 — pivot half potentials, nine-eigenvalue result, main theorem, threshold accounting — PASS

For a scalar pivot `|a_ii|>=eta`, Schur complementation leaves at least one unit spectral direction in Proposition `pivot-H`; the quarter-power lemma removes atoms and controls the logarithm. Definite and indefinite pair branches retain the required original-coordinate conditioning and have the stated uniform bounds.

For `s_9(A)>=1`, pivot and no-pivot branches together give a full half-potential bound after adding at most one from the tail `|Q-a|>1`. In the 17-eigenvalue theorem, a scalar pivot removes one spectral direction and leaves at least 16, more than enough for the nine-direction half-potential receiver; a two-coordinate pivot removes at most two and the pair arguments need only the stated residual spectral information. The final `K,s` rescaling is correct:

\[
Y=KX,\quad \widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c,
\quad Q=(s/K^2)\widetilde Q.
\]

Thus density scales by `K^2/s`.

## New proved constant sharpening

The manuscript keeps several intentionally loose round constants. One can close the same proof with a substantially smaller final constant without changing any hypothesis.

Let

\[
L_0=4+4\log16.
\]

In the scalar-pivot branch of Proposition `pivot-H`, the exact displayed manuscript inequalities give

\[
H(Q)\le 10(8+3L_0)
=200+120\log16.
\]

This dominates the manuscript's other pivot-H branches (`4pi eta^-1/2` in the definite case, and the displayed hyperbolic bound in the indefinite case). The no-pivot nine-direction branch has full half potential `<200`. Therefore Proposition `nine` may be strengthened from `601` to

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le 201+120\log16.
\]

The outer scalar pivot in the main theorem contributes the factor `eta^-1/2=10`, so

\[
\|p_Q\|_\infty
\le 10(201+120\log16)
=2010+1200\log16.
\]

The competing normalized branches are smaller:

\[
800e < 2010+1200\log16,
\qquad
10\pi < 2010+1200\log16,
\]

and for the main indefinite pair the manuscript gives

\[
10(10+5\log16)+1/e < 2010+1200\log16.
\]

Hence the entire theorem, with the same proof and full quantifiers, strengthens to

\[
\boxed{
\|p_{X^TAX+b^TX+c}\|_\infty
\le (2010+1200\log16)\frac{K^2}{s}
<5338\frac{K^2}{s}
}
\]

whenever `s_17(A)>=s>0`.

This is a proved constant improvement, **not** a multiplicity reduction.

## Multiplicity-reduction attempt: why this run does not certify 13

The audited interpolation proposition works equally at `k=4`: in the no-pivot branch, `s_13(A)>=1` forces a positive order-four crossing volume at a fixed quantitative scale. But the determinant receiver then yields only

\[
|\phi(t)|\le\min(1,u_4/|t|),
\]

whose absolute integral diverges logarithmically. Therefore the present `L1` Fourier inversion argument cannot convert the order-four volume into an `L^infty` density bound.

I also checked the natural attempt to change the Jensen/copy power. The fresh fleet01/B03 artifact proves the general leverage-free family

\[
|\phi_Z(t)|\le
\det\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/(4q)},\qquad q\ge2,
\]

so order `k` decays at best as `|t|^{-k/(2q)}`. Since `q>=2` is forced by the available uniform scalar Fourier input, `q=2` is already optimal in that mechanism and `k=4` remains exactly the `|t|^-1` endpoint. For `q<2`, uniform scalar `L^p` Fourier control fails for cap-one densities. I independently checked the algebraic exponent in that artifact against the manuscript's scalar-power/BL calculation; it is consistent.

Thus **no 17 -> 13 theorem is certified in this run**. The next proof obligation is a genuinely new order-four endpoint argument: a dimension-free small-ball/density estimate that can exploit cancellation or extra product structure without requiring `int|phi|<infinity` from the crude endpoint envelope.

## Package/review status

- 17-eigenvalue mathematical baseline: **PASS in this audit**.
- Fatal mathematical defect: **none found**.
- New quantitative theorem: **constant improved to `2010+1200 log16 < 5338`**.
- Multiplicity reduction: **none proved**; 17 remains the lowest threshold certified by this run.
- Full three-eigenvalue conjecture: **OPEN**.
- Global continuity: **OPEN/not claimed**; no-pivot Fourier branch is continuous.
- Repository package: **GAP** because `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` were absent from the root listing despite README references.
- Independent-validation label: **not self-awarded**; release synthesis must count genuinely separate complete reviews.

## Exact next obligation

Prove an order-four endpoint receiver under the same rough product-law hypotheses. Concretely, if an original-coordinate cross block `M` has `Z_4(M)>=zeta>0`, prove a dimension-free bound on the density (or `P(Z in I)<=C(zeta)|I|`) while retaining arbitrary measurable same-bank phases and affine terms. Such a theorem would splice directly into the audited structural proposition and lower the fixed multiplicity threshold from 17 to 13.
