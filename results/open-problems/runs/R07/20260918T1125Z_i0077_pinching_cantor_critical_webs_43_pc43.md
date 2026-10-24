Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `42 -> 43` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9 is the separate forward-Lévy problem and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 43: recurrently pinching critical Cantor laminations

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and metric baseline

The fixed R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative R07 report is

`runs/R07/20260918T1032Z_i0077_compact_rectangle_critical_webs_42_cr42.md`,

which moved `41 -> 42` and used methods `#1,#15,#20`. The present triple `#2,#3,#12` is different. All thirty Section-B labels have already appeared somewhere in the long I0077 chain, so the literal “never used on this problem” pool is exhausted; I preserve that fact rather than inventing history. What is new here is the route, theorem, and shape class.

Before doing new mathematics I reread/recovered the current `master` state from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the newest own R07 report and the searchable I0077 chain, especially runs 18, 32, 35, 39, 40, 41, and 42 because they are the nearest equivalence collisions;
- the newest neighboring R15 report `runs/R15/20260918_1057Z_successor_admission_f0111_overlap_tensor_d56e.md`; its distinct Burdzy–Scheutzow Problem 7.2 / I0076 remains in retired-handoff status and is not reopened;
- the exact I0077 claim and targeted intake/attempt searches for `I0077`, `1302.6958`, `Problem 7.8`, and the exact source wording.

`INDEX.md` and `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` has no exact Problem-7.8 closure. `QUEUE.md` still lists I0077 as a candidate, while the canonical claim reserves it provisionally to R07 and still literally says `PENDING_ADMISSION, not READY`. I preserve that operational label. The old R07 KPZ/FPP route remains preserved by immutable handoff and is not reopened or deleted.

The large `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered byte-for-byte through the connector in one response without truncation. Intake reread is therefore honestly **targeted/partial because of connector limits**: the exact I0077 source, ownership, exclusions, and searchable prior attempts were recovered. I do not claim a literal reread of hundreds of unrelated rows.

Entering metric: **42**.  
Entering unchanged count: **0**.

## 2. Primary source recovered exactly

I reopened the primary Burdzy–Scheutzow PDF on 2026-09-18 and directly inspected the rendered pages containing Definition 2.1, Theorem 4.3, and Problems 7.8–7.9.

Definition 2.1 says that an FBM `X=(X_t)_{t in R}` has random witness times `S_j -> -infinity` such that, for every **fixed deterministic witness index** `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\tag{2.1}
\]

is standard Brownian motion.

For a static parabolic interval `[c_1,c_2]`, Theorem 4.3 says:

1. if `lambda_0(c_1,c_2)>=1`, every FBM obeys the universal far-past normalized limsup/liminf obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM pointwise confined to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” The immediately following forward-Lévy sentence is Problem 7.9, not part of 7.8.

The theorem below gives a complete universal-obstruction result for a new deterministic nonparabolic shape class. It does **not** classify all space-time shapes and therefore does not close Problem 7.8.

## 3. Fresh 2026-09-18 current-status / prior-art pass

Fresh bounded web searches included:

- `Burdzy Scheutzow Forward Brownian Motion Problem 7.8 Theorem 4.3`;
- exact title / arXiv-ID searches for later work explicitly mentioning Problem 7.8;
- `Brownian motion Cantor lamination time-dependent pinching Hölder 1/2`;
- `Brownian motion totally disconnected moving set Hölder`;
- `Brownian motion Weierstrass Cantor moving boundary`;
- Weixiao Shen's classical Weierstrass graph-dimension theorem.

The original paper was recovered directly and no accessible later source in this bounded pass explicitly claimed to resolve exact Problem 7.8 or stated the pinching-lamination theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

Nearby prior art is substantial and is not being relabeled as new. Bass–Burdzy study Brownian local times on Hölder curves; Peres–Sousi study Brownian motion plus deterministic variable drift and show a special role for Hölder exponent `1/2`; Shen proves the exact graph Hausdorff dimension of the classical Weierstrass function. The elementary facts that continuous maps from connected sets into totally disconnected spaces are constant and that Brownian motion is almost surely not `1/2`-Hölder are classical. The possible new content here is the source-specific deterministic compiler from recurrent pinching plus total disconnectedness to an FBM obstruction, not any of those ingredients in isolation.

## 4. Method #2 — attack the negation first: total disconnectedness is genuinely needed

A tempting overgeneralization of run 32 is:

