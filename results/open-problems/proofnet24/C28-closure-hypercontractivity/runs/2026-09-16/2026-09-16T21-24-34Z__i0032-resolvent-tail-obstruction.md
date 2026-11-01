Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum. GPT-6/maximum was requested, but the runtime/task controls exposed here provide no model-family selector or reasoning-effort selector, so I do not claim otherwise. **no movement — frozen I0032 comparison metric remains `2 -> 2`; unchanged-run count `1 -> 2`; Section-B moves 17, 20, 22. New result: every fixed finite-depth resolvent/proximal approximation has UNBOUNDED comparison factor with the source `s_*`, already on transitive uniform refresh chains.**

# C28 — finite-resolvent tail obstruction for Aldous–Fill Open Problem 8.23

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Run date (UTC report path): 2026-09-16.
Allocation/status: CLOSABLE OUTSIDE, **CLAIMED / PENDING_ADMISSION / NOT READY**.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access change, shared-ledger edit, peer-file edit, or new schedule.

## 1. Continuity, repository sweep, ownership, and reserve

I continued from the newest durable C28 report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-16/2026-09-16T20-24-56Z__i0032-dyadic-sharpness-instability.md`

rather than restarting. The live C28 run directory contains the four predecessor reports at 17:36, 18:26, 19:36, and 20:24 UTC; no newer C28 report was present at run start.

I reread/queried the campaign `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, canonical claim `operations/claims/I0032.md`, the exact I0032 intake row in `probability_1000_intake_I_20260914/problems.jsonl`, repository-wide I0032 attempt/history hits, the newest C29 neighboring report, and the prior C27 audit chain. Large intake/attempt surfaces were queried by exact IDs/source phrases; I do not describe that as manually rendering every byte of every JSONL file.

The canonical claim still says Owner C28 and **CLAIMED / PENDING_ADMISSION — NOT READY**. No competing canonical I0032 claim was found. `QUEUE.md` still lists I0032 as an admission candidate; root `RESULTS.md` has an older stale C28 value and therefore cannot overwrite the newer complete C28 reports. The exact intake row labels Open Problem 8.23, Section 8.4, and was recorded as `open_per_source`; current status is rechecked separately below rather than inherited blindly from that 14 September intake row.

The old Paley-ETF conditioning attack stays in **HARD RESERVE**. Preserve the newer exact reserve facts from the predecessor report: at `(p,m)=(73,14)`,

\[
\kappa_*
=\sqrt{\frac{\sqrt{73}-1+2\sqrt{13}}
{\sqrt{73}-1-2\sqrt{13}}}
=6.6575355565204281495\ldots,
\]

with strict exact two-swap local maximality against all

\[
\binom{14}{2}\binom{60}{2}=161070
\]

exchange-radius-two neighbors and a proved common neighbor upper bound `6.603863488301192967...`; the archived checker ends `ALL_EXACT_CHECKS_PASS`. This is a finite local statement only. The governing quantifier correction is unchanged: one badly conditioned finite submatrix, even an exact local maximum, does **not** refute an existential assertion that some asymptotic family is uniformly well conditioned.

## 2. Exact source scope and current-literature check

Aldous–Fill Chapter 8, §8.4.2 considers a finite irreducible reversible continuous-time chain and defines

\[
N(s)=\|P_s\|_{2\to\infty}.
\]

The source says that it would be useful, especially for the comparison technique, to characterize in terms of the Dirichlet form `E` the time `s*` at which `N(s)=2`, and states Open Problem 8.23: **Characterize `s*` in terms of `E`.** The later finite-`q` quantities

\[
s_q=\inf\{s:\|P_s\|_{2\to q}\le1\}
\]

are different source parameters. I continue to use the total-domain convention

\[
s_*:=\inf\{s\ge0:\|P_s\|_{2\to\infty}\le2\},
\tag{2.1}
\]

which equals the source root whenever that positive root exists and gives `s_*=0` when `N(0)<=2`.

Fresh bounded searches in this run included:

- `"Open Problem 8.23" Aldous Fill "Characterize s*" Dirichlet form`;
- `"s*" "2 to infinity" "Dirichlet form" Markov chain hypercontractivity`;
- `"Sensitivity of mixing times of Cayley graphs" Aldous Fill 8.23`;
- `"On sensitivity of uniform mixing times" Hermon`;
- `resolvent ultracontractivity finite Markov chains Nash inequality`.

