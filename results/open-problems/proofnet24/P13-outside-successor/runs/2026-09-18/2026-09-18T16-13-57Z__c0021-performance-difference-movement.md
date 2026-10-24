Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SOURCE-METRIC MOVEMENT: `W_sigma = 0.0834657539138522087582722094784310187397726966161... -> 0.0834588708713055426959122798576235957440527899102...`; C0021 unchanged-run streak `1 -> 0`. Methods actually tried: B3, B15, B25.**

# P13 C0021 — performance-difference theorem, sign-oriented Bellman defects, and a stronger depth-4 policy

Date: 2026-09-18 UTC. Track: P13 Outside Counterexample Research. Native slot: `6aa7b253b37c8191b693d8dc79298d37`. Own root: `proofnet24/P13-outside-successor/`.

## 1. Recovered state, continuity, ownership, and exclusions

The active create-only ownership marker remains `operations/claims/C0021.md`: Garban--Steif, *Noise Sensitivity of Boolean Functions and Percolation*, Part VIII Exercise VIII.5, the revealment exponent of iterated 3-majority. It still names this P13 native slot. No competing C0021 ownership marker was recovered. The mandatory predecessor exclusions remain intact: retired I0051 was not reopened; handed-off P0082 was not reopened; six-run-handed-off D0093 was not reopened; peer-owned I0054 was not touched. The newest R11 record recovered in this run is still actively advancing I0054, so there is no ownership ambiguity.

The controlling owner directive at commit `749da260517828ed311f6f1b1af74915c054bdf3`, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md`/`RANKING.md`, root `POSTED.md`/`RESULTS.md`/`QUEUE.md`, the C0021 claim, the intake/attempt history, the C0021 memo, and the newest complete P13 report were re-read. `RESULTS.md` still contains an older P13 configuration row, but it expressly says to recover newer complete reports before replacing retained state; this report therefore continues the immutable C0021 history rather than resetting to I0051. Unknown quantities were not converted to zero.

The newest complete P13 report before this one is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T14-54-38Z__c0021-limit-state-uncertainty.md`

at creation commit `406c1ba1a1b416f4b3a2860b70d2a648770bc03c`. It froze

```text
sigma_lower = 0.1783937532290626654407820192070906898593985836476...
sigma_upper = 0.2618595071429148741990542286855217085991712802638...
W_sigma     = 0.0834657539138522087582722094784310187397726966161...
unchanged streak = 1
```

and prescribed B3/B15/B25.

### Recovered post-report artifacts

After that complete report, four P13-owned exact artifacts were created but no later immutable report was present. I treated them as legitimate recovered track history rather than redoing or overwriting them:

- `c0021_canonical_policy_certificate_check.py`, creation commit `dee15ac93f1534e1cfede6f3cbcdbb4eab1ae685`, blob `fe7d40c5e7589a610bdc50a3ac3d5674ea95c633`;
- `c0021_canonical_policy_certificate_check.out`, creation commit `40fab3c4f8d76ecb3a2ed2e35c538a44d62332cf`, blob `9fe531c679988f8d3708198eeb98245b85166d47`;
- `c0021_stronger_policy_performance_check.py`, creation commit `74fdf4b0afe01582346d44fec58f554f270cfb4e`, blob `79d0c12b6ddf40ecdfa281b299846127994d4de9`;
- `c0021_stronger_policy_performance_check.out`, creation commit `7a60d2211f9a439695bae70caf89a00385ec7f8d`, blob `39b1f04385ee23fadc2228d7cc62409f2cff2e0f`.

All four were read back at their actual creation commits before this report. Both outputs end in an explicit PASS line. They are self-checks, not independent closure audits.

## 2. Source and literature refresh — bounded 2026-09-18 check

The controlling source remains Garban--Steif, Cambridge University Press (2014), DOI `10.1017/CBO9781139924160`. The source exercise asks for the exponent governing revealment decay for iterated 3-majority and says the exponent is open in that text. Garban's current author page still advertises the almost-final book version. The author-hosted PDF itself timed out/inaccessible in the current web fetch path, so this run relied on the previously recovered source-exact text in the C0021 memo plus the current Cambridge bibliographic page; that access limitation is recorded rather than silently treated as a fresh PDF read.

