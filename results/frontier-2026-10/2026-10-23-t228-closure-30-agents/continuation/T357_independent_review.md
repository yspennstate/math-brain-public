# Independent review: categorical random-feature calibration and one-step atom collapse

23 October 2026. Reviewer A29. No subagents. Author files and the frozen campaign were not modified.

**Verdict: PASS for both mathematical derivations, with the scope and quantifiers below. No required mathematical correction was found.** This is a fully proved categorical random-feature instance of the explicit tasks in the original T357 registry: an actual two-layer network, cross-entropy GD, a proportional-limit calibration characterization, and an informative early-stopping conclusion. It does not prove the stronger Gaussian-input dossier, generic-feature dynamics, overconfidence at every informative-teacher score, or publication novelty.

## 1. Exact material reviewed

| Item | SHA256 |
|---|---|
| `followup/categorical_rf_calibration.md` | `6c040b97f7d2300109d840a458c80151d59aea4916db987929dac8daf057aa9e` |
| `followup/T357_one_step_calibration_discontinuity.md` | `492e7cfeb4e7e302369fd4109f63efe215ff53b5c2e8b4bf4247c6a4ac735404` |
| `a03/registry422.jsonl` | `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0` |
| `a03/rows_T357_DOSSIER.md` | `4f150d1a55209ed37d8b1c6bca8e6ed85b9b4b50dbac24e616b5126791fb5ff9` |

T357 is JSONL line 357, rank 335. The exact line, excluding its terminating newline, has SHA256 `354d0cd4e71345e105368edaeedc7639da543a2cb8e476a6bfaa3df14715b330`. The author confirmed that the first file was stable at the hash above; its final numerical example was included in this review.

I independently checked the recurrences, occupancy limit, calibration functional, event probabilities, Taylor constants, stopping argument, divisor sums, and every displayed constant in the one-step supplement. Numerical calculations below are checks of the algebra, not proof substitutes.

## 2. Finite network, sampling and scaling

For a hidden weight matching cell $u$, its ReLU feature is exactly one on $u$ and zero elsewhere. Its output coefficient therefore changes by $c(S_u-N_u\sigma(z_u))$, so summing the $M_u$ identical coefficients gives

\[
z_{t+1}=z_t+cM_u(S_u-N_u\sigma(z_t)).
\]

This verifies actual full-batch GD, including the factor $M_u$. It is not a statement about a logistic MLE or a ridge estimator. The feature layer is frozen, as permitted by the registry's random-feature option. Zero initialization means the trainable output coefficients are zero, not that the frozen hidden weights vanish. The teacher is a unit-direction logistic single-index teacher because $\theta_*^T x_{j,\pm}=\pm1$, and the categorical input is isotropic.

The step is fixed on the **summed** empirical loss. A mean-loss implementation requires learning rate $cn_d$. Likewise, the network uses an unnormalized feature sum; importing another feature normalization without adjusting the rate changes the recursion. These are explicit choices, not omitted dimension factors. The sample and width ratios in the registry are $2\alpha$ and $2\gamma$, respectively. A bound on a constant mean-loss learning rate does not follow from this theorem.

The random features must be independent of the training data, as used explicitly in the proof. I read this as part of the specified model. The two finite-dimensional occupancy vectors have multinomial dependence across cells. Thus the introductory phrase “independent histogram cells” means that their training dynamics decouple given the counts; it must not be read as finite-dimensional probabilistic independence. The actual proof correctly uses multinomial counts and limiting independence, so this wording is not a proof gap.

Since $|S-N\sigma(z)|\le N$, induction gives $|z_t|\le ctMN$ for each finite integer $t$. No stability assumption on mixed-label cells is used or needed.

## 3. Occupancy limit and calibration continuity

Let $P_d$ be the random empirical law of $(H,M,S,F)$, where $F=N-S$, over the $2d$ equally likely test cells. For each fixed count state, its expectation converges to the claimed Poisson product mixture. For two distinct cells of prescribed types, the joint multinomial probability generating function converges to the product of the corresponding Poisson generating functions. State-indicator covariances therefore tend to zero. Their empirical average has variance tending to zero, proving convergence in probability of each state mass.

