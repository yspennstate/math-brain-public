SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-24T10:38:08.750760Z.
attacking: two and multi-macroscopic non-collinear rows: derive the compensated cone-tip expansion and test whether splitting macroscopic variance across directions can overshoot 3 sqrt(2); apply the newest fleet02/B17 finite tight-frame Poisson result to an explicit target family.

# QFORM-MULTIMACRO-SECONDORDER-RIGIDITY-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T103808Z-fleet01-B17-QFORM-auto11`  
Status: `NEW SUPPORTING THEOREM / EXACT NONCOLLINEAR DENSE WITNESS / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. The unrestricted continuity conclusion remains separate. This report uses no post-rotation independence of physical inputs, no law-uniform pointwise oscillatory decay, no arbitrary-joint coarea bound, no conditional projection-density moment, and no dimension-free fiber-supremum step.

The strongest source-valid numerical lower obstruction remains
\[
\boxed{C_{\rm univ}\ge 3\sqrt2.}
\]
The new result identifies the second-order geometry of *any finite collection* of compensated macroscopic uniform rows near this obstruction. In particular, for a fixed number of rows and fixed total macroscopic variance, splitting the rows into non-collinear directions cannot improve the cone-tip to second order: the unique second-order optimum is equal fragmentation along the minority eigendirection.

## 1. General compensated finite-macro model

Work in the three-dimensional active spectral space with
\[
J=\operatorname{diag}(1,1,-1).
\]
This is only a latent spectral coordinate system; no independence of rotated physical coordinates is asserted.

Fix unit vectors \(v_1,\ldots,v_k\in\mathbb R^3\) and coefficients \(\alpha_j\ge0\). For \(\varepsilon>0\), put
\[
H_\varepsilon=\varepsilon\sum_{j=1}^k\alpha_jv_jv_j^T
\]
and assume \(H_\varepsilon<I\). Let
\[
G_\varepsilon\sim N\!\left(0,\frac{I-H_\varepsilon}{12}\right),
\qquad U_j\stackrel{\rm iid}{\sim}{\rm Unif}[-1/2,1/2],
\]
all independent, and define
\[
Y_\varepsilon
=G_\varepsilon+
\sum_{j=1}^k\sqrt{\varepsilon\alpha_j}\,v_jU_j,
\qquad
Q_\varepsilon=Y_\varepsilon^T JY_\varepsilon.
\tag{1.1}
\]
The covariance is exactly preserved:
\[
\operatorname{Cov}(Y_\varepsilon)
=\frac{I-H_\varepsilon}{12}
+\frac1{12}H_\varepsilon
=\frac1{12}I.
\tag{1.2}
\]
Thus the perturbation changes higher cumulants while keeping the second-order covariance at the minimum-variance cube value.

For a unit vector \(v\), write
\[
t(v)=(v\cdot e_3)^2
\]
and define
\[
F(t)=\frac{19+2t-13t^2}{8}
=1+\frac{(1-t)(13t+11)}8.
\tag{1.3}
\]
Hence
\[
F(t)\ge1\quad(0\le t\le1),
\]
with equality only at \(t=1\), i.e. only when \(v=\pm e_3\).

## 2. Theorem: universal second-order cone-tip rigidity

### Theorem A
For fixed \(k,(\alpha_j),(v_j)\), as \(\varepsilon\downarrow0\),
\[
\boxed{
\frac{p_{Q_\varepsilon}(0)}{3\sqrt2}
=1-
\frac{3\varepsilon^2}{80}
\sum_{j=1}^k\alpha_j^2F(t(v_j))
+O(\varepsilon^3).
}
\tag{2.1}
\]
The remainder is uniform when the finite parameter tuple ranges over a compact set on which \(I-H_\varepsilon\) stays uniformly positive.

Consequently, if
\[
A_0:=\sum_{j=1}^k\alpha_j
\]
is fixed, then
\[
\sum_{j=1}^k\alpha_j^2F(t(v_j))
\ge \sum_{j=1}^k\alpha_j^2
\ge\frac{A_0^2}{k},
\tag{2.2}
\]
and equality throughout holds exactly when
\[
\alpha_1=\cdots=\alpha_k=A_0/k,
\qquad v_j=\pm e_3\quad\forall j.
\tag{2.3}
\]
Thus among all \(k\)-row compensated perturbations of fixed total macroscopic variance, the **unique second-order maximizer of the cone-tip is equal collinear fragmentation along the minority eigendirection**.

This simultaneously explains the earlier one-row coefficient \(3/80\) and the two-equal-collinear coefficient \(3/160\), and shows that a genuinely non-collinear pair is strictly less dangerous at quadratic order.

### Proof
The characteristic function of \(Y_\varepsilon\) is
\[
\widehat\rho_\varepsilon(\xi)
=e^{-|\xi|^2/24}
\prod_{j=1}^k
\left[
 e^{\varepsilon\alpha_j(v_j\cdot\xi)^2/24}
 \operatorname{sinc}\!\left(
 \frac{\sqrt{\varepsilon\alpha_j}}2(v_j\cdot\xi)
 \right)
\right].
\tag{2.4}
\]
Using
\[
\log\operatorname{sinc}z
=-\frac{z^2}{6}-\frac{z^4}{180}
-\frac{z^6}{2835}+O(z^8),
\tag{2.5}
\]
the quadratic term cancels exactly against the covariance compensation and
\[
\log\frac{\widehat\rho_\varepsilon(\xi)}
{e^{-|\xi|^2/24}}
=-\frac{\varepsilon^2}{2880}
\sum_{j=1}^k\alpha_j^2(v_j\cdot\xi)^4
+O\!\left(\varepsilon^3(1+|\xi|^6)\right).
\tag{2.6}
\]
Since the Gaussian part remains uniformly nondegenerate for sufficiently small \(\varepsilon\), this expansion and all finitely many derivatives are dominated by a Gaussian times a polynomial. Fourier inversion therefore gives the Schwartz expansion
\[
\rho_\varepsilon
=\rho_0-rac{\varepsilon^2}{2880}
\sum_{j=1}^k\alpha_j^2\partial_{v_j}^4\rho_0
+O_{\mathcal S}(\varepsilon^3),
\tag{2.7}
\]
where
\[
\rho_0(y)=\left(\frac6\pi\right)^{3/2}e^{-6|y|^2}.
\]

Parameterize one null-cone sheet of \(J\) by
\[
a_\phi=(\cos\phi,\sin\phi,1).
\]
Central symmetry gives the cone-tip functional
\[
L(f)=\frac12\int_0^{2\pi}\int_{\mathbb R}
 f(ra_\phi)\,dr\,d\phi,
\qquad
p_{Q_\varepsilon}(0)=L(\rho_\varepsilon).
\tag{2.8}
\]
The map \(L\) is continuous on Schwartz space, since a fixed Schwartz seminorm dominates the line integral by an integrable \((1+|r|)^{-2}\) envelope. Hence (2.7) can be inserted in (2.8).

For a unit \(v\), put \(\beta_\phi=v\cdot a_\phi\). Along the line \(ra_\phi\),
\[
\partial_v^4\rho_0(ra_\phi)
=\left(20736\beta_\phi^4r^4
-10368\beta_\phi^2r^2+432\right)
\rho_0(ra_\phi).
\tag{2.9}
\]
Because \(|a_\phi|^2=2\), the line weight is proportional to \(e^{-12r^2}\), under which
\[
\mathbb E r^2=\frac1{24},
\qquad
\mathbb E r^4=\frac1{192}.
\]
Therefore
\[
\frac{\int_{\mathbb R}\partial_v^4\rho_0(ra_\phi)\,dr}
{\int_{\mathbb R}\rho_0(ra_\phi)\,dr}
=108(2-\beta_\phi^2)^2.
\tag{2.10}
\]
Rotating only inside the positive eigenspace, write
\[
v=(\sqrt{1-t},0,\sqrt t),
\qquad t=(v\cdot e_3)^2.
\]
A direct trigonometric average gives
\[
\frac1{2\pi}\int_0^{2\pi}
(2-\beta_\phi^2)^2\,d\phi
=\frac{19+2t-13t^2}{8}=F(t).
\tag{2.11}
\]
Since \(L(\rho_0)=3\sqrt2\) and \(108/2880=3/80\), equations (2.7)--(2.11) give (2.1). The inequalities (2.2) are respectively (1.3) and Cauchy--Schwarz. Their equality conditions give (2.3). QED.

## 3. An explicit genuinely non-collinear two-row stress family

Choose
\[
v_1=e_3,
\qquad
v_2=\frac{(2,0,1)^T}{\sqrt5},
\qquad
\alpha_1=\alpha_2=\frac12.
\tag{3.1}
\]
The directions are non-collinear. Here
\[
t(v_1)=1,
\qquad t(v_2)=\frac15,
\]
and exactly
\[
F(1)=1,
\qquad F(1/5)=\frac{59}{25}.
\]
Thus
\[
\sum_j\alpha_j^2F(t(v_j))
=\frac14\left(1+\frac{59}{25}\right)
=\frac{21}{25}.
\]
Theorem A becomes
\[
\boxed{
\frac{p_{Q_q}(0)}{3\sqrt2}
=1-\frac{63}{2000}q^2+O(q^3),
}
\tag{3.2}
\]
where \(q=\varepsilon\). For comparison, two equal collinear minority rows have
\[
1-\frac3{160}q^2+O(q^3),
\]
so the non-collinear pair pays the strict extra second-order amount
\[
\frac{63}{2000}-\frac3{160}
=\frac{51}{4000}.
\tag{3.3}
\]
This is an analytic obstruction to a proposed overshoot mechanism: merely rotating one of two macroscopic rows away from the minority axis cannot improve the near-Gaussian cone-tip.

## 4. Exact finite, entrywise-dense realization

Let
\[
V=\frac12
\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},
\qquad V^TV=I_3.
\tag{4.1}
\]
For \(0<q\le1/10\), put
\[
H_q=\frac q2(v_1v_1^T+v_2v_2^T),
\qquad
S_q=(I-H_q)^{1/2}.
\tag{4.2}
\]
For each \(m\ge2\), form a \((4m+2)\times3\) synthesis matrix \(R_{m,q}\) whose first two rows are
\[
\sqrt{q/2}\,v_1^T,
\qquad
\sqrt{q/2}\,v_2^T,
\]
and whose remaining rows are \(m\) copies of each row of \(VS_q/\sqrt m\). Then
\[
R_{m,q}^TR_{m,q}=H_q+S_q^2=I_3.
\tag{4.3}
\]
Define
\[
A_{m,q}=R_{m,q}JR_{m,q}^T.
\tag{4.4}
\]
Because \(R_{m,q}\) is an isometric embedding of the active three-space,
\[
\boxed{\operatorname{spec}_{\ne0}(A_{m,q})=\{1,1,-1\}}
\tag{4.5}
\]
for every finite \(m\).

The matrices are also **entrywise nonzero** throughout \(0<q\le1/10\). At \(q=0\), the diffuse kernel is
\[
VJV^T=
\begin{pmatrix}
1/4&-1/4&3/4&1/4\\
-1/4&1/4&1/4&3/4\\
3/4&1/4&1/4&-1/4\\
1/4&3/4&-1/4&1/4
\end{pmatrix},
\tag{4.6}
\]
whose smallest entry magnitude is \(1/4\). Since
\[
\|H_q\|=\frac q2\left(1+\frac1{\sqrt5}\right)
\le0.072361,
\]
we may use
\[
\delta_q:=\|S_q-I\|
=1-\sqrt{1-\|H_q\|}\le\|H_q\|.
\]
Then
\[
\|S_qJS_q-J\|\le2\delta_q,
\]
so every diffuse-kernel entry changes by at most
\[
\frac34(2\delta_q)<0.109<\frac14.
\tag{4.7}
\]
For the macro--diffuse entries, the unperturbed inner products are
\[
v_1^TJV_i^T\in\{\pm1/2\},
\]
\[
v_2^TJV_i^T\in\left\{\frac1{2\sqrt5},\frac3{2\sqrt5}\right\},
\]
while the perturbation magnitude is at most
\[
\delta_q\|V_i\|<0.063<\frac1{2\sqrt5}.
\tag{4.8}
\]
Finally the macro--macro \(J\)-inner products are
\[
-1,\qquad 3/5,\qquad -1/\sqrt5,
\]
all nonzero. Hence every physical entry of \(A_{m,q}\) is nonzero.

Take all physical coordinates independently uniform on \([-1/2,1/2]\). The latent vector \(R_{m,q}^TX\) converges to (1.1) with the pair (3.1). The two macro leverages are \(q/2\), and each diffuse leverage is at most \(3/(4m)\). Thus for \(q\le1/10\), \(m\ge2\), all leverages are at most \(1/2\).

The completed Fresnel--Brascamp--Lieb Theorem F at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

therefore gives a common integrable \(O(|t|^{-3/2})\) characteristic-function majorant for the **actual finite physical forms**. Pointwise convergence of characteristic functions plus dominated convergence and Fourier inversion yield
\[
\boxed{
\|p_{m,q}-p_q\|_\infty\longrightarrow0
\quad(m\to\infty)
}
\tag{4.9}
\]
for every fixed \(q\in(0,1/10]\).

Combining (3.2) and (4.9), for every \(\eta>0\) one can first choose \(q>0\) sufficiently small and then \(m\) sufficiently large so that the exact finite, entrywise-dense, non-collinear two-row target satisfies
\[
\|p_{X^TA_{m,q}X}\|_\infty
\ge p_{m,q}(0)>3\sqrt2-\eta.
\tag{4.10}
\]
Thus the known lower obstruction \(C_{\rm univ}\ge3\sqrt2\) survives even under this stronger geometric requirement. The two special rows are genuinely present for every fixed \(q>0\), but their leverages \(q/2\) necessarily tend to zero in the sharpness limit \(q\downarrow0\); no fixed-positive-leverage sharpness claim is made here.

## 5. Completed fleet02/B17 result applied to an actual target family

The newest designated-partner result is fleet02/B17's
`finite tight-frame Poisson-location barrier`, source-pinned at

`yspennstate/math-open-problems@1e29eef72bce4aa7766f2f81c8ea13fb0786b6c9`

with checker results at

`yspennstate/math-open-problems@765da2b09b7612839c204e1899a7363574e10014`.

It proves, for every fixed finite Parseval tight frame with root-\(m\) cap-one satellite laws, that the exact finite target matrices have complete output-density convergence to an isotropic Gaussian core plus a generally non-collinear compound-Poisson location, and
\[
\limsup_m\|p_{Q_m}\|_\infty\le3\sqrt2.
\tag{5.1}
\]

Here is a concrete application. Let
\[
u_1=\frac{(1,1,1)}{\sqrt3},\quad
u_2=\frac{(1,-1,1)}{\sqrt3},\quad
u_3=\frac{(1,1,-1)}{\sqrt3},\quad
u_4=\frac{(1,-1,-1)}{\sqrt3},
\]
and take weights
\[
w_1=\cdots=w_4=\frac34.
\]
Then
\[
\sum_{a=1}^4w_au_au_a^T=I_3,
\]
and the physical synthesis rows are exactly the four tetrahedral rows in (4.1), divided by \(\sqrt m\).

Take the dense reflection
\[
n=\frac{(1,2,4)^T}{\sqrt{21}},
\qquad
B=I-2nn^T,
\]
and set
\[
\widetilde A_m=T_mBT_m^T.
\tag{5.2}
\]
Then every finite stage has exact nonzero spectrum
\[
\boxed{\{1,1,-1\}.}
\tag{5.3}
\]
Moreover the unscaled \(4\times4\) physical kernel is
\[
VBV^T=
\begin{pmatrix}
-5/12&-1/4&5/12&7/12\\
-1/4&15/28&-5/28&17/28\\
5/12&-5/28&61/84&11/84\\
7/12&17/28&11/84&13/84
\end{pmatrix},
\tag{5.4}
\]
so every physical entry is nonzero.

Instantiate the partner's exact cap-one satellite law with
\[
\lambda_a=1,
\qquad R_a=1
\qquad(a=1,\ldots,4).
\]
Thus every original physical density consists of a central interval of length \(1-1/m\) plus two remote intervals of length \(1/(2m)\) each, centered at \(\pm(2+\sqrt m)\). The limit is
\[
Y_m\Rightarrow G+M,
\qquad
G\sim N(0,I_3/12),
\]
where
\[
M=\sum_{a=1}^4\frac{\sqrt3}{2}
(N_{a,+}-N_{a,-})u_a,
\qquad
N_{a,\pm}\stackrel{\rm ind}{\sim}{\rm Poisson}(1/2).
\tag{5.5}
\]
This is genuinely non-collinear and non-Lindeberg. Applying the completed fleet02/B17 theorem gives the actual exact-target inequality
\[
\boxed{
\limsup_{m\to\infty}
\|p_{X^T\widetilde A_mX}\|_\infty
\le3\sqrt2.
}
\tag{5.6}
\]

We can make this concrete inequality strict by combining the same partner construction with fleet02/B17's earlier completed quantitative Gaussian-location theorem

`yspennstate/math-open-problems@f1b5f3b66e19fa17acf395ea31e6615d7ddc7440`,
checks at `97d91254e56ad2f8c79b121a0ce8bf66472a11d9`.

For \(G\sim N(0,I/12)\), a reflection \(B\), and deterministic shift \(m\), that theorem gives
\[
\|p_{(G+m)^TB(G+m)}\|_\infty
\le e^{-6|m|^2}C_0+(1-e^{-6|m|^2})C_1,
\tag{5.7}
\]
where
\[
C_0=3\sqrt2,
\qquad
C_1=\frac{12e^{-1/2}}{\sqrt{2\pi}}.
\]
For (5.5), the total number of Poisson jumps is \({\rm Poisson}(4)\). On the event of exactly one jump, which has probability \(4e^{-4}\), one has
\[
|M|=\frac{\sqrt3}{2}.
\]
On all other events we simply use \(e^{-6|M|^2}\le1\). Hence
\[
\mathbb E e^{-6|M|^2}
\le1-4e^{-4}(1-e^{-9/2}).
\tag{5.8}
\]
Averaging (5.7) gives
\[
\boxed{
\|p_{(G+M)^TB(G+M)}\|_\infty
\le
C_1+(C_0-C_1)
\bigl[1-4e^{-4}(1-e^{-9/2})\bigr]
}
\tag{5.9}
\]
with numerical value
\[
\boxed{4.14563248192024416656\ldots<4.146<3\sqrt2.}
\tag{5.10}
\]
The newest fleet02/B17 finite-stage theorem supplies uniform convergence of the complete densities, so (5.10) implies
\[
\boxed{
\|p_{X^T\widetilde A_mX}\|_\infty<4.146
\quad\text{for all sufficiently large }m.
}
\tag{5.11}
\]
This is the requested application of a completed partner result to a genuine finite QFORM family, not merely to a latent control calculation.

## 6. What this constrains

The sharp-witness picture is now more rigid near the known obstruction:

1. One compensated macroscopic row cannot improve the cone-tip above \(3\sqrt2\), in arbitrary orientation (previous B17 theorem).
2. Two equal collinear minority rows are globally subcritical and have half the one-row quadratic penalty (previous B17 theorem).
3. **This run:** for every fixed number \(k\), *all* compensated finite-macro configurations have a negative second-order correction; for fixed total macro variance the least negative correction is uniquely attained by equal fragmentation along the minority eigendirection.
4. A finite non-collinear tight-frame compound-Poisson location on top of the minimum Gaussian core is globally capped by \(3\sqrt2\), and the explicit tetrahedral instance above is in fact strictly below \(4.146\).

Therefore an overshoot above \(3\sqrt2\), if it exists, cannot be generated perturbatively by finitely many compensated uniform macro rows near the Gaussian point. The remaining sharp-witness mechanisms are genuinely nonperturbative finite-macro interactions, rough residual shapes without a surviving covariance-floor Gaussian core, or additional active spectrum that interacts before rank-three aggregation.

This is a supporting sharpness theorem, not a proof that \(3\sqrt2\) is the universal sharp constant and not a proof of the full QFORM theorem.

## 7. Correction compliance and source status

Consumed current corrections include: false law-uniform pointwise quadratic decay; false arbitrary-joint rank-three coarea; false positive conditional projection-density moment; dimension loss under naive fiber suprema; and no independence after spectral rotation. The finite constructions preserve original-coordinate independence explicitly. The only rotations are inside the fixed three-dimensional coefficient calculation or rotationally invariant Gaussian comparator.

The mathematical dependencies used as proved inputs are:

- Fresnel--Brascamp--Lieb Theorem F: `e5f71d79eff325201dd0274053d20268ce65b837`.
- fleet02/B17 finite tight-frame Poisson-location barrier: `1e29eef72bce4aa7766f2f81c8ea13fb0786b6c9`, checks `765da2b09b7612839c204e1899a7363574e10014`.
- fleet02/B17 random-location Gaussian quantitative theorem: `f1b5f3b66e19fa17acf395ea31e6615d7ddc7440`, checks `97d91254e56ad2f8c79b121a0ce8bf66472a11d9`.

The new second-order theorem and the concrete matrix identities are independently reproducible from the accompanying checker. Full QFORM remains open.