Dated bounded queries included:

```text
"Exercise VIII.5" "Iterated 3-Majority" revealment
"iterated 3-majority" revealment sigma Garban Steif
"recursive majority" "expected number of queries" decision tree uniform
"Level-p-complexity of Boolean functions" iterated majority
"Minimizing the time to a decision" recursive majority
```

The closest checked later primary work remains Julia Jansson and Patrik Jansson, *Journal of Functional Programming* 33 (2023), e13, which defines exactly the Bernoulli-`p` minimum expected decision-tree cost and computes the **two-level** iterated-majority case; it does not determine the asymptotic exponent. Jacka--Warren--Windridge (Ann. Appl. Probab. 2011) concerns a continuous three-diffusion majority scheduling problem, not the discrete recursive uniform exponent. The bounded search found no checked primary source supplying the exact C0021 exponent. This is bounded negative evidence only, not a worldwide openness or novelty certificate.

## 3. Frozen source metric and idea before computation

The already proved reduction is

```text
delta_{f_k} = D_k / 3^k,
c = lim_k D_k^(1/k),
sigma = 1 - log_3(c),
```

where `D_k` is the minimum expected number of queried leaves among zero-error deterministic decision trees evaluating depth-`k` recursive 3-majority under unbiased independent leaf bits. The frozen metric is the width of one rigorous interval for this single `sigma`, target zero. Auxiliary structure does not count unless it moves an endpoint.

The three methods actually tried were:

- **B3 — PROVE SOMETHING STRONGER.** First I tried to strengthen the previous run's residual-support observation into an inductive cost/uncertainty invariant. That route still fails because the globally false inequality `V_h(s) <= D_h(1-m(s)^2)` has no proved residual-support closure under the outer Bellman dynamics. I then strengthened a different part of the argument successfully: the earlier antichain-only policy replacement lemma is replaced below by a full arbitrary-finite-patch performance-difference theorem.
- **B15 — BREAK THE SYMMETRY ON PURPOSE.** Put the unbiased problem inside the Bernoulli-`p` family and orient sign-conjugate Bellman defects by their first derivative at `p=1/2`. This explains why sign-paired patches have equal unbiased defects but opposite first derivatives and supplies a concrete orientation coordinate.
- **B25 — COUNT THE SAME THING TWICE.** Count a policy improvement both by direct root-value subtraction and by summing local Bellman defects weighted by **total state hit probabilities**. The exact identity catches a subtle error: a canonical state can be reached at more than one query clock, so one fixed-layer probability is not generally its coefficient.

The B3/B15/B25 synthesis yields a stronger explicit depth-4 policy and therefore genuine source-metric movement.

## 4. B3+B25 theorem — arbitrary-patch performance difference

### Theorem 4.1 (finite acyclic performance-difference identity)

Let `S` be the canonical state space of a finite Boolean decision problem under a product input law with unbiased unrevealed bits. Let `pi` and `pi'` be deterministic zero-error policies. Every nonterminal action queries one previously unrevealed raw bit and has canonical successors `s^+` and `s^-`, each with conditional probability `1/2`. Assume every query strictly decreases an integer rank, so termination is finite.

Let `E_pi(s)` be the expected additional number of queries made by `pi` from `s`. For the action selected by `pi'` at `s`, define its Bellman defect relative to `pi` by

```text
d(s) = E_pi(s) - [1 + (E_pi(s^+) + E_pi(s^-))/2].
```

Then, from any initial state `r`,

```text
E_pi(r) - E_pi'(r)
  = E_pi'[ sum_{t < tau} d(S_t) ]
  = sum_s H_pi'(r,s) d(s),                         (4.1)
```

where `tau` is the stopping time and `H_pi'(r,s)` is the total probability that the `pi'` trajectory starting at `r` ever visits canonical state `s`. Because the rank strictly decreases, a trajectory visits any fixed canonical state at most once. In particular, if every visited defect is nonnegative, `pi'` is no worse than `pi`; if at least one positive defect has positive hit probability, it is strictly better.

#### Proof

Set

```text
G(s) = E_pi(s) - E_pi'(s).
```

At a terminal state both values are zero, hence `G=0`. At a nonterminal state, `pi'` obeys its own exact first-step recursion

