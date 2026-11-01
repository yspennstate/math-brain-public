# Deterministic finite-time state evolution for the original Gaussian tanh RF model

24 October 2026. B04. Independent source and proof audit, with an explicit
state recursion and a direct nondegeneracy proof. This file changes no
frozen result.

**Conclusion.** The generalized-invariance route closes the deterministic
finite-time gap for the actual output-layer logistic-GD trajectory, for
every fixed positive step constant and every fixed finite horizon. The
matrix input is Theorem 5 of `b03_gaussian_dynamics.md`, independently
checked in `b05_RF_universality_audit.md`. The algorithmic embedding is
Section 9 of B03. The explicit rectangular-cumulant simplification was
derived in `b01_GD_state_evolution_check.md`, equations (10) and (16),
and independently checked here directly against Fan's
formulas. In particular, all required AMP state covariances are positive
definite. **No limiting perturbation argument is needed for zero network
initialization:** the AMP is initialized by the nonzero label residual.

The theorem below is for fixed time. A statement uniform over all training
times still requires the separate stability/coercivity argument; it does
not follow just by taking a union over infinitely many fixed-time limits.

## 1. The model and theorem

Take independent \(X_i\sim N(0,I_d)\), feature rows
\(W_j\sim N(0,I_d/d)\), a deterministic unit vector \(\theta_d\), and
labels
\(Y_i\mid X_i\sim\operatorname{Bernoulli}(\sigma(\beta\theta_d^\top X_i))\),
with fixed finite \(\beta\ge0\). Suppose

\[
n/d\to\alpha\in(0,\infty),\qquad
m/d\to\gamma\in(0,\infty).
\]

Put \(H_{ij}=\tanh(W_j^\top X_i)\). For fixed \(c>0\), train the raw
readout from zero by

\[
b^0=0,\qquad
b^{t+1}=b^t+\frac{cd}{nm}H^\top
                      [Y-\sigma(Hb^t)].
\tag{1.1}
\]

This is precisely mean-loss GD with step \(cd\) in the original
\(m^{-1/2}a^\top h\) parameterization, since \(b=a/\sqrt m\).
Let \(\mathcal E_d\) contain the realized training sample and features,
and set \(S_{t,d}(X)=(b^t)^\top\tanh(FX)\) for a fresh independent
\(X\sim N(0,I_d)\).

Define

\[
a=\mathbb E[G\tanh G],\qquad
v=\mathbb E\tanh^2G,\qquad \nu=v-a^2>0,
\quad \kappa=\mathbb E[G\{\sigma(\beta G)-1/2\}].
\tag{1.2}
\]

**Theorem 1 (finite-time deterministic Gaussian test law and exact
calibration).** Fix \(T<\infty\). The recursion in Section 2 determines
finite deterministic numbers \(q_1,\ldots,q_T\) and a positive definite
matrix \(\Sigma_T\). Put

\[
A_t=sq_t,\qquad
Q_{st}=\Sigma_{st}+s^2q_sq_t,\qquad s=a\sqrt\gamma.
\tag{1.3}
\]

For a Gaussian vector \((Z,E_1,\ldots,E_T)\), where
\(Z\sim N(0,1)\), \(E_{1:T}\sim N(0,\Sigma_T)\), and \(Z\) and
\(E_{1:T}\) are independent, set \(S_t=A_tZ+E_t\). Then:

1. The conditional covariance parameters of the original trained RF
   path converge in probability:
   \[
   \mathbb E_X[ZS_{t,d}\mid\mathcal E_d]\to A_t,
   \qquad
   \mathbb E_X[S_{s,d}S_{t,d}\mid\mathcal E_d]\to Q_{st}.
   \tag{1.4}
   \]
2. The conditional law of
   \((Z,S_{1,d},\ldots,S_{T,d})\) converges weakly in probability to
   \((Z,S_1,\ldots,S_T)\). For each positive \(t\le T\), the
   conditional law of \((Z,S_{t,d})\) converges in total variation in
   probability to \((Z,S_t)\).
3. Population logistic risk converges in \(L^1\) over the environment to
   \[
   L_t=\mathbb E_G\log\{2\cosh(\sqrt{Q_{tt}}G/2)\}-\kappa A_t.
   \tag{1.5}
   \]
