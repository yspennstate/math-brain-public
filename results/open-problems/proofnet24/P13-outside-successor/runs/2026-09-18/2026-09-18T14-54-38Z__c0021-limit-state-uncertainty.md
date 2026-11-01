Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `W_sigma = 0.083465753913852208758272209478431... -> 0.083465753913852208758272209478431...`; C0021 unchanged-run streak `0 -> 1`. Methods actually tried: B7, B13, B30.**

# P13 C0021 — limiting-state obstruction, posterior uncertainty, and one-scale residual geometry

Date: 2026-09-18 UTC. Track: P13 Outside Counterexample Research. Native slot: `6aa7b253b37c8191b693d8dc79298d37`. Own root: `proofnet24/P13-outside-successor/`.

## 1. Recovered state, ownership, and exclusions

The active create-only claim remains `operations/claims/C0021.md`: Garban--Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Part VIII Exercise VIII.5, the revealment exponent of iterated 3-majority. The claim still names this P13 native slot and no competing C0021 ownership marker was recovered.

The source reduction already proved in the repository is

```text
delta_{f_k} = D_k / 3^k,
c = lim_k D_k^(1/k),
sigma = 1 - log_3(c),
```

where `D_k` is the minimum expected number of queried leaves, under the uniform product input law, among zero-error decision trees evaluating depth-`k` recursive 3-majority. The frozen source-faithful metric is the width of one rigorous interval for this single source exponent `sigma`, target zero.

The newest preceding P13 report, `2026-09-18T13-05-52Z__c0021-parameter-symmetry-mdp-movement.md`, gave the explicit depth-4 policy bound

```text
U_4 = 1332517664326644559 / 36028797018963968
```

and hence

```text
sigma >= 0.1783937532290626654407820192070906898593985836476...
sigma <= 0.2618595071429148741990542286855217085991712802638...
W_sigma = 0.0834657539138522087582722094784310187397726966161...
```

Only a rigorous change to one of those source-domain endpoints counts as movement. This run did not obtain such a change.

The owner-required exclusions were preserved. Retired I0051 was not reopened. Handed-off P0082 was not reopened. Six-run-handed-off D0093 was not reopened. Peer-owned I0054 was not touched. The repository policy, campaign INDEX/RANKING, root POSTED/RESULTS, active C0021 claim, newest P13 report, and the prior C0021 exact artifacts were re-read before the new work. Historical shared ledgers were not edited.

## 2. Source and literature refresh — 2026-09-18

The original exercise was rechecked in the author-hosted/Clay text. Exercise VIII.5 asks what can be said about the revealments of iterated 3-majority and explicitly says they decay as `1/n^sigma` for some `sigma`, while determining `sigma` is an open question in that source.

Dated bounded web queries included:

```text
"Exercise VIII.5" "iterated 3-Majority" revealment
"iterated 3-majority" revealment sigma Garban Steif 2026
"recursive majority" expected number queries uniform distribution 2026
"Minimizing the time to a decision" recursive majority Jacka Warren Windridge
```

The closest structural prior art remains Jacka--Warren--Windridge, *Annals of Applied Probability* 21 (2011), 1795--1826, which solves a continuous three-diffusion majority scheduling problem and discusses recursive-majority query-cost growth but does not determine this discrete asymptotic constant. The 2026 majority-tree search hits found during this bounded pass concern different problems such as reducing a bag of decision trees and do not match the uniform expected zero-error recursive-majority cost here. No checked source in this bounded pass supplied the exact source exponent. This is bounded negative search evidence only; it is not a worldwide openness or novelty certificate.

## 3. Idea before computation

The preceding two runs improved a finite depth-4 policy by patching concrete Bellman defects. That moved the source metric, but it risks degenerating into ever-deeper finite patching. This run deliberately changed viewpoint.

- **B7 — TAKE THE LIMIT.** Ask whether a small scale-free state variable controls the optimal recursive-majority policy. The most tempting candidate is `(posterior p, optimal remaining cost V)`. If that pair closed under optimal transitions, one could hope for a limiting Markov control or transfer operator.
- **B13 — FIND WHAT ONLY INCREASES.** Search for a monotone quantity of the adaptive child posteriors. Two odd orientation coordinates suggested by the previous bias calculation fail monotonicity, but posterior uncertainty has an exact supermartingale law. This leads to a universal terminal identity for the unfinished child.
- **B30 — ONE SCALE AT A TIME.** Solve the complete residual geometry for the first three outer scales `h=0,1,2`, preserving the third child at the instant the outer majority is decided. This tests exactly which state restrictions are true on the optimal residual support and which fail globally.

