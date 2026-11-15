# A smooth obstruction for the unmodified probability-flow ODE

Write `TV(μ,ν)=sup_A |μ(A)-ν(A)|`, equal to half the L1 distance for densities. Let γ denote the standard Gaussian law on R, with density φ. Consider the OU normalization

\[
dX_t=-X_t\,dt+\sqrt2\,dB_t.
\]

When `X_0~γ`, every forward marginal `p_t`, including `p_delta` for every fixed positive delta, is γ. Its score is `s_t(x)=-x`. Over the reverse interval from forward time `delta+1` to `delta`, put `u=delta+1-t`. The unmodified approximate probability-flow ODE is

\[
\dot Y_u=Y_u+\widehat s_{\delta+1-u}(Y_u),\qquad Y_0\sim\gamma,
\quad 0\le u\le1.
\tag{1}
\]

Thus the initialization has no error, and there is no issue at a singular endpoint.

## Proposition

Fix `0<c<1`. For every integer `k>=1`, use the fixed, time-independent score estimate

\[
\widehat s^{(k)}_t(x)=-x+\frac c k\sin(kx)
\tag{2}
\]

at every forward time. Let `P_k` be the law of the exact solution of (1) at `u=1`. Then:

1. At every time the score error satisfies
   \[
   \|\widehat s^{(k)}_t-s_t\|_\infty\le c/k,
   \qquad
   \mathbb E_\gamma|\widehat s^{(k)}_t(X)-s_t(X)|^2
   =\frac{c^2}{2k^2}(1-e^{-2k^2}).
   \tag{3}
   \]
2. The estimate is the score of a positive smooth density
   \[
   q_k(x)=Z_k^{-1}\exp\left(-\frac{x^2}{2}-\frac c{k^2}\cos(kx)\right).
   \tag{4}
   \]
   Its negative log density has second derivative between `1-c` and `1+c`. In particular all these estimated scores are `(1+c)`-Lipschitz. These densities have uniformly bounded second moments.
3. Set
   \[
   D(c)=\frac4\pi\arctan(e^{c/2})-1
       =\frac2\pi\arcsin(\tanh(c/2))>0.
   \tag{5}
   \]
   There is an explicit finite-frequency estimate
   \[
   \left|\operatorname{TV}(P_k,\gamma)-D(c)\right|
   \le\frac{\sqrt{2\pi}}{k}.
   \tag{6}
   \]
4. The same construction admits a coupling with
   \[
   |Y_1-Y_0|\le c/k\quad\text{almost surely}.
   \tag{7}
   \]

Consequently, even for a fixed one-dimensional target of second moment one and covariance condition number one, uniform score accuracy tending to zero, uniformly Lipschitz estimated scores, and exact ODE integration do not imply total-variation convergence for this sampler.

## Proof

**Score error and regularity.** The stationary Gaussian marginal follows either from the explicit OU solution or from invariance of γ. Formula (3) follows from

\[
\sin^2(kx)=\frac{1-\cos(2kx)}2,
\qquad \mathbb E\cos(2kX)=e^{-2k^2},\quad X\sim\gamma.
\]

The Gaussian characteristic-function identity here can be obtained by integrating by parts: `G(a)=E exp(iaX)` satisfies `G'(a)=-aG(a)` and `G(0)=1`, so `G(a)=exp(-a^2/2)`.

Differentiating the logarithm in (4) gives (2). The normalizing constant is finite because the cosine term is bounded. If `V_k(x)=x^2/2+(c/k^2)cos(kx)`, then

\[
V_k''(x)=1-c\cos(kx)\in[1-c,1+c].
\]

Also `q_k(x)/φ(x)` lies between `exp(-2c/k^2)` and `exp(2c/k^2)`, by bounding both the exponential perturbation and its Gaussian normalizer. Thus `E_{q_k}X^2<=exp(2c)` for `k>=1`. In fact the same bound on the density ratio shows `TV(q_k,γ)=O(k^{-2})` for fixed c. No assertion is made that the family `q_k` across forward times is itself an OU trajectory: the approximate-score oracle assumption does not require that consistency.

**Exact phase flow.** Substituting (2) into (1) gives

\[
\dot Y_u=\frac c k\sin(kY_u).
\tag{8}
\]

This vector field is globally c-Lipschitz, so it generates a smooth increasing flow map `F_k:R→R`. Its magnitude is at most `c/k`, which proves (7) by integration. The points `jπ/k` are stationary. Each period cell

\[
I_j=[2\pi j/k,2\pi(j+1)/k],\qquad j\in\mathbb Z,
\]

is mapped onto itself. In phase coordinates `θ=kx-2πj`, the time-one map is the lift `H_c` of the circle flow

