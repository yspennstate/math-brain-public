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


---

# Complete detailed proof modules

The following modules are reproduced in full. Each module states its own local dependencies; the synthesis above proves their composition and closes the cross-module inputs. Equation numbers restart within each module. Published spectral and AMP theorems are explicitly identified and their application hypotheses are checked.


---

# Appendix A: Random-feature dynamics and matrix hypotheses

Source module: `b03_gaussian_dynamics.md`. SHA-256: `b5992c4a107b715a92fe79413ef79e1acb000afe3300e78c1e0af114340b59c9`.

# T357: Gaussian tanh random features beyond one GD step

Author: B03. Date: 2026-10-24. This file does not modify the frozen followup notes.

**Status.** Theorem 6 assembles a complete arbitrary fixed finite-horizon theorem for the original Gaussian tanh random-feature GD model, using the explicit recursion in B01 and the exact calibration transfer in B04. Sections 1–6 prove the structural lemmas; Section 8 verifies the dynamical-universality matrix hypotheses; Section 9 supplies the exact causal AMP embedding and overlap comparison. The theorem covers every finite positive aspect ratio and every fixed positive step size. It does not claim an arbitrary-ratio infinite-time or unbounded-stopping result. Independent matrix, recursion, and analytic-transfer checks are recorded in the companion files.

## 1. Model and normalization

Use the Gaussian model in `followup/T357_gaussian_first_step_attempt.md`: inputs $X_i\sim N(0,I_d)$, a deterministic unit teacher $\theta$, conditionally independent labels $Y_i\mid X_i\sim\mathrm{Bernoulli}(\sigma(\beta\theta^\top X_i))$, fixed finite $\beta\ge0$, and independent feature rows $W_j\sim N(0,I_d/d)$. Let $n/d\to\alpha>0,m/d\to\gamma>0$, $\phi=\tanh$, $H_{ij}=\phi(W_j^\top X_i)$, and $K=HH^\top/m$.

Write the score as $S_t(x)=(b^t)^\top h(x)$, where $b^t=a^t/\sqrt m$ in the old network convention. Mean-loss GD with output-weight step $cd$ is exactly

\[
b^0=0,\quad u^t=Hb^t,\quad r^t=Y-\sigma(u^t),\quad
b^{t+1}=b^t+\frac{\lambda_d}{m}H^\top r^t,
\qquad\lambda_d=\frac{cd}{n}\longrightarrow\frac c\alpha. \tag{1.1}
\]

Consequently $u^{t+1}=u^t+\lambda_dKr^t$. All statements below allow any fixed $c>0$, except the explicit small-step conclusion in Proposition 3. The horizon $T$ is a fixed integer independent of dimension. No claim concerns $T_d\to\infty$.

Define
\[
a=\mathbb E[G\phi(G)],\quad v=\mathbb E\phi(G)^2,\quad
\nu=v-a^2>0,
\quad A(q)=\mathbb E\phi'(\sqrt qG).
\tag{1.2}
\]
Strict positivity of $\nu$ follows because tanh is not a scalar multiple of its input in Gaussian $L^2$.

## 2. Uniform feature-matrix bounds

Conditional on $F$, whose rows are $W_j^\top$, the rows of $H$ are independent centered random vectors. For any unit $v_0\in\mathbb R^m$, the function $x\mapsto v_0^\top\phi(Fx)$ is $\|F\|_{\rm op}$-Lipschitz and odd. Gaussian concentration therefore gives
\[
\mathbb E[\exp(sv_0^\top h(X))\mid F]
\le \exp(s^2\|F\|_{\rm op}^2/2).
\tag{2.1}
\]
For a unit $u_0\in\mathbb R^n$, conditional independence gives the same bound for $u_0^\top Hv_0$. Taking $1/4$-nets of the two unit spheres and using the standard net inequality proves
\[
\|H\|_{\rm op}=O_P(\sqrt d),\qquad
\|K\|_{\rm op}=O_P(1). \tag{2.2}
\]
The failure probabilities at sufficiently large fixed constants decay exponentially in $d$. The same net argument for the Gaussian matrices proves $\|F\|_{\rm op}=O_P(1)$ and $\|X\|_{\rm op}=O_P(\sqrt d)$, again with exponential tails. Integrating these bounds shows that all fixed moments of the corresponding normalized norms are uniformly bounded.

The elementary proof above does not infer a bounded spectral norm merely from entrywise boundedness.

## 3. Delocalization along every fixed finite GD path

**Theorem 1.** For each fixed $T<\infty$,
\[
\max_{0\le t\le T}\|b^t\|_2=O_P(1),\qquad
\max_{0\le t\le T}\|b^t\|_\infty
=O_P\!\left(\sqrt{\frac{\log d}{d}}\right). \tag{3.1}
\]
The first bound has uniformly bounded fixed moments. The proof uses the same reused training sample at every step.

**Proof.** Since $\|r^t\|_2\le\sqrt n$, (1.1) gives directly
\[
\|b^t\|_2\le \frac{T\lambda_d}{m}\|H\|_{\rm op}\sqrt n=O_P(1). \tag{3.2}
\]

For the coordinate bound, denote feature column $j$ by $h_j$, replace that column by zero, and retain the denominator $m$. Write $K^{-j}=K-h_jh_j^\top/m$, and let $u^{-j,t},r^{-j,t}$ be the corresponding GD scores and residuals. The matrices satisfy $0\preceq K^{-j}\preceq K$.

Conditional on $X,Y,F_{-j}$, the vector $r^{-j,t}$ is independent of $W_j$, bounded in Euclidean norm by $\sqrt n$, and
\[
G\mapsto (r^{-j,t})^\top\phi(XG/\sqrt d)
\]
is odd and $\|X\|_{\rm op}\sqrt{n/d}$-Lipschitz for $G\sim N(0,I_d)$. Its conditional mean is zero. Gaussian concentration followed by a union bound over $j\le m,t<T$, on $\|X\|_{\rm op}\le C\sqrt d$, therefore yields
\[
\max_{j,t<T}|h_j^\top r^{-j,t}|=O_P(\sqrt{d\log d}). \tag{3.3}
\]
The conditioning here is essential: later residuals in the original model are not independent of $W_j$.

Set $e^{j,t}=u^t-u^{-j,t}$. Since sigmoid is $1/4$-Lipschitz,
\[
\|e^{j,t+1}\|_2
\le\left(1+\frac{\lambda_d\|K\|_{\rm op}}4\right)\|e^{j,t}\|_2
+\frac{\lambda_d\|h_j\|_2}{m}|h_j^\top r^{-j,t}|. \tag{3.4}
\]
We have $e^{j,0}=0$ and $\|h_j\|_2\le\sqrt n$. On the simultaneous high-probability bounds (2.2) and (3.3), iteration for fixed $T$ gives
\[
\max_{j,t\le T}\|e^{j,t}\|_2=O_P(\sqrt{\log d}). \tag{3.5}
\]
Thus
\[
|h_j^\top r^t|
\le|h_j^\top r^{-j,t}|+\tfrac14\sqrt n\,\|e^{j,t}\|_2
=O_P(\sqrt{d\log d})
\]
uniformly over the finitely many times and all features. Summing (1.1) over time and dividing by $m$ proves the second assertion in (3.1). ∎

## 4. Joint fresh-test Gaussian approximation for the entire finite path

Let $\mathcal E_d$ contain the features and training sample, and define the exact conditional covariances
\[
A_{t,d}=\mathbb E_X[(\theta^\top X)S_t(X)\mid\mathcal E_d],\qquad
Q_{st,d}=\mathbb E_X[S_s(X)S_t(X)\mid\mathcal E_d]. \tag{4.1}
\]
Write $C_d$ for the covariance matrix of $(\theta^\top X,S_1(X),\ldots,S_T(X))$. All means are zero by oddness.

**Theorem 2.** For fixed $T$, in bounded-Lipschitz distance,
\[
d_{\rm BL}\!\left(
\mathcal L((\theta^\top X,S_1(X),\ldots,S_T(X))\mid\mathcal E_d),
N(0,C_d)\right)\longrightarrow0\quad\text{in probability}. \tag{4.2}
\]
This is a Gaussian approximation whose covariance is allowed to depend on the realized network. It does not assert that $C_d$ has a deterministic limit.

**Proof.** Fix real $u,v_1,\ldots,v_T$, put $b=\sum_tv_tb^t$, and let
\[
f(x)=u\theta^\top x+b^\top\phi(Fx).
\]
Then $\mathbb Ef(X)=0$, and globally
\[
\|\nabla f\|_2\le L:=|u|+\|F\|_{\rm op}\|b\|_2=O_P(1),
\quad
\|\nabla^2 f\|_{\rm op}\le
\varepsilon:=\|\phi''\|_\infty\|F\|_{\rm op}^2\|b\|_\infty=o_P(1).
\tag{4.3}
\]

