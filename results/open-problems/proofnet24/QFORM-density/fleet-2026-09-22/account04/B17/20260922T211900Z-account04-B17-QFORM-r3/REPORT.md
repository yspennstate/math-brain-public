# QFORM-B17 sharp rotated witness (revision 2026-09-22.15)

Run: `20260922T211900Z-account04-B17-QFORM-r3`  
Status: `ESSENTIAL_STEP_APPLIED`; full conjecture open; `WITHOUT_VERIFIED_BRAIN`.

## Result

Let \(J=\operatorname{diag}(1,1,-1)\) and
\[
O={1\over7}\begin{pmatrix}6&-2&-3\\-2&3&-6\\-3&-6&-2\end{pmatrix},
\qquad O^TO=I.
\]
Write \(v_j=Oe_j\).  For every integer \(m\ge3\), take the \(3m\)
independent variables \(X_{jk}\sim\mathrm{Unif}[-1/2,1/2]\), and repeat the
physical row \(v_j/\sqrt m\) for \(1\le k\le m\).  If \(R_m\) is the resulting
\(3m\times3\) matrix, set
\[
A_m=R_mJR_m^T,
\qquad Q_m=X^TA_mX.
\]
Then every input density is exactly one on a set of length one,
\(R_m^TR_m=I_3\), and the nonzero spectrum of \(A_m\) is exactly
\(\{1,1,-1\}\).  Moreover
\[
B:=O^TJO={1\over49}\begin{pmatrix}
31&-36&-12\\-36&-23&-24\\-12&-24&41
\end{pmatrix}.
\]
All nine entries of \(B\) are nonzero.  Thus the form is an exact, genuinely
rotated indefinite form: all three physical banks are coupled, while no
post-rotation independence is assumed.

The density of \(Q_m\) is continuous and obeys the sharp expansion
\[
\boxed{
p_{Q_m}(0)=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right).
}
\]
Consequently any universal constant in the owner conjecture must satisfy
\[
\boxed{C_{\rm universal}\ge3\sqrt2.}
\]
This is a genuine lower bound for the exact quantifiers, not a Gaussian input
example: every finite member uses independent cap-one uniform densities and a
matrix with precisely three eigenvalues of magnitude one.

For comparison, the unrotated three-bank control has
\[
p(0)=3\sqrt2\left(1-{69\over320m}+O(m^{-2})\right).
\]
The larger rotated deficit \(5295/21952>69/320\) is consistent with the
completed tight-frame mixing-deficit inequality, but both families converge
to the same sharp obstruction.

## Proof

Put
\[
Y_{mj}=m^{-1/2}\sum_{k=1}^mX_{jk},\qquad \sigma^2=1/12.
\]
Then \(Y_{m1},Y_{m2},Y_{m3}\) are independent and
\[
Q_m=Y_m^TBY_m=(OY_m)^TJ(OY_m).
\]

### Weighted local Edgeworth lemma

If \(g_m\) is the density of \(Y_{mj}\), \(\gamma_\sigma\) is the
\(N(0,\sigma^2)\) density, and \(H_4(u)=u^4-6u^2+3\), then, with an integrable
polynomially weighted remainder,
\[
g_m(y)=\gamma_\sigma(y)
\left[1-{1\over20m}H_4(y/\sigma)\right]+O(m^{-2}).
\tag{1}
\]
For completeness, standardize the summands. Their characteristic function is
\(\operatorname{sinc}(\sqrt3t)\), and
\[
m\log\operatorname{sinc}(\sqrt3t/\sqrt m)
=-{t^2\over2}-{t^4\over20m}+O(t^6/m^2).
\]
Fourier inversion on \(|t|\le m^{1/8}\) gives (1).  On the complement, use
\(|\operatorname{sinc}u|\le\min(1,|u|^{-1})\), splitting once more at
\(|t|=\sqrt m\).  Applying the same bounds after finitely many Fourier
derivatives gives an \(O(m^{-2})(1+|y|)^{-8}\) majorant.  This both justifies
termwise integration below and supplies continuity for \(m\ge3\).

