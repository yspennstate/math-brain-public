Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.**

# PROB10-04 — finite-support covariance transport and a robust Díaz outer-ball compiler

Status: **analytic auxiliary theorem / source OPEN**. Nothing in this note changes the external explicit-decimal random-3-SAT bracket `[3.52,4.4898]`.

## 1. Finite block exponential families

Let `B` be a finite index set. For each block `b` let `m_b>0`, let `S_b subset R^d` be finite, and assign every `s in S_b` a weight `g_{b,s}>0`. Define

\[
A(\theta)=\sum_{b\in B}m_b\log Z_b(\theta),\qquad
Z_b(\theta)=\sum_{s\in S_b}g_{b,s}e^{\theta\cdot s}.
\tag{1.1}
\]

Write

\[
y(\theta)=\nabla A(\theta),\qquad
\Sigma(\theta)=\nabla^2A(\theta).
\tag{1.2}
\]

For each block, let `S_b(theta)` be a random state with Gibbs probability proportional to `g_{b,s}e^{theta·s}`. Then

\[
\Sigma(\theta)=\sum_bm_b\operatorname{Cov}_\theta(S_b).
\tag{1.3}
\]

For a natural-parameter displacement `delta` define the exact block-range seminorm

\[
R(\delta)=\max_{b\in B}\max_{s,t\in S_b}|\delta\cdot(s-t)|.
\tag{1.4}
\]

## 2. Main transport theorem

### Theorem 2.1 — multiplicative covariance transport

For every `theta_0,delta` and every `t in [0,1]`,

\[
\boxed{
e^{-tR(\delta)}\Sigma(\theta_0)
\preceq
\Sigma(\theta_0+t\delta)
\preceq
e^{tR(\delta)}\Sigma(\theta_0).
}
\tag{2.1}
\]

In particular, if `Sigma(theta_0)` is positive definite, every covariance on the segment is positive definite.

### Proof

Fix `x in R^d` and put

\[
g_x(t)=x^T\Sigma(\theta_0+t\delta)x.
\]

For block `b` set

\[
X_b=x\cdot S_b,\qquad Y_b=\delta\cdot S_b.
\]

Differentiating the block variance under exponential tilting gives

\[
{d\over dt}\operatorname{Var}_t(X_b)
=\mathbb E_t[(X_b-\mathbb E_tX_b)^2(Y_b-\mathbb E_tY_b)].
\tag{2.2}
\]

Indeed, differentiating `E_t X_b^2-(E_tX_b)^2` and using

\[
{d\over dt}\mathbb E_tf(S_b)=\operatorname{Cov}_t(f(S_b),Y_b)
\]

yields (2.2) after cancellation. Since `Y_b` is supported in an interval whose length is at most `R(delta)`, its mean lies in the same interval and therefore

\[
|Y_b-\mathbb E_tY_b|\le R(\delta).
\]

Consequently

\[
\left|{d\over dt}\operatorname{Var}_t(X_b)\right|
\le R(\delta)\operatorname{Var}_t(X_b).
\]

After multiplication by `m_b` and summation,

\[
|g_x'(t)|\le R(\delta)g_x(t).
\tag{2.3}
\]

If `g_x(0)=0`, (2.3) forces `g_x(t)=0`; otherwise Grönwall applied to `log g_x` gives

\[
e^{-tR(\delta)}g_x(0)\le g_x(t)\le e^{tR(\delta)}g_x(0).
\]

This holds for every `x`, which is exactly the Loewner-order statement (2.1). QED.

## 3. Inverting the mean map without solving multipliers

Let

\[
\Sigma_0=\Sigma(\theta_0),\qquad y_0=y(\theta_0),
\]

and assume `Sigma_0` is positive definite.

### Corollary 3.1 — Euclidean mean-ball transport

Let

\[
L=\max_{b,s,t}\|s-t\|_2,\qquad
\lambda_0=\lambda_{\min}(\Sigma_0).
\tag{3.1}
\]

If `y_1=y(theta_1)` and

\[
\rho=\|y_1-y_0\|_2<\lambda_0/L,
\]

then, with

\[
s={L\rho\over\lambda_0}<1,
\]

one has

\[
\boxed{(1-s)\Sigma_0\preceq\Sigma(\theta_1)
\preceq(1-s)^{-1}\Sigma_0.}
\tag{3.2}
\]

### Proof

Set `delta=theta_1-theta_0` and `q=||delta||_2`. Since `R(delta)<=Lq`, Theorem 2.1 along the segment gives

\[
\begin{aligned}
\delta\cdot(y_1-y_0)
&=\int_0^1\delta^T\Sigma(\theta_0+t\delta)\delta\,dt\\
&\ge \lambda_0q^2\int_0^1e^{-tLq}\,dt
={\lambda_0q\over L}(1-e^{-Lq}).
\end{aligned}
\tag{3.3}
\]

