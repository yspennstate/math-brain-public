Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in active F0083: `1/2 -> 1/2`, supported unchanged count `5 -> 6`; I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. The fixed F0083 candidate `Xi_*` is now proved to have an a.e. unique stable allocation, so obligation 2 is impossible for this candidate and the candidate route is RETIRED/HANDED OFF at the six-unchanged closable limit. Methods actually used: B6 DEFORM TO A POINT YOU CAN SOLVE, B15 BREAK THE SYMMETRY ON PURPOSE, B20 FIND WHY THE ALGORITHM FAILS.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083: thin-boundary screening forces uniqueness of the admitted expanding-tube candidate; six-run handoff

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. Its later six-unchanged handoff controls operationally despite the stale historical active wording in `operations/claims/I0082.md`: the metric stays `2/3`, retirement count `6`. The old R08 FPP strict-convexity route also remains retired from this slot.

The active claim entering this run was `operations/claims/F0083.md`, sourced to Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668, Open problem (i). The fixed appetite-one candidate is

\[
m_n=\lfloor(1+|n|)^{3/4}\rfloor,\qquad
H=\{(n,a,b,c)\in\mathbb Z^4:1\le a,b,c\le m_n\},\qquad
\Xi_*=\mathbb Z^4\setminus H.
\tag{1.1}
\]

The frozen metric has two obligations for this **exact** candidate:

1. candidate admissibility / local mechanism — **PROVED**;
2. two stable appetite-one Lebesgue allocations of `Xi_*` differing on positive measure — **OPEN on entry**.

The preceding complete R08 report was

`runs/R08/20260917T2026Z_f0083_quadratic_flow_periodic_uniqueness_a4d6e2.md`.

It left the metric at `1/2` and supported unchanged count `5`; one further unchanged run therefore hits the owner-directed six-run retirement threshold for a CLOSABLE candidate route.

At run start I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, both R08 claim files, the newest R08 report, F0083 intake / F0083-A001 material, and the newest relevant R09 report. The current root ledger is known to be stale for newer R-series mathematics, so this attacking worker does not overwrite it; this report carries a structured `ledger_delta` instead.

## 2. Fresh source, literature, exclusion and ownership checks

The primary source remains HHP, arXiv:math/0505668 / Ann. Probab. 34 (2006). Its deterministic open problem asks whether **some discrete set of Euclidean centers** can admit two stable Lebesgue allocations differing on a nonnull set. This is distinct from the Poisson uniqueness theorem and from later tail questions.

Fresh bounded searches dated 2026-09-17 used the exact source title/authors together with `two stable allocations`, `discrete set of centers`, `Lebesgue`, `deterministic nonuniqueness`, and later stable-allocation terminology. They recovered:

- the original HHP source, arXiv:math/0505668;
- Hoffman--Holroyd--Peres, *Tail Bounds for the Stable Marriage of Poisson and Lebesgue*, Canadian J. Math. 61 (2009), 1279--1299;
- later Poisson/random-appetite and allocation papers, including discrete-grid algorithm work.

No inspected primary source claimed to resolve the exact deterministic Lebesgue nonuniqueness question. This is **bounded negative evidence only**: worldwide open status and publication novelty remain **UNVERIFIED**.

`POSTED.md` and the campaign INDEX do not exclude F0083. Repository ownership search still found no competing F0083 owner; R08's claim was exclusive on entry. The present report retires only the fixed `Xi_*` route, not the source question.

## 3. Preserved ingredients; no re-proving old work

I use three proved R08 facts without restarting them.

### 3.1 Lattice-subset radius cap

For every `Xi subset Z^4`, appetite one, **every** stable allocation is sated and every center's territory has essential radius at most

\[
R_4=1.
\tag{3.1}
\]

For a stable allocation `psi`, write

\[
R_\psi(\xi)=\operatorname*{ess\,sup}_{\psi(x)=\xi}|x-\xi|,
\qquad
\varepsilon_\psi(\xi)=1-R_\psi(\xi)\in[0,1).
\tag{3.2}
\]