4. Exact, unbinned, model-conditional calibration error converges in
   probability and every finite \(L^p\) to
   \[
   C_t=\mathbb E_G\left|
     \mathbb E_J\sigma\!\left(\beta\left[
       \frac{A_t}{\sqrt{Q_{tt}}}G+
       \sqrt{1-\frac{A_t^2}{Q_{tt}}}\,J\right]\right)
     -\sigma(\sqrt{Q_{tt}}G)\right|>0,
   \tag{1.6}
   \]
   with independent standard normals \(G,J\). In particular every
   positive time in this fixed horizon is asymptotically miscalibrated.

All assertions hold for every fixed \(c>0\), without the small-step
restriction used for the earlier coefficient-norm lower bound. The
strictly positive residual variance here is
\(Q_{tt}-A_t^2=\Sigma_{tt}>0\).

## 2. Explicit deterministic recursion

Append \(n\) independent test rows and use \(N=2n\) rows in total. The
mask \(M_i\) is one on training rows and zero on test rows. The limiting
constants are

\[
\pi=\tfrac12,\qquad \delta=\lim N/d=2\alpha,
\qquad \rho=\lim N/m=\delta/\gamma,
\qquad \lambda=c/\alpha,
\qquad s=a\sqrt\gamma,
\qquad h=a^2\delta.
\tag{2.1}
\]

Here \(\delta\) is a dimension ratio, not a conditional variance. One
may instead append any fixed positive proportional test block, replacing
\(\pi,\delta,\rho\) consistently; the resulting test law is unchanged.

Use two scalar probability spaces:

* On the row space, \(Z\sim N(0,1)\),
  \(Y\mid Z\sim\operatorname{Bernoulli}(\sigma(\beta Z))\), and
  \(M\sim\operatorname{Bernoulli}(\pi)\) is independent of \((Z,Y)\).
  The Gaussian row fields \(E_{1:t}\) are independent of this side
  information.
* On the column space, \(V\sim N(0,1)\). The Gaussian column fields
  \(G_{1:t}\) are independent of \(V\).

Only expectations within each space are used. The two spaces communicate
through deterministic moments, not through an unspecified joint law of
their scalar coordinates.

Let \(R_t\) denote a row residual and \(B_t\) a scalar column/readout
iterate. We use \(\mathsf A_t,\mathsf B_t\) for memory matrices, to
distinguish them from \(B_t\) and the test covariance \(A_t\).
Initialize

\[
B_0=0,\qquad R_1=M(Y-1/2),\qquad
\ell_1=\mathbb E[ZR_1]=\pi\kappa,
\quad \Delta_1=\pi/4,\quad\Phi_1=0.
\tag{2.2}
\]

The moment/Jacobian matrices at time \(t\) are

\[
\Delta_t=(\mathbb E[R_iR_j])_{i,j\le t},\qquad
\Gamma_t=(\mathbb E[B_iB_j])_{i,j\le t},
\]
\[
(\Phi_t)_{ij}=\mathbb E[\partial_{E_j}R_i]\ (j<i),
\quad (\Phi_t)_{ij}=0\ (j\ge i),
\qquad
(\Psi_t)_{ij}=\partial_{G_j}B_i\ (j\le i),
\quad (\Psi_t)_{ij}=0\ (j>i).
\tag{2.3}
\]

The column iterate is affine in its Gaussian fields, so its derivatives
in \(\Psi_t\) are deterministic. In contrast, the derivatives defining
\(\Phi_t\) are taken through the row recursion **before** taking the
expectation; an expectation of a product of derivatives must not be
replaced by a product of expectations.

For each \(t=1,\ldots,T\), perform the following alternating update.

**Column update.** Before computing \(B_t\), pad the previously computed
\(\Gamma_{t-1}\) with a zero last row and column, and pad
\(\Psi_{t-1}\) with a zero last row and column. With these provisional
\(\Gamma_t,\Psi_t\), define

\[
L_t=(I-h\Phi_t\Psi_t)^{-1},
\]
\[
\boxed{
\begin{aligned}
\mathsf B_t
 &=\rho\{\nu\Phi_t+a^2L_t\Phi_t\},\\
\Omega_t
 &=\rho\nu\Delta_t+
   \rho a^2L_t(\Delta_t+h\Phi_t\Gamma_t\Phi_t^\top)L_t^\top.
\end{aligned}}
\tag{2.4}
\]

