# fleet01/B18 — QFORM literature-to-proof transfer r30

SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T10:51:50Z.
attacking: literature-to-proof transfer for the surviving near-coloop / nonplanar 1+2 aggregate; sharpen the completed fleet02/B18 diffuse-MSS payment and extend its leverage range using the pinned D' theorem, while recording a primary-source projection consequence that does not cross the false arbitrary-joint coarea interface.

## Status

**PROVED SUPPORTING TARGET-LEVEL SHARPENING / FULL QFORM OPEN.**

Claim label: `QFORM-MSS-BALANCED-HUB-DETERMINANT-v1`.

This report does not claim the full conjecture. It proves a stronger whole-line density bound, with continuity, in the exact-rank-three Schur-isotropic diffuse branch treated by the completed designated partner fleet02/B18 r26. It also extends the admissible residual row-leverage range from `delta<=1/18` to the exact interval

\[
0<\delta<\delta_*:=\frac{39-6\sqrt{30}}{98}=0.0626188423437758\ldots .
\]

The remaining large-shear growth is still of order `r^(1/3)`, so the first unpaid global implication remains the nonplanar product-preserving asymmetric `1+2` mechanism.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Sources and correction boundary

### 1.1 Completed designated partner actually applied

Fleet02/B18 r26:

- repository/commit: `yspennstate/math-open-problems@b0fe7c60d4fb400917fb53d2435d5262fdcfea97`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/20260923T081256Z-fleet02-B18-QFORM-r26/REPORT.md`;
- claim: `QFORM-SHEAR-CROSSVOLUME-MSS-BARRIER-v1`.

Its canonical Schur-isotropic setup is

\[
Q=(Y+r nX_0)^TD(Y+r nX_0),\qquad Y=V^TX_R,
\]
where `D=D^T` is nonsingular `3 x 3`, `V^TV=I_3`, `||n||=1`, `n^TDn=0`, and the rows `v_j` of `V` form a residual Parseval frame. With the physical coefficient matrix `U` having rows

\[
u_0=rn,\qquad u_j=v_j,\]
we have

\[
U^TU=I_3+r^2nn^T,
\qquad
|\det_{\ne0} A|=|\det D|(1+r^2).
\]
If the three nonzero eigenvalues of `A=UDU^T` have modulus at least `s`, then

\[
\boxed{|\det D|(1+r^2)\ge s^3.}\tag{1.1}
\]

The partner also proves, for any disjoint physical cut `I,J`, the exact cross-volume identity

\[
Z=e_3(A_{IJ}^TA_{IJ})
=|\det D|^2\det G_I\det G_J,
\qquad G_I=U_I^TU_I,\quad G_J=U_J^TU_J.\tag{1.2}
\]

### 1.2 Primary source: Marcus–Spielman–Srivastava

A. Marcus, D. Spielman, N. Srivastava, *Interlacing Families II: Mixed characteristic polynomials and the Kadison–Singer problem*, Ann. of Math. 182 (2015), Corollary 1.5, DOI `10.4007/annals.2015.182.1.8`.

Exact hypothesis/result used: if

\[
\sum_j v_jv_j^T=I,\qquad \|v_j\|^2\le\delta,
\]
then for `q=2` there exists a partition `R=S\dot\cup T` such that both partial Gram operators obey

\[
G_S,G_T\le a_\delta I,
\qquad
a_\delta:=\left(\frac1{\sqrt2}+\sqrt\delta\right)^2
=\frac12+\sqrt{2\delta}+\delta.\tag{1.3}
\]

This is exactly the residual Parseval-frame hypothesis here; no probabilistic assumption on the input laws is involved in this deterministic partition step.

Put

\[
c_\delta:=1-a_\delta=\frac12-\sqrt{2\delta}-\delta.\tag{1.4}
\]
Since `G_S+G_T=I`, (1.3) also gives

\[
c_\delta I\le G_S,G_T\le a_\delta I.\tag{1.5}
\]

### 1.3 Pinned quadratic-form density theorem D and extension D'

Pinned source:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`;
- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, Theorem D;
- companion `FOURIER_ROUTE_REPORT.md`, Section 1.1, extension D'.

For a disjoint cut `I,J`, let `Z=e_3(A_{IJ}^TA_{IJ})` and let the row volume-sampling marginals be `alpha_i`. Theorem D gives

\[
\|p_Q\|_\infty\le6\sqrt e\,Z^{-1/6}\tag{1.6}
\]
when `max alpha_i<=1/2`. Extension D' gives, for any `1/2<=h<3/4` with `max alpha_i<=h`,

\[
\|p_Q\|_\infty
\le6\sqrt e\,(2h)^{-1/2}(3-4h)^{-1}Z^{-1/6}.\tag{1.7}
\]

Both bounds arise from an integrable characteristic-function majorant, so they also provide a continuous density; continuity is recorded separately below.

### 1.4 Primary source: Livshyts–Paouris–Pivovarov

