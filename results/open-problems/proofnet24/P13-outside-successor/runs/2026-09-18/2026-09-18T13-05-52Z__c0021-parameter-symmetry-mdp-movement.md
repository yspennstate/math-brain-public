Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SOURCE-METRIC MOVEMENT: `W_sigma = 0.083512030742080514252572131305984... -> 0.083465753913852208758272209478431...`; C0021 unchanged-run streak `0 -> 0`. Methods actually tried: B5, B14, B18.**

# P13 C0021 — bias derivative, sign quotient, and Bellman-MDP policy improvement

Date: 2026-09-18 UTC. Track: P13 Outside Counterexample Research. Native slot: `6aa7b253b37c8191b693d8dc79298d37`. Own root: `proofnet24/P13-outside-successor/`.

## 1. Recovered state, ownership, exclusions

The active create-only claim remains `operations/claims/C0021.md`: Garban--Steif Exercise VIII.5, the revealment exponent of iterated 3-majority. No competing C0021 owner was recovered. Retired I0051 was not reopened; handed-off P0082 was not reopened; six-run-handed-off D0093 was not reopened; the mandatory I0054 lead remains unavailable because it is owned by another track. P13's secondary directed-audit duty to P14 is preserved; this run did not repeat a completed audit.

The source reduction already proved in the C0021 memo is

```text
delta_{f_k} = D_k / 3^k,
c = lim_k D_k^(1/k),
sigma = 1 - log_3(c),
```

where `D_k` is the optimal uniform expected zero-error decision-tree cost for depth-`k` recursive 3-majority. The frozen source-faithful metric remains the width `W_sigma` of one rigorous interval for this single source exponent, target zero. The newest preceding report, `2026-09-18T12-19-43Z__c0021-shallow-bellman-family-movement.md`, gave the certified explicit depth-4 policy cost

```text
U_old = 1332788674231672015 / 36028797018963968
      = 36.992316827290985...
```

and hence

```text
sigma >= 0.178347476400834359946482097379537...
sigma <= 0.261859507142914874199054228685522...
W_sigma = 0.083512030742080514252572131305984...
```

Only a rigorous endpoint change in this same source domain counts as movement.

## 2. Source and literature refresh, 2026-09-18

The Clay Mathematics Proceedings source was rechecked. Its Part VIII exercise sheet states Exercise VIII.5 for iterated 3-majority and explicitly says that the revealment sequence decays like `1/n^sigma` for some `sigma` but that it is an open question what `sigma` is. The same source gives Theorem VIII.6, `delta_f >= I(f)^2/n` for monotone Boolean functions, which is the source of the unchanged upper endpoint `sigma <= log_3(4/3)`. The PDF text layer was accessible; a required screenshot attempt on the source PDF failed with a cache miss, and that access failure is recorded rather than silently ignored.

Dated bounded queries were: `"iterated 3-majority" revealment sigma open problem Garban Steif 2026`, `"recursive majority" expected number decision tree uniform distribution 2026`, `"level-p-complexity" recursive majority Jansson Jansson`, and the exact Exercise VIII.5 phrase. The closest checked later work remains Julia Jansson and Patrik Jansson, *Level-p-complexity of Boolean functions using thinning, memoization, and polynomials*, JFP 33 (2023), which computes the two-level problem and whose public code repository conjectures a piecewise polynomial for the three-level level-`p` complexity. At `p=1/2` its displayed three-level value is exactly the already recovered `D_3=15796051/1048576`. No checked source in this bounded search determines the asymptotic uniform exponent `sigma`. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

## 3. Idea before computation

The preceding run found a 14-state shallow override table but did not explain why its Bellman defects occur in sign pairs or how to search beyond query depth 5 without merely growing an empirical table. This run changed language before adding code.

- **B5** adds an input-bias parameter `p` and differentiates the value of a fixed policy at `p=1/2`. This makes the transverse direction away from the source's unbiased point explicit.
- **B14** quotients by the global sign-flip group. If an improving state and action have a sign partner, the unbiased defect must agree while the bias derivative changes sign.
- **B18** rewrites the canonical-state recursion as a finite acyclic stochastic-shortest-path Markov decision process. A shallow patch is then an exact policy-improvement step, not a heuristic local rule.