These expressions do not depend on the provisionally missing entries,
because \(\Phi_t\) is strictly lower triangular. Generate
\(G_{1:t}\sim N(0,\Omega_t)\), consistently with its already generated
earlier marginal, and define

\[
B_t=B_{t-1}+\lambda\left[
 G_t+\sum_{j<t}(\mathsf B_t)_{tj}B_j+s\rho\ell_t V\right],
\qquad q_t=\mathbb E[VB_t].
\tag{2.5}
\]

Complete \(\Gamma_t,\Psi_t\) using (2.3). In particular
\((\Psi_t)_{tt}=\lambda>0\). All older entries remain unchanged.

**Row update.** Define

\[
K_t=(I-h\Psi_t\Phi_t)^{-1},
\]
\[
\boxed{
\begin{aligned}
\mathsf A_t
 &=\nu\Psi_t+a^2K_t\Psi_t,\\
\Sigma_t
 &=\nu\Gamma_t+
   a^2K_t(\Gamma_t+h\Psi_t\Delta_t\Psi_t^\top)K_t^\top.
\end{aligned}}
\tag{2.6}
\]

Generate \(E_{1:t}\sim N(0,\Sigma_t)\), consistently with earlier
marginals and independently of \((M,Z,Y)\). Define the physical row
score and next residual by

\[
U_t=E_t+\sum_{j\le t}(\mathsf A_t)_{tj}R_j+s q_tZ,
\qquad
R_{t+1}=M\{Y-\sigma(U_t)\},
\quad \ell_{t+1}=\mathbb E[ZR_{t+1}].
\tag{2.7}
\]

Compute the new row/column of \(\Delta_{t+1}\) and the new row of
\(\Phi_{t+1}\) by (2.3). This completes one step.

Both inverse matrices in (2.4) and (2.6) are **finite triangular
polynomials**: their strictly lower triangular arguments have zero
\(t\)th powers. Thus there are no singular inverse matrices, infinite
series convergence restrictions, or time-step fixed-point equations in
this prescription. The top-left blocks of all covariance and memory
matrices agree with those already computed at earlier times.

On the test event \(M=0\), every \(R_j\) is zero. Consequently the
physical score (2.7) simplifies exactly to

\[
U_t\mid(M=0)=E_t+s q_tZ.
\tag{2.8}
\]

Equations (1.3), (1.5), and (1.6) now compute the deterministic test
covariance, risk, and exact calibration curve from this recursion.

## 3. Why these are the correct rectangular cumulants and memory formulas

The source convention matters. Wang--Zhong--Fan's singular-value law is
padded to the **row** dimension \(N\). It is not the feature-normalized
law of \(A_0^\top A_0\). Let its rectangular cumulants, with aspect
\(\rho=N/m\), be \(k_{2j}\). The correct sequence is

\[
\boxed{\qquad k_2=v,\qquad
k_{2j}=a^{2j}\delta^{j-1}\quad(j\ge2).\qquad}
\tag{3.1}
\]

Here is an independent formal-moment check. The feature population
covariance law is the image of \(\mathrm{MP}_\gamma\) under
\(x\mapsto\nu+a^2x\). Its ordinary free-cumulant series is

\[
R_H(u)=\nu+\frac{a^2}{1-a^2\gamma u}.
\]

Write \(M(z)=\sum_{j\ge1}m_{2j}z^j\) for row squared-singular moments,
and \(M_H\) for population covariance moments. The sample-covariance
moment relation gives
\(\rho M=M_H(\rho z(1+M))\). Combine this with
\(M_H(u)=u(1+M_H(u))R_H(u(1+M_H(u)))\). With
\(w=z(1+M)(1+\rho M)\), this yields

\[
M(z)=wR_H(\rho w)
    =\nu w+\frac{a^2w}{1-a^2\delta w}.
\]

The defining rectangular moment-cumulant relation is
\(M(z)=\sum_{j\ge1}k_{2j}w^j\). Coefficient comparison proves (3.1).
The first two row moments provide a separate normalization check:

\[
m_2=v,\qquad
m_4=v^2+\rho(v^2+a^4\gamma),
\quad k_4=m_4-(1+\rho)v^2=a^4\delta.
\tag{3.2}
\]

