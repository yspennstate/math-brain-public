Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT:** H0002 `g_twoaxis(epsilon,rho,kappa)` remains at the last supported concrete value `rho*(q_128-q0/64)` with asymptotic supremum `rho*(q_inf-q0/64)`; this run proves a new source-valid Perron-profile spectral criterion implying the frozen H1/H2 hypotheses and improves the repaired endpoint approach from `O(lambda^(-1/2))` to `O(lambda^(-1))` at constant success probability. Section-B methods actually used: **#1 CHANGE THE CATEGORY, #14 FIND THE GROUP ACTING, #22 READ THE FAILURES**.

# R16 — H0002: Perron-profile spectral criterion and an `O(1/lambda)` endpoint approach

## 1. Continuity, ownership, and required reads

This run continues the active R16 HARD OUTSIDE claim `H0002`, Question 5.1 of Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026). It does **not** restart the stale Beck--Fiala scheduler title, reopen H0022, or switch targets.

Before research I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/H0002.md`;
- the H-intake verification for arXiv:2608.19145 Question 5.1;
- the newest own R16 report `runs/R16/2026-09-18T14-58-00Z_h0002-asymptotic-endpoint-proof-repair_c7e4.md`;
- the newest visible same-source neighboring handoff context for G0010 / G0011.

The canonical frozen H0002 class is still:

- `0 < epsilon <= 1`, `0 < rho <= 1`, `kappa>0`, `n=|G|`, `lambda=lambda(G)`;
- `q0 := 1-exp(-epsilon^2/288)`, `alpha0 := q0*rho/64`;
- **H1:** `lambda(G-S) >= (1-epsilon/8) lambda` for every `|S|<=rho*n`;
- **H2:** `e_G(A,B) >= kappa*lambda*n` for all disjoint `A,B` with `|A|,|B|>=alpha0*n`;
- **H3:** `lambda(G)->infinity`.

The tracked quantity remains the largest explicit giant fraction uniformly certified on this frozen class at

`p >= (1+epsilon)/lambda(G)`

with probability bounded below by a positive constant depending only on the frozen parameters.

The preceding correction report is controlling: the coarse artificial-block gluing was invalid and withdrawn; the sound gluing state space is the quotient by the **actual first-round connected components**.

Fresh source checks on 18 Sep 2026 still find arXiv:2608.19145v1 as the current CMW version. Its Question 5.1 asks exactly for natural conditions giving a linear giant at `(1+epsilon)/lambda(G)` and explicitly warns that ordinary robust connectivity can miss localization of the spectral radius.

## 2. Fresh prior-art / failure reading

Three current baselines matter to this run.

1. **Christoph--Morawski--Wigderson (2026), Question 5.1.** They identify spectral localization as the reason a generic robust-connectivity assumption is unlikely to suffice.

2. **Diskin--Erde--Kang--Krivelevich, `Percolation through Isoperimetry`.** Their negative construction shows that even a fixed positive ordinary edge-isoperimetric constant can coexist with no linear giant at `p=C/d` on suitable growing-degree regular graphs. Thus merely replacing H2 by a weak one-set boundary lower bound cannot solve the source problem.

3. **Abiad--Zeijlemaker, `A unified framework for the Expander Mixing Lemma for irregular graphs and its applications` (LAA 2024; arXiv:2401.07125).** Perron-eigenvector versions of irregular expander mixing are established literature. Therefore the spectral decomposition mechanism below is **not** claimed as new. What is new within R16 is the explicit reduction from two Perron-profile quantities to the already proved H0002 giant criterion. A bounded search did not locate this exact percolation corollary, but that is not a novelty certificate.

Chung--Horn--Lu's `Percolation in General Graphs` remains the nearest older general-graph giant result, but its threshold is phrased in terms of the second-order average degree and its giant-size notion is not the cardinality statement requested by CMW.

## 3. Method #1 — change category: replace graph hypotheses by two Perron profiles

Let `G` be connected, with adjacency matrix `A`, spectral radius `lambda=lambda_1`, normalized positive Perron vector `v`, and

`Lambda := max_{i>=2} |lambda_i|`, `theta := Lambda/lambda`.

For fixed `rho,alpha in (0,1)` define the two profiles

`U_rho(v) := max_{|S|<=rho*n} sum_{x in S} v_x^2`,

`L_alpha(v) := min_{|S|>=alpha*n} (1/sqrt(n)) sum_{x in S} v_x`.

`U_rho` measures **small-set l2 localization** of the Perron mass. `L_alpha` measures whether every macroscopic vertex set carries a non-negligible amount of Perron l1 mass.

These are exactly the two axes suggested by the source obstruction: one prevents a tiny spectral core from governing `lambda(G)`, and the other turns an adjacency spectral gap into direct macroscopic pair mixing.

### Proposition 3.1 — Perron profile implies H1

If

`U_rho(v) <= epsilon/(8+epsilon)`,

then for every `S` with `|S|<=rho*n`,

`lambda(G-S) >= (1-epsilon/8) lambda(G)`.

#### Proof

Fix such `S`, put `T=V\S`, and let

`m := sum_{x in S} v_x^2`.

Restrict `v` to `T`. Since `Av=lambda v`, the total quadratic form contributed by terms touching `S` is at most `2 lambda m`, and therefore

`v_T^T A[T] v_T >= lambda(1-2m)`.

Also `||v_T||_2^2=1-m`. By the Rayleigh principle,

`lambda(G-S) >= lambda * (1-2m)/(1-m)`.

For `m<=epsilon/(8+epsilon)`,

`(1-2m)/(1-m) >= 1-epsilon/8`.

This is H1. QED.

### Proposition 3.2 — Perron profile plus spectral gap implies H2

Fix `alpha in (0,1/2]` and put `L:=L_alpha(v)`. If

`kappa_spec := L^2 - theta/2 > 0`,

then every pair of disjoint sets `A,B` with `|A|,|B|>=alpha*n` satisfies

`e_G(A,B) >= kappa_spec * lambda * n`.

#### Proof

Write the spectral decomposition

`A = lambda v v^T + E`,

where `||E||_op=Lambda`. For disjoint `A,B`, with indicator vectors `1_A,1_B`,

`e_G(A,B) = 1_A^T A 1_B`

`= lambda <1_A,v><1_B,v> + 1_A^T E 1_B`.

By definition of `L`,

`<1_A,v>, <1_B,v> >= L sqrt(n)`.

Hence the Perron term is at least `lambda L^2 n`. The error term obeys

`1_A^T E 1_B >= -Lambda sqrt(|A||B|)`.

Because `A,B` are disjoint, `|A|+|B|<=n`, so

`sqrt(|A||B|) <= n/2`.

Therefore

`e_G(A,B) >= lambda L^2 n - (Lambda n)/2`

`= (L^2-theta/2) lambda n`

`= kappa_spec lambda n`.

This is H2. QED.

### Theorem 3.3 — a natural spectral sufficient condition for CMW Question 5.1

Retain the canonical

`q0=1-exp(-epsilon^2/288)`, `alpha0=q0*rho/64`.

Suppose along a graph sequence:

1. `lambda(G)->infinity`;
2. `U_rho(v) <= epsilon/(8+epsilon)`;
3. with `L=L_alpha0(v)` and `theta=Lambda/lambda`,
   `L^2-theta/2 >= kappa_* > 0` uniformly.

Then the graph sequence satisfies the canonical frozen H1--H2--H3 hypotheses with `kappa=kappa_*`. Consequently all of the **repaired** R16 H0002 conclusions apply. In particular, with

`a := 1-epsilon/8`,

`eta_inf := epsilon*(7-epsilon)/8`,

`q_inf := 1-exp(-eta_inf^2/18)`,

the percolated graph at every

`p >= (1+epsilon)/lambda(G)`

has, with probability bounded below by a positive constant, a component of asymptotic fraction arbitrarily close from below to

`g_inf := rho*(q_inf-q0/64)`.

The proof is exactly Propositions 3.1 and 3.2 followed by the repaired H0002 all-cut theorem from the previous report. No artificial disconnected macroblocks are used.

This is a source-valid PARTIAL answer to Question 5.1: it gives an explicit spectral family of natural sufficient conditions addressing both localization and global mixing. It is not claimed to characterize the optimal class.

## 4. Coordinate-flat corollary

A simpler but stronger checkable form follows immediately. Suppose

`c/sqrt(n) <= v_x <= C/sqrt(n)`

for every vertex. Then

`U_rho(v) <= C^2 rho`,

and

`L_alpha(v) >= c alpha`.

Hence it suffices that

`C^2 rho <= epsilon/(8+epsilon)`

and

`Lambda/lambda < 2 c^2 alpha0^2`.

Under these conditions and `lambda->infinity`, the same linear-giant conclusion follows at the exact CMW spectral threshold `(1+epsilon)/lambda`.

The important point is conceptual rather than the constant: **upper Perron flatness prevents spectral localization; lower Perron flatness plus a non-Perron adjacency spectral gap forces macroscopic pair mixing.**

## 5. Method #14 — find the group acting

Every automorphism `P` of `G` commutes with `A`. Because the positive Perron eigenvector is unique after normalization,

`Pv=v`.

Therefore `v` is constant on every automorphism orbit. This gives an immediate symmetry reduction of the two Perron profiles to orbit-level data.

For a vertex-transitive graph, `v=n^(-1/2) 1`, hence

`U_rho(v) <= rho`,

`L_alpha(v) >= alpha`.

Thus for a `d`-regular vertex-transitive graph with `d->infinity`, the criterion above reduces to the explicit conditions

`rho <= epsilon/(8+epsilon)`

and

`max_{i>=2}|lambda_i|/d < 2 alpha0^2`.

This regular symmetric special case lies squarely in classical pseudorandom-percolation territory and is **not** presented as a novel theorem. Its purpose here is diagnostic: symmetry automatically kills the localization obstruction, while the nontrivial remaining axis is pair mixing.

The same calculation also explains why symmetry alone is insufficient. Balanced complete bipartite graphs are vertex-transitive and have perfectly flat Perron vectors, but they carry the eigenvalue `-lambda`, so the absolute non-Perron ratio is `1`; moreover two large sets in the same side have zero direct edges. Thus the two axes are genuinely independent.

## 6. Method #22 — read the failures: what existing counterexamples force any criterion to contain

The source and the isoperimetric counterexamples point to two separate failure modes.

### Failure mode A: spectral localization

CMW explicitly note that a graph can have an induced subgraph on `(1-o(1))n` vertices with spectral radius much smaller than `lambda(G)`. Then `p=(1+epsilon)/lambda(G)` is still subcritical on most vertices. A connectivity assumption that ignores the Perron mass can miss this completely.

`U_rho(v)` targets exactly this obstruction: it says no set of at most `rho n` vertices captures enough Perron `l2` mass to cause a large drop in spectral radius when deleted.

### Failure mode B: ordinary isoperimetry without pair mixing

Diskin--Erde--Kang--Krivelevich construct regular graphs with a positive constant ordinary isoperimetric lower bound for which, at `p=C/d`, all components are still `o(n)` whp. Therefore a criterion of the form “every set has at least `h|S|` boundary edges” cannot by itself replace the pair-mixing axis at the exact source scale.

`L_alpha(v)^2-theta/2>0` is stronger and more targeted: it guarantees **direct** edge capacity between every two disjoint macroscopic sets through the Perron term, after controlling the entire orthogonal spectrum.

The lesson from the failed routes is now precise: the source question needs one hypothesis that prevents localization of the top eigenvalue and another that prevents the remaining Perron-delocalized mass from being arranged in a macroscopically separated way.

## 7. Secondary quantitative improvement on the frozen class: endpoint gap `O(1/lambda)`

This does **not** change the fixed constant metric `g_twoaxis`, whose asymptotic supremum was already identified in the preceding repaired report. It does materially sharpen the convergence rate to that endpoint.

Recall

`a = 1-epsilon/8`,

`eta_inf = epsilon*(7-epsilon)/8`,

`q_inf = 1-exp(-eta_inf^2/18)`,

`g_inf = rho*(q_inf-q0/64)`.

The repaired all-cut proof contracts actual first-round components. If the first-round margin is at least `eta_inf/2`, then every successful seed component has size at least

`(a*eta_inf/12) lambda`,

so the number `m` of successful quotient vertices satisfies

`m <= [12/(a*eta_inf)] n/lambda`.

Hence the total cut entropy is at most

`2^m <= exp(C0*n/lambda)`,

where

`C0 := 12 log(2)/(a*eta_inf)`.

Fix once and for all `s=log 2`, and for all sufficiently large `lambda` reserve

`theta_lambda := (C0+s)/(kappa*lambda)`

of the supercritical numerator for round two, i.e.

`p1 := (1+epsilon-theta_lambda)/lambda`,

`1-p=(1-p1)(1-p2)`.

Then

`p2 >= theta_lambda/lambda`.

For every H2 macroscopic quotient cut, the number of candidate host edges is at least `kappa*lambda*n`, so the probability that the cut receives no round-two edge is at most

`exp(-kappa*theta_lambda*n)`

`= exp(-(C0+s)n/lambda)`.

Union-bounding over all quotient cuts gives total conditional gluing failure at most

`exp(-s*n/lambda) <= exp(-s)=1/2`,

because always `lambda<=n-1`.

Thus, unlike the previous `theta_lambda=lambda^(-1/2)` choice, we need only a reserve of order `1/lambda` to obtain a **uniform constant** gluing probability; making the gluing failure `o(1)` was stronger than the fixed metric requires.

The first-round residual margin is

`eta_lambda = eta_inf-a*theta_lambda`.

With `q(x)=1-exp(-x^2/18)`,

`q'(x)=(x/9)exp(-x^2/18) <= eta_inf/9`,

