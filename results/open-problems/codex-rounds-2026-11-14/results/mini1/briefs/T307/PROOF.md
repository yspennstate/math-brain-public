# An approximation obstruction for homogeneous space–time denoisers

Fix an integer `d >= 1`. All norms below are Euclidean. Set

\[
\mu=\tfrac12 e_1,\qquad r=\tfrac1{16},\qquad
K=\overline B(\mu,r).
\]

Let `p0` be any probability density supported in `K`. In particular, `p0` can be a smooth compactly supported density. The bound `||X0|| <= 1` holds, and the clipping radius throughout this result is `D=1`.

Consider the Ornstein–Uhlenbeck diffusion

\[
dX_t=-X_t\,dt+\sqrt2\,dB_t,
\qquad
\alpha_t=e^{-t},\quad h_t=1-e^{-2t}.
\]

Thus, conditional on `X0=u`, `Xt` has density

\[
\varphi_t(x\mid u)
=(2\pi h_t)^{-d/2}
\exp\!\left(-\frac{\|x-\alpha_tu\|^2}{2h_t}\right).
\tag{1}
\]

Write `pt` for the density of `Xt` and

\[
m_t(x)=\mathbb E[X_0\mid X_t=x].
\]

For every `t>0`, `pt(x)>0` for every `x`, and this conditional mean is defined by the quotient of the corresponding integrals against (1).

Let `0 <= T0 <= 1/2` and `T >= 2`, and write `L=T-T0`. A measurable function `F(x,t)` is homogeneous in space and shifted time if

\[
F(cx,T_0+c(t-T_0))=cF(x,t)
\tag{2}
\]

for positive `c` whenever both arguments have times in `[T0,T]`. Define

\[
\Pi_1(v)=\frac{v}{\max\{1,\|v\|\}},\qquad
G(x,t)=\Pi_1(F(x,t)).
\]

## Theorem

Every such `F` satisfies

\[
\mathcal R(G):=
\frac1L\int_{T_0}^{T}\mathbb E\|G(X_t,t)-m_t(X_t)\|^2\,dt
\ \ge\ \frac{C_d}{L},
\qquad
C_d=\frac{5e^{-1}}{1024\,[32\sqrt{2\pi d}]^d}>0.
\tag{3}
\]

The inequality is uniform over the density `p0` just specified, network width, weights, and training rule.

For example, (2) holds for every bias-free two-layer ReLU network

\[
F(x,t)=\frac1{\sqrt M}\sum_{j=1}^M a_j
\operatorname{ReLU}\big(w_j^\top(x,t-T_0)\big),
\qquad a_j\in\mathbb R^d.
\tag{4}
\]

Here either layer may be trained. It also holds for deeper networks whose layers consist only of linear maps and positively homogeneous activations, with no added biases or constant input coordinate.

### Proof

**1. The posterior mean stays in the same ball.** The conditional law of `X0` given `Xt=x` is supported in `K`, because its density is proportional to `p0(u) varphi_t(x|u)`. Hence

\[
\|m_t(x)-\mu\|
=\|\mathbb E[X_0-\mu\mid X_t=x]\|
\le \mathbb E[\|X_0-\mu\|\mid X_t=x]
\le \tfrac1{16}.
\tag{5}
\]

In particular `||m_t(x)|| <= 9/16`.

**2. Two dilated inputs cannot both be fitted.** Let `u,v` be any two vectors in `K`, and let `a` be any vector in `R^d`. We claim

\[
\|\Pi_1(a)-u\|^2+\|\Pi_1(2a)-v\|^2\ge\frac5{256}.
\tag{6}
\]

If `||a|| >= 1/2`, then `||Pi_1(2a)||=1`. Since `||v|| <= 9/16`, the second summand is at least `(7/16)^2=49/256`, which implies (6).

If `||a|| < 1/2`, neither projection changes its argument. Completing the square gives the exact identity

\[
\|a-u\|^2+\|2a-v\|^2
=5\left\|a-\frac{u+2v}{5}\right\|^2
+\frac15\|2u-v\|^2.
\tag{7}
\]

Moreover

\[
\|2u-v\|
=\|\mu+2(u-\mu)-(v-\mu)\|
\ge \tfrac12-\tfrac2{16}-\tfrac1{16}
=\tfrac5{16}.
\tag{8}
\]

Equations (7) and (8) imply (6), since `(1/5)(5/16)^2=5/256`. The boundary `||a||=1/2` was included in the first case.

**3. Choose two regions with positive mass.** Use shifted time `tau=t-T0` and set