The main mathematical outcome is not a new exponent endpoint. It is a sharper state-space obstruction plus an exact universal identity that isolates the next plausible source-moving lemma.

## 4. B7 — the pair `(posterior, remaining cost)` does not close the optimal dynamics

Represent a partially revealed recursive-majority subtree by a canonical state `s`. Let

```text
p(s) = P(subtree output = + | revealed transcript),
V(s) = minimum expected additional number of leaf queries needed to determine it.
```

For the initial depth-`h` subtree write `D_h = V(full_h)`. Exact Bellman recursion gives

```text
D_1 = 5/2,
D_2 = 393/64,
D_3 = 15796051/1048576.
```

Consider every state reachable from the initial depth-3 tree by repeatedly taking an optimal Bellman action, retaining all ties. Exact enumeration gives 499 states, of which 497 are nonterminal. Every one of those 497 nonterminal states has a **unique** optimal next-query orbit.

I then grouped those 497 states by the pair `(p,V)`. There are exactly six collisions. Every collision has size two, and each pair consists of global-sign conjugates. Therefore `(p,V)` is not an injective description even on the unique optimal depth-3 policy graph.

More importantly, the collision is dynamically real rather than merely a duplicate encoding. One exact pair is

```text
S = (
  (-, (u,u,u), (u,u,u)),
  ((+,u,u), (+,u,u), (u,u,u)),
  ((+,u,u), (-,u,u), (u,u,u))
),
```

with `J(S)` its global sign flip. Both satisfy

```text
p(S) = p(J(S)) = 1/2,
V(S) = V(J(S)) = 2335/256.
```

But under their unique optimal next queries the `+/-` successor data are reversed in cost:

```text
S:
  + successor: p = 153/256, V = 33369/4096,
  - successor: p = 103/256, V = 33159/4096;

J(S):
  + successor: p = 153/256, V = 33159/4096,
  - successor: p = 103/256, V = 33369/4096.
```

Thus the pair `(p,V)` does not determine the one-step optimal transition kernel. Any limiting control law that retains only current output posterior and current completion value loses an orientation variable already at depth three.

### 4.1 Two exact orientation coordinates

For the unique optimal policy on these depth-3 reachable states, let `V_r^pi(s)` denote its expected remaining query cost if unrevealed leaves are Bernoulli-`r`, while the policy itself is frozen. Define the unbiased bias derivative

```text
K(s) = d/dr V_r^pi(s) |_{r=1/2}.
```

If the chosen query has `+/-` successors `a,b`, then the finite-tree differentiation identity is

```text
K(s) = V(a) - V(b) + [K(a)+K(b)]/2.
```

Also define the outcome-cost skew

```text
H(s) = E[C 1_{Y=+} | s] - E[C 1_{Y=-} | s]
```

for the same fixed policy and subtree output `Y`. Its recursion is

```text
H(s) = 2p(s)-1 + [H(a)+H(b)]/2.
```

For the collision above,

```text
K(S) =  31/2048,   K(J(S)) = -31/2048,
H(S) =  19/256,    H(J(S)) = -19/256.
```

Exact enumeration yields a useful finite fact:

> **Finite state-separation fact.** On all 497 nonterminal states in the depth-3 optimal-reachable graph, both maps `s -> (p(s),V(s),K(s))` and `s -> (p(s),V(s),H(s))` are injective.

This does **not** establish that either triple is sufficient at arbitrary depth. It says that a single odd orientation coordinate resolves every `(p,V)` ambiguity at the first nontrivial scale tested. That is the positive B7 signal.

B7 therefore partly failed and partly worked. The naive two-coordinate limiting state is rigorously insufficient. A three-coordinate oriented state remains plausible and is now the smallest concrete candidate supported by the exact finite graph.

## 5. B13 — posterior uncertainty is a genuine monovariant

The obvious orientation magnitudes are not monovariants. Along the 497-state unique optimal depth-3 policy graph, exact comparison of the current magnitude with the average successor magnitude gives

```text
|K|: successor average increases at 174 states,
     decreases at 320 states,
     is equal at 3 states;

|H|: successor average increases at 194 states,
     decreases at 302 states,
     is equal at 1 state.
```

