# A matrix depth profile for a jointly deep and wide linear network

The initialization is scalar times the identity, as in the earlier work. Training on noncollinear inputs produces a noncommuting matrix block. The limit below closes on a continuous matrix function of depth. It does not close on a single matrix, and it is not a result for Gaussian matrix initialization or ReLU networks.

## 1. Model and limiting recursion

Fix an integer d, a unit vector e in R^d, training inputs x_1,...,x_q in R^d, targets y_i in R, positive weights alpha_i summing to one, and a learning rate eta>0. Embed R^d as the first d coordinates E of R^n. The readout is the fixed embedded vector e. Let

\[
L=L_n,\qquad L/n\longrightarrow t\in(0,\infty),\qquad
W_l=\Theta_l/\sqrt n,
\]
\[
f(x)=b+e^T W_L\cdots W_1x,\qquad
\mathcal L=\frac12\sum_{i=1}^q\alpha_i(f(x_i)-y_i)^2.
\]

All entries of all Theta_l and b are trained by simultaneous Euclidean gradient descent. Initialize b=0 and

\[
W_l=s_l I_n,\qquad
s_l=\exp(\mu/n+\sigma Z_l/\sqrt n),\qquad
Z_l\overset{\mathrm{iid}}\sim N(0,1).
\tag{1}
\]

Here mu is real and sigma>0. The deterministic theorem below also covers sigma=0.

Draw a single positive random variable

\[
S=\exp(\mu t+\sigma\sqrt t\,Z),\qquad Z\sim N(0,1).
\tag{2}
\]

The limiting state at step k is a scalar b_k and a continuous function C_k:[0,1]->R^{d by d}. Set b_0=0 and C_0(z)=0. Given this state, solve the ordinary differential equation in normalized depth z,

\[
\partial_z U_k(z)=t C_k(z)U_k(z),\qquad U_k(0)=I_d,
\qquad V_k(z)=U_k(1)U_k(z)^{-1}.
\tag{3}
\]

Define

\[
r_{i,k}=b_k+S e^T U_k(1)x_i-y_i,\qquad
h_k=\sum_i\alpha_i r_{i,k},\qquad
g_k=\sum_i\alpha_i r_{i,k}x_i.
\tag{4}
\]

The closed training update is

\[
\boxed{\begin{split}
b_{k+1}&=b_k-\eta h_k,\\
C_{k+1}(z)&=C_k(z)-\eta S
 V_k(z)^T e\,g_k^T U_k(z)^T.
\end{split}}
\tag{5}
\]

For test inputs x=x_E+x_perp and x'=x'_E+x'_perp, put

\[
w_k(z)=\|V_k(z)^T e\|^2,
\]
\[
M_k=tS^2\int_0^1 w_k(z)U_k(z)^T U_k(z)\,dz,
\qquad
B_k=tS^2\int_0^1 w_k(z)\,dz.
\tag{6}
\]

**Theorem.** At every fixed finite set of training steps, jointly in outputs and full Euclidean NTKs,

