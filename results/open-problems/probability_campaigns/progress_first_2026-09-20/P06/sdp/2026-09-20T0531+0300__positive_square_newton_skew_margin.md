Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated completed-run reasoning telemetry is unavailable, so I do not claim otherwise.**

# P06 complementary P07 iteration — positive square-Newton repair and a directional-skew closure criterion

Status: **P06 SOURCE KNOWN / no novelty claim for Conjecture 17. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.  
Captured pre-write `master`: `1826d7b9debc1ed52fc92fa96422ab312813d138`.  
No P07-A/P07-B canonical claim or peer report is modified. This remains a complementary SDP/moment-polytope line.

## 1. Fixed source metric and inherited bottleneck

P06 / Randomstrasse Conjecture 17 remains a **KNOWN** later-literature endpoint, with repository metric

`U_ER^cert = 1`.

I do not rescreen it.

For P07 / Randomstrasse Conjecture 18, the inherited full-source bound remains

\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

Hence the source-level iterated-log loss is unchanged in this run.

The preceding complementary reports established, on odd prime orders, a Gibbs seed

\[
p_{D,c}(j)\propto \exp\!\left(-\frac{c}{\sqrt n}S_D(j)\right),
\qquad
S_D(j)=\sum_{a\in D}\cos(2\pi aj/n),
\]

together with sharp partition self-averaging, an exact total Fourier-energy identity, an annealed selected-energy formula, and an exact **linear** Newton repair. If

\[
\mu=\mathbb E_p\Phi,
\qquad
r=\mu-t,
\qquad
\Sigma=\operatorname{Cov}_p(\Phi),
\qquad
h=-\Sigma^{-1}r,
\]

and

\[
g(j)=h^T(\Phi(j)-\mu),
\]

then the signed law `p(1+g)` has the target moments exactly. The preceding run therefore targeted the pointwise condition `g>=-1`, or a bounded one-sided distortion along a damped path.

The present run changes that correction architecture. The pointwise lower bound is **not necessary**. There is a positivity-preserving quadratic update whose first-order term is the same exact Newton repair. Its error is governed by one source-coupled third central moment rather than by the worst time-coordinate of `g`. A small regularization then prevents covariance collapse. This yields a new exact deterministic closure criterion for P07 in terms of a directional skewness margin.

No finite SDP experiment is used as proof below.

---

# 2. Positive square-Newton identity

The next theorem is deterministic and does not use the circulant model.

Let `Omega` be a finite set, let `p` be a probability law on `Omega`, and let

\[
\Phi:\Omega\to\mathbb R^m
\]

be any feature map. Fix a target `t in R^m`. Write

\[
\mu=\mathbb E_p\Phi,
\qquad
r=\mu-t,
\qquad
X=\Phi-\mu,
\qquad
\Sigma=\mathbb E_p[XX^T].
\tag{2.1}
\]

Assume `Sigma` is positive definite and define the Newton vector and score

\[
h=-\Sigma^{-1}r,
\qquad
g=h^TX.
\tag{2.2}
\]

Then

\[
\mathbb E_pg=0,
\qquad
\mathbb E_p[Xg]=-r.
\tag{2.3}
\]

Put

\[
\nu^2:=\mathbb E_pg^2=r^T\Sigma^{-1}r
\tag{2.4}
\]

and define the source-coupled third-cumulant vector

\[
\tau:=\mathbb E_p[Xg^2].
\tag{2.5}
\]

## Theorem 2.1 — exact positive quadratic repair

For every real `alpha`, define

\[
p_\alpha^+(\omega)
:=
\frac{p(\omega)(1+\alpha g(\omega))^2}
{1+\alpha^2\nu^2}.
\tag{2.6}
\]

Then `p_alpha^+` is automatically a probability law, with no pointwise sign condition on `g`. Its target residual is exactly

\[
\boxed{
 r_\alpha^+
 =
 \frac{(1-2\alpha+\alpha^2\nu^2)r+\alpha^2\tau}
 {1+\alpha^2\nu^2}.
}
\tag{2.7}
\]

### Proof

Because `E_p g=0`,

\[
\mathbb E_p(1+\alpha g)^2=1+\alpha^2\nu^2,
\]

so (2.6) is normalized and nonnegative. Also

\[
\mathbb E_p[\Phi g]
=\mathbb E_p[(X+\mu)g]
=\mathbb E_p[Xg]
=-r.
\]

Finally,

\[
\mathbb E_p[\Phi g^2]
=\mu\nu^2+\tau.
\]

Therefore

\[
\begin{aligned}
\mu_\alpha^+
&=\frac{\mu+2\alpha\mathbb E_p[\Phi g]
+\alpha^2\mathbb E_p[\Phi g^2]}
{1+\alpha^2\nu^2}\\
&=\frac{\mu-2\alpha r+\alpha^2(\mu\nu^2+\tau)}
{1+\alpha^2\nu^2}.
\end{aligned}
\]

