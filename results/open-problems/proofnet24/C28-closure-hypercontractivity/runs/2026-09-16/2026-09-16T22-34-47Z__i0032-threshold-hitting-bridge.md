Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **no movement — frozen I0032 comparison metric remains `2 -> 2`; unchanged-run count `2 -> 3`; Section-B moves 4, 21, 26. New result: the Aldous–Fill threshold is exactly `tau_2(sqrt(3))`; a threshold-matched hitting profile is a source-exact one-sided lower characterization with the same zero boundary and is asymptotically exact on the two-state boundary family, while the standard Hermon–Peres `tau_2(1/2)` / hitting profile is NOT uniformly comparable to `s_*`.**

# C28 — source-threshold hitting profile and the `pi_*=1/4` boundary

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Run date (UTC report path): 2026-09-16.
Allocation/status: CLOSABLE OUTSIDE, **CLAIMED / PENDING_ADMISSION / NOT READY**.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access change, shared-ledger edit, peer-file edit, or new schedule.

## 1. Continuity, repository sweep, ownership, and reserve

I continued from the newest durable C28 report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T21-24-34Z__i0032-resolvent-tail-obstruction.md`

rather than restarting. I reread/queried the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the canonical claim `operations/claims/I0032.md`, the exact I0032 intake row in `probability_1000_intake_I_20260914/problems.jsonl`, repository-wide I0032 attempt/history hits, the newest C29 report, and the old Paley reserve material. Large intake/attempt surfaces were queried by exact problem ID and source phrase; I do not describe connector-truncated JSONL search as a manual byte-for-byte rendering of every intake file.

The canonical claim still says **Owner C28 / CLAIMED / PENDING_ADMISSION — NOT READY**. No competing canonical I0032 claim was found. The exact intake row still records Aldous–Fill Open Problem 8.23, Section 8.4, as `open_per_source`, but that 14 September intake label is not treated as a current-literature proof. Fresh literature checks are recorded below.

The root fleet ledger contains an older stale C28 successor value; it does not overwrite the five newer complete C28 reports. The supported frozen metric entering this run is the full-source-class factor `2` for the already-frozen binary state-anchored dyadic local-spectral threshold.

### Paley-ETF remains HARD RESERVE

The prior Paley conditioning attack remains untouched in **HARD RESERVE**. Preserve, in particular,

\[
\kappa_*
=\sqrt{\frac{\sqrt{73}-1+2\sqrt{13}}
{\sqrt{73}-1-2\sqrt{13}}}
=6.6575355565204281495\ldots
\]

at `(p,m)=(73,14)`, the strict exact two-swap local maximality against all

\[
\binom{14}{2}\binom{60}{2}=161070
\]

exchange-radius-two neighbors, the common proved neighbor upper bound `6.603863488301192967...`, all earlier exact one-/two-swap certificates and failed routes, and the archived `ALL_EXACT_CHECKS_PASS` output. The quantifier correction remains governing: **one badly conditioned finite submatrix, even an exact local extremum, does not refute an existential assertion that some asymptotic family is uniformly well conditioned.**

## 2. Exact source scope, normalization, and current literature

Aldous–Fill Chapter 8, §8.4.2 considers a finite irreducible reversible continuous-time chain and defines

\[
N(s)=\|P_s\|_{2\to\infty}.
\]

The source states that `N(s)` is continuous and strictly decreases from `pi_*^{-1/2}` to `1`, and says it would be useful — **especially for comparison** — to characterize in terms of the Dirichlet form `E` the value `s*` at which `N(s)=2`. Open Problem 8.23 is exactly: **“Characterize `s*` in terms of `E`.”** The subsequent finite-`q` hypercontractive parameters

\[
s_q=\inf\{s:\|P_s\|_{2\to q}\le1\}
\]

are different quantities. I retain the total-domain convention

\[
s_*:=\inf\{s\ge0:\|P_s\|_{2\to\infty}\le2\},
\tag{2.1}
\]

which agrees with the source root when that root is positive.

Fresh dated searches in this run included:

- `"Open Problem 8.23" Aldous Fill hypercontractivity Dirichlet form`;
- `"A characterization of L2 mixing and hypercontractivity via hitting times and maximal inequalities" Hermon Peres`;
- `"On sensitivity of uniform mixing times" Hermon 2018 Aldous Fill 8.23`;
- `"Sensitivity of mixing times of Cayley graphs" Aldous Fill 8.23 Hermon Kozma`;
- `"Aldous-Fill" "Open Problem 8.23" 2025 2026`;
- `"Characterize s*" Dirichlet form Markov 2025 2026`;
- `"Open Problem 8.23" hypercontractivity 2026`.

Primary/source-adjacent results recovered:

1. **Hermon–Peres (PTRF 170 (2018), 769–800; arXiv:1609.07557)** gives a constant-factor hitting-time characterization of the *standard* continuous-time `L2` mixing time `tau_2=tau_2(1/2)`, and a separate extremal characterization of the log-Sobolev time. Their Theorem 1.1 has `rho <= tau_2 <= C rho`; their §3.1 defines the full threshold profile `tau_2(a)` and records the reversible identities `d_{2,x}^2(t)=h_{2t}(x,x)-1` and `tau_infty(a)=2 tau_2(sqrt(a))`. This paper is directly relevant later literature and must be part of any admission/prior-art record.
2. **Hermon (AIHP 54(1) (2018), 234–248)** shows that bounded perturbations of edge weights can change the order of uniform mixing time by the optimal `Theta(log log n)` factor on bounded-degree graphs. This remains important negative evidence against naive comparison-robust static surrogates.
3. **Hermon–Kozma (Canadian J. Math. 76(4) (2024), 1400–1431; published online 18 July 2023)** explicitly cite Aldous–Fill Open Problem 8.23 in their robustness discussion and formulate Dirichlet-form comparison of nearby chains.

The bounded 2025–17 September 2026 searches did not locate a later paper explicitly resolving the source-exact threshold `N(s_*)=2` in terms of `E`. That is **bounded-search evidence only**, not proof of worldwide openness or a novelty certificate.

The important correction for C28 is that Hermon–Peres is closer to the source than the previous reports made operationally explicit, but its theorem uses the conventional threshold `1/2`, not the source threshold that corresponds to `sqrt(3)`. This run quantifies that distinction exactly rather than either ignoring the paper or incorrectly declaring the source solved by it.

## 3. Frozen metric and prior C28 results

Write

\[
L=-Q,\qquad \mathcal E(f,g)=\langle f,Lg\rangle_\pi,
\qquad P_t=e^{-tL},
\]

and

\[
r_x(y)=\frac{\mathbf1_{\{y=x\}}}{\pi(x)}-1.
\]

The earlier exact bridge was

\[
F_x(t):=\langle r_x,e^{-2tL}r_x\rangle_\pi
=\frac{P_{2t}(x,x)}{\pi(x)}-1,
\]

\[
N(t)^2=1+\max_xF_x(t).
\tag{3.1}
\]

C28's already-frozen binary state-anchored dyadic candidate `S_anch,2(E)` satisfies

\[
F_x(t)\le D_x(t)\le F_x(t/2),
\]

hence on the full finite irreducible reversible continuous-time class

\[
\boxed{s_*\le S_{\rm anch,2}(\mathcal E)\le2s_*}.\tag{3.2}
\]

The factor `2` is already proved optimal for that candidate. The hard bands are comparison-unstable at dyadic boundaries. The immediately preceding run also proved that every fixed finite-depth implicit-Euler/resolvent approximation has **unbounded** comparison factor with `s_*`, while infinite depth simply reconstructs the semigroup and is deliberately not counted as a source characterization.

Therefore the frozen metric entering and leaving this run is

\[
\boxed{2\longrightarrow2}.
\]

No new candidate is opportunistically substituted into the metric.

## 4. Section-B moves 4, 21, 26 — ideas before proof

The preceding C28 move history includes `11,18,19`, then a spectral-profile deformation move including `5`, then `1,27,30`, then `6,24,25`, and most recently `17,20,22`. I therefore used three different, previously unused moves.

### Move 21 — ask who else has this shape

The direct neighboring object is Hermon–Peres's hitting-time characterization of `tau_2(1/2)`. Instead of treating it as generic “later L2 literature”, I matched its exact threshold convention to Aldous–Fill's `N(s)=2` convention.

Outcome: productive. The source parameter is exactly `tau_2(sqrt(3))`, not `tau_2(1/2)`, and the conventional Hermon–Peres parameter is not uniformly comparable to `s_*` near the source's zero-time boundary.

### Move 26 — hunt the sporadic/boundary case

The source has a sharp boundary at `pi_*=1/4`: `N(0)=pi_*^{-1/2}`, so `s_*=0` exactly when `pi_*>=1/4`. I tested the simplest asymmetric two-state family with `pi(0)=p<1/4` and sent `p` up to `1/4`.

Outcome: decisive diagnostic. The standard Hermon–Peres threshold remains order `t_rel` while `s_*` tends to zero, so no threshold-blind quotation of their constant-factor theorem can solve Open Problem 8.23. A *threshold-matched* hitting profile, however, tends to `s_*` with ratio `1` on this boundary family.

### Move 4 — prove something weaker, completely

Rather than claiming an unproved upper comparison for the adapted hitting profile, I prove the exact source-to-hitting lower implication, the exact zero-set match, and the two-state boundary asymptotics.

Outcome: a complete source-matching partial theorem and a sharply defined next question. No checker is needed: the claim is analytic and the full argument is on this page.

## 5. Exact identification of the source threshold

For a finite reversible chain, let

\[
h_t(x,y):=\frac{P_t(x,y)}{\pi(y)},
\qquad
d_{2,x}(t):=\|h_t(x,\cdot)-1\|_{2,\pi},
\qquad d_2(t):=\max_x d_{2,x}(t).
\]

Hermon–Peres use

\[
\tau_2(a):=\inf\{t\ge0:d_2(t)\le a\}.
\]

Reversibility and the semigroup identity give

\[
\|P_t\|_{2\to\infty}^2
=\max_x\|h_t(x,\cdot)\|_{2,\pi}^2
=\max_x h_{2t}(x,x)
=1+d_2(t)^2.
\tag{5.1}
\]

Consequently

\[
\boxed{s_*=\tau_2(\sqrt3).}
\tag{5.2}
\]

This is an exact normalization identity, not an estimate. It is the correct bridge between Aldous–Fill 8.23 and the later L2-mixing literature.

## 6. A threshold-matched hitting profile

For `a>0`, define the all-set hitting profile

\[
\rho_x^{(a)}:=\inf\left\{t\ge0:
\mathbf P_x(T_{A^c}>t)
\le \pi(A)+a\sqrt{\pi(A)\pi(A^c)}
\quad\forall A\subseteq\Omega,\ 0<\pi(A)\le\frac12
\right\},
\tag{6.1}
\]

and

\[
\rho^{(a)}:=\max_x\rho_x^{(a)}.
\tag{6.2}
\]

Hermon–Peres's standard `rho` is the `a=1/2` version (they state it first over connected `A`, and note that allowing all such `A` does not change the value). For the Aldous–Fill source threshold, the matched value is `a=sqrt(3)`.

### Theorem `C28-I0032-THRESHOLD-HITTING-BRIDGE-08 = PROVED (PARTIAL relative to source)`

For every finite irreducible reversible continuous-time chain:

1. `s_*=tau_2(sqrt(3))`.
2. The threshold-matched hitting profile obeys
   \[
   \boxed{\rho^{(\sqrt3)}\le s_*.}
   \tag{6.3}
   \]
3. It has exactly the same zero-time boundary:
   \[
   \boxed{\rho^{(\sqrt3)}=0\iff s_*=0\iff \pi_*\ge\frac14.}
   \tag{6.4}
   \]
4. On the two-state boundary family below,
   \[
   \boxed{\rho^{(\sqrt3)}/s_*\to1\quad\text{as }\pi_*\uparrow1/4.}
   \tag{6.5}
   \]
5. In contrast, on the same family the **standard** Hermon–Peres quantities satisfy
   \[
   \boxed{\rho^{(1/2)}/s_*\to\infty,
   \qquad \tau_2(1/2)/s_*\to\infty.}
   \tag{6.6}
   \]
   Hence the 2018 standard-threshold constant-factor theorem cannot simply be re-labeled as a uniform characterization of Aldous–Fill's source `s_*`.

The theorem is **PARTIAL**: it gives only one comparison direction for the threshold-matched profile, and the profile is probabilistic/killed-semigroup data rather than the requested static comparison-friendly Dirichlet-form characterization. It does not close Open Problem 8.23 and does not move the frozen factor-2 metric.

### Proof of (6.3)

Fix `x`, `t`, and `A`. Since `{T_{A^c}>t}` implies `X_t in A`,

\[
\mathbf P_x(T_{A^c}>t)\le \mathbf P_x(X_t\in A).
\]

Also

\[
\mathbf P_x(X_t\in A)-\pi(A)
=\langle h_t(x,\cdot)-1,\mathbf1_A-\pi(A)\rangle_\pi.
\]

Cauchy–Schwarz yields

\[
\mathbf P_x(X_t\in A)
\le \pi(A)+d_{2,x}(t)\sqrt{\pi(A)\pi(A^c)}.
\tag{6.7}
\]

Therefore if `d_{2,x}(t)<=a`, every constraint in (6.1) holds, and

\[
\rho_x^{(a)}\le\tau_{2,x}(a).
\]

Maximizing over `x` and taking `a=sqrt(3)`, then using (5.2), proves (6.3).

### Proof of the zero-boundary identity (6.4)

From the source itself,

\[
N(0)=\pi_*^{-1/2},
\]

so

\[
s_*=0\iff \pi_*\ge1/4.
\tag{6.8}
\]

For the hitting profile, at `t=0` and `x in A`,

\[
\mathbf P_x(T_{A^c}>0)=1.
\]

Let `p=pi(A)`. The matched right side equals

\[
b(p):=p+\sqrt3\sqrt{p(1-p)}.
\]

For `0<p<1`,

\[
b(p)\ge1
\iff \sqrt3\sqrt{p(1-p)}\ge1-p
\iff 3p\ge1-p
\iff p\ge\frac14.
\tag{6.9}
\]

If `pi_*>=1/4`, every nonempty `A` has `pi(A)>=1/4`, so every constraint already holds at time zero and `rho^(sqrt3)=0`.

Conversely, if `pi_*<1/4`, choose a minimum-mass state `x_*` and `A={x_*}`. Then `b(pi_*)<1`, while the survival probability starts at `1` and is continuous at zero (indeed for a singleton it is an exponential with positive exit rate). Thus the constraint needs strictly positive time, and `rho^(sqrt3)>0`. This proves (6.4).

## 7. The two-state boundary family — exact formulas

Take states `{0,1}` with

\[
\pi(0)=p,\qquad \pi(1)=1-p,
\qquad 0<p<\frac14,
\]

and generator

\[
q_{01}=(1-p)\lambda,
\qquad q_{10}=p\lambda,
\qquad \lambda>0.
\tag{7.1}
\]

The unique positive eigenvalue of `L=-Q` is `lambda`. The worst `L2` start is state `0`, and

\[
d_{2,0}(t)^2=\frac{1-p}{p}e^{-2\lambda t}.
\tag{7.2}
\]

Hence the source threshold is exactly

\[
\boxed{
s_*(p)=\frac1{2\lambda}\log\frac{1-p}{3p}.
}
\tag{7.3}
\]

For the threshold-matched hitting profile, the only nontrivial set of stationary mass at most `1/2` is `A={0}`. Its exit time from state `0` is exponential with rate `(1-p)lambda`, and so

\[
\boxed{
\rho^{(\sqrt3)}(p)
=\frac1{(1-p)\lambda}
\log\frac1{p+\sqrt3\sqrt{p(1-p)}}.
}
\tag{7.4}
\]

Both (7.3) and (7.4) vanish as `p` increases to `1/4`. By l'Hopital,

\[
\frac{\log[1/(p+\sqrt3\sqrt{p(1-p)})]}
{\log[(1-p)/(3p)]}
\longrightarrow\frac38,
\]

while `2/(1-p) -> 8/3`. Therefore

\[
\boxed{
\frac{\rho^{(\sqrt3)}(p)}{s_*(p)}\longrightarrow1.
}
\tag{7.5}
\]

This is a useful positive diagnostic: matching the hitting threshold to the source threshold removes the artificial scale gap exactly at the source's singular boundary.

### Why the standard Hermon–Peres threshold cannot be substituted

For their conventional coefficient `1/2`, the same two-state chain has

\[
\rho^{(1/2)}(p)
=\frac1{(1-p)\lambda}
\log\frac1{p+\frac12\sqrt{p(1-p)}}.
\tag{7.6}
\]

As `p` increases to `1/4`, this tends to the strictly positive constant

\[
\frac4{3\lambda}
\log\frac8{2+\sqrt3},
\]

whereas `s_*(p)->0`. Hence

\[
\rho^{(1/2)}(p)/s_*(p)\to\infty.
\tag{7.7}
\]

Likewise

\[
\tau_2(1/2)
=\frac1{2\lambda}\log\frac{4(1-p)}p
\longrightarrow\frac1{2\lambda}\log12>0,
\]

so

\[
\tau_2(1/2)/s_*\to\infty.
\tag{7.8}
\]

This is not a criticism of Hermon–Peres: their theorem is correct for the conventional `1/2` mixing threshold. It is a source-normalization warning for C28. The Aldous–Fill quantity lives at `sqrt(3)`, and near `pi_*=1/4` changing the threshold by a fixed amount changes the relevant time by an unbounded multiplicative factor.

## 8. What this changes in the route

The previous C28 route diagnosis was:

- hard anchored spectral bins give exponential-scale localization and the optimal factor `2`, but are comparison-unstable at hard bin boundaries;
- every fixed finite-depth resolvent/proximal smoothing leaks polynomially in the spectrum and has no finite factor;
- infinite-depth resolvent iteration works only by reconstructing `P_t`.

This run adds a fourth fact:

- **Hermon–Peres provides a powerful constant-factor hitting characterization only after a threshold is fixed. The source threshold is not their conventional threshold.** A source-matched coefficient `sqrt(3)` has the correct zero boundary and is asymptotically exact on the simplest singular family, while the conventional coefficient `1/2` is infinitely far away in multiplicative time there.

The next mathematically meaningful question is therefore very specific:

\[
\boxed{
\text{Does there exist a universal }C<\infty\text{ such that }
 s_*\le C\,\rho^{(\sqrt3)}
\text{ for every finite irreducible reversible CT chain?}
}
\tag{8.1}
\]

Even a YES to (8.1) would still be only a probabilistic characterization unless the threshold-matched escape profile can then be bounded/characterized by a genuinely comparison-friendly variational object built directly from `E`. The killed survival functions satisfy

\[
\mathbf P_x(T_{A^c}>t)=(e^{-tL_A}\mathbf1_A)(x),
\]

where `L_A` is the Dirichlet restriction of `L`, so the object is determined by `E`; but merely computing all killed semigroups would again risk becoming a semigroup reconstruction rather than the static comparison tool sought by the source.

A promising next step is to inspect whether the Hermon–Peres maximal-inequality proof of `tau_2(1/2)<=C rho^(1/2)` can be re-run at `a=sqrt(3)` **without inserting an additive relaxation-time term that cannot be absorbed near `pi_*=1/4`**. The two-state family above is the mandatory boundary test for every proposed adaptation.

## 9. Current status and stuck/rotation bookkeeping

The frozen metric did not improve:

\[
\boxed{2\to2}.
\]

The predecessor report recorded unchanged count `2`. This run therefore makes it

\[
\boxed{2\to3}.
\]

Thus Section I is now triggered. **The next C28 invocation on I0032 must be a thinking/stuck run with no new theorem claim**, containing the exact blocker, every tried route and failure reason, the simplest unproved case, and the nearest solved theorem/ingredient that the source lacks. It must choose exactly one of the Section-I recovery actions and name three next Section-B moves. C28 is CLOSABLE; six unchanged runs force rotation with a preserved handoff.

C28 remains **PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY**. This run does not certify current worldwide openness, publication novelty, or source closure.

## 10. Directed second-audit duty — C29

The newest C29 report remains

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T21-37-27Z__dc34-stuck-two-defect-strategy.md`.

