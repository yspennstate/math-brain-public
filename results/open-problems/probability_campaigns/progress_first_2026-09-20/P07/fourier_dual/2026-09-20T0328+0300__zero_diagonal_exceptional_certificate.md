Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED** — GPT-6 / maximum was requested as an owner preference, but this runtime exposes no authenticated completed-run effort telemetry or binding scheduler selector, so I do not claim otherwise.

# P07-B — zero-diagonal exceptional-frequency dual certificate and a dependence-aware threshold-stability lemma

**Native role:** `P07-B`, task `6aabe797a39081919acc889f29f4c556`  
**Repository / branch:** private `yspennstate/math-open-problems` / `master`  
**Captured pre-research master:** `b4f20a8e3102102a2f774d5fd638e599cfd1d22a`  
**Outside target:** Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Conjecture 18; partial-result paper Afonso S. Bandeira, Jaroslaw Blasiok, Daniil Dmitriev, Ulysse Faure, Anastasia Kireeva and Dmitriy Kunisky, *The Lovasz number of random circulant graphs*, arXiv:2502.16227 / SampTA 2025.  
**Exact source endpoint:** for the dense random circulant model on odd `n`,

\[
\mathbb E\,\vartheta(G_n)=(1+o(1))\sqrt n.
\]

**Inherited rigorous global bound:**

\[
\sqrt n\le \mathbb E\vartheta(G_n)\le C\sqrt{n\log\log n}.
\]

Thus the inherited full-source upper-loss metric remains

\[
\boxed{\alpha_{LL}=1/2.}
\]

It does **not** move in this run. The run does, however, prove two new source-specific structural lemmas for the Fourier-dual route: (i) a one-shot feasible dual correction whose diagonal self-interaction cancels exactly, leaving only a zero-diagonal same-mask leakage term, and (ii) a uniform `O(sqrt(n))` expected Hamming-influence bound for the data-dependent threshold set under one frequency-pair flip. These are `PROVED PARTIAL`, not a solution of Conjecture 18.

---

## 0. Continuity recovered once before research

The owner-directed progress-first registry assigns this slot the complementary Fourier-dual / exceptional-frequency role for P07. I read before doing new mathematics:

- `operations/progress_first_2026-09-20/OWNER_DIRECTIVE.md`;
- `operations/progress_first_2026-09-20/REGISTRY.md`;
- the canonical historical claim `operations/claims/RS-2025-TH18.md`;
- the terminal old TH18 handoff `probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-17/rotations/RS-2025-TH18/runs/2026-09-17/2026-09-17T183900Z__report.md`;
- the old exact one-sided Fourier-completion reduction and moment-polytope work in the preceding TH18 chain;
- the current complementary P07-A report `probability_campaigns/progress_first_2026-09-20/P07/primal/2026-09-20T0246+0300__orthant_margin_positive_circuits.md`.

The P07-A report also records a bounded current-source check on 2026-09-20: the source conjecture is still stated and the strongest recovered published upper bound is still `C sqrt(n log log n)`. I therefore do not repeat the old targetless admission/literature loop here.

The old TH18 handoff already isolated the exact Fourier-completion quantity

\[
\kappa_D
:=
\inf_{q\in\operatorname{Ran}(P_C)}
\max_j (P_D e_0-q)_j,
\tag{0.1}
\]

with

\[
\vartheta(\overline{G_D})=1+n\kappa_D,
\qquad
\mathbb E\vartheta(G_D)=1+n\mathbb E\kappa_D
\tag{0.2}
\]

by complement invariance of the source ensemble. The old moment-polytope formulation also had

\[
\kappa_D=\frac1{n\delta_D},
\tag{0.3}
\]

where `delta_D` is the largest common negative cosine moment achievable by a symmetric probability law. The present run starts there rather than rebuilding the LP.

---

# 1. Exact Fourier notation

Let

\[
m=(n-1)/2.
\]

