Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. SOURCE-METRIC MOVEMENT: W_sigma = 0.0840175985788401785... -> 0.0837399423382529385...; C0021 unchanged-run streak 1 -> 0. Methods actually tried: B11, B12, B24.**

# P13 C0021 — depth-4 one-deviation improvement

Date: 2026-09-18 UTC.  Track: P13 Outside Counterexample Research.  Native slot: `6aa7b253b37c8191b693d8dc79298d37`.  Own root: `proofnet24/P13-outside-successor/`.

## 1. Recovered state and exclusions

The active create-only ownership marker remains `operations/claims/C0021.md`: C0021, Garban--Steif Exercise VIII.5, revealment exponent of iterated 3-majority.  This run did not touch retired I0051, handed-off P0082, or six-run-handed-off D0093.  The R7-01 C0021 note remains a shard-mismatch rejection with no competing claim.  A same-day NM13 report also recognizes C0021 as P13's active CLOSABLE claim.

The intake row is `probability_1000_intake_claude_20260907/problems.jsonl`, where C0021 asks to determine the exponent `sigma` in the decay of revealment for iterated 3-majority and is historically `source_says_open`; the old attempt ledger row `C0021-A001` only gave the former interval `[0.166,0.369]`.  The later repository memo improves and corrects that to the exact reduction

    delta_{f_k} = D_k / 3^k,
    sigma = 1 - log_3(c),  c = lim_k D_k^(1/k),

with

    D_1 = 5/2,
    D_2 = 393/64,
    D_3 = 15796051/1048576,

and the prior certified explicit depth-4 policy cost

    U_4 = 20871140813662641 / 562949953421312.

The source-side upper endpoint remains

    sigma_U = log_3(4/3) = 0.2618595071429148741990542286855... .

The frozen metric is the rigorous source interval width `W_sigma = sigma_U - sigma_L`, target zero.  Before this run,

    sigma_L(old) = 0.1778419085640746956828387359782...,
    W_sigma(old) = 0.08401759857884017851621549270733... .

No auxiliary lemma counts as movement; only a rigorous endpoint improvement for this same exponent does.

## 2. Dated source / literature refresh

Queries run on 2026-09-18 included `Exercise VIII.5 iterated 3-majority revealment sigma`, `recursive majority expected cost decision tree 2024 2025 2026`, `recursive majority Schramm Braverman 2.28 expected cost`, and `recursive majority generalized costs`.

* Garban--Steif, *Noise Sensitivity of Boolean Functions and Percolation* (Cambridge, 2014), Exercise VIII.5 remains the controlling source as recovered in the admission record; no later source-matching determination of `sigma` was found in this bounded refresh.
* Julia Jansson and Patrik Jansson, *Level-p-complexity of Boolean functions using thinning, memoization, and polynomials*, JFP 33 (2023), computes the two-level problem and agrees at `p=1/2` with `D_2=393/64`; it does not determine the asymptotic exponent.
* Jacka--Warren--Windridge, *Minimising the time to a decision* (Ann. Appl. Probab. 2011), explicitly discusses this same uniform expected-cost growth constant.  Their text records the published lower bound `9/4`, numerics near `2.45`, and a footnote that Schramm and Braverman communicated an improvement to `2.28` but did not publish details.  I therefore do not import `2.28` as a theorem.
* Leonardos's generalized-cost paper and later Magniez--Nayak--Santha--Sherman--Tardos--Xiao bounds concern worst-case/randomized decision-tree complexity under different objectives/distributions.  They are technique analogues, not source-level bounds on the uniform expected cost `D_k` used here.

This is bounded negative evidence only; it is not a claim of worldwide openness or novelty.  No material primary-source access failure affected the mathematics below.

## 3. Idea before computation

The previous run's residual-completion route suggested looking for a lower bound.  Instead B11 exposed a cheaper way to move the frozen interval: dualize the already certified depth-4 policy `pi_0` by inspecting its exact Bellman residuals.  A positive residual at any reachable state immediately produces a strictly better explicit policy, hence a better upper bound on `D_4`, hence a larger rigorous lower bound on `sigma`.

The earliest state where a nontrivial choice exists is after the first queried leaf.  The baseline depth-4 heuristic `pi_0` then starts an untouched depth-3 root child.  The candidate deviation is the opposite: query a second leaf in the same bottom `MAJ_3` gate inside the already touched depth-3 root child, then revert forever to `pi_0`.

The striking feature, checked below, is that this deviation is *locally suboptimal* for completing the touched child but globally better for deciding the depth-4 root.

## 4. B11 — Bellman dual / one-state policy-improvement lemma

