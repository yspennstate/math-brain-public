# T357 extension: full-ratio frontier and a uniform large-norm obstruction

24 October 2026. B06 independent scope, source, and mathematical investigation. This is new work; no accepted proof under `fullproof/` is modified. The current finite-time/regime theorem is not relabeled as a complete all-regime resolution.

## 1. Strongest precise next target

Keep the actual model fixed: Gaussian inputs, independent Gaussian tanh features with \(m/d\to\gamma>0\), logistic single-index teacher of fixed finite strength \(\beta\), and the exact reused-sample full-batch output-weight GD recursion from zero with the stated normalization. The next complete target is a dimension-uniform description, for **every** fixed positive \((\alpha,\gamma)\), of exact model-conditional calibration along training, including positive data-dependent times that may grow with dimension and the appropriate terminal behavior in both nonseparable and separable phases. At a phase boundary, a meaningful statement must specify the limit order or any dimension-dependent critical scaling; an assumed exchange of \(d\to\infty\) and \(t\to\infty\) is not a theorem.

For a stable-step version, the allowed step condition must be a single explicit spectral/stability condition valid across the model, not chosen after seeing which times are easy to prove. Asking for every positive fixed step is a distinct stronger problem because nonseparable convex logistic GD can fail to converge for excessively large steps. Training the hidden features is another distinct extension requiring its own width, initialization, and time normalization. It must not be silently conflated with the original random-feature branch.

The frozen theorem covers every fixed time at all positive finite aspect ratios, plus all times in one explicit large-sample regime. The result below treats **all coefficient vectors of sufficiently large norm**, without delocalization, and therefore applies across aspect ratios. It does not yet control every moderate-norm trajectory at arbitrarily late times.

## 2. Uniform large-norm calibration and population-risk theorem

Let \(X\sim N(0,I_d)\), \(Z=\theta^\top X\), \(\|\theta\|=1\), and
\[
p(Z)=\mathbb P(Y=1\mid X)=\sigma(\beta Z),\qquad 0\le\beta<\infty.
\]
Fix any feature matrix \(F\in\mathbb R^{m\times d}\), set \(h(X)=\tanh(FX)\), and assume
\[
\|F\|_{\rm op}\le L,\qquad
\Sigma_F:=\mathbb E[h(X)h(X)^\top]\succeq sI_m
\tag{1}
\]
for fixed \(s,L>0\). For arbitrary \(b\in\mathbb R^m\), let \(S_b=b^\top h(X)\) and
\[
\operatorname{CE}_F(b)
=\mathbb E\left|\mathbb E[p(Z)\mid S_b]-\sigma(S_b)\right|,
\quad
\mathcal R_F(b)
=\mathbb E[\log(1+e^{S_b})-p(Z)S_b].
\tag{2}
\]
These are the exact unbinned calibration error and population cross-entropy conditional on the fixed feature matrix and any training environment that selected \(b\).

Define
\[
\kappa=\sqrt{s/2},\qquad
p_0=\frac{s^2}{20L^4},\qquad
B=\sqrt{2\log(4/p_0)},\qquad
q=\sigma(-\beta B),
\tag{3}
\]
\[
C=\log\frac4{q p_0},\qquad
R=\frac C\kappa,\qquad
\varepsilon=\frac{q p_0}4,\qquad
\rho=\frac{q\kappa p_0}2.
\tag{4}
\]
The assumptions imply \(s\le L^2\), so \(0<p_0\le1/20\) and these constants are well defined and positive.

**Theorem 1.** Under (1), simultaneously for every \(b\in\mathbb R^m\),
\[
\|b\|\ge R\quad\Longrightarrow\quad
\operatorname{CE}_F(b)\ge\varepsilon,
\tag{5}
\]
and
\[
\mathcal R_F(b)\ge\rho\|b\|.
\tag{6}
\]
No training algorithm, coefficient delocalization, coefficient/feature independence, or max-margin convergence is assumed.

### Proof: a uniform small-ball estimate

For a unit vector \(u\), \(f_u(X)=u^\top\tanh(FX)\) is odd and \(L\)-Lipschitz. Thus it has mean zero. Gaussian Poincare gives
\[
s\le\mathbb E f_u^2\le L^2,\qquad
\mathbb E f_u^4
\le(\mathbb E f_u^2)^2+4L^2\mathbb E f_u^2
\le5L^4.
\tag{7}
\]
Apply Paley--Zygmund to \(f_u^2\) at half its expectation. Since \(s/2\le\mathbb E f_u^2/2\),
\[
\mathbb P(|f_u|\ge\kappa)\ge
\frac{(\mathbb E f_u^2)^2}{4\mathbb E f_u^4}
\ge p_0.
\tag{8}
\]
This deterministic conclusion holds for every \(u\); it is not a union bound over coefficient vectors. Consequently
\[
\mathbb P(|S_b|\ge\kappa\|b\|)\ge p_0
\quad(b\ne0).
\tag{9}
\]
Also the Gaussian tail bound and (3) give
\[
\mathbb P(|Z|>B)\le2e^{-B^2/2}=p_0/2.
\tag{10}
\]
No independence between \(S_b\) and \(Z\) is asserted.

### Proof: a score-measurable signed witness

