Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT:** H0002 `g_twoaxis(epsilon,rho,kappa): (rho/64)(1-exp(-epsilon^2/288)) -> rho*q*(30-q)/(32*(2+q))`, where `q=1-exp(-epsilon^2/288)`; Section-B methods actually used: **#3 PROVE SOMETHING STRONGER, #19 MAKE IT AN ALGORITHM, #30 DO ONE SCALE AT A TIME**.

# R16 — H0002 second run: optimized seed mass, sharp gluing scale, and a Perron-delocalization criterion

## 1. Continuity and source/status checks

This run continues the active R16 HARD OUTSIDE claim `H0002`, created in `operations/claims/H0002.md`. It does not reopen H0021/H0022 or the stale Beck--Fiala scheduler title.

Before research I reread/recovered the required campaign/control surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest R16 report `runs/R16/2026-09-18T09-24-16Z_h0002-two-axis-giant-criterion_7b3f.md`, the H0002 claim and H/G intake aliases, and useful same-source neighboring material (`G0010` = Question 5.2, `G0011` = Conjecture 5.3). The older `G0009` intake row is the exact alias of H0002 and had already suggested Perron-vector delocalisation as a possible ingredient, but did not prove a source-level giant criterion.

Primary source: Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1, submitted 19 Aug 2026, Question 5.1. The exact source question asks for natural conditions on a finite graph `G` implying that for `p >= (1+epsilon)/lambda(G)`, `G_p` has a component of order `Omega(|G|)` with constant probability.

Fresh bounded web checks on 18 Sep 2026 still located v1 as the current arXiv version and no later source-matching resolution. Related baselines found again include Chung--Horn--Lu's general-graph giant criterion using spectral-gap/degree-moment hypotheses and Diskin--Krivelevich's regular-graph percolation theorem (published in *Transactions AMS* in 2026). These make regular-expander special cases non-novel baselines; no novelty claim is made for the criterion below.

## 2. Frozen metric and movement

Fix `0<epsilon<=1`, `0<rho<=1`, `kappa>0`. Put

`q := 1-exp(-epsilon^2/288)`,

`alpha := q rho/64`.

The frozen H0002 class from the preceding R16 report consists of graphs satisfying

**(H1)** for every `S` with `|S|<=rho n`,

`lambda(G-S) >= (1-epsilon/8)lambda(G)`,

and

**(H2)** for every disjoint `A,B` with `|A|,|B|>=alpha n`,

`e_G(A,B) >= kappa lambda(G)n`.

The preceding proved value was

`g_old = q rho/64 = alpha`.

This run proves

`g_new = q rho/(2+q) - 2 alpha`

and hence

`g_new = q rho (30-q)/(32(2+q))`.

Therefore the tracked quantity moves to

`g_twoaxis(epsilon,rho,kappa) >= q rho (30-q)/(32(2+q))`.

For small `epsilon`, `q` is small and the multiplicative gain over the previous displayed bound approaches `30`.

The source status remains **PARTIAL / OPEN**: this gives a stronger explicit sufficient criterion and a more natural Perron-vector corollary, not a classification of all graphs in Question 5.1.

## 3. Stronger theorem

### Theorem 3.1 (optimized two-axis giant criterion)

Fix `0<epsilon<=1`, `0<rho<=1`, `kappa>0`. Let `G=G_n` be an `n`-vertex graph with spectral radius `lambda`, satisfying (H1) and (H2). Let `gamma=gamma(epsilon/4)>0` be the constant supplied by Christoph--Morawski--Wigderson Lemma 3.1(b), in the same normalization used in the preceding R16 report.

It is enough to assume the explicit scale condition

`lambda >= Lambda_0 := max{1+epsilon, 4 log(2)/(kappa epsilon gamma(1-epsilon/8))}`,

rather than `lambda->infinity`.

Then for

`p >= (1+epsilon)/lambda`

we have

`P( L_1(G_p) >= g_new n ) >= c_epsilon-o(1)`,

where

`g_new = q rho (30-q)/(32(2+q))`

and one may take

`c_epsilon := 1-exp(-q/16)>0`.

If `lambda->infinity`, the `o(1)` sprinkling term is automatic as in the preceding report.

### Proof

By monotonicity it is enough to use `p=(1+epsilon)/lambda`. Split into independent rounds

`1-p=(1-p1)(1-p2)`,

with

`p1=(1+epsilon/2)/lambda`.

Exactly as in the preceding R16 report,

`p2 >= epsilon/(2lambda)`.                                             (3.1)

