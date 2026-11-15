# A subcritical basin at boundary-scale initialization

Let m>=d+1, d>=1. Both layers of the network

\[
f_{a,W}(x)=a^TWx,\qquad
L_b(a,W)=\frac12\|W^Ta-b\|^2
\tag{1}
\]

are trainable. The target b in R^d is fixed. This is the empirical square loss on x_j=sqrt(d)e_j, y_j=sqrt(d)b_j, averaged over j, and the population square loss for x~N(0,I_d). Sharpness is the largest Hessian eigenvalue in the Euclidean parameter coordinates (a,W).

For eta>0 set a=eta^(-1/2)A, W=eta^(-1/2)U, and y=eta b. Gradient descent on (1) is exactly

\[
A^+=A-Ur,\qquad U^+=U-Ar^T,\qquad r=U^TA-y.
\tag{2}
\]

Write Z=[A U], q=||A||^2, C=U^TU, v=U^TA, and s=q+||C||_op. All matrix norms without a subscript below are operator norms; the norm of a parameter pair is its Euclidean/Frobenius norm. Define the open set

\[
\mathcal B=\{(A,U):\operatorname{rank}[A\ U]=d+1,
\quad \|A\|^2+\|U\|_{\rm op}^2<2\}.
\tag{3}
\]

## Basin theorem

Fix z_0=(A_0,U_0) in B and write s_0=||A_0||^2+||U_0||_op^2.

1. For y=0, (2) converges in parameter space to a zero-residual global minimizer z_*; its residual and parameter error decay geometrically after a finite time. Every iterate satisfies q_t<=q_0 and 0<=C_t<=C_0 in Loewner order. The endpoint obeys

\[
0<q_*+\lambda_{\min}(C_*)\leq
q_*+\lambda_{\max}(C_*)\leq s_0<2.
\tag{4}
\]

2. For each fixed b, there is eta_0(z_0,b)>0 such that, for every 0<eta<eta_0, (2) with y=eta b converges to a global minimizer. Its sharpness in the original coordinates satisfies

\[
\eta\lambda_{\max}(\nabla^2L_b(a_\infty,W_\infty))
\leq \frac{2+s_0}{2}<2.
\tag{5}
\]

The neighborhood and eta_0 may depend on the initial point. No uniform eta_0 over B is asserted.

### Exact zero-target identities

For y=0, put h=||v||^2 and k=v^TCv. Expanding (2) gives

\[
q^+=q-2h+k,\qquad C^+=C+(q-2)vv^T,
\tag{6}
\]

and

\[
v^+=[I-C-qI+hI]v.
\tag{7}
\]

For example U^{+T}A^+=(U^T-vA^T)(A-Uv)=v-Cv-qv+hv. The first identity in (6) follows from A^+=A-Uv and A^TUv=h. The second follows from U^+=U-Av^T and U^TA=v.

Set c_0=||C_0||. If q<=q_0 and C<=C_0 then k<=c_0 h, and (6) gives

\[
q^+\leq q-(2-c_0)h\leq q,
\qquad C^+\leq C
\tag{8}
\]

because c_0<2 and q<=q_0<2. Also C^+ is positive semidefinite because it is U^{+T}U^+. Induction proves these bounds for every t. Consequently

\[
\sum_{t=0}^\infty h_t\leq \frac{q_0}{2-c_0},\qquad
h_t\longrightarrow0,
\qquad \operatorname{tr}(Z_t^TZ_t)\leq M:=q_0+\operatorname{tr}C_0.
\tag{9}
\]

Cauchy--Schwarz gives h_t<=q_t||C_t||<=q_0c_0. Let rho=q_0c_0. Since q_0+c_0=s_0<2, rho<=s_0^2/4<1.

### Preservation of full column rank

Define the (d+1)-square symmetric matrix

\[
K_t=\begin{pmatrix}0&v_t^T\\v_t&0\end{pmatrix},
\qquad G_t=Z_t^TZ_t.
\]

Equation (2) says Z_{t+1}=Z_t(I-K_t). The eigenvalues of K_t are ||v_t||, -||v_t|| and d-1 zeros (all zero if v_t=0). Therefore

\[
\det G_{t+1}=\det G_t(1-h_t)^2.
\tag{10}
\]

The initial determinant D_0=det G_0 is positive by the full column rank hypothesis. For 0<=h<=rho<1,

\[
\log(1-h)=-\int_0^h\frac{du}{1-u}\geq-\frac{h}{1-\rho}.
\]

Equations (9)--(10) imply, for every t,

\[
\det G_t\geq D_*:=D_0
\exp\!\left[-\frac{2q_0}{(1-\rho)(2-c_0)}\right]>0.
\tag{11}
\]

Every eigenvalue of G_t is at most its trace, which is at most M. Since G_t has d+1 eigenvalues, their product is at most lambda_min(G_t) M^d. Thus

\[
G_t\succeq\mu I_{d+1},\qquad
\mu=D_*/M^d>0.
\tag{12}
\]