\[
Q=\left[0,\frac1{32\sqrt d}\right]^d,\qquad
E=Q\times[\tfrac12,\tfrac34].
\]

Let `2E={(2x,2tau):(x,tau) in E}`. The interiors of `E` and `2E` are disjoint because their shifted-time intervals are `[1/2,3/4]` and `[1,3/2]`. Their physical times lie in `[1/2,2]`, which is contained in `[T0,T]`. Boundaries have Lebesgue measure zero. Also

\[
|E|=\frac14(32\sqrt d)^{-d},
\qquad \|x\|\le\tfrac1{16}\quad\text{on }E\cup2E.
\tag{9}
\]

For physical times in `[1/2,2]`,

\[
0<\alpha_t\le1,\qquad
\tfrac12<1-e^{-1}\le h_t<1.
\]

The strict lower bound uses `e>2`. For every initial point `u in K` and every spatial point in these two regions,

\[
\|x-\alpha_tu\|
\le\tfrac1{16}+\tfrac9{16}=\tfrac58,
\qquad
\frac{\|x-\alpha_tu\|^2}{2h_t}<\frac{25}{64}<1.
\]

Consequently (1), followed by integration against the probability density `p0`, yields

\[
p_t(x)\ge b_d,
\qquad b_d=e^{-1}(2\pi)^{-d/2},
\quad (x,t-T_0)\in E\cup2E.
\tag{10}
\]

**4. Integrate the two-point obstruction.** Put

\[
e(x,\tau)=\|G(x,T_0+\tau)-m_{T_0+\tau}(x)\|^2.
\]

By nonnegativity, disjointness of the two regions, and (10),

\[
L\mathcal R(G)
\ge b_d\left(\int_E e(x,\tau)\,dx\,d\tau
+\int_{2E} e(x,\tau)\,dx\,d\tau\right).
\tag{11}
\]

The change of variables `(x,tau) -> (2x,2tau)` has Jacobian `2^(d+1)`. Therefore the right side of (11) equals

\[
b_d\int_E\left(e(x,\tau)+2^{d+1}e(2x,2\tau)\right)\,dx\,d\tau
\ge b_d\int_E\left(e(x,\tau)+e(2x,2\tau)\right)\,dx\,d\tau.
\tag{12}
\]

At every point of `E`, set

\[
a=F(x,T_0+\tau),\quad
u=m_{T_0+\tau}(x),\quad
v=m_{T_0+2\tau}(2x).
\]

Equation (2) gives `F(2x,T0+2tau)=2a`, and (5) places `u,v` in `K`. Applying (6) pointwise in (12) proves

\[
L\mathcal R(G)\ge b_d|E|\frac5{256}
=\frac{5e^{-1}}{1024\,[32\sqrt{2\pi d}]^d},
\]

which is (3). Finally, (4) satisfies (2) because `ReLU(cs)=c ReLU(s)` for positive `c`. This proves the theorem.

## Consequence for denoising score matching

Define the score estimate associated with the clipped denoiser by

\[
s_G(x,t)=\frac{\alpha_t}{h_t}G(x,t)-\frac{x}{h_t}.
\tag{13}
\]

Differentiating the integral `pt(x)=int varphi_t(x|u)p0(u) du` gives

\[
\nabla p_t(x)
=\int-\frac{x-\alpha_tu}{h_t}\varphi_t(x\mid u)p_0(u)\,du.
\]

This differentiation is valid for each `t>0`: the initial support is compact and the kernel and its derivatives are continuous and bounded there locally in `x`. Dividing by `pt(x)>0` gives

\[
\nabla\log p_t(x)=\frac{\alpha_t}{h_t}m_t(x)-\frac{x}{h_t}.
\tag{14}
\]

For `lambda(t)=h_t^2/alpha_t^2`, equations (13) and (14) give the exact equality

\[
\frac1L\int_{T_0}^T\lambda(t)
\mathbb E\|s_G(X_t,t)-\nabla\log p_t(X_t)\|^2\,dt
=\mathcal R(G)\ge\frac{C_d}{L}.
\tag{15}
\]

When `T0=0`, all integrals can be taken over `t>0`; the value at that single endpoint does not matter.

This is also a lower bound for the *excess population denoising score-matching loss*, with no factor `1/2` in the definition of that loss. Indeed the denoising target is

\[
Y_t=-\frac{X_t-\alpha_tX_0}{h_t},
\qquad \mathbb E[Y_t\mid X_t]=\nabla\log p_t(X_t).
\]

