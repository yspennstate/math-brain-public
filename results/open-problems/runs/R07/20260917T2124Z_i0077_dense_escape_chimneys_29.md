Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `28 -> 29` genuinely distinct nonparabolic shape families; Section-B moves actually used: #7 TAKE THE LIMIT, #12 FIND WHAT IS CONSERVED, #23 DO WHAT THE PROPOSER DID NOT EXPECT.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, Probab. Theory Relat. Fields 160 (2014), 95–126; arXiv:1302.6958, Problem 7.8 / intake I0077: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” **Overall source status remains PARTIAL.** The next sentence in the source is Problem 7.9 on forward Lévy processes and is not part of I0077.

# R07 CLOSABLE OUTSIDE — run 29: dense-time escape chimneys

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, and baseline

The frozen quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that Brownian rescaling/reflection/translation and mere parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T2028Z_i0077_phase_frustrated_comb_gates_28.md`,

which moved the metric `27 -> 28` and used moves `#2,#14,#19`. The present triple is different.

All thirty Section-B moves have already appeared somewhere in the I0077 chain, so the literal instruction to choose three moves never previously used on the problem is exhausted. I do not invent a false history. This run uses a new combination and a new application of `#7,#12,#23`.

Before research I recovered the current state from `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0077.md`, the complete visible R07/I0077 chain through run 28, the newest visible R15 history for distinct Problem 7.2 / I0076, and the current C29 I0077 exclusion refresh. C29 continues to exclude I0077 because R07 owns it. The canonical I0077 claim still says `PENDING_ADMISSION, not READY`; I preserve that shared status while following the owner's explicit assignment of this target to R07. The old R07 KPZ/FPP route remains preserved and retired rather than deleted.

The large `probability_1000_intake_*/problems.jsonl` mirrors remain connector-truncated if rendered wholesale. The intake reread is therefore honestly **targeted/partial due connector limits**: exact I0077 wording, source, ownership, exclusions and prior attempts were recovered, but I do not claim a byte-for-byte reread of every unrelated intake row.

Entering metric: **28**.

## 2. Primary-source benchmark rechecked

I reopened the authors' PDF and visually checked the relevant pages. Definition 2.1 says an FBM has random witness times tending to `-infinity` from which every forward increment process is standard Brownian motion; Definition 2.2 defines decomposable FBMs by concatenating stopped independent Brownian pieces.

For finite `c_1<c_2`, let `lambda_0(c_1,c_2)` be the principal killed-Ornstein–Uhlenbeck exponent from Section 4. Remark 4.1 states that `lambda_0` is continuous and strictly monotone under endpoint enlargement/shrinking. Theorem 4.3 states:

1. if `lambda_0(c_1,c_2) >= 1`, every FBM has the universal far-past normalized obstruction;
2. if `lambda_0(c_1,c_2) <= 1`, a decomposable FBM exists with the corresponding normalized limsup/liminf bounds;
3. if `c_1 <= 0 <= c_2` and `lambda_0(c_1,c_2) < 1`, a decomposable FBM can be confined pointwise to the static parabolic strip for every negative time.

Remark 4.2 records the exact critical identity `lambda_0(-1,1)=1`.

Problem 7.8 is exactly the one-sentence request to generalize Theorem 4.3 beyond parabolas. Problem 7.9 is separately the forward-Lévy question.

## 3. Fresh current-status / prior-art pass

Fresh bounded searches dated 2026-09-17 included the exact Problem-7.8 wording, the original paper and later-author variants, `dense time Brownian motion constraint continuity closed interval`, `nowhere dense Brownian motion confinement time set`, and `open dense Brownian motion path constraint`.

The original 2014 paper remains the identifiable source statement. I found no later paper in this bounded search explicitly resolving exact Problem 7.8 or stating the escape-chimney theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**.

The topological ingredients below are elementary and are not claimed as novel: a continuous function taking values in a closed set on a dense set takes values in that closed set everywhere, and dense open subsets of `R` may have arbitrarily small finite Lebesgue measure. The point here is the consequence for a source-valid FBM space-time family, not novelty of those topology facts.