Taking principal submatrices gives q_t>=mu and C_t>=mu I_d. In particular

\[
2\mu I_d\preceq C_t+q_t I_d\preceq s_0 I_d.
\tag{13}
\]

This determinant argument concerns all columns of Z. No alignment, balance, scalar-input, or invariant-slice assumption is used.

### Convergence of the zero-target trajectory

Let kappa=min{2mu,2-s_0,1}>0. From (13), each eigenvalue alpha of C_t+q_t I lies in [kappa,2-kappa], so

\[
\|I-C_t-q_t I\|\leq1-\kappa.
\]

By (9), choose T so that h_t<=kappa/2 for every t>=T. Equation (7) then gives

\[
\|v_{t+1}\|\leq(1-\kappa/2)\|v_t\|,\qquad t\geq T.
\tag{14}
\]

Moreover the parameter increment satisfies

\[
\|z_{t+1}-z_t\|^2
=\|U_tv_t\|^2+q_t\|v_t\|^2
\leq M\|v_t\|^2.
\tag{15}
\]

The geometric series in (14) makes the sum of parameter increments finite. Hence z_t converges to z_*, with a geometric tail bound. Continuity and v_t->0 give U_*^TA_*=0; this is a global minimum of the nonnegative loss. Passing to the limit in (12)--(13) proves (4).

### A local lemma for small nonzero targets

For an arbitrary target y and residual r=v-y, expansion of (2) gives the exact recurrence

\[
r^+=[I-C-qI+(v^Tr)I]r.
\tag{16}
\]

Indeed v^+=v-(C+qI)r+(v^Tr)r and subtraction of y gives (16).

Fix the zero-target endpoint z_* just constructed. Put a_*=q_*+lambda_min(C_*)>0 and s_*=q_*+lambda_max(C_*)<2. Let k=min{a_*,2-s_*,1}/2>0. At z_* the eigenvalues of H_out(z):=C+qI lie in [2k,2-2k]. By continuity there is a radius R>0 such that throughout the closed parameter ball ||z-z_*||<=R,

\[
k I\preceq H_{\rm out}(z)\preceq(2-k)I,
\quad \|z\|\leq B:=\|z_*\|+R,
\quad s(z)\leq (2+s_0)/2.
\tag{17}
\]

Such a ball exists because s_*<=s_0<(2+s_0)/2. The constant B is positive. Choose e>0 so small that

\[
e(e+1)\leq k/2,\qquad 2Be/k\leq R/4.
\tag{18}
\]

Suppose ||y||<=1, an initial point z obeys ||z-z_*||<=R/4, and its residual norm is <=e. While the trajectory stays in the ball and its residual norm stays <=e, one has ||v||<=e+1. Equations (16)--(18) give

\[
\|r^+\|\leq[1-k+(e+1)e]\|r\|
\leq (1-k/2)\|r\|.
\tag{19}
\]

The parameter step has norm at most B||r||, by the same calculation as (15). The sum of all step norms allowed by (19) is at most 2Be/k<=R/4. Induction on the number of steps therefore puts every iterate within distance R/2 of z_* and makes every residual <=e. This justifies the hypotheses used at each step; no first exit is possible. The increments are summable, the parameters converge, and the residual tends to zero. The endpoint lies in the ball and satisfies the last bound in (17).

### Entry into this local neighborhood for y=eta b

Choose a finite T for the zero-target trajectory so large that ||z_T(0)-z_*||<R/8 and ||U_T(0)^TA_T(0)||<e/4. Each finite iterate z_T(y) is a polynomial, hence continuous, function of y, since the initialization z_0 is fixed and (2) is polynomial. The residual U_T(y)^TA_T(y)-y is also continuous. There is consequently eps>0 such that ||y||<eps implies ||y||<=1, ||z_T(y)-z_*||<=R/4 and ||U_T(y)^TA_T(y)-y||<=e. The local lemma applies from time T onward.

For fixed b!=0, take eta_0=eps/||b||, decreasing it if necessary to make all inequalities strict. For b=0, the first part applies for every eta. Thus the scaled iterates converge with r_infinity=0 whenever eta is sufficiently small.

At any original zero-residual point the Hessian is J^TJ, where J(u,V)=W^Tu+V^Ta. Direct composition gives

\[
JJ^T=W^TW+\|a\|^2I_d
=\eta^{-1}(C+qI_d).
\tag{20}
\]

The positive eigenvalues of J^TJ and JJ^T coincide: for example, if JJ^Tx=lambda x with lambda>0, then J^Tx is nonzero and is an eigenvector of J^TJ with the same eigenvalue, and conversely. The remaining eigenvalues of J^TJ are zero. The endpoint bound in (17) therefore proves (5). This completes the basin theorem.

## The basin can start above the classical curvature threshold

