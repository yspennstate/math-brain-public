# Convergence in a larger zero-target basin

Let m>=d+1 and d>=1. Both layers of the linear network

\[
 f_{a,W}(x)=a^TWx,\qquad L_0(a,W)=\tfrac12\|W^Ta\|^2
\]

are trained by simultaneous full-batch gradient descent with step eta>0. This is the population square loss for x~N(0,I_d) and zero labels, or the empirical loss on x_j=sqrt(d)e_j with zero labels, averaged over the d examples. Put A=sqrt(eta)a and U=sqrt(eta)W. The exact scaled update is

\[
 A^+=A-Uv,\qquad U^+=U-Av^T,\qquad v=U^TA. \tag{1}
\]

Write Z=[A U], q=||A||^2, C=U^TU, c=||C||_op and h=||v||^2. For x in R^d define

\[
 K(x)=\begin{pmatrix}0&x^T\\x&0_{d\times d}\end{pmatrix}.
\]

Then Z^+=Z(I-K(v)), and ||K(x)||_op=||x||. The norm of Z as a parameter vector is its Frobenius norm.

## Theorem

Suppose

\[
 q_0<2,\qquad c_0<2,\qquad \operatorname{rank} Z_0=d+1,
 \qquad h_t\ne1\quad\hbox{for every finite }t. \tag{2}
\]

The iterates (1) converge in parameter space to a full-column-rank Z_infinity with U_infinity^TA_infinity=0. In particular the limit is a global minimizer. There is no condition q_0+c_0<2. No rate or upper bound 2 on endpoint sharpness is asserted.

If all entries of Z_0 have any joint law absolutely continuous with respect to Lebesgue measure, the rank and h_t conditions in (2) hold almost surely. Consequently almost every initialization in the entire open region q_0<2, c_0<2 converges to a global minimum. For independent N(0,tau^2) scaled entries this is the original initialization variance tau^2/eta, for every eta>0 with zero target.

### Monotonicity and summable residual squares

Direct multiplication of (1) gives

\[
 q^+=q-2h+v^TCv,\quad
 C^+=C-(2-q)vv^T,\quad
 v^+=(I-C-qI+hI)v. \tag{3}
\]

For the first identity expand ||A-Uv||^2 and use A^TUv=h. For the second expand (U-Av^T)^T(U-Av^T), using U^TA=v. For the third expand (U^T-vA^T)(A-Uv), again using A^TUv=h.

Let delta=2-c_0>0. If q<=q_0 and 0<=C<=C_0, the first two identities give

\[
 q^+\leq q-\delta h\leq q,\qquad 0\preceq C^+\preceq C. \tag{4}
\]

The lower bound C^+>=0 holds because C^+=U^{+T}U^+. Since q_0<2, induction proves (4) at every time. Therefore

\[
 \sum_{t=0}^\infty h_t\leq q_0/\delta<\infty,
 \quad h_t\longrightarrow0,\quad
 ||Z_t||_F^2\leq M:=q_0+\operatorname{tr}C_0. \tag{5}
\]

Also h_t<=q_t c_t<=q_0 c_0<4, so ||v_t||<2. The scalar q_t converges. Each quadratic form x^TC_tx decreases to a limit. Applying polarization to the coordinate vectors shows that C_t converges entrywise, hence in norm. Equivalently its total variation in operator norm is bounded by sum (2-q_t)h_t.

### A positive determinant without the bound h<1

Let G_t=Z_t^TZ_t. The eigenvalues of K(v_t) are ||v_t||, -||v_t|| and d-1 zeros. Taking determinants in G_{t+1}=(I-K(v_t))G_t(I-K(v_t)) gives

\[
 \det G_{t+1}=\det G_t(1-h_t)^2. \tag{6}
\]

Choose T such that h_t<=1/2 for all t>=T, using (5). By (2), det G_T>0. For 0<=x<=1/2, the integral identity log(1-x)=-int_0^x(1-u)^{-1}du gives log(1-x)>=-2x. Consequently for t>=T,