Let `eta=epsilon/4`. For any union `S` of already exposed first-round components with `|S|<rho n`, hypothesis (H1) gives

`lambda(G-S) >= (1-epsilon/8)lambda`,

and hence

`p1 lambda(G-S) >= (1+epsilon/2)(1-epsilon/8) >= 1+epsilon/4`.          (3.2)

Choose a Perron eigenvector of `G-S`, normalized to have maximum coordinate one, and expose the `p1`-component of a maximizing vertex. Christoph--Morawski--Wigderson Lemma 3.1(b) therefore gives, conditionally on the previous exploration history,

`P( |C| > s | history ) >= q`,                                        (3.3)

where

`s := gamma(1-epsilon/8)lambda`.                                      (3.4)

Call an attempt **successful** if `|C|>s`; a failed attempt removes at most `s` vertices.

The improvement over the preceding report is an optimized stopping rule.

Set

`R := rho n`,

`a := 2/(2+q)`,

`b := q/(2+q)`.

Thus `a+b=1`. We claim that with probability at least

`c_epsilon=1-exp(-q/16)`                                               (3.5)

the union `U` of successful first-round components has size at least

`|U| >= bR = (q rho/(2+q))n`.                                         (3.6)

To prove this, write `x=aR/s`.

If `x<2`, make one attempt. Then `s>aR/2=R/(2+q)>=bR` because `q<=1`. A successful attempt already gives (3.6), and it occurs with probability at least `q>c_epsilon`.

Assume now `x>=2` and let

`T=floor(x)`.

Run at most `T` attempts, stopping early if the total deleted mass first reaches `R`. Before every attempt the deleted set has size `<R`, so (3.3) is available.

If early stopping occurs, the total mass of failed components is at most

`T s <= aR`.

Hence successful components have mass at least

`R-aR=bR`,                                                            (3.7)

so (3.6) holds deterministically on this branch.

Suppose there is no early stopping. Then all `T` attempts occur. Their success indicators have conditional success probability at least `q`, and therefore stochastically dominate `Bin(T,q)`. A Chernoff lower-tail bound gives

`P( successes < (3q/4)T ) <= exp(-qT/32) <= exp(-q/16)`,              (3.8)

because `T>=2`.

On the complementary event, note that for `x>=2`,

`floor(x)/x >= 2/3`.

Therefore

`T s >= (2/3)aR`,                                                     (3.9)

and the successful mass is strictly larger than

`(3q/4) T s >= (3q/4)(2/3)aR = (q/2)aR = bR`.                        (3.10)

This proves (3.5)--(3.6).

Now condition on a first-round realization satisfying (3.6). The successful components all have size greater than `s`, so their number `m` satisfies

`m < n/s`.                                                            (3.11)

Expose the independent `p2`-round only on edges between these components. Define

`g := b rho - 2 alpha`

so that

`g = q rho/(2+q)-q rho/32 = q rho(30-q)/(32(2+q))`.                  (3.12)

Suppose no sprinkling component has total original weight at least `gn`. Greedily take a union `A` of whole sprinkling components until its weight first reaches `alpha n`. Since each sprinkling component has weight `<gn`,

`alpha n <= |A| < (alpha+g)n`.                                       (3.13)

Let `B=U\A`. By (3.6) and the definition `g=b rho-2alpha`,

`|B| > b rho n-(alpha+g)n = alpha n`.                                (3.14)

Thus both sides meet the (H2) threshold. Since `A,B` are unions of whole first-round components, every host edge between them was `p1`-closed, and its independent second-round bit remains Bernoulli(`p2`). For a fixed partition,

`P(no p2-open edge across A,B | G_{p1})`
` <= exp(-p2 kappa lambda n)`
` <= exp(-kappa epsilon n/2)`.                                       (3.15)

There are at most `2^m` partitions. By (3.11), the total bad-cut probability is at most

`exp( (log 2)n/s - kappa epsilon n/2 )`.                              (3.16)

The explicit assumption on `lambda` makes `(log 2)/s <= kappa epsilon/4`, so (3.16) is at most

`exp(-kappa epsilon n/4)=o(1)`.                                      (3.17)

Hence with conditional probability `1-o(1)` the sprinkling graph has a component of weight at least `gn`. Multiplying by (3.5) proves the theorem. ∎

## 4. A natural Perron-delocalization hypothesis implies (H1)

The old G0009 intake attempt suggested a delocalized Perron vector but did not supply the exact bridge to deletion resilience. The following elementary lemma supplies that bridge.

### Lemma 4.1 (Perron mass controls spectral deletion)

