Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT:** H0002 `g_twoaxis(epsilon,rho,kappa): 61*rho*q0/64 -> rho*(q_star-q0/64)`, where `q0=1-exp(-epsilon^2/288)`, `eta_star=epsilon*(440-63*epsilon)/512`, and `q_star=1-exp(-eta_star^2/18)`; Section-B methods actually used: **#4 PROVE SOMETHING WEAKER, COMPLETELY, #10 DERANDOMIZE, #20 FIND WHY THE ALGORITHM FAILS**.

# R16 — H0002 fourth substantive run: endpoint seed mass, deterministic cut extraction, and the sharp black-box barrier

## 1. Continuity, source, ownership, and required reads

This run continues the complete latest R16 research chain on the exclusive HARD OUTSIDE target `H0002`, Question 5.1 of Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (submitted 19 Aug 2026). It does **not** reopen H0021/H0022 or the stale Beck--Fiala scheduler title.

Before research I reread/reconciled the required campaign surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the H-intake row for H0002, the canonical claim `operations/claims/H0002.md`, the newest R16 report

`runs/R16/2026-09-18T10-46-29Z_h0002-seed-large-deviation-linear-pair-expansion_6a4c.md`,

and the newest same-source neighboring terminal/handoff records for G0010 and G0011. I continue from the latest supported H0002 value rather than from the stale root R16/Beck--Fiala row.

A separate file `operations/claims/H0018.md` now also names R16 as owner of another HARD target. At run start there was no H0018 report in `runs/R16/` and no release/handoff of H0002. To avoid inventing a rotation or mixing two targets, this run does not touch H0018 and preserves the complete H0002 report chain as the active research state used here. This ownership inconsistency should be reconciled by the fleet coordinator; it is not permission for this run to edit shared roots or another claim.

Fresh current-source checks on 18 Sep 2026 still show arXiv:2608.19145v1 as the current version. Question 5.1 asks:

> What natural conditions on `G` imply that if `p >= (1+epsilon)/lambda(G)` then with constant probability `G_p` contains a component of size `Omega(|G|)`?

The authors emphasize that robust connectivity alone can miss the obstruction because the spectral radius may be localized on a small part of the graph. No later source-matching resolution was found in the bounded current search. This is current-status evidence, not an exhaustive novelty certificate.

## 2. Frozen H0002 class and the previous metric

Fix

`0<epsilon<=1`, `0<rho<=1`, `kappa>0`,

let `n=|G|`, `lambda=lambda(G)`, and define

`q0 := 1-exp(-epsilon^2/288)`,

`alpha := q0*rho/64`.

The canonical frozen class from `operations/claims/H0002.md` has:

**(H1) Spectral deletion resilience.** For every `S` with `|S|<=rho*n`,

`lambda(G-S) >= (1-epsilon/8)*lambda`.

**(H2) Macroscopic pair expansion.** For all disjoint `A,B` with

`|A|,|B| >= alpha*n`,

`e_G(A,B) >= kappa*lambda*n`.

**(H3)** `lambda(G)->infinity` along the graph sequence.

The tracked quantity `g_twoaxis(epsilon,rho,kappa)` is the largest explicit giant fraction proved uniformly on this frozen class at every

`p >= (1+epsilon)/lambda(G)`

with probability bounded below by a positive constant depending only on the frozen parameters.

The preceding report proved

`g_old = 61*rho*q0/64`.

This run proves the strictly larger concrete value

`g_new = rho*(q_star-q0/64)`,

where

`eta_star := (1+63*epsilon/64)*(1-epsilon/8)-1`

`          = epsilon*(440-63*epsilon)/512`,

and

`q_star := 1-exp(-eta_star^2/18)`.

Since for `0<epsilon<=1`,

`eta_star >= (377/512)*epsilon > epsilon/4`,

we have `q_star>q0`, and therefore

`g_new > (63/64)rho*q0 > (61/64)rho*q0 = g_old`.

Thus the frozen metric genuinely moves and the H0002 unchanged counter remains/reset to `0`.

## 3. Fixed split: reserve only one sixty-fourth of the epsilon margin for sprinkling

By monotonicity it is enough to prove the result at

`p=(1+epsilon)/lambda`.

Instead of the earlier first-round density `(1+epsilon/2)/lambda`, fix the concrete split

