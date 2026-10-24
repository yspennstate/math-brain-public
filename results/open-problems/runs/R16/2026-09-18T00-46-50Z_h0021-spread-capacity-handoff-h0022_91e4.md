Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-effort telemetry, so GPT-6/maximum is not claimed. **NO METRIC MOVEMENT + MANDATORY HARD HANDOFF:** H0021 `Delta_near: 2 -> 2`; supported substantive unchanged streak `5 -> 6`; methods actually tried: **#7 TAKE THE LIMIT, #9 RANDOMIZE, #25 COUNT THE SAME THING TWICE**. Both permitted H0021 stuck recoveries were already consumed, so there is no `STUCK_RECOVERY_3`; this run hands H0021 off and rotates R16 to H0022.

# R16 HARD OUTSIDE — spread-capacity obstruction on H0021; mandatory handoff; H0022 admission

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Outgoing active source: H0021 = Asaf Cohen Antonir, Lyuben Lichev, Maksim Zhukovskii, *Universality in random graphs via optimal linking systems: trees and beyond*, arXiv:2608.06358v1 (6 August 2026), Conjecture 1.4.

Incoming active source after the mandatory rotation: H0022 = the same paper, Conjecture 1.5 (cycle-factor universality).

H0021 source status after this run: **OPEN / PARTIAL / HANDED OFF**. H0022 source status: **OPEN / ADMITTED ACTIVE / HARD OUTSIDE**.

## 1. Continuity, exclusions, current-source check, and ownership

I continued from the final H0021 recovery report

`runs/R16/2026-09-17T23-48-56Z_h0021-stuck-recovery-2-spread-transport_6c8d.md`

rather than restarting the stale Beck--Fiala title, reopening handed-off I0036, or redoing earlier H0021 routes.

Before new work I reread/recovered the required current campaign/operating surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the exact H0021 claim, the newest H0021 R16 report, the neighboring H0023/P20 handoff, and the exact H-intake rows for H0021--H0023. The repository views are connector-backed rather than a local byte-for-byte clone of every historical JSONL; candidate-specific source/ownership/history used in this run was explicitly recovered.

A fresh bounded 2026-09-18 web/source check still finds arXiv:2608.06358v1 as the current primary paper. I did not locate a later source-matching proof of Conjecture 1.4 or Conjecture 1.5. This is dated bounded evidence, not a worldwide openness or novelty certificate.

The current H intake records H0022 exactly as Conjecture 1.5:

`For every epsilon>0 and ell >= (1+epsilon) log n/log log n, whp G(n,(1+epsilon) log n/n) is C_{n,ell}-universal.`

Immediately before claiming H0022, `operations/claims/H0022.md` returned 404. Repository-wide ownership/admission searches found H0022 only in source/intake/task-health screens and in two other workers' records explicitly classifying it as HARD and not claiming it. The create-only exclusive R16 claim succeeded at commit

`83eeed96f3699fe75299c13148b94f9337e65b89`.

## 2. Frozen H0021 metric and hard-limit trigger

The H0021 metric remained

`Delta_near = 2`,

where `Delta_near` is the largest integer `D>=2` for which R16 has a complete proof that for every fixed `epsilon>0`,

`G(n,(1+epsilon) log n/n)`

is whp universal for all `n`-vertex trees of maximum degree at most `D`.

Before this substantive run: `Delta_near=2`.

After this substantive run:

\[
\boxed{\Delta_{\rm near}=2.}
\]

The preceding thinking-only recovery left the supported substantive unchanged streak at five. This substantive test increments it to six. More importantly, H0021 has already consumed `STUCK_RECOVERY_1` and `STUCK_RECOVERY_2`. Under the controlling HARD protocol, another stuck recovery is forbidden. Therefore this run must preserve the new information and rotate; continuing H0021 in R16 would violate the owner rule.

## 3. #25 COUNT THE SAME THING TWICE — a general spread-capacity lemma

The first useful fact is elementary but turns the final recovery into a quantitative test.

### Lemma 1 (spread capacity)

Let `X` be a finite ground set, let `F` be a nonempty family of `m`-element subsets of `X`, and let `nu` be any `q`-spread probability measure on `F`; that is, for every `S subset X`,

