Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `24 -> 25` genuinely distinct nonparabolic shape families; Section-B moves actually tried: #10 DERANDOMIZE, #26 HUNT THE SPORADIC CASE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

Problem/source: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion* (PTRF 160 (2014), 95–126; arXiv:1302.6958v4), Problem 7.8: “Can one generalize Theorem 4.3 from parabolas to other space-time shapes?” Intake I0077. **Overall source status remains PARTIAL; the source's open-ended request is not claimed closed.**

# R07 CLOSABLE OUTSIDE — run 25: additive-time alternating one-sided parabolic fences

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler changes.

## 1. Continuity, admission, ownership, exclusions, and baseline

The frozen R07 quantity remains

> the number of genuinely distinct nonparabolic space-time shape families for which R07 has a complete source-appropriate theorem, modulo the frozen convention that trivial Brownian rescaling/reflection and parameter changes inside one structural family do not create new metric points.

The preceding authoritative own report is

`runs/R07/20260917T1622Z_i0077_vanishing_gate_fences_24.md`,

which moved the metric `23 -> 24` and used Section-B moves `#1,#8,#17`. The present triple is different.

At this point the R07 I0077 chain has already used **all thirty** Section-B moves at least once. Thus the literal instruction “pick three never tried on this problem” is exhausted and cannot be satisfied without inventing history. This run therefore uses a new combination and a genuinely new application of `#10,#26,#30`, none of which is the immediately preceding triple.

Before new mathematics I recovered/rechecked current `master`, including campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, canonical claim `operations/claims/I0077.md`, the complete R07 directory through run 24, the newest visible R06 and R15 states, and targeted intake/ownership searches. The old R07 KPZ/FPP reports remain preserved and retired rather than deleted. R15's old Problem 7.2/I0076 track remains a distinct retired handoff and has rotated elsewhere; it is not this source. `INDEX.md`/`RANKING.md` settle Problem 7.5, not 7.8. `POSTED.md` contains no 7.8 exclusion. The canonical I0077 claim still names R07 as owner and still literally says `PENDING_ADMISSION, not READY`; the current owner task explicitly assigns I0077 to R07, so I continue the already-established chain rather than pretending the stale queue/status field newly admitted it.

The entering metric is therefore `24`.

## 2. Source benchmark rechecked

Definition 2.1 of the source says that an FBM `X` has witness times `S_j -> -infinity` such that, for every fixed witness index `j`,

\[
W_j(t)=X_{S_j+t}-X_{S_j},\qquad t\ge0,
\]

is standard Brownian motion. Definition 2.2 defines decomposable FBMs by concatenating independent Brownian pieces; the i.i.d. version is strongly decomposable.

Theorem 4.3 gives the parabolic benchmark in terms of the principal killed-OU exponent `lambda_0(c_1,c_2)`: supercritical/critical universal far-past obstruction, subcritical/critical decomposable asymptotic existence, and strict-subcritical pointwise existence when the interval straddles zero.

The source also proves the particularly useful Proposition 4.4: for every `epsilon>0`, there exists a **strongly decomposable** FBM with

\[
\inf_{t<0}\frac{X_t}{\sqrt{|t|}}\ge1-\epsilon\quad\text{a.s.}
\tag{2.1}
\]

By reflection there is the analogous process below `-(1-epsilon)sqrt(|t|)`.

Problem 7.8 is exactly the one-line request to generalize Theorem 4.3 from parabolas to other space-time shapes. The following forward-Levy-process request is Problem 7.9 and is not part of this assignment.

## 3. Fresh prior-art/status pass — 2026-09-17

Fresh bounded searches covered exact `Forward Brownian Motion` / Problem 7.8 queries, Brownian alternating/square-root boundary queries, discrete-time square-root barriers, and later square-root-boundary first-passage literature. The nearest explicit literature found remains ordinary-Brownian boundary crossing: Sato's 1977 square-root-boundary first-passage paper and Denisov--Hinrichs--Sakhanenko--Wachtel (2022) on asymptotically square-root boundaries. Those works are relevant prior art for ordinary Brownian first passage, not evidence that the FBM source question has been resolved.

