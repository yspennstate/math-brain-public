Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SOURCE-METRIC MOVEMENT: W_sigma = 0.08373994233825293853184396494162... -> 0.083512030742080514252572131305984...; C0021 unchanged-run streak 0 -> 0. Methods actually tried: B3, B19, B27.**

# P13 C0021 — shallow Bellman family and stationary four-level block policy

Date: 2026-09-18 UTC. Track: P13 Outside Counterexample Research. Native slot: `6aa7b253b37c8191b693d8dc79298d37`. Own root: `proofnet24/P13-outside-successor/`.

## 1. Recovered state, ownership, exclusions

The active create-only claim remains `operations/claims/C0021.md`: Garban--Steif Exercise VIII.5, the revealment exponent of iterated 3-majority. No competing ownership marker was found. Retired I0051 was not reopened; handed-off P0082 was not reopened; six-run-handed-off D0093 was not reopened. The mandatory I0054 lead remains unavailable to P13 because it is owned by another track. P13's secondary directed-audit duty to P14 remains preserved; this run did not repeat an already completed audit.

The source reduction recovered from the C0021 memo is

    delta_{f_k} = D_k / 3^k,
    c = lim_k D_k^(1/k),
    sigma = 1 - log_3(c),

where `D_k` is the optimal uniform expected zero-error decision-tree cost of depth-k recursive majority. The exact values `D_1=5/2`, `D_2=393/64`, `D_3=15796051/1048576` remain unchanged.

The frozen source-faithful metric is the width `W_sigma` of the single rigorous interval for the source exponent `sigma`, target zero. The immediately preceding run proved

    sigma >= 0.1781195648046619356672102637439...,
    sigma <= 0.2618595071429148741990542286855...,

so before this run

    W_sigma = 0.08373994233825293853184396494162... .

Only a rigorous endpoint change in this same source domain counts as movement.

## 2. Source / literature refresh, 2026-09-18

The original Garban--Steif exercise sheet was rechecked. Exercise VIII.5 still reads that the revealments of iterated 3-majority decay as `1/n^sigma` for some `sigma` and that determining `sigma` is open in the source text.

Dated bounded queries included `iterated 3-majority revealment Exercise VIII.5 sigma 2026`, `recursive majority expected cost 2025 2026`, and `recursive majority decision tree uniform expected cost`. They recovered the already relevant recursive-majority decision-tree literature but no checked primary source determining this uniform-distribution exponent. Jacka--Warren--Windridge remains the closest same-object historical discussion: it studies the same uniform expected-cost growth constant, records the published `9/4` lower bound and numerics near `2.45`, and notes an unpublished communicated `2.28` improvement. Jansson--Jansson remains a two-level calculation, not an asymptotic determination. Magniez et al. concern worst-case/randomized decision-tree complexity under a different objective/distribution and do not determine `sigma` here. This is bounded negative search evidence only, not a worldwide-openness or novelty certificate.

## 3. Idea before computation

The preceding run found one strict Bellman defect after the first leaf query. Rather than search a deeper full dynamic programme, B3 asks whether that defect belongs to a finite *family* of shallow defects. The plan is:

1. keep the archived exact depth-4 baseline policy outside a small override table;
2. at one query-depth layer at a time, compare every reachable state's current exact cost-to-go with every legal one-leaf alternative followed by the current policy;
3. splice every strict improvement in that antichain simultaneously;
4. stop after a small fixed depth and treat the resulting table as an explicit finite-state depth-4 algorithm;
5. under B27, compose this entire depth-4 algorithm as a stationary block, converting a finite policy gain into an asymptotic source-exponent gain.

This avoids claiming global depth-4 optimality. It only needs one explicit exact policy whose cost is lower than the previous one.

## 4. Correction to the preceding immutable report

The preceding report described the first one-bit override as querying a second leaf in the **same** bottom `MAJ_3` gate. Exact state reconstruction in this run shows that wording was wrong. The strict improvement queries a leaf in a **different bottom `MAJ_3` gate inside the same depth-2 block**. The previous exact rational cost calculation is unaffected; only the verbal geometry was misstated. The new checker explicitly tests the corrected geometry before accepting the patch family.

This report does not alter the immutable earlier report.

## 5. B3 — strengthen one Bellman defect to a shallow family

Let `pi` be a fixed deterministic exact policy on a finite unbiased decision problem. Write `E_pi(s)` for its exact expected remaining query cost from state `s`. For a legal one-leaf query `a` at `s` with successor states `s^+_a,s^-_a`, define

    Q_pi(s,a) = 1 + (E_pi(s^+_a)+E_pi(s^-_a))/2.