This extends to total variation, not merely weak convergence. In fact, with $C=M+S+F=M+N$,

\[
P_d(C>K)\le \frac{m_d+n_d}{2dK}
\]

holds deterministically. The limiting law has the analogous first-moment bound $(\alpha+\gamma)/K$. A finite-state truncation and the converging state masses imply

\[
\|P_d-P\|_1\longrightarrow0
\quad\text{in probability}.
\]

The count-to-score map is exactly the same for every dimension at a fixed step and iteration. For any such map $q=q(H,M,S,F)$, define

\[
\rho_P(\{q_0\})
=\sum_{s:q(s)=q_0}(p_{H(s)}-q_0)P(s).
\]

The unbinned calibration error is $\|\rho_P\|_1$. Combining equal score atoms before taking absolute values is essential. Directly,

\[
|\operatorname{CE}(P_d)-\operatorname{CE}(P)|
\le\|\rho_{P_d}-\rho_P\|_1
\le\|P_d-P\|_1.
\]

This proves the author's calibration convergence even when different count triples produce exactly equal scores. At any fixed limiting atom of positive mass, convergence of its numerator and denominator also validates the stated calibration curve. No claim concerning conditional probabilities outside the support is needed.

Population cross-entropy is bounded above by $\log2+ctMN$. At a uniformly chosen cell, the binomial count moments of every fixed order remain bounded; $M$ is independent of $N$. In particular the loss has uniformly bounded second moment for fixed $c,t$. Truncation therefore converts count-law convergence into convergence of the unbounded loss. This is sufficient for any fixed finite collection of times. The note does not assert a rate in $d$, convergence of the entire risk path uniformly over time, or a $d$-dependent stopping theorem.

## 4. Strict calibration error and informative stopping

Write

\[
b_m=\alpha e^{-(\alpha+\gamma)}\frac{\gamma^m}{m!}.
\]

The event $(M,N,S)=(m,1,1)$ has probability $b_m/2$, since averaging $p_H$ over the two teacher types gives $1/2$. Its reflected all-failure event has the same probability. The all-success logit starts at $cm/2$ and increases strictly thereafter; the failure logit is its negative. Choose $m=m_0\ge1$ with $\sigma(cm_0/2)>p$, which exists for every $c>0,p<1$.

For every score atom, $g_t(q)\in[1-p,p]$. Consequently,

\[
\operatorname{CE}_t\ge
\mathbb E\big[(q_t-p)_++(1-p-q_t)_+\big]
\ge b_{m_0}\big(\sigma(cm_0/2)-p\big).
\]

The two events lie in disjoint score regions. This checks both the factor of two and the fact that atom collisions cannot cancel their contributions. The lower bound is positive and independent of the positive integer $t$, at fixed $c,\alpha,\gamma,p$. It may be extremely small. It proves positive-measure overconfident score regions and positive CE, not overconfidence at every score or positive signed average overconfidence for an informative teacher. At $p=1/2$, $g_t\equiv1/2$, so the pure-noise specialization is also correct.

For $p>1/2$, put $D=S-N/2$ and $\delta=p-1/2$. Conditional on $H$, Poisson thinning gives

\[
\mathbb ED=\alpha(p_H-1/2),\qquad
\operatorname{Var}D=\alpha/4,\qquad
\mathbb ED^2=\alpha/4+\alpha^2\delta^2.
\]

Since $z_1=cMD$, the global logistic Taylor upper bound with second derivative at most $1/4$ gives exactly

\[
L_1\le\log2-c\alpha\gamma\delta^2
 +\frac{c^2}{8}(\gamma^2+\gamma)
 \left(\frac\alpha4+\alpha^2\delta^2\right).
\]

Thus $0<c\le4A/B$ implies the claimed strict risk improvement by at least $cA/2$. Bayes loss is $h(p)$, since the two teacher probabilities have equal entropy. Time zero is calibrated but fails this strictly improved risk target.

On $(M,N,S)=(1,1,1)$, probability $w=\alpha\gamma e^{-(\alpha+\gamma)}/2>0$, the logit increases to infinity. Its conditional population loss is at least $(1-p)z_t$. Nonnegativity of all other losses then gives $L_t\ge w(1-p)z_t\to\infty$. Every finite $L_t$ is finite. Therefore the limiting sequence $L_0,L_1,\ldots$ attains a minimum at a finite integer, and the small-step improvement excludes zero as a minimizer.

