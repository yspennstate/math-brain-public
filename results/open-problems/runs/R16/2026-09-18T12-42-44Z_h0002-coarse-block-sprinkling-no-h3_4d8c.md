Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT + STRICT HYPOTHESIS WEAKENING:** H0002 `g_twoaxis(epsilon,rho,kappa): rho*(q_star-q0/64) -> rho*(q_127-q0/64)`, where `q0=1-exp(-epsilon^2/288)`, `eta_inf=epsilon*(7-epsilon)/8`, `q_127=1-exp(-((127/128)*eta_inf)^2/18)`; moreover the same theorem no longer needs frozen hypothesis (H3) `lambda(G)->infinity`. Section-B methods actually used: **#6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS**.

# R16 — H0002 fifth substantive run: coarse-block sprinkling, vanishing second-round budget, and removal of the spectral-growth hypothesis

## 1. Continuity, source, ownership, and required reads

This run continues the latest complete R16 chain on the exclusive HARD OUTSIDE target `H0002`, Question 5.1 of Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (submitted 19 Aug 2026). It does **not** reopen H0021/H0022 or the stale Beck--Fiala scheduler title.

Before research I reread/reconciled the required campaign/control surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the H-intake row for H0002, the canonical claim `operations/claims/H0002.md`, the newest R16 report

`runs/R16/2026-09-18T11-42-33Z_h0002-endpoint-seed-balanced-cut_91e4.md`,

and same-source neighboring G0010 records. The latest G0010 record is a handoff and does not alter H0002 ownership. I continue from the latest supported H0002 value rather than from the stale root R16/Beck--Fiala row.

There remains a repository ownership inconsistency: `operations/claims/H0018.md` separately names R16 as owner of a distinct SK Glauber target, while there is no H0018 R16 run report and no H0002 release/handoff. I do not invent a rotation or touch that claim. The complete H0002 chain remains the active research state used here; coordinator reconciliation is a shared-root task, not permission for R16 to edit claims.

Fresh web/source checks on 18 Sep 2026 still recover arXiv:2608.19145 under the same title/authors and no later source-matching resolution in the bounded search. Question 5.1 asks for natural conditions on a finite graph `G` implying that, for

`p >= (1+epsilon)/lambda(G)`,

`G_p` has a component of order `Omega(|G|)` with constant probability. Diskin--Erde--Kang--Krivelevich, *Percolation through Isoperimetry* (arXiv:2308.10267), remains a relevant regular growing-degree baseline, not a resolution of this irregular `1/lambda(G)` source question.

## 2. Frozen H0002 class and previous metric

Fix

`0<epsilon<=1`, `0<rho<=1`, `kappa>0`,

write `n=|G|`, `lambda=lambda(G)`, and define

`q0 := 1-exp(-epsilon^2/288)`,

`alpha := q0*rho/64`.

The canonical frozen class has

**(H1) spectral deletion resilience:** for every `S` with `|S|<=rho*n`,

`lambda(G-S) >= (1-epsilon/8)*lambda`;

**(H2) macroscopic pair expansion:** for all disjoint `A,B` with

`|A|,|B| >= alpha*n`,

`e_G(A,B) >= kappa*lambda*n`;

and originally

**(H3)** `lambda(G)->infinity`.

The preceding report proved

`g_prev = rho*(q_star-q0/64)`,

where

`eta_star = epsilon*(440-63*epsilon)/512`

and

`q_star = 1-exp(-eta_star^2/18)`.

The new argument proves the strictly larger concrete value

`g_new = rho*(q_127-q0/64)`,

with

`eta_inf := (1+epsilon)*(1-epsilon/8)-1 = epsilon*(7-epsilon)/8`,

`q_127 := 1-exp(-((127/128)*eta_inf)^2/18)`,

and it proves this on the **larger class obtained by dropping H3 entirely**.

Strict movement is elementary. In denominator 1024,

`(127/128)*eta_inf = epsilon*(889-127*epsilon)/1024`,

whereas

`eta_star = epsilon*(880-126*epsilon)/1024`.

