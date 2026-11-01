Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `48 -> 49` genuinely distinct nonparabolic shape families; Section-B moves actually used: #1 CHANGE THE CATEGORY, #2 ATTACK THE NEGATION FIRST, #3 PROVE SOMETHING STRONGER.**

# R07 CLOSABLE OUTSIDE — countable finite-variation fractal gates for Burdzy–Scheutzow Problem 7.8

Status: **PARTIAL** on the source problem. The theorem-sized claims T63/T64 below are proved on this page, but they have `0/2` required independent OTHER-track audits. Publication novelty is **UNVERIFIED**.

## 1. Continuity, admission, ownership, and source recovery

This run continues the existing R07/I0077 line rather than restarting it.

Before research I read/rechecked:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md` and `RESULTS.md`;
- `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/I0077.md`;
- the newest own report `runs/R07/20260918T163148Z_i0077_critical_gauge_affine_pinholes_48_cg48.md`;
- the current neighboring R15 report `runs/R15/20260918_1553Z_successor_screen_f0111_paircycle_g61q.md`; R15's distinct Burdzy–Scheutzow Problem 7.2 route remains retired/handoff and does not claim Problem 7.8;
- targeted repository search for I0077 and prior R07 families, including the critical-Hölder webs, occupation curtains, strict-dimension fractal pinning, sparse block gates, and run-48 critical-gauge affine pinholes;
- the intake/claim trail for I0077. The very large JSONL intake remains impractical to render literally row-by-row through the connector, so this is a targeted intake reread rather than a claim to have displayed all ~780 rows. The exact I0077 row/claim, duplicate-attempt history, and ownership were recovered.

The canonical claim still literally says `PENDING_ADMISSION, not READY` and provisionally reserves I0077 to R07. `INDEX.md` settles Burdzy–Scheutzow Problem 7.5, not Problem 7.8. `POSTED.md` does not exclude 7.8. The old R07 KPZ/FPP route remains preserved in its immutable handoff and was not deleted or reopened.

### Primary source, full relevant definitions

I rechecked the primary Burdzy–Scheutzow paper, *Forward Brownian Motion*, arXiv:1302.6958.

Definition 2.1: an FBM `X` has random times `S_j -> -infinity` almost surely such that for every **fixed deterministic index** `j`,

\[
B^{(j)}_s:=X_{S_j+s}-X_{S_j},\qquad s\ge 0,
\]

is standard Brownian motion.

Section 4 studies parabolic regions

\[
\{(t,x):t<0,\ c_1\sqrt{|t|}<x<c_2\sqrt{|t|}\}.
\]

Remark 4.1 defines

\[
\mathcal A=\frac12\left(\frac{d^2}{dx^2}-x\frac d{dx}\right),
\qquad m(dx)=2e^{-x^2/2}\,dx,
\]

and, on `[c_1,c_2]`, the Dirichlet Sturm--Liouville problem `A psi=lambda psi`; `-lambda_0(c_1,c_2)` is its largest eigenvalue. The source records continuity and strict domain monotonicity of `lambda_0`, with critical level `1`.

Theorem 4.3 has all three clauses:

1. if `lambda_0(c_1,c_2)>=1`, every FBM escapes at least one parabolic boundary asymptotically, in the source's limsup/liminf sense;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM satisfying the reverse asymptotic inequalities;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM pointwise confined between the two parabolas for all negative times.

Problem 7.8 is exactly:

> Can one generalize Theorem 4.3 from parabolas to other space-time shapes?

The next forward-Lévy sentence is Problem 7.9 and is not part of I0077.

The entering frozen metric is `48`, from the immediately preceding immutable run. The frozen equivalence convention does not count Brownian rescalings, reflection/translation, or a mere parameter change inside an already-counted structural family as a new point.

## 2. Fresh literature/current-status pass

Dated 2026-09-18, I searched the exact Problem-7.8 wording and combinations of `Forward Brownian Motion`, `space-time shapes`, later/citing work, and Brownian restriction regularity. The bounded search again recovered the original paper but no accessible later primary source explicitly claiming to settle exact Problem 7.8. This is **bounded negative evidence only**, not a worldwide-openness or novelty certificate.

The useful adjacent prior art is instead a different Brownian-geometry literature:

- Richárd Balka and Yuval Peres, *Restrictions of Brownian motion*, arXiv:1406.2789 (2014), Theorem 1.2: for `1<=beta<=2`, almost surely there is **no set** `A subset [0,1]` with `dim_H A>beta/2` such that Brownian motion restricted to `A` has finite `beta`-variation. Their proof explicitly handles a random/path-dependent candidate set, so the almost-sure statement is pathwise over all sets `A`.
- Their Theorem 1.1 similarly forbids an `alpha`-Hölder Brownian restriction on any set of dimension `>1/2` when `alpha>1/2`.
- Tonći Antunović, Krzysztof Burdzy, Yuval Peres and Julia Ruscher, *Isolated zeros for Brownian motion with variable drift*, arXiv:1009.3603 / EJP 2011, is nearby fixed-drift prior art; in particular it identifies the `1/2` scale for Hölder/BV drifts. It does not state the FBM theorem below.

The Balka--Peres universal restriction quantifier is the key input that removes the random-witness-phase obstruction left open by run 48.

## 3. Definition: beta-variation on a subset

For a function `f:A->R`, with `A subset R`, define

\[
\operatorname{Var}^{\beta}_A(f)
:=\sup\left\{
\sum_{r=1}^m |f(t_r)-f(t_{r-1})|^{\beta}:
 t_0<\cdots<t_m,\ t_r\in A
\right\}.
\]

A function has finite `beta`-variation on `A` if this quantity is finite. Restricting the domain can only decrease the variation. Translation of the range does not change it; reflection/translation of the time variable also preserves finiteness.

Balka--Peres Theorem 1.2 is stated on `[0,1]`, but deterministic Brownian scaling gives the following equivalent version on every fixed `T>0`:

\[
\boxed{
\mathbb P\left(
\exists A\subset[0,T]:\ \dim_H A>\beta/2,\ 
\operatorname{Var}^{\beta}_A(B)<\infty
\right)=0.
}
\tag{3.1}
\]

Indeed `T^{-1/2}B_{Tt}` is standard Brownian motion, Hausdorff dimension is invariant under nonzero linear time scaling, and finite `beta`-variation is preserved by multiplying the range by a nonzero constant.

The simultaneous/pathwise quantifier in (3.1) is what matters: the set `A` is allowed to depend on the Brownian path and therefore may depend on the FBM witness below.

## 4. I0077-R07-T63 — countable finite-variation fractal-gate obstruction

**Theorem T63.** Fix `1<=beta<=2` and `T>0`. Let `Z subset (0,infinity)` be deterministic and closed. Assume that for some `U_0<infinity`,

\[
\boxed{
\dim_H\bigl(Z\cap[U-T,U]\bigr)>\frac\beta2
\qquad\text{for every }U\ge U_0.
}
\tag{4.1}
\]

Let `q_1,q_2,...:(0,infinity)->R` be deterministic functions such that every `q_m` has finite `beta`-variation on every compact interval.

Let `K(u) subset R` be deterministic fibers satisfying only

\[
\boxed{
K(u)\subset \{q_m(u):m\ge1\}
\qquad (u\in Z),
}
\tag{4.2}
\]

with **no restriction whatsoever** imposed by the theorem on `K(u)` for `u notin Z`.

Then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)\quad\forall u\ge R
\right)=0.
}
\tag{T63}
\]

### Proof

Assume the event in T63 has positive probability. By a countable union over integer tail radii, choose a deterministic integer

\[
R\ge U_0
\]

such that

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability `p>0`.

Let `(S_j)` be an FBM witness sequence. Since `S_j -> -infinity` almost surely, choose one **deterministic index** `j` so far left that

\[
\mathbb P(S_j\le -R-T)>1-p/2.
\tag{4.3}
\]

Then

\[
G:=E_R\cap\{S_j\le-R-T\}
\]

has probability at least `p/2>0`.

For this fixed index set

\[
B_s:=X_{S_j+s}-X_{S_j},\qquad 0\le s\le T.
\tag{4.4}
\]

By the FBM definition, `B` is **unconditionally** standard Brownian motion. Hence (3.1) holds for this path with probability one.

Fix an outcome in `G` lying in that probability-one Balka--Peres event, and write

\[
U=-S_j\ge R+T.
\]

Reflect the gate set into the witness window:

\[
F:=\{s\in[0,T]:U-s\in Z\}.
\tag{4.5}
\]

The map `s -> U-s` is an isometry from `F` onto `Z cap [U-T,U]`, so by (4.1),

\[
\dim_H F>\frac\beta2.
\tag{4.6}
\]

For each `m>=1`, define the branch-selection set

\[
F_m:=\{s\in F:X_{S_j+s}=q_m(U-s)\}.
\tag{4.7}
\]

Because the outcome lies in `E_R`, every `s in F` corresponds to the age `u=U-s>=R`, and because `u in Z`, (4.2) implies that `X_{S_j+s}` equals `q_m(U-s)` for at least one `m`. Therefore

\[
F=\bigcup_{m=1}^{\infty}F_m.
\tag{4.8}
\]

Hausdorff dimension is countably stable:

\[
\dim_HF=\sup_m\dim_HF_m.
\tag{4.9}
\]

Since the left side is strictly larger than `beta/2`, there exists a deterministic branch index `m=m(omega)` for which

\[
\dim_HF_m>\frac\beta2.
\tag{4.10}
\]

On this set,

\[
B_s=q_m(U-s)-X_{S_j},\qquad s\in F_m.
\tag{4.11}
\]

The map `s -> q_m(U-s)` has finite `beta`-variation on `[0,T]`, because `q_m` has finite `beta`-variation on `[U-T,U]`. Its restriction to `F_m` therefore has finite `beta`-variation. Subtracting the constant `X_{S_j}` changes nothing, so

\[
\operatorname{Var}^{\beta}_{F_m}(B)<\infty.
\tag{4.12}
\]

Equations (4.10)--(4.12) contradict the pathwise Brownian restriction statement (3.1). Therefore `p=0`, proving T63. `QED`

### Dependence audit

The proof never conditions on `S_j` and never assumes that `S_j` is independent of its future. The witness **index** `j` is fixed deterministically before invoking the probability-one Brownian restriction event. Both the reflected set `F` and the selected branch set `F_m` may depend on the entire outcome; Balka--Peres is strong enough because it rules out **all subsets** of excessive Hausdorff dimension on a single probability-one Brownian path.

This is exactly the random-phase issue that the pointwise Cameron--Martin argument in run 48 could not safely handle for nonlinear tracks.

## 5. Section-B move #1 — CHANGE THE CATEGORY

The previous run treated moving pinholes as a level-set problem. For a nonlinear track `q(U-s)`, that language produces a continuum of witness-phase-dependent drifts and a uniform Cameron--Martin problem.

The new translation is different:

> confinement on the reflected fractal gate set forces the Brownian witness itself, on some large-dimensional branch-selection subset, to equal a finite-variation deterministic trace plus a constant.

That is a **restriction-regularity** problem rather than a moving-boundary or level-set problem. Balka--Peres already has the universal quantifier over subsets needed for the random FBM phase.

**Outcome: success.** It removes the phase-uniformity obstruction and yields T63.

## 6. Section-B move #2 — ATTACK THE NEGATION FIRST

I tested two overextensions before stating T63.

### 6.1 Equality in the dimension threshold cannot be obtained from this mechanism

Balka--Peres prove their threshold is sharp. In particular Brownian motion does admit finite-`beta`-variation restrictions on sets of the critical dimension `beta/2` (their sharpness construction; for related clauses the Brownian zero set witnesses the `1/2` endpoint).

Therefore replacing the strict condition

\[
\dim_HF>\beta/2
\]

by `>= beta/2` is not justified by restriction dimension alone. This is consistent with run 48 needing an **exact Hausdorff gauge** to say something at the critical point-target dimension `1/2`.

### 6.2 Arbitrarily uncountable track families make the statement false

Countability in (4.2) is structural, not bookkeeping. If one permits the family of all constant tracks `q_a(u)=a`, `a in R`, then at every gate age the union of track values is all of `R`, so (4.2) imposes no confinement at all. Every path satisfies that gate condition.

The proof pinpoints the same boundary: (4.9) uses **countable** stability of Hausdorff dimension. An uncountable union can gain dimension even when every individual branch-selection set is tiny.

**Outcome: success as a boundary test.** The failed overextensions identify both the strict dimension threshold and countability as genuine hypotheses of this route. They do **not** refute the source's open-ended Problem 7.8.

## 7. Section-B move #3 — PROVE SOMETHING STRONGER

Instead of proving only the bounded-variation (`beta=1`) singular-staircase example that first suggested the route, T63 is stated for:

- every `1<=beta<=2`;
- an arbitrary countable family of moving tracks;
- arbitrary branch switching on the fractal gate set;
- completely unrestricted fibers away from the gate set.

The proof does not require the tracks to be smooth, Hölder, separated, locally finite, or to have conserved labels. It needs only local finite `beta`-variation and countability.

**Outcome: success.** The induction/pigeonhole object is Hausdorff dimension under a countable union, which closes the stronger statement directly.

## 8. Canonical metric family: a singular-staircase countable gate comb

The concrete shape below is designed so that the finite-variation clause, the countable branch decomposition, and the fractal-time restriction are all genuinely used.

### 8.1 Temporal fractal gates

Let `C_3 subset [0,1]` be the middle-thirds Cantor set and periodize it:

\[
E=(C_3+\mathbb Z)\cap(0,\infty).
\tag{8.1}
\]

It has Lebesgue measure zero. Its Hausdorff dimension is

\[
d=\frac{\log 2}{\log 3}>\frac12.
\tag{8.2}
\]

For every sufficiently large real `U`, in fact for every `U>1`,

\[
\boxed{
\dim_H(E\cap[U-1,U])=d.
}
\tag{8.3}
\]

To see this, write `U=n+theta`, `0<=theta<1`. Up to integer translation, the two pieces of `E` inside the unit window correspond to `C_3 cap [theta,1]` and `C_3 cap [0,theta]`; their union is `C_3`. Hausdorff dimension of a finite union is the maximum of the dimensions of the pieces, proving (8.3). The strict inequality in (8.2) is equivalently `4>3` after exponentiating `2 log 2>log 3`; no numerical approximation is used.

### 8.2 A nonlinear singular BV center track

Let `D_5 subset[0,1]` be the two-map Cantor set generated by

\[
x\mapsto x/5,\qquad x\mapsto 4/5+x/5,
\]

and let `F_5:[0,1]->[0,1]` be the distribution function of its natural `(1/2,1/2)` Cantor measure. Thus `F_5` is continuous, nondecreasing, and has total variation `1`.

Lift it continuously across unit intervals by

\[
q(n+t)=n+F_5(t),\qquad n\in\mathbb Z_{\ge0},\ 0\le t\le1.
\tag{8.4}
\]

Since `F_5(0)=0` and `F_5(1)=1`, the definitions match at integers. Hence `q` is continuous, nondecreasing, and locally of bounded variation.

It is deliberately **not** a smooth or even `1/2`-Hölder track. On the leftmost level-`m` Cantor cylinder,

\[
F_5(5^{-m})-F_5(0)=2^{-m},
\]

so

\[
\frac{F_5(5^{-m})-F_5(0)}{\sqrt{5^{-m}}}
=\left(\frac{\sqrt5}{2}\right)^m\longrightarrow\infty.
\tag{8.5}
\]

Thus neither `F_5` nor the lifted `q` is `1/2`-Hölder. The center trace has a genuine singular Cantor component in its variation measure.

### 8.3 Countably many moving pin positions

Let

\[
A=\{0\}\cup\{1/m:m\ge1\}\subset[0,1],
\qquad h(u)=\min\{u,1\},
\]

and define the compact countable moving gate fiber

\[
L(u)=q(u)+h(u)A.
\tag{8.6}
\]

Equivalently its tracks are

\[
q_0(u)=q(u),\qquad
q_m(u)=q(u)+\frac{h(u)}m,\quad m\ge1.
\tag{8.7}
\]

Every `q_m` is continuous and locally of bounded variation. For `u>=1`, the pin fiber is countably infinite with a genuine accumulation point at `q(u)`.

Now let

\[
r(u)=u^3\operatorname{dist}(u,E)
\tag{8.8}
\]

and define the deterministic fibers

\[
K_*(u)=\{x\in\mathbb R:\operatorname{dist}(x,L(u))\le r(u)\}.
\tag{8.9}
\]

Finally put

\[
\mathcal S_{BV}
=\{(-u,x):u>0,\ x\in K_*(u)\}\cup\{(0,0)\}.
\tag{8.10}
\]

The set is closed. Indeed `q` and `h` are continuous, `A` is compact, so `L(u)` varies continuously in Hausdorff distance; `r` is continuous. As `u downarrow0`, `q(u)->0`, `h(u)->0`, and `r(u)<=u^4` because `0` is a limit pin time, so every bounded space-time limit at time zero lands at `(0,0)`.

At every gate age `u in E`,

\[
r(u)=0,\qquad K_*(u)=L(u)=\{q_m(u):m\ge0\}.
\tag{8.11}
\]

Thus T63 applies with `beta=1`, `T=1`, the gate set `E`, and the countable BV tracks (8.7). We obtain:

**Theorem T64.** For every forward Brownian motion `X`,

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ (-u,X_{-u})\in\mathcal S_{BV}
\quad\forall u\ge R
\right)=0.
}
\tag{T64}
\]

### 8.4 The spaces between gates are genuinely huge

Let

\[
u_n=n+\frac12.
\]

The midpoint `1/2` lies in the largest complementary gap `(1/3,2/3)` of `C_3`, so

\[
\operatorname{dist}(u_n,E)=\frac16,
\qquad
r(u_n)=\frac{u_n^3}{6}.
\tag{8.12}
\]

For all sufficiently large `n`, the radius `r(u_n)` is much larger than the largest gap in `A`, so the neighborhood in (8.9) is the single interval

\[
K_*(u_n)=[q(u_n)-r(u_n),\ q(u_n)+1+r(u_n)]
\]

and has diameter

\[
\boxed{1+\frac{u_n^3}{3}.}
\tag{8.13}
\]

Hence this is not a narrow ribbon or a parabolic cage: between the zero-measure fractal gate times its admissible chambers grow cubically.

A continuous deterministic selector also exists, for example `u -> q(u)`. Thus the obstruction is not topological nonexistence of a continuous path through the shape.

## 9. Frozen-equivalence audit: why this earns point 49

This is not counted merely because a parameter changed.

- **Versus run 48 (critical-gauge affine pinholes):** run 48 has a *single* affine pin position at each critical (`dim=1/2`) gate time and needs an exact logarithmic Hausdorff gauge. Here the gate fiber is **countably infinite with an accumulation point**, the center track is singular BV and not `1/2`-Hölder, and the temporal gate dimension is strictly above `1/2`. The proof is countable branch decomposition plus Brownian restriction variation, not level-set exact gauge. Brownian scaling/reflection/constant translation preserves fiber cardinality and cannot turn a singular Cantor variation component into an affine derivative.
- **Versus run 45 (strict fractal-dimension pinning):** run 45 pins into one fixed bounded spatial fractal and uses Brownian image dimension. Here the allowed pin set moves with `u`, is countable, and its center escapes linearly; there is no fixed spatial target to which the run-45 image argument applies.
- **Versus runs 40--42 (critical Hölder webs/forests/lattice braid):** those constrain the path on every time in a witness window and derive a `1/2`-Hölder selector contradiction. Here the restriction occurs only on a zero-measure fractal set of times, the tracks are singular BV and the canonical center is not `1/2`-Hölder, while the complementary chambers are cubic.
- **Versus run 43 (pinching Cantor lamination):** that family has uncountable Cantor fibers and full-time lamination structure. T63 depends essentially on a **countable** moving track family and only fractal-time gates.
- **Versus run 44 (positive-density occupation curtains):** `E` has zero Lebesgue measure, so the positive occupation-time argument is silent.
- **Versus run 39 (global dimension barrier):** the shape has open two-dimensional chambers between gate times; its whole space-time dimension is not below `3/2`.

The invariants “countably infinite accumulating gate fiber”, “singular BV center trace”, and “fractal gate-time set of dimension strictly between `1/2` and `1`” survive the frozen trivial equivalences. Therefore this is a genuinely different structural family and the metric moves `48 -> 49`.

## 10. Exact checking / audit status

There is no finite enumeration or numerical finite core in T63/T64. The proof is analytic and rests on the published Balka--Peres pathwise restriction theorem plus elementary variation and Hausdorff-dimension facts. I therefore did **not** manufacture a checker merely to certify trivial arithmetic such as `4>3`.

Self-checks performed on the page:

1. fixed deterministic witness index before the Brownian probability-one event;
2. no conditioning on the random witness time;
3. reflected gate set has the correct sliding-window dimension;
4. countable-union dimension step is the only place countability enters;
5. restriction of a locally finite-`beta`-variation track remains finite variation after reflection and constant subtraction;
6. concrete singular staircase is BV but fails the `1/2`-Hölder test;
7. canonical shape is closed and has cubic-width chambers between gates.

These are **self-checks**, not independent audits. New claims T63/T64 have `0/2` required OTHER-track audits. Consequently the source problem remains **PARTIAL**, not PROVED/closed.

## 11. What the new route says to try next

The new sharp obstruction is no longer “how many branches?” by itself. Two genuine frontiers remain:

1. **critical restriction dimension** `dim_H Z=beta/2`, where Balka--Peres is sharp and one needs exact gauges/capacities rather than dimension;
2. **uncountable but geometrically thin track families**, where countable stability fails but a parameter-space dimension estimate may still force one branch class to carry a large restriction set.

The second suggests a possible next theorem of the form

\[
\dim_H Z>\frac\beta2+\dim_H(\text{track parameter space})\times(\text{appropriate loss}),
\]

but no such formula is claimed here. A correct proof would need a slicing or incidence theorem that survives path-dependent branch selection.

## 12. Model/scheduler control status

The configuration limitation is still present at the exposed control surface. The available scheduler schema provides title/prompt, schedule/start-offset, enablement and timing mode, but **no binding model-family selector, no reasoning-effort selector, no guaranteed-hour execution field, and no authenticated applied-model receipt**. Thus `GPT-6 / maximum` remains a prompt request only in this environment; this run actually reports GPT-5.6 Sol and leaves reasoning as UNVERIFIED.

The current compact `RESULTS.md` refines the historical permissions story: the old P26 `You cannot modify this task` failure was context-specific; P26's full prompt update later **succeeded from an authorized context**. The same ledger also records a separate reconciliation context in which all 20 R-series native IDs rejected edits. The legitimate remedy for a still-denied native task is therefore the owning/authorized account or workspace, an authorized ownership/admin correction, or platform support. It is not a duplicate schedule, permission bypass, or repository edit.

Actually enforcing GPT-6 maximum would require the product/scheduler to expose persistent `model` and `reasoning_effort` controls (or a workspace policy that pins them) and authenticated runtime telemetry confirming what ran. No scheduler change is attempted in this run.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  allocation: CLOSABLE_OUTSIDE
  source_id: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  target: "generalize Theorem 4.3 beyond parabolic regions"
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  before: 48
  after: 49
  movement: "+1"
  new_claims:
    - I0077-R07-T63: "countable finite-beta-variation fractal-gate obstruction"
    - I0077-R07-T64: "singular-staircase countable gate-comb corollary"
  source_status: PARTIAL
  claim_registry_status: "PENDING_ADMISSION, not READY"
  novelty: UNVERIFIED
  audits_new_claims: "0/2 independent OTHER-track audits"
  finite_core_checker: "NONE — no finite computational core"
  old_kpz_route: "retired handoff preserved"
  methods: [1, 2, 3]
  unchanged_streak_after_run: 0
  remaining_obligation: "independent audits for any closure claim; source Problem 7.8 remains open-ended; next mathematical frontier is critical-dimension or uncountable thin track families"
```
