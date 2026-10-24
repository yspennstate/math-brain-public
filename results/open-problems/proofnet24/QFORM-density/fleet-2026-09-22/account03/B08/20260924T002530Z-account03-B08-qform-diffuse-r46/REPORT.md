SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T00:25:30Z.
attacking: large physical diagonal twists in the aligned two-bank survivor; pivot a diffuse arm coordinate and show exact Schur determinant cancellation turns the twist itself into rank-two fractional curvature, while near cancellation forces high arm leverage or large normalized carrier curvature.

# account03/B08 r46 — aligned large-twist diffuse Schur router

Programme `QFORM-DENSITY-3EIG-20260922`. Status: **NEW SUPPORTING THEOREM / FULL TARGET OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. This report advances the large-diagonal-twist survivor of r45 using only original independent coordinates. It adds no moments, support, log-concavity, iid, sign, or rotated-independence assumption. The new Schur branch proves essential boundedness only; the separately cited low-rank-paving and partner child-window branches are continuous `C_0`.

## 1. Correction boundary and source theorem

The live corrections were reread in this actual run. In particular the new account01/B15 event `QFORM-HALFRIESZ-PLUS-BARE-SQUARE-NOT-SUFFICIENT-v1`, source `yspennstate/math-open-problems@a2e3c99bd7c6715ec4260fa3a7918499c4ae8b3d`, shows that a black-box square-root small-ball certificate plus a bare independent square is endpoint-critical and can fail. The argument below does not use that interface. It uses the stronger completed translation-uniform **half-Riesz expectation** for a rank-two product projection with arbitrary coordinate-separable phases.

