Model: GPT-5.6 Sol. Reasoning level: UNVERIFIED; GPT-6/maximum was requested, but this runtime and the exposed scheduler provide no model-family selector or reasoning-effort selector, so I do not claim otherwise. **movement — frozen I0032 best-proved two-sided comparison factor +infinity -> 2 for the newly frozen canonical state-anchored dyadic characterization; Section-B moves 1, 27, 30.**

# C28 — state-anchored dyadic spectral characterization for Aldous–Fill Open Problem 8.23

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Run date: 2026-09-16.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, permission change, peer-file edit, shared-ledger edit, or new schedule.

## 1. Continuity, source scope, ownership, and reserve

I continued from the newest C28 report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T18-26-42Z__i0032-kozma-spectral-profile-obstruction.md`

rather than restarting. I reread/queried the campaign index/ranking, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, canonical claim `operations/claims/I0032.md`, exact-ID intake/attempt material, and the newest C29 report for the directed second-audit duty.

The canonical claim still gives C28 exclusive ownership of I0032 and remains **CLAIMED / PENDING_ADMISSION — NOT READY**. I found no conflicting I0032 claim or source-exact closure in the bounded search performed this run. A failed or incomplete search is not proof of openness.

The old Paley-ETF conditioning attack remains in **HARD RESERVE**. Preserve all its exact lower/upper bounds, exact phase examples, local-search certificates, and failed routes. In particular, the quantifier correction remains binding: one badly conditioned finite submatrix does **not** refute a source assertion that there exists a good asymptotic family.

## 2. Exact Aldous–Fill problem and current literature refresh

Aldous–Fill Chapter 8, §8.4.2 defines

\[
N(s)=\|P_s\|_{2\to\infty}
\]

for a finite irreducible reversible continuous-time chain and states that `N(s)` is continuous and decreases from `pi_*^{-1/2}` to 1. They then ask for a characterization, in terms of the Dirichlet form `E`, of the time `s*` such that `N(s*)=2 (say)`. This is Open Problem 8.23. The finite-`q` hypercontractive threshold `s_q` is introduced only afterwards and is a different parameter.

The total-domain convention remains

\[
 s_*:=\inf\{s\ge0:N(s)\le2\},
\tag{2.1}
\]

which agrees with the source root whenever `N(0)>2` and also handles small state spaces where the threshold is already met at time zero.

The source itself cites Diaconis–Saloff-Coste, *Logarithmic Sobolev inequalities for finite Markov chains* (1996), Theorem 3.9 with `q=infinity`, as a partial result. That theorem controls log-Sobolev information from a prescribed `2->q` bound but is not the requested exact characterization.

A fresh 2026-09-16 bounded literature search included the exact phrases

- `"Open Problem 8.23" "Characterize s*" Aldous Fill`,
- `"N(s)" "equals 2" "Dirichlet form" Markov chain`,
- `"spectral measure" "2 to infinity" Markov semigroup heat kernel diagonal Dirichlet form`,
- `"dyadic spectral" heat kernel diagonal reversible Markov chain mixing`,
- `"spectral projection" heat kernel diagonal reversible Markov chain mixing`, and
- `"local spectral measure" heat kernel Markov chain diagonal`.

These searches recover Aldous–Fill itself and the modern robustness/sensitivity line, including Hermon–Kozma, *Sensitivity of mixing times of Cayley graphs* (published online 2023, Canadian J. Math. 2024), which explicitly cites Aldous–Fill Open Problem 8.23 in the context of robust geometric mixing bounds. I did not locate a later source-exact resolution of 8.23 or the specific state-anchored dyadic packaging below. The underlying local spectral-measure and dyadic functional-calculus machinery is standard/folklore spectral theory; **no novelty claim is made** for that machinery, and the bounded search is not a publication certificate.

## 3. Previous candidate is dead, so freeze the replacement before comparing

The preceding C28 run proved that the ordinary spectral-profile candidate

\[
S_{\rm sp}(\mathcal E)
=\int_{4\pi_*}^{4/3}\frac{dv}{v\Lambda_{\mathcal E}(v)}
\]

has no finite reverse comparison with `s_*`: Kozma's sharpness construction yields `S_sp/s_* -> infinity`. The diagnosis was that the spectral profile may choose a different worst set at every mass scale and then add all those independent costs.

This run therefore changes category and quantifier order. We keep one starting state fixed through all spectral scales, aggregate its local spectral mass, and maximize over the state only at the end.

**Frozen replacement characterization, before comparison:** let

\[
L=-Q\ge0,
\qquad
\mathcal E(f,g)=\langle f,Lg\rangle_\pi,
\qquad
P_t=e^{-tL}.
\]

Let `gamma=lambda_1>0` be the spectral gap of `L`. For each state `x`, define the mean-zero point anchor

\[
r_x(y)=\frac{\mathbf 1_{\{y=x\}}}{\pi(x)}-1.
\tag{3.1}
\]

For `k>=0`, let

\[
\Pi_k=\mathbf 1_{[2^k\gamma,\,2^{k+1}\gamma)}(L)
\tag{3.2}
\]

be the basis-free spectral projector, and define the state-anchored band masses

\[
w_{x,k}=\|\Pi_k r_x\|_{2,\pi}^2.
\tag{3.3}
\]

Only finitely many are nonzero. Define

\[
D_x(t)=\sum_{k\ge0} e^{-2t\,2^k\gamma} w_{x,k},
\tag{3.4}
\]

and the canonical binary state-anchored threshold

\[
\boxed{
S_{\rm anch,2}(\mathcal E)
:=\inf\left\{t\ge0:\max_x D_x(t)\le3\right\}.
}
\tag{3.5}
\]

The threshold `3` is not adjustable bookkeeping: it is forced by the source normalization `N=2`, because `N(t)^2-1=3` at threshold.

## 4. Exact heat-kernel / local-spectral identity

### Lemma `C28-I0032-LOCAL-SPECTRAL-03`

For every finite irreducible reversible continuous-time chain in the source class,

\[
F_x(t):=\langle r_x,e^{-2tL}r_x\rangle_\pi
=\frac{P_{2t}(x,x)}{\pi(x)}-1,
\tag{4.1}
\]

and

\[
\boxed{N(t)^2=1+\max_x F_x(t).}
\tag{4.2}
\]

### Proof

The evaluation functional on `L^2(pi)` at `x` is represented by `delta_x/pi(x)`. Hence

\[
\|P_t\|_{2\to\infty}^2
=\max_x\sum_y \frac{P_t(x,y)^2}{\pi(y)}.
\]

By reversibility and the semigroup identity,

\[
\sum_y \frac{P_t(x,y)^2}{\pi(y)}
=\frac{P_{2t}(x,x)}{\pi(x)}.
\]

Since the constant spectral component contributes exactly one, subtracting it is exactly the same as replacing `delta_x/pi(x)` by the mean-zero anchor `r_x`. This proves (4.1) and (4.2).

Equivalently, if `mu_x` is the local spectral measure of `L` at `r_x`, then

\[
F_x(t)=\int_{(0,\infty)} e^{-2t\lambda}\,d\mu_x(\lambda).
\tag{4.3}
\]

Thus the source threshold is

\[
\boxed{
 s_*=\inf\left\{t\ge0:\max_x F_x(t)\le3\right\}.
}
\tag{4.4}
\]

## 5. Main theorem: uniform factor 2

### Theorem `C28-I0032-ANCHORED-DYADIC-04`

For every finite irreducible reversible continuous-time Markov chain, with exactly the source normalization above,

\[
\boxed{
 s_*\le S_{\rm anch,2}(\mathcal E)\le 2s_*.
}
\tag{5.1}
\]

In particular, the newly frozen binary state-anchored Dirichlet/spectral characterization has a proved uniform two-sided factor `2` on the **entire source class**. The factor `2` is a proved comparison factor; **its optimality for this frozen candidate is UNMEASURED**.

### Proof

Fix `x`. On the `k`th spectral band,

\[
2^k\gamma\le\lambda<2^{k+1}\gamma.
\]

Therefore for every `t>=0`,

\[
e^{-2t\lambda}
\le e^{-2t\,2^k\gamma}
\le e^{-t\lambda}.
\tag{5.2}
\]

Integrating (5.2) against the local spectral mass of `r_x` on each band and summing gives

\[
\boxed{F_x(t)\le D_x(t)\le F_x(t/2).}
\tag{5.3}
\]

Taking maxima over `x`, if `D_x(t)<=3` for every `x`, then `F_x(t)<=3` for every `x`; hence `s_*<=S_anch,2`.

Conversely, continuity of the finite sum in (4.3) implies that the threshold in (4.4) is attained. At `t=2s_*`, (5.3) gives

\[
D_x(2s_*)\le F_x(s_*)\le3
\]

for every `x`, hence `S_anch,2<=2s_*`.

The edge case `s_*=0` causes no problem. Then `F_x(0)<=3` for every `x`, while `D_x(0)=F_x(0)` exactly because the dyadic bands partition the positive spectrum. Thus `S_anch,2=0` as well.

This completes the proof.

## 6. Parametric refinement, deliberately not used to game the frozen metric

For any fixed `rho>1`, one may instead use spectral bands

\[
[\rho^k\gamma,\rho^{k+1}\gamma)
\]

and define

\[
D_{\rho,x}(t)=\sum_k e^{-2t\rho^k\gamma}\,w^{(\rho)}_{x,k}.
\]

The same scalar comparison gives

\[
F_x(t)\le D_{\rho,x}(t)\le F_x(t/\rho),
\]

so the corresponding threshold obeys

\[
 s_*\le S_{\rm anch,\rho}\le\rho s_*.
\tag{6.1}
\]

This is useful evidence that the discretization loss is controllable. It is **not** used to rewrite the frozen run metric as an artificial `1+epsilon`: the canonical binary candidate (3.5) was frozen before its comparison proof, and its recorded factor for this run is `2`.

At the opposite extreme, the exact unbinned local spectral measure recovers `s_*` itself. That is tautological functional calculus and is not being presented as the source's intended comparison-friendly solution.

## 7. Explicit procedure (Move 19's earlier demand, now made comparison-valid)

The construction is an actual finite procedure determined by `E` and `pi`:

1. Recover the self-adjoint generator `L` from `E(f,g)=<f,Lg>_pi` by finite-dimensional Riesz representation.
2. Compute the spectral gap `gamma` and the dyadic projectors `Pi_k=1_[2^k gamma,2^{k+1} gamma)(L)`. Conceptually no choice of eigenbasis is needed.
3. For each state `x`, form `r_x` and the band masses `w_{x,k}=||Pi_k r_x||^2`.
4. Form the finite monotone exponential sums `D_x(t)`.
5. Solve the one-dimensional monotone threshold equation `max_x D_x(t)=3` (or return zero if already below threshold).

No finite simulation is involved. I did not manufacture a checker: the new claim is an analytic theorem with its complete proof above.

## 8. Why this route escapes the Kozma obstruction, and why it is still PARTIAL

The ordinary spectral profile independently optimizes a bad set at each volume scale. Kozma's family exploits exactly that freedom: many unrelated bad scales contribute additively to the profile integral even though no single worst-start heat trajectory pays all of them.

The new state-anchored functional swaps the quantifiers:

- first fix `x`;
- keep the same local spectral measure of `r_x` through every band;
- add the costs across spectral scales;
- only then maximize over `x`.

That cross-scale compatibility is exactly what the previous diagnosis demanded, and (5.3) shows that it loses at most a factor two.

However, this does **not** yet justify calling Aldous–Fill Open Problem 8.23 solved. Their motivation explicitly says “especially for use in conjunction with the comparison technique.” The present functional uses spectral projectors of the full generator. Although it is basis-free and determined by `E`, its stability under coarse Dirichlet-form comparison is not established, and computing those projectors is close to spectral diagonalization. Thus the theorem is an honest source-matching **PARTIAL** characterization/algorithm, not a comparison-technique closure.

The next high-value question is therefore not another approximation lemma. It is whether the state-anchored band masses admit a variational or comparison-stable surrogate, e.g. through resolvent/K-functional quantities, that preserves the same one-anchor-across-scales structure.

## 9. Section-B moves this run

The preceding run used moves 5, 20, 22, so I did not repeat them.

### Move 1 — change category

I moved from set isoperimetry/spectral-profile data to **local spectral measures of point anchors** for the self-adjoint generator. Outcome: successful; it yields the factor-2 theorem.

### Move 27 — swap the quantifiers

Instead of choosing a new extremal set at every scale, fix one state `x` over all scales and maximize over `x` only after aggregation. Outcome: successful; this removes the exact incompatibility exposed by Kozma's example.

### Move 30 — one scale at a time

Partition the positive spectrum into dyadic bands and compare the heat multiplier on each band separately. Outcome: successful; summing the scalar inequalities produces (5.3) with no accumulation of scale-dependent constants.

## 10. Directed second-audit duty: C29

Newest C29 claim audited:

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T18-37-17Z__dc34-fivepoint-spike-threshold.md`.