Hence

`(127/128)*eta_inf - eta_star = epsilon*(9-epsilon)/1024 > 0`,

so `q_127>q_star` and therefore `g_new>g_prev`.

Because the frozen metric moved, the H0002 supported unchanged count is `0` after this run.

## 3. Method #6 — deform the sprinkling budget to the solvable endpoint scale

The preceding proof reserved a fixed fraction `epsilon/64` of the supercritical margin for the second round. That was unnecessary because H2 supplies `Theta(lambda*n)` candidate edges between any two macroscopic blocks. A second-round edge density of order `1/(lambda*n)` already gives a **constant** chance to connect one prescribed macroscopic pair.

By monotonicity it suffices to work at

`p=(1+epsilon)/lambda`,

whenever this lies in `[0,1]`; if `(1+epsilon)/lambda>1`, the source-threshold assertion is vacuous for that graph.

Define

`p1 := p - 1/(lambda*n) = (1+epsilon-1/n)/lambda`,

and choose `p2` through the independent two-round coupling

`1-p=(1-p1)(1-p2)`.

Then

`p2=(p-p1)/(1-p1) >= 1/(lambda*n)`.

Now set

`eta_inf := (1+epsilon)(1-epsilon/8)-1 = epsilon*(7-epsilon)/8`.

Fix any constant `sigma in (0,1)`. For all sufficiently large `n=n(epsilon,sigma)`,

`(1+epsilon-1/n)*(1-epsilon/8) >= 1 + sigma*eta_inf`.

Indeed the left side equals

`1+eta_inf-(1-epsilon/8)/n`,

so it suffices that

`n >= (1-epsilon/8)/((1-sigma)*eta_inf)`.

During an adaptive first-round exploration, before total deleted mass reaches `rho*n`, H1 therefore gives

`p1*lambda(G-S) >= 1+sigma*eta_inf`.

As in the preceding R16 reports, apply CMW Lemma 3.1(b) at a Perron-maximizing vertex of the residual graph. With parameter

`eta_sigma := sigma*eta_inf`,

that lemma gives conditional probability at least

`q_sigma := 1-exp(-eta_sigma^2/18)`

of obtaining a component larger than

`(eta_sigma/6)*lambda(G-S)`.

Using H1 once more, every such successful component has more than

`s_sigma := (eta_sigma/6)*(1-epsilon/8)*lambda`

vertices.

The endpoint adaptive seed lemma proved in the preceding R16 report requires no assumption that `R/s_sigma` diverges. Applying it with

`R=rho*n`, `q=q_sigma`, `s=s_sigma`

shows that, with probability at least a positive constant `c_end(q_sigma)>0`, the first round contains a union `U` of successful components of total mass

`W:=|U| >= q_sigma*rho*n`.

**Crucial point:** this first-round conclusion did not use `lambda->infinity`.

For the concrete metric movement in this report take

`sigma=127/128`.

Then `q_sigma=q_127` as defined above.

## 4. Method #13 — a monotone coarse-block closure process

The old sprinkling argument contracted every successful first-round component and union-bounded over all `2^m` cuts. That created an artificial entropy term and forced `m=o(n)`, hence H3. Instead, coarse-grain first and connect only a constant number of macroscopic blocks.

### Lemma 4.1 (coarse blocking with one small remainder)

Let disjoint pieces have total weight `W`, and fix `a>0`. Then either

1. one piece already has weight at least `W-a`; or
2. all but less than `a` of the total weight can be partitioned into blocks `B_1,...,B_r`, each a union of whole pieces and each having weight at least `a`. Moreover

`r <= W/a <= n/a`

when the pieces lie in an `n`-vertex ground set.

### Proof

If a piece has weight at least `W-a`, stop. Otherwise, every piece with weight at least `a` is made a block by itself. All remaining pieces have weight `<a`. Greedily accumulate those remaining pieces into a current block and close the block the first time its weight reaches `a`; every such closed greedy block has weight in `[a,2a)`. At the end there is at most one unfinished remainder, and its weight is `<a`. Thus all but `<a` total weight is covered by blocks of weight at least `a`. The number of blocks is at most total covered weight divided by `a`, hence at most `W/a` and therefore at most `n/a`. ∎

