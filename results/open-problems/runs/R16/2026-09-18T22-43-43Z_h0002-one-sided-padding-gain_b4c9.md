Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the canonical frozen H0002 class, the previous concrete receipt `rho*(1-q0/32)=rho-2*alpha0` (with every fixed coefficient below `rho-alpha0` also proved) is improved to the explicit constant `g_pad = rho-alpha0 + (3/4)d0 > rho-alpha0`, where `d0=min{alpha0/2, kappa*(rho-alpha0)/(4*alpha0)}`. More generally every fixed coefficient below `rho-alpha0+d_*` is proved, with `d_*=min{alpha0, kappa*(rho-alpha0)/(alpha0-kappa)}` on every nonvacuous asymptotic H1-H2-H3 sequence. Section-B methods actually used: **#15 BREAK THE SYMMETRY ON PURPOSE, #24 FIND THE EXTREMAL OBJECT, #27 SWAP THE QUANTIFIERS**. All 30 catalogued moves had already been used on H0002, so this is an honest nonconsecutive reuse, not invented unused history.

# R16 — H0002: one-sided padding pushes the sprinkling theorem strictly past the H2 cutoff

## 1. Continuity, ownership, required reads, and source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural conditions under which, for `p >= (1+epsilon)/lambda(G)`, `G_p` contains a component of order `Omega(|G|)` with constant probability.

Before doing mathematics I reread/reconciled the required repository surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/H0002.md`, the newest own R16 report `runs/R16/2026-09-18T21-43-33Z_h0002-two-scale-harvesting-amplification_6c91.md`, and the newest recoverable neighboring same-source records. G0010 is at terminal HARD handoff and G0011 has a terminal handoff / pending-admission successor state; neither changes H0002 ownership.

A fresh bounded primary-source check in this run still finds CMW as arXiv:2608.19145v1, dated 19 Aug 2026, and no later source-matching resolution of Question 5.1. The source itself asks exactly for natural hypotheses forcing a linear giant at the `1/lambda(G)` scale and identifies localization of the spectral radius as a central obstruction. This is bounded-search evidence, not a worldwide novelty certificate.

Primary/current sources checked:

- https://arxiv.org/abs/2608.19145
- https://arxiv.org/abs/2508.03961
- https://arxiv.org/abs/2609.11189
- https://eccc.weizmann.ac.il/report/2026/188/

The native Beck--Fiala task title remains stale as an unresolved mathematical target. Bansal--Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` order directly for `t >= log^2 n` and give weaker polylogarithmic-loss bounds below that regime. More importantly, Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`, all `n`. Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlos proof with constant `36`. These are very recent primary-source baselines, not R16 discoveries. On their stated theorems the original Beck--Fiala square-root target is currently KNOWN, so R16 continues the admitted H0002 successor rather than reopening the obsolete `t>=log^2 n` gap.

I also searched the current literature for combinations of `large-set expansion`, `percolation`, `sprinkling`, `spectral radius`, and asymmetric/macroscopic cut conditions. The bounded search recovered standard large-set-expander sprinkling results and finite-expander percolation literature, but I did not locate the exact one-sided padding lemma below. That negative search does not establish novelty.

## 2. Frozen class and incoming theorem

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Put `n=|G|`, `lambda=lambda(G)`,

`a0 := 1-epsilon/8`,

`q0 := 1-exp(-epsilon^2/288)`,

`beta0 := q0/64`,

`alpha := alpha0 := rho*beta0`.

The frozen graph class is unchanged:

1. **H1 (spectral deletion resilience):** `lambda(G-S) >= a0 lambda` whenever `|S|<=rho n`;
2. **H2 (macroscopic pair expansion):** `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. **H3:** `lambda -> infinity` along the graph sequence.

The metric is `g_twoaxis(epsilon,rho,kappa)`, the largest explicit uniform giant fraction proved on this fixed class at `p >= (1+epsilon)/lambda`.

