Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `43 -> 44` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #1 CHANGE THE CATEGORY, #24 FIND THE EXTREMAL OBJECT.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** Problem 7.9 is the separate forward-Lévy question and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 44: positive-density occupation curtains and fat-Cantor temporal pinning

Run date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and frozen metric

The fixed R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/constant translation and mere parameter changes inside one structural family do not create new metric points.

The immediately preceding authoritative R07 report is

`runs/R07/20260918T1125Z_i0077_pinching_cantor_critical_webs_43_pc43.md`,

created at `96070ecc2665a34f198efded1bcb08c92765f337`. It moved `42 -> 43` and used methods `#2,#3,#12`. The present triple `#2,#1,#24` is not the preceding triple. As recorded in runs 42 and 43, all thirty Section-B labels have already appeared somewhere in the long I0077 chain; the literal pool of labels “never tried on this problem” is exhausted, so I do not invent a false unused label. The route and theorem below are new.

Before new mathematics I reread/recovered current `master` from:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and `operations/claims/I0077.md`;
- the newest own R07 report and the closest possible equivalence collisions, especially runs 24, 29, 32, 35–36, and 39–43;
- current neighboring R15 state. Its Burdzy–Scheutzow Problem 7.2 / I0076 remains in retired-handoff state; the newest R15 work is a distinct Talagrand successor screen, so there is no ownership collision;
- targeted repository searches for `I0077`, `1302.6958`, `Problem 7.8`, and prior R07 shape-family labels.

`INDEX.md` / `RANKING.md` settle Burdzy–Scheutzow Problem 7.5, not 7.8. `POSTED.md` contains no exact Problem-7.8 closure. `QUEUE.md` continues to list I0077, while the canonical claim reserves it provisionally to R07 and still literally says `PENDING_ADMISSION, not READY`. I preserve that operational label rather than silently promoting it. The old R07 KPZ/FPP route remains preserved by immutable handoff and is not reopened or deleted.

The huge `probability_1000_intake_*/problems.jsonl` mirrors cannot be rendered row-by-row through the connector without truncation. Intake reread is therefore honestly **targeted/partial due connector limits**: exact I0077 source, ownership, exclusions, and searchable prior attempts were recovered; I do not claim a byte-for-byte reread of hundreds of unrelated rows.

Entering metric: **43**.  
Entering unchanged count: **0**.

## 2. Primary source recovered again

I reopened the primary Burdzy–Scheutzow paper and checked Definition 2.1, Theorem 4.3, and Problems 7.8–7.9.

Definition 2.1 says that an FBM `X=(X_t)_{t in R}` has random witness times `S_j -> -infinity` such that, for each **fixed deterministic witness index** `j`,

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j},\qquad s\ge0,
\tag{2.1}
\]

is standard Brownian motion.

For a static parabolic interval `[c_1,c_2]`, Theorem 4.3 gives the source benchmark:

1. if `lambda_0(c_1,c_2)>=1`, every FBM satisfies the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2)<=1`, there exists a decomposable FBM with the corresponding normalized asymptotic inclusion;
3. if `c_1<=0<=c_2` and `lambda_0(c_1,c_2)<1`, there exists a decomposable FBM pointwise confined to the exact parabolic strip for every `t<=0`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 “from parabolas to other space-time shapes.” The immediately following forward-Lévy sentence is Problem 7.9 and is not part of 7.8.

The theorem below is a complete universal-obstruction theorem for a new temporal-pinning family. It does **not** classify all space-time shapes and therefore does not close Problem 7.8.

## 3. Fresh current-status and prior-art pass — 2026-09-18

Fresh bounded searches included:

- exact `Forward Brownian Motion` / `Problem 7.8` / `other space-time shapes` queries;
- later/citing-paper searches around Burdzy–Scheutzow;
- `Brownian motion occupation density level set Lebesgue measure zero local time`;
- `Brownian motion prescribed values positive measure time set`;
- `Brownian motion Cantor pinning time set` and `fat Cantor Brownian occupation`.

The original paper remains the identifiable source. The visible citation trail remains sparse (for example Pitman–Tang's spacetime-shift paper is adjacent but does not state an exact Problem-7.8 resolution). I found no accessible later source in this bounded pass explicitly resolving exact Problem 7.8 or stating the positive-density temporal-pinning theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

The probabilistic ingredient is classical and is not claimed new: Brownian occupation measure on a compact time interval is almost surely absolutely continuous with respect to spatial Lebesgue measure, with local time as density. Equivalently, on that almost-sure path event, Brownian motion spends zero clock time in **every** spatial Lebesgue-null Borel set simultaneously. The new source-specific step is to make this pathwise absolute-continuity fact compatible with a random FBM witness time without conditioning on that witness.

## 4. Method #2 — attack the negation first: topological abundance of pinch times is not enough

Before using occupation measure, I tried the stronger purely topological statement:

> perhaps an uncountable recurrent set of exact pinning times already forces enough path rigidity to obstruct FBMs.

That deterministic statement is false. Let `Z` be the 1-periodic extension of the ordinary middle-thirds Cantor set, which is closed, uncountable, nowhere dense, and Lebesgue null. Consider the maximally permissive deterministic curtain whose fiber is `{0}` at ages in `Z` and all of `R` at ages outside `Z`.

The continuous nonzero path

\[
h(u)=\operatorname{dist}(u,Z)
\tag{4.1}
\]

belongs to that curtain for every `u`: it equals zero on `Z`, and outside `Z` the curtain imposes no restriction. Thus neither uncountability, perfectness, recurrence, nor nowhere-density of the pinch set by itself forces a continuous selector to be zero or even roughness-controlled.

This is an exact deterministic counterexample to the proposed proof mechanism. It is **not** a counterexample to Problem 7.8 and does not assert existence of an FBM in that null-time curtain. What survives the counterexample search is quantitative clock-time mass, not topology alone.

**Outcome #2: successful falsification of the overgeneralized deterministic route.**

## 5. Method #1 — change category: from spatial geometry to Brownian occupation measure

Runs 39–43 controlled what a witness path could look like geometrically: dimension, Hölder roughness, local finiteness, and totally disconnected sheet addresses. The new route ignores geometric roughness of the admissible region away from selected ages.

For a continuous path `f:[0,T]->R`, define its occupation measure

\[
\mu_f(A)=\operatorname{Leb}\{s\in[0,T]:f(s)\in A\}.
\tag{5.1}
\]

For standard Brownian motion `B`, the occupation-density theorem gives, almost surely,

\[
\mu_B(A)=\int_A L_T^x\,dx
\tag{5.2}
\]

for every Borel set `A`, where `L_T^x` is Brownian local time. Consequently, on one pathwise probability-one event,

\[
\boxed{
|A|=0\quad\Longrightarrow\quad
\operatorname{Leb}\{s\in[0,T]:B_s\in A\}=0
\quad\text{for every Borel }A.
}
\tag{5.3}
\]

This simultaneous formulation is essential. The forbidden spatial set below will be randomly translated by `-X_{S_j}`, so a merely “for each deterministic level” statement would be too weak. Absolute continuity of the whole occupation measure handles all null sets at once.

## 6. I0077-R07-T53 — uniform positive-time null-fiber obstruction

### Theorem T53

Let `Z subset (0,infinity)` be deterministic and measurable. Suppose there exist constants

\[
T>0,\qquad m>0,\qquad U_0<\infty
\tag{6.1}
\]

such that every sufficiently far sliding age window contains at least `m` units of pinning time:

\[
\boxed{
\operatorname{Leb}\bigl(Z\cap[U-T,U]\bigr)\ge m
\qquad\forall U\ge U_0.
}
\tag{6.2}
\]

Let `A subset R` be a fixed Borel set of Lebesgue measure zero. For each age `u>0`, let `K(u) subset R` be an arbitrary deterministic fiber satisfying only

\[
\boxed{K(u)\subset A\qquad\text{for every }u\in Z.}
\tag{6.3}
\]

There is **no restriction whatsoever** on `K(u)` when `u notin Z`; it may equal all of `R`.

Then every forward Brownian motion `X` satisfies

\[
\boxed{
\mathbb P\left(
\exists R<\infty:\ X_{-u}\in K(u)
\quad\forall u\ge R
\right)=0.
}
\tag{T53}
\]

### Proof

Assume contrariwise that the displayed eventual-confinement event has positive probability. By a countable union over integer tail radii, choose a deterministic integer

\[
R\ge U_0
\]

such that

\[
E_R:=\{X_{-u}\in K(u)\ \forall u\ge R\}
\]

has probability `p>0`.

Let `(S_j)` be an FBM witness sequence. Since `S_j->-infinity` almost surely, choose one **deterministic witness index** `j` so far left that

\[
\mathbb P(S_j\le -R-T)>1-p/2.
\tag{6.4}
\]

Then

\[
G:=E_R\cap\{S_j\le-R-T\}
\tag{6.5}
\]

has probability at least `p/2>0`.

Fix an outcome in `G` and write

\[
U=-S_j.
\]

For `s in [0,T]`, the corresponding age is

\[
u=-(S_j+s)=U-s,
\]

which lies in `[U-T,U] subset [R,infinity)`. Define

\[
J_U:=\{s\in[0,T]:U-s\in Z\}.
\tag{6.6}
\]

Reflection of Lebesgue measure gives

\[
|J_U|
=|Z\cap[U-T,U]|
\ge m.
\tag{6.7}
\]

For every `s in J_U`, eventual confinement and (6.3) imply

\[
X_{S_j+s}\in A.
\tag{6.8}
\]

Subtracting the random constant `X_{S_j}` yields

\[
B^{(j)}(s):=X_{S_j+s}-X_{S_j}
\in A-X_{S_j}
\qquad(s\in J_U).
\tag{6.9}
\]

The random translate `A-X_{S_j}` is still a spatial Lebesgue-null Borel set. Hence (6.7)–(6.9) imply that the Brownian witness path `B^{(j)}` spends at least `m` units of clock time in **some** spatial null Borel set.

But for this fixed deterministic witness index `j`, Definition 2.1 says that `B^{(j)}` is unconditionally standard Brownian motion. On the probability-one occupation-density event (5.3), its occupation measure is absolutely continuous and therefore assigns zero time to **every** spatial null Borel set, including the path-dependent translate `A-X_{S_j}`. Thus the event described in (6.9) has probability zero.

This contradicts `P(G)>=p/2`. Therefore (T53) holds. `QED`

### Dependence audit

The proof does **not** condition on `S_j`, does not assume `S_j` is independent of `B^{(j)}`, and does not require `X_{S_j}` to have any distributional regularity. We use only one deterministic witness index `j` and a path-only almost-sure property of standard Brownian occupation measure that is simultaneous over all null spatial sets.

## 7. Method #24 — find the extremal object

T53 is strongest when the shape is made as permissive as possible away from the pinning ages. Define the maximal occupation curtain

\[
\widehat{\mathcal O}_{Z,A}
=
\{(-u,x):u\in Z,\ x\in A\}
\cup
\{(-u,x):u\notin Z,\ x\in\mathbb R\}.
\tag{7.1}
\]

If (6.2) holds and `|A|=0`, T53 says no FBM tail can remain even in this maximal curtain. Therefore **every deterministic subshape** obtained by narrowing the fibers away from `Z` inherits the same impossibility. There is no need to estimate the width, speed, roughness, Hausdorff dimension, or branch count of those nonpinning fibers.

This extremal formulation is the key distinction from the earlier cage and critical-web theorems: the complement of the pinning ages can literally contain the whole spatial line.

## 8. I0077-R07-T54 — fat-Cantor temporal pinning with ballistic escape chambers

The maximal curtain (7.1) need not be closed when `Z` is closed and nowhere dense, so I also give an explicit **closed** canonical space-time family with enormous escape chambers.

Let `C_SV subset [0,1]` be the Smith–Volterra–Cantor set. Recall the standard construction: remove the middle interval of length `1/4`, then the two middle intervals of length `1/16`, then four of length `1/64`, and so on. The limit set is compact, nowhere dense, and

\[
|C_{SV}|=\frac12.
\tag{8.1}
\]

Periodize it:

\[
E=C_{SV}+\mathbb Z.
\tag{8.2}
\]

Then `E` is closed, 1-periodic, nowhere dense, and by periodicity

\[
\boxed{|E\cap[a,a+1]|=\frac12\qquad\forall a\in\mathbb R.}
\tag{8.3}
\]

Let `C` be the ordinary middle-thirds Cantor set in `[0,1]`; it is compact and has Lebesgue measure zero. Define

\[
r(u)=u\,\operatorname{dist}(u,E),
\tag{8.4}
\]

and the closed backward shape

\[
\boxed{
\mathcal O_{SV,C}
=
\left\{(-u,x):u>0,\ \operatorname{dist}(x,C)\le r(u)\right\}
\cup\{(0,0)\}.
}
\tag{8.5}
\]

The map `(u,x) -> dist(x,C)-u dist(u,E)` is continuous. Because `0 in E`, `r(u)->0` as `u downarrow0`, so adjoining `(0,0)` gives the natural closed seam version.

At every `u in E`,

\[
r(u)=0,
\qquad
\mathcal O_{SV,C}(u)=C,
\tag{8.6}
\]

so the fiber is an uncountable spatial Cantor null set. At every `u notin E`, the fiber is a positive-thickness neighborhood of `C`. In particular, at the midpoint `u=n+1/2` of the first deleted Smith–Volterra gap `(n+3/8,n+5/8)`,

\[
\operatorname{dist}(u,E)=\frac18,
\qquad
r(u)=\frac{u}{8}.
\tag{8.7}
\]

For large `n`, `r(u)>1/6`, so the `r(u)`-neighborhood of the middle-thirds Cantor set fills all of its internal gaps and is the single interval

\[
[-r(u),1+r(u)],
\]

whose diameter is

\[
1+2r(u)=1+\frac u4.
\tag{8.8}
\]

Thus between pinches the allowed fiber has **ballistic order-`u` diameter**, far wider than the source's order-`sqrt(u)` parabolic scale. The obstruction is not a narrow corridor in disguise.

Apply T53 with

\[
Z=E\cap(0,\infty),\qquad T=1,\qquad m=\frac12,\qquad A=C.
\]

We obtain

\[
\boxed{
\mathbb P\left(
\exists R:\ (-u,X_{-u})\in\mathcal O_{SV,C}
\quad\forall u\ge R
\right)=0
}
\tag{T54}
\]

for every FBM `X`.

This is the counted metric family: **positive-density temporal null-fiber occupation curtains**, with the fat-Cantor/ballistic-chamber construction as a closed canonical representative.

## 9. Why this earns metric point 44

The family is not being counted merely because `1/2` was replaced by another density or because one Cantor set was substituted for another. The structural mechanism is new under the frozen equivalence convention.

### Not run 29: dense escape chimneys

Run 29 imposed a fixed closed parabolic interval on an **open dense** set of log-times (which could have arbitrarily small finite total measure) and allowed the full spatial line on the closed nowhere-dense complement. Continuity then filled the missing times, so the mechanism was purely topological dense-set saturation.

Here the restrictive age set `E` is the opposite category geometry: it is **closed nowhere dense** and therefore not dense. Continuity does not fill its complement. The obstruction instead comes from **positive clock-time measure** and absolute continuity of Brownian occupation measure. The two mechanisms survive opposite measure/category extremes.

### Not runs 24–28: gates and fences

Those shapes used separated gate intervals or sampled geometric epochs and paid persistence/transition costs. Here the restrictive set has empty interior and contains no pinning interval at all; interval-by-interval gate survival is unavailable. Every unit window nevertheless contains exactly `1/2` time of pinning in a dust-like set.

### Not runs 35–38: bounded/variable cage and braided ribbon bounds

The canonical escape chambers have order-`u` diameter along infinitely many ages, and the maximal theorem permits the entire real line away from `Z`. There is no finite fixed-lag cross-diameter or subdiffusive width hypothesis to exploit.

### Not runs 39–43: fractal dimension and critical Hölder webs

Those results constrained the geometry of one-dimensional sheets/laminations or selectors. The present closed shape has two-dimensional interior on open portions of spacetime and positive-width connected fibers for a dense open set of ages. Its obstruction does not say the selector is Hölder or low-dimensional; it says a Brownian witness cannot devote positive clock time to a spatial null set. The Cantor object that matters in the theorem may sit in the **fiber only at pinning ages**, while the decisive new structure is the positive-measure **temporal** pinning set.

Brownian scaling/reflection/constant translation cannot turn a closed nowhere-dense positive-measure temporal pinning set into run 29's open dense restrictive set, nor can it turn order-`u` escape chambers into a fixed bounded-width ribbon. The new family therefore earns one metric point under the frozen convention.

## 10. What the negation search says about the boundary

The proof reveals a real threshold for this mechanism.

- Topological largeness of the pinning set is insufficient: a perfect uncountable null pinning set admits nontrivial continuous selectors such as `dist(u,Z)`.
- Positive time mass in every witness-sized window is sufficient when the pin fiber is spatially Lebesgue-null.
- Spatial nullness is the exact occupation-measure hypothesis used by the argument. If the pin fiber has positive spatial measure, Brownian occupation measure can charge it and the proof no longer works.

No converse is claimed. In particular, I do **not** claim that a null temporal pinning set is feasible for an FBM, or that a positive-measure spatial pin fiber makes eventual confinement possible. Those are separate questions.

A natural next route is to replace positive Lebesgue time by a fractal criterion. Brownian level sets have Hausdorff dimension `1/2`; one can ask whether a deterministic pinning set with zero Lebesgue measure but dimension strictly greater than `1/2`, or suitable positive capacity, already forces a contradiction for all FBMs. That would genuinely extend T53 rather than vary its density parameter.

## 11. Verification / closure state

There is no finite arithmetic core in T53/T54, so **no checker was manufactured**. The new theorem-sized claim is written in full on the page, including the random-witness dependence audit. The only imported mathematical fact is the classical Brownian occupation-density theorem, explicitly identified as prior art.

Independent OTHER-track audits for the new claim:

- P26: **missing for T53/T54**;
- second distinct track: **missing for T53/T54**.

Therefore the source status remains

\[
\boxed{\text{PARTIAL, not closed}.}
\]

No paper package is created before the required independent audits. Publication novelty remains **UNVERIFIED**.

## 12. Model / scheduler-control status

The requested runtime line remains prompt-only. The exposed task-control interface documented by the current repository policy provides prompt/title, schedule/start-offset, enablement and timing mode, but no binding model-family selector, reasoning-effort selector, guaranteed one-hour execution control, or authenticated completed-run model receipt. Therefore I report the actual visible model as GPT-5.6 Sol and reasoning telemetry as UNVERIFIED rather than claiming GPT-6 maximum.

The historical P26 `You cannot modify this task` result was authorization-context-specific; current `RESULTS.md` records that P26 was later updated successfully from another authorized context. For a task that still refuses modification, the legitimate workaround is the owning/authorized account or workspace context, an authorized ownership/admin correction, or platform support. No permission bypass, duplicate task, or scheduler mutation was attempted here.

## 13. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  source_id: I0077
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8"
  fixed_metric: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem under the frozen equivalence convention"
  metric_before: 43
  metric_after: 44
  movement: "+1"
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_this_run: [2, 1, 24]
  new_family: "positive-density temporal null-fiber occupation curtains; closed fat-Cantor pinning / ballistic escape chambers"
  theorem_ids: [I0077-R07-T53, I0077-R07-T54]
  theorem_status: "PROVED_ON_PAGE_SELF_CHECKED_UNAUDITED"
  source_status: PARTIAL
  p26_audit: missing
  second_other_track_audit: missing
  finite_core: none
  checker: not_applicable
  prior_art_status: "fresh bounded search; no exact later resolution found; novelty UNVERIFIED"
  canonical_claim_status: "PENDING_ADMISSION, not READY (preserved)"
  next_frontier: "zero-Lebesgue-time pinning sets above the Brownian level-set dimension/capacity threshold"
```

## 14. Result of the three Section-B moves

- **#2 ATTACK THE NEGATION FIRST — success as falsification:** an uncountable perfect recurrent pinch set of zero time measure does not force continuous-path rigidity; `h(u)=dist(u,Z)` is an exact selector counterexample to that proposed route.
- **#1 CHANGE THE CATEGORY — success:** recasting the witness segment through its occupation measure removes all dependence on off-pinning geometry and yields T53.
- **#24 FIND THE EXTREMAL OBJECT — success:** T53 already kills the maximal curtain that allows all of `R` away from the pinning set; every narrower shape inherits the obstruction, and T54 supplies a closed, ballistic-width representative.

**Metric exit:** `43 -> 44`. **Unchanged count:** `0`. **Problem 7.8:** `PARTIAL`. **Closure audits for T53/T54:** `0/2`.