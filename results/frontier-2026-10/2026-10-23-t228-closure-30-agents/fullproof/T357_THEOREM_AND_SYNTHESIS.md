# T357: calibration along gradient descent in a Gaussian two-layer network

## What is proved

This is a complete mathematical answer to the **Gaussian random-feature regime** of T357, “Overconfidence of overparameterized classifiers,” in the owner's **TOP200_DL** list. Random features are expressly allowed by the original question. The network uses nonlinear tanh features on Gaussian inputs, a logistic single-index teacher, and ordinary full-batch gradient descent on cross-entropy. It is not the earlier categorical example.

The result has three parts, with different assumptions stated explicitly:

1. For every finite positive sample/input ratio and width/input ratio, and every fixed positive learning scale, a deterministic recursion gives the exact asymptotic calibration and population risk at **every fixed training time**.
2. In an explicit nonempty regime with sufficiently many samples per feature and a sufficiently small fixed positive step, the calibration approximation is **uniform over all positive training times**, including the limiting MLE. No data-dependent positive stopping time achieves exact asymptotic calibration there.
3. At the population-risk-optimal **first-step** learning scale, the classifier improves on the constant predictor and is strictly overconfident on average. Compatibility with part 2 is not automatic; the explicit weak-teacher corollary below proves a nonempty common regime where all conclusions hold for the same fixed step.

The proofs and their independent mathematical audits are included in the accompanying package. This is an internally checked theorem, not a claim of external peer review, formal proof-assistant verification, or certified publication novelty. The list's original open-status flag was unverified. Prior random-feature calibration results already exist; the precise source comparison is in `T357_PRIMARY_SOURCE_COMPARISON.md`.

## 1. Model, algorithm, and calibration definition

Let \(d,n,m\to\infty\), with
\[
n/d\to\alpha\in(0,\infty),\qquad m/d\to\gamma\in(0,\infty).
\]
Fix a deterministic unit vector \(\theta_d\), finite \(\beta\ge0\), and independent
\[
X_i\sim N(0,I_d),\qquad W_j\sim N(0,I_d/d),
\qquad Y_i\mid X_i\sim\operatorname{Bernoulli}(\sigma(\beta\theta_d^\top X_i)),
\]
where the labels are conditionally independent and \(\sigma(u)=(1+e^{-u})^{-1}\).
The two-layer score and probability are
\[
S_b(x)=\sum_{j=1}^m b_j\tanh(W_j^\top x),\qquad p_b(x)=\sigma(S_b(x)).
\]
Only the output coefficients are trained. Write \(H_{ij}=\tanh(W_j^\top X_i)\), and define mean cross-entropy
\[
\mathcal L_n(b)=\frac1n\sum_i[\log(1+e^{(Hb)_i})-Y_i(Hb)_i].
\]
For fixed \(c>0\), the **actual algorithm** is
\[
b^0=0,\qquad
b^{t+1}=b^t+\frac{cd}{nm}H^\top[Y-\sigma(Hb^t)]. \tag{1}
\]
This is mean-loss GD with step \(cd/m\) in \(b\), equivalently step \(cd\) in the normalized output coefficients \(w=\sqrt m\,b\). The same sample and feature matrix are reused at every step.

Let \(\mathcal E_d\) contain all training data and features. For a fresh independent input, put \(Z=\theta_d^\top X\) and \(S_{t,d}=S_{b^t}(X)\). Define
\[
A_{t,d}=\mathbb E[ZS_{t,d}\mid\mathcal E_d],\qquad
Q_{t,d}=\mathbb E[S_{t,d}^2\mid\mathcal E_d].
\]
The exact, unbinned, model-conditional calibration error is
\[
\mathrm{CE}_{t,d}=\mathbb E\big[\,|\mathbb E[Y\mid S_{t,d},\mathcal E_d]-\sigma(S_{t,d})|\mid\mathcal E_d\big]. \tag{2}
\]
Conditioning on the score or its sigmoid is equivalent. This is not a fixed-bin estimator or an average of calibration computed under resampled models.