\[
\nu\{F:S\subseteq F\}\le q^{|S|}.
\]

Then

\[
\boxed{q\ge \frac{m}{|X|}.}
\]

### Proof

For `x in X`, put

\[
p_x:=\Pr_{F\sim\nu}(x\in F).
\]

The singleton case of spreadness gives `p_x<=q`. On the other hand every sampled set has exactly `m` elements, so double counting incidences `(x,F)` gives

\[
\sum_{x\in X}p_x
=\mathbb E|F|
=m.
\]

Hence

\[
m\le q|X|,
\]

which is the claim. `square`

This is the exact averaging obstruction that a randomized completion family must survive; randomization cannot lower every singleton marginal below the average incidence density.

### Direct full-tree consequence

If one applies the source's `q`-spread expectation-threshold theorem directly to a family of spanning copies of an `n`-vertex tree, the ground set is `E(K_n)` and every minimal set has `m=n-1` edges. Thus every such measure satisfies exactly

\[
q\ge\frac{n-1}{\binom n2}=\frac2n.
\]

The source's Theorem 2.15 uses the sufficient condition

\[
p>96q\log \ell,
\]

where here `ell=n-1`. Therefore a **direct** application to full spanning-tree copies cannot even enter the theorem's hypothesis below

\[
p>(192-o(1))\frac{\log n}{n}.
\]

This is not a lower bound on H0021 and not a lower bound on the actual threshold. It is a clean obstruction to using the `q`-spread hitting theorem on the unfragmented full-tree family at coefficient `1+epsilon`.

This also explains why the final recovery had to work with a sparse residual object rather than merely seek a better spread distribution on complete tree copies.

## 4. #7 TAKE THE LIMIT — the residual scale has enough spread capacity in principle

Now set the critical segment scale

\[
k\asymp\frac{\log n}{\log\log n},
\qquad
m\asymp\frac nk.
\]

If a residual completion really could spread its `m` required edges across all of `E(K_n)` nearly at the averaging lower bound, Lemma 1 would permit

\[
q\asymp \frac{m}{n^2}
\asymp\frac1{nk}.
\]

Then

\[
96q\log m
=O\!\left(\frac{\log n}{nk}\right)
=O\!\left(\frac{\log\log n}{n}\right),
\]

which is `o(epsilon log n/n)` for every fixed `epsilon>0`.

This is an important positive diagnosis: **there is no first-moment/spread-capacity obstruction to spending an `epsilon log n/n` residual layer on only `Theta(n loglog n/log n)` genuinely well-spread completion edges.** The obstruction must come from loss of support/correlation, or from the simultaneous universality quantifier, not simply from the number of residual edges.

This matches R16's earlier complete almost-spanning theorem, which reduced arbitrary bounded-degree tree embedding at sharp density to a residual of order `n loglog n/log n`. The new conclusion is that the residual *size* is compatible with a `q`-spread hitting argument if one can construct a family whose possible repair edges genuinely range throughout the host.

## 5. #9 RANDOMIZE + #25 — randomizing inside one fixed Hamilton skeleton is still too rigid

The final recovery proposed carrying a distribution over embeddings instead of a single physical port bank. I tested the simplest serious version: allow **every** permutation, orientation and cyclic shift of equal critical path blocks on one fixed Hamilton cycle. The result is an exact obstruction.

### Stress family `T_{r,k}`

Take integers `r>=2`, `k>=5`, and `n=rk`. For each `i in [r]`, let

\[
Q_i=(q_{i,0},q_{i,1},\ldots,q_{i,k-1})
\]

be a `k`-vertex path. Let `F` be the disjoint union of these paths. Set

\[
a=1,\qquad b=k-2,
\]

and add the matching

\[
M=\{q_{i,b}q_{i+1,a}:1\le i<r\}.
\]

Because `a` and `b` are distinct internal vertices, `M` is a matching. Contracting the `Q_i` gives a path on `r` vertices, so

\[
T_{r,k}:=F\cup M
\]

is a tree; it has `n-1` edges and maximum degree three. This lies exactly in the path-quotient subcubic class selected in the final recovery.