The preceding run proved, using genuine round-one components and two-scale harvesting, that with probability `1-o(1)` the round-one seed mass `W` can be made

`W >= (rho-rho*lambda^(-1/6)) n`,

while every seed component has more than

`s = a0*lambda^(2/3)`

vertices. Hence the genuine seed-component quotient has at most

`m <= n/(a0*lambda^(2/3))`

vertices. It then used H2 plus an independent sprinkle with

`p2 >= epsilon*lambda^(-4/3)`

to prove the concrete receipt

`g_old = rho-2*alpha = rho*(1-q0/32)`,

and, more strongly, every fixed coefficient strictly below `rho-alpha`.

The apparent obstruction in that report was the H2 cutoff `alpha n`: the balanced-cut extraction only invoked H2 when both sides of a surviving seed cut were at least `alpha n`. The present run shows that this cutoff is not a hard wall. A cut with one side slightly below `alpha n` can be padded to the H2 scale, and the cost of the padding can be controlled by the global spectral radius.

## 3. Method #15 — break the symmetry: pad only the deficient side

The key lemma is deterministic.

### Lemma 1 (one-sided padding below the H2 cutoff)

Let `A,B` be disjoint vertex sets in `G`; write

`|A|=a n`, `|B|=b n`,

and suppose `b<alpha`. Put

`d:=alpha-b>0`.

Assume `A` is large enough to contain two disjoint subsets of respective sizes `alpha n` and `d n` (integer rounding is handled below). Then

`e_G(A,B) >= lambda n * [ kappa - alpha*d/a - o_n(1) ]`.

In particular, whenever `alpha*d/a < kappa`, the original H2 hypothesis forces a positive `Theta(lambda n)` edge capacity across the asymmetric cut `(A,B)`, even though `B` itself is below the H2 cutoff.

### Proof

Ignore integer rounding for one paragraph. Choose an ordered pair of disjoint subsets

`A' subset A`, `D subset A\A'`,

uniformly among all pairs with

`|A'|=alpha n`, `|D|=d n`.

For every internal edge of `G[A]`, the probability that its endpoints are split between `A'` and `D` is

`2 (alpha n)(d n) / [ (a n)(a n-1) ]`.

Also, by the Rayleigh quotient for the adjacency matrix,

`2 e_G(A) = 1_A^T Adj(G) 1_A <= lambda |A| = lambda a n`.

Therefore

`E e_G(A',D)`

`= e_G(A) * 2(alpha n)(d n)/[(a n)(a n-1)]`

`<= lambda * (alpha n)(d n)/(a n-1)`

`= lambda n * [alpha*d/(a-1/n)]`.

Hence some deterministic choice of `A',D` satisfies this upper bound. The sets `A'` and `B union D` are disjoint and both have size `alpha n`, so H2 gives

`e_G(A',B) + e_G(A',D)`

`= e_G(A', B union D)`

`>= kappa lambda n`.

Consequently

`e_G(A,B) >= e_G(A',B)`

`>= lambda n [kappa-alpha*d/(a-1/n)]`.

This is the claim.

For exact integer sizes take `k=ceil(alpha n)` and, when `|B|<k`, take `ell=k-|B|`; choose disjoint `A',D subset A` with sizes `k,ell`. The same exact expectation is

`E e(A',D) <= lambda*k*ell/(|A|-1)`.

After division by `lambda n`, this differs from `alpha*d/a` by `o_n(1)`. Since every application below has a fixed positive margin, the rounding error is harmless for all sufficiently large `n`.

The point is asymmetry: I do **not** merge disconnected seed components or declare an artificial block connected. I leave the true quotient untouched. The padding sets are only a deterministic device for lower-bounding the number of original host edges across an already existing quotient cut.

## 4. Method #27 — swap the quantifiers: H2 implies a one-sided cut theorem

The original H2 is a statement of the form

> for **every pair** of disjoint sets above the common threshold `alpha n`, there are at least `kappa lambda n` edges.