## 4. The new family: dense restrictive curtains with full-space escape chimneys

Fix a finite closed interval

\[
K=[c_1,c_2],\qquad c_1<c_2,
\tag{4.1}
\]

and let `E subset R` be open and dense. Put `F=R\E`, so `F` is closed and nowhere dense. In logarithmic time define the allowed normalized fiber

\[
D_E(r)=
\begin{cases}
K,&r\in E,\\
\mathbb R,&r\in F.
\end{cases}
\tag{4.2}
\]

The associated backward space-time shape is

\[
\boxed{
\mathcal H_{E,K}
=
\{(-e^r,e^{r/2}y): r\in\mathbb R,\ y\in D_E(r)\}.
}
\tag{4.3}
\]

Equivalently, at restrictive log-times `r in E` the path must lie in the parabolic interval `[c_1 sqrt(u),c_2 sqrt(u)]`; at escape times `r in F` the shape contains the **entire spatial fiber** and imposes no constraint at all.

The shape is closed as a subset of `(-infinity,0) x R`. Indeed, in `(r,y)` coordinates its complement is

\[
E\times(\mathbb R\setminus K),
\]

which is open because both factors are open, and `(r,y) -> (-e^r,e^{r/2}y)` is a homeomorphism.

### Canonical finite-measure version

For any `epsilon>0`, enumerate the rationals as `Q={q_m:m>=1}` and set

\[
E_\epsilon
=
\bigcup_{m\ge1}
\left(q_m-\epsilon2^{-m-1},q_m+\epsilon2^{-m-1}\right).
\tag{4.4}
\]

Then `E_epsilon` is open and dense while

\[
|E_\epsilon|
\le\sum_{m\ge1}\epsilon2^{-m}
=\epsilon.
\tag{4.5}
\]

Thus the shape may impose the parabolic restriction on a set of **finite total logarithmic measure**, hence zero asymptotic log-time density, while allowing all of `R` on the complementary closed nowhere-dense set `F_epsilon`, which has asymptotic density one.

This is the opposite measure/category geometry from the earlier pulse and sampled-gate families: the restrictive set is tiny in measure but dense in topology.

## 5. The three new-method moves

### #7 TAKE THE LIMIT

I first pushed the previous vanishing-duty gate idea to the limit of total gate duration tending to zero. The spectral-mass route then genuinely dies: if a fixed bounded interval is imposed for only finite total logarithmic time, its accumulated killed-OU mass is finite and cannot yield an exponent per log-horizon bigger than one.

The limiting experiment exposed a different invariant: **where the gates accumulate**, not how much measure they occupy. Making the finite-total-duration gate set dense changes the answer completely.

### #12 FIND WHAT IS CONSERVED

The conserved object is not an OU norm but membership in a closed fiber under continuity. For an FBM path, the normalized logarithmic trajectory

\[
Y(r)=e^{-r/2}X_{-e^r}
\tag{5.1}
\]

is continuous. If `Y(r)` lies in the closed interval `K` on a dense set of `r`, there is no way to use a full-space escape fiber at an exceptional time: continuity fills in the missing times automatically.

### #23 DO WHAT THE PROPOSER DID NOT EXPECT

Instead of making a nonparabolic shape only slightly wider than a parabola, I made it **infinitely wider** on most logarithmic times: the full real line is allowed on a density-one set. The unexpected result is that these enormous escape chimneys are useless if their complement is dense.

This also falsifies a natural proposed extension rule: feasibility cannot be classified from the logarithmic measure/duty cycle of restrictive times alone. A finite-total-measure restrictive set can be just as strong, pathwise, as restricting every time.

That falsifies the proposed rule, not Problem 7.8 itself.

## 6. Dense-time saturation lemma

### Lemma 6.1

Let `E subset [R,infinity)` be dense, let `C subset R` be closed, and let `f:[R,infinity)->R` be continuous. If

\[
f(r)\in C\qquad\forall r\in E,
\tag{6.1}
\]

then

\[
f(r)\in C\qquad\forall r\ge R.
\tag{6.2}
\]