```text
E_pi'(s) = 1 + [E_pi'(s^+) + E_pi'(s^-)]/2.
```

Subtracting this from the definition of `d(s)` gives

```text
G(s) = d(s) + [G(s^+) + G(s^-)]/2.                 (4.2)
```

Iterate (4.2) along the finite `pi'` trajectory. Since the rank falls strictly at each query, the iteration stops after finitely many steps and the terminal `G` term vanishes. Conditional expectation at each step therefore yields

```text
G(r) = E_pi'[sum_{t<tau} d(S_t)].
```

Because a fixed canonical state cannot be revisited on one strictly rank-decreasing trajectory, indicator expansion gives

```text
E_pi'[sum_{t<tau} d(S_t)]
 = sum_s P_pi'(s is ever visited from r) d(s),
```

which is the second equality in (4.1). The sign consequences are immediate. QED.

### Why the total-hit coefficient matters

Canonicalization collapses determined subtrees and therefore forgets how many already-consumed raw leaves lie inside a collapsed sign. Consequently the same canonical state can occur at different **clock depths across different trajectories**, even though it cannot be revisited on one trajectory. B25's exact witness is one new depth-10 patch state with

```text
local defect             = 298677 / 4294967296,
clock-depth-10 probability = 1 / 1024,
total hit probability      = 15 / 4096.
```

The direct root-value contribution is

```text
4480155 / 17592186044416,
```

and exactly

```text
(15/4096) * (298677/4294967296)
  = 4480155/17592186044416.
```

Thus using only `1/1024` would undercount the improvement. The archived certificate checks this identity in exact rational arithmetic.

This theorem is stronger than the previous same-layer/antichain patch lemma: patches may occur at arbitrary finite canonical states and the exact interaction is absorbed into the `pi'` occupancy measure.

## 5. B15 theorem — sign symmetry fixes values but reverses first derivatives

Let `J` denote global sign flip. Freeze a sign-equivariant deterministic policy `pi`, and let `E_p(s)` be its expected remaining query cost when each unrevealed raw leaf equals `+` with probability `p`. Sign-equivariance means that the query selected at `J(s)` is the sign-flipped image of the query selected at `s`.

### Theorem 5.1 (odd orientation of sign-conjugate defects)

For every canonical state `s`,

```text
E_p(s) = E_{1-p}(J(s)).                             (5.1)
```

Hence, writing

```text
K(s) = d/dp E_p(s) |_{p=1/2},
```

one has

```text
K(J(s)) = -K(s).                                    (5.2)
```

More generally, let `a` be any legal query action at `s`, with successors `s^+,s^-`, and let `J(a)` be its sign-conjugate action at `J(s)`. Define the `p`-Bellman defect relative to the frozen policy by

```text
g_p(s,a)
 = E_p(s) - [1 + p E_p(s^+) + (1-p) E_p(s^-)].
```

Then

```text
g_p(J(s),J(a)) = g_{1-p}(s,a).                     (5.3)
```

In particular, conjugate defects have the same value at `p=1/2` and opposite first derivatives there.

#### Proof

Under Bernoulli-`p` inputs, globally flipping every bit produces Bernoulli-`1-p` inputs. A sign-equivariant policy follows the globally flipped transcript with exactly the same number of queries. Therefore the pathwise query count from `s` under parameter `p` has the same law as the query count from `J(s)` under parameter `1-p`, proving (5.1). Differentiate at `p=1/2`; the derivative of the right-hand side contributes a minus sign, giving (5.2).

For a queried raw bit, global sign flip exchanges the `+` and `-` successors: the `+` successor of `J(s)` under `J(a)` is `J(s^-)`, and its `-` successor is `J(s^+)`. Applying (5.1) to the state and both successors gives

```text
g_p(J(s),J(a))
 = E_{1-p}(s)
   - [1 + p E_{1-p}(s^-) + (1-p)E_{1-p}(s^+)]
 = g_{1-p}(s,a).
```

This is (5.3). Evaluation and differentiation at `p=1/2` give the final statements. QED.

The depth-10 exact defect family displays this theorem concretely. There are four positive unbiased defect magnitudes, each occurring in a sign pair, while the derivative multiset consists of the four exact `+/-` pairs

