# Gaussian first-step calibration consequences and precise probability guarantees

23 October 2026. A29. No subagents. This note proves the scalar Gaussian consequences and their valid transfer from A26's first-step joint and two-test-replica CLTs in followup/T357_gaussian_first_step_attempt.md, final SHA256 1469aad3c34b902a363fe66d32eff199c451adc28d2ae5ae4de6cbb716fd630b. A28 independently reviewed the mathematically identical substantive version with SHA256 9e6647ba2ed3e8246f2dd54fd8709dc3dd179c4b61e2b16cecc1eaf53cbd28c5; final changes clarify status, label notation, and witness measurability. This note does not independently certify the CLTs. Sections 2–7 explicitly isolate what the one-test annealed limit proves; Section 8 uses the separately proved replica result.

**Result:** every fixed positive first-step rate has a strictly positive asymptotic lower bound on population calibration error, with probability tending to one. Population log-loss converges in $L^1$ over trained predictors. An explicit nonempty interval of small positive rates improves that loss while retaining a positive calibration lower bound; large rates have signed average overconfidence. The unique zero of the signed statistic is not a calibrated predictor. The high-probability statements use the two-test-replica theorem, not merely the annealed CLT. These are first-step results, not a full training trajectory or optimal-stopping theorem.

## 1. Model and exact probabilistic input

Use A26's Gaussian-input, logistic-teacher, tanh random-feature model, with $n/d\to\alpha>0$, $m/d\to\gamma>0$, unit teacher direction, and informative signal $\beta>0$. For independent standard normals $Z,G$, put

\[
a=\mathbb E[G\tanh G],\quad b=\mathbb E[\tanh^2G],\quad
\mu=\mathbb E[Z\{\sigma(\beta Z)-1/2\}],
\]
\[
k=a^2\mu,\qquad
\tau^2=\frac{\mu^2a^2b}{\gamma}
       +\frac{a^4+b^2/\gamma}{4\alpha},\qquad
U=kZ+\tau G,\qquad V=k^2+\tau^2.                 \tag{1}
\]

Here $b$ is the full feature second moment, not its higher-Hermite residual. The correspondence with A26's notation is $(a,b,\mu)=(a_1,v,\kappa)$. For tanh, $a=1-b>0$, and Gaussian integration by parts gives $\mu=\beta\mathbb E\sigma'(\beta Z)>0$. In particular $k,\tau,V>0$.

Let $\mathcal F_d$ contain the training data and features. For a fresh test example define

\[
U_d=\frac dn\sum_{i=1}^n(Y_i-1/2)K_m(X_0,X_i),
\quad S_{1,d}=cU_d,\quad Q_d=\sigma(cU_d).          \tag{2}
\]

This is mean-loss GD at rate $cd$ for the $m^{-1/2}$ readout, or rate $cd/m$ for the raw readout. The probabilistic input is the **annealed** convergence

\[
(Z_0,U_d)\Longrightarrow(Z,U),\qquad
Z_0=\theta_d^\top X_0.                            \tag{H1}
\]

The fresh label has conditional mean $\sigma(\beta Z_0)$ given $X_0,\mathcal F_d$. Hence bounded expectations involving the label follow by replacing it with this mean; no convergence of conditional calibration curves is needed.

The population quantities for each realized trained predictor are

\[
\operatorname{CE}_d(\mathcal F_d)=
\mathbb E\!\left[
 \left|\mathbb E[Y_0\mid Q_d,\mathcal F_d]-Q_d\right|
 \,\middle|\,\mathcal F_d\right],
\quad
L_d(\mathcal F_d)=
\mathbb E[\log(1+e^{cU_d})-Y_0cU_d\mid\mathcal F_d].       \tag{3}
\]

Until the two-test result is invoked in Section 8, finite-network conclusions concern expectations over $\mathcal F_d$.

## 2. Bounded witnesses transfer calibration lower bounds

For every deterministic measurable $h:\mathbb R\to[-1,1]$, $U_d=c^{-1}\operatorname{logit}Q_d$ is score-measurable when $c>0$. Conditional expectation therefore gives

