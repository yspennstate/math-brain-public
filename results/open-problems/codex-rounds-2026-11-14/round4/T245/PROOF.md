# End-to-end closure in the small-step limit of the structured model

This concerns the scalar-identity initialization in the preceding reports. It gives no law for independent Gaussian matrix weights or ReLU networks. The end-to-end operator below is the balanced deep-linear operator; its finite-depth and infinite-depth versions are established in the literature. The result here connects that operator to the preceding random depth profile, including its full test kernel, and separates gradient flow from discrete gradient descent.

## 1. Statement

Fix d, a unit vector e in R^d, training inputs x_i, targets y_i, and positive weights alpha_i with sum one. Fix t>0 and S>0. For a matrix P and scalar b write

\[
r_i=b+e^TPx_i-y_i,\qquad
h=\sum_i\alpha_i r_i,\qquad
g=\sum_i\alpha_i r_i x_i,\qquad
\ell=\tfrac12\sum_i\alpha_i r_i^2.
\tag{1}
\]

For an invertible matrix P define

\[
\mathcal A_P(G)=\int_0^1 (PP^T)^{1-z}G(P^TP)^z\,dz.
\tag{2}
\]

All powers are positive-definite spectral powers. Consider the finite-dimensional system

\[
\boxed{\dot P=-t\mathcal A_P(eg^T),\qquad
\dot b=-h,\qquad P(0)=SI_d,\quad b(0)=0.}
\tag{3}
\]

Dots denote continuous training time tau; t remains the depth/width ratio.

**Theorem.** System (3) has a unique solution for every tau>=0, and P remains invertible at every finite time. The small-step limit of the preceding depth-profile recursion, with k eta approximating tau, has output b+e^TPx_E and full kernel