C29 studies

\[
K_4=\{(0,0,0),(1,0,0),(0,1,0),(1,1,1)\}
\]

with planar directions `(1,0)`, `(0,1)`, `(1,-alpha)`, adds

\[
P=(a,b,ab+\delta),
\]

and defines

\[
U_\delta(s,t)=st+\delta T_a(s)T_b(t),
\qquad
\delta_c(a,b)=\min\{a(1-b),(1-a)b\}.
\]

I independently checked the core calculation.

On each of the four cells cut by `s=a,t=b`, along `d=(1,-alpha)`,

\[
D_d^2(st)=-2\alpha,
\qquad
D_d^2(\delta T_aT_b)=-2\alpha\delta p_sp_t.
\]

The two mixed-sign cells give exactly

\[
\delta\le a(1-b),
\qquad
\delta\le(1-a)b,
\]

while the same-sign cells are automatically concave. The one-sided slope jumps at the tent kinks are downward, so there is no missing positive singular curvature. Hence `U_delta` is `D_2`-concave iff `delta<=delta_c`.

The lower boundary remains the previous

\[
h(s,t)=\max\{0,\ st-\alpha^{-1}t(1-t),\ s+t-1\}
\]

because `h` is still admissible at the upward spike and any five-point minorant is in particular an admissible four-corner minorant. For the reverse inclusion, the four cross-grid points follow by coordinate laminations; on each of the four rectangles `U_delta` is bilinear, so coordinate laminations generate its full graph from the nine grid nodes; vertical lamination with the already-generated lower graph fills the interval. This validates the claimed finite-round semialgebraic hull in the subcritical regime.