so

`q_inf-q(eta_lambda) <= (a*eta_inf/9) theta_lambda`.

The endpoint adaptive seed lemma from the valid 11:42 line gives successful seed mass at least `rho*q(eta_lambda)n` with a uniformly positive probability for all sufficiently large `lambda`. Combining with the `>=1/2` conditional gluing probability yields

`P( L1(G_p)/n >= g_inf - D/(lambda) ) >= c_*(epsilon,rho)/2`,

where the explicit constant is

`D := [rho*a*eta_inf/(9*kappa)] * (C0+log 2)`

`   = [rho*log 2/(9*kappa)] * (12+a*eta_inf)`.

So the repaired endpoint approach improves from

`g_inf - O_epsilon,rho,kappa(lambda^(-1/2))`

to

`g_inf - O_epsilon,rho,kappa(lambda^(-1))`

at the probability level actually required by the frozen metric.

This is a real quantitative improvement, but because `g_twoaxis` records a **constant** giant fraction rather than the convergence rate, I do not relabel it as fixed-metric movement.

## 8. Beck--Fiala scheduler-title reconciliation

The native title is stale and is not the active source claim. Current primary literature still makes the original Beck--Fiala target a baseline rather than an open R16 problem:

- Bansal--Jiang, arXiv:2508.03961, prove `O(sqrt(t))` in the regime `t>=log^2 n`, with additional logarithmic losses below that range.
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger real Komlos bound `3 sqrt(2 pi)` and explicitly derive
  `disc(F) < 3 sqrt(2 pi t)` for every integer `t>=1`, with no `n` restriction.
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), give an independent elementary proof of Komlos with constant `36`.