The exact calibration error is the variation norm of the signed measure on score space whose density relative to the score marginal is
\(\sigma(S_b)-\mathbb E[p(Z)\mid S_b]\). Therefore for every measurable \(|w|\le1\),
\[
\operatorname{CE}_F(b)
\ge\mathbb E[(\sigma(S_b)-p(Z))w(S_b)].
\tag{11}
\]
If \(\|b\|\ge R\), set
\[
E_b=\{|S_b|\ge C\},\qquad
w(x)=\operatorname{sign}(x)\mathbf1_{\{|x|\ge C\}}.
\tag{12}
\]
The witness depends only on the score, which is essential for (11). Equations (9)--(10) imply
\[
\mathbb P(E_b)\ge p_0,\qquad
\mathbb P(E_b\cap\{|Z|\le B\})\ge p_0/2.
\]
On \(E_b\), the signed residual is confidence minus the conditional probability that the predicted class is correct:
\[
(\sigma(S_b)-p(Z))\operatorname{sign}S_b
=\sigma(|S_b|)-p_{\rm correct}(Z,S_b).
\]
Always \(p_{\rm correct}\le1\); on \(|Z|\le B\), one has \(p_{\rm correct}\le1-q\). Since \(\sigma(|S_b|)\ge1-e^{-C}\),
\[
\begin{aligned}
\mathbb E[(\sigma(S_b)-p(Z))w(S_b)]
&\ge q\,\mathbb P(E_b,|Z|\le B)-e^{-C}\mathbb P(E_b)\\
&\ge q p_0/2-e^{-C}
=q p_0/4.
\end{aligned}
\tag{13}
\]
This proves (5). It is an overconfidence witness on a high-confidence subset, not a claim that the unconditional average signed error or every confidence level is positive.

### Proof: population risk is uniformly coercive

For every real score \(z\) and Bernoulli mean \(p\),
\[
\log(1+e^z)-pz\ge \min(p,1-p)|z|.
\tag{14}
\]
For \(z\ge0\), use \(\log(1+e^z)\ge z\); for \(z<0\), use \(\log(1+e^z)\ge0\). On \(|Z|\le B\), \(\min(p(Z),1-p(Z))\ge q\). The event \(\{|S_b|\ge\kappa\|b\|,\ |Z|\le B\}\) has probability at least \(p_0/2\) by (9)--(10). Thus
\[
\mathcal R_F(b)\ge
q\kappa\|b\|\cdot p_0/2=\rho\|b\|.
\]
The case \(b=0\) is immediate. This completes both statements. \(\square\)

## 3. Consequences for the actual proportional random-feature model

For \(F\) with independent \(N(0,I_d/d)\) rows and \(m/d\to\gamma>0\), the covariance proof already supplied in the accepted Gaussian modules gives, with probability tending to one,
\[
\|F\|_{\rm op}\le 8\sqrt{1+\gamma},\qquad
\Sigma_F\succeq(\nu/2)I_m,
\quad
\nu=\mathbb E\tanh^2G-(\mathbb E[G\tanh G])^2>0.
\tag{15}
\]
Thus use \(L=8\sqrt{1+\gamma}\), \(s=\nu/2\) in Theorem 1. The probability event depends only on features. On that **single** event, the conclusions hold for all coefficients at once, including every GD iterate, every training-dependent stopping rule, and coefficients localized on a few features.

In particular, for any data-dependent sequence \(b_d\) such that \(\|b_d\|\to\infty\) in probability,
\[
\mathcal R_{F_d}(b_d)\xrightarrow{P}\infty,\qquad
\mathbb P\{\operatorname{CE}_{F_d}(b_d)\ge\varepsilon\}\longrightarrow1.
\tag{16}
\]
This is a simultaneous dimension/training-time statement whenever the norm-divergence premise is proved for the chosen times. It does not use an iterated fixed-dimension max-margin limit to manufacture that premise.

The lemma can be spliced with a uniform optimization-time argument. If a data event gives, for a deterministic finite \(T\), \(\inf_{t\ge T}\|b^t\|\ge R\), then (5) controls the entire late-time tail. The existing finite-time theorem gives a positive exact-calibration limit at each of \(1,\ldots,T-1\), so a finite union gives a positive calibration floor for the whole positive-time trajectory. B02 is investigating this splice in the sufficiently wide-feature regime. An independent check of its constants and hypotheses will be appended below.

## 4. Limits and next mathematical obligation

Theorem 1 does not prove that every nonzero norm has a positive uniform calibration floor. In particular, its high-confidence witness is only effective once \(\|b\|\ge R\). Closing the remaining moderate-norm window at arbitrary growing training times would need either a uniform dynamical compactness/delocalization argument or a theorem for arbitrary localized readouts.

A possible localized-limit analysis splits a bounded coefficient sequence into its largest finitely many coordinates and a diffuse remainder. The diffuse remainder has small Hessian and a Gaussian approximation jointly with the teacher and those finitely many feature coordinates. The heavy part remains nonlinear and must not be replaced by Gaussian noise. Correlations between the diffuse Gaussian component and the heavy feature coordinates can survive, even though pairwise feature directions are nearly orthogonal: the readout is data dependent. Thus an eventual limit can involve terms of the form \(b_j\tanh G_j+\rho_jG_j\), not merely an independent logistic-normal smoothing. The accepted scalar single-crossing proof does not cover this larger family. No all-coefficient moderate-norm impossibility theorem is claimed here.

## 5. Source investigation and audit log

This section is in progress. All literature statements below will be separated from the independent theorem above. Theorem 1 is not assigned a publication-novelty claim merely because its short proof has been derived here.