The input spectral comparison and sample-covariance moment law are
established in B03 Section 8 and independently source-audited by B05.

I checked Fan's equations (5.9)--(5.13), printed pages 19--20 of
arXiv:2008.11892v5, directly in the original PDF. Transposing his stored
memory matrices to the lower triangular convention used here gives

\[
\mathsf A=\sum_{j\ge0}k_{2j+2}\Psi(\Phi\Psi)^j,
\qquad
\mathsf B=\rho\sum_{j\ge0}k_{2j+2}\Phi(\Psi\Phi)^j.
\tag{3.3}
\]

His covariance formula is the sum of the corresponding terms in which
\(\Gamma\) or \(\Psi\Delta\Psi^\top\) is sandwiched between powers
of \(\Psi\Phi\), and, on the column side, \(\Delta\) or
\(\Phi\Gamma\Phi^\top\) is sandwiched between powers of
\(\Phi\Psi\), with the column factor \(\rho\). Inserting
\(k_{2j+2}=a^2h^j+\nu\mathbf1_{\{j=0\}}\) sums those finite
polynomials exactly to (2.4) and (2.6). For example, the first row
covariance sum factors as

\[
\nu\Gamma+a^2\sum_{r,s\ge0}
 h^{r+s}(\Psi\Phi)^r
 [\Gamma+h\Psi\Delta\Psi^\top]
 (\Phi^\top\Psi^\top)^s,
\]

which is (2.6). This checks the factor order, aspect ratio, and
transpose convention independently of a numerical comparison.

## 4. All state covariances are nondegenerate: no regularization gap

This section removes the potentially serious source-hypothesis gap.
The statement is for **every** fixed \(c>0\), not merely generic step
sizes. The ingredient that makes it possible is \(\nu>0\).

**Lemma 4.1.** At each positive finite time,
\(\Delta_t,\Omega_t,\Gamma_t,\Sigma_t\) are positive definite.

**Proof.** Initially \(\Delta_1=\pi/4>0\). Suppose
\(\Delta_t\succ0\), with all preceding state covariances already
defined. Formula (2.4) is a sum of positive semidefinite matrices and
gives

\[
\Omega_t\succeq\rho\nu\Delta_t\succ0.
\tag{4.1}
\]

By (2.5), the column vector is
\(B_{1:t}=\Psi_tG_{1:t}+q_{1:t}V\). The matrix \(\Psi_t\) is lower
triangular with every diagonal entry equal to \(\lambda>0\).
Independence of \(V\) and the Gaussian fields therefore gives

\[
\Gamma_t=\Psi_t\Omega_t\Psi_t^\top+q_{1:t}q_{1:t}^\top\succ0.
\tag{4.2}
\]

Formula (2.6) then gives

\[
\Sigma_t\succeq\nu\Gamma_t\succ0.
\tag{4.3}
\]

Conditional on \((M,Z,Y,E_1,\ldots,E_{t-1})\), the Gaussian field
\(E_t\) has strictly positive conditional variance. On the event
\(M=1\), which has probability \(\pi>0\), every \(R_j\), \(j\le t\),
is measurable with respect to this conditioning, whereas

\[
R_{t+1}=Y-\sigma\left(E_t+
           \sum_{j\le t}(\mathsf A_t)_{tj}R_j+s q_tZ\right)
\]

is a strictly nonconstant function of this fresh Gaussian innovation.
Its conditional variance is strictly positive. Hence it cannot equal a
linear combination of \(R_1,\ldots,R_t\) almost surely. Together with
\(\Delta_t\succ0\), this proves \(\Delta_{t+1}\succ0\), completing
the induction. All variables are square integrable: row residuals are
bounded and column variables are Gaussian affine functions with finite
coefficients at a fixed horizon. \(\square\)

Thus the zero network vector \(b^0=0\) never requires applying a
state-evolution theorem to a zero AMP initialization: its first matrix
query is initialized by \(R_1=M(Y-1/2)\), whose squared norm has the
strictly positive limit \(\pi/4\). Nor are linearly dependent later
column iterates a problem: (4.1)--(4.3) explicitly prove their required
Gram and Gaussian covariance matrices nonsingular.