Throughout, \(\|\mu-\nu\|_{\rm TV}=\sup_{|f|\le1}|\int f\,d(\mu-\nu)|\), the full total-variation norm, twice the probability-distance convention.

For a centered Gaussian pair with \(\operatorname{Var}Z=1\), covariance \(A\), and score variance \(Q>A^2\), set
\[
\begin{aligned}
g_{A,Q}(s)&=\mathbb E_V\sigma\left(\beta\left[\frac AQs+\sqrt{1-A^2/Q}\,V\right]\right),\\
C_\beta(A,Q)&=\mathbb E_U\left|g_{A,Q}(\sqrt Q\,U)-\sigma(\sqrt Q\,U)\right|,\\
\mathcal R_\beta(A,Q)&=\mathbb E_U\log\left(2\cosh(\sqrt Q\,U/2)\right)-\mu_\beta A,\\
\mu_\beta&=\mathbb E[U(\sigma(\beta U)-1/2)],
\end{aligned} \tag{3}
\]
where \(U,V\) are independent standard normals.

## 2. Finite-time theorem

**Theorem A.** Under the model above, for every fixed integer \(T\ge1\) and fixed \(c>0\), the explicit recursion in Section 3 defines deterministic \(A_t,Q_t\) and a positive-definite matrix \(\Sigma_T\), with
\[
Q_t-A_t^2=(\Sigma_T)_{tt}>0,\qquad 1\le t\le T.
\]
For each such time,
\[
A_{t,d}\xrightarrow{P}A_t,\quad Q_{t,d}\xrightarrow{P}Q_t,\quad
\left\|\mathcal L((Z,S_{t,d})\mid\mathcal E_d)-
N\left(0,\begin{pmatrix}1&A_t\\A_t&Q_t\end{pmatrix}\right)\right\|_{\rm TV}
\xrightarrow{P}0. \tag{4}
\]
The entire finite test-score path converges conditionally weakly in probability to the Gaussian path in (10) below. In particular,
\[
\mathrm{CE}_{t,d}\xrightarrow{P}C_\beta(A_t,Q_t)>0,\qquad
\mathbb E[\ell(Y,S_{t,d})\mid\mathcal E_d]\xrightarrow{P}\mathcal R_\beta(A_t,Q_t). \tag{5}
\]
The TV and calibration convergences also hold in every finite \(L^p\) over the training environment, since their errors are uniformly bounded. The calibration curves satisfy the stronger integrated statement
\[
\mathbb E\left[\left|\mathbb E[Y\mid S_{t,d},\mathcal E_d]-g_{A_t,Q_t}(S_{t,d})\right|\mid\mathcal E_d\right]\xrightarrow{P}0. \tag{6}
\]
All finite aspect ratios are allowed, including \(m>n\). The theorem fixes time before taking the dimension limit; it alone does not justify a growing-time conclusion.

## 3. Explicit recursion: the dependence on sample ratio, width, and time

Set
\[
a=\mathbb E[U\tanh U],\quad v=\mathbb E[\tanh^2U],\quad
\nu=v-a^2>0,\quad \lambda=c/\alpha,\quad s=a\sqrt\gamma.
\]
There are two scalar probability spaces. On the training-row space, \(Z\sim N(0,1)\) and \(Y\mid Z\sim\operatorname{Bernoulli}(\sigma(\beta Z))\). Gaussian row fields \(G_1,G_2,\ldots\) are independent of \((Z,Y)\). On the column space, standard normal \(H_\star\) is independent of Gaussian column fields. Both Gaussian covariance sequences are constructed below.

