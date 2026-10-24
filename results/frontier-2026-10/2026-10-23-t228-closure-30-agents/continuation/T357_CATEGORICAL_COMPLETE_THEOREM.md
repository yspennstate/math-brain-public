# A categorical random-feature theorem for overconfidence, calibration, and stopping

23 October 2026. Integrated derivation by Agent 27 from the pinned categorical notes, with the additional proofs below. Internal mathematical research, not external peer review, formal verification, or a publication-novelty claim. No frozen campaign file is modified.

**Result.** A specified two-layer random-ReLU-feature network trained by actual full-batch cross-entropy gradient descent has an explicit proportional-limit prediction law and calibration curve. For one informative, overparameterized regime, every nonneutral first-step score is overconfident, yet the first step improves population log-loss. Every positive finite stopping rule, including dimension-dependent and data-dependent rules, has calibration error bounded away from zero with probability tending to one. A finite positive population-risk-optimal stopping index exists with probability tending to one and inherits that calibration lower bound.

The input and feature geometry is categorical and axis aligned. The result is a concrete solvable random-feature instance of the original T357 request, not the stronger Gaussian-input/tanh-feature dossier, a generic-network theorem, or a transfer theorem between those models.

## 1. Model, metrics, and exact finite-dimensional dynamics

Fix \(p\in(1/2,1)\), a learning rate \(c>0\), and positive constants \(\alpha,\gamma\). For each dimension \(d\), the input is uniform on

\[
x_{j,+}=\sqrt d\,e_j,\qquad x_{j,-}=-\sqrt d\,e_j,
\qquad 1\le j\le d.
\]

Write the cell type as \(H\in\{+,-\}\), and set \(p_+=p\), \(p_-=1-p\). Labels are conditionally independent Bernoulli variables with success probability \(p_H\). This is an isotropic input distribution, and its teacher is logistic single index:

\[
E[XX^T]=I_d,\qquad
\Pr(Y=1\mid X)=\sigma(b\theta_*^TX),\quad
\theta_*=(1,\ldots,1)/\sqrt d,\quad
b=\log\frac p{1-p}.
\]

Here \(\sigma(z)=(1+e^{-z})^{-1}\). Draw \(m_d\) hidden weights independently and uniformly from \(\{\pm e_j/\sqrt d:1\le j\le d\}\), independently of the \(n_d\) training examples. Freeze those hidden weights. Train the output coefficients of

\[
f_a(x)=\sum_{r=1}^{m_d}a_r[v_r^Tx]_+
\]

from \(a^0=0\), using full-batch gradient descent of step \(c\) on the **summed** empirical logistic loss. For a mean-loss convention the identical algorithm has learning rate \(cn_d\). Neither a constant mean-loss learning rate nor a different feature normalization is implicit here. Assume

\[
\frac{n_d}{2d}\to\alpha,\qquad
\frac{m_d}{2d}\to\gamma.
\]

Thus the original sample and width ratios are \(n_d/d\to2\alpha\) and \(m_d/d\to2\gamma\).

For cell \(u=(j,H)\), let \(M_u\) be its matching hidden-unit count, \(S_u\) its successful training-label count, \(F_u\) its failed-label count, and \(N_u=S_u+F_u\). A hidden ReLU is exactly one on its matching cell and zero elsewhere. Consequently, at every finite \(d\),

\[
z_0(m,n,s)=0,\qquad
z_{t+1}(m,n,s)=z_t(m,n,s)
+cm\{s-n\sigma(z_t(m,n,s))\},
\qquad q_t=\sigma(z_t).
\tag{1}
\]

This follows by summing the identical updates of the \(M_u\) output coefficients. It is the exact GD recurrence, not an MLE or ridge approximation. In particular,

\[
|z_t(m,n,s)|\le ct mn
\tag{2}
\]

for every finite integer \(t\). Mixed-label cells may overshoot; no global stability or convergence assumption is made about them. Cells have decoupled dynamics given their counts, but their finite-dimensional occupancy counts are multinomially dependent.

All population test quantities below are conditional on the trained network, equivalently on its training sample and frozen features. For a fresh test point, define

\[
g_{d,t}(q)=E[p_H\mid q_t=q,\text{training, features}],
\]