G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949; Israel J. Math. 216 (2016), Theorem 1.1.

For a product probability density with one-dimensional factors bounded by one, every `k`-dimensional orthogonal marginal has density cap at most `2^(k/2)`. No moment, centering, iid, support, log-concavity or smoothness hypothesis is added.

A useful exact corollary, by polar decomposition, is: for any full-row-rank `k x m` matrix `L`,

\[
\boxed{\|p_{LX}\|_\infty\le
\frac{2^{k/2}}{\sqrt{\det(LL^T)}}.}\tag{1.8}
\]
Indeed `B=(LL^T)^(-1/2)L` has orthonormal rows, so LPP applies to `BX`; the final invertible `k x k` linear map contributes the Jacobian factor `det(LL^T)^(-1/2)`.

Applied to the partner's spectral variable

\[
Z_0=Y+r nX_0,
\]
whose original-coordinate coefficient matrix has Gram `I+r^2nn^T`, (1.8) gives the concrete source-valid estimate

\[
\boxed{\|p_{Z_0}\|_\infty\le\frac{2\sqrt2}{\sqrt{1+r^2}}.}\tag{1.9}
\]

This is **not** converted into a quadratic-output bound by arbitrary-joint coarea: that interface is explicitly refuted in the live correction ledger. Equation (1.9) is recorded because it shows that the spectral projection itself becomes flatter as shear grows; the unresolved difficulty is the curved quadratic trace together with product provenance.

### 1.5 Corrections preserved

No step below uses independence after spectral rotation, arbitrary-joint rank-three coarea, positive conditional projection-density moments, conditional cap as a substitute for independence, pointwise law-uniform quadratic-phase decay, deletion of small coefficients, or a fixed-good-minor claim.

## 2. New determinant sharpening of the partner's MSS cut

Let

\[
\delta:=\max_j\|v_j\|^2.
\]
Use the MSS partition `R=S\dot\cup T` from (1.3). Because the two pieces are exchangeable, relabel them so that

\[
n^TG_Tn\le\frac12.\tag{2.1}
\]
This is always possible since

\[
n^TG_Sn+n^TG_Tn=n^TIn=1.
\]

Take the partner's physical cut

\[
I=S,\qquad J=\{0\}\cup T.
\]
Then

\[
G_J=G_T+r^2nn^T.\tag{2.2}
\]

### 2.1 Exact product of the two residual determinants

Since `G_T=I-G_S`, the two matrices commute. If `lambda_1,lambda_2,lambda_3` are the eigenvalues of `G_S`, then by (1.5)

\[
c_\delta\le\lambda_k\le a_\delta=1-c_\delta,
\]
and hence

\[
\lambda_k(1-\lambda_k)\ge c_\delta a_\delta.
\]
Therefore

\[
\boxed{\det G_S\det G_T
\ge(c_\delta a_\delta)^3.}\tag{2.3}
\]

This replaces the partner's coarser lower bound `c_delta^6`.

### 2.2 Orienting the partition toward the null hub

The matrix Cauchy–Schwarz inequality gives, for every positive definite `G_T`,

\[
(n^TG_Tn)(n^TG_T^{-1}n)\ge(n^Tn)^2=1.
\]
Together with (2.1),

\[
n^TG_T^{-1}n\ge2.\tag{2.4}
\]

The determinant lemma applied to (2.2) yields

\[
\det G_J
=\det G_T\bigl(1+r^2n^TG_T^{-1}n\bigr)
\ge\det G_T(1+2r^2).\tag{2.5}
\]

Combining (1.2), (2.3) and (2.5),

\[
\boxed{
Z\ge |\det D|^2(c_\delta a_\delta)^3(1+2r^2).
}\tag{2.6}
\]

This is the main new deterministic inequality.

## 3. Extended leverage range via D'

For the exact-rank-three factorization, the partner computed the row volume-sampling marginal

\[
\alpha_i=v_i^TG_S^{-1}v_i.
\]
By `G_S>=c_delta I`,

\[
\alpha_i\le \frac{\delta}{c_\delta}=:h_\delta.\tag{3.1}
\]

The original Theorem D applies when `h_delta<=1/2`, which is exactly `delta<=1/18`. But D' only needs `h_delta<3/4`. Solving

\[
\frac{\delta}{\frac12-\sqrt{2\delta}-\delta}<\frac34
\]
gives

\[
7\delta+3\sqrt{2\delta}<\frac32,
\]
and hence the exact endpoint

\[
\boxed{
\delta<\delta_*:=\frac{39-6\sqrt{30}}{98}
=0.0626188423437758\ldots .
}\tag{3.2}
\]

Thus the diffuse MSS branch is source-valid on a strictly larger leverage interval than in the completed partner report.

Define

\[
F_\delta:=
\begin{cases}
1,& h_\delta\le1/2,\\[1mm]
(2h_\delta)^{-1/2}(3-4h_\delta)^{-1},&1/2<h_\delta<3/4.
\end{cases}\tag{3.3}
\]