These are extremely recent manuscripts/technical reports, not mature refereed consensus. But on their stated theorems the old all-`t,n` Beck--Fiala gap is currently superseded. R16 therefore continues H0002 under its canonical exclusive claim instead of duplicating the pre-September discrepancy problem.

## 9. Prior-art honesty

The following mechanisms are established literature and are **not** claimed as R16 novelties:

- Perron-weighted / irregular expander-mixing inequalities;
- percolation on regular pseudorandom graphs;
- seed-and-sprinkle arguments;
- the Diskin--Erde--Kang--Krivelevich positive and negative isoperimetric results.

What this run adds internally is:

1. the exact two-profile reduction `(U_rho, L_alpha, Lambda/lambda) -> (H1,H2)` with explicit constants;
2. the resulting natural spectral sufficient condition at the CMW `1/lambda(G)` threshold on the active H0002 line;
3. the symmetry/orbit interpretation of that criterion;
4. the sharper `O(1/lambda)` approach to the already identified frozen-class endpoint, obtained by asking only for constant gluing probability rather than `1-o(1)` gluing probability.

A bounded 18 Sep 2026 search did not locate this exact combined statement. That is not proof of novelty.

## 10. Metric, status, stuck counter, and next methods

Fixed metric before:

`g_twoaxis concrete supported value = rho*(q_128-q0/64)`;