The new search found two certified strict overrides at query depth 7 and four at query depth 8, all arranged in global-sign pairs. These six legal actions lower the explicit depth-4 cost and therefore move the source exponent through the previously proved stationary four-level block composition theorem.

## 4. B5 — add Bernoulli bias and differentiate the fixed-policy value

Fix any deterministic exact decision policy `pi` on a finite partial-assignment state `s`. For `p in (0,1)`, let `E_p^pi(s)` be its expected remaining query cost when every unrevealed leaf is independently `+` with probability `p`. If `pi(s)` queries one leaf and its `+/-` successor states are `s^+` and `s^-`, then

```text
E_p^pi(s) = 1 + p E_p^pi(s^+) + (1-p) E_p^pi(s^-).
```

### Lemma 4.1 (fixed-policy bias derivative)

For every state of a finite exact policy, `E_p^pi(s)` is a polynomial in `p`. Writing

```text
E(s)  = E_{1/2}^pi(s),
E'(s) = d/dp E_p^pi(s) |_{p=1/2},
```

we have

```text
E(s)  = 1 + (E(s^+) + E(s^-))/2,
E'(s) = E(s^+) - E(s^-) + (E'(s^+) + E'(s^-))/2.
```

For a legal alternative query `a` followed thereafter by `pi`, with successor states `t^+,t^-`, the Bellman defect

```text
A_p^pi(s,a) = E_p^pi(s) - [1 + p E_p^pi(t^+) + (1-p) E_p^pi(t^-)]
```

therefore satisfies at `p=1/2`

```text
A = E(s) - 1 - (E(t^+) + E(t^-))/2,
A' = E'(s) - [E(t^+) - E(t^-) + (E'(t^+) + E'(t^-))/2].
```

**Proof.** A finite decision tree has finitely many root-to-leaf transcripts. Each transcript probability is a monomial in `p` and `1-p`, so its expected cost is a polynomial. The first recursion is the law of total expectation after the next queried bit. Differentiating that finite polynomial identity and evaluating at `p=1/2` gives the displayed derivative recursion. The alternative-action formula is the same calculation with the first action replaced and `pi` used afterward. QED.

For the two new depth-7 sign-paired states, the exact unbiased Bellman defect is

```text
A = 18224279181 / 1099511627776
  = 0.01657488535875018...
```

for each state, while the derivatives are

```text
A' = +/- 3142409184233 / 4398046511104
   = +/- 0.7145011259656258... .
```

After installing that pair, the four new depth-8 states have two unbiased defect sizes,

```text
2514971655 / 137438953472 = 0.018298827162652742...   (twice),
91533515 / 17179869184    = 0.005327951803337783...   (twice),
```

and their exact bias derivatives are the two opposite-sign pairs

```text
+/- 3268295917 / 8589934592,
+/- 9062117167 / 68719476736.
```

Thus the new improvements are not isolated numerical accidents at unrelated states: their first-order bias behavior comes in the exact sign-conjugate pattern predicted by the symmetry.

B5 **worked structurally** and helped organize the search. It does not by itself determine the asymptotic exponent; its source-level value is that it identifies a parameter direction in which the policy defects can be compared and paired exactly.

## 5. B14 — quotient the new policy defects by global sign

Let `J` flip every observed `+` to `-` and every `-` to `+`, leaving unrevealed leaves unchanged, followed by the usual canonical sorting of sibling states. Recursive majority commutes with this involution, and a query transition `(s^+,s^-)` is carried to `(J(s^-),J(s^+))` because the outcome labels swap.

### Lemma 5.1 (sign conjugacy)

Suppose a policy `pi` is sign-equivariant: at `J(s)` it makes the `J`-conjugate query to the one made at `s`. Then

```text
E_{1/2}^pi(J(s)) = E_{1/2}^pi(s).
```

For a conjugate pair of alternative actions `a,Ja`, their unbiased Bellman defects are equal and their bias derivatives are opposite:

```text
A_{1/2}^pi(J(s),Ja) = A_{1/2}^pi(s,a),
(d/dp)A_p^pi(J(s),Ja)|_{1/2} = -(d/dp)A_p^pi(s,a)|_{1/2}.
```

