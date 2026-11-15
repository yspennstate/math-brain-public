# A closed joint-limit law for an aligned deep linear network

This is a special initialization and a single-example training problem. It is not a theorem for independent Gaussian weight matrices or for ReLU networks.

## Model and statement

Let $L=L_n$, $L/n\to t\in(0,\infty)$. Each of the $L$ matrices has size $n\times n$. The parameters are the entries of $\Theta_1,\ldots,\Theta_L$ and a scalar $b$. Define

\[
 W_l=\Theta_l/\sqrt n,\qquad
 f(x)=b+e_1^T W_L\cdots W_1x.
\]

The readout $e_1$ is fixed. There are no hidden biases. Initialize

\[
 b=0,\quad W_l=s_l I_n,\quad
 s_l=\exp(\mu/n+\sigma Z_l/\sqrt n),\qquad Z_l\stackrel{\mathrm{iid}}\sim N(0,1),
\]

where $\mu\in\mathbb R$, $\sigma>0$ are fixed. Train on the one example $ (e_1,y)$ using the loss $\tfrac12(f(e_1)-y)^2$. Ordinary simultaneous gradient descent in **all entries** of the $\Theta_l$ and in $b$ uses a fixed learning rate $\eta>0$. Let $K_n^k$ be the ordinary Euclidean NTK after $k$ steps.

**Theorem.** For each fixed integer $m\geq0$, the joint law of the outputs and kernels at steps $0,\ldots,m$ has the following limit. Draw one variable

\[
 S=\exp(\mu t+\sigma\sqrt t\,Z),\qquad Z\sim N(0,1).
\]

Set $b_0=c_0=0$, and recursively define

\[
 P_k=S e^{t c_k},\quad r_k=b_k+P_k-y,
 \qquad b_{k+1}=b_k-\eta r_k,
 \qquad c_{k+1}=c_k-\eta P_k r_k.                 \tag{1}
\]

Write $x=x_1e_1+x_\perp$, and likewise for $x'$.  Then