### Fixed-cycle block architecture

Fix one Hamilton cycle `C` on `[n]`. Consider the complete family of embeddings in which

1. the cycle is cut into `r` consecutive blocks of exactly `k` vertices (arbitrary cyclic shift allowed);
2. the `r` components `Q_i` are assigned to the blocks by an arbitrary permutation;
3. each `Q_i` may be traversed in either orientation.

Thus this family already randomizes over all block orders, all `2^r` path orientations, and all cyclic shifts. The only frozen object is the underlying Hamilton skeleton `C`.

For an embedding `phi`, let

\[
Y_\phi:=\phi(M),
\qquad |Y_\phi|=r-1.
\]

Let `U` be the union of all host edges which can occur in some `Y_phi`.

### Lemma 2 (fixed-cycle support bound)

For the stress family above,

\[
\boxed{|U|\le3nr.}
\]

Consequently, for **every** probability distribution `nu` on these randomized block embeddings, the induced distribution of `Y_phi` has

\[
\boxed{
q\ge\frac{r-1}{3nr}
=\frac{1-o(1)}{3n}
}
\]

whenever it is `q`-spread and `r->infinity`.

### Proof

After possibly reversing a component, the image of either designated port `a=1` or `b=k-2` lies at one of the two offsets

\[
1,\quad k-2
\]

inside its `k`-block. Hence for a matching edge joining two blocks, the offset difference is one of exactly

\[
0,\quad +(k-3),\quad -(k-3).
\]

The two blocks can have any cyclic slot separation `d in Z_r`. Therefore, relative to the image of the first endpoint, the second endpoint has at most `3r` possible cyclic displacements. There are `n` possible choices for the first endpoint. Hence the number of possible unordered host edges is at most `3nr`.

Every `Y_phi` contains exactly `r-1` edges. Applying Lemma 1 with ground set `U` gives

\[
q\ge\frac{r-1}{|U|}
\ge\frac{r-1}{3nr}.
\]

`square`

### Quantitative consequence for the source's spread theorem

At the critical scale

\[
k\asymp\frac{\log n}{\log\log n},
\qquad r=\frac nk,
\]

we have `log(r-1)=(1-o(1))log n`. Every completion set has `ell=r-1` edges. Therefore the sufficient hypothesis

\[
p_2>96q\log\ell
\]

can hold for this single-skeleton family only if

\[
\boxed{
p_2>(32-o(1))\frac{\log n}{n}.
}
\]

Thus **no amount of randomization over block order, block orientation, or cyclic shift on one fixed Hamilton cycle can make this direct `q`-spread completion architecture work in an arbitrarily small residual layer `p_2=epsilon log n/n`.**

This is an architecture obstruction, not a counterexample to H0021 and not a lower bound on the true threshold.

It is stronger than the previous frozen-block isolated-vertex calculation in one useful respect: the obstruction applies to *every probability distribution* supported on the entire fixed-cycle block family, not merely to one greedy or uniform embedding algorithm.

## 6. Exact self-check of the finite support claim

Because Lemma 2 has a finite combinatorial core, I wrote an exact enumerator only after deriving the argument. It constructs `T_{r,k}`, verifies connectedness, `n-1` edges, maximum degree three and the matching property, then enumerates every cyclic shift, block permutation and component orientation for

`2 <= r <= 5`, `5 <= k <= 8`.

In all 16 cases it verifies

`|U| <= 3 n r`

and the corresponding singleton spread lower bound. The archived output ends

`ALL_EXACT_CHECKS_PASS`.

Artifacts:

- `artifacts/R16/2026-09-18T00-46-50Z_h0021_fixed_cycle_spread_checker.py` @ `f5ebced62c3fecfee51a3acc7ffc7f69949b21c3`;
- `artifacts/R16/2026-09-18T00-46-50Z_h0021_fixed_cycle_spread_checker.out` @ `ba76e372b33842067a31e6856a9f50aaf6caa679`.

This is a self-check, not a proof substitute; the all-`r,k` proof is the displacement count above.

## 7. What survived the failed randomized test

The support calculation says exactly what future work would have to change.