Expanding the square and conditioning on `Xt` cancels the cross term, so

\[
\mathbb E\|s_G(X_t,t)-Y_t\|^2
-\mathbb E\|\nabla\log p_t(X_t)-Y_t\|^2
=\mathbb E\|s_G(X_t,t)-\nabla\log p_t(X_t)\|^2.
\]

The weighted losses are finite even down to `t=0`: multiplication by `lambda(t)` turns the squared denoising residual into `||G(Xt,t)-X0||^2`, which is bounded. Thus integrating this identity is legitimate.

There is also an unweighted score-error lower bound `e^(-4) C_d/L`. To see this, restrict the proof to the same two regions, where `t<=2` and

\[
\frac{\alpha_t^2}{h_t^2}\ge e^{-4}.
\]

The unweighted error integral elsewhere is nonnegative; if infinite it also satisfies the bound.

If `T=T_N <= A log N`, `T_N>=2`, and eventually `T0_N<=1/2`, then (15) is at least `C_d/(A log N)`. In particular it cannot be `O(N^(-eta) (log N)^k)` for any fixed `eta>0` and fixed real `k`, since `N^eta/(log N)^(k+1)` tends to infinity. No increase in width or training time removes this obstruction within (2) and the specified clipping rule.

## The corresponding homogeneous tangent kernel

The same obstruction holds for the reproducing kernel Hilbert space of

\[
\kappa(z,z')=(z^\top z')\,
\mathbb E_{w\sim N(0,I_{d+1})}
\left[\mathbf1_{w^\top z\ge0}\mathbf1_{w^\top z'\ge0}\right],
\quad z=(x,t-T_0).
\tag{17}
\]

This is a positive semidefinite kernel: it is the expected inner product of the vector features `z 1_{w^T z >= 0}`. For every positive `c`,

\[
\kappa(cz,z')=c\kappa(z,z'),
\tag{18}
\]

because positive scaling leaves the indicator unchanged. Finite linear combinations of kernel sections therefore satisfy (2). Such combinations are dense in the RKHS. If `fn` converges to `f` in its norm, evaluation at any fixed `z` converges because

\[
|f_n(z)-f(z)|\le
\|f_n-f\|_{\mathcal H}\sqrt{\kappa(z,z)}.
\]

Passing to the limit at `z` and `cz` preserves (2). This argument works on the restricted space–time domain as well, whenever both inputs lie in that domain. Applying it coordinate by coordinate gives the same conclusion for the vector kernel `kappa I_d`.

Thus every vector-valued function in this RKHS has clipped risk at least (3). The raw risk is at least as large. To verify the last assertion directly, for `||v||=s>=1`, write `v=sw` with `||w||=1`. For a target `u` of norm at most one,

\[
\|v-u\|^2-\|\Pi_1(v)-u\|^2
=(s-1)(s+1-2w^\top u)\ge0.
\]

For `||v||<1` the two distances agree. Consequently a universal approximation claim for this kernel on these denoising targets cannot hold merely by allowing its RKHS norm to grow. The obstruction also applies when the risk is restricted to any spatial ball containing `E` and `2E`.

## A smooth non-Gaussian class

One example is

\[
p_0(u)=Z^{-1}
\begin{cases}
\exp\!\left(-\dfrac1{1-256\|u-\mu\|^2}\right),
&\|u-\mu\|<1/16,\\
0,&\text{otherwise}.
\end{cases}
\tag{16}
\]

The normalizing constant `Z` is finite and positive: the integrand is bounded on a ball of finite volume and strictly positive on its interior. Every derivative inside the ball is a finite sum of a polynomial in `u-mu` times a power of `(1-256||u-mu||^2)^(-1)` times the exponential. Each term tends to zero at the boundary, because `v^(-j) exp(-1/v) -> 0` as `v -> 0+` for every nonnegative integer `j`. The extension by zero is therefore smooth, with bounded derivatives of every order. It is compactly supported and is not Gaussian. The theorem also holds for all other densities supported in `K`, so it is not restricted to one fixed example.

## Scope

This is a limitation of homogeneous joint space–time parameterizations with the declared clipping radius. A hidden bias, an output bias, or an added constant input coordinate removes the homogeneity premise. The theorem gives no optimization guarantee for those architectures and no lower bound for all trained score networks. It also gives no total-variation lower bound for the distribution produced by a sampler.

The clipping radius `D=1` is part of the statement. Changing it changes the class and requires another argument. The proof uses positive-measure regions with positive Gaussian density; it is not an argument based on the single input `(0,T0)`.