\[
f_n^k(x)\ \Rightarrow\ b_k+S e^T U_k(1)x_E,
\]
\[
K_n^k(x,x')\ \Rightarrow\
1+x_E^T M_k x'_E+B_k\langle x_\perp,x'_\perp\rangle.
\tag{7}
\]

For input sequences depending on n, it suffices that their E coordinates and their perpendicular pairwise inner products converge. Only finitely many test inputs are asserted at once. Equations (2)--(6) give their joint law: all randomness is the one variable S. The recursion is function valued, with a fixed d by d matrix at each depth; it has no hierarchy of increasing tensor order. No claim about an unbounded number of training steps is made.

## 2. Exact block invariance and finite-size identities

Suppose at one step

\[
W_l=A_l\oplus s_l I_{n-d}.
\tag{8}
\]

For a training input both the forward vector and backward vector lie in E. Their outer product is supported in the E by E block. Thus the gradient vanishes outside that block. This proves (8) at every step, since it holds initially.

Normalize the active factors by

\[
D_l=A_l/s_l=I_d+C_l/n,
\qquad Q_j=D_j\cdots D_1,\quad Q_0=I_d,
\qquad R_l=D_L\cdots D_{l+1},\quad R_L=I_d,
\qquad S_n=\prod_{l=1}^L s_l.
\tag{9}
\]

No inverse of a finite-size D_l is needed. The training outputs and their aggregate derivatives are

\[
f_n(x_i)=b+S_n e^T Q_Lx_i,\quad
r_{i,n}=f_n(x_i)-y_i,\quad
h_n=\sum_i\alpha_i r_{i,n},\quad
g_n=\sum_i\alpha_i r_{i,n}x_i.
\]

The forward activation before layer l is (prod_{j<l}s_j)Q_{l-1}x_i. The backward vector after that layer is (prod_{j>l}s_j)R_l^T e. Therefore the derivative of the loss with respect to the active W_l block is

\[
\nabla_{A_l}\mathcal L
=\frac{S_n}{s_l}R_l^T e\,g_n^T Q_{l-1}^T.
\]

Euclidean descent in Theta_l corresponds to an update -eta/n times this derivative in W_l. Multiplying the active update by n/s_l gives the exact recursion

\[
C_l^+=C_l-\eta\frac{S_n}{s_l^2}
 R_l^T e\,g_n^T Q_{l-1}^T,\qquad
b^+=b-\eta h_n.
\tag{10}
\]

In particular all separate partial scalar products have canceled; only S_n and the local factor s_l^{-2} remain. This cancellation uses the scalar-identity initialization and does not hold for arbitrary matrix-valued initial factors.

For any test input, including one outside E,

\[
\nabla_{\Theta_l}f(x)
=\frac1{\sqrt n}(W_L\cdots W_{l+1})^Te
                 (W_{l-1}\cdots W_1x)^T.
\]

The Frobenius inner product of gradients at x,x' is the squared backward norm times the inner product of the forward vectors, divided by n. The E and E-perpendicular forward vectors are orthogonal. Consequently the exact full kernel is

\[
K_n(x,x')=1+x_E^T M_nx'_E+B_n\langle x_\perp,x'_\perp\rangle,
\tag{11}
\]
\[
M_n=\frac{S_n^2}{n}\sum_{l=1}^L s_l^{-2}
 \|R_l^Te\|^2 Q_{l-1}^TQ_{l-1},\qquad
B_n=\frac{S_n^2}{n}\sum_{l=1}^L s_l^{-2}\|R_l^Te\|^2.
\tag{12}
\]

The term B_n includes derivatives with respect to entries whose input index is outside E and output index is inside E. Those parameters do not move on the training set, but they remain trainable and contribute to the test kernel. Restricting the parameter space to the active block would remove this term and would be a different model.

## 3. Uniform convergence of ordered products

The following deterministic fact fixes the order of multiplication in (3). Let z_l=(l-1)/L and suppose a continuous matrix function C satisfies

\[
\max_{l\le L}\|C_l-C(z_l)\|\longrightarrow0.
\tag{13}
\]

For D_l=I+C_l/n and Q_j as in (9), let U solve U'=tCU, U(0)=I. Then

\[
\max_{0\le j\le L}\|Q_j-U(j/L)\|\longrightarrow0,
\]
\[
\max_{l\le L}\|R_l-V(z_l)\|\longrightarrow0,
\qquad V(z)=U(1)U(z)^{-1}.
\tag{14}
\]

Here and below use the operator norm. To prove the first assertion, (13) bounds all C_l by some M. Every product of at most L factors has norm at most

\[
(1+M/n)^L\le \exp(M L/n).
\tag{15}
\]

Continuity of C and the integral equation for U give, uniformly in l,

\[
U(l/L)=\left(I+\frac tL C(z_l)\right)U(z_l)+\rho_l,
\qquad \max_l\|\rho_l\|=o(1/L).
\tag{16}
\]

Indeed, subtract the first-order term from the integral of t C(v)U(v) over [z_l,l/L]. Uniform continuity of C(v)U(v) makes the integrand error o(1), so its integral is o(1/L). Subtracting (16) from Q_l=(I+C_l/n)Q_{l-1}, and using (15), bounds the total error by a constant times

\[
\frac Ln\max_l\|C_l-C(z_l)\|
+\left|\frac Ln-t\right|\max_z\|C(z)\|
+L\max_l\|\rho_l\|,
\]

which tends to zero. This estimate follows by iterating the one-step error inequality and bounding every multiplying product by (15).

For the suffix assertion, solve V'=-tVC with V(1)=I. Its existence follows from the same finite-dimensional linear ODE theorem. Differentiating VU shows V(z)U(z)=U(1), so it equals the expression in (14). U is invertible: the solution H'=-tHC, H(0)=I satisfies (HU)'=0, hence H=U^{-1}. Backward iteration of

\[
R_{l-1}=R_l(I+C_l/n),\qquad R_L=I
\]

and the corresponding integral equation for V gives the same estimate as above, with R_l approximating V(l/L). Replacing l/L by z_l costs o(1), uniformly, by continuity. This proves (14) without assuming invertibility of any finite D_l.

## 4. Deterministic training limit

Assume

\[
L/n\to t>0,\qquad
\max_l|s_l-1|\to0,\qquad
S_n=\prod_l s_l\to S\in(0,\infty).
\tag{17}
\]

Starting from C_l^0=0 and b_n^0=0, prove by induction on each fixed k that

\[
b_n^k\to b_k,\qquad
\max_l\|C_l^k-C_k(z_l)\|\to0.
\tag{18}
\]

The statement is immediate at k=0. If it holds at k, (14) gives uniform convergence of the prefixes and suffixes to U_k and V_k. Hence the finite outputs, h_n and g_n converge to (4). The factors S_n/s_l^2 converge to S uniformly in l by (17). Applying the exact update (10) proves (18) at k+1 with (5). The function C_{k+1} is continuous because C_k, U_k and V_k are continuous. Every such function is bounded on [0,1]; linear ODEs (3) therefore exist on this whole interval. Finite induction defines the limit at any prescribed finite training horizon, without a uniform-in-k assertion.

The summands in (12) now converge uniformly to the continuous integrands in (6). Write 1/n=(L/n)/L and apply left Riemann sums on [0,1]. This proves (6)--(7) under (17). The argument also proves joint convergence over any fixed finite set of k, since it is the same deterministic induction.

## 5. The random law

The normal sum in (1) gives exactly

\[
\log S_n\sim N(\mu L/n,\sigma^2 L/n).
\tag{19}
\]

For each fixed epsilon>0, for all sufficiently large n,

\[
\Pr\left(\max_l|\log s_l|>\varepsilon\right)
\le 2L\exp\left(-\frac{n\varepsilon^2}{8\sigma^2}\right).
\tag{20}
\]

This is the union bound and the normal tail estimate, after bounding |mu|/n by epsilon/2. The right side is summable in n because L=O(n).

One coupling makes the application of the deterministic theorem explicit. Draw one standard normal Z. For each n draw L independent standard normals xi_{n,l}, independent of Z, and set

\[
Z_{n,l}=\xi_{n,l}-\bar\xi_n+Z/\sqrt L.
\]

At each n the vector is jointly Gaussian with covariance
(I-11^T/L)+11^T/L=I. Its entries are thus independent standard normals. Its sum is sqrt(L) Z, so S_n=exp(mu L/n+sigma sqrt(L/n) Z) converges almost surely to (2). By (20) and the first Borel--Cantelli lemma, applied to every positive rational epsilon, max_l|log s_l| tends to zero almost surely as well. These are (17). Section 4 applies pathwise on this coupling and proves the claimed convergence in distribution for the original initialization law.

## 6. Check against the earlier one-example result

For d=1, e=1 and the single training input x=1, the recursion preserves a depth-independent scalar C_k(z)=c_k. Indeed,

\[
U_k(z)=e^{tc_kz},\qquad V_k(z)=e^{tc_k(1-z)},
\qquad V_k(z)U_k(z)=e^{tc_k}.
\]

Thus P_k=S exp(tc_k), and (5) becomes

\[
c_{k+1}=c_k-\eta P_k(b_k+P_k-y),\qquad
b_{k+1}=b_k-\eta(b_k+P_k-y).
\]

Equation (6) gives M_k=tP_k^2 and

\[
B_k=tS^2\int_0^1e^{2tc_k(1-z)}dz
=S^2\int_0^t e^{2c_ku}du.
\]

These reproduce the earlier full kernel, including its perpendicular coefficient. At k=0 the present theorem gives K_0(x,x')=1+tS^2<x,x'> for every d.

## 7. An explicit off-diagonal change and failure of the common-block ansatz

The first step is explicit for arbitrary training data. Let g=g_0, h=h_0. Since U_0=V_0=I,

\[
C_1(z)=-\eta S e g^T,\qquad b_1=-\eta h,
\]
\[
U_1(z)=\exp(-\eta St z e g^T),\qquad
V_1(z)=\exp(-\eta St(1-z)e g^T).
\tag{21}
\]

These formulas inserted in (6) give the exact first-step kernel for every eta. Define the initial rate as the one-step directional derivative

\[
\dot M_0:=\lim_{\eta\downarrow0}\frac{M_1-M_0}{\eta},
\qquad
\dot B_0:=\lim_{\eta\downarrow0}\frac{B_1-B_0}{\eta}.
\]

This definition requires neither convergence for many small steps nor interchange of a size limit with a time derivative. Expanding (21) uniformly in z gives

\[
\|V_1(z)^Te\|^2
=1-2\eta St(1-z)e^Tg+O(\eta^2),
\]
\[
U_1(z)^TU_1(z)
=I-\eta Stz(eg^T+ge^T)+O(\eta^2).
\]

Integrating z and 1-z, both with integral 1/2, yields

\[
\boxed{\begin{split}
\dot M_0&=-t^2S^3\left[(e^Tg)I_d+
                     \frac12(eg^T+ge^T)\right],\\
\dot B_0&=-t^2S^3 e^Tg.
\end{split}}
\tag{22}
\]

The absolute rate has a t^2 prefactor. Dividing by the initial matrix-weight coefficient tS^2 gives a t prefactor. This comparison fixes S and the training data while varying t; in the random model the distribution of S also depends on t. Setting g=(S-y)e recovers the earlier parallel and perpendicular rates, -2t^2S^3(S-y) and -t^2S^3(S-y).

For a concrete two-dimensional example, take t=S=1, e=e_1, equal training weights 1/2, inputs e_1,e_2, and targets 1,1. This is a valid deterministic array in (17), for example s_l=1 and L=n. It is also a conditional benchmark for the random-law formulas; no positive probability of the event S=1 is claimed when sigma>0. Here

\[
g=(0,-1/2)^T,\quad h=-1/2,\quad
C_1=\frac\eta2 e_1e_2^T,\quad b_1=\eta/2.
\]

The matrix e_1 e_2^T is nilpotent. Consequently

\[
U_1(z)=\begin{pmatrix}1&\eta z/2\\0&1\end{pmatrix},
\quad
V_1(z)^Te_1=\begin{pmatrix}1\\\eta(1-z)/2\end{pmatrix},
\]
\[
U_1(z)^TU_1(z)=
\begin{pmatrix}1&\eta z/2\\\eta z/2&1+\eta^2z^2/4\end{pmatrix}.
\]

Equation (6) is now polynomial integration. Using
integral_0^1 (1-z)^2 dz=1/3,
integral_0^1 z(1-z)^2 dz=1/12, and
integral_0^1 z^2(1-z)^2 dz=1/30, gives

\[
\boxed{M_1=
\begin{pmatrix}
1+\eta^2/12&\eta/4+\eta^3/96\\
\eta/4+\eta^3/96&1+\eta^2/6+\eta^4/480
\end{pmatrix},\qquad B_1=1+\eta^2/12.}
\tag{23}
\]

Both diagonal first derivatives vanish, whereas the off-diagonal first derivative is 1/4. The full training kernel is 11^T+M_1, so its off-diagonal entry changes by eta/4+eta^3/96. A test restricted to diagonal kernel rates would miss the leading change in this example.

The common-block ansatz stops being invariant at the next step. At step one,

\[
r_{1,1}=\eta/2,\quad r_{2,1}=\eta-1,\quad
g_1=(\eta/4,(\eta-1)/2)^T.
\]

The second component of V_1(z)^Te_1 is eta(1-z)/2. The second component of U_1(z)g_1 is (eta-1)/2. Therefore the (2,2) entry in the outer product in (5) is eta(1-z)(eta-1)/4, and

\[
\boxed{(C_2(z))_{22}=\frac{\eta^2(1-\eta)}4(1-z).}
\tag{24}
\]

For 0<eta<1 this is nonconstant in depth. Thus replacing the scalar c_k by a single common matrix C_k is already false after two updates. Equations (3)--(6) retain the depth dependence needed for this example. This does not rule out other finite-dimensional descriptions with additional variables.

There is also genuine noncommutativity. Computing the other entries in the same outer product gives

\[
C_2(0)=\begin{pmatrix}
-\eta^2/4&\eta(2-\eta)/2\\
-\eta^3/8&\eta^2(1-\eta)/4
\end{pmatrix},\qquad
C_2(1)=\begin{pmatrix}
-\eta^3/4&\eta(2-\eta)/2\\0&0
\end{pmatrix}.
\]

The (2,1) entry of C_2(0)C_2(1) is eta^6/32, whereas the (2,1) entry of C_2(1)C_2(0) is zero. Their commutator is therefore nonzero for every eta>0. Ordinary exponentiation of the average profile cannot be substituted for the ordered-product solution (3) without a separate argument.

## 8. Independent finite-size derivation of the initial rate

Equation (22) can also be obtained before taking the size limit. At initialization D_l=I. Let g_n be the initial residual vector sum from Section 2. Differentiating the exact update (10) at eta=0 gives

\[
\dot D_l=-\frac{S_n}{n s_l^2} e g_n^T.
\]

Hence

\[
\dot Q_{l-1}=-\frac{S_n}{n}\sum_{j<l}s_j^{-2}eg_n^T,
\qquad
\dot R_l=-\frac{S_n}{n}\sum_{j>l}s_j^{-2}eg_n^T.
\]

In (12), the scalar S_n remains the fixed initial normalization; its derivative is zero. Differentiating the backward norm gives

\[
\left.\frac d{d\eta}\|R_l^Te\|^2\right|_0
=-\frac{2S_n}{n}(e^Tg_n)\sum_{j>l}s_j^{-2}.
\]

Let

\[
J_n=\sum_{1\le j<l\le L}s_j^{-2}s_l^{-2}
=\frac12\left[\left(\sum_l s_l^{-2}\right)^2-
                        \sum_l s_l^{-4}\right].
\]

The forward and backward unordered-pair sums coincide, so direct differentiation of (12) yields exactly

\[
\dot M_n=-\frac{S_n^3J_n}{n^2}
       \left[2(e^Tg_n)I_d+eg_n^T+g_ne^T\right],\quad
\dot B_n=-\frac{2S_n^3J_n}{n^2}e^Tg_n.
\tag{25}
\]

Under (17), n^{-1}sum_l s_l^{-2}->t and n^{-2}sum_l s_l^{-4}->0, so J_n/n^2->t^2/2. Also g_n->g. Substitution in (25) gives (22) independently of differentiating any limiting integral.

## Scope

The new conclusion is a full-kernel joint-limit recursion for a fixed block with multiple training directions, with an explicit two-dimensional example of off-diagonal kernel change. The closure is a deterministic depth profile driven by a single lognormal initial variable. Scalar gains cancel because they commute with every active block. No estimate here controls an initial perturbation outside this structure. Independent Gaussian matrix entries, activation gates, an increasing active dimension, and an increasing training horizon require separate arguments.