Cauchy--Schwarz gives `delta·(y_1-y_0)<=q rho`. If `q>0`, canceling `q` yields

\[
\rho\ge {\lambda_0\over L}(1-e^{-Lq}).
\]

Thus

\[
e^{-Lq}\ge1-{L\rho\over\lambda_0}=1-s,
\qquad e^{Lq}\le(1-s)^{-1}.
\]

Theorem 2.1 at `t=1` gives (3.2). The case `q=0` is trivial. QED.

## 4. Mahalanobis transport: the useful version here

The Euclidean diameter is crude for the Díaz variable blocks. Define

\[
L_*^2=\max_{b,s,t}(s-t)^T\Sigma_0^{-1}(s-t)
\tag{4.1}
\]

and, for mean displacement `z`,

\[
\|z\|_{\Sigma_0^{-1}}=\sqrt{z^T\Sigma_0^{-1}z}.
\]

### Theorem 4.1 — covariance-adapted mean-ball transport

If

\[
r_*:=\|y_1-y_0\|_{\Sigma_0^{-1}}<1/L_*,
\]

then with `s_*=L_*r_*<1`,

\[
\boxed{(1-s_*)\Sigma_0\preceq\Sigma(\theta_1)
\preceq(1-s_*)^{-1}\Sigma_0.}
\tag{4.2}
\]

### Proof

Again write `delta=theta_1-theta_0`, but now put

\[
q_0=\sqrt{\delta^T\Sigma_0\delta}.
\]

For every support difference `d=s-t`, Cauchy--Schwarz in the `Sigma_0` metric gives

\[
|\delta\cdot d|
\le q_0\sqrt{d^T\Sigma_0^{-1}d}
\le L_*q_0,
\]

so `R(delta)<=L_*q_0`. Theorem 2.1 therefore implies

\[
\begin{aligned}
\delta\cdot(y_1-y_0)
&\ge q_0^2\int_0^1e^{-tL_*q_0}\,dt\\
&={q_0\over L_*}(1-e^{-L_*q_0}).
\end{aligned}
\tag{4.3}
\]

Dual Cauchy--Schwarz gives

\[
\delta\cdot(y_1-y_0)
\le q_0\|y_1-y_0\|_{\Sigma_0^{-1}}
=q_0r_*.
\]

Canceling `q_0` when nonzero yields

\[
e^{-L_*q_0}\ge1-L_*r_*=1-s_*.
\]

Hence `e^{R(delta)}<=e^{L_*q_0}<=(1-s_*)^{-1}` and Theorem 2.1 gives (4.2). QED.

### Euclidean-ball consequence

If all that is known is `||y_1-y_0||_2<=rho`, then

\[
r_*\le\sqrt{\|\Sigma_0^{-1}\|_{op}}\,\rho.
\]

Thus it suffices to take

\[
\boxed{
s_*\le a_*\rho,\qquad
a_*:=L_*\sqrt{\|\Sigma_0^{-1}\|_{op}}.}
\tag{4.4}
\]

Unlike the crude coefficient `L/lambda_min(Sigma_0)`, the constant in (4.4) retains the actual orientation of the finite support differences.

## 5. Robust parallel-sum compiler for the Díaz outer problem

For PROB10-04, the inherited exact Hessian identity is

\[
\nabla^2\Phi(y)=D(y)^{-1}-\Sigma_V(y)^{-1}-\Sigma_C(y)^{-1}.
\tag{5.1}
\]

The preceding run proved: for any fixed real matrix `T`, strict positivity of

\[
M_T(y):=D(y)-T^T\Sigma_V(y)T-(I-T)^T\Sigma_C(y)(I-T)
\tag{5.2}
\]

implies `nabla^2 Phi(y) prec 0`.

Suppose a reference mean `y_0` obeys

\[
M_T(y_0)\succeq\eta_0I.
\tag{5.3}
\]

Let `s_V,s_C<1` be any valid covariance transport parameters on a mean ball `||y-y_0||_2<=rho`, i.e.

\[
\Sigma_V(y)\preceq(1-s_V)^{-1}\Sigma_{V,0},\qquad
\Sigma_C(y)\preceq(1-s_C)^{-1}\Sigma_{C,0}.
\tag{5.4}
\]

Put

\[
R_{V,0}=T^T\Sigma_{V,0}T,\qquad
R_{C,0}=(I-T)^T\Sigma_{C,0}(I-T).
\]

### Theorem 5.1 — robust outer-ball certificate

If `||D(y)-D(y_0)||_op<=L_D rho` on the ball and

\[
\boxed{
\Delta(\rho):=L_D\rho
+{s_V\over1-s_V}\|R_{V,0}\|_{op}
+{s_C\over1-s_C}\|R_{C,0}\|_{op}<\eta_0,
}
\tag{5.5}
\]

then for every realizable outer mean in the ball

\[
M_T(y)\succeq(\eta_0-\Delta(\rho))I\succ0,
\]

and therefore `nabla^2 Phi(y) prec 0` throughout that ball.