The resulting minimizing index is a deterministic index for fixed model parameters, may be nonunique, and has positive CE. The argument does not establish convergence of empirical/data-selected stopping rules or finite-dimensional oracle minimizers. The author's explicit restriction to a deterministic iteration index is appropriate. Exact calibration at a useful positive deterministic stopping index is impossible in this model; approximate calibration-risk optimization is a separate question.

## 5. Independent verification of the one-step supplement

Under the positive teacher, write $K=S-F$, where $S,F$ are independent Poisson variables with means $\alpha p,\alpha(1-p)$. For integer $k$, the displayed series for $A_k=\Pr(K=k\mid H=+)$ follows by summing over $F=j,S=j+k$. Reindexing verifies

\[
A_{-k}(\alpha,p)=A_k(\alpha,1-p),\qquad
A_k(\alpha,p)/A_k(\alpha,1-p)
=\left(p/(1-p)\right)^k.
\]

For $r\ne0$, $R=MK=r$ requires the positive integer $M$ to divide $|r|$. Summing precisely these disjoint events gives the finite divisor sums $u_\pm(r)$. For $r=0$, the disjoint possibilities $M=0$ and $M>0,K=0$ give the stated $\mu_0$; reflection makes $g_0=1/2$. All integers $r\ne0$ have positive mass, since $M=1$ and $K=r$ have positive probability. For every $c>0$, $r\mapsto\sigma(cr/2)$ is injective, so the posterior-type calculation defining $g_r$ is exact.

The likelihood-ratio identity is strictly greater than one for every positive $k$. Hence every positive divisor summand satisfies $A_{r/m}(p)>A_{r/m}(1-p)$, giving $g_r>1/2$ for $r>0$. Symmetry yields the exact factor-two formula

\[
\mathrm{CE}_1(c)=2\sum_{r>0}\mu_r|g_r-\sigma(cr/2)|.
\]

There is no missing factor of two in its zero-rate limit: specifically,

\[
2\mu_r(g_r-1/2)=\delta\big(u_+(r)-u_-(r)\big).
\]

Summing over positive $r$ first conditions on $M>0$ and preserves the sign of $K$. Dominated convergence therefore gives exactly

\[
L_0=\delta(1-e^{-\gamma})
 \big[\Pr(K>0\mid H=+)-\Pr(K<0\mid H=+)\big]>0.
\]

For clarity, this supplement's symbol $L_0$ denotes a calibration limit, whereas the main note uses $L_0=\log2$ for initial log-loss. The definitions are internally clear but the two symbols must be distinguished when combining the notes.

The $k=1$ difference is

\[
A_1-A_{-1}
=e^{-\alpha}\alpha(2p-1)
 \sum_{j\ge0}
 \frac{\big(\alpha^2p(1-p)\big)^j}{j!(j+1)!}
\ge2\alpha\delta e^{-\alpha}.
\]

All other positive-$k$ pairs contribute nonnegatively. Multiplication by $\delta(1-e^{-\gamma})$ verifies the lower bound $2\alpha\delta^2e^{-\alpha}(1-e^{-\gamma})$.

Finally, reverse triangle inequality and the sigmoid Lipschitz constant $1/4$ give

\[
|\mathrm{CE}_1(c)-L_0|
\le\mathbb E|\sigma(cR/2)-1/2|
\le\frac c8\mathbb E|R|
\le\frac{c\alpha\gamma}{8},
\]

because $M\perp K$ and $|K|\le S+F$. The stated step restriction makes this deviation at most half of the explicit $L_0$ lower bound. Its intersection with $0<c\le4A/B$ is nonempty and yields both risk improvement and the positive CE floor.

At exactly $c=0$, all scores merge and the population conditional mean becomes $1/2$. Thus zero-rate discontinuity is real; weak or uniform convergence of numerical score values does not preserve unbinned calibration. The result is for exact real-valued probabilities and does not assert a discontinuity for fixed bins or rounding. The limit is taken in the proportional-limit model as $c\downarrow0$; the stated connection to finite networks is for each fixed $c>0$. No unsupported interchange with a dimension-dependent rate is used. At $p=1/2$, the informative term vanishes and the separate bound $\mathrm{CE}_1(c)\le c\alpha\gamma/8$ is correct.