Let `pi` be any fixed deterministic exact policy on a finite unbiased decision problem and let `E_pi(s)` be its exact expected remaining number of queries from state `s`.  For a legal query `a` at `s`, with successor states `s^+` and `s^-`, define

    Q_pi(s,a) = 1 + (E_pi(s^+) + E_pi(s^-))/2.

**Lemma (one-state Bellman improvement).** If `Q_pi(s,a) < E_pi(s)`, then the policy `pi'` which uses `a` at `s` and thereafter follows `pi` has exact value `E_pi'(s)=Q_pi(s,a)<E_pi(s)`.  If a predecessor reaches `s` with probability `p`, keeping all other decisions unchanged decreases the predecessor value by exactly `p(E_pi(s)-Q_pi(s,a))`.

**Proof.** Conditional on making query `a`, its value is one unit of query cost plus the average of the two continuation costs, because the queried unrevealed bit is unbiased and independent of the history.  After the query `pi'` and `pi` agree, so those continuation values are exactly `E_pi(s^+)` and `E_pi(s^-)`.  This proves the first identity.  At any unchanged predecessor, linearity of conditional expectation propagates the value difference multiplied by the probability of reaching `s`.  QED.

I re-evaluated the archived baseline policy with exact `Fraction` arithmetic and reproduced

    E_0(root depth 4) = U_4
                      = 20871140813662641 / 562949953421312.

After the first query, either sign leads (by sign symmetry) to a one-bit state with

    E_0(s_+) = E_0(s_-)
             = 20308190860241329 / 562949953421312
             = U_4 - 1.

For the deviation described above, exact baseline continuation evaluation gives, for the two outcomes from `s_+`,

    C_+ = 39081644577912289 / 1125899906842624,
    C_- =  9949379448235949 /  281474976710656.

Therefore its exact branch value is

    Q_0(s_+,a*)
      = 1 + (C_+ + C_-)/2
      = 81130962184541333 / 2251799813685248
      = 36.0293848909082705... .

By sign symmetry the same value holds from `s_-`.  Hence the full modified policy `pi_*` has

    U_4* = E_{pi_*}(root)
         = 1 + Q_0(s_+,a*)
         = 83382761998226581 / 2251799813685248
         = 37.0293848909082705... .

The exact strict gain over the old explicit policy is

    U_4 - U_4*
      = 101801256423983 / 2251799813685248
      = 0.04520883952707022... > 0.

This is a theorem-sized finite policy statement: `D_4 <= U_4*` because `pi_*` is an explicit exact decision tree policy.

## 5. B12 — conserved posterior, and why the better move is locally worse

Condition on the first answer being `+`.  The touched depth-3 child has posterior `9/16`; the other two root children remain at `1/2`, so the depth-4 root posterior is

    q_root = MajProb(9/16,1/2,1/2) = 17/32.

The new second query stays in the same bottom majority gate.  Its two outcomes move the touched child's posterior to `5/8` or `1/2`; consequently the depth-4 root posterior moves to `9/16` or `1/2`.  Thus

    (9/16 + 1/2)/2 = 17/32,

as required by the posterior martingale.  So posterior mean cannot distinguish the two choices.

More importantly, the new move is not locally optimal inside that touched depth-3 child.  Its local one-step completion value is

    14776803 / 1048576,

whereas the exact local optimum is

    V_3(touched state) = 14747475 / 1048576.

The deliberate local sacrifice is therefore

    14776803/1048576 - 14747475/1048576
      = 1833/65536
      = 0.0279693603515625.

Yet at the depth-4 root the move *saves* `0.0452088395...` expected queries.  This proves a concrete structural point: an optimal outer policy need not make a locally optimal query inside the child it touches.  Any asymptotic ansatz that forces child-local Bellman optimality loses valid globally useful interleavings.

This is the conserved-quantity lesson of B12: the posterior martingale is unchanged, but the arrangement of partial information among recursive subtrees matters beyond scalar posterior and child-local completion cost.

## 6. B24 — extremal one-bit state / exact one-deviation search

The first one-bit state is the earliest nontrivial symmetry-breaking state of depth 4.  I enumerated its canonical legal next-query orbits and evaluated each against the exact baseline continuation `E_0`.  The same-bottom-gate query above is the strict best one-deviation at that state in this finite search.  Only the existence of this strict improving deviation is needed for the theorem; no claim about global depth-4 optimality is made.

This identifies a useful extremal object for the next run: the **earliest Bellman-defect state** of a recursively local policy.  Rather than attempting the intractable full depth-4 dynamic programme, search only reachable shallow states for positive Bellman residuals, splice those deviations into an explicit policy, and certify each improvement exactly.

## 7. Source-metric movement

Because `D_4 <= U_4*`, submultiplicativity gives

    c <= (U_4*)^(1/4),