Let `A` be the adjacency matrix of `G`, let `lambda=lambda(G)`, and let `v>=0` be a unit Perron eigenvector: `Av=lambda v`, `||v||_2=1`. For `S subseteq V(G)` set

`m_S := sum_{x in S} v_x^2`.

If `m_S<1`, then

`lambda(G-S) >= lambda (1-2m_S)/(1-m_S)`.                             (4.1)

#### Proof

Write `T=V\S` and split the Perron vector as `(v_S,v_T)`. Put

`a=v_S^T A_{SS}v_S >=0`,

`b=v_S^T A_{ST}v_T >=0`.

From the eigenvector equation restricted against `v_S`,

`a+b=lambda m_S`.                                                     (4.2)

Also

`lambda=v^TAv=a+2b+v_T^T A_{TT}v_T`.                                 (4.3)

Since `a+2b=2lambda m_S-a <=2lambda m_S`,

`v_T^T A_{TT}v_T >= lambda(1-2m_S)`.                                 (4.4)

As `||v_T||_2^2=1-m_S`, the Rayleigh quotient in `G-S` gives (4.1). ∎

### Corollary 4.2 (one-line delocalization condition)

Suppose the unit Perron vector satisfies

`||v||_infinity^2 <= mu/n`.                                           (4.5)

If

`mu rho <= epsilon/(8+epsilon)`,                                     (4.6)

then (H1) holds for every `|S|<=rho n`.

Indeed `m_S<=mu rho`, and (4.6) is exactly

`m_S/(1-m_S) <= epsilon/8`.

Equation (4.1) therefore yields

`lambda(G-S) >= (1-epsilon/8)lambda(G)`.

Consequently, **Perron delocalization + macroscopic pair expansion** is a fully explicit natural sufficient condition for the source's giant-component conclusion at the exact spectral density `(1+epsilon)/lambda(G)`, with the quantitative giant fraction in Theorem 3.1.

This is a sufficient condition, not a necessity statement. Delocalization alone is still insufficient: many disconnected comparable dense blocks can have a spread top eigenspace while preventing a linear component.

## 5. The three Section-B methods and what they did

### #3 — PROVE SOMETHING STRONGER

Rather than add another local lemma, I optimized the entire seed stage. The old proof deliberately spent a factor `16` converting repeated `Omega(lambda)` components into linear successful mass. The new stopping rule balances the two failure modes:

- early exhaustion of the deletion budget, which forces successful mass because failed components cost at most `s` each;
- no exhaustion, where the number of successful attempts is controlled by a one-sided Chernoff bound.

The balance `a=2/(2+q)`, `b=q/(2+q)` raises the certified first-round successful mass from `q rho/16` to `q rho/(2+q)`.

The same method also removes the unnecessary asymptotic restriction `lambda->infinity`: the proof only needs the cut-entropy inequality `(log 2)/s < kappa epsilon/2`, and the theorem uses an explicit stronger margin.

### #19 — MAKE IT AN ALGORITHM

Writing the proof as an adaptive procedure exposed where the old constants were lost.

The procedure is:

1. split the edge bits into `p1` and `p2`;
2. in the current residual graph, take a Perron-maximizing vertex and expose its `p1` component;
3. classify it by whether its size exceeds the source-lemma scale `s`;
4. stop when either the deletion budget `rho n` is exhausted or the optimized attempt cap `floor(a rho n/s)` is reached;
5. contract the successful components and expose only the `p2` edges between contracted pieces.

No polynomial-time novelty claim is made: the source lemma supplies an existential `gamma`, and finding connected components is trivial once percolation is sampled. The algorithmic rewrite was useful because it converted the proof into a clean stopping-time optimization and produced the metric movement.

### #30 — ONE SCALE AT A TIME

The gluing step has a general scale law. If the first round produces total component mass `beta n`, and pair expansion is known for disjoint sets of size at least `alpha n`, then the sprinkling argument certifies a component of size

`(beta-2alpha)n`,                                                     (5.1)

provided `beta>2alpha` and the cut-entropy penalty is dominated by the sprinkling exponent.

The old report used only `beta/4`, leaving a factor on the table. In the frozen H0002 class,

`beta = q rho/(2+q)`,

`alpha = q rho/64`,

and (5.1) is exactly the new metric value.

This scale law also identifies the next real problem: weaken pair expansion (H2) without losing control of all unions of the mesoscopic seed components.

## 6. Prior-art boundary and current source comparison