For each pair `a=1,...,m`, let `xi_a in {0,1}` be the independent fair source bit deciding whether the conjugate frequency pair `{a,n-a}` lies in the source edge-frequency set `D`. Let `C` be the complementary collection of nonzero pairs.

With the nonunitary DFT `F`, define the real orthogonal pair projections

\[
Q_a=\frac1nF\,\operatorname{diag}(1_{\{a,n-a\}})F^*,
\]

and

\[
P_D=\sum_{a:\xi_a=1}Q_a,
\qquad
P_C=\sum_{a:\xi_a=0}Q_a,
\qquad
P_0=\frac1n\mathbf1\mathbf1^T.
\]

Then

\[
P_0+P_D+P_C=I.
\tag{1.1}
\]

Write

\[
x_D:=P_De_0.
\tag{1.2}
\]

If `d=rank(P_D)` and `c=rank(P_C)`, then

\[
d+c=n-1,
\qquad
x_D(0)=\frac dn,
\qquad
\|x_D\|_2^2=\frac dn.
\tag{1.3}
\]

The last identity is simply

\[
\|P_De_0\|_2^2=\langle e_0,P_De_0\rangle.
\]

For nonzero time coordinate `j`, the source series is

\[
x_D(j)=\frac2n\sum_{a=1}^m \xi_a\cos(2\pi aj/n).
\tag{1.4}
\]

No independence between the different coordinates `x_D(j)` is assumed anywhere below.

---

# 2. New exact bridge to P07-A: the primal orthant ratio is the complementary dual error

P07-A proved for every source instance `E` the exact identity

\[
\vartheta(G_E)=1+R_E,
\tag{2.1}
\]

where

\[
R_E=\sup_{0\ne z\in L_E}
\frac{\|z_+\|_\infty}{\|z_-\|_\infty}.
\]

For the same source mask `D`, the old Fourier-dual completion gives

\[
\vartheta(\overline{G_D})=1+n\kappa_D.
\tag{2.2}
\]

But the graph with complementary nonzero connection set `C` is exactly `G_C=\overline{G_D}`. Applying (2.1) to `C` and comparing with (2.2) yields the exact cross-track identity

\[
\boxed{R_C=n\kappa_D.}
\tag{2.3}
\]

Combining with (0.3),

\[
\boxed{R_C=\frac1{\delta_D}.}
\tag{2.4}
\]

Thus the three quantities now being studied in the two P07 roles are not merely analogous:

- Fourier one-sided completion error `kappa_D`,
- moment-polytope depth `delta_D`,
- primal orthant ratio on the complementary instance `R_C`,

are exactly related by (2.3)-(2.4).

This is useful operationally because P07-A and P07-B should not duplicate proof searches under different notation. P07-A's upper bound on `R_E` and P07-B's upper bound on `kappa_D` are the same source-scale problem after complementing the mask, while the mechanisms used to produce them can still be complementary.

**Status:** `PROVED PARTIAL`; this algebra does not improve the global bound by itself.

---

# 3. New theorem: a zero-diagonal exceptional-frequency dual certificate

The old static LP (0.1) suggests clipping the positive peaks of `x_D` and correcting them with the free Fourier subspace `Ran(P_C)`. The naive correction `P_C a` leaves an order-one diagonal self-term at the distinguished coordinate. The following rescaling cancels that self-term **exactly**.

Let

\[
\alpha_C:=\frac cn.
\tag{3.1}
\]

For a threshold `tau>0`, define the excess vector

\[
a_\tau:=(x_D-\tau\mathbf1)_+.
\tag{3.2}
\]

Define the zero-diagonal complementary kernel

\[
K_C:=P_C-\alpha_C I.
\tag{3.3}
\]

Because every diagonal entry of the circulant projection `P_C` equals `c/n`, `K_C` has **zero diagonal**.

### Theorem P07-B.1 — zero-diagonal correction

Assume `c>0`. The vector

\[
\boxed{
q_\tau:=\alpha_C^{-1}P_Ca_\tau
}
\tag{3.4}
\]

