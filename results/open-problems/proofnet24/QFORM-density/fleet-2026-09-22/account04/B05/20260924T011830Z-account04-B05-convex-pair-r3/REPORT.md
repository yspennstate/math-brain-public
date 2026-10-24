SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B05, 2026-09-24T01:18:30Z.
attacking: a rough-input convex coarea theorem on an actual physical two-coordinate block, followed by a comparison with the newest shared-remainder/disjoint-square theorem.

# B05 — exact convex physical-pair interval theorem

Run: \`20260924T011830Z-account04-B05-convex-pair-r3\`.

Status: **NEW FULL-LINE SUPPORTING THEOREM / ROUGH INPUTS / FULL QFORM OPEN**.

The unrestricted conjecture is not proved or disproved here. The result below applies only when an actual original-coordinate \(2\times2\) principal block is definite. It preserves arbitrary outside couplings and spectrum, arbitrary signs outside the block, unbounded and fragmented supports, and conditioning-generated affine terms. No independence after rotation is used.

## 1. The rough convex theorem

### Theorem \`QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1\`

Let \(X_1,\dots,X_n\) be independent real variables with probability densities \(0\le f_i\le m_i\). Let \(A=A^T\), and suppose that for two original coordinates \(i,j\), the principal block
\[
C=A[\{i,j\},\{i,j\}]
\]
is positive or negative definite. Then for every interval \(I\subset\mathbb R\),
\[
\boxed{
 \Pr\{X^TAX\in I\}
 \le \frac{\pi m_i m_j}{\sqrt{|\det C|}}\,|I|.
}
\tag{1.1}
\]
Consequently \(X^TAX\) has a density satisfying
\[
\boxed{
 \|p_{X^TAX}\|_{\infty,\mathrm{ess}}
 \le \frac{\pi m_i m_j}{\sqrt{|\det C|}}.
}
\tag{1.2}
\]

In the cap-one case, \(\|p_Q\|_{\infty,\mathrm{ess}}\le\pi/\sqrt{|\det C|}\). The estimate is homogeneous of degree \(-1\) in \(A\).

### Proof

Write \(U=(X_i,X_j)^T\), and condition on every other original coordinate, denoted by \(Z=z\). The conditional quadratic is
\[
q_z(u)=u^TCu+2\ell(z)^Tu+r(z).
\tag{1.3}
\]
Only the affine vector and output constant depend on the conditioning. The conditional joint density of \(U\) is still the literal product \(f_i(u_1)f_j(u_2)\), hence is bounded by \(m_i m_j\).

Multiplying the whole form by \(-1\) if necessary, assume \(C>0\). Complete the square:
\[
q_z(u)=(u+C^{-1}\ell(z))^TC(u+C^{-1}\ell(z))
+r(z)-\ell(z)^TC^{-1}\ell(z).
\tag{1.4}
\]
For \(t\ge0\), the ellipse
\[
E_t=\{u:(u-u_z)^TC(u-u_z)\le t\}
\]
has area
\[
|E_t|=\frac{\pi t}{\sqrt{\det C}},
\tag{1.5}
\]
and \(E_t\) is empty for \(t<0\). Therefore the preimage of any interval \(I\) under \(q_z\) has area at most
\[
\frac{\pi}{\sqrt{\det C}}|I|.
\tag{1.6}
\]
This remains true when the interval crosses the minimum, because the negative part contributes no area. Hence
\[
\Pr\{q_z(U)\in I\mid Z=z\}
\le m_i m_j\,|\{u:q_z(u)\in I\}|
\le \frac{\pi m_i m_j}{\sqrt{\det C}}|I|.
\tag{1.7}
\]
Averaging over \(Z\) proves (1.1). The interval domination criterion gives absolute continuity and (1.2).

This is already a rough-input proof. It evaluates neither a pointwise density trace nor a prescribed-surface representative. Equivalently, the coarea Jacobian is certified by the exact area derivative
\[
\frac{d}{dt}|E_t|=\frac{\pi}{\sqrt{\det C}}
\quad\text{for a.e. }t>0.
\tag{1.8}
\]
Arbitrary outside coupling is harmless because conditioning produces only the affine term in (1.3). \(\square\)

## 2. Why this is a genuine convex/two-sheet payment

For a definite binary quadratic, a level set is an ellipse and an interval preimage is an elliptical annulus, or a filled ellipse when the interval crosses the extremum. The two root sheets are both included in the area identity (1.5); there is no missing branch factor. The argument uses the product cap only in the original two coordinates.

For an indefinite block, the corresponding annular area is infinite. Thus (1.1) must not be extended by replacing \(\det C>0\) with \(|\det C|>0\). Hyperbolic blocks require one of the ruled, Moyal, determinant-coarea, or hub receivers. This is the exact boundary of the theorem.

## 3. Applying the completed account01/B05 theorem at the same equation

The newest completed account01/B05 theorem, \`QFORM-SHARED-REMAINDER-DISJOINT-SQUARE-v1\` at commit \`ad88bc891f3094c84b4e7c3be104d407c8ed032f\`, states that
\[
Q=2HA(Z)+R(Z)+\gamma Y^2+2W(Z)Y
\]
obeys, for cap-one \(H,Y\) and \(\|p_A\|_\infty\le M_A\),
\[
\|p_Q\|_\infty
\le4\sqrt2\,\sqrt{M_A}\,|\gamma|^{-1/2}.
\tag{3.1}
\]
It allows arbitrary same-source dependence among \(A,R,W\).

Apply both theorems to the actual target-valid family
\[
Q_b=2HL+2bLP+V^2+Y^2,
\tag{3.2}
\]
where \(H,L,P,V,Y\) are independent original cap-one variables. Its homogeneous matrix in the displayed order is
\[
B_b=
\begin{pmatrix}
0&1&0&0&0\\
1&0&b&0&0\\
0&b&0&0&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix},
\tag{3.3}
\]
with spectrum
\[
\{0,\sqrt{1+b^2},-\sqrt{1+b^2},1,1\}.
\tag{3.4}
\]
Hence it has four eigenvalues of modulus at least one for every \(b\).

First use account01/B05 with \(A=L\), \(R=2bLP+V^2\), \(\gamma=1\), \(W=0\). Since \(L\) has density cap one,
\[
\|p_{Q_b}\|_\infty\le4\sqrt2.
\tag{3.5}
\]
Now retain the actual physical pair \((V,Y)\). Its principal block is \(I_2\), so Theorem 1 gives the sharper full-line inequality
\[
\boxed{
\Pr\{Q_b\in I\}\le\pi|I|,
\qquad
\|p_{Q_b}\|_{\infty,\mathrm{ess}}\le\pi
}
\tag{3.6}
\]
uniformly for all \(b\), and even after adjoining arbitrary extra coordinates and arbitrary couplings to them. This is a concrete use of the completed account01 theorem and a strict convex-coarea improvement at the same equation.

More generally, whenever a form lies simultaneously in the account01 shared-remainder branch and contains a definite physical pair \(C\), the valid bound is
\[
\|p_Q\|_{\infty,\mathrm{ess}}
\le
\min\left\{
4\sqrt2\,m_Y\sqrt{m_HM_A}|\gamma|^{-1/2},
\frac{\pi m_i m_j}{\sqrt{|\det C|}}
\right\}.
\tag{3.7}
\]

## 4. Scope and remaining gap

This closes the convex physical-pair branch completely, including rough inputs, both root sheets, conditioning-generated affine terms, and arbitrary outside spectrum/coupling. It does not supply a universal definite physical pair from the sole global assumption \(s_3(A)\ge1\).

The remaining B05 debt is genuinely hyperbolic/diffuse: matrices with no quantitatively definite original-coordinate pair, especially the near-null overlapping square-carrier configuration identified by account01/B05. There the physical interval preimage can have infinite area, so the present convex argument cannot be continued by an arbitrary-joint coarea bound. One must spend product provenance through a ruled, hub, or aggregate mechanism.

Continuity is not asserted as part of Theorem 1; the theorem gives an essential density bound. In target matrices of rank at least three, the separate account04/B15 regularity compiler can be applied after the interval estimate.

## 5. Source pins

- Owner/control package: \`yspennstate/math-research-brain\` fresh main, OWNER CONTROL revision \`2026-09-22.15\`.
- Required Claude package begins at \`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/\`.
- Prior rough ruled/two-sheet B05 report: \`math-open-problems@ae670b9085d4bb7ab01c54021cd89f620aa2f0b3\`.
- Completed account01/B05 input: \`math-open-problems@ad88bc891f3094c84b4e7c3be104d407c8ed032f\`.
- Rough regularity compiler: account04/B15, commit \`d734abaae2eedafe9572b4215107c9637807acaa\`.

Repository delivery is not native brain ingestion. Model and thinking metadata remain UNKNOWN.