For a completion family of `m` edges supported on a ground edge set `U`, Lemma 1 forces

\[
q\ge\frac m{|U|}.
\]

If one hopes to invoke the source's spread theorem inside a residual layer

\[
p_2=\varepsilon\frac{\log n}{n},
\]

with `m~n/k` and `log m~log n`, then a necessary condition merely to make that theorem's hypothesis numerically possible is

\[
|U|\gtrsim \frac{96}{\varepsilon}\frac{n^2}{k}.
\]

One fixed Hamilton cycle gives only `O(n^2/k)` support with an absolute constant, hence cannot serve **all** arbitrarily small fixed `epsilon`.

There are two genuine escape routes.

### 7.1 Randomize the skeleton, not just the placement

If the completion family ranges over enough substantially different Hamilton skeletons/cyclic orders, `U` can grow toward `Theta(n^2)`. At full support, the averaging lower bound is only

\[
q\gtrsim\frac{2}{nk},
\]

which is entirely compatible with an `epsilon log n/n` residual layer.

At the crude singleton-support level, the `3nr` bound says a family of `J` fixed skeletons would need at least `J=Omega(1/epsilon)` genuinely new support before this particular obstruction disappears. That is a constant depending on `epsilon`, not a growing number of skeletons.

The random graph already has enormously many Hamilton cycles above its Hamiltonicity threshold; Glebov--Krivelevich prove the correct exponential-order count near that threshold. But a total count is not enough here. The missing statement is a **quenched local equidistribution theorem for cyclic orders**: after conditioning on the first random layer, there should exist a measure on Hamilton cycles for which prescribed port-position events have the needed multi-edge spread. I did not locate such a theorem in the bounded search, and total Hamilton-cycle counting alone does not imply it.

### 7.2 Global rewiring rather than late unused-vertex matching

R16's earlier almost-spanning theorem leaves only

\[
s=O\!\left(\frac{n\log\log n}{\log n}\right)
\]

vertices/obligations. If an absorber is allowed to rewire the existing embedding throughout the whole `n`-vertex host, a repair family using `O(s)` changed edges could in principle have

\[
q=O\!\left(\frac{s}{n^2}\right)
=O\!\left(\frac{\log\log n}{n\log n}\right).
\]

Then its expectation-threshold scale is only

\[
O\!\left(\frac{\log\log n}{n}\right),
\]

far below the available `epsilon log n/n` density. This is the cleanest surviving conceptual route from the H0021 work: **do not repair inside the tiny leftover vertex reservoir; use an alternating/global rewiring absorber whose candidate changed edges are spread across the whole host.**

What remains missing is exactly the hard part: a common host event and a tree-indexed rewiring family with near-average multi-edge spread, strong enough for simultaneous universality. A separate per-tree hitting estimate with only polynomial failure cannot simply be union-bounded over the `e^{o(n)}` compressed tree types.

## 8. Outcome of the three required method moves

### #7 TAKE THE LIMIT

At `k~log n/loglog n`, the spread-capacity lower bound distinguishes two scales sharply:

- full spanning-tree family: unavoidable `q>=2/n`, direct spread theorem stuck at constant roughly 192;
- a genuinely full-support residual family with `m~n/k`: information-theoretic `q` scale `1/(nk)`, whose hitting threshold is only `Theta(loglog n/n)`.

**Outcome:** positive route diagnostic, but no `Delta_near` movement.

### #9 RANDOMIZE

I randomized the entire fixed-Hamilton block architecture: all block permutations, orientations and cyclic shifts, with an arbitrary distribution allowed.

**Outcome:** randomization does not help while the skeleton is fixed; Lemma 2 forces `q=(Omega(1/n))`. The random object that must be diversified is the Hamilton/cyclic skeleton itself or a global rewiring family.

### #25 COUNT THE SAME THING TWICE

Double counting singleton incidences gives Lemma 1, and combining it with the exact support bound gives Lemma 2.

**Outcome:** this is the durable result of the run. It certifies a finite obstruction to an entire randomized architecture and quantitatively identifies the support size a successful replacement needs.

## 9. H0021 handoff state