Finally,

\[
\delta_c(a,b)
\le\sqrt{a(1-a)b(1-b)}\le\frac14,
\]

with equality exactly at `a=b=1/2`, so the stated extremal threshold is correct.

Verdict:

\[
\boxed{\texttt{C28-AUDIT-C29-DC34-FIVEPOINT-SPIKE-06 = PASS (claim-scoped).}}
\]

Scope: this PASS covers the subcritical five-point exact hull, the iff threshold for the simple upper envelope, finite-lamination semialgebraicity, and the `1/4` extremum. It does **not** prove Randomstrasse Conjecture 34, does not prove supercritical nonsemialgebraicity, and does not change C29's frozen metric of 2.

## 11. Metric and status

Previous frozen candidate: ordinary spectral profile; best two-sided factor `+infinity` (finite factor disproved by the Kozma family).

Newly frozen candidate before comparison: `S_anch,2(E)` in (3.5).

**Frozen metric this run:**

\[
\boxed{+\infty\longrightarrow 2}
\]

where `2` means “proved uniform two-sided comparison factor on the complete finite irreducible reversible continuous-time source class.” It does **not** mean that 2 is the optimal constant for this candidate. Sharpness remains **UNMEASURED**.

Source-level status: **PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY**.

No source-level closure is claimed. No finite simulation is used to establish an asymptotic statement.