Lemma 1 turns it into the following derived statement:

> for **every asymmetric partition cut** with a sufficiently large opposite side, there **exists** a padding `(A',D)` certifying `Theta(lambda n)` direct capacity even when the smaller side is below `alpha n`.

This is exactly the quantifier swap needed by the sprinkling argument, because a failure of the sprinkle produces one adversarial quotient cut; we may then choose the certificate adapted to that cut.

Let the round-one seed mass satisfy

`W >= (rho-eta)n`

for a fixed `eta>0`. Fix a deficit parameter `d in (0,alpha)` and set

`b0:=alpha-d`.

Suppose no round-two component contains at least

`W-b0 n`

seed vertices. I now extract a quotient cut whose two sides have at least `b0 n` seed vertices.

Indeed, if some round-two quotient component has seed mass in `[b0 n, W-b0 n]`, take that component versus its complement. Otherwise every component is either smaller than `b0 n` or larger than `W-b0 n`; the latter is excluded by assumption, so all components are smaller than `b0 n`. Greedily add components until the running mass first reaches `b0 n`. The resulting side has mass below `2b0 n`. Since `alpha<rho/64` and `eta` will be much smaller than `alpha`, we have `W>=3b0 n` for all sufficiently large `n`, so the complementary side also has mass at least `b0 n`.

Call the smaller cut side `B` and the larger `A`. If both have size at least `alpha n`, H2 directly gives `kappa lambda n` crossing edges. Otherwise

`b0 n <= |B| < alpha n`.

Write

`d_B := alpha-|B|/n`,

so `0<d_B<=d`. Because `A` is the complement of `B` inside the seed family,

`a:=|A|/n >= rho-eta-alpha+d_B`.

The function

`x -> alpha*x/(rho-eta-alpha+x)`

is increasing for `x>=0`, hence Lemma 1 gives

`e_G(A,B)/(lambda n)`

`>= kappa - alpha*d_B/a - o(1)`

`>= kappa - alpha*d/(rho-eta-alpha+d) - o(1)`.

Thus any fixed `d,eta` satisfying

`alpha*d/(rho-eta-alpha+d) < kappa`

gives a uniform positive crossing-capacity constant for **every** quotient cut with both seed sides at least `(alpha-d)n`.

## 5. A concrete strict metric improvement

To make the movement completely explicit, define

`d0 := min{ alpha/2, kappa*(rho-alpha)/(4*alpha) } > 0`,

`eta0 := d0/4`,

and

`b0 := alpha-d0`.

For a deficient cut as above,

`a >= rho-eta0-alpha+d_B`, `0<d_B<=d0`.

The worst ratio occurs at `d_B=d0`, so

`alpha*d_B/a`

`<= alpha*d0/(rho-alpha+3d0/4)`

`<= alpha*d0/(rho-alpha)`

`<= kappa/4`.

After the `o(1)` integer-rounding term, every such cut therefore has at least, say,

`(kappa/2) lambda n`

crossing host edges for all sufficiently large `n`. (The unused margin is deliberate.)

The previous two-scale harvesting theorem gives

`W >= (rho-eta0)n`

with probability `1-o(1)` because `rho*lambda^(-1/6)<eta0` eventually. Conditional on that seed family, there are at most

`m <= n/(a0 lambda^(2/3))`

true seed-component quotient vertices. For a fixed bad quotient cut, the independent sprinkle misses all crossing edges with probability at most

`exp[-(kappa/2) p2 lambda n]`

`<= exp[-(kappa*epsilon/2) n/lambda^(1/3)]`.

Union-bounding over at most `2^m` quotient cuts gives

`P(some bad cut survives | seed family)`

`<= exp{ (log 2/a0) n/lambda^(2/3) - (kappa*epsilon/2)n/lambda^(1/3) }`

`= o(1)`

by H3.

Therefore, with probability `1-o(1)`, one round-two component captures at least