\[
\operatorname{CE}_d(\mathcal F_d)
\ge\left|\mathbb E[(Y_0-Q_d)h(U_d)\mid\mathcal F_d]\right|,
\qquad
\mathbb E\operatorname{CE}_d
\ge\left|\mathbb E[(Y_0-Q_d)h(U_d)]\right|.              \tag{4}
\]

For bounded continuous $h$, the final expectation converges under (H1). It also converges for $h(u)=\operatorname{sign}u$, since $U\sim N(0,V)$ has no mass at its only discontinuity.

Gaussian conditioning gives the limiting regression function

\[
g(u)=\mathbb E[Y\mid U=u]
=\mathbb E_H\sigma(\lambda u+sH),\qquad
\lambda=\frac{\beta k}{V}>0,\quad
s=\frac{\beta\tau}{\sqrt V}>0,                         \tag{5}
\]

where $H$ is standard normal. Define $d_c(u)=g(u)-\sigma(cu)$ and $C_G(c)=\mathbb E|d_c(U)|$. Both functions in $d_c$ are continuous. For each positive integer $r$, the bounded continuous witness $h_r(u)=\tanh(r\,d_c(u))$ gives

\[
\liminf_{d\to\infty}\mathbb E\operatorname{CE}_d
\ge\mathbb E[d_c(U)\tanh(r\,d_c(U))].
\]

The integrand increases to $|d_c(U)|$. Taking the supremum of these separate lower bounds proves

\[
\boxed{\liminf_{d\to\infty}\mathbb E\operatorname{CE}_d
\ge C_G(c).}                                           \tag{6}
\]

This is a lower bound, not exact CE convergence. No equality of annealed and model-conditional calibration is asserted. The simpler witness $h=d_c$ also yields the computable lower bound

\[
\liminf_d\mathbb E\operatorname{CE}_d
\ge\mathbb E[d_c(U)^2].                                \tag{7}
\]

## 3. No positive rate perfectly calibrates the noisy informative Gaussian model

**Proposition.** If $\beta,k,\tau>0$, then $C_G(c)>0$ for every $c>0$.

**Proof.** If $C_G(c)=0$, positivity of the Gaussian density and continuity would imply $g(u)=\sigma(cu)$ for every real $u$. But

\[
e^{\lambda u}\{1-g(u)\}
=\mathbb E_H\frac{e^{-sH}}{1+e^{-\lambda u-sH}}
\longrightarrow e^{s^2/2}\qquad(u\to+\infty).          \tag{8}
\]

Dominated convergence applies with integrable bound $e^{-sH}$. The logistic tail satisfies $e^{cu}\{1-\sigma(cu)\}\to1$. Equality first forces $c=\lambda$ by the exponential rates, and then $e^{s^2/2}=1$ by the leading constants, contradicting $s>0$. Thus $d_c$ is nonzero on an open set of positive Gaussian probability. Both $C_G(c)$ and the square-witness bound in (7) are strictly positive. $\square$

The noise hypothesis is essential: at $\tau=0,k>0$, the noiseless model is calibrated at $c=\beta/k$. At exactly $c=0$, the constant predictor is calibrated under the symmetric teacher. Neither exception applies to a positive step under (1).

## 4. Signed error: a unique sign change is not calibration

Define

\[
B(c)=\mathbb E[(\sigma(\beta Z)-\sigma(cU))\operatorname{sign}U].
                                                               \tag{9}
\]

The sign witness proves $\liminf_d\mathbb E\operatorname{CE}_d\ge|B(c)|$. Write $B_0=\lim_{c\downarrow0}B(c)$. Conditioning on $Z$ gives

\[
B_0=\mathbb E[
(\sigma(\beta Z)-1/2)\{2\Phi(kZ/\tau)-1\}]
\in(0,1/2).                                             \tag{10}
\]

The factors have the same strict sign away from zero; the strict upper bound follows from $|\sigma(\beta Z)-1/2|<1/2$. Symmetry of $U$ yields