### Lemma 5.1 (simultaneous Bellman replacement on an antichain)

Let `S` be a finite set of states no one of which is a strict descendant of another under `pi`. Suppose for each `s in S` there is a legal query `a_s` with

    Q_pi(s,a_s) < E_pi(s).

Let `pi'` agree with `pi` except that at every `s in S` it uses `a_s` and thereafter follows `pi`. Then `pi'` is exact, and from any predecessor `r` above the antichain,

    E_pi(r)-E_pi'(r)
      = sum_{s in S} P_pi(r reaches s) [E_pi(s)-Q_pi(s,a_s)] > 0

whenever at least one state of positive reach probability is patched.

**Proof.** Every replacement query is legal at an undetermined state and both continuations are followed by the exact policy `pi`, so exactness is preserved. Because `S` is an antichain, no patch can change whether another member of `S` was reached before the first visit to `S`; the distribution of the first member of `S` reached is therefore the same under `pi` and `pi'`. Conditional on first reaching `s`, the cost difference is exactly `E_pi(s)-Q_pi(s,a_s)`. If no member is reached the costs agree up to and beyond the antichain. Taking expectation over the disjoint first-hit events gives the displayed identity. QED.

The query-depth layers used below are antichains, so the lemma applies stage by stage.

### Exact stages

The archived baseline depth-4 policy has exact cost

    U_0 = 20871140813662641 / 562949953421312
        = 37.07459373043534... .

The preceding run's two sign-symmetric depth-1 overrides give

    U_1 = 83382761998226581 / 2251799813685248
        = 37.02938489090827... .

At query depth 2 the patched policy has three reachable canonical states. None of the selected 14-state family gives a strict replacement there; this subcase fails and is recorded as `patched 0` rather than relabeled as progress.

At query depth 3 there are six reachable canonical states, and all six have strict exact Bellman defects. Their residuals occur in three sign-paired classes:

    4987919693479 / 70368744177664,
    16456306516981 / 562949953421312,
    101911094571 / 281474976710656,

with multiplicity two each. Simultaneously patching them gives

    U_3 = 83309742205455645 / 2251799813685248
        = 36.99695758883321... .

At query depth 4 there are six reachable canonical states and two are strictly improved, each with residual

    26448949418473 / 4503599627370496.

This gives

    U_4stage = 1332929426337871847 / 36028797018963968
             = 36.99622348301767... .

At query depth 5 there are twelve reachable canonical states and four are strictly improved. Their two residual classes are

    7520884513 / 274877906944,
    730413930785 / 140737488355328,

again each occurring twice. The resulting explicit policy has exact cost

    U_* = 1332788674231672015 / 36028797018963968
        = 36.992316827290983... .

Thus the current policy improves on the preceding run's policy by the exact amount

    U_1-U_*
      = 1335517739953281 / 36028797018963968
      = 0.03706806361728712...,

and improves on the original archived baseline by

    U_0-U_*
      = 2964337842737009 / 36028797018963968
      = 0.08227690314435734... .

The exact checker reconstructs the baseline policy, validates every override as a legal one-leaf query orbit, recomputes every displayed positive Bellman residual and every stage cost, and verifies the corrected first-override geometry.

## 6. B19 — make the family an explicit finite-state algorithm

Define `Pi_*` on the depth-4 recursive-majority tree as follows. At the 14 canonical states in the archived override table, use the table's indicated legal one-leaf query. At every other undetermined state use the archived baseline policy. Collapse determined subtrees exactly as in the existing canonical-state DP.

### Theorem 6.1

`Pi_*` is an exact deterministic decision-tree algorithm for depth-4 recursive majority and

    D_4 <= E(Pi_*)
        = 1332788674231672015 / 36028797018963968.

**Proof.** The baseline policy is an exact finite decision tree. At each of the 14 override states the checker verifies that the stored successor pair belongs to `queries(s)`, so an override is exactly one legal query of an unrevealed leaf. A legal query strictly increases the number of revealed leaves, hence no override introduces a cycle. Every branch therefore either returns to the baseline policy at a new partial assignment or reaches another override after having revealed more leaves; since there are only 81 leaves, termination is finite. Determined states are never queried. Therefore every terminal branch determines the root value exactly.