A noise-perturbation/continuity proof would be an alternative. Invoking
such an argument without checking nonsingularity of the perturbed state
would leave a gap. The present direct induction makes that detour
unnecessary.

## 5. Exact GD-to-AMP reduction and source-hypothesis mapping

Rotate \(\theta=e_1\), write teacher coordinates \(z_i\) and
\(t_j=W_j^\top\theta\), and put \(v_j=\sqrt d\,t_j\). Let
\(A_0=H^0/\sqrt m\) be the feature matrix with this teacher coordinate
removed. B03 Proposition 4 proves

\[
H/\sqrt m=A_0+(s_d/m)zv^\top+o_P(1)_{\rm op},
\qquad s_d=a\sqrt{m/d}\to s.
\tag{5.1}
\]

The matrix \(A_0\) is independent of \((M,z,Y,v)\). With
\(w_t=\sqrt m\,b^t\), the limiting-constant physical iteration is

\[
w_0=0,\quad
q_t^{\rm emp}=m^{-1}v^\top w_t,\quad
r_t=M\odot\{Y-\sigma(A_0w_t+s q_t^{\rm emp}z)\},
\]
\[
\ell_{t+1}^{\rm emp}=N^{-1}z^\top r_t,\qquad
w_{t+1}=w_t+\lambda\{A_0^\top r_t+s\rho\ell_{t+1}^{\rm emp}v\}.
\tag{5.2}
\]

The differences between the constants at finite dimension and their
limits, and the operator error in (5.1), change the finitely many
iterates by \(o_P(\sqrt m)\) in coefficient norm and
\(o_P(\sqrt N)\) in score norm. This follows by subtracting the
updates, using bounded matrix operator norms, the \(1/4\)-Lipschitz
sigmoid, and bounded normalized residual/coefficient norms. The
comparison is only for a fixed number of iterations; its constant may
depend on \(T,c\).

For the AMP in Wang--Zhong--Fan equation (2.14), take its row iterate to
be \(R_t=r_{t-1}\), its column iterate to be \(B_t=w_t\), and define
fields by

\[
G_t^{\rm amp}=A_0^\top R_t-
                 \sum_{j<t}(\mathsf B_t)_{tj}B_j,
\quad
E_t^{\rm amp}=A_0B_t-
                 \sum_{j\le t}(\mathsf A_t)_{tj}R_j.
\tag{5.3}
\]

Use the coordinate nonlinearities (2.5) and (2.7), with deterministic
\(\ell_t,q_t\) computed in the state recursion. Substitution of
(5.3) cancels the two memory sums **exactly**. The resulting finite
algorithm is the physical GD (5.2) with its rank-one empirical overlaps
replaced by their deterministic state values. The addition of the
memory terms inside the nonlinearities is essential; simply deleting
the Onsager terms from a state-evolution theorem would be invalid.

There is no circular specification. At the beginning of time \(t\),
\(R_t\) and \(\ell_t\) are already known; (2.4)--(2.5) determine
\(B_t,q_t\); only then does (2.6)--(2.7) define \(R_{t+1}\).

The theorem-to-model mapping is:

| Wang--Zhong--Fan requirement | Verification here |
|---|---|
| Rectangular generalized invariance, Definition 2.20 | B03 Theorem 5 verifies Proposition D.1(b2) through clipped Gaussian concentration for all fixed matrix powers, then independent signed-permutation invariance. |
| Matching complete diagonal distribution, not just spectral law | The same proposition applies after the spectral match with the bi-orthogonally invariant Gaussian-product-plus-noise matrix. |
| Eventually bounded operator norm | B03's concentration/net bound has exponentially small failure probability, hence an eventual almost-sure deterministic bound. |
| Independent side information | Teacher-coordinate removal makes \(A_0\) independent of the row teacher/label/mask and column teacher coordinate. |
| Side empirical laws and polynomial density, Assumption 2.17 | Gaussian coordinates and finitely supported coordinates have exponential moments near zero; polynomial density follows by the analytic-transform argument described below. |
| Nonzero AMP initialization | \(\mathbb E R_1^2=\pi/4>0\). |
| Continuous, polynomial-growth nonlinearities uniformly Lipschitz in field arguments | Column updates are affine; row updates are bounded sigmoid compositions with finite memory. Extend the mask by a bounded continuous clipping function away from its actual \(\{0,1\}\) support. Labels are side coordinates, not a discontinuous sampling rule inside an update. |
| Positive singular second moment | \(\mathbb E D^2=v>0\), with the row-normalized convention. |
| Nonsingular \(\Omega_t,\Sigma_t\) | Lemma 4.1. |
| Exact source memory/covariance prescription | Section 3 checks Fan (5.9)--(5.13), yielding (2.4) and (2.6). |

