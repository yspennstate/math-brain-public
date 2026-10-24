Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT:** H0002 `g_twoaxis(epsilon,rho,kappa): rho*q*(30-q)/(32*(2+q)) -> 61*rho*q/64`, where `q=1-exp(-epsilon^2/288)`; Section-B methods actually used: **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #11 DUALIZE, #21 ASK WHO ELSE HAS THIS SHAPE**.

# R16 — H0002 third run: near-q seed mass and linear-scale macroscopic pair expansion

## 1. Continuity, source, ownership, and required reads

This run continues the exclusive R16 HARD OUTSIDE claim `operations/claims/H0002.md`. It does not reopen H0021/H0022 or the stale Beck--Fiala scheduler title.

Before doing mathematics I reread the campaign/control surfaces required by the owner: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current H0002 claim, the newest R16 report `runs/R16/2026-09-18T09-48-03Z_h0002-optimized-seed-perron-delocalization_3f7a.md`, the H-intake verification row for H0002, and neighboring same-source terminal reports for G0010 (Question 5.2) and G0011 (the long-cycle conjecture). The neighboring reports are handoffs and do not alter H0002 ownership.

Primary source: Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1, submitted 19 Aug 2026, Question 5.1. The source asks for natural conditions on a finite graph `G` guaranteeing that for

`p >= (1+epsilon)/lambda(G)`

bond percolation has a component of order `Omega(|G|)` with constant probability.

Fresh bounded web checks on 18 Sep 2026 still found v1 as the current arXiv version and no later source-matching resolution. This is bounded current-status evidence, not an exhaustive novelty certificate.

## 2. Frozen metric and previous value

Fix

`0<epsilon<=1`, `0<rho<=1`, `kappa>0`,

and write

`q := 1-exp(-epsilon^2/288)`,

`alpha := q*rho/64`.

The frozen H0002 class in the canonical claim satisfies, with `n=|G|`, `lambda=lambda(G)`:

**(H1)** for every `S` with `|S|<=rho n`,

`lambda(G-S) >= (1-epsilon/8)lambda`;

**(H2)** for all disjoint `A,B` with `|A|,|B|>=alpha n`,

`e_G(A,B) >= kappa lambda n`;

and `lambda->infinity` along the graph sequence.

The preceding R16 report proved

`g_old = rho*q*(30-q)/(32*(2+q))`.

This run proves the concrete stronger frozen-class value

`g_new = 61*rho*q/64`.

Hence

`g_twoaxis(epsilon,rho,kappa) >= 61*rho*q/64`.

The source remains **OPEN / PARTIAL**: this is a stronger sufficient criterion and quantitative bound, not a classification of all graphs in Question 5.1.

## 3. Setup reused from the preceding proof

By monotonicity it is enough to take

`p=(1+epsilon)/lambda`.

Split the percolation into independent rounds by

`1-p=(1-p1)(1-p2)`,

with

`p1=(1+epsilon/2)/lambda`.

Then

`p2 >= epsilon/(2lambda)`.

Let `eta=epsilon/4`. Under (H1), before the deleted set reaches `rho n`,

`p1*lambda(G-S) >= (1+epsilon/2)(1-epsilon/8) >= 1+epsilon/4`.

In the same normalization as the previous two R16 reports, Christoph--Morawski--Wigderson Lemma 3.1(b) therefore supplies a constant `gamma=gamma(epsilon/4)>0` such that, from a Perron-maximizing residual vertex, the next first-round component has conditional probability at least

`q = 1-exp(-epsilon^2/288)`

of having more than

`s := gamma*(1-epsilon/8)*lambda`

vertices. Call such an exploration **successful**. A failed exploration deletes at most `s` vertices.

For brevity put

`gamma0 := gamma*(1-epsilon/8)`,

so `s=gamma0*lambda`.

## 4. Method #5: a parameterized seed lemma

The previous report balanced early deletion against a fixed Chernoff threshold and obtained first-round successful mass `q*rho n/(2+q)`. That balance is not optimal for the source, because the proof only needs a **positive constant** success probability, not a high one.

The right parameter is the target successful-mass fraction itself.

### Lemma 4.1 (adaptive seed mass up to every beta<q)

Fix any constant `beta` with

`0<beta<q`.

Run the same adaptive first-round exploration, stopping as soon as either

1. the total mass of successful components is at least `beta*rho*n`, or
2. the total deleted mass is at least `rho*n`.

Then there exists a constant

`c_seed=c_seed(q,beta)>0`

independent of `n`, `lambda`, and the graph in the frozen class, such that

`P(successful first-round mass >= beta*rho*n) >= c_seed`.