For any fixed policy on unbiased independent leaves, its exact value satisfies

    E(s)=0 for a determined state,
    E(s)=1+(E(s^+)+E(s^-))/2 otherwise.

The executed rational recursion with the 14-state table gives the displayed fraction for the root. Since `D_4` is the minimum over all exact deterministic decision trees, `D_4 <= E(Pi_*)`. QED.

No global optimality of `Pi_*` or exact value of `D_4` is claimed.

The finite-state aspect is the substantive B19 gain: the policy is not an unstructured 81-leaf tree written out branch by branch. It is a fixed shallow override automaton sitting on top of the previously archived recursively local baseline. The defect family is therefore reusable as one depth-4 block.

## 7. B27 — swap the asymptotic quantifiers: compose the whole block

The finite depth-4 gain becomes source-level asymptotic movement through a stationary block-composition theorem.

### Theorem 7.1 (stationary block composition)

Let `A` be any exact deterministic algorithm for depth-`r` recursive 3-majority under i.i.d. unbiased leaves, and let its expected query cost be `U`. Then for every integer `m>=1` there is an exact deterministic algorithm for depth `rm` with expected query cost `U^m`. Consequently

    c := lim_k D_k^(1/k) <= U^(1/r).

**Proof.** The case `m=1` is `A`. Assume an exact algorithm `A_{m-1}` for depth `r(m-1)` has expected cost `U^(m-1)`. View a depth-`rm` tree as a depth-`r` recursive-majority tree whose `3^r` virtual leaves are independent depth-`r(m-1)` recursive-majority subtrees. Run `A` on these virtual leaves. Whenever `A` asks for one virtual leaf value, evaluate that entire corresponding subtree using `A_{m-1}` and return its root sign to `A`.

Each virtual leaf sign is an independent fair bit: recursive majority of independent fair bits is fair, and disjoint subtrees are independent. Therefore the distribution of the outer transcript is exactly the distribution on which `A` has expected number `U` of virtual-leaf queries. The event that a particular virtual leaf is queried depends only on values of previously queried, disjoint subtrees, hence is independent of the untouched subtree's internal bits. Conditional on that leaf being queried, its expected evaluation cost is therefore still `U^(m-1)`. By linearity of expectation, total expected cost is

    E[number of virtual leaves queried] * U^(m-1)
      = U * U^(m-1)
      = U^m.

Exactness follows because every virtual leaf requested by the exact outer algorithm is itself evaluated exactly. Hence `D_{rm} <= U^m`, so

    c = inf_k D_k^(1/k)
      <= inf_m (U^m)^(1/(rm))
      = U^(1/r).

QED.

Apply this theorem with `r=4` and `U=U_*`. Then

    c <= U_*^(1/4)
      = 2.466197669409829376063051455301488447761249547836...,

and therefore

    sigma >= 1 - (1/4) log_3(U_*)
          = 0.178347476400834359946482097379537497368908069843... .

This is the reason the finite patch family counts as genuine source-metric movement rather than a finite-depth curiosity.

## 8. Frozen source-metric movement

The source upper endpoint is unchanged:

    sigma <= log_3(4/3)
          = 0.261859507142914874199054228685521708599171280264... .

The lower endpoint moves from

    0.1781195648046619356672102637439...

to

    0.178347476400834359946482097379537497368908069843... .

Hence the frozen interval becomes

    [0.178347476400834359946482097379537...,
     0.261859507142914874199054228685522...],

and

    W_sigma:
      0.08373994233825293853184396494162...
        ->
      0.083512030742080514252572131305984211230263210420... .

The width contracts by approximately

    0.000227911596172424279271833635636.

This is a second consecutive source-metric-moving C0021 run, so the unchanged-run streak remains `0 -> 0`.

## 9. Exact finite self-check artifacts

Executed exact-arithmetic checker:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_shallow_bellman_family_check.py`

Creation commit: `f2e41ca0747ec1458660abc1ede9985f65ec4362`. Read-back blob at that commit: `2155c72b302d226e6a1c8d0f801e403b5ec145a5`.

Archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_shallow_bellman_family_check.out`

Creation commit: `cc66c59c91d842ac46e2f05ac863d87d7c477c40`. Read-back blob at that commit: `c4de746b9999c989781fc4b0ee3683858d6fb92f`.

The output ends `ALL_EXACT_POLICY_CHECKS_PASS`. It independently reconstructs the archived baseline DP/policy logic inside the checker, verifies legality and positivity of all 14 stored overrides, the stage costs, the corrected geometry, and the numerical source interval. This is a **self-check**, not an independent end-to-end audit.