For m=16,d=8 take A_0=e_1, the first column of U_0 equal to (4/5)e_1+(1/10)e_2, and column j equal to (1/10)e_(j+1) for 2<=j<=8. Then Z_0 has nine independent columns, q_0=1 and C_0 is diagonal with entries 13/20,1/100,...,1/100. Thus s_0=33/20<2.

At zero target, take the parameter direction h=(e_1,V), with V_11=1 and all other entries zero. Its squared norm is 2. The output differential is J h=(9/5)e_1 and the residual is (4/5)e_1. Expanding the square loss along this direction gives

\[
\nabla^2 L_0[h,h]=\|Jh\|^2+2e_1^TVv
=81/25+8/5=121/25.
\]

The Hessian Rayleigh quotient is therefore 121/50>2. By continuity an open neighborhood still has s_0<2, full column rank, and initial sharpness above 2. The theorem gives convergence there for zero target, and for sufficiently small scaled targets. In original coordinates this is convergence despite initial sharpness exceeding 2/eta. It does not imply nonmonotone loss or a sustained edge regime.

## Gaussian probability consequence at variance tau^2/eta

Fix tau>0. Let all entries of A_0,U_0 be independent N(0,tau^2); equivalently initialize all original parameters independently as N(0,tau^2/eta). For m>=d+1, Z_0 has full column rank almost surely. To see this without a rank-distribution formula, the determinant of its first d+1 rows is a nonzero polynomial in continuously distributed entries. A nonzero polynomial has a zero set of Lebesgue measure zero, by induction on the number of variables and Fubini's theorem, treating it as a univariate polynomial outside the null sets where all its coefficients vanish.

Let w(eta)>=0 be any deterministic function tending to zero. Let E_eta be the event that GD converges in parameter space to a global minimizer satisfying

\[
|\eta\lambda_{\max}(\nabla^2L_b(a_\infty,W_\infty))-2|
\leq w(\eta).
\tag{21}
\]

Any extra requirement of edge entry or nonmonotone training can only shrink this event. Then

\[
\limsup_{\eta\downarrow0}\Pr(E_\eta)
\leq \Pr\{\|A_0\|^2+\|U_0\|_{\rm op}^2\geq2\}.
\tag{22}
\]

Indeed couple all eta by the same random scaled initialization Z_0. For every Z_0 in B, (5) leaves a fixed positive gap (2-s_0)/2 below 2, so E_eta is false for all sufficiently small eta. For any sequence eta_n->0, the reverse Fatou inequality for indicators bounded by 1 gives limsup_n Pr(E_eta_n)<=Pr(Z_0 not in B). The null rank-deficient set can be discarded. Since this holds for every sequence, it proves (22). The events are measurable: parameter convergence is a countable Cauchy condition on the polynomial iterates, and the limit and its continuous loss and Hessian can be evaluated on that set.

For b=0 the right side in (22) also bounds Pr(E_eta) at every eta whenever w(eta) is replaced by zero: each point in B has scaled endpoint sharpness strictly below 2. A uniform positive-width window still requires either a fixed gap subset of B or the limiting statement (22).

There is a simple explicit bound for (22). Put p=m(d+1). Since ||U||_op^2<=||U||_F^2, its right side is at most Pr(S>=2), where S=||A_0||^2+||U_0||_F^2 and S/tau^2 is a sum of p independent squared standard Gaussians. If

\[
u:=\frac{2}{p\tau^2}>1,
\]

then

\[
\Pr(S\geq2)\leq
\exp\!\left[-\frac p2(u-1-\log u)\right].
\tag{23}
\]

For completeness the Gaussian integral gives E exp(t S/tau^2)=(1-2t)^(-p/2), 0<t<1/2. Markov's inequality with t=(1-1/u)/2 yields exp(-tpu)(1-2t)^(-p/2)=exp[-p(u-1-log u)/2]. This proves (23).

For the same concrete network as the earlier report, m=16,d=8,p=144, choose tau^2=1/(2p)=1/288. Then u=4, and

\[
\boxed{\ \limsup_{\eta\downarrow0}\Pr(E_\eta)
\leq \exp[-72(3-\log4)]<3.5\times10^{-51}.\ }
\tag{24}
\]

For every fixed nonzero b this is an asymptotic bound with no asserted finite-eta rate. The absolute endpoint window |lambda_max-2/eta|<=epsilon(eta), epsilon(eta)->0, is covered by taking w(eta)=eta epsilon(eta).

## Limits of the conclusion

The theorem proves convergence and exclusion of a near-edge endpoint on one open basin, at the variance scale left untreated by the earlier report. It does not classify the complementary Gaussian initializations, establish an edge-of-stability phase, or address nonlinear activation functions. The rank assumption is satisfied almost surely in the stated overparameterized Gaussian model and is used to preserve a spectral gap; rank-deficient starts are not covered by this argument. The zero-target analysis is exact. The nonzero-target passage uses a neighborhood reached after a finite, initialization-dependent time, so (24) is a limsup rather than an explicit eta-uniform estimate. No novelty claim relative to the full literature on matrix factorization is made.