For clarity concerning polynomial density, all coordinates of the side
law have a finite exponential moment of their absolute values in a
neighborhood of zero. If an \(L^2\) function were orthogonal to every
polynomial, its product with that probability measure would be a finite
signed measure with an exponential moment, by Cauchy--Schwarz. Its
analytic Fourier/Laplace transform would have every derivative zero at
the origin, hence would vanish and identify the signed measure as zero.
This proves the required density even though \(Y\) depends on \(Z\).
It is not necessary to pretend that the side coordinates are independent.

The source theorem therefore applies directly to the frozen-overlap AMP
and gives its joint empirical Wasserstein-2 limits.

### 5.1 Replacing frozen overlaps by the actual adaptive overlaps

This replacement is an additional argument, not an unstated extension
of the source theorem. Let bars denote the frozen-overlap iterates.
Empirical Wasserstein-2 convergence gives, at every fixed time,

\[
\epsilon_t^q=|m^{-1}v^\top\bar w_t-q_t|\to0,
\qquad
\epsilon_t^\ell=|N^{-1}z^\top\bar r_t-\ell_{t+1}|\to0.
\tag{5.4}
\]

The products are continuous tests with quadratic growth. Put
\(e_t=\|w_t-\bar w_t\|/\sqrt m\),
\(j_t=\|r_t-\bar r_t\|/\sqrt N\),
\(Z_N=\|z\|/\sqrt N\), and \(V_m=\|v\|/\sqrt m\).
On \(\|A_0\|_{\rm op}\le C\), direct subtraction gives

\[
j_t\le\tfrac14\{(C/\sqrt\rho+sZ_NV_m)e_t
                         +sZ_N\epsilon_t^q\},
\]
\[
e_{t+1}\le e_t+\lambda\{(C\sqrt\rho+s\rho V_mZ_N)j_t
                         +s\rho V_m\epsilon_t^\ell\}.
\tag{5.5}
\]

Since \(e_0=0\), \(Z_N,V_m\to1\), and the horizon is fixed,
(5.4)--(5.5) prove \(\max_{t\le T}(e_t+j_t)\to0\) in probability.
This establishes the same deterministic state law for the true adaptive
rank-one GD, then for the original RF model through (5.1).

## 6. From the appended test block to model-conditional test covariances

The original RF iteration, with the test mask identically zero, does not
use those test inputs in training. Conditional on \(\mathcal E_d\),
the appended inputs are therefore iid fresh Gaussians. B03's coefficient
bounds and Gaussian Poincare give, for each fixed time,

\[
\mathbb E_X[S_{t,d}^4\mid\mathcal E_d]
 \le5\|F\|_{\rm op}^4\|b^t\|_2^4=O_P(1).
\tag{6.1}
\]

Conditional variances show that the test empirical moments
\(n^{-1}\sum Z_iS_{t,d}(X_i)\) and
\(n^{-1}\sum S_{s,d}(X_i)S_{t,d}(X_i)\) differ from their conditional
population moments by \(o_P(1)\). On the other hand, the empirical
state law applied to the zero-mask block identifies their limits from
(2.8) as \(sq_t\) and \(\Sigma_{st}+s^2q_sq_t\). When using the full
row law to select that block, a bounded continuous function equal to
\(1-M\) at \(M\in\{0,1\}\) keeps the moment tests of quadratic
growth. This proves (1.4).