I do not claim the seed-and-sprinkle philosophy, expansion-based percolation proofs, Perron--Frobenius variational inequality, or regular-expander special cases as novel.

Current baselines checked this run:

- Christoph--Morawski--Wigderson, arXiv:2608.19145v1 (19 Aug 2026), which proves the universal `Omega(lambda(G))` supercritical component scale and poses Question 5.1 for a linear giant;
- Chung--Horn--Lu, *Percolation in General Graphs* (Internet Mathematics 6), which proves a giant under spectral-gap and degree-moment hypotheses at a threshold expressed through the second-order average degree rather than `lambda(G)`;
- Diskin--Krivelevich, *Components, large and small, are as they should be I*, published in *Transactions of the AMS* in 2026, which proves substantially sharper giant-component behavior for growing-degree regular graphs under expansion/local-sparsity assumptions.

A bounded search did not locate the exact combination of (4.5)--(4.6), the deletion bridge (4.1), and the pair-expansion theorem at the exact source threshold. This is not a novelty certificate. Before publication, the spectral-deletion lemma and the two-axis criterion require a deeper citation search and independent audits.

## 7. Beck--Fiala scheduler-title reconciliation

The scheduler title is stale relative to the active R16 research claim.

Fresh checks on 18 Sep 2026 found:

- Bansal--Jiang, arXiv:2508.03961v2, still gives the conjectured `O(sqrt(t))` Beck--Fiala order for `t>=log^2 n`, with extra polylogarithmic losses below that regime;
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), states the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly derives `disc(F)<3 sqrt(2 pi t)` for every integer `t>=1`;
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), gives a separately authored elementary proof of Komlos with constant `36`.

Thus the old all-`t,n` Beck--Fiala gap is, on the stated current preprint results, superseded by stronger Komlos theorems. These are extremely recent preprint/technical-report results rather than mature refereed consensus, so the correct status is **current primary claims resolve/supersede the target; do not restart stale R16 Beck--Fiala research**.

## 8. Status, next methods, and ledger delta

No exact-arithmetic checker was created: this run's new claims are theorem-sized analytic inequalities with full proofs on the page, not finite enumerations. This follows the 90/10 rule and avoids certificate-only work.

H0002 has **real metric movement**, so its unchanged-run count resets to `0`; no stuck recovery is active.

Next nonrepeating Section-B methods proposed:

- **#5 ADD A PARAMETER AND DIFFERENTIATE:** parameterize the pair-expansion scale `alpha` and optimize the tradeoff between seed mass, cut entropy and required expansion;
- **#11 DUALIZE:** express failure of (H2) through sparse/macroscopic cuts and compare with spectral or flow dual certificates;
- **#21 ASK WHO ELSE HAS THIS SHAPE:** port the weakest joining hypotheses from modern isoperimetric percolation theorems, while preserving the exact `1/lambda(G)` source threshold.

```yaml
ledger_delta:
  track: R16
  source_id: H0002
  canonical_alias: G0009
  source: "Christoph--Morawski--Wigderson, arXiv:2608.19145v1, Question 5.1"
  source_status: OPEN
  result_status: PARTIAL
  metric:
    name: g_twoaxis(epsilon,rho,kappa)
    before: "(rho/64)*(1-exp(-epsilon^2/288))"
    after: "rho*q*(30-q)/(32*(2+q)), q=1-exp(-epsilon^2/288)"
    movement: true
  restrictions:
    H1: "spectral deletion resilience through rho*n deletions"
    H2: "pair expansion e(A,B)>=kappa*lambda*n for |A|,|B|>=q*rho*n/64"
    spectral_scale: "lambda >= max(1+epsilon, 4log2/(kappa*epsilon*gamma*(1-epsilon/8)))"
  new_bridge:
    statement: "If unit Perron v has ||v||_inf^2<=mu/n and mu*rho<=epsilon/(8+epsilon), then H1 holds."
    status: PROVED_IN_REPORT
  methods_used: [3, 19, 30]
  unchanged_count_after: 0
  stuck_recovery: none
  closure: false
  audits: 0
```

## 9. Model/scheduler control limit

The actual runtime visible to this report is GPT-5.6 Sol; reasoning effort is not authenticated, hence `UNVERIFIED`. The exposed automation control schema still has prompt/title/schedule/timing/enabled fields but no binding model-family selector, no reasoning-effort selector, and no authenticated per-run model receipt. GPT-6/maximum therefore remains prompt-only in this environment.

No scheduler state, email, Drive content, public post, paid compute, permissions, shared root ledger, or peer research file was changed in this run. Only this immutable R16 report is written.