Initialize the training residual function \(R_1=Y-1/2\), the column coefficient \(q_0=0\), and empty matrices \(\Psi_0,\Gamma_0,\Sigma_0\). At stage \(t\), the previous row covariance determines the joint law of \((G_1,\ldots,G_{t-1})\) and hence the already defined functions \(R_1,\ldots,R_t\). Compute
\[
\widehat\Delta_t=\alpha(\mathbb E[R_iR_j])_{i,j\le t},\quad
(\widehat\Phi_t)_{ij}=\alpha\mathbb E[\partial_{G_j}R_i]\ (j<i),\quad
\widehat\ell_t=\alpha\mathbb E[ZR_t], \tag{7}
\]
with all other entries of \(\widehat\Phi_t\) zero. Embed the preceding \(\Psi,\Gamma\) in \(t\times t\) matrices with zero last row and column. First calculate
\[
\begin{aligned}
U_t&=(I-a^2\widehat\Phi_t\Psi_t)^{-1},\quad T_t=(I-a^2\Psi_t\widehat\Phi_t)^{-1},\\
\mathsf B_t&=\gamma^{-1}(\nu\widehat\Phi_t+a^2U_t\widehat\Phi_t),\\
\Omega_t&=\gamma^{-1}\left[\nu\widehat\Delta_t+
a^2U_t(\widehat\Delta_t+a^2\widehat\Phi_t\Gamma_t\widehat\Phi_t^\top)U_t^\top\right].
\end{aligned} \tag{8}
\]
The last column of \(\widehat\Phi_t\) is zero, so these expressions use only previous column information. If \(\psi_j\) denotes row \(j\) of \(\Psi\), padded with zeros, complete the current row and coefficient by
\[
\psi_t=\psi_{t-1}+\lambda\left[e_t^\top+\sum_{j<t}(\mathsf B_t)_{tj}\psi_j\right],
\quad q_t=q_{t-1}+\lambda\left[\sum_{j<t}(\mathsf B_t)_{tj}q_j+
\frac{s}{\gamma}\widehat\ell_t\right].
\]
Here \(\psi_0=0\). Put \(q_{1:t}=(q_1,\ldots,q_t)^\top\) and
\[
\begin{aligned}
\Gamma_t&=\Psi_t\Omega_t\Psi_t^\top+q_{1:t}q_{1:t}^\top,\\
\mathsf A_t&=\nu\Psi_t+a^2T_t\Psi_t,\\
\Sigma_t&=\nu\Gamma_t+a^2T_t
(\Gamma_t+a^2\Psi_t\widehat\Delta_t\Psi_t^\top)T_t^\top,
\end{aligned} \tag{9}
\]
where \(T_t\) is now evaluated with the completed \(\Psi_t\). Its inverses exist without a small-step assumption: the products with \(\widehat\Phi_t\) are strictly lower triangular, so their inverses are finite geometric polynomials.

Let \(G_{1:t}\sim N(0,\Sigma_t)\), consistently with previous stages and independently of \((Z,Y)\), and set
\[
S_t^{\rm train}=G_t+\sum_{j\le t}(\mathsf A_t)_{tj}R_j+s q_tZ,
\qquad R_{t+1}=Y-\sigma(S_t^{\rm train}).
\]
Derivatives required in (7) are computed recursively, with deterministic coefficients held fixed:
\[
\partial_{G_j}R_{t+1}=-\sigma'(S_t^{\rm train})
\left[\mathbf1_{j=t}+\sum_{k\le t}(\mathsf A_t)_{tk}\partial_{G_j}R_k\right].
\]
This finishes one causal stage. Only finite matrices and Gaussian expectations occur. The fresh-test law and required overlaps are
\[
S_t^{\rm test}=s q_tZ+G_t,
\quad A_t=s q_t,
\quad Q_t=s^2q_t^2+(\Sigma_t)_{tt}. \tag{10}
\]
Thus (3), (7)–(10) explicitly characterize calibration and risk as functions of \(\alpha,\gamma,\beta,c,t\).

As an exact normalization check, at the first update
\[
A_1=ca^2\mu_\beta,\qquad
Q_1-A_1^2=c^2\tau^2,\quad
\tau^2=\frac{\mu_\beta^2a^2v}{\gamma}+
\frac{a^4+v^2/\gamma}{4\alpha}. \tag{11}
\]
This agrees with the independently proved one-step result. The two variance terms both matter.