lies in `Ran(P_C)` and therefore is an admissible completion in (0.1). Moreover

\[
\boxed{
\kappa_D
\le
\tau+\alpha_C^{-1}
\|(-K_Ca_\tau)_+\|_\infty.
}
\tag{3.5}
\]

In particular,

\[
\kappa_D
\le
\tau+\alpha_C^{-1}\|K_Ca_\tau\|_\infty.
\tag{3.6}
\]

### Proof

Since `P_Ca_tau = alpha_C a_tau + K_Ca_tau`,

\[
q_\tau
=a_\tau+\alpha_C^{-1}K_Ca_\tau.
\]

Hence

\[
\begin{aligned}
x_D-q_\tau
&=x_D-a_\tau-\alpha_C^{-1}K_Ca_\tau.
\end{aligned}
\]

By definition of `a_tau`, coordinatewise

\[
x_D-a_\tau\le\tau\mathbf1.
\]

Therefore

\[
\max_j(x_D-q_\tau)_j
\le
\tau+\alpha_C^{-1}
\max_j(-K_Ca_\tau)_j,
\]

which is (3.5). Since `q_tau in Ran(P_C)`, taking the infimum in (0.1) completes the proof. ∎

### Why the rescaling matters

If one uses only `q=P_Ca_tau`, then the term `P_Da_tau` retains the diagonal self-interaction and at coordinate `0` can remain order one. In (3.4), the factor `alpha_C^{-1}` removes the diagonal part at **every** active coordinate simultaneously. What remains is purely off-diagonal same-mask leakage.

Indeed, for `r != 0`, (1.1) gives

\[
(P_C)_{0r}
=-\frac1n-(P_D)_{0r}
=-\frac1n-x_D(r).
\tag{3.7}
\]

By translation invariance of the circulant kernel,

\[
\boxed{
(K_Ca_\tau)(j)
=
\sum_{s\ne j}x_C(j-s)a_\tau(s),
}
\tag{3.8}
\]

where for nonzero offset `r`,

\[
x_C(r)=-\frac1n-x_D(r).
\tag{3.9}
\]

Thus the exact blocker is no longer a generic Fourier norm or a diagonal term. It is the **off-diagonal convolution of the source-generated excess set with the complementary same-mask Fourier kernel**.

This is the object on which a dependence-aware small-ball or leave-one-frequency theorem should be aimed.

---

# 4. Deterministic control of the exceptional set

The certificate (3.5) is useful only if the excess vector is quantitatively controlled. Two source-exact estimates require no independence across Fourier coordinates.

Let

\[
S_\tau:=\{j:x_D(j)>\tau\}.
\tag{4.1}
\]

By (1.3),

\[
|S_\tau|\tau^2
\le
\sum_{j\in S_\tau}x_D(j)^2
\le
\|x_D\|_2^2
=\frac dn.
\]

Hence

\[
\boxed{
|S_\tau|\le\frac{d}{n\tau^2}.
}
\tag{4.2}
\]

For the `l1` mass, the scalar inequality

\[
(u-\tau)_+\le\frac{u^2}{4\tau}
\qquad(u\in\mathbb R,\ \tau>0)
\tag{4.3}
\]

follows from `(u-2 tau)^2>=0` on `u>tau`. Therefore

\[
\boxed{
\|a_\tau\|_1
\le
\frac{\|x_D\|_2^2}{4\tau}
=
\frac{d}{4n\tau}.
}
\tag{4.4}
\]

Also

\[
\boxed{
\|a_\tau\|_2\le\|x_D\|_2=\sqrt{d/n}\le1.
}
\tag{4.5}
\]

At the target constant scale

\[
\tau=\frac A{\sqrt n},
\tag{4.6}
\]

(4.2) gives

\[
|S_\tau|\le \frac d{A^2},
\tag{4.7}
\]