`p1 := (1+63*epsilon/64)/lambda`

and define `p2` by the independent two-round coupling

`1-p=(1-p1)(1-p2)`.

For all sufficiently large `n` in the frozen class, `p1<1`, and

`p2 = (p-p1)/(1-p1) >= epsilon/(64*lambda)`.

Suppose an adaptive exploration has already deleted a set `S` with `|S|<rho*n`. By (H1),

`p1*lambda(G-S)`

`>= (1+63*epsilon/64)*(1-epsilon/8)`

`= 1+eta_star`.

Let `w_S` be a Perron eigenvector of `G-S`, normalized so that `max_v w_S(v)=1`, and start the next component exploration at a maximizing vertex. Lemma 3.1(b) of the source paper, applied with parameter `eta_star` and `C=1`, gives an explicit `gamma_star=eta_star/6` such that the next `p1`-component has size more than

`s := gamma_star*lambda(G-S)`

with conditional probability at least

`q_star = 1-exp(-eta_star^2/18)`.

Using (H1) again, throughout the permitted deletion window every successful component therefore has more than

`s0 := gamma_star*(1-epsilon/8)*lambda`

vertices.

This is the only source input needed for the first-round counting below.

## 4. Method #4 — prove the endpoint seed statement completely

The previous run proved seed mass `beta*rho*n` for every fixed `beta<q`, but deliberately did not take the endpoint. At the endpoint the large-deviation exponent vanishes, so one needs a different argument. The endpoint is nevertheless true at the constant-probability level required by Question 5.1.

### Lemma 4.1 (endpoint adaptive seed lemma)

Let `0<q<1`, `R>0`, and `s>0`. Consider any adaptive sequence of disjoint explored components while total deleted mass is below `R`, with the following two properties at every attempted step:

1. conditionally on the past, the component is successful with probability at least `q`;
2. a successful component has size `>s`, while a failed component has size `<=s`.

Stop as soon as either successful mass reaches `qR` or total deleted mass reaches `R`.

Then there exists `c_end(q)>0`, independent of `R/s` and of the adaptive history, such that

`P(successful mass >= qR) >= c_end(q)`.

### Proof

Put `y=R/s`. While the process has not stopped, couple the actual success indicators from below by iid Bernoulli(`q`) variables. This is standard: at step `i`, if the conditional success probability is `q_i>=q`, take an independent uniform `U_i`, declare the comparison Bernoulli to be `1_{U_i<=q}` and the actual success to be `1_{U_i<=q_i}`.

Suppose the target `qR` is not reached and the process stops because total deleted mass has reached `R`. Let `S` and `F` be the numbers of successful and failed attempts by then.

Because each successful component has size `>s` and the total successful mass is `<qR`,

`S < qR/s = qy`.

Because total deleted mass is at least `R`, while successful mass is `<qR`, failed mass is `>(1-q)R`; since every failed component has size at most `s`,

`F > (1-q)R/s = (1-q)y`.

Define

`k(y):=ceil(qy)`,

`r(y):=floor((1-q)y)+1`.

Thus target failure forces `r(y)` comparison failures to occur before the `k(y)`-th comparison success. Hence

`P(target succeeds)`

`>= P(Bin(N(y),q) >= k(y))`,

where

`N(y):=k(y)+r(y)-1=ceil(qy)+floor((1-q)y)`.

Now

`|N(y)-y|<=1`

and

`|k(y)-qN(y)|<=2`.

As `y->infinity`, the standardized displacement of the threshold from the binomial mean therefore tends to zero:

`(k(y)-qN(y))/sqrt(N(y)q(1-q)) -> 0`.

By the de Moivre--Laplace central limit theorem,

`P(Bin(N(y),q) >= k(y)) -> 1/2`.

Consequently there exists a finite `Y(q)` such that this probability is at least, say, `1/3` whenever `y>=Y(q)`.

For `0<y<Y(q)`, the integer pair `(k(y),r(y))` ranges over only finitely many possibilities. For each such pair, the event that the first `k(y)` comparison trials are all successes has positive probability `q^{k(y)}` and guarantees `k(y)` successes before `r(y)` failures. Hence the minimum success probability over this finite collection is positive.

Taking the smaller of this finite minimum and `1/3` proves a uniform constant `c_end(q)>0`. ∎

### Application to H0002