## 4. Uniform training-time and early-stopping theorem

We give explicit sufficient constants, without claiming they are sharp. Let
\[
L=8\sqrt{1+\gamma},\quad s_0=\nu/2,\quad k_0=\sqrt{s_0/2},\quad
p_0=s_0^2/(20L^4),
\]
\[
B_0=\sqrt{2\log(4/p_0)},\quad p_1=\sigma(-\beta B_0)p_0/2,\quad
\mathfrak a=k_0p_1/4,
\quad C_* = \max\{1,(32L/(k_0p_1))^2\},\quad \Lambda=16L^2.
\]
Assume additionally
\[
\alpha/\gamma>C_*,\qquad 0<c<\gamma/(2\Lambda). \tag{12}
\]
These are finite constants for every fixed finite \(\beta\) and \(\gamma>0\), so the regime is nonempty. It has more samples than trained output coefficients.

**Theorem B.** Under (12), with probability tending to one, the empirical logistic loss has a unique finite MLE \(b^*\), and GD converges to it geometrically with a dimension-independent contraction factor. Use \(t=\infty\) for this MLE. The deterministic trajectory from Section 3 has limits \(A_\infty,Q_\infty\), and
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
\{|A_{t,d}-A_t|+|Q_{t,d}-Q_t|\}\xrightarrow{P}0,
\]
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
|\mathrm{CE}_{t,d}-C_\beta(A_t,Q_t)|\xrightarrow{P}0. \tag{13}
\]
There is a deterministic \(\varepsilon_*>0\), depending only on the fixed parameters, such that
\[
\mathbb P\left\{\inf_{t\in\{1,2,\ldots,\infty\}}\mathrm{CE}_{t,d}\ge\varepsilon_*/2\right\}\longrightarrow1. \tag{14}
\]
Consequently no training-measurable stopping rule with a positive integer value, or the value \(\infty\), attains asymptotic calibration in this regime. A stopping rule may grow arbitrarily with dimension. If it diverges in probability, its calibration tends to \(C_\beta(A_\infty,Q_\infty)>0\). This conclusion keeps \(c\) fixed and positive; it does not cover dimension-dependent vanishing steps or all late-time overparameterized regimes.

At time zero, the constant prediction \(1/2\) is calibrated by teacher symmetry. Equation (14) concerns positive training times and nontrivial learning. It does not confuse calibration with Bayes accuracy.

## 5. Strict overconfidence with an improved predictor

**Theorem C.** Let \(\beta>0\) and any fixed \(\alpha,\gamma>0\). Put \(k=a^2\mu_\beta>0\), let \(\tau>0\) be given by (11), and set \(U=kZ+\tau G\) with independent standard normals. Define \(g(u)=\mathbb E[\sigma(\beta Z)\mid U=u]\) and
\[
R(c)=\mathbb E[\log(1+e^{cU})-cU g(U)].
\]
There is a unique population-risk-optimal first-step scale \(c_*>0\). For GD (1) run with this fixed scale, its first-step population risk and signed overconfidence satisfy
\[
\mathcal R_{1,d}\xrightarrow{P}R(c_*)<\log2,
\]
\[
\mathrm{OC}_{1,d}:=
\mathbb E[(\sigma(S_{1,d})-\sigma(\beta Z))\operatorname{sign}(S_{1,d})\mid\mathcal E_d]
\xrightarrow{P}\mathrm{OC}_*>0. \tag{15}
\]
The signed quantity is **average predicted confidence minus classification accuracy**. It does not assert pointwise overconfidence at every score. In fact the optimal-scale Gaussian predictor is overconfident close to its decision boundary and underconfident in the far tails.

This theorem uses Theorem A with \(c=c_*\). The scale need not automatically lie in (12); the following corollary gives explicit sufficient conditions for that compatibility. Optimizing first-step risk is not asserted to optimize over the entire GD path.

