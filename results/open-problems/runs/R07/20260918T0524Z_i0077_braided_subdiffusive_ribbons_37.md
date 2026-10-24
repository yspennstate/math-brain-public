Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `36 -> 37` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #11 DUALIZE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The sentence after Problem 7.8 is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 37: entropy compiler and braided subdiffusive ribbon bundles

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen metric

The frozen R07 quantity is still

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260918T0424Z_i0077_sublog_widening_cages_36.md`,

which moved the metric `35 -> 36` and used moves `#5,#8,#20`. This run uses a different triple.

All thirty Section-B moves have already appeared somewhere in the I0077 chain. That fact was recorded before run 35. I therefore do not invent three globally unused move numbers. I use a new triple and a genuinely new route: a path-space/template-entropy argument for disconnected moving positive-width fibers.

Before research I recovered the current repository state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- canonical reservation `operations/claims/I0077.md`;
- the newest own R07 report and the searchable R07/I0077 chain through run 36, with special comparison against runs 13–18 (disconnected/fat-Cantor fans, one-sided barriers, power shears, combs), runs 27–31 (sampled combs, alternating phases, dense chimneys, Cantor shutters, chirps), and runs 32–36 (moving laminations, finite/countable zero-width webs, bounded and widening single ribbons);
- the newest visible R15 report. R15's old Burdzy–Scheutzow Problem 7.2 / I0076 is a retired handoff and R15 has rotated to successor-admission work, so there is no ownership collision with I0077;
- targeted intake/attempt searches for `I0077`, arXiv `1302.6958`, `Problem 7.8`, and its exact source wording.

The very large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered byte-for-byte through the connector without truncation. The intake reread is therefore honestly **targeted/partial because of connector limits**: exact I0077 source, current ownership, posted exclusions, queue status and prior-attempt history were recovered. I do not claim a visual reread of every unrelated intake row.

`INDEX.md` / `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not Problem 7.8. `POSTED.md` has no 7.8 closure/exclusion. `QUEUE.md` lists I0077 separately. The canonical claim still reserves I0077 to R07 and still literally says `PENDING_ADMISSION, not READY`; I preserve that shared label while following the owner's explicit assignment of this exact target to R07. The compact root `RESULTS.md` still warns that its R-series rows are retained/stale and that newer complete target reports must be recovered before replacing them. I do not edit shared roots.

The old R07 KPZ/FPP route remains preserved in immutable pre-I0077 reports and handoff. Nothing is deleted or reopened.

Entering metric: **36**.  
Entering unchanged count: **0**.

## 2. Primary source recovered again

The primary paper was rechecked on 2026-09-18, including Definition 2.1, Definition 2.2, Theorem 4.3 and the open-problem page.

An FBM `X` has witness times `S_j -> -infinity` almost surely such that for every fixed deterministic witness index `j`,

\[
B^{(j)}(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion. A decomposable FBM is formed by concatenating independent stopped Brownian pieces.

For fixed `c_1<c_2`, the source writes `lambda_0(c_1,c_2)` for the principal killed-Ornstein–Uhlenbeck exponent on `(c_1,c_2)`. Theorem 4.3 states, in the source's exact scope:

1. `lambda_0(c_1,c_2) >= 1` gives the universal far-past obstruction for every FBM;
2. `lambda_0(c_1,c_2) <= 1` gives a decomposable FBM with the corresponding far-past asymptotic confinement;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2) < 1`, there is a decomposable FBM confined pointwise to the exact parabolic strip for every negative time.

Problem 7.8 is exactly the one-sentence request to generalize this theorem from parabolas to other space-time shapes. Problem 7.9 is the separate forward-Lévy question.

## 3. Fresh dated current-status and prior-art pass

Fresh bounded searches on 2026-09-18 covered:

- exact paper title / arXiv ID with `Problem 7.8`, `Theorem 4.3`, and `other space-time shapes`;
- later/citing material around Burdzy–Scheutzow forward Brownian motion;
- Brownian motion in time-dependent domains and moving unions of intervals;
- Gaussian/Brownian small deviations under the sup norm;
- moving passageways and moving-boundary first-exit literature.