They recover the live Aldous–Fill source, Diaconis–Saloff-Coste's 1996 log-Sobolev paper, Hermon's uniform-mixing sensitivity result, and Hermon–Kozma, *Sensitivity of mixing times of Cayley graphs* (published online 18 July 2023; *Canadian Journal of Mathematics* 76(4), 2024, 1400–1431). Hermon–Kozma explicitly cite Aldous–Fill Open Problem 8.23 in their robustness discussion. Hermon's earlier result shows that uniform mixing times can change by an optimal `Theta(log log n)` factor under bounded edge-weight perturbations on bounded-degree graphs. I did not locate a later source-exact resolution of Open Problem 8.23 in these bounded searches. This is **not** proof of worldwide openness or a novelty certificate.

Diaconis–Saloff-Coste's machinery and the classical Nash/super-Poincare/resolvent technology are prior art around ultracontractivity. The new claim below is deliberately narrow: it is an exact obstruction to the specific finite-depth resolvent/proximal route suggested by C28's preceding report. I make no novelty claim for the resolvent variational identity or implicit-Euler approximation itself.

## 3. Frozen metric and the route inherited from the preceding run

Let

\[
L=-Q,\qquad \mathcal E(f,g)=\langle f,Lg\rangle_\pi,
\qquad P_t=e^{-tL},
\]

and

\[
r_x(y)=\frac{\mathbf1_{\{y=x\}}}{\pi(x)}-1.
\]

Then

\[
F_x(t):=\langle r_x,e^{-2tL}r_x\rangle_\pi
=\frac{P_{2t}(x,x)}{\pi(x)}-1,
\]

and the exact source bridge is

\[
N(t)^2=1+\max_xF_x(t).
\tag{3.1}
\]

The frozen binary state-anchored candidate from the 19:36 report is

\[
S_{\rm anch,2}(\mathcal E)
=\inf\{t:\max_xD_x(t)\le3\},
\]

with dyadic local spectral masses and

\[
F_x(t)\le D_x(t)\le F_x(t/2).
\]

Hence the already-proved full-source-class comparison is

\[
\boxed{s_*\le S_{\rm anch,2}(\mathcal E)\le2s_*}.\tag{3.2}
\]

The newest predecessor report proved the constant 2 **optimal** for this frozen binary candidate and showed the hard-band surrogate is discontinuously comparison-sensitive near bin edges. Therefore the frozen metric remains exactly

\[
\boxed{2\longrightarrow2}.
\]

That report proposed replacing hard spectral bands by the smoother resolvent functional

\[
R_x(a)=\langle r_x,(I+aL)^{-1}r_x\rangle_\pi
=\sup_g\{2\langle r_x,g\rangle_\pi-\|g\|_{2,\pi}^2-a\mathcal E(g,g)\}.
\tag{3.3}
\]

This run attacks that proposed route before promoting it to a new frozen candidate.

## 4. Section-B moves 17, 20, 22 — ideas before proof

The preceding run used 6, 24, 25; earlier C28 runs used 11, 18, 19; 5 (among the spectral-profile obstruction moves); and 1, 27, 30. This run therefore uses three different moves not found in the C28 history searched here.

### Move 17 — look for the numbers somewhere else

The key numerical distinction is **spectral-tail shape**. Heat flow damps a spectral value `lambda` by `exp(-2t lambda)`. A fixed resolvent damps it only by `(1+a lambda)^{-1}`, and any fixed finite implicit-Euler cascade damps it polynomially at high frequency. This points away from a merely smoother spectral partition and toward a tail-mismatch obstruction.

Outcome: productive. The complete refresh chain turns this heuristic into an exact calculation.

### Move 20 — find why the algorithm fails

Turn (3.3) into an actual constructive procedure: approximate `e^{-2tL}` by `n` implicit-Euler / proximal steps

\[
B_{n,t}:=\left(I+\frac{2t}{n}L\right)^{-n}.
\]

Then ask whether **any fixed depth `n`** already gives a uniform constant-factor characterization of `s_*`.

Outcome: decisive negative result. For every fixed `n`, the comparison factor is unbounded even on transitive refresh chains.

### Move 22 — read the failures, not the successes

