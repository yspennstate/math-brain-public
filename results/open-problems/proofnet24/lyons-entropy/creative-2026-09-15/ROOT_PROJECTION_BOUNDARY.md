# A comparable-scale interior tube at every fully supported rank-one three-site projection

Root constructive proof, 2026-09-15. This treats a simultaneous approach to eigenvalues zero and one, distinct from the surviving-eigenvalue-in-(0,1) theorem in ROOT_RANK_ONE_BOUNDARY.md. No full Lyons claim or historical priority is asserted.

## The theorem

Let \(u\in\mathbb C^3\) be a unit vector with every coordinate nonzero, \(Q=uu^*\), and \(P=I-Q\). Fix \(h>0\) and a supported covariance shape \(J=PJP>0\) on \(u^\perp\). Then
\[
K_\epsilon=(1-h\epsilon)Q+\epsilon J
\]
has negative-definite full Hermitian entropy Hessian for every sufficiently small positive \(\epsilon\). The result is uniform on compact families where the three \(|u_i|\), \(h\), and the two eigenvalues of the supported \(J\) have positive lower and finite upper bounds. Thus all three distances to the limiting spectral endpoints may vanish together at comparable rates. Complementation gives the rank-two projection version. Arbitrarily separated rates are not included.

## 1. Coordinates and the finite dark-mode inequality

Use the fixed occupation-preserving diagonal gauge making \(u_i>0\). Use the tangent coordinates from ROOT_RANK_ONE_BOUNDARY.md:
\[
A=aQ+uv^*+vu^*+B,\qquad
B=S+i b\begin{pmatrix}0&1\\-1&0\end{pmatrix}
\]
in a real orthonormal basis of \(u^\perp\), with \(S\) real symmetric and \(v\perp u\). Write \(q_i=u_i^2\), \(r_i=1-q_i\), \(d=\det J\), and for the complementary pair \(\{j,k\}=[3]\setminus\{i\}\),
\[
w_i=u_k e_j-u_j e_k,\qquad c_i=w_i^*Jw_i.
\]
The vectors satisfy \(\|w_i\|^2=r_i\) and \(\sum_iw_iw_i^*=P\). Define
\[
\Lambda_J=\sum_i r_i\log c_i-\log d-\sum_iq_i\log q_i.
\tag{1}
\]
The scalar spectral Jensen inequality for the concave logarithm gives
\[
\log\frac{w_i^*Jw_i}{r_i}
\ge\frac{w_i^*(\log J)w_i}{r_i}.
\]
Multiply by \(r_i\), sum, and use the frame identity to obtain
\[
\sum_i r_i\log(c_i/r_i)\ge\operatorname{tr}\log J=\log d.
\]
Consequently
\[
\boxed{\Lambda_J\ge\Lambda(q):=
\sum_i(1-q_i)\log(1-q_i)-\sum_iq_i\log q_i>0.}\tag{2}
\]
The strict inequality has the elementary exact representation already proved in C019:
\[
\Lambda(q)=\int_0^{q_1}\int_0^{q_2}\int_0^{q_3}
\frac{da\,db\,dc}{(a+b+c)^2}\ge q_1q_2q_3>0.
\]
This supplies the one finite tangent gap left after the leading Fisher and logarithmic terms are separated.

## 2. All nine modes

Put \(L=\log(1/\epsilon)\). At the projection limit, only the three singleton atoms are positive, with probabilities \(q_i\). The empty and pair atoms have expansions
\[
p_\varnothing=h\epsilon+O(\epsilon^2),\qquad
p_{[3]\setminus\{i\}}=\epsilon c_i+O(\epsilon^2),
\]
and the triple atom is exactly \((1-h\epsilon)\epsilon^2d\).
Their affine first derivatives satisfy
\[
Dp_\varnothing[A]=-a+O(\epsilon\|A\|_F),\qquad
Dp_{jk}[A]=w_i^*S w_i+O(\epsilon\|A\|_F).
\]
The binary-quadratic argument in ROOT_RANK_ONE_BOUNDARY.md proves
\[
F_J(S)=\sum_i\frac{(w_i^*S w_i)^2}{c_i}\ge\lambda\|S\|_F^2
\]
for some \(\lambda>0\), uniformly on the stated compact families. Thus the four leading Fisher terms give
\[
\mathrm{FI}\ge\frac{a^2}{2h\epsilon}
+\frac{F_J(S)}{2\epsilon}-C\epsilon\|A\|_F^2,
\tag{3}
\]
after dropping the remaining nonnegative Fisher terms when convenient.