hence

    sigma >= 1 - (1/4) log_3(U_4*)
          = 0.1781195648046619356672102637439... .

The source-side upper endpoint is unchanged:

    sigma <= log_3(4/3)
          = 0.2618595071429148741990542286855... .

Therefore the frozen interval moves from

    [0.1778419085640746956828387359782...,
     0.2618595071429148741990542286855...]

to

    [0.1781195648046619356672102637439...,
     0.2618595071429148741990542286855...],

and the frozen width moves

    W_sigma:
    0.08401759857884017851621549270733...
      ->
    0.08373994233825293853184396494162... .

Exact width improvement:

    0.0002776562405872399843715277657088... .

This is genuine source-metric movement.  The C0021 unchanged-run streak resets from `1` to `0`.

## 8. Exact self-check artifacts

The exact `Fraction` Bellman evaluation in this run first reproduced the old certified `U_4`, then evaluated the alternate successor states above.  A compact arithmetic self-check was executed and archived at

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_depth4_one_deviation_check.py`

with output

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_depth4_one_deviation_check.out`.

The output ends `ALL_EXACT_ARITHMETIC_CHECKS_PASS`.  It checks the exact rational policy improvement, posterior identity, local-optimality sacrifice, and both old/new source interval endpoints.  This is a **self-check**, not an independent audit.  The baseline-policy evaluator itself is the previously archived `prob1000_lean_20260908/ultracode_20260909/C0021/policy_heur.py`; no claim is made that the compact arithmetic checker independently recomputes the entire 37k-state baseline policy.

## 9. What remains

The exact exponent is not determined.  The improvement is only a better explicit depth-4 policy, so C0021 remains **OPEN-LOOKING / PARTIAL**, not solved.  In particular, the source-matching closure target would require identifying the exact exponential growth constant `c` (equivalently `sigma`), not merely improving a finite-depth upper bound.

The present mechanism suggests a finite-state route: recursively local policies have detectable shallow Bellman defects because outer value can reward a query that is locally suboptimal inside a child.  The next run should test whether a small finite automaton of such defect states yields a repeatable composition rule, rather than merely another isolated depth-4 patch.

Next distinct methods: **B3, B19, B27**.

* B3: strengthen the one-state deviation into a certified family of shallow deviations and ask whether the depth-4 improvement composes at every scale.
* B19: design an explicit finite-state recursive policy whose state records only the small set of Bellman-defect patterns needed to reproduce the interleaving.
* B27: swap the asymptotic quantifiers by first proving a stationary finite-state policy has a fixed per-level growth factor, then optimize that factor exactly.

## 10. Structured ledger_delta for P26

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
    before: "0.08401759857884017851621549270733..."
    after: "0.08373994233825293853184396494162..."
    movement: true
    delta: "-0.0002776562405872399843715277657088..."
  endpoint_delta:
    sigma_lower_before: "0.1778419085640746956828387359782..."
    sigma_lower_after: "0.1781195648046619356672102637439..."
    sigma_upper_unchanged: "0.2618595071429148741990542286855..."
  mathematical_delta:
    old_depth4_policy_bound: "20871140813662641/562949953421312"
    new_depth4_policy_bound: "83382761998226581/2251799813685248"
    exact_cost_gain: "101801256423983/2251799813685248"
    theorem: "D_4 <= 83382761998226581/2251799813685248"
  methods:
    B11: "Bellman-dual one-state policy improvement; positive exact residual found"
    B12: "posterior martingale conserved; improving global move proved locally suboptimal by 1833/65536"
    B24: "earliest one-bit Bellman-defect state isolated and canonical next-query orbits checked"
  unchanged_streak:
    before: 1
    after: 0
    reason: "frozen source interval strictly narrowed"
  exact_artifacts:
    checker: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_depth4_one_deviation_check.py"
    output: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_depth4_one_deviation_check.out"
    output_tail: "ALL_EXACT_ARITHMETIC_CHECKS_PASS"
    audit_status: "self-check only"
  literature:
    checked_date: "2026-09-18"
    source_match_found: false
    caveat: "bounded negative search is not a global openness or novelty certificate"
    closest_same_object: "Jacka-Warren-Windridge 2011; Jansson-Jansson 2023"
    unpublished_note: "JWW footnote reports Schramm-Braverman 2.28 communicated without published details; not imported"
  closure: false
  audits_required_for_closure: "P26 plus one distinct OTHER-track end-to-end audit, after a source-exact full result"
  next_methods: [B3, B19, B27]
```

No shared root ledger, peer file, historical report, workflow, permission, public post, email/Gmail item, Drive item, credential, paid-compute resource, or schedule was modified.
