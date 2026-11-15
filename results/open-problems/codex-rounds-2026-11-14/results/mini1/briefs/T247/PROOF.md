# Exact second moments for independent gates and orthogonal weights

This result concerns the independent-gate surrogate. In a nonlinear network the derivative gates depend on the forward propagation and the weights. No replacement of those dependent gates by independent ones is proved here. Only the first two spectral moments are treated.

## 1. Model and exact formula

Fix integers n >= 1 and L >= 0. For each layer l, let O_l be Haar distributed on the real orthogonal group O(n). Let

\[
D_l=\operatorname{diag}(\sqrt{a_{l1}},\ldots,\sqrt{a_{ln}}),
\qquad a_{li}\geq 0.
\]

All O_l and all a_li are mutually independent. Within layer l the a_li are identically distributed, with

\[
\mathbb E a_{li}=1,\qquad
\mathbb E a_{li}^2=1+v_l<\infty.
\]

The numbers v_l are nonnegative and may depend on n and L. A weight variance can be absorbed into a_li. Define

\[
J_l=D_lO_l\cdots D_1O_1,\quad J_0=I_n,\quad
X_l=J_lJ_l^\top,
\]

\[
s_l=\mathbb E\frac{\operatorname{Tr}X_l^2}{n},\qquad
t_l=\mathbb E\left(\frac{\operatorname{Tr}X_l}{n}\right)^2,
\quad
P_l=\prod_{j=1}^l\left(1+\frac{3v_j}{n+2}\right).
\]

Empty products equal 1.

**Theorem.** At every finite n and l,

\[
\mathbb E\frac{\operatorname{Tr}X_l}{n}=1,
\qquad
s_l=1+\frac{n+2}{3}(P_l-1),
\qquad
t_l=1+\frac{n+2}{3n}(P_l-1).                 \tag{1}
\]

In particular, if

\[
Z_l=\frac1n\operatorname{Tr}(X_l-I_n)^2,
\]

then

\[
\mathbb E Z_l=\frac{n+2}{3}(P_l-1),\qquad
\operatorname{Var}\left(\frac{\operatorname{Tr}X_l}{n}\right)
=\frac{\mathbb E Z_l}{n}.                    \tag{2}
\]

The variance in (2) is the variance of the empirical mean eigenvalue across random realizations. It is distinct from the spectral variance within a realization.
In fact, the expected spectral variance about each realization's own empirical mean is

\[
\mathbb E\left[\frac{\operatorname{Tr}X_l^2}{n}
-\left(\frac{\operatorname{Tr}X_l}{n}\right)^2\right]
=s_l-t_l=\left(1-\frac1n\right)\mathbb E Z_l.
\]

### Proof of the Haar identity

Let u be uniform on the unit sphere in R^n. For n >= 2, put A = E u_1^4 and B = E u_1^2 u_2^2. Sign symmetry makes odd monomials have zero expectation. Rotating the first two coordinates gives

\[
A=\mathbb E\left(\frac{u_1+u_2}{\sqrt2}\right)^4
=\frac{2A+6B}{4},
\]

so A = 3B. Also

\[
1=\mathbb E\left(\sum_i u_i^2\right)^2=nA+n(n-1)B.
\]

Consequently

\[
\mathbb E u_i^4=\frac3{n(n+2)},\qquad
\mathbb E u_i^2u_j^2=\frac1{n(n+2)}\quad(i\ne j).
\]

For n = 1 the first identity also holds directly. If X is a fixed real symmetric matrix, diagonalize it and use rotational invariance. Writing T = Tr X and Q = Tr X^2 yields

\[
\mathbb E(u^\top Xu)^2=\frac{T^2+2Q}{n(n+2)}.       \tag{3}
\]

Every row of a Haar O has this sphere distribution. Thus, for B = OXO^top,

\[
\mathbb E_O\sum_i B_{ii}^2=\frac{T^2+2Q}{n+2}.     \tag{4}
\]

No independence of the rows is used.

### Proof of the recursion

Condition on X = X_(l-1) and O = O_l, and set B = OXO^top. With a_i = a_li,

\[
\operatorname{Tr}X_l=\sum_i a_i B_{ii},\qquad
\operatorname{Tr}X_l^2=\sum_{i,j}a_i a_j B_{ij}^2.
\]

Independence of the a_i, their mean 1, and their second moment 1 + v_l give

\[
\mathbb E_D\operatorname{Tr}X_l=T,
\]

\[
\mathbb E_D(\operatorname{Tr}X_l)^2
=T^2+v_l\sum_i B_{ii}^2,
\]

\[
\mathbb E_D\operatorname{Tr}X_l^2
=Q+v_l\sum_i B_{ii}^2.                       \tag{5}
\]

Here sum_ij B_ij^2 = Q because B is symmetric. Averaging (5) over O with (4) and then over X gives