Substituting (2.6) into D/D' gives

\[
\|p_Q\|_\infty
\le6\sqrt e\,F_\delta
|\det D|^{-1/3}(c_\delta a_\delta)^{-1/2}(1+2r^2)^{-1/6}.\tag{3.4}
\]

Finally use the partner's spectral ledger (1.1):

\[
|\det D|^{-1/3}\le s^{-1}(1+r^2)^{1/3}.
\]
Therefore

\[
\boxed{
\|p_Q\|_\infty
\le
6\sqrt e\,F_\delta\,(c_\delta a_\delta)^{-1/2}s^{-1}
\left(\frac{(1+r^2)^2}{1+2r^2}\right)^{1/6},
\qquad \delta<\delta_*.
}\tag{3.5}
\]

This is a whole-line density estimate for every independent cap-one original-coordinate law satisfying the stated partner branch; no moment or support restriction is introduced.

## 4. Clean `delta=1/18` specialization and comparison

At `delta=1/18`,

\[
a_\delta=\frac89,\qquad c_\delta=\frac19,
\qquad h_\delta=\frac12,
\qquad c_\delta a_\delta=\frac8{81}.
\]
Then (3.5) becomes

\[
\boxed{
\|p_Q\|_\infty
\le
27\sqrt{\frac e2}\,s^{-1}
\left(\frac{(1+r^2)^2}{1+2r^2}\right)^{1/6}.
}\tag{4.1}
\]

The completed partner r26 bound at the same leverage threshold was

\[
54\sqrt e\,s^{-1}(1+r^2)^{1/6}.\tag{4.2}
\]

The ratio of the new certificate to (4.2) is exactly

\[
\frac1{2\sqrt2}
\left(\frac{1+r^2}{1+2r^2}\right)^{1/6}
\le\frac1{2\sqrt2}=0.353553\ldots .\tag{4.3}
\]

Thus the numerical certificate is reduced by at least `64.64%` throughout this branch, and by more as `r` grows. The improvement comes from two exact facts not spent in r26: `G_T=I-G_S` forces the determinant product (2.3), and the partition can be oriented so that the hub-side residual Gram has at most half of the `n`-energy, giving (2.4).

The large-shear behavior is nevertheless still

\[
O(s^{-1}r^{1/3}),
\]
so this does not solve the remaining shear-uniform endpoint.

## 5. Continuity, tracked separately

Unlike a purely small-ball or essential-density payment, D/D' produces an explicit characteristic-function decay exponent strictly greater than one:

- for `h_delta<=1/2`, `|phi(t)|=O(|t|^{-3/2})`;
- for `1/2<h_delta<3/4`, the D' proof gives exponent `3/(4h_delta)>1`.

Hence `phi in L^1(R)`. Fourier inversion therefore gives a continuous `C_0` density. Consequently (3.5), and in particular (4.1), holds for that continuous representative pointwise, not merely essentially.

This continuity conclusion is confined to the branch proved here; the full conjecture's continuity statement remains open.

## 6. Literature check for an exact prior full-target theorem

A targeted check included:

- Livshyts–Paouris–Pivovarov: exact product-marginal density control, used in (1.8)–(1.9), but no theorem there controls the indefinite quadratic trace of the resulting dependent projection.
- Hanson–Wright / its refinements: require subgaussian or Bernstein-moment assumptions, absent from the owner target.
- Egor Kosov, *Oscillatory integrals with polynomial phase and regularity of distributions* (arXiv:2511.02679, 2025): gives dimension-free regularity estimates for polynomial images of product measures under additional regularity hypotheses used in the product-measure part (not arbitrary fragmented cap-one densities), and does not supply the universal `L^infinity` quadratic-output conclusion needed here.

No exact prior source matching all owner quantifiers was found in this targeted check. This search miss is **not** treated as evidence of novelty.

## 7. Remaining implication

The partner r26 obstruction remains real: in a normalized exact-spectrum family, any single pinned three-volume cut necessarily loses a positive power of shear. The new determinant accounting improves the coefficient substantially and extends the leverage range, but it cannot change the `r^(1/3)` exponent.

The first unpaid structural implication remains

`QFORM-NONPLANAR-ONEPLUS2-AGGREGATE-v1`:

> Before conditioning destroys product provenance, construct an asymmetric original-coordinate `1+2` aggregate that spends the residual Pluecker identity
> \[
> \sum_{i<j}\det(n,v_i,v_j)^2=1
> \]
> at the coefficient scale `r^2|det D|`, or route failure into an already-paid physical-pair/ridge/finite-bank branch.

Equation (1.9) adds a useful diagnostic: the full three-dimensional spectral variable already has density cap `O(1/r)` in large shear, so the missing issue is not concentration of the linear projection itself; it is the dependence-safe curved trace.

Full-target status: `OPEN -> OPEN`.
Independent end-to-end review: not performed in this run.