\[
\dot\theta=c\sin\theta,\qquad
\tan\frac{H_c(\theta)}2=e^c\tan\frac\theta2.
\tag{9}
\]

The tangent identity follows by differentiating `tan(θ/2)`: its derivative along the flow is `c tan(θ/2)`. Choose the increasing continuous branch on `[0,2π]`; it fixes `0,π,2π`. The inverse is `H_{-c}`. Differentiation, using the half-angle identities, gives

\[
H_c'(\theta)=\frac1{\cosh c-\sinh c\cos\theta},\qquad
H_{-c}'(\theta)=\frac1{\cosh c+\sinh c\cos\theta}.
\tag{10}
\]

These positive derivatives also verify that no interval collapses to an atom.

**TV for a uniform phase.** Let `U` be uniform on `[0,2π]`. Its image under `H_c` has density `r_c(θ)/(2π)`, where

\[
r_c(\theta)=\frac1{\cosh c+\sinh c\cos\theta}.
\tag{11}
\]

It exceeds the uniform density precisely on `(a,2π-a)`, where

\[
\cos a=\frac{1-\cosh c}{\sinh c}=-\tanh(c/2),
\qquad a=2\arctan(e^{c/2})\in(\pi/2,\pi).
\]

The second expression follows from the cosine double-angle formula. Equation (9) with parameter `-c` gives

\[
H_{-c}(a)=2\arctan(e^{-c/2})=\pi-a,
\quad H_{-c}(2\pi-a)=2\pi-H_{-c}(a).
\]

Therefore the difference of the image and uniform probabilities of this interval is

\[
\frac{2\pi-2H_{-c}(a)}{2\pi}
-\frac{2\pi-2a}{2\pi}
=\frac{2a-\pi}{\pi}
=D(c).
\tag{12}
\]

For two equal-mass densities, the positive part of their difference integrates to TV; thus (12) is exactly the phase TV, not just a lower bound. Since `cos a=-tanh(c/2)`, we also have `a=π/2+arcsin(tanh(c/2))`, proving the second expression in (5).

**Transfer from uniform cells to a Gaussian.** The following elementary estimate supplies a quantitative error rather than an informal equidistribution argument. If an absolutely continuous probability density f has integrable derivative, partition R into cells of length `ell` and replace f on each cell by its average, obtaining density g. For one cell `I=[b,b+ell]`,

\[
\begin{aligned}
\int_I|f(x)-g(x)|\,dx
&\le\frac1\ell\int_I\int_I|f(x)-f(y)|\,dy\,dx\\
&\le\frac1\ell\int_I 2(z-b)(b+\ell-z)|f'(z)|\,dz\\
&\le\frac\ell2\int_I|f'(z)|\,dz.
\end{aligned}
\tag{13}
\]

The middle inequality uses the fundamental theorem of calculus between x and y and Tonelli's theorem. For fixed z, the ordered pairs with z between x and y occupy area `2(z-b)(b+ell-z)`. Summing (13) and dividing by two gives

\[
\operatorname{TV}(f\,dx,g\,dx)\le\frac\ell4\|f'\|_1.
\tag{14}
\]

Apply this to `f=φ`, `ell=2π/k`, with the cells `I_j` above, and call the resulting probability measure `G_k`. Each cell has the same mass under `G_k` and `F_{k#}G_k`; conditioned on that cell, the initial phase is uniform and the image phase has density (11). The cells are disjoint up to null endpoints. Summing their L1 differences therefore yields