So neither `|K|` nor `|H|` is a submartingale or supermartingale even on this finite optimal graph.

The successful monovariant is simpler. For a child Boolean output `Y in {+1,-1}`, let

```text
m = E[Y | current transcript],
U = 1 - m^2 = 4p(1-p).
```

Because `m` is a bounded martingale under further queries,

```text
E[U_next | F] = U - Var(m_next | F) <= U.
```

Thus posterior uncertainty is a supermartingale, with an exact drift equal to the newly created posterior variance.

The more useful result comes from applying this simultaneously to the three child outputs of the outer majority.

### Theorem 5.1 — residual-child magnetization identity

Let `Y_1,Y_2,Y_3` be the outputs of three independent unbiased Boolean subproblems, each taking values in `{+1,-1}`. Let an arbitrary finite adaptive zero-error algorithm query information from one child at a time until the majority sign

```text
R = Maj(Y_1,Y_2,Y_3)
```

is logically determined. Write

```text
m_i(t) = E[Y_i | F_t].
```

At the stopping time `tau`, choose two children whose outputs have been determined to equal `R`, and let `J` be the remaining child. Then

```text
E[R m_J(tau)] = -1/2.                 (5.1)
```

Consequently,

```text
E[ P(Y_J = R | F_tau) ] = 1/4,        (5.2)
E[m_J(tau)^2] >= 1/4,                 (5.3)
E[1-m_J(tau)^2] <= 3/4.               (5.4)
```

#### Proof

Each `m_i(t)` is a martingale. Since every elementary query reveals information from only one child, for `i != j` the product `m_i m_j` is also a martingale: if child `i` is queried then `m_j` is unchanged and

```text
E[m_i(t+1)m_j(t+1) | F_t]
 = m_j(t) E[m_i(t+1)|F_t]
 = m_i(t)m_j(t),
```

and the other cases are identical. Therefore

```text
Z_t = m_1(t)m_2(t) + m_1(t)m_3(t) + m_2(t)m_3(t)
```

is a bounded martingale. Initially all three unbiased child magnetizations are zero, so `Z_0=0` and hence `E Z_tau=0`.

A zero-error majority decision cannot be certified unless at least two child outputs are themselves forced to the decided sign `R`: if fewer than two were forced to `R`, disjointness of the child input sets would allow two children to be completed to `-R`, contradicting that the root value is fixed. Choose such two children and call the third `J`. Their terminal magnetizations are both exactly `R`, hence

```text
Z_tau = R^2 + R m_J + R m_J = 1 + 2R m_J.
```

Taking expectations and using `E Z_tau=0` proves (5.1).

Given `F_tau`, the probability that the residual child agrees with the root is `(1+R m_J)/2`. Taking expectations and applying (5.1) gives (5.2). Since `(R m_J)^2=m_J^2`, Jensen's inequality gives

```text
E[m_J^2] = E[(R m_J)^2] >= (E[R m_J])^2 = 1/4,
```

which is (5.3), and subtracting from one gives (5.4). QED.

This theorem is independent of the internal recursive-majority depth and independent of the scheduling rule. It identifies an exact conservation law behind the residual child: on average the unfinished child agrees with the already-decided root only one quarter of the time.

## 6. Why the uncertainty theorem does not yet move `sigma`

The first C0021 run proved the residual-completion accounting inequality

```text
D_{h+1} >= 3 D_h - E[V_h(S_J)],       (6.1)
```

where `S_J` is the terminal residual state of the unfinished child and `V_h(S_J)` is its optimal completion cost.

The new theorem would immediately become source-moving if one had a uniform comparison such as

```text
V_h(s) <= D_h [1-m(s)^2]               (6.2)
```

on the residual states that an optimal outer policy can produce. Then (5.4) would give

```text
E[V_h(S_J)] <= (3/4)D_h,
D_{h+1} >= (9/4)D_h.
```

To beat the old `9/4` scale one would need either strict improvement in the uncertainty term on optimal residual support or a sharper cost-versus-uncertainty comparison.

However, (6.2) is **false as a global state inequality already at depth two**. Consider

```text
s^dagger = (-, (-,u,u), (-,u,u)).
```

Exact Bellman arithmetic gives