\[
B(c)=B_0-\mathbb E[\sigma(c|U|)-1/2],\qquad
B'(c)=-\mathbb E[|U|\sigma'(cU)]<0,\qquad
B(\infty)=B_0-1/2<0.                                    \tag{11}
\]

Differentiation uses $\sigma'\le1/4$ and $\mathbb E|U|<\infty$; the limit uses dominated convergence. There is exactly one $c_{\rm sign}\in(0,\infty)$ with $B(c_{\rm sign})=0$. Section 3 proves that this predictor is still miscalibrated, and (6) gives a positive expected-CE lower bound even there.

The binary top-probability signed overconfidence statistic is $-B(c)=\mathbb E[(\sigma(cU)-Y)\operatorname{sign}U]$. Thus small $c$ is underconfident on average and sufficiently large $c$ is overconfident on average. No uniform sign at every score is asserted.

## 5. An explicit nonempty risk-improving, miscalibrated regime

Put

\[
A=\mathbb E[(\sigma(\beta Z)-1/2)U]
=k\mu=a^2\mu^2>0,\qquad m_1=\mathbb E|U|=\sqrt{2V/\pi}.
\]

The limiting log-loss is $L(c)=\mathbb E[\log(1+e^{cU})-cU\sigma(\beta Z)]$. The global logistic Taylor bound and sigmoid Lipschitz constant give

\[
L(c)\le\log2-cA+c^2V/8,\qquad
B(c)\ge B_0-cm_1/4.                                    \tag{12}
\]

Hence the nonempty interval

\[
0<c\le c_{\rm small}:=
\min\left\{\frac{4A}{V},\frac{2B_0}{m_1}\right\}          \tag{13}
\]

guarantees

\[
L(c)\le\log2-cA/2<\log2,\qquad
B(c)\ge B_0/2>0,\qquad C_G(c)\ge B_0/2.                 \tag{14}
\]

Even the integral for $B_0$ can be replaced by an elementary lower bound. For any fixed $r>0$, restricting (10) to $|Z|\ge r$ gives

\[
B_0\ge b_r:=
2\overline\Phi(r)\{\sigma(\beta r)-1/2\}
                 \{2\Phi(kr/\tau)-1\}>0.                \tag{15}
\]

Replace $B_0$ in (13) by $b_r$ to obtain $B(c),C_G(c)\ge b_r/2$. The choice $r=1$ is concrete. Under (H1) and the moment bound in Section 7, the finite-network conclusions are

\[
\lim_d\mathbb E L_d=L(c)\le\log2-cA/2,\qquad
\liminf_d\mathbb E\operatorname{CE}_d\ge B_0/2,           \tag{16}
\]

or $b_r/2$ under the elementary version. These are fixed positive risk and calibration gaps for fixed parameters and $c>0$. Subtracting the same Bayes loss $\mathbb E h(\sigma(\beta Z))$ gives the identical improvement in excess log-loss.

## 6. Explicit large-rate overconfidence and optimal first-step rate

Let $e=1/2-B_0>0$, the error of the sign classifier. Then

\[
-B(c)=e-\mathbb E(1+e^{c|U|})^{-1}
\ge e-\frac{\sqrt{2/\pi}\log2}{c\sqrt V}.                \tag{17}
\]

Indeed, the folded-normal density is bounded by $\sqrt{2/\pi}/\sqrt V$, and $\int_0^\infty(1+e^{cx})^{-1}dx=(\log2)/c$. Thus
$c\ge2\sqrt{2/\pi}\log2/(e\sqrt V)$ guarantees signed overconfidence at least $e/2$ and the same expected-CE lower bound.

For a wholly elementary threshold, the sign classifier cannot beat Bayes classification error. For any $r>0$,

\[
e\ge\mathbb E\sigma(-\beta|Z|)
\ge e_r:=(2\Phi(r)-1)\sigma(-\beta r)>0.                 \tag{18}
\]

