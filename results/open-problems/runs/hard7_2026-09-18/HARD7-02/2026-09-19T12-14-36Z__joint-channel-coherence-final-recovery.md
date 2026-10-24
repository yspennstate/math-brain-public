Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime surface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed execution duration. **No movement in the frozen source metric: `S=5 -> 5`. Final-recovery methods tried: B3, B7, B11.**

# HARD7-02 final recovery, run 1 — joint-channel coherence, an exact alpha=1 two-message RDE, and the parity-signed Hermitization susceptibility

Status of Campbell–O'Rourke Question 1.8: **PARTIAL / source question remains OPEN in bounded current-status search.**

This is the first substantive execution after the second and final Section-I recovery checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T11-12-38Z__stuck2-joint-hermitization-susceptibility-plan.md`.

That checkpoint selected exactly one recovery: decide, or make source-level progress toward deciding,

\[
\mu_{1,\vartheta_{1/4}}\stackrel{?}{=}\mu_{1,\vartheta_{1/2}},
\tag{0.1}
\]

where

\[
\eta_x=\operatorname{Law}\left(\sqrt{x}e^{i\phi},\sqrt{1-x}e^{-i\phi}\right),
\qquad
\vartheta_x=\frac12(\eta_x+\tau_\#\eta_x),
\quad 0<x\le \frac12.
\]

The run does **not** decide (0.1), and it does not manufacture a sixth full-source transformation law. It does, however, close the first genuinely joint piece that STUCK2 identified as missing. At every fixed regularization `eta>0`, the two zero-shift Hermitized channels admit a common real gauge on the same PWIT, and their joint resolvent vectors have an exact positive overlap recursion. A normalized overlap/coherence is exactly `1` at the Hermitian endpoint `x=1/2` and is **strictly less than `1` for every interior `0<x<1/2`**, in particular at `x=1/4`. Thus the paired-mark correlation survives all the way into a fixed-eta joint resolvent observable; replacing the two channels by their marginals is rigorously invalid.

For `alpha=1` the run also derives an exact two-dimensional Laplace fixed-point equation for the coupled cavity messages. Finally, dualizing back to the real-shift Hermitized determinant shows why this still falls short of the planar ESD: the physical second variation is a **parity-signed** version of the positive overlap. The remaining obstruction has therefore narrowed from “unknown joint law” to a specific signed-cancellation plus `eta downarrow 0` problem.

## 1. Continuity, whole-repository reads, ownership, and status refresh

At run start I re-read or refreshed the controlling files and fleet state required by policy:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the canonical claim `operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`;
- the HARD7-02 chain through STUCK2, including the zero-shift swap-symmetric theorem and the earlier subcritical product-universality/cycle obstruction;
- current repository searches for Campbell–O'Rourke, `theta_d`, heavy-tailed elliptic matrices, and neighboring random-matrix claims;
- the latest recovered neighboring R7-06 state. R7-06 has already handed off its former heavy-tail `C0032` target and is now exclusively on `F0011`, Vu's integral-spectrum conjecture. That is not an equivalent or competing claim.

The canonical ownership record remains unique to HARD7-02. No posted author manuscript, Bernoulli-singularity target, least-singular-value manuscript, Toeplitz/Hankel target, additive-spike target, or gated-product target collides with Question 1.8.

### Primary source and exact question

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability **27** (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`:

- https://arxiv.org/abs/2010.01261
- https://doi.org/10.1214/22-EJP849

Section 1.3, Question 1.8 asks:

> **What properties of `theta_d` determine `mu_{alpha,theta_d}`?**

Theorem 1.6, not the question, is the already-proved convergence theorem under Condition C2.

### Fresh current-status check — 2026-09-19

I repeated a bounded web/current-literature search using the exact source title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, dependence measure, PWIT, Hermitization, Brown measure, and 2025–2026 date terms. The search recovered the 2022 source and Sean O'Rourke's current publication page, last updated 2 January 2026. That page lists the 2025 Carpenter–O'Rourke preprint *The Limiting Spectral Distribution for Sparse Elliptic Random Matrices* (`arXiv:2508.04891`) but no claimed resolution of the heavy-tailed dependence-classification Question 1.8. I found no located later paper claiming a full solution of Question 1.8. This is **bounded negative evidence only**, not a worldwide openness or novelty certificate.