Aldous–Fill explicitly motivate the desired characterization by comparison. Diaconis–Saloff-Coste already supply partial functional-inequality control rather than an exact `s_*` formula; Hermon and Hermon–Kozma show how delicate uniform mixing is under geometric perturbation. Combined with the predecessor's hard-band instability, this says that a useful answer cannot be obtained just by swapping discontinuous hard bands for a fixed finite robust rational filter.

Outcome: the next route must retain exponential/infinite-scale damping while avoiding a tautological reconstruction of the semigroup.

## 5. The finite-depth proximal characterization

For `n>=1` define

\[
B_{n,t}:=\left(I+\frac{2t}{n}L\right)^{-n},
\qquad
R_{x,n}(t):=\langle r_x,B_{n,t}r_x\rangle_\pi,
\tag{5.1}
\]

and its level-three threshold

\[
S_n(\mathcal E):=
\inf\{t\ge0:\max_xR_{x,n}(t)\le3\}.
\tag{5.2}
\]

This is a genuine Dirichlet-form procedure at every fixed finite `n`. One resolvent step solves

\[
(I+aL)^{-1}u
=\arg\min_g\left\{\|g-u\|_{2,\pi}^2+a\mathcal E(g,g)\right\},
\tag{5.3}
\]

so `B_{n,t}r_x` is obtained by `n` repeated minimizations with `a=2t/n`. Equivalently the scalar one-step quadratic form satisfies

\[
\langle f,(I+aL)^{-1}f\rangle_\pi
=\sup_g\left\{2\langle f,g\rangle_\pi-\|g\|_{2,\pi}^2-a\mathcal E(g,g)\right\}.
\tag{5.4}
\]

Thus fixed-depth `S_n` is exactly the kind of explicit variational/procedural surrogate suggested by the previous run. It is also smooth in the spectral parameter, unlike the hard dyadic projector construction.

## 6. Main new theorem — every fixed finite resolvent depth has infinite comparison factor

### Theorem `C28-I0032-FINITE-RESOLVENT-OBSTRUCTION-07 = PROVED (PARTIAL relative to source)`

For every fixed integer `n>=1`,

\[
\boxed{
\sup_{\substack{\text{finite irreducible reversible CT chains}\\s_*>0}}
\frac{S_n(\mathcal E)}{s_*}=+\infty.
}
\tag{6.1}
\]

The supremum is already infinite on the subclass of finite transitive chains with uniform stationary law. Consequently **no fixed finite number of resolvent/proximal steps can replace the frozen dyadic characterization with any uniform finite two-sided comparison factor.**

### Proof

Fix `n`. For `m>=5` and `lambda>0`, let the chain be the `m`-state refresh chain

\[
Q=\lambda(\Pi-I),
\tag{6.2}
\]

where `Pi` is averaging onto constants. It is finite, irreducible, reversible, transitive, and has uniform stationary distribution. Its Laplacian `L=-Q` has eigenvalue `0` on constants and the single positive eigenvalue `lambda` with multiplicity

\[
M:=m-1>3.
\]

For every state `x`, the centered point anchor `r_x` lies entirely in the positive eigenspace and

\[
\|r_x\|_{2,\pi}^2=M.
\tag{6.3}
\]

Therefore

\[
F_x(t)=M e^{-2\lambda t}.
\tag{6.4}
\]

By the exact source bridge (3.1), the source threshold is the unique solution of `F_x(t)=3`, namely

\[
\boxed{
s_* = \frac{\log(M/3)}{2\lambda}.
}
\tag{6.5}
\]

For the depth-`n` surrogate, the same one-eigenvalue calculation gives

\[
R_{x,n}(t)
=M\left(1+\frac{2t\lambda}{n}\right)^{-n}.
\tag{6.6}
\]

Its level-three threshold is therefore exactly

\[
\boxed{
S_n
=\frac{n}{2\lambda}\left[\left(\frac M3\right)^{1/n}-1\right].
}
\tag{6.7}
\]

Dividing (6.7) by (6.5),

\[
\boxed{
\frac{S_n}{s_*}
=\frac{n\big((M/3)^{1/n}-1\big)}{\log(M/3)}.
}
\tag{6.8}
\]

For fixed `n`, the numerator grows as a positive constant times `M^{1/n}` whereas the denominator grows only logarithmically. Hence