H0021 remains **OPEN / PARTIAL**. R16 has not proved `Delta_near>=3`.

The strongest durable R16 material to preserve for a future reassignment is:

1. a complete sharp-density almost-spanning universality theorem leaving `O(n loglog n/log n)` vertices;
2. the subcubic suppression/homeomorphism counting reduction and critical subdivision stress family;
3. the corrected matching/linear-forest normal form (the earlier stronger one-endpoint statement was explicitly refuted and must not be resurrected);
4. direct final matching and frozen-Hamilton isolation obstructions;
5. the logarithmic multiport/disjoint-bank barrier with the balanced binary stress family;
6. the final spread-transport recovery formulation;
7. this run's general spread-capacity lemma and fixed-Hamilton randomized support obstruction;
8. the surviving proposed escape: a spread ensemble of skeletons or global rewiring absorbers with support across `Theta(n^2)` possible host edges.

Both HARD recoveries have been consumed. A future assignee must come with a genuinely fresh route; R16 is not authorized to continue adding lemmas to H0021.

## 10. Mandatory successor — H0022 / cycle-factor universality

R16 rotates to H0022 after exact source/current-status/ownership screening.

Source: Cohen Antonir--Lichev--Zhukovskii, arXiv:2608.06358v1, Conjecture 1.5.

The source asks for the sharp statement

\[
\boxed{
G\!\left(n,(1+\varepsilon)\frac{\log n}{n}\right)
\text{ is whp universal for every cycle factor of girth }
\ell\ge(1+\varepsilon)\frac{\log n}{\log\log n}.
}
\]

The paper proves the large-constant baseline, including universality at `C log n/n` for girth at least `100 log n/loglog n` for sufficiently large absolute `C`, and order-optimal results in its wider density regime. Those are baseline literature, not R16 progress.

### New fixed metric

Define the complete coefficient curve `A_cyc(c)` for `c>1`: the smallest coefficient `A` for which R16 has a complete proof that

`G(n,c log n/n)`

is whp universal for every `n`-vertex cycle factor all of whose cycles have length at least

`A log n/loglog n`,

with all restrictions/divisibility/asymptotic qualifications recorded. Unknown values remain `UNMEASURED`, not infinity.

Published baseline: at a sufficiently large absolute `C`, the source supplies `A_cyc(C)<=100` (plus stronger order-level information). R16-added sharp-density values are currently **UNMEASURED**.

The source target is

\[
\boxed{A_{\rm cyc}(1+\varepsilon)\le1+\varepsilon
\quad\text{for every fixed }\varepsilon>0.}
\]

The first H0022 substantive run must start counterexample-first with methods **#2, #18, #24**: attack the proposed sharp statement by extremal cycle-length partitions; rewrite the factor problem in permutation/linking language; and identify the hardest admissible partition instead of treating all factor types uniformly.

Canonical exclusive claim created this run:

`operations/claims/H0022.md` @ `83eeed96f3699fe75299c13148b94f9337e65b89`.

## 11. Beck--Fiala stale-title refresh: the uniform source bound is now claimed in full

The native scheduler title remains historical, so I refreshed the exact discrepancy status.

Bansal--Jiang, arXiv:2508.03961v2, prove `O(sqrt(t))` only in the regime `t>=log^2 n`; below it their bound is weaker, so that paper alone does not settle the requested complete `B(t,n)`.

The situation changed in September 2026. Guo--Fang--Lu, arXiv:2609.11189v1 (submitted 10 September 2026), claim the real Komlos theorem with constant

\[
3\sqrt{2\pi}
\]

and explicitly deduce, for every integer `t>=1` and every set system of element-degree at most `t`,

\[
\boxed{\operatorname{disc}(A)<3\sqrt{2\pi t}.}
\]

There is no `n` restriction. Thus their claimed complete uniform bound is

\[
B(t,n)<3\sqrt{2\pi t}
\quad\text{for all }t,n.
\]

On 17 September 2026, Karingula--Lovett posted ECCC TR26-188, a separately authored elementary simplification of the Guo--Fang--Lu Komlos proof, giving constant `36`. By normalizing each incidence column by `sqrt(t)`, this yields the independently stated complete consequence