Apply this with

`a:=alpha*n=(q0*rho/64)*n`.

Since `q_sigma>q0`, on the endpoint seed event we have `W>=q_sigma*rho*n>64a`; in particular the lemma applies nontrivially.

If case 1 occurs, a single first-round component already has size at least

`W-a >= (q_sigma*rho-alpha)n`,

which is the desired final bound.

Otherwise obtain full blocks `B_1,...,B_r`, all satisfying

`|B_i|>=a=alpha*n`,

and covering total mass more than `W-a`. Furthermore

`r <= n/a = 1/alpha`,

which is a constant depending only on the frozen parameters `epsilon,rho` and **not** on `n` or `lambda`.

Now impose the deterministic chain

`B_1 -- B_2 -- ... -- B_r`.

For each link `(B_i,B_{i+1})`, H2 gives at least

`kappa*lambda*n`

host edges. Since

`p2 >= 1/(lambda*n)`,

the probability that this prescribed pair receives at least one second-round open edge is at least

`1-(1-p2)^(kappa*lambda*n) >= 1-exp(-kappa)`.

The edge sets belonging to distinct links of the chain are disjoint, even when two links share a block, so the corresponding second-round events are independent. Consequently, conditional on the first-round seed event, all `r-1` links open with probability at least

`(1-exp(-kappa))^(r-1)`

`>= (1-exp(-kappa))^(ceil(1/alpha)-1) =: c_tree(epsilon,rho,kappa) > 0`.

On this event the union of all full blocks lies in one second-round connected component. Its original-vertex mass is greater than

`W-a >= (q_sigma*rho-alpha)n`.

This process has an explicit monovariant: the total seed mass in the connected block-cluster containing `B_1` only increases as successive prescribed tree links open. No global cut analysis is needed.

## 5. Method #27 — swap the sprinkling quantifiers

The conceptual change is a quantifier swap.

The preceding architecture asked, after observing `m` random seed components,

> for **every** partition of those `m` components into two macroscopic sides, is there **some** sprinkling edge crossing it?

That requires controlling up to `2^m` random cuts and is the sole reason the prior proof needed `m=o(n)`.

The present architecture first deterministically compresses the seed family into at most `ceil(1/alpha)` macroscopic blocks, then asks only

> for each of the `r-1=O_{epsilon,rho}(1)` **predetermined** neighboring block pairs in one fixed spanning tree, is there some sprinkling edge between that pair?

H2 already quantifies over all macroscopic vertex pairs, so it applies to these selected pairs automatically. Probabilistically, however, the requirement has changed from exponentially many cuts to finitely many prescribed links. This is exactly why a `1/(lambda*n)` sprinkling density suffices and why no growth assumption on `lambda` is needed.

## 6. Main theorem of this run

### Theorem 6.1 (coarse-block two-axis giant criterion; H3 removed)

Fix `0<epsilon<=1`, `0<rho<=1`, `kappa>0`. Let `G=G_n` be any sequence of finite graphs satisfying H1 and H2 above. **No assumption that `lambda(G_n)->infinity` is required.**

For every fixed `sigma in (0,1)`, define

`eta_inf = epsilon*(7-epsilon)/8`,

`q_sigma = 1-exp(-(sigma*eta_inf)^2/18)`,

`q0 = 1-exp(-epsilon^2/288)`,

`alpha=q0*rho/64`.

Then, for all sufficiently large `n`, whenever

`p >= (1+epsilon)/lambda(G)`

is a valid percolation probability,

`P( L_1(G_p) >= rho*(q_sigma-q0/64)*n )`

is bounded below by the positive constant

`c_end(q_sigma) * (1-exp(-kappa))^(ceil(1/alpha)-1)`,

up to the harmless convention that if the first-round seed already contains one component of the target size, no sprinkling link is required.

In particular, choosing `sigma=127/128`,

`g_twoaxis(epsilon,rho,kappa)`