\[
\operatorname{TV}(F_{k\#}G_k,G_k)=D(c).
\tag{15}
\]

For any measurable map F, TV contracts under pushforward, since every preimage of an event is an event. Twice the triangle inequality now gives

\[
\begin{aligned}
\big|\operatorname{TV}(F_{k\#}\gamma,\gamma)-D(c)\big|
&\le\operatorname{TV}(F_{k\#}\gamma,F_{k\#}G_k)
  +\operatorname{TV}(\gamma,G_k)\\
&\le2\operatorname{TV}(\gamma,G_k)
\le\frac\ell2\|\varphi'\|_1.
\end{aligned}
\]

Finally `φ'(x)=-xφ(x)`, so `||φ'||_1=E|X|=sqrt(2/π)`. Substituting `ell=2π/k` proves (6). This completes the proof.

## Consequences and scope

For `c=1/2`, the exact limiting error is `D(1/2)`, approximately `0.15752`. Formula (6), rather than that decimal, is the rigorous finite-k assertion. In particular the lower bound is positive for all sufficiently large k, whereas the L2 score error tends to zero. There cannot be a bound on the exact unmodified ODE's TV error depending only on this L2 error that tends to zero, even if it also uses the fixed target moment and the fixed score Lipschitz upper bound `3/2`.

The estimate's second derivative is `-ck sin(kx)`, whose uniform norm grows with k. Its first-derivative error relative to the true score is `c cos(kx)`; its squared Gaussian mean is `c^2(1+exp(-2k^2))/2`, which does not vanish. Thus neither a small-Jacobian-error theorem nor a theorem with a fixed bound on the score's second derivative is contradicted.

This proposition concerns plugging the supplied estimate directly into the probability-flow ODE. It does not apply to an algorithm that regularizes the oracle, adds a stochastic corrector, or exploits knowledge of the target. In particular γ can itself be sampled without a score query. This is not a lower bound for arbitrary score-oracle algorithms, and it does not determine the optimal dependence on d or epsilon for stochastic samplers. It shows that the pure-ODE part, under just the stated approximate-score hypothesis, has a stability obstruction before iteration complexity is considered.

## Corollary: a bound uniform over all positive Euler step counts

For the same oracle, let `P_{k,N}` be the output of N equal explicit Euler steps over the unit interval in (8), for any integer `N>=1`. Then

\[
\operatorname{TV}(P_{k,N},\gamma)
\ge B(c)-\frac{\sqrt{2\pi}}k,
\qquad B(c)=\frac{c(1-c/2)e^{-c}}4>0.
\tag{16}
\]

In particular, choosing N as an arbitrary function of k does not repair this example within this Euler family.

**Proof.** Put `a=c/N`. Each Euler step on the phase is

\[
E_a(\theta)=\theta+a\sin\theta.
\]

Its derivative is in `[1-a,1+a]`, so it is an increasing smooth bijection of every period cell onto itself. Start the phase uniformly on `[0,2π]`, and write `Θ_j=E_a^j(Θ_0)`. The derivative of this j-step map is at most `(1+a)^j<=e^c` for `0<=j<=N`, using `log(1+a)<=a`. Change of variables consequently shows that every `Θ_j` has phase density at least `e^{-c}/(2π)`. Hence

\[
\mathbb E\sin^2\Theta_j\ge e^{-c}/2.
\tag{17}
\]

Taylor's formula with `|cos''|<=1` gives, for every real θ,

\[
\cos(\theta+a\sin\theta)
\le\cos\theta-a\sin^2\theta+\frac{a^2}2\sin^2\theta.
\]

Taking expectations, using (17), and summing over j yields

\[
\mathbb E\cos\Theta_N
\le -\frac{N(a-a^2/2)e^{-c}}2
=-\frac{c(1-c/(2N))e^{-c}}2
\le-\frac{c(1-c/2)e^{-c}}2.
\tag{18}
\]

The initial cosine expectation is zero. For any two laws μ,ν and any function with absolute value at most one, the absolute difference of expectations is at most `2 TV(μ,ν)`, by integrating against the signed density difference (or its total-variation measure). The phase TV after N steps is therefore at least `B(c)`.

Replace the Gaussian by the cellwise uniform law `G_k` used in (14). Every period cell has the same conditional phase dynamics and retains its mass under the N-step Euler map. Its TV distance from its image is thus the phase TV just bounded. The same pushforward contraction and triangle inequality used for (6) lose at most `sqrt(2π)/k`, proving (16).

For `c=1/2`, `B(c)=3e^{-1/2}/32`, approximately `0.05686`. At `k=1000`, (16) gives a TV lower bound greater than `0.054` for **every** `N>=1`, while (3) gives RMS score error below `0.000354`. These decimals can be replaced directly by the exact expressions in (3) and (16).

This corollary integrates the supplied field for a prescribed unit time. An algorithm that outputs its initial Gaussian without integrating is outside this Euler family and succeeds on this known Gaussian target; no impossibility for arbitrary algorithms follows.

## Relation to existing results

The insufficiency of L2 error alone is already illustrated by a discontinuous discrete quantization example in Section 3.2 of Gen Li, Yuting Wei, Yuejie Chi and Yuxin Chen, *A Sharp Convergence Theory for The Probability Flow ODEs of Diffusion Models*, [arXiv:2408.02320](https://arxiv.org/html/2408.02320v1). The result above supplies an explicit continuous-time smooth example, with estimated scores of uniformly strongly log-concave densities and a closed-form limiting TV error. No claim is made that the general instability phenomenon is new.

Daniel Zhengyu Huang, Jiaoyang Huang and Zhengjiang Lin, *Convergence Analysis of Probability Flow ODE for Score-based Generative Models*, [arXiv:2404.09730v3](https://arxiv.org/html/2404.09730v3), impose first- and second-derivative control on the estimated score in Assumption 3.3; their Theorem 3.5 depends on that control. Here its second-derivative constant grows linearly with k.