B03 Theorem 2 supplies joint conditional Gaussian approximation of the
finite fresh-test path with its realized-network covariance. Combining
it with (1.4) proves the joint weak limit in Theorem 1. Equivalently,
apply the dimension-free conditional characteristic-function bound from
B03 (4.6) to each fixed linear combination. Its small-Hessian error is
\(o_P(1)\), its conditional variance converges by (1.4), and bounded-class
localization of the tight gradient bounds yields conditional weak
convergence in probability. This argument does not infer almost-sure
uniform boundedness from a merely \(O_P(1)\) assumption. B03 Theorem 1
also gives \(\|b^t\|_2=O_P(1)\) and
\(\|b^t\|_\infty=O_P(\sqrt{\log d/d})\). Lemma 4.1 supplies
\(Q_{tt}-A_t^2=\Sigma_{tt}>0\). Corollary 3.1 of
`b04_calibration_transfer.md` therefore upgrades each teacher/score pair
to conditional TV convergence. Its signed-measure Lipschitz bound for
calibration proves (1.6), including convergence of the regression curve
integrated under the network's actual score law.

Risk convergence follows by truncating the logistic loss, using TV on
the bounded truncation, and controlling the tail by the score second
moment. The fixed-moment coefficient and matrix bounds in B03 make
these score moments uniformly bounded after averaging over the
environment, so the risk convergence is in \(L^1\), not merely in
probability. Gaussian conditioning gives (1.5).

Strict positivity in (1.6) follows from the noisy logistic-normal
calibration argument in B04 Section 5.2: nonpositive signal covariance
gives a constant/decreasing regression curve against an increasing
sigmoid; positive signal covariance gives a Gaussian-smoothed logistic
curve whose tail exponent and leading constant cannot both match an
unsmoothed logistic when its residual variance is positive.

This proves Theorem 1 using the verified matrix reduction and source
theorem, together with the independent total-variation transfer.

## 7. First-step algebraic verification

This check is independent of numerical quadrature. At \(t=1\),

\[
\Delta_1=\pi/4,\quad\Phi_1=0,\quad
\Omega_1=\rho v\pi/4,
\quad B_1=\lambda G_1+\lambda s\rho\pi\kappa V.
\]

Because \(\rho\pi=\alpha/\gamma\),

\[
q_1=c a\kappa/\sqrt\gamma,\qquad
A_1=sq_1=ca^2\kappa,
\]
\[
\Gamma_1=\frac{c^2v}{4\alpha\gamma}
             +\frac{c^2a^2\kappa^2}{\gamma},
\quad\Psi_1=\lambda.
\]

The first residual-score covariance from (2.6) is

\[
\begin{aligned}
\Sigma_1
 &=v\Gamma_1+a^4\delta\lambda^2\Delta_1\\
 &=c^2\left\{
 \frac{\kappa^2a^2v}{\gamma}
 +\frac{a^4+v^2/\gamma}{4\alpha}\right\}.
\end{aligned}
\tag{7.1}
\]

The forward memory term is \(\lambda vR_1\), which vanishes on every
test row. Thus (2.8) recovers exactly the independently audited original
first-step signal and all three variance contributions.

## 8. Independent Gaussian-query cross-check

The same deterministic law can be computed without free-cumulant
formulas by the Gaussian surrogate

\[
D_G=kAB^\top+\sqrt\nu\,C+(s/m)zv^\top,
\quad k=a/\sqrt\gamma,
\tag{8.1}
\]

where \(A\) is \(N\times d\), \(B\) is \(m\times d\), and
\(C\) is \(N\times m\), independently Gaussian with entry variances
\(1/d,1/d,1/m\), respectively. Removing one teacher coordinate
changes the finite coefficients by \(o(1)\) and does not change this
limiting prescription.

For a generic Gaussian matrix \(J\in\mathbb R^{u\times v}\) with
entry variance \(1/v\), store past forward inputs \(V\) and outputs
\(Y=JV\), and past backward inputs \(U\) and outputs \(Z=J^\top U\).
All products in the following rules are expectations on the appropriate
row or column scalar space. For a new forward input \(f\), set

\[
\alpha=(\mathbb E VV^\top)^+\mathbb E[Vf],\quad
f_\perp=f-\alpha^\top V,\quad
\beta=\frac vu(\mathbb E UU^\top)^+
                         \mathbb E[Zf_\perp].
\]

The new forward output law is

\[
\alpha^\top Y+\beta^\top U+
              \sqrt{\mathbb E f_\perp^2}\,G_{\rm new}.
\tag{8.2}
\]

For a new backward input \(g\), set

\[
\alpha=(\mathbb E UU^\top)^+\mathbb E[Ug],\quad
g_\perp=g-\alpha^\top U,\quad
\beta=\frac uv(\mathbb E VV^\top)^+
                         \mathbb E[Yg_\perp].
\]