**Corollary: one fixed model can satisfy all three conclusions.** The regimes are not disjoint. Retain \(L,k_0,p_0,B_0\) above, and choose
\[
\alpha/\gamma>C_0:=\max\{1,(256L/(k_0p_0))^2\},\qquad
0<\beta<\min\{\log(3)/B_0,\ v/(8aL\sqrt\alpha)\}.
\tag{16}
\]
Then \(\sigma(-\beta B_0)>1/4\), so \(C_*(\beta)\le C_0\). Further,
\[
c_*<\frac{\beta k}{k^2+\tau^2}
\le\frac{a^2\alpha\gamma\beta^2}{v^2}
<\frac{\gamma}{64L^2}<\frac{\gamma}{2\Lambda}.
\]
Here \(\mu_\beta\le\beta/4\) and \(\tau^2\ge v^2/(4\alpha\gamma)\). Thus the **same** fixed-step network, with \(c=c_*\), has the complete deterministic training-time calibration curve, an improved and strictly overconfident first iterate, and the uniform positive calibration floor for every positive stopping time. Equation (16) is an explicit nonempty open regime with a weak but nonzero teacher. It does not impose this restriction on Theorem A or on Theorem C separately.

## 6. Proof of the combined theorem

The complete detailed arguments are reproduced in the appended proof modules of `T357_GAUSSIAN_COMPLETE_PROOF.md`. The following establishes their logical composition and identifies every imported mathematical theorem.

**Step 1: actual random-feature matrix and independent teacher signal.** Rotate \(\theta=e_1\), and write input and feature vectors as their first coordinate plus perpendicular coordinates. Taylor expansion of tanh gives, for training rows and a proportional independent test block together,
\[
H/\sqrt m=A_0+(a\sqrt\gamma/m)zh^\top+E_d,
\qquad \|E_d\|_{\rm op}\xrightarrow{P}0.
\]
The perpendicular matrix \(A_0\) is independent of \(z,h\), labels, and the training/test mask. The error follows from Gaussian sup-norm bounds, a centered derivative-feature matrix bound, and a Frobenius bound on the Taylor remainder; no entrywise-to-operator inference is omitted.

**Step 2: the universality hypotheses are proved for this matrix.** Clip each underlying Gaussian matrix in operator norm and then clip the normalized feature matrix. These Frobenius-nonexpansive projections preserve signed-permutation symmetry and make each fixed matrix-power entry globally \(O(d^{-1/2})\)-Lipschitz in all Gaussian entries. Gaussian concentration gives summable failure bounds for every fixed power: off-diagonal entries vanish at the required rate, and diagonal entries approach their normalized trace uniformly. The clipped and original matrices agree eventually almost surely. Conditional Hermite covariance analysis and the Louart–Liao–Couillet spectral theorem identify the limiting singular law with the biorthogonally invariant Gaussian comparison matrix. These facts verify Wang–Zhong–Fan Proposition D.1(b2), including more than just an empirical spectral distribution.

The row-normalized rectangular cumulants are
\[
\kappa_2=v,\qquad \kappa_{2j}=a^{2j}\delta^{j-1}\quad(j\ge2),
\]
where \(\delta\) is the total training-plus-query row ratio before the query block is eliminated. Substitution into Fan's rectangular covariance and memory formulas sums finite triangular series. After conditioning on training rows, every \(\delta\) cancels exactly, yielding (8)–(9).

**Step 3: ordinary GD is represented causally.** Write \(w^t=\sqrt m\,b^t\) for the normalized coefficient vector. Introduce auxiliary column fields by subtracting the deterministic memory terms \(\mathsf B\) from \(A_0^\top\mathbf R_t\), and row fields by subtracting \(\mathsf A\) from \(A_0w^t\), where \(\mathbf R_t\) is the sample residual vector. Define the coordinatewise nonlinearities by adding exactly these terms back. They cancel algebraically in the physical update. Teacher overlaps are first fixed to their deterministic recursive expectations. The resulting history-dependent maps meet the continuity, growth, Lipschitz, and independent-side-information assumptions of Wang–Zhong–Fan Theorem 2.22.