\[
 \det G_t\geq \det G_T\exp\left(-4\sum_{j=T}^\infty h_j\right)>0. \tag{7}
\]

The finitely many positive determinants before T have a positive minimum. Let D>0 be the smaller of that minimum and the right side of (7); if T=0 use just the right side. Then det G_t>=D for every t. All eigenvalues of G_t are bounded above by tr G_t<=M. It follows that

\[
 G_t\succeq\mu I_{d+1},\qquad \mu=D/M^d>0, \tag{8}
\]

because det G_t<=lambda_min(G_t) M^d. Principal submatrices give q_t>=mu and C_t>=mu I_d. Thus, for

\[
 H_t=C_t+q_t I_d,\qquad \gamma=2\mu,
\]

one has

\[
 \gamma I_d\preceq H_t\preceq (q_0+c_0)I_d\prec4I_d. \tag{9}
\]

This lower bound, rather than an upper bound below 2, is the ingredient needed for parameter convergence.

### A corrected parameter matrix

The changes in H_t satisfy

\[
 H_{t+1}-H_t=-(2-q_t)v_tv_t^T-(2h_t-v_t^TC_tv_t)I_d.
\]

Both terms on the right are negative semidefinite. Their norms are at most 2h_t each, so

\[
 ||H_{t+1}-H_t||\leq4h_t. \tag{10}
\]

Define w_t=H_t^{-1}v_t. The inverse identity gives

\[
 ||H_{t+1}^{-1}-H_t^{-1}||\leq4h_t/\gamma^2. \tag{11}
\]

Using v_{t+1}=(I-H_t+h_tI)v_t, a direct rearrangement gives the exact equality

\[
 \begin{split}
 w_{t+1}-w_t+v_t
 ={}&(H_{t+1}^{-1}-H_t^{-1})v_t\\
 &+H_{t+1}^{-1}(H_{t+1}-H_t)v_t
   +h_tH_{t+1}^{-1}v_t.
 \end{split} \tag{12}
\]

By (9)--(11), with B=4/gamma^2+5/gamma,

\[
 ||w_{t+1}-w_t+v_t||\leq B h_t||v_t||. \tag{13}
\]

Furthermore (3), (5) and (9) imply

\[
 ||v_{t+1}||\leq(1+||H_t||+h_t)||v_t||\leq9||v_t||,
 \qquad ||w_{t+1}||\leq9||v_t||/\gamma. \tag{14}
\]

Set F_t=Z_t(I-K(w_t)). Linearity of K and Z_{t+1}=Z_t(I-K(v_t)) yield

\[
 \begin{split}
 F_{t+1}-F_t
 ={}&-Z_tK(v_t+w_{t+1}-w_t)\\
 &+Z_tK(v_t)K(w_{t+1}).
 \end{split} \tag{15}
\]

Taking Frobenius norms, and using ||Z_t||_F<=sqrt(M), ||v_t||<=2 and h_t=||v_t||^2, gives

\[
 ||F_{t+1}-F_t||_F
 \leq\sqrt M(2B+9/\gamma)h_t. \tag{16}
\]

By (5), these increments are summable, hence F_t converges. At the same time

\[
 ||Z_t-F_t||_F\leq \sqrt M||w_t||
 \leq\sqrt M||v_t||/\gamma\longrightarrow0. \tag{17}
\]

It follows that Z_t converges. Continuity and (5) give U_infinity^TA_infinity=0. Passing to the limit in (8) gives full column rank at the limit. This proves the deterministic assertion. More explicitly, (16)--(17) give the tail bound

\[
 ||Z_t-Z_\infty||_F
 \leq \sqrt M\left[(2B+9/\gamma)\sum_{j=t}^\infty h_j
                +||v_t||/\gamma\right]. \tag{18}
\]

This bound does not assert summability of the original parameter increments.

### The exceptional set has measure zero

