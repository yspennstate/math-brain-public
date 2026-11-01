# A scoped calibration theorem for categorical random ReLU features

Author: A26. Date: 2026-10-23. Status: self-contained supplementary derivation; not independently audited and not a claim of publication novelty or closure of the Gaussian-feature T357 dossier. No frozen campaign artifact is amended by this note.

This model gives a genuine two-layer random-feature network trained by full-batch discrete gradient descent, with an explicit proportional-limit prediction law. Its special geometry makes it a collection of independent histogram cells. The theorem therefore supplies a tractable example, not a transfer theorem for Gaussian inputs or overlapping nonlinear features.

## 1. Exact finite-dimensional model

Let the input take the $2d$ values $x_{j,+}=\sqrt d\,e_j$ and $x_{j,-}=-\sqrt d\,e_j$, uniformly. These inputs are isotropic: $\mathbb E[XX^\top]=I_d$. Fix $p\in[1/2,1)$, write $p_+=p$, $p_-=1-p$, and generate independent labels with

\[
\Pr(Y=1\mid X=x_{j,\epsilon})=p_\epsilon.
\]

For $p>1/2$, this is the single-index teacher

\[
\Pr(Y=1\mid X)=\sigma(b\theta_*^\top X),\qquad
\theta_*=(1,\ldots,1)/\sqrt d,\quad b=\log\frac p{1-p},
\]

with $\|\theta_*\|=1$; $b=0$ gives pure noise. Here $\sigma(z)=(1+e^{-z})^{-1}$.

Draw $m_d$ frozen hidden weights independently and uniformly from $\{\pm e_j/\sqrt d:1\le j\le d\}$. Train only the output weights of

\[
f_a(x)=\sum_{r=1}^{m_d}a_r\,[v_r^\top x]_+.
\]

Use $n_d$ independent training examples, zero initialization, summed logistic cross-entropy, and a fixed step $c>0$:

\[
a^{t+1}=a^t-c\nabla_a\sum_{i=1}^{n_d}
\{\log(1+e^{f_a(X_i)})-Y_i f_a(X_i)\}.
\]

Equivalently, for the mean empirical loss the learning rate is $c n_d$. This scaling is part of the theorem. There is no claim that it is a globally stable learning rate for every occupied cell.

For a cell $u=(j,\epsilon)$, let $M_u$ count its matching hidden units, $N_u$ its training examples, and $S_u$ its positive training labels. A hidden ReLU is exactly one on its matching cell and zero on all other cells. Consequently the cell logit and probability satisfy, **exactly at every finite $d$**,

\[
z_0(M,N,S)=0,\qquad
z_{t+1}=z_t+cM\{S-N\sigma(z_t)\},\qquad q_t=\sigma(z_t). \tag{1}
\]

This is ordinary full-batch GD on output weights, not a fitted estimator substituted for GD. Identical features acquire identical coefficients automatically. For every finite $t$, (1) is well-defined and

\[
|z_t(M,N,S)|\le ctMN. \tag{2}
\]

Large cell counts can cause overshoot. The finite-time results below do not assume monotonicity for mixed-label cells or convergence of the full GD trajectory.

## 2. Proportional-limit law, including conditional calibration

Assume

\[
\frac{n_d}{2d}\longrightarrow\alpha\in(0,\infty),\qquad
\frac{m_d}{2d}\longrightarrow\gamma\in(0,\infty).
\]

Thus the original ratios are $n_d/d\to2\alpha$ and $m_d/d\to2\gamma$. Draw a limiting cell type $H\in\{+,-\}$ with equal probabilities and, independently of the hidden count, draw

\[
M\sim\operatorname{Pois}(\gamma),\quad N\sim\operatorname{Pois}(\alpha),\quad
S\mid(N,H)\sim\operatorname{Bin}(N,p_H). \tag{3}
\]

Apply the fixed map (1). The resulting prediction law is an explicit countable Poisson-binomial mixture. Its weights are

\[
w_H(m,n,s)=\frac12 e^{-(\alpha+\gamma)}
\frac{\gamma^m}{m!}\frac{\alpha^n}{n!}
\binom ns p_H^s(1-p_H)^{n-s}. \tag{4}
\]

**Theorem 1.** For every fixed finite set of iteration indices, the population test laws conditional on the training sample and hidden features converge in probability to the laws (3)–(4). More precisely, the empirical cell law of $(H,M,S,N-S)$ converges in total variation on its countable state space. Hence its pushforward to $(H,q_t)$ also converges in total variation.

