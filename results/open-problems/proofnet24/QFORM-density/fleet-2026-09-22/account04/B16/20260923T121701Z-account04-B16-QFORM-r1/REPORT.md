SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B16, 2026-09-23T12:17:01Z.
attacking: the transverse-affine fresh-bank boundary left by account01/B16, while retaining original-coordinate product provenance.

# account04/B16 r1 — heavy-coordinate transverse fresh-bank closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260923T121701Z-account04-B16-QFORM-r1`  
**Status:** NEW SUPPORTING TARGET-LEVEL THEOREM / ACCOUNT01 RESULT APPLIED / FULL QFORM OPEN.  
**Regularity:** absolute continuity and an essential density bound are proved in the stated class. Continuity is not asserted.

## 1. Source-bound input and the precise unpaid edge

Account01/B16 at commit `de540e741ccb54a9f6f849fadec76f4af188234d` proves a full-ambient lift when a fresh original-coordinate bank enters through one aggregate scalar, but leaves open arbitrary outside coupling into directions of that bank transverse to the reserved aggregate.

The analytic input used below is the orientation-free rank-two affine half-Riesz theorem at commit `e542b1a6ef471b329e4e88a6553e1aacb45acc1a`. In non-normalized form, if
\[
P=M X_I\in\mathbb R^2,\qquad \operatorname{rank}M=2,
\]
\(B\) is invertible symmetric, and \(\ell\) is an arbitrary affine vector on the whole \(I\)-bank, then
\[
\sup_w\mathbb E\left|P^TBP+\ell^TX_I-w\right|^{-1/2}
\le 128\,[\det(MM^T)|\det B|]^{-1/4}. \tag{1.1}
\]
No independence between the two coordinates of \(P\) is used.

## 2. New transverse-affine theorem

### Theorem `QFORM-HEAVY-FRESH-TRANSVERSE-CROSS-LIFT-v1`

Let \(I,J,K\) be disjoint original-coordinate banks. Put
\[
P=M X_I\in\mathbb R^2,\qquad V=n^T X_J,
\]
where \(\operatorname{rank}M=2\), \(\|n\|_2=1\), and for some physical coordinate \(j_*\in J\),
\[
|n_{j_*}|^2\ge \frac12. \tag{2.1}
\]
Let \(B\) be invertible symmetric \(2\times2\), \(\gamma\ne0\), \(R,S\) arbitrary matrices of compatible sizes, \(a\in\mathbb R^{|I|}\), \(r\in\mathbb R^{|K|}\), and \(C=C^T\). Define
\[
\begin{aligned}
Q={}&P^TBP+2X_I^TRX_K\\
&+\gamma\bigl[V+a^TX_I+r^TX_K\bigr]^2
+2X_J^TSX_K+X_K^TCX_K. \tag{2.2}
\end{aligned}
\]
For arbitrary independent cap-one input densities,
\[
\boxed{
\|p_Q\|_\infty
\le
\frac{128}{|n_{j_*}|\sqrt{|\gamma|}}\,
[\det(MM^T)|\det B|]^{-1/4}
\le
\frac{128\sqrt2}{\sqrt{|\gamma|}}\,
[\det(MM^T)|\det B|]^{-1/4}.
} \tag{2.3}
\]

This permits arbitrary outside bilinear coupling into every physical coordinate of the fresh bank \(J\). The coupling need not factor through \(V\).

### Proof

Condition first on the genuine outside original-coordinate bank \(X_K=z\). Write \(x=X_{j_*}\), \(y=X_{J\setminus\{j_*\}}\),
\[
n^TX_J=n_*x+T(y),\qquad d=2Sz,\qquad H=T(y)+a^TX_I+r^Tz.
\]
Next condition on \(y\), but not on \(X_I\) or \(x\). The entire \(x\)-dependent part is
\[
\gamma(n_*x+H)^2+d_*x.
\]
The exact completion
\[
\gamma(n_*x+H)^2+d_*x
=
\gamma n_*^2\left(x+\frac H{n_*}+
\frac{d_*}{2\gamma n_*^2}\right)^2
-\frac{d_*}{n_*}H-\frac{d_*^2}{4\gamma n_*^2} \tag{2.4}
\]
shows that, after the square is isolated, the remaining dependence on \(X_I\) is
\[
P^TBP+
\left(2Rz-\frac{d_*}{n_*}a\right)^TX_I+\text{constant}. \tag{2.5}
\]
Thus it is exactly a rank-two quadratic receiver with an arbitrary original-coordinate affine term.