I did not find in this bounded dated search a later paper explicitly resolving exact Burdzy--Scheutzow Problem 7.8 or stating the additive alternating-FBM theorem below. This is **negative bounded evidence only; publication novelty remains UNVERIFIED**. The Brownian modulus estimates used below are classical/folklore and are not claimed as novel.

## 4. New shape family: additive-time one-sided parabolic fences

Fix `a in (0,1)` and a sign sequence

\[
\sigma=(\sigma_n)_{n\ge1},\qquad \sigma_n\in\{-1,+1\}.
\]

At negative integer time `-n`, impose the one-sided parabolic fence

\[
\boxed{\sigma_n X_{-n}\ge a\sqrt n.}
\tag{4.1}
\]

Equivalently, the normalized cross-section at the `n`th fence is the right half-line `[a,infinity)` when `sigma_n=+1` and the left half-line `(-infinity,-a]` when `sigma_n=-1`; away from the fence times the discrete version imposes no constraint.

Call an index `n` a **switch** when

\[
\sigma_{n+1}=-\sigma_n.
\tag{4.2}
\]

The decisive geometric feature is now physical/additive time: consecutive relevant scales satisfy

\[
\frac{n+1}{n}\to1,
\tag{4.3}
\]

rather than the fixed ratio `e^P>1` of run 24's geometric fences.

## 5. Methods #10, #26, #30

### #10 DERANDOMIZE

I first considered an i.i.d. Bernoulli sign environment. The useful observation was not a quenched persistence exponent: every local sign switch itself forces a macroscopic displacement over one unit of Brownian time. Randomness is unnecessary. The route derandomizes completely to deterministic sign sequences whose switch set has bounded gaps, and in particular to every nonconstant eventually periodic word.

### #26 HUNT THE SPORADIC CASE

The same observation exposes the proof boundary. If switches become so sparse that a large interval `[T/3,2T/3]` can contain no switch, the argument below no longer forces a macroscopic unit increment at a scale comparable with the FBM witness terminal `T`. Thus rare, multiplicatively lacunary switches are a genuinely different unresolved regime, not something this run silently classifies.

### #30 ONE SCALE / ONE DIRECTION AT A TIME

Instead of using killed-OU survival over a whole tail, localize to one adjacent pair `n,n+1` at a switch. The two one-sided constraints force

\[
|X_{-(n+1)}-X_{-n}|\ge a(\sqrt{n+1}+\sqrt n),
\tag{5.1}
\]

which is order `sqrt(n)` over a physical time interval of length exactly one. Standard Brownian motion cannot have such unit increments at scales comparable with its terminal time infinitely often. This closes the bounded-gap switching case with a pathwise Brownian-modulus argument and no OU spectral calculation.

## 6. Brownian lemma: maximal unit increment is `o(sqrt(T))`

Let `B` be standard Brownian motion and define

\[
M(T):=\sup\{|B_{s+1}-B_s|:0\le s\le T\}.
\tag{6.1}
\]

### Lemma 6.1

Almost surely,

\[
\boxed{\frac{M(T)}{\sqrt T}\longrightarrow0\qquad(T\to\infty).}
\tag{6.2}
\]

### Proof

For integer `N>=1`, if `s in [k,k+1]` then

\[
|B_{s+1}-B_s|
\le2\sup_{0\le u\le2}|B_{k+u}-B_k|.
\]

By a union bound, stationarity of increments, the reflection principle, and the elementary Gaussian Chernoff bound,

\[
\mathbb P\{M(N)>x\}
\le4(N+1)e^{-x^2/16}.
\tag{6.3}
\]

For fixed `eta>0`, setting `x=eta sqrt(N)` makes the right-hand side summable in `N`. Borel--Cantelli gives `M(N)/sqrt(N)<=eta` eventually. Apply this to a countable sequence `eta downarrow 0`; monotonicity of `M` extends the conclusion from integer to real `T`. `square`

In particular, for every `c>0`, if

\[
G_A(c)=\{\exists T\ge A:M(T)\ge c\sqrt T\},
\tag{6.4}
\]

then