```text
p(s^dagger) = 1/16,
U(s^dagger) = 4p(1-p) = 15/64,
V_2(s^dagger) = 15/8,
D_2 = 393/64,
V_2(s^dagger)/D_2 = 40/131,
[V_2(s^dagger)/D_2] / U(s^dagger) = 512/393 > 1.
```

So the tempting global domination is rigorously false. This is the exact obstruction B13 had to survive.

The important distinction is that `s^dagger` need not lie in the terminal residual support of an optimal outer policy. B30 checks that support exactly at the first three scales.

## 7. B30 — exact one-scale residual geometry

Instead of collapsing an outer majority state as soon as two child signs agree, I retained the third child state at the stopping instant and solved the outer Bellman recursion exactly for child depths `h=0,1,2`.

For each `h`, the exact optimal outer cost equals the known `D_{h+1}`, and the residual statistics are:

```text
h=0:
  D_1 = 5/2,
  E[V_0(S_J)] = 1/2,
  E[V_0(S_J)]/D_0 = 1/2,
  E[U(S_J)] = 1/2,
  E[R m_J] = -1/2.

h=1:
  D_2 = 393/64,
  E[V_1(S_J)] = 87/64,
  E[V_1(S_J)]/D_1 = 87/160,
  E[U(S_J)] = 39/64,
  E[R m_J] = -1/2.

h=2:
  D_3 = 15796051/1048576,
  E[V_2(S_J)] = 3539117/1048576,
  E[V_2(S_J)]/D_2 = 3539117/6438912
                    = 0.5496451885...,
  E[U(S_J)] = 158023/262144
              = 0.6028099060...,
  E[R m_J] = -1/2.
```

At `h=2` the preserved-root Bellman graph has 497 nonterminal states and 12 terminal residual types. On **every one of those 12 actual terminal residual types** with nonzero uncertainty,

```text
V_2(s) <= D_2 U(s),
```

and the maximum ratio `V_2(s)/(D_2 U(s))` is exactly one, attained by the untouched depth-2 child. Thus the global counterexample `s^dagger` is genuinely outside this optimal terminal residual support.

This finite result is the most useful B30 signal. The next possible theorem is not the false global inequality (6.2), but a **support-restricted residual inequality**: characterize the states that can remain when an optimal outer recursive-majority policy stops, and prove a cost-versus-uncertainty bound on that restricted set.

There is a serious obstacle. The preceding depth-4 policy work already showed that a globally better outer policy can deliberately take a query that is locally suboptimal for completing the currently touched child. Therefore one cannot define the admissible residual support merely as states reachable by child-local optimal policies. Any induction must encode enough oriented global state to allow such interleaving.

B30 therefore worked at one exact scale but did not yet glue across scales.

## 8. What the three methods established

**B7:** the naive limiting state `(p,V)` is false as a Markov compression. Six exact depth-3 collisions exist, all sign-paired; the displayed pair has the same `(p,V)` but opposite orientation of successor costs. Adding either exact odd coordinate `K` or `H` separates all 497 tested nonterminal states, but this is finite evidence only.

**B13:** `|K|` and `|H|` fail monotonicity. Posterior uncertainty `U=1-m^2` is a true supermartingale, and the three-child product martingale gives the universal exact identity `E[R m_J]=-1/2`, hence `E U_J <= 3/4`. The natural global completion-cost domination by `U` is nevertheless false, with an exact depth-2 counterexample ratio `512/393`.

**B30:** the support-restricted inequality survives the complete exact `h=2` optimal terminal residual support, where the maximum ratio is exactly one and `E U_J=158023/262144`. This isolates a plausible support theorem rather than another arbitrary finite Bellman patch.

These are genuine structural advances, but none changes a rigorous asymptotic endpoint for `sigma`, so the frozen source metric is unchanged and the stagnation streak becomes one.

## 9. Exact finite self-check and immutable artifacts

The mathematical ideas and theorem proof above were written before the checker. The executed exact-arithmetic self-check is

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_limit_state_uncertainty_check.py`

Creation commit: `3c12ecd5ce6144542a1202e8d02d5652ae16ade4`. Read-back blob at that exact commit: `2f55ba08b0e74a816b7d196e336c2bceaddeeb1a`.

Archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_limit_state_uncertainty_check.out`

Creation commit: `6ac679698b19c840c362493895138289bf77fa4c`. Read-back blob at that exact commit: `a20c5e0f123d6e44047ac5b79157e33e11baa47c`.

