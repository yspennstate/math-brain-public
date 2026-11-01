# Original-problem scope audit: T357 and T336

Author: A30. Date: 2026-10-23. This is an internal, independent reading of the original registry and the mathematical proofs identified below. It does not edit a registry, certify publication novelty, or certify remote persistence. The original registry's unchecked statements about what is open are not accepted as literature findings.

## 1. Decision and counting boundary

**T357:** the categorical random-ReLU-feature construction answers every operative task in the original row for an explicitly permitted solvable random-feature regime. It supplies a genuine two-layer network and actual discrete gradient descent, an informative single-index teacher, dependence on sample ratio, width and training time, score-conditional overconfidence, and a nonvacuous negative answer to calibration by early stopping. The strengthened results below cover arbitrary finite data-dependent stopping and, in an explicit overparameterized regime, simultaneous first-step risk improvement and overconfidence at every nonneutral score atom. The chosen input and feature distributions must accompany a completion claim. This is not a completion of the later Gaussian-input dossier or a generic neural-network theorem.

**T336:** the exact finite-rank polynomial-GP representation and non-singleton ERM theorem satisfy a precise specified-prior reading of the original request: representation is uniform over all real-label datasets, while learned convergence is in prior-averaged forward KL. The original text does not specify the topology of learned convergence. It therefore does not force a learned uniform-all-label guarantee, but it also does not justify presenting that stronger guarantee as proved. The result is a completed theorem for the stated prior, architecture and learning criterion, not an arbitrary-GP or stock-transformer theorem.

These judgments distinguish satisfying an instantiated mathematical request from establishing a new result in the literature. Neither the unchecked registry nor this audit establishes a priority claim or an official solved-problem count.

## 2. Exact original text and later specialization

The source is `a03/registry422.jsonl`, SHA-256 `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0`. Line hashes below exclude the terminating newline.

### T357, line 357, rank 335

Title: **Overconfidence of overparameterized classifiers**.

The complete original `statement` is:

> Bai, Mei, Wang and Xiong prove that logistic regression fitted by maximum likelihood in the proportional regime (n, d → ∞, n/d fixed) is overconfident: its predicted probabilities exceed the true conditional probabilities, even without overparameterization. Prove a comparable theorem for a two-layer network trained by gradient descent on cross-entropy in a solvable regime (random features, or mean-field with a single-index teacher): characterize the calibration error as a function of n/d, width and training time, and show whether early stopping yields calibration.

Exact JSON-line SHA-256: `354d0cd4e71345e105368edaeedc7639da543a2cb8e476a6bfaa3df14715b330`.

The row has `ledger_status: unverified` and `where_it_stands_checked: false`. Its locator itself begins “to verify.” No Gaussian input law, hidden-weight law, fixed activation, training of both layers, or numerical convergence rate in dimension is specified. The random-feature option expressly allows a frozen hidden layer. The phrase “comparable theorem” still requires a real score-conditional overconfidence conclusion; positive calibration error alone would not establish its sign.

The later `a03/rows_T357_DOSSIER.md` makes a narrower choice. Its operative repaired statement is:

> Repaired statement (the audit: use the source's score-conditional definition of over-confidence, state the regime where the MLE exists, choose the network class, initialization, signal scaling and a population calibration metric other than binned ECE; early stopping must also meet a risk target): for one Gaussian single-index teacher P(y = 1 | x) = sigma(beta <w*, x>) and random-feature logistic regression (N features, ridge lambda or gradient-flow time t, n/d and N/d proportional), derive the population score-calibration curve E[y | p_hat = p] - p and the excess risk along training, and decide whether a stopping time improves a joint calibration-risk objective.

Its architecture and subsequent calculations concern Gaussian equivalence and tanh features. That Gaussian target is established by the dossier, but it is an additional specialization, not a restriction present in the original registry. It must not be silently substituted for the original request in either direction.

For comparison with the named primary source, I read [Bai–Mei–Wang–Xiong, arXiv:2102.07856v2](https://arxiv.org/html/2102.07856v2), Sections 2.1–2.2 and Theorem 1/Corollary 2. They use population score conditioning and unbinned calibration error. Their Gaussian logistic-MLE theorem establishes overconfidence at every confidence level above one half for small positive dimension/sample ratio, with a first-order expansion. Our categorical construction has different geometry and a different proof mechanism; it does not establish that expansion or reproduce their underparameterized dense-design phenomenon.

### T336, line 336, rank 314

Title: **Transformers as amortized Bayesian inference: approximation and generalization**.

The complete original `statement` is:

> Müller et al. train transformers on datasets sampled from a prior over data-generating processes so that the network outputs the posterior predictive distribution (prior-data fitted networks). Give quantitative guarantees: for a given prior (e.g. a Gaussian process prior), bound the size of transformer needed to approximate the posterior predictive within epsilon in KL uniformly over datasets of size N, and the number of pretraining datasets needed, and show that the pretrained network's predictions converge to the Bayes predictor as both grow.

Exact JSON-line SHA-256: `f0b9babf34c4b5b0e656737f8acbce6b6782e26c448487d1600d763c7295aa89`.

This row also has `ledger_status: unverified` and `where_it_stands_checked: false`. It does not choose a prior, architecture, noise convention, KL direction, label bound, optimization algorithm, or convergence mode for learned predictions. It explicitly requires uniformity in the representation clause. Choosing a prior does not license changing “uniformly over datasets” into bounded-label or average representation error.

## 3. T357 obligation map

| Original obligation | Verified categorical result | Boundary |
|---|---|---|
| Two-layer network in a solvable regime | ReLU random-feature network with frozen independently sampled hidden weights and trained output weights | The features are axis-aligned indicators on categorical inputs |
| Gradient descent on cross-entropy | Exact full-batch discrete-GD recurrence from zero initialization | Step `c` is for summed loss; the equivalent mean-loss rate is `c n_d` |
| A meaningful teacher | Logistic single-index teacher with unit signal direction and nonzero finite signal | Inputs are isotropic categorical, not Gaussian |
| Dependence on sample ratio and width | Explicit countable Poisson mixture with parameters `alpha=lim n_d/(2d)` and `gamma=lim m_d/(2d)` | Ratios in the row are `2 alpha` and `2 gamma` |
| Dependence on training time | Exact recurrence for every integer time; entire population score-trajectory law converges in total variation | Fixed positive `c`; no changing-step-size limit is inferred |
| Population calibration | Exact score-conditional curve, CE and signed overconfidence; CE/OC convergence is uniform over all integer times | Coincident score atoms must be grouped before conditioning |
| Overconfidence, not merely miscalibration | Positive-mass overconfident score regions at every positive time; every nonneutral first-step atom is overconfident in a stated regime | The all-score first-step assertion is not asserted at every later time |
| Whether useful early stopping calibrates | Uniform positive CE at every positive time, including arbitrary finite data-dependent choices; an actual finite-dimensional population-risk oracle exists and is positive with high probability in the informative regime | This is an oracle-risk statement, not an efficient validation-selection algorithm |

The theorem is mathematically elementary because the hidden features have disjoint supports on the data distribution. This makes its mechanism histogram overfitting with random feature coverage. It remains a valid random-feature network within the original existential regime choice. Its tractability must remain visible when describing what has been completed.

## 4. Independently checked categorical certificate and strengthenings

### 4.1 Model, law and exact calibration

Let the input be uniform on `x_(j,+)=sqrt(d)e_j` and `x_(j,−)=−sqrt(d)e_j`, `1<=j<=d`. Its covariance is the identity. The true label probabilities are `p_+=p`, `p_−=1−p`, with `1/2<p<1`. This is the logistic teacher with unit direction `(1,...,1)/sqrt(d)` and signal `beta=log(p/(1−p))`.

Each frozen hidden weight is independently uniform on `{+e_j/sqrt(d),−e_j/sqrt(d)}`. A ReLU feature is exactly one on its matching input cell and zero on every other input. For a cell, let `M` be its matching-feature count, `N` its training count, and `S` its positive-label count. Full-batch GD on summed logistic loss gives exactly

\[
z_0=0,\qquad z_{t+1}=z_t+cM\{S-N\sigma(z_t)\},\qquad q_t=\sigma(z_t).
\tag{1}
\]

As `n_d/(2d)->alpha>0`, `m_d/(2d)->gamma>0`, the empirical law `P_d` of cell state `(H,M,S,N−S)` converges in probability in the count-mass `l1` norm to the law `P` with equiprobable `H=+,-`, independent `M~Pois(gamma)` and `N~Pois(alpha)`, and `S|(N,H)~Bin(N,p_H)`. Its weights are

\[
w_H(m,n,s)=\tfrac12e^{-\alpha-\gamma}
 \frac{\gamma^m}{m!}\frac{\alpha^n}{n!}
 \binom ns p_H^s(1-p_H)^{n-s}.
\tag{2}
\]

The proof uses convergence of one-cell and two-cell multinomial counts to independent Poisson limits, variance convergence of empirical count-state frequencies, and a finite-state truncation with bounded expected count tails. It is convergence of the whole count law, not only finitely many moments.

For each score atom `q`, set `mu_t(q)=sum_(q_t=q)w_H` and `nu_t(q)=sum_(q_t=q)p_H w_H`. Then

\[
g_t(q)=\frac{\nu_t(q)}{\mu_t(q)},\quad
\mathrm{CE}_t=\sum_q|\nu_t(q)-q\mu_t(q)|,
\quad
\mathrm{OC}_t=\sum_q\{q\mu_t(q)-\nu_t(q)\}
                    \operatorname{sign}(q-\tfrac12).
\tag{3}
\]

CE is the unbinned population `L1` calibration error. OC measures signed overconfidence for the predicted class. These are different quantities outside a regime where every nonneutral score is overconfident. The risk and excess risk are

\[
L_t=\sum w_H\{\log(1+e^{z_t})-p_Hz_t\},\qquad
R_t=L_t-h(p).
\tag{4}
\]

Equation (1) is a dimension-independent map at fixed `c`. Mapping a state to its **entire countable trajectory** `(H,(q_t)_(t>=0))` therefore preserves total-variation convergence. More specifically, the signed calibration measure is the pushforward of `(p_H−q_t)P`. The triangle inequality for its total-variation norm gives

\[
\sup_{t\ge0}|\mathrm{CE}_d(t)-\mathrm{CE}_t|
 \le\|P_d-P\|_1\longrightarrow0
 \quad\text{in probability}.
\tag{5}
\]

The same bound holds for OC, because its integrand has absolute value at most one. This proves uniform calibration convergence over all discrete times. It does not assert uniform convergence of the ratios `g_t(q)` at atoms of vanishing mass. Risk is unbounded, so (5) does not extend to uniform-time risk. For each fixed finite time, `|z_t|<=ctMN` and bounded count moments give uniform integrability and `L_d(t)->L_t` in probability.

### 4.2 All positive stopping times remain miscalibrated

Fix any positive integer `m0` with `q0=sigma(c m0/2)>p`. Define

\[
g_0=q_0-p>0,\qquad
b=\alpha e^{-\alpha-\gamma}\frac{\gamma^{m_0}}{m_0!}>0,
\qquad
J_d=\frac{\#\{\text{cells}:M=m_0,N=1\}}{2d}.
\tag{6}
\]

Here `g_0` is a gap, not a calibration curve at time zero. On each such cell the observed label is either one or zero. In the first case its logit starts at `cm0/2` and increases thereafter; in the second case it is the negative of that trajectory. At every finite dimension, conditional on the trained network, the true score-conditional label probability is a convex combination of `p` and `1−p`. Thus, for every realization and **simultaneously for every `t>=1`**,

\[
\mathrm{CE}_d(t)
\ge \mathbb E_X[(q_t-p)_++(1-p-q_t)_+]
\ge g_0J_d.
\tag{7}
\]

Score collisions cannot cancel these errors outside `[1−p,p]`. The occupancy convergence gives `J_d->b` in probability, so

\[
\Pr\!\left\{\inf_{t\ge1}\mathrm{CE}_d(t)\ge\frac{g_0b}{2}\right\}
\longrightarrow1.
\tag{8}
\]

This covers every finite stopping index `T_d>=1`, including choices depending on dimension, the training sample, the random features, and independent selection data. The index selects one network for future fresh predictions; it is not a different time selected separately for each fresh test input. There is no exchange of a fixed-time limit and a random-time limit in (7).

Time zero has prediction one half and is exactly calibrated, with population risk `log 2`. A pathwise or high-probability risk target `L_d(T_d)<=log 2−epsilon` excludes time zero on its success event. Expected risk improvement alone does not imply `T_d>0` with high probability and must not be used to claim that exclusion.

### 4.3 Informative risk improvement and an actual finite-dimensional risk oracle

Put `delta=p−1/2`,

\[
A=\alpha\gamma\delta^2,\qquad
B=(\gamma^2+\gamma)(\alpha/4+\alpha^2\delta^2).
\]

The logistic loss has second derivative at most one quarter. Since `z1=cM(S−N/2)`, direct conditioning gives

\[
L_1\le\log2-cA+c^2B/8.
\tag{9}
\]

In particular `0<c<=4A/B` gives a strict improvement at least `cA/2`. More generally, any explicitly proved positive first-step gap suffices for the following argument.

On a finite-dimensional realization with `J_d>0`, at least one covered singleton cell has an all-success or all-failure trajectory. Its absolute logit tends to infinity: a finite limit would leave an increment bounded away from zero. Its true minority probability is at least `1−p>0`, so its population loss tends to infinity. Since every other cell loss is nonnegative, `L_d(t)->infinity` as `t->infinity` on this realization. Every finite-time risk is finite. Hence the integer risk sequence has a finite minimizer.

If `L1<=log 2−eta` for some fixed `eta>0`, fixed-time risk convergence implies `L_d(1)<log 2−eta/2` with probability tending to one. Together with `J_d->b>0`, this proves that a population-risk-minimizing integer `T_d*` exists, is finite and positive with high probability, and obeys the CE lower bound (8). This is stronger than existence of a minimizer of the limiting risk sequence; it needs no uniform-time risk convergence. It is an oracle population-risk statement, not an algorithm for estimating the best time from a finite validation sample.

### 4.4 All nonneutral first-step scores are overconfident

Write `K=S−(N−S)` and `R=MK`. At the first step, `z1=cR/2`, with integer `R`. If

\[
c>2\log\frac p{1-p},
\tag{10}
\]

then at every positive score atom, `q>=sigma(c/2)>p>=g(q)`. At every negative score atom, `q<=1−sigma(c/2)<1−p<=g(q)`. These are overconfident predictions for their respective predicted classes. Reflection symmetry of the limiting law makes the neutral score one half calibrated. Consequently

\[
\mathrm{CE}_1=\mathrm{OC}_1
\ge[\sigma(c/2)-p](1-e^{-\gamma})[1-A_0(\alpha,p)]>0,
\tag{11}
\]

where `A0(alpha,p)=Pr(K=0|H=+)`. The equality uses limiting symmetry; a realized finite-dimensional neutral-score group need not be exactly balanced. The nonneutral pointwise sign is already true in finite dimensions. At `p=1/2`, the same assertion holds for every `c>0`.

The assertion is on the actual score support. It does not assign conditional probabilities to confidence values outside that support. At later times (7) supplies overconfident regions and positive CE; the all-score conclusion (10) is specifically a first-step result.

### 4.5 One explicit regime has overparameterization, learning and all-score overconfidence together

The large-step condition (10) and the sufficient small-step bound following (9) need not overlap. The following direct estimate avoids treating them as though they did.

Take

\[
p=9/10,\qquad c=5,\qquad
\alpha=1/200,\qquad\gamma=3/200.
\tag{12}
\]

Then `m_d/n_d->3`, so there are asymptotically three trainable output coefficients per training example. Moreover `5>2 log 9`, so (10) applies. Conditional on `M=N=1`, averaging over the observed label and teacher type gives the exact risk increment

\[
d_1=\log\cosh(5/4)-4/5<-2/15.
\tag{13}
\]

For completeness, `e^(5/2)>12` follows from the exponential Taylor sum through degree six, and `log 2>2/3` follows from `log(1+x)>2x/(2+x)` at `x=1`. Therefore

\[
\log\cosh(5/4)
=5/4-\log2+\log(1+e^{-5/2})
<5/4-2/3+1/12=2/3,
\]

which proves (13). On all remaining count states the increase in population logistic loss is at most `|z1|<=cMN/2`. The event in (13) has mass `w11=alpha gamma e^(−alpha−gamma)` and contributes one to `MN`. Hence

\[
\begin{aligned}
L_1-\log2
&\le w_{11}d_1+\tfrac52(\alpha\gamma-w_{11})\\
&\le-\frac{121}{1500}\alpha\gamma<0,
\end{aligned}
\tag{14}
\]

using `alpha+gamma=1/50` and `e^(−1/50)>=49/50`. Thus a single informative, overparameterized regime has first-step risk improvement and overconfidence at every nonneutral score atom. Equations (7)–(8) and the finite-dimensional risk-oracle conclusion also apply. The constants can be small; none of these lower bounds is a claim of a large practical calibration effect.

The exact one-step divisor-sum calibration formula and its positive-rate discontinuity at zero step size are further accepted results in the pinned supplement. They are not needed to turn a purely noisy teacher into the informative example (12).

## 5. The separate Gaussian one-step theorem and its remaining boundary

During this audit the Gaussian follow-up was finalized. A26's `followup/T357_gaussian_first_step_attempt.md` now contains the one-test and two-fresh-test-replica limits; A28's independent review accepts those results at the final source hash listed below. A29's `followup/T357_gaussian_calibration_consequences.md` derives their scalar calibration and risk consequences. I read the final independent review and the consequences report, and independently checked the scalar conditioning, calibration-witness and scope arguments. The detailed independent Gaussian CLT audit is A28's work; it is not recertified merely by listing it here.

For Gaussian inputs, Gaussian tanh features and a logistic teacher, the one-step limit has the form `(Z,S1)->(Z,c k Z+c tau G)` with independent standard normals. In A29's notation,

\[
a=E[G\tanh G],\quad b=E[\tanh^2G],\quad
\mu=E[Z\{\sigma(\beta Z)-1/2\}],\quad k=a^2\mu,
\]
\[
\tau^2=\frac{\mu^2a^2b}{\gamma}
+\frac{a^4+b^2/\gamma}{4\alpha}>0,
\qquad \alpha=\lim n_d/d,\quad\gamma=\lim m_d/d.
\tag{G1}
\]

These Gaussian ratios use `d`, whereas the categorical ratios above use `2d`. The exact score normalization and corresponding GD learning rate are stated in the Gaussian proof and must not be inferred from the categorical convention.

An annealed weak limit alone does **not** prove convergence of a realized trained network's exact conditional calibration error. Calibration is not continuous under ordinary weak convergence, as the categorical small-step example itself demonstrates. The separate two-replica result supplies concentration of fixed bounded test observables. Its combination with continuous bounded score-measurable witnesses yields, for every fixed `c>0` and `epsilon>0`,

\[
\Pr\{\mathrm{CE}_d\ge C_G(c)-\epsilon\}\longrightarrow1,
\]

where `C_G(c)>0` for the informative noisy limiting Gaussian model. The strict positivity follows because a logistic-normal mixture has a different tail prefactor from every logistic curve: matching exponential decay rates cannot match the positive Gaussian-variance prefactor. The replica theorem and a second-moment bound also give convergence of conditional population log-loss in `L1` over trained predictors. There is an explicit small-positive-rate regime with strict risk improvement and a positive calibration lower bound; sufficiently large rates have signed average overconfidence.

These accepted statements are useful Gaussian **one-step** progress. They do not give exact CE convergence, a full later-GD calibration-risk path, a conclusion about all useful stopping times, or calibration at data-dependent rates. The unique optimal first-step learning rate in A29's scalar calculation is not an optimal stopping time. Thus the Gaussian dossier's full training-time and stopping target remains incomplete. The original T357 completion in the explicitly allowed categorical regime does not depend on these separate Gaussian results.

## 6. T336: exact quantifiers and the remaining interpretation boundary

The accepted theorem fixes a known finite-rank polynomial GP on a compact raw-input domain, positive known observation-noise variance `s`, and a maximum context length `n`. A concrete nonconstant example is

\[
f(x)=G_0+G_1x+G_2x^2,\qquad x\in[-1,1],\qquad
(G_0,G_1,G_2)\sim N(0,I_3),
\]

with independent `N(0,s)` observation noise. It handles continuous and repeated designs, every real label vector, and a nontrivial posterior; it is not a constant predictor or a finite-domain lookup table.

The architecture is a costed residual length-normalized ReLU-attention transformer, with one ordinary full-token LayerNorm feed-forward stage, structural scratch-token routing and source cancellation, and an exact raw-label linear readout. It is not asserted to be a stock softmax transformer with full pre-normalization at every block.

| Original T336 clause | Proven quantified statement | Not implied |
|---|---|---|
| For a given prior | The stated polynomial finite-rank GP family, including the quadratic example | Every possible given prior or an infinite-rank RBF GP |
| Size needed for uniform KL approximation | Explicit finite network depth, width, heads and total stored entries; exact posterior coefficients and noisy variance | Finite-bit robustness or an arbitrary architecture |
| Uniform over datasets of size N | For each fixed maximum `n`, all raw covariates, repeated designs, lengths at most `n`, and all real context labels; representation KL is exactly zero | A bounded-label substitution |
| Number of pretraining datasets | Explicit high-probability approximate-ERM sample bound for independent genuine GP tasks, without label clipping | SGD optimization convergence |
| Learned convergence to Bayes as capacity and data grow | Prior-averaged forward KL tends to zero for capacity/sample sequences satisfying the displayed bound; almost-sure risk convergence follows with summable failure probabilities | Worst-label uniform convergence of the learned network, or arbitrary uncontrolled capacity growth |

The exact representation uses the Cauchy–Binet sum-of-squared-minors identity for `det(s I+Phi^T Phi)`, calibrated LayerNorm for its exact reciprocal, and polynomial adjugate numerators. The compiler counts raw polynomial-feature evaluation, cofactors, routing, erasure/reloading and readout. The ordinary full-token normalization stage transmits only a fixed difference of two equal source coordinates, so source-label effects cancel identically; its surviving scratch computation is label independent.

The learning class is genuinely non-singleton. The designated feature/coefficient arithmetic weights vary over a compact box, while routing, normalization gains/biases and source-cancelling selector, coefficient/variance clips, and final label-linear readout stay structurally fixed. Every parameter therefore gives a design-dependent coefficient vector and variance, with mean `a_theta(Z)^T y`. The exact posterior is one comparator in the larger class. The explicit coefficient-bias subfamily only witnesses non-singletonness; the main theorem is not ERM over a singleton or a frozen exact-Bayes computation.

The bound is quantitative. In the notation of the pinned proof, with explicitly propagated parameter-Lipschitz constants and

\[
u=P\log(2+2W/\rho)+\log(4/\delta),
\]

an optimization error at most `epsilon/4` and

\[
J\ge\max\{1,512A_0^2u/\epsilon^2,8A_0u/\epsilon\}
\tag{15}
\]

give prior-averaged forward KL at most `epsilon` with probability at least `1−delta`, for the proof's explicit choice of `rho`. All constants, including `A0`, are finite computable functions of the prior, noise, context bound, compiler and parameter box. The statistical proof controls unbounded Gaussian labels with a subexponential loss envelope. It makes no label-clipping assumption.

### Why uniform representation and averaged learning must remain separate

At a fixed design, let the true noisy predictive be `N(a^T y,v)` with `v>0`. Suppose a learned coefficient vector differs from `a`. Even allowing the predicted variance to depend arbitrarily on labels, the elementary Gaussian identity gives

\[
\inf_{w>0}\mathrm{KL}\{N(m,v)\Vert N(\widehat m,w)\}
=\tfrac12\log\!\left(1+\frac{(m-\widehat m)^2}{v}\right).
\tag{16}
\]

Taking `y=t(a−ahat)` makes this diverge whenever `ahat!=a` (a fixed additive mean bias does not change the conclusion). Thus arbitrarily small nonzero coefficient errors generally give infinite worst-label KL. Approximate ERM and coefficient convergence do not turn into learned uniform-all-label convergence.

The word “uniformly” in the original sentence explicitly qualifies the size/approximation clause. The later convergence clause does not state a mode. A prior-average learning theorem is also the natural population criterion of prior-data fitting: [Müller et al., arXiv:2112.10510v7](https://arxiv.org/pdf/2112.10510v7), Corollary 1.1 on printed page 4, identifies expected NLL with prior-averaged forward KL plus a model-independent constant. That identity alone supplies no finite-sample bound. The accepted construction therefore meets a defensible precise reading of the actual original words. It would be an overstatement to say those words uniquely force that reading, or that the theorem covers a stronger learned-uniform interpretation.

**Accepted T336 wording:** “For a specified polynomial finite-rank GP and the stated transformer architecture, an explicit finite network represents the posterior predictive exactly over all real-label datasets of bounded size; a genuine structured ERM class has an explicit pretraining bound and converges to Bayes in prior-averaged forward KL.”

**Unsupported T336 wording:** “The trained transformer converges uniformly over every possible dataset,” “the GP case is solved for arbitrary kernels,” or “a standard transformer trained by SGD has these guarantees.” The earlier bounded-label A02 approximation and A05 average ERM pair alone did not prove the all-label representation clause; the exact reciprocal construction is the substantive new completion of that clause.

## 7. Reviewed snapshots and final acceptance

The following immutable-content hashes identify the versions used in this audit. An edited future version is not silently covered.

| File | SHA-256 |
|---|---|
| `a03/registry422.jsonl` | `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0` |
| `a03/rows_T357_DOSSIER.md` | `4f150d1a55209ed37d8b1c6bca8e6ed85b9b4b50dbac24e616b5126791fb5ff9` |
| `followup/categorical_rf_calibration.md` | `6c040b97f7d2300109d840a458c80151d59aea4916db987929dac8daf057aa9e` |
| `followup/T357_one_step_calibration_discontinuity.md` | `492e7cfeb4e7e302369fd4109f63efe215ff53b5c2e8b4bf4247c6a4ac735404` |
| `followup/T357_independent_review.md` | `633574459e64ef2ffcc066d41646c60b7ba5eda009b44bca88a18726325cdfc6` |
| `followup/T357_CATEGORICAL_COMPLETE_THEOREM.md` | `2afde40ad003392b17d90cbc90f94a87d96fcef2771695a03c35af62b271c3bd` |
| `followup/T357_gaussian_first_step_attempt.md` | `1469aad3c34b902a363fe66d32eff199c451adc28d2ae5ae4de6cbb716fd630b` |
| `followup/T357_gaussian_first_step_independent_review.md` | `7c9b8412cc8d38e184972b9256773d7854cf7878b2bb2e1df5a8eafda80fc73f` |
| `followup/T357_gaussian_calibration_consequences.md` | `124e5b2782f1fa000fc0103f04ce834eaaa70bb18b1483dfbd0d64fe0b4363fd` |
| `followup/T336_scope_and_obstruction.md` | `5c1ea4e7c3691c4eef8814b25ede5ebb9997b476c524fbf674cfed55b9bb75d0` |
| `followup/T336_architecture_compiler.md` | `8dbb67bbc8609cb86b0a1fb888f61c64abf36b07c8ebfc0464b0d0e5a4adf175` |

**Independent mathematical acceptance: PASS for the integrated categorical theorem at SHA-256 `2afde40ad003392b17d90cbc90f94a87d96fcef2771695a03c35af62b271c3bd`.** I read its complete final text, including the explicit pre-query stopping clarification, and checked the exact GD recurrence and scaling, occupancy-law proof, whole-trajectory pushforward, uniform CE/OC bounds, pathwise arbitrary-positive-stopping bound, first-step all-score sign, finite-dimensional risk-oracle argument, and common-regime calculations. Independent exact rational arithmetic reproduces the Taylor remainder `89/9216`, risk gap `121/20,000,000`, and strict calibration-constant lower bound `441/260,000,000`. No mathematical blocker or hidden quantifier broadening was found. The acceptance is based on the arguments, not a count of agents or votes. The Gaussian source is pinned for attribution and scope; no Gaussian result is a premise of the categorical acceptance.

**Accepted original-row description:** “T357 is completed in the original row's explicitly permitted categorical random-feature regime: calibration is characterized as a function of proportional sample ratio, width and discrete GD time; an informative overparameterized regime is overconfident at every nonneutral first-step score while improving risk; and every useful finite positive stopping rule remains miscalibrated.” The categorical/axis-aligned geometry, frozen first layer and summed-loss step scaling are part of that statement. “The Gaussian multistep problem is solved” and “generic trained neural networks are covered” are not accepted descriptions.

No frozen campaign artifact or registry was changed by this report. Final package validation and preservation in both repositories remain the coordinator's separate obligations; this report does not certify their completion.
