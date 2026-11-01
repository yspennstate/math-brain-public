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