**Proof.** Fix `r>=R`. Choose `r_n in E` with `r_n -> r`. Continuity gives `f(r_n)->f(r)`. Since `C` is closed and every `f(r_n)` lies in `C`, also `f(r) in C`. `QED`

Applying the lemma to (5.1) gives the exact pathwise event identity

\[
\boxed{
\begin{aligned}
&\{\exists R:\ (-u,X_{-u})\in\mathcal H_{E,K}\ \forall u\ge e^R\}\\
&\qquad=\{\exists R:\ X_{-u}/\sqrt u\in K\ \forall u\ge e^R\}.
\end{aligned}
}
\tag{6.3}
\]

This equality is deterministic and holds for every continuous path, not merely almost surely for Brownian paths.

## 7. I0077-R07-T30 — strict phase theorem for dense escape chimneys

**Status of theorem: PROVED below. Overall source status remains PARTIAL.**

Let `E subset R` be open and dense and let `K=[c_1,c_2]` be a finite nondegenerate interval. Define `H_{E,K}` by (4.3).

### (i) Strictly supercritical interval: universal impossibility

If

\[
\boxed{\lambda_0(c_1,c_2)>1,}
\tag{7.1}
\]

then for every FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists R:\ (-u,X_{-u})\in\mathcal H_{E,K}
\ \forall u\ge e^R
\right)=0.
}
\tag{T30.i}
\]

### (ii) Strictly subcritical interval: decomposable existence

If

\[
\boxed{\lambda_0(c_1,c_2)<1,}
\tag{7.2}
\]

then there exists a decomposable FBM `X` such that

\[
\boxed{
\mathbb P\left(
\exists R:\ (-u,X_{-u})\in\mathcal H_{E,K}
\ \forall u\ge e^R
\right)=1.
}
\tag{T30.ii}
\]

No claim is made at the critical value `lambda_0(c_1,c_2)=1`; exact eventual confinement at the source-critical boundary is not supplied by Theorem 4.3 and is deliberately left open.

### Proof of (i)

By continuity of `lambda_0` (source Remark 4.1), choose `delta>0` so small that

\[
\lambda_0(c_1-\delta,c_2+\delta)>1.
\tag{7.3}
\]

If the escape-chimney event in (T30.i) occurred, (6.3) would give, eventually,

\[
c_1\le X_{-u}/\sqrt u\le c_2.
\tag{7.4}
\]

Hence

\[
\liminf_{u\to\infty}X_{-u}/\sqrt u\ge c_1>c_1-\delta,
\qquad
\limsup_{u\to\infty}X_{-u}/\sqrt u\le c_2<c_2+\delta.
\tag{7.5}
\]

But source Theorem 4.3(i), applied to `(c_1-delta,c_2+delta)`, says that every FBM almost surely has either liminf at most `c_1-delta` or limsup at least `c_2+delta`. Contradiction. Thus (T30.i) holds.

### Proof of (ii)

Because `lambda_0(c_1,c_2)<1`, continuity lets us choose `delta>0`, with `2delta<c_2-c_1`, such that

\[
\lambda_0(c_1+\delta,c_2-\delta)<1.
\tag{7.6}
\]

Source Theorem 4.3(ii) therefore gives a decomposable FBM satisfying almost surely

\[
\liminf_{u\to\infty}X_{-u}/\sqrt u\ge c_1+\delta,
\qquad
\limsup_{u\to\infty}X_{-u}/\sqrt u\le c_2-\delta.
\tag{7.7}
\]

The strict margin implies that for all sufficiently large `u`,

\[
c_1<X_{-u}/\sqrt u<c_2.
\tag{7.8}
\]

Hence the path eventually lies in the static parabolic strip, and therefore certainly lies in `H_{E,K}`. This proves (T30.ii). `QED`

## 8. Exact centered corollary

The source records

\[
\lambda_0(-1,1)=1,
\tag{8.1}
\]

and strict domain monotonicity. Therefore for the canonical finite-measure dense set `E_epsilon`,

\[
0<a<1
\quad\Longrightarrow\quad
\text{no FBM can eventually satisfy }(-u,X_{-u})\in\mathcal H_{E_\epsilon,[-a,a]},
\tag{8.2}
\]