\[
s_l=s_{l-1}+\frac{v_l}{n+2}(2s_{l-1}+nt_{l-1}),
\]

\[
t_l=t_{l-1}+\frac{v_l}{n(n+2)}(2s_{l-1}+nt_{l-1}). \tag{6}
\]

All required moments are finite by induction from X_0 = I. The first moment stays n by the first equation of (5). Equation (6) preserves

\[
s_l-nt_l=1-n.
\]

Substituting nt_(l-1) = s_(l-1) + n - 1 in (6),

\[
s_l+\frac{n-1}{3}
=\left(1+\frac{3v_l}{n+2}\right)
  \left(s_{l-1}+\frac{n-1}{3}\right).
\]

Since s_0 = t_0 = 1, iteration proves (1). Expanding Tr(X_l-I)^2 and using E Tr X_l = n proves (2). This completes the proof.

## 2. Explicit accumulated error

Put V = sum_(l=1)^L v_l and c = 3/(n+2). Nonnegativity and 1+x <= exp(x) give

\[
1+cV\leq P_L\leq e^{cV}.
\]

For y >= 0, Taylor's integral remainder gives

\[
e^y-1-y=\int_0^y(y-r)e^r\,dr\leq \frac{y^2}{2}e^y.
\]

It follows that

\[
0\leq \mathbb E Z_L-V
\leq\frac{3V^2}{2(n+2)}\exp\left(\frac{3V}{n+2}\right). \tag{7}
\]

Thus the fixed-depth free second-moment prediction s_free = 1 + V has an explicit finite-width error bound. To see this free prediction independently, write a mean-one positive free variable A as 1+A_0 and an independent free positive variable B of mean one as 1+B_0. In the expansion of tau(ABAB), all terms containing just one centered variable have trace zero; freeness also gives tau(A_0 B_0)=0, tau(A_0 B_0^2)=tau(A_0^2 B_0)=0, and tau(A_0 B_0 A_0 B_0)=0. The remaining terms give

\[
\tau(ABAB)=1+\tau(A_0^2)+\tau(B_0^2)
=\tau(A^2)+\tau(B^2)-1.
\]

Applying this identity layer by layer yields 1 + V. In (7) no freeness is assumed at finite width.

If V remains bounded as n tends to infinity, (7) is O(1/n), with no restriction on L(n) beyond the bound on V. If V > 0 and V/n tends to zero, the relative error in the spread E Z_L divided by V tends to zero.

For homogeneous v_l = v > 0,

\[
\mathbb E Z_L=\frac{n+2}{3}
 \left[\left(1+\frac{3v}{n+2}\right)^L-1\right].       \tag{8}
\]

The binomial expansion gives the lower bound

\[
\mathbb E Z_L-Lv\geq\frac{3v^2L(L-1)}{2(n+2)}.      \tag{9}
\]

Consequently, for fixed v > 0 and n,L tending to infinity, the absolute error between s_L and 1 + Lv tends to zero if and only if L^2/n tends to zero. Necessity follows from (9). For sufficiency, L^2/n -> 0 implies V^2/n -> 0 and V/n -> 0, so (7) applies. The relative error in the spread tends to zero if and only if L/n -> 0: divide (9) by Lv for necessity, and divide (7) by V for sufficiency. These are statements about this moment comparison, not necessary thresholds for weak spectral convergence.

For example, if L/n -> alpha in (0,infinity), then taking logarithms in (8) gives

\[
\frac{\mathbb E Z_L}{n}\longrightarrow
\frac{e^{3v\alpha}-1}{3},
\quad\text{whereas}\quad \frac{Lv}{n}\longrightarrow v\alpha.
\]

Indeed, log(1+3v/(n+2)) = 3v/(n+2) + O(n^-2), and L = O(n). This discrepancy already occurs for the second moment of independent gates. Nonzero limiting trace variance by itself is not a proof of nonconvergence in probability, since uniform integrability would also need checking.

## 3. A joint-limit empirical isometry regime

Let n tend to infinity, allow arbitrary L(n) tending to infinity, and allow triangular arrays of gate distributions as in Section 1. Then

\[
\mathbb E Z_{L(n)}\longrightarrow0
\quad\Longleftrightarrow\quad
V_n=\sum_{l=1}^{L(n)}v_{n,l}\longrightarrow0.          \tag{10}
\]

Necessity follows from E Z_L >= V. Sufficiency follows from (7).

Let mu_n be the empirical measure of the eigenvalues lambda_i of X_L (the squared singular values). Since the only coupling of mu_n with the point mass delta_1 sends every lambda_i to 1,

\[
W_2(\mu_n,\delta_1)^2
=\frac1n\sum_i(\lambda_i-1)^2=Z_L.
\]

If V_n -> 0, (10) and Markov's inequality prove W_2(mu_n,delta_1) -> 0 in probability. In particular, for every epsilon, eta > 0,

\[
\mathbb P\left\{\frac1n\#\{i:|\lambda_i-1|>\epsilon\}>\eta\right\}
\leq\frac{\mathbb E Z_L}{\eta\epsilon^2}\longrightarrow0.
\]

The singular values also concentrate empirically: for lambda >= 0,
|sqrt(lambda)-1| = |lambda-1|/(sqrt(lambda)+1) <= |lambda-1|.

A stronger sufficient condition for uniform control is n V_n -> 0. Indeed,

\[
\|X_L-I\|_{\mathrm{op}}^2\leq\operatorname{Tr}(X_L-I)^2=nZ_L,
\]

so (7) and Markov's inequality give ||X_L-I||_op -> 0 in probability under that stronger condition. No necessity for that condition is asserted.

### Independent tanh derivative example

Let G_li be independent standard real Gaussians, independent of the Haar matrices, and set, for q > 0,

\[
b_q(G)=\operatorname{sech}^4(\sqrt q\,G),\quad
\mu_q=\mathbb E b_q(G),\quad a_{li}=b_q(G_{li})/\mu_q.
\]

This is the squared tanh derivative divided by its mean, so E a_li = 1. It does not specify a self-consistent forward network. Its gate variance obeys

\[
v(q)=\operatorname{Var}(a_{li})=8q^2+o(q^2).         \tag{11}
\]

To prove the coefficient, use the identity 1-sech^4(x) = 2 tanh^2(x)-tanh^4(x) and |tanh(x)| <= |x|. Thus 0 <= 1-sech^4(x) <= 2x^2. Also tanh(x)/x -> 1 at zero, so

\[
\frac{b_q(G)-1}{q}\longrightarrow-2G^2,
\qquad \left|\frac{b_q(G)-1}{q}\right|\leq2G^2.
\]

Since E G^4 < infinity, this convergence holds in L^2 by dominated convergence. Therefore Var(b_q)/q^2 -> Var(-2G^2) = 4(3-1) = 8. Here E G^2=1 and E G^4=3 follow by integrating the Gaussian density by parts twice (the boundary terms vanish). Finally mu_q -> 1, and Var(a)=Var(b_q)/mu_q^2 proves (11).

For q_n -> 0, the exact joint-limit criterion (10) is consequently

\[
\mathbb E Z_{L(n)}\to0
\quad\Longleftrightarrow\quad L(n)q_n^2\to0.        \tag{12}
\]

No relation between n and L(n) is needed for this expected empirical distortion criterion in the independent-gate model.

## 4. Empirical isometry need not control the least singular value

Take n >= 2, p_n = 1-1/n, L_n = floor(sqrt(n)), and independent gates

\[
a_{li}=\begin{cases}1/p_n&\text{with probability }p_n,\\
0&\text{with probability }1-p_n.\end{cases}
\]

Then v_n = 1/p_n-1 = 1/(n-1), and V_n = L_n/(n-1) -> 0. The empirical isometry conclusion in Section 3 holds. However, a product of square matrices is invertible if and only if every factor is invertible. All O_l are invertible, and D_l is invertible exactly when its n Bernoulli gates are nonzero. Independence therefore gives

\[
\mathbb P\{s_{\min}(J_{L_n})>0\}
=p_n^{nL_n}\leq e^{-L_n}\longrightarrow0.             \tag{13}
\]

Thus the least singular value equals zero with probability tending to one, even though the empirical squared-singular-value measure converges to delta_1 in W_2 in probability. This does not contradict (10): a vanishing fraction of singular values can account for a kernel. A full-spectrum isometry theorem needs additional control beyond an empirical second moment.

## 5. Independent derivation of the product factor

Fix a deterministic unit vector x. Conditional on J_(l-1)x, its image under the independent Haar O_l is uniform on the sphere of radius ||J_(l-1)x||. This remains valid with the fourth-moment identity interpreted as zero when that vector is zero. For unit uniform u independent of a_li,

\[
\mathbb E\left(\sum_i a_{li}u_i^2\right)^2
=1+v_l\sum_i\mathbb E u_i^4
=1+\frac{3v_l}{n+2}.
\]

Conditional iteration gives

\[
\mathbb E\|J_Lx\|^4=P_L.                            \tag{14}
\]

Average also over an independent uniform unit vector x. Equation (3), applied to J_L^top J_L, gives

\[
\mathbb E\|J_Lx\|^4
=\frac{nt_L+2s_L}{n+2}.
\]

Combining this with nt_L = s_L+n-1 reproduces (1). This derivation checks the factor 3/(n+2) by a single-vector norm calculation rather than by solving the two-trace recursion. At n = 1, (1) reduces to s_L = product_l(1+v_l), as required directly for a scalar product.