\[
\operatorname{CE}_d(t)=E_X|q_t(X)-g_{d,t}(q_t(X))|,
\quad
\operatorname{OC}_d(t)=E_X[(q_t-g_{d,t}(q_t))
\operatorname{sign}(q_t-1/2)],
\tag{3}
\]

with \(\operatorname{sign}(0)=0\). CE is population unbinned absolute calibration error. OC is signed average predicted-class overconfidence. Positive CE alone does not imply positive OC.

The population log-loss and excess Bayes risk are

\[
L_d(t)=E_X[\log(1+e^{z_t(X)})-p_Hz_t(X)],
\qquad R_d(t)=L_d(t)-h(p),
\tag{4}
\]

where \(h(p)=-p\log p-(1-p)\log(1-p)\). At time zero all predictions are \(1/2\), so \(L_d(0)=\log2\) and \(\operatorname{CE}_d(0)=0\) exactly.

## 2. Explicit proportional-limit law and calibration at all times

Let \(P_d\) be the empirical distribution of \((H,M,S,F)\) over the \(2d\) test cells. Define the deterministic limit \(P\) by drawing \(H\) uniformly, and conditionally on \(H\), independently drawing

\[
M\sim\operatorname{Pois}(\gamma),\quad
S\sim\operatorname{Pois}(\alpha p_H),\quad
F\sim\operatorname{Pois}(\alpha(1-p_H)).
\tag{5}
\]

Then

\[
\|P_d-P\|_1\longrightarrow0
\quad\text{in probability},
\tag{6}
\]

where the norm is the sum of absolute count-state mass differences. Equivalently, with \(N=S+F\), the state weights are

\[
w_H(m,n,s)=\frac12e^{-(\alpha+\gamma)}
\frac{\gamma^m}{m!}\frac{\alpha^n}{n!}
\binom ns p_H^s(1-p_H)^{n-s}.
\tag{7}
\]

Apply (1) to these states. This gives the limiting prediction law explicitly for every iteration. For each score atom \(q\), put

\[
\mu_t(q)=\sum_{H,m,n,s:q_t(m,n,s)=q}w_H(m,n,s),
\quad
\nu_t(q)=\sum_{H,m,n,s:q_t(m,n,s)=q}p_Hw_H(m,n,s).
\]

The calibration curve and metrics are

\[
g_t(q)=\frac{\nu_t(q)}{\mu_t(q)}\quad(\mu_t(q)>0),
\qquad
\operatorname{CE}_t=\sum_q|\nu_t(q)-q\mu_t(q)|,
\tag{8}
\]

\[
\operatorname{OC}_t=\sum_q[q\mu_t(q)-\nu_t(q)]
\operatorname{sign}(q-1/2),
\quad
L_t=\sum_{H,m,n,s}w_H(m,n,s)
[\log(1+e^{z_t})-p_Hz_t].
\tag{9}
\]

Equal scores from different count states are combined **before** taking the absolute value in (8). These countable sums and recurrence characterize dependence on \(\alpha,\gamma,c,t,p\); no scalar fixed-point or unknown limiting estimator is left unspecified.

More strongly, the entire countable prediction trajectory \((H,(q_t)_{t\ge0})\), conditional on the finite-dimensional training data and features, converges in total variation to its deterministic limiting law. In particular,

\[
\sup_{t\ge0}|\operatorname{CE}_d(t)-\operatorname{CE}_t|
\le\|P_d-P\|_1\to0,
\qquad
\sup_{t\ge0}|\operatorname{OC}_d(t)-\operatorname{OC}_t|
\le\|P_d-P\|_1\to0
\tag{10}
\]

in probability. For each fixed finite time, \(L_d(t)\to L_t\) in probability. No uniform-in-time risk convergence is asserted.

**Proof.** For one fixed cell, multinomial rare-category counts converge to the independent Poisson variables in (5). Hidden counts are independent of training counts. For any two distinct specified cells of fixed types, the joint multinomial generating functions converge to the product of their Poisson generating functions. Covariances of fixed count-state indicators therefore tend to zero. Averaging over the \(d\) cells of each type proves convergence in probability of every state mass. Furthermore,

\[
P_d(M+N>K)\le\frac{m_d+n_d}{2dK}
\]