### Runtime / scheduler capability

The scheduler surface exposed to this worker still offers title, prompt, schedule/timing, enabled state and task update controls but **no authenticated model selector or reasoning-effort selector**. Therefore GPT-6/maximum cannot be made binding from this surface. Changing that would require an authorized platform interface that exposes model/effort fields plus runtime telemetry.

The repository preserves historical `You cannot modify this task` errors for P26/P01/P03, while `RESULTS.md` records that P26 was later editable from a different authorized native context. For any task that still refuses modification, the compliant route is the authorized owner/account/workspace interface or platform support/ownership transfer; it is **not** a permission bypass and **not** a duplicate schedule. No scheduler mutation was attempted here.

## 2. Frozen metric and recovery state

The canonical claim freezes

`S = number of exact nontrivial full-source transformation laws theta_d -> mu_{alpha,theta_d}`

under the claim's established counting rule.

Before this run: `S=5`.

After this run: **`S=5` — no movement.**

The new theorem is a fixed-regularization theorem for the joint Hermitized limit operator, not a full equality/invariance law for `mu_{alpha,theta_d}`, so it is deliberately not counted.

STUCK2 was the second and final Section-I recovery episode. This execution is the **first ordinary substantive run of that final recovery sequence**. Thus the post-STUCK2 unchanged streak is one, not a third stuck episode. If this final recovery sequence later reaches the Section-I trigger again, HARD7-02 must hand off Question 1.8 and rotate; it may not create STUCK3.

## 3. B3 — prove something stronger: keep both zero-shift channels on one probability space

Run 14 identified each marginal zero-shift channel but intentionally discarded their joint coupling. The first task now is to put the two scalar channels back on the **same** marked tree without losing the paired-coordinate information.

Fix `0<x<=1/2`. For a mark from `eta_x`,

\[
w_1=\sqrt{x}e^{i\phi},\qquad \overline{w_2}=\sqrt{1-x}e^{i\phi}.
\]

For a mark from `tau#eta_x`,

\[
w_1=\sqrt{1-x}e^{-i\phi},\qquad \overline{w_2}=\sqrt{x}e^{-i\phi}.
\]

Thus, **edge by edge, the two weights used by the two zero-shift Hermitized components have the same complex phase**. Only their positive amplitudes differ. Since the underlying PWIT is a tree, choose the root gauge to be one and recursively remove that common phase on every edge. Apply the same vertex phase at the two lifted copies of each original tree vertex. This has two consequences:

1. both zero-shift component operators become real self-adjoint weighted-tree operators on the same rooted tree;
2. a same-vertex matching between the two lifted copies is unchanged by the common gauge. In particular a **real** Hermitization shift remains a scalar matching between the two channels.

After absorbing the deterministic depth-parity swap into the fair mark coin, we obtain the following exact coupled representation.

### Proposition 3.1 — common-gauge channel representation

On one rooted PWIT, let every edge `e` carry a radial mark `r_e>0` and an independent fair coin `C_e` taking the values `x` and `1-x`. Then the two zero-shift component operators can be coupled so that their positive edge weights satisfy

\[
t_{+,e}=r_e\sqrt{C_e},\qquad
 t_{-,e}=r_e\sqrt{1-C_e}.
\tag{3.1}
\]

In particular,

\[
t_{+,e}t_{-,e}=\beta_x r_e^2,
\qquad
\beta_x:=\sqrt{x(1-x)},
\tag{3.2}
\]

which is independent of the fair coin. At `x=1/2`, the two operators coincide pathwise:

\[
H_+^{(1/2)}=H_-^{(1/2)}.
\tag{3.3}
\]

For `0<x<1/2`, their marginals are identical by channel-swap symmetry, but the operators are not pathwise identical.

#### Proof

The phase statement above is literal for the two atoms of the mixture `vartheta_x`. The zero-shift bipartization has the two parity/copy components from run 14. On a given original edge, one component takes `w_1` and the other takes `overline{w_2}`, with a deterministic interchange depending on depth. These two numbers share the same phase. Tree acyclicity therefore lets one remove the common edge phases recursively with one vertex gauge. The mixture coin is independent across PWIT marks, and the deterministic depth interchange preserves its fair law. The remaining moduli are exactly (3.1); multiplying them gives (3.2). At `x=1/2` both moduli are `r_e/sqrt(2)` on every edge, proving (3.3). `QED`