\[
\frac{S_n}{s_*}\longrightarrow\infty
\qquad(M\to\infty).
\]

This proves (6.1). `square`

### Interpretation

This is a **tail mismatch**, not a band-edge pathology. The heat kernel has exponential spectral damping. Every fixed-depth implicit-Euler filter has only polynomial high-frequency damping. A large point-anchor mass at one fast eigenvalue amplifies that mismatch until the threshold-time ratio diverges.

The same calculation immediately warns against any proposed replacement consisting of a fixed finite positive rational/Stieltjes combination whose high-frequency tail is only polynomial. I do not freeze or claim a maximally general class here; Theorem 07 itself needs only the exact `n`-step family above.

No checker was manufactured: the new claim is analytic, with a complete exact proof on this page and no finite enumeration component.

## 7. Infinite depth reconstructs the source exactly — but this is deliberately NOT counted as progress on the source

There is an important sanity check. Spectrally,

\[
\left(1+\frac{2t\lambda}{n}\right)^{-n}
\downarrow e^{-2t\lambda}
\qquad(n\to\infty).
\]

Since the source state space is finite, for every `x,t`,

\[
R_{x,n}(t)\downarrow F_x(t),
\tag{7.1}
\]

and therefore

\[
\max_xF_x(t)=\inf_n\max_xR_{x,n}(t).
\tag{7.2}
\]

Moreover

\[
S_n(\mathcal E)\downarrow s_*.
\tag{7.3}
\]

Indeed `R_{x,n}>=F_x`, so `S_n>=s_*`. If `s_*>0`, then for each `epsilon>0` the source's strict monotonicity gives `max_xF_x(s_*+epsilon)<3`; finite-spectrum convergence in (7.1) is uniform over the finitely many states, so `max_xR_{x,n}(s_*+epsilon)<3` for large `n`, implying `S_n<=s_*+epsilon`. If `s_*=0`, then the level-three condition already holds at time zero for every `n`, so `S_n=0`.

Thus an infinite sequence of Dirichlet-form proximal solves recovers `s_*` exactly. **I do not count this as a factor-1 solution, metric movement, or source closure.** It is the implicit-Euler/Hille–Yosida reconstruction of the semigroup from its generator. Since the Dirichlet form determines `L`, simply rebuilding `e^{-tL}` would make Aldous–Fill's comparison-motivated question tautological. Counting (7.3) as a source solution would game the problem rather than answer it.

This distinction is now explicit in the C28 handoff:

- hard state-anchored spectral bins: exponential-scale localization and an optimal finite factor `2`, but severe comparison instability at bin edges;
- any fixed finite-depth resolvent/proximal smoothing: comparison-friendly variational steps, but polynomial spectral leakage and **no finite uniform comparison factor**;
- infinite-depth resolvent iteration: exact exponential damping, but only because it reconstructs the semigroup itself.

A genuinely useful next characterization must therefore contain an **infinite-scale or exponential-tail mechanism without merely re-encoding `P_t`**, while retaining the successful state-anchoring quantifier order that defeated the ordinary spectral-profile route. An anchored capacity/Nash/super-Poincare-type object is the most plausible next category, but the earlier Kozma obstruction warns that maximizing independently at each scale will reintroduce the wrong quantifier order.

## 8. Current status and stuck/rotation bookkeeping

The frozen metric did not improve numerically:

\[
\boxed{2\to2}.
\]

The predecessor was the first unchanged run after the `+infinity -> 2` improvement, so this run makes the unchanged count

\[
\boxed{1\to2}.
\]

This is **not yet** the three-run stuck threshold. C28 remains **PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY**. The new obstruction is valuable route-pruning but is not a source characterization. If the metric remains unchanged on the next run, Section I triggers and the following invocation must be thinking/stuck rather than another theorem-producing run. As a CLOSABLE task, six unchanged runs trigger rotation under the owner directive.

## 9. Directed second-audit duty — C29 newest claim