For an atom $q$ of the limiting prediction distribution, define

\[
\mu_t(q)=\sum_{H,m,n,s:q_t(m,n,s)=q}w_H(m,n,s),\qquad
\nu_t(q)=\sum_{H,m,n,s:q_t(m,n,s)=q}p_H w_H(m,n,s).
\]

The calibration curve on its support is

\[
g_t(q)=\mathbb E[Y\mid q_t=q]=\frac{\nu_t(q)}{\mu_t(q)},\qquad
\operatorname{CE}_t=\sum_q|\nu_t(q)-q\mu_t(q)|. \tag{5}
\]

Here CE is population $L^1$ calibration error, without binning. Distinct count triples producing the same probability must be combined before taking the absolute value. The finite-dimensional population CE converges in probability to (5).

The population cross-entropy also converges in probability to

\[
L_t=\sum_{H,m,n,s} w_H(m,n,s)
\{\log(1+e^{z_t(m,n,s)})-p_Hz_t(m,n,s)\}. \tag{6}
\]

The excess log-loss over the Bayes predictor is $R_t=L_t-h(p)$, where $h(p)=-p\log p-(1-p)\log(1-p)$.

**Proof.** For one specified cell of type $H$, its success/failure training counts are multinomial with probabilities $p_H/(2d)$ and $(1-p_H)/(2d)$. Their joint law converges to independent Poisson variables with means $\alpha p_H$ and $\alpha(1-p_H)$. The matching hidden count converges independently to $\operatorname{Pois}(\gamma)$. This gives (3).

For two distinct specified cells of prescribed types, the corresponding joint multinomial counts converge to independent copies of these Poisson variables. Thus the covariance of the two bounded count-state indicators tends to zero. Averaging indicators over the $d$ cells of each type proves convergence in probability of each empirical state frequency. For a finite set of count states, sum these errors. Outside that set, use the expected empirical tail mass, which equals the tail probability for one uniformly selected cell and is uniformly small by the bounded first moments of $M+N$. This proves total-variation convergence on the countable space.

The map (1) is the same for every $d$, so pushforward does not increase total variation. This point would require additional care if $c$ varied with $d$: convergence in distribution alone need not preserve conditional calibration. In the present model define the signed measure

\[
\rho_t(A)=\mathbb E[(p_H-q_t)\mathbf1_{\{q_t\in A\}}].
\]

Its total-variation norm is exactly (5). Its dependence on the base cell law is a bounded signed pushforward, so convergence of that law in total variation implies convergence of CE, including at colliding prediction atoms.

Finally, (2) bounds cross-entropy by $\log2+ctMN$. The binomial cell counts have uniformly bounded moments of every fixed order, and hidden counts are independent of training counts. Truncation therefore gives uniform integrability of the test loss; the bounded finite-state convergence extends to (6). A finite union covers any fixed finite set of times. ∎

## 3. Overconfident predictions persist at every positive time

**Theorem 2.** For every $c,\alpha,\gamma>0$, every $p\in[1/2,1)$, and every integer $t\ge1$, the limiting population calibration error is strictly positive. Choose any positive integer $m_0$ such that

\[
\sigma(cm_0/2)>p.
\]

Then the following bound holds simultaneously for all these times:

\[
\operatorname{CE}_t\ge
\alpha e^{-(\alpha+\gamma)}\frac{\gamma^{m_0}}{m_0!}
\big\{\sigma(cm_0/2)-p\big\}>0. \tag{7}
\]

Both score regions $q>p$ and $q<1-p$ have positive probability. They are overconfident for the respective predicted classes. This does **not** claim positive signed average overconfidence, or that typical predictions are overconfident: early underconfidence may dominate, and the bound (7) can be extremely small.

**Proof.** On $M=m_0,N=S=1$, the first logit is $cm_0/2$, and every later increment is $cm_0(1-\sigma(z_t))>0$. Hence $q_t\ge\sigma(cm_0/2)>p$. The probability of this event, averaging over the two cell types, is

\[
\frac12\alpha e^{-(\alpha+\gamma)}\frac{\gamma^{m_0}}{m_0!}.
\]

The mirrored event $M=m_0,N=1,S=0$ has the same probability and prediction $1-q_t<1-p$. Since $g_t(q)\in[1-p,p]$ at every atom, each event contributes at least its probability times $\sigma(cm_0/2)-p$ to CE. Collisions with other count states cannot cancel this error outside ([1-p,p]). Summing the two events proves (7). ∎

For pure noise $p=1/2$, $g_t(q)=1/2$ exactly and

