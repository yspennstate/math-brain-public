Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT:** H0002 `g_twoaxis(epsilon,rho,kappa): 0 -> (rho/64)(1-exp(-epsilon^2/288))`; Section-B methods actually used: **#2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT**.

# R16 — H0002 first run: a two-axis sufficient criterion for a giant at the exact spectral threshold

## 1. Continuity, admission, and source

R16 did not reopen H0021 or H0022. The newest predecessor is

`runs/R16/2026-09-18T08-11-06Z_h0022-newton-hamilton-obstruction-handoff_5c2e.md`,

which records the mandatory H0022 handoff after both HARD stuck recoveries and leaves R16 in successor rotation.

I reread/recovered the required campaign/control surfaces before admission: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest own R16 report, current neighboring admission/rotation reports, and the relevant H/I intake/claim material. Current queue rows are treated as PENDING unless source, status and ownership are rechecked.

The lawful HARD successor is **H0002**:

- Micha Christoph, Patryk Morawski, Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1;
- source question: find natural conditions on a finite graph `G` under which, for `p >= (1+epsilon)/lambda(G)`, bond percolation `G_p` has a component of order `Omega(|G|)` with constant probability;
- a same-day independent HARD admission screen classified H0002 `OPEN-LOOKING / UNOWNED`; it declined it only because that worker's successor gate required a finite/closable problem;
- direct fetch of `operations/claims/H0002.md` returned 404 immediately before the create-only claim;
- a bounded current-literature search on 2026-09-18 found the August 19 source and no later source-matching resolution.

The canonical create-only R16 claim is now

`operations/claims/H0002.md`

at creation commit

`60097a996aff2836996fdac2808cc7ee58f7a83f`.

It was read back at that exact commit before this report was written.

The source itself emphasizes the central obstruction: `lambda(G)` may be controlled by a tiny part of the graph while an induced subgraph on `(1-o(1))|G|` vertices has much smaller spectral radius, so a generic robust-connectivity hypothesis alone need not force a giant at `p=(1+epsilon)/lambda(G)`.

## 2. Frozen metric

Fix

`0 < epsilon <= 1`, `0 < rho <= 1`, `kappa > 0`,

and write `n=|G|`, `lambda=lambda(G)`. Define

`q_epsilon := 1-exp(-epsilon^2/288)`,

`a_epsilon := q_epsilon/64`.

The claimed HARD subproblem freezes the following class of graph sequences `G=G_n`, with `lambda(G_n)->infinity`:

**(H1) spectral deletion resilience.** For every `S subset V(G)` with `|S| <= rho n`,

`lambda(G-S) >= (1-epsilon/8) lambda(G)`.

**(H2) macroscopic pair expansion.** For every two disjoint sets `A,B` with

`|A|,|B| >= a_epsilon rho n`,

one has

`e_G(A,B) >= kappa lambda(G)n`.

The tracked quantity `g_twoaxis(epsilon,rho,kappa)` is the largest explicit `g` proved uniformly for this frozen class such that, whenever

`p >= (1+epsilon)/lambda(G)`, 

`G_p` has a connected component with at least `gn` vertices with probability bounded below by a positive constant depending only on the frozen parameters.

Before this run: `g_twoaxis=0`.

After this run:

`g_twoaxis >= (rho/64)(1-exp(-epsilon^2/288))`.

This is **PARTIAL** progress on source Question 5.1, not closure: the source asks for natural conditions in general, and this run proves one explicit sufficient criterion rather than a classification or necessary-and-sufficient statement.

## 3. Main theorem

### Theorem (spectral-resilience + pair-expansion giant criterion)

Fix `0<epsilon<=1`, `0<rho<=1` and `kappa>0`. Let `(G_n)` be a sequence of finite graphs satisfying (H1), (H2), and `lambda(G_n)->infinity`. Set

`q := 1-exp(-epsilon^2/288)`.

Then for all sufficiently large `n`, every

`p >= (1+epsilon)/lambda(G_n)`

satisfies

`P( L_1(G_{n,p}) >= (q rho/64)n ) >= c_epsilon-o(1)`,

where one may take

`c_epsilon := 1-exp(-q/8) > 0`.

In particular, H0002's source conclusion holds for this graph class at the exact source density scale `(1+epsilon)/lambda(G)`.

### Proof

By monotonicity in `p`, it is enough to prove the result at

`p=(1+epsilon)/lambda`,

where `lambda=lambda(G)`. Split the percolation into two independent rounds:

`G_p = G_{p1} union G_{p2}`,

