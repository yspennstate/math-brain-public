# All positive stopping times in strongly overparameterized Gaussian tanh RF GD

Author: B02. Date: 2026-10-24. New extension; the frozen `fullproof/` files are unchanged.

**Status.** The theorem below proves a uniform positive exact-calibration floor at every positive integer GD time, including arbitrary dimension-dependent, data-dependent stopping times, in an explicit strongly overparameterized proportional regime. The late-time proof does not assume relative coefficient delocalization, a uniform-time Gaussian score approximation, or a dimension-fixed convergence rate. It combines a dimension-uniform optimization bound with the large-norm calibration witness developed by B06 and independently checked by B04. The complete witness argument is reproduced here.

The same argument proves that population cross-entropy diverges uniformly at late times while empirical cross-entropy vanishes. Consequently the population-risk optimum over the entire discrete GD path lies in a deterministic finite window, and the existing finite-time recursion determines that optimum. Section 9 states the abstract positive-margin criterion that can extend this result beyond the explicit row-Gram regime; no unverified phase-universality assertion is used here.

## 1. Model and explicit nonempty regime

Use the exact original Gaussian tanh model:
\[
X_i\sim N(0,I_d),\quad W_j\sim N(0,I_d/d),\quad
Y_i\mid X_i\sim\operatorname{Bernoulli}(\sigma(\beta\theta^\top X_i)),
\]
with independent inputs and feature rows, conditionally independent labels, \(\|\theta\|=1\), and fixed finite \(\beta\ge0\). Let
\[
n/d\to\alpha>0,\qquad m/d\to\gamma>0,\quad
h(x)=\tanh(Fx),\quad H_{ij}=h_j(X_i).
\]
Only the output coefficients are trained. Put \(s_i=2Y_i-1\),
\(\ell(z)=\log(1+e^{-z})\), and
\[
\mathcal L_n(b)=\frac1n\sum_i\ell(s_i h_i^\top b),\qquad
b^0=0,\quad b^{t+1}=b^t-\eta_d\nabla\mathcal L_n(b^t),
\quad \eta_d=\frac{cd}{m}.
\tag{1.1}
\]
Thus the actual update coefficient multiplying \(H^\top[Y-\sigma(Hb^t)]\) is \(cd/(nm)\), as in the frozen theorem. The scale \(c>0\) is fixed independently of dimension.

Define
\[
a=\mathbb E[G\tanh G],\quad v=\mathbb E\tanh^2G,\quad
\nu=v-a^2>0,\quad s=\nu/2,\quad \kappa=\sqrt{s/2},
\quad G\sim N(0,1).
\]
For the training-input side, set
\[
L_X=8\sqrt{1+\alpha},\quad p_X=\frac{s^2}{20L_X^4},\quad
C_X=\max\left\{1,\left(\frac{32L_X}{\kappa p_X}\right)^2\right\},
\]
\[
k_0=\frac{\kappa^2p_X}{16},\qquad k_1=64L_X^2.
\tag{1.2}
\]
The explicit assumptions for this module are
\[
\boxed{\qquad\gamma/\alpha>C_X,\qquad 0<c<2\alpha/k_1.\qquad}
\tag{1.3}
\]
For each fixed \(\alpha>0\) and finite \(\beta\), these conditions leave nonempty open intervals of width ratios and learning scales. They imply \(m>n\) for large dimension. Their conservative constants are not claimed to be sharp.

For the fresh-input feature side, define
\[
L_F=8\sqrt{1+\gamma},\quad p_F=\frac{s^2}{20L_F^4},\quad
B_F=\sqrt{2\log(4/p_F)},\quad q_F=\sigma(-\beta B_F)>0,
\]
\[
C_F=\log\frac4{q_Fp_F},\quad
R_F=\frac{C_F}{\kappa},\quad
\varepsilon_F=\frac{q_Fp_F}{4},\quad
a_F=\frac{q_F\kappa p_F}{2}>0.
\tag{1.4}
\]
Finally put
\[
D=2\sqrt{\gamma k_1/\alpha},\qquad
\mathfrak B_t=\frac1{t+1}+\frac{\alpha}{ck_0}\frac{\log^2(t+1)}t
\quad(t\ge1).
\tag{1.5}
\]
These are all deterministic dimension-independent constants or sequences.