At the projection \(Q\), the determinant identities give
\[
\begin{aligned}
p_\varnothing''&=2a\operatorname{tr}S-2\|v\|^2,\\
p_{jk}''&=2\det A_{jk}-2\det B,\\
p_{123}''&=2\det B.
\end{aligned}
\]
Combining one logarithm \(-L\) from the empty atom, three from the pairs, and \(-2L\) from the triple yields the exact leading logarithmic form
\[
4L\left[a\operatorname{tr}S-\|v\|^2\right].\tag{4}
\]
All coefficient errors are \(O(\epsilon(1+L)\|A\|_F^2)\).

Collect the finite logarithmic terms and the singleton Fisher terms in a bounded quadratic form \(R(A)\). Drop the nonnegative triple Fisher term entirely; doing so gives a valid upper bound even when its limit on \(b\) is nonzero. On the pure imaginary supported direction, \(a=v=S=0\), one has
\[
\det A_{jk}=-b^2q_i,\qquad \det B=-b^2.
\]
The singleton second derivatives tend to \(-2b^2q_i\), their scores tend to zero, and the empty second derivative tends to zero. The pair and triple constants then give exactly
\[
\boxed{R(i bJ_0)=-2\Lambda_J b^2,}\tag{5}
\]
where \(J_0\) is the standard real skew matrix in the supported basis. Notice the essential singleton contribution \(2b^2\sum_iq_i\log q_i\); omitting it would give the wrong sign. All other constant terms are bounded on compact families.

Together (3)-(5) imply
\[
H''\le-\frac{a^2}{2h\epsilon}-\frac{F_J(S)}{2\epsilon}
+4L[a\operatorname{tr}S-\|v\|^2]+R(A)
+O(\epsilon(1+L)\|A\|_F^2).
\tag{6}
\]
This inequality can also be derived by direct substitution in the exact three-site atom formulas; no finite-difference approximation is involved.

## 3. Closing the bound

By (2), (5), boundedness, and Young's inequality there is a finite \(C_1\) such that
\[
R(A)\le-\Lambda_J b^2+C_1(a^2+\|S\|_F^2+\|v\|^2).
\]
Also \(4L|a\operatorname{tr}S|\le 2\sqrt2 L(a^2+\|S\|_F^2)\). The negative terms of order \(1/\epsilon\) dominate this logarithmic expression and every bounded contribution in \(a,S\). The negative \(-4L\|v\|^2\) dominates the bounded mixing terms. The error tends to zero and can be absorbed in the strictly positive uniform lower bound for \(\Lambda_J\).

Hence there is \(\epsilon_0>0\) such that for \(0<\epsilon<\epsilon_0\),
\[
\boxed{H''\le-\frac{a^2}{4h\epsilon}
-\frac{\lambda}{4\epsilon}\|S\|_F^2
-2L\|v\|^2-\frac{\Lambda_J}{2}b^2<0\quad(A\ne0).}
\]
The proof accounts for all nine real tangent modes: four at Fisher scale \(1/\epsilon\), four at logarithmic scale, and one with the positive finite gap (2). The uniformity and conical-tube interpretation follow from the explicit positive leading coefficients and compactness, as in the preceding rank-one boundary note. No claim is made that the tubes exhaust every approach to the spectral boundary.

## Finite diagnostic

The second diagnostic in ROOT_RANK_ONE_BOUNDARY_check.py uses u=(1,2,2)/3, h=0.8, and a fixed complex supported J. At epsilon=10^-3,10^-6,10^-12 the largest scaled Hessian eigenvalues are approximately -0.342322,-0.341908,-0.341908. The finite dark-mode curvatures are approximately -1.22436,-1.20497,-1.20493. ROOT_PROJECTION_BOUNDARY_results.json retains these finite floating-point results; the analytic proof above supplies the universal restricted theorem.