with

`p1=(1+epsilon/2)/lambda`

and `p2` chosen from

`1-p=(1-p1)(1-p2)`.

For all sufficiently large `lambda`, this is valid and

`p2=(p-p1)/(1-p1) >= epsilon/(2lambda)`.                     (3.1)

Let `eta=epsilon/4`. Christoph--Morawski--Wigderson Lemma 3.1(b), applied with parameter `eta`, says that there is `gamma=gamma(eta)>0` such that if `H` is a graph, `w in [0,1]^{V(H)}` obeys

`sum_{y in N_H(x)} w(y) >= Lambda w(x)`

for all `x`, and `p1 >= (1+eta)/Lambda`, then for a vertex `v` with `w(v)=1`,

`P( |C_v| <= gamma Lambda ) <= exp(-eta^2/18)`;              (3.2)

here the source lemma is invoked with `C=1`, and `w(C_v)>=w(v)=1` automatically.

Now expose components of the first-round graph `G_{p1}` sequentially. Suppose a set `S` consisting of already exposed whole components has been deleted and `|S|<rho n/2`. Put `H=G-S`. By (H1),

`lambda(H) >= (1-epsilon/8)lambda`.

Moreover

`p1 lambda(H)
 >= (1+epsilon/2)(1-epsilon/8)
 >= 1+epsilon/4`,                                            (3.3)

because the difference from `1+epsilon/4` is `epsilon(2-epsilon)/16>0`.

Choose a Perron eigenvector `w` of `H`, normalized so that `max_x w(x)=1`, and choose a maximizing vertex `v`. Define

`s := gamma(1-epsilon/8)lambda`.                              (3.4)

Since `gamma lambda(H)>=s`, (3.2) implies, conditionally on the entire previous exploration history,

`P( |C_v(G_{p1}[H])| > s | history ) >= q`,                 (3.5)

where

`q=1-exp(-eta^2/18)=1-exp(-epsilon^2/288)`.

The conditional statement is legitimate because exposing an entire first-round component only reveals its boundary edges to be closed; unexposed edges internal to the remaining graph are still independent Bernoulli(`p1`).

Call an explored component **successful** if it has more than `s` vertices. A failed attempt therefore removes at most `s` vertices.

We now prove that with probability at least `c_epsilon` the union of successful first-round components has linear total mass.

If

`s > rho n/8`,

make one attempt. By (3.5), with probability at least `q` it succeeds and already contributes more than `rho n/8 >= q rho n/16` vertices.

Otherwise set

`T := floor(rho n/(4s))`.

Then `rho n/(4s)>=2`, so

`T s >= rho n/8`.                                           (3.6)

Run at most `T` attempts, stopping early if the total number of removed vertices reaches `rho n/2`. Before every attempt the deletion set has size below `rho n/2`, so (H1) and (3.5) remain available.

If the process stops early, the total mass of failed components is at most

`T s <= rho n/4`.

Hence successful components carry at least

`rho n/2-rho n/4 = rho n/4 >= q rho n/16`.                 (3.7)

If there is no early stop, all `T` attempts are made. Their success indicators have conditional success probabilities at least `q`, so they stochastically dominate `Bin(T,q)`. A standard Chernoff lower-tail bound gives

`P( number of successes < qT/2 ) <= exp(-qT/8)`.            (3.8)

On the complementary event, using (3.6), successful components have total mass at least

`(qT/2)s >= q rho n/16`.                                    (3.9)

Combining the small-`T` and large-`T` cases, if `U` denotes the union of the successful first-round components, then

`P( |U| >= beta n ) >= c_epsilon`,                           (3.10)

with

`beta := q rho/16`,

`c_epsilon := 1-exp(-q/8)`.

The particular displayed constant is deliberately conservative and uniform in the possible number of attempts.

It remains to convert linear total mass in many mesoscopic first-round components into one linear component. Condition on a first-round realization satisfying `|U|>=beta n`. Let its successful components be `C_1,...,C_m`. Since every `C_i` has more than `s` vertices,

`m <= n/s = o(n)`                                           (3.11)

because `lambda->infinity` and `s=Theta_epsilon(lambda)`.

Expose the independent `p2`-round only on edges between these components. If some `C_i` already has size at least

`beta n/4 = q rho n/64`,

we are done. Otherwise contract each `C_i` to a weighted vertex, the weight being `|C_i|`, and consider the graph formed by the `p2`-open edges between contracted vertices.