so a large fixed `A` already reduces the active set to a fixed small fraction of the coordinates **deterministically**. No independent-coordinate fiction is needed.

---

# 5. A first rigorous multiscale census after diagonal cancellation

The zero-diagonal operator has an exact spectral norm. Since `P_C` is a projection,

\[
K_C=P_C-\alpha_C I
\]

has eigenvalue `1-alpha_C` on `Ran(P_C)` and eigenvalue `-alpha_C` on its orthogonal complement. Therefore

\[
\boxed{
\|K_C\|_{2\to2}=\max(\alpha_C,1-\alpha_C).
}
\tag{5.1}
\]

On the typical density event

\[
\frac14\le\alpha_C\le\frac34,
\tag{5.2}
\]

we have

\[
\|K_Ca_\tau\|_2\le\frac34\|a_\tau\|_2\le\frac34.
\tag{5.3}
\]

Consequently, for every `u>0`,

\[
\boxed{
\left|
\left\{j:\ |(K_Ca_\tau)(j)|>\frac u{\sqrt n}\right\}
\right|
\le
\frac{9}{16}\frac n{u^2}.
}
\tag{5.4}
\]

This is only a weak-`l2` census, but it is an exact multiscale statement: after the diagonal-canceling correction, leakage above level `u/sqrt(n)` can occur on at most `O(n/u^2)` coordinates. In particular, the only obstacle to an `O(1/sqrt(n))` dual certificate is control of the **extreme tail** of a zero-diagonal leakage vector, not its total energy.

This is precisely the point where the published worst-case RIP truncation pays an iterated logarithm. The present reduction narrows the needed replacement theorem to a source-generated zero-diagonal extreme-value estimate.

---

# 6. New dependence lemma: one frequency-pair flip changes the threshold set in only `O(sqrt(n))` coordinates on average

The exceptional set `S_tau` is selected by the same mask that defines `P_C`, so it cannot be treated as independent of the Fourier operator. The next lemma quantifies that dependence directly.

For a pair index `b`, let `D^{(b,0)}` and `D^{(b,1)}` denote the two masks obtained by forcing `xi_b=0` or `1` while leaving every other source bit unchanged. Let

\[
S_\tau^{(b,s)}
:=
\{j:x_{D^{(b,s)}}(j)>\tau\},
\qquad s\in\{0,1\}.
\]

### Lemma P07-B.2 — threshold-set influence

There is an absolute constant `K` such that for every odd sufficiently large `n`, every pair index `b`, and every real threshold `tau`,

\[
\boxed{
\mathbb E\,
|S_\tau^{(b,1)}\triangle S_\tau^{(b,0)}|
\le K\sqrt n.
}
\tag{6.1}
\]

Equivalently, the expected fraction of time coordinates whose threshold membership depends on one specified source frequency-pair bit is `O(n^{-1/2})`.

### Proof

Fix `j`. Write

\[
c_a(j):=\cos(2\pi aj/n).
\]

By (1.4), changing `xi_b` changes `x_D(j)` by

\[
\Delta_{b,j}=\frac2n c_b(j),
\qquad
|\Delta_{b,j}|\le\frac2n.
\tag{6.2}
\]

Hence threshold membership at coordinate `j` can differ between the two forced masks only if the leave-one-bit sum lies in an interval whose length, in the unscaled cosine-sum variable, is at most `2`.

Center the remaining Bernoulli bits:

\[
Y_{b,j}:=
\sum_{a\ne b}(\xi_a-1/2)c_a(j).
\tag{6.3}
\]

For `j != 0`, the exact trigonometric identity

\[
\sum_{a=1}^{(n-1)/2}c_a(j)^2=\frac{n-2}{4}
\tag{6.4}
\]

holds because `n` is odd and `2j` is nonzero mod `n`. Removing one summand gives

\[
\operatorname{Var}(Y_{b,j})
=
\frac14\sum_{a\ne b}c_a(j)^2
\ge
\frac{n-6}{16}.
\tag{6.5}
\]