```text
±10813595521/34359738368,
±1388717721/17179869184,
±852562887/4294967296,
±4087921/67108864.
```

B15 therefore succeeds as a structural explanation: the unbiased problem hides an orientation variable that an infinitesimal input bias makes visible. It does not by itself move `sigma`; the source movement comes from installing the paired positive-defect actions at `p=1/2`.

## 6. Exact stronger depth-4 policy

Start from the preceding explicit 20-patch depth-4 policy with exact expected cost

```text
U_before = 1332517664326644559 / 36028797018963968
         = 36.98479479137941...
```

The recovered exact search/certificate installs sign-equivariant positive-defect patches at four successive query clocks. Each stage is evaluated against the immediately preceding policy and then adopted before the next stage.

```text
clock  reachable states  new patches  sign orbits  exact root cost after stage
10     155               8            4            1332501816044412239 / 36028797018963968
11     254               4            2            1332497576336439119 / 36028797018963968
12     414               4            2            1332495381349676879 / 36028797018963968
13     658               4            2            1332477360033879887 / 36028797018963968
```

The final deterministic policy contains 40 stored override states. Its table hash is

```text
e3ffa83af5107d8805e32e25c86be204a1bb4a5c088b732cc3f159c062a5454f.
```

The certificate verifies every override is a legal one-leaf query, every successor strictly decreases unresolved-leaf rank, and the whole table is globally sign-equivariant. Thus it is a genuine finite zero-error decision tree policy, not an abstract value assignment.

Its exact expected cost is

```text
U_new = 1332477360033879887 / 36028797018963968
      = 36.98367612253394...,
```

with exact improvement

```text
U_before - U_new
 = 39359660903 / 35184372088832
 = 0.001118668845464299...
```

The independent exact performance-difference recursion reproduces every stage gain and ends

`ALL_EXACT_STRONGER_POLICY_PERFORMANCE_CHECKS_PASS`.

The compressed canonical certificate independently checks the legal-move/rank/symmetry facts, the stage ledger, the B15 derivative pairing, the B25 occupancy identity, and the source-number conversion, ending

`ALL_EXACT_CANONICAL_POLICY_CERTIFICATE_CHECKS_PASS`.

These are P13 self-checks, not OTHER-track audits.

## 7. Source-domain movement

### Proposition 7.1 (stationary four-level block composition)

If a zero-error depth-4 recursive-majority policy has unbiased expected leaf-query cost `U`, then for every positive integer `m` there is a zero-error policy for depth `4m` with expected cost `U^m`. Consequently

```text
c = lim_k D_k^(1/k) <= U^(1/4).
```

#### Proof

Induct on `m`. For `m=1`, use the given depth-4 policy. For depth `4m`, view the top four levels as a depth-4 majority tree whose 81 virtual leaves are roots of independent depth-`4(m-1)` recursive-majority subtrees. Run the fixed depth-4 policy on those virtual leaf values. Whenever it requests a virtual leaf, evaluate that entire lower subtree using the inductively constructed policy.

Each lower subtree output is unbiased and independent of all other lower subtree outputs. Before a virtual leaf is requested, the event that the top policy requests it depends only on previously evaluated virtual leaves, hence is independent of that lower subtree's internal input. Thus the expected cost factorizes: the top policy requests `U` virtual leaves on average, and each requested lower subtree costs `U^(m-1)` on average. The total expected cost is `U^m`. Therefore `D_{4m} <= U^m`. Since the already established submultiplicative limit `c=lim_k D_k^(1/k)` exists, taking `4m`-th roots and `m -> infinity` gives `c <= U^(1/4)`. QED.

Apply the proposition to `U_new`. Exact high-precision conversion gives

```text
c <= 2.4660536425240241936481564864589771622596431517084...
```

and therefore

```text
sigma >= 1 - (1/4) log_3(U_new)
      = 0.1784006362716093315031419488278981128551184903536...
```

The existing rigorous source-side upper endpoint remains

```text
sigma <= log_3(4/3)
      = 0.2618595071429148741990542286855217085991712802638...
```

so the frozen interval width is now

```text
W_sigma
 = 0.0834588708713055426959122798576235957440527899102...
```