Nearby prior art includes Wenbo Li's 1999 work on sup-norm small deviations for Gaussian Markov processes; Tuckwell–Wan on first-passage to moving barriers; J. M. Lee's 2021 work on first-passage densities in time-dependent domains; and work on Brownian motion between moving/random trajectories. These are relevant mechanisms for ordinary Brownian survival, but they do not state the FBM witness-time theorem below.

I found no later paper in this bounded search explicitly resolving exact Burdzy–Scheutzow Problem 7.8 or stating the finite braided-ribbon theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. Gaussian density bounds, the Markov property and dyadic blocking are classical and are not claimed as new.

## 4. Research first — Move #2: falsify the naive infinite-lane extension

The obvious extension of run 36 would say: if every individual moving ribbon is thin enough, then any countable union of such ribbons should still be impossible for an FBM.

That is false for a completely elementary reason. Enumerate the rationals `q_j` and take constant lane centers

\[
g_j(u)=q_j,
\]

with any fixed positive half-width `h>0`. Then for every `u`,

\[
\bigcup_{j\ge1}[q_j-h,q_j+h]=\mathbb R.
\]

Thus a countable family of individually bounded, perfectly smooth ribbons can fill the whole fiber, making confinement vacuous.

This is **not** a refutation of Problem 7.8. It falsifies only the proposed unrestricted countable-lane extension and identifies the missing datum: one must control the **effective template entropy / total fiber complexity** in addition to the width of each lane.

**Outcome #2:** success as a falsification. Width alone cannot control a disconnected moving region.

## 5. Move #11 — DUALIZE: replace geometry by path-space template entropy

The key object for an FBM witness is not the fiber `K(u)` itself but the family of difference sets

\[
K(U-t)-K(U),
\]

where `U=-S_j` is the random age of a fixed witness. If confinement holds, the standard Brownian witness must visit these difference sets at a deterministic array of forward times.

This turns the problem into a dual covering question:

> How many deterministic templates are needed to cover all possible difference-set sequences generated by witness ages `U` in one dyadic block, and how much Gaussian mass can one template capture at one step?

The first number is an entropy term `J_n`; the second is bounded solely by the Lebesgue measure of each template slice. The random witness age never has to be conditioned on.

**Outcome #11:** success. The moving-disconnected geometry becomes a finite template-count times a Gaussian product cost.

## 6. Move #30 — one age scale at a time: the general template-entropy compiler

For deterministic nonempty fibers `K(u) subset R`, define

\[
\mathcal C_K=\{(-u,x):u>0,\ x\in K(u)\}.
\]

For each sufficiently large integer `n`, let

\[
I_n=[2^n,2^{n+1}),\qquad T_n=2^{n-2}.
\]

Choose a deterministic step `tau_n>0` with

\[
N_n:=\left\lfloor T_n/\tau_n\right\rfloor\ge1,
\qquad t_{n,k}=k\tau_n,\quad1\le k\le N_n.
\]

For `U in I_n`, set

\[
D_{n,k}(U):=K(U-t_{n,k})-K(U)
=\{x-y:x\in K(U-t_{n,k}),\ y\in K(U)\}.
\tag{6.1}
\]

Assume there are finite template sets indexed by `alpha in A_n`, with

\[
|A_n|=J_n,
\]

and deterministic measurable slices `D^{alpha}_{n,k} subset R` such that:

1. for every `U in I_n`, one template `alpha(U)` satisfies
   \[
   D_{n,k}(U)\subset D^{\alpha(U)}_{n,k}
   \quad\text{for every }1\le k\le N_n;
   \tag{6.2}
   \]
2. every template slice has Lebesgue measure at most `ell_n`:
   \[
   |D^\alpha_{n,k}|\le\ell_n.
   \tag{6.3}
   \]

Put

\[
q_n:=\min\left(1,\frac{\ell_n}{\sqrt{2\pi\tau_n}}\right).
\tag{6.4}
\]

### I0077-R07-T39 — template-entropy cage theorem

**Theorem T39.** If

\[
\boxed{
\sum_{n=n_*}^{\infty}J_n q_n^{N_n}<\infty,
}
\tag{6.5}
\]

