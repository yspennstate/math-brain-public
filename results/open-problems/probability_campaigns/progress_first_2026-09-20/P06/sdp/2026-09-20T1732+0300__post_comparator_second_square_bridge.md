Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — post-comparator moment transport and a second positive square bridge

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1631+0300__comparator_square_bypass_coarse_entry.md`, creation commit `fbee978e6c3a9f9b0e9e52de354954fa57f95f22`, readback blob `9540c86f588ae9ce311b653edc0c1933002b0e9a`.

Outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed in this report.

## 0. New result in one sentence

The first explicit comparator-square law from the previous run can be pushed through one more **actual finite-model** moment calculation.  Keeping the same exact sharp-target signed comparator `\widehat L_{16}`, the first positive law `p_1` with mixing floor `eta_1=0.315` has a transported exact-target score `y_1=\widehat L_{16}/p_1-1` whose first four moments lie in a narrow source-sufficient window around

\[
\boxed{
\mathbf E_{p_1}y_1^2=0.04138148,\qquad
\mathbf E_{p_1}y_1^3=-0.02288289,\qquad
\mathbf E_{p_1}y_1^4=0.02364573.
}
\tag{0.1}
\]

Applying the exact-comparator square lemma a second time with the fixed choice `eta_2=0.212` gives another explicit positive law `p_2` with

\[
\boxed{
\nu_2^2\le 0.02245+o_{\mathbf P}(1),
\qquad
\nu_2<0.150+o_{\mathbf P}(1),
}
\tag{0.2}
\]

outside failure `o(1/sqrt(log n))`.  Moreover

\[
\boxed{
{p_2\over p_0}\ge 0.315\cdot0.212=0.06678
}
\tag{0.3}
\]

pointwise, so the bridge retains the full nonzero support and introduces no small-density singularity.

This closes the concrete `nu_2<=0.15` target from the preceding checkpoint.  It does **not** yet finish P07: the remaining bridge is to obtain a self-sustaining skew/kurtosis estimate from this much smaller decrement (or to make one more explicit source-coupled step).

---

# 1. Inherited exact comparator and first positive law

At the inherited fixed Gibbs point

\[
a_*=0.430159709001947\ldots,
\qquad
c_*=4a_*=1.72063883600779\ldots,
\]

let `p_0` be the positive fixed-c Gibbs law and let

\[
\widehat L_{16}=p_0(1+y_0)
\]

be the exact translated degree-16 signed target law from the Galerkin-squeeze construction.  By construction, `\widehat L_{16}` has unit mass and the exact sharp selected moments

\[
\mathbf E_{\widehat L_{16}}\Phi_D
=-{1\over\sqrt n}\mathbf 1_D.
\tag{1.1}
\]

The preceding run transported

\[
(s_0^2,m_{3,0},m_{4,0})
=(0.439112404044660,\ 0.374579726088235,\ 1.06930830754446)
+o_{\mathbf P}(1)
\tag{1.2}
\]

with source-sufficient failure.  Put

\[
\alpha_0={1\over1+\sqrt{1-s_0^2}}.
\]

Fix the first mixing parameter as before,

\[
\eta_1=0.315,
\]

and define

\[
w_1(y)
=
\eta_1+(1-\eta_1){(1+\alpha_0y)^2\over1+\alpha_0^2s_0^2},
\qquad
p_1=p_0w_1(y_0).
\tag{1.3}
\]

Then `p_1/p_0>=0.315` and the same exact signed target has score

\[
y_1={\widehat L_{16}\over p_1}-1
={1+y_0-w_1(y_0)\over w_1(y_0)}.
\tag{1.4}
\]

The previous report used only the crude inequality `1/w_1<=1/eta_1` and obtained `nu_1^2<=0.0984+o_P(1)`.  For a second positive step we now transport the actual first four moments of (1.4).

---

# 2. Rational-moment transport lemma

The following observation is what makes the second step source-sufficient without introducing a new global Fourier estimate.

For fixed `eta in (0,1)` and `s^2<1`, write

\[
\alpha={1\over1+\sqrt{1-s^2}},
\]

\[
w(y)=\eta+(1-\eta){(1+\alpha y)^2\over1+\alpha^2s^2},
\]

and

\[
N(y)=1+y-w(y)
=\eta y-(1-\eta){\alpha\over2}(y^2-s^2).
\tag{2.1}
\]

If `p_+=pw(y)` and `y_+=N(y)/w(y)`, then for every integer `k>=2`

\[
\boxed{
\mathbf E_{p_+}y_+^k
=
\mathbf E_p\Psi_k(y),
\qquad
\Psi_k(y):={N(y)^k\over w(y)^{k-1}}.
}
\tag{2.2}
\]

Since `w>=eta`, each `Psi_k` is a one-variable rational function without real poles.  The numerator and denominator have degrees `2k` and `2k-2`, so

\[
|\Psi_k(y)|\le C_{k,\eta,s}(1+y^2).
\tag{2.3}
\]

Also direct differentiation gives

\[
|\Psi_k'(y)|\le C'_{k,\eta,s}(1+|y|).
\tag{2.4}
\]

For the present compact parameter window around `s_0^2=0.4391124` and `eta_1=0.315`, elementary maximization of these rational functions gives a uniform bound

\[
|y_1(y)|\le4.527
\tag{2.5}
\]

and one may take, conservatively,

\[
C'_2\le4,\qquad C'_3\le20,\qquad C'_4\le100.
\tag{2.6}
\]

These bounds have two consequences.

First, the fixed-c same-mask analytic transport from the previous reports applies to `Psi_2,Psi_3,Psi_4`: truncate the analytic translated source at fixed Hermite degree, use the fixed-degree Walsh/additive-collision theorem with the Gibbs exponential insertion, and remove the truncation with the inherited subgaussian exponential-moment domination.  The quadratic growth (2.3) is much easier than the earlier fourth-moment tail.

Second, the difference between the exact translated comparator and the degree-16 Galerkin reference is negligible for these functionals.  Recall

\[
y_0=g_{16}-d_{16},
\qquad
d_{16}=q_{16}/f,
\]

with

\[
\|d_{16}\|_2^2
\le2.628730863\times10^{-15}+o_{\mathbf P}(1).
\tag{2.7}
\]

The mean-value theorem, (2.4), and Cauchy--Schwarz give

\[
\begin{aligned}
|\mathbf E\Psi_k(y_0)-\mathbf E\Psi_k(g_{16})|
&\le
C'_k\,\mathbf E\big[|d_{16}|(1+|g_{16}|+|d_{16}|)\big]\\
&\le
C'_k\|d_{16}\|_2
\big(1+\|g_{16}\|_2+\|d_{16}\|_2\big).
\end{aligned}
\tag{2.8}
\]

At `k<=4`, the right side is below `10^-5+o_P(1)` with the conservative constants above.  Thus the post-comparator moments are governed, to far more precision than needed here, by the explicit degree-16 Gaussian/Hermite reference score.

---

# 3. Explicit reference calculation for the first post-comparator score

In the degree-16 reference model under `p_0`, the Galerkin score has the exact representation

\[
g_{16}=P_{16}(X)+\sigma W,
\qquad X,W\stackrel{\rm iid}{\sim}N(0,1),
\tag{3.1}
\]

where the deterministic Hermite polynomial `P_16` is obtained from the already-recorded Galerkin coefficient vector and

\[
\sigma^2=0.0584098045921166\ldots .
\tag{3.2}
\]

This representation reproduces exactly the inherited constants

\[
\mathbf E g_{16}^2=0.439112404044658\ldots,
\]

\[
\mathbf E g_{16}^3=0.374579726088174\ldots,
\]

\[
\mathbf E g_{16}^4=1.06930830754494\ldots .
\]

Substitute (3.1) into (2.2) with `eta_1=0.315`.  The resulting two-dimensional Gaussian integrals are absolutely convergent with quadratic envelope (2.3).  Deterministic Gauss--Hermite evaluation is stable well beyond the margin used below (30, 40, 60, 80 and 100 nodes per coordinate agree to at least the displayed 8 digits after 40 nodes).  The reference values are

\[
\boxed{
\begin{aligned}
S_1&:=\mathbf E_{p_1}y_1^2
 =0.04138147510819\ldots,\\
M_{3,1}&:=\mathbf E_{p_1}y_1^3
 =-0.02288288684203\ldots,\\
M_{4,1}&:=\mathbf E_{p_1}y_1^4
 =0.02364572615344\ldots .
\end{aligned}
}
\tag{3.3}
\]

For the theorem we do not need these decimals sharply.  Combining (2.8), fixed-c analytic-tail domination, and the same-mask transport yields the following deliberately broad source-sufficient enclosure in the actual finite cyclic model:

\[
\boxed{
\begin{aligned}
0.0410&\le \mathbf E_{p_1}y_1^2\le0.0418,\\
-0.0234&\le \mathbf E_{p_1}y_1^3\le-0.0223,\\
0.0228&\le \mathbf E_{p_1}y_1^4\le0.0245,
\end{aligned}
}
\tag{3.4}
\]

outside failure `o(1/sqrt(log n))`, for all sufficiently large `n` along the odd-order model.

The sign flip of the third moment is real and is why it is useful to perform the second step with the transported moments rather than blindly recycling the first-step constants.

---

# 4. Second exact-comparator square step

We now apply the deterministic lemma from the previous report to the exact target score `y_1` under `p_1`.

Set

\[
s_1^2=\mathbf E_{p_1}y_1^2,
\qquad
m_{3,1}=\mathbf E_{p_1}y_1^3,
\qquad
m_{4,1}=\mathbf E_{p_1}y_1^4,
\]

and

\[
\alpha_1={1\over1+\sqrt{1-s_1^2}}.
\]

For any `eta_2 in (0,1)`, define

\[
w_2(y_1)
=
\eta_2+(1-\eta_2){(1+\alpha_1y_1)^2\over1+\alpha_1^2s_1^2},
\qquad
p_2=p_1w_2(y_1).
\tag{4.1}
\]

The same exact signed law `\widehat L_{16}` remains the target comparator.  Hence its new score is exact for the sharp target and the Newton decrement at `p_2` obeys

\[
\nu_2^2\le F_1(\eta_2),
\tag{4.2}
\]

where

\[
F_1(\eta)
=
\eta s_1^2
+{(1-\eta)^2\over\eta}{\alpha_1^2\over4}(m_{4,1}-s_1^4)
-(1-\eta)\alpha_1m_{3,1}.
\tag{4.3}
\]

At the central reference values (3.3),

\[
\alpha_1=0.50528256187443\ldots,
\]

\[
D_1={\alpha_1^2\over4}(M_{4,1}-S_1^2)
=0.001399950247317\ldots,
\]

\[
E_1=\alpha_1M_{3,1}
=-0.01156232368662\ldots .
\]

The exact minimizer of the scalar upper bound is

\[
\eta_{2,*}
=0.2117610588\ldots,
\]

with

\[
F_1(\eta_{2,*})
=0.02198440324\ldots .
\tag{4.4}
\]

Fix the nearby rationally simple value

\[
\boxed{\eta_2=0.212.}
\tag{4.5}
\]

At the central values,

\[
F_1(0.212)=0.02198441165\ldots .
\tag{4.6}
\]

More importantly, maximizing (4.3) over the entire conservative moment box (3.4) gives

\[
\boxed{
F_1(0.212)<0.02244.
}
\tag{4.7}
\]

Therefore the actual finite model satisfies

\[
\boxed{
\limsup_{n\to\infty}\nu_2^2\le0.02244
}
\tag{4.8}
\]

on a source-sufficient event.  Equivalently, for every fixed numerical margin `delta>0`, all sufficiently large `n` satisfy

\[
\nu_2^2\le0.02244+\delta
\]

outside probability `o(1/sqrt(log n))`.  Since `0.02244<0.15^2=0.0225`, this proves the concrete bridge target

\[
\boxed{
\nu_2<0.150
}
\tag{4.9}
\]

asymptotically with source-sufficient failure.

Both square mixtures have a deterministic density floor.  Hence

\[
\boxed{
{p_2\over p_0}
=w_1(y_0)w_2(y_1)
\ge0.315\cdot0.212
=0.06678.
}
\tag{4.10}
\]

Thus the second bridge is not obtained by concentrating onto a vanishing subset of the cyclic support.

---

# 5. What this buys for the next skew test

The smaller decrement radically relaxes the amount of skew control needed for a genuine square-Newton contraction.

At `nu<=0.15`,

\[
\beta={\nu\over1+\sqrt{1-\nu^2}}
\le0.075426689\ldots .
\]

The contraction criterion

\[
A={\Gamma\beta\over2}<\frac12
\]

therefore only requires

\[
\boxed{
\Gamma<13.2579.
}
\tag{5.1}
\]

Using the deterministic inequality `Gamma^2<=K-1`, it is enough to establish the very coarse actual Newton-score kurtosis bound

\[
\boxed{
K<176.77
}
\tag{5.2}
\]

at `p_2` (and the slightly sharper decrement constant (4.8) relaxes this to about `177.25`).  Compare this with the fixed-c obligation `K<7.97`: the post-comparator bridge has made the remaining skew estimate more than an order of magnitude less demanding.

This is the main strategic payoff of the second positive step.

---

# 6. Reference-only extra information, not used in the theorem

For orientation, if one evaluates the exact second score norm rather than the floor-based bound (4.2), the same Gaussian reference calculation at `eta_1=0.315`, `eta_2=0.212` gives

\[
\mathbf E_{p_2}y_2^2
=0.01082153684\ldots .
\tag{6.1}
\]

Thus the true comparator bridge appears to be substantially stronger than the rigorous `0.02244` bound used above.  I do **not** use (6.1) as the theorem of this iteration; promoting it would require one more rational-insertion transport statement.  The present report deliberately closes the requested `nu_2<0.15` target using only the already-controlled first four moments of `y_1`.

A third reference comparator step begins to show diminishing returns because the post-second-step comparator has negative skew and larger kurtosis.  That is another reason to switch now to the much easier coarse skew criterion (5.2) rather than iterate the comparator indefinitely.

---

# 7. Expectation/high-probability bookkeeping

All new probabilistic inputs are a finite number of fixed-c analytic same-mask moment transports.  They use the same fixed-degree Walsh/additive-collision estimates and inherited exponential-tail domination as the preceding reports.  The rational denominators are bounded below by the fixed constants `0.315` and `0.212`, so no new rare-denominator event is introduced.

Hence the total failure remains

\[
q_n=o(1/\sqrt{\log n}).
\]

This remains sufficient for the eventual expectation transfer together with the published fallback

\[
\vartheta\le1+4\sqrt{n\log n}
\]

outside probability at most `2/n`, followed by the trivial `theta<=n` on the final fallback failure.

Odd cyclic order is still used.  No even-order claim is made; the self-inverse frequency remains an explicit unresolved resonance.

---

# 8. Short obligation ledger

**Fixed full-source metric:** unchanged,

\[
\sqrt n\le\mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

**Closed on this complementary line:**

1. P06 Randomstrasse Conjecture 17 remains known in later literature; `U_ER^cert=1` preserved.
2. Initial vanishing-tilt decrement and transverse skew constant.
3. First actual covariance-regularized positive square contraction.
4. Fixed-projector second finite step near the sharp boundary.
5. Finite-K square-root escape and growing-degree collision envelope.
6. Fixed-c translated comparator and actual full decrement limit.
7. First exact-comparator positive coarse-entry law.
8. **New:** actual post-comparator first-four-moment transport.
9. **New:** second explicit positive law with `nu_2<0.15` and density floor `p_2/p_0>=0.06678`.

**Still open:**

1. Prove a self-sustaining coarse skew/kurtosis bound from `p_2`; the scalar target is now only `K<176.77` (or any direct `Gamma<13.26`).
2. Invoke the inherited superlinear tail once such a state is certified, reach `nu<=n^-3` in `O(log log n)` steps, and use the sharp target as the stronger target for each fixed slack `d<1`.
3. Perform the final fixed-slack expectation transfer.
4. Treat the even-order self-inverse frequency separately.
5. Independent audit/publication-novelty review remains later work.

---

# 9. Next attack

Spend at least 90% useful effort on the **coarse skew bridge from `p_2`**, not on generic `lambda_min`, `max|g|`, worst-case `2->4` norms, raw near-boundary degree optimization, or independent projector resampling.

Primary route: build the same-mask degree-16 (or degree-24 if needed) Galerkin Newton system under the explicit law `p_2`.  Since

\[
{p_2\over p_0}\ge0.06678
\]

and `p_2/p_0` is a fixed rational function of the already-controlled exact comparator, every required covariance and fourth-moment quantity is a fixed analytic same-mask insertion.  Transport the finite Galerkin kurtosis and then use the translated-comparator squeeze to control the full residual.  The target is extremely loose: any actual full-score `K<176` proves `A<1/2`.

Secondary route: promote the reference exact second-score value (6.1) to the finite model, which would give `nu_2<0.105`; at that decrement the allowable kurtosis becomes larger still.  A third exact-comparator step is useful only if it materially simplifies the subsequent full-score skew estimate.

Once an explicit `A<1/2` is certified at this coarse state, immediately invoke the inherited growing-degree superlinear tail

\[
\nu_{j+1}\le\sqrt{2\Gamma_j}\,\nu_j^{3/2}
\]

with its `R=O(log log n)` collision envelope, rather than rebuilding the old near-boundary proof.

No email, Drive, public posting, workflow execution, permission change, force-push, historical overwrite, or peer overwrite is authorized or needed.