\[
\boxed{\mathbb P(G_A(c))\to0\quad(A\to\infty).}
\tag{6.5}
\]

## 7. Theorem I0077-R07-T26 — bounded-gap switching obstruction and periodic classification

Fix `a in (0,1)`.

### T26(i): bounded-gap switching is universally impossible

Assume there are `L<infinity` and `N_sigma` such that every integer interval `[m,m+L]` with `m>=N_sigma` contains a switch index. Then for **every** FBM `X`,

\[
\boxed{
\mathbb P\left(
\exists N:\ \sigma_n X_{-n}\ge a\sqrt n\quad\forall n\ge N
\right)=0.
}
\tag{T26.i}
\]

### T26(ii): exact classification of eventually periodic words in the subcritical one-sided regime

Suppose `sigma` is eventually periodic. Then:

- if the eventual periodic word is nonconstant, no FBM satisfies the fences eventually;
- if the eventual periodic word is constant, there exists a **strongly decomposable** FBM satisfying the eventual fences (indeed the corresponding one-sided inequality holds for every negative time).

Hence, for every fixed `0<a<1`,

\[
\boxed{
\text{eventual periodic fence is FBM-feasible}
\iff
\text{its tail word is constant}.
}
\tag{T26.ii}
\]

The word “feasible” on the left means existence of an FBM; in the positive case the construction is strongly decomposable.

## 8. Proof of T26(i): force a macroscopic unit increment inside one Brownian witness

Assume contrariwise that

\[
E:=\left\{\exists N:\sigma_nX_{-n}\ge a\sqrt n\ \forall n\ge N\right\}
\tag{8.1}
\]

has positive probability. Since `E` is a countable union, some deterministic `N_0` has

\[
q:=\mathbb P(E_{N_0})>0,
\qquad
E_{N_0}:=\{\sigma_nX_{-n}\ge a\sqrt n\ \forall n\ge N_0\}.
\tag{8.2}
\]

Let `S_j -> -infinity` be any FBM witness sequence and put

\[
T_j=-S_j,
\qquad
W_j(t)=X_{S_j+t}-X_{S_j},\quad t\ge0.
\tag{8.3}
\]

For every deterministic `j`, `W_j` is standard Brownian motion.

Choose `A` so large that

1. `[T/3,2T/3-1]` contains a switch beyond `N_0 vee N_sigma` whenever `T>=A`; this is possible from the bounded-gap hypothesis;
2. with
   \[
   c_a:=\frac{2a}{\sqrt3},
   \tag{8.4}
   \]
   the Brownian event `G_A(c_a)` from (6.4) has probability `<q/2`.

Because `T_j -> infinity` along the witness sequence almost surely, choose a **deterministic witness index** `j` such that

\[
\mathbb P(T_j<A)<q/4.
\tag{8.5}
\]

On `E_{N_0} cap {T_j>=A}`, choose a switch `n` with

\[
T_j/3\le n\le2T_j/3-1.
\tag{8.6}
\]

At a switch, the two fence inequalities point in opposite directions. Therefore

\[
|X_{-n}-X_{-(n+1)}|
\ge a(\sqrt n+\sqrt{n+1})
\ge\frac{2a}{\sqrt3}\sqrt{T_j}
=c_a\sqrt{T_j}.
\tag{8.7}
\]

But from (8.3),

\[
W_j(T_j-n)=X_{-n}-X_{S_j},
\qquad
W_j(T_j-n-1)=X_{-(n+1)}-X_{S_j},
\tag{8.8}
\]

and both arguments lie in `[0,T_j]`. Thus (8.7) implies

\[
M_{W_j}(T_j)\ge c_a\sqrt{T_j},
\]

so the entire Brownian path `W_j` lies in the path-only event `G_A(c_a)`.

Consequently

\[
\begin{aligned}
\mathbb P(G_A(c_a;W_j))
&\ge\mathbb P(E_{N_0}\cap\{T_j\ge A\})\\
&\ge q-\mathbb P(T_j<A)\\
&>3q/4,
\end{aligned}
\tag{8.9}
\]