Apply Lemma 4.1 with

`q=q_star`, `R=rho*n`, `s=s0`.

Therefore, with probability at least the fixed positive constant `c_end(q_star)`, the first round contains a union `U` of successful components with

`|U| >= q_star*rho*n`.

Every successful component has more than `s0=Theta_epsilon(lambda)` vertices, so the number `m` of successful first-round components satisfies

`m <= n/s0 = O_epsilon(n/lambda)`.

This endpoint statement is strictly stronger than the preceding `beta<q` lemma at the level relevant to the frozen metric.

## 5. Method #10 — derandomize the gluing witness

The preceding report used a conservative greedy cut and lost `2*alpha*n` vertices. The correct deterministic statement loses only `alpha*n`.

### Lemma 5.1 (deterministic balanced-cut extraction)

Let positive weights `w_1,...,w_m` have total weight `W`, and let `a>0` with `W>=3a`. Then exactly one of the following must occur:

1. some weight satisfies `w_i >= W-a`; or
2. there is a subset `I` such that

`a <= sum_{i in I} w_i <= W-a`.

Equivalently, unless one component already carries all but `a` of the mass, there is a partition of the components into two sides of weight at least `a` each.

### Proof

If some `w_i` lies in `[a,W-a]`, take `I={i}`. If some `w_i>=W-a`, we are in case 1. Thus it remains only to consider the case in which every `w_i<a`.

Order the weights arbitrarily and greedily add them until their partial sum first reaches `a`. The previous partial sum is `<a` and the last added weight is `<a`, so the resulting sum is `<2a`. Since `W>=3a`, we have `2a<=W-a`. This gives case 2. ∎

This is an explicit deterministic algorithm for producing the obstructing cut; no probabilistic partitioning is needed.

### Sprinkling consequence

Condition on a first-round outcome satisfying

`|U|=:W >= q_star*rho*n`.

Contract each successful first-round component to one weighted vertex and expose the `p2` edges between them. Let

`a:=alpha*n=(q0*rho/64)n`.

Because `q_star>q0`, we have `W>=64a`, so in particular `W>=3a`.

If every second-round connected component on the contracted graph had original weight `<W-a`, Lemma 5.1 would produce a partition `A,B` of unions of whole second-round components with

`|A|,|B|>=a=alpha*n`.

There is no `p2`-open edge crossing this cut. By frozen hypothesis (H2), however,

`e_G(A,B) >= kappa*lambda*n`.

For a fixed partition, since `p2>=epsilon/(64lambda)`,

`P(no p2-open A--B edge | first round)`

`<= exp(-p2*kappa*lambda*n)`

`<= exp(-kappa*epsilon*n/64)`.

There are at most `2^m` cuts of the `m` successful first-round components. Since

`m <= n/s0 = O_epsilon(n/lambda)=o(n)`

by (H3), a union bound gives

`P(any such bad cut survives | first round)`

`<= exp(O_epsilon(n/lambda)-kappa*epsilon*n/64)=o(1)`.

Therefore, conditional on the endpoint seed event, with probability `1-o(1)` some second-round component has size at least

`W-a`

`>= q_star*rho*n - (q0*rho/64)n`

`= rho*(q_star-q0/64)n`.

Combining with Lemma 4.1 proves the following source-valid partial theorem.

### Theorem 5.2 (improved frozen-class giant fraction)

For the canonical H0002 frozen class and every

`p >= (1+epsilon)/lambda(G)`, 

for all sufficiently large `n`,

`P( L_1(G_p) >= rho*(q_star-q0/64)*n )`

`>= c_end(q_star)-o(1)`,

where

`q0=1-exp(-epsilon^2/288)`,

`eta_star=epsilon*(440-63*epsilon)/512`,

`q_star=1-exp(-eta_star^2/18)`.

Hence

`g_twoaxis(epsilon,rho,kappa) >= rho*(q_star-q0/64)`.

The source remains **OPEN / PARTIAL** because Question 5.1 asks for natural conditions/classification, not merely this sufficient two-axis class.

## 6. Method #20 — exact reasons this architecture now stops where it does

This run deliberately looked for the failure mode of the improved procedure rather than immediately stacking another lemma on top of it.

### 6.1 The endpoint `q_star` is sharp for the black-box seed process

Lemma 4.1 uses only the per-attempt guarantee