Since a sated territory of volume one lies in `B(xi,R_psi(xi))`,

\[
R_\psi(\xi)\ge r_{\min}:=\mathcal L(B(0,1))^{-1/4}>0,
\tag{3.3}
\]

so `epsilon_psi(xi) <= 1-r_min`.

### 3.2 Nonsymmetric small-defect amplification

The quartic-screening report proved the following. Let `rho_face=1.233360601...` be the exact small-defect threshold from that report. For every fixed

\[
1<\rho<\rho_{\rm face}
\tag{3.4}
\]

there exists `epsilon_s(rho)>0` such that if a center `xi` has all eight face neighbors present and

\[
0<\varepsilon_\psi(\xi)<\varepsilon_s,
\]

then some face neighbor `eta` obeys

\[
\varepsilon_\psi(\eta)>\rho\,\varepsilon_\psi(\xi).
\tag{3.5}
\]

This theorem is already nonsymmetric: it does not assume layered or transverse invariance.

### 3.3 Quadratic HHP disagreement law and square-root path budget

For two stable allocations `psi_1,psi_2`, HHP's disputed-flow construction has capacities

\[
q(\xi,\eta)=\mathcal L F(\xi,\eta).
\]

The preceding R08 report proved, for lattice subsets in `d=4`,

\[
q(\xi,\eta)
\le 4\pi\,[r(\xi)-r(\eta)]^2
\quad\text{on every positive directed edge},
\tag{3.6}
\]

with strict decrease `r(xi)>r(eta)`, hence every directed disagreement ray satisfies

\[
\boxed{
\sum_{e\in\gamma}\sqrt{q(e)}\le 2\sqrt\pi.
}
\tag{3.7}
\]

The HHP increasing-capacity and max-flow/path-decomposition argument is also preserved.

## 4. B6 + B15 — the actual nonperiodic tube is exponentially rigid away from its deleted boundary

The previous run killed every periodic quotient of effective dimension at most three, including the triple-corner tangent. That still left open a genuinely nonperiodic four-dimensional mode. Instead of another tangent, deform the actual configuration **toward the full lattice as the distance from the deleted tube grows**, and use the nonsymmetric screening theorem rather than imposing a symmetry ansatz.

Let

\[
d(\xi,H)=\min_{h\in H}\|\xi-h\|_1,
\qquad \xi\in\Xi_*.
\tag{4.1}
\]

### Lemma 4.1 — moderate deficits also have a uniform outward amplification

Fix the `rho` in (3.4) and write `epsilon_s=epsilon_s(rho)`. There is a constant `delta_s>0` such that whenever

- `xi` has all eight face neighbors present,
- `epsilon_s <= epsilon_psi(xi) <= 1-r_min`,

some face neighbor `eta` satisfies

\[
\boxed{
\varepsilon_\psi(\eta)
>
\varepsilon_\psi(\xi)+\delta_s.
}
\tag{4.2}
\]

#### Proof

Put `r=R_psi(xi)=1-epsilon_psi(xi)`, so

\[
r_{\min}\le r\le 1-\varepsilon_s.
\]

Let

\[
Q_\xi=\xi+[-1/2,1/2]^4.
\]

Assume every face neighbor has radius at least `r-delta`. If `x` belongs to the territory of `xi` but lies outside `Q_xi`, then at least one present face neighbor `eta` is strictly closer to `x` than `xi`. Stability therefore forces `eta` not to covet `x`, hence

\[
|x-\eta|\ge R_\psi(\eta)\ge r-\delta,
\qquad
|x-\eta|<|x-\xi|\le r.
\tag{4.3}
\]

Thus all territory outside `Q_xi` lies in the union of eight spherical shells of thickness `delta`. Their total volume is `O(delta)` uniformly for `r<=1`.