**B3 outcome:** succeeded. The recovery no longer has only two marginal scalar laws; it has an exact joint random-operator coupling that preserves the paired mark.

## 4. Exact fixed-eta joint resolvent recursion

Fix `eta>0` and write

\[
R_\pm=(H_\pm-i\eta)^{-1},
\qquad
u_\pm=R_\pm\delta_o.
\]

Because the real-gauged operators have zero diagonal and are bipartite, their root diagonal resolvents are purely imaginary with positive imaginary part:

\[
g_\pm:=\langle\delta_o,R_\pm\delta_o\rangle=i q_\pm,
\qquad q_\pm>0.
\tag{4.1}
\]

For every child subtree `k`, use `q_{+,k},q_{-,k}` for the corresponding cavity root messages. Schur complementation gives the coupled scalar equations

\[
q_+=\frac{1}{\eta+\sum_k t_{+,k}^2q_{+,k}},
\qquad
q_-=\frac{1}{\eta+\sum_k t_{-,k}^2q_{-,k}}.
\tag{4.2}
\]

Now retain the object that all earlier marginal reductions threw away:

\[
Z_x(\eta):=\langle \nu_+,\nu_-\rangle_{\ell^2}.
\tag{4.3}
\]

### Theorem 4.1 — positive joint-overlap recursion

For every `0<alpha<2`, `0<x<=1/2`, and fixed `eta>0`, the common-gauge coupling satisfies

\[
\boxed{
Z_x(\eta)
=q_+q_-\left(1+\sum_k \beta_x r_k^2 Z_{x,k}(\eta)\right).
}
\tag{4.4}
\]

The series is nonnegative and finite. Moreover

\[
0<Z_x(\eta)\le \|\nu_+\|\,\|\nu_-\|,
\qquad
\|\nu_\pm\|^2=\frac{q_\pm}{\eta}.
\tag{4.5}
\]

#### Proof

First truncate the PWIT at finite depth. With the root separated from its child subtrees, the root column of the resolvent restricts on child subtree `k` as

\[
\nu_\pm|_{T_k}=-g_\pm t_{\pm,k}\nu_{\pm,k}.
\tag{4.6}
\]

The root contribution to the Hilbert inner product is

\[
\overline{g_+}g_-=q_+q_-.
\]

The contribution from subtree `k` is

\[
\overline{g_+}g_-\,t_{+,k}t_{-,k}\,
\langle\nu_{+,k},\nu_{-,k}\rangle
=q_+q_-\,\beta_x r_k^2Z_{x,k},
\]

using (3.2). Summing proves (4.4) on finite truncations. Every term is nonnegative. Passing through the standard self-adjoint PWIT truncations at fixed `eta` gives the infinite-tree identity; alternatively, the right side is bounded by the left-side Hilbert-space norm bound below, so the monotone nonnegative sum is finite.

The first inequality in (4.5) is Cauchy–Schwarz. The second is the standard resolvent/Ward identity

\[
\|R_\pm\delta_o\|^2
=\frac{\operatorname{Im}\langle\delta_o,R_\pm\delta_o\rangle}{\eta}
=\frac{q_\pm}{\eta}.
\]

The root term `q_+q_->0` gives strict positivity. `QED`

## 5. A new strict invariant: endpoint coherence is 1, every interior coherence is below 1

Swap symmetry gives `E q_+=E q_-`. Define the normalized fixed-eta channel coherence

\[
\kappa_x(\eta)
:=
\frac{\eta\,\mathbb E Z_x(\eta)}{\mathbb E q_+}.
\tag{5.1}
\]

The denominator is finite and positive because `0<q_+<=1/eta`; also `Z<=1/eta^2`.

### Theorem 5.1 — strict loss of channel coherence away from the Hermitian endpoint

For every `eta>0`,

\[
\boxed{\kappa_{1/2}(\eta)=1,}
\tag{5.2}
\]

whereas for every `0<x<1/2`,

\[
\boxed{0<\kappa_x(\eta)<1.}
\tag{5.3}
\]

In particular,

\[
\kappa_{1/4}(\eta)<\kappa_{1/2}(\eta)=1
\qquad\text{for every }\eta>0.
\tag{5.4}
\]