\[
 f_k(x)=b_k+P_kx_1,
\]
\[
 K^k(x,x')=1+A_kx_1x'_1+B_k\langle x_\perp,x'_\perp\rangle,       \tag{2}
\]
\[
 A_k=tP_k^2,\qquad
 B_k=S^2\int_0^t e^{2c_ku}\,du
     =tS^2H(2tc_k),                                      \tag{3}
\]

where $H(z)=(e^z-1)/z$ for $z\ne0$ and $H(0)=1$.
The convergence in (2) means joint convergence for any finite collection of deterministic input sequences whose first coordinates and perpendicular pairwise inner products converge. In particular it applies to inputs in any fixed coordinate subspace embedded in \(\mathbb R^n\).

No stability or convergence of (1) as $k\to\infty$ is asserted. The horizon $m$ is fixed before the size limit.

## 1. Exact finite-dimensional orbit

Put $E=e_1e_1^T$. At every step the matrices have the form

\[
 W_l=s_l I_n+(a_l-s_l)E.                                  \tag{4}
\]

Indeed, (4) holds initially with $a_l=s_l$. Under (4), the forward activation of the training input before layer $l$ is
\((\prod_{j<l}a_j)e_1\), and the backward vector after that layer is
\((\prod_{j>l}a_j)e_1\). Thus

\[
 \nabla_{\Theta_l}f(e_1)
 =\frac1{\sqrt n}\left(\prod_{j\ne l}a_j\right)E.
\]

Only the $E$ component changes, proving invariance. Let $P=\prod_l a_l$ and $r=b+P-y$. As long as every $a_l\ne0$, the exact update is

\[
 a_l^+=a_l-\frac\eta n r\frac P{a_l},\qquad b^+=b-\eta r.   \tag{5}
\]

Without division, the first update in (5) is
\(a_l^+=a_l-(\eta/n)r\prod_{j\ne l}a_j\), which is valid also at zeros. All asymptotic uses below take place where $a_l>0$.

## 2. Exact NTK, including orthogonal test inputs

For a general input $x$, the activation before layer $l$ is

\[
 v_{l-1}(x)=\left(\prod_{j<l}a_j\right)x_1e_1
       +\left(\prod_{j<l}s_j\right)x_\perp.
\]

The backward vector is $ (\prod_{j>l}a_j)e_1$. Consequently

\[
 \nabla_{\Theta_l} f(x)
 =\frac1{\sqrt n}\left(\prod_{j>l}a_j\right)e_1v_{l-1}(x)^T.
\]

The Frobenius inner product of two such gradients is
\(n^{-1}(\prod_{j>l}a_j^2)\langle v_{l-1}(x),v_{l-1}(x')\rangle\).
The bias derivative is one. Summing proves the exact form (2) with

\[
 A_n=\frac{P^2}{n}\sum_{l=1}^L a_l^{-2},\qquad
 B_n=\frac1n\sum_{l=1}^L
           \left(\prod_{j>l}a_j^2\right)
           \left(\prod_{j<l}s_j^2\right).                  \tag{6}
\]

In particular $K_n(e_1,e_1)=1+A_n$. Although the output along (4) depends only on $x_1$, the NTK contains a perpendicular term: derivatives with respect to off-diagonal matrix entries contribute to it. Restricting the trainable parameters to the diagonal would give a different kernel.

## 3. Deterministic triangular-array limit

The following deterministic argument handles the training limit. Assume

\[
 t_n=L/n\to t>0,\quad \epsilon_n=\max_{l\le L}|s_l-1|\to0,
 \quad S_n=\prod_l s_l\to S\in(0,\infty).                \tag{7}
\]

For every fixed $k$, the updates (5) satisfy

\[
 b_n^k\to b_k,\quad P_n^k\to P_k,\quad
 \max_{l\le L}\left|n(a_l^k-s_l)-c_k\right|\to0,          \tag{8}
\]

with (1). This is proved by induction. At $k=0$, (8) follows directly from (7). Suppose it holds at step $k$. Then \(\max_l|a_l^k-1|\to0\), so every $a_l^k$ is positive and bounded away from zero for sufficiently large $n$. Multiplying (5) by $n$ gives

\[
 n(a_l^{k+1}-s_l)
 =n(a_l^k-s_l)-\eta r_n^kP_n^k/a_l^k.
\]

The last term converges uniformly in $l$ to \(-\eta r_kP_k\), giving the third assertion of (8) at $k+1$. The bias update gives its first assertion.

To obtain the product assertion at that step, write
\(a_l=s_l+(c+\delta_l)/n\), with \(\max_l|\delta_l|\to0\) and $c=c_{k+1}$. For large $n$, Taylor's formula on a fixed neighborhood of zero yields

\[
 \log(a_l/s_l)=\frac{c+\delta_l}{ns_l}+O(n^{-2}),          \tag{9}
\]

uniformly in $l$. Summation gives

\[
 \log(P_n/S_n)
 =\frac c n\sum_l s_l^{-1}+o(L/n)+O(L/n^2)
 \longrightarrow tc.
\]

This proves \(P_n\to Se^{tc}\) and completes the induction. The same estimate, summed over any suffix, gives the stronger uniform statement

\[
 \max_{0\le l\le L}
 \left|\log\prod_{j=l+1}^L(a_j/s_j)
                  -c(L-l)/n\right|\longrightarrow0.     \tag{10}
\]

Every induction step uses only finitely many finite real limits. Positivity at a fixed finite horizon therefore follows from (8), without a global bound on all training times or all initial $S$.

By (8), the first expression in (6) tends to $tP_k^2$. Rewriting the second expression gives

\[
 B_n=\frac{S_n^2}{n}\sum_{l=1}^L
     s_l^{-2}\exp\left(2\log\prod_{j>l}(a_j/s_j)\right).
\]

Uniform convergence in (7) and (10), followed by a Riemann sum with spacing $1/n$, gives

\[
 B_n\longrightarrow S^2\int_0^t e^{2cu}\,du.
\]

This proves (1)–(3) under (7).

## 4. Random initialization and joint convergence

The sum of the independent normal log gains is exactly normal:

\[
 \log S_n\sim N(\mu t_n,\sigma^2t_n).
\]

Moreover \(\max_l|\log s_l|\to0\) in probability. For any fixed \(\varepsilon>0\), once \(|\mu|/n<\varepsilon/2\), the union bound and the normal tail bound give

\[
 \Pr\{\max_l|\log s_l|>\varepsilon\}
 \le 2L\exp[-n\varepsilon^2/(8\sigma^2)]\longrightarrow0.
\]

For completeness, an explicit coupling turns the deterministic argument into distributional convergence. For each $n$, draw independent normals \(\xi_{n,1},\ldots,\xi_{n,L}\) and one common independent \(Z\sim N(0,1)\). Define

\[
 Z_{n,l}=\xi_{n,l}-\bar\xi_n+Z/\sqrt L.
\]

For each $n$, this vector is jointly Gaussian with covariance $I_L$: the centered component has covariance $I_L-\mathbf1\mathbf1^T/L$, and the common component has covariance \(\mathbf1\mathbf1^T/L\). Thus its entries are independent standard normals, as required. Its sum is \(\sqrt L Z\), so

\[
 S_n=\exp(\mu t_n+\sigma\sqrt{t_n}Z)\longrightarrow S
\]

almost surely. The displayed exponential tail bound is summable in $n$, since $L=O(n)$. The first Borel–Cantelli lemma therefore gives \(\max_l|\log s_l|\to0\) almost surely on this coupling, hence (7). Applying Section 3 pathwise proves the claimed joint convergence. The finite collection of input inner products then passes through (2) by continuity.

## 5. Kernel change and the role of the aspect ratio

At initialization, $A_0=B_0=tS^2$, so

\[
 K^0(x,x')=1+tS^2\langle x,x'\rangle.
\]

The random coefficient $A_0$ is lognormal, with

\[
 \log A_0\sim N(\log t+2\mu t,4\sigma^2t),\quad
 \mathbb E A_0=t e^{(2\mu+2\sigma^2)t},\quad
 \frac{\operatorname{Var}(A_0)}{(\mathbb E A_0)^2}
       =e^{4\sigma^2t}-1.                                \tag{11}
\]

After the first discrete GD step,

\[
 P_1=S\exp[-\eta tS(S-y)],\quad
 K^1(e_1,e_1)-K^0(e_1,e_1)
 =tS^2\{\exp[-2\eta tS(S-y)]-1\}.                       \tag{12}
\]

For $t,\eta,\sigma>0$, this change is nonzero almost surely, because $S>0$ has a continuous distribution and the only possible zero is $S=y$. Thus this model has feature learning in the sense of a nonconstant NTK, without any claim about nonlinear representation learning.

Taking the small-step limit of the closed recursion (1) on a bounded time interval on which its ODE exists gives

\[
 \dot b=-r,\quad \dot c=-Pr,\quad
 P=Se^{tc},\quad r=b+P-y,\quad \dot P=-tP^2r.           \tag{13}
\]

This is a consequence of the usual Euler approximation for the smooth right-hand side in $(b,c)$: on any compact neighborhood of the ODE path its derivative is bounded, the one-step local error is $O(\eta^2)$, and iterating the Lipschitz error bound gives $O(\eta)$ at fixed time. This statement takes $\eta\to0$ **after** the size limit, not simultaneously.

Differentiating the explicit coefficients gives

\[
 \dot A=-2t^2P^3r,\qquad
 \dot B=-2S^2Pr\int_0^t u e^{2cu}\,du.                 \tag{14}
\]

In particular at initialization,

\[
 \dot A_0=-2t^2S^3(S-y),\qquad
 \dot B_0=-t^2S^3(S-y).                                 \tag{15}
\]

These identities distinguish several possible rates. The absolute initial kernel-change rate carries $t^2$. Relative to the initial matrix-weight contribution $A_0=tS^2$, the rate is \(-2tS(S-y)\). The bias contribution to $K$ is one and remains constant. A statement that the change is “at rate $t$” must specify which normalization and clock it uses.

An independent derivation of the first identity in (14) starts from the finite-size formula (6), under gradient flow in the original parameters. Let $Q=\sum_l a_l^{-2}$, $R=\sum_l a_l^{-4}$. Equation (5) becomes \(\dot a_l=-rP/(na_l)\), whence

\[
 \dot P=-rP^2Q/n,\quad \dot Q=2rPR/n,
 \quad \dot A_n=-\frac{2rP^3}{n^2}(Q^2-R).              \tag{16}
\]

Under the deterministic assumptions, $Q/n\to t$ and $R/n^2\to0$, recovering \(-2t^2P^3r\). This algebraic check does not require interchanging a limiting operation with differentiation.

For fixed $L$ and $n\to\infty$, the same model has $S_n\to1$, and at each fixed training horizon its matrix coefficients tend to zero: $K_n^k(x,x')\to1$, while only the output bias moves to leading order. This supplies a nonzero frozen fixed-depth kernel, but it is degenerate as a kernel on input space. It is not the usual nondegenerate fixed-depth Gaussian NTK limit.

## 6. The small-step limiting flow fits the sample and has an explicit final kernel

Time in this section is the continuous training time $\tau$ of (13). The flow in (13) has the first integral

\[
 \frac1{P(\tau)}+tb(\tau)=\frac1S.                       \tag{17}
\]

Indeed, $d(1/P)/d\tau=t r$ and $t\dot b=-tr$, so their sum is constant. Also

\[
 \dot r=-(1+tP^2)r,\qquad
 r(\tau)=(S-y)\exp\left[-\tau-t\int_0^\tau P(v)^2\,dv\right]. \tag{18}
\]

Hence $|r(\tau)|\le |S-y|e^{-\tau}$ on every local existence interval, and $|b(\tau)|\le |S-y|$. Since $P=y+r-b$, this bounds $P$ from above by $|y|+2|S-y|$. Positivity follows from $P=Se^{tc}$. The conserved quantity further gives

\[
 P(\tau)\ge\frac1{1/S+t|S-y|}>0.
\]

Thus $b,P,c=t^{-1}\log(P/S)$ remain in a compact set on the entire maximal forward interval. The smooth ODE can be extended beyond every finite endpoint, so the solution exists for all $\tau\ge0$. Its derivatives $\dot b=-r$ and $\dot P=-tP^2r$ are absolutely integrable by (18) and the upper bound on $P$. Therefore $b,P$ converge, and their limits satisfy

\[
 b_*+P_*=y,\qquad 1/P_*+tb_*=1/S.
\]

Eliminating $b_*$ gives the quadratic

\[
 tP_*^2+(1/S-ty)P_*-1=0.
\]

Its constant term is negative and $t>0$, so exactly one root is positive. Consequently

\[
 P_*=
 \frac{2}{\sqrt{(1/S-ty)^2+4t}+(1/S-ty)},\quad
 b_*=y-P_*,\quad c_*=\frac1t\log(P_*/S).                \tag{19}
\]

Equations (2)–(3) give the explicit final coefficients

\[
 A_*=tP_*^2,\qquad B_*=tS^2H(2\log(P_*/S)).             \tag{20}
\]

Equivalently, substituting (17) into the equation for $P$ reduces the flow to the scalar cubic

\[
 \dot P=-P\{tP^2+(1/S-ty)P-1\}.                         \tag{21}
\]

The positive root (19) is its unique positive equilibrium; the sign on either side also checks the direction of motion. These formulas describe the order of limits: size limit, small-step limit, then infinite continuous training time. They do not interchange those limits or assert convergence of fixed-step GD for arbitrarily long time.

## Scope

The proof uses aligned scalar-identity initialization, linear activation, a fixed readout, one training example, and a finite GD horizon. Width enters both the $1/\sqrt n$ parameterization and the prescribed gain distribution. No independent-neuron averaging, Gaussian-matrix universality, or ReLU gate evolution is proved. The result is an explicit full-kernel benchmark in the joint regime, with a random law and exact training recursion; the original Gaussian ReLU problem remains open here.