Here is a self-contained normal-approximation argument. For the Gaussian Ornstein–Uhlenbeck semigroup $P_s$, set
\[
U_f(x)=\int_0^\infty e^{-s}P_s\nabla f(x)\,ds,
\qquad T_f(x)=\nabla f(x)\cdot U_f(x).
\]
Gaussian integration by parts, or integration of $\frac d{ds}P_sf$, gives for smooth bounded $g$
\[
\mathbb E[f(X)g(f(X))]=\mathbb E[T_f(X)g'(f(X))],
\quad\mathbb ET_f=\mathbb Ef^2=:q.
\tag{4.4}
\]
The semigroup derivative identity gives $\|U_f\|_\infty\le L$ and $\|DU_f\|_{\rm op,\infty}\le\varepsilon/2$, whence $\|\nabla T_f\|_2\le3L\varepsilon/2$. Gaussian Poincaré yields
\[
\mathbb E|T_f-q|\le\tfrac32L\varepsilon. \tag{4.5}
\]
For $\psi(t)=\mathbb Ee^{itf(X)}$, (4.4) gives $\psi'(t)=-tq\psi(t)-t\mathbb E[(T_f-q)e^{itf(X)}]$. Solving this scalar differential equation and using $q\ge0$ gives
\[
|\psi(t)-e^{-qt^2/2}|\le\tfrac34t^2L\varepsilon. \tag{4.6}
\]
No lower bound on $q$ is needed.

The conditional covariance matrices are tight because (4.3) and Poincaré bound all diagonal entries. Every subsequence admits a further subsequence on which the bounds in (4.3) hold almost surely and $C_d$ converges along further deterministic realizations in a compact set. Applying (4.6) to a countable dense collection of coefficient vectors, tightness and the characteristic-function criterion identifies every conditional subsequential limit with the corresponding Gaussian covariance limit. This proves (4.2). ∎

The old covariance-operator lemma applies uniformly to these data-dependent weights because their Euclidean norms are tight:
\[
A_{t,d}=a\theta^\top F^\top b^t+o_P(1),
\quad
Q_{st,d}=a^2(F^\top b^s)^\top(F^\top b^t)+\nu(b^s)^\top b^t+o_P(1). \tag{4.7}
\]
Indeed the exact first formula is $A_{t,d}=\theta^\top F^\top D_A b^t$, where $D_A=\operatorname{diag}(A(\|W_j\|^2))$, and $\|D_A-aI\|_{\rm op}\to0$. The exact second formula is $Q_{st,d}=(b^s)^\top\Sigma_Fb^t$.

For any subsequence on which $(A_{t,d},Q_{st,d})$ converges in probability to deterministic limits, Theorem 2 supplies the full joint finite-time Gaussian test-law limit on that subsequence. With fresh labels, apply the common Markov kernel $Y\mid Z\sim\mathrm{Bernoulli}(\sigma(\beta Z))$.

The total-variation and exact-calibration strengthening is proved separately in `fullproof/b04_calibration_transfer.md`; its conditions are furnished by Theorem 1 together with a nonvanishing coefficient norm, for example Proposition 3 below.

## 5. A rigorous nondegeneracy condition

Put $\rho_\beta=\mathbb E\sigma'(\beta G)>0$. This is positive for every fixed finite $\beta$.

**Proposition 3.**
\[
\|b^1\|_2^2\ge\frac{c^2v\rho_\beta}{\alpha\gamma}+o_P(1). \tag{5.1}
\]
If $\lambda_d\|K\|_{\rm op}\le4$, then pathwise
\[
\|b^t\|_2\ge\tfrac12\|b^1\|_2\quad\text{for every integer }t\ge1. \tag{5.2}
\]
In particular a sufficiently small, fixed positive $c$ makes (5.2) hold with probability tending to one. At every fixed positive time in this regime, the teacher-orthogonal fresh-score variance is bounded away from zero in probability.

**Proof.** Conditional on $X,F$, write $R=Y-1/2=\mu+\epsilon$, where $\mu_i=\sigma(\beta Z_i)-1/2$, independent centered $\epsilon_i$ have variance $D_{ii}=\sigma'(\beta Z_i)$, and $D$ is diagonal. Since
\[
\|b^1\|_2^2=\frac{\lambda_d^2}{m}R^\top KR,
\]
expanding the quadratic form and using independence and bounded fourth moments gives
\[
\operatorname{Var}(R^\top KR\mid X,F)
\le C\{\operatorname{tr}(K^2)+\|K\mu\|_2^2\}
\le Cn\|K\|_{\rm op}^2. \tag{5.3}
\]
Thus $\|b^1\|_2^2=\lambda_d^2m^{-1}(\mu^\top K\mu+\operatorname{tr}KD)+o_P(1)$. The first term is nonnegative. Conditional on $F$, the row quantities $D_{ii}K_{ii}$ are iid, bounded, and have mean
\[
\frac1m\sum_j\mathbb E_X[\sigma'(\beta\theta^\top X)\phi(W_j^\top X)^2].
\]
Uniformly over $j$, $\|W_j\|^2\to1$ and $\theta^\top W_j\to0$. Continuity of bounded Gaussian expectations therefore makes this mean tend to $v\rho_\beta$. The conditional LLN proves $n^{-1}\operatorname{tr}KD\to v\rho_\beta$, yielding (5.1).

For (5.2), let $L(b)=\sum_i\ell(Y_i,h_i^\top b)$, $g_0=\nabla L(0)=-H^\top R$, and $\eta=\lambda_d/m$. Its gradient is $\|H\|_{\rm op}^2/4$-Lipschitz. Under the displayed step condition, descent gives $L(b^t)\le L(b^1)\le L(0)-\eta\|g_0\|^2/2$. Convexity gives $L(b^t)\ge L(0)+g_0^\top b^t$. Combining these and Cauchy–Schwarz yields $\|b^t\|\ge\eta\|g_0\|/2=\|b^1\|/2$. Finally, the exact Hermite decomposition implies
\[
Q_{tt,d}-A_{t,d}^2\ge(\nu-o_P(1))\|b^t\|_2^2, \tag{5.4}
\]
uniformly for the fixed-time path. ∎

## 6. Teacher-coordinate removal is operator-small

Rotate coordinates so that $\theta=e_1$. Write $X_i=(z_i,x_i)$ and $W_j=(t_j,f_j)$, with $x_i\in\mathbb R^{d-1}$, $f_j\in\mathbb R^{d-1}$. Let $V$ have rows $f_j^\top$, $U_{ij}=x_i^\top f_j$, $H^0=\phi(U)$. The vectors $z,t$, the noise matrix $H^0$, and label randomness conditional on $z$ have the required independence: $H^0$ is independent of $(z,t,Y)$.

**Proposition 4.** For any fixed proportional number of rows, including training rows together with an additional proportional block of test rows,
\[
\left\|\frac{H-H^0-a zt^\top}{\sqrt m}\right\|_{\rm op}\longrightarrow0
\quad\text{in probability}. \tag{6.1}
\]

**Proof.** Taylor's theorem gives
\[
H-H^0-a zt^\top
=\operatorname{diag}(z)[\phi'(U)-a\mathbf1\mathbf1^\top]\operatorname{diag}(t)+R,
\quad |R_{ij}|\le C z_i^2t_j^2. \tag{6.2}
\]
The remainder satisfies
\[
\|R\|_F^2\le C\Big(\sum_i z_i^4\Big)\Big(\sum_jt_j^4\Big)=O_P(1),
\]
so $\|R\|_{\rm op}/\sqrt m=o_P(1)$.

Conditional on $V$, the centered rows of the derivative matrix $\phi'(U)$ are independent. The same concentration-and-net proof as in Section 2 applies with Lipschitz constant $\|\phi''\|_\infty\|V\|_{\rm op}$; hence the centered matrix has operator norm $O_P(\sqrt d)$. Its row mean minus $a\mathbf1$ is the vector $\delta_j=A(\|f_j\|^2)-a$. Bounded $A'$ and $\mathbb E(\|f_j\|^2-1)^2=O(d^{-1})$ give $\|\delta\|_2=O_P(1)$. Thus
\[
\|\phi'(U)-a\mathbf1\mathbf1^\top\|_{\rm op}=O_P(\sqrt d).
\]
Finally $\|z\|_\infty=O_P(\sqrt{\log d})$ and $\|t\|_\infty=O_P(\sqrt{\log d/d})$, so the first matrix in (6.2), after division by $\sqrt m$, is $O_P(\log d/\sqrt d)=o_P(1)$. ∎

This is an operator-norm statement for the normalized *feature matrix*, not just for its population covariance. If $A,\widetilde A$ have bounded operator norm and $\|A-\widetilde A\|_{\rm op}=o_P(1)$, finite-time logistic GD in the parameter $w=\sqrt m b$, with normalized scores $Aw$, differs by $o_P(\sqrt m)$ in coefficient norm and $o_P(\sqrt n)$ in score norm. To verify, subtract the two recursions, use $1/4$-Lipschitzness of sigmoid, $\|r\|\le\sqrt n$, and $\|w^t\|=O_P(\sqrt m)$, and iterate the resulting linear inequality for fixed $T$.

## 7. Source audit and the route not yet certified here

Primary sources were opened on 2026-10-24. The following notes distinguish inspected theorem assumptions from merely relevant titles.

1. [Gerbelot et al., arXiv:2210.06591v3](https://arxiv.org/html/2210.06591v3), Theorem 2 and assumptions A1–A7: the iterated matrix has iid Gaussian entries; iterate width is finite. Applying this directly with $H=\tanh(XF^\top)$ fails the matrix assumption. Taking all feature coordinates as an index vector instead makes the width extensive. A separate universality reduction is required.
2. [Nishiyama–Imaizumi, arXiv:2602.06320v2](https://arxiv.org/html/2602.06320v2), Assumption 2.1 and Section 2: their model has independent design entries and studies stochastic gradient flow. The paper expressly does not prove exact high-dimensional SGD–SGF equivalence. It cannot itself justify the present discrete RF-GD path.
3. [Fan–Wang, arXiv:2601.21093v3](https://arxiv.org/html/2601.21093v3), revised 21 October 2026: Assumption 2.2(a) keeps the student and teacher index dimensions fixed; Assumption 2.1 uses sublinear minibatches. The extensive random-feature hidden layer and the discrete full-batch trajectory here do not directly satisfy that setup.
4. [Hu–Lu, arXiv:2009.07669v3](https://arxiv.org/pdf/2009.07669): the basic object is the regularized optimizer. Assumption A.5 requires a strongly convex regularizer. Its Gaussian-equivalence theorem is not a finite-time unregularized-GD theorem.
5. [Wang–Zhong–Fan, arXiv:2206.13037v5](https://arxiv.org/html/2206.13037v5), Definition 2.20, Proposition D.1(b), Theorem 2.22 and Lemma D.9: this is the useful prospective route. It requires signed-permutation invariance, the complete limiting diagonal distribution, uniform small offdiagonal entries for generated polynomial matrices, bounded operator norm, independent side information, and regular AMP nonlinearities. Singular state covariances require a justified perturbation argument. The paper's tensor-network result supports polynomial first-order iterations; passing to logistic dynamics must be justified through its AMP embedding/approximation argument rather than asserted from matching spectral laws.
6. [Louart–Liao–Couillet, arXiv:1702.05419v2](https://arxiv.org/pdf/1702.05419), Theorem 2: after conditioning on $V$, take their Gaussian matrix to be the perpendicular data and their bounded deterministic input matrix to be $V^\top$. Tanh is Lipschitz and all three dimensions are proportional. Their spectral deterministic equivalent depends on the feature covariance. Our Hermite operator estimate reduces this covariance to $a^2VV^\top+\nu I$, which is the covariance of $aXV^\top+\sqrt\nu G$. This establishes a spectral candidate; spectral matching alone is insufficient for dynamics.
7. [Gorini et al., arXiv:2604.11729v1](https://arxiv.org/html/2604.11729v1): Section 1.3 explicitly discusses polynomial versus Lipschitz first-order methods. Its general polynomial results do not remove the required logistic approximation step automatically.

The next proof obligations are concrete:

* Prove that $A_0=H^0/\sqrt m$ satisfies Proposition D.1(b)'s simultaneous entrywise bounds for every fixed matrix power. A promising self-contained argument clips the operator norms of the base Gaussian matrices and of $A_0$, then applies Gaussian concentration to each polynomial matrix entry; clipping makes its global Lipschitz constant $O(d^{-1/2})$. Sign symmetry gives zero offdiagonal means; permutation symmetry identifies diagonal means.
* Combine that lemma with the inspected spectral theorem to identify the diagonal distribution with the bi-orthogonally invariant surrogate $A_G=(aXV^\top+\sqrt\nu G)/\sqrt m$.
* Give the causal AMP embedding of the masked logistic GD recursion for $A_0+(a/\sqrt m)zt^\top$, with finite Gaussian perturbations if needed, and verify all nondegeneracy and polynomial-density hypotheses. The rank-one scalar coefficients are empirical overlaps and must also be controlled.
* Append a proportional independent test block and set its training mask to zero. This avoids incorrectly trying to recover test covariance from the singular-value law of the training matrix alone.
* Supply a finite-dimensional Gaussian-query recursion for the three independent Gaussian matrices in $A_G$, then prove the resulting deterministic test-path covariance limit. Theorem 2 and B04's TV theorem would then deliver exact risks and calibration. A limiting optimizer over all training times needs an additional argument beyond any fixed horizon.

These obligations were the initial audit checklist. Sections 8–9 and the companion B01/B04 proofs now close the fixed-horizon items, as assembled in Theorem 6. The separate unbounded-time obligation remains subject to the explicitly restricted B02 extension.

## 8. The perpendicular RF matrix satisfies generalized invariance

This section closes the first two matrix proof obligations in Section 7. The AMP embedding and state-evolution identification remain separate obligations.

Let $N/d\to\delta>0$ be the total number of rows, $p=d-1$, $X\in\mathbb R^{N\times p}$ have independent standard Gaussian entries, and $G\in\mathbb R^{m\times p}$ be an independent standard Gaussian matrix. Set
\[
V=G/\sqrt d,\qquad
A_0=\frac1{\sqrt m}\phi(XV^\top),\qquad r=N/m\to\delta/\gamma.
\tag{8.1}
\]
For the almost-sure source-theorem application below, choose the standard product construction in which the full data-array sequence is independent of the full feature-array sequence, and different dimensions may be taken independent. This choice is harmless for the final in-probability conclusions, which depend only on the per-dimension laws. It avoids conditioning on an entire feature sequence that could encode data from another dimension under an adversarial cross-dimension coupling.

**Theorem 5 (matrix hypothesis verification).** The matrix $A_0$ has the rectangular generalized-invariance property used by Wang–Zhong–Fan, with the same limiting diagonal distribution as
\[
A_G=\frac{aXV^\top+\sqrt\nu\,E}{\sqrt m},
\tag{8.2}
\]
where $E$ is an independent standard Gaussian $N\times m$ matrix. In particular:

1. The operator norm is eventually bounded by a deterministic constant.
2. The singular-value distribution has a deterministic compactly supported limit, identical to that of (8.2), and its second moment is positive.
3. For every fixed integer $k\ge0$ and every $\epsilon>0$, the following inequalities hold eventually almost surely (with positive powers used for the first two lines):
\[
\max_i\left|((A_0A_0^\top)^k)_{ii}-\frac1N\operatorname{tr}(A_0A_0^\top)^k\right|
+\max_{i\ne j}|((A_0A_0^\top)^k)_{ij}|
\le m^{-1/2+\epsilon},
\tag{8.3}
\]
\[
\max_i\left|((A_0^\top A_0)^k)_{ii}-\frac1m\operatorname{tr}(A_0^\top A_0)^k\right|
+\max_{i\ne j}|((A_0^\top A_0)^k)_{ij}|
\le m^{-1/2+\epsilon},
\tag{8.4}
\]
\[
\max_{i,j}|((A_0A_0^\top)^kA_0)_{ij}|\le m^{-1/2+\epsilon}.
\tag{8.5}
\]
4. It is invariant under independent signed permutations of its rows and columns.

**Proof of the uniform entry estimates.** For a matrix $B$, let $\mathcal P_R(B)$ denote its Frobenius-metric projection onto the closed convex set $\{C:\|C\|_{\rm op}\le R\}$. This map clips singular values at $R$ and is Frobenius-nonexpansive. It commutes with left and right orthogonal transformations.

Fix sufficiently large deterministic constants $C_X,C_G,C_A$, and define
\[
\bar X=\mathcal P_{C_X\sqrt d}(X),\quad
\bar G=\mathcal P_{C_G\sqrt d}(G),\quad
B=\mathcal P_{C_A}\!\left(\frac1{\sqrt m}\phi(\bar X\bar G^\top/\sqrt d)\right).
\tag{8.6}
\]
The exponential norm bounds in Section 2 show $B=A_0$ outside an event of probability at most $C e^{-cd}$. Thus $B=A_0$ eventually almost surely. This explicit clipping step avoids the invalid inference that a derivative bound only on a nonconvex high-probability set is automatically a global Lipschitz bound.

For any two base inputs, the product inequality and the scalar Lipschitz property of tanh give
\[
\|B(X,G)-B(X',G')\|_F
\le\frac C{\sqrt m}\big(\|X-X'\|_F+\|G-G'\|_F\big)
\le\frac {C'}{\sqrt d}\|(X,G)-(X',G')\|_F.
\tag{8.7}
\]
Because $\|B\|_{\rm op}\le C_A$, each scalar entry of $(BB^\top)^k$, $(B^\top B)^k$, or $(BB^\top)^kB$ is a globally $C_k$-Lipschitz function of $B$ in Frobenius norm. This follows by telescoping products; for example
\[
\|(BB^\top)^k-(B'B'^\top)^k\|_F
\le 2k C_A^{2k-1}\|B-B'\|_F.
\]
Consequently each such scalar entry is $C_k'/\sqrt d$-Lipschitz in the independent standard Gaussian base entries.

Oddness of tanh and equivariance of all clipping maps imply that $B$ is invariant under row and column signed permutations. Therefore every offdiagonal entry of $(BB^\top)^k$ or $(B^\top B)^k$ has expectation zero; all diagonal entries in a given block have the same expectation; and all entries of $(BB^\top)^kB$ have expectation zero. Gaussian concentration and a union bound over $O(d^2)$ entries give, for any fixed $\eta>0$, failure probability at most
\[
C_kd^2\exp(-c_k d^{2\eta})
\]
for the assertion that every entry differs from its expectation by at most $d^{-1/2+\eta}$. This sequence is summable. The difference between a diagonal expectation and the realized average trace is bounded by the same maximum diagonal error. Choose $\eta<\epsilon$ and absorb fixed constants and dimension ratios. Borel–Cantelli and $B=A_0$ eventually prove (8.3)–(8.5), simultaneously for the countable collection of integer $k$ and rational positive $\epsilon$. Arbitrary positive $\epsilon$ follows by decreasing it to a rational number.

**Proof of spectral matching.** Let
\[
\Sigma_V=\mathbb E_x[\phi(Vx)\phi(Vx)^\top],\qquad
C_V=a^2VV^\top+\nu I_m.
\]
The old covariance proof strengthens to almost sure operator convergence here:
\[
\|\Sigma_V-C_V\|_{\rm op}\to0. \tag{8.8}
\]
Indeed Gaussian norm and spherical-inner-product tails imply, eventually almost surely,
\[
\max_j|\|f_j\|^2-1|=O(\sqrt{\log d/d}),\qquad
\max_{j\ne k}\frac{|f_j^\top f_k|}{\|f_j\|\|f_k\|}
=O(\sqrt{\log d/d}).
\]
The offdiagonal higher-odd-Hermite remainder has operator norm at most its maximal absolute row sum, hence at most $C m(\log d/d)^{3/2}=o(1)$. The diagonal remainder and linear Hermite coefficient converge uniformly, proving (8.8).

Condition on any realization of the sequence $V$ satisfying these bounds. The inspected Louart–Liao–Couillet spectral theorem applies to $\phi(XV^\top)$, since $V^\top$ is bounded in operator norm, tanh is Lipschitz, and all dimensions are proportional. It gives the same spectral deterministic equivalent as a Gaussian sample matrix with row covariance $\Sigma_V$. A Gaussian coupling and
\[
\|\Sigma_V^{1/2}-C_V^{1/2}\|_{\rm op}
\le\|\Sigma_V-C_V\|_{\rm op}^{1/2}
\]
replace $\Sigma_V$ by $C_V$ without changing the limiting spectral law. Conditional on $V$, (8.2) has exactly Gaussian independent rows with covariance $C_V/m$. Fubini's theorem transfers this conditional almost-sure conclusion to the joint model.

The empirical eigenvalue law of $VV^\top$ tends to the Marchenko–Pastur law with aspect $\gamma$, so the empirical law of $C_V$ tends to its image under $x\mapsto\nu+a^2x$. The fixed-point description in the spectral theorem consequently has a deterministic limit. More explicitly, if $H$ is that image law, the feature-side squared-singular law is characterized for $\zeta>0$ by
\[
\delta_\zeta=\int\frac{t}{\zeta+rt/(1+\delta_\zeta)}\,dH(t),\qquad
m(-\zeta)=\int\frac1{\zeta+rt/(1+\delta_\zeta)}\,dH(t).
\tag{8.9}
\]
The positive solution is unique: divide its defining equation by $1+\delta_\zeta$ to obtain $\delta_\zeta/(1+\delta_\zeta)=\int t/[\zeta(1+\delta_\zeta)+rt]\,dH(t)$, whose left side is strictly increasing and right side decreasing. The bound $0\le\delta_\zeta\le(\sup\operatorname{supp}H)/\zeta$ makes continuity under weak convergence of uniformly compactly supported covariance laws immediate by subsequences. The deterministic operator bounds turn weak spectral convergence into convergence of every fixed spectral moment. Also $m^{-1}\operatorname{tr}(A_0^\top A_0)\to r v>0$. **Normalization for the AMP source:** its singular-value law $D$ is padded to the row dimension $N$, whereas (8.9) is normalized to the feature dimension $m$. For $k\ge1$, $\mathbb E[D^{2k}]=r^{-1}\int\lambda^k\,d\mu_{\rm feature}(\lambda)$; in particular $\mathbb E D^2=v$, not $rv$. The aspect ratio is $r=N/m$. As an additional normalization check, $\mathbb E D^4=v^2+r(v^2+a^4\gamma)$, so the singular-value law is nonconstant. This also supplies the positive-variance singular-law hypothesis used by the AMP degeneracy-removal argument.

Finally (8.2) is bi-orthogonally invariant: Gaussian left multiplication of $X,E$ and Gaussian right multiplication of $V,E$ preserve their joint law. The independently signed-permutation representation required by the generalized-invariance definition follows by taking an independent copy of $A_0$ and multiplying it by independent uniform signed permutations. The law is unchanged, and these permutations can be independent of any side information already independent of $A_0$. Items 1–4 are precisely the sufficient matrix conditions of the inspected Proposition D.1(b), which identifies the limiting diagonal distribution. ∎

Theorem 5 does not infer dynamics from an empirical spectral law. It verifies the additional entrywise-polynomial and independence hypotheses needed by a dynamical universality theorem. Combined with Proposition 4, the residual issue is the finite-time algorithmic embedding, rather than an unchecked Gaussian-equivalence conjecture for the RF matrix.

Independent check: B06 audited Sections 1–6 and the Section 8 matrix proof on 2026-10-24. Its cross-dimension conditioning precision was incorporated: the almost-sure source application now explicitly uses a product construction. B05 separately verified the LLC source assumptions and spectral comparison and identified the row-versus-feature singular-law convention; that normalization clarification was incorporated above.

## 9. Causal embedding of the rank-one logistic recursion in rectangular AMP

This section supplies the exact algorithmic embedding and the deterministic-overlap comparison. The Gaussian query/state recursion and the covariance-degeneracy regularization are detailed independently by B04/B01. The present formulas specify their normalization and show that no extra universality for arbitrary empirical scalar coefficients is being assumed.

Use a proportional block of additional test inputs, for example $N=2n$, and the deterministic row mask $M_i=1$ for the $n$ training rows and $0$ for the test rows. Set
\[
\pi=n/N=1/2,\quad r=N/m\to2\alpha/\gamma,\quad
\lambda= c/\alpha,\quad s=a\sqrt\gamma,\quad v=\sqrt d\,t.
\tag{9.1}
\]
Here the letter $v$ denotes the feature-side teacher vector only within this section; the scalar feature moment in earlier sections remains $\mathbb E\tanh(G)^2$. Write $w_t=\sqrt m\,b^t$. Proposition 4 reduces the normalized feature matrix to
\[
D=A_0+\frac{s}{m}zv^\top.
\]
The small differences between $(\lambda_d,s_d,r_d)$ and their limits are harmless by the same finite-time stability estimate. The exact resulting physical iteration is
\[
q_t^{\rm emp}=m^{-1}v^\top w_t,\quad
S_t=A_0w_t+s q_t^{\rm emp}z,\quad
r_t=M\odot[Y-\sigma(S_t)],
\tag{9.2}
\]
\[
\rho_t^{\rm emp}=N^{-1}z^\top r_t,\qquad
w_{t+1}=w_t+\lambda[A_0^\top r_t+s r\rho_t^{\rm emp}v],\qquad w_0=0.
\tag{9.3}
\]
The side vectors $(M,z,Y)$ and $v$ are independent of $A_0$. Their empirical laws converge to $(M,Z,Y)$ and $V$, where $M\sim\mathrm{Bernoulli}(\pi)$ is independent of $(Z,Y)$, $Z,V$ are standard Gaussian, and $Y\mid Z\sim\mathrm{Bernoulli}(\sigma(\beta Z))$. Gaussian and bounded side variables have all moments. Polynomial density follows, for example, by splitting the two finite coordinates $M,Y$ and using polynomial density under the Gaussian measure; their joint law is dominated by a constant times Gaussian measure times counting measure.

Let $a_{th},b_{th}$ be the deterministic rectangular-AMP correction coefficients prescribed by the row-normalized singular law in Theorem 5. The AMP has column fields $Z_t^{\rm A}$, row fields $Y_t^{\rm A}$, feature iterates $Q_t$, and residual iterates $R_t$:
\[
Z_t^{\rm A}=A_0^\top R_t-\sum_{h<t}b_{th}Q_h,\qquad
Y_t^{\rm A}=A_0Q_t-\sum_{h\le t}a_{th}R_h.
\tag{9.4}
\]
Initialize $Q_0=0$ and $R_1=M\odot(Y-1/2)$. Define its nonlinearities recursively by
\[
Q_t=Q_{t-1}+\lambda\left[Z_t^{\rm A}+\sum_{h<t}b_{th}Q_h+s r\rho_{t-1}V\right],
\tag{9.5}
\]
\[
R_{t+1}=M\left[Y-\sigma\!\left(Y_t^{\rm A}+\sum_{h\le t}a_{th}R_h+s q_tZ\right)\right],
\tag{9.6}
\]
where
\[
\rho_{t-1}=\mathbb E[Z R_t],\qquad q_t=\mathbb E[VQ_t]
\tag{9.7}
\]
are taken in the limiting AMP law. Each $Q_h$ in (9.5) is already a deterministic function of the past column fields and feature-side information, and each $R_h$ in (9.6) is already a deterministic function of past row fields and sample-side information. Thus these are legitimate memory-dependent coordinatewise nonlinearities.

**Causality.** Before the $t$th column update, the law of $R_t$ and hence $\rho_{t-1}$ are already known. The column field law and (9.5) then determine $Q_t$ and $q_t$. Only after this does (9.6) define $R_{t+1}$. Consequently the overlap definitions introduce no circular fixed point at a time step. The source's AMP covariance and correction-coefficient prescriptions follow the same alternating order.

**Regularity.** At a fixed horizon, (9.5) is affine in its Gaussian-field arguments. Equation (9.6) is recursively globally Lipschitz in its Gaussian-field arguments because $0\le M\le1$ and $\|\sigma'\|_\infty\le1/4$. To meet a theorem requiring definitions on the entire Euclidean side-information space, replace the formal arguments $M,Y$ by their projections onto $[0,1]$; this changes no observed value and keeps the Lipschitz constants uniform in the side arguments. All functions have at most polynomial growth. The Bernoulli sampling threshold is not an update nonlinearity: the already generated label is supplied as side information.

**Exact cancellation.** Substituting (9.4) into (9.5) cancels all $b_{th}$ corrections. Substituting (9.4) into (9.6) cancels all $a_{th}$ corrections. Thus the finite-dimensional AMP trajectory is exactly logistic GD with the scalar overlaps frozen to (9.7). These identities are algebraic and do not use a limit.

**Deterministic-overlap freezing.** Suppose the source theorem is applied to this AMP, or first to its regularized version with fresh side Gaussian perturbations as in the companion proof. Let $(\bar w_t,\bar r_t)$ denote its frozen-overlap physical iterates. Joint empirical $W_2$ convergence gives
\[
\epsilon^q_t:=|m^{-1}v^\top\bar w_t-q_t|\to0,
\qquad
\epsilon^\rho_t:=|N^{-1}z^\top\bar r_t-\rho_t|\to0,
\tag{9.8}
\]
since both products are continuous with quadratic growth. Define
\[
e_t=\|w_t-\bar w_t\|_2/\sqrt m,\quad
h_t=\|r_t-\bar r_t\|_2/\sqrt N,\quad
V_m=\|v\|_2/\sqrt m,\quad Z_N=\|z\|_2/\sqrt N.
\]
On $\|A_0\|_{\rm op}\le C$, Cauchy–Schwarz and sigmoid's derivative bound give
\[
h_t\le\frac14\left[\left(C/\sqrt r+sZ_NV_m\right)e_t+sZ_N\epsilon^q_t\right],
\tag{9.9}
\]
\[
e_{t+1}\le e_t+\lambda\left[\left(C\sqrt r+s rV_mZ_N\right)h_t+s rV_m\epsilon^\rho_t\right].
\tag{9.10}
\]
We have $e_0=0$, $V_m,Z_N\to1$, and finitely many times. Induction using (9.8) proves $\max_{t\le T}(e_t+h_t)\to0$ in probability. Differences in dimension-dependent constants add only $o_P(1)$ terms. Therefore the adaptive-overlap physical iteration has exactly the same finite-time empirical limit as the frozen AMP.

This comparison is independent of whether the source's remark on empirical Onsager coefficients includes the rank-one overlaps: it proves the required replacement directly. B05 independently checked (9.9)–(9.10) and the causal indexing.

## 10. Assembled finite-horizon theorem and its boundary

The preceding inputs, the explicit recursion in `fullproof/b01_GD_state_evolution_check.md`, and the total-variation theorem in `fullproof/b04_calibration_transfer.md` now close the arbitrary fixed finite-horizon Gaussian model. B03 independently reviewed B01's causal recursion, the query-block cancellation, positive-definiteness induction, overlap comparison, and first-step check; B04 independently checked its primary-source covariance formulas. B05/B06 independently checked the matrix inputs above.

**Theorem 6 (original Gaussian tanh GD, each fixed finite horizon).** Fix $\alpha,\gamma,c\in(0,\infty)$, $0\le\beta<\infty$, and a fixed integer $T$. Run the original model (1.1). Compute $q_{1:T},\Sigma_T$ by B01's explicit recursion (16), with $s=a\sqrt\gamma$, and put
\[
A_t=sq_t,\qquad Q_{st}=s^2q_sq_t+(\Sigma_T)_{st}.
\]
Then $\Sigma_T$ is positive definite. Conditional on the realized features and training sample, the joint fresh-test law converges weakly in probability to
\[
\bigl(Z,S_1,\ldots,S_T,Y\bigr),\qquad
S_t=A_tZ+G_t,
\quad G_{1:T}\sim N(0,\Sigma_T),\quad G\perp Z,
\quad Y\mid Z\sim\mathrm{Bernoulli}(\sigma(\beta Z)).
\tag{10.1}
\]
For every $1\le t\le T$, the conditional law of $(Z,S_t,Y)$ in fact converges in total variation in probability. The exact, unbinned, model-conditional calibration error converges in probability and every finite $L^p$ to
\[
C_t=\mathbb E_{S\sim N(0,Q_{tt})}|g_t(S)-\sigma(S)|,
\quad
 g_t(x)=\mathbb E_H\sigma\!\left(\beta\left[\frac{A_t}{Q_{tt}}x+
 \sqrt{\frac{(\Sigma_T)_{tt}}{Q_{tt}}}\,H\right]\right).
\tag{10.2}
\]
Its population logistic risk converges in $L^1$ to
\[
R_t=\mathbb E_G\log\left(2\cosh\left(\frac{\sqrt{Q_{tt}}G}{2}\right)\right)-\kappa A_t,
\qquad
\kappa=\mathbb E[Z(\sigma(\beta Z)-1/2)].
\tag{10.3}
\]
All these convergences are uniform over the finite index set $\{1,\ldots,T\}$. At time zero, $C_0=0$ and $R_0=\log2$ exactly.

**Assembly proof.** Theorem 5 and the side-information/regularity checks in Section 9 verify WZF's matrix and algorithm assumptions. B01's positive-definiteness induction verifies all of its nonsingularity assumptions without perturbation, for every $c>0$. The AMP embedding cancels the memory corrections exactly; (9.9)–(9.10) remove frozen-overlap dependence; Proposition 4 and finite-time operator stability restore the actual tanh features. On a mask-zero test row all residual iterates vanish, so the limiting score is exactly $sq_tZ+G_t$, proving (10.1) for appended test rows.

Conditional on the original training environment those appended rows are independent fresh inputs. Conditional LLNs for bounded observables therefore yield the claimed conditional test-law convergence. For the covariance identification, Gaussian concentration gives
$\mathbb E_X|S_t(X)|^4\le C\|F\|_{\rm op}^4\|b^t\|_2^4=O_P(1)$; hence conditional variances of the appended empirical quadratic averages are $O_P(N^{-1})$. This identifies the realized-model covariance limit with $Q$, including teacher covariances $A$.

Theorem 1 supplies coefficient delocalization. Since B01 proves $(\Sigma_T)_{tt}>0$, B04's deterministic smoothing theorem upgrades each conditional pair to total variation. Adding the fresh label is a common Markov kernel and contracts total variation. B04's signed-measure inequality then proves (10.2). Gaussian integration gives (10.3); uniform second-moment bounds for the scores imply uniform integrability of logistic losses and conditional risks, so the convergence is in $L^1$. Finite unions give the stated uniformity over $t\le T$. ∎

For clarity, $C_t>0$ at every positive finite time. If $\beta=0$, the regression curve is $1/2$ and the score is nondegenerate. If $\beta>0$ and $A_t\le0$, monotonicity prevents $g_t$ from equaling the increasing sigmoid. If $A_t>0$, dominated convergence gives
\[
1-g_t(x)\sim
\exp\!\left[-\frac{\beta A_t}{Q_{tt}}x+
\frac{\beta^2(\Sigma_T)_{tt}}{2Q_{tt}}\right]
\quad(x\to\infty).
\]
Equality with $1-\sigma(x)\sim e^{-x}$ would require both $\beta A_t/Q_{tt}=1$ and $(\Sigma_T)_{tt}=0$, contradicting positive definiteness. Continuity and the everywhere-positive score density turn nonidentity into strictly positive calibration error.

For any training-dependent stopping time $\tau_d\in\{0,\ldots,T\}$, the realized population risk and calibration are approximated, in probability, by $R_{\tau_d}$ and $C_{\tau_d}$. If the deterministic finite-grid risk has a unique minimizer, every minimizer of the realized population risk on that grid converges to it in probability. Minimizing calibration alone includes the exact zero-score solution at time zero. No monotonicity of the risk or calibration curve is asserted.

This theorem concerns every fixed finite horizon, at arbitrary positive finite aspect ratios and step size. It does not, by itself, identify an infinite-time limit or optimize over an unbounded stopping horizon. The companion `fullproof/b02_uniform_time_GD.md` gives an additional all-time result under its explicitly stated sample-ratio and small-step assumptions; those hypotheses must remain visible whenever that extension is used.


---

# Appendix B: Explicit finite-time state evolution

Source module: `b01_GD_state_evolution_check.md`. SHA-256: `077b6c8134a2780f4ad5132be70fe50ccdfccd7240d00a50b4ea775d1ea0338f`.

# Explicit finite-time state evolution for the original Gaussian RF logistic GD

Independent derivation and normalization audit — 2026-10-23 (America/New_York).

**Conclusion.** The finite-time recursion below describes ordinary full-batch output-weight gradient descent. The AMP memory coefficients are added and subtracted in an auxiliary representation and cancel from the physical update. For the spectral law proved in B03, every rectangular free cumulant has a closed expression, so the recursion uses only finite triangular matrix inverses and Gaussian expectations. Its covariance matrices are positive definite at every fixed time when the step size is positive. No added algorithmic noise or change from GD to AMP is required. The first-step test signal and variance agree exactly with the separately audited formulas.

This report relies on B03's Proposition 4 (the teacher-spike decomposition) and Theorem 5 (the generalized-invariance and spectral hypotheses), whose statements are in `fullproof/b03_gaussian_dynamics.md`. Those matrix inputs are being independently audited by B05/B06. The statements here concern each fixed finite horizon; they do not exchange the limits in dimension and training time.

**Finite-horizon theorem.** In the Gaussian tanh model of Section 1, for each fixed integer $T\ge1$, each fixed $c>0$, and every $\alpha,\gamma>0$ and finite $\beta\ge0$, the actual GD sequence (1) has the deterministic state evolution (11)–(16). In probability, its training empirical path distribution converges in $W_2$ to the scalar training law (12) conditioned on $M=1$, and
\[
(b^s)^\top b^t\longrightarrow(\Gamma_T)_{st}\qquad(1\le s,t\le T).
\]
Conditional on the training data and random features, the joint law of a fresh teacher coordinate and fresh score path converges weakly, with convergence of all second moments, to
\[
\left(Z_\star,s q_1Z_\star+G_1,\ldots,s q_TZ_\star+G_T\right),
\qquad G_{1:T}\sim N(0,\Sigma_T),\quad G_{1:T}\perp Z_\star.
\]
Thus the realized test covariances converge to (18). Every $\Omega_t$ and $\Sigma_t$ in the recursion is positive definite. Sections 2–8 prove this theorem from the stated B03 matrix results and the inspected WZF theorem.

## 1. Model, dimensions, and the physical update

Let $X_i\sim N(0,I_d)$, let $\theta$ be a deterministic unit vector, and let
\[
Y_i\mid X_i\sim\operatorname{Bernoulli}(\sigma(\beta\theta^\top X_i)),
\qquad \sigma(x)=(1+e^{-x})^{-1},\quad 0\le\beta<\infty.
\]
There are $n$ training examples and $m$ independent random features $W_j\sim N(0,I_d/d)$, with
\[
n/d\to\alpha>0,\qquad m/d\to\gamma>0,\qquad
H_{ij}=\tanh(W_j^\top X_i).
\]
Write
\[
a=\mathbb E[G\tanh G],\qquad v=\mathbb E[\tanh^2G],\qquad
\nu=v-a^2>0,\quad G\sim N(0,1).
\]
Strict positivity follows because $\tanh G$ is not a scalar multiple of $G$ in Gaussian $L^2$.

In B03's normalization, $w^t=\sqrt m\,b^t$, $A=H/\sqrt m$, and a mean-loss GD step of size $cd$ gives
\[
w^0=0,\qquad w^{t+1}=w^t+\lambda_d A^\top r^t,
\quad r^t=M\odot(Y-\sigma(Aw^t)),\quad \lambda_d=cd/n\to\lambda=c/\alpha.
\tag{1}
\]
Here a proportional independent query block is appended to the rows, and $M_i=1$ on training rows and $M_i=0$ on query rows. If the total number of rows is $N$, set
\[
N/d\to\delta>\alpha,\qquad r=N/m\to\delta/\gamma,
\qquad p=n/N\to\alpha/\delta.
\tag{2}
\]
The common choice $N=2n$ gives $p=1/2$, $\delta=2\alpha$. No result depends on that choice.

Rotate $\theta$ to the first coordinate. Let $z_i=\theta^\top X_i$ and $h_j=\sqrt d\,\theta^\top W_j$. Then $z_i,h_j$ are standard normal, and B03's decomposition is
\[
A=A_0+\frac{s_d}{m}zh^\top+E_d,
\quad s_d=a\sqrt{m/d}\to s=a\sqrt\gamma,
\quad \|E_d\|_{\rm op}=o_{\mathbb P}(1).
\tag{3}
\]
The perpendicular matrix $A_0$ is independent of $(z,Y,M,h)$. For the exact spike matrix $A_0+s_dzh^\top/m$, the physical GD update is
\[
Q_t=Q_{t-1}+\lambda_d\left[A_0^\top R_t+s_d r_d\ell_t^{(d)}h\right],
\quad R_{t+1}=M\odot\left[Y-\sigma(A_0Q_t+s_dq_t^{(d)}z)\right],
\tag{4}
\]
where $Q_t=w^t$, $R_t=r^{t-1}$,
\[
q_t^{(d)}=m^{-1}h^\top Q_t,\qquad
\ell_t^{(d)}=N^{-1}z^\top R_t,\qquad r_d=N/m.
\]
In particular the column spike coefficient is $s r\ell_t$, not $s\ell_t$.

## 2. The RF rectangular cumulants have a closed form

Let $\mu_k$ be the limiting **row-normalized** moments
\[
\mu_k=\lim N^{-1}\operatorname{tr}(A_0A_0^\top)^k.
\]
The squared singular-value law is padded with zeros to $N$ values when necessary. B03's comparison Gaussian matrix has independent rows conditional on its feature covariance, whose limiting covariance law is
\[
\mathcal H=\mathcal L(\nu+a^2 L),\qquad L\sim\operatorname{MP}_{\gamma},
\quad \mathbb EL=1.
\]
Let $M(z)=\sum_{k\ge1}\mu_kz^k$ and $M_{\mathcal H}(z)=\sum_{k\ge1}(\int t^k\,d\mathcal H(t))z^k$. The spectral fixed point in B03, expanded at infinity, gives the formal-power-series identity
\[
rM(z)=M_{\mathcal H}\big(rz(1+M(z))\big).
\tag{5}
\]
For completeness, writing $m_F(-\zeta)$ for the feature-side Stieltjes transform and $e_\zeta$ for B03's auxiliary scalar, its fixed point implies
$r e_\zeta/(1+e_\zeta)=1-\zeta m_F(-\zeta)$.
Since the feature moment series is $rM$, substitution $z=-1/\zeta$ gives
$e_\zeta=-M/(1+M)$ and then (5).

The ordinary free $R$-transform of $\mathcal H$ is
\[
R_{\mathcal H}^{\rm ord}(u)=\nu+\frac{a^2}{1-a^2\gamma u}.
\]
Equivalently,
\[
M_{\mathcal H}(w)=w(1+M_{\mathcal H}(w))
\left[\nu+\frac{a^2}{1-a^2\gamma w(1+M_{\mathcal H}(w))}\right].
\]
Combine this identity with (5), and set $t=z(1+M)(1+rM)$. Since $r\gamma=\delta$, this yields
\[
M(z)=\nu t+\frac{a^2t}{1-a^2\delta t}.
\tag{6}
\]
Fan's rectangular moment/cumulant identity is $M(z)=R_{\rm rect}(z(1+M(z))(1+rM(z)))$. Therefore
\[
\boxed{R_{\rm rect}(t)=\nu t+\frac{a^2t}{1-a^2\delta t},\qquad
\kappa_2=v,\quad\kappa_{2k}=a^{2k}\delta^{k-1}\ (k\ge2).}
\tag{7}
\]
This is a formal-series identity; no convergence radius or small-step condition is needed. In particular
\[
\mu_1=v,\qquad
\mu_2=(1+r)v^2+\delta a^4
=v^2+r(v^2+a^4\gamma),\qquad \kappa_4=\delta a^4.
\tag{8}
\]

## 3. Exact finite-dimensional memory and covariance formulas

Use $R_t$ for the scalar row residual and $Q_t$ for the scalar column iterate. The centered row and column Gaussian fields will be $G_t$ and $Z_t$, respectively. Their covariance matrices are $\Sigma_t$ and $\Omega_t$. The teacher scalar is denoted $Z_\star$, and the independent column teacher coordinate is $H_\star$.

Define the $t\times t$ matrices
\[
\Delta_t=(\mathbb E[R_iR_j])_{i,j\le t},\quad
\Gamma_t=(\mathbb E[Q_iQ_j])_{i,j\le t},
\]
\[
(\Phi_t)_{ij}=\mathbb E\left[\frac{\partial R_i}{\partial G_j}\right]
\quad(j<i),\qquad
(\Psi_t)_{ij}=\mathbb E\left[\frac{\partial Q_i}{\partial Z_j}\right]
\quad(j\le i),
\tag{9}
\]
and put zero in the remaining entries. Thus $\Phi_t$ is strictly lower triangular and $\Psi_t$ is lower triangular. All derivatives hold the deterministic recursion coefficients fixed.

Our coefficient matrices $\mathsf A_t=(a_{ij})$ and $\mathsf B_t=(b_{ij})$ are **lower** triangular. They are the transposes of Fan's displayed upper-triangular matrices $A_t,B_t$. Set $h_0=a^2\delta$. Then the explicit formulas are
\[
\boxed{\begin{aligned}
\mathsf A_t&=\nu\Psi_t+a^2\Psi_t(I-h_0\Phi_t\Psi_t)^{-1},\\
\mathsf B_t&=r\nu\Phi_t+ra^2\Phi_t(I-h_0\Psi_t\Phi_t)^{-1},\\
\Sigma_t&=\nu\Gamma_t+a^2(I-h_0\Psi_t\Phi_t)^{-1}
\left[\Gamma_t+h_0\Psi_t\Delta_t\Psi_t^\top\right]
(I-h_0\Psi_t\Phi_t)^{-\top},\\
\Omega_t&=r\nu\Delta_t+ra^2(I-h_0\Phi_t\Psi_t)^{-1}
\left[\Delta_t+h_0\Phi_t\Gamma_t\Phi_t^\top\right]
(I-h_0\Phi_t\Psi_t)^{-\top}.
\end{aligned}}
\tag{10}
\]
Every inverse is a finite polynomial: $\Phi_t\Psi_t$ and $\Psi_t\Phi_t$ are strictly lower triangular, so $(I-h_0L)^{-1}=\sum_{j=0}^{t-1}h_0^jL^j$.

Here is an explicit check against the primary-source formulas. With $L=\Phi\Psi$ and $K=\Psi\Phi$, Fan's covariance coefficients, in our notation, are
\[
\Theta^{(j)}=\sum_{i=0}^jL^i\Delta(L^\top)^{j-i}
+\sum_{i=0}^{j-1}L^i\Phi\Gamma\Phi^\top(L^\top)^{j-1-i},
\]
\[
\Xi^{(j)}=\sum_{i=0}^jK^i\Gamma(K^\top)^{j-i}
+\sum_{i=0}^{j-1}K^i\Psi\Delta\Psi^\top(K^\top)^{j-1-i}.
\]
The second sums are empty for $j=0$. His prescriptions give
$\Sigma=\sum_{j\ge0}\kappa_{2j+2}\Xi^{(j)}$,
$\Omega=r\sum_{j\ge0}\kappa_{2j+2}\Theta^{(j)}$,
$\mathsf A=\sum_{j\ge0}\kappa_{2j+2}\Psi(\Phi\Psi)^j$, and
$\mathsf B=r\sum_{j\ge0}\kappa_{2j+2}\Phi(\Psi\Phi)^j$.
Inserting (7) and summing the two finite geometric series proves (10). In particular no additional factor of $r$ belongs inside either covariance bracket.

## 4. Causal recursion and its implementation without circular definitions

Let
\[
Z_\star,H_\star\sim N(0,1),\quad
Y\mid Z_\star\sim\operatorname{Bernoulli}(\sigma(\beta Z_\star)),
\quad M\sim\operatorname{Bernoulli}(p),
\]
with $M$ independent of $(Z_\star,Y)$ and $H_\star$ on the separate column probability space. Initialize
\[
R_1=M(Y-1/2),\qquad Q_0=0,\qquad q_0=0.
\]
For $t=1,2,\ldots$, carry out the following operations.

1. From the already defined row functions $R_{1:t}(G_{1:t-1},Z_\star,Y,M)$ and $\Sigma_{t-1}$, compute $\Delta_t$, $\Phi_t$, and $\ell_t=\mathbb E[Z_\star R_t]$.
2. Embed the previous $\Psi_{t-1},\Gamma_{t-1}$ in $t\times t$ matrices with zero last row/column. Compute $\mathsf B_t,\Omega_t$ from (10). Their values do not depend on the missing current column function: the last column of $\Phi_t$ is zero, so $\Phi_t\Psi_t$ and $\Phi_t\Gamma_t\Phi_t^\top$ only use previous column information.
3. Let $Z_{1:t}\sim N(0,\Omega_t)$ independently of $H_\star$, consistently with previous stages. Define
\[
Q_t=Q_{t-1}+\lambda\left[Z_t+\sum_{j<t}b_{tj}Q_j+s r\ell_tH_\star\right],
\qquad q_t=\mathbb E[H_\star Q_t].
\tag{11}
\]
4. Compute the current derivative row of $\Psi_t$ and $\Gamma_t$, then compute $\mathsf A_t,\Sigma_t$ using (10). Let $G_{1:t}\sim N(0,\Sigma_t)$ independently of $(Z_\star,Y,M)$. Define
\[
S_t=G_t+\sum_{j\le t}a_{tj}R_j+s q_tZ_\star,
\qquad R_{t+1}=M(Y-\sigma(S_t)).
\tag{12}
\]

All column functions are linear. More precisely,
\[
Q_{1:t}=\Psi_tZ_{1:t}+q_{1:t}H_\star,\qquad
\Gamma_t=\Psi_t\Omega_t\Psi_t^\top+q_{1:t}q_{1:t}^\top,
\tag{13}
\]
and their coefficients can be calculated without integration:
\[
(\Psi_t)_{tj}=(\Psi_{t-1})_{t-1,j}
+\lambda\mathbf1_{\{j=t\}}+\lambda\sum_{k<t}b_{tk}(\Psi_{t-1})_{kj},
\]
\[
q_t=q_{t-1}+\lambda\sum_{j<t}b_{tj}q_j+\lambda s r\ell_t,
\tag{14}
\]
where nonexistent entries at $t=1$ are zero. In particular every diagonal entry of $\Psi_t$ equals $\lambda$.

For the row derivatives, differentiate the already explicit scalar recursion:
\[
\frac{\partial R_{t+1}}{\partial G_j}
=-M\sigma'(S_t)\left[\mathbf1_{\{j=t\}}
+\sum_{k\le t}a_{tk}\frac{\partial R_k}{\partial G_j}\right],\quad j\le t.
\tag{15}
\]
Thus the remaining computations are finite-dimensional Gaussian integrals and a Bernoulli average; there is no unknown limiting quantity outside the recursion.

## 5. Query-block size cancels exactly

The apparent dependence on $\delta$ in (7)–(12) is only a bookkeeping choice. Let $R^{\rm tr}_t$ be the row recursion conditioned on $M=1$. Define
\[
\widehat\Delta_t=\alpha(\mathbb E[R_i^{\rm tr}R_j^{\rm tr}])_{i,j\le t},\qquad
\widehat\Phi_t=\alpha(\mathbb E[\partial_{G_j}R_i^{\rm tr}])_{i,j\le t},
\qquad \widehat\ell_t=\alpha\mathbb E[Z_\star R_t^{\rm tr}].
\]
Since $R_t=0$ when $M=0$,
\[
\widehat\Delta_t=\delta\Delta_t,\qquad
\widehat\Phi_t=\delta\Phi_t,\qquad \widehat\ell_t=\delta\ell_t.
\]
Define $T_t=(I-a^2\Psi_t\widehat\Phi_t)^{-1}$ and
$U_t=(I-a^2\widehat\Phi_t\Psi_t)^{-1}$. Then (10) becomes
\[
\boxed{\begin{aligned}
\mathsf A_t&=\nu\Psi_t+a^2\Psi_tU_t,\\
\mathsf B_t&=\gamma^{-1}\left[\nu\widehat\Phi_t+a^2\widehat\Phi_tT_t\right],\\
\Sigma_t&=\nu\Gamma_t+a^2T_t\left[\Gamma_t+a^2\Psi_t\widehat\Delta_t\Psi_t^\top\right]T_t^\top,\\
\Omega_t&=\gamma^{-1}\left\{\nu\widehat\Delta_t+a^2U_t
\left[\widehat\Delta_t+a^2\widehat\Phi_t\Gamma_t\widehat\Phi_t^\top\right]U_t^\top\right\}.
\end{aligned}}
\tag{16}
\]
Replace $s r\ell_t$ in (11) by $(s/\gamma)\widehat\ell_t$ and use $M=1$ in the training scalar recursion. This is an entirely $\delta$-free prescription, depending only on $(\alpha,\gamma,\beta,c,a,\nu)$.

On a query row $M=0$, every $R_j$ is zero. The physical test path is therefore
\[
\boxed{S_t^{\rm test}=s q_tZ_\star+G_t,\qquad
G_{1:T}\sim N(0,\Sigma_T)\text{ independently of }Z_\star.}
\tag{17}
\]
Its deterministic teacher/score overlaps are
\[
\mathcal A_t=s q_t,\qquad
\mathcal Q_{st}=s^2q_sq_t+(\Sigma_T)_{st}.
\tag{18}
\]
Equation (16) proves algebraically that these quantities are independent of the number of appended queries.

## 6. Positive definiteness: no regularization or algorithm change

Suppose $c>0$. Equations (10) imply
\[
\Omega_t\succeq r\nu\Delta_t,\qquad \Sigma_t\succeq\nu\Gamma_t.
\tag{19}
\]
Initially $\Delta_1=p/4>0$. If $\Delta_t\succ0$, then $\Omega_t\succ0$. Since $\Psi_t$ is triangular with diagonal $\lambda>0$, (13) gives $\Gamma_t\succ0$, hence $\Sigma_t\succ0$.

To continue the induction, suppose $R_{t+1}$ were in the linear span of $R_1,\ldots,R_t$ almost surely. Condition on $(Z_\star,Y,M,G_1,\ldots,G_{t-1})$. On the event $M=1$ of positive probability, all previous residuals are fixed. But the conditional variance of $G_t$ is positive because $\Sigma_t\succ0$, and
\[
R_{t+1}=Y-\sigma\left(G_t+\sum_{j\le t}a_{tj}R_j+s q_tZ_\star\right)
\]
is a strictly monotone nonconstant function of that conditional Gaussian. This is impossible. Therefore $\Delta_{t+1}\succ0$. Induction establishes positive definiteness at every finite stage, including the uninformative-teacher case $\beta=0$.

The case $c=0$ is immediate from (1): every score is zero. It need not be passed through a theorem requiring nonsingular covariances.

## 7. Why this is ordinary GD, including adaptive overlaps

For any fixed deterministic arrays $a_{tj},b_{tj}$, introduce fields
\[
\mathbf Z_t=A_0^\top\mathbf R_t-\sum_{j<t}b_{tj}\mathbf Q_j,
\qquad
\mathbf G_t=A_0\mathbf Q_t-\sum_{j\le t}a_{tj}\mathbf R_j.
\]
Using (11) and (12) coordinatewise adds these same terms back. With empirical teacher overlaps, the resulting algorithm is identically (4), at every finite dimension. This algebra does not impose an Onsager correction on GD.

For the theorem application, first use the deterministic scalar overlaps $q_t,\ell_t$ of (11)–(12). The resulting auxiliary AMP has coordinatewise nonlinearities, so WZF applies. Its empirical overlaps converge to $q_t,\ell_t$ by its joint $W_2$ convergence with the teacher side information. Then compare it with the empirical-overlap recursion (4).

Here are explicit bounds closing that comparison. Normalize errors by
$e^Q_t=\|Q_t^{\rm GD}-Q_t^{\rm aux}\|/\sqrt m$ and
$e^R_t=\|R_t^{\rm GD}-R_t^{\rm aux}\|/\sqrt N$.
On events where $\|A_0\|_{\rm op}$, $\|h\|/\sqrt m$, $\|z\|/\sqrt N$, and the fixed dimension ratios are bounded, Cauchy–Schwarz gives
\[
|q_t^{\rm GD}-q_t|\le C e^Q_t+
|m^{-1}h^\top Q_t^{\rm aux}-q_t|,
\]
\[
|\ell_t^{\rm GD}-\ell_t|\le C e^R_t+
|N^{-1}z^\top R_t^{\rm aux}-\ell_t|.
\]
The two trailing terms tend to zero. The physical updates and $\operatorname{Lip}(\sigma)=1/4$ then imply
\[
e^Q_t\le e^Q_{t-1}+C e^R_t+o_{\mathbb P}(1),\qquad
e^R_{t+1}\le C e^Q_t+o_{\mathbb P}(1).
\tag{20}
\]
The initial error is zero, so both errors vanish at every fixed time. Replacing $s_d,\lambda_d,r_d$ by their limits only adds vanishing terms of the same kind.

Finally, $\|E_d\|_{\rm op}=o_{\mathbb P}(1)$ in (3) transfers this conclusion to the **actual tanh RF matrix**. At fixed time $\|Q_t\|/\sqrt m=O_{\mathbb P}(1)$ and $\|R_t\|/\sqrt N\le1$. Thus every occurrence of $E_dQ_t$ or $E_d^\top R_t$ is $o_{\mathbb P}(1)$ in the relevant normalized norm, and the same finite induction proves convergence of actual-GD iterates and score vectors.

The appended queries never enter the update, since their mask is zero. Conditional on the training data and features, their score paths are iid fresh-test paths. A conditional law of large numbers for bounded Lipschitz functions therefore converts empirical query convergence into convergence in probability of the conditional fresh-test law to (17). Quadratic observables also converge: the fixed-time operator bounds and Gaussian Lipschitz concentration give bounded conditional fourth moments in probability, so the conditional variance of their query averages is $O_{\mathbb P}(1/N)$. Consequently the realized fresh-test covariance in B03 converges to (18).

## 8. Source hypotheses and indexing audit

The directly inspected primary sources are:

- Zhou Fan, *Approximate Message Passing algorithms for rotationally invariant matrices*, Annals of Statistics 50(1), 197–224 (2022), [arXiv:2008.11892v5](https://arxiv.org/pdf/2008.11892). Section 2.4 gives the rectangular cumulant convention. Section 5.1, equations (5.7)–(5.13), gives the memory/covariance prescription. Corollary 5.4 addresses degeneracy for the invariant comparison ensemble.
- Tianhao Wang, Xinyi Zhong, and Zhou Fan, *Universality of Approximate Message Passing algorithms and tensor networks*, Annals of Applied Probability 34(4), 3943–3994 (2024), [arXiv:2206.13037v5](https://arxiv.org/html/2206.13037v5). The applicable result is Theorem 2.22 with Assumption 2.17, algorithm (2.14), and prescriptions (D.4)–(D.5). Proposition D.1(b) supplies the matrix criterion checked in B03.

The application checks are as follows.

| Requirement | Verification |
|---|---|
| Generalized-invariant matrix with invariant comparison law | B03 Theorem 5, applied to the perpendicular RF matrix with all training/query rows present |
| Independent initialization and side information | $A_0$ is independent of $z,Y,M,h$ after teacher-coordinate separation |
| Nonzero initial AMP second moment | $R_1=M(Y-1/2)$ and $\mathbb ER_1^2=p/4$; zero GD weights do not mean zero AMP initialization |
| All side-information moments and polynomial density | Gaussian teacher coordinates and bounded labels/masks have exponential moments; their polynomial algebra is dense in $L^2$ |
| Coordinatewise continuous, polynomial-growth, Lipschitz functions | Column functions are linear; row functions are finite compositions of sigmoid and affine functions with deterministic coefficients |
| Uniform Lipschitz constants over side information | Extend the mask off $\{0,1\}$ by the smooth bounded function $\sin^2(\pi x/2)$; this leaves actual iterates unchanged and keeps row derivatives uniformly bounded |
| Eventual operator bound and positive spectral second moment | B03 Theorem 5; $\mathbb ED^2=v>0$ |
| Nonsingular $\Omega_t,\Sigma_t$ | The direct induction in Section 6 |
| Empirical teacher-overlap dependence | Apply the theorem to deterministic overlaps first, then use (20) |
| Fixed time and consistent finite aspect ratios | Every statement fixes $T$ before $d\to\infty$; deterministic parameter replacements are handled by (20) |
| Fresh-test extraction | Mask-zero appended rows, (17), and the conditional law of large numbers |

The source notation uses a matrix with “$m$ rows and $n$ columns.” Here these correspond to $N$ rows and $m$ features, so its aspect parameter is $r=\delta/\gamma$, **not** the RF ratio $\gamma=m/d$. The zero padding in Section 2 is essential when $N>m$.

## 9. Exact first-step validation

Put
\[
\mu=\mathbb E[Z_\star(\sigma(\beta Z_\star)-1/2)].
\]
Using the query-independent recursion (16),
\[
\widehat\Delta_{11}=\alpha/4,\quad \widehat\Phi_{11}=0,
\quad \widehat\ell_1=\alpha\mu,\quad
\Omega_{11}=\frac{\alpha v}{4\gamma},\quad \Psi_{11}=\lambda.
\]
Consequently
\[
Q_1=\lambda Z_1+\frac{ca\mu}{\sqrt\gamma}H_\star,
\quad q_1=\frac{ca\mu}{\sqrt\gamma},\quad
\Gamma_{11}=\frac{c^2v}{4\alpha\gamma}+\frac{c^2a^2\mu^2}{\gamma}.
\]
The forward memory coefficient is $a_{11}=\lambda v$. It vanishes from a test score because $R_1=0$ on the test block. The Gaussian residual variance is
\[
\begin{aligned}
\Sigma_{11}
&=v\Gamma_{11}+a^4\lambda^2\widehat\Delta_{11}\\
&=c^2\left[\frac{\mu^2a^2v}{\gamma}
+\frac{a^4+v^2/\gamma}{4\alpha}\right].
\end{aligned}
\]
Since $s q_1=ca^2\mu$, the fresh-test law is exactly
\[
\boxed{S_1^{\rm test}=ca^2\mu\,Z_\star+	au_1G,\qquad
\tau_1^2=c^2\left[\frac{\mu^2a^2v}{\gamma}
+\frac{a^4+v^2/\gamma}{4\alpha}\right],}
\tag{21}
\]
with $G$ independent standard normal. This reproduces both terms of the audited first-step variance. Omitting $\kappa_4=\delta a^4$ would incorrectly remove $c^2a^4/(4\alpha)$; forgetting the mask-zero query block would incorrectly retain the training self term $\lambda v(Y-1/2)$.

## 10. Review status

B04 independently compared (10) with Fan's primary-source equations and checked the positive-definiteness induction. B03 independently checked the causal construction, all four query-ratio cancellations, the overlap comparison, the query extraction, and the all-order cumulant derivation; its separate three-Gaussian query calculation also agrees with (21). B05 independently checked the cumulant derivation and the B03 spectral/source hypotheses. These reviewers found no gap in the stated finite-horizon conclusion. The matrix input remains explicitly B03 Theorem 5 and its teacher-spike decomposition. No statement here asserts novelty of the original AMP theorem or a uniform-in-time GD limit.


---

# Appendix C: Total variation and exact calibration

Source module: `b04_calibration_transfer.md`. SHA-256: `ce160157647aed6aa8d405979525f31649ce8f91d99ca9ce8821d3d849eaa574`.

# Exact model-conditional calibration for Gaussian tanh random features

24 October 2026. B04. New proof; no frozen file is changed.

**Main result.** The first-step Gaussian tanh RF model in
`followup/T357_gaussian_first_step_attempt.md` has convergence of its exact,
unbinned, model-conditional calibration error to the proposed Gaussian
quantity, in probability and in every finite \(L^p\) over the trained model.
The missing ingredient is a total-variation upgrade, proved below. It uses
delocalization of the output coefficients, not weak convergence alone.

There is also a structural result for later trained readouts: every
delocalized readout with nondegenerate residual variance admits a joint
Gaussian approximation in total variation, conditional on the realized
features and coefficients. Its covariance may remain model-dependent.
Consequently its exact calibration is approximated by an explicit Gaussian
functional of those covariances. This result does **not** establish a
deterministic state evolution for later GD iterates.

The proofs of the analytic transfer and the first-step coefficient bounds
are supplied here. The only model-specific probabilistic limit imported
for the first-step conclusion is the already independently audited
one-test/two-test-replica result in the files named above and in
`followup/T357_gaussian_first_step_independent_review.md`.

## 1. Notation and the exact calibration functional

Write

\[
X\sim N(0,I_d),\quad Z=\theta_d^\top X,\quad \|\theta_d\|=1,
\quad S=f_d(X),\quad
Y\mid X,\mathcal E_d\sim\operatorname{Bernoulli}(p(Z)),
\quad p(z)=\sigma(\beta z).
\]

The environment \(\mathcal E_d\) contains the training data and random
features, and the fresh \(X\) is independent of this environment. A
realized score is a deterministic function of this fresh input. We use
the **total-variation norm** convention

\[
\|\mu-\nu\|_{\rm TV}
 =\sup_{|h|\le1}\left|\int h\,d\mu-\int h\,d\nu\right|,
\tag{1.1}
\]

which is twice \(\sup_A|\mu(A)-\nu(A)|\) for probability measures.

Let \(\mu\) be the conditional law of \((Z,S)\). Its exact calibration
functional is

\[
\mathcal C_\beta(\mu)
 =\mathbb E_\mu\left|
       \mathbb E_\mu[p(Z)\mid S]-\sigma(S)\right|.
\tag{1.2}
\]

This equals the original calibration error conditioned on the predicted
probability and the environment, since sigmoid is one-to-one and
\(\mathbb E[Y\mid X,\mathcal E_d]=p(Z)\).

For a finite signed measure on the score line define

\[
\zeta_\mu(B)=\int\mathbf1_{\{s\in B\}}
                    [p(z)-\sigma(s)]\,\mu(dz,ds).
\]

Its Radon--Nikodym derivative relative to the score marginal is
\(\mathbb E_\mu[p(Z)\mid S=s]-\sigma(s)\), so

\[
\mathcal C_\beta(\mu)=\|\zeta_\mu\|_{\rm TV}.
\]

Consequently, for any two probability laws on \(\mathbb R^2\),

\[
\boxed{\quad
 |\mathcal C_\beta(\mu)-\mathcal C_\beta(\nu)|
 \le \|\mu-\nu\|_{\rm TV}.
 \quad}
\tag{1.3}
\]

Indeed \(|p(z)-\sigma(s)|\le1\), and multiplication by this bounded
function followed by projection onto the score coordinate contracts the
total-variation norm. Thus no continuity of a conditional-expectation
operator under weak convergence is being asserted.

There is a useful stronger statement. Let
\(g_\mu(s)=\mathbb E_\mu[p(Z)\mid S=s]\), and choose an everywhere
\([0,1]\)-valued version of \(g_\nu\) on the whole score line. The same signed-measure argument,
applied to the positive measures \(g_\mu\mu_S\) and \(g_\nu\nu_S\),
gives

\[
\int |g_\mu(s)-g_\nu(s)|\,\mu_S(ds)
 \le 2\|\mu-\nu\|_{\rm TV}.
\tag{1.4}
\]

This is convergence of the conditional calibration curve integrated under
the actual score law. It does not assert pointwise convergence at every
score.

## 2. A deterministic Gaussian smoothing theorem

All norms on derivatives in this section are uniform over
\(x\in\mathbb R^d\). A Hilbert--Schmidt norm is denoted by
\(\|\cdot\|_{\rm HS}\).

**Theorem 2.1 (joint TV approximation with matched covariance).**
Let \(f_d:\mathbb R^d\to\mathbb R\) be smooth, odd functions, and let
\(X_d\sim N(0,I_d)\). Suppose, for fixed finite \(L,H\),

\[
\|\nabla f_d\|\le L,\qquad
\|\nabla^2 f_d\|_{\rm HS}\le H,\qquad
\|\nabla^2 f_d\|_{\rm op}\le\varepsilon_d\longrightarrow0.
\tag{2.1}
\]

Put

\[
A_d=\mathbb E[Z_df_d(X_d)],\quad
Q_d=\mathbb E f_d(X_d)^2,\quad
\delta_d=Q_d-A_d^2,
\quad Z_d=\theta_d^\top X_d.
\]

If \(\delta_d\ge\delta_*>0\), then

\[
\left\|\mathcal L(Z_d,f_d(X_d))-
 N\!\left(0,\begin{pmatrix}1&A_d\\A_d&Q_d\end{pmatrix}\right)
\right\|_{\rm TV}\longrightarrow0.
\tag{2.2}
\]

The covariance need not converge. In particular, if the pair converges
weakly to a nonsingular centered Gaussian with covariance
\(\left(\begin{smallmatrix}1&A\\A&Q\end{smallmatrix}\right)\), then
its convergence is in total variation.

The proof has two separate parts: weak Gaussian approximation from the
small Hessian operator norm, and a smoothing estimate using the bounded
Hessian Hilbert--Schmidt norm. Supplying both is necessary for a joint TV
conclusion.

### 2.1 Self-contained weak Gaussian approximation

For a centered smooth Gaussian functional \(f(X)\), define the
Ornstein--Uhlenbeck semigroup

\[
P_tf(x)=\mathbb E f(e^{-t}x+\sqrt{1-e^{-2t}}X'),
\qquad
U_f(x)=\int_0^\infty e^{-t}P_t\nabla f(x)\,dt.
\]

Gaussian integration by parts and the semigroup generator give the
covariance identity

\[
\mathbb E[f(X)h(X)]
 =\mathbb E[U_f(X)\cdot\nabla h(X)].
\tag{2.3}
\]

For completeness, \(f-\mathbb Ef=-\int_0^\infty\partial_tP_tf\,dt\).
The generator is \(\mathcal L=\Delta-x\cdot\nabla\), and
\(-\mathbb E[(\mathcal Lg)h]=\mathbb E\nabla g\cdot\nabla h\).
Also \(\nabla P_tf=e^{-t}P_t\nabla f\). Substitution proves (2.3).
The bounded derivative assumptions, Gaussian moments, and an initial
truncation justify these integrations for the functions used here.

If \(\|\nabla f\|\le L_f\) and
\(\|\nabla^2f\|_{\rm op}\le\varepsilon_f\), then

\[
\|U_f\|\le L_f,\qquad
\|DU_f\|_{\rm op}
 =\left\|\int_0^\infty e^{-2t}P_t\nabla^2f\,dt\right\|_{\rm op}
 \le\varepsilon_f/2.
\]

Set \(T_f=\nabla f\cdot U_f\). Equation (2.3), with \(h=f\), gives
\(\mathbb ET_f=\operatorname{Var}(f(X))=:v_f\). Moreover

\[
\|\nabla T_f\|
 \le\tfrac32 L_f\varepsilon_f,
\qquad
\operatorname{Var}(T_f)
 \le\tfrac94 L_f^2\varepsilon_f^2
\tag{2.4}
\]

by Gaussian Poincare. Apply (2.3) to \(h=e^{itf}\). The characteristic
function \(\chi_f(t)=\mathbb E e^{itf}\) satisfies

\[
\chi_f'(t)=-t v_f\chi_f(t)
           -t\mathbb E[(T_f-v_f)e^{itf}].
\]

Solving this scalar differential equation and using (2.4) gives

\[
|\chi_f(t)-e^{-v_ft^2/2}|
 \le\tfrac34 L_f\varepsilon_f t^2.
\tag{2.5}
\]

Apply (2.5) to \(f=uZ_d+v f_d(X_d)\), whose gradient is bounded by
\(|u|+|v|L\) and Hessian operator norm by \(|v|\varepsilon_d\).
Along every subsequence where \((A_d,Q_d)\to(A,Q)\), it follows that
\((Z_d,f_d(X_d))\) converges weakly to the Gaussian with that covariance.
Such covariance-convergent subsequences exist because Poincare gives
\(Q_d\le L^2\), and \(|A_d|\le L\).

This derivation uses no independence of feature coordinates and no
assumed random-feature Gaussian equivalence.

### 2.2 A nondegenerate Gaussian derivative matrix with high probability

Temporarily suppress the dimension subscript. Write

\[
g=\nabla f,\quad J=\nabla^2f,\quad
P=I-\theta\theta^\top,\quad q=Pg,\quad
\Delta=\|q\|^2.
\]

The determinant of the Gaussian derivative Gram matrix of \((Z,f)\) is
exactly \(\Delta\). Let \(a=\theta\cdot g\). Gaussian integration by
parts gives \(\mathbb Ea=A\), while Poincare gives

\[
\operatorname{Var}(a)\le\mathbb E\|J\theta\|^2
 \le\varepsilon^2.
\]

Using Poincare again for \(f\),

\[
\mathbb E\Delta
 =\mathbb E\|g\|^2-\mathbb Ea^2
 \ge Q-A^2-\varepsilon^2.
\tag{2.6}
\]

Also \(\nabla\Delta=2Jq\), so

\[
\operatorname{Var}(\Delta)
 \le 4L^2\varepsilon^2.
\tag{2.7}
\]

If \(Q-A^2\ge\delta_*\), equations (2.6)--(2.7) imply

\[
\Pr\{\Delta\le\delta_*/4\}=o(1).
\tag{2.8}
\]

For example, when \(\varepsilon^2\le\delta_*/4\), the left side is at
most \(16L^2\varepsilon^2/\delta_*^2\), since
\(\mathbb E\Delta-\delta_*/4\ge\delta_*/2\).

Thus one needs neither a pointwise lower bound on \(\Delta\) nor inverse
moments of \(\Delta\) over its entire distribution.

### 2.3 Localized integration by parts and the smoothing estimate

Choose a fixed smooth \(\chi:[0,\infty)\to[0,1]\) equal to zero on
\([0,\delta_*/8]\) and to one on \([\delta_*/4,\infty)\). On
\(\Delta>0\) define

\[
v_2=\frac q\Delta,\qquad
v_1=\theta-a v_2.
\]

They obey

\[
\theta\cdot v_1=1,\quad g\cdot v_1=0,
\qquad
\theta\cdot v_2=0,\quad g\cdot v_2=1.
\tag{2.9}
\]

Set \(V_i=\chi(\Delta)v_i\), extended by zero on the region where the
cutoff vanishes. These are globally smooth vector fields. On the support
of the cutoff, \(\Delta\ge\delta_*/8\). The bounds

\[
\|v_2\|=\Delta^{-1/2},\qquad
\|Dv_2\|_{\rm HS}
 \le\frac{\|J\|_{\rm HS}}\Delta
       +\frac{\|q\|\|\nabla\Delta\|}{\Delta^2}
 \le\frac{3H}\Delta
\]

and \(|a|\le L\), \(\|\nabla a\|\le H\), together with the cutoff
derivative bound, imply

\[
\|V_i\|+\|DV_i\|_{\rm HS}
 \le C(L,H,\delta_*),\qquad i=1,2.
\tag{2.10}
\]

The constant is independent of input dimension. No trace-of-Hessian bound
is used here.

For a vector field \(V\), its Gaussian divergence is
\(\mathfrak d(V)=X\cdot V-\operatorname{div}V\). Two Gaussian
integrations by parts give

\[
\mathbb E\mathfrak d(V)^2
 =\mathbb E\|V\|^2
   +\mathbb E\sum_{i,j}(\partial_iV_j)(\partial_jV_i)
 \le\mathbb E\|V\|^2+\mathbb E\|DV\|_{\rm HS}^2.
\tag{2.11}
\]

This identity can first be proved for smooth truncated fields and then
extended by Gaussian Sobolev approximation; (2.10) supplies the required
integrability. In particular its bound is dimension-free, although the
two terms defining \(\mathfrak d(V)\) separately need not be.

For \(\psi\in C_c^\infty(\mathbb R^2)\), (2.9) and integration by parts
yield

\[
\mathbb E[\chi(\Delta)\,\partial_i\psi(Z,f)]
 =\mathbb E[\psi(Z,f)\mathfrak d(V_i)].
\tag{2.12}
\]

Therefore the positive subprobability measure

\[
\eta(B)=\mathbb E[\chi(\Delta)\mathbf1_{\{(Z,f)\in B\}}]
\]

has distributional first derivatives with total-variation norms bounded
by \(C(L,H,\delta_*)\). More directly, integrate
\(\psi(x+h)-\psi(x)\) along the segment from \(x\) to \(x+h\) and use
(2.12). Taking the supremum over smooth bounded test functions gives

\[
\|\tau_h\eta-\eta\|_{\rm TV}\le C\|h\|.
\tag{2.13}
\]

The same supremum equals the total-variation norm for finite regular
Borel measures; smooth approximation of continuous compactly supported
tests justifies this step.

Let \(\rho_r\) be a nonnegative smooth probability mollifier on
\(\mathbb R^2\), supported in a ball of radius \(r\). Integrating
(2.13) against the mollifier and writing \(\mu=\mathcal L(Z,f)\) gives

\[
\begin{aligned}
\|\mu-\mu*\rho_r\|_{\rm TV}
&\le2\|\mu-\eta\|_{\rm TV}
       +\|\eta-\eta*\rho_r\|_{\rm TV}\\
&\le2\mathbb E[1-\chi(\Delta)]+Cr
 =o(1)+Cr.
\end{aligned}
\tag{2.14}
\]

This is the required uniform regularization estimate for the joint law.

### 2.4 Completing the TV proof

Pass to any subsequence along which \((A_d,Q_d)\to(A,Q)\). Its Gaussian
covariance is nonsingular because \(Q-A^2\ge\delta_*\). Section 2.1
gives \(\mu_d\Rightarrow G_{A,Q}\). For fixed \(r>0\), convolution
densities \(\mu_d*\rho_r\) converge pointwise to
\(G_{A,Q}*\rho_r\), since the translated mollifier is a bounded
continuous test function. All these nonnegative densities have mass one,
so Scheffe's argument gives convergence in \(L^1\), equivalently TV.
The elementary argument is
\(\int|p_d-p|=2-2\int\min(p_d,p)\to0\), by dominated convergence
for the minimum.

Use (2.14), this fixed-\(r\) convergence, and
\(\|G_{A,Q}-G_{A,Q}*\rho_r\|_{\rm TV}\to0\) as \(r\downarrow0\).
First taking the dimension limit and then \(r\downarrow0\) proves
\(\|\mu_d-G_{A,Q}\|_{\rm TV}\to0\).
Gaussian densities with converging nonsingular covariance matrices also
converge pointwise and in \(L^1\), so
\(\|G_{A_d,Q_d}-G_{A,Q}\|_{\rm TV}\to0\). The triangle inequality
proves (2.2) on this subsequence. Compactness of the covariance parameters
then proves (2.2) for the whole sequence. This completes Theorem 2.1.

For the last assertion of the theorem, bounded gradients and oddness
give the uniform fourth-moment bound
\(\mathbb E f_d^4\le5L^4\): apply Poincare to \(f_d^2\) and use
\(\mathbb E f_d^2\le L^2\). Hence a weak limit gives convergence of
\(A_d,Q_d\) to \(A,Q\), and \(Q>A^2\) supplies \(\delta_*>0\)
eventually.

## 3. Structural theorem for trained random-feature readouts

Let \(F_d\) have rows \(W_j^\top\), and, conditional on an arbitrary
environment containing \((F_d,b_d)\), let

\[
f_d(x)=\sum_{j=1}^m b_{d,j}\tanh(W_j^\top x).
\tag{3.1}
\]

There is **no independence assumption between the trained \(b_d\) and
the features or training sample**. The fresh input remains independent
of the environment.

Writing \(J_2=\sup_u|\tanh''u|\le2\), the exact derivative bounds are

\[
\begin{aligned}
\|\nabla f_d\|
 &\le\|F_d\|_{\rm op}\|b_d\|_2,\\
\|\nabla^2f_d\|_{\rm op}
 &\le J_2\|F_d\|_{\rm op}^2\|b_d\|_\infty,\\
\|\nabla^2f_d\|_{\rm HS}
 &\le J_2\|F_d\|_{\rm op}^2\|b_d\|_2.
\end{aligned}
\tag{3.2}
\]

For the last inequality use
\(\nabla^2 f_d=F_d^\top\operatorname{diag}
(b_{d,j}\tanh''(W_j^\top x))F_d\) and
\(\|ABC\|_{\rm HS}\le\|A\|_{\rm op}\|B\|_{\rm HS}\|C\|_{\rm op}\).

Let

\[
A_d=\mathbb E_X[Zf_d(X)\mid\mathcal E_d],\quad
Q_d=\mathbb E_X[f_d(X)^2\mid\mathcal E_d],\quad
\delta_d=Q_d-A_d^2.
\tag{3.3}
\]

**Corollary 3.1 (conditional matched-Gaussian TV).** If

\[
\|F_d\|_{\rm op}=O_P(1),\qquad
\|b_d\|_2=O_P(1),\qquad
\|b_d\|_\infty\to0\text{ in probability},\qquad
\delta_d^{-1}=O_P(1),
\tag{3.4}
\]

then, writing \(\mu_d=\mathcal L_X(Z,f_d(X)\mid\mathcal E_d)\),

\[
\|\mu_d-G_{A_d,Q_d}\|_{\rm TV}\to0
\quad\text{in probability and every finite }L^p.
\tag{3.5}
\]

Here \(\delta_d^{-1}=O_P(1)\) includes positivity with probability
tending to one; values on a vanishing exceptional event can be assigned
arbitrarily. The \(L^p\) conclusion uses the bound of two for TV.

To justify the use of deterministic Theorem 2.1 with random environments,
first restrict to events with fixed bounds on
\(\|F_d\|_{\rm op},\|b_d\|_2,\delta_d^{-1}\). The deterministic
convergence is uniform in the sequential sense on each such bounded
class: if uniformity failed, choose one violating deterministic
environment at each dimension and contradict Theorem 2.1. The
\(O_P(1)\) assumptions make the complementary probabilities arbitrarily
small. Finally use \(\|b_d\|_\infty\to0\). No almost-sure boundedness
of the sequence of random environments is assumed.

The same reasoning gives a direct transfer version: if the first three
conditions in (3.4) hold and the conditional law of \((Z,f_d(X))\)
converges weakly in probability to a fixed nonsingular Gaussian, then
its convergence is in TV in probability. Uniform fourth moments on each
bounded environment event give convergence of the covariances, as in
the last paragraph of Section 2.

### 3.1 RF covariance, relative delocalization, and nondegeneracy

For Gaussian rows \(W_j\sim N(0,I_d/d)\), define

\[
a_1=\mathbb E[G\tanh G],\quad v=\mathbb E\tanh^2G,
\quad\nu=v-a_1^2>0.
\]

Strict positivity holds by the strict Cauchy--Schwarz inequality, since
\(\tanh G\) is not a multiple of \(G\) almost surely. Put
\(q_j=\|W_j\|^2\),
\(D_A=\operatorname{diag}(\mathbb E\tanh'(\sqrt{q_j}G))\), and
\(\Sigma_F=\mathbb E_X[h(X)h(X)^\top]\). The exact first-Hermite
decomposition and the already audited operator lemma give

\[
\Sigma_F=D_AFF^\top D_A+D_R+E_F,
\quad \|D_R-\nu I\|_{\rm op}\to0,
\quad\|E_F\|_{\rm op}\to0
\tag{3.6}
\]

in probability, when \(m/d\to\gamma\in(0,\infty)\). Here
\((D_R)_{jj}=\mathbb E\tanh^2(\sqrt{q_j}G)-q_j(D_A)_{jj}^2\).
The off-diagonal remainder obeys the cubic Hermite bound, whose squared
Frobenius expectation is \(O(d^{-1})\); row-norm concentration handles
the diagonal.

Gaussian integration by parts gives the exact covariance
\(A_d=\theta^\top F^\top D_A b_d\). Thus, uniformly over all readout
vectors, including data-dependent vectors,

\[
\begin{aligned}
Q_d-A_d^2
 &=\|(I-\theta\theta^\top)F^\top D_A b_d\|^2
   +b_d^\top(D_R+E_F)b_d\\
 &\ge (\nu-o_P(1))\|b_d\|_2^2.
\end{aligned}
\tag{3.7}
\]

In particular, a norm bounded away from zero supplies the last condition
of (3.4). There is also a scale-free alternative: if

\[
\Pr\{b_d=0\}\to0,\qquad
\frac{\|b_d\|_\infty}{\|b_d\|_2}\to0
\quad\text{in probability},
\tag{3.8}
\]

retain \(\|F_d\|_{\rm op}=O_P(1)\), which the Gaussian-row hypothesis
supplies, and normalize the score by \(\|b_d\|_2\). Its coefficient norm is one and
(3.7) gives a residual variance at least \(\nu/2\) with probability
tending to one. Corollary 3.1 applies to the normalized score. The
invertible, environment-dependent rescaling of its second coordinate
preserves TV, proving (3.5) for the original score as well. This variant
does not require its raw variance to stay bounded away from zero.

Absolute coefficient delocalization alone cannot be silently substituted
for relative delocalization when the whole coefficient vector vanishes.
At exactly zero score the conditioning sigma-field changes, so this is a
substantive distinction for calibration.

## 4. Exact first-step closure

Use the previously audited model and normalization:

\[
n/d\to\alpha>0,\quad m/d\to\gamma>0,\quad
R_i=Y_i-\tfrac12,\quad
b_{d,j}=\frac{cd}{nm}\sum_{i=1}^n R_i\tanh(W_j^\top X_i),
\qquad c>0.
\tag{4.1}
\]

Thus \(S_{1,d}(X)=\sum_j b_{d,j}\tanh(W_j^\top X)\) is exactly the
one-step score in the original proof. The coefficient here is the raw
readout coefficient \(b_j=a_j^1/\sqrt m\), not the differently scaled
network parameter \(a_j^1\).

### 4.1 Coefficient delocalization is proved directly

Let

\[
B(w)=\mathbb E[(\sigma(\beta Z)-\tfrac12)\tanh(w^\top X)].
\]

Gaussian covariance interpolation, or integration of its elementary
Gaussian integration-by-parts derivative, gives

\[
|B(w)|\le\frac\beta4|\theta^\top w|.
\tag{4.2}
\]

Indeed the derivatives of the teacher mean and tanh have bounds
\(\beta/4\) and one, while their Gaussian cross-covariance is
\(\theta^\top w\). This also covers \(\beta=0\).

Conditional on \(F\), for each fixed \(j\), the summands
\(R_i\tanh(W_j^\top X_i)\) are independent and lie in
\([-1/2,1/2]\), with mean \(B(W_j)\). Hoeffding and a union bound over
\(m=O(d)\) coordinates give

\[
\max_j\left|
 \frac1n\sum_iR_i\tanh(W_j^\top X_i)-B(W_j)
\right|=O_P\!\left(\sqrt{\frac{\log d}{n}}\right).
\]

The scalar variables \(\theta^\top W_j\) are iid \(N(0,1/d)\), so
(4.2) and (4.1) imply

\[
\boxed{\quad
\|b_d\|_\infty
 =O_P\!\left(\sqrt{\frac{\log d}{d}}\right)\longrightarrow0.
\quad}
\tag{4.3}
\]

No coordinate independence of the training features is needed for that
union bound. Moreover conditional variance plus squared mean gives

\[
\mathbb E\|b_d\|_2^2
 \le\frac{c^2d^2}{m^2}
    \left\{\frac m{4n}+\frac{\beta^2m}{16d}\right\}
 =O(1).
\tag{4.4}
\]

Therefore \(\|b_d\|_2=O_P(1)\). The elementary Gaussian matrix norm
bound supplies \(\|F\|_{\rm op}=O_P(1)\).

### 4.2 The audited replica result supplies the deterministic target

Use the original constants

\[
\kappa=\mathbb E[G\{\sigma(\beta G)-\tfrac12\}],\qquad
\tau^2=\frac{\kappa^2a_1^2v}{\gamma}
       +\frac{a_1^4+v^2/\gamma}{4\alpha},
\]

and put

\[
A=ca_1^2\kappa,\qquad Q=A^2+c^2\tau^2,
\qquad S_\infty=AZ+c\tau G,
\tag{4.5}
\]

with independent standard normal \(Z,G\). In particular
\(Q-A^2=c^2\tau^2>0\) for every fixed \(c>0\), including
\(\beta=0\).

The audited one-test/two-test theorem proves, for each fixed bounded
continuous \(h:\mathbb R^2\to\mathbb R\),

\[
\int h\,d\mu_d\longrightarrow\mathbb Eh(Z,S_\infty)
\quad\text{in }L^2\text{ over }\mathcal E_d.
\tag{4.6}
\]

This implies weak convergence of the random measures in probability.
An elementary verification restricts bounded Lipschitz functions to a
large compact square, takes a finite uniform net there, and controls the
outside mass with continuous cutoff functions. The finitely many tests
then use (4.6). Equivalently, any metric for weak convergence tends to
zero in probability. This step does not itself claim TV.

Now (4.3)--(4.4), the matrix norm bound, and the transfer version of
Corollary 3.1 yield the genuinely stronger result

\[
\boxed{\quad
\left\|\mathcal L_X(Z,S_{1,d}(X)\mid\mathcal E_d)
             -\mathcal L(Z,S_\infty)\right\|_{\rm TV}
 \longrightarrow0
\quad\text{in probability and every finite }L^p.
\quad}
\tag{4.7}
\]

Fresh labels can be appended by the common Markov kernel
\(Y\mid Z\sim\operatorname{Bernoulli}(\sigma(\beta Z))\); applying a
Markov kernel contracts TV. Predictions \(\sigma(S)\) can also be
appended or substituted by measurable pushforward.

### 4.3 Exact calibration and the integrated regression curve

For the Gaussian target define the everywhere continuous function

\[
g_\infty(s)
 =\mathbb E_H\sigma\!\left(\beta\left[
    \frac A Qs+\sqrt{1-\frac{A^2}Q}\,H\right]\right).
\tag{4.8}
\]

Let \(g_d(s)=\mathbb E[Y\mid S_{1,d}=s,\mathcal E_d]\) be any
regular conditional version. Equations (1.3)--(1.4) and (4.7) prove

\[
\boxed{\quad
\operatorname{CE}_d
 \longrightarrow
 \mathbb E|g_\infty(S_\infty)-\sigma(S_\infty)|
 \quad\text{in probability and every finite }L^p.
\quad}
\tag{4.9}
\]

They also prove

\[
\mathbb E_X\bigl[
 |g_d(S_{1,d})-g_\infty(S_{1,d})|\mid\mathcal E_d\bigr]
 \longrightarrow0
\tag{4.10}
\]

in probability and every finite \(L^p\). Boundedness by one supplies
these \(L^p\) upgrades. This closes the precise first-step upper-bound gap
left open in the earlier files; their lower bounds and scalar Gaussian
consequences remain valid, and now have an exact CE limit.

No almost-sure quenched convergence, uniform-in-score curve convergence,
dimension-dependent step choice, or multi-step state evolution is
deduced from (4.7)--(4.10).

## 5. Later fixed-time readouts: exact Gaussian calibration proxy

For \(Q>A^2\), define the deterministic scalar functional

\[
C_\beta(A,Q)=\mathbb E_T\left|
 \mathbb E_H\sigma\!\left(\beta\left[
 \frac A{\sqrt Q}T+\sqrt{1-\frac{A^2}Q}\,H\right]\right)
 -\sigma(\sqrt Q\,T)\right|,
\tag{5.1}
\]

where \(T,H\) are independent standard normals. Corollary 3.1 and
(1.3) immediately imply

\[
\operatorname{CE}_d-C_\beta(A_d,Q_d)\longrightarrow0
\quad\text{in probability and every finite }L^p.
\tag{5.2}
\]

This is an exact calibration approximation for the original trained
network with its own conditional covariance, not calibration under a
different training distribution. It holds for any fixed training time
whose coefficients satisfy (3.4), or the relative variant (3.8).

If additionally \(A_d\to A\) and \(Q_d\to Q>A^2\) in probability,
bounded convergence in (5.1) gives the deterministic exact limit
\(\operatorname{CE}_d\to C_\beta(A,Q)\). This explicitly identifies
what a later-time overlap or DMFT theorem must provide.

The companion analysis `b03_gaussian_dynamics.md`, Theorem 1, proves
fixed-horizon coefficient norm bounds and coordinate delocalization for
actual output-layer GD by a leave-one-feature argument. These facts
combine with this theorem without independence between coefficients and
features. B03 Proposition 3 supplies a direct small-step nondegeneracy
condition. The subsequent deterministic state-evolution proof in
`b04_state_evolution_audit.md`, Lemma 4.1 and Theorem 1, supplies
nondegeneracy at every fixed positive time for every fixed positive step
constant, as well as the deterministic overlap limits. Absolute
coordinate delocalization by itself would still not prove nondegeneracy.

### 5.1 Risk also has a covariance proxy

On events with bounded \(\|F\|_{\rm op}\|b_d\|_2\), Gaussian
Poincare and oddness bound the score second moment uniformly. Truncate
logistic loss, use (3.5) for the bounded truncation, then let the
truncation level grow. The upper bound
\(0\le\ell(Y,S)\le\log2+|S|\) makes the tail uniformly small on
these events. Localization therefore proves

\[
L_d-\left\{
 \mathbb E_T\log\bigl(2\cosh(\sqrt{Q_d}T/2)\bigr)
 -\kappa A_d\right\}\longrightarrow0
\quad\text{in probability}.
\tag{5.3}
\]

The Gaussian formula uses
\(\mathbb E[S\sigma(\beta Z)]=A_d\mathbb E[Z\sigma(\beta Z)]
=\kappa A_d\). An \(L^1\) conclusion for (5.3) needs unconditional
uniform integrability; it is not inferred from \(O_P(1)\) bounds alone.

### 5.2 Positive calibration without deterministic overlap convergence

For every \(\beta\ge0\), \(Q>A^2\), and \(Q>0\),

\[
C_\beta(A,Q)>0.
\tag{5.4}
\]

If \(\beta=0\) or \(A=0\), the conditional teacher mean is \(1/2\),
while \(\sigma(S)\) is nonconstant. If \(\beta>0,A<0\), the former
mean is strictly decreasing in the score whereas the prediction is
strictly increasing. If \(\beta>0,A>0\), write the former mean as

\[
g(s)=\mathbb E_H\sigma(\lambda s+rH),\quad
\lambda=\beta A/Q>0,\quad r=\beta\sqrt{1-A^2/Q}>0.
\]

If calibration held, continuity and positivity of the Gaussian density
would imply \(g(s)=\sigma(s)\) for every real \(s\). But dominated
convergence gives

\[
e^{\lambda s}(1-g(s))\longrightarrow e^{r^2/2}
\quad(s\to+\infty).
\]

Comparison with the logistic tail first forces \(\lambda=1\), then
\(e^{r^2/2}=1\), a contradiction.

The map \(C_\beta\) is continuous on the region \(Q>A^2\). Hence for
each fixed \(0<\delta_*\le Q_*<\infty\),

\[
c_*(\beta,\delta_*,Q_*)
 :=\min_{\substack{Q\le Q_*\\Q-A^2\ge\delta_*}}
 C_\beta(A,Q)>0.
\tag{5.5}
\]

The set is compact and \(Q\ge\delta_*\). Therefore if a finite
collection of trained times satisfies common deterministic upper and
lower covariance bounds with probability tending to one, as well as
the hypotheses of Corollary 3.1, then

\[
\Pr\left\{\min_{1\le t\le T}\operatorname{CE}_{t,d}
                    \ge c_*/2\right\}\longrightarrow1.
\tag{5.6}
\]

A union bound over the fixed number of times suffices. Deterministic
overlap convergence is unnecessary for this qualitative conclusion.
It is still necessary for an explicit deterministic trajectory of risk
and calibration, unless another argument identifies those functionals
without identifying the overlaps.

## 6. Relation to primary literature and acceptance boundary

The small-Hessian Gaussian approximation is the mechanism of second-order
Gaussian Poincare inequalities. A primary source is Sourav Chatterjee,
[*Fluctuations of eigenvalues and second order Poincare inequalities*](https://arxiv.org/abs/0705.1224),
*Probability Theory and Related Fields* 143 (2009), 1--40. The joint
regularization mechanism is related to Vlad Bally, Lucia Caramellino,
and Guillaume Poly,
[*Regularization lemmas and convergence in total variation*](https://arxiv.org/abs/1907.12328),
*Electronic Journal of Probability* 25 (2020), paper 74. Both original
papers were consulted as checks on the mechanism. The precise
dimension-free estimates and RF specialization needed here are proved
in Sections 2--4 rather than imported through an unchecked theorem.

| Claim | Status in this note |
|---|---|
| Small-Hessian weak Gaussian approximation | Proved by OU covariance identity and a characteristic-function equation. |
| Joint weak-to-TV upgrade | Proved by determinant concentration, localized Gaussian integration by parts, and fixed-scale convolution. |
| First-step output-coefficient bounds | Proved directly by conditional Hoeffding and a second-moment estimate. |
| Exact first-step model-conditional CE limit | Proved, using the separately audited replica CLT. |
| Integrated first-step calibration-curve convergence | Proved. |
| Matched-Gaussian exact-CE proxy for arbitrary trained readouts | Proved under the displayed delocalization and nondegeneracy conditions. |
| Application to every fixed GD time | Established by combining this transfer with B03's coefficient bounds and the subsequent state-evolution theorem. |
| Deterministic later-time overlaps / fixed-horizon RF state evolution | Proved separately in `b01_GD_state_evolution_check.md` and audited in `b04_state_evolution_audit.md`, using B03's matrix and algorithmic reduction. |
| A whole-trajectory or global early-stopping theorem | Not claimed from this transfer theorem. |

The categorical examples are not used anywhere in this proof.


---

# Appendix D: Uniform-time GD and stopping rules

Source module: `b02_uniform_time_GD.md`. SHA-256: `1102592bcfdc5b3b9b82476b7d6065b7f0c596f3f6b14b05d1362637f104483f`.

# Uniform-in-time logistic GD for Gaussian tanh random features

Author: B02. Date: 2026-10-24. This is new work under `fullproof/`; no frozen file is modified.

**Status.** The coercivity, curvature, MLE, and uniform-in-time delocalization results below are proved directly. They apply when the fixed sample-to-width ratio is sufficiently large and the fixed positive step is sufficiently small. With B04's independently audited total-variation transfer theorem, they give a calibration floor simultaneously at every positive training time, including the MLE and arbitrary data-dependent positive stopping times. A deterministic calibration curve additionally needs the finite-time deterministic overlaps. Section 9 states exactly how such overlaps, once proved, extend uniformly to all times. This note does not silently assume that separate state-evolution theorem.

## 1. Model, constants, and theorem

Let
\[
X_i\stackrel{\mathrm{iid}}\sim N(0,I_d),\qquad
Y_i\mid X_i\sim\operatorname{Bernoulli}(\sigma(\beta\theta^\top X_i)),
\quad \|\theta\|=1,
\]
with conditionally independent labels, fixed finite \(\beta\geq0\), and \(\sigma(u)=(1+e^{-u})^{-1}\). Independently, the rows of \(F\in\mathbb R^{m\times d}\) are \(W_j\sim N(0,I_d/d)\). Put
\[
h(x)=\tanh(Fx),\quad H_{ij}=h_j(X_i),\quad
\mathcal L_n(b)=\frac1n\sum_{i=1}^n
 \big\{\log(1+e^{h(X_i)^\top b})-Y_i h(X_i)^\top b\big\}.
\tag{1.1}
\]
Assume \(n/d\to\alpha>0\), \(m/d\to\gamma>0\). The raw score is \(b^\top h(x)\); in the alternative network notation \(b=a/\sqrt m\). The GD update in the other notes is exactly
\[
b^0=0,\qquad b^{t+1}=b^t-\eta_d\nabla\mathcal L_n(b^t),
\qquad \eta_d=\frac{cd}{m}.
\tag{1.2}
\]

Here are explicit, deliberately conservative constants. For \(G\sim N(0,1)\), define
\[
a_1=\mathbb E[G\tanh G],\quad v=\mathbb E\tanh^2G,
\quad \nu=v-a_1^2>0.
\]
Choose any deterministic \(L\) for which \(\|F\|_{\mathrm{op}}\leq L\) with probability tending to one. The elementary Gaussian net bound permits, for example,
\[
L=8\sqrt{1+\gamma}.
\]
Set
\[
s=\nu/2,\qquad \kappa=\sqrt{s/2},\qquad
p_0=\frac{s^2}{20L^4},\qquad
B=\sqrt{2\log(4/p_0)},
\]
\[
q_\beta=\sigma(-\beta B),\quad
p_1=q_\beta p_0/2,\quad
\mathfrak a=\kappa p_1/4,\quad
C_*=\max\left\{1,\left(\frac{32L}{\kappa p_1}\right)^2\right\}.
\tag{1.3}
\]
The ratio and step assumptions for this note are
\[
\boxed{\quad\alpha/\gamma>C_*,\qquad
0<c<\frac{\gamma}{2\Lambda},\quad
\Lambda=16L^2.\quad}
\tag{1.4}
\]
These define a nonempty proportional regime for each fixed \(\beta,\gamma\). No assertion that these thresholds are sharp is made.

Further set
\[
R_0=\frac{\log2}{\mathfrak a},\quad R=2R_0,
\quad C_H=64L^2,\quad \delta=p_0/4,
\quad M=R\sqrt{C_H/\delta},
\]
\[
\chi=\frac{\kappa^2p_0}{16},\qquad
\mu=\chi\sigma'(M)>0,\qquad
\eta_-=\frac{c}{2\gamma},\qquad q=1-\eta_-\mu\in(0,1).
\tag{1.5}
\]
All these constants are independent of \(d\), although some are very small or very large.

**Theorem 1 (whole GD trajectory).** Under (1.4), with probability tending to one:

1. \(\mathcal L_n(b)\geq\mathfrak a\|b\|\) for every \(b\in\mathbb R^m\). There is a unique finite unregularized MLE \(b^*\), with \(\|b^*\|\leq R_0\).
2. Every GD iterate and every feature-deleted GD iterate defined in Section 6 lies in \(\{\|b\|\leq R_0\}\). On the larger ball \(\{\|b\|\leq R\}\),
   \[
   \mu I\preceq\nabla^2\mathcal L_n(b)\preceq\Lambda I.
   \tag{1.6}
   \]
3. For every integer \(t\geq0\), simultaneously,
   \[
   \|b^t-b^*\|\leq R_0q^t.
   \tag{1.7}
   \]
4. The MLE and the whole trajectory are delocalized:
   \[
   \|b^*\|_\infty+\sup_{t\geq0}\|b^t\|_\infty
      =O_P\!\left(\sqrt{\frac{\log d}{d}}\right).
   \tag{1.8}
   \]
5. For a deterministic \(r_*>0\),
   \[
   \inf_{t\geq1}\|b^t\|\geq r_*,\qquad \|b^*\|\geq r_*
   \tag{1.9}
   \]
   with probability tending to one. One permissible choice is
   \[
   r_* =\frac c4\sqrt{\frac{v\rho_\beta}{\alpha\gamma}},
   \qquad \rho_\beta=\mathbb E\sigma'(\beta G)>0.
   \tag{1.10}
   \]

The label mechanism is not independent of the feature vector after conditioning on \(F\). The proof below does not make that assumption.

## 2. The good feature event

Write \(\Sigma_F=\mathbb E_X h(X)h(X)^\top\) and
\(g_F=\mathbb E_X[(\theta^\top X)h(X)]\). There is an event \(\mathcal F_d\), depending only on \(F\), on which
\[
\|F\|_{\mathrm{op}}\leq L,\qquad
\Sigma_F\succeq sI,\qquad
\Sigma_F-g_Fg_F^\top\succeq sI,
\tag{2.1}
\]
with \(\mathbb P(\mathcal F_d^c)=O(d^{-1})+O(de^{-c_Fd})\) for some fixed \(c_F>0\). Constants in probability estimates may depend on fixed model parameters.

For completeness, the covariance claim follows directly from Hermite expansion. Put \(q_j=\|W_j\|^2\),
\(A(q)=\mathbb E\tanh'(\sqrt qG)\), and \(D_A=\operatorname{diag}(A(q_j))\). Oddness gives only odd Hermite coefficients, and Gaussian integration by parts identifies the linear coefficient. Thus
\[
\Sigma_F=D_AFF^\top D_A+D_\nu+E,
\quad (D_\nu)_{jj}=\mathbb E\tanh^2(\sqrt{q_j}G)-q_jA(q_j)^2,
\tag{2.2}
\]
where \(E_{jj}=0\) and, for \(j\ne k\),
\[
|E_{jk}|\leq |\rho_{jk}|^3,\qquad
\rho_{jk}=\frac{W_j^\top W_k}{\|W_j\|\|W_k\|}.
\tag{2.3}
\]
Indeed, Cauchy--Schwarz on the Hermite coefficients of degree at least three bounds their sum by \(|\rho_{jk}|^3\), since tanh has second moment at most one. Independent Gaussian directions give
\[
\mathbb E\|E\|_F^2\leq
\frac{15m(m-1)}{d(d+2)(d+4)}=O(d^{-1}).
\tag{2.4}
\]
Uniform concentration of \(q_j\) around one and continuity give \(\min_j(D_\nu)_{jj}\geq3\nu/4\) except on an exponentially unlikely event. Markov's inequality gives \(\|E\|_{\mathrm{op}}\leq\nu/4\) with failure \(O(d^{-1})\). Also
\[
g_F=D_AF\theta,
\quad
\Sigma_F-g_Fg_F^\top
=D_AF(I-\theta\theta^\top)F^\top D_A+D_\nu+E\succeq sI.
\tag{2.5}
\]
The operator norm bound follows by a Gaussian sphere-net argument. These observations prove (2.1).

Conditional on \(F\in\mathcal F_d\), for every unit \(u\in\mathbb R^m\), the function \(x\mapsto u^\top h(x)\) is odd and \(L\)-Lipschitz. In particular,
\[
\mathbb E e^{t u^\top h(X)}\leq e^{t^2L^2/2},\qquad
s\leq\mathbb E(u^\top h(X))^2\leq L^2,
\quad
\mathbb E(u^\top h(X))^4\leq5L^4.
\tag{2.6}
\]
The fourth-moment bound follows from Gaussian Poincare applied first to the centered function and then to its square:
\(\mathbb E f^4\leq(\mathbb E f^2)^2+4L^2\mathbb E f^2\leq5L^4\).

## 3. Uniform small-ball events and noisy-label coercivity

Everything in this section is conditional on a fixed \(F\in\mathcal F_d\). The pairs \((X_i,Y_i)\) are iid under this conditioning. For each unit \(u\), Paley--Zygmund, or Cauchy--Schwarz applied above the threshold, gives
\[
\mathbb P(|u^\top h(X)|\geq\kappa)\geq p_0.
\tag{3.1}
\]
Let \(Z=\theta^\top X\) and \(T=2Y-1\). The chosen \(B\) has \(\mathbb P(|Z|>B)\leq p_0/2\). On \(|Z|\leq B\), either label has conditional probability at least \(q_\beta\). Therefore
\[
\mathbb P(-T u^\top h(X)\geq\kappa)
\geq q_\beta\mathbb P(|u^\top h(X)|\geq\kappa,|Z|\leq B)
\geq p_1.
\tag{3.2}
\]
This is a conditional-label calculation at each \(X\); it never separates the dependent events involving \(h(X)\) and \(Z\).

Define the bounded cutoff
\[
\psi(x)=
\begin{cases}
0,&x\leq\kappa/2,\\
2x/\kappa-1,&\kappa/2<x<\kappa,\\
1,&x\geq\kappa.
\end{cases}
\tag{3.3}
\]
It is \(2/\kappa\)-Lipschitz and vanishes at zero. For either class
\[
f_u(X,Y)=\psi(-T u^\top h(X)),\qquad
\widetilde f_u(X)=\psi(|u^\top h(X)|),\quad \|u\|=1,
\]
symmetrization and Rademacher contraction give
\[
\mathbb E\sup_{\|u\|=1}|(P_n-P)f_u|
\leq\frac{8}{\kappa}
 \mathbb E\left\|\frac1n\sum_i\epsilon_iT_i h(X_i)\right\|
\leq\frac{8L}{\kappa}\sqrt{\frac mn}.
\tag{3.4}
\]
The same bound holds for \(\widetilde f_u\), with \(T_i\) omitted. The numerical factor eight safely includes the absolute-value form of contraction. The last inequality uses \(T_i^2=1\) and the independent Rademacher signs, not independence of \(T_i\) and \(h(X_i)\).

Since changing one sample changes each supremum by at most \(1/n\), bounded differences imply an upper-tail bound \(e^{-2nz^2}\) above its expectation. If \(n/m\geq C_*\), (3.4) is at most \(p_1/4\). Using \(z=p_1/4\) for the signed class and \(z=p_0/4\) for the unsigned class proves, simultaneously, except with probability
\[
e^{-np_1^2/8}+e^{-np_0^2/8},
\tag{3.5}
\]
that for every unit \(u\),
\[
\frac1n\sum_i\psi(-T_i u^\top h_i)\geq p_1/2,
\qquad
\frac1n\#\{i:|u^\top h_i|>\kappa/2\}\geq p_0/2.
\tag{3.6}
\]
Measurability of the suprema is unproblematic: the cutoff classes are continuous in \(u\), so a countable dense subset of the sphere suffices.

The logistic loss obeys \(\log(1+e^{-Tz})\geq(-Tz)_+\). Also \(x_+\geq(\kappa/2)\psi(x)\). Consequently, for every \(b\ne0\), using \(u=b/\|b\|\),
\[
\mathcal L_n(b)
\geq\|b\|\frac1n\sum_i(-T_i u^\top h_i)_+
\geq\frac{\kappa p_1}{4}\|b\|
=\mathfrak a\|b\|.
\tag{3.7}
\]
The inequality at \(b=0\) is immediate. Thus the entire initial sublevel set \(\{\mathcal L_n\leq\log2\}\) is contained in the deterministic radius-\(R_0\) ball.

## 4. Robust covariance and curvature on the whole ball

The unsigned event in (3.6) gives an arbitrary-deletion bound: for **every** subset \(I\subseteq\{1,\ldots,n\}\) with \(|I^c|\leq\delta n\),
\[
\frac1n\sum_{i\in I}h_i h_i^\top\succeq\chi I_m.
\tag{4.1}
\]
Indeed, for each unit \(u\), at least \(p_0n/2\) rows have \(|u^\top h_i|>\kappa/2\); after arbitrary deletion of at most \(p_0n/4\) rows, at least \(p_0n/4\) remain, contributing at least \(\kappa^2p_0/16\). This proof does not union-bound over subsets and does not assume deleted rows are independent of the data.

We also have, with conditional failure at most \(2e^{-3n}\) when \(n\geq m\),
\[
\|H\|_{\mathrm{op}}\leq8L\sqrt n,
\qquad \frac1nH^\top H\preceq C_H I_m.
\tag{4.2}
\]
For a direct proof, take \(1/4\)-nets of the two unit spheres, of cardinalities at most \(9^n,9^m\). Each bilinear form \(u^\top Hv\) is centered \(L\)-subGaussian by independence of the rows and (2.6). The bound at \(4L\sqrt n\), a union bound, and the factor-two net inequality give failure
\(2\exp\{(n+m)\log9-8n\}\leq2e^{-3n}\). This uses no within-row independence.

For any \(\|b\|\leq R\), let \(I_b=\{i:|h_i^\top b|\leq M\}\). Equation (4.2) gives
\[
\frac{|I_b^c|}{n}\leq\frac{b^\top H^\top Hb}{nM^2}
\leq\frac{C_HR^2}{M^2}=\delta.
\]
The logistic Hessian is therefore bounded simultaneously on the ball by
\[
\nabla^2\mathcal L_n(b)
=\frac1n\sum_i\sigma'(h_i^\top b)h_ih_i^\top
\succeq\sigma'(M)\frac1n\sum_{i\in I_b}h_ih_i^\top
\succeq\mu I_m.
\tag{4.3}
\]
Globally, \(\nabla^2\mathcal L_n(b)\preceq C_HI/4=\Lambda I\). Thus the desired curvature is simultaneous for all points in the ball, not merely at a prespecified iterate.

Let \(\mathcal G_d\) be the feature event together with (3.6) and (4.2). For large \(d\), (1.4) gives \(n/m\geq C_*\), and
\[
\mathbb P(\mathcal G_d^c)
\leq\mathbb P(\mathcal F_d^c)
 +e^{-np_1^2/8}+e^{-np_0^2/8}+2e^{-3n}=o(1).
\tag{4.4}
\]

## 5. MLE existence and uniform contraction

On \(\mathcal G_d\), coercivity and continuity give a finite global minimizer. Its loss is at most \(\mathcal L_n(0)=\log2\), so its norm is at most \(R_0\). Strict convexity on the containing ball proves uniqueness; call the minimizer \(b^*\). Its full gradient is zero.

For probabilistic expressions involving the MLE, assign \(b^*=0\) on any exceptional realization without a unique finite MLE. This arbitrary extension has vanishing probability and does not change any conclusion.

For large \(d\), the step assumption implies
\[
\eta_-\leq\eta_d\leq2c/\gamma<1/\Lambda.
\tag{5.1}
\]
The global smoothness inequality gives
\[
\mathcal L_n(b-\eta_d\nabla\mathcal L_n(b))
\leq\mathcal L_n(b)-\frac{\eta_d}{2}\|\nabla\mathcal L_n(b)\|^2.
\tag{5.2}
\]
Thus all iterates remain in the initial sublevel set, and hence in the radius-\(R_0\) ball.

For \(x,y\) in this ball, integrate the Hessian along their line segment. It yields a symmetric matrix \(A_{x,y}\) with spectrum in \([\mu,\Lambda]\) such that
\[
[x-\eta_d\nabla\mathcal L_n(x)]-[y-\eta_d\nabla\mathcal L_n(y)]
=(I-\eta_dA_{x,y})(x-y).
\]
Consequently the GD map contracts by
\[
q_d=1-\eta_d\mu\leq q<1.
\tag{5.3}
\]
Applying this with \(y=b^*\) proves (1.7), uniformly for every integer time. No dimension-dependent burn-in is hidden in the contraction factor.

## 6. Leave-one-feature definitions and concentration

Let \(P_j\) set coordinate \(j\) to zero. Define restricted GD for every data realization, including outside \(\mathcal G_d\), by
\[
b^{-j,0}=0,\qquad
b^{-j,t+1}=b^{-j,t}-\eta_d P_j\nabla\mathcal L_n(b^{-j,t}).
\tag{6.1}
\]
The coordinate \(j\) stays zero, so this update uses only \(X,Y,F_{-j}\). On \(\mathcal G_d\), the same descent inequality applied on the coordinate subspace shows that every restricted iterate has loss at most \(\log2\) and norm at most \(R_0\). Therefore the same full Hessian bounds apply simultaneously along the full and all restricted trajectories.

Also define \(\bar b^{-j}\), for every data realization, to minimize \(\mathcal L_n\) over the deterministic compact set
\[
\{b:b_j=0,\ \|b\|\leq R\}.
\tag{6.2}
\]
If needed, select the unique minimum-norm minimizer. This is a measurable selector: it is the limit as \(\epsilon\downarrow0\) of the unique minimizers after adding \(\epsilon\|b\|^2\). The definition uses only \(X,Y,F_{-j}\). On \(\mathcal G_d\), its loss is at most \(\log2\), so \(\|\bar b^{-j}\|\leq R_0<R\). It is then an unconstrained minimizer in its coordinate subspace, and
\[
\nabla\mathcal L_n(\bar b^{-j})=g_j^*e_j.
\tag{6.3}
\]
The larger compact ball in the definition is essential: it keeps the object well defined and independent of \(W_j\) even on exceptional samples, while still giving interior stationarity on the good event.

For any of these restricted coefficient vectors \(b\), put
\[
g_j(b)=\frac1n\sum_i
 [\sigma(h_{i,-j}^\top b_{-j})-Y_i]\tanh(W_j^\top X_i).
\tag{6.4}
\]
Conditional on \(X,Y,F_{-j}\), the bracketed residual vector is fixed, has norm at most \(\sqrt n\), and is independent of \(W_j=G_j/\sqrt d\). As a function of standard Gaussian \(G_j\), (6.4) is odd, has mean zero, and has Lipschitz constant at most
\[
\frac{\|X\|_{\mathrm{op}}}{\sqrt{nd}}.
\tag{6.5}
\]
Hence
\[
\mathbb P(|g_j(b)|>u\mid X,Y,F_{-j})
\leq2\exp\!\left(-\frac{ndu^2}{2\|X\|_{\mathrm{op}}^2}\right).
\tag{6.6}
\]
This conditioning is valid for the compact restricted minimizer and for every deterministic restricted-GD time. Conditioning instead on a good event involving \(W_j\) before applying concentration would not be valid; we do not do so.

Choose a deterministic \(B_X\) with \(\mathbb P(\|X\|_{\mathrm{op}}>B_X\sqrt d)\leq e^{-c_Xd}\) for large \(d\); the same net proof permits \(B_X=8\sqrt{1+\alpha}\). For \(d\geq3\), define
\[
T_d=1+\left\lceil\frac{\max\{0,\log(R_0d)\}}{-\log q}\right\rceil,
\qquad
\tau_d=B_X\sqrt{\frac{8\log d}{n}}.
\tag{6.7}
\]
In particular \(T_d=O(\log d)\) with a dimension-independent implied constant. Applying (6.6) and a union bound over \(j\leq m\), \(0\leq t<T_d\), and the restricted minimizers gives
\[
\max_{j,t<T_d}|g_j(b^{-j,t})|\leq\tau_d,
\qquad \max_j|g_j^*|\leq\tau_d
\tag{6.8}
\]
except with probability at most
\[
e^{-c_Xd}+2m(T_d+1)d^{-4}=o(1).
\tag{6.9}
\]
No independence between different leave-one-feature problems or different times is asserted or required.

## 7. Uniform coefficient delocalization

First compare the full and restricted MLEs on the intersection of \(\mathcal G_d\) and (6.8). Strong monotonicity along their segment gives
\[
\mu\|\bar b^{-j}-b^*\|^2
\leq\langle\nabla\mathcal L_n(\bar b^{-j})-
 \nabla\mathcal L_n(b^*),\bar b^{-j}-b^*\rangle
=-g_j^*b_j^*.
\]
Cauchy--Schwarz implies
\[
|b_j^*|\leq\|\bar b^{-j}-b^*\|\leq|g_j^*|/\mu,
\quad\text{hence}\quad \|b^*\|_\infty\leq\tau_d/\mu.
\tag{7.1}
\]

For the trajectories, let \(G_d(b)=b-\eta_d\nabla\mathcal L_n(b)\). Equation (6.1) says
\[
b^{-j,t+1}=G_d(b^{-j,t})+\eta_dg_j(b^{-j,t})e_j.
\]
The contraction established on the common ball gives
\[
\|b^{t+1}-b^{-j,t+1}\|
\leq q_d\|b^t-b^{-j,t}\|+\eta_d|g_j(b^{-j,t})|.
\tag{7.2}
\]
Starting from zero and using \(1-q_d=\eta_d\mu\), (6.8) implies
\[
\max_{j,\ 0\leq t\leq T_d}\|b^t-b^{-j,t}\|
\leq\frac{\eta_d\tau_d}{1-q_d}=\frac{\tau_d}{\mu}.
\tag{7.3}
\]
Since the restricted coordinate is zero, this bounds every \(|b_j^t|\) through time \(T_d\). For every \(t\geq T_d\), (1.7) and the definition of \(T_d\) give
\[
\|b^t\|_\infty\leq\|b^*\|_\infty+R_0q^{T_d}
\leq\tau_d/\mu+d^{-1}.
\tag{7.4}
\]
Thus on this single event,
\[
\boxed{\quad\sup_{t\geq0}\|b^t\|_\infty
\leq\tau_d/\mu+d^{-1},\qquad \|b^*\|_\infty\leq\tau_d/\mu.\quad}
\tag{7.5}
\]
Together with (4.4) and (6.9), this proves (1.8) with an explicit failure bound. The proof handles infinitely many GD times by deterministic contraction after a logarithmic horizon; it does not union-bound infinitely many concentration events.

## 8. Positive norms and simultaneous calibration floor

The lower-norm result is the argument in B03 Proposition 3; it is included here to make its use explicit. Put \(K=HH^\top/m\), \(\lambda_d=cd/n\), and \(R_Y=Y-1/2\). Then
\[
\|b^1\|^2=\frac{\lambda_d^2}{m}R_Y^\top K R_Y.
\tag{8.1}
\]
Conditional on \(X,F\), decompose \(R_Y=\bar r+\epsilon\), with independent centered bounded \(\epsilon_i\), and
\(D_{ii}=\mathbb E(\epsilon_i^2\mid X,F)=\sigma'(\beta Z_i)\). A quadratic-form expansion gives
\[
\operatorname{Var}(R_Y^\top KR_Y\mid X,F)
\leq C\{\operatorname{tr}K^2+\|K\bar r\|^2\}
\leq Cn\|K\|_{\mathrm{op}}^2.
\tag{8.2}
\]
The norm \(\|K\|\) is bounded in probability, so the normalization in (8.1) makes its centered fluctuation \(o_P(1)\). The contribution \(\bar r^\top K\bar r\) is nonnegative. Conditional on \(F\), the bounded iid row variables \(D_{ii}K_{ii}\) have expectation tending to \(v\rho_\beta\): uniformly over features, \(\|W_j\|^2\to1\) and \(\theta^\top W_j\to0\), and the relevant bounded bivariate Gaussian expectation is continuous. Hence
\[
\frac1n\operatorname{tr}(KD)\to v\rho_\beta,
\qquad
\|b^1\|^2\geq\frac{c^2v\rho_\beta}{\alpha\gamma}+o_P(1).
\tag{8.3}
\]

Let \(g_0=\nabla\mathcal L_n(0)\). Descent and convexity respectively give, for every \(t\geq1\),
\[
\mathcal L_n(b^t)\leq\log2-\frac{\eta_d}{2}\|g_0\|^2,
\qquad
\mathcal L_n(b^t)\geq\log2+g_0^\top b^t.
\]
Therefore \(\|b^t\|\geq\eta_d\|g_0\|/2=\|b^1\|/2\), simultaneously at all positive times. Letting \(t\to\infty\) gives the same bound for \(b^*\). Equation (8.3) proves (1.9)--(1.10).

For a fresh test pair, condition on the complete training environment \(\mathcal E_d=(F,X_{1:n},Y_{1:n})\). Let \(S_{t,d}=h(X)^\top b^t\) and
\[
A_{t,d}=\mathbb E_X[ZS_{t,d}\mid\mathcal E_d]=g_F^\top b^t,
\qquad
Q_{t,d}=\mathbb E_X[S_{t,d}^2\mid\mathcal E_d]=(b^t)^\top\Sigma_Fb^t.
\tag{8.4}
\]
Use \(t=\infty\) for \(b^*\). Equations (2.1), (1.9), and Poincare yield, simultaneously for all \(t\in\{1,2,\ldots,\infty\}\),
\[
Q_{t,d}-A_{t,d}^2\geq s r_*^2=:\Delta_*>0,
\qquad Q_{t,d}\leq L^2R_0^2=:Q_*.
\tag{8.5}
\]
The readout derivative bounds are uniform in time:
\[
\|\nabla S_t\|\leq LR_0,\quad
\|\nabla^2S_t\|_{\mathrm{HS}}\leq2L^2R_0,\quad
\|\nabla^2S_t\|_{\mathrm{op}}
\leq2L^2\sup_u\|b^u\|_\infty=o_P(1).
\tag{8.6}
\]
The proof of B04 Theorem 2.1 is sequentially uniform over classes with fixed bounds in (8.5)--(8.6). Otherwise a deterministic sequence violating uniformity would contradict that theorem. Consequently its random-environment argument gives
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
\left\|\mathcal L((Z,S_{t,d})\mid\mathcal E_d)
-N\!\left(0,\begin{pmatrix}1&A_{t,d}\\A_{t,d}&Q_{t,d}\end{pmatrix}\right)
\right\|_{\mathrm{TV}}\longrightarrow0
\quad\text{in probability}.
\tag{8.7}
\]
This argument does not require deterministic overlap limits or a union bound over time.

For \(Q>A^2\), define the explicit Gaussian calibration functional
\[
\mathcal C_\beta(A,Q)
=\mathbb E_{U}\left|
\mathbb E_V\sigma\!\left(\beta\frac{A}{\sqrt Q}U
+\beta\sqrt{1-\frac{A^2}{Q}}V\right)
-\sigma(\sqrt Q U)\right|,
\qquad U,V\stackrel{\mathrm{iid}}\sim N(0,1).
\tag{8.8}
\]
Let \(\mathrm{CE}_{t,d}\) be exact, unbinned population calibration error of the predictor \(\sigma(S_{t,d})\), conditional on \(\mathcal E_d\). Since sigmoid is injective, conditioning on its probability is equivalent to conditioning on the score. B04's signed-measure argument makes this calibration error TV-Lipschitz. Applying the common label kernel \(Y\mid Z\) and (8.7),
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
|\mathrm{CE}_{t,d}-\mathcal C_\beta(A_{t,d},Q_{t,d})|
\longrightarrow0
\quad\text{in probability}.
\tag{8.9}
\]

For clarity, strict positivity of (8.8) holds for every \(Q-A^2>0\). If \(\beta=0\), the true curve is the constant \(1/2\) and the nonconstant prediction has positive error. If \(\beta>0,A\leq0\), the Gaussian conditional probability is nonincreasing while sigmoid is strictly increasing. If \(\beta>0,A>0\), write its conditional curve as
\(g(s)=\mathbb E\sigma(ks+\tau V)\), with
\(k=\beta A/Q>0\) and \(\tau=\beta\sqrt{1-A^2/Q}>0\). Dominated convergence gives
\[
\lim_{s\to\infty}e^{ks}(1-g(s))=e^{\tau^2/2}.
\]
Equality with \(\sigma(s)\) for every \(s\) would force first \(k=1\) and then \(e^{\tau^2/2}=1\), a contradiction. Equality almost everywhere would imply equality everywhere by continuity. Thus the error is strictly positive.

The parameter set
\[
\mathcal K=\{(A,Q): Q\leq Q_*,\ Q-A^2\geq\Delta_*\}
\tag{8.10}
\]
is compact. Formula (8.8) is continuous on it by dominated convergence. Therefore
\[
\varepsilon_*:=\min_{(A,Q)\in\mathcal K}\mathcal C_\beta(A,Q)>0.
\tag{8.11}
\]
Equations (8.5) and (8.9) prove the simultaneous statement
\[
\mathbb P\!\left(
\inf_{t\in\{1,2,\ldots,\infty\}}\mathrm{CE}_{t,d}
\geq\varepsilon_*/2\right)\longrightarrow1.
\tag{8.12}
\]
In particular, **no training-measurable stopping rule taking a positive integer time, even one diverging with dimension, attains asymptotic calibration in this fixed-step regime.** The same holds if the rule may output the MLE. At time zero the constant predictor \(1/2\) is calibrated, since the symmetric teacher has marginal class probability \(1/2\). The theorem does not cover steps \(c=c_d\to0\), which alter the stated regime.

Positive absolute calibration error does not alone assert that every confidence level is overconfident. The full curve in (8.8), or its conditional form \(g(s)\), determines the direction. Early positive iterates can be underconfident while still having strictly positive exact calibration error.

## 9. Promotion of deterministic finite-time overlaps to all times

This section is a conditional consequence with a clearly identified remaining input. Suppose a separate finite-time state-evolution theorem proves, for every fixed integer \(t\geq1\), deterministic limits
\[
A_{t,d}\xrightarrow{P}A_t(\alpha,\gamma,c,\beta),\qquad
Q_{t,d}\xrightarrow{P}Q_t(\alpha,\gamma,c,\beta).
\tag{9.1}
\]
Then these limits extend to \(t=\infty\), and convergence is uniform over all positive integer times and the MLE:
\[
\sup_{t\in\{1,2,\ldots,\infty\}}
\big\{|A_{t,d}-A_t|+|Q_{t,d}-Q_t|\big\}\xrightarrow{P}0.
\tag{9.2}
\]

Here is the proof, including the exchange of limits. The population norm bounds are \(\|g_F\|\leq L\) and \(\|\Sigma_F\|\leq L^2\). From (1.7), for every \(t\geq T\), including infinity,
\[
\|b^t-b^T\|\leq2R_0q^T,
\]
\[
|A_{t,d}-A_{T,d}|\leq2LR_0q^T,
\qquad
|Q_{t,d}-Q_{T,d}|\leq4L^2R_0^2q^T.
\tag{9.3}
\]
For each fixed \(t,T\), take probability limits in these deterministic inequalities on events of probability tending to one. This gives the same bound between \((A_t,Q_t)\) and \((A_T,Q_T)\). Therefore the deterministic sequence is exponentially Cauchy and has a limit \((A_\infty,Q_\infty)\). For arbitrary fixed \(T\), split the supremum in (9.2) into the finite times below \(T\) and the common exponential tail. Equation (9.1) controls the finite part, while (9.3) controls both tails. Let \(d\to\infty\), then \(T\to\infty\). This proves (9.2) without interchanging unproved limits.

Combining uniform continuity on (8.10), (8.9), and (9.2) gives the deterministic whole-trajectory theorem
\[
\boxed{\quad
\sup_{t\in\{1,2,\ldots,\infty\}}
\left|\mathrm{CE}_{t,d}
-\mathcal C_\beta\big(A_t(\alpha,\gamma,c,\beta),
Q_t(\alpha,\gamma,c,\beta)\big)\right|
\xrightarrow{P}0.\quad}
\tag{9.4}
\]
For a data-dependent positive stopping rule \(\tau_d\), the same uniform estimate holds after substituting \(t=\tau_d\). If \(\tau_d\to\infty\) in probability, then \(\mathrm{CE}_{\tau_d,d}\to\mathcal C_\beta(A_\infty,Q_\infty)>0\) in probability. If the stopping time has no limiting value, the deterministic curve still approximates its realized index and the common positive floor still applies.

The imported input (9.1) is what makes (9.4) a calibration function of the aspect ratios and training time. Equations (8.7)--(8.12) themselves do not require that input and are already unconditional consequences of the proofs above and B04's analytic transfer theorem.

## 10. Scope and dependencies

- The general proportional regime of this note is an explicit open set: arbitrary fixed finite \(\beta\), arbitrary fixed width ratio \(\gamma>0\), sufficiently large fixed \(\alpha/\gamma\), and sufficiently small fixed positive \(c\). The proof neither covers separable small-sample regimes nor claims a sharp sample-to-width threshold.
- The feature covariance and empirical coercivity/curvature arguments are proved here. They account for teacher-feature dependence and adaptive row deletion.
- Leave-one-feature objects are defined independently of the omitted feature even on exceptional samples. The common curvature event holds for both full and restricted trajectories because both stay in the same initial sublevel ball.
- The time-uniform probabilistic claim uses concentration only through a deterministic \(O(\log d)\) horizon and a dimension-independent geometric tail afterward.
- The only analytic calibration input is `fullproof/b04_calibration_transfer.md`, Theorem 2.1 and its signed-measure CE continuity argument, independently audited in `fullproof/b02_gaussian_calibration_audit.md`.
- A deterministic state-evolution theorem is an explicit additional hypothesis only in Section 9. This note supplies the rigorous uniform-time extension once that theorem is certified.


---

# Appendix E: Signed overconfidence and the common regime

Source module: `b06_gaussian_overconfidence.md`. SHA-256: `b65ea33e7e0208b825f429f5369ac1fbd1e470803848356df749b7208fbcb532`.

# Gaussian logistic scores: strict overconfidence at the risk-optimal scale

24 October 2026. Independent proof and scope audit by B06.

This note proves the scalar lemma requested for the ordinary Gaussian random-feature model. It verifies, with an elementary integral argument, the single-crossing assertion suggested in `a03/rows_T357_DOSSIER.md` on 20 October at 17:34. It does not assume that assertion or invoke an unverified total-positivity theorem. The normal-mixture representation of the logistic law is classical; a derivation is included. No publication-novelty claim is made.

## 1. Statement

Let $Z,G$ be independent standard normal variables, let $k,\tau,\beta>0$, and put

\[
U=kZ+\tau G,\qquad V=k^2+\tau^2.
\tag{1}
\]

Given $Z$, let $Y$ be Bernoulli with mean $\sigma(\beta Z)$, independently of $G$, where $\sigma(x)=(1+e^{-x})^{-1}$. Its conditional regression given the score coordinate is

\[
g(u):=\mathbb E[Y\mid U=u]
=\mathbb E_H\sigma(\lambda u+sH),\qquad
\lambda=\frac{\beta k}{V},\quad s=\frac{\beta\tau}{\sqrt V},
\tag{2}
\]

with $H$ standard normal. Consider the positive-scale predictors $p_c(u)=\sigma(cu)$ and their population cross-entropy

\[
R(c)=\mathbb E\{\log(1+e^{cU})-cU g(U)\}.
\tag{3}
\]

**Theorem.** For every $k,\tau,\beta>0$:

1. The function
   \[
   h(u)=\frac{\operatorname{logit}g(u)}u,\qquad u>0,
   \tag{4}
   \]
   is continuous and strictly increasing, with endpoint limits
   \[
   h(0+)=4g'(0)=4\lambda\mathbb E\sigma'(sH),
   \qquad h(+\infty)=\lambda.
   \tag{5}
   \]
2. $R$ has a unique global minimizer $c_*$, and
   \[
   4g'(0)<c_*<\lambda,\qquad R(c_*)<R(0)=\log2.
   \tag{6}
   \]
3. There is a unique $u_*>0$ such that
   \[
   \sigma(c_*u)-g(u)
   \begin{cases}>0,&0<u<u_*,\\=0,&u=u_*,\\<0,&u>u_*.
   \end{cases}
   \tag{7}
   \]
4. The average signed overconfidence is strictly positive:
   \[
   \operatorname{OC}(c_*):=
   \mathbb E\big[(\sigma(c_*U)-g(U))\operatorname{sign}U\big]>0.
   \tag{8}
   \]

Here the predicted class is $\mathbf1_{\{U>0\}}$, its confidence is $\sigma(c_*|U|)$, and its conditional probability of being correct is $g(|U|)$. With $S=c_*U$, conditioning on $U$ gives the equivalent exact definition

\[
\operatorname{OC}(c_*)=\mathbb E[(\sigma(S)-\sigma(\beta Z))\operatorname{sign}S].
\]

Thus (8) is exactly mean confidence minus mean accuracy. It is not a claim of overconfidence at every score: (7) proves underconfidence in the far tails.

## 2. Logistic noise as a normal variance mixture

Let $E_1,E_2,\ldots$ be independent exponential variables of mean one, and define

\[
W=2\sum_{j=1}^{\infty}\frac{E_j}{j^2}.
\tag{9}
\]

The series is finite almost surely, because its expectation is $2\sum j^{-2}=\pi^2/3<\infty$. If $N$ is an independent standard normal variable, the characteristic function of $\sqrt W N$ is

\[
\mathbb E e^{-t^2W/2}
=\prod_{j=1}^{\infty}(1+t^2/j^2)^{-1}
=\frac{\pi t}{\sinh(\pi t)},
\tag{10}
\]

with the continuous value one at $t=0$. The last identity is Euler's product for $\sinh$. On the other hand, the characteristic function of a standard logistic variable $L$ is

\[
\int_{-\infty}^{\infty}e^{itx}\frac{e^x}{(1+e^x)^2}\,dx
=\int_0^{\infty}\frac{r^{it}}{(1+r)^2}\,dr
=\Gamma(1+it)\Gamma(1-it)
=\frac{\pi t}{\sinh(\pi t)}.
\tag{11}
\]

The middle equality is the beta integral, and the last follows from the gamma reflection identity. Uniqueness of characteristic functions therefore proves

\[
L\ \overset d=\ \sqrt W N.
\tag{12}
\]

We also need strict support, not just a formal mixture. Write $W=2E_1+Q$, where $Q=2\sum_{j\ge2}E_j/j^2$. For every $w>0$, $\mathbb P(Q<w)>0$: choose a finite cutoff whose remaining tail has expectation less than $w/4$; the tail is below $w/2$ with positive probability by Markov's inequality, and the finite initial sum is below $w/2$ with positive probability, independently. Conditioning on $Q$ gives the density

\[
f_W(w)=\frac12 e^{-w/2}
\mathbb E\big[e^{Q/2}\mathbf1_{\{Q<w\}}\big]>0
\quad(w>0).
\tag{13}
\]

It is finite, since the integrand is bounded by $e^{w/2}$. Hence the CDF $F_W$ is strictly increasing on $(0,\infty)$, is positive at every positive argument, and vanishes at nonpositive arguments.

## 3. A direct strict single-crossing argument

For $s>0$, write

\[
F_s(x)=\mathbb E\sigma(x+sH),\qquad
\Lambda_s(x)=\operatorname{logit}F_s(x).
\tag{14}
\]

By symmetry of $H$, $F_s$ is the CDF of $L+sH$. Conditional on $W$, this is a centered normal variable of variance $W+s^2$. Consequently

\[
F_s(x)=\mathbb E\Phi\left(\frac{x}{\sqrt{W+s^2}}\right),
\qquad
\sigma(cx)=\mathbb E\Phi\left(\frac{x}{\sqrt W/c}\right)
\quad(c>0).
\tag{15}
\]

Set $x=e^t$. The difference of the CDFs of the logarithms of the two random scales in (15) is

\[
N_c(u)
=F_W(e^{2u}-s^2)-F_W(c^2e^{2u}).
\tag{16}
\]

Integration by parts yields

\[
D_c(t):=F_s(e^t)-\sigma(ce^t)
=\int_{\mathbb R}K(t-u)N_c(u)\,du,
\qquad K(v)=e^v\varphi(e^v).
\tag{17}
\]

For completeness, the function being integrated against the signed scale law is $u\mapsto\Phi(e^{t-u})$; its derivative is $-K(t-u)$. The boundary terms vanish because $N_c(u)\to0$ at both ends. The integral is absolutely convergent: $|N_c|\le1$ and $\int K(v)\,dv=1/2$.

If $c\ge1$, (13) and (16) give $N_c(u)<0$ for every finite $u$; hence $D_c(t)<0$ for every $t$. In particular

\[
\tfrac12<F_s(x)<\sigma(x)\quad(x>0).
\tag{18}
\]

The first strict inequality follows from symmetry and strict monotonicity of $F_s$.

For $0<c<1$, put

\[
u_c=\frac12\log\frac{s^2}{1-c^2}.
\tag{19}
\]

Strict monotonicity of $F_W$ implies

\[
N_c(u)<0\ (u<u_c),\qquad
N_c(u_c)=0,\qquad
N_c(u)>0\ (u>u_c).
\tag{20}
\]

For any $t_2>t_1$, the kernel ratio

\[
Q(u):=\frac{K(t_2-u)}{K(t_1-u)}
=e^{t_2-t_1}
\exp\left[-\frac{e^{2t_2}-e^{2t_1}}2e^{-2u}\right]
\tag{21}
\]

is strictly increasing in $u$, and is bounded above by $e^{t_2-t_1}$. Therefore

\[
D_c(t_2)-Q(u_c)D_c(t_1)
=\int_{\mathbb R}K(t_1-u)
  [Q(u)-Q(u_c)]N_c(u)\,du>0.
\tag{22}
\]

Every factor except the bracket and $N_c$ is positive; these last two factors have the same strict sign on either side of $u_c$. The integral is finite by the bound on $Q$ and the integrability of $K$. In particular, a zero of $D_c$ is followed by strictly positive values. This proves the exact direction of the required single crossing without an appeal to a general variation-diminishing result.

Now fix $0<x_1<x_2$, and choose

\[
c=\frac{\Lambda_s(x_1)}{x_1}\in(0,1),
\tag{23}
\]

where membership in $(0,1)$ follows from (18). Then $D_c(\log x_1)=0$. Equation (22) gives

\[
F_s(x_2)>\sigma(cx_2),\quad\text{so}\quad
\frac{\Lambda_s(x_2)}{x_2}>
\frac{\Lambda_s(x_1)}{x_1}.
\tag{24}
\]

This is strict monotonicity for every pair $x_1<x_2$, without needing an analyticity argument.

At zero, dominated differentiation and $F_s(0)=1/2$ give

\[
\lim_{x\downarrow0}\frac{\Lambda_s(x)}x
=4\mathbb E\sigma'(sH)\in(0,1).
\tag{25}
\]

For the other endpoint,

\[
e^x[1-F_s(x)]
=\mathbb E\frac{e^{-sH}}{1+e^{-x-sH}}
\longrightarrow e^{s^2/2}
\tag{26}
\]

by dominated convergence, since $e^{-sH}$ is integrable. Thus

\[
\Lambda_s(x)=x-\frac{s^2}2+o(1),\qquad
\lim_{x\to\infty}\frac{\Lambda_s(x)}x=1.
\tag{27}
\]

Applying (24)--(27) with $x=\lambda u$ proves (4)--(5).

## 4. Risk minimization and strict signed overconfidence

The normal law of $U$ has all moments, so dominated differentiation gives

\[
R'(c)=\mathbb E[U(\sigma(cU)-g(U))],\qquad
R''(c)=\mathbb E[U^2\sigma'(cU)]>0.
\tag{28}
\]

Since $g(u)>1/2$ for $u>0$, symmetry implies $R'(0)<0$. On the other hand,

\[
\lim_{c\to\infty}R'(c)
=\mathbb E[|U|(1-g(|U|))]>0.
\tag{29}
\]

The integrand is strictly positive almost surely and is integrable. Thus the strictly convex function $R$ has a unique critical point $c_*>0$, and it is its global minimizer. Its value is strictly below $R(0)=\log2$.

Let $h_0=4g'(0)$. By the strict increase already proved, $h_0<h(u)<\lambda$ for every $u>0$. Hence $R'(c)<0$ for $c\le h_0$, and $R'(c)>0$ for $c\ge\lambda$. This proves $h_0<c_*<\lambda$. Continuity, strict increase and the endpoint limits produce a unique $u_*>0$ with $h(u_*)=c_*$, and (7) follows from the strict increase of $\sigma$.

Write $e(u)=\sigma(c_*u)-g(u)$, and let $\varphi_V$ denote the $N(0,V)$ density. The first-order condition and oddness of $e$ give

\[
0=R'(c_*)=2\int_0^\infty u\,e(u)\varphi_V(u)\,du.
\tag{30}
\]

Subtracting this identity divided by $u_*$ from the unweighted signed error gives

\[
\begin{aligned}
\operatorname{OC}(c_*)
&=2\int_0^\infty e(u)\varphi_V(u)\,du\\
&=2\int_0^\infty e(u)
    \left(1-\frac u{u_*}\right)\varphi_V(u)\,du
>0.
\end{aligned}
\tag{31}
\]

The two factors $e(u)$ and $1-u/u_*$ have the same strict sign for every $u>0$ other than $u_*$. Integrability follows from $|e|\le1$ and the first absolute normal moment. This completes the theorem.

One may compute $c_*$ through a one-dimensional strictly monotone equation. Stein's identity and the original representation (1) give

\[
Vc_*\,\mathbb E\sigma'(c_*\sqrt V\,H)
=k\beta\,\mathbb E\sigma'(\beta H).
\tag{32}
\]

Equation (28), rather than any presumed monotonicity of the individual factors in (32), proves uniqueness.

## 5. Exact scope of the consequence for T357

Suppose a first-step Gaussian random-feature theorem gives, conditional on the trained model,

\[
\mathcal L(Z,U_d\mid\text{model})
\longrightarrow \mathcal L(Z,kZ+\tau G)
\quad\text{in total variation in probability},
\tag{33}
\]

with $k,\tau>0$, and gives population cross-entropy convergence at every fixed deterministic scale. Taking the fixed scale $c=c_*$ from this note then yields

\[
\operatorname{OC}_d(c_*)\xrightarrow{\mathbb P}
\operatorname{OC}(c_*)>0,\qquad
R_d(c_*)\xrightarrow{\mathbb P}R(c_*)<\log2.
\tag{34}
\]

Indeed signed OC is the conditional expectation of the bounded measurable function

\[
(z,u)\longmapsto
[\sigma(c_*u)-\sigma(\beta z)]\operatorname{sign}u,
\tag{35}
\]

so total variation proves the first assertion directly. A second moment bound or the separately established risk-transfer theorem handles the unbounded cross-entropy integrand. In particular, fixed positive margins below $\log2$ and above zero hold simultaneously with probability tending to one. B04's first-step TV theorem and the previously audited first-step risk theorem are the relevant proposed inputs; this note does not replace their proofs.

Because $u\mapsto\sigma(c_*u)$ is one-to-one, the limiting exact unbinned calibration error is

\[
\mathbb E|\sigma(c_*U)-g(U)|
\ge\operatorname{OC}(c_*)>0.
\tag{36}
\]

The finite-model OC statement (34) itself does not require continuity of conditional regression: it uses the bounded test function (35). This is weaker in prerequisite than proving convergence of an entire conditional calibration curve.

The theorem treats all positive parameters in the Gaussian scalar experiment, not a selected categorical surrogate or one numerical parameter choice. It closes a signed-overconfidence proof obligation at a risk-optimal **first-step scale**. It does not establish a deterministic arbitrary-time neural-GD trajectory, interchange a training-time limit with dimension, optimize over all stopping times, or show that the scalar risk optimum is a global optimum over the full GD path. Those remain separate T357 obligations. The limiting predictor is overconfident near the boundary and underconfident in the tails, so a claim of pointwise overconfidence at all scores would be false.

## 6. An explicit common regime with the whole-trajectory stopping theorem

The risk-optimal scale above is not automatically a stable GD step. Nevertheless, there is an explicit nonempty regime in which it satisfies the small-step and sample-size conditions of B02's entire-trajectory theorem. Thus the overconfidence and stopping conclusions need not be about incompatible parameter choices.

Use the actual first-step law from the Gaussian tanh RF calculation, with the step scale factored out:
\[
S_1=cU,\qquad
k=a^2\mu_\beta,\qquad
\tau^2=\frac{\mu_\beta^2a^2v}{\gamma}
+\frac{a^4+v^2/\gamma}{4\alpha},
\tag{37}
\]
where
\[
a=\mathbb E[H\tanh H]>0,\quad
v=\mathbb E\tanh^2H>0,\quad
\nu=v-a^2>0,\quad
\mu_\beta=\mathbb E[H(\sigma(\beta H)-1/2)]
=\beta\mathbb E\sigma'(\beta H).
\]
These are exactly the coefficients in B01 equation (21), equivalently the previously audited Gaussian first-step theorem. For $\beta>0$, both $k$ and $\tau$ are strictly positive.

Fix any $\gamma>0$, and use B02's constants
\[
L=8\sqrt{1+\gamma},\qquad
s_0=\nu/2,\qquad
\kappa=\sqrt{s_0/2},\qquad
p_0=\frac{s_0^2}{20L^4},\qquad
B=\sqrt{2\log(4/p_0)}.
\]
Choose
\[
\frac{\alpha}{\gamma}>
C_0:=\max\left\{1,\left(\frac{256L}{\kappa p_0}\right)^2\right\},
\qquad
0<\beta<
\min\left\{\frac{\log3}{B},\frac{v}{8aL\sqrt\alpha}\right\}.
\tag{38}
\]
Every interval here has positive length. In particular this is a nonempty open set of proportional sample, width and teacher parameters, although its sample ratio is deliberately very conservative.

The first inequality on $\beta$ gives
$q_\beta=\sigma(-\beta B)>1/4$ and hence
$p_1=q_\beta p_0/2>p_0/8$ in B02. Thus its threshold satisfies
\[
C_*(\beta)=
\max\left\{1,\left(\frac{32L}{\kappa p_1}\right)^2\right\}
\le C_0<\alpha/\gamma.
\tag{39}
\]
Next, $\mu_\beta\le\beta/4$ and (37) give
\[
0<c_*<\frac{\beta k}{k^2+\tau^2}
\le\frac{a^2\alpha\gamma\beta^2}{v^2}
<\frac{\gamma}{64L^2}
<\frac{\gamma}{32L^2}
=\frac{\gamma}{2\Lambda},
\qquad\Lambda=16L^2.
\tag{40}
\]
This is precisely inside B02's stable fixed-step interval. The scalar risk optimum is therefore a valid fixed deterministic GD parameter in the same model for which B02 proves its all-time statements.

Consequently, after the companion finite-model transfer and whole-trajectory theorems are certified, this one model simultaneously has:

- A first positive iterate with population risk strictly below $\log2$ and strictly positive signed overconfidence, with probability tending to one.
- A fixed positive exact-calibration floor, with probability tending to one, simultaneously over every positive integer training time, the MLE, and any training-measurable stopping rule taking those values.
- A calibrated time-zero predictor with risk exactly $\log2$.

This also gives a nonvacuous risk-constrained stopping conclusion. For any fixed $\Delta>0$ and any training-measurable rule $T_d\in\{0,1,\ldots,\infty\}$ such that
\[
\mathbb P\{R_d(T_d)\le\log2-\Delta\}\longrightarrow1,
\tag{41}
\]
one necessarily has $\mathbb P(T_d>0)\to1$, because the risk at time zero is exactly $\log2$. The simultaneous positive calibration floor then applies to $T_d$. On the other hand, a fixed first-step rule satisfies (41) for every $\Delta<R(0)-R(c_*)$ by (34). Thus such risk improvement is attainable but cannot coexist with asymptotic exact calibration through stopping alone in this fixed-step regime.

This common regime still has sufficiently large $n/m$, so the fitted output layer is underparameterized. The random-feature architecture remains the original dense Gaussian nonlinear model; no categorical design is introduced. The argument does not extend the all-time statement to every overparameterized sample ratio or to dimension-dependent vanishing steps.

## 7. Source and originality note

The classical normal scale-mixture representation appears in L. A. Stefanski, *A normal scale mixture representation of the logistic distribution*, Statistics & Probability Letters 11(1), 69--70 (1991), [DOI 10.1016/0167-7152(91)90181-P](https://doi.org/10.1016/0167-7152(91)90181-P). Bibliographic identity was checked against the publisher's volume listing. The institutional full-text endpoint returned a fetch error during this audit; no inaccessible passage is used as a proof premise. Equations (9)--(13) establish the representation and strict support independently from standard characteristic-function and gamma identities.

The old local dossier already suggested a normal-mixture single-crossing route. The contribution of this audit is the explicit ratio calculation (21)--(24), the strict-support argument, and the fully stated risk-to-signed-OC implication. This verifies the local mathematical claim; it does not certify that the conclusion is new in the literature.