`P(success_i | past) >= q_star`

plus the dichotomy `success size >s`, `failure size <=s`.

No theorem using only these facts can guarantee a uniform seed fraction `beta>q_star` with positive probability independent of `R/s`.

Indeed, take the comparison process itself: iid Bernoulli(`q_star`) attempts, with every attempted component having exactly size `s` for bookkeeping purposes. If `R/s=y` is an integer tending to infinity, the fraction of successful mass before total deleted mass reaches `R` is simply the empirical Bernoulli fraction. For every fixed `beta>q_star`, the law of large numbers gives

`P(successful mass >= beta*R) -> 0`.

Thus `q_star` is the exact endpoint of what the single-vertex source lemma can force without using additional information about the distribution or sizes of successful components.

This is a method obstruction, not a counterexample to Question 5.1.

### 6.2 The `alpha*n` gluing loss is sharp for the pair-threshold information alone

Hypothesis (H2) says nothing about a leftover side of size `<alpha*n`. Therefore the deterministic statement one can force from “no macroscopic cut survives sprinkling” is precisely that one second-round component carries all but `<alpha*n` of the seed mass.

Without an expansion assumption below the `alpha*n` scale, an argument based only on the absence of cuts with both sides at least `alpha*n` cannot force the final component to absorb that last sub-`alpha*n` remainder.

Hence the improvement from the old `W-2alpha*n` to `W-alpha*n` saturates the present cut-information architecture.

### 6.3 Why ordinary one-set isoperimetry does not mechanically replace pair expansion

The intended next question from the previous report was whether (H2) can be replaced by a more standard one-set edge-isoperimetric condition. The direct implication needed by the current proof is false.

A simple infinite family already shows the issue. Let

`G=K_{2m,m}`

with the side of size `2m` partitioned into two sets `A,B` of size `m` each, and let the other side be `C` of size `m`. Then

`e_G(A,B)=0`,

even though the graph has very large one-set edge boundaries: every nontrivial set of size at most `|G|/2` sends many edges to its complement. The boundary of `A` and of `B` is routed entirely through the reservoir `C`.

This does **not** refute the desired percolation conclusion—indeed, multi-hop paths through `C` may join the pieces. It refutes only the mechanical substitution

`one-set boundary lower bound => direct host edges between every two large seed unions`.

To exploit ordinary isoperimetry one needs a genuinely new multi-hop reliability argument, or a contraction/growth process that uses the reservoir rather than demanding direct A--B edges.

## 7. What each selected Section-B move did

### #4 PROVE SOMETHING WEAKER, COMPLETELY — succeeded

Instead of trying to classify all natural conditions in Question 5.1, I isolated the one-dimensional adaptive seed process and proved its exact constant-probability endpoint `q`, including the vanishing-large-deviation boundary where the previous `beta<q` argument stopped.

### #10 DERANDOMIZE — succeeded

The gluing witness is now deterministic: unless one sprinkled component already has weight at least `W-a`, a greedy algorithm constructs a balanced component cut with both sides at least `a`. This removes one full `alpha*n` of artificial loss from the previous metric.

### #20 FIND WHY THE ALGORITHM FAILS — succeeded as a barrier diagnosis

Two losses are now certified as intrinsic to the current black-box inputs: seed fraction above `q_star` cannot follow from the per-attempt probability bound alone, and final loss below `alpha*n` cannot follow from a pair-expansion hypothesis that is silent beneath the `alpha*n` scale. Standard one-set isoperimetry also does not directly imply the pair-edge condition because boundary can route through a third reservoir.

The next route therefore has to change information, not merely sharpen constants.

## 8. Prior-art/current-status comparison

The primary CMW source still states Question 5.1 as open in v1 and specifically warns that localization of the spectral radius can defeat robust-connectivity conditions by itself.

The closest established expansion theorem I found in the bounded current comparison is Diskin--Erde--Kang--Krivelevich, *Percolation through isoperimetry* (Ann. IHP Probab. Stat. 62 (2026), 900--918). Their result concerns **regular graphs of growing degree** and one-set isoperimetric hypotheses at the `1/d` scale, proving a linear giant with the Erdős--Rényi survival-law size. That is a stronger conclusion on a much more regular class. It is an important baseline but does not subsume the present irregular `1/lambda(G)` formulation with explicit spectral-deletion resilience.