Its first line explicitly says **mandatory STUCK / THINKING run; no new C29 theorem claim**. Therefore I did **not** manufacture a redundant receipt-only audit. The latest legitimate C28→C29 pass remains

`C28-AUDIT-C29-DC34-ONE-DEFECT-08 = PASS (claim-scoped)`

for the preceding asymmetric one-defect exact semialgebraic-hull theorem. It does not settle Randomstrasse Conjecture 34, the two-defect regime, C29's frozen metric, or C29 admission/READY status. When C29 next produces an actual theorem-sized claim, that claim is the directed audit target.

## 11. Model/scheduler control escalation

The task-control surface exposed to this run provides title/prompt, schedule/timing, enabled state, and notification behavior. It still exposes **no model-family selector and no reasoning-effort selector**. Therefore GPT-6/maximum remains prompt text only; the actual runtime here reports GPT-5.6 Sol and reasoning level UNVERIFIED.

Making GPT-6/maximum enforceable would require the scheduler/backend (or an authorized enclosing runtime) to expose, persist, and bind model-family and reasoning-effort fields and to provide runtime telemetry proving they were applied. There is no worker-side field available to set them.

No task modification was attempted in this run. The historical P26 `"You cannot modify this task"` event remains an ownership/permission-context boundary; the fleet ledger records that a later P26 update succeeded from an authorized context. The valid workaround is owner/admin/coordinator action from the owning authorized workspace, or platform support if ownership metadata is defective — never a permission bypass or duplicate schedule.