For any cap-one density of \(x\), the change of variables through
\(u\mapsto \gamma n_*^2(u-u_0)^2+c\) gives the conditional density majorant
\[
p_{Q\mid X_I,y,z}(t)
\le
\frac1{|n_*|\sqrt{|\gamma|}}\,
|t-W(X_I,y,z)|^{-1/2}. \tag{2.6}
\]
Averaging (2.6) over \(X_I\) and applying (1.1) to (2.5) gives the first bound in (2.3), uniformly in \(y,z\). Averaging over the remaining conditioned product coordinates proves (2.3). Condition (2.1) gives the final inequality.

Only original coordinates were conditioned. The two projected receiver coordinates were never declared independent, and no conditional projection-density supremum was introduced.

## 3. Concrete target-level application of account01/B16

Use the account01/B16 balanced shared-bank construction. Let
\[
L=m^{-1/2}\sum X_j,\quad
U=m^{-1/2}\sum\varepsilon_jX_j,\quad
T=m^{-1/2}\sum\tau_jX_j,
\]
with the sign vectors mutually orthogonal, and put
\[
Y=X_0+\eta(L+\rho T),\qquad
s^2=1+\eta^2(1+\rho^2),
\]
where \(\eta^2(1+\rho^2)<1/63\) and \(0<\delta\le1/16\).

Take a disjoint fresh bank \(X_J\) and any unit \(n\) satisfying (2.1), set \(V=n^TX_J\), and define
\[
Q_0=4\delta Y^2+8YU+4V^2. \tag{3.1}
\]
Now add an arbitrary disjoint outside bank \(Z\in\mathbb R^q\):
\[
Q_{\rm tr}
=
Q_0+2X_I^TRZ+2X_J^TSZ+Z^TCZ, \tag{3.2}
\]
where \(R,S,C\) are arbitrary. In particular, the \(J\)-to-\(Z\) coupling \(S\) may have components orthogonal to \(n\), which was the explicit unpaid boundary in account01/B16.

Apply Theorem 2 with
\[
P=(Y/s,U),\quad MM^T=I_2,\quad
B=4\begin{pmatrix}\delta s^2&s\\s&0\end{pmatrix},
\quad |\det B|=16s^2,\quad \gamma=4.
\]
Then
\[
\boxed{
\|p_{Q_{\rm tr}}\|_\infty
\le \frac{32}{|n_{j_*}|\sqrt s}
\le \frac{32\sqrt2}{\sqrt s}
\le 32\sqrt2
=45.2548339959\ldots .
} \tag{3.3}
\]

This is an actual use of account01/B16's physical construction and determinant ledger.

## 4. Actual matrix spectrum

Let \(y,u,n\) denote the physical coefficient vectors of \(Y,U,V\). The three vectors \(y/s,u,n\) are orthonormal original-coordinate vectors. The compression of the full coefficient matrix of (3.2) to their span is exactly
\[
\Gamma=
4\begin{pmatrix}
\delta s^2&s&0\\
s&0&0\\
0&0&1
\end{pmatrix}. \tag{4.1}
\]
The arbitrary \(R,S,C\) terms vanish under this compression because one leg lies in the outside bank. The eigenvalues of the \(2\times2\) block are
\[
2\left(\delta s^2\pm\sqrt{\delta^2s^4+4s^2}\right), \tag{4.2}
\]
and the third is \(4\). Hence there are two positive eigenvalues at least \(4\) and one negative eigenvalue with magnitude
\[
2\left(\sqrt{\delta^2s^4+4s^2}-\delta s^2\right)
=\frac{8s^2}{\sqrt{\delta^2s^4+4s^2}+\delta s^2}>1. \tag{4.3}
\]
The last inequality follows already from \(s\ge1\), \(\delta\le1/16\), and \(s^2<64/63\). By Poincare separation/min-max, the full symmetric matrix of (3.2) has at least three eigenvalues of absolute value at least one, for every ambient dimension and arbitrary \(R,S,C\).

Thus (3.3) is a genuine target-level class with all extra-spectrum signs and couplings retained.

## 5. Scope boundary

The full conjecture remains open. The new theorem closes the transverse fresh-bank coupling edge only when the reserved direction has a physical coefficient of squared size at least \(1/2\). The diffuse case
\[
\max_{j\in J}|n_j|^2<\frac12
\]
remains unpaid: conditioning on one coordinate then loses the aggregate scale, while a bare two-dimensional marginal cap along a parabola is not a valid substitute. The genuinely shared/null-Rayleigh case with no disjoint fresh bank also remains open.

Continuity is separate and is not claimed here.
