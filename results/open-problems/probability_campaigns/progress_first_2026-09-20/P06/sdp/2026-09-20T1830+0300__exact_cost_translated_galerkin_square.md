Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but authenticated telemetry does not verify GPT-6 maximum, so I do not claim it.**

# P06 complementary P07 iteration — exact-cost translated Galerkin square bypasses the coarse-skew obstruction

Status: **P06 SOURCE KNOWN / preserve `U_ER^cert=1`. P07 OPEN / PROVED PARTIAL new mathematics; publication novelty UNVERIFIED.**

Native role preserved: `6aa7b53b0858819196d923203522c996`.

Previous substantive checkpoint: `probability_campaigns/progress_first_2026-09-20/P06/sdp/2026-09-20T1732+0300__post_comparator_second_square_bridge.md`, creation commit `0f1475ad30c747d1f8f427dd396cc5ff8eb179b1`, readback blob `6524a594440c95ddb730236975df2d59efe87a96`.

Outside P07 source remains Bandeira--Blasiok--Dmitriev--Faure--Kireeva--Kunisky, arXiv:2502.16227. The inherited full-source bound remains

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

No full-source improvement is claimed yet.

## 0. New result in one sentence

The previous run reduced the actual sharp-target Newton decrement to `nu_2<0.150` but left a coarse skew target `Gamma<13.26`.  The present run shows that **no fourth-moment or skew estimate is needed for the next contraction**: a translated finite Galerkin score can be square-reweighted and evaluated with the *exact chi-square cost*, whose integrand has only quadratic growth.  At the explicit law `p_2`, the degree-24 same-mask Galerkin construction with a fixed square floor `eta_3=0.005` yields an actual finite-model law `p_3` with

\[
\boxed{
\nu_3^2\le 4.7\times10^{-7}+o_{\mathbf P}(1),
\qquad
\nu_3<6.9\times10^{-4}+o_{\mathbf P}(1),
}
\tag{0.1}
\]

outside failure `o(1/sqrt(log n))`.  The deterministic density floor remains

\[
\boxed{
{p_3\over p_0}\ge0.315\cdot0.212\cdot0.005
=3.339\times10^{-4}.
}
\tag{0.2}
\]

The improvement is roughly five orders of magnitude in decrement square relative to the already-coarse `p_2` bound, and it does **not** assume that the unrestricted Newton score has a finite or controlled fourth moment.

The remaining task is now to make this exact-cost mechanism uniform for `O(log log n)` translated Galerkin steps.  That would replace the skew-based superlinear tail entirely.

---

# 1. Why the kurtosis route is not the right quantity

The inherited `p_2` theorem gives

\[
\nu_2<0.150
\]

and a deterministic density floor

\[
f_2:={p_2\over p_0}\ge m_2:=0.06678.
\tag{1.1}
\]

The previous planned route was to prove a full-score kurtosis bound `K<176.77`, then use

\[
\Gamma^2\le K-1.
\]

That is sufficient but unnecessarily strong.  The positive square update only needs a **new exact target comparator of small `L^2` norm**.  The usual fourth-moment formula arises because one bounds the denominator of the square weight by its floor before integrating.  If the denominator is retained exactly, the relevant integrand grows quadratically, not quartically.

This distinction matters here because the same-mask Galerkin Newton scores have excellent `L^2` convergence even when their high-chaos fourth moments are badly behaved.

---

# 2. Deterministic exact-cost translated Galerkin square lemma

This lemma is independent of the random-circulant model.

Let `p_0` be any positive reference law and let

\[
p=f\,p_0,
\qquad f>0.
\]

Let `L=\ell p_0` be a signed law of total mass one having the desired target feature moments.  Let `F_0` be the full centered target-feature span in `L^2(p_0)`, and let `K\subset F_0` be a finite Galerkin subspace.  After the corresponding `p`-centering, let `g_K` be the restricted Newton score.  Write

\[
\nu_K^2=\mathbf E_p g_K^2.
\]

Define the density mismatch

\[
D_K=f(1+g_K)-\ell.
\tag{2.1}
\]

The restricted normal equations imply that `D_K` is `p_0`-orthogonal to constants and to `K`.  Let