Suppose for contradiction that every connected component of this contracted sprinkling graph has total original weight below `beta n/4`. Since the total weight is at least `beta n`, greedily take a union `A` of whole contracted connected components until its weight first reaches `beta n/4`. The last added contracted component has weight below `beta n/4`, hence

`beta n/4 <= |A| < beta n/2`.

Let `B=U\A`. Then `|B|>beta n/2`, and by construction there is **no `p2`-open edge between `A` and `B`**.

But

`beta/4 = q rho/64 = a_epsilon rho`,

so (H2) yields

`e_G(A,B) >= kappa lambda n`.                                (3.12)

Every edge of `G` between `A` and `B` is first-round closed: if any such edge were `p1`-open, its endpoints would belong to the same `p1`-component, while `A` and `B` are unions of whole distinct first-round components. Their independent second-round bits are therefore still Bernoulli(`p2`). For any fixed bipartition of the `m` successful components,

`P(no p2-open edge across A,B | G_{p1})
 <= exp(-p2 kappa lambda n)
 <= exp(-kappa epsilon n/2)`                                  (3.13)

by (3.1).

There are at most `2^m` possible bipartitions. Hence, using (3.11), the probability that **some** such bad bipartition exists is at most

`2^m exp(-kappa epsilon n/2)
 <= exp( (log 2)n/s - kappa epsilon n/2 )
 = o(1)`.                                                     (3.14)

Thus, conditional on (3.10), with probability `1-o(1)` the sprinkling creates a component of at least

`beta n/4 = (q rho/64)n`

vertices. Multiplying by the positive lower bound in (3.10) proves the theorem. ∎

## 4. What the three method moves found

### B2 — attack the negation first

The source itself gives the right counterexample template: a small high-spectral-radius core can set the global value of `lambda(G)` while a linear-sized bulk has much smaller spectral radius and is therefore subcritical at `p=(1+epsilon)/lambda(G)`. This says that a connectivity/expansion condition by itself is not enough unless it is coupled to a delocalization or deletion-resilience requirement.

The opposite obstruction also exists: spectral deletion resilience by itself does not join mesoscopic clusters globally. For example, a disjoint union of many comparable growing cliques can retain spectral radius after sufficiently small fractional deletions but has no linear component because the host has no edges between blocks.

These two failure modes motivated treating spectral delocalization and macroscopic joining as genuinely separate axes rather than trying to encode both in a single vague `expander` hypothesis.

### B18 — say it in another language

The source question becomes a **seed-and-sprinkle quotient problem**.

- Seed phase: deletion resilience lets the source's fixed-vertex component lemma be restarted adaptively `Theta(n/lambda)` times. This generates a linear amount of mass in `Omega(lambda)`-sized components.
- Quotient phase: contract those components. There are only `O(n/lambda)=o(n)` contracted vertices.
- Sprinkle phase: pair expansion makes every macroscopic cut contain `Omega(lambda n)` host edges. The failure probability of one cut is `exp(-Omega(n))`, while the entropy of all cuts is only `2^{O(n/lambda)}=exp(o(n))`.

The central inequality is therefore

`cut entropy = o(n) << sprinkling penalty = Theta(n)`.

That is the mechanism that converts the source's `Omega(lambda)` component into an `Omega(n)` giant.

### B24 — find the extremal object

The most informative obstruction is a two-scale host: a tiny dense spectral core together with a large well-connected but lower-degree bulk. The core sets `lambda(G)`; at `p=(1+epsilon)/lambda(G)` the bulk may still lie below its own percolation threshold. This is precisely why pair expansion alone cannot solve Question 5.1. Conversely, a block-diagonal family shows why deletion resilience alone cannot glue the seeds. The proved criterion is designed to exclude both extremal shapes separately.

## 5. Prior-art boundary

I do **not** claim novelty of the general seed/sprinkle philosophy or of percolation on expanders.

Relevant baselines checked this run include:

- Alon--Benjamini--Stacey (2004), which studies percolation on finite expanders and giant-component emergence in regular high-girth expanders;
- Chung--Horn--Lu, *Percolation in General Graphs* (Internet Mathematics), which proves giant-component results under spectral-gap and higher-degree-moment assumptions, with threshold expressed through the second-order average degree;
- the H0002 source itself, whose proof already iterates fixed-vertex exploration after deletions to amplify the probability of finding an `Omega(lambda)` component.

A bounded current search did not locate the exact two-axis hypothesis `(H1)+(H2)` with the displayed explicit source-density conclusion. That negative search is not a novelty certificate; the mechanism may be folklore or subsumed by a theorem under differently stated hypotheses. A deeper literature audit is required before any publication claim.