## 6. Arithmetic cross-checks

At $\alpha=3,\gamma=2,p=3/4,c=1/10$, exact rational arithmetic gives

\[
A=3/8,\quad B=63/8,\quad 4A/B=4/21,
\quad cA-c^2B/8=177/6400.
\]

An independent sum using the three independent counts $M,S,F\in\{0,\ldots,40\}$, grouping by the integer $R=M(S-F)$ before evaluating calibration, gives:

| Quantity | Floating-point check |
|---|---:|
| $L_1(0.1)$ | 0.6652569920635 |
| $\log2-177/6400$ | 0.6654909305599 |
| $\mathrm{CE}_1(0.1)$ | 0.0875079784455 |
| positive-rate calibration limit $L_0$ of the supplement | 0.1308074461568 |
| explicit lower bound on that limit | 0.0161434205133 |
| $\mathrm{CE}_1(0.005)$ | 0.1285658261602 |
| $\mathrm{CE}_1(0.0001)$ | 0.1307626109867 |

The retained mass is approximately $0.999999999999999$. Also $m_0=22$ is valid at $c=0.1,p=3/4$, and the main note's calibration lower bound is approximately $1.96197\times10^{-20}$. These checks agree with the claims and illustrate why the uniform-in-time strict-positive bound is not a claim of large typical overconfidence.

## 7. Original T357 versus the Gaussian dossier

The exact operative request in the registry is:

> Prove a comparable theorem for a two-layer network trained by gradient descent on cross-entropy in a solvable regime (random features, or mean-field with a single-index teacher): characterize the calibration error as a function of n/d, width and training time, and show whether early stopping yields calibration.

It does not specify Gaussian inputs, a particular random-feature distribution, training of both layers, or a universal all-score sign assertion. Those restrictions must not be silently imported from the later dossier. Conversely, the source paper's stronger all-confidence-level conclusion must not be silently attributed to this categorical example.

| Original requested element | What is fully established here |
|---|---|
| Two-layer network in a solvable random-feature regime | Frozen categorical ReLU features; actual trainable output layer; informative single-index teacher. |
| Gradient descent on cross-entropy | Exact finite-network recurrence for full-batch discrete GD with specified objective scaling. |
| Sample ratio, width, training time dependence | Explicit Poisson mixture, exact score-conditioning formula, and risk sequence for all fixed finite integer times. |
| Calibration/overconfidence phenomenon | Positive CE and positive-mass overconfident regions at every positive time; exact one-step curve and a positive small-step CE floor. |
| Early stopping and a useful risk target | A positive finite risk-minimizing limiting index exists for the specified small-step regime and is miscalibrated; only zero is exactly calibrated. |

The dossier's `STATEMENT` instead fixes Gaussian single-index inputs; its architecture and later calculations concern Gaussian equivalence and tanh features. The occupancy proof supplies none of that dynamical equivalence. The categorical input/feature geometry makes this a solvable occupancy model and should remain visible in every description of the result.

For the comparison with the named source, I directly read [Bai–Mei–Wang–Xiong, arXiv:2102.07856v2](https://arxiv.org/html/2102.07856v2), Section 2.1, equations (1)–(2), and Section 3, Theorem 1 and Corollary 2. These define the same unbinned CE and score-conditional sign. Their theorem concerns Gaussian logistic MLE, small positive $d/n$, and positive signed error at every score above $1/2$, with a small-$d/n$ expansion. The present informative-teacher theorem proves a different sign scope and does not claim that expansion. No imported theorem from that paper is needed for the elementary categorical proof.

**Accepted description:** a rigorously proved categorical random-feature instance answering the original registry's explicit calibration-and-stopping tasks, with exact GD-time dependence and a nontrivial risk target. **Not accepted:** Gaussian/general-network closure, universal informative-teacher overconfidence, a quantitative convergence rate in dimension, a data-dependent stopping theorem, or a publication-priority claim. The registry's unchecked broad status line is not a literature theorem and this review does not certify it.