Substituting `mu=t+r` and subtracting `t` gives (2.7). ∎

This identity is the main progress of the run. The linear repair `p(1+g)` is exact but may be signed; the square repair is always positive and retains an exact algebraic residual formula.

---

# 3. New optimal cancellation: remove the entire old residual term

Assume

\[
0<\nu^2<1.
\tag{3.1}
\]

The coefficient of `r` in (2.7) vanishes when

\[
1-2\alpha+\alpha^2\nu^2=0.
\]

Choose the smaller positive root

\[
\boxed{
\alpha_*(\nu)
=\frac{1}{1+\sqrt{1-\nu^2}}
\in\left(\frac12,1\right).
}
\tag{3.2}
\]

Then the positive update has the exact residual

\[
\boxed{
 r^+
 =\frac{\alpha_*}{2}\,\tau
 =\frac{\tau}{2(1+\sqrt{1-\nu^2})}.
}
\tag{3.3}
\]

Indeed

\[
\alpha_*^2\nu^2
=\frac{1-\sqrt{1-\nu^2}}
{1+\sqrt{1-\nu^2}},
\]

and hence

\[
\frac{\alpha_*^2}{1+\alpha_*^2\nu^2}
=\frac{\alpha_*}{2}.
\]

Thus the old residual `r` is canceled **exactly**. The only remaining obstruction is the third central moment in the actual Newton direction.

This is qualitatively different from the previous one-sided-max target. A rare time point at which `g` is very negative is harmless to positivity because the update uses a square. The proof obligation is now an averaged, source-coupled third-moment estimate.

---

# 4. Directional skewness and a covariance-stable regularized iteration

Define the Mahalanobis norm

\[
\|v\|_{\Sigma^{-1}}=(v^T\Sigma^{-1}v)^{1/2}.
\]

The Newton decrement is exactly

\[
\nu=\|r\|_{\Sigma^{-1}}.
\]

Define the **directional skew ratio**

\[
\boxed{
\Gamma(p,t)
:=
\frac{\|\tau\|_{\Sigma^{-1}}}{\nu^2}
}
\tag{4.1}
\]

when `nu>0`.

By (3.3), after the unregularized positive square step,

\[
\boxed{
\|r^+\|_{\Sigma^{-1}}
=
\frac{\Gamma\nu^2}
{2(1+\sqrt{1-\nu^2})}.
}
\tag{4.2}
\]

The metric in (4.2) is the **old** covariance metric. To iterate without assuming that the square factor is bounded below, mix a fraction of the old law back in. For `eta in (0,1)`, set

\[
\widehat p=(1-\eta)p^++\eta p.
\tag{4.3}
\]

Let `widehat Sigma` and `widehat r` be its covariance and residual. The covariance of a mixture obeys

\[
\boxed{
\widehat\Sigma\succeq\eta\Sigma.
}
\tag{4.4}
\]

This is exact: the mixture covariance equals the weighted sum of the two component covariances plus the positive-semidefinite between-means term.

Also

\[
\widehat r=(1-\eta)r^++\eta r.
\]

Therefore

\[
\begin{aligned}
\widehat\nu
&:=\|\widehat r\|_{\widehat\Sigma^{-1}}\\
&\le \eta^{-1/2}\|\widehat r\|_{\Sigma^{-1}}\\
&\le
\sqrt\eta\,\nu
+\frac{1-\eta}{\sqrt\eta}
\frac{\Gamma\nu^2}
{2(1+\sqrt{1-\nu^2})}.
\end{aligned}
\tag{4.5}
\]

Put

\[
A:=
\frac{\Gamma\nu}
{2(1+\sqrt{1-\nu^2})}.
\tag{4.6}
\]

Then

\[
\boxed{
\frac{\widehat\nu}{\nu}
\le
\sqrt\eta+A\frac{1-\eta}{\sqrt\eta}.
}
\tag{4.7}
\]

Writing `y=sqrt(eta)`, the right side is

\[
(1-A)y+\frac A y.
\]

If

\[
\boxed{A<\frac12,}
\tag{4.8}
\]

the minimizing choice is

\[
\boxed{
\eta_*=rac{A}{1-A},
}
\tag{4.9}
\]

and gives the strict contraction

\[
\boxed{
\frac{\widehat\nu}{\nu}
\le 2\sqrt{A(1-A)}<1.
}
\tag{4.10}
\]

This is an exact deterministic replacement for the previous pointwise condition `max(-g)_+=O(1)`.

## Corollary 4.1 — iterative closure under a skew margin

Suppose an iteration starts from a law with positive-definite covariance and, until the target is reached, every current pair `(p_k,t)` obeys