The new backward output law is

\[
\alpha^\top Z+\beta^\top V+
              \sqrt{\frac uv\mathbb E g_\perp^2}\,G_{\rm new}.
\tag{8.3}
\]

Each new Gaussian is independent of the transcript on its scalar space.
For nonsingular input Gram matrices these formulas follow directly from
the exact conditional Gaussian mean

\[
\mathbb E[J\mid JV=Y,J^\top U=Z]
 =Y(V^\top V)^{-1}V^\top
   +U(U^\top U)^{-1}Z^\top P_{V^\perp},
\]

and residual \(P_{U^\perp}\widetilde J P_{V^\perp}\). The finite
rank output projections are negligible for empirical laws. The factors
\(v/u\) and \(u/v\) in (8.2)--(8.3) come from normalizing the
different coordinate-space Gram matrices; omitting them gives the wrong
first-step variance.

For a computational implementation with degenerate queries, add a fresh
independent Gaussian input of size \(\varepsilon\) to each query,
apply the rules with ordinary inverses, and let \(\varepsilon\downarrow0\)
after the finite-horizon recursion. Each perturbed input has conditional
innovation variance at least \(\varepsilon^2\), and matrix-operator
bounds plus the finite Lipschitz program give an \(O_T(\varepsilon)\)
comparison in normalized Euclidean norm. Thus this prescription has a
well-defined limit even when directly evaluating a pseudoinverse is
numerically ill conditioned. This auxiliary query regularization is not
needed for the AMP proof in Sections 2--6.

Execute the actual GD program using the three matrix query ledgers:

\[
p_t=B^\top w_t,\quad x_t=Ap_t,\quad c_t=Cw_t,
\quad U_t=kx_t+\sqrt\nu c_t+s\mathbb E[Vw_t]Z,
\]
\[
r_t=M(Y-\sigma U_t),\quad
l_t=A^\top r_t,\quad f_t=Bl_t,\quad e_t=C^\top r_t,
\]
\[
w_{t+1}=w_t+\lambda\{k f_t+\sqrt\nu e_t
                         +s\rho\mathbb E[Zr_t]V\}.
\tag{8.4}
\]

At the first step the independent calculation gives

\[
\mathbb E w_1^2=\frac{c^2a^2\kappa^2}{\gamma}
                   +\frac{c^2v}{4\alpha\gamma},
\]
\[
\mathbb E p_1^2=
\frac{c^2a^2\gamma}{4\alpha}+c^2a^2\kappa^2
                   +\frac{c^2v}{4\alpha}.
\]

The test residual variance is
\(k^2\mathbb E p_1^2+\nu\mathbb E w_1^2\), which simplifies to
(7.1). This supplies another independent check on normalization and
the causal use of the same matrices at every step.

## 9. Primary sources and acceptance boundary

The sources actually inspected are:

* Tianhao Wang, Xinyi Zhong, Zhou Fan,
  [*Universality of Approximate Message Passing algorithms and tensor networks*, arXiv:2206.13037v5](https://arxiv.org/html/2206.13037v5):
  Definition 2.20, Proposition D.1(b2), Assumption 2.17, Theorem 2.22,
  and Appendix D.1.
* Zhou Fan,
  [*Approximate Message Passing algorithms for rotationally invariant matrices*, arXiv:2008.11892v5](https://arxiv.org/pdf/2008.11892):
  Section 5, specifically (5.9)--(5.13), Theorem 5.3, Corollary 5.4,
  and the degeneracy discussion. The exact finite sums were checked in
  the original page images.
* Cosme Louart, Zhenyu Liao, Romain Couillet,
  [*A Random Matrix Approach to Neural Networks*, arXiv:1702.05419v2](https://arxiv.org/pdf/1702.05419):
  the spectral comparison used by B03/B05, not an unsupported direct
  dynamical universality claim.

The central acceptance point is that the proof does not substitute a
spectral law for the full generalized-invariance hypotheses, does not
replace GD by AMP without algebraic cancellation, and does not ignore
degenerate state covariances. Each of those three obligations is
explicitly handled above. The remaining distinction is fixed finite
time versus a theorem uniform over arbitrarily late stopping times.
