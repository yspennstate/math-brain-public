Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `29 -> 30` genuinely distinct nonparabolic shape families; Section-B moves actually used: #2 ATTACK THE NEGATION FIRST, #15 BREAK THE SYMMETRY ON PURPOSE, #27 SWAP THE QUANTIFIERS.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The following source sentence is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 30: Cantor-parity one-sided shutters

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and baseline

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T2124Z_i0077_dense_escape_chimneys_29.md`,

which moved the metric `28 -> 29` and used moves `#7,#12,#23`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain. Thus the literal instruction to use three moves never previously used on the problem is exhausted; I do not invent a false history. This run uses a new combination and, more importantly, a new mathematical mechanism: a perfect nowhere-dense transition set separates positive-duration shutter gaps of two incompatible colors.

Before research I recovered current state from `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0077.md`, the complete visible R07/I0077 report chain through run 29, the current C29 I0077 exclusion/ownership refresh, and the newest neighboring R15 state. R15 has long since handed off distinct Burdzy–Scheutzow Problem 7.2 / I0076 and is now on other sources; it does not own I0077. C29 explicitly excludes I0077 because R07 owns it.

The canonical I0077 claim still says `PENDING_ADMISSION, not READY`; I preserve that shared status while following the owner's explicit direct assignment of this exact target to R07. `INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8, and `POSTED.md` does not list Problem 7.8 as settled or posted. The old R07 KPZ/FPP route remains preserved and retired by immutable handoff rather than deleted.

The large `probability_1000_intake_*/problems.jsonl` resources remain connector-truncated if rendered wholesale. The intake reread in this run is therefore honestly **targeted/partial because of connector limits**: the exact I0077 row, source statement, ownership, exclusions, and searchable prior attempts were recovered, but I do not claim a byte-for-byte reread of every unrelated intake row.

Entering metric: **29**.  
Entering unchanged count: **0**.

## 2. Primary-source benchmark rechecked

I reopened the authors' primary PDF and visually checked the relevant pages.

Definition 2.1 says an FBM has witness times `S_n -> -infinity` from which every forward increment process is standard Brownian motion. Definition 2.2 defines decomposable FBMs by concatenating independent stopped Brownian pieces.

For the principal killed-Ornstein–Uhlenbeck exponent `lambda_0(c_1,c_2)`, Theorem 4.3 states:

1. if `lambda_0(c_1,c_2) >= 1`, every FBM has the universal far-past normalized limsup/liminf obstruction;
2. if `lambda_0(c_1,c_2) <= 1`, a decomposable FBM exists with the corresponding normalized limsup/liminf bounds;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2) < 1`, a decomposable FBM can be confined pointwise to the static parabolic strip for every negative time.

Remark 4.1 records continuity and strict domain monotonicity of `lambda_0`, and the source records the critical centered identity `lambda_0(-1,1)=1`.

Proposition 4.4 gives an especially useful one-sided source construction: for every `epsilon>0` there is a **strongly decomposable** FBM satisfying

\[
\inf_{t<0}\frac{X_t}{\sqrt{|t|}}\ge 1-\epsilon
\qquad\text{a.s.}
\tag{2.1}
\]

Reflection gives the corresponding process below the negative half-line.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 beyond parabolas. Problem 7.9 is separately the forward-Lévy question.

## 3. Fresh current-status / prior-art pass

Fresh bounded searches on 2026-09-17 UTC included:

- the exact quoted wording of Problem 7.8;
- `Forward Brownian Motion Problem 7.8 Burdzy Scheutzow`;
- later/current `forward Brownian motion` papers and references;
- `forward Brownian motion Cantor boundary space-time shape`;
- `Brownian motion Cantor time constraints half-line continuous path`;
- `Ornstein Uhlenbeck Cantor time persistence`.

The original paper remains the identifiable source statement. I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the Cantor-parity shutter result below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

The deterministic topological ingredients used below are elementary and are not claimed as novel: the middle-thirds Cantor complement has generation-`m` gaps accumulating at its endpoints, and a continuous function has the same limit along every sequence approaching a point. The source-specific content is that each shutter color separately is realizable by a strongly decomposable FBM while their Cantor interlacing is impossible.

## 4. Negation first: can a perfect transition set rescue branch switching?

Run 29 showed that if one closed interval is imposed on a dense time set, full-space fibers on the complementary nowhere-dense set are useless: continuity simply saturates the interval constraint.

The natural escape from that mechanism is to let the exceptional perfect set act as a **transition set** between different constraints on different complementary gaps. I therefore attacked the optimistic extension first:

> Proposed extension rule: if two one-sided parabolic constraints are each individually realizable, then putting them on different open gaps while allowing the whole real line on a perfect transition set should let a continuous path switch between them.

The rule is false. The obstruction is not duty cycle, OU spectral mass, or a forced jump over a fixed physical-time interval. It is the **generation structure of the Cantor gaps**: opposite shutter colors can accumulate at the same transition point from arbitrarily small scales. Continuity then demands two incompatible one-sided limits simultaneously.

This failure is a refutation of the proposed extension rule, **not** a refutation of the source's open-ended Problem 7.8.

## 5. The new family: periodic Cantor-parity shutters

Let `C subset [0,1]` be the standard middle-thirds Cantor set. Its complement is the disjoint union of the open intervals removed during the Cantor construction. Call a gap a **generation `m` gap** if it is first removed at stage `m>=1`.

For a real parameter `a`, define two closed one-sided normalized fibers

\[
K_+(a)=[a,\infty),
\qquad
K_-(a)=(-\infty,-a].
\tag{5.1}
\]

For logarithmic time `r in R`, write `n=floor(r)` and `s=r-n in [0,1)`. Define

\[
D_a(r)=
\begin{cases}
K_+(a),&s\text{ lies in a generation-}m\text{ Cantor gap with }m\text{ odd},\\
K_-(a),&s\text{ lies in a generation-}m\text{ Cantor gap with }m\text{ even},\\
\mathbb R,&s\in C.
\end{cases}
\tag{5.2}
\]

At the integer endpoints we use the Cantor fiber `R` (both `0` and `1` are in `C`). The associated backward space-time shape is

\[
\boxed{
\mathcal S_a
=
\{(-e^r,e^{r/2}y):r\in\mathbb R,\ y\in D_a(r)\}.
}
\tag{5.3}
\]

This is a closed subset of `(-infinity,0) x R`: in `(r,y)` coordinates its complement is the union, over open Cantor gaps, of products of that open time gap with the open forbidden half-line. Brownian scaling translates `r`; it cannot remove the Cantor generation structure. Reflection exchanges the two colors but does not collapse them to the single-fiber family of run 29.

The restrictive time set is the open dense complement of a perfect nowhere-dense Cantor set. Unlike run 29, however, there is **no single closed fiber imposed densely everywhere**. On each positive-duration complementary gap only one of the two half-line shutters is active, and the full-space Cantor set is in principle available for continuous transport.

## 6. The three new-method moves

### #2 ATTACK THE NEGATION FIRST

I tried to make the full-space Cantor fibers serve as switching portals between two source-feasible one-sided parabolic regimes. The construction itself produced the counterexample: if opposite colors occur at gap generations accumulating at one Cantor point, continuity prevents the switch.

### #15 BREAK THE SYMMETRY ON PURPOSE

A single repeated fiber recreates run 29's saturation. I therefore broke that symmetry by assigning `K_+` to odd-generation gaps and `K_-` to even-generation gaps. The scale parity survives every rescaling and is the new obstruction.

### #27 SWAP THE QUANTIFIERS

The raw statement is

\[
\text{for every odd gap }G,\ y(G)\subset K_+,
\quad
\text{and for every even gap }H,\ y(H)\subset K_-.
\]

At a Cantor endpoint where gaps of both parities accumulate, continuity swaps this family of quantified conditions into the simultaneous point condition

\[
y(c)\in K_+\cap K_-.
\]

When the intersection is empty, the entire infinite collection collapses to a one-point contradiction.

## 7. Cantor endpoint lemma

For every `m>=1`, the leftmost generation-`m` gap of `C` is

\[
G_m=(3^{-m},2\,3^{-m}).
\tag{7.1}
\]

Hence there are odd-generation and even-generation gaps whose points converge to `0`.

### Lemma 7.1 — parity accumulation

Let `y:[0,1]->R` be continuous. Suppose

\[
y(s)\in K_+(a)
\quad\text{on every odd-generation gap},
\tag{7.2}
\]

and

\[
y(s)\in K_-(a)
\quad\text{on every even-generation gap}.
\tag{7.3}
\]

Then

\[
\boxed{y(0)\in K_+(a)\cap K_-(a).}
\tag{7.4}
\]

**Proof.** For each odd `m`, choose `s_m in G_m`. Then `s_m->0`, so continuity gives `y(s_m)->y(0)`. Since `K_+(a)` is closed, `y(0) in K_+(a)`. Repeating with even `m` and using closedness of `K_-(a)` gives `y(0) in K_-(a)`. QED.

Exactly the same argument applies at the left endpoint of every translated log-time block `[n,n+1]`.

A useful deterministic corollary is that a continuous path satisfying all shutters on one complete block exists **if and only if** `K_+(a) cap K_-(a)` is nonempty: necessity is Lemma 7.1, while sufficiency follows by taking any constant value in the intersection. Thus the topological part is sharp.

## 8. I0077-R07-T31 — Cantor-parity shutter theorem

**Status of theorem: PROVED below. Overall source status remains PARTIAL.**

Let `S_a` be the space-time shape (5.3).

### T31(i): separated shutters are impossible for every continuous path

If

\[
\boxed{a>0,}
\tag{8.1}
\]

then `K_+(a) cap K_-(a)=emptyset`, and therefore for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R:\ (-u,X_{-u})\in\mathcal S_a\ \forall u\ge e^R
\right)=0.
}
\tag{T31.i}
\]

In fact, the probability statement is stronger than necessary: **no continuous function at all** can be confined to `S_a` through even one complete logarithmic block.

### T31(ii): wide overlapping shutters admit a decomposable FBM

If

\[
\boxed{a<-1,}
\tag{8.2}
\]

put `A=-a>1`. Then

\[
K_+(a)\cap K_-(a)=[-A,A].
\tag{8.3}
\]

Since the source has `lambda_0(-1,1)=1` and strict domain monotonicity,

\[
\lambda_0(-A,A)<1.
\tag{8.4}
\]

Consequently Theorem 4.3(iii) supplies a decomposable FBM `X` satisfying

\[
\boxed{|X_t|\le A\sqrt{|t|}\qquad\forall t\le0}
\tag{8.5}
\]

almost surely. Therefore

\[
\boxed{
\mathbb P\left(
(-u,X_{-u})\in\mathcal S_a\ \forall u>0
\right)=1.
}
\tag{T31.ii}
\]

No claim is made for `-1<=a<=0`; in that regime the two shutters overlap but the common centered core is source-critical or supercritical, while the Cantor gaps allow excursions outside the core. A correct classification there would require new persistence information and is not smuggled into T31.

### Proof of T31(i)

Suppose a continuous path `X` were eventually confined. Its Lamperti-normalized logarithmic trajectory

\[
Y(r)=e^{-r/2}X_{-e^r}
\tag{8.6}
\]

is continuous. Choose any integer `n>R`. Restricted to `[n,n+1]`, the function `s -> Y(n+s)` satisfies the hypotheses of Lemma 7.1. Hence

\[
Y(n)\in[a,\infty)\cap(-\infty,-a].
\tag{8.7}
\]

For `a>0` the intersection is empty, a contradiction. This is deterministic, so it applies to every FBM without any witness-time or independence issue. QED.

### Proof of T31(ii)

For `a=-A<-1`, the static centered interval `[-A,A]` lies inside **both** shutter colors. By source Theorem 4.3(iii) and (8.4), choose a decomposable FBM with (8.5). At odd Cantor gaps its normalized value belongs to `[-A,A] subset [-A,infinity)=K_+(a)`; at even gaps it belongs to `[-A,A] subset (-infinity,A]=K_-(a)`; at Cantor times the whole real line is allowed. Thus the process lies in `S_a` for every negative time. QED.

## 9. Canonical sharp contrast: each color is source-feasible, the interlacing is not

Take

\[
\boxed{a=\frac12.}
\tag{9.1}
\]

If only the odd-generation positive shutters were retained, Proposition 4.4 with `epsilon=1/2` gives a strongly decomposable FBM satisfying the **stronger** condition

\[
X_t\ge\frac12\sqrt{|t|}\qquad\forall t<0.
\tag{9.2}
\]

If only the even-generation negative shutters were retained, reflection gives a strongly decomposable FBM satisfying

\[
X_t\le-\frac12\sqrt{|t|}\qquad\forall t<0.
\tag{9.3}
\]

Thus each color separately is feasible for every negative time, not merely on its assigned gaps. Nevertheless their Cantor-parity interlacing has **no continuous confined path at all**.

This gives a clean source-appropriate falsification of the proposed composability principle

\[
\boxed{
\text{separately feasible temporal colors}
\not\Rightarrow
\text{feasible interlacing, even with full-space transition fibers}.
}
\tag{9.4}
\]

Again, (9.4) refutes the proposed rule, not Problem 7.8.

For contrast, at `a=-2` the two distinct shutters are

\[
[-2,\infty),\qquad(-\infty,2],
\]

with common core `[-2,2]`. The source theorem gives a decomposable FBM confined to that core pointwise, so the same Cantor geometry is genuinely feasible in a wide regime. The new family is therefore not merely a pathological impossible set.

## 10. Why this is a new metric family rather than run 29 with another parameter

Run 29 had **one fixed bounded closed fiber** `K` on an open dense time set and the whole line on the complementary nowhere-dense set. Density alone made the escape fibers pathwise irrelevant: confinement was exactly equivalent to confinement in the static strip `K` at every time.

T31 has a different time-fiber topology:

1. complementary gaps have positive duration and carry **two different unbounded half-line fibers**;
2. neither shutter color is imposed densely inside the interior of a gap of the opposite color;
3. the perfect Cantor set is a genuine candidate transition set, rather than automatically useless by a single dense closed-fiber saturation argument;
4. impossibility comes from **opposite generation parities accumulating at a common Cantor point**, not from one restriction being dense everywhere;
5. the positive `a<-1` regime shows the same Cantor geometry can be followed by a decomposable FBM when the two shutters share a source-subcritical core.

Brownian rescaling, reflection, translation, or changing `a` cannot transform the single-fiber dense-curtain geometry of run 29 into this two-color generation-parity lamination. Under the frozen equivalence convention this is therefore one new structural family, not a parameter duplicate.

As in run 29, if a future owner were to replace the frozen convention by a much coarser equivalence relation that identifies arbitrary shapes after all continuous-path topological reductions, metric counts would have to be recomputed. No such convention is currently in force.

The frozen metric therefore moves

\[
\boxed{29\longrightarrow30},
\qquad
\text{unchanged count}=0.
\tag{10.1}
\]

## 11. Verification and closure status

There is no finite computational core in T31. The theorem is a deterministic continuity/Cantor argument plus direct invocation of primary-source Theorem 4.3 and Proposition 4.4. The full argument is on the page, so I did not manufacture a checker merely to generate a certificate.

T31 currently has **0/2 independent OTHER-track audits**. It has neither the required P26 end-to-end audit nor a second independent OTHER-track audit. Therefore T31 does not close the source, and no `paper_*` package is created this run.

Overall Problem 7.8 status remains **PARTIAL**. A high-value next route is the unresolved overlap strip `-1<a<=0`: the Cantor set forces the normalized path into the narrow common core at every Cantor time, while the complementary gaps permit one-sided excursions. The right object appears to be a **Cantor-time OU persistence operator** over one logarithmic period. A sharp spectral radius for that operator would produce a genuinely probabilistic phase transition between the deterministic separated-shutter obstruction and the broad-core source construction.

## 12. Model / scheduler-control status

The exposed task-control surface still provides prompt/title, schedule/start-offset, enabled state, and timing mode, but no model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry. Therefore GPT-6/maximum remains prompt-only and is not claimed here.

The historical `You cannot modify this task` result for P26 was authorization-context-specific; current repository evidence records that a full P26 prompt update later succeeded from another authorized context. The legitimate remedy for model/reasoning enforcement remains an owning/admin product surface or backend/API support that exposes and persists those fields and reports authenticated execution metadata. There is no worker-level bypass, and no scheduler modification was attempted in this run.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  source: I0077
  target: Burdzy-Scheutzow Problem 7.8
  metric: distinct nonparabolic shape families with complete source-appropriate theorem
  before: 29
  after: 30
  movement: +1
  new_family: periodic Cantor-parity one-sided shutters
  theorem: I0077-R07-T31
  theorem_status: PROVED_ON_PAGE_SELF_CHECKED
  source_status: PARTIAL
  independent_audits: 0/2
  unchanged_count: 0
  prior_art: bounded_negative_only_novelty_unverified
  finite_core: none
  next_obligation: Cantor-time OU persistence in the overlap regime -1<a<=0; or independent audits if closure packaging is prioritized later
```

## 14. Next-run methods

Because the full Section-B list has already been exhausted historically, I cannot honestly promise three globally unused numbers. The next run should use a different combination from `#2,#15,#27`, preferably:

- #5 ADD A PARAMETER AND DIFFERENTIATE — vary the overlap width and look for a Cantor-time spectral derivative;
- #11 DUALIZE — formulate the one-period constrained OU evolution as a positive operator / Dirichlet-form problem;
- #16 COMPUTE EVERY SMALL CASE — approximate finite Cantor stages first, but only build a checker if the spectral quantity itself moves.

Those moves target the actual unresolved probabilistic core rather than generating another receipt.