deterministically, and the limiting law has the analogous first-moment tail bound. Finite-state truncation proves (6).

At fixed \(c\), the map from a count state to its entire trajectory is the same in every dimension. Total variation contracts under this measurable pushforward. For CE, let

\[
\rho_{d,t}(A)=\sum_s (p_{H(s)}-q_t(s))
\mathbf1_{\{q_t(s)\in A\}}P_d(s).
\]

Its signed-measure norm equals \(\operatorname{CE}_d(t)\). Since \(|p_H-q_t|\le1\), its distance from the limiting signed pushforward is at most \(\|P_d-P\|_1\), simultaneously for every integer \(t\). OC is directly the expectation of the bounded function \((q_t-p_H)\operatorname{sign}(q_t-1/2)\), giving the other inequality in (10).

For risk, (2) bounds loss by \(\log2+ctMN\). Binomial cell-count moments of every fixed order are uniformly bounded, and \(M\) is independent of \(N\). The losses are uniformly integrable at each fixed time, so truncation extends (6) to (9). The unbounded factor \(tMN\) is why (10) is not claimed for risk. Reflection \((H,S,F)\mapsto(-H,F,S)\) also shows \(\mu_t(1-q)=\mu_t(q)\), \(g_t(1-q)=1-g_t(q)\), and \(g_t(1/2)=1/2\). These symmetry statements concern the limiting law; random finite-dimensional neutral cells need not balance exactly. ∎

## 3. A pathwise lower bound excluding all positive finite stopping rules

Choose an integer \(m_0\ge1\) with

\[
q_*:=\sigma(cm_0/2)>p,
\qquad
\kappa:=\alpha e^{-(\alpha+\gamma)}
\frac{\gamma^{m_0}}{m_0!}(q_*-p)>0.
\tag{11}
\]

Such an integer exists for every fixed \(c>0\) and \(p<1\). Define the observed singleton-cell fraction

\[
B_d=\frac1{2d}\#\{u:M_u=m_0,\ N_u=1\}.
\]

For every finite training sample and hidden-feature realization,

\[
\boxed{\quad
\operatorname{CE}_d(t)\ge(q_*-p)B_d
\quad\text{simultaneously for all integers }t\ge1.
\quad}
\tag{12}
\]

Moreover \(B_d\to b:=\alpha e^{-(\alpha+\gamma)}\gamma^{m_0}/m_0!\) in probability. Therefore, for **any** random finite integer \(T_d\ge1\), including a rule depending arbitrarily on the training data, features, dimension, or additional randomness, the following holds. The rule selects one trained network before a fresh test query is drawn; it is not an input-dependent choice of iteration for each test point.

\[
\Pr\{\operatorname{CE}_d(T_d)\ge\kappa/2\}\longrightarrow1.
\tag{13}
\]

The event underlying this assertion works simultaneously for every such rule. Also \(\operatorname{CE}_t\ge\kappa\) at every positive limiting iteration. No positive finite stopping rule achieves vanishing unbinned calibration error at fixed \(c,\alpha,\gamma,p\). If a rule is allowed to return zero, the same pathwise inequality holds on its event \(\{T_d\ge1\}\); time zero remains calibrated but has risk \(\log2\).

**Proof.** On a cell with \(M=m_0,N=S=1\), the first logit is \(cm_0/2\), and every later increment is strictly positive. Its score is at least \(q_*>p\). For the failure cell \(M=m_0,N=1,S=0\), reflection gives a score at most \(1-q_*<1-p\). Every score-conditional teacher mean, at every finite dimension and time, lies in \([1-p,p]\). Consequently

\[
\operatorname{CE}_d(t)
\ge E_X[(q_t-p)_++(1-p-q_t)_+].
\]

Each counted singleton cell contributes at least \(q_*-p\) to this expectation, regardless of its label or type. Equal-score collisions cannot cancel errors outside \([1-p,p]\). This proves (12) simultaneously along the realized trajectory. Count-law convergence gives \(B_d\to b\), hence (13); no exchange of a dimension limit with a random-time limit is needed. ∎

This theorem is stronger than a fixed-time positive-CE statement. It still does not assert that signed average overconfidence is positive at every time: errors inside the teacher range may have either sign.

## 4. Pointwise first-step overconfidence on every nonneutral score