For m>=d+1, one (d+1)-row square minor of Z_0 is a nonzero polynomial in its entries. The rank-deficient set is contained in its zero set and has Lebesgue measure zero. For each fixed finite t, the entries of Z_t are polynomials in the entries of Z_0, by induction in (1). Thus h_t-1 is a polynomial. At Z_0=0 every iterate is zero and h_t-1=-1, so this polynomial is not identically zero. Its zero set has measure zero.

For completeness, the zero set of a nonzero real polynomial has measure zero by induction on the number of variables. In one variable there are finitely many roots. In higher dimension, regard it as a polynomial in the last variable. Outside the common zero set of all coefficient polynomials it has finitely many roots on each fiber; the exceptional coefficient set has measure zero by the induction hypothesis applied to one nonzero coefficient. Fubini on bounded boxes completes the argument. Taking a countable union over t and adding the rank-deficient set proves the almost-sure assertion. No assumption that the update map is a diffeomorphism is used.

## A nonstationary full-rank example with supercritical endpoint

Use the first two standard coordinate vectors in R^m and set

\[
 A_0=(4/3)e_1+(1/3)e_2,\qquad
 U_{0,1}=(52/51)e_1+(47/51)e_2.
\]

For 2<=j<=d put U_{0,j}=(1/2)e_{j+1}. Empty extra columns are allowed when d=1. The first two columns have determinant

\[
 (4/3)(47/51)-(1/3)(52/51)=8/9\ne0,
\]

and the remaining columns are independent and orthogonal to their span. Thus Z_0 has full augmented rank. Direct dot products give

\[
 q_0=17/9,\qquad
 C_0=\operatorname{diag}(17/9,1/4,\ldots,1/4),\qquad
 v_0=(5/3,0,\ldots,0)^T.
\]

In particular q_0,c_0<2 but q_0+c_0=34/9>2. One step of (1) gives

\[
 A_1=-(56/153)e_1-(184/153)e_2,\qquad
 U_{1,1}=-(184/153)e_1+(56/153)e_2.
\]

Their dot product is zero and both squared norms equal 128/81. The extra columns remain unchanged. Therefore v_1=0 and all subsequent iterates are equal to Z_1. Neither h_0=25/9 nor the later h_t=0 equals 1. The determinant of the first two columns at time 1 is -128/81, also nonzero, independently confirming rank preservation.

At any zero-residual point, the parameter Hessian is J^TJ for

\[
 J(\alpha,V)=U^T\alpha+V^TA,
 \qquad JJ^T=C+qI_d.
\]

The nonzero eigenvalues of J^TJ and JJ^T coincide: if JJ^Tx=lambda x with lambda>0, then J^Tx is a nonzero eigenvector of J^TJ with the same eigenvalue, and conversely. Hence at the example's endpoint the scaled sharpness is

\[
 q_1+\lambda_{\max}(C_1)=256/81>2. \tag{19}
\]

In the original parameters it is 256/(81 eta). Indeed L_0(eta^{-1/2}A,eta^{-1/2}U)=eta^{-2}L_0(A,U), and its Hessian in (a,W) is eta^{-1} times the Hessian in (A,U). The example embeds in m=16,d=8 with all 144 parameters trainable.

This example belongs to a proper algebraic set: it lands exactly at zero residual after one step. In particular it does not imply any positive Gaussian probability of a supercritical endpoint. It does show that (2), including preservation of full rank, cannot imply a universal endpoint bound at or below 2. Its loss drops to zero in one step; it is not an example of a sustained edge regime.

## Scope

The earlier basin required q_0+c_0<2 and obtained an eventual geometric rate and small-nonzero-target persistence. The theorem here proves almost-sure parameter convergence on the larger region q_0<2, c_0<2, for zero target only. It permits h_t>1 and does not require any upper output-spectrum gap below 2. It does not extend the nonzero-target persistence or the endpoint-probability bound to this whole region. Determining the distribution of limiting sharpness under a nonsingular Gaussian law remains necessary to answer the edge-entry question. No conclusion about edge residence follows from parameter convergence.