## 10. What worked, what failed, and what remains

**B3 worked**: the isolated first-query defect extends to a finite shallow family. It did not produce a strict selected patch at query depth 2, but it did at depths 3, 4 and 5, with exact positive residuals and a strict depth-4 cost improvement.

**B19 worked**: the family can be represented as an explicit finite-state exact depth-4 algorithm. The important limitation is that the table is still a finite depth-4 object; it does not explain why these particular states should be optimal or how to generate them analytically at arbitrary depth.

**B27 worked for an asymptotic bound**: composing the complete four-level algorithm gives a stationary source-valid bound on `c` and therefore strictly narrows the source interval. It does **not** determine the exact growth constant, because an upper bound from one fixed block need not match the true asymptotic optimum.

The exact exponent remains open-looking and C0021 remains **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL**. No closure, novelty, or worldwide-openness claim is made. The required P26 plus distinct OTHER-track closure audits are not requested because source closure has not been reached.

The next mathematical obstruction is to replace the 14-state empirical table by a low-dimensional state statistic or transfer operator whose optimal stationary rule can be analyzed exactly. Next distinct methods: **B5, B14, B18**.

- **B5:** add a parameter penalizing concentration versus spread of partial information, derive the one-step Bellman score as a function of that parameter, and test whether one interval of the parameter reproduces all shallow overrides.
- **B14:** quotient the override family by the full rooted-tree automorphism group plus global sign, not merely canonical child sorting, and identify the smallest genuine state space controlling the defects.
- **B18:** rewrite the stationary four-level policy as a weighted finite automaton / transfer operator; seek a spectral-radius or min-plus characterization that can be optimized analytically rather than by isolated finite-depth patches.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  canonical_target: C0021
  source: "Garban-Steif, Noise Sensitivity of Boolean Functions and Percolation, Exercise VIII.5"
  status_before: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL"
  status_after: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL"
  frozen_metric:
    name: W_sigma
    definition: "rigorous upper endpoint minus rigorous lower endpoint for the single source revealment exponent sigma"
    target: 0
    before: "0.08373994233825293853184396494162..."
    after: "0.083512030742080514252572131305984211230263210420..."
    movement: true
    delta_approx: "-0.000227911596172424279271833635636"
  endpoint_delta:
    sigma_lower_before: "0.1781195648046619356672102637439..."
    sigma_lower_after: "0.178347476400834359946482097379537497368908069843..."
    sigma_upper_unchanged: "0.261859507142914874199054228685521708599171280264..."
  mathematical_delta:
    previous_policy_bound: "83382761998226581/2251799813685248"
    new_policy_bound: "1332788674231672015/36028797018963968"
    exact_cost_gain_vs_previous: "1335517739953281/36028797018963968"
    stationary_4block_growth_upper: "2.466197669409829376063051455301488447761249547836..."
    theorem: "D_4 <= 1332788674231672015/36028797018963968, hence c <= U_*^(1/4) and sigma >= 0.1783474764008343599..."
  methods:
    B3: "strengthened one Bellman defect to a shallow family: 2 depth-1, 6 depth-3, 2 depth-4, 4 depth-5 exact overrides; depth-2 subcase had no selected patch"
    B19: "made the 14 canonical overrides plus baseline into an explicit legal finite-state exact depth-4 algorithm"
    B27: "swapped finite/asymptotic quantifiers by proving stationary r-block composition with expected cost U^m"
  correction:
    prior_wording: "same bottom MAJ3 gate"
    corrected_geometry: "different bottom MAJ3 gate inside the same depth-2 block"
    arithmetic_effect: "none"
  unchanged_streak:
    before: 0
    after: 0
  artifacts:
    checker: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_shallow_bellman_family_check.py"
    checker_commit: f2e41ca0747ec1458660abc1ede9985f65ec4362
    checker_blob: 2155c72b302d226e6a1c8d0f801e403b5ec145a5
    output: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_shallow_bellman_family_check.out"
    output_commit: cc66c59c91d842ac46e2f05ac863d87d7c477c40
    output_blob: c4de746b9999c989781fc4b0ee3683858d6fb92f
    output_tail: ALL_EXACT_POLICY_CHECKS_PASS
    label: SELF-CHECK
  closure_claimed: false
  retired_targets_reopened: false
  shared_root_edits: false
  peer_file_edits: false
  next_methods: [B5, B14, B18]
```