whereas `W_j` has the law of standard Brownian motion and hence, by the choice of `A`, the left-hand side is `<q/2`. Contradiction.

The argument never conditions on the random terminal time `T_j` and never assumes independence between `T_j` and the Brownian witness path. It uses only that the event `G_A(c_a)` is a property of the entire standard Brownian path. This proves T26(i). `square`

## 9. Proof of T26(ii): constant tail versus switching tail

If an eventually periodic `sigma` is nonconstant, its periodic tail has at least one adjacent sign transition per period (including the wrap transition), so the switch set has bounded gaps. T26(i) applies.

If the eventual tail is `sigma_n=+1`, choose `epsilon>0` with

\[
1-\epsilon>a.
\]

Source Proposition 4.4 gives a strongly decomposable FBM with

\[
X_t\ge(1-\epsilon)\sqrt{|t|}>a\sqrt{|t|}\qquad\forall t<0
\tag{9.1}
\]

a.s.; therefore all sufficiently large positive-orientation fences hold. If the eventual tail is `-1`, reflect that process. This proves T26(ii). `square`

## 10. Canonical alternating example and the falsified naive extension

Take

\[
a=\frac12,
\qquad
\sigma_n=(-1)^n.
\tag{10.1}
\]

The required fences alternate:

\[
X_{-2k}\ge\frac12\sqrt{2k},
\qquad
X_{-(2k+1)}\le-\frac12\sqrt{2k+1}
\tag{10.2}
\]

for all sufficiently large `k` (up to the harmless choice of parity convention). T26 gives

\[
\boxed{
\mathbb P(\text{eventual alternating confinement})=0
\quad\text{for every FBM}.}
\tag{10.3}
\]

Yet each frozen orientation is source-admissible in the strongest possible sense: Proposition 4.4 gives a strongly decomposable FBM above `(1/2)sqrt(|t|)` for **all** negative times, and reflection gives one below `-(1/2)sqrt(|t|)` for all negative times.

Thus the proposed extension rule

> “if every individual one-sided parabolic gate is source-subcritical/admissible, then an FBM can eventually satisfy the moving collection of gates”

is false. This falsifies the proposed rule, **not** Problem 7.8 itself.

## 11. Positive-width / continuous-endpoint thickening

The discrete fence can be thickened without changing the theorem. Choose `0<delta<1/4` and

\[
\phi(z)=\frac{z^2}{1-z^2},\qquad |z|<1.
\tag{11.1}
\]

For `u=|t|` inside the disjoint window `|u-n|<delta`, define the allowed cross-section by

\[
D_u=
\begin{cases}
[(a-\phi((u-n)/\delta))\sqrt u,\infty),&\sigma_n=+1,\\
(-\infty,(-a+\phi((u-n)/\delta))\sqrt u],&\sigma_n=-1,
\end{cases}
\tag{11.2}
\]

and put `D_u=R` outside the gate windows. In the extended-real endpoint topology the boundary opens continuously to all of `R` at the window edges; at the center `u=n` it is exactly the fence (4.1).

Any FBM eventually confined in this thickened shape satisfies the center fences, so T26(i) gives the same obstruction. If the tail sign is constant, the Proposition-4.4 process from (9.1) lies in every positive-orientation gate because its lower bound exceeds `a sqrt(u)` and the gate threshold is at most `a sqrt(u)`; reflection handles the negative tail. Thus T26(ii)'s periodic classification holds for this positive-width space-time family as well.

This thickening is included in the same metric point, not counted again.

## 12. Why this is a new metric family rather than another parameter of T25 or earlier families

The frozen equivalence convention excludes mere rescalings and parameter changes. T26 survives that check for several structural reasons.