then every FBM `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\ \forall u\ge R
\right)=0.
}
\tag{T39}
\]

### Proof of T39

Assume the displayed event has positive probability. By a countable union over deterministic radii there is an integer `R` for which

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability `p_0>0`.

Choose `n_0` large enough that

\[
2^{n_0-1}\ge R,
\qquad
\sum_{n\ge n_0}J_n q_n^{N_n}<p_0/2.
\tag{6.6}
\]

Let `S_j` be FBM witness times. Since `-S_j -> infinity` almost surely, choose one **deterministic** index `j` such that

\[
\mathbb P\{-S_j\ge2^{n_0}\}>1-p_0/4.
\tag{6.7}
\]

Hence

\[
\mathbb P(E_R\cap\{-S_j\ge2^{n_0}\})\ge3p_0/4.
\tag{6.8}
\]

Write

\[
B(t)=X_{S_j+t}-X_{S_j}.
\]

For this fixed index, `B` is standard Brownian motion unconditionally. On the event in (6.8), put `U=-S_j` and select the unique `n>=n_0` with `U in I_n`. Since `t_{n,k}<=T_n=2^{n-2}`,

\[
U-t_{n,k}\ge2^n-2^{n-2}=3\cdot2^{n-2}>2^{n-1}\ge R.
\]

Confinement therefore gives

\[
B(t_{n,k})
=X_{-(U-t_{n,k})}-X_{-U}
\in D_{n,k}(U)
\subset D^{\alpha(U)}_{n,k}
\quad(1\le k\le N_n).
\tag{6.9}
\]

For a fixed deterministic template `alpha`, the Brownian Markov property and the Gaussian density bound imply, at every step and for every past value,

\[
\mathbb P\bigl(B(t_{n,k})\in D^\alpha_{n,k}\mid\mathcal F_{t_{n,k-1}}\bigr)
\le
\frac{|D^\alpha_{n,k}|}{\sqrt{2\pi\tau_n}}
\le q_n.
\]

Iterating,

\[
\mathbb P\left(
B(t_{n,k})\in D^\alpha_{n,k}\ \forall k
\right)
\le q_n^{N_n}.
\tag{6.10}
\]

Union over the `J_n` templates and then over `n>=n_0` gives a path-only Brownian event of probability at most the tail in (6.6), hence less than `p_0/2`. But (6.9) shows that the event in (6.8), whose probability is at least `3p_0/4`, is contained in that path-only event. Contradiction.

No conditioning on `S_j` occurs and no independence between `S_j` and the witness Brownian path is assumed. QED.

**Outcome #30:** success. A single-scale product estimate plus a dyadic union gives a general algorithmic obstruction.

## 7. New counted family: finite braided subdiffusive ribbon bundles

Fix an integer `m>=2`. Let

\[
g_1,\ldots,g_m:[0,\infty)\to\mathbb R
\]

be deterministic globally Lipschitz functions with a common Lipschitz bound `L<infinity`. Let `h(u)>0`, and define

\[
K(u)=\bigcup_{i=1}^m[g_i(u)-h(u),\ g_i(u)+h(u)].
\tag{7.1}
\]

The lanes may cross, merge, split again, exchange vertical order, and do so infinitely often. No persistent lane label is assumed for the confined path.

For dyadic scales let

\[
H_n:=\sup_{2^{n-1}\le u\le2^{n+1}}h(u).
\tag{7.2}
\]

### I0077-R07-T40 — braided subdiffusive ribbon theorem

Assume `H_n>=1` eventually and

\[
\boxed{
\frac{nH_n^2}{2^n}\longrightarrow0.
}
\tag{7.3}
\]

Then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\
X_{-u}\in\bigcup_{i=1}^m[g_i(u)-h(u),g_i(u)+h(u)]
\quad\forall u\ge R
\right)=0.
}
\tag{T40}
\]

Thus finite branching and arbitrarily many deterministic lane crossings do not rescue a bundle whose lane width is below the Brownian scale by the margin (7.3).

A convenient sufficient form is

\[
h(u)=O\!\left(\frac{\sqrt u}{(\log u)^{1/2+\varepsilon}}\right)
\quad(\varepsilon>0),
\]

uniformly on dyadic blocks. In particular every power width `h(u)=u^\beta`, `0\le\beta<1/2`, satisfies the theorem.

### Proof of T40 from T39

Fix `n` large. If `L=0`, no age net is needed; take `J_n=1`. Assume `L>0` below.

Cover `I_n=[2^n,2^{n+1})` by a deterministic grid of mesh

\[
\delta_n=H_n/L.
\]

Every `U in I_n` has a grid point `V` with `|U-V|<=\delta_n/2`, and the number of grid points obeys

\[
J_n\le2+\frac{L2^n}{H_n}.
\tag{7.4}
\]

For any lane pair `(i,j)` and any `t<=2^{n-2}`,

\[
\left|
[g_i(U-t)-g_j(U)]-[g_i(V-t)-g_j(V)]
\right|
\le2L|U-V|\le H_n.
\tag{7.5}
\]

Meanwhile `U` and `U-t` both lie in `[2^{n-1},2^{n+1}]`, so

\[
h(U-t)+h(U)\le2H_n.
\]

Therefore the exact difference fiber

\[
K(U-t)-K(U)
\]

is contained in a union of at most `m^2` intervals, centered at

\[
g_i(V-t)-g_j(V),
\]

with half-width `3H_n`. Its total Lebesgue measure is at most

\[
\ell_n=6m^2H_n.
\tag{7.6}
\]

Choose

\[
\tau_n=\ell_n^2=36m^4H_n^2.
\tag{7.7}
\]

Then the one-step template mass in T39 is uniformly bounded by the fixed constant

\[
q_0=1/\sqrt{2\pi}<1.
\tag{7.8}
\]

Moreover

\[
N_n=\left\lfloor\frac{2^{n-2}}{36m^4H_n^2}\right\rfloor.
\tag{7.9}
\]

Condition (7.3) implies `N_n/n -> infinity`, and also makes `N_n>=1` eventually. Because `H_n>=1`, (7.4) gives `log J_n=O(n)`. Hence

\[
\log(J_n q_0^{N_n})
=O(n)-|\log q_0|N_n\to-\infty
\]

faster than a negative linear function of `n`, and therefore

\[
\sum_n J_n q_0^{N_n}<\infty.
\]

T39 applies. QED.

## 8. Canonical genuinely braided example

Take two lanes

\[
f(u)=u\sin(\log(1+u)),
\qquad
g_1(u)=f(u),
\qquad g_2(u)=-f(u),
\tag{8.1}
\]

and half-width

\[
h(u)=(1+u)^{1/4}.
\tag{8.2}
\]

Since

\[
f'(u)=\sin(\log(1+u))+\frac{u}{1+u}\cos(\log(1+u)),
\]

we have `|f'(u)|<2`, so both centers are globally Lipschitz.