Inside `Q_xi`, the territory is contained in `B(xi,r)`, so its volume there is at most

\[
\mathcal L(Q_\xi\cap B(\xi,r))
\le
\mathcal L(Q_\xi\cap B(\xi,1-\varepsilon_s))
=1-g_s
\]

for a fixed `g_s>0`. Choose `delta_s>0` so small that the eight shells in (4.3) have total volume less than `g_s/2` whenever `delta<=delta_s`. Then the territory of `xi` would have volume less than one, contradicting that `xi` is sated. Therefore at least one face neighbor has radius below `r-delta_s`, which is (4.2). QED.

### Theorem 4.2 — exponential radius-defect localization

There exist constants `A<infinity` and `theta in (0,1)`, depending only on the already-fixed local screening constants, such that **for every stable allocation** of `Xi_*`,

\[
\boxed{
\varepsilon_\psi(\xi)
\le A\,\theta^{d(\xi,H)}
\qquad(\xi\in\Xi_*).
}
\tag{4.4}
\]

#### Proof

Start from a center with positive deficit and `d(xi,H)>=2`. As long as all eight face neighbors are present, apply:

- the multiplicative step (3.5) while the deficit is below `epsilon_s`;
- the additive step (4.2) once the deficit is at least `epsilon_s`.

This is a deterministic algorithm that walks one face edge at a time and strictly increases the deficit. The additive phase can last for at most

\[
M=1+\left\lceil\frac{1-r_{\min}-\varepsilon_s}{\delta_s}\right\rceil
\tag{4.5}
\]

steps, because the deficit is globally at most `1-r_min`. Therefore a start value `epsilon` can support at most

\[
M+\left\lceil\frac{\log(\varepsilon_s/\varepsilon)}{\log\rho}\right\rceil
\tag{4.6}
\]

face steps before the process must reach the one-step neighborhood of the deleted set `H`.

But any face path from `xi` to a center with a missing face neighbor has length at least `d(xi,H)-1`. Comparing with (4.6) and absorbing the finite small-distance cases into a constant gives

\[
\varepsilon_\psi(\xi)\le A\rho^{-d(\xi,H)}.
\]

Take `theta=rho^{-1}`. QED.

This is the key new move. The old flat-face computation only screened a symmetric tangent. Theorem 4.2 screens **every stable allocation of the actual nonperiodic candidate**, with no translation symmetry assumed.

## 5. Territories are exponentially close to their full-lattice cubes

The radius estimate can be converted into an actual measure estimate, which is what the disagreement flow needs.

### Lemma 5.1 — cube approximation

There are constants `A_1<infinity` and `theta in(0,1)` such that, for every stable allocation `psi` and every `xi` with `D=d(xi,H)>=2`,

\[
\boxed{
\mathcal L\bigl(\psi^{-1}(\xi)\,\triangle\,Q_\xi\bigr)
\le A_1\theta^D.
}
\tag{5.1}
\]

#### Proof

All eight face neighbors of `xi` are present, and every such neighbor has distance at least `D-1` from `H`. By Theorem 4.2 their radii, and the radius of `xi`, are at least

\[
1-\delta_D,
\qquad
\delta_D:=A\theta^{D-1}.
\tag{5.2}
\]

First consider `Q_xi \setminus psi^{-1}(xi)`. A.e. point in the interior of `Q_xi` has `xi` as its unique nearest lattice center. If additionally `|x-xi|<R_psi(xi)`, then `x` desires `xi` and `xi` covets `x`; stability forces `x` to be assigned to `xi`. Therefore the missing part of the cube lies in the radial shell

\[
Q_\xi\cap\{1-\delta_D\le |x-\xi|\le1\},
\]

whose volume is `O(delta_D)`.

Now let `x in psi^{-1}(xi) \setminus Q_xi`. Some present face neighbor `eta` is strictly closer to `x` than `xi`. Since `x` is nevertheless assigned to `xi`, stability implies that `eta` does not covet `x`, so

