SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T23:46:00Z.
attacking: the genuinely non-aligned minority-sign/two-sheet branch of the three diffuse uniform-bank witness family; rule out an off-tip finite-bank spike uniformly over every spectral rotation.

# QFORM-THREEBANK-ALLROT-DIFFUSE-NOSPIKE-v1

Status: **new supporting theorem; unrestricted QFORM OPEN / NOT PROVED / NOT DISPROVED**.  Full-target continuity remains separate.  Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact finite target family

Let `m=(m1,m2,m3)` with each `mj>=2`.  Take independent physical variables
\[
 U_{jk}\sim \mathrm{Unif}[-1/2,1/2],\qquad
 Y_j=m_j^{-1/2}\sum_{k=1}^{m_j}U_{jk}.
\]
Every physical input density is exactly one.  Let `R_m` be the `(m1+m2+m3) x 3` synthesis matrix whose rows in bank `j` are `e_j/sqrt(m_j)`.  Thus
\[
R_m^TR_m=I_3.
\]
For arbitrary `O in O(3)` put
\[
J=\operatorname{diag}(1,1,-1),\qquad B_O=O^TJO,\qquad A_{m,O}=R_mB_OR_m^T.
\]
Then `A_{m,O}(R_mv)=R_mB_Ov`, so every finite physical matrix has exact nonzero spectrum
\[
\boxed{\operatorname{spec}_{\ne0}(A_{m,O})=\{1,1,-1\}.}
\]
The physical quadratic form is exactly
\[
Q_{m,O}=Y^TB_OY.
\]
No independence after spectral rotation is asserted or used.

## 2. Pinned Fresnel--Brascamp--Lieb estimate applied to the actual form

