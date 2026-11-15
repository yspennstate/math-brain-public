# First learning-rate correction for the structured deep-linear profile

The model is the scalar-identity initialization of the preceding three sessions. The result below gives a first-order correction to its gradient-flow endpoint and full NTK. The correction retains one symmetric matrix field in depth. It is not a finite-dimensional closure, nor a result for independent Gaussian matrices or ReLU activation.

## 1. Definitions and statement

Fix a positive depth/width ratio t, a positive total initial gain S, an active dimension d, a unit readout e, and finitely many training pairs (x_i,y_i) in R^d times R with positive weights alpha_i summing to one. For an endpoint matrix P and bias b define

\[
r_i=b+e^TPx_i-y_i,\quad h=\sum_i\alpha_i r_i,\quad
g=\sum_i\alpha_i r_i x_i,\quad v=P^Te.
\tag{1}
\]

For a depth profile C let

\[
U_z=tCU,\quad U(0)=I,\quad Q=U(1),\quad P=SQ,\quad
V(z)=QU(z)^{-1},\quad A(z)=U(z)^TU(z).
\tag{2}
\]

The size-limit GD recursion from round 3 is Euler's method, with step eta, for

\[
C_\tau=G(C,b)(z)=-S V(z)^Te\,g^TU(z)^T,\qquad b_\tau=-h,
\quad C(0,z)=0,\ b(0)=0.
\tag{3}
\]

Training time is tau and normalized depth is z in [0,1]. Superscript eta denotes its discrete iterates at tau_k=k eta. For all profiles the exact kernel coefficients are

\[
M=t\int_0^1(v^TA^{-1}v)A\,dz,\qquad
B=t\int_0^1 v^TA^{-1}v\,dz.
\tag{4}
\]

The full kernel and output are