The output ends

```text
ALL_EXACT_LIMIT_STATE_UNCERTAINTY_CHECKS_PASS
```

and verifies the exact `D_1,D_2,D_3`, the 499/497 depth-3 optimal-reachable state counts, uniqueness of all 497 optimal moves, all six `(p,V)` collisions and sign pairing, injectivity of `(p,V,K)` and `(p,V,H)`, the explicit collision successor fractions, the `|K|/|H|` nonmonotonicity counts, all `h=0,1,2` residual statistics, the `h=2` support-restricted ratio maximum one, and the global counterexample ratio `512/393`. This is a **self-check**, not an independent closure audit.

## 10. Source metric and next obligation

No source endpoint moved:

```text
sigma_lower(before) = 0.1783937532290626654407820192070906898593985836476...
sigma_lower(after)  = 0.1783937532290626654407820192070906898593985836476...

sigma_upper(before) = 0.2618595071429148741990542286855217085991712802638...
sigma_upper(after)  = 0.2618595071429148741990542286855217085991712802638...

W_sigma(before) = 0.0834657539138522087582722094784310187397726966161...
W_sigma(after)  = 0.0834657539138522087582722094784310187397726966161...
```

C0021 therefore remains **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL**, with unchanged-run streak `0 -> 1`. Closure is not claimed, and no outside closure audits are requested.

The sharp next obligation is to replace the empirical `h=2` support fact by a scale-free theorem. A useful sufficient form would be an invariant class `A_h` of possible optimal residual states such that

```text
S_J in A_h almost surely,
V_h(s) <= D_h U(s) for every s in A_h,
```

with enough additional slack in `E U(S_J)` or in the pointwise inequality to beat the existing lower-growth constant. The `(p,V)` obstruction means `A_h` cannot be tracked by those two scalars alone; an orientation coordinate such as `K` or a more intrinsic replacement is required.

Next distinct methods recorded for the following run: **B3, B15, B25** — strengthen the state invariant until it inducts, deliberately break the unbiased/sign symmetry to expose the missing orientation variable, and count the terminal residual law two ways to seek a weighted identity involving completion cost rather than only magnetization.

## 11. Structured ledger delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  own_root: proofnet24/P13-outside-successor
  canonical_target: C0021
  source: "Garban-Steif, Noise Sensitivity of Boolean Functions and Percolation, Part VIII Exercise VIII.5"
  status_before: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL"
  status_after: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL"
  metric_name: W_sigma
  metric_domain: "width of one rigorous interval for the single source revealment exponent sigma"
  metric_before: "0.0834657539138522087582722094784310187397726966161..."
  metric_after: "0.0834657539138522087582722094784310187397726966161..."
  movement: false
  unchanged_streak_before: 0
  unchanged_streak_after: 1
  methods_tried: [B7, B13, B30]
  theorem_claims:
    - "P13-C0021-RESIDUAL-MAGNETIZATION-IDENTITY-01: E[R*m_J] = -1/2 for any finite exact adaptive majority-of-three algorithm on independent unbiased child outputs"
  finite_self_checks:
    - "depth3 optimal graph: 499 states / 497 nonterminal / all 497 unique optimal moves"
    - "six (p,V) collision pairs, all global-sign pairs"
    - "(p,V,K) and (p,V,H) injective on the 497 tested nonterminal states"
    - "h=2 optimal terminal residual support has max V_2/(D_2 U) = 1"
    - "global depth2 counterexample to V<=DU has ratio 512/393"
  artifacts:
    checker: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_limit_state_uncertainty_check.py"
    checker_commit: "3c12ecd5ce6144542a1202e8d02d5652ae16ade4"
    checker_blob: "2f55ba08b0e74a816b7d196e336c2bceaddeeb1a"
    output: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_limit_state_uncertainty_check.out"
    output_commit: "6ac679698b19c840c362493895138289bf77fa4c"
    output_blob: "a20c5e0f123d6e44047ac5b79157e33e11baa47c"
    output_tail: "ALL_EXACT_LIMIT_STATE_UNCERTAINTY_CHECKS_PASS"
  next_methods: [B3, B15, B25]
  closure_claimed: false
  audits_requested: false
  shared_root_edits: false
  peer_file_edits: false
  retired_targets_reopened: false
```