I do **not** claim novelty of seed-and-sprinkle, Perron exploration, greedy cut extraction, or binomial endpoint asymptotics. A bounded search finding no identical theorem is not a publication-level novelty certificate.

## 9. Beck--Fiala reconciliation: stale native title remains superseded

The scheduler title still names Beck--Fiala, but the current mathematical literature changed after the Bansal--Jiang baseline.

Bansal--Jiang, arXiv:2508.03961, prove the conjectured `O(sqrt(t))` scale for `t>=log^2 n` and give a polylogarithmically weakened bound below that range.

More importantly, Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 Sep 2026, state a `3*sqrt(2*pi)` bound for the full Komlós signing problem. Their abstract explicitly derives, for every integer `t>=1`,

`disc(F) < 3*sqrt(2*pi*t)`

for every set system in which each element belongs to at most `t` sets, with no restriction on `n`.

Karingula--Lovett, ECCC TR26-188, posted 17 Sep 2026, give an elementary proof of Komlós with constant `36`, hence another complete uniform `36*sqrt(t)` Beck--Fiala consequence.

These are extremely recent preprint/technical-report results rather than mature refereed consensus, but on their stated claims the old all-`t,n` Beck--Fiala gap has been superseded by the stronger Komlós theorem. R16 therefore must not restart from the Bansal--Jiang `t>=log^2 n` baseline as if the September papers did not exist.

## 10. No checker this run

No finite computational claim was introduced. The endpoint seed theorem, deterministic cut lemma, and two obstruction statements are analytic and proved on the page. Under the owner's 90/10 rule I therefore did not manufacture a checker merely to produce a certificate.

## 11. Next route and stuck state

Because the frozen metric moved, H0002 is not stuck and its supported unchanged count is `0`.

The next nonrepeating Section-B methods are:

- **#6 DEFORM TO A POINT YOU CAN SOLVE:** deform the direct pair-edge condition toward one-set isoperimetry by allowing a bounded number of intermediate reservoirs and identify the first genuinely provable multi-hop joining statement;
- **#13 FIND WHAT ONLY INCREASES:** expose sprinkling in batches and search for a monotone seed-mass/closure functional that grows whenever no giant has formed;
- **#27 SWAP THE QUANTIFIERS:** replace expansion for *all* macroscopic pairs by a statement only for the random family of seed-union cuts produced by the first round, while retaining a uniform probability guarantee.

The immediate mathematical target is not another constant tweak. It is to replace the strong pair-expansion hypothesis by a more standard condition without losing the exact source density `p=(1+epsilon)/lambda(G)`.

## 12. Model/scheduler control status

The exposed task-control surface still provides title/prompt, schedule/start offset, timing mode, enablement, and task identity, but no binding model-family selector, no reasoning-effort selector, and no authenticated per-run model receipt. Therefore GPT-6/maximum remains prompt-only here.

The repository's current `RESULTS.md` records that a P26 update succeeded in one authorized context, while R-series edits were denied in another; the older `You cannot modify this task` event is therefore authorization-context-specific rather than a mathematical issue. The compliant remedy for a task that still returns that error is the owning authorized workspace/account context or platform support, never duplication or permission bypass.

No scheduler state, shared root ledger, peer research file, email, Drive content, public post, purchase, permission, or workflow was changed.

## ledger_delta

```yaml
ledger_delta:
  track: R16
  target: H0002
  category: HARD_OUTSIDE
  source_status: OPEN
  result_status: PARTIAL
  metric: g_twoaxis(epsilon,rho,kappa)
  before: "61*rho*q0/64, q0=1-exp(-epsilon^2/288)"
  after: "rho*(q_star-q0/64), eta_star=epsilon*(440-63*epsilon)/512, q_star=1-exp(-eta_star^2/18)"
  movement: true
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_used: [4, 10, 20]
  recovery_state: NONE
  source_exactly_closed: false
  finite_checker_created: false
  next_methods: [6, 13, 27]
  remaining_obligation: "Replace macroscopic pair expansion by a more standard source-natural condition, or certify a source-valid obstruction; preserve p=(1+epsilon)/lambda(G)."
  ownership_note: "H0002 report chain continued; separate same-owner H0018 claim observed but not researched or modified because no H0002 release/handoff was present."
```