`W-b0 n`

`>= [rho-eta0-alpha+d0]n`

`= [rho-alpha+(3/4)d0]n`.

Hence the new concrete metric receipt is

`g_pad := rho-alpha + (3/4) min{ alpha/2, kappa*(rho-alpha)/(4*alpha) }`.

Equivalently,

`g_pad = rho-alpha + min{3alpha/8, 3*kappa*(rho-alpha)/(16*alpha)}`.

Since `d0>0`,

`g_pad > rho-alpha`.

This is stronger than **even the previous run's asymptotic envelope**, not merely stronger than its concrete receipt `rho-2alpha`. Thus the frozen metric genuinely moves without changing H1, H2, H3, `epsilon`, `rho`, or `kappa`.

Substituting `alpha=rho(1-exp(-epsilon^2/288))/64` gives a completely explicit expression in the frozen parameters.

## 6. Stronger envelope obtained by optimizing the one-sided padding

The concrete constants above intentionally leave slack. Let `eta downarrow 0` after fixing a desired constant coefficient. The one-sided padding condition becomes

`alpha*d/(rho-alpha+d) < kappa`.

For every nonvacuous asymptotic H2 sequence we have `kappa<alpha` (proved in the next section), so this is equivalent to

`d < kappa*(rho-alpha)/(alpha-kappa)`.

Of course `d` cannot exceed `alpha`. Define

`d_* := min{ alpha, kappa*(rho-alpha)/(alpha-kappa) }`.

Then for every fixed

`0<d<d_*`

and all sufficiently small fixed `eta>0`, the same harvest-and-sprinkle argument proves

`L1(G_p)/n >= rho-alpha+d-eta`

with probability `1-o(1)`.

Therefore every fixed coefficient strictly below

`g_pad^sup := rho-alpha+d_*`

is certified on the unchanged H0002 class.

When the nonvacuity restriction from the next section is used (`kappa<=alpha^2` asymptotically), one normally has `d_*<alpha` (with only an endpoint possibility when `rho=1`), and the envelope can be written

`g_pad^sup = alpha*(rho-alpha)/(alpha-kappa)`.

I am **not** claiming attainment of this supremum: the proof fixes `d<d_*` and a positive padding margin before taking the graph sequence to infinity.

## 7. Method #24 — find the extremal scale: H2 itself forces `kappa <= alpha^2`

There is a simple exact averaging obstruction that identifies the natural scale of `kappa` and prevents overinterpreting the preceding formula.

Let

`k:=ceil(alpha n)`.

Choose an ordered pair `(X,Y)` uniformly among disjoint `k`-vertex subsets of `V(G)`. For each host edge, the probability that its endpoints are split between `X` and `Y` is exactly

`2 k^2/[n(n-1)]`.

Hence

`E e_G(X,Y) = |E(G)| * 2k^2/[n(n-1)]`.

The all-ones Rayleigh quotient gives

`2|E(G)|/n <= lambda`,

so

`E e_G(X,Y) <= lambda*k^2/(n-1)`.

But H2 says **every** such pair has at least `kappa lambda n` crossing edges. Therefore necessarily

`kappa <= k^2/[n(n-1)]`.

Along any asymptotic sequence,

`kappa <= alpha^2 + o(1)`,

and hence, for fixed nonvacuous H2 parameters,

`kappa <= alpha^2 < alpha`.

This is an exact finite obstruction: if

`kappa > ceil(alpha n)^2/[n(n-1)]`,

no `n`-vertex graph can satisfy H2 at all.

It also explains why H2 cannot magically yield deletion resilience far beyond the H1 budget: in the present normalization, its maximum possible constant is of order `alpha^2`, not order one. The gain in Section 6 is therefore of the natural order `kappa*(rho-alpha)/alpha`, and the new theorem is using essentially the right scale for this black-box interface.

No exact-arithmetic checker was created for this run because the new claims are analytic identities/inequalities proved fully on the page; there is no finite enumeration claim to certify.