The lower endpoint gain, equivalently the width contraction, is

```text
0.0000068830425466660623599296208074229957199067060...
```

up to the displayed precision inherited from the preceding decimal baseline. This is genuine source-domain movement: an explicit legal policy decreases a rigorous upper bound on the asymptotic decision-cost growth constant, which increases the rigorous lower endpoint for the source exponent.

## 8. B3 residual-support route: precise failure and what remains useful

The previous run found that on all 12 terminal residual state types generated by the exact optimal `h=2` outer policy,

```text
V_2(s) <= D_2 [1-m(s)^2],
```

while the same inequality is globally false at the explicit state

```text
s^dagger = (-,(-,u,u),(-,u,u))
```

with violation ratio `512/393 > 1`.

The attempted stronger induction in this run would need a class `R_h` of residual states satisfying both:

1. every state actually left unfinished by an optimal outer depth-`h+1` policy lies in `R_h`; and
2. the Bellman successors needed to prove the cost/uncertainty estimate remain inside a recursively controlled class.

I do not have that closure. In fact the earlier depth-4 Bellman improvements already show why a naive child-local induction is unsafe: a globally better outer action can be locally suboptimal for completing the currently touched child. Thus the support-restricted inequality remains a plausible route but is not promoted to a theorem here.

The successful B3 replacement is Theorem 4.1: instead of demanding a pointwise invariant strong enough to force the whole optimum, prove a stronger exact comparison theorem for arbitrary finite policy modifications and use total occupancy to accumulate rigorously certified local improvements.

## 9. Status and next research direction

C0021 remains **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL**. The exact exponent is not determined. No closure, novelty certificate, P26 audit, second OTHER-track audit, or paper package is claimed. The unchanged-run streak resets to zero because the frozen source metric moved.

The next nonrepeating research triple is **B10, B22, B28**:

- B10: replace the 40-state override table by a deterministic symbolic rule and prove that it reproduces a positive fraction of the certified defects at every four-level scale;
- B22: read the failure modes in recursive-majority/decision-tree literature specifically for uniform expected complexity, looking for the missing lower-bound potential rather than another upper-bound patch;
- B28: weaken the false pointwise residual cost/uncertainty domination to an occupancy-weighted or typical-state inequality, which is exactly the form Theorem 4.1 suggests.

## 10. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  canonical_id: C0021
  category: CLOSABLE_OUTSIDE
  source_status: CURRENT_OPEN_LOOKING_BOUNDED_CHECK
  status_before: PARTIAL
  status_after: PARTIAL
  metric_name: W_sigma_rigorous_interval_width
  metric_domain: Garban-Steif Exercise VIII.5, one exponent sigma for unbiased iterated 3-majority
  metric_before: 0.0834657539138522087582722094784310187397726966161...
  metric_after: 0.0834588708713055426959122798576235957440527899102...
  movement: true
  unchanged_streak_before: 1
  unchanged_streak_after: 0
  methods_tried: [B3, B15, B25]
  theorem_ids:
    - P13-C0021-PERFORMANCE-DIFFERENCE-01
    - P13-C0021-SIGN-DEFECT-DERIVATIVE-01
    - P13-C0021-FOURLEVEL-COMPOSITION-01
  finite_policy:
    depth: 4
    patch_count: 40
    patch_table_sha256: e3ffa83af5107d8805e32e25c86be204a1bb4a5c088b732cc3f159c062a5454f
    exact_cost: 1332477360033879887/36028797018963968
  new_sigma_lower: 0.1784006362716093315031419488278981128551184903536...
  sigma_upper_unchanged: 0.2618595071429148741990542286855217085991712802638...
  exact_self_checks:
    - proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_canonical_policy_certificate_check.py
    - proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_canonical_policy_certificate_check.out
    - proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_stronger_policy_performance_check.py
    - proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_stronger_policy_performance_check.out
  closure_claimed: false
  external_audits_claimed: 0
  preserved_retirements: [I0051, P0082, D0093]
  peer_claim_not_touched: I0054
  next_methods: [B10, B22, B28]
```

No shared root ledger, peer file, historical report, claim file, workflow, permission, credential, public surface, email/Gmail item, Drive item, or schedule was modified by this report.