### Coarea calculation

Since \(B\) is nonsingular of inertia \((2,1)\),
\[
p_{Q_m}(0)=\int_{y^TBy=0}{\prod_{j=1}^3g_m(y_j)\over |2By|}\,d\mathcal H^2(y).
\tag{2}
\]
The cone singularity at the origin is integrable in dimension three.
Parametrize it by
\[
y=O^T(r\cos\theta,r\sin\theta,\varepsilon r),
\quad r>0,\quad0\le\theta<2\pi,\quad\varepsilon\in\{\pm1\}.
\]
Because \(B^2=I\), each nappe contributes
\(d\mathcal H^2/|2By|=\tfrac12\,dr\,d\theta\).
The Gaussian term in (1) therefore gives
\[
(2\pi\sigma^2)^{-3/2}
\int_0^{2\pi}\int_0^\infty e^{-r^2/\sigma^2}\,dr\,d\theta
={1\over2^{3/2}\sigma^2}=3\sqrt2.
\tag{3}
\]

It remains to evaluate the first Edgeworth correction.  Under the normalized
measure in (3), \(q=r/\sigma\) has density
\(2\pi^{-1/2}e^{-q^2}\), hence
\(\mathbb Eq^2=1/2\), \(\mathbb Eq^4=3/4\).  With
\(w_\varepsilon=(\cos\theta,\sin\theta,\varepsilon)\) and
\(a_j=(O^Tw_\varepsilon)_j\), one has \(\sum_ja_j^2=2\).  If
\(u_j=O_{3j}^2\), averaging first in \(\theta,\varepsilon\) gives
\[
A_4:=\mathbb E_{\theta,\varepsilon}\sum_ja_j^4
=\sum_j\left[{3\over8}(1-u_j)^2+3u_j(1-u_j)+u_j^2\right]
={27\over8}-{13\over8}\sum_ju_j^2.
\]
Here \((u_1,u_2,u_3)=(9,36,4)/49\), so
\[
\sum_ju_j^2={199\over343},\qquad A_4={3337\over1372}.
\]
Consequently
\[
\mathbb E\sum_jH_4(qa_j)
={3\over4}A_4-6\left({1\over2}\right)2+9
={26475\over5488}.
\]
Multiplying by the coefficient \(-1/(20m)\) in (1) yields
\(5295/21952m\), proving the displayed expansion.  The weighted remainder in
(1), together with the cone parametrization, integrates to \(O(m^{-2})\).

Continuity follows from the same parametrization and dominated convergence;
this continuity statement is only for this witness family, not for the full
owner target.

## Partner-result integration

Account01/B17 proved that every infinitesimal tight-frame weak limit has
Gaussian covariance \(\Gamma\succeq I_3/12\), and hence that every such
three-large-eigenvalue limiting quadratic density is at most \(3\sqrt2\).
The present rows have leverage exactly \(1/m\), and the uniform triangular
array converges to \(N(0,I_3/12)\).  Applying the partner inequality to this
limiting law gives \(\|p_{Q_\infty}\|_\infty\le3\sqrt2\).  The local
Edgeworth calculation above supplies the additional local-limit statement
\(p_{Q_m}(0)\to p_{Q_\infty}(0)=3\sqrt2\).  Thus the partner ceiling is sharp, even along
exact dense rotated finite-dimensional forms.

Partner source:
`yspennstate/math-open-problems@1b7a876f7577cf99599322926154ce0032a034fd`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/QFORM-B17-20260922T155124Z/REPORT.md`.

## Scope and remaining gap

This settles a sharp necessary lower bound and an exact rotated stress family.
It does not prove the universal upper bound.  In particular, the partner
theorem controls diffuse limits, while a full proof must still control finite
leverage/localized configurations and arbitrary added spectrum.  The full
continuity claim also remains open.

Controls refreshed immediately before publication: owner revision
`2026-09-22.15`; owner README blob
`fca13a89d221115332ce5e60d49554ee0e213efa`; correction inbox blob
`c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.