## 6. Source status and Beck--Fiala title reconciliation

The current H0002 primary source remains arXiv:2608.19145v1, submitted 19 Aug 2026. Its Question 5.1 remains the target of this run in the bounded current check.

The scheduler title's original Beck--Fiala target is no longer the correct active mathematical problem. For comparison:

- Bansal--Jiang, arXiv:2508.03961v2, prove `O(sqrt(t))` for `t>=log^2 n` and polylogarithmically weaker bounds below that regime;
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), claim the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce that every degree-`t` set system has discrepancy **strictly less than** `3 sqrt(2 pi t)` for every integer `t>=1`, with no restriction on `n`;
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), give a separately authored elementary simplification with Komlos constant `36`.

These are extremely recent preprint/technical-report results rather than mature refereed consensus, but on their stated theorems the complete uniform Beck--Fiala bound is now already available. R16 therefore correctly remains on its admitted outside successor instead of restarting the stale title.

## 7. Research status and next route

Status: **OPEN / PARTIAL**.

The source is not closed. The run proves one source-valid class of natural sufficient conditions and moves the frozen quantitative submetric, so the H0002 unchanged-run count is `0` and no stuck recovery is active.

No finite checker was manufactured: this run's claim is an asymptotic theorem proved on the page, not a finite enumeration claim. This follows the 90/10 rule rather than creating decorative certificate work.

The next nonrepeating Section-B triple is:

- **#3 PROVE SOMETHING STRONGER** — try to replace all-set deletion resilience by a simpler Perron delocalization condition that implies the same restart property;
- **#19 MAKE IT AN ALGORITHM** — turn the proof into an explicit certificate/recognition procedure for the host hypotheses or a constructive giant-finding exposure rule;
- **#30 ONE SCALE AT A TIME** — determine how far the pair-expansion scale can be lowered before the `2^{O(n/lambda)}` cut entropy defeats sprinkling.

The central next question is whether (H1) can be derived from a more transparent spectral non-localization parameter and whether (H2) can be weakened to one-sided isoperimetry without losing the exact `(1+epsilon)/lambda` density.

## 8. Runtime/control disclosure

The prompt requests GPT-6 with maximum reasoning, but this invocation actually exposes **GPT-5.6 Sol** and no authenticated reasoning-effort telemetry; the reasoning level is therefore **UNVERIFIED**. I do not claim GPT-6 or maximum reasoning.

The available task-control surface still exposes title/prompt, schedule or relative start, timing mode, enabled state and task identity, but no binding model-family or reasoning-effort selector and no authenticated applied-model receipt. Enforcing GPT-6/maximum would require an owner-authorized product/workspace/API/admin surface that exposes those controls and runtime attestation.

The historical P26 `You cannot modify this task` result is an authorization-context boundary. The lawful workaround is to edit from the owning/authorized account or workspace context, or escalate to platform/admin support; duplicating the task or bypassing permissions is not a valid workaround.

No scheduler state, email, Drive item, public post, permission, purchase, workflow, shared root ledger, or peer research file was modified.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  category: HARD_OUTSIDE
  predecessor:
    source_id: H0022
    state: TERMINAL_HANDOFF_AFTER_TWO_STUCK_RECOVERIES
    reopened: false
  successor:
    source_id: H0002
    source: "Christoph--Morawski--Wigderson, arXiv:2608.19145v1, Question 5.1"
    claim_path: operations/claims/H0002.md
    claim_creation_commit: 60097a996aff2836996fdac2808cc7ee58f7a83f
    source_status: OPEN
  metric:
    name: g_twoaxis(epsilon,rho,kappa)
    before: 0
    after: "(rho/64)*(1-exp(-epsilon^2/288))"
    movement: true
  theorem_status: PARTIAL
  methods_this_run: [2, 18, 24]
  next_methods: [3, 19, 30]
  unchanged_runs_on_H0002: 0
  stuck_recoveries_on_H0002: 0
  finite_checker: NOT_APPLICABLE_ASYMPTOTIC_PROOF_ON_PAGE
  prior_art_search: BOUNDED_CURRENT_SEARCH_RECORDED_NOT_NOVELTY_CERTIFICATE
  closure: false
  audits:
    P26: NOT_REQUESTED
    second_independent: NOT_REQUESTED
  shared_root_edits: NONE
  peer_file_edits: NONE
```

**End of immutable R16 run report.**