\[
K(x,x')=1+x_E^TMx'_E+B\langle x_\perp,x'_\perp\rangle,
\qquad f(x)=b+e^TPx_E.
\]

The factor S has canceled from (4), but A(1)=P^TP/S^2 still depends on S.

Write

\[
H=P^TP/S^2,\quad K=\log H,\quad A_0(z)=H^z,\qquad
f(P,b)=-tP\int_0^1 A_0^{-1}v g^T A_0\,dz.
\tag{5}
\]

The preceding endpoint flow is

\[
\dot P=f(P,b),\quad \dot b=-h,\qquad P(0)=SI,\ b(0)=0.
\tag{6}
\]

It is global, with P invertible at every finite training time, as proved in round 4. Let M_0(P),B_0(P) denote (4) with A=A_0. These are exactly the round-4 balanced kernel formulas.

All quantities in the following equations are evaluated along (6). Define

\[
X(z)=-A_0(z)^{-1}v g^T A_0(z),\qquad
R(z)=t\int_0^z X(a)\,da,
\tag{7}
\]
\[
N(z)=(g^TA_0(z)g)vv^T
       -(v^TA_0(z)^{-1}v)A_0(z)gg^TA_0(z).
\tag{8}
\]

The symmetric memory field J is the solution, separately at each z, of

\[
\boxed{\dot J=R^T J+JR-tN,\qquad J(0,z)=0.}
\tag{9}
\]

At each time let W(z) be the solution of the linear boundary problem

\[
W_{zz}=W_zK+KW_z-KWK+tJ,\qquad W(0)=W(1)=0.
\tag{10}
\]

Its solution is unique. It is an instantaneous linear function of J; W is not an additional evolving state.

Define the following endpoint and kernel corrections:

\[
\begin{split}
\mathcal F(P,b,J)
 &=-tP\int_0^1
 \{A_0^{-1}v g^T W-A_0^{-1}WA_0^{-1}v g^TA_0\}\,dz,\\
\mathcal M(P,J)
 &=t\int_0^1\{(v^TA_0^{-1}v)W
       -(v^TA_0^{-1}WA_0^{-1}v)A_0\}\,dz,\\
\mathcal B(P,J)
 &=-t\int_0^1v^TA_0^{-1}WA_0^{-1}v\,dz,\\
\mathcal T(P,b)
 &=t^2P\int_{0<a<c<1}X(c)X(a)\,da\,dc .
\end{split}
\tag{11}
\]

For a differentiable map D denotes its ordinary directional derivative, with S,t and the data fixed. Define a matrix p and scalar beta by the finite-dimensional linear inhomogeneous system

\[
\boxed{\begin{split}
\dot p&=Df(P,b)[p,\beta]+\mathcal F+\mathcal T
              -\tfrac12 Df(P,b)[f,-h],\\
\dot\beta&=-Dh(P,b)[p,\beta]
              +\tfrac12 Dh(P,b)[f,-h],\\
p(0)&=0,\qquad \beta(0)=0.
\end{split}}
\tag{12}
\]

**Theorem.** For every fixed T<infinity and fixed S>0, as eta decreases to zero, uniformly over nodes k eta<=T,

\[
\boxed{\begin{split}
P^\eta_k&=P(\tau_k)+\eta p(\tau_k)+O_T(\eta^2),\\
b^\eta_k&=b(\tau_k)+\eta\beta(\tau_k)+O_T(\eta^2),\\
M^\eta_k&=M_0(P(\tau_k))+
 \eta\{DM_0(P(\tau_k))[p(\tau_k)]+\mathcal M(P(\tau_k),J(\tau_k))\}
 +O_T(\eta^2),\\
B^\eta_k&=B_0(P(\tau_k))+
 \eta\{DB_0(P(\tau_k))[p(\tau_k)]+\mathcal B(P(\tau_k),J(\tau_k))\}
 +O_T(\eta^2).
\end{split}}
\tag{13}
\]

There is also the useful expansion at the *actual discrete endpoint*:

\[
\boxed{
M^\eta_k=M_0(P^\eta_k)+\eta\mathcal M(P(\tau_k),J(\tau_k))+O_T(\eta^2),
\quad
B^\eta_k=B_0(P^\eta_k)+\eta\mathcal B(P(\tau_k),J(\tau_k))+O_T(\eta^2).
}
\tag{14}
\]

Thus (6),(9),(10),(12) describe the full first correction without evolving the nonlinear profile C. The evolving state consists of P,b,p,beta and the one field J. The theorem does not show that this field can be replaced by finitely many matrices.

For the random-gain model, all these statements apply conditionally at every S>0. Set S=exp(mu t+sigma sqrt(t) Z), with Z standard normal, after the size limit. The remainder constants may depend on S; no expectation bound uniform in the lognormal tails is claimed.

## 2. Independent recheck of the preceding bridge

Put

\[
\mathcal D(C)=(C+C^T)_z-t[C,C^T].
\tag{15}
\]

Here [F,G]=FG-GF. Since U_z=tCU and V_z=-tVC, differentiating (3) in z gives

\[
G_z=t(GC^T-C^TG).
\tag{16}
\]

Transposing gives G_z^T=t(CG^T-G^TC). Consequently

\[
D\mathcal D(C)[G]
=(G+G^T)_z-t([G,C^T]+[C,G^T])=0.
\tag{17}
\]

An exact expansion of the quadratic expression (15) gives, for every Euler step,

\[
\mathcal D(C+\eta G)=\mathcal D(C)-t\eta^2[G,G^T].
\tag{18}
\]

Let H_C=C+C^T. Direct depth differentiation gives

\[
A_z=tU^TH_CU,\qquad
A_{zz}=tU^T\{(H_C)_z+tC^TH_C+tH_CC\}U.
\]

Use UA^{-1}U^T=I to subtract A_z A^{-1}A_z. The remaining bracket is

\[
(H_C)_z+tC^TH_C+tH_CC-tH_C^2
=(H_C)_z-t[C,C^T]=\mathcal D(C).
\]

Thus, with no balancedness assumption,

\[
\boxed{A_{zz}-A_zA^{-1}A_z=tU^T\mathcal D(C)U.}
\tag{19}
\]

Under continuous flow, (17) and the initial condition give D=0. Then (A^{-1}A_z)_z=0 and A(0)=I imply A(z)=exp(zK) with K=log A(1). Substitution in (4), and the endpoint derivative

\[
\dot P=tS\int_0^1 VGU\,dz
       =-tP\int_0^1 A^{-1}v g^TA\,dz,
\tag{20}
\]

recovers (5),(6) and the round-4 kernel formulas. This rechecks the main claim, the transpose order and the S normalization.

## 3. Euler's first error term and the defect limit

Use the Banach space C^1([0,1];R^{d by d}) times R with its usual sum norm. Write Y=(C,b) and F(Y)=(G,-h). On bounded sets F is smooth with bounded derivatives of each fixed finite order. Indeed U is obtained by the convergent ordered-integral series for a linear ODE; on ||C||<=m its terms and every fixed derivative are bounded by the corresponding differentiated exponential series. Inversion of U is equivalently the linear ODE (U^{-1})_z=-tU^{-1}C. The depth derivatives follow from these equations. Products and the finite sums defining residuals preserve the stated bounds.

The round-4 global result bounds the flow path in this space on every finite interval. It also gives ordinary O(eta) Euler convergence in a fixed bounded neighborhood. To sharpen this, solve

\[
\dot Z=DF(Y)Z-\tfrac12 DF(Y)F(Y),\qquad Z(0)=0.
\tag{21}
\]

This is a linear ODE with bounded continuous coefficients. It has a unique solution on [0,T]. Set a_k=Y(tau_k)+eta Z(tau_k). Taylor's formula in time gives

\[
Y(\tau+\eta)=Y+\eta F+\tfrac12\eta^2 DF\,F+O_T(\eta^3),
\]
\[
\eta Z(\tau+\eta)=\eta Z+\eta^2(DF\,Z-\tfrac12 DF\,F)+O_T(\eta^3).
\]

Their sum is Y+eta Z+eta F+eta^2 DF Z+O(eta^3), while
a_k+eta F(a_k) has the same expansion. Thus a_k has one-step residual O(eta^3). Subtracting the Euler recursion gives an error bounded by
(1+c eta) times its previous value plus c eta^3. Iteration from zero yields

\[
\max_{k\eta\le T}\|Y^\eta_k-Y(\tau_k)-\eta Z(\tau_k)\|
\le c_T\eta^2.
\tag{22}
\]

The bounded-neighborhood argument used for first-order convergence justifies this estimate by induction for sufficiently small eta. The expansions only require derivatives through finite order, already bounded above.

Let Z_C be the profile component of Z. Expanding D at the flow profile gives

\[
\mathcal D(C^\eta_k)=\eta E(\tau_k)+O_T(\eta^2),
\quad E=D\mathcal D(C)Z_C.
\tag{23}
\]

Alternatively sum (18):

\[
\eta^{-1}\mathcal D(C^\eta_k)
=-t\eta\sum_{j<k}[G^\eta_j,(G^\eta_j)^T].
\tag{24}
\]

Euler convergence, local Lipschitz dependence of G and a uniform Riemann-sum error show, in the sup norm in z,

\[
E(\tau,z)=-t\int_0^\tau [G(s,z),G(s,z)^T]\,ds.
\tag{25}
\]

The error between (24) and (25) is O_T(eta); after multiplying by eta this agrees with (23). This is the leading accumulated defect, including its sign.

Define J=U^T E U. To express its evolution using only the endpoint flow, variation of constants on a prefix gives

\[
U_\tau(z)=tU(z)\int_0^z U(a)^{-1}G(a)U(a)\,da=U(z)R(z).
\tag{26}
\]

The last equality follows from

\[
G(z)=-U(z)^{-T}v g^TU(z)^T,\qquad
U^{-1}GU=-A_0^{-1}v g^TA_0=X(z).
\tag{27}
\]

Using (27) twice,

\[
U^TGG^TU=(g^TA_0g)vv^T,
\quad
U^TG^TGU=(v^TA_0^{-1}v)A_0gg^TA_0.
\tag{28}
\]

Differentiate U^T E U, insert (25),(26),(28), and obtain (9). J is symmetric because both its initial condition and its source are symmetric. Its coefficients are determined by the known P,b path, so it exists uniquely and stays bounded on every fixed interval.

The transport terms R^TJ+JR are necessary: integrating -tN without them would accumulate defects in changing prefix coordinates.

## 4. The forced Gram problem

Let a(z)=DA(C)[Z_C] be the full first variation of the prefix Gram matrix. Its endpoint values are

\[
a(0)=0,\quad
a(1)=(p^TP+P^Tp)/S^2,\qquad p=DP(C)[Z_C].
\tag{29}
\]

Differentiate (19) at a balanced profile:

\[
a_{zz}=a_zK+Ka_z-KaK+tJ.
\tag{30}
\]

For example A_0^{-1}(A_0)_z=K and (A_0)_z A_0^{-1}=K; varying A_z A^{-1}A_z gives exactly a_zK+Ka_z-KaK.

The variation a_bal=D(H^z)[p] satisfies the homogeneous equation in (30). To see this without differentiating a matrix logarithm formula, note that H^z solves the zero-source geodesic equation for every positive-definite endpoint H; differentiate that identity along P+epsilon p. Its endpoints are the same as (29).

Subtracting gives W=a-a_bal and exactly (10). For uniqueness and an explicit formula put

\[
W(z)=e^{zK/2}Y(z)e^{zK/2}.
\]

Differentiating and canceling the first derivatives in (10) yields

\[
Y_{zz}-\tfrac14[K,[K,Y]]
=t e^{-zK/2}J(z)e^{-zK/2},\qquad Y(0)=Y(1)=0.
\tag{31}
\]

Choose an orthonormal eigenbasis of K with eigenvalues k_i. Each entry solves

\[
Y_{ij}''-\kappa_{ij}^2Y_{ij}
=t(e^{-zK/2}Je^{-zK/2})_{ij},
\qquad \kappa_{ij}=|k_i-k_j|/2.
\]

The Dirichlet Green function is

\[
\Gamma_\kappa(z,a)=
\begin{cases}
-\dfrac{\sinh(\kappa\min(z,a))
          \sinh(\kappa(1-\max(z,a)))}{\kappa\sinh\kappa},
 &\kappa>0,\\
-\min(z,a)(1-\max(z,a)),&\kappa=0.
\end{cases}
\tag{32}
\]

On each side of a it solves the homogeneous scalar equation, vanishes at the appropriate boundary, is continuous at a and has derivative jump +1 there. These four facts prove that its integral against the source solves (31). The homogeneous scalar boundary problem has only the zero solution: multiply Y''-kappa^2Y=0 by Y and integrate to obtain minus the integral of (Y')^2+kappa^2Y^2 equal to zero. This proves uniqueness, including repeated eigenvalues. Formula (32) is continuous at kappa=0 by sinh u/u tending to one.

Consequently W is determined by the endpoint P and one field J, without any choice of singular-vector derivatives or any reconstruction of C.

## 5. Full kernel correction

Differentiate (4). Holding P fixed and varying A by W gives

\[
\delta(A^{-1})=-A_0^{-1}WA_0^{-1}.
\]

The two resulting product terms give exactly Mcal and Bcal in (11). The remaining variations, arising from p and a_bal, are DM_0[p] and DB_0[p]. Equation (22) and smoothness of the kernel map give (13) for M,B, with O_T(eta^2) remainders.

Expanding M_0(P^\eta_k) and B_0(P^\eta_k) by the first line of (13) proves (14). In particular, an imbalance of order eta has an order-eta kernel effect on a fixed training interval. The earlier one-step discrepancy was order eta^2 because only time eta had elapsed.

## 6. Endpoint correction

For general profiles write the right side of (20) as L(P,b,A). On the balanced manifold L=f. Its first variation in direction Z is

\[
DL[Z]=Df(P,b)[p,\beta]+\mathcal F(P,b,J).
\tag{33}
\]

This follows by splitting a=a_bal+W as above and differentiating the two A factors in (20); their contributions are exactly the first line of (11).

Let Phi(C)=S U_C(1). Since p=DPhi(C)Z_C, differentiating in training time and using (21) gives

\[
\dot p=D(D\Phi\,G)[Z]
             -\tfrac12D\Phi\,(DF\,F)_C
=Df[p,\beta]+\mathcal F
             -\tfrac12D\Phi\,(DF\,F)_C.
\tag{34}
\]

Here Phi does not depend on b, while G does; DF includes the bias component throughout. Along the balanced flow, the chain rule gives

\[
Df[f,-h]=D^2\Phi[G,G]+D\Phi\,(DF\,F)_C.
\tag{35}
\]

It remains to evaluate the Hessian term. Differentiate the depth-ordered exponential twice in the fixed direction G. One insertion at depth a and another at depth c, 0<a<c<1, contributes

\[
t^2P\,
(U(c)^{-1}G(c)U(c))
(U(a)^{-1}G(a)U(a)).
\]

There are two orders of differentiation with the same insertion depths. Thus

\[
\tfrac12D^2\Phi[G,G]
=t^2P\int_{0<a<c<1}X(c)X(a)\,da\,dc=\mathcal T.
\tag{36}
\]

The larger depth multiplies on the left. No commutation assumption was used.
Substituting (35),(36) into (34) proves the matrix equation in (12).

The bias component of (21) is

\[
\dot\beta=-Dh[p,\beta]+\tfrac12 Dh[f,-h],
\]

which proves the other equation. Since (12) is linear in p,beta with bounded coefficients and bounded forcing, it has a unique solution on every fixed interval. Equations (22) and the chain rule prove the endpoint part of (13), completing the theorem.

## 7. Mandatory benchmark and independent checks of constants

Take t=S=1, e=e_1, inputs e_1,e_2, targets 1,1 and weights 1/2. Initially g=(0,-1/2)^T, G=e_1e_2^T/2 and

\[
E_\tau(0)=-\tfrac14\operatorname{diag}(1,-1),\qquad
J(\tau,z)=-\tfrac{\tau}{4}\operatorname{diag}(1,-1)+O(\tau^2).
\]

At tau=0, K=0. Hence (10) and its zero boundary values give

\[
W(\tau,z)=\frac{\tau z(1-z)}8\operatorname{diag}(1,-1)
            +O(\tau^2).
\tag{37}
\]

Substituting in (11), with v=e_1 and A_0=I, yields

\[
\mathcal M(\tau)=
 \tau\begin{pmatrix}0&0\\0&-1/24\end{pmatrix}+O(\tau^2),
\qquad
\mathcal B(\tau)=-\tau/48+O(\tau^2).
\tag{38}
\]

The integrals used are integral z(1-z) dz=1/6 and the factor 1/8 in (37). Thus actual minus balanced kernel has M_22 correction -eta tau/24 and perpendicular correction -eta tau/48 at small tau.

These constants can also be checked without the correction equations. One Euler step gives C_1=(eta/2)e_1e_2^T, so

\[
M_1=\begin{pmatrix}
1+\eta^2/12&\eta/4+\eta^3/96\\
\eta/4+\eta^3/96&1+\eta^2/6+\eta^4/480
\end{pmatrix},\qquad B_1=1+\eta^2/12.
\tag{39}
\]

Direct multiplication gives

\[
[M_1,P_1^TP_1]_{12}=\eta^3/48+\eta^5/640.
\tag{40}
\]

The second update gives

\[
(C_2(z))_{22}=\eta^2(1-\eta)(1-z)/4,\qquad
[C_2(0),C_2(1)]_{21}=\eta^6/32.
\tag{41}
\]

Expanding the balanced formula at P_1=I+(eta/2)e_1e_2^T gives
(M_0(P_1))_22=1+5eta^2/24+O(eta^3) and
B_0(P_1)=1+5eta^2/48+O(eta^3). Subtract (39): actual minus balanced is -eta^2/24 and -eta^2/48 to leading order, agreeing with (38) at tau=eta. This one-step match is a check of constants, not an assertion of a stronger uniform remainder than (13).

There is a second sign check directly from the Gram matrices after one step. Put a=eta/2. Then

\[
A_1(z)=I+az(e_1e_2^T+e_2e_1^T)+a^2z^2e_2e_2^T.
\]

Expanding (A_1(1))^z shows

\[
A_1(z)-(A_1(1))^z
=\tfrac{a^2z(1-z)}2\operatorname{diag}(1,-1)+O(a^3),
\]

which is eta W(eta,z) from (37). This checks the sign independently of the Green function.

For d=1, every commutator vanishes. Thus J=W=0 and the kernel remains the exact scalar function of the endpoint at every eta. The correction p,beta in (12) can still be nonzero, because Euler's time discretization changes the endpoint trajectory. For zero residuals every correction vanishes. For zero training inputs J,p remain zero, but beta contains the familiar Euler correction to bias-only relaxation. These cases distinguish imbalance from ordinary time discretization.

## 8. Scope and the remaining compression problem

The first-order correction is closed in one symmetric depth field, driven by the already known endpoint flow, plus a finite-dimensional linear sensitivity equation. It avoids the nonlinear C profile but does not eliminate continuous depth. The Green representation shows exactly which weighted depth integrals of J enter the endpoint and kernel corrections. Their weights depend on the changing endpoint spectrum.

No impossibility theorem for finitely many additional matrices follows from these formulas. A special trajectory could compress the field, and the equations above do not exclude a different choice of finite state. Establishing or refuting such a reduction is the remaining concrete question within this model.

The result is conditional on the earlier scalar-identity joint-size theorem, with the size limit taken before the small-step expansion on fixed training intervals. It makes no assertion for iid Gaussian matrices, ReLU gates, an increasing active dimension, simultaneous eta/size rates, or infinite training time.
