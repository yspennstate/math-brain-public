# fleet02/B20 release-gate audit and leverage endpoint

Run: `20260924T120035Z-fleet02-B20-fixedmult-audit-r1`
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`
Audited manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
Initial pinned manuscript commit recorded by the package: `7c0d6e60946b19423e6400a12d34b473cf0591e2`
Fresh master snapshot used for the line-by-line read: `e063884fe2bb91b35ffb092199f02db7d1bbd5a5`

## Release-gate verdict

**PASS for the mathematical 17-eigenvalue theorem in this independent audit, with one local wording repair; NOT independently validated by this report alone.** I read the complete 790-line `manuscript.tex` and reconstructed the proof chain rather than importing prior PASS verdicts. I found no fatal mathematical defect in the theorem

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s
\]

for independent arbitrary real coordinate laws with densities bounded by `K`.

The unrestricted three-eigenvalue conjecture is not proved here.

## Complete audit ledger

- **Lines 1--74: PASS.** Quantifiers, singular-value convention, affine terms, and normalization target are consistent. No moments, support, log-concavity, or rotated-coordinate independence are added.
- **Lines 75--176: PASS.** Fourier convention, Gaussian inversion, Plancherel normalization, the power envelope, and the Riesz half-potential constant are consistent. In particular the order-three exponent `3/4` is used only after the `|t|^{-1/2}` weight.
- **Lines 177--226: PASS.** Nonsymmetric singular-value perturbation is valid. The principal-pivot Schur count `N_S(t)>=N_A(t)-k` follows through the complementary compression of `A^{-1}` and the singular perturbation limit.
- **Lines 227--302: PASS.** The heat-flow Brascamp--Lieb proof has the correct monotonicity sign, Gaussian limit, and monotone-approximation passage.
- **Lines 303--335: GAP, local wording only.** In the projection lemma, after rows with `b_i=0` are omitted, the line identifying `sum_{b_i>0}(1-b_i)` with `d` is not literally correct. The needed statement is
  \[
  \sum_{b_i>0}(1-b_i)\le \sum_i(1-b_i)=d.
  \]
  This repairs the sentence and leaves `||p_{U^TX}||_infty<=e^{d/2}` and every downstream constant unchanged.
- **Lines 336--449: PASS.** Integrated scalar Fourier powers, two-copy decoupling, the regularized graph frame, all powers of `c_j,d_i`, and `alpha=(2pi e)^2` give exactly
  \[
  |\phi_Z(t)|\le\det\!\left(I+\frac{t^2}{\pi^2e^2}M^TM\right)^{-1/8}.
  \]
  No post-rotation independence is used.
- **Lines 450--477: PASS.** Cauchy--Binet gives `Z_k`, and the order-five and order-three consequences have the stated constants.
- **Lines 478--546: PASS.** Scalar-square and definite-pair changes of variables are valid as measure domination statements. The indefinite hyperbolic parameterization has Jacobian `1/(2 sqrt(D))`; the tail estimate uses only original-coordinate density caps and total mass.
- **Lines 547--597: PASS.** The quarter-power small-ball estimate correctly splits the diagonal and off-diagonal cases. The sign partition produces a physical cross block with norm at least `||S||/4`; Gaussian smoothing yields the claimed `rho^{1/4}` bound and logarithmic potential.
- **Lines 598--647: PASS.** For a disjoint seed, the bordered determinant identity and volume sampling are correct. Singular seeds are properly omitted, hence the aggregate comparison is an inequality. The nonsymmetric interpolant has `rank P<=r`; in the completion, `D` vanishes on the seed, `rank R<=3r`, and the sharper restriction `rank R[L,L]<=r` is correct.
- **Lines 648--684: PASS.** The no-pivot spectral-to-volume contradiction is valid. With `m=4k-3`, rank perturbation leaves at least `r+1` large entries of `D` in `L`; the explicit diagonal-dominance gap is positive for `r<=4`, contradicting the restricted rank bound. The `r=0` case is separately valid.
- **Lines 685--711: PASS.** Random cuts retain each ordered disjoint minor with probability `4^{-k}`. The `k=3` full half-potential and `k=5` density constants follow.
- **Lines 712--759: PASS.** Truncated half-potential kernels, scalar/definite/indefinite pivot branches, and the nine-eigenvalue full half-potential estimate are consistent. Exceptional slices are avoided by test-function/Tonelli formulations.
- **Lines 760--790: PASS.** Under `s_17>=1`, no-pivot, scalar-pivot, definite-pair, and indefinite-pair branches close below `10^4`. The scaling `Y=KX`, `Q=(s/K^2)\widetilde Q` correctly yields `10^4K^2/s`. The manuscript appropriately claims only an essentially bounded density globally.

## Exact obstruction to a naive rank improvement

For `r=1`, take `S={1}`, `T={2}` and
\[
A=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}.
\]
Then `B=A_{1,2}=1`. With `L={3}`, the manuscript construction has `E=0`, `D_{33}=-1`, and
\[
R=\begin{pmatrix}0&1&1\\1&0&1\\1&1&1\end{pmatrix},
\qquad \det R=1.
\]
Thus the actual nonsymmetric-interpolation completion can attain global rank `3=3r`; simply replacing the global `3r` by `2r` is false for this construction. Scaling preserves this rank fact. A lower multiplicity therefore needs a genuinely different analytic or structural step.

## New result: leverage-interpolated crossing determinant

The direct order-four route in the baseline stalls because the fourth-moment determinant estimate gives the borderline decay `|t|^{-1}`. There is, however, a strictly stronger estimate whenever one physical side of the crossing is not dominated by a nearly-coloop row.

For the cross form
\[
Z=F(X_I)+2X_I^TMX_J+G(X_J),
\]
let `m_i` be row `i` of `M` and define its ordinary row leverage
\[
\ell_i=m_i^T(M^TM)^\dagger m_i\in[0,1].
\]

**Lemma (q-leverage determinant).** Let `1<=q<2`. If `max_i ell_i <= q/2`, then
\[
\boxed{
|\phi_Z(t)|\le
\det\!\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/(4q)}.}
\]
The same conclusion with row leverage replaced by column leverage follows after swapping `I,J`.

**Proof.** From the manuscript's unsquared decoupling inequality,
\[
|\phi_Z(t)|^2\le \mathbb E_D\prod_i|\widehat f_i(2t(MD)_i)|.
\]
Raise to the power `q` and use Jensen:
\[
|\phi_Z(t)|^{2q}\le \mathbb E_D\prod_i|\widehat f_i(2t(MD)_i)|^q.
\]
Set `a=2t`,
\[
\alpha=(2\pi e)^2\frac{2}{q},\qquad H=\alpha I+a^2M^TM,
\]
and use the same graph frame as the manuscript,
\[
c_j=\alpha e_j^TH^{-1}e_j,\qquad d_i=a^2m_i^TH^{-1}m_i.
\]
If `M=U Sigma V^T`, then
\[
d_i=\sum_{r}\frac{a^2\sigma_r^2}{\alpha+a^2\sigma_r^2}U_{ir}^2
\le\sum_rU_{ir}^2=\ell_i\le q/2.
\]
Thus `q/d_i>=2`, so the manuscript's scalar Fourier-power bound applies at exponent `q/d_i`:
\[
\left\||\widehat f_i|^q\right\|_{1/d_i}
\le\bigl(2\pi\sqrt{2e d_i/q}\bigr)^{d_i}.
\]
The `d_i^{-d_i/2}` graph factors cancel the powers of `d_i`; the `c_j` entropy contribution is at most `e^{theta/2}`. The choice of `alpha` makes the remaining scalar factor exactly one. Consequently
\[
|\phi_Z(t)|^{2q}\le
\det\!\left(I+\frac{q t^2}{2\pi^2e^2}M^TM\right)^{-1/2},
\]
which proves the claim.

Retaining the order-`k` determinant term gives
\[
|\phi_Z(t)|\le
\min\left\{1,
\left(\frac{\pi e\sqrt{2/q}\,Z_k(M)^{-1/(2k)}}{|t|}\right)^{k/(2q)}
\right\}.
\]
For `k=4`, this is integrable for every `q<2`, and Fourier inversion yields
\[
\boxed{
\|p_Z\|_\infty\le
\frac{2e\sqrt{2/q}}{2-q}\,Z_4(M)^{-1/8}.}
\]

## A rigorous 13-eigenvalue diffuse-leverage branch

Assume the normalized hypotheses `K=s=1` and `s_13(A)>=1`. Pivot branches already close with the manuscript's arguments: a scalar pivot leaves at least twelve large Schur directions, hence the nine-direction half-potential estimate; definite pairs are direct; indefinite pairs leave at least eleven directions and need only one surviving direction.

In the no-pivot branch, Proposition 6.3 with `k=4` and the random-cut lemma give a physical cut with
\[
Z_4(M)\ge4^{-4}\kappa^4,
\qquad Z_4(M)^{-1/8}\le160.
\]
If for at least one such volume-good cut either the row or column leverage maximum is at most `3/4`, take `q=3/2`. The new determinant estimate becomes
\[
|\phi_Z(t)|\le
\det\!\left(I+\frac{3t^2}{4\pi^2e^2}M^TM\right)^{-1/6},
\]
and the order-four term has decay exponent `4/3>1`. Hence
\[
\boxed{
\|p_Q\|_\infty\le \frac{8e}{\sqrt3}Z_4(M)^{-1/8}
\le\frac{1280e}{\sqrt3}<2009.}
\]
The pivot branches are bounded by `6010`, so under this explicit diffuse-leverage condition the full thirteen-eigenvalue theorem holds with
\[
\boxed{\|p_Q\|_\infty\le6010K^2/s.}
\]
No moment, support, log-concavity, diagonal-basis, or post-rotation-independence assumption has been introduced.

## First unpaid implication after this run

For a universal `17 -> 13` improvement using this architecture, the first unpaid structural/analytic step is now sharply localized:

> In the no-pivot `s_13(A)>=1` regime, after choosing a physical cut with `Z_4(A[I,J])>=4^{-4}\kappa^4`, either produce a volume-good cut for which one orientation has maximum leverage bounded away from `1` by a universal constant, or pay the complementary **two-sided near-coloop / heavy-leverage** case by a different original-coordinate receiver.

The new lemma pays every fixed leverage gap `lambda<1`: taking `q=max(1,2lambda)` gives a finite explicit constant. Thus only leverage tending to one is genuinely outside this endpoint mechanism.

## Package/reproducibility gap

At the fresh master snapshot used here, `README.md`, `AUDIT.md`, and `manuscript.tex` were present, but direct retrieval of `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` at the manuscript root returned not found, despite the README describing them as canonical package members. This is release-relevant but not a mathematical defect in the symbolic proof. Do not claim the repository currently contains those four artifacts unless a later source refresh restores them.

## Status

- Mathematical multiplicity-17 baseline: **PASS in this independent audit, after the local projection-line repair above**.
- Fatal mathematical defect found: **none**.
- New unconditional multiplicity threshold proved here: **none**.
- New conditional multiplicity-13 branch: **proved**, with exact leverage hypothesis and constants.
- Universal 13 threshold: **OPEN**, reduced to the two-sided heavy-leverage endpoint above within this mechanism.
- Full three-eigenvalue conjecture: **OPEN**.
- Independent validation: this audit is one complete review; the owner requirement still calls for a genuinely separate second complete review before validation status.