**Proof.** Couple the `p`-biased input on `s` to the `(1-p)`-biased sign-flipped input on `J(s)` by flipping every unrevealed bit. The coupled transcripts under a sign-equivariant policy use exactly the same number of queries. Hence `E_p^pi(s)=E_{1-p}^pi(J(s))`. Apply the same coupling after replacing the first action by a conjugate alternative. Subtract the two identities to obtain `A_p^pi(s,a)=A_{1-p}^pi(J(s),Ja)`. Evaluate at `p=1/2` and differentiate. QED.

The executed exact checker verifies that the six new override states form exactly **three size-two global-sign orbits**, and that the stored actions satisfy the transition-order conjugacy

```text
patch[J(s)] = (J(s^-_patch), J(s^+_patch)).
```

The quotient therefore needs only three new action templates rather than six unrelated cases. B14 **worked**: it halves this new patch family and explains the exact derivative pairing from B5.

## 6. B18 — canonical decision trees as an acyclic stochastic-shortest-path MDP

Use the canonical partial-assignment types as states. Determined root values `+/-` are terminal states of cost zero. At every undetermined state, an action is a legal leaf-query orbit; it costs one query and moves with probability `1/2` to its `+` or `-` successor. Since every action reveals one previously unknown leaf, this MDP is finite and acyclic.

For a deterministic policy `pi`, its value function is exactly the policy cost `E^pi`. For a legal action `a`, define

```text
Q^pi(s,a) = 1 + [E^pi(s_a^+) + E^pi(s_a^-)]/2.
```

### Theorem 6.1 (finite antichain policy improvement)

Let `S` be a set of states lying at one query-depth layer under `pi`. If for each `s in S` a legal action `a_s` satisfies

```text
Q^pi(s,a_s) < E^pi(s),
```

then the policy `pi'` obtained by using `a_s` on `S` and otherwise using `pi` is exact, and its root expected cost is strictly lower whenever the root reaches at least one state of `S` with positive probability.

**Proof.** Every replacement still queries an unrevealed leaf, so each branch strictly increases the revealed-leaf count and finite termination is preserved. After the replacement action the policy follows the exact original decision tree, so root correctness is preserved. States on one query-depth layer form an antichain in the policy tree: before the first hit of `S`, `pi` and `pi'` have identical transcripts. Conditional on first hitting `s`, the continuation cost decreases by exactly `E^pi(s)-Q^pi(s,a_s)>0`. Averaging over the disjoint first-hit events yields a strictly positive root decrease. QED.

Apply this theorem first to the two certified depth-7 states. Starting from the preceding run's policy,

```text
U_old = 1332788674231672015 / 36028797018963968
```

we obtain

```text
U_7 = 1332632382813415759 / 36028797018963968
    = 36.987978869013496... .
```

Then apply it to the four certified depth-8 states under the updated policy. This gives the explicit exact depth-4 policy

```text
U_new = 1332517664326644559 / 36028797018963968
      = 36.98479479137941... .
```

The total exact improvement is

```text
U_old - U_new
  = 2117264883027 / 281474976710656
  = 0.0075220359115739654... .
```

B18 **worked quantitatively**: the MDP language turns the symmetry-reduced defect templates into two certified policy-improvement sweeps and a lower explicit depth-4 cost. No claim is made that `U_new=D_4` or that these are all improving states at those depths.

## 7. Source-metric movement

The preceding report proved the stationary block-composition theorem: any exact depth-4 policy of uniform expected cost `U` yields

```text
c <= U^(1/4),
sigma >= 1 - (1/4) log_3 U.
```

Applying that already-proved theorem to `U_new` gives

```text
c <= 2.466072290386942266301702772987020532...
```

and hence

```text
sigma >= 0.1783937532290626654407820192070906898593985836476... .
```

The source upper endpoint remains

```text
sigma <= log_3(4/3)
       = 0.2618595071429148741990542286855217085991712802638... .
```

Therefore the frozen interval width moves from

```text
W_sigma(before) = 0.083512030742080514252572131305984211230263210420...
```

to