asymptotic supremum from the repaired report:

`g_inf = rho*(q_inf-q0/64)`.

Fixed metric after: **same**.

Therefore this run is honestly **NO FIXED-METRIC MOVEMENT**, despite the new source-valid criterion and improved endpoint convergence rate.

Supported unchanged count: `0 -> 1`.

Status: **PARTIAL / SOURCE OPEN / ACTIVE**.

No stuck recovery is triggered.

Next nonrepeating Section-B methods:

- **#3 PROVE SOMETHING STRONGER:** try to replace absolute adjacency spectral gap by a weaker one-sided or nonbacktracking mixing condition that still gives direct macroscopic pair capacity;
- **#17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE:** compare the threshold `L_alpha(v)^2 > (Lambda/lambda)/2` with Perron-weight discrepancy / irregular expander-mixing constants and with dense graphon spectral criteria;
- **#23 DO WHAT THE PROPOSER DID NOT EXPECT:** test whether a useful sufficient condition can allow strong bipartiteness (`lambda_n approx -lambda`) by replacing direct pair mixing with a two-step Perron kernel `A^2` and a genuinely connected two-hop sprinkling argument.

## 11. Model / scheduler control limits

The model-control limitation is still unchanged. The task-control surface exposed in this runtime permits title/prompt, schedule/start offset, timing mode, enablement and task identity. It exposes **no binding model-family selector, no reasoning-effort selector, and no authenticated per-run applied-model receipt**. GPT-6/maximum is therefore prompt-only here.