Suppose

\[
c>2\log\frac p{1-p}.
\tag{14}
\]

At the first step, let \(K=S-F\) and \(R=MK\). Then

\[
z_1=cR/2,\qquad q_1=\sigma(cR/2),\qquad R\in\mathbb Z.
\]

Every supported nonneutral positive score satisfies

\[
q\ge\sigma(c/2)>p\ge g_1(q),
\]

and every supported score below \(1/2\) satisfies

\[
q\le1-\sigma(c/2)<1-p\le g_1(q).
\tag{15}
\]

Thus the model is overconfident in its predicted class at **every nonneutral score atom**, not merely on a rare subset. The neutral atom is calibrated in the limiting law. Consequently

\[
\boxed{\quad
\operatorname{CE}_1=\operatorname{OC}_1
\ge[\sigma(c/2)-p](1-e^{-\gamma})[1-A_0(\alpha,p)]>0,
\quad}
\tag{16}
\]

where

\[
A_0(\alpha,p)=e^{-\alpha}
\sum_{j=0}^\infty
\frac{[\alpha^2p(1-p)]^j}{(j!)^2}
=\Pr(K=0\mid H=+).
\]

**Proof.** The integer spacing of \(R\) gives (15), using only the universal bound \(g\in[1-p,p]\). Under (5), \(M\) is independent of \((H,K)\), and \(\Pr(K=0\mid H=+)\) equals its value under the reflected teacher. Thus the nonneutral mass is \((1-e^{-\gamma})(1-A_0)\). It is positive, for example because \(M=N=1\) has positive probability. Symmetry gives \(g_1(1/2)=1/2\). All remaining signed errors have the predicted-class sign, proving (16). ∎

For completeness, the complete first-step calibration curve is also expressible by finite divisor sums. Define

\[
A_k=e^{-\alpha}\sum_{j\ge\max(0,-k)}
\frac{(\alpha p)^{j+k}(\alpha(1-p))^j}{(j+k)!j!},
\qquad u_+(r)=\sum_{m\mid|r|,\ m\ge1}
e^{-\gamma}\frac{\gamma^m}{m!}A_{r/m},
\quad u_-(r)=u_+(-r)
\]

for \(r\ne0\). At \(q_r=\sigma(cr/2)\),

\[
\mu_1(q_r)=\frac{u_+(r)+u_-(r)}2,
\qquad
g_1(q_r)=\frac{p u_+(r)+(1-p)u_-(r)}{u_+(r)+u_-(r)}.
\tag{17}
\]

The neutral mass is \(e^{-\gamma}+(1-e^{-\gamma})A_0\). These expressions specialize (8) and explicitly resolve score collisions.

Condition (14) is a sufficient first-step sign condition, not a claim of pointwise overconfidence at every later time. The same nonneutral inequalities hold at finite dimension, but the finite-dimensional neutral atom can have residual error. Thus \(\operatorname{CE}_d(1)=\operatorname{OC}_d(1)\) is not asserted exactly; their difference tends to zero by (10).

## 5. Risk improvement and finite positive optimal stopping

For general \(p>1/2\), put \(\delta=p-1/2\) and

\[
A=\alpha\gamma\delta^2,\qquad
B=(\gamma^2+\gamma)(\alpha/4+\alpha^2\delta^2).
\]

The logistic loss has second derivative at most \(1/4\). Using \(z_1=cM(S-N/2)\), \(E[M]=\gamma\), \(E[M^2]=\gamma^2+\gamma\), and

\[
E[S-N/2\mid H]=\alpha(p_H-1/2),
\quad E[(S-N/2)^2\mid H]=\alpha/4+\alpha^2\delta^2,
\]

gives

\[
L_1\le\log2-cA+c^2B/8.
\tag{18}
\]

In particular, \(0<c\le4A/B\) guarantees a strict improvement \(L_1\le\log2-cA/2\). This small-step sufficient condition and (14) are different sufficient regimes. The common regime in Section 6 below proves both desirable conclusions together by a sharper risk calculation.

For **every** fixed \(c>0\),

\[
L_t\longrightarrow\infty\quad\text{as }t\to\infty.
\tag{19}
\]