Therefore $c\ge2\sqrt{2/\pi}\log2/(e_r\sqrt V)$ suffices for $-B(c)\ge e_r/2$.

There is also a precise **first-step rate** optimum:

\[
L(c)=\mathbb E\log(2\cosh(cU/2))-cA,\quad
L'(0)=-A<0,\quad
L''(c)=\mathbb E[U^2\sigma'(cU)]>0,\quad
L'(\infty)=m_1/2-A>0.                                  \tag{19}
\]

The last inequality follows from
$A=\mathbb E[(\sigma(\beta Z)-1/2)U]<\mathbb E|U|/2$.
Hence a unique finite positive rate $c_{\rm risk}$ minimizes one-step limiting log-loss and is miscalibrated by Section 3. This is optimization over the first-step rate, not over GD stopping times.

## 7. Independent uniform-integrability check for expected risk

A26 asserts $\sup_d\mathbb E U_d^2<\infty$. Here is a direct verification independent of the delicate covariance-equivalence limit.

Let $F$ have rows $W_j^\top$, $h(x)=\tanh(Fx)$, and $\Sigma_F=\mathbb E_X h(X)h(X)^\top$. Oddness gives zero feature means. Gaussian covariance interpolation gives, for differentiable $f,g$,

\[
\operatorname{Cov}(f(X),g(X))
=\int_0^1\mathbb E[
\nabla f(X)\cdot\nabla g(tX+\sqrt{1-t^2}X')]\,dt,         \tag{20}
\]

where $X,X'$ are independent standard Gaussians. Differentiate the covariance interpolation and integrate by parts to obtain the identity; bounded logistic and tanh derivatives justify the operations here. Apply it to $f=g=v^\top h$, whose gradient norm is at most $\|F\|_{\rm op}\|v\|$, obtaining $\Sigma_F\preceq\|F\|_{\rm op}^2I_m$.

For $r_j=\mathbb E[(\sigma(\beta\theta_d^\top X)-1/2)h_j(X)]$, (20) also gives

\[
|r_j|\le(\beta/4)|W_j^\top\theta_d|,\qquad
\|r\|^2\le(\beta^2/16)\|F\theta_d\|^2.
\]

Condition on $F,X_0$ and separate the training mean and variance in (2):

\[
\begin{aligned}
\mathbb E U_d^2
&\le\frac{d^2}{4nm}\mathbb E\|F\|_{\rm op}^2
 +\frac{\beta^2d^2}{16m^2}
   \mathbb E[\|F\|_{\rm op}^2\|F\theta_d\|^2]\\
&\le\frac{d^2}{4nm}\mathbb E\|F\|_{\rm op}^2
 +\frac{\beta^2d^2}{16m^2}\mathbb E\|F\|_{\rm op}^4
=O(1).                                                 \tag{21}
\end{aligned}
\]

For the variance term use $(Y_i-1/2)^2=1/4$ and $\|h(X_0)\|^2\le m$. For the mean term first integrate $X_0$ to obtain $d^2r^\top\Sigma_Fr/m^2$. Gaussian matrix norm moments are uniformly bounded at bounded $m/d$: fixed bilinear forms have variance $1/d$, and $1/4$-nets on both unit spheres combined with the Gaussian tail give an exponentially decaying norm tail above a constant. Integration bounds the second and fourth moments.

The nonnegative logistic loss is at most $\log2+c|U_d|$. Thus (21) implies uniform integrability, and (H1) gives convergence of **expected** population risk to $L(c)$. This does not itself give concentration over trained networks.

## 8. Two-test replicas give concentration over trained predictors

A26's Section 8 proves the additional input: two fresh test points sharing $\mathcal F_d$ converge jointly to **independent copies** of $(Z,U)$ in (H1), with their fresh labels. Its equation (19) is the replica limit, and equations (28)–(29) give concentration of fixed bounded test observables. This is a separate substantive result from (H1).

For a bounded witness let $T_d(h)=\mathbb E[(Y_0-Q_d)h(U_d)\mid\mathcal F_d]$. The one-test limit gives its mean, and the two-test limit gives $\mathbb E[T_d(h)^2]\to T(h)^2$, because the test examples are independent conditional on $\mathcal F_d$. Hence $T_d(h)\to T(h)$ in $L^2$.

The sign witness then gives $T_d(\operatorname{sign})\to B(c)$ in $L^2$ and a calibration lower bound $|B(c)|$ in probability. Using the continuous $h_r$ from Section 2 and choosing a fixed sufficiently large $r$ gives, for every $\varepsilon>0$,

\[
\Pr\{\operatorname{CE}_d\ge C_G(c)-\varepsilon\}\to1.     \tag{22}
\]

This still does not imply exact CE convergence. Applying the two-test argument to bounded truncated losses gives $L^2$ convergence of their conditional expectations. The uniform integrability from (21) makes the expected conditional tail uniformly small. The triangle inequality, followed by the truncation level tending to infinity, therefore proves the stronger statement

\[
\mathbb E_{\mathcal F_d}|L_d(\mathcal F_d)-L(c)|\to0.
\tag{23}
\]

For every fixed $c$ in (13), (14), (22), and (23) imply, for example,

\[
\Pr\!\left\{
L_d\le\log2-\frac{cA}{4},\
\operatorname{CE}_d\ge\frac{B_0}{4}
\right\}\longrightarrow1.                            \tag{24}
\]

Under the elementary small-rate restriction use $b_r/4$ in place of $B_0/4$. The slack factors avoid incorrectly placing the limiting quantities exactly at a probability threshold. Likewise, a large-rate threshold from (17) or (18) gives signed overconfidence at least $e/4$ or $e_r/4$ with probability tending to one. Every fixed $c>0$, including $c_{\rm sign}$ and $c_{\rm risk}$, satisfies the universal positive calibration lower bound (22). Without the replica result, only the annealed conclusions in the earlier sections would be justified.

## 9. Uncertified numerical illustration and scope

For illustration, take $\alpha=3,\gamma=2,\beta=2$. The identity $\sigma(2z)-1/2=\tanh(z)/2$ gives $\mu=a/2$ exactly. All decimals below come from floating-point Gaussian quadrature and root finding without certified quadrature-error bounds. They are not used in any proof or claimed as a certified numerical parameter instance. The quadrature gives:

| Quantity | Approximate value |
|---|---:|
| $a$ | 0.6057055096022 |
| $b$ | 0.3942944903978 |
| $\mu$ | 0.3028527548011 |
| $k$ | 0.1111103656063 |
| $\tau^2$ | 0.0243285534525 |
| $V$ | 0.0366740667977 |
| $A$ | 0.0336500803108 |
| $B_0$ | 0.1454401655522 |
| $b_1$ from (15) | 0.0632857932533 |
| elementary small-rate upper bound | 0.8283552449937 |
| $c_{\rm sign}$ | 4.1663154926067 |
| $c_{\rm risk}$ | 4.1924380517088 |

These values suggest that $c=0.4$ lies inside the elementary interval. If the exact interval condition is checked, the symbolic theorem gives expected log-loss improvement at least $0.2A$ and expected CE at least $b_1/2$; their quadrature estimates are approximately $0.0067300161$ and $0.0316428966$. The interval membership and these decimal estimates are illustrative, not certified numerical inequalities. At the numerically located $c_{\rm sign}$, quadrature gives the square-witness expectation in (7) about $3.25\cdot10^{-6}$; strict positivity at the exact signed root is proved analytically and does not depend on this calculation.

This is a nonvacuous comparison between initialization and one genuine GD step, using the separately audited first-step and replica CLTs. It does not characterize subsequent iterates, locate a risk-optimal stopping time, show that every useful later stop is miscalibrated, or prove finite-dimensional exact-CE convergence. The rates are fixed constants; dimension-dependent or data-selected rates are not covered by the pointwise convergence statements. It uses Gaussian inputs and actual tanh features, but remains a one-step result. No publication novelty or whole-T357 closure is claimed.