## 12. `ledger_delta` for P26

```text
track=C28
target=I0032 / Aldous-Fill Open Problem 8.23
source_parameter=s_*:=inf{s>=0: ||P_s||_{2->infinity}<=2}
source_class=finite irreducible reversible continuous-time chains
old_candidate=ordinary spectral-profile integral S_sp
old_metric=+infinity (no finite reverse factor; Kozma obstruction)
new_candidate=S_anch,2(E): binary state-anchored dyadic local-spectral threshold
new_metric=2 (proved uniform two-sided factor; optimality UNMEASURED)
status=PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY
movement=yes
unchanged_streak=0
new_claim=C28-I0032-ANCHORED-DYADIC-04: s_* <= S_anch,2 <= 2 s_*
audit=C28-AUDIT-C29-DC34-FIVEPOINT-SPIKE-06 = PASS (claim-scoped)
paley_etf=HARD RESERVE unchanged; existential-quantifier correction preserved
shared_ledger_edit=no (P26 only)
report_path=proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T19-36-48Z__i0032-state-anchored-dyadic-spectrum.md
```

## 13. Model / scheduler control escalation

The actual exposed task-control object was inspected this run. It provides title, prompt, schedule/timing mode, enablement, and notification metadata, but **no model-family field and no reasoning-effort field**. Thus GPT-6/maximum remains requested in prompt text only; this worker cannot truthfully report it as enforced.

To make GPT-6/maximum enforceable, the scheduler/backend schema or an authorized enclosing runtime must expose and persist model and reasoning selectors and bind execution to them.

A historical task modification error reading `You cannot modify this task` is an ownership/permission-context boundary, not evidence that repository edits can fix the scheduler. The legitimate workaround is modification by the owner/admin/coordinator from the task's owning authorized workspace/context. Do not bypass the boundary or create a duplicate task to simulate ownership.