\[
\operatorname{CE}_t=\mathbb E|q_t-1/2|,
\quad
\operatorname{CE}_t\ge\alpha\gamma e^{-(\alpha+\gamma)}
\{\sigma(c/2)-1/2\}.
\]

The constant predictor at time zero is calibrated for both teachers. Pure noise alone provides no useful learning claim because that predictor is already Bayes optimal.

## 4. Informative learning and a nonvacuous early-stopping conclusion

Assume $p>1/2$, and put $\delta=p-1/2$,

\[
A=\alpha\gamma\delta^2>0,\qquad
B=(\gamma^2+\gamma)\left(\frac\alpha4+\alpha^2\delta^2\right)>0.
\]

**Theorem 3.** One GD step satisfies

\[
L_1\le\log2-cA+\frac{c^2B}{8}. \tag{8}
\]

In particular, $0<c\le4A/B$ guarantees

\[
R_1\le R_0-\frac{cA}{2}<R_0,
\qquad R_0=\log2-h(p). \tag{9}
\]

Every positive finite stopping time chosen as a deterministic iteration index still has strictly positive limiting calibration error by (7). Thus time zero is the only exactly calibrated index in the limiting model, and it fails the explicit nontrivial risk target in (9).

For every fixed $c>0$, $L_t\to\infty$ as $t\to\infty$. Therefore, for a step satisfying (9), a risk-minimizing integer iteration exists, is finite and positive, and has nonzero calibration error. This proves a genuine risk/calibration distinction without identifying a ridge parameter with training time.

**Proof.** Logistic cross-entropy as a function of its logit has second derivative at most $1/4$. Consequently

\[
\ell_{p_H}(z)\le\log2+(1/2-p_H)z+z^2/8.
\]

At the first step $z=cM(S-N/2)$. Conditional on $H$,

\[
\mathbb E[S-N/2\mid H]=\alpha(p_H-1/2),\quad
\mathbb E[(S-N/2)^2\mid H]=\alpha/4+\alpha^2\delta^2.
\]

The second identity follows equally from the independent Poisson success/failure counts. Since $\mathbb EM=\gamma$ and $\mathbb EM^2=\gamma^2+\gamma$, taking expectations gives (8) and then (9).

For divergence, use only the fixed event $M=N=S=1$, whose probability is $w=\alpha\gamma e^{-(\alpha+\gamma)}/2>0$. Its logit obeys $z_{t+1}=z_t+c(1-\sigma(z_t))$, so it increases to infinity: a finite limit would leave a strictly positive increment. On this event the true success probability is at most $p<1$, and its population loss is at least $(1-p)z_t$. Thus $L_t\ge w(1-p)z_t\to\infty$. Every finite $L_t$ exists by (2); a sequence tending to infinity attains its minimum at a finite integer. Inequality (9) excludes index zero as a minimizer. ∎

## 5. What this establishes, and what remains outside scope

The theorem provides an explicit prediction law, population calibration curve on its atoms, and risk as functions of sample ratio, width ratio, and actual discrete GD time. It gives positive-time miscalibration, informative risk improvement, and a useful early-stopping distinction for a precisely specified random-feature model.

Its restrictions are substantial: categorical isotropic inputs; axis-aligned one-cell ReLU gates; output-layer training only; a specified objective/stepsize scaling; fixed finite-time asymptotics; and no claim of generic or typical overconfidence for informative teachers. No full trajectory convergence is claimed for mixed-label cells. No Gaussian-equivalence theorem, feature interaction, Gaussian-input result, or efficient tuning theorem follows.

The literal T357 registry permits a solvable random-feature regime, so this is relevant evidence toward one scoped interpretation. The preserved dossier instead selects Gaussian inputs and tanh random features. This note neither replaces that statement nor certifies whole-row closure. Its statistical mechanism is histogram overfitting with random feature coverage; publication novelty has not been established. An independent review of the occupancy, calibration, and risk arguments is required before promoting it to an audited result.

As an algebra check, $\alpha=3,\gamma=2,p=3/4,c=1/10$ gives $A=3/8$, $B=63/8$, $c<4A/B=4/21$, and the exact bound $L_1\le\log2-177/6400$. A standard-library floating-point sum over $0\le M,N\le40$ gave $L_1\approx0.6652569921$, below the analytic upper bound $0.6654909306$; this numerical check is not part of the proof. The same parameters give $m_0=22$ and a very small lower bound in (7), approximately $1.96\cdot10^{-20}$, illustrating why the strict-positive statement must not be described as a large or typical overconfidence effect.