### Proof

Set

`R:=rho*n`, `y:=R/s`.

Let `Y_i` be the indicator that the `i`th attempted residual component is successful. As long as the procedure has not stopped, the deleted set has size `<R`, so the source lemma applies and

`P(Y_i=1 | past) >= q`.

Thus the success indicators stochastically dominate an iid Bernoulli(`q`) sequence; equivalently one may couple iid `B_i~Bernoulli(q)` so that `B_i<=Y_i` attempt by attempt.

Suppose the procedure fails to reach successful mass `beta R`. It can then stop only because total deleted mass has reached `R`.

Let `S` and `F` be the numbers of successful and failed attempts up to that stopping time. Every successful component has more than `s` vertices, so failure of the target gives

`S < beta*R/s = beta*y`.

Every failed component has at most `s` vertices, while the failed mass is larger than `(1-beta)R`; therefore

`F > (1-beta)*R/s = (1-beta)*y`.

Define

`k(y):=ceil(beta*y)`,

`r(y):=floor((1-beta)*y)+1`.

Hence target failure forces at least `r(y)` failures to occur before `k(y)` successes. Under the Bernoulli domination,

`P(seed target fails)`

`<= P( Bin(r(y)+k(y)-1,q) <= k(y)-1 )`.                 (4.1)

Because `beta<q`,

`(k(y)-1)/(r(y)+k(y)-1) -> beta < q`

as `y->infinity`. A standard Chernoff lower-tail estimate therefore makes the right-hand side of (4.1) tend to zero as `y->infinity`.

Choose `Y<infinity` so that for every `y>=Y` the right-hand side is at most `1/2`. For `0<y<=Y`, the integer pair `(r(y),k(y))` ranges over only finitely many possibilities, and the event that the first `k(y)` Bernoulli trials are all successes has probability `q^{k(y)}>0` and certainly achieves `k(y)` successes before `r(y)` failures. Therefore

`inf_{0<y<=Y} P(k(y) successes before r(y) failures) > 0`.

Combining the bounded and large-`y` regimes proves a uniform positive constant `c_seed(q,beta)`. ∎

### Concrete metric choice

Take

`beta := 63*q/64`.

Lemma 4.1 then gives, with positive probability bounded away from zero,

`|U| >= (63*q*rho/64)n`,

where `U` is the union of successful first-round components.

This is the key metric improvement: the source only asks for constant probability, so the seed mass can be pushed arbitrarily close to `q*rho*n`, rather than stopping at roughly `(q/2)rho*n`.

More generally, Lemma 4.1 works for every `beta<q`. I record the concrete `63q/64` value in the frozen metric rather than claiming an unattained endpoint.

## 5. Gluing the stronger seed in the frozen class

Condition on a first-round realization with

`|U| >= beta*rho*n`, `beta=63q/64`.

Every successful component has more than `s=gamma0 lambda` vertices, so their number `m` satisfies

`m < n/s = n/(gamma0 lambda)`.

Expose the second-round edges only between these successful components. Put

`g := beta*rho - 2*alpha`.

If no second-round component has total original weight at least `g n`, greedily take a union `A` of whole second-round components until its total weight first reaches `alpha n`. Since each such component has weight `<g n`,

`alpha n <= |A| < (alpha+g)n`.

Let `B=U\A`. Then

`|B| > beta*rho*n-(alpha+g)n = alpha*n`.

Thus (H2) applies. For a fixed partition,

`P(no p2-open edge between A and B | first round)`

`<= exp(-p2*kappa*lambda*n)`

`<= exp(-kappa*epsilon*n/2)`.

There are at most `2^m` partitions, hence the total bad-cut probability is at most

`exp( (log 2)n/(gamma0 lambda) - kappa*epsilon*n/2 ) = o(1)`

because the frozen class has `lambda->infinity`.

Therefore with conditional probability `1-o(1)` sprinkling creates a component of size at least `g n`.

For the concrete values

`beta=63q/64`, `alpha=q*rho/64`,

we obtain

`g = (63/64)q*rho - (2/64)q*rho = 61q*rho/64`.

Together with Lemma 4.1 this proves

`P( L_1(G_p) >= (61q*rho/64)n ) >= c_seed(q,63q/64)-o(1)`.

Hence the frozen metric genuinely moves to

`g_twoaxis(epsilon,rho,kappa) >= 61q*rho/64`.

## 6. Method #11: dualize the gluing step — cut entropy versus sprinkling capacity

The old pair-expansion hypothesis (H2) asks for

`e_G(A,B) >= kappa*lambda*n`.

The proof never needs that scale. The actual dual competition is:

- **entropy:** at most `2^m` possible cuts of the contracted seed graph, with `m<=n/(gamma0 lambda)`;
- **capacity:** one cut with `E` host edges survives sprinkling with probability at most `exp(-p2 E)`.

Therefore the natural threshold is `E=Theta(n)`, not `Theta(lambda n)`.

Define the macroscopic pair-edge profile

`chi_alpha(G) := min e_G(A,B)/n`,

where the minimum runs over disjoint `A,B` with `|A|,|B|>=alpha n`.

### Theorem 6.1 (linear-scale pair expansion suffices)

Keep (H1), the same `epsilon,rho`, and `alpha=q*rho/64`. Fix any

`h > h_c := 2 log(2)/(epsilon*gamma0)`.

Assume only

**(H2-linear)** `chi_alpha(G) >= h`,

i.e.

`e_G(A,B) >= h n`

for all disjoint `A,B` of size at least `alpha n`.

Then for every fixed `beta<q` with `beta*rho>2alpha`, at

`p >= (1+epsilon)/lambda(G)`

there is a component of size at least

`(beta*rho-2alpha)n`

with probability bounded below by a positive constant depending only on the frozen parameters. No assumption `lambda->infinity` is needed for the sprinkling union bound.

### Proof

The seed lemma is unchanged. Conditional on seed mass at least `beta*rho*n`, the number of successful components is at most `n/(gamma0 lambda)`.

For a bad cut `(A,B)`, (H2-linear) and `p2>=epsilon/(2lambda)` give

`P(cut survives sprinkling)`

`<= exp(-epsilon*h*n/(2lambda))`.

Union over at most `2^{n/(gamma0 lambda)}` component cuts:

`P(any bad cut survives)`

`<= exp( -D*n/lambda )`,

where

`D := epsilon*h/2 - log(2)/gamma0 > 0`.

For every simple `n`-vertex graph, `lambda<=n-1`, hence `n/lambda>1`; therefore

`P(any bad cut survives) <= exp(-D)`.

Thus, conditional on the seed event, sprinkling succeeds with probability at least

`1-exp(-D)>0`.

The same greedy weighted-cut argument as in Section 5 then yields a component of size `(beta*rho-2alpha)n`. ∎

This is a substantial weakening of the previous R16 theorem: the required number of host edges between two macroscopic pieces drops from order `lambda*n` to order `n`. In dense graphs this removes an entire factor `lambda` from the sufficient joining condition.

Combining Theorem 6.1 with the preceding Perron-delocalization lemma gives a particularly natural source-level sufficient condition:

- the unit Perron vector is sufficiently delocalized so that deletions of `rho n` vertices retain `(1-epsilon/8)lambda`;
- every two disjoint sets of size at least `alpha n` have at least `h n` host edges between them, for some `h>h_c`.

These two conditions separately rule out the source paper's two obstructions: a tiny spectral core controlling `lambda`, and a macroscopic failure of communication between supercritical seed regions.

## 7. Method #21: who else has this shape?

Fresh literature comparison found several established expansion-based percolation results, but none surfaced as the exact H0002 statement:

1. Alon--Benjamini--Stacey (2004) study percolation on bounded-degree uniform expanders and uniqueness/emergence of a giant under regular-expander-type hypotheses.
2. Benjamini--Boucheron--Lugosi--Rossignol (Ann. Probab. 2012) prove sharp-threshold results for bounded-degree expanders.
3. Diskin--Krivelevich (Random Structures & Algorithms 2024) study expansion of the giant in supercritical random subgraphs of `(n,d,lambda)` pseudo-random graphs.
4. Christoph--Morawski--Wigderson (2026) deliberately ask for natural hypotheses in the arbitrary irregular spectral-radius setting because `lambda(G)` may be localized on a tiny core.

The present proof architecture resembles the classical seed-and-sprinkle/expansion paradigm, so I do **not** claim that paradigm, the cut union bound, or Perron variational estimates as novel. What is new within the R16 route is the exact quantitative observation that, once the source's `Omega(lambda)` seed lemma is combined with adaptive deletion resilience, only **linear** macroscopic pair-edge capacity is needed to beat the entropy of the contracted seed cuts at the exact `1/lambda(G)` density.

A bounded search finding no identical theorem is not a novelty certificate; a publication-level prior-art audit would still be required.

## 8. What failed / what the run learned

### #5 ADD A PARAMETER AND DIFFERENTIATE IN IT — succeeded

Parameterizing the seed target by `beta<q` showed that the previous `q/(2+q)` mass was an artifact of demanding an overly comfortable Chernoff margin. At constant-probability level, the adaptive process reaches every fixed fraction `beta<q` of the deletion budget with uniformly positive probability.