The analytic input is account01/B14 `QFORM-SCHUR-DIFFUSE-RANK2-PLUS-SEPARABLE-v1`, source `yspennstate/math-open-problems@fe5ac898cc159fa879c94a5bd3c71984d6aab834`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B14/20260922T181432Z-account01-B14-QFORM-r15/REPORT.md`. If an original scalar pivot has coefficient `a!=0` and a bank of its exact Schur complement is

`D+U Lambda U^T`, `U^T U=I_2`, `max row_leverage(U)<=1/2`, `det Lambda!=0`,

with `D` arbitrary diagonal and all outside coefficients arbitrary, then

`||p_Q||_infinity <= 4 sqrt(2e) |a|^(-1/2) |det Lambda|^(-1/4)`.

## 2. Exact aligned normal form

Continue the r45 normal form

\[
A=\begin{pmatrix}B&M\\M^T&M^TRM+D\end{pmatrix},\qquad
D=\operatorname{diag}(d_1,\ldots,d_m),                         \tag{2.1}
\]

where `B,R` are arbitrary symmetric `2 x 2` matrices and `M` is `2 x m` of full row rank. Put

\[
G=MM^T,
\quad m_j=M[:,j],
\quad \ell_j=m_j^TG^{-1}m_j,
\quad \mu=\max_j\ell_j,                                       \tag{2.2}
\]

and for a physical light coordinate `j`

\[
a_j=d_j+m_j^TRm_j.                                             \tag{2.3}
\]

Assume first `a_j!=0`. Let `K={1,...,m}\setminus{j}` and `M_K=M[:,K]`. Pivoting only the original coordinate `X_j`, the `K x K` block of the exact full Schur complement is

\[
D_K+M_K^TR_jM_K,
\qquad
R_j=R-a_j^{-1}Rm_jm_j^TR.                                     \tag{2.4}
\]

No hub or outside term is deleted.

Two determinant identities are exact:

\[
\boxed{\det(M_KM_K^T)=\det(G)(1-\ell_j)}                       \tag{2.5}
\]

by the matrix determinant lemma, and, if `det R!=0`,

\[
\boxed{\det R_j=\det R\,{d_j\over a_j}}.                       \tag{2.6}
\]

Indeed `det R_j=det R(1-a_j^{-1}m_j^TRm_j)` and `a_j-m_j^TRm_j=d_j`. Thus the physical diagonal twist survives **exactly** in the post-pivot rank-two determinant.

## 3. Diffuse leverage survives deletion

Assume

\[
\mu\le1/3.                                                       \tag{3.1}
\]

Then `ell_j<1`, so `G_K=M_KM_K^T` is positive definite. Set

\[
U_K=M_K^TG_K^{-1/2},\qquad U_K^TU_K=I_2.                        \tag{3.2}
\]

For `k!=j`, Sherman--Morrison gives

\[
\ell_k^{(K)}=m_k^TG_K^{-1}m_k
=\ell_k+{(m_k^TG^{-1}m_j)^2\over1-\ell_j}.                     \tag{3.3}
\]

Cauchy--Schwarz in the `G^{-1}` inner product gives `(m_k^TG^{-1}m_j)^2<=ell_k ell_j`, hence

\[
\boxed{
\ell_k^{(K)}\le{\ell_k\over1-\ell_j}
\le{\mu\over1-\mu}\le1/2.}                                    \tag{3.4}
\]

So a `1/3`-diffuse physical two-frame remains within the exact `1/2` leverage gate needed by the completed rank-two half-Riesz theorem after deleting any one arm coordinate.

## 4. Main theorem

### `QFORM-ALIGNED-LARGETWIST-DIFFUSE-SCHUR-v1`

Under (2.1), `rank M=2`, and `mu<=1/3`, fix `j` with

\[
d_j\ne0,\qquad a_j\ne0,\qquad \det R\ne0.                    \tag{4.1}
\]

Then for every admissible cap-one product input the full quadratic form has an essentially bounded density and

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le4\sqrt{2e}\,
\bigl(|a_jd_j|\,|\det R|\,\det(MM^T)(1-\ell_j)\bigr)^{-1/4}.} \tag{4.2}
\]

**Proof.** Define

\[
\Lambda_j=G_K^{1/2}R_jG_K^{1/2}.                               \tag{4.3}
\]

Then `M_K^TR_jM_K=U_K Lambda_j U_K^T`, and by (2.5)-(2.6)

\[
|\det\Lambda_j|
=\det G(1-\ell_j)|\det R|{|d_j|\over|a_j|}.                   \tag{4.4}
\]

The frame `U_K` satisfies the row gate (3.4), and the remaining bank diagonal `D_K` is arbitrary. Apply the cited B14 theorem with scalar pivot `a_j`. It gives

`4 sqrt(2e)|a_j|^(-1/2)|det Lambda_j|^(-1/4)`,

which becomes (4.2) after substituting (4.4). QED.

Define the normalized two-arm area currency

\[
\Gamma=\sqrt{|\det R|\det(MM^T)}.                              \tag{4.5}
\]

If, at target scale `L>0`,

\[
|d_j|\ge\delta L,\quad |a_j|\ge\alpha L,\quad \Gamma\ge\gamma L,
\tag{4.6}
\]

then `1-ell_j>=2/3` and

\[
\boxed{
\|p_Q\|_\infty
\le4\sqrt{2e}\bigl((2/3)\alpha\delta\gamma^2\bigr)^{-1/4}L^{-1}.}
\tag{4.7}
\]

Numerically `4 sqrt(2e)=9.326575926388497`. With the convenient noncancellation gate `alpha=delta/2`,

\[
\boxed{\|p_Q\|_\infty
\le12.274464207(\delta\gamma)^{-1/2}L^{-1}.}                    \tag{4.8}
\]

## 5. Cancellation router

Normalize the aligned carrier by

\[
K_R=G^{1/2}RG^{1/2},\qquad q_j=G^{-1/2}m_j.                    \tag{5.1}
\]

Then `||q_j||^2=ell_j` and `m_j^TRm_j=q_j^TK_Rq_j`.

### `QFORM-TWIST-CANCELLATION-LEVERAGE-ROUTER-v1`

For `0<theta<1`, if

\[
|a_j|<\theta|d_j|,                                               \tag{5.2}
\]

then

\[
\boxed{
\ell_j\ge{(1-\theta)|d_j|\over\|K_R\|_{op}}.}                 \tag{5.3}
\]

Proof: (5.2) forces `|q_j^TK_Rq_j|>(1-theta)|d_j|`, while `|q_j^TK_Rq_j|<=ell_j||K_R||op`.

Consequently, under `mu<=1/3`, if `|d_j|>=delta L` and

\[
\|K_R\|_{op}\le(3\delta/2)L,                                   \tag{5.4}
\]

then `theta=1/2` rules out `|a_j|<|d_j|/2`; every such large twist falls into (4.8), provided `Gamma>0`.

There is also an aggregate cancellation budget. Since `sum_j q_jq_j^T=I_2`,

\[
\sum_j|q_j^TK_Rq_j|
\le\sum_jq_j^T|K_R|q_j
=\operatorname{tr}|K_R|=\|K_R\|_*.                            \tag{5.5}
\]

Hence for any set `J` all satisfying (5.2),

\[
\boxed{(1-\theta)\sum_{j\in J}|d_j|<\|K_R\|_*.}                \tag{5.6}
\]

Thus many near-cancelled large physical twists force a genuinely large two-dimensional normalized carrier; cancellation cannot remain diffuse at bounded carrier curvature.

## 6. Existing diffuse low-rank exit handles arbitrary diagonal twists

Let

\[
A_0=\begin{pmatrix}B&M\\M^T&M^TRM\end{pmatrix}.               \tag{6.1}
\]

As in r45, `rank(A_0)<=4`. Account01/B19 `QFORM-LOWRANK5-DIFFUSE-PAVING-v1`, source `yspennstate/math-open-problems@a09353b7b4cc9b1b812b1d1f2f319f5dcef5e10b`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260923T151334Z-account01-B19-QFORM-auto11/REPORT.md`, applies directly to `A=A_0+diag(0,0,D)`. If

