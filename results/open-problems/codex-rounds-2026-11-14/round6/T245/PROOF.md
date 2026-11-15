# A finite depth jet for the first learning-rate correction

This concerns the scalar-identity deep-linear model of the preceding reports. The size limit is taken first, and the learning rate then tends to zero on a fixed training interval. All statements are conditional on a fixed initial gain S>0. They do not concern independent Gaussian weight matrices or ReLU gates.

## 1. The preceding equations

Fix t>0, an active dimension d, a unit readout e, data (x_i,y_i), and positive weights alpha_i summing to one. At continuous training time tau put

\[
r_i=b+e^TPx_i-y_i,\qquad h=\sum_i\alpha_i r_i,
\qquad g=\sum_i\alpha_i r_ix_i,\qquad v=P^Te.
\]

The balanced endpoint trajectory from round 4 satisfies

\[
\dot P=f(P,b)=-tP\int_0^1 A(z)^{-1}vg^TA(z)\,dz,
\quad \dot b=-h,\quad P(0)=SI,\quad b(0)=0,
\tag{1}
\]
\[
H=P^TP/S^2,\qquad K=\log H,\qquad A(z)=e^{zK}.
\]

This trajectory is global and invertible at every finite time. Here K denotes a matrix logarithm; the full neural tangent kernel is denoted Theta below.

Round 5 expresses the first learning-rate correction through a symmetric depth field J:

\[
\dot J=R^TJ+JR-tN,\qquad J(0,z)=0,
\tag{2}
\]
\[
R(z)=-t\int_0^z e^{-aK}vg^Te^{aK}\,da,
\tag{3}
\]
\[
N(z)=(g^Te^{zK}g)vv^T
 -(v^Te^{-zK}v)e^{zK}gg^Te^{zK}.
\tag{4}
\]

Transpose in complex depth means transpose, without complex conjugation. On real depth all matrices in (1)--(4) are real.

For a symmetric source J, define W by the Dirichlet problem

\[
W''=W'K+KW'-KWK+tJ,\qquad W(0)=W(1)=0.
\tag{5}
\]

The correction functionals are

\[
\begin{split}
\mathcal F[J]&=-tP\int_0^1\left\{
 A^{-1}vg^TW-A^{-1}WA^{-1}vg^TA\right\}\,dz,\\
\mathcal M[J]&=t\int_0^1\left\{
 (v^TA^{-1}v)W-(v^TA^{-1}WA^{-1}v)A\right\}\,dz,\\
\mathcal B[J]&=-t\int_0^1v^TA^{-1}WA^{-1}v\,dz.
\end{split}
\tag{6}
\]

Let X(z)=-A(z)^{-1}vg^TA(z), and let

\[
\mathcal T=t^2P\int_{0<a<c<1}X(c)X(a)\,da\,dc.
\]

The endpoint sensitivity (p,beta) solves

\[
\begin{split}
\dot p&=Df[p,\beta]+\mathcal F[J]+\mathcal T
                    -\tfrac12Df[f,-h],\\
\dot\beta&=-Dh[p,\beta]+\tfrac12Dh[f,-h],
\qquad (p,\beta)(0)=0.
\end{split}
\tag{7}
\]

The full balanced kernel coefficients are

\[
M_0(P)=t\int_0^1(v^TA^{-1}v)A\,dz,
\qquad B_0(P)=t\int_0^1v^TA^{-1}v\,dz.
\tag{8}
\]

At actual discrete training nodes tau_k=k eta<=T, round 5 proves, uniformly in k,

\[
\begin{split}
P_k^\eta&=P+\eta p+O_T(\eta^2),\qquad
b_k^\eta=b+\eta\beta+O_T(\eta^2),\\
M_k^\eta&=M_0(P)+\eta\{DM_0(P)[p]+\mathcal M[J]\}
                                      +O_T(\eta^2),\\
B_k^\eta&=B_0(P)+\eta\{DB_0(P)[p]+\mathcal B[J]\}
                                      +O_T(\eta^2).
\end{split}
\tag{9}
\]

For inputs x=x_E+x_perp the full kernel is