```text
W_sigma(after)  = 0.083465753913852208758272209478431018739772696616...
```

with exact-decimal contraction

```text
0.0000462768282283054942999218275531924904905138038... .
```

This is genuine source-domain movement, so the C0021 unchanged-run streak remains `0 -> 0`.

## 8. Exact finite self-check

The mathematical idea and proofs above were written before the checker. The executed exact-arithmetic self-check is:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_parameter_symmetry_mdp_check.py`

Creation commit: `df46b950763b31ed1bf1c3fe9414e105b0a70926`; read-back blob at that commit: `0f24b57210d02ea2bcde0e7152c353eb550b5c7f`.

Archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_parameter_symmetry_mdp_check.out`

Creation commit: `f81ef36e4f0e34c86519531fd553a047011d24db`; read-back blob at that commit: `ea599cf05f10cbcb5bab994546298b075802a22f`.

The output ends `ALL_EXACT_PARAMETER_SYMMETRY_MDP_CHECKS_PASS`. It verifies the old root cost, legal reachability of the two depth-7 and four depth-8 patch states, positivity of every stored exact Bellman defect, all displayed defect and derivative fractions, the two staged root costs, the three global-sign orbits and action equivariance, and the source interval conversion. This is a **self-check**, not an independent closure audit.

## 9. What remains and next methods

The new quotient still describes a finite depth-4 policy, not an asymptotic stationary rule on arbitrary recursive-majority depth. The strongest unresolved structural question is whether Bellman advantage can be expressed by a bounded-dimensional statistic of the three child states -- for example posterior, exact completion value, and one extra imbalance coordinate -- so that the same sign-equivariant rule can be iterated at every scale. A proof of such a stationary rule with analytically controlled growth could attack the exact exponent rather than only improve finite-block upper bounds.

No closure is claimed. The source exponent remains unknown, the frozen interval is nonzero, and the required P26 plus distinct OTHER-track end-to-end audits do not apply until a source-matching closure candidate exists.

Next distinct methods recorded for the following run: **B7** (take the block-depth limit of a symmetry-reduced policy class), **B13** (seek a monotone Bellman-advantage or information potential along canonical states), and **B30** (solve one additional local quotient class at a time and identify the exact obstruction to gluing it into a scale-free rule).

## 10. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  own_root: proofnet24/P13-outside-successor
  canonical_target: C0021
  source: "Garban-Steif, Noise Sensitivity of Boolean Functions and Percolation, Part VIII Exercise VIII.5"
  status_before: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL"
  status_after: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL"
  metric:
    name: W_sigma
    domain: "single source exponent sigma for iterated 3-majority revealment"
    target: 0
    before: "0.083512030742080514252572131305984211230263210420..."
    after: "0.083465753913852208758272209478431018739772696616..."
    movement: true
    contraction: "0.0000462768282283054942999218275531924904905138038..."
  source_lower_endpoint_before: "0.178347476400834359946482097379537497368908069843..."
  source_lower_endpoint_after: "0.1783937532290626654407820192070906898593985836476..."
  source_upper_endpoint: "0.2618595071429148741990542286855217085991712802638..."
  explicit_depth4_cost_before: "1332788674231672015/36028797018963968"
  explicit_depth4_cost_after: "1332517664326644559/36028797018963968"
  unchanged_streak_before: 0
  unchanged_streak_after: 0
  methods_tried: [B5, B14, B18]
  finite_self_check:
    script: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_parameter_symmetry_mdp_check.py
    script_creation_commit: df46b950763b31ed1bf1c3fe9414e105b0a70926
    output: proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_parameter_symmetry_mdp_check.out
    output_creation_commit: f81ef36e4f0e34c86519531fd553a047011d24db
    result: ALL_EXACT_PARAMETER_SYMMETRY_MDP_CHECKS_PASS
    role: self-check
  literature_refresh_date: 2026-09-18
  literature_result: "bounded search found no checked source-matching determination; not a global openness/novelty certificate"
  source_pdf_screenshot: "attempted; cache-miss failure recorded"
  closure_claimed: false
  audits_requested: false
  exclusions_preserved: [I0051, P0082, D0093]
  next_methods: [B7, B13, B30]
```