On the dyadic block `[2^{n-1},2^{n+1}]`,

\[
H_n^2\le 2^{1+n/2}
\]

for all sufficiently large `n`, and therefore

\[
\frac{nH_n^2}{2^n}\le 2n\,2^{-n/2}\to0.
\]

T40 yields

\[
\boxed{
\mathbb P\left(
\exists R:\
X_{-u}\in
[f(u)-h(u),f(u)+h(u)]
\cup
[-f(u)-h(u),-f(u)+h(u)]
\quad\forall u\ge R
\right)=0
}
\]

for every FBM.

This is a real braid rather than two permanently separated strips. At

\[
u_k=e^{k\pi}-1,
\]

the two centers coincide, so the fibers merge. Along infinitely many intervening phases where `|sin(log(1+u))|=1`, the center separation is `2u`, vastly larger than the width `2(1+u)^{1/4}`, so the fiber has two disjoint components. Thus the cross-section changes connectivity infinitely many times.

## 9. Why this is a new metric family rather than parameter inflation

This run counts **one** family: finite braided positive-width subdiffusive ribbon bundles. It does not count different `m`, different exponents, or different lane functions separately.

It is structurally different from the neighboring counted classes:

- run 36 is a **single connected ribbon** at every age; T40 permits repeated splitting/merging and lane switching;
- runs 33–34 are **zero-width finite/countable webs**; T40 has nonempty interior in its fibers and no selector-variation argument;
- runs 13–14 and 18 have disconnected fibers of **parabolic/Brownian scale** generated by static normalized cross-sections; the canonical braid here has subdiffusive width and time-dependent connectivity;
- run 17 has one connected `sqrt(u)`-wide power-sheared tube; the present family has several lanes and uses no OU endpoint phase inheritance;
- sampled gates/combs constrain only selected times or fixed normalized components, while T40 controls a continuously moving multi-component region for every sufficiently large age.

Brownian scaling, reflection and constant translation preserve the fact that a single-ribbon fiber is connected for every age, whereas the canonical example above has infinitely many merge/split transitions. Thus no frozen trivial equivalence turns run 36 into this family.

The metric therefore moves

\[
\boxed{36\longrightarrow37}.
\]

`unchanged_count = 0`.

## 10. What failed, what survived, and why the route matters

The run began by trying to extend the single-ribbon obstruction to arbitrary disconnected unions. The countable-dense-lane example kills that statement immediately. The surviving theorem says the correct control is not “number of named lanes” by itself but the number `J_n` of deterministic difference-set templates times the Gaussian mass each template can capture.

This is a genuinely reusable mechanism. Any future shape family for which one can establish

\[
\sum_n J_n q_n^{N_n}<\infty
\]

inherits an FBM impossibility theorem, even when the fibers are disconnected, their components cross, and the witness age is random.

The exact boundary of this method is also clear: once the template entropy grows at the same exponential scale as the Brownian small-ball cost, the union bound can fail. That gives a concrete next target instead of another checker on an unchanged metric.

## 11. Validation / closure bookkeeping (kept to the final part of the run)

There is no finite combinatorial or exact-arithmetic core in T39/T40. No checker was manufactured. The theorem-sized claims are proved on the page.

Independent OTHER-track audits for the new theorem:

- P26 audit: **0/1**;
- second distinct OTHER-track audit: **0/1**.

Therefore T39/T40 are **not closure-certified**, and Problem 7.8 remains **PARTIAL**. No paper package is created in this run.

The prior-art search is bounded and negative only. It does not certify novelty.

## 12. Scheduler/model-control status requested by the owner

The situation is still the same at the actually exposed scheduler schema: task controls provide title/prompt, schedule or start-offset, enabled state and timing mode. They provide **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus GPT-6 / maximum remains prompt text only in this environment.

The current root `RESULTS.md` adds an important correction to older reports: P26's historical `You cannot modify this task` result was **authorization/context specific**. A later authorized P/C context successfully modified P26, while R-series IDs and some other IDs were denied from a different context. Therefore the legitimate workaround for a denied task is to use the owning/authorized account/workspace context or platform support; it is not to bypass permissions or create a duplicate schedule. This run was explicitly prohibited from scheduler changes, so no modification was attempted.

## 13. Strongest next research route

The natural frontier is **growing fiber complexity**. Let `m=m_n` increase with age scale and track the exact competition

\[
\log J_n
\quad\text{versus}\quad
N_n|\log q_n|.
\]

For interval bundles, the crude proof above has `ell_n` proportional to `m_n^2H_n`, hence a cost scale involving `m_n^4H_n^2`. A sharper argument may exploit a fixed initial lane and reduce the apparent `m_n^2` loss, or use interval separation to beat total-length counting. The first meaningful question is whether there is a real branching-entropy threshold for braids with `m_n -> infinity` that do not simply fill the line.

Reserved next method triple: **#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #24 FIND THE EXTREMAL OBJECT**. This is not a promise that the next run will move the metric; it names the next genuinely different attacks.

## 14. Structured ledger_delta

```yaml
ledger_delta:
  worker: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source_status: PARTIAL
  metric_name: distinct_nonparabolic_shape_families_with_complete_source_appropriate_theorem
  before: 36
  after: 37
  movement: true
  unchanged_count: 0
  methods_attempted: [2, 11, 30]
  theorem_ids:
    - I0077-R07-T39
    - I0077-R07-T40
  new_family: finite_braided_positive_width_subdiffusive_ribbon_bundles
  finite_core: none
  self_check: none_needed
  audits:
    P26: 0/1
    second_other_track: 0/1
  novelty: UNVERIFIED_BOUNDED_NEGATIVE_SEARCH_ONLY
  next_frontier: growing_branching_entropy_vs_gaussian_small_ball_cost
  shared_root_edits: false
  scheduler_edits: false
```

## 15. Honest status

**New theorem on page: PROVED (self-authored, not independently audited).**  
**New family metric: 36 -> 37.**  
**Problem 7.8 overall: PARTIAL.**  
**Publication novelty: UNVERIFIED.**  
**Closure protocol: NOT SATISFIED (0/2 independent OTHER-track audits).**