\[
\Theta(x,x')=1+x_E^TMx'_E+B\langle x_\perp,x'_\perp\rangle.
\tag{10}
\]

## 2. Statement of the finite approximation

Use the Frobenius norm for matrix fields and the spectral norm for K and multiplication bounds. For a nonnegative integer m, evolve symmetric matrices j_0,...,j_m as follows. All coefficients below depend only on the endpoint trajectory (1).

Put T_0=vg^T and ad_K(D)=KD-DK. Define

\[
r_0=0,\qquad
r_a=-\frac{t(-1)^{a-1}}{a!}\operatorname{ad}_K^{a-1}(T_0)
\quad (a\ge1).
\tag{11}
\]

For q>=0 set

\[
\alpha_q=\frac{g^TK^qg}{q!},\qquad
\beta_q=\frac{(-1)^qv^TK^qv}{q!},
\tag{12}
\]
\[
D_0=gg^T,\qquad D_q=\frac{KD_{q-1}+D_{q-1}K}{q}
\quad(q\ge1),
\tag{13}
\]
\[
n_q=\alpha_q vv^T-\sum_{a=0}^q\beta_aD_{q-a}.
\tag{14}
\]

The finite system is

\[
\boxed{\displaystyle
\dot j_q=\sum_{a=1}^q
 \left(r_a^Tj_{q-a}+j_{q-a}r_a\right)-tn_q,
\qquad j_q(0)=0,\quad 0\le q\le m.}
\tag{15}
\]

An empty sum is zero. Thus j_0 has no transport term, and each later equation uses only earlier j's. Define

\[
J_m(\tau,z)=\sum_{q=0}^m j_q(\tau)z^q.
\tag{16}
\]

Compute W_m from (5) with source J_m, and replace J by J_m in (6),(7). Denote the resulting sensitivity by (p_m,beta_m). Define the approximation to discrete observations by

\[
\begin{split}
\widehat P_m&=P+\eta p_m,\qquad
\widehat b_m=b+\eta\beta_m,\\
\widehat M_m&=M_0(P)+\eta\{DM_0(P)[p_m]+\mathcal M[J_m]\},\\
\widehat B_m&=B_0(P)+\eta\{DB_0(P)[p_m]+\mathcal B[J_m]\}.
\end{split}
\tag{17}
\]

**Theorem.** Fix T<infinity and S>0. For every rho>1 there are finite constants C_T and M_rho, independent of m and eta, such that

\[
\sup_{0\le\tau\le T,\ 0\le z\le1}
 \|J(\tau,z)-J_m(\tau,z)\|_F
\le\frac{M_\rho}{\rho-1}\rho^{-m},
\tag{18}
\]
\[
\max_{k\eta\le T}
\left(\|P_k^\eta-\widehat P_m\|_F+
 |b_k^\eta-\widehat b_m|+
 \|M_k^\eta-\widehat M_m\|_F+
 |B_k^\eta-\widehat B_m|\right)
\le C_T\left(\eta^2+
 \eta\frac{M_\rho}{\rho-1}\rho^{-m}\right).
\tag{19}
\]

The approximations on the right are evaluated at tau_k. The coefficients j_q in (15) are the exact Taylor coefficients of J at z=0, even when the system is stopped at q=m. Consequently there is no feedback error from the discarded coefficients.

For example, take rho=2 and

\[
m(\eta)=\max\left(0,\left\lceil
 \log_2(M_2/\eta)\right\rceil\right)
\tag{20}
\]

when M_2>0. This gives uniform O_T(eta^2) error in (19). If M_2=0, all the j_q vanish and m=0 suffices. The number of evolving real coordinates is

\[
2(d^2+1)+(m+1)d(d+1)/2.
\tag{21}
\]

There is no evolving depth field in this finite approximation. The integrals and the boundary solve are instantaneous functions of its matrices. The theorem does not assert that a fixed finite m gives the exact correction, that m must grow at the stated rate, or that a different exact finite closure is impossible.

## 3. An explicit analytic bound

Let ell_0=(1/2)sum_i alpha_i r_i(0)^2. Set

\[
k_*=2\sqrt{tT\ell_0},\qquad
V=S\exp(\sqrt{tT\ell_0}),\qquad
G=\sqrt{2\ell_0\sum_i\alpha_i\|x_i\|^2}.
\tag{22}
\]

The earlier singular-value and loss bounds give, throughout [0,T],

\[
\|K\|_2\le k_*,\quad \|P\|_2,\|v\|\le V,\quad \|g\|\le G.
\tag{23}
\]

For the last inequality, apply Cauchy--Schwarz to sum alpha_i r_i x_i and use sum alpha_i r_i^2<=2ell_0. The first bound follows by taking the logarithm of each eigenvalue of P^TP/S^2.

For complex depth |z|<=rho, the power series for the matrix exponential gives

\[
\|e^{\pm zK}\|_2\le e^{\rho k_*}.
\]

Integrating (3) along the straight segment from 0 to z and bounding the two terms in (4) yields

\[
\|R(z)\|_2\le r_\rho:=t\rho VG e^{2\rho k_*},
\tag{24}
\]
\[
\|N(z)\|_F\le n_\rho:=V^2G^2
 (e^{\rho k_*}+e^{3\rho k_*}).
\tag{25}
\]

For example, ||vv^T||_F=||v||^2, and
|v^Te^{-zK}v| ||e^{zK}gg^Te^{zK}||_F
is at most V^2G^2 e^{3rho k_*}. These estimates hold for the complex spectral and Frobenius norms; no positivity in complex depth is needed.

The integral equation for (2) gives

\[
\|J(\tau,z)\|_F\le
 \int_0^\tau(2r_\rho\|J(s,z)\|_F+tn_\rho)\,ds.
\]

Iterating this scalar inequality, or integrating its constant-coefficient comparison equation, gives the valid bound

\[
\boxed{M_\rho=tTn_\rho e^{2Tr_\rho}.}
\tag{26}
\]

It is generally a large bound, not a proposed practical stopping criterion. It suffices for a uniform truncation theorem. It also covers T=0 or G=0 with M_rho=0.

To justify analyticity, on every compact complex depth disk use Picard iteration for (2). R and N are entire in z by the exponential series and the straight-segment integral. On |z|<=rho, (24)--(25) bound every Picard iterate and give uniform convergence of its integral series, whose successive terms are bounded by a constant times (2r_rho T)^a/a!. Each iterate is holomorphic in z, and the uniformly convergent series is holomorphic in the interior of every disk. Thus J(tau,z) is entire for every tau, with the bound (26) uniform in tau. The time integral equation and the same bounds also justify differentiating its Cauchy coefficient integrals in tau.

## 4. Exact coefficient equations and truncation

Expand the conjugation in (3). Its derivative with respect to z is minus ad_K applied to the conjugated matrix, so its exponential series is

\[
e^{-zK}T_0e^{zK}
=\sum_{q=0}^\infty\frac{(-z)^q}{q!}
 \operatorname{ad}_K^q(T_0).
\]

Integrating term by term gives precisely R(z)=sum_{a>=1}r_a z^a with (11). The series are absolutely and uniformly convergent on each compact disk, so this integration is justified.

The first scalar factor of (4) has coefficients alpha_q. The scalar factor in its second term has coefficients beta_q. If D(z)=e^{zK}gg^Te^{zK}, then D'=KD+DK and D(0)=gg^T. Matching coefficients gives (13). Multiplying the scalar and matrix series in the second term of (4) now gives (14). This proves N(z)=sum_{q>=0}n_q z^q.

Let j_q be the Cauchy coefficient of J. Matching coefficients in (2), or taking their Cauchy integrals, gives (15). In particular, r_0=0 makes this system strictly triangular in the j's. The first m+1 equations are the same for every larger truncation. Uniqueness of these finite linear inhomogeneous ODEs proves that a truncated computation produces the exact coefficients j_0,...,j_m.

The source n_q is symmetric, and (r_a^Tj+jr_a)^T equals itself for symmetric j. Thus all j_q are symmetric. No division by a spectral gap occurs in (11)--(15); coinciding eigenvalues require no separate convention.

Cauchy's integral formula on |z|=rho, together with (26), gives ||j_q(tau)||_F<=M_rho rho^{-q}. Therefore, for real z in [0,1],

\[
\|J-J_m\|_F\le M_\rho\sum_{q=m+1}^\infty\rho^{-q}
=\frac{M_\rho}{\rho-1}\rho^{-m}.
\]

This proves (18), including the factor and the exponent of rho.

## 5. Stability of the boundary solve

Write W=e^{zK/2}Ye^{zK/2}. Equation (5) becomes

\[
Y''-\tfrac14[K,[K,Y]]=t e^{-zK/2}Je^{-zK/2},
\qquad Y(0)=Y(1)=0.
\tag{27}
\]

In an orthonormal eigenbasis of K, each entry has scalar operator D^2-kappa_ij^2, with kappa_ij=|k_i-k_j|/2. Its Dirichlet Green function Gamma_kappa is nonpositive and satisfies

\[
|\Gamma_\kappa(z,a)|\le
 \min(z,a)(1-\max(z,a))=|\Gamma_0(z,a)|.
\tag{28}
\]

Here is a direct comparison argument. For nonnegative continuous source f, let u_kappa solve -u''+kappa^2 u=f with zero boundary values. A negative interior minimum contradicts its equation, so u_kappa>=0. Also - (u_0-u_kappa)''=kappa^2u_kappa>=0 with zero boundary values, hence u_0-u_kappa>=0 by the same minimum argument. Applying this to nonnegative sources concentrated near a and using continuity of the Green functions proves (28). Uniqueness follows by multiplying the zero-source equation by its solution and integrating. These arguments include kappa=0.

Let delta=sup_z ||J(z)-J_m(z)||_F at a fixed training time. The matrix with entries Gamma_kappa_ij(z,a) times a source matrix has Frobenius norm at most |Gamma_0(z,a)| times the source's Frobenius norm. Since

\[
\int_0^1|\Gamma_0(z,a)|\,da=z(1-z)/2\le1/8,
\]

equations (27)--(28), the triangle inequality under the integral, and (23) give

\[
\sup_z\|Y-Y_m\|_F\le(t/8)e^{k_*}\delta.
\]

Multiplication by the two e^{zK/2} factors gives

\[
\boxed{\sup_z\|W-W_m\|_F\le
 C_W\delta,\qquad C_W=(t/8)e^{2k_*}.}
\tag{29}
\]

The constant is independent of m. The value 1/8 is also obtained directly by solving u''=1, u(0)=u(1)=0: u=-z(1-z)/2.

## 6. Propagating the truncation error to the full kernel

On real depth, ||A||_2 and ||A^{-1}||_2 are at most e^{k_*}, and ||A||_F<=sqrt(d)e^{k_*}. Apply these bounds to each product in (6), using (29). One obtains

\[
\begin{split}
\|\mathcal F[J]-\mathcal F[J_m]\|_F
 &\le C_F\delta,
 &C_F&=tV^2G(e^{k_*}+e^{3k_*})C_W,\\
\|\mathcal M[J]-\mathcal M[J_m]\|_F
 &\le C_M\delta,
 &C_M&=tV^2(e^{k_*}+\sqrt d\,e^{3k_*})C_W,\\
|\mathcal B[J]-\mathcal B[J_m]|
 &\le C_B\delta,
 &C_B&=tV^2e^{2k_*}C_W.
\end{split}
\tag{30}
\]

For clarity, the two terms in the first bound use respectively
||P||_2 ||A^{-1}||_2 ||v|| ||g|| ||W-W_m||_F
and
||P||_2 ||A^{-1}||_2^2 ||W-W_m||_F ||v|| ||g|| ||A||_2.
The two terms in the second bound use
|v^TA^{-1}v|<=V^2e^{k_*}
and
|v^TA^{-1}(W-W_m)A^{-1}v|<=V^2e^{2k_*}||W-W_m||_F.

The difference between (7) and its truncated version solves a finite linear ODE with zero initial condition and forcing (F[J]-F[J_m],0). The coefficient matrix is continuous on [0,T], hence has a finite operator-norm bound L_T for the norm ||p||_F+|beta|. Its integral equation and the same scalar comparison used above give

\[
\sup_{\tau\le T}(\|p-p_m\|_F+|\beta-\beta_m|)
\le T e^{L_TT} C_F
 \frac{M_\rho}{\rho-1}\rho^{-m}.
\tag{31}
\]

The derivatives DM_0 and DB_0 are bounded along the compact, invertible endpoint path: the logarithm and exponential defining (8) are smooth there. Equations (30)--(31) therefore bound the difference between the exact first-order coefficients in (9) and those in (17) by a constant independent of m times M_rho rho^{-m}/(rho-1). Add the O_T(eta^2) remainder in (9) to obtain (19). The constants in the original remainder do not depend on m, since (9) is invoked only for its exact coefficient. This proves the theorem.

For test inputs with ||x||,||x'||<=R_x, (10) bounds the full kernel error by R_x^2 times the sum of the M and B errors. The output error is at most |b-bhat|+R_x||P-Phat||_F. Thus (19) controls both test outputs and the full test kernel on every bounded set of test inputs, including perpendicular directions.

## 7. Why this is a finite matrix system

For fixed m the evolving variables are P,b,p_m,beta_m and the symmetric matrices j_0,...,j_m. Equations (11)--(15) use only their present values and finite matrix operations. Reconstructing W_m does not add evolving variables.

One exact finite construction of the instantaneous boundary solve is useful. Set V_depth=W_m', introduce scalar depth variables xi_q(z)=z^q, and use

\[
W_m'=V_{\rm depth},\qquad
V_{\rm depth}'=V_{\rm depth}K+KV_{\rm depth}-KW_mK
                    +t\sum_{q=0}^m j_q\xi_q,
\]
\[
\xi_0'=0,\quad \xi_q'=q\xi_{q-1}\ (q\ge1),
\qquad \xi_0(0)=1,\quad \xi_q(0)=0\ (q\ge1).
\]

After vectorization this is a constant-coefficient homogeneous linear system of dimension 2d^2+m+1. Its solution is a matrix exponential. Set W_m(0)=0 and choose V_depth(0) to make W_m(1)=0. The linear map from V_depth(0) to the homogeneous W_m(1) is injective by the uniqueness proof in section 5; its domain and codomain both have dimension d^2, so it is invertible. A finite linear solve thus determines the boundary solution. The integrals in (6) are consequently well-defined functions of the finite state, just as the balanced integrals in (1),(8) are functions of P. Numerical quadrature for those functions is an evaluation choice, not an additional dynamical state.

## 8. Checks and limits

In the mandatory two-example benchmark t=S=1, e=e_1, x_1=e_1, x_2=e_2, y_1=y_2=1, alpha_i=1/2, one has initially K=0, v=e_1 and g=-e_2/2. Therefore

\[
\dot j_0(0)=-\tfrac14\operatorname{diag}(1,-1),
\qquad \dot j_q(0)=0\quad(q\ge1).
\]

Already m=0 therefore gives the correct leading small-time memory:

\[
W_m(\tau,z)=\tfrac18\tau z(1-z)\operatorname{diag}(1,-1)
 +O(\tau^2),
\]
\[
\mathcal M[J_m]_{22}=-\tau/24+O(\tau^2),\qquad
\mathcal B[J_m]=-\tau/48+O(\tau^2).
\]

These follow from integral_0^1 z(1-z) dz=1/6. Independently, the exact one-step nilpotent Gram matrix differs from its balanced endpoint power by eta^2 z(1-z)diag(1,-1)/8+O(eta^3), giving the same two constants at tau=eta.

If v and g stay parallel on a scalar commuting orbit, N=0 along that orbit and J and every jet remain zero. For d=1, the two terms in (4) agree identically, so the same conclusion holds without further assumptions. Zero residuals or zero training inputs also give J=J_m=0. A scalar K alone does not imply N=0: when K=cI,

\[
N(z)=e^{cz}(\|g\|^2vv^T-\|v\|^2gg^T).
\]

Thus repeated eigenvalues are not a reason to discard the source. Equations (11)--(15) preserve it.

A manufactured constant-coefficient equation checks the factorials independently. Freeze K=0, t=1, v=e_1 and g=e_1+e_2 in (2)--(4). Then

\[
R(z)=-z\begin{pmatrix}1&1\\0&0\end{pmatrix},\qquad
N(z)=\begin{pmatrix}1&-1\\-1&-1\end{pmatrix}.
\]

The 11 entry of (2) satisfies dot J_11=-2zJ_11-1 with zero initial value. Hence

\[
J_{11}(\tau,z)=-\frac{1-e^{-2z\tau}}{2z},\qquad
(j_q)_{11}=-\frac{\tau^{q+1}(-2)^q}{(q+1)!}.
\]

At z=0 the quotient has continuous value -tau. Every coefficient is nonzero for tau>0. These frozen coefficients are not asserted to form an endpoint trajectory of (1). They test the general linear memory equation and show why triangular dependence does not imply that a Taylor series terminates; they give no impossibility theorem for finite-state descriptions of actual training trajectories.

The analytic estimate is conditional on S and may be large on lognormal tails. It supplies no moment bound uniform in S. The theorem does not settle exact compression at fixed m, fixed positive learning rate, Gaussian initialization, activation-gate evolution, simultaneous size/step limits, or unbounded training time.