#### Proof

At `x=1/2`, Proposition 3.1 gives `H_+=H_-` pathwise, hence `nu_+=nu_-`, so

\[
Z_{1/2}=\|\nu_+\|^2=q_+/\eta.
\]

Taking expectations gives (5.2).

Now fix `0<x<1/2`. We first show that `nu_+` and `nu_-` are almost surely not proportional. If they were proportional, comparison of their root coordinates forces the proportionality constant to be

\[
c=q_-/q_+>0.
\]

For every child `k`, comparison of the child-root coordinates from (4.6) would then force

\[
\frac{t_{-,k}}{t_{+,k}}
\frac{q_{-,k}}{q_{+,k}}=1.
\tag{5.5}
\]

Condition on all child-subtree environments, hence on every ratio `q_{-,k}/q_{+,k}`. The parent-edge fair coin `C_k` is independent of that child environment. Since `x ne 1/2`, the edge ratio `t_{-,k}/t_{+,k}` has two distinct reciprocal values. For a fixed positive cavity ratio, at most **one** of the two coin values can satisfy (5.5). Thus, conditionally, the probability that (5.5) holds for the first `m` children is at most `2^{-m}`. The radial Lévy PWIT has infinitely many children almost surely; letting `m to infinity` shows that simultaneous validity for every child has probability zero.

Therefore strict Cauchy–Schwarz holds almost surely:

\[
Z_x<\sqrt{\|\nu_+\|^2\|\nu_-\|^2}
\le \frac12\left(\|\nu_+\|^2+\|\nu_-\|^2\right).
\]

Take expectations and use channel-swap symmetry plus (4.5):

\[
\mathbb E Z_x
<\frac{1}{2\eta}\mathbb E(q_++q_-)
=\frac{\mathbb E q_+}{\eta}.
\]

This is exactly `kappa_x<1`. Positivity follows from Theorem 4.1. `QED`

### What this proves and what it does not

This theorem is a rigorous answer to the first STUCK2 sub-obligation: the joint two-channel environment **does retain interior dependence information** that the marginal zero-shift law does not. The pair `x=1/4` and `x=1/2` is distinguished for every positive regularization by a joint resolvent statistic.

It does **not** yet prove `mu_{1,vartheta_{1/4}} != mu_{1,vartheta_{1/2}}`. A nonnormal planar ESD is recovered from the nonzero-shift logarithmic potential; a fixed-eta joint statistic can in principle disappear through the signed Hermitization response or the `eta downarrow 0` limit. The next sections identify that issue exactly rather than hiding it.

## 6. B7 — take the fixed-eta limit first: exact alpha=1 two-message Laplace RDE

Now specialize to the recovery case `alpha=1`. Put

\[
U_k=r_k^2.
\]

The radial Lévy intensity `r^{-2}dr` pushes forward to

\[
\frac12u^{-3/2}du.
\tag{6.1}
\]

Let `C_k` be the fair `{x,1-x}` coin on the parent edge, independent of the child message pair. Define

\[
S_+=\sum_k U_k C_k q_{+,k},
\qquad
S_-=\sum_k U_k (1-C_k)q_{-,k},
\tag{6.2}
\]

so that

\[
(q_+,q_-)=\left((\eta+S_+)^{-1},(\eta+S_-)^{-1}\right).
\tag{6.3}
\]

### Proposition 6.1 — exact joint Laplace fixed point at alpha=1

For all `s,t>=0`,

\[
\boxed{
\mathbb E e^{-tS_+-sS_-}
=\exp\left\{-\sqrt\pi\,
\mathbb E\sqrt{tCq_+ + s(1-C)q_-}\right\},
}
\tag{6.4}
\]

where on the right `(q_+,q_-)` is an independent cavity copy and `C` is an independent fair `{x,1-x}` coin.

#### Proof

Apply the Poisson Laplace functional to the marked point process `(U,C,q_+,q_-)`. For

\[
A=tCq_+ + s(1-C)q_-\ge0,
\]

(6.1) gives

\[
\int_0^\infty (1-e^{-uA})\frac12u^{-3/2}du
=\sqrt\pi\,A^{1/2}.
\]

Averaging over the independent mark `(C,q_+,q_-)` yields (6.4). `QED`

