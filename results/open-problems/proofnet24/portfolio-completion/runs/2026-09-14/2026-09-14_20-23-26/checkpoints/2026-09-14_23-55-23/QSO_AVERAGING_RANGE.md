# Global averaged convergence beyond the half step

Parent derivation, 14 September 2026. This note extends the [explicit half-step contraction](QSO_HALF_STEP_EXPLICIT.md). It uses the operator norm proved there. [Independent audit046](agents/046.md) verified the perturbative extension and the proof for every positive weight below one half. The stronger [global range through 0.51](QSO_GLOBAL_051.md) also passed that audit. No optimality or historical-novelty claim is made.

Let \(V\) be any strictly non-Volterra quadratic stochastic operator on four types, with symmetric parental coefficients, and put
\[
T_\lambda=(1-\lambda)I+\lambda V,\qquad
0<\lambda\le\frac{251}{500}.
\]
All allowed coefficients may vanish. Let \(p\) be its unique fixed point, as proved in [the main note](FOUR_TYPE_UNIQUENESS.md).

**Theorem.** Every orbit of \(T_\lambda\) in the closed simplex converges to \(p\). For \(1/2\le\lambda\le251/500\), put
\[
e=\lambda-\frac12,\qquad R=\frac{7967}{8192}.
\]
Then
\[
\|T_\lambda^n x-p\|_1
\le 2(R+13e)^{n-3},\qquad n\ge3,
\]
and
\[
R+13e\le\frac{1022499}{1024000}<1.
\]
For \(0<\lambda<1/2\), a separate explicit bound is given in Section 3. The endpoint \(251/500\) is a sufficient global range, not a proposed sharp threshold.

## 1. Quantitative comparison of the third images

For a vector \(m\), define the matrix
\[
A(m)_{kj}=\sum_i P_{ij,k}m_i.
\]
When \(m\) is a probability vector, \(A(m)\) is column-stochastic. For any real vector \(w\), its linear dependence on \(w\) gives the ambient norm bound
\[
\|A(w)\|_{1\to1}\le\|w\|_1.
\tag{1}
\]
Indeed, every column is a linear combination, with coefficients \(w_i\), of probability vectors. The exact quadratic identity
\[
V(x)-V(y)=2A((x+y)/2)(x-y)
\tag{2}
\]
implies that \(V\) is globally 2-Lipschitz on the simplex. For \(0\le\lambda\le1\), \(T_\lambda\) is consequently \((1+\lambda)\)-Lipschitz there.

Write \(T=T_{1/2}\). For \(e\ge0\),
\[
\|T_\lambda x-Tx\|_1=e\|V(x)-x\|_1\le2e.
\]
Starting from the same \(x\), the triangle inequality yields
\[
\|T_\lambda^{j+1}x-T^{j+1}x\|_1
\le(1+\lambda)\|T_\lambda^j x-T^j x\|_1+2e.
\]
Thus, uniformly over all initial points,
\[
\|T_\lambda^3x-T^3x\|_1
\le a_3:=2e\bigl[1+(1+\lambda)+(1+\lambda)^2\bigr].
\tag{3}
\]
For any two initial points \(x,y\), set
\[
m_\lambda=\frac{T_\lambda^3x+T_\lambda^3y}{2},\qquad
m_0=\frac{T^3x+T^3y}{2}.
\]
Equation (3) gives \(\|m_\lambda-m_0\|_1\le a_3\).

## 2. Contraction on the perturbed invariant image

Let \(E=\{z:\sum_i z_i=0\}\). The full column-cut argument in the half-step note proves
\[
\left\|\left(\frac12 I+A(m_0)\right)\big|_E\right\|_{1\to1}
\le R.
\tag{4}
\]
This is a norm bound on every vector in \(E\), not merely on \(T^3x-T^3y\).

The corresponding difference matrix for \(T_\lambda\) is
\[
B_\lambda(m_\lambda)=(1-\lambda)I+2\lambda A(m_\lambda).
\]
Exactly,
\[
B_\lambda(m_\lambda)-\left(\frac12I+A(m_0)\right)
=e\bigl(2A(m_\lambda)-I\bigr)+A(m_\lambda-m_0).
\tag{5}
\]
Since \(m_\lambda\) is a probability vector, the first matrix in parentheses has ambient norm at most 3. Equations (1), (3), (4) and (5) therefore give
\[
\|B_\lambda(m_\lambda)|_E\|_{1\to1}
\le R+3e+a_3\le R+13e.
\tag{6}
\]
For the last inequality, \(1+\lambda\le751/500\), and
\[
3+2\left[1+\frac{751}{500}+\left(\frac{751}{500}\right)^2\right]
=\frac{1564501}{125000}<13.
\]
Also
\[
1-R-\frac{13}{500}=\frac{1501}{1024000}>0.
\tag{7}
\]

The set \(S_\lambda=T_\lambda^3(\Delta_3)\) is compact, nonempty and invariant: \(T_\lambda(S_\lambda)=T_\lambda^4(\Delta_3)\subseteq S_\lambda\), since \(T_\lambda(\Delta_3)\subseteq\Delta_3\). Every pair of points in \(S_\lambda\) has representations used above. Its difference lies in \(E\), and (2) shows that applying \(T_\lambda\) multiplies that difference by \(B_\lambda(m_\lambda)\). Thus (6) is a contraction estimate on \(S_\lambda\), even though this set need not be convex.

The fixed point \(p\) belongs to \(S_\lambda\), and the simplex has diameter 2 in \(\ell^1\). Iterating (6) after the first three steps proves the stated error bound. There is no appeal to global convergence from eigenvalues alone.

## 3. Every smaller positive averaging weight

Fix \(0<\lambda<1/2\), and put
\[
q=\max\{2/5,\lambda\}<1/2,\qquad
d=\lambda(3q-q^2-1)>0,
\]
\[
N=\left\lceil\frac{1-q}{d}\right\rceil,
\qquad L=1-\lambda(1-2q)<1.
\tag{8}
\]
The positivity of \(d\) follows from \(q\ge2/5\), since \(3(2/5)-(2/5)^2-1=1/25\), and \(3q-q^2-1\) is increasing on \([2/5,1]\).

Strict parent exclusion gives \(V_i(x)\le(1-x_i)^2\). Define
\[
f(u)=(1-\lambda)u+\lambda(1-u)^2.
\]
If all coordinates of \(x\) are at most \(r\in[q,1]\), convexity of \(f\) gives
\[
\max_i(T_\lambda x)_i\le\max\{f(0),f(r)\}
\le\max\{q,r-d\}.
\tag{9}
\]
Here \(f(0)=\lambda\le q\), while \(r-f(r)=\lambda(3r-r^2-1)\ge d\). Inductively, every orbit has maximum coordinate at most \(\max\{q,1-nd\}\) after \(n\) steps. Hence \(T_\lambda^N(\Delta_3)\subseteq K_q\), where \(K_q\) is the capped simplex.

Theorem 2 of the main note proves that \(K_q\) is invariant and that \(T_\lambda\) contracts there with factor \(L\), because \(q\ge2/5>(3-\sqrt5)/2\) and \(0<\lambda\le q<1/2\). Therefore
\[
\|T_\lambda^n x-p\|_1\le2L^{n-N},\qquad n\ge N.
\tag{10}
\]
Equations (6) and (10) cover all \(0<\lambda\le251/500\). The entrance bound (8) is intentionally simple and need not be the fastest bound for a particular weight. Unaveraged iteration can still be unstable or cyclic, as the explicit examples in the accompanying reports show.