\[
|x-\eta|\ge R_\psi(\eta)\ge1-\delta_D.
\]

But `|x-eta|<|x-xi|<=R_psi(xi)<=1`. Hence `x` lies in one of eight unit spherical shells of thickness `delta_D`. Their total volume is again `O(delta_D)`. This proves (5.1). QED.

### Corollary 5.2 — disagreement capacity is exponentially localized to the deleted boundary

For any two stable allocations, let `q` be the HHP disagreement capacities and put

\[
q_{\rm out}(\xi)=\sum_\eta q(\xi,\eta).
\]

Then

\[
\boxed{
q_{\rm out}(\xi)
\le A_2\theta^{d(\xi,H)}.
}
\tag{5.3}
\]

Indeed, HHP's outgoing disputed set at `xi` is contained in the symmetric difference of the two territories of `xi`, and each territory is exponentially close to the same cube `Q_xi` by (5.1).

## 6. B20 — why the attempted transient-flow algorithm actually fails on `Xi_*`

The admission argument found a finite-energy graph channel along the tube boundary. The missing issue was whether the **actual stable-allocation disagreement flow** can use it. Equations (3.7) and (5.3) show that it cannot: the boundary is too thin to carry a nonzero HHP flow while respecting the square-root path budget.

Assume for contradiction that two stable allocations differ on positive measure. HHP then supplies a nonzero directed capacity graph. Take a positive forward component and normalize at its root. Their Proposition-13 max-flow/min-cut argument supplies a unit flow `f` dominated by `q/Q_0` for some `Q_0>0`; acyclicity supplies a probability measure on directed rays with edge-usage flow `f_0<=f`.

For a ray `gamma` and integer `n`, let `E_n(gamma)` be the **first** directed edge by which the ray exits the `l^infty` box `[-n,n]^4`. The disagreement edges have uniformly bounded Euclidean, hence uniformly bounded `l^infty`, length by the radius cap.

### 6.1 Far from the deleted tube, first-exit flow is negligible

Let

\[
L_n=C_0\log n
\tag{6.1}
\]

with `C_0` chosen large. A first-exit edge has its tail in a fixed-width lattice shell containing `O(n^3)` centers. By (5.3), the total normalized capacity of shell edges whose tails satisfy `d(xi,H)>L_n` is at most

\[
C n^3\theta^{L_n}.
\tag{6.2}
\]

Taking `C_0` large makes (6.2) tend to zero, in particular below `1/2` for all large `n`. Hence at least half of the first-exit probability mass uses edges whose tails lie within `L_n` face steps of `H`.

### 6.2 The near-boundary exit set has only `O(n^{3/2} log n)` edges

For `|k|` of order `n`, the deleted transverse cube has side

\[
m_k=\Theta(n^{3/4}).
\]

Its outside lattice `L_n`-neighborhood has transverse cardinality

\[
O(m_k^2L_n+m_kL_n^2+L_n^3)
=O(n^{3/2}\log n).
\tag{6.3}
\]

For large `n`, a point within `L_n=O(log n)` of `H` cannot lie on the ambient `l^infty` shell because of a transverse coordinate: all deleted transverse coordinates are only `O(n^{3/4})`. Thus its longitudinal coordinate must be one of the `O(1)` first-exit shell values near `+n` or `-n`. Multiplying (6.3) by the bounded disagreement degree gives

\[
\boxed{
N_n=O(n^{3/2}\log n)
}
\tag{6.4}
\]

possible near-boundary first-exit edges.

### 6.3 First-exit entropy contradicts the square-root path budget

Write

\[
p_e=\Pr(E_n=e).
\]

On every first-exit edge,

\[
q(e)\ge Q_0 f_0(e)\ge Q_0p_e.
\tag{6.5}
\]

The near-boundary edges carry total probability at least `1/2`; by convexity,