Indeed, on \(M=N=S=1\), of limiting probability \(\alpha\gamma e^{-(\alpha+\gamma)}/2\), the recurrence is

\[
z_{t+1}=z_t+c(1-\sigma(z_t)).
\]

It increases to infinity, since a finite limit would leave a positive increment. Its population loss is at least \((1-p)z_t\). All other losses are nonnegative, proving (19). Each finite \(L_t\) is finite by (2). Thus the limiting integer risk sequence attains its minimum at a finite index, and any strict improvement \(L_1<\log2\) forces every minimizing index to be positive. Such a minimum has calibration error at least \(\kappa\) by (11)–(12).

There is a finite-dimensional counterpart, requiring no uniform-time risk limit. The fraction of cells with \(M=N=1\) converges in probability to \(\alpha\gamma e^{-(\alpha+\gamma)}>0\). When at least one such cell exists, its logit diverges with the sign of its sole training label, and its true noisy label probability is strictly between zero and one. Therefore \(L_d(t)\to\infty\) as \(t\to\infty\). For each such sample the finite risk sequence has a finite minimizing integer. If \(L_1\le\log2-\eta\) for a fixed \(\eta>0\), fixed-time risk convergence gives

\[
\Pr\{L_d(1)\le\log2-\eta/2\}\to1.
\]

Consequently, with probability tending to one, the least population-risk-minimizing index \(T_d^*\) exists, is finite and positive, and satisfies

\[
L_d(T_d^*)\le\log2-\eta/2,
\qquad \operatorname{CE}_d(T_d^*)\ge\kappa/2.
\tag{20}
\]

This is an oracle existence result, not an algorithm for estimating population risk or selecting its minimizer from validation data. No claim that \(T_d^*\) converges to a particular deterministic index is needed. More generally, any finite stopping rule meeting a strict population-risk target below \(\log2\) must choose a positive time on that event and hence obeys the same pathwise calibration obstruction.

## 6. A common informative, overparameterized regime with explicit constants

Take

\[
\boxed{\quad
p=\frac9{10},\qquad c=5,\qquad
\alpha=\frac1{200},\qquad \gamma=\frac3{200}.
\quad}
\tag{21}
\]

The trainable output-parameter/sample ratio tends to \(m_d/n_d=3\); the example is overparameterized by that count. Duplicate one-cell features and sparse occupancy remain substantive features of its geometry.

First, \(e^{5/2}>12>9\), so \(5>2\log9\): (14) holds. To verify the elementary exponential inequality without numerical approximation, the Taylor sum through degree six is

\[
\sum_{k=0}^{6}\frac{(5/2)^k}{k!}
=12+\frac{89}{9216}>12.
\]

Thus every nonneutral first-step score is overconfident. Also

\[
\sigma(5/2)-9/10>12/13-9/10=3/130.
\tag{22}
\]

Second, the same step strictly improves risk. Let \(E_{11}=\{M=N=1\}\) and \(w_{11}=\Pr(E_{11})=\alpha\gamma e^{-(\alpha+\gamma)}\). Conditional on this event, averaging over the teacher type and its training label gives exactly

\[
E[\ell_{p_H}(z_1)-\log2\mid E_{11}]
=\log\cosh(c/4)-c(p-1/2)^2
=\log\cosh(5/4)-4/5.
\tag{23}
\]

For \(x>1\), differentiating \(\log x-2(x-1)/(x+1)\) shows it is strictly increasing from zero, so \(\log2>2/3\). Also \(\log(1+u)<u\) for \(u>0\). Therefore

\[
\log\cosh(5/4)
=5/4-\log2+\log(1+e^{-5/2})
<5/4-2/3+1/12=2/3.
\]

The conditional excess in (23) is strictly less than \(-2/15\). Off \(E_{11}\), the loss has derivative of absolute value at most one, and \(|z_1|\le(c/2)MN\). Since \(E[MN]=\alpha\gamma\),

\[
\begin{aligned}
L_1-\log2
&\le-\frac2{15}w_{11}
+\frac52(\alpha\gamma-w_{11})\\
&=\alpha\gamma\left[-\frac2{15}e^{-1/50}
+\frac52(1-e^{-1/50})\right]\\
&\le-\frac{121}{1500}\alpha\gamma
=-\frac{121}{20{,}000{,}000}<0,
\end{aligned}
\tag{24}
\]