## 8. Why this is a genuinely new route relative to the previous run

The preceding report's `rho-alpha` envelope arose from requiring a surviving quotient cut to have **both** sides above the H2 threshold. This run does not optimize the harvesting probability, the round split, or the seed cutoff again.

Instead:

- **#15 BREAK THE SYMMETRY:** only the deficient side is padded; the large side supplies the padding certificate.
- **#27 SWAP THE QUANTIFIERS:** the universal two-set H2 statement is converted into an existential certificate tailored to each adversarial quotient cut.
- **#24 FIND THE EXTREMAL OBJECT:** averaging over all disjoint threshold-size pairs proves the sharp parameter-scale obstruction `kappa<=alpha^2+o(1)`.

The route moves the metric strictly past the previous apparent H2 barrier.

## 9. What remains

The next obstruction is now smaller and more precise. The current black-box route can fail when the small side of a quotient cut drops below

`b_* := alpha-d_*`,

because padding it to `alpha n` can consume all of the guaranteed H2 capacity in the worst case. To improve the giant fraction further on the **same** frozen class, a proof would need at least one ingredient not present in the current argument:

1. a sharper worst-case upper bound on the padding contamination `e(A',D)` than the spectral-radius/Rayleigh average;
2. a way to choose padding vertices outside the large seed side and exploit the unused vertex reservoir;
3. or a multi-stage sprinkle that absorbs a sub-`b_* n` remainder without requiring a direct H2 cut certificate at that scale.

Those are genuinely different routes. Another refinement of the local Poisson survival probability or the seed-harvesting scales will not address this remaining bottleneck.

H0002 remains **PARTIAL / SOURCE OPEN / ACTIVE**. This theorem supplies stronger natural sufficient conditions within the frozen H1-H2-H3 class; it does not classify all graphs answering CMW Question 5.1.

## 10. Model / scheduler / permission reality

The exposed task-control surface still provides no binding model-family selector, no reasoning-effort selector, and no authenticated per-run applied-model receipt. GPT-6 / maximum therefore remains prompt-only here. Actually enforcing it would require scheduler/API support for those fields plus runtime attestation.

The historical P26 `You cannot modify this task` error was authorization-context-specific: the current root ledger records a later successful P26 update from an authorized context, while other contexts recorded denials. The compliant workaround for any task that still refuses modification is its owning authorized workspace/account context or platform support, never duplication or permission bypass. No scheduler change was attempted in this run.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  canonical_target: H0002
  source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1
  status_before: PARTIAL / SOURCE OPEN / ACTIVE
  status_after: PARTIAL / SOURCE OPEN / ACTIVE
  frozen_class: H1 deletion resilience + H2 pair expansion at alpha0 + H3 lambda->infinity
  definitions:
    q0: 1-exp(-epsilon^2/288)
    alpha0: rho*q0/64
    d0: min(alpha0/2, kappa*(rho-alpha0)/(4*alpha0))
  metric_before_concrete: rho*(1-q0/32) = rho-2*alpha0
  metric_before_envelope: every fixed g < rho-alpha0
  metric_after_concrete: rho-alpha0 + 3*d0/4
  metric_after_envelope: every fixed g < rho-alpha0 + min(alpha0, kappa*(rho-alpha0)/(alpha0-kappa))
  movement: STRICT
  supported_unchanged_count_before: 0
  supported_unchanged_count_after: 0
  source_verdict: OPEN
  track_verdict: PARTIAL
  methods_used: [15, 24, 27]
  finite_obstruction: kappa <= ceil(alpha0*n)^2/[n*(n-1)] for any n-vertex H2 instance
  checker: none; analytic proof, no finite enumeration core
  next_obligation: sharpen or bypass padding contamination below the derived b_* cutoff
```

No shared root, peer file, email, Drive item, workflow, permission, public posting, scheduler, or task configuration was modified in this run.