No degeneracy assumption is left open. The residual second-moment matrix begins with \(\Delta_1>0\). From (8)–(9), \(\Omega_t\) dominates a positive multiple of \(\Delta_t\), and \(\Sigma_t\succeq\nu\Gamma_t\). The derivative matrix \(\Psi_t\) has positive diagonal \(\lambda\), so \(\Gamma_t\succ0\). Conditional on the past and a training row, the next sigmoid residual depends strictly on a fresh Gaussian innovation; hence it cannot lie in the linear span of preceding residuals. This proves positive definiteness inductively for every fixed time and every \(c>0\).

The AMP theorem now gives joint empirical state convergence. Its overlap convergence, a normalized Euclidean stability bound, and a finite induction replace frozen teacher overlaps by the actual empirical ones. The same stability argument removes \(E_d\). On query rows all residuals are zero, so the limiting physical score is exactly (10). Conditional laws of large numbers and conditional fourth-moment bounds identify the realized-network covariances. This proves finite-time conditional weak convergence and the deterministic overlaps for the original nonlinear GD, rather than a different AMP training algorithm.

**Step 4: exact calibration requires, and receives, total variation.** A leave-one-feature comparison proves \(\|b^t\|_2=O_P(1)\) and \(\|b^t\|_\infty=O_P(\sqrt{\log d/d})\) at any fixed horizon. Thus the fresh score has bounded gradient and Hessian Hilbert–Schmidt norm, while its Hessian operator norm vanishes. An Ornstein–Uhlenbeck covariance identity proves Gaussian weak approximation with matched covariance. The teacher-orthogonal derivative Gram determinant is concentrated away from zero whenever the residual score variance is positive. Localized inverse-vector fields and Gaussian integration by parts give a dimension-free total-variation smoothing bound. Mollification then upgrades weak convergence to joint TV. This analytic argument is proved directly in the calibration module.

For any joint law \(\mu\) of \((Z,S)\), define the signed measure
\[
\zeta_\mu(B)=\int\mathbf1_{s\in B}[\sigma(\beta z)-\sigma(s)]\,\mu(dz,ds).
\]
Its TV norm equals calibration error. Therefore
\(|C(\mu)-C(\widetilde\mu)|\le\|\mu-\widetilde\mu\|_{\rm TV}\).
The same measure argument controls the integrated conditional regression curve. Logistic loss is at most \(\log2+|S|\), so bounded conditional second moments justify truncation for risk. These observations prove (4)–(6).

Strict positivity in (5) is elementary. For \(A\le0\) or \(\beta=0\), the conditional teacher curve cannot equal a strictly increasing nonconstant sigmoid. For \(A>0,\beta>0\), write it as \(g(s)=\mathbb E\sigma(ks+rG)\) with \(r>0\). Its upper tail satisfies \(e^{ks}(1-g(s))\to e^{r^2/2}\). Equality with \(\sigma(s)\) would first require \(k=1\), then \(r=0\), a contradiction.

**Step 5: all times are controlled on one event.** Under (12), the conditional feature covariance and its teacher-orthogonal residual both dominate \((\nu/2)I\). A bounded-cutoff small-ball argument and the noisy labels yield empirical coercivity uniformly in every coefficient direction. Uniform unsigned small-ball bounds give a sample covariance lower bound even after deleting an arbitrary small fraction of rows. On the bounded initial loss sublevel set, this yields uniform positive logistic Hessian curvature. GD and every feature-deleted GD path stay in that same ball and contract by a common dimension-independent factor \(q<1\).