where the final inequality uses \(e^{-1/50}\ge49/50\). Set \(\eta=121/20{,}000{,}000\).

Here \(m_0=1\) is valid in (11), and

\[
\kappa=\alpha\gamma e^{-1/50}
[\sigma(5/2)-9/10]
>\frac{441}{260{,}000{,}000}>0.
\tag{25}
\]

Thus this **single fixed regime** has all of the following properties:

1. An informative single-index teacher, a two-layer random-feature network, and actual full-batch cross-entropy GD with the stated scaling.
2. An explicit proportional-limit prediction law, calibration curve, and risk sequence.
3. First-step predicted-class overconfidence at every nonneutral supported score, with \(\operatorname{CE}_1=\operatorname{OC}_1>0\).
4. A strict first-step population log-loss improvement of at least \(\eta\) in the limit.
5. A calibration floor \(\kappa/2\) with probability tending to one at every arbitrary finite positive stopping rule.
6. A finite positive population-risk-optimal stopping index with probability tending to one, satisfying both the strict risk target and the calibration lower bound in (20).

The displayed lower bounds are small. They establish nonvanishing asymptotic effects and an all-supported-score sign statement, not a claim that this sparse model produces a large calibration defect in most test predictions. Its large neutral mass is explicitly included in the theorem.

## 7. Relation to the original request and precise limitations

The original T357 registry permits a solvable random-feature regime and asks for a comparable overconfidence theorem, calibration dependence on sample ratio, width and GD time, and whether early stopping yields calibration. It does not specify Gaussian input or a particular random-feature distribution. The theorem above gives a concrete answer to those obligations in its stated categorical regime. The pointwise conclusion (15) supplies the overconfidence sign, beyond mere positive absolute calibration error. The data-dependent stopping obstruction and strict risk target prevent a vacuous answer based on the calibrated time-zero predictor.

For comparison, Bai, Mei, Wang and Xiong's primary paper defines the same population unbinned CE and score-conditional calibration sign; its main logistic-MLE theorem is for Gaussian inputs and small positive \(d/n\), with overconfidence at every score above one half. Our result has different geometry and actual discrete GD, and its all-score statement is on its countable prediction support at the first step. It does not inherit their continuum-score assertion or small-\(d/n\) expansion. See [arXiv:2102.07856v2, Section 2.1 and Theorem 1](https://arxiv.org/html/2102.07856v2), directly checked for this comparison.

The accepted scope excludes Gaussian-input/tanh-feature dynamics, overlapping generic random features, feature learning in both layers, universal informative-teacher overconfidence at every time, changing-rate limits \(c_d\), rounded or binned calibration, finite-precision training, quantitative rates in dimension, uniform-time risk convergence, and efficient data-based selection of the risk oracle. No publication novelty or whole-registry administrative status is certified here. The sharper Gaussian dossier remains a separate mathematical task.

## 8. Pinned supporting notes and registry

The proofs above are self-contained. These are the exact prior notes and original statement used; another review's verdict is not a proof premise.

| File | SHA-256 |
|---|---|
| `followup/categorical_rf_calibration.md` | `6c040b97f7d2300109d840a458c80151d59aea4916db987929dac8daf057aa9e` |
| `followup/T357_one_step_calibration_discontinuity.md` | `492e7cfeb4e7e302369fd4109f63efe215ff53b5c2e8b4bf4247c6a4ac735404` |
| `a03/registry422.jsonl` | `c1a7636d5ef95888a26e92b36a017e2a2aae72d7140de9f6d39c695c67d2d3b0` |
| Original T357 JSONL row, excluding terminating newline | `354d0cd4e71345e105368edaeedc7639da543a2cb8e476a6bfaa3df14715b330` |
| `a03/rows_T357_DOSSIER.md` | `4f150d1a55209ed37d8b1c6bca8e6ed85b9b4b50dbac24e616b5126791fb5ff9` |

The entire-trajectory calibration consequence, finite-dimensional arbitrary-stopping bound, first-step all-nonneutral-score sign theorem, common regime (21)–(25), and finite-dimensional population-risk-oracle conclusion are explicitly proved here rather than assumed to be present in the earlier pinned notes.