Setting `s=0` recovers the marginal stable closure from run 14 because the parent coin is independent of the child message:

\[
\mathbb E\sqrt{Cq_+}
=\frac{\sqrt{x}+\sqrt{1-x}}{2}\,\mathbb E\sqrt{q_+}.
\]

Thus (6.4) is not a new marginal ansatz: it is an exact **two-message refinement** of the already-checked marginal law.

**B7 outcome:** succeeded at fixed `eta`. The recovery now has an explicit two-dimensional distributional fixed point for `alpha=1`. I do **not** interchange `eta downarrow 0` with this RDE. Uniform control at that boundary remains a separate obligation.

## 7. B11 — dualize back to the Hermitized determinant: the physical response is parity-signed

The strict positive coherence `Z` is useful only if we understand how it enters the logarithmic potential. The real-shift direction exposes the issue cleanly.

On a finite tree truncation after the common gauge, a real Hermitization shift `z=t in R` couples corresponding vertices by `-tI`. Hence

\[
\mathcal B_t-i\eta I
=
\begin{pmatrix}
H_+-i\eta I & -tI\\
-tI & H_--i\eta I
\end{pmatrix}.
\tag{7.1}
\]

Let `R_+=(H_+-i eta)^{-1}` and `R_-=(H_--i eta)^{-1}`.

### Lemma 7.1 — exact quadratic Schur susceptibility

Writing `s=t^2`,

\[
\boxed{
\left.\frac{d}{ds}\log\det(\mathcal B_{\sqrt{s}}-i\eta I)\right|_{s=0}
=-\operatorname{Tr}(R_-R_+).
}
\tag{7.2}
\]

#### Proof

Schur complementation gives

\[
\det(\mathcal B_t-i\eta I)
=\det(H_+-i\eta I)\,
\det(H_--i\eta I-t^2R_+).
\]

Differentiate the second logarithmic determinant at `t^2=0`. `QED`

At the root define the same-sign overlap

\[
X_x(\eta):=\langle\delta_o,R_-R_+\delta_o\rangle.
\tag{7.3}
\]

Unlike `Z`, this is not a Hilbert inner product. The same tree decomposition gives the exact signed recursion

\[
\boxed{
X_x(\eta)
=-q_+q_-\left(1+\sum_k\beta_xr_k^2X_{x,k}(\eta)\right).
}
\tag{7.4}
\]

To see the geometric difference between (4.4) and (7.4), let `d(v)` be tree depth. For positive real edge weights the root-resolvent coordinate has a phase depending only on depth:

\[
(R_\pm\delta_o)(v)=i(-i)^{d(v)}A_\pm(v),
\qquad A_\pm(v)\ge0.
\tag{7.5}
\]

Therefore

\[
Z_x=\sum_v A_+(v)A_-(v),
\tag{7.6}
\]

whereas

\[
X_x=\sum_v(-1)^{d(v)+1}A_+(v)A_-(v).
\tag{7.7}
\]

The physical real-shift second variation is thus the **alternating-depth transform** of the positive coherence. This is the missing sign structure that a marginal or Cauchy–Schwarz argument cannot see.

At the Hermitian endpoint `x=1/2`, `H_+=H_-=:H`, so

\[
X_{1/2}(\eta)
=\langle\delta_o,(H-i\eta)^{-2}\delta_o\rangle
=\frac{d}{d\eta}q_{1/2}(\eta),
\tag{7.8}
\]

using `d(H-i eta)^{-1}/d eta=i(H-i eta)^{-2}` and `g=iq`. Away from the endpoint there is no corresponding one-message derivative identity; the signed recursion (7.4) is genuinely joint.

**B11 outcome:** succeeded as a reduction, but it also gives the decisive warning. The strict inequality `kappa_{1/4}<1` cannot simply be relabeled as a planar-ESD inequality: the logarithmic-potential response uses `X`, not `Z`.

## 8. Exact finite algebra self-check

Only after the mathematical route was written down did I build a checker for its finite algebraic core.