Feature-deleted minimizers are defined on a fixed compact ball even on exceptional data, preserving independence from the omitted feature. Their missing-coordinate gradients have centered Gaussian concentration. A union bound only through a deterministic \(O(\log d)\) horizon, followed by the common geometric tail, proves
\[
\sup_{t\ge0}\|b^t\|_\infty=O_P(\sqrt{\log d/d}).
\]
The first update makes a nonvanishing loss decrease, so convexity bounds every positive iterate's norm away from zero. This gives uniform lower residual variance and upper score variance. The TV theorem is sequentially uniform on this bounded class. Its calibration functional is continuous and strictly positive on the resulting compact covariance set, proving (14).

Finally, the geometric coefficient tail gives a geometric tail for \(A_{t,d},Q_{t,d}\). Fixed-time deterministic limits from Theorem A are therefore exponentially Cauchy. Splitting a supremum into finitely many times and the common tail proves (13). This supplies the needed exchange of training-time and dimension limits rather than assuming it.

**Step 6: signed overconfidence at the best first-step scale.** For \(U=kZ+\tau G\), Gaussian conditioning gives \(g(u)=\mathbb E\sigma(\lambda_0u+rG)\), where \(\lambda_0=\beta k/(k^2+\tau^2)>0\) and \(r>0\). The scalar module proves that \(\operatorname{logit}g(u)/u\) is strictly increasing on \(u>0\), from \(4g'(0)\) to \(\lambda_0\). Its proof derives a normal variance-mixture representation of logistic noise from its characteristic function, then proves the necessary strict single-crossing property by an explicit kernel-ratio inequality.

The cross-entropy has strictly positive second derivative and a unique minimizer \(c_*\in(4g'(0),\lambda_0)\). The error \(e(u)=\sigma(c_*u)-g(u)\) is positive below one threshold \(u_*\) and negative above it. Risk stationarity gives \(\mathbb E[Ue(U)]=0\). Consequently
\[
\mathrm{OC}_*=2\int_0^\infty e(u)(1-u/u_*)\varphi_{k^2+\tau^2}(u)\,du>0.
\]
Both factors have the same strict sign. Also \(R'(0)<0\), so \(R(c_*)<\log2\). Theorem A's TV and risk convergence transfer both strict conclusions to the actual trained network, proving (15). This completes Theorems A–C.

## 7. Verification and reading map

| Proof component | Full argument | Independent checks |
|---|---|---|
| Actual RF matrix, delocalization, teacher decomposition, universality conditions | `b03_gaussian_dynamics.md` | B05, B06, root |
| Explicit deterministic GD recursion and positive covariances | `b01_GD_state_evolution_check.md` | B03, B04, B05, root |
| Conditional TV and exact calibration transfer | `b04_calibration_transfer.md` | B02, root |
| Uniform-time GD and stopping rules | `b02_uniform_time_GD.md` | B05, root |
| Risk-optimal first-step signed overconfidence and common-regime corollary | `b06_gaussian_overconfidence.md` | B02, B04, root |
| Original scope and literature comparison | `T357_PRIMARY_SOURCE_COMPARISON.md` | B06, root |

The numerical check `check_T357_finite_time.py` independently implements (7)–(10). It compares two parameter regimes, five updates, dimensions 250/500/1000, and twelve independent network realizations at each dimension. Its finite-network \(A,Q\) measurements are the asymptotically equivalent covariance proxies \(a(F^\top b)_1\) and \(a^2\|F^\top b\|^2+\nu\|b\|^2\); the coefficient norm is measured directly. First-step errors relative to the closed formula are below \(6\times10^{-8}\); two independent quadrature scrambles differ by less than \(4\times10^{-7}\) across the recorded moments. At dimension 1000 all fifteen recorded moment comparisons in each regime are within two reported Monte Carlo standard errors. These are normalization checks; none is used as a proof premise.

The original question allows a solvable regime. Theorems A–C provide one, with a full training-time formula and an all-time early-stopping answer where (12) holds. They do not establish every-regime late-time behavior, train both layers, or certify that this theorem was previously unknown. The source comparison records those boundaries explicitly.
