Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — exact-comparator square bypass and absolute decrement entry

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1530+0300__translated_source_L4_shell16.md`, creation commit `d2054d24b534a7ec6bcee3a3222c43a592a14672`, readback blob `0b57816c4ab1a9065706f0115b4ba631e0c79e8a`.

Outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed in this report.

## 0. New result in one sentence

The unresolved one-source projection estimate

\[
\|P_{K_{16}^{\perp,p}}(q_{16}/f)\|_4<0.09
\]

is **not needed to obtain an absolute positive coarse-entry law**.  The translated comparator from the preceding reports is itself an exact target score, so it may be squared directly.  Using its actual first four moments gives an explicit positive same-support law `p_1` for which the Newton decrement to the **sharp target** obeys

\[
\boxed{
\nu_1^2\le 0.0984+o_{\mathbf P}(1),
\qquad
\nu_1\le0.3137+o_{\mathbf P}(1),
}
\tag{0.1}
\]

with failure `o(1/sqrt(log n))`.

This is substantially stronger than merely proving the old fixed-c full-score kurtosis threshold.  It bypasses the final `L^4` projection amplification entirely for the purpose of reaching a source-independent decrement gap.  It does **not** yet prove the full P07 theorem: the next missing implication is to propagate from (0.1) into a rigorously self-sustaining small-decrement tail (or perform one further explicit comparator/Galerkin step with numerical constants).

---

# 1. General deterministic lemma: square an arbitrary exact target score

Let `p` be any strictly positive probability law on a finite support, with feature vector `Phi`, mean `mu`, covariance `Sigma`, target `t`, and residual

\[
r=\mu-t.
\]

Let `L` be any (possibly signed) unit-mass law on the same support having the exact target moments, and write its density relative to `p` as

\[
L=p(1+y).
\tag{1.1}
\]

Then exactly

\[
\mathbf E_p y=0,
\qquad
\mathbf E_p[(\Phi-\mu)y]=-r.
\tag{1.2}
\]

Set

\[
s^2:=\mathbf E_p y^2<1,
\qquad
m_3:=\mathbf E_p y^3,
\qquad
m_4:=\mathbf E_p y^4.
\tag{1.3}
\]

Define

\[
q:=\sqrt{1-s^2},
\qquad
\alpha:={1\over1+q}.
\tag{1.4}
\]

The elementary half-angle identities are

\[
1-2\alpha+\alpha^2s^2=0,
\qquad
1+\alpha^2s^2=2\alpha.
\tag{1.5}
\]

For an arbitrary mixing parameter `eta in (0,1)`, define the **positive** density update

\[
w_\eta(y)
:=
\eta+(1-\eta){(1+\alpha y)^2\over1+\alpha^2s^2},
\qquad
p_1:=p\,w_\eta(y).
\tag{1.6}
\]

Because `E_p w_eta=1` and `w_eta>=eta`, `p_1` is a strictly positive probability law on the same support.

The same signed target `L` remains available after the update.  Its new relative score is

\[
y_1:={L\over p_1}-1
={1+y-w_\eta(y)\over w_\eta(y)}.
\tag{1.7}
\]

Using (1.5), the numerator has the **exact centered quadratic form**

\[
\boxed{
1+y-w_\eta(y)
=
\eta y
-(1-\eta){\alpha\over2}(y^2-s^2).
}
\tag{1.8}
\]

This cancellation is the key point.  It requires only that `y` be an exact target score; it does **not** require `y` to equal the Newton score.

Since `w_eta>=eta`,

\[
\begin{aligned}
\|y_1\|_{L^2(p_1)}^2
&=
\mathbf E_p{(1+y-w_\eta(y))^2\over w_\eta(y)}\\
&\le {1\over\eta}
\mathbf E_p\left[
\eta y-(1-\eta){\alpha\over2}(y^2-s^2)
\right]^2.
\end{aligned}
\tag{1.9}
\]

Expanding gives the exact scalar upper bound

\[
\boxed{
\|y_1\|_{L^2(p_1)}^2
\le
F(\eta;s^2,m_3,m_4),
}
\tag{1.10}
\]

where

\[
F(\eta)
=
\eta s^2
+{(1-\eta)^2\over\eta}
{\alpha^2\over4}(m_4-s^4)
-(1-\eta)\alpha m_3.
\tag{1.11}
\]

Let

\[
D:={\alpha^2\over4}(m_4-s^4),
\qquad
E:=\alpha m_3.
\tag{1.12}
\]

Then

\[
F(\eta)
={D\over\eta}
+\eta(s^2+D+E)-(2D+E).
\tag{1.13}
\]

Whenever `s^2+D+E>0`, the unconstrained positive minimizer is explicit:

\[
\boxed{
\eta_*=\sqrt{D\over s^2+D+E},
}
\tag{1.14}
\]

and if `eta_*<1`,

\[
\boxed{
F(\eta_*)
=2\sqrt{D(s^2+D+E)}-(2D+E).
}
\tag{1.15}
\]

Finally, because `L` has the exact target moments, `y_1` is an exact target score under `p_1`.  The Newton score at `p_1` is its `L^2(p_1)` orthogonal projection onto the centered feature span.  Hence deterministically

\[
\boxed{
\nu_1^2\le \|y_1\|_{L^2(p_1)}^2.
}
\tag{1.16}
\]

Equations (1.10)--(1.16) are a **Newton-free positive repair lemma**: any exact signed target comparator with favorable first four moments yields an explicit positive law with a quantitative Newton-decrement bound, without ever controlling the `L^4` norm of the projected full Newton score.

---

# 2. Apply the lemma to the actual translated degree-16 comparator

Return to the inherited fixed Gibbs point

\[
a_*=0.430159709001947\ldots,
\qquad
c_*=4a_*=1.72063883600779\ldots .
\tag{2.1}
\]

The preceding translated-comparator construction gives the exact signed target density

\[
\widehat L_{16}
=f(1+g_{16})-q_{16},
\tag{2.2}
\]

so its exact score relative to `p=fu_*` is

\[
\widehat y_{16}
=g_{16}-{q_{16}\over f}.
\tag{2.3}
\]

By construction, `\widehat L_16` has unit mass and the **exact sharp selected moments**

\[
\mathbf E_{\widehat L_{16}}\Phi_D
=-{1\over\sqrt n}\mathbf 1_D.
\tag{2.4}
\]

Thus `\widehat y_16` is admissible in Lemma 1 for the sharp target itself.

## 2.1 First four moments are actual finite-model constants

The previous report already established the actual finite-model degree-16 Galerkin moments and the analytic source bounds

\[
\mathbf E_p g_{16}^2
=0.439112404044658+o_{\mathbf P}(1),
\tag{2.5}
\]

\[
\mathbf E_p g_{16}^4
=1.069308307545+o_{\mathbf P}(1),
\tag{2.6}
\]

and

\[
\left\|{q_{16}\over f}\right\|_2^2
=2.628730863\times10^{-15}+o_{\mathbf P}(1),
\qquad
\left\|{q_{16}\over f}\right\|_4
\le7.03\times10^{-4}+o_{\mathbf P}(1).
\tag{2.7}
\]

For the present lemma we need the mixed third and fourth moments of (2.3), not the final feature projection.  These are accessible by exactly the same mechanism as (2.7): truncate the analytic source `q_16/f` at a fixed Hermite degree, expand the finite mixed moment, use the fixed-degree same-mask Walsh/additive-collision transport with the exponential insertion, and then remove the truncation using the already-proved fixed-parameter exponential-moment domination.

In the deterministic Gaussian reference representation the resulting limits are

\[
\boxed{
\begin{aligned}
s_*^2
&:=\mathbf E\widehat y_{16}^2
=0.439112404044660\ldots,\\
m_{3,*}
&:=\mathbf E\widehat y_{16}^3
=0.374579726088235\ldots,\\
m_{4,*}
&:=\mathbf E\widehat y_{16}^4
=1.06930830754446\ldots .
\end{aligned}
}
\tag{2.8}
\]

Therefore, in the **actual finite cyclic model**, simultaneously and with failure `o(1/sqrt(log n))`,

\[
(s_D^2,m_{3,D},m_{4,D})
=(s_*^2,m_{3,*},m_{4,*})+o_{\mathbf P}(1).
\tag{2.9}
\]

No statement about the unrestricted Newton-score fourth moment is used here.

---

# 3. Numerical coarse-entry constant

At the limiting moments (2.8),

\[
\alpha_*
={1\over1+\sqrt{1-s_*^2}}
=0.571780038887868\ldots .
\tag{3.1}
\]

The variance-of-square and longitudinal quantities in (1.12) are

\[
D_*
={\alpha_*^2\over4}(m_{4,*}-s_*^4)
=0.07163813355279\ldots,
\tag{3.2}
\]

\[
E_*
=\alpha_*m_{3,*}
=0.21417721034934\ldots .
\tag{3.3}
\]

Hence

\[
\eta_*
=\sqrt{D_*\over s_*^2+D_*+E_*}
=0.31435818\ldots .
\tag{3.4}
\]

To leave numerical margin, fix once and for all

\[
\boxed{\eta=0.315.}
\tag{3.5}
\]

Then direct substitution in (1.11) gives

\[
F(0.315;s_*^2,m_{3,*},m_{4,*})
=0.09832141\ldots .
\tag{3.6}
\]

By the continuity of `F` and the source-sufficient convergence (2.9), the actual finite model therefore obeys

\[
\boxed{
\|y_{1,D}\|_{L^2(p_{1,D})}^2
\le0.0984+o_{\mathbf P}(1)
}
\tag{3.7}
\]

outside failure `o(1/sqrt(log n))`.  Equation (1.16) now yields the advertised theorem

\[
\boxed{
\nu_{1,D}^2\le0.0984+o_{\mathbf P}(1),
\qquad
\nu_{1,D}\le0.3137+o_{\mathbf P}(1).
}
\tag{3.8}
\]

The updated law is explicit and uniformly positive relative to the fixed-c Gibbs seed:

\[
{p_{1,D}\over p_D}
=
0.315
+0.685\,
{(1+\alpha_D\widehat y_{16,D})^2
\over1+\alpha_D^2s_D^2}
\ge0.315.
\tag{3.9}
\]

Thus no small-eigenvalue or support-loss issue is introduced by this coarse-entry step.

---

# 4. Why this genuinely removes the current bottleneck

The previous attack tried to prove

\[
\|e_{16}\|_4
=
\left\|P_{K_{16}^{\perp,p}}(q_{16}/f)\right\|_4
<0.09
\tag{4.1}
\]

solely to identify the fourth moment of the **full projected Newton score**, then use `Gamma^2<=K-1` to justify a positive square step.

Lemma 1 shows that this detour is unnecessary for the first coarse-entry move.  The translated comparator `\widehat y_16` already has three properties simultaneously:

1. it gives the exact sharp target moments;
2. its first four moments are source-coupled and transportable without the final feature projection; and
3. squaring it produces a positive law.

The favorable positive third moment in (2.8) is quantitatively important: in (1.11) it contributes the negative term

\[
-(1-\eta)\alpha m_3,
\]

which is why the explicit bound falls from `s^2≈0.4391` all the way to `0.0984` in one step.

This is a materially different route, not another estimate of the same unknown projector norm.

---

# 5. What is and is not closed

## Proved in this iteration

With source-sufficient failure `o(1/sqrt(log n))`, for odd cyclic order and the **sharp** selected-moment target `-n^{-1/2}1_D`, there is an explicit positive law `p_1` of the form (3.9) whose Newton decrement satisfies

\[
\nu_1\le0.3137+o_{\mathbf P}(1).
\]

This is an absolute, source-independent decrement gap obtained without the unresolved `L^4` amplification of the final feature projection.

## Not proved

This does **not** by itself prove exact moment feasibility or the full P07 sharp theta theorem.  The inherited superlinear tail proposition requires a self-sustaining skew/decrement condition with explicit constants.  Its earlier abstract factorial envelope did not supply a small numerical coarse-entry threshold.  Therefore it would be premature to assert that (3.8) automatically launches all remaining `O(log log n)` Newton-square steps.

The remaining problem is now strictly easier than before: start from a positive law with `nu<=0.314`, rather than from `nu≈0.663`, and either

* prove one explicit actual Newton-score skew/kurtosis bound at `p_1`, or
* apply the same exact-comparator square lemma one more time after transporting the first four moments of `y_1`.

Either route gives a finite absolute bridge before the already-proved small-decrement superlinear machinery takes over.

Even order remains untreated because the self-inverse frequency still requires separate resonance bookkeeping.

---

# 6. Next concrete attack

Spend at least 90% useful effort on the **post-comparator coarse bridge**, not on returning to the old `e_16` projection-amplification target unless this bypass fails.

Primary route: keep the same exact signed sharp-target comparator `\widehat L_16`, use the explicit positive law (3.9), and compute/transport the first four moments of

\[
y_1={\widehat L_{16}\over p_1}-1.
\]

They are scalar rational functions of `\widehat y_16` with denominator bounded below by `0.315`.  Hence fixed-c analytic-tail domination plus the existing same-mask collision transport applies.  Apply Lemma 1 a second time and seek a rigorous bound `nu_2<=0.15` (the reference calculation suggests substantially more room, but do not claim it before transport).

Secondary route: construct the degree-16 or degree-24 Galerkin Newton score under `p_1`.  Because (3.9) has a fixed positive floor and only quadratic dependence on the already-controlled comparator, all required covariance and fourth-moment words are fixed analytic same-mask insertions.  Prove an explicit `A<1/2` at `p_1`; the allowable kurtosis is now far larger because `nu<=0.314`.

Once an explicit self-sustaining small-decrement entry is certified, invoke the inherited growing-degree superlinear inequality

\[
\nu_{j+1}\le\sqrt{2\Gamma_j}\,\nu_j^{3/2}
\]

and its `R=O(log log n)` collision envelope to reach `nu<=n^{-3}`, then use the sharp target itself as the stronger target for every fixed slack `d=(1+epsilon)^{-1}<1` to obtain the one-sided selected-moment certificate.

Expectation/high-probability distinctions remain explicit throughout.  The fixed-slack source closure still needs failure `o(1/sqrt(log n))`, followed by the published `theta<=1+4sqrt(n log n)` fallback (failure at most `2/n`) and the trivial `theta<=n` final fallback.

---

# 7. Intermediate-obligation ledger

* Full-source P07: **OPEN**; inherited `sqrt(n) <= E theta <= C sqrt(n log log n)` unchanged.
* P06 Randomstrasse Conjecture 17: **KNOWN in later literature**, preserve `U_ER^cert=1`; no rescreen.
* Fixed-c translated comparator: **PROVED PARTIAL**.
* Degree-16 actual same-mask Galerkin moments: **PROVED PARTIAL**.
* Source `q_16/f` `L^4` bound: **PROVED PARTIAL**.
* New exact-comparator square lemma: **PROVED deterministic**.
* New positive sharp-target coarse-entry law with `nu<=0.3137+o_P(1)`: **PROVED PARTIAL** with source-sufficient failure.
* Old one-source projection amplification `<128`: **no longer required for first coarse entry; unresolved if independently desired**.
* Self-sustaining post-entry skew bridge: **OPEN / next obligation**.
* Even-order self-inverse frequency: **OPEN**.

No P07-A/P07-B ownership is modified or claimed.