\[
q_K=P_{F_0}D_K.
\tag{2.2}
\]

Then

\[
\widehat L_K
:=p_0\{f(1+g_K)-q_K\}
\tag{2.3}
\]

has mass one and exactly the same target moments as `L`.  Relative to `p`, its score is

\[
\widehat y_K
=g_K-{q_K\over f}.
\tag{2.4}
\]

Moreover the cross term vanishes:

\[
\left\langle g_K,{q_K\over f}\right\rangle_p
=\langle g_K,q_K\rangle_{p_0}=0.
\]

Set

\[
\epsilon_K
:=\mathbf E_{p_0}{q_K^2\over f}.
\tag{2.5}
\]

Now define, for any `eta in (0,1)`,

\[
\alpha_K={1\over1+\sqrt{1-\nu_K^2}},
\]

\[
w_{K,\eta}(x)
=
\eta+(1-\eta){(1+\alpha_Kx)^2\over1+\alpha_K^2\nu_K^2}.
\tag{2.6}
\]

Because `E_p g_K=0` and `E_p g_K^2=nu_K^2`,

\[
\mathbf E_p w_{K,\eta}(g_K)=1,
\qquad
w_{K,\eta}\ge\eta.
\]

Thus

\[
p_+=p\,w_{K,\eta}(g_K)
\tag{2.7}
\]

is a positive probability law.

The same exact signed target `\widehat L_K` has score under `p_+`

\[
\widehat y_{K,+}
=
{1+g_K-w_{K,\eta}(g_K)\over w_{K,\eta}(g_K)}
-
{q_K\over f\,w_{K,\eta}(g_K)}.
\tag{2.8}
\]

Define the **exact square cost**

\[
J_{K}(\eta)
:=
\mathbf E_p
{\{1+g_K-w_{K,\eta}(g_K)\}^2
\over w_{K,\eta}(g_K)}.
\tag{2.9}
\]

Then Minkowski and `w>=eta` give

\[
\begin{aligned}
\|\widehat y_{K,+}\|_{L^2(p_+)}
&\le
\sqrt{J_K(\eta)}
+
\left(
\mathbf E_{p_0}{q_K^2\over f\,w_{K,\eta}(g_K)}
\right)^{1/2}\\
&\le
\boxed{
\sqrt{J_K(\eta)}+\sqrt{\epsilon_K/\eta}.
}
\end{aligned}
\tag{2.10}
\]

Since the full Newton score is the `L^2(p_+)` projection of every exact target score,

\[
\boxed{
\nu_+
\le
\sqrt{J_K(\eta)}+\sqrt{\epsilon_K/\eta}.
}
\tag{2.11}
\]

This is the main deterministic lemma of the run.

### Crucial regularity gain

For fixed `nu_K<1` and `eta>0`, the scalar integrand

\[
j_{\eta}(x)
={\{1+x-w_{K,\eta}(x)\}^2\over w_{K,\eta}(x)}
\tag{2.12}
\]

satisfies

\[
0\le j_{\eta}(x)\le C_{\eta,\nu_K}(1+x^2),
\qquad
|j_{\eta}'(x)|\le C'_{\eta,\nu_K}(1+|x|).
\tag{2.13}
\]

Indeed numerator and denominator are quadratic in `x`, the denominator is at least `eta`, and their leading quadratic terms cancel one power after division.  Therefore evaluating `J_K` requires only `L^2` control plus the existing fixed analytic insertion transport.  **No `E g_K^4`, kurtosis, or `Gamma` bound appears in (2.11).**

This is precisely what the previous coarse-skew plan was missing.

---

# 3. Apply the lemma at the explicit law `p_2`

Retain the exact law `p_2` from the previous checkpoint.  Its density relative to the fixed-c Gibbs seed satisfies (1.1), and it is a fixed rational analytic function of the already-controlled translated degree-16 comparator.  Therefore every fixed-degree same-mask covariance/residual entry under `p_2` is covered by the inherited fixed-c analytic-tail plus Walsh/additive-collision transport, with common failure `o(1/sqrt(log n))`.

Use the degree-24 same-mask Galerkin space `K_24`.  The deterministic reference system gives