To enforce GPT-6/maximum would require the authorized scheduler/API itself to expose those fields plus runtime attestation. Repository edits cannot repair this.

The historical P26 `You cannot modify this task` error was authorization-context-specific; the current root ledger records that a later P26 update succeeded from an authorized context. If a task still returns that denial, the compliant route is the owning authorized workspace/account or platform support, never duplication or permission bypass.

## ledger_delta

```yaml
ledger_delta:
  worker: R16
  target: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608.19145v1_Question_5.1
  lane: HARD_OUTSIDE
  status_before: PARTIAL_SOURCE_OPEN_ACTIVE
  status_after: PARTIAL_SOURCE_OPEN_ACTIVE
  fixed_metric: g_twoaxis(epsilon,rho,kappa)
  metric_before: rho*(q_128-q0/64)
  metric_after: rho*(q_128-q0/64)
  metric_movement: false
  asymptotic_supremum: rho*(q_inf-q0/64)
  secondary_quantitative_progress:
    endpoint_gap_before: O(lambda^(-1/2))
    endpoint_gap_after: O(lambda^(-1))
    success_probability: positive_constant_uniform
  new_source_valid_result:
    name: Perron-profile spectral criterion
    localization_profile: U_rho(v) <= epsilon/(8+epsilon)
    mixing_profile: L_alpha0(v)^2 - (Lambda/lambda)/2 >= kappa_star > 0
    consequence: frozen H1-H2-H3 and linear giant at p>=(1+epsilon)/lambda
  unchanged_count_before: 0
  unchanged_count_after: 1
  section_B_methods: [1,14,22]
  next_methods: [3,17,23]
  beck_fiala_current_baseline:
    bound: "B(t,n) < 3*sqrt(2*pi*t)"
    restrictions: "all integer t>=1, all n, per Guo-Fang-Lu arXiv:2609.11189v1"
    status: "very recent current-literature baseline; not an R16 result"
  delivery:
    repository: yspennstate/math-open-problems
    branch: master
    report_path: runs/R16/2026-09-18T15-52-39Z_h0002-perron-profile-spectral-criterion_4e91.md
```