Code:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T12-14-36Z__joint-channel-check.py`

creation commit:

`a94ebb61ceee50968789cb8c9cf3b0afe25d2536`

Output:

`artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T12-14-36Z__joint-channel-check.out`

creation commit:

`a2dd73bebc651e9f6393d757d6e78d01deee8d18`

The checker uses a one-edge/two-vertex pair of channels and verifies symbolically:

1. the positive overlap recursion;
2. the same-sign overlap recursion;
3. the exact `t^2` block-logdet coefficient `-Tr(R_-R_+)`;
4. the endpoint Ward identity `Z=q/eta`.

Its final line is

`ALL_EXACT_CHECKS_PASS = True`.

This is explicitly a **self-check** of finite algebra, not an independent proof of the infinite-PWIT theorem or the `eta downarrow 0` bridge.

## 9. What moved mathematically despite `S` not moving

The source metric does not move, but the final recovery is materially narrower after this run.

Before this run, STUCK2's blocker was:

> derive the correct joint two-channel fixed-eta object and find an observable that retains `x`.

That obligation is now met. The exact joint coupling is (3.1), the positive overlap RDE is (4.4), the strict endpoint/interior distinction is (5.2)–(5.4), and at `alpha=1` the full two-message cavity law satisfies (6.4).

The remaining source-level obligation is now:

\[
\boxed{
\text{control the parity-signed fixed-eta response }X_{1/4}(\eta)
\text{ well enough, uniformly as }\eta\downarrow0,
\text{ to produce a non-harmonic logarithmic-potential difference.}
}
\tag{9.1}
\]

Equivalently, one must prove that the alternating cancellation in (7.7) does not erase the joint-coherence defect after regularization removal, or discover an exact cancellation mechanism showing equality in (0.1).

This is much sharper than the prior phrase “joint Hermitization is unknown”: both the positive joint law and its physical signed transform are now written as explicit recursions.

## 10. Counterexample orientation / negation check

The recovery continues to attack the negation of an overly strong universality principle. The tempting claim after run 14 was that perhaps the full ESD on the swap-symmetric family is determined by the same marginal statistic `M_alpha` that determines the zero-shift singular law. Theorem 5.1 rules out the strongest route to such a proof: even at fixed `eta`, two measures with different `x` but identical treatment at the one-channel level do **not** have the same joint resolvent coupling. In particular, the Hermitian endpoint is maximally coherent and every interior point loses coherence.

This is not yet a counterexample to equality of the planar ESDs, because the signed transform could still cancel. The report therefore remains PARTIAL rather than REFUTED or PROVED.

## 11. Next-method rotation if the target continues

This run used **B3/B7/B11**, different from STUCK2's B1/B20/B30 and run 14's B4/B5/B18. If the next scheduled execution remains on this final recovery sequence, the next triple should rotate again. A natural nonrepeating choice is:

- **B5 — add the parameter `x` and differentiate:** linearize the signed recursion (7.4) at the Hermitian endpoint `x=1/2` and check whether the first nonzero derivative is forced by the fair-coin variance;
- **B15 — break the symmetry on purpose:** compare real and imaginary spectral shifts, where the parity matching weights `z` and `bar z` enter differently, to isolate even/odd depth contributions;
- **B29 — add the boundary point `eta=0`:** formulate the exact uniform integrability/tightness statement needed to pass from fixed-eta signed susceptibility to the unregularized logarithmic potential, and prove it in the simplest `alpha=1`, `x in {1/4,1/2}` pair or identify the precise failure.

No claim is made that these three steps will close (0.1).

## 12. Capability honesty and ledger delta

No email, Drive, public posting, paid compute, workflow execution, scheduler mutation, neighboring-track edit, force push, or shared-root ledger edit was made. Shared `RESULTS.md` remains under the designated coordinator/P26 reconciliation policy; this worker records only its structured delta here.

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.8
  canonical_claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
  status: PARTIAL
  metric: S
  before: 5
  after: 5
  movement: no movement
  section_I: final_recovery_sequence_run_1_after_STUCK2
  methods: [B3, B7, B11]
  new_theorem: fixed-eta strict joint-channel coherence on vartheta_x
  alpha1_reduction: exact two-message Laplace RDE
  remaining_obligation: parity-signed susceptibility plus eta_downarrow_0 log-potential bridge
  exact_checker: artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T12-14-36Z__joint-channel-check.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-02/2026-09-19T12-14-36Z__joint-channel-check.out
  exact_check_result: ALL_EXACT_CHECKS_PASS=True
  runtime_model: GPT-5.6 Sol
  runtime_reasoning: UNVERIFIED
```