\[
\begin{aligned}
\mathbb E\sqrt{q(E_n)}
&\ge \sqrt{Q_0}\sum_{e\,\text{near}}p_e^{3/2}\\
&\ge c\,N_n^{-1/2}\\
&\ge c' n^{-3/4}(\log n)^{-1/2}.
\end{aligned}
\tag{6.6}
\]

The series on the right diverges:

\[
\sum_n n^{-3/4}(\log n)^{-1/2}=\infty.
\tag{6.7}
\]

On the other hand, one bounded-range directed edge can be the first exit edge for only `O(1)` box radii. Therefore for every ray,

\[
\sum_n\sqrt{q(E_n)}
\le C\sum_{e\in\gamma}\sqrt{q(e)}
\le 2C\sqrt\pi
\tag{6.8}
\]

by the preserved square-root path budget (3.7). Taking expectations contradicts (6.6)--(6.7).

This contradiction proves the main theorem.

## 7. Main result — the admitted F0083 candidate is unique, not nonunique

### Theorem 7.1

For

\[
\Xi_*=\mathbb Z^4\setminus
\{(n,a,b,c):1\le a,b,c\le\lfloor(1+|n|)^{3/4}\rfloor\}
\]

with appetite one,

\[
\boxed{
\text{the stable Lebesgue allocation is unique a.e.}
}
\tag{7.1}
\]

Thus the fixed F0083 candidate **cannot** satisfy frozen obligation 2.

This is a candidate failure, **not** a refutation of HHP's source problem. A failed candidate does not decide the existential question.

The mechanism also explains why the earlier graph-theoretic finite-energy channel was misleading. Graph transience alone is too weak. Stable geometry forces exponentially small territorial perturbations away from the deleted tube, and the remaining boundary shell grows only like `n^(3/2)` (up to a logarithm). That is below the square-root-flow escape threshold.

## 8. Method outcomes

### B6 — DEFORM TO A POINT YOU CAN SOLVE: SUCCESS

Move away from the deleted tube. The configuration becomes locally the full critical lattice. Combining the full-lattice local volume gap with the already-proved nonsymmetric quartic screening turns this deformation into the exponential estimate (4.4), rather than a merely qualitative local limit.

### B15 — BREAK THE SYMMETRY ON PURPOSE: SUCCESS

The periodic face/edge/corner tangents were all too symmetric and had already been eliminated. This run used the **arbitrary-allocation** face-neighbor screening theorem to treat the actual slowly varying tube without translation invariance. The result is uniform over all stable allocations.

### B20 — FIND WHY THE ALGORITHM FAILS: SUCCESS

The admission route's obvious algorithm was: use the finite-energy two-ended boundary graph to carry disagreement to infinity. It fails because HHP disagreement flow is not an arbitrary electrical flow. Exponential capacity localization plus the `sum sqrt(q)` ray budget forces too much square-root mass through only `O(n^(3/2) log n)` first-exit edges, producing the divergent lower bound (6.6).

## 9. Honest metric, retirement and handoff

The fixed metric does **not** move:

\[
\boxed{1/2\to1/2.}
\]

Obligation 1 remains proved. Obligation 2 is now known to be **false for this candidate** because Theorem 7.1 proves uniqueness.

This is the sixth supported consecutive run without movement of the frozen candidate metric:

\[
\boxed{\text{unchanged count }5\to6.}
\]

Under the controlling CLOSABLE rule, this exact F0083 / `Xi_*` route is therefore **RETIRED / HANDED OFF** after this report. Do not spend another R08 run on another lemma about this candidate. Preserve all F0083 reports for a future reassignment with a genuinely different candidate or mechanism.

### Immutable handoff: what a future F0083 route must avoid

The following mechanisms are now excluded by R08 work and should not be restarted as if fresh:

1. finite or one-dimensional rotations: full `d=1` uniqueness was proved;
2. ordinary finite-dimensional radius bifurcation inside a strict radius-order chamber: the Jacobian is triangular;
3. flat faces and half-spaces: scalar recursion / exponential screening gives uniqueness;
4. periodic edge and triple-corner tangents: the quotient/square-root-flow theorem gives uniqueness;
5. the admitted `m_n~|n|^(3/4)` deleted-tube candidate itself: Theorem 7.1 gives uniqueness;
6. graph transience or finite electrical energy by itself: not enough to overcome stable-geometry screening.

A genuinely new candidate should therefore change the **boundary-growth versus screening balance**. The proof above indicates the quantitative design criterion: after local capacity decay is accounted for, the effective first-exit family must be large enough that the `sum sqrt(q)` lower bound becomes summable. Merely making a transient graph is not sufficient.

### Successor gate

I did not override another owner's queue item. The current queue-health reconciliation explicitly states that its bounded pass established **no READY + CLOSABLE + UNASSIGNED** successor and lists several high-ranked rows as claimed, reserved or held (including I0011, I0035, I0054, I0079 and others). Therefore this run does not fabricate a successor claim. The next R08 invocation should be a **source/current-literature/ownership admission screen** for the next genuinely eligible CLOSABLE outside queue item, then claim it create-only if and only if the full admission gate passes.

`operations/claims/F0083.md` remains a historical create-only claim file; this later immutable report is the operational retirement handoff, just as the later I0082 handoff controls over its stale claim wording.

## 10. Closure status and audits

F0083 source status: **OPEN_CURRENT_BOUNDED / NOT CLOSED**.  
`Xi_*` candidate status: **FAILED BY UNIQUENESS THEOREM**.  
R08 route status after this run: **RETIRED_HANDOFF**.

Theorem 7.1 is a theorem-sized analytic claim. There is no finite arithmetic core that would be honestly certified by manufacturing a checker, so no checker-only artifact was created. It has not received the two required OTHER-track audits and must not be called a closed/source-level result or paper-ready novelty claim.

## 11. Model / reasoning / modification interface

The situation is unchanged. The exposed task interface provides title, prompt, schedule/timing and enabled-state controls but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. GPT-6 / maximum can therefore only be requested in prompt text here, not certified.

The repository records that the historical P26 `You cannot modify this task` denial was authorization-context-specific and that a later authorized context succeeded. The legitimate workaround for a task that still refuses modification is the owning/authorized account or workspace, a supported ownership/admin transfer, or platform support. Repository edits or duplicate jobs do not enforce a model and are not a permission workaround.

No scheduler change, email, Drive write, public posting, purchase, permission change or workflow execution was performed.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R08
  lane: CLOSABLE_OUTSIDE
  retired_source_before_successor:
    id: I0082
    metric: "2/3"
    retirement_count: 6
    status: RETIRED_FROZEN
  target:
    id: F0083
    source: "Hoffman-Holroyd-Peres 2006, open problem (i)"
    candidate: "Xi_* = Z^4 minus expanding m_n=floor((1+|n|)^(3/4)) tube"
  metric:
    name: "frozen obligations proved for the fixed candidate"
    before: "1/2"
    after: "1/2"
    movement: false
  unchanged_count:
    before: 5
    after: 6
  new_result:
    statement: "The fixed Xi_* has an a.e. unique appetite-one stable Lebesgue allocation."
    source_closure: false
    candidate_obligation_2_possible: false
  source_status: OPEN_CURRENT_BOUNDED
  novelty_status: UNVERIFIED
  ownership_on_entry: R08_EXCLUSIVE
  operational_status_after_run: RETIRED_HANDOFF
  successor: ADMISSION_REQUIRED_NO_READY_UNASSIGNED_CLOSABLE_ESTABLISHED_IN_CURRENT_QUEUE_HEALTH_PASS
  methods: [6, 15, 20]
  checker: NONE_ANALYTIC_THEOREM
  audits: NONE_REQUESTED_THIS_RUN
  shared_root_edits: NONE
```