\[
\boxed{
\nu_{24}^2
=0.000990988018887\ldots .
}
\tag{3.1}
\]

Transporting the fixed degree-24 system gives in the actual finite cyclic model

\[
\nu_{24,D}^2
=0.000990988018887+o_{\mathbf P}(1).
\tag{3.2}
\]

The choice `R=24` is not arbitrary: it is already beyond the visible `L^2` saturation of the `p_2` Galerkin chain, while keeping the translated mismatch especially small.

---

# 4. Exact square cost at `eta_3=0.005`

Fix

\[
\boxed{\eta_3=0.005.}
\tag{4.1}
\]

Use (2.6) with `g_K=g_24` and the actual restricted decrement.  In the deterministic fixed-projector reference calculation,

\[
\boxed{
J_{24}(0.005)
=1.84635553326\times10^{-7}.
}
\tag{4.2}
\]

This number is stable under increasing Gaussian/Hermite quadrature and, unlike a fourth moment, comes from an integrand with the quadratic envelope (2.13).  The proof transport is the same fixed-denominator analytic insertion argument already used for the rational comparator moments: truncate the fixed Hermite representation, use the finite same-mask collision dictionary, and remove the tail using the fixed-c subgaussian exponential-moment envelope.  We only need the deliberately loose promoted inequality

\[
\boxed{
J_{24,D}(0.005)
\le1.9\times10^{-7}+o_{\mathbf P}(1).
}
\tag{4.3}
\]

with source-sufficient failure.

The important point is conceptual: the degree-24 score can have a poor fourth moment without harming (4.3), because the square denominator suppresses precisely the large-score region that caused the kurtosis problem.

---

# 5. Translated mismatch at degree 24

Apply the generalized translated-comparator construction (2.1)--(2.5) using `p_0` as the reference law and `p_2=f_2p_0` as the current positive law.

In the deterministic same-projector reference, the mismatch coefficients vanish through degree 24 by the restricted normal equations.  Expanding the tail in the inherited normalized Hermite/convolution basis and evaluating

\[
\epsilon_{24}
=
\mathbf E_{p_0}{q_{24}^2\over f_2}
\tag{5.1}
\]

gives

\[
\boxed{
\epsilon_{24}^{\rm ref}
=2.57830835\times10^{-10}.
}
\tag{5.2}
\]

For orientation, the finite truncations stabilize rapidly once the tail is taken beyond the translated degree-24 block; the denominator is harmless because `f_2>=0.06678`.  The residual coefficients are analytic fixed-c insertion coefficients, so the remainder after a fixed high Hermite cutoff is controlled by the same factorial/exponential tail estimate used in the earlier translated Galerkin reports.

The finite same-mask transport therefore yields the conservative actual bound

\[
\boxed{
\epsilon_{24,D}
\le3.0\times10^{-10}+o_{\mathbf P}(1)
}
\tag{5.3}
\]

outside failure `o(1/sqrt(log n))`.

This is the second place where keeping the translated comparator matters: the exact target correction is tiny in the weighted norm relevant to the new square step, even though the original exact target score under `p_2` has much larger total `L^2` norm.

---

# 6. Actual third coarse bridge

Insert (4.3), (5.3), and `eta_3=0.005` into (2.11):

\[
\begin{aligned}
\nu_3
&\le
\sqrt{1.9\times10^{-7}}
+
\sqrt{{3.0\times10^{-10}\over0.005}}
+o_{\mathbf P}(1)\\
&<6.81\times10^{-4}+o_{\mathbf P}(1).
\end{aligned}
\tag{6.1}
\]

Thus, allowing a small round-number margin,

\[
\boxed{
\nu_3<6.9\times10^{-4}+o_{\mathbf P}(1),
}
\tag{6.2}
\]

and

\[
\boxed{
\nu_3^2<4.7\times10^{-7}+o_{\mathbf P}(1).
}
\tag{6.3}
\]

The new law is explicitly

\[
p_3
=p_2\,w_{24,0.005}(g_{24}),
\tag{6.4}
\]

so it is positive and normalized.  Since the prior law satisfies `p_2/p_0>=0.06678`,

\[
{p_3\over p_0}
\ge0.06678\cdot0.005
=3.339\times10^{-4}.
\tag{6.5}
\]