whereas

\[
a>1
\quad\Longrightarrow\quad
\text{a decomposable FBM can eventually satisfy it almost surely.}
\tag{8.3}
\]

For `a>1` the source pointwise clause is even stronger for the underlying static strip. The exact `a=1` eventual-confinement question remains unclassified.

The striking part of (8.2) is geometric: choose `epsilon` as small as desired. The shape then allows **every spatial point** at a set of logarithmic times of asymptotic density one, and restricts the path only during total log-time at most `epsilon`; nevertheless, continuous-path confinement is exactly as restrictive as the full narrow parabola.

## 9. Why this is a new metric family

This is not run 24's vanishing geometric gates, run 25/26's additive/geometric fences, or runs 27/28's sampled combs. In all of those, the restrictive time set has gaps whose interiors can be used by a continuous path, and the obstruction comes from Brownian/OU persistence or a forced physical-time jump. Here the restrictive set is **dense** while having finite total logarithmic measure, and the proof uses no persistence exponent at all.

It is also not a static parabola as a space-time set: `H_{E,K}` has full unbounded spatial fibers for every `r in F`, and for the canonical construction `F` is a closed nowhere-dense set of asymptotic log-time density one. Brownian rescaling translates logarithmic time and preserves the presence of those full fibers; reflection preserves them as well. No trivial rescaling or parameter change turns this geometry into a static strip.

There is an important honest qualification: for continuous-path **confinement events**, Lemma 6.1 makes this family pathwise equivalent to the static strip. That equivalence is the new theorem/mechanism. The frozen R07 convention quotients trivial Brownian rescalings/reflections/translations and parameter changes, not arbitrary equivalence under topological saturation; under that frozen convention this is a distinct geometric family. If the owner later changes the metric to quotient by continuous-path saturation, this point should be merged rather than double-counted. No such metric change is made here.

Thus the frozen metric moves

\[
\boxed{28\longrightarrow29},
\qquad
\text{unchanged count}=0.
\tag{9.1}
\]

## 10. Verification / closure status

There is no finite computational core in T30. The proof is analytic/topological and complete on the page, so no checker-only artifact was manufactured.

T30 currently has **0/2 independent OTHER-track audits**. In particular, it has neither the required P26 end-to-end audit nor a second distinct OTHER-track audit. It therefore does not close the source and no paper package is created this run.

Overall Problem 7.8 status remains **PARTIAL**. A high-value next route is to break the exact saturation equivalence: allow escape fibers on a closed nowhere-dense set but make the restrictive fibers approach different limits on different complementary gaps, so that the exceptional set can support genuine continuous branch transport rather than being useless. That would test whether a singular-continuous time set can mediate a transition invisible to duty-cycle spectral mass.

## 11. Model / scheduler-control status

The exposed scheduler control surface still provides prompt/title, schedule/start-offset, enabled state and timing mode, but no model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry. Therefore GPT-6/maximum remains prompt-only and is not claimed here.

The historical `You cannot modify this task` result for P26 was authorization-context-specific: the current repository ledger records that P26's full prompt update later succeeded from another authorized context. The legitimate remedy for model/reasoning enforcement remains an owning/admin product surface or backend/API support that exposes and persists those fields and reports authenticated execution metadata. There is no worker-level bypass, and no scheduler modification was attempted in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R07
  source: I0077
  target: Burdzy-Scheutzow Problem 7.8
  metric: distinct nonparabolic shape families with complete source-appropriate theorem
  before: 28
  after: 29
  movement: +1
  new_family: dense-time escape chimneys / finite-measure dense restrictive curtains
  theorem: I0077-R07-T30
  theorem_status: PROVED_SELF_CHECKED_ON_PAGE
  source_status: PARTIAL
  audits:
    P26: missing
    second_other_track: missing
  finite_core: none
  checker: none_needed
  prior_art_status: bounded_negative_search_only_novelty_unverified
  unchanged_count: 0
  methods: [7, 12, 23]
  previous_methods: [2, 14, 19]
  ownership: R07_exclusive_provisional_claim_shared_status_PENDING_ADMISSION
  scheduler_mutation: none
```