`>= rho*(q_127-q0/64)`,

where

`q_127 = 1-exp(-((127/128)*epsilon*(7-epsilon)/8)^2/18)`.

This strictly improves the preceding value `rho*(q_star-q0/64)`.

### Proof

Sections 3--5 give the complete proof. The first round yields seed mass at least `q_sigma*rho*n` with probability `c_end(q_sigma)>0`. Coarse blocking discards less than `alpha*n` seed vertices and produces at most `ceil(1/alpha)` full blocks. H2 and `p2>=1/(lambda*n)` give a fixed positive chance to open every edge of one prescribed block-chain. On that event the connected mass exceeds `(q_sigma*rho-alpha)n`. No step uses H3. ∎

### Endpoint envelope, stated honestly

Letting `sigma` increase to `1` shows that the **supremum of constants certified by this architecture** reaches

`rho*( 1-exp(-eta_inf^2/18) - q0/64 )`,

with

`eta_inf=epsilon*(7-epsilon)/8`.

I do **not** claim the endpoint itself from this argument: for each actual theorem one fixes `sigma<1`, and the lower probability constant may depend on that fixed `sigma`. The concrete tracked value is the `sigma=127/128` theorem above.

## 7. What genuinely changed, and what did not

### Genuine movement

1. The frozen giant-fraction metric strictly increases from

`rho*(q_star-q0/64)`

to

`rho*(q_127-q0/64)`.

2. The theorem simultaneously holds on a strictly larger graph class because frozen hypothesis H3 `lambda(G)->infinity` is unnecessary.

3. The second-round budget can be only `Theta(1/(lambda*n))`, rather than a fixed `Theta(1/lambda)` fraction of the supercritical margin.

4. The proof identifies the previous entropy term `2^m` as an artefact of asking for all cuts simultaneously; after coarse blocking, only `O(1)` prescribed links need to open.

### Remaining real barrier

H2 still requires **direct** macroscopic edge capacity between every pair of sufficiently large disjoint sets. Ordinary one-set isoperimetry does not mechanically imply this: a large boundary of `A` may be routed through a third reservoir rather than directly into a given large set `B`. The earlier `K_{2m,m}` diagnostic demonstrates the logical gap in that direct implication, though it is not a counterexample to giant formation.

Thus the next genuinely new question is no longer how to improve sprinkling constants. It is whether H2 can be replaced by a natural multi-hop connectivity condition (for example one-set isoperimetry plus a reservoir/closure argument) while retaining the exact `1/lambda(G)` source threshold.

## 8. Prior-art/current-source check

Fresh bounded checks on 18 Sep 2026:

- CMW arXiv:2608.19145 remains the source page recovered for *The critical probability for percolation on finite graphs*; no later source-matching solution to Question 5.1 was found in the bounded search.
- Diskin--Erde--Kang--Krivelevich, arXiv:2308.10267, proves a strong giant theorem under one-set isoperimetry for regular graphs of growing degree. This is important baseline machinery, not the same irregular `lambda(G)` hypothesis or the same theorem proved here.
- I did not locate the exact coarse-block `(H1)+(H2)` statement or the `1/(lambda*n)` prescribed-tree sprinkling formulation in this bounded search. This is **not** a novelty certificate. Coarse-graining, sprinkling, and spanning-tree connection arguments are standard techniques; novelty would require a deeper citation audit before publication claims.

The source remains **OPEN / PARTIAL**. This theorem supplies a stronger explicit sufficient condition package, not a classification of all natural conditions requested by Question 5.1.

## 9. Beck--Fiala stale-title reconciliation

The old scheduler title is no longer a live research gap. Fresh checks on 18 Sep 2026 show:

- Bansal--Jiang, arXiv:2508.03961, prove `O(sqrt(t))` for `t>=log^2 n` and polylogarithmically weakened bounds below that regime.
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger Komlos theorem with constant `3*sqrt(2*pi)` and explicitly conclude that every set system of maximum element degree `t` has discrepancy `< 3*sqrt(2*pi*t)` for every integer `t>=1`, with no restriction on `n`.
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), give an independent elementary proof of Komlos with constant `36`.