The required pinned source is
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md` and `FOURIER_ROUTE_REPORT.md`.
Its completed Theorem F applies directly to `A_{m,O}`.

Indeed, with spectral frame
\[
V=R_mO^T,
\]
we have `V^TV=I_3`.  A physical row in bank `j` has squared leverage exactly `1/m_j<=1/2`, independently of `O`.  Taking the theorem's coordinate set `I` to be all physical coordinates gives `G_I=I_3`, residual quadratic block zero (hence diagonal), and `|lambda_1lambda_2lambda_3|=1`.  Therefore the actual characteristic function satisfies for every real `t`
\[
\boxed{
|\Phi_{m,O}(t)|\le g(t):=
\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.
}
\tag{2.1}
\]
This is a real obstruction inequality, not a citation-only use of the source.  The majorant is integrable and
\[
\int_{\mathbb R}g(t)\,dt=24\pi.
\tag{2.2}
\]
Consequently every finite form in this family has a bounded continuous density.  The generic density ceiling `12` from Theorem F is not sharp enough to decide `3sqrt(2)`; the point of (2.1) here is compactness strong enough to exclude a hidden narrowing spike.

## 3. Uniform CLT over every rotation and every bank allocation

Let
\[
M(m)=\min(m_1,m_2,m_3),
\]
and let `G~N(0,I_3/12)`.  I claim
\[
\boxed{
\lim_{M\to\infty}
\sup_{\substack{m_j\ge M\\ O\in O(3)}}
\|p_{Q_{m,O}}-p_{G^TJG}\|_\infty=0.
}
\tag{3.1}
\]

Proof.  It is enough to prove uniform `L^1` convergence of characteristic functions.  If this failed, there would be `epsilon>0`, a sequence `m^(r)` with `M(m^(r))->infinity`, and `O_r in O(3)` for which
\[
\|\Phi_{m^{(r)},O_r}-\Phi_G\|_1\ge\epsilon.
\]
Pass to a subsequence with `O_r->O`, using compactness of `O(3)`.  Each one-dimensional normalized bank satisfies the ordinary CLT, and the three banks are independent, hence
\[
Y_{m^{(r)}}\Rightarrow G.
\]
Since `B_{O_r}->B_O`, the continuous mapping theorem gives
\[
Y_{m^{(r)}}^TB_{O_r}Y_{m^{(r)}}\Rightarrow G^TB_OG.
\]
Isotropy of `G` makes `G^TB_OG` equal in law to `G^TJG`; therefore for every fixed `t`,
\[
\Phi_{m^{(r)},O_r}(t)\to\Phi_G(t).
\]
By (2.1), `|Phi_{m^(r),O_r}|<=g`; taking the pointwise limit also gives `|Phi_G|<=g`.  Hence
`|Phi_{m^(r),O_r}-Phi_G|<=2g`, and dominated convergence contradicts the displayed `L^1` gap.  Thus
\[
\sup_{m_j\ge M,O}\|\Phi_{m,O}-\Phi_G\|_1\to0.
\]
Fourier inversion now yields (3.1), since
\[
\|p_{Q_{m,O}}-p_G\|_\infty
\le(2\pi)^{-1}\|\Phi_{m,O}-\Phi_G\|_1.
\]
This proves the claim.  Notice that weak convergence alone would not rule out an off-tip spike; the pinned Fresnel majorant is precisely what upgrades it to uniform convergence of the whole output density.

## 4. Exact Gaussian endpoint, including the minority-sign side

In the spectral basis write
\[
G^TJG=G_1^2+G_2^2-G_3^2,\qquad G_i\sim N(0,1/12).
\]
For `s>=0`, direct convolution gives
\[
\boxed{p_G(s)=3\sqrt2\,e^{-6s}.}
\tag{4.1}
\]
For `r>=0`, the negative/two-sheet side is
\[
\boxed{
p_G(-r)=3\sqrt2\,e^{6r}\operatorname{erfc}(\sqrt{12r}).
}
\tag{4.2}
\]
If `x=sqrt(12r)`, then `erfc(x)<e^{-x^2}` for `x>0` (the difference `e^{-x^2}-erfc(x)` starts at zero, has one positive maximum, and returns to zero).  Thus (4.2) is strictly below `3sqrt(2)` for every `r>0`.  Hence
\[
\boxed{\|p_G\|_\infty=p_G(0)=3\sqrt2.}
\tag{4.3}
\]
Combining (3.1) and (4.3),
\[
\boxed{
\lim_{M\to\infty}
\sup_{\substack{m_j\ge M\\O\in O(3)}}
\big|\|p_{Q_{m,O}}\|_\infty-3\sqrt2\big|=0.
}
\tag{4.4}
\]
Equivalently: for every `eta>0` there is `M_eta` such that every exact finite target witness in this family with all three banks at least `M_eta` satisfies
\[
\|p_{Q_{m,O}}\|_\infty\le3\sqrt2+\eta
\]
**uniformly over the spectral rotation**, including genuinely non-aligned negative eigenvectors and every output level.

An explicit fully coupled example is the Householder core
\[
B_*=I-\frac23\mathbf1\mathbf1^T,
\]
whose negative eigenvector is `(1,1,1)/sqrt(3)` and whose entries are all nontrivial.  Taking any three bank sizes tending to infinity gives exact finite spectrum `{1,1,-1}` and, by (4.4), global density norm tending to `3sqrt(2)` despite the non-aligned two-sheet geometry.

## 5. Latest account03/B17 result applied at the boundary

The latest compatible completed designated-partner theorem is
`math-open-problems@05d7f088563f665ac7ae3795be5be61728181844`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T230133Z-account03-B17-QFORM-auto11/REPORT.md`.
For
\[
B_0=\begin{pmatrix}
1/2&-1/2&-1/\sqrt2\\
-1/2&1/2&-1/\sqrt2\\
-1/\sqrt2&-1/\sqrt2&0
\end{pmatrix},
\qquad \operatorname{spec}(B_0)=\{1,1,-1\},
\]
it proves, for arbitrary joint heavy density `rho<=1` and an independent `N(0,1/12)` coordinate,
\[
\|p_Q\|_\infty\le
C_{2H1G}=4.109270566451296\ldots<3\sqrt2.
\tag{5.1}
\]
It also transfers (5.1) to the exact finite physical family with two cap-one heavy coordinates and one normalized uniform bank.  In the present bank-size compactification this is the boundary sequence
`(m_1,m_2,m_3)=(1,1,m)` with the lightlike core `B_0`, and therefore
\[
\boxed{
\limsup_{m\to\infty}\|p_{Q_{(1,1,m),B_0}}\|_\infty
\le4.109270566451296\ldots<3\sqrt2.
}
\tag{5.2}
\]
Thus both the fully diffuse interior (all rotations) and this canonical two-heavy/one-diffuse zero-pivot edge fail to generate an asymptotic overshoot above the Gaussian obstruction.

## 6. Sharp-witness implication and exact remaining gap

The theorem is deliberately not a full-QFORM result.  It proves the following genuine witness obstruction:

If a sequence inside the three disjoint uniform-bank rank-three architecture satisfies
\[
\limsup\|p_Q\|_\infty>3\sqrt2,
\]
then at least one bank size must stay bounded along a subsequence.  Hence a sharp-constant counter-witness cannot be produced by a genuinely all-diffuse non-aligned rotation; it must retain intermediate/macroscopic leverage.  The canonical `(1,1,m)` lightlike zero-pivot boundary is also excluded by (5.2).

Still unpaid are finite/intermediate bank-size configurations with genuinely non-aligned minority-sign geometry, rough non-log-concave laws in the bank coordinates, shared macroscopic rows or multiscale fragments that do not reduce to three independent banks, and arbitrary additional spectrum.  Failure to extend the present compactness argument to those classes would only be a failure of this proof mechanism.  A finite example with peak above `3sqrt(2)` would refute that proposed sharp constant, not the existence of some larger universal QFORM bound; a counterexample to QFORM itself must make every universal bound fail.