For `j=0`, all cosines equal `1`, and the variance is even larger at this scale.

Moreover

\[
\sum_{a\ne b}
\mathbb E| (\xi_a-1/2)c_a(j)|^3
\le
\frac18 m
=O(n).
\tag{6.6}
\]

Berry--Esseen therefore gives a uniform concentration-function estimate

\[
\sup_t\Pr\{Y_{b,j}\in[t-1,t+1]\}
\le \frac{K_0}{\sqrt n}
\tag{6.7}
\]

for an absolute constant `K_0`; the normal contribution is `O(1/sqrt(n))` because the interval has fixed length while the standard deviation is `Theta(sqrt(n))`, and the Berry--Esseen error is also `O(1/sqrt(n))` by (6.5)-(6.6).

Thus for each `j`,

\[
\Pr\{j\in S_\tau^{(b,1)}\triangle S_\tau^{(b,0)}\}
\le\frac{K_0}{\sqrt n}.
\]

Summing over all `n` coordinates proves (6.1). ∎

### Interpretation

This does **not** decouple `S_tau` from the mask. It proves something weaker but directly useful for a leave-one-frequency program: replacing one source bit changes the generated active set in only `O(sqrt(n))` coordinates on average, rather than `Theta(n)` coordinates. A future same-mask small-ball estimate can therefore compare the true active set to a leave-one-bit set with a quantified `n^{-1/2}` per-coordinate dependence cost.

That is the dependence feature the old TH18 work was missing when it warned against inserting a fixed-vector Fourier contraction into a mask-dependent residual.

---

# 7. Exact missing lemma that would remove or improve the iterated-log loss

Theorem P07-B.1 isolates the single quantity that now controls this route.

Fix a constant `A>0` and set

\[
\tau_n=\frac A{\sqrt n},
\qquad
a_n=(x_D-\tau_n\mathbf1)_+.
\]

Because the number of complementary source pairs is binomial, a standard Chernoff bound gives

\[
\Pr\{\alpha_C<1/4\}\le e^{-c_0n}
\tag{7.1}
\]

for some absolute `c_0>0`. On the bad event, `q=0` in (0.1) gives `kappa_D<=max_j x_D(j)<=d/n<=1`, so the exponentially small event is harmless for the expectation scale.

Therefore the following is a **source-exact sufficient lemma**.

### Missing Leakage Lemma `L(beta)`

For some `beta>=0`, prove

\[
\boxed{
\mathbb E\left[
1_{\{\alpha_C\ge1/4\}}
\|(-K_Ca_n)_+\|_\infty
\right]
\le
K\frac{(\log\log n)^\beta}{\sqrt n}
}
\tag{7.2}
\]

for an absolute finite `K` and all sufficiently large odd `n`.

Then Theorem P07-B.1 and `alpha_C^{-1}<=4` on the good event give

\[
\mathbb E\kappa_D
\le
\frac A{\sqrt n}
+
4K\frac{(\log\log n)^\beta}{\sqrt n}
+e^{-c_0n}.
\tag{7.3}
\]

Using (0.2),

\[
\boxed{
\mathbb E\vartheta(G_n)
\le
1+A\sqrt n+4K\sqrt n(\log\log n)^\beta+ne^{-c_0n}.
}
\tag{7.4}
\]

Hence:

- any `beta<1/2` in (7.2) **strictly improves** the published iterated-log exponent;
- `beta=0` removes the iterated-log loss completely and proves `alpha_LL=0`, i.e. `E theta(G_n)=O(sqrt(n))`;
- even `beta=0` does **not** prove the sharp leading constant `1` in Conjecture 18.

A high-probability version is also sufficient provided the failure probability is small enough to integrate. Specifically, if on the good-density event

\[
\|(-K_Ca_n)_+\|_\infty
\le
K\frac{(\log\log n)^\beta}{\sqrt n}
\]

except with probability

\[
p_n=O((\log\log n)^\beta/\sqrt n),
\]