Newest C29 theorem audited:

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T20-36-30Z__dc34-one-defect-exact-hull.md`,

claim `C29-DC34-ONE-DEFECT-SEMIALGEBRAIC-08`.

C29's setup has

\[
D_2=\mathbb R(1,0)\cup\mathbb R(0,1)\cup\mathbb R(1,-\alpha),\quad \alpha>1,
\]

a four-corner lifted hull, and a spike `(a,b,ab+delta)`. Its separately concave upper envelope is

\[
U_\delta(s,t)=st+\delta T_a(s)T_b(t),
\]

with mixed-cell activation thresholds

\[
\tau_{SE}=(1-a)b,\qquad \tau_{NW}=a(1-b).
\]

For `0<b<a<1` and

\[
(1-a)b<\delta<a(1-b),
\]

only the southeast cell is defective. C29 writes `c=delta/((1-a)b)`, `q=c-1`, and on that cell obtains exactly

\[
U_\delta=t(c-qs).
\]

On each line `r=t+alpha s`, this is a convex quadratic. I independently checked the line segment endpoints

\[
[s_0,s_1]=\left[\max\{a,(r-b)/\alpha\},\min\{1,r/\alpha\}\right]
\]

and the chord correction

\[
V-U_\delta=\alpha q(s-s_0)(s_1-s).
\]

Substitution reproduces C29's four formulas `V_A,V_B,V_C,V_D`. The report's derivative-jump inequalities (7.3)--(7.16) have the correct signs for third-direction and coordinate concavity. Its minimality argument is also sound: any `D_2`-concave majorant first dominates the separately concave envelope `U_delta`, then on each third-direction line must dominate that restriction's least concave majorant `V`. Finally, the reverse hull inclusion is genuinely constructive: the nine grid nodes and bilinear `U_delta` graph arise by coordinate laminations, one allowed third-direction chord creates graph `V`, and the vertical direction fills from the old exact lower graph `h` to `V`.

Verdict:

\[
\boxed{\texttt{C28-AUDIT-C29-DC34-ONE-DEFECT-08 = PASS (claim-scoped)}}.
\]

The PASS covers only C29's asymmetric **one-defect** exact semialgebraic-hull theorem. It does **not** certify Randomstrasse Conjecture 34, the two-defect regime, C29's frozen four-point metric, admission/READY status, or source-level closure.

## 10. Model/scheduler control escalation

The control surface available to this run still exposes prompt/title, schedule/timing, enabled state, and notification behavior, but no model-family selector and no reasoning-effort selector. Therefore GPT-6/maximum remains a prompt request, not an enforceable scheduler setting here. Making it enforceable requires scheduler/backend support, or an authorized enclosing runtime that exposes, persists, and binds those two fields.

The historical P26 `"You cannot modify this task"` case remains a permission/ownership-context issue, not a mathematical one. Root `RESULTS.md` records that the full P26 update later succeeded from an authorized context. The valid workaround is owner/admin/coordinator action from the owning authorized workspace (or platform support if ownership metadata is defective), never a permission bypass or duplicate schedule.

## ledger_delta for P26

```text
track=C28
target=I0032 / Aldous-Fill Open Problem 8.23
source_parameter=s_*:=inf{s>=0: ||P_s||_{2->infinity}<=2}
source_class=finite irreducible reversible continuous-time chains
frozen_candidate=S_anch,2(E) / binary state-anchored dyadic local-spectral threshold
metric=best proved uniform two-sided comparison factor
before=2
after=2
movement=no movement
unchanged_count_before=1
unchanged_count_after=2
status=PARTIAL / CLAIMED / PENDING_ADMISSION / NOT READY
new_claim=C28-I0032-FINITE-RESOLVENT-OBSTRUCTION-07 = PROVED (PARTIAL relative to source)
new_claim_summary=for every fixed n>=1, the n-step implicit-Euler/resolvent threshold S_n has sup S_n/s_*=infinity, already on finite transitive uniform refresh chains
formal_nonprogress=the infinite-depth proximal limit S_n downarrow s_* exactly, but this is semigroup reconstruction and is explicitly NOT counted as a source characterization or factor-1 metric movement
audit=C28-AUDIT-C29-DC34-ONE-DEFECT-08 = PASS (claim-scoped)
section_B_moves=17,20,22
reserve=Paley-ETF HARD RESERVE preserved, including p=73,m=14 kappa=6.6575355565204281495..., 161070 exact two-swap neighbors, neighbor upper bound 6.603863488301192967..., and existential-quantifier correction
next_route=seek an anchored infinite-scale/exponential-tail variational object (capacity/Nash/super-Poincare type) that does not simply reconstruct P_t and does not reintroduce cross-scale extremizer swapping
```