### #11 DUALIZE — succeeded

Writing the gluing step as `cut entropy` versus `sprinkling capacity` exposed the true scale. The entropy is only `Theta(n/lambda)` because each seed component has `Omega(lambda)` vertices. Since `p2=Theta(1/lambda)`, a cut needs only `Theta(n)` host edges to carry a constant exponential advantage. The old `Theta(lambda n)` requirement was far stronger than the proof needed.

### #21 ASK WHO ELSE HAS THIS SHAPE — useful boundary, no source closure

The nearest literature treats bounded-degree expanders, regular/pseudorandom graphs, or sharper properties of the already-existing giant. Those are important baselines but do not remove the H0002 irregular spectral-localization issue. I found no later paper explicitly closing Question 5.1 in the bounded fresh search.

## 9. Beck--Fiala scheduler-title reconciliation, refreshed 18 Sep 2026

The native title still says Beck--Fiala, but the current primary literature makes that source stale as an active R16 target.

Bansal--Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` order for `t>=log^2 n` and give polylogarithmically weaker bounds below that range.

More importantly, Guo--Fang--Lu, arXiv:2609.11189v1, submitted **10 Sep 2026**, state the stronger Komlos theorem with universal constant `3 sqrt(2 pi)` and explicitly derive for every set system of maximum element degree `t>=1`

`disc(F) < 3 sqrt(2 pi t)`.

Thus, on the stated theorem, the complete uniform Beck--Fiala bound is

`B(t,n) < 3 sqrt(2 pi t)`

for all `t,n`, with no `t>=log^2 n` restriction.

Karingula--Lovett, ECCC TR26-188, posted **17 Sep 2026**, give a separately authored elementary proof of Komlos with constant `36`, hence the independent weaker complete consequence `B(t,n)<=36 sqrt(t)`.

These are extremely recent preprint/technical-report results rather than mature refereed consensus. They are nevertheless current primary claims stronger than the stale native Beck--Fiala target, so R16 should continue H0002 rather than duplicate the pre-September gap.

## 10. Status, stuck counter, next methods

H0002 status: **PARTIAL / source OPEN / active R16 claim**.

Because the frozen metric moved this run, its unchanged-run count resets to `0`; no stuck recovery is active.

No finite claim was introduced, so no exact-arithmetic checker was manufactured. The theorem-sized claims are proved on the page. This follows the owner's 90/10 rule: the run spent its effort on the route, not on another certificate for an unchanged number.

The next nonrepeating Section-B triple is:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY** — test whether ordinary one-sided edge expansion can replace pair expansion in a source-relevant subclass;
- **#10 DERANDOMIZE** — replace the union over all seed-component cuts by a canonical merge rule or deterministic sparse connector certificate;
- **#20 FIND WHY THE ALGORITHM FAILS** — build a graph satisfying Perron delocalization plus standard cut expansion but failing macroscopic pair expansion, to determine whether the pair condition is genuinely needed or only a proof artifact.

The central next question is whether the two-axis theorem can be reduced from a *pair* expansion profile to a standard one-set isoperimetric condition without losing the exact `(1+epsilon)/lambda(G)` density.

## 11. Scheduler/model-control reality

The runtime exposed to this worker still provides no binding model-family selector, no reasoning-effort selector, and no authenticated applied-effort receipt. This run identifies itself as GPT-5.6 Sol with reasoning level UNVERIFIED; GPT-6/maximum remains prompt text only here.

The historical `You cannot modify this task` problem is an authorization-context issue, not something this research worker may bypass. The compliant remedies remain modification from the owning workspace/account context or platform support. No scheduler state was changed in this run.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  target: H0002
  source_status: OPEN
  claim_status: ACTIVE
  mathematical_status: PARTIAL
  metric_name: g_twoaxis(epsilon,rho,kappa)
  metric_before: rho*q*(30-q)/(32*(2+q))
  metric_after: 61*rho*q/64
  q_definition: 1-exp(-epsilon^2/288)
  movement: true
  unchanged_count_after: 0
  methods_used: [5, 11, 21]
  new_results:
    - adaptive_seed_mass_beta_for_every_beta_less_than_q
    - concrete_seed_beta_63q_over_64
    - frozen_class_giant_fraction_61q_rho_over_64
    - linear_scale_macroscopic_pair_expansion_suffices
  source_closed: false
  finite_checker_needed: false
  next_methods: [4, 10, 20]
  shared_root_edits: false
  peer_file_edits: false
  email: false
  drive: false
  public_posting: false
  scheduler_change: false
```