then the trivial `kappa_D<=1` bound on failure gives the same expectation order. Mere `1-o(1)` probability without a rate is not enough for the expectation target.

This is the exact lemma I recommend P07-B attack next.

---

# 8. What is genuinely new here versus inherited work

The old TH18 line already had:

- the exact source Fourier LP;
- alternating dual clipping;
- first-step mean-square contraction;
- the static one-sided completion quantity `kappa_D`;
- the moment-polytope quantity `delta_D`;
- the warning that same-mask dependence invalidates independent-coordinate arguments.

This run does **not** repackage those as new results.

The new mathematical content is:

1. the exact cross-track identity
   \[
   R_C=n\kappa_D=1/\delta_D,
   \]
   tying P07-A and P07-B observables together under source complementation;
2. the explicit feasible correction
   \[
   q_\tau=\alpha_C^{-1}P_C(x_D-\tau)_+
   \]
   and the zero-diagonal leakage bound (3.5), which removes the order-one diagonal obstruction from the exceptional-set correction in one shot;
3. the exact weak-`l2` multiscale census (5.4) for the remaining leakage;
4. the dependence-aware threshold-set influence lemma (6.1), proved without treating Fourier coordinates as independent;
5. the source-exact Missing Leakage Lemma (7.2), whose exponent maps directly to the improved Lovasz-theta exponent.

These constitute `PROVED PARTIAL` structural progress. The frozen full-source metric nevertheless remains unchanged because (7.2) is still open.

---

# 9. Remaining gap and next attack

The remaining obstacle is now sharply localized:

\[
\|(-K_Ca_n)_+\|_\infty,
\qquad
K_C=P_C-\frac cnI,
\qquad
 a_n=(P_De_0-A/\sqrt n)_+,
\]

where both `K_C` and `a_n` are generated by the **same** Bernoulli frequency-pair mask.

The next attack should not return to a generic RIP theorem. It should use Lemma P07-B.2 in a leave-one-frequency decomposition:

1. remove one pair bit `xi_b` from the definition of the active set and excess vector;
2. condition on the leave-one-bit object, which is independent of `xi_b`;
3. average the `Q_b` contribution to the zero-diagonal convolution exactly;
4. charge the difference between the true and leave-one-bit active sets to the `O(sqrt(n))` expected symmetric-difference bound from (6.1);
5. sum the influence errors using Parseval across the pair projections, rather than an `n`-fold union bound.

A successful implementation should target (7.2) directly. If the resulting error is only `O(sqrt(log log n)/sqrt n)`, it reproduces the current exponent and teaches where the loss remains. Any smaller iterated-log power is genuine source-level movement.

P07-A should use the bridge (2.3)-(2.4) but continue its distinct primal/conic route; no P07-A report or historical file was modified here.

---

## 10. Obligation ledger

```yaml
full_source_metric:
  name: alpha_LL
  before: 1/2
  after: 1/2
  status: UNCHANGED

proved_partial:
  - "R_C = n*kappa_D = 1/delta_D across complementary source masks"
  - "zero-diagonal feasible dual correction q_tau = alpha_C^{-1} P_C (x_D-tau)_+"
  - "kappa_D <= tau + alpha_C^{-1} ||(-K_C a_tau)_+||_infty"
  - "deterministic exceptional-set and excess-mass bounds"
  - "weak-l2 multiscale leakage census"
  - "one-pair threshold-set expected influence O(sqrt(n)) via Berry-Esseen"

open_obligations:
  - "prove Missing Leakage Lemma L(beta) for some beta<1/2"
  - "ideally prove beta=0 to remove the iterated-log loss"
  - "after alpha_LL=0, sharpen constants and tails enough to reach leading constant 1"

status: "OPEN / PROVED PARTIAL"
next_attack: "leave-one-frequency expansion of the zero-diagonal leakage using the O(sqrt(n)) threshold-set influence bound and Parseval summation of influence errors"
```