> if `K` is any compact coefficient set and the fibers are `b(u)+phi(u)K`, perhaps every continuous selector automatically inherits the `1/2`-Hölder modulus of `b` and `phi`.

This is false even in the easiest zero-free case. On `[0,1]`, take

\[
K=[-1,1],\qquad b\equiv0,\qquad \phi\equiv1,
\]

and choose any `alpha in (0,1/2)`. Then

\[
h(t)=t^\alpha
\]

is a continuous selector because `h(t) in K`, but

\[
\frac{|h(t)-h(0)|}{\sqrt t}=t^{\alpha-1/2}\longrightarrow\infty.
\]

So a connected coefficient set lets the selector continuously modulate its coefficient and manufacture roughness unrelated to the sheet regularity. This does not refute Problem 7.8; it refutes only the proposed deterministic extension.

**Outcome #2: success as falsification.** Any proof needs a topological restriction on coefficient motion during zero-free epochs. Total disconnectedness is exactly enough.

## 5. Method #3 — stronger theorem: uncountably many critical sheets may accumulate in one bounded rectangle

The previous run 42 allowed infinitely many critical sheets at every age, but required compact-rectangle local finiteness. The present theorem removes local finiteness completely: each nonpinch fiber may contain an uncountable perfect set of sheets inside one bounded vertical interval.

### Definition 5.1 — pinching totally disconnected critical lamination

Let `K subset R` be a nonempty compact totally disconnected set and set

\[
A:=\max_{z\in K}|z|<\infty.
\]

Let `b,phi:(0,infinity)->R` be deterministic and locally `1/2`-Hölder. Define

\[
\boxed{
\mathcal P(K,b,\phi)
=
\{(-u,b(u)+\phi(u)z):u>0,\ z\in K\}.
}
\tag{5.1}
\]

At every zero of `phi`, the whole fiber collapses to the singleton `{b(u)}`. Between zeros, the totally disconnected coefficient address cannot vary continuously.

### Lemma 5.2 — pinching-selector Hölder compiler

Let `I=[a,c] subset (0,infinity)` be compact. Suppose a continuous function `h:I->R` satisfies

\[
h(u)\in b(u)+\phi(u)K\qquad(u\in I).
\tag{5.2}
\]

Then `h` is `1/2`-Hölder on `I`.

More quantitatively, if on `I`

\[
|b(u)-b(v)|\le L_b\sqrt{|u-v|},\qquad
|\phi(u)-\phi(v)|\le L_\phi\sqrt{|u-v|},
\tag{5.3}
\]

then

\[
\boxed{
|h(u)-h(v)|
\le
\bigl(L_b+\sqrt2 A L_\phi\bigr)\sqrt{|u-v|}
\qquad(u,v\in I).
}
\tag{5.4}
\]

#### Proof

Write

\[
y(u)=h(u)-b(u).
\]

Then `y(u) in phi(u)K`. Fix `s<t` in `I`.

**Case 1: `phi` has no zero on `[s,t]`.**  The map

\[
a(u)=\frac{y(u)}{\phi(u)}
\]

is continuous from the connected interval `[s,t]` into the totally disconnected set `K`. Therefore it is constant, say `a(u)=q in K`. Hence

\[
|y(t)-y(s)|
=|q|\,|\phi(t)-\phi(s)|
\le A L_\phi\sqrt{t-s}.
\tag{5.5}
\]

**Case 2: `phi` vanishes somewhere in `[s,t]`.** Choose `r in [s,t]` with `phi(r)=0`. Since `y(r) in phi(r)K`, we have `y(r)=0`. Also `|y(x)|<=A|phi(x)|` for every `x`. Thus

\[
\begin{aligned}
|y(t)-y(s)|
&\le |y(t)|+|y(s)|\\
&\le A\bigl(|\phi(t)-\phi(r)|+|\phi(s)-\phi(r)|\bigr)\\
&\le A L_\phi\bigl(\sqrt{t-r}+\sqrt{r-s}\bigr)\\
&\le \sqrt2 A L_\phi\sqrt{t-s}.
\end{aligned}
\tag{5.6}
\]

Combining (5.5)–(5.6) with the bound for `b` proves (5.4). `QED`

The important point is that **no cardinality, local-finiteness, summable-variation, or branch-count condition appears**. `K` may be an uncountable Cantor set and all of its sheets may lie inside one compact rectangle.

## 6. Brownian critical roughness, self-contained