Therefore the complete current primary-claim baseline for the original R16 scheduler metric is already

`B(t,n) < 3*sqrt(2*pi*t)`

for every `t>=1,n`, assuming the very recent Guo--Fang--Lu preprint as stated. This is **KNOWN/current literature, not an R16 discovery**. The papers are extremely recent preprint/technical-report results rather than mature refereed consensus, so the correct action remains to record them as baselines rather than duplicate the pre-September Beck--Fiala gap.

## 10. Validation discipline

No checker was created. This run introduced theorem-sized analytic claims with full proofs on the page and no finite computational core. Under the owner's 90/10 rule, manufacturing an exact checker merely to produce another certificate would be backwards.

The key arithmetic comparisons are transparent symbolic identities:

`eta_inf = epsilon*(7-epsilon)/8`,

`(127/128)*eta_inf - eta_star = epsilon*(9-epsilon)/1024 > 0`.

The probabilistic inequalities used are written explicitly in Sections 3--6.

## 11. Next methods and stuck state

Because the metric moved, H0002 is not stuck and the supported unchanged count is `0`. No recovery is active.

The next nonrepeating Section-B moves should be:

- **#7 TAKE THE LIMIT:** identify the weakest limiting one-set expansion/reservoir property sufficient to connect the coarse blocks;
- **#15 BREAK THE SYMMETRY ON PURPOSE:** study hosts where macroscopic blocks communicate only through a distinguished reservoir, rather than direct pair expansion;
- **#25 COUNT THE SAME THING TWICE:** count successful block-to-reservoir connectors both from the block side and from the reservoir side to seek a multi-hop replacement for H2.

The binary next target is: either prove a source-valid giant theorem with H2 replaced by a standard one-set isoperimetric/multi-hop condition, or produce a concrete family showing that the current spectral-resilience plus one-set expansion package is insufficient at the exact `1/lambda(G)` scale.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  target: H0002
  source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1
  lane: HARD_OUTSIDE
  status_before: PARTIAL_SOURCE_OPEN
  status_after: PARTIAL_SOURCE_OPEN
  metric: g_twoaxis(epsilon,rho,kappa)
  q0: 1-exp(-epsilon^2/288)
  eta_inf: epsilon*(7-epsilon)/8
  sigma_concrete: 127/128
  q_127: 1-exp(-((127/128)*eta_inf)^2/18)
  value_before: rho*(q_star-q0/64)
  q_star: 1-exp(-(epsilon*(440-63*epsilon)/512)^2/18)
  value_after: rho*(q_127-q0/64)
  movement: STRICT_INCREASE
  additional_movement: REMOVE_H3_lambda_to_infinity
  unchanged_count_after: 0
  methods_used: [6,13,27]
  next_methods: [7,15,25]
  source_closed: false
  closure_claimed: false
  checker_created: false
  reason_no_checker: theorem-sized analytic claim; full proof on page; no finite core
  h0018_conflict: preserved_no_rotation_invented
  shared_root_edits: none
  peer_file_edits: none
  scheduler_changes: none
```

## 13. Model / scheduler / permission reality

This report was actually generated by **GPT-5.6 Sol**. The runtime does not authenticate a reasoning-effort setting, hence `UNVERIFIED`; I do not claim GPT-6/maximum.

The exposed automation/task-control surface continues to offer task prompt/title, schedule/start, timing mode, enabled state and identity, but no binding model-family selector, reasoning-effort selector, or authenticated per-run applied-model receipt. Enforcing GPT-6/maximum would require an authorized scheduler/API surface exposing those fields plus execution attestation.

For task IDs that return `You cannot modify this task`, the compliant workaround remains modification from the owning authorized workspace/account context or escalation to platform support. Repository edits, duplicate tasks, or permission bypass are not scheduler repairs.

No email, Drive action, public posting, purchase, permission change, workflow execution, scheduler edit, shared-root edit, or peer-track edit was performed in this run.