### Proof

From (5.4),

\[
T^T\Sigma_V(y)T\preceq(1-s_V)^{-1}R_{V,0},
\]

and analogously for the clause term. Also

\[
D(y)\succeq D(y_0)-L_D\rho I.
\]

Subtracting the two upper covariance bounds from the lower `D` bound, then using (5.3), gives

\[
M_T(y)\succeq M_T(y_0)-\Delta(\rho)I,
\]

which proves the claim. QED.

## 6. Exact copy-covariance Lipschitz constant

In the Díaz coordinates `y=(u,v,w)`,

\[
D(y)=\begin{pmatrix}
u(\lambda_p-u)/\lambda_p&0&0\\
0&v(\lambda_n-v)/\lambda_n&-vw/\lambda_n\\
0&-vw/\lambda_n&w(\lambda_n-w)/\lambda_n
\end{pmatrix}.
\tag{6.1}
\]

### Lemma 6.1

On the copy simplex,

\[
\boxed{\|D(y)-D(y')\|_{op}\le\sqrt6\,\|y-y'\|_2.}
\tag{6.2}
\]

### Proof

The derivative of the positive scalar block is `1-2u/lambda_p`, whose absolute value is at most one for `0<=u<=lambda_p`.

For the negative `2 x 2` block `B(v,w)`,

\[
\partial_vB=\begin{pmatrix}1-2v/\lambda_n&-w/\lambda_n\\-w/\lambda_n&0\end{pmatrix},
\]

and similarly with `v,w` exchanged for `partial_w B`. Every displayed normalized coordinate lies in `[0,1]`, hence each derivative has Frobenius norm at most `sqrt3`, and therefore operator norm at most `sqrt3`. Along a line segment,

\[
\|B(v,w)-B(v',w')\|_{op}
\le\sqrt3(|v-v'|+|w-w'|)
\le\sqrt6\sqrt{(v-v')^2+(w-w')^2}.
\]

Taking the maximum of the positive and negative block norms yields (6.2). QED.

## 7. Exact finite-support constants for the Díaz families

For the variable family at truncation `M=23`, a light block `(i,j)` has support

\[
S_{ij}=\{(i,0,0)\}\cup\{(0,k,j-k):1\le k\le j\},
\qquad1\le j\le i\le23.
\]

The largest Euclidean distance in any such block is attained between `(23,0,0)` and `(0,23,0)` and equals

\[
\boxed{L_V=23\sqrt2.}
\tag{7.1}
\]

The heavy-negative block has diameter `sqrt2` and is smaller.

For the clause family, one must compare states only **within the same syntactic positive-count class** `r=ps+pu`, because those are the separate log-sum-exp blocks. Exhausting the sixteen admissible extended clause types gives maximum squared Euclidean diameter

\[
\boxed{L_C^2=10.}
\tag{7.2}
\]

This finite enumeration will be preserved in the checker; it is not a probabilistic simulation.

The Mahalanobis constants are likewise finite maximizations over the same within-block support differences. They can therefore be certified exactly once a rational center covariance enclosure is supplied.

## 8. What the three attacks say

### Attack A: isotropic transport — succeeds, but is conservative

Equations (3.2), (5.5), (6.2), (7.1), and (7.2) already give a complete analytic compiler from a certified center covariance to a certified mean ball. No natural-parameter root solve is needed inside the ball.

### Attack B: Mahalanobis transport — succeeds and is strictly stronger at the inherited surrogate

Theorem 4.1 is not a heuristic; it is an exact replacement of the Euclidean diameter by a covariance-adapted support norm. On the inherited finite-decimal saddle surrogate, the finite support maximization is expected to reduce the variable transport coefficient substantially. The matching checker will record the exact rational surrogate values and a rigorous finite-decimal ball certificate separately from source claims.

### Attack C: one-center globalization — fails as a method

Both Corollary 3.1 and Theorem 4.1 necessarily require their transport parameter `s<1`. Thus any one-center certificate becomes vacuous once the mean leaves a finite local neighborhood whose radius is controlled by the smallest covariance direction and the extreme support differences. This is structural: rare high-degree variable states permit large natural-parameter motion for a small covariance eigenvalue. Consequently covariance transport can remove the **local** outer-grid burden, but it cannot by itself replace the global separation step.

The next method must therefore combine this local compiler with one of two genuinely different global devices: (i) a recentered cover pruned by the exact support oracles already proved in PROB10-04, or (ii) a direct upper bound on the outer exponent away from the saddle using a value gap rather than Hessian transport.

## 9. Scope

This note proves finite-dimensional convex-analytic statements only. To convert them into a new random-3-SAT upper endpoint one would still need all of the following at a lower density: an outward-certified center and covariance enclosure, the rescue-aware exponent itself, global separation of every feasible outer mean outside the local ball(s), and the original configuration-model-to-iid transfer. None of those remaining obligations is silently promoted here.