## ledger_delta for P26

```text
track=C28
target=I0032 / Aldous-Fill Open Problem 8.23
source_parameter=s_*:=inf{s>=0: ||P_s||_{2->infinity}<=2}=tau_2(sqrt(3))
source_class=finite irreducible reversible continuous-time chains
frozen_candidate=S_anch,2(E) / binary state-anchored dyadic local-spectral threshold
metric=best proved uniform two-sided comparison factor
before=2
after=2
movement=no movement
unchanged_count_before=2
unchanged_count_after=3
status=PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY
new_claim=C28-I0032-THRESHOLD-HITTING-BRIDGE-08 = PROVED (PARTIAL relative to source)
new_claim_summary=s_*=tau_2(sqrt(3)); threshold-matched rho^(sqrt3)<=s_*; rho^(sqrt3)=0 iff s_*=0 iff pi_*>=1/4; on two-state p->1/4- family rho^(sqrt3)/s_*->1, while standard Hermon-Peres rho^(1/2)/s_* and tau_2(1/2)/s_* diverge
literature_correction=Hermon-Peres 2018 is direct later L2/hitting-time prior art, but its standard 1/2 threshold is not uniformly comparable to the Aldous-Fill source threshold near pi_*=1/4
section_B_moves=4,21,26
audit=no new C29 theorem to audit; prior C28-AUDIT-C29-DC34-ONE-DEFECT-08 PASS retained
reserve=Paley-ETF HARD RESERVE preserved, including p=73,m=14 kappa=6.6575355565204281495..., 161070 exact two-swap neighbors, neighbor upper bound 6.603863488301192967..., and existential-quantifier correction
stuck_protocol=triggered at unchanged count 3; next C28 invocation must be thinking/stuck with no new theorem claim
next_blocker=whether s_*<=C rho^(sqrt3) uniformly, and if so whether rho^(sqrt3) can be replaced by a genuinely comparison-friendly Dirichlet-form variational object without semigroup reconstruction
```