\[
K_\tau(x,x')=1+x_E^TM_\tau x'_E+
 B_\tau\langle x_\perp,x'_\perp\rangle,
\tag{4}
\]
\[
\boxed{M_\tau=t\int_0^1
 [e^T(PP^T)^{1-z}e](P^TP)^z\,dz,\qquad
 B_\tau=t\int_0^1 S^{2z}e^T(PP^T)^{1-z}e\,dz.}
\tag{5}
\]

Convergence as eta decreases to zero is uniform on every finite training interval, for the profile, outputs, and kernel coefficients. The state has d^2+1 real coordinates; the integrals are functions of that state, not additional dynamical variables.

For the earlier width-n, depth-L model with W_l=Theta_l/sqrt(n), fixed readout e, trainable bias, and independent initial gains

\[
W_l=s_l I_n,\qquad
s_l=\exp(\mu/n+\sigma Z_l/\sqrt n),
\]

the resulting **iterated** limiting law is obtained by first taking L/n -> t at each fixed eta and fixed finite number of steps, and then taking eta -> 0 on a fixed continuous training interval. In (3)--(5) set

\[
S=\exp(\mu t+\sigma\sqrt t\,Z),\qquad Z\sim N(0,1).
\tag{6}
\]

There is no assertion here that eta and the size can tend to their limits at arbitrary simultaneous rates, nor that the infinite training-time limit can be interchanged with either limit.

If ell_0 is the initial loss, every singular value sigma_j(P(tau)) satisfies

\[
\boxed{
S\exp[-\sqrt{t\tau\ell_0}]
\le \sigma_j(P(\tau))
\le S\exp[\sqrt{t\tau\ell_0}],\qquad
|b(\tau)|\le\sqrt{\tau\ell_0}.}
\tag{7}
\]

These are finite-time bounds, not convergence rates as tau tends to infinity.

## 2. Recheck of the preceding profile

Let the active factors be A_l=s_lD_l, D_l=I+C_l/n, and put

\[
S_n=\prod_l s_l,\quad Q_j=D_j\cdots D_1,\quad
R_l=D_L\cdots D_{l+1}.
\]

The output is b+S_n e^TQ_Lx. A forward vector before layer l and a backward vector after that layer carry scalar factors prod_{j<l}s_j and prod_{j>l}s_j. Their product is S_n/s_l. Gradient descent in Theta_l changes A_l by -eta/n times the W_l gradient. Multiplying this update by n/s_l gives

\[
C_l^+=C_l-\eta S_n s_l^{-2} R_l^T e\,g_n^TQ_{l-1}^T.
\tag{8}
\]

The Frobenius inner product of two parameter derivatives is the forward inner product times the backward squared norm, divided by n. Splitting a test vector into its active and perpendicular parts therefore gives

\[
M_n=\frac{S_n^2}{n}\sum_l s_l^{-2}\|R_l^Te\|^2Q_{l-1}^TQ_{l-1},
\quad B_n=\frac{S_n^2}{n}\sum_l s_l^{-2}\|R_l^Te\|^2.
\tag{9}
\]

The perpendicular term includes trainable entries whose gradients on the training data vanish. Removing them would change the kernel. Equations (8)--(9) rederive the preceding report's finite-size identities independently from the parameter derivatives. Under max_l|s_l-1| -> 0 and S_n -> S, ordered products give its limiting profile recursion.

Precisely, for C:[0,1] -> R^{d by d}, let

\[
U_z=tCU,\quad U(0)=I,\qquad
V(z)=U(1)U(z)^{-1}.
\tag{10}
\]

Its update is Euler's method for

\[
C_\tau=F(C,b)(z):=-S V(z)^T e\,g^TU(z)^T,
\qquad b_\tau=-h,
\tag{11}
\]

where P=SU(1), and C(0,z)=0. Its kernel is

\[
M=tS^2\int_0^1\|V^Te\|^2U^TU\,dz,
\qquad B=tS^2\int_0^1\|V^Te\|^2\,dz.
\tag{12}
\]

The preceding report proves the fixed-step size limit; the following argument begins with (10)--(12).

The normalization in that size limit can also be checked directly. If C_l converges uniformly to C((l-1)/L), every product of I+C_l/n has norm at most exp((L/n) max_l||C_l||). Compare each multiplication with the integral equation U_z=tCU on its interval of length 1/L. Iterating the difference bounds the prefix error by a constant times (L/n) max_l||C_l-C((l-1)/L)||, plus |L/n-t| max_z||C(z)||, plus the modulus of continuity of CU on intervals of length 1/L. All three terms vanish. The suffix comparison is the same backward iteration. Equation (8) then propagates uniform convergence to the next fixed training step, since S_n s_l^{-2} converges uniformly to S. Equation (9) is a Riemann sum with prefactor L/n, giving exactly (12). This checks the load-bearing limit as well as the finite-size derivative identities.

## 3. Local existence and the balancedness identity

Use the Banach space C^1([0,1];R^{d by d}) times R, with the sum of the sup norms of C, C_z and b. On a bounded set in this space the integral equation for U bounds U and U^{-1} by exp(t||C||_infinity). Subtracting two integral equations and iterating their integral error bound shows that U and U^{-1} depend locally Lipschitz continuously on C. Their depth derivatives are tCU and -tU^{-1}C, so this dependence is also locally Lipschitz in C^1. The residuals in (1) depend linearly on b and U(1). Products in (11) are consequently locally Lipschitz in this Banach space. Picard iteration gives a unique local C^1 solution. The same formulas are continuously differentiable on bounded sets, which also gives the ordinary Euler error estimate used below.

Write G=C_tau=F(C,b). From V_z=-tVC and U_z=tCU one obtains

\[
G_z=t(GC^T-C^TG)=t[G,C^T].
\tag{13}
\]

Here [A,B]=AB-BA. Set

\[
\mathcal D(C)=(C+C^T)_z-t[C,C^T].
\tag{14}
\]

Taking the transpose of (13) gives G_z^T=t[C,G^T]. It follows that

\[
\partial_\tau\mathcal D(C)
=G_z+G_z^T-t([G,C^T]+[C,G^T])=0.
\]

Since C is initially zero, the exact flow satisfies

\[
(C+C^T)_z=t[C,C^T].
\tag{15}
\]

This conservation law holds for noncommuting profiles. It does not assert that C is independent of depth or that C is symmetric.

## 4. Prefix and suffix Gram matrices

Put H=C+C^T and A(z)=U(z)^TU(z), at a fixed training time. Equation (10) gives

\[
A_z=tU^THU.
\]

By (15), H_z=t[C,C^T]. Therefore

\[
\begin{aligned}
A_{zz}
&=tU^T(H_z+tC^TH+tHC)U\\
&=t^2U^T\{[C,C^T]+C^T(C+C^T)+(C+C^T)C\}U\\
&=t^2U^T H^2 U
=A_z A^{-1}A_z.
\end{aligned}
\tag{16}
\]

For the last equality use U A^{-1} U^T=I. Differentiating A^{-1}A_z using (16) shows that it is constant in z. Since A(0)=I, it equals the symmetric matrix J=A_z(0). Hence A_z=AJ and

\[
A(z)=\exp(zJ)=A(1)^z.
\tag{17}
\]

The symmetric logarithm of the positive-definite matrix A(1) is unique, so the second equality follows without a choice of logarithm. Write Q=U(1). Then

\[
U(z)^TU(z)=(Q^TQ)^z,
\]
\[
V(z)V(z)^T
=Q(U(z)^TU(z))^{-1}Q^T
=Q(Q^TQ)^{-z}Q^T
=(QQ^T)^{1-z}.
\tag{18}
\]

The final equality follows by a singular value decomposition of Q. Thus the Gram matrices needed by the kernel are functions of the endpoint even though U itself can rotate with depth.

## 5. End-to-end equation and full kernel

Differentiate (10) with respect to training time. Variation of constants yields

\[
\dot U(1)=t\int_0^1 V(z)G(z)U(z)\,dz.
\]

Substitute (11), multiply by S, and use (18):

\[
\dot P=-tS^2\int_0^1
(QQ^T)^{1-z}eg^T(Q^TQ)^z\,dz.
\]

Because P=SQ, the scalar factors in the integrand are
S^2 S^{-2(1-z)}S^{-2z}=1. This proves (3).
Substitution of (18) into (12) cancels the same factors for M and leaves S^{2z} for B, proving (5). In particular M commutes with P^TP.

The integrals can be evaluated without a depth grid. Let

\[
P=O\operatorname{diag}(\sigma_1,\ldots,\sigma_d)R^T,
\qquad a=O^Te,
\]
\[
\Lambda(u,v)=\int_0^1u^{1-z}v^z\,dz
=\begin{cases}(v-u)/(\log v-\log u),&u\ne v,\\u,&u=v.
\end{cases}
\tag{19}
\]

The continuous value at equality follows either by differentiation or directly from the integral. In singular coordinates,

\[
\mathcal A_P(G)
=O\left(\Lambda(\sigma_i^2,\sigma_j^2)
                 (O^TGR)_{ij}\right)_{ij}R^T,
\]
\[
M=tR\operatorname{diag}\left(
\sum_i a_i^2\Lambda(\sigma_i^2,\sigma_j^2)
\right)_{j=1}^dR^T,
\quad
B=t\sum_i a_i^2\Lambda(\sigma_i^2,S^2).
\tag{20}
\]

Repeated singular values cause no ambiguity: (2) and (5) define the matrices independently of the chosen singular bases, and (19) is continuous there.

## 6. Global finite-time bounds

The right side of (3) is smooth on invertible P. Indeed the logarithm and exponential are smooth on positive-definite matrices, and the powers in (2) are exp(z log(P^TP)) and exp((1-z) log(PP^T)), integrated over a compact interval. Thus (3) has a unique maximal solution until P leaves every compact subset of the invertible matrices or b becomes unbounded.

Let v=P^Te, H=P^TP, and D=g^TMg. Equations (3) and (5) give

\[
\dot\ell=h\dot b+g^T\dot P^Te=-h^2-D,\qquad D\ge0.
\tag{21}
\]

For 0<=tau<=T in the interval of existence,

\[
\int_0^\tau(h^2+D)\,ds\le\ell_0,
\qquad |b(\tau)|\le\sqrt{\tau\ell_0}.
\tag{22}
\]

To control the singular values, use

\[
e^T(PP^T)^{1-z}e=v^TH^{-z}v.
\tag{23}
\]

This identity follows by SVD, or by P^T(PP^T)^{-z}=(P^TP)^{-z}P^T. In an orthonormal eigenbasis of H with eigenvalues lambda_j>0, (5) now gives

\[
D=t\int_0^1
 \left(\sum_i v_i^2\lambda_i^{-z}\right)
 \left(\sum_j g_j^2\lambda_j^z\right)dz
\ge t\,v_i^2g_i^2
\quad\text{for every }i.
\tag{24}
\]

Every summand in the product is nonnegative; the i=j summand alone proves the bound.
Differentiating H in (3) gives

\[
\dot H=-t\int_0^1
\{H^{1-z}vg^TH^z+H^zgv^TH^{1-z}\}\,dz.
\tag{25}
\]

For a unit eigenvector u_i, its diagonal element is

\[
u_i^T\dot H u_i=-2t\lambda_i (u_i^Tv)(u_i^Tg).
\tag{26}
\]

The ordered eigenvalues of a C^1 symmetric matrix path are locally Lipschitz. At almost every time their derivatives are diagonal elements of dot H in suitable orthonormal eigenvectors; at a repeated eigenvalue one diagonalizes dot H restricted to its eigenspace. Equation (26) and (24) apply to these vectors as well. Consequently, almost everywhere,

\[
\left|\frac d{d\tau}\log\lambda_i\right|
\le 2\sqrt{tD}.
\]

Integrating and using Cauchy--Schwarz and (22) yields

\[
|\log\lambda_i(\tau)-2\log S|
\le2\sqrt{t\tau\ell_0}.
\tag{27}
\]

Since sigma_i=sqrt(lambda_i), this is (7). Thus on every finite interval P and P^{-1} are bounded and b is bounded. Their values lie in a compact subset of the domain of (3), so its solution extends across any purported finite maximal time. This proves global existence and finite-time invertibility. No rank or affine-spanning assumption on the training inputs was used.

The local profile solution cannot fail earlier. On any finite interval on which it exists, it projects to the solution (3) by uniqueness. Equations (18) and (7) bound ||U|| and ||V|| uniformly, since

\[
\|U(z)\|,\|V(z)\|\le\max(1,\|P/S\|).
\]

The residuals, h and g are bounded by (1), or directly by ell<=ell_0 and the fixed data. Equation (11) then bounds ||G||_infinity on that interval. Integrating C_tau=G bounds ||C||_infinity. Equation (13) bounds

\[
\|G_z\|_\infty\le2t\|G\|_\infty\|C\|_\infty,
\]

and integration bounds ||C_z||_infinity too. The vector field is uniformly bounded and locally Lipschitz on these bounded sets, with constants depending only on their bounds, so the integral equation has a limit at a finite endpoint and its local existence theorem extends the solution. This proves global existence of the profile and establishes (3)--(5) for all finite times.

## 7. Euler convergence and the exact discrete defect

Fix T<infinity and S>0. On a bounded neighborhood in C^1 times R of the flow path on [0,T], the vector field (11) has a Lipschitz constant L_0 and a bound F_0. Its integral equation shows that a flow step minus its Euler step has norm at most L_0 F_0 eta^2/2. If e_k is the difference between the exact path and Euler's method, then

\[
e_{k+1}\le(1+L_0\eta)e_k+L_0F_0\eta^2/2.
\]

Iteration, using (1+L_0 eta)^k<=exp(L_0T), gives max_{k eta<=T}e_k<=C_T eta. For sufficiently small eta this bound keeps the iterates inside the chosen neighborhood, justifying the estimate by induction. Linear interpolation also differs from the flow by O(eta). The output and kernel maps (10),(12) are locally Lipschitz there, so their errors are O(eta) too.

There is a precise reason not to use the balanced formula as an exact discrete-GD law. For an arbitrary current C and its vector field G, (13) holds regardless of balancedness. Expanding (14) after the Euler step C^+=C+eta G gives exactly

\[
\boxed{\mathcal D(C^+)=\mathcal D(C)-t\eta^2[G,G^T].}
\tag{28}
\]

The order-eta terms cancel by (13). Therefore, from C_0=0,

\[
\|\mathcal D(C_k)\|_\infty
\le2t\eta^2\sum_{j<k}\|G_j\|_\infty^2
\le2tT\eta\max_{j<k}\|G_j\|_\infty^2
\quad(k\eta\le T).
\tag{29}
\]

The last maximum is bounded uniformly for small eta by the preceding Euler convergence argument. This quantifies the balance defect without assuming exact balancedness of discrete steps.

There is a separate finite-layer check of its sign and order. For raw factors A_l let G_l be the gradient of the loss in A_l coordinates, so A_l^+=A_l-(eta/n)G_l. Write the adjacent balance matrix as J_l=A_l A_l^T-A_{l+1}^T A_{l+1}. The product rule for the loss gives

\[
G_l A_l^T=A_{l+1}^T G_{l+1},\qquad
A_lG_l^T=G_{l+1}^T A_{l+1}.
\]

For example, if F=A_{l-1}\cdots A_1, T=A_L\cdots A_{l+2}, and E is the derivative of the loss in the end-to-end product, then G_l=A_{l+1}^TT^TEF^T and G_{l+1}=T^TEF^TA_l^T, proving the first equality; the second is its transpose. Expanding the two updated Gram matrices therefore cancels both linear terms and leaves exactly

\[
J_l^+-J_l=\frac{\eta^2}{n^2}
(G_lG_l^T-G_{l+1}^TG_{l+1}).
\]

For unit scalar gains and a smooth normalized profile A_l=I+C((l-1)/L)/n with L/n -> t, expansion gives

\[
n^2 J_l\longrightarrow -(C+C^T)_z/t+[C,C^T]
=-\mathcal D(C)/t.
\]

The quadratic finite-layer expression thus has the sign and scaling of (28). This last comparison is a local smooth-profile check; the exact discrete bound used in the theorem is (28)--(29).

For the earlier example t=S=1, e=e_1, inputs e_1,e_2, targets both 1 and weights 1/2, G_0=e_1e_2^T/2. Thus already

\[
\mathcal D(C_1)=-\frac{\eta^2}{4}
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{30}
\]

Here C_1=(eta/2)e_1e_2^T and P_1=I+(eta/2)e_1e_2^T. Direct polynomial integration of (12) gives the preceding report's exact

\[
M_1=\begin{pmatrix}
1+\eta^2/12&\eta/4+\eta^3/96\\
\eta/4+\eta^3/96&1+\eta^2/6+\eta^4/480
\end{pmatrix},\qquad B_1=1+\eta^2/12.
\tag{31}
\]

Multiplying the two 2 by 2 matrices gives

\[
\boxed{[M_1,P_1^TP_1]_{12}
=\eta^3/48+\eta^5/640>0\quad(\eta>0).}
\tag{32}
\]

But every matrix M in (5) commutes with P^TP. Thus (5) fails as an exact kernel formula for this discrete trajectory after its first step. This obstructs this particular balanced endpoint formula, not every possible finite-dimensional discrete recursion.

For an additional check, put a=eta/2 and J=e_1e_2^T+e_2e_1^T. Then P_1P_1^T=I+aJ+a^2e_1e_1^T and P_1^TP_1=I+aJ+a^2e_2e_2^T. Expanding spectral powers about I gives the balanced prediction

\[
(M_{\rm bal}(P_1))_{22}
=1+5\eta^2/24+O(\eta^3),\qquad
B_{\rm bal}(P_1)=1+5\eta^2/48+O(\eta^3).
\tag{33}
\]

For example, the scalar left weight in (5) is
1+a^2(1-z)(2-z)/2+O(a^3). Its integral is 1+5a^2/12+O(a^3), proving the B expression. In the (2,2) entry the right power adds a^2(z+z(z-1)/2); integrating gives an additional 5a^2/12 and hence 1+5a^2/6+O(a^3). Thus the discrepancies from (31) begin at eta^2/24 and eta^2/48, respectively. These expansions agree with the nonzero exact defect (30).

## 8. Normalization and scope

At tau=0, P=SI, M_0=tS^2 I and B_0=tS^2. Differentiating (5) at that point, or using the preceding finite-size layer derivative, gives

\[
\dot M_0=-t^2S^3\{(e^Tg_0)I+
\tfrac12(eg_0^T+g_0e^T)\},\qquad
\dot B_0=-t^2S^3e^Tg_0.
\tag{34}
\]

For instance dot P_0=-tS^2 e g_0^T, so dot(PP^T)_0=-tS^3(e g_0^T+g_0 e^T), and similarly for dot(P^TP)_0. At a scalar matrix the derivative of X^p is p(S^2)^{p-1} dot X; integrating z and 1-z gives (34). This is an independent endpoint derivation of the preceding rate. The absolute prefactor is t^2 and the rate relative to tS^2 has a t prefactor, with S held fixed. The law of S also depends on t.

For d=1, (3) becomes dot P=-tP^2 g and dot b=-h; for one input x=1, h=g=b+P-y. Formula (5) gives M=tP^2 and B=t Lambda(P^2,S^2), exactly the first report's scalar and perpendicular kernels. For zero residuals everything is stationary. For zero training inputs only b moves. The proof includes repeated singular values, negative targets, and non-spanning or zero data.

The closure applies after the small-step limit of the structured, scalar-identity model. Its matrix-power operator is the established balanced deep-linear flow; see Armin Eftekhari, *Training Linear Neural Networks: Non-Local Convergence and Complexity Results* (ICML 2020), and Nadav Cohen, Govind Menon, Zsolt Veraszto, *Deep Linear Networks for Matrix Completion -- An Infinite Depth Limit*, arXiv:2210.12497. The preceding profile supplies the unequal-gain random law, while (15)--(18) identify its flow kernel. None of these steps establishes stability under dense random initialization or activation-gate changes. The original joint Gaussian ReLU problem remains open within this work.