\[
\nu_k<1,
\qquad
A_k\le A_*<\frac12.
\tag{4.11}
\]

At each step use the positive square update (3.2) and then the covariance-preserving mixture (4.3) with `eta_k=A_k/(1-A_k)`. Then

\[
\nu_{k+1}
\le q_*\nu_k,
\qquad
q_*:=2\sqrt{A_*(1-A_*)}<1.
\tag{4.12}
\]

Every finite-step covariance remains positive definite by (4.4), and `nu_k->0` geometrically. Since the probability simplex is compact, a convergent subsequence of the laws has moment vector exactly `t`. Thus the target lies in the moment polytope.

This criterion is finite-dimensional and exact. It does **not** assert that the random-circulant source satisfies (4.11); proving that is now the probabilistic bottleneck.

---

# 5. A fourth-moment sufficient condition

The directional skew ratio has an immediate source-useful upper bound. Define the actual Newton-score kurtosis

\[
K:=\frac{\mathbb E_pg^4}{(\mathbb E_pg^2)^2}
=\frac{\mathbb E_pg^4}{\nu^4}.
\tag{5.1}
\]

For any vector `u` with `u^T Sigma u<=1`, Cauchy-Schwarz gives

\[
\begin{aligned}
u^T\tau
&=\mathbb E_p[(u^TX)g^2]\\
&\le
\sqrt{\mathbb E_p(u^TX)^2}\,
\sqrt{\mathbb E_pg^4}\\
&\le\sqrt{\mathbb E_pg^4}.
\end{aligned}
\]

Taking the dual supremum over the covariance unit ball yields

\[
\boxed{
\Gamma\le\sqrt K.
}
\tag{5.2}
\]

Hence the simpler directional-kurtosis condition

\[
\boxed{
\sqrt K\,\nu
<1+\sqrt{1-\nu^2}
}
\tag{5.3}
\]

implies `A<1/2` and therefore one strict regularized square-Newton contraction.

The important point is that `K` is required only for the **actual Newton score**. A uniform `L^4/L^2` bound over the whole selected Fourier subspace would be much stronger and is not needed.

---

# 6. Correct source-closing target: fixed supercritical slack is enough

The earlier exact target

\[
t=-n^{-1/2}{\bf1}_D
\]

is sufficient for an instance bound `theta<=1+sqrt(n)`, but it is stronger than necessary for proving the expectation asymptotic.

Fix any `epsilon>0` and put

\[
d_\epsilon:=\frac1{1+\epsilon},
\qquad
 t_\epsilon=-\frac{d_\epsilon}{\sqrt n}{\bf1}_D.
\tag{6.1}
\]

If a symmetric probability realizes all selected moments equal to `t_epsilon`, then the inherited moment-depth identity gives

\[
\delta_D\ge\frac{d_\epsilon}{\sqrt n}
\]

and therefore

\[
\boxed{
\vartheta(G_D)
\le 1+(1+\epsilon)\sqrt n.
}
\tag{6.2}
\]

Thus a source-closing probabilistic theorem may work at **any fixed supercritical slack** `epsilon>0`; after the expectation estimate one lets `epsilon downarrow0`. There is no need to force an exact critical-boundary certificate at every large `n`.

If the slack certificate fails with probability

\[
q_n=o\!\left(\frac1{\sqrt{\log n}}\right),
\tag{6.3}
\]

then combining (6.2) on the good event with the primary fallback

\[
\vartheta(G_D)\le1+4\sqrt{n\log n}
\]

outside its own probability at most `2/n`, and using `theta<=n` on that final fallback failure, makes the bad-event contribution `o(sqrt(n))`. Hence

\[
\mathbb E\vartheta(G_D)
\le(1+\epsilon)\sqrt n+o(\sqrt n).
\]

Letting `epsilon downarrow0` and using the known lower bound would prove the source endpoint.

This slack formulation should be used for the next probabilistic attack; it is both sufficient and less boundary-sensitive.

---

# 7. New slack-dependent Gibbs seed formulas

The preceding report proved, for fixed `c>0` on prime orders,

\[
\mathbb E\sum_{a\in D}\mu_a(c)^2
\to
\frac14\left(e^{c^2/16}-1\right)
\tag{7.1}
\]

and

\[
\frac1{\sqrt n}\sum_{a\in D}\mu_a(c)
\to -\frac c{16}.
\tag{7.2}
\]

For a general target depth `d/sqrt(n)`, define

\[
R_{D,d}(c)
:=\sum_{a\in D}
\left(\mu_a(c)+\frac d{\sqrt n}\right)^2.
\tag{7.3}
\]

Expanding (7.3) and applying (7.1)-(7.2) gives the new annealed curve