\[
s_3(A_0)\ge\sigma,\qquad
\max_i(P_{\operatorname{Ran}A_0})_{ii}\le1/320,                 \tag{6.2}
\]

then for **arbitrary** diagonal `D`, however large,

\[
\boxed{\|p_Q\|_\infty\le{96\sqrt e\over7\sigma},\qquad p_Q\in C_0.} \tag{6.3}
\]

At `sigma=L/128`,

\[
\boxed{\|p_Q\|_\infty<2894.213/L.}                             \tag{6.4}
\]

So the new theorem is needed only when the rank-at-most-four aligned skeleton itself is not already paid by diffuse paving.

## 7. Designated partner account04/B08 applied to the same physical coordinate

The completed partner theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` is at

`yspennstate/math-open-problems@af30108d1fd48a138ef13c683d397a74f8e0228e`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

For the same selected physical light coordinate `j`, write

\[
A=\begin{pmatrix}a_j&b_j^T\\b_j&C_j\end{pmatrix}.             \tag{7.1}
\]

If `C_j` has three eigenvalues of modulus at least `L/64` and its spectral projection onto `|lambda(C_j)|>=L/4096` has maximum physical leverage at most `1/32`, the partner theorem with `m=L/64` gives

\[
\boxed{\|p_Q\|_\infty<4096/L,\qquad p_Q\in C_0.}              \tag{7.2}
\]

This bound is independent of `a_j`, `d_j`, and `det R`, so it pays an actual part of the cancellation/singular-carrier endpoint left outside Theorem 4. The remaining partner failure is concrete: the deletion child loses its third spectral direction or has a physical child coordinate with window leverage `>1/32`.

## 8. Regression checks

A seeded finite-dimensional checker tested the algebra over 1915 admissible random instances. It found maximum absolute error `<3.98e-13` in (2.5), `<2.21e-12` in (2.6), and zero violations of (3.4); the largest numerical value of `max_k ell_k^(K)-mu/(1-ell_j)` was `<-3.3e-08`.

Recorded constants:

`4 sqrt(2e)=9.326575926388497`,
`4 sqrt(2e) 3^(1/4)=12.274464206548219`,
`(96 sqrt(e)/7)*128=2894.2124249090252`.

These computations are regression evidence only; the proof is analytic.

## 9. Remaining implication

The full conjecture and full continuity remain OPEN. This run closes the large-twist branch whenever either the rank-four aligned skeleton is diffusely three-dimensional, or a diffuse two-arm coordinate has nonzero `det R` and its physical pivot is not cancelled, or the designated partner deletion child is three-dimensional and diffuse.

The next B08 implication is `QFORM-ALIGNED-CANCELLED-TWIST-HUGECARRIER-OR-CHILDLOCALIZED-v1`: consume a large physical twist for which `a_j` is zero/tiny and the normalized carrier is large enough to avoid (5.3), or consume the partner failure where the same child loses third spectrum or develops a high-leverage spectral-window coordinate. The `det R=0` endpoint also remains unless the child-window theorem pays it. Any continuation must retain the exact carrier and arbitrary diagonal twists; it may not treat cancellation as a small random perturbation.