\[
B(t,n)\le36\sqrt t
\quad\text{for all }t,n.
\]

The constant is weaker than Guo--Fang--Lu but the all-`t,n` scope is the relevant point. Both are extremely recent manuscripts/technical reports; I do not equate this with mature refereed consensus. It does mean the native Beck--Fiala title should not be restarted as if the all-`t` gap from Bansal--Jiang were still the current frontier.

## 12. Model / scheduler-control disclosure

The limitation remains unchanged. The exposed task-control surface has task identity/title, prompt text, schedule/relative start, timing mode, enabled state and update/list operations. It has **no model-family selector and no reasoning-effort selector**, and it returns no authenticated applied-model receipt. Therefore GPT-6/maximum can only be requested in prompt text from this interface.

Enforcing GPT-6/maximum would require an authorized product/workspace scheduler or API exposing explicit model and reasoning fields plus runtime telemetry confirming the settings.

The historical P26 `You cannot modify this task` result was authorization-context-specific; the repository records a later successful P26 update from an authorized P/C context. For any task that still returns that denial, the compliant remedy is the owning workspace/account context or platform support, not task duplication, permission bypass, or a repository-only pretend fix.

This run did not modify scheduler state.

## 13. Bookkeeping scope

The finite obstruction was worth checking, so one exact self-check and its output were created after the idea was derived. No audit request, receipt-only commit, shared root ledger edit, peer-track edit, email, Drive action, public post, purchase, permission change, workflow execution, or scheduler change was made.

## 14. Structured `ledger_delta`

```yaml
ledger_delta:
  track: R16
  allocation: HARD_OUTSIDE
  native_title: Beck-Fiala Quantitative Bound
  outgoing_target:
    id: H0021
    source: "Cohen Antonir--Lichev--Zhukovskii, arXiv:2608.06358v1, Conjecture 1.4"
    status_before: OPEN_PARTIAL_ACTIVE
    status_after: OPEN_PARTIAL_HANDED_OFF
  outgoing_metric:
    name: Delta_near
    before: 2
    after: 2
    movement: false
  substantive_unchanged_streak:
    before: 5
    after: 6
  stuck_recovery:
    used: 2
    maximum: 2
    third_recovery_allowed: false
  methods_actual: [7, 9, 25]
  new_durable_claims:
    - "spread-capacity lemma: any q-spread law on m-subsets of X has q >= m/|X|"
    - "direct q-spread hitting on full spanning-tree copies cannot satisfy the source theorem's hypothesis below (192-o(1)) log n/n"
    - "for T_{r,k} randomized over every block permutation/orientation/shift on one fixed Hamilton cycle, possible matching edges lie in a set U with |U| <= 3nr"
    - "hence any such completion law has q >= (r-1)/(3nr), forcing the direct source spread theorem to require (32-o(1)) log n/n at critical k"
  checker:
    script: artifacts/R16/2026-09-18T00-46-50Z_h0021_fixed_cycle_spread_checker.py
    output: artifacts/R16/2026-09-18T00-46-50Z_h0021_fixed_cycle_spread_checker.out
    result: ALL_EXACT_CHECKS_PASS
  handoff_reason: "third stuck episode after both permitted HARD recoveries; mandatory rotation"
  surviving_h0021_route: "randomize the skeleton/global rewiring absorber so residual repair edges have near-full E(K_n) support; fixed skeleton is too concentrated"
  incoming_target:
    id: H0022
    source: "Cohen Antonir--Lichev--Zhukovskii, arXiv:2608.06358v1, Conjecture 1.5"
    status: OPEN_ADMITTED_ACTIVE
    claim_commit: 83eeed96f3699fe75299c13148b94f9337e65b89
  incoming_metric:
    name: A_cyc(c)
    definition: "complete proved girth-coefficient curve at density c log n/n, with all restrictions"
    r16_sharp_baseline: UNMEASURED
    source_target: "A_cyc(1+epsilon) <= 1+epsilon for every fixed epsilon>0"
  next_methods: [2, 18, 24]
  shared_roots_modified: false
  scheduler_modified: false
  email_or_drive: false
```