\[
\boxed{
\mathbb E R_{D,d}(c)
\to
\rho_d(c)
:=
\frac14\left(e^{c^2/16}-1+d^2\right)
-\frac{dc}{8}.
}
\tag{7.4}
\]

Its unique positive minimizer solves

\[
\boxed{
 c\,e^{c^2/16}=4d.
}
\tag{7.5}
\]

For `d=1`, this recovers the previous mean-square optimum `c_MS=2.611674562...`. For the source-sufficient slack target use `d=d_epsilon=(1+epsilon)^{-1}`.

Similarly, using the full Fourier-energy bound instead of the annealed selected energy gives

\[
R_{D,d}(c)
\le
b_d(c)+o_{\mathbb P}(1),
\tag{7.6}
\]

where

\[
\boxed{
 b_d(c)
=
\frac12\left(e^{c^2/16}-1\right)
-\frac{dc}{8}
+\frac{d^2}{4}.
}
\tag{7.7}
\]

The high-probability envelope is minimized at

\[
\boxed{
 c\,e^{c^2/16}=2d.
}
\tag{7.8}
\]

Again `d=1` recovers the preceding `c_HP` equation. Equations (7.5) and (7.8) give a clean family of seeds for testing the new skew-margin criterion at fixed supercritical slack.

---

# 8. What changed, what remains open

### Old result

The complementary line had a small Gibbs residual and an exact signed linear repair, but positivity was reduced to the worst pointwise negative score `max_j(-g(j))_+`. The next requested attack was to bound that maximum or keep it bounded along a damped multiplicative path.

### New result

The pointwise extreme is no longer the controlling deterministic obstruction. The positive update

\[
p\mapsto p\frac{(1+\alpha_*g)^2}{1+\alpha_*^2\nu^2}
\]

cancels the old residual term exactly and leaves only the third-cumulant vector `tau`. A small old-law mixture gives an exact covariance comparison and a strict Newton-decrement contraction whenever the source-coupled scalar

\[
A=\frac{\Gamma\nu}{2(1+\sqrt{1-\nu^2})}
\]

is below `1/2`. A directional kurtosis bound is sufficient. This bypasses all rare-point positivity failures that made the one-sided `L^infinity` route brittle.

### Fixed full-source metric

The source theorem itself remains **OPEN**. The bound

\[
\sqrt n\le\mathbb E\vartheta(G_n)
\le C\sqrt{n\log\log n}
\]

is unchanged.

### Intermediate obligation ledger

1. **DONE:** positive square-Newton identity (2.7), no sign hypothesis.
2. **DONE:** optimal scalar `alpha_*` cancels the entire inherited residual term when `nu^2<1`.
3. **DONE:** covariance-stable regularization and exact skew-margin contraction criterion (4.8)-(4.12).
4. **DONE:** actual-score kurtosis implies the directional skew bound, equation (5.2).
5. **DONE:** replace unnecessarily critical source target by fixed-slack targets `d_epsilon/sqrt(n)`, sufficient for the expectation endpoint.
6. **DONE:** derive the slack-dependent annealed and high-probability Gibbs seed optimizers (7.5), (7.8).
7. **OPEN:** prove, for a source-valid Gibbs seed and fixed `epsilon>0`, an initial decrement bound `nu_0^2<1-c_epsilon` with failure `o(1/sqrt(log n))`.
8. **OPEN:** prove the actual Newton-score directional skew margin `A_k<=1/2-c_epsilon` along the regularized square path, preferably via a two-/three-replica expansion. A sufficient stronger route is an actual-score kurtosis bound satisfying (5.3).
9. **OPEN:** remove the prime-order restriction by a genuine gcd/resonance analysis after the source-coupled skew step is controlled.

### Next concrete attack

Work at fixed `epsilon>0`, target `t_epsilon`, and start from either the high-probability seed solving (7.8) or the mean-square seed solving (7.5). Do **not** return to a generic `max_j|g(j)|` estimate. Instead derive exact replica formulas for

\[
\nu^2=r^T\Sigma^{-1}r,
\qquad
\tau=\mathbb E[Xg^2],
\qquad
\Gamma=\frac{\|\tau\|_{\Sigma^{-1}}}{\nu^2},
\]

using leave-one-frequency conditioning. The first theorem-sized target is a fixed-slack estimate

\[
\Pr\left\{
\nu_0^2\le1-c_\epsilon,
\quad
\Gamma_0\nu_0
\le (1-c_\epsilon)
\left(1+\sqrt{1-\nu_0^2}\right)
\right\}
=1-o\!\left(\frac1{\sqrt{\log n}}\right).
\]

Then prove that the same margin is preserved by the regularized square update. This is a directional third-moment problem, not a uniform Fourier-subspace hypercontractivity problem.

Prime restriction remains real. Every statement above is **PROVED PARTIAL** unless explicitly identified as an open source-dependent obligation.