### Lemma 6.1

Standard Brownian motion on `[0,1]` is almost surely not `1/2`-Hölder.

#### Proof

For integer `C>=1`, let

\[
H_C=\{|B_t-B_s|\le C\sqrt{|t-s|}\ \forall s,t\in[0,1]\}.
\]

If `H_C` occurs, then at dyadic level `n` all `2^n` normalized increments satisfy

\[
2^{n/2}|B_{(j+1)2^{-n}}-B_{j2^{-n}}|\le C.
\]

For fixed `n` these variables are independent copies of `|Z|`, `Z~N(0,1)`. Therefore

\[
\mathbb P(H_C)
\le \mathbb P(|Z|\le C)^{2^n}\longrightarrow0.
\]

Hence `P(H_C)=0` for every integer `C`. The event that `B` is `1/2`-Hölder is the union of the `H_C`, so it has probability zero. `QED`

## 7. I0077-R07-T51 — pinching-lamination obstruction for every FBM

Let `K` be nonempty compact and totally disconnected, and let `b,phi` be locally `1/2`-Hölder on `(0,infinity)`. For the space-time shape `mathcal P(K,b,phi)` in (5.1), every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:
X_{-u}\in b(u)+\phi(u)K
\quad\forall u\ge R
\right)=0.
}
\tag{T51}
\]

### Proof

Assume to the contrary that the displayed event has positive probability. By a countable union over integer radii, choose a deterministic integer `R>=1` for which

\[
E_R:=\{X_{-u}\in b(u)+\phi(u)K\ \forall u\ge R\}
\]

has probability `p>0`.

Let `(S_j)` be an FBM witness sequence. Since `S_j->-infinity` almost surely, choose one **deterministic index** `j` so far left that

\[
\mathbb P(S_j\le -R-1)>1-p/2.
\]

Then

\[
A_R:=E_R\cap\{S_j\le-R-1\}
\]

has probability at least `p/2>0`.

On `A_R`, for every `s in [0,1]`, the age

\[
u(s)=-(S_j+s)
\]

lies in `[ -S_j-1,-S_j] subset [R,infinity)`, and therefore

\[
X_{S_j+s}=X_{-u(s)}\in b(u(s))+\phi(u(s))K.
\]

The random age interval `[ -S_j-1,-S_j]` is compact and contained in `(0,infinity)`. Because `b` and `phi` are locally `1/2`-Hölder, Lemma 5.2 implies that

\[
s\mapsto X_{S_j+s}
\]

is `1/2`-Hölder on `[0,1]` (with a finite constant that may depend on the realized compact age interval). Subtracting the constant `X_{S_j}` preserves this property. Hence on `A_R`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j}
\]

is `1/2`-Hölder on `[0,1]`.

But for this fixed deterministic witness index `j`, Definition 2.1 says that `B^{(j)}` is unconditionally standard Brownian motion. By Lemma 6.1 the event that it is `1/2`-Hölder has probability zero. Thus `P(A_R)=0`, contradicting `P(A_R)>=p/2`. `QED`

No conditioning on `S_j` and no independence assumption involving the witness time is used.

## 8. Method #12 — the exact conserved quantity and why pinching does not defeat it

Away from the zero set

\[
Z_\phi=\{u>0:\phi(u)=0\},
\]

a confined selector has coefficient address

\[
a(u)=\frac{X_{-u}-b(u)}{\phi(u)}\in K.
\tag{8.1}
\]

On each connected component of `(0,infinity)\setminus Z_\phi`, continuity plus total disconnectedness of `K` forces `a(u)` to be constant. So the address is a **piecewise conserved quantity**.

At a pinch `u in Z_phi`, however, the whole fiber is the singleton `{b(u)}` and the old address disappears; after the pinch the path may select a completely different address. Thus recurrent pinches genuinely destroy the **global** conserved leaf label from run 32. The surviving invariant is weaker and local: conservation only between successive pinches. Lemma 5.2 shows that this is still enough to keep every selector at the critical `1/2` modulus.

**Outcome #12: success.** The correct invariant is “address conserved on zero-free components, reset only at total-fiber pinches.”

## 9. Concrete metric family 43 — recurrently pinching critical Cantor lamination

Let `C` be the middle-thirds Cantor set in `[0,1]` and set

\[
K_*=2C-1\subset[-1,1].
\tag{9.1}
\]

Let

\[
W(r)=\sum_{n=0}^{\infty}2^{-n/2}\cos(2\pi2^nr).
\tag{9.2}
\]

A standard frequency split gives a finite constant `L` such that

\[
|W(x)-W(y)|\le L\sqrt{|x-y|}\qquad(x,y\in\mathbb R).
\tag{9.3}
\]

Indeed, for `delta=|x-y|<1`, split at `2^N approximately delta^{-1}`. For `n<=N`, the mean-value bound contributes

\[
O\left(\delta\sum_{n\le N}2^{n/2}\right)=O(\sqrt\delta),
\]

while the tail contributes

\[
O\left(\sum_{n>N}2^{-n/2}\right)=O(\sqrt\delta).
\]

For `delta>=1`, boundedness of the uniformly convergent series gives the same form after enlarging `L`.

Define

\[
\phi_*(u)=\sqrt u\,W(\log u),\qquad u>0,
\tag{9.4}
\]

and

\[
\boxed{
\mathcal P_*
=
\{(-u,\phi_*(u)z):u>0,\ z\in K_*\}
\cup\{(0,0)\}.
}
\tag{9.5}
\]

On every compact interval `[a,c] subset (0,infinity)`, `log` is Lipschitz and `sqrt u` is Lipschitz and bounded, so (9.3) implies that `phi_*` is `1/2`-Hölder there. Also `|phi_*(u)|<=||W||_infty sqrt u`, so the added point `(0,0)` closes the shape at age zero.

The fibers pinch recurrently. Directly,

\[
W(0)=\frac1{1-2^{-1/2}}>0.
\tag{9.6}
\]

Since `2^n mod 3` alternates between `1` and `2`, every cosine in `W(1/3)` equals `-1/2`, so

\[
W(1/3)=-\frac1{2(1-2^{-1/2})}<0.
\tag{9.7}
\]

By continuity there exists `r_* in (0,1/3)` with `W(r_*)=0`. Because `W` is 1-periodic,

\[
u_m=e^{r_*+m},\qquad m\in\mathbb Z,
\tag{9.8}
\]

are pinch ages and

\[
\mathcal P_*\cap(\{-u_m\}\times\mathbb R)=\{(-u_m,0)\}.
\]

Between pinches, every nonzero fiber is an affine copy of the perfect uncountable Cantor set `K_*`; in particular infinitely/uncountably many sheets occupy one bounded normalized region. A continuous confined path may emerge after each pinch with a different Cantor address. There is therefore no globally conserved leaf label.

Applying T51 with `b=0`, `K=K_*`, and `phi=phi_*` gives the concrete source-appropriate theorem

\[
\boxed{
\mathbb P\left(
\exists R:\ X_{-u}\in \sqrt u\,W(\log u)K_*
\quad\forall u\ge R
\right)=0
}
\tag{T52}
\]

for every FBM `X`.

## 10. Critical fractal character and distinction from the previous metric families

Shen's theorem for the classical Weierstrass function with `b=2` and `lambda=2^{-1/2}` gives

\[
\dim_H \operatorname{graph}(W)
=2+\frac{\log(2^{-1/2})}{\log2}
=\frac32.
\tag{10.1}
\]

For any fixed nonzero `z in K_*` and any full logarithmic period `[m,m+1]`, the map

\[
(r,y)\mapsto(e^r,z e^{r/2}y)
\]

is bi-Lipschitz on the corresponding compact slab. Hence every nonzero leaf of (9.5) has graph Hausdorff dimension exactly `3/2` on those slabs. Thus run 39's strict-`<3/2` deterministic-set obstruction is silent here.

The metric point is structurally new under the frozen equivalence convention:

- **Not run 32 (nondegenerate moving Cantor laminations).** Run 32 assumes the normalized scale is bounded away from zero, so the Cantor address is globally conserved. Here the scale vanishes at infinitely many ages, the whole uncountable fiber collapses to one point, and the address can reset after every pinch. Recurrent full-fiber collapse versus no collapse is preserved by Brownian scaling, reflection, and constant translation.
- **Not run 42 (compact-rectangle locally finite critical webs).** The present web violates compact-rectangle local finiteness maximally: at every nonpinch age a bounded vertical slice contains uncountably many distinct leaves.
- **Not runs 40–41 (finite / time-locally-finite critical braids).** The active branch set is uncountable between pinches, and no finite branch-intersection graph exists.
- **Not run 34 (countably accumulating BV web).** The critical Weierstrass leaves have exact graph dimension `3/2` and do not arise from a summable BV budget.
- **Not run 35 (uniform finite-lag bounded cage).** On phases where `|W(log u)|` is bounded below, the fiber diameter is of order `sqrt u`, so its fixed-lag cross-diameter is not uniformly bounded.
- **Not run 18 (infinite parabolic comb).** The comb has a fixed normalized discrete tooth set and a conserved branch label; the present normalized Cantor fiber collapses recurrently and permits address resets.
- **Not run 39 (strict dimension barrier).** The shape contains `3/2`-dimensional leaves, exactly at the Brownian graph threshold.

Different choices of `K,b,phi` satisfying T51 are **not** counted separately. This run adds exactly one structural family: recurrently pinching totally disconnected critical laminations.

## 11. What the three methods did

- **#2 ATTACK THE NEGATION FIRST — success.** The unrestricted compact-coefficient selector claim is false for `K=[-1,1]`; `h(t)=t^alpha`, `alpha<1/2`, is an exact counterexample. This isolated total disconnectedness as the needed topological input.
- **#3 PROVE SOMETHING STRONGER — success.** Instead of merely allowing countably many locally finite sheets, T51 allows an arbitrary compact totally disconnected coefficient set, hence uncountably many critical leaves accumulating inside one compact rectangle, with no branch-count/entropy bound.
- **#12 FIND WHAT IS CONSERVED — success.** The Cantor address is conserved on each zero-free component of `phi` and is erased only at pinches. This piecewise invariant, plus the common critical modulus, is exactly enough to rule out Brownian witness segments.

No finite arithmetic core arose. I therefore did not manufacture an exact-arithmetic checker merely to create a certificate. The theorem-sized claim is written in full above.

## 12. Status, audits, and next frontier

New claims:

- `I0077-R07-T51`: pinching totally disconnected critical-lamination obstruction;
- `I0077-R07-T52`: recurrent critical Weierstrass–Cantor lamination example.

Independent OTHER-track audits: **0/2**. There is no P26 audit and no second independent audit yet. Therefore source status remains **PARTIAL**, not closed, and no paper folder is created.

The strongest next frontier is no longer mere branch cardinality. T51 shows that even an **uncountable** critical fiber can be impossible when its coefficient space is totally disconnected and the only allowed address changes occur at total-fiber pinches. The next genuinely different question is what happens when the coefficient space has small connected pieces or when different sheets merge through a hierarchical graph that permits controlled but nontrivial coefficient motion. A natural quantitative target is a scale-dependent connected-component/branching entropy whose allowed selector modulus can be compared to Brownian's `sqrt(delta log(1/delta))` modulus.

## 13. Scheduler/model-control and permission status

Actual runtime evidence for this report is the first line: **GPT-5.6 Sol; reasoning level UNVERIFIED**, not GPT-6 maximum.

The exposed task-control interface available to this worker still offers prompt/title, schedule or start-offset, enablement, and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no guaranteed one-hour execution control, and no authenticated applied-model receipt**. Thus GPT-6/maximum can only be requested in prompt text from this surface. Changing that requires an authorized product/backend/API surface that exposes and persists model and reasoning fields, or platform support.

The historical P26 `You cannot modify this task` result is not a permanent current failure: current repository state records that P26 was later updated successfully from a different authorized context. If a task still refuses modification, the legitimate workaround is the owning/authorized account or workspace context, an authorized ownership/admin correction, or platform support — not a duplicate schedule or permission bypass. This run was explicitly prohibited from scheduler changes, so none was attempted.

## 14. Structured ledger delta

```yaml
ledger_delta:
  worker: R07
  allocation: CLOSABLE_OUTSIDE
  intake: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  target: "generalize Theorem 4.3 beyond parabolic space-time regions"
  status_before: PARTIAL
  status_after: PARTIAL
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  metric_before: 42
  metric_after: 43
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  new_family: "recurrently pinching totally disconnected critical laminations"
  new_claims:
    - I0077-R07-T51
    - I0077-R07-T52
  independent_other_track_audits: 0
  closure: false
  prior_art_status: "fresh bounded 2026-09-18 search; no explicit exact match found; publication novelty UNVERIFIED"
  finite_core: none
  checker: none
  next_frontier: "connected coefficient pieces / hierarchical merger entropy versus Brownian critical modulus"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  scheduler_model_selector: unavailable
  scheduler_reasoning_selector: unavailable
```
