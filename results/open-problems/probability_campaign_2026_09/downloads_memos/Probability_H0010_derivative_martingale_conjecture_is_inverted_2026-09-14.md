# The derivative martingale in the cascade front conjecture: the hypothesis is inverted, and repairing it proves half the conjecture

Ledger row H0010 (intake H). Source: A. Kumar and A. Duddala, *Front propagation and the sensitive regime for cascades on unimodular trees*, arXiv:2608.21125, Proposition 3.1 and Conjecture 3.2. Written 14 September 2026, about 09:30.

## What the source says

For the multitype branching random walk $\{(|v|, T_v)\}$ attached to a cascade on a unimodular tree, with $\theta^*$ the optimiser in the velocity variational formula and $\varphi$ the left Perron eigenvector of $B(\theta^*)$, the paper defines
$$W_n(\theta) = \rho(B(\theta))^{-n}\sum_{|v|=n}\varphi_{d(v)}e^{-\theta T_v}, \qquad \partial W_n = -\frac{d}{d\theta}\Big|_{\theta^*}W_n(\theta) = \rho(B(\theta^*))^{-n}\sum_{|v|=n}\varphi_{d(v)}\big(T_v - n\bar T\big)e^{-\theta^*T_v}.$$
Proposition 3.1 ends: "$\partial W_n \to \partial W_\infty$ a.s., and $\partial W_\infty > 0$ a.s. on survival provided $(\partial W_n)$ is uniformly integrable." Conjecture 3.2 then reads: "the derivative martingale $\partial W_n$ is uniformly integrable (equivalently, $\partial W_\infty > 0$ a.s. on survival), and consequently the front obeys $F(t) = c^*t - \frac{3}{2\theta^*c^*}\log t + O_{\mathbb P}(1)$", with the recentred front converging to a randomly shifted decorated Gumbel process. Programme 3.3(2) says uniform integrability "holds iff the offspring point process satisfies the $\int x\log_+^2x$ condition of [4, 13]".

## The correction

The two conditions are not equivalent. They are incompatible, and uniform integrability is the one that must go.

**Proposition.** Suppose, as in the source, that $T_{\mathrm{root}} = 0$, that $(\partial W_n)$ is a martingale, and that $\partial W_n \to \partial W_\infty \ge 0$ almost surely. If $(\partial W_n)$ is uniformly integrable then $\partial W_\infty = 0$ almost surely. Hence the parenthetical equivalence in Conjecture 3.2 is false, and the clause in Proposition 3.1 asserts the opposite of what uniform integrability delivers.

*Proof.* At $n = 0$ the sum has the root alone and the centring $T_v - n\bar T$ vanishes there, so $\partial W_0 = \varphi_{d(\mathrm{root})}\cdot 0\cdot 1 = 0$, and the martingale property gives $\mathbb{E}[\partial W_n] = 0$ for every $n$. Uniform integrability upgrades the almost sure convergence to $L^1$ convergence, so $\mathbb{E}[\partial W_\infty] = 0$; with $\partial W_\infty \ge 0$ this forces $\partial W_\infty = 0$ a.s. $\square$

The nonnegativity of the limit is not an extra assumption smuggled in: it is part of the derivative-martingale mechanism the source invokes (Biggins and Kyprianou), where the signed martingale converges almost surely to a nonnegative limit. And the failure of uniform integrability in the boundary case is not marginal. The limit has a Cauchy tail, $\mathbb{P}(\partial W_\infty > x) \sim c/x$ (Buraczewski, Iksanov and Mallein; Madaule), so $\mathbb{E}[\partial W_\infty] = \infty$ while every $\mathbb{E}[\partial W_n] = 0$: the martingale is about as far from uniformly integrable as a martingale can be.

## The repair, and what it settles

Replace "uniformly integrable" by "nondegenerate" throughout. Proposition 3.1's last clause should read: $\partial W_n \to \partial W_\infty \ge 0$ a.s., and $\partial W_\infty > 0$ a.s. on survival if and only if the $x\log^2_+x$ condition holds. That is exactly Chen's theorem, which the source already cites as its [13] — Chen's condition is necessary and sufficient for the nontriviality of the limit, not for uniform integrability, so Programme 3.3(2) is correct once its first four words are changed.

With the hypothesis repaired, the first half of Conjecture 3.2 is a theorem in the regime the source itself identifies. Remark 3.4 observes that in the bounded-degree dissipative regime the one-generation weight is bounded, so all $\log^2$ moments are finite; by Chen's criterion (and, in the form needed here, Biggins and Kyprianou together with Aïdékon) the derivative martingale is then nondegenerate, $\partial W_\infty > 0$ a.s. on survival. So in that regime nothing is conjectural about the martingale side; what remains is the transcription of the decorated-point-process convergence to the genealogical tree walk, which is what Remark 3.4 already names as the only gap. The conjecture should be restated with the martingale clause as a proposition and the front clause as the conjecture.

## Status

A correction plus a partial resolution: the martingale half of Conjecture 3.2, once stated correctly, is a theorem in the bounded-degree dissipative regime; the front half stands. Verification: author checked; the only inputs are $\partial W_0 = 0$, the martingale property the source proves, the nonnegativity of the limit in the mechanism it cites, and Chen's criterion. Prior art: the paper is from August 2026; the inversion appears to be a slip in writing rather than a mathematical error elsewhere in it, since Programme 3.3 and Remark 3.4 both describe the nondegeneracy condition correctly under the wrong name. Not a clearance.

## New open problem

The source's own Remark 3.5 is the question worth carrying: does the disorder of the unimodular Galton–Watson environment move the Bramson coefficient away from $3/2$, as it does for branching random walk in random environment, and do the quenched and annealed logarithmic corrections differ for cascades on a fixed tree? Their Section 5 pressure function already separates quenched and annealed speeds off boundary-homogeneous trees, so the corresponding separation at the logarithmic order is the first place to look.