1. **Additive versus multiplicative scales.** Here fence centers are `u_n=n` and `u_{n+1}/u_n -> 1`; run 24 uses `u_k=e^{kP}` with fixed ratio `e^P>1`. Brownian rescaling sends the additive lattice to another additive lattice and preserves the ratio-limit invariant.
2. **Linear versus logarithmic gate count.** There are `Theta(T)` additive gates up to physical scale `T`, versus `Theta(log T)` geometric fences in T25.
3. **Unbounded alternating half-lines versus bounded centered windows.** T25 constrains to `[-a,a]`; T26 alternates between opposite unbounded half-lines.
4. **New obstruction mechanism.** T25 uses sampled-OU persistence over many multiplicative scales. T26 needs only one adjacent switch and the Brownian unit-increment modulus: a forced displacement of order `sqrt(T)` in time one.
5. The log-periodic one-sided-barrier family has one orientation and continuous/logarithmic evolution; the branch-swapping exterior family offers both exterior branches simultaneously and continuity conserves a branch. T26 externally forces the **only** allowed branch to alternate at additive scales.

Therefore this is a genuinely different shape family under the frozen convention, and the metric legitimately moves

\[
\boxed{24\longrightarrow25}.
\tag{12.1}
\]

## 13. Validation, audits, and status

There is no finite combinatorial/numerical core in T26: the proof is analytic/pathwise and all constants are symbolic. Under the owner's new-methods-first rule I did **not** manufacture a checker merely to create a certificate. The full theorem-sized argument is on this page.

No closure is claimed. T26 has **zero** independent OTHER-track end-to-end audits at this moment; it still needs the required P26 audit and a second distinct outside-track audit. A prior PASS on an earlier R07 theorem does not audit T26. Publication novelty is also UNVERIFIED.

Current R07/source status:

- fixed metric: `24 -> 25`;
- movement: `+1`;
- unchanged count: `0`;
- source verdict: `PARTIAL`;
- no paper folder created.

The strongest next mathematical question is the sporadic-switch regime identified by method #26: how sparse can the sign changes be while still forcing universal FBM obstruction? The present proof works whenever switches are bounded-gap (more generally, whenever every sufficiently large interval `[cT,CT]` with `0<c<C<1` contains a switch). Multiplicatively lacunary switch sets are not classified here.

## 14. Model/scheduler control — actual exposed limit

The requested `GPT-6 / maximum` setting is **not** authenticated by this run. The exposed task-control schema still offers title/prompt, schedule, enabled state, start-offset/timing controls, but no model-family selector and no reasoning-effort selector, and no authenticated completed-run model telemetry. Thus `GPT-6 / maximum` remains prompt text only.

Repository policy records historical `You cannot modify this task` responses for P26/P01/P03 in one authorization context, while the current fleet ledger records that P26 was subsequently updated successfully in another authorized context. The legitimate remedy for a denied task is therefore the owning/authorized account or workspace surface, or platform support exposing the missing fields—not a worker-level permission bypass or duplicate schedule. No scheduler modification was attempted in this run.

## 15. Structured ledger delta

```yaml
ledger_delta:
  track: R07
  lane: CLOSABLE_OUTSIDE
  source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.8 / I0077"
  claim_id: I0077-R07-T26
  metric_name: "number of genuinely distinct nonparabolic shape families with a complete source-appropriate theorem"
  metric_before: 24
  metric_after: 25
  movement: +1
  unchanged_count: 0
  status_before: PARTIAL
  status_after: PARTIAL
  new_family: "additive-time alternating one-sided parabolic fences; positive-width thickening included in same family"
  theorem_scope: "for each fixed 0<a<1, bounded-gap sign switching is impossible for every FBM; eventual periodic words are feasible iff eventually constant, with strongly decomposable existence in the constant case"
  methods: [10, 26, 30]
  finite_core: null
  self_check: "full pathwise proof on report page; no artificial finite checker"
  audits: []
  prior_art: "bounded dated search; ordinary Brownian square-root boundary literature found; exact Problem 7.8 resolution not located; novelty UNVERIFIED"
  source_verdict: PARTIAL
  remaining_obligation: "P26 end-to-end audit + second distinct OTHER-track audit for T26; sporadic/multiplicatively-lacunary switch regime unclassified"
```

Next recommended method combination, since all individual Section-B moves have already appeared somewhere in R07 and literal freshness is exhausted: `#11 DUALIZE`, `#22 READ THE FAILURES`, `#28 TYPICAL INSTEAD OF FOR ALL`, applied specifically to lacunary switch sets rather than another bounded-gap variant.
