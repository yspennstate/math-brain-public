# B02: full-row triage and a complete fixed-parameter obstruction for T352

Date: 2026-10-24. Author: B02. Scope: the exact `TOP200_DL` rows T323–T422 in `a03/registry422.jsonl`. Frozen files in `a03/` and `followup/` were read, not edited. T353 and T228 are not new candidates; the categorical T357 example and finite-polynomial T336 result are not treated as full original-row solutions.

**Disposition:** I do not certify a new solution of a full, currently open, originally published Top200 DNN problem. The strongest complete mathematical result obtained here is a universal fixed-parameter theorem for T352, with a matching genuinely nonconvex stationary lower bound. It excludes the row's requested positive, sample-size-independent plateau when geometry, noise, step and Rényi order are fixed independently of the sample size. This is stronger than the previous last-step-only diagnostic, but it does not settle the practical all-parameter privacy problem or establish publication novelty. It must not be counted as an original-row closure without resolving those scope differences.

## 1. Exact row and source reconciliation

The exact T352 statement in the registry is:

> Projected noisy SGD on a compact convex domain of diameter D, with per-example losses that are L-Lipschitz and M-smooth but not convex, fixed step eta and Gaussian noise of variance sigma^2 per step, releasing only the last iterate. For convex losses Altschuler and Talwar (arXiv:2205.13710, Theorem 1.3) show that the Renyi privacy loss of order alpha plateaus at order alpha L^2/(n^2 sigma^2) times min(T, D n/(L eta)) as the number of steps T grows; without convexity, a time-uniform bound that does not decrease with n follows from the last noisy step alone. Find geometric conditions on the nonconvex losses (for example a one-point dissipativity condition, or a bound on the negative curvature relative to eta and sigma) under which the time-uniform Renyi bound decreases with n at the convex rate, and construct a smooth nonconvex loss on a compact domain for which the plateau is of order alpha L^2/sigma^2 times a constant independent of n.

This is a locally repaired registry statement, not a verbatim published conjecture. The following primary sources were opened on 2026-10-24:

1. [Altschuler–Talwar, arXiv:2205.13710v2](https://arxiv.org/html/2205.13710v2), informal Theorem 1.3 and the discussion of convexity and parameter restrictions in Section 1.2. The paper poses relaxing convexity. Its theorem has an explicit parameter regime, including a noise-versus-diameter restriction in its matching lower bound. Consequently its displayed plateau cannot be extrapolated to all sample sizes with all other parameters held fixed. The paper's usual noise convention is gradient noise, so state-update standard deviation is `eta*sigma`; below I use the unambiguous state-update standard deviation `s`.
2. [Asoodeh–Diaz, arXiv:2305.09903v1](https://arxiv.org/html/2305.09903v1), Theorems 1–2, Proposition 3 and Appendix B. Theorem 2 already gives a convergent hockey-stick privacy profile without convexity or smoothness. For fresh size-`b` uniform batches, it bounds delta by `p*theta*(1-((1-p)*theta)^T)/(1-(1-p)*theta)`, where `p=b/n` and `theta` is the Gaussian hockey-stick contraction coefficient at `(D+2*eta*C)/s`. The TV-contraction ingredient below is therefore not new. The theorem as displayed does not by itself give the batch-independent `n^-2` fixed-order Rényi bound proved below.
3. [Chien–Li, ICLR 2025, arXiv:2410.01068v2](https://arxiv.org/html/2410.01068v2), Theorems 3.1 and 3.12, and Section 5. Theorem 3.1 covers smooth nonconvex full-batch loss using expansion constant `1+eta*L`; Theorem 3.12 treats fresh uniform minibatches. These are already nonconvex convergent Rényi results. Their optimization-based bounds retain a diameter-dependent term when the update is expansive. The authors explicitly describe the original convexity-relaxation question as answered affirmatively. Thus merely proving a nonconvex finite plateau would not solve a currently open original question.
4. [Liang et al., arXiv:2502.17772v2](https://arxiv.org/html/2502.17772v2), Theorem 3.4 and Remark 3.5; [AAAI 2026 publication page](https://ojs.aaai.org/index.php/AAAI/article/view/39510). The displayed smooth-nonconvex bounded-domain upper bound is the sum of a sample-dependent term and a diameter term independent of `n`; under extra sampling/noise restrictions its first term is proportional to `n^-2`. This is not a lower bound proving an `n`-independent privacy plateau.

The exact issue in T352 is a quantifier mismatch: an upper bound independent of `n` does not establish an example with a positive `n`-independent lower bound. Also, fixed positive noise and a fixed compact state range create uniform mixing even for very nonconvex drifts. Exponentially poor mixing constants can matter enormously before the eventual sample-size asymptotics apply.

## 2. The mechanism and every quantifier

Let `K` be a nonempty compact convex subset of `R^d` with diameter at most `D`. Fix `eta >= 0`, `s > 0`, and `G >= 0`. For a dataset `S=(z_1,...,z_n)` let measurable vector fields `g_z:K -> R^d` satisfy

\[
\sup_{z,x\in K}\|g_z(x)\|\leq G.
\]

Gradients of differentiable, uniformly `G`-Lipschitz losses are a special case; no smoothness, convexity, or continuity of the fields is needed for the upper bound. At every iteration, independently of the past, draw a uniformly random subset `B_t` of size `b`, where `1 <= b <= n`, and a standard Gaussian `Z_t` in `R^d`. Set

\[
X_{t+1}=\Pi_K\!\left(X_t-\frac{\eta}{b}
                   \sum_{i\in B_t}g_{z_i}(X_t)+sZ_t\right).
\tag{1}
\]

This is independent fresh minibatch sampling, including full batch `b=n`. It is not random reshuffling across dependent batches. Adjacent datasets have equal size and differ by one replacement. Initial states have the same data-independent distribution on `K`. Only `X_T` is released.

For every fixed real `alpha>1`, there is an explicit finite constant

\[
C_\alpha=C_\alpha(D,\eta G,s),
\]

independent of `d,n,b,T`, of the data, and of the vector fields, such that

\[
\sup_{T\geq0}\sup_{S\sim S'}
D_\alpha\!\left(\mathcal L_S(X_T)\,
\middle\|\,\mathcal L_{S'}(X_T)\right)
\leq \frac{C_\alpha}{n^2}.
\tag{2}
\]

The same statement holds after interchanging `S,S'`. Constants can grow exponentially in `(D+2*eta*G)^2/s^2`, and rapidly in `alpha`. There is no uniform claim for `alpha` growing with `n` or for `s` shrinking with `n`.

## 3. Explicit constants

Write `Phi` for the standard normal distribution function, and put

\[
R=D+2\eta G,\qquad
\rho=2\Phi\!\left(\frac{R}{2s}\right)-1<1,\qquad
A=\frac{2\eta G}{s\sqrt{2\pi}}.
\tag{3}
\]

For every real `r>=1` define

\[
m_r=(\mathbb E|Z|^r)^{1/r},\quad Z\sim N(0,1),
\]

\[
E_r=\exp\!\left(\frac{(r-1)R^2}{2s^2}\right),
\qquad
B_r=E_r\left[
\frac{2A}{1-\rho}
+\frac{2\eta G}{s}
 \left(m_r+\frac{(r-1)R}{s}\right)
\right].
\tag{4}
\]

Let `k=max(2,ceil(alpha))` and

\[
H_k=\sum_{j=2}^{k}{k\choose j} B_j^j.
\tag{5}
\]

A slightly stronger version of (2) is

\[
D_\alpha\!\left(\mathcal L_S(X_T)\|
                        \mathcal L_{S'}(X_T)\right)
\leq\frac{1}{k-1}\log\left(1+\frac{H_k}{n^2}\right)
\leq\frac{H_k}{(k-1)n^2}.
\tag{6}
\]

For `1<alpha<=2` one can simply use
`log(1+B_2^2/n^2)`. Constants were chosen for a transparent proof, not optimized.

## 4. Proof of the universal upper bound

All total variation distances below use `TV(P,Q)=sup_A |P(A)-Q(A)|`, so the total variation norm of the signed measure `P-Q` is `2*TV(P,Q)`.

### 4.1 A uniform contraction and an adjacent-kernel perturbation

Let `P_S(x,.)` be the one-step projected Markov kernel in (1). Every mean before adding noise, for any dataset, state or batch, lies in

\[
\mathcal A=K+\overline B(0,\eta G),
\]

a convex set of diameter at most `R`. For equal-covariance Gaussians,

\[
\operatorname{TV}(N(a,s^2I),N(c,s^2I))
=2\Phi\!\left(\frac{\|a-c\|}{2s}\right)-1.
\tag{7}
\]

Projection cannot increase TV. Coupling the same batch when comparing two states and averaging (7) gives

\[
\sup_{x,y\in K}\operatorname{TV}(P_S(x,\cdot),P_S(y,\cdot))
\leq\rho.
\tag{8}
\]

Thus `TV(mu P_S,nu P_S)<=rho*TV(mu,nu)` for any probability measures `mu,nu`. To see this directly, write their signed difference as `delta*(mu_+-mu_-)`, with `delta=TV(mu,nu)`, and couple `mu_+,mu_-`; (8) applies pairwise.

For adjacent datasets at the same input state, use the same uniformly sampled batch. It contains the replaced index with probability `b/n`. Conditional on containing it, the means differ by at most `2*eta*G/b`. Since `2*Phi(u/2)-1 <= u/sqrt(2*pi)`,

\[
\sup_x\operatorname{TV}(P_S(x,\cdot),P_{S'}(x,\cdot))
\leq\frac{b}{n}\frac{2\eta G}{bs\sqrt{2\pi}}
=\frac{A}{n}.
\tag{9}
\]

Let `mu_t,nu_t` be the state laws and `delta_t=TV(mu_t,nu_t)`. Equations (8)–(9) give

\[
\delta_{t+1}\leq\rho\delta_t+\frac{A}{n},\qquad
\delta_0=0,
\]

so

\[
\delta_t\leq\frac{A(1-\rho^t)}{n(1-\rho)}.
\tag{10}
\]

This step alone is a TV guarantee, not a Rényi guarantee. The next step is necessary.

### 4.2 Final Gaussian smoothing controls likelihood-ratio moments

Let `phi_a(y)` be the density of `N(a,s^2 I)`. If `q` is any mixture of `phi_c` with `c in A`, then, for `r>=1` and `a in A`,

\[
\left(\int\frac{\phi_a(y)^r}{q(y)^{r-1}}\,dy\right)^{1/r}
\leq E_r.
\tag{11}
\]

Indeed, convexity of `u -> u^(1-r)` gives `q^(1-r)<=E_c phi_c^(1-r)`, and Gaussian completion of the square gives

\[
\int\phi_a^r\phi_c^{1-r}
=\exp\!\left(\frac{r(r-1)\|a-c\|^2}{2s^2}\right).
\tag{12}
\]

There is also a derivative estimate: for `a,a' in A`,

\[
\left(\int\frac{|\phi_a-\phi_{a'}|^r}{q^{r-1}}\right)^{1/r}
\leq E_r\left(m_r+\frac{(r-1)R}{s}\right)
             \frac{\|a-a'\|}{s}.
\tag{13}
\]

To prove it, integrate the derivative of `phi_(a+u(a'-a))` for `0<=u<=1` and apply Minkowski's inequality in the weighted `L^r` space. For a unit vector `v`,

\[
\partial_v\phi_a(y)=\frac{v\cdot(y-a)}{s^2}\phi_a(y).
\]

Under the normalized density proportional to `phi_a^r phi_c^(1-r)`, `y` is Gaussian with mean `r*a-(r-1)*c` and covariance `s^2 I`. Hence the `L^r` norm of `v.(y-a)/s` is at most `m_r+(r-1)*R/s`. Equation (12) supplies `E_r`. Convexity of `A` keeps the derivative path inside it. Jensen's inequality for the reference mixture completes (13).

Now fix `T>=1`, and consider the unprojected final updates; denote their strictly positive Lebesgue densities by `p,q`. Let `tilde P_S` be the unprojected one-step kernel. Decompose

\[
p-q=(\mu_{T-1}-\nu_{T-1})\widetilde P_S
     +\nu_{T-1}(\widetilde P_S-\widetilde P_{S'}).
\tag{14}
\]

The first term has weighted `L^r` norm at most `2*E_r*delta_(T-1)`, by its Jordan decomposition and (11). In the second term, couple the same state and batch. The mean discrepancy is zero off the replaced index, and at most `2*eta*G/b` otherwise. Minkowski and (13) give weighted norm at most

\[
\frac{b}{n}E_r\left(m_r+\frac{(r-1)R}{s}\right)
\frac{2\eta G}{bs}.
\]

Combining with (10),

\[
\left(\int q\left|\frac pq-1\right|^r\right)^{1/r}
\leq\frac{B_r}{n}.
\tag{15}
\]

This proves the missing stronger control; neither TV convergence by itself nor a loose last-step Rényi bound suffices for (15).

### 4.3 Cancellation of the linear term yields `n^-2`

Put `z=p/q-1`. We have `z>=-1` and `E_q z=0`. For integer `k>=2`, the finite binomial expansion and (15) give

\[
\int q\left(\frac pq\right)^k
=1+\sum_{j=2}^{k}{k\choose j}\mathbb E_q z^j
\leq1+\sum_{j=2}^{k}{k\choose j}\frac{B_j^j}{n^j}
\leq1+\frac{H_k}{n^2}.
\tag{16}
\]

The odd moments need not be nonnegative; the upper bound uses their absolute values. Taking logarithms proves the order-`k` bound in (6). Rényi divergence is nondecreasing in its order, so `D_alpha<=D_k`. Projecting the unprojected final updates is data processing, completing the proof for `X_T`. For `T=0`, the common initialization gives zero divergence. Reversing the adjacent datasets proves the reverse direction. QED.

## 5. A smooth nonconvex stationary example with matching `n^-2` order

The upper bound is not merely an artifact that could improve to zero for every nonconvex system. The following one-dimensional example has a positive stationary privacy loss of exact order `n^-2`, uniformly over all minibatch sizes.

Take `K=[-r,r]` with `r>0`. Fix `a>0` and `lambda>0` such that `a*r+lambda<=G`, and if a smoothness limit is prescribed also take `a<=M`. Define

\[
\ell_0(x)=-\frac a2x^2,\qquad
\ell_1(x)=-\frac a2x^2+\lambda x.
\tag{17}
\]

Both functions are smooth and strictly concave, hence nonconvex on this nontrivial interval. All gradients have absolute value at most `G`. Dataset `S` has `n` copies of `ell_0`; its neighbor `S'` replaces one copy by `ell_1`. Write `beta=1+eta*a`, `h=eta*lambda/b`, and `p_b=b/n`. Their chains are

\[
X_{t+1}=\operatorname{clip}_{[-r,r]}(\beta X_t+sZ_t),
\]

\[
Y_{t+1}=\operatorname{clip}_{[-r,r]}(\beta Y_t-hI_t+sZ_t),
\qquad I_t\sim\operatorname{Bernoulli}(p_b).
\tag{18}
\]

The contraction (8) gives unique invariant laws `pi_0,pi_1` and TV convergence to them from any initialization. One elementary existence proof is that `mu P^t` is Cauchy in TV since `TV(mu P^(t+1),mu P^t)<=rho^t`; probability measures are complete in TV. The limit is invariant and unique by contraction.

The maps in (18) preserve order because `beta>0`. Under common noises and common initial values, `X_t>=Y_t` for every `t`. Passing to stationary limits yields `pi_0` stochastically dominating `pi_1`.

Let `A_+=[0,r]`. Clipping preserves the sign of the pre-clipped value and the Gaussian probability of equality to zero is zero. Thus

\[
P_0(x,A_+)=\Phi(\beta x/s),
\]

\[
P_1(x,A_+)=(1-p_b)\Phi(\beta x/s)
             +p_b\Phi((\beta x-h)/s).
\]

Stationarity and stochastic domination, since `Phi(beta*x/s)` is increasing, imply

\[
\begin{aligned}
\pi_0(A_+)-\pi_1(A_+)
&\geq p_b\int\left[\Phi(\beta x/s)
                        -\Phi((\beta x-h)/s)\right]\pi_1(dx)\\
&\geq \frac{p_bh}{s}\,
   \phi\!\left(\frac{\beta r+h}{s}\right)\\
&\geq\frac{\eta\lambda}{ns}\,
   \phi\!\left(\frac{\beta r+\eta\lambda}{s}\right),
\end{aligned}
\tag{19}
\]

where `phi` is the standard normal density. The second inequality integrates the normal density over an interval of length `h/s`, wholly within absolute coordinate `(beta*r+h)/s`.

For all fixed `alpha>1`, monotonicity of Rényi divergence and Pinsker's inequality give

\[
D_\alpha(\pi_0\|\pi_1)
\geq D_{\rm KL}(\pi_0\|\pi_1)
\geq2\operatorname{TV}(\pi_0,\pi_1)^2
\geq\frac{2\eta^2\lambda^2}{n^2s^2}
 \phi\!\left(\frac{\beta r+\eta\lambda}{s}\right)^2.
\tag{20}
\]

The upper bound (6) holds for the invariant laws too. For example, their TV discrepancy satisfies (10) by passing to the limit, and the final-step proof applies directly to `pi_0 P_0=pi_0` and `pi_1 P_1=pi_1`. Thus, for `eta>0`,

\[
D_\alpha(\pi_0\|\pi_1)=\Theta(n^{-2}),
\tag{21}
\]

with strictly positive finite constants depending only on the fixed displayed parameters and `alpha`, uniformly for every `1<=b<=n`. This is a stationary, genuinely nonconvex example; no finite-time-only lower bound is being substituted for a plateau claim.

## 6. What this resolves, and what remains genuinely unresolved

* Under fixed `D,G,eta,s,alpha`, the requested T352 construction with a positive lower bound independent of `n` cannot exist for mechanism (1). This is a full-class impossibility result, not just a specially selected benign example.
* In this fixed-parameter interpretation, sample dependence `n^-2` is the sharp worst-case asymptotic order, including strictly nonconvex smooth losses. The first half of T352 does not need extra geometry merely to make the plateau vanish with sample size.
* The theorem does not give the convex result's good dependence on all parameters. For `R/s` large, `1/(1-rho)` and `E_r` are enormous. The need for useful geometric hypotheses is therefore not eliminated.
* If `D/s`, `eta*G/s`, or `alpha` grows with `n`, (6) may not tend to zero. A metastable counterexample in such a regime is not ruled out. T352 never fully specifies which parameters must stay fixed across its proposed counterexample family. Treating the fixed-parameter impossibility as solving every interpretation would be an overclaim.
* This proof applies to fresh iid uniform batches and full-batch training. Random reshuffling, deterministic cycling and data-dependent initialization require separate treatment. In particular, a cyclic schedule can expose the changed record immediately before release and need not have this sampling gain.
* The original 2022 source's broad convexity-relaxation question was already answered by later papers. This note does not certify that its particular `n^-2` formulation or proof is absent from the entire literature. It is a complete local derivation with a clear novelty boundary, not a publication priority claim.

Accordingly the exact acceptance status is **complete theorem and full-class obstruction; original-row/full-open-problem closure NOT established**.

## 7. Other whole-row candidates and why none was promoted

All 100 registry statements T323–T422 were screened. The following are the useful nearby decision points, rather than a claim of exhaustive theorem-level audit of all 100 papers.

| Row | Precise mathematical route | Completion or novelty barrier |
|---|---|---|
| T331 | Build a sparse-graph GNN with a nontrivial limiting classification probability, or extend the published zero-one theorem. | The exact fixed architecture, activation and classification-boundary assumptions must be retained. A threshold at a deterministic limiting score can manufacture a CLT counterexample even in dense graphs and may violate the source hypotheses. No valid whole-source counterexample is claimed here. |
| T332 | Couple radius-`L` ER/SBM neighborhoods to marked Galton–Watson trees; couple two roots to control empirical averages. | This is a strong full-family route with explicit growing-depth bounds, but local-limit machinery predates the row. Current relevant work includes [Pluska–Malhotra, arXiv:2510.21392](https://arxiv.org/abs/2510.21392), whose abstract explicitly addresses limiting MPNN behavior. The exact originally published unresolved theorem was not located by the prior registry audit. An elementary coupling lemma alone is not verified novel closure. |
| T344 | Small diverging widths repeated for growing depth create dying ReLU layers, contradicting a universal width-profile claim. | The source already has failures at very large depth and the registry already flags bottlenecks. A slow-width counterexample would repair another overbroad quantifier but would not automatically settle the original quantitative perturbation problem. |
| T352 | Universal fixed-parameter RDP theorem plus nonconvex stationary lower bound, proved above. | Best completed theorem here, but original all-parameter practical rate and publication novelty remain unresolved. |
| T355 | Quantitative homogenization near a normally attracting minimizer manifold. | Whole-row rates require uniform basin control, derivative bounds and an explicit long-time remainder, not just one solvable quadratic or the existing qualitative weak-limit theorem. |
| T366 | Positive-contraction theorem, then exact historical-forgetting transfer and matching lower bound. | Stale as a new iid rate target; see below. |
| T370 | Markov jump linear-system spectral-radius criterion for constant steps, stochastic approximation for decreasing steps, then a nonlinear target-network perturbation theorem. | The row joins three different tasks. Necessary-and-sufficient almost-sure conditions with general decreasing steps are not supplied by a mean matrix criterion. A simple linear criterion is not full closure. |
| T417 | Exact heavy-ball second-moment operator, then optimize step and momentum over a specified distribution family. | A narrow isotropic or finite-support family would be a selected special case. Power-law/Gaussian classification with minibatches and noise remains a real multivariate operator optimization problem. |

For T366, I opened [Dereziński–Dong, arXiv:2606.29593v1](https://arxiv.org/html/2606.29593v1), Theorem 3.1 and Lemma 3.6. Theorem 3.1 bounds the difference of consecutive iterates of the positive-contraction covariance operator by `3/(T+1)` in operator norm; Lemma 3.6 supplies the deterministic deletion estimate. These validate the freshness warning in `followup/target_selection.md`. Exact historical-loss and repeated-epoch interpretations still need careful reconciliation, but the formerly missing iid last-iterate rate is not a new open problem to claim.

No registry status was modified. This file gives the parent a complete theorem to review and an explicit reason not to misreport it as the full original solution requested by the user.