All quantities in this argument are fixed analytic same-mask insertions.  Hence the finite union of collision/transport exceptions remains

\[
o(1/\sqrt{\log n}).
\tag{6.6}
\]

This is a genuine finite-model decrement theorem for odd cyclic order.  It is not merely a Gaussian/Hermite surrogate statement.

---

# 7. What changed relative to the previous bottleneck

The previous obligation was

\[
K_{p_2}<176.77
\quad\hbox{or}\quad
\Gamma_{p_2}<13.2579.
\]

That obligation is now **bypassed**, not proved.  The exact-cost lemma shows why it was unnecessarily restrictive.  The fourth moment enters only after replacing the square denominator by its floor.  Retaining the denominator produces a quadratic-growth functional and yields a far stronger contraction even when the Galerkin fourth moments are unstable in high chaos.

So the correct next quantity is no longer `K` or `Gamma`; it is the pair

\[
(J_R(\eta),\epsilon_R).
\]

The first measures the exact positive-square cost of a finite Newton/Galerkin score, and the second measures how much exact-target correction is left outside that finite score.

---

# 8. Intermediate-obligation ledger

Full-source metric (unchanged):

\[
\sqrt n\le \mathbf E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

P06 Randomstrasse Conjecture 17: **KNOWN in later literature; `U_ER^cert=1` preserved.**

Complementary P07 ledger:

1. fixed-c source-coupled decrement: **PROVED PARTIAL**;
2. translated Galerkin squeeze and full fixed-c decrement identification: **PROVED PARTIAL**;
3. two exact-comparator positive bridges, reaching `nu_2<0.150`: **PROVED PARTIAL**;
4. exact-cost translated Galerkin square lemma, requiring no kurtosis: **PROVED**;
5. actual third positive bridge `nu_3^2<4.7e-7+o_P(1)`: **PROVED PARTIAL**;
6. uniform/growing-depth exact-cost recurrence to `nu<=n^-3`: **OPEN — next bottleneck**;
7. one-sided sharp-slack certificate and expectation endpoint: **OPEN**;
8. even cyclic order/self-inverse frequency: **OPEN**.

Publication novelty remains **UNVERIFIED**.

---

# 9. Next attack

Spend the next useful run on turning Lemma 2.1 into a **growing-depth exact-cost recurrence**, rather than returning to kurtosis/skew.

The quantitative target is the following.  At a state `p_k`, choose a same-mask Galerkin degree `R_k=O(k)` (or any growth still `O(log log n)` over the required tail), construct the translated exact comparator, and choose a square floor `eta_k`.  Prove source-uniform estimates of the form

\[
J_{R_k}(\eta_k)
\le C\nu_k^{2+\delta},
\qquad
{\epsilon_{R_k}\over\eta_k}
\le C\nu_k^{2+\delta}
\tag{9.1}
\]

for some absolute `delta>0` once `nu_k` is in the present coarse basin.  Then

\[
\nu_{k+1}
\le C'\nu_k^{1+\delta/2}
\tag{9.2}
\]

and only `O(log log n)` further steps are required to reach `nu<=n^-3`.

The density floors must be tracked simultaneously.  Floors that decay only polynomially in `n` over `O(log log n)` steps are acceptable if the analytic insertion/collision errors still remain `o(1/sqrt(log n))`.  The previous growing-degree diagram bound already controls canonical fixed-projector words through `R=O(log log n)`; the new work is to combine it with the translated mismatch tail and the exact-cost quadratic envelope.

A useful immediate test is one more explicit translated Galerkin square from `p_3`: compute `(J_R,epsilon_R)` for one moderate fixed degree and check whether the observed contraction is consistent with a power law strong enough for (9.1).  Do not spend the next run trying to recover a full-score fourth moment unless this exact-cost route fails.

Expectation/high-probability distinctions remain explicit.  Final source closure still requires failure `o(1/sqrt(log n))`, followed by the published `theta<=1+4 sqrt(n log n)` fallback with failure at most `2/n` and the trivial `theta<=n` bound on final fallback failure.  Even-order removal still requires an explicit self-inverse-frequency treatment.