## 2. The simultaneous design event, proved for the actual nonlinear features

With probability tending to one, all of the following hold:
\[
\|F\|_{\mathrm{op}}\le L_F,\qquad
\Sigma_F:=\mathbb E_X[h(X)h(X)^\top]\succeq sI_m,
\tag{2.1}
\]
\[
k_0I_n\preceq HH^\top/m\preceq k_1I_n.
\tag{2.2}
\]
We prove these facts rather than inferring them from bounded entries or an uninspected spectral theorem.

### 2.1 Population covariance on either side

Consider a matrix \(V\) with \(r\) independent rows \(N(0,I_d/d)\), where \(r/d\) tends to a fixed positive constant. For an independent \(G\sim N(0,I_d)\), write \(h_V(G)=\tanh(VG)\). If \(q_j=\|V_j\|^2\) and \(A(q)=\mathbb E\tanh'(\sqrt qG_1)\), the Hermite expansion gives
\[
\mathbb E[h_Vh_V^\top]
=D_AVV^\top D_A+D_\nu+E,
\tag{2.3}
\]
where
\[
(D_\nu)_{jj}=\mathbb E\tanh^2(\sqrt{q_j}G_1)-q_jA(q_j)^2,
\quad E_{jj}=0,
\quad |E_{ij}|\le|\rho_{ij}|^3\ (i\ne j).
\]
Here \(\rho_{ij}\) is the inner product of the two normalized rows. The linear Hermite coefficient is identified by Gaussian integration by parts; all remaining degrees are odd and at least three. Cauchy--Schwarz on their coefficients gives the displayed remainder bound, since the second moment of tanh is at most one. Independent Gaussian row directions satisfy
\[
\mathbb E\|E\|_F^2
\le\frac{15r(r-1)}{d(d+2)(d+4)}=O(d^{-1}).
\tag{2.4}
\]
Uniform row-norm concentration makes \(D_\nu\to\nu I\) in operator norm, while (2.4) makes \(\|E\|_{\mathrm{op}}\to0\) in probability. Thus the covariance is at least \(sI\) with probability tending to one. Gaussian sphere nets also give \(\|V\|_{\mathrm{op}}\le8\sqrt{1+r/d+o(1)}\) with exponential probability; the stated constants \(L_F,L_X\) have ample fixed slack. More explicitly, the covariance event can be chosen with failure \(O(d^{-1})+O(de^{-c_0d})\).

Apply this first to \(V=F\), obtaining (2.1). Apply it also to \(V=X/\sqrt d\), obtaining an event \(\mathcal X_d\), measurable in the training inputs alone, on which
\[
\|X\|_{\mathrm{op}}/\sqrt d\le L_X,\qquad
K_X:=\mathbb E_G[\tanh(XG/\sqrt d)\tanh(XG/\sqrt d)^\top]
\succeq sI_n.
\tag{2.5}
\]
This second use is legitimate because the rows \(X_i/\sqrt d\) are iid Gaussian. It does not replace the actual feature matrix by independent entries.

### 2.2 Conditional independent columns and small balls

Condition on \(X\in\mathcal X_d\). The \(m\) columns \(h_j\) of \(H\) are iid centered vectors of the form \(\tanh(XG_j/\sqrt d)\). For every unit \(u\in\mathbb R^n\), \(u^\top h_j\) is a centered \(L_X\)-Lipschitz function of a standard Gaussian vector. Consequently
\[
\mathbb E e^{z u^\top h_j}\le e^{z^2L_X^2/2},\quad
\mathbb E(u^\top h_j)^2\ge s,\quad
\mathbb E(u^\top h_j)^4\le5L_X^4.
\tag{2.6}
\]
The fourth-moment bound follows by Gaussian Poincare applied to the function and its square. Paley--Zygmund then gives
\[
\mathbb P(|u^\top h_j|\ge\kappa\mid X)\ge p_X.
\tag{2.7}
\]

Let \(\psi(z)=0\) for \(|z|\le\kappa/2\), let it rise linearly to one on \(\kappa/2<|z|<\kappa\), and let it equal one for \(|z|\ge\kappa\). It is \(2/\kappa\)-Lipschitz, bounded by one, and vanishes at zero. Symmetrization, Rademacher contraction, and \(\operatorname{tr}K_X\le nL_X^2\) give
\[
\mathbb E\sup_{\|u\|=1}\left|
\frac1m\sum_j\psi(u^\top h_j)-\mathbb E\psi(u^\top h_j)
\right|
\le\frac{8L_X}{\kappa}\sqrt{\frac nm}.
\tag{2.8}
\]
If \(m/n\ge C_X\), this is at most \(p_X/4\). Bounded differences with deviation \(p_X/4\) proves, except with conditional probability \(e^{-mp_X^2/8}\),
\[
\inf_{\|u\|=1}\frac1m\#\{j:|u^\top h_j|>\kappa/2\}\ge p_X/2.
\tag{2.9}
\]
In fact (2.9) is robust: after deleting any subset of at most \(p_Xm/4\) columns, the remaining Gram matrix, still normalized by \(m\), is at least
\(\kappa^2p_XI/16=k_0I\). No independence of the deleted columns or union bound over subsets is needed. In particular it proves the lower half of (2.2).

The same two-sphere-net bound applied to \(H^\top\) gives
\[
\|H\|_{\mathrm{op}}\le8L_X\sqrt m
\tag{2.10}
\]
with conditional failure at most \(2e^{-3m}\) when \(m\ge n\): each fixed bilinear form is centered \(L_X\)-subGaussian, and \(1/4\)-nets have cardinalities at most \(9^m,9^n\). This proves the upper half of (2.2).

Let \(\mathcal G_d\) combine (2.1), (2.5), and (2.2). For large \(d\), (1.3) ensures \(m/n\ge C_X\), and
\[
\mathbb P(\mathcal G_d^c)
\le O(d^{-1})+O(de^{-c_0d})+e^{-mp_X^2/8}+2e^{-3m}=o(1).
\tag{2.11}
\]
No independence between the good feature event and the conditional sample-Gram event is asserted: a union bound suffices. Labels play no role in this design event.

## 3. Uniform empirical loss decay

On \(\mathcal G_d\), the full row rank in (2.2) makes every binary labeling strictly separable. For \(R>0\), the explicit comparator
\[
b_R=H^\top(HH^\top)^{-1}(R s_{1:n})
\tag{3.1}
\]
has every signed training margin equal to \(R\), and
\[
\mathcal L_n(b_R)=\ell(R)\le e^{-R},\qquad
\|b_R\|^2\le\frac{nR^2}{mk_0}.
\tag{3.2}
\]

The empirical Hessian is globally bounded by
\[
\nabla^2\mathcal L_n(b)\preceq\frac{H^\top H}{4n},
\quad\text{so its smoothness constant is at most }\frac{mk_1}{4n}.
\]
For large \(d\), \(n/d\ge\alpha/2\); assumption (1.3) gives
\[
\eta_d\frac{mk_1}{4n}=\frac{cdk_1}{4n}<1.
\tag{3.3}
\]
Hence ordinary GD decreases the empirical loss at every step.

For clarity, the convex smooth-GD comparator inequality used here is
\[
\mathcal L_n(b^t)-\mathcal L_n(u)\le\frac{\|u\|^2}{2\eta_dt}
\quad(t\ge1).
\tag{3.4}
\]
It follows directly by expanding \(\|b^{k+1}-u\|^2\), using convexity, and using descent to replace \(\eta_d^2\|\nabla\mathcal L_n(b^k)\|^2\) by \(2\eta_d[\mathcal L_n(b^k)-\mathcal L_n(b^{k+1})]\). Summing gives the bound on the average of losses at times \(1,\ldots,t\), and monotonicity bounds the final loss by that average. No strong convexity or finite MLE is needed.

Use (3.2) in (3.4), then take \(R=\log(t+1)\). Since \(n/d\le2\alpha\) eventually,
\[
\boxed{\quad
\mathcal L_n(b^t)
\le\frac1{t+1}+\frac{n}{2cdk_0}\frac{\log^2(t+1)}t
\le\mathfrak B_t\qquad\text{for every }t\ge1.
\quad}
\tag{3.5}
\]
This inequality holds simultaneously at all integer times on one event. In particular it applies to times growing arbitrarily quickly with dimension.

## 4. Uniform norm growth and a deterministic crossing time

For any \(b\), Jensen's inequality, monotonicity of \(\ell\), and Cauchy--Schwarz give
\[
\mathcal L_n(b)
\ge\ell\!\left(\frac1n\sum_i s_i h_i^\top b\right)
\ge\ell\!\left(\frac{\|Hb\|}{\sqrt n}\right)
\ge\ell(D\|b\|).
\tag{4.1}
\]
The last inequality uses \(\|H\|^2/m\le k_1\) and
\(m/n\le4\gamma/\alpha\) for large \(d\). Thus (3.5) implies
\[
\boxed{\quad
\|b^t\|\ge\frac1D
\left[-\log(e^{\mathfrak B_t}-1)\right]_+
\quad(t\ge1).\quad}
\tag{4.2}
\]
Its right-hand side grows as \(D^{-1}(\log t-2\log\log t-O(1))\). The path need not have monotone norm; the simultaneous lower bound is what is used.

For any deterministic threshold \(R_*>0\), define the explicit finite integer
\[
T(R_*)=\min\{T\ge2:\mathfrak B_T<\ell(DR_*)\}.
\tag{4.3}
\]
It exists because \(\mathfrak B_T\to0\). At this time the loss is below \(\ell(DR_*)\); monotone empirical loss and (4.1) then give
\[
\|b^t\|>R_*\qquad\text{for every integer }t\ge T(R_*).
\tag{4.4}
\]
The time \(T(R_*)\) depends only on the fixed model parameters and the chosen threshold, never on dimension or the data. This is stronger than taking \(t\to\infty\) separately for each fixed dataset.

## 5. A calibration floor for every sufficiently large readout

This is the B06 large-norm witness, also independently checked by B04. On (2.1), every coefficient vector \(b\), including arbitrary training-dependent vectors, satisfies
\[
\mathbb E_X S_b^2\ge s\|b\|^2,\qquad
\mathbb E_X S_b^4\le5L_F^4\|b\|^4,
\quad S_b=b^\top h(X).
\]
Consequently
\[
\mathbb P_X(|S_b|\ge\kappa\|b\|)\ge p_F
\quad\text{for every }b\ne0.
\tag{5.1}
\]
All constants and inequalities are simultaneous over \(b\). This statement follows from uniform population moment bounds; it does not union-bound over coefficient vectors.

Write \(Z=\theta^\top X\), \(p(Z)=\sigma(\beta Z)\). The choice of \(B_F\) ensures
\(\mathbb P(|Z|>B_F)\le p_F/2\), and on the complementary event either label has probability at least \(q_F\). Define the bounded measurable score witness
\[
f(S)=\operatorname{sign}(S)\mathbf1_{\{|S|\ge C_F\}}.
\]
For every score and teacher coordinate,
\[
[\sigma(S)-p(Z)]f(S)
\ge q_F\mathbf1_{\{|S|\ge C_F,\ |Z|\le B_F\}}
   -e^{-C_F}\mathbf1_{\{|S|\ge C_F\}}.
\tag{5.2}
\]
Indeed, on a positive score the signed difference is at least \(1-p(Z)-e^{-C_F}\), and on a negative score it is at least \(p(Z)-e^{-C_F}\). Outside the bounded-teacher event the remaining lower bound is still \(-e^{-C_F}\).

If \(\|b\|\ge R_F=C_F/\kappa\), (5.1) implies
\(\mathbb P(|S_b|\ge C_F,|Z|\le B_F)\ge p_F/2\). Hence
\[
\mathbb E_X[(\sigma(S_b)-p(Z))f(S_b)]
\ge q_Fp_F/2-e^{-C_F}\ge\varepsilon_F.
\tag{5.3}
\]
By the defining signed-measure characterization of exact calibration error, or just conditional expectation and \(|f|\le1\),
\[
\mathrm{CE}(b)
=\mathbb E_X\left|\mathbb E[p(Z)\mid S_b]-\sigma(S_b)\right|
\ge\left|\mathbb E_X[(\sigma(S_b)-p(Z))f(S_b)]\right|.
\]
Therefore
\[
\boxed{\qquad \inf_{\|b\|\ge R_F}\mathrm{CE}(b)\ge\varepsilon_F>0.\qquad}
\tag{5.4}
\]
This holds on the good feature event for all readouts at once. It does not require their coefficients to be delocalized or their fresh score to be approximately Gaussian. The bounded-teacher and score-tail events may be dependent; only the union bound was used.

## 6. All positive times and arbitrary stopping rules

Set \(T_F=T(R_F)\), a deterministic finite integer. On \(\mathcal G_d\), (4.4) and (5.4) give
\[
\inf_{t\ge T_F}\mathrm{CE}_{t,d}\ge\varepsilon_F.
\tag{6.1}
\]
For the finitely many earlier times, import precisely **Theorem A of the frozen Gaussian synthesis** `fullproof/T357_THEOREM_AND_SYNTHESIS.md`. It applies to every fixed finite horizon, every fixed \(c>0\), and all finite positive \(\alpha,\gamma\). It proves deterministic limits
\[
\mathrm{CE}_{t,d}\xrightarrow{P}C_\beta(A_t,Q_t)>0
\qquad(1\le t<T_F).
\tag{6.2}
\]
The positive-definite residual covariance in that theorem is valid also in the present separable regime. No finite-MLE result is imported.

Define
\[
\varepsilon_{\rm early}
=\frac12\min_{1\le t<T_F}C_\beta(A_t,Q_t)>0,
\qquad
\varepsilon_* =\min\{\varepsilon_F,\varepsilon_{\rm early}\}>0.
\tag{6.3}
\]
The minimum is over a nonempty finite set because \(T_F\ge2\). A finite union bound in (6.2), combined with (2.11) and (6.1), proves the new theorem:
\[
\boxed{\qquad
\mathbb P\!\left\{\inf_{t\in\{1,2,\ldots\}}
\mathrm{CE}_{t,d}\ge\varepsilon_*\right\}\longrightarrow1.
\qquad}
\tag{6.4}
\]

In particular, for **every** sequence of training-measurable stopping rules
\(\tau_d\in\{1,2,\ldots\}\), with no upper bound on their size,
\[
\mathbb P(\mathrm{CE}_{\tau_d,d}\ge\varepsilon_*)\longrightarrow1.
\tag{6.5}
\]
The event in (6.4) is common to all rules; the order of its quantifiers is stronger than proving (6.5) one rule at a time. Extra randomization of the rule does not affect this pathwise implication. Time zero remains the calibrated constant predictor. A finite unregularized MLE does not exist in this separable regime, so no such object is claimed here.

## 7. Population-risk divergence and a finite optimal-stopping window

The same feature event yields a useful stronger conclusion about risk. Conditional on \(X\), logistic cross-entropy is at least
\[
\min\{p(Z),1-p(Z)\}|S_b|.
\]
Use the joint event \(\{|S_b|\ge\kappa\|b\|,|Z|\le B_F\}\), whose probability is at least \(p_F/2\). Uniformly for all coefficients,
\[
\mathcal R_F(b):=\mathbb E[\ell(Y,S_b)\mid F,b]
\ge a_F\|b\|,
\qquad
\mathcal R_F(b)\le\log2+L_F\|b\|.
\tag{7.1}
\]
In the lower bound, \(\ell(Y,S)=\log(1+e^S)-YS\); this is the same loss as \(\ell((2Y-1)S)\) in Section 1. The upper bound follows from \(\ell(Y,S)\le\log2+|S|\) and Gaussian Poincare. If \(b\) is trained on data, both expectations are fresh-test population quantities conditioned on that training environment.

Combining (7.1) and (4.2), on one event of probability tending to one,
\[
\mathcal R_{t,d}\ge\frac{a_F}{D}
\left[-\log(e^{\mathfrak B_t}-1)\right]_+
\quad\text{for every }t\ge1.
\tag{7.2}
\]
This proves uniform late-time divergence: for each fixed \(M>0\), a deterministic finite time exists after which \(\mathcal R_{t,d}>M\) simultaneously for all later times with probability tending to one. For every \(\tau_d\to\infty\) in probability, \(\mathcal R_{\tau_d,d}\to\infty\) in probability. Empirical risk nevertheless tends to zero by (3.5).

In particular, let
\[
R_{\rm risk}=(\log2+1)/a_F,\qquad
T_{\rm risk}=T(R_{\rm risk}).
\tag{7.3}
\]
Then \(\mathcal R_{t,d}>\log2+1\) for all \(t\ge T_{\rm risk}\) on \(\mathcal G_d\), whereas \(\mathcal R_{0,d}=\log2\). Therefore the population-risk optimum over the whole GD path is attained before this fixed time:
\[
\inf_{t\ge0}\mathcal R_{t,d}
=\min_{0\le t<T_{\rm risk}}\mathcal R_{t,d}
\quad\text{with probability tending to one}.
\tag{7.4}
\]
Finite-time risk convergence from the frozen theorem now gives the deterministic characterization
\[
\inf_{t\ge0}\mathcal R_{t,d}
\xrightarrow{P}
\min_{0\le t<T_{\rm risk}}\mathcal R_\beta(A_t,Q_t),
\tag{7.5}
\]
where the time-zero value is \(\log2\). Thus the fixed-time recursion suffices to compute optimal population-risk stopping in this regime: no unproved exchange of infinite time and dimension is used. If the finite limiting minimum has a unique index, a population-risk-minimizing index equals it with probability tending to one. Without uniqueness, the limiting minimizing set remains the correct conclusion.

## 8. Nontrivial learning and the calibration obstruction can coexist

For \(\beta>0\), retain the exact first-step constants
\[
\mu_\beta=\mathbb E[G(\sigma(\beta G)-1/2)]>0,
\quad k=a^2\mu_\beta,
\]
\[
\tau^2=\frac{\mu_\beta^2a^2v}{\gamma}
+\frac{a^4+v^2/\gamma}{4\alpha},\qquad V=k^2+\tau^2.
\tag{8.1}
\]
The limiting first-step score is \(cU\) with \(U=kZ+\tau G\). Its risk \(R(c)\) has
\(R'(0)=-a^2\mu_\beta^2\) and \(R''(c)\le V/4\). Hence
\[
R(c)\le\log2-ca^2\mu_\beta^2+c^2V/8.
\]
Choosing a fixed
\[
0<c<\min\left\{2\alpha/k_1,\ 4a^2\mu_\beta^2/V\right\}
\tag{8.2}
\]
simultaneously satisfies stability and gives
\[
R(c)<\log2-\tfrac12ca^2\mu_\beta^2.
\tag{8.3}
\]
Thus a positive-step predictor improves population risk by a fixed amount, yet every positive stopping time still has the uniform calibration floor (6.4). In particular, a rule allowed to output time zero that achieves a fixed positive risk improvement with probability tending to one must output a positive time with probability tending to one, and therefore cannot attain asymptotic exact calibration. The result is not merely a pathology of steps that never learn.

There is also an explicit common regime with **strict signed overconfidence at the actual risk-optimal first step**. Retain (1.3)'s width condition and choose
\[
0<\beta<\frac{v}{a\sqrt{\gamma k_1}}.
\tag{8.4}
\]
Let \(c_{\rm risk}\) be the unique minimizer of the first-step Gaussian risk. The scalar theorem in the frozen `fullproof/b06_gaussian_overconfidence.md` proves both strict risk improvement and strictly positive average confidence minus accuracy at this scale, and gives
\[
0<c_{\rm risk}<\frac{\beta k}{V}
\le\frac{a^2\alpha\gamma\beta^2}{v^2}
<\frac{\alpha}{k_1}<\frac{2\alpha}{k_1}.
\tag{8.5}
\]
Here \(\mu_\beta\le\beta/4\) and \(V\ge v^2/(4\alpha\gamma)\). Thus choosing the fixed step \(c=c_{\rm risk}\) satisfies the same stability assumption as the entire-trajectory theorem. For this single strongly overparameterized model, the first iterate strictly improves risk and is overconfident on average, while no positive stopping time attains exact asymptotic calibration. As in the scalar theorem, this is an average signed statement, not overconfidence at every score. Condition (8.4) restricts this compatibility corollary only; the calibration floor and population-risk divergence allow every fixed finite \(\beta\).

## 9. Abstract extension to any uniformly positive separability margin

The row-Gram condition is a concrete sufficient certificate, not a logical necessity for the late-time argument. Suppose instead that, with probability tending to one:

1. The fresh-input feature conditions (2.1) hold with common constants.
2. \(\|H\|_{\mathrm{op}}/\sqrt n\le D_0\).
3. A unit vector \(u_d\) has \(\min_i s_i h_i^\top u_d\ge\kappa_{\rm sep}>0\), with a deterministic constant \(\kappa_{\rm sep}\).
4. The GD steps satisfy \(0<\eta_-\le\eta_d\le4/D_0^2\).

The comparator \(b_R=(R/\kappa_{\rm sep})u_d\) and (3.4) give
\[
\mathcal L_n(b^t)
\le\frac1{t+1}+\frac{\log^2(t+1)}{2\eta_-\kappa_{\rm sep}^2t}.
\tag{9.1}
\]
Equation (4.1) holds with \(D_0\) in place of \(D\). The remainder of Sections 4--7 therefore applies verbatim. If the same fixed-time positive calibration theorem is available, all positive stopping times again have a common calibration floor and the population-risk optimum is in a deterministic finite window.

Consequently a separately proved exact-model max-margin limit \(\kappa_d\to\kappa_*>0\) would extend this module to every parameter point covered by that positive-margin theorem. This paragraph is an implication, not an assertion that a particular external universality theorem has already verified the premise for every aspect ratio. At a zero-margin phase boundary, the deterministic crossing time may diverge and this proof does not close the stopping-time quantifier.

## 10. Exact scope, remaining quantifiers, and dependencies

- Equations (6.4)--(6.5) are proved for the actual dense Gaussian tanh RF model under the explicit nonempty strongly overparameterized conditions (1.3). They concern every positive finite integer time, even arbitrarily fast dimension-dependent times, on a common event. They use fixed positive \(c\), finite fixed \(\beta\), and proportional dimensions.
- No finite MLE is claimed in the separable regime. A terminal hard-classifier limit, if desired, needs a separately justified direction-limit theorem; finite stopping-time conclusion (6.5) does not require it.
- The entire late-time calibration proof is independent of relative delocalization and score-Gaussian approximation. The early finite window uses the already proved finite-time theorem, with its exact unbinned conditional calibration conclusion. Large-norm conclusions do not identify a deterministic late-time calibration curve or a max-margin direction.
- The bounds are uniform over readouts on the good feature event and over all GD times on the good design event. Neither the bounded-teacher event nor arbitrary feature deletions are assumed independent of the score or data.
- Intermediate sample-to-width ratios, a zero-margin boundary, and dimension-dependent vanishing steps are not silently included. Section 9 identifies the exact additional positive-margin premise that enlarges the regime.
- The frozen finite-time input is `fullproof/T357_THEOREM_AND_SYNTHESIS.md`, SHA-256 `7b773eba4446340893bd8e67a1397ba06b154bf79b9f89a348e68c1a93282d51`, Theorem A. The scalar constants in (8.1) are its equation (11). The signed-overconfidence compatibility corollary uses `fullproof/b06_gaussian_overconfidence.md`, SHA-256 `b65ea33e7e0208b825f429f5369ac1fbd1e470803848356df749b7208fbcb532`, whose scalar theorem was independently audited in the frozen B02 final review. The B06/B04 large-norm witness and population-risk argument are written in full above; no unpublished assertion from their parallel work is required as a proof premise.

No novelty or original-row universal-regime claim follows solely from this extension. Its new completion is the strongly overparameterized all-positive-stopping-time theorem, together with a rigorous positive-margin route for extending it further.
