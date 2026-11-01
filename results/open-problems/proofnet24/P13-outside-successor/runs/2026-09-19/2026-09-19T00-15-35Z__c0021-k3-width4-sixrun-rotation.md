Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `W_sigma = 0.083457166870867772411698563411662... -> 0.083457166870867772411698563411662...`; C0021 unchanged-run streak `5 -> 6`; methods actually tried: B9, B19, B23.**

# P13 CLOSABLE OUTSIDE — exact K=3 interleaving computation and six-run rotation

UTC report time: 2026-09-19T00:15:35Z  
Repository / branch: private `yspennstate/math-open-problems` / `master`  
Own root: `proofnet24/P13-outside-successor/`  
Native slot: `6aa7b253b37c8191b693d8dc79298d37`  
Canonical claim entering this run: `operations/claims/C0021.md`

## 1. Continuity, source, ownership, exclusions

I continued the newest immutable P13 state rather than trusting the scheduler title. The predecessor report is

`proofnet24/P13-outside-successor/runs/2026-09-18/2026-09-18T23-50-42Z__c0021-interleaving-width-recovery2-no-movement.md`.

That report left C0021 at five consecutive source-metric-unchanged runs and selected exactly one recovery for this invocation: **reduce to and execute a finite computation**, namely the orientation-preserving `K=3` interleaving-capped Bellman problem for the explicit height-four lifted state `S4=L(S3)`.

The former P13 I0051 / Aldous--Janson Open Problem 9 clade-covariance route remains **RETIRED** and was not reopened. P0082 and D0093 remain at their historical handoffs. P22/P23/P25, old AF4.49(ii)/PROB20-13, DLA exponent work, and the POSTED/INDEX exclusions remain excluded. P13 stayed entirely on outside work.

The owner's mandatory first-screen lead I0054 was checked again before any successor action. R11 has a later immutable I0054 report at

`runs/R11/2026-09-18T23-38-11Z_i0054-polynomial-hash-u034-c055-b8e3.md`,

so I0054 remains actively occupied by a peer. P13 did not duplicate it or touch its claim.

The source was rechecked directly on 2026-09-19 UTC. The author-hosted Garban--Steif PDF page image for Chapter XIII rendered successfully and visibly states Open Problem XIII.1: find the randomized algorithm with smallest revealment for iterated majority, with even the decay exponent unknown. Fresh bounded web queries were:

- `"iterated majority" revealment exponent sigma randomized algorithm Garban Steif recursive majority 2026` (30-day window);
- `"recursive majority" revealment exponent decision tree 2026` (365-day window);
- `"iterated 3-majority" revealment algorithm`;
- `"Garban" "Steif" "iterated majority" 2026`, plus author-name variants.

They recovered the original source, Jansson--Jansson's 2023 two-level level-p complexity paper, Magniez et al.'s distinct worst-case randomized-decision-tree complexity line, and later author work on different iterated-majority observables, but no checked source-matching determination of this revealment exponent. This is bounded negative evidence only, not a worldwide openness or priority certificate.

The frozen source-faithful metric remains

`W_sigma = rigorous upper endpoint for sigma - rigorous lower endpoint for sigma`,

with all conventions unchanged. Entering this run,

`W_sigma = 0.083457166870867772411698563411662...`.

## 2. The explicit finite state carried into this recovery

The current lower-bound route is organized around the lifted height-four partial state

`S4 = L(S3)`,

whose posterior is exactly

`q(S4)=31/256`, hence `|m(S4)|=97/128`.

The previous run proved that bottom-level states may be represented exactly by the six orientation-preserving symbols

`U=(u,u,u), P=(+,u,u), M=(-,u,u), X=(+,-,u), +, -`,

with one-leaf transitions

`U -> P/M`, `P -> +/X`, `M -> X/-`, `X -> +/-`.

For a policy started from `S4`, define its **interleaving width** as the largest number of bottom blocks simultaneously entered but unfinished. Let `V^(K)(S4)` denote the minimum expected remaining number of leaf queries among deterministic zero-error policies whose width is at most `K` on every path.

Previously certified values were

`V^(1)(S4)=2739915/131072 = 20.90389251708984375`,

`V^(2)(S4)=1377453593/67108864 = 20.525658026337623596...`,

and a previously certified unrestricted explicit deterministic policy `pi_*` had

`E_pi*(S4)=10885886259/536870912 = 20.276543235406279563...`.

Thus the previous run established only that every unrestricted optimum has width at least three. The unresolved finite recovery was to decide `K=3` exactly.

## 3. B9 — RANDOMIZE: randomization cannot remove this finite obstruction

I first tried Section-B method 9 literally: allow a randomized zero-error policy under the fixed unbiased completion law and ask whether randomization can beat the deterministic capped optimum.

### Theorem (fixed-law Las Vegas randomization gives no expected-cost advantage)

Let `S` be any finite partial Boolean state, let `P` be any fixed input law on its unresolved leaves, and let `A` be any class of deterministic zero-error decision trees closed under conditioning on an external random seed (for example, all width-`<=K` policies). Then

`inf_randomized E_P,cost = inf_deterministic-in-A E_P,cost`.

### Proof

A zero-error randomized algorithm is a distribution over deterministic decision trees obtained by conditioning on its complete external random seed. Because the algorithm is zero-error, every seed in its support defines a correct deterministic tree; if a pathwise width cap is required, every conditioned tree obeys the same cap. If `C(r)` is the expected query cost under input law `P` for seed `r`, then by Fubini/linearity

`E_{r,x} cost = E_r C(r)`.

An average cannot be smaller than the infimum of the quantities averaged, so some deterministic seed has expected cost at most the randomized average. The reverse inequality holds because deterministic trees are a special case of randomized ones. QED.

For C0021 this matters twice. First, in the source symmetry reduction, randomization can symmetrize which leaf is queried without lowering the underlying optimal *average* number of queries `D_h`; that is why revealment can be recovered from the deterministic fixed-law optimum. Second, randomization cannot evade the width-three finite obstruction below. B9 therefore **fails as an escape route**: the relevant objective is linear in the external random seed.

## 4. B19 — MAKE IT AN ALGORITHM: exact `K=3` Bellman solver

The new mathematical idea was to turn the six-symbol oriented automaton into a compiled exact finite dynamic program rather than retry the earlier slow unrestricted recursion.

For every canonical state `s`, let `a_K(s)` be the set of legal one-leaf query actions whose two successors both have at most `K` active unfinished bottom blocks. Because every query reduces unresolved rank by one, the state graph is finite and acyclic. Therefore backward induction gives the exact recurrence

`V^(K)(s)=0` for terminal `s`, and otherwise

`V^(K)(s) = 1 + min_{a in a_K(s)} ( V^(K)(s_a^+) + V^(K)(s_a^-) )/2`.

This recurrence is exact, not a relaxation: the six-symbol language is exactly the canonical set of partial states of each bottom `MAJ_3` block, recursive sibling sorting quotients only source symmetries, and every legal leaf query occurs as one recurrence action. Conversely every recurrence action is a legal leaf query. A rank induction therefore identifies the DP value with the true optimal width-capped expected cost.

The new C++ self-check evaluates expectations as integers scaled by `2^81`. Since a depth-four ternary majority has 81 leaves and each unresolved outcome is fair, every finite zero-error decision tree has a dyadic expected cost with denominator dividing `2^81`; every division by two is checked for exact divisibility.

The executed exact output is:

- `K=1`: `2739915/131072`; 53,155 nonterminal memo states;
- `K=2`: `1377453593/67108864`; 409,999 nonterminal memo states;
- `K=3`: **`2801905528867/137438953472`**; 2,220,303 nonterminal memo states.

In decimal form,

`V^(3)(S4) = 20.386545866982486...`.

The exact incremental option value from permitting a third simultaneously active block is

`V^(2)-V^(3) = 19119429597/137438953472 = 0.1391121593551361...`.

The checker independently regenerates the canonical decision graph from the majority recursion, recomputes all three capped values, and ends

`ALL_EXACT_K3_WIDTH4_ROTATION_CHECKS_PASS`.

This is a **P13 self-check**, not an independent audit.

## 5. B23 — DO WHAT THE PROPOSER DID NOT EXPECT: width three is still insufficient

The bounded-interleaving heuristic tacitly hoped that once a small number of blocks could be open simultaneously, unrestricted option value would essentially be captured. B23 assumes the opposite and checks it exactly.

The previously exact-certified unrestricted explicit policy satisfies

`E_pi*(S4)=10885886259/536870912`.

The new exact capped optimum is

`V^(3)(S4)=2801905528867/137438953472`.

Putting the explicit policy on the same denominator gives the exact strict gap

`V^(3)(S4)-E_pi*(S4)`

`= 15118646563/137438953472`

`= 0.11000263157620793... > 0`.

Therefore:

### Theorem (height-four interleaving-width obstruction)

Every unrestricted optimal deterministic zero-error policy started from `S4` has interleaving width at least **four**.

### Proof

By the exact Bellman computation, every width-`<=3` policy has expected cost at least `V^(3)(S4)`. The explicit unrestricted zero-error policy `pi_*` has strictly smaller expected cost. Hence no width-`<=3` policy is unrestricted-optimal. QED.

By the B9 theorem, allowing external randomization does not change this fixed-law expected-cost conclusion. Thus the finite obstruction is not an artefact of deterministic tie-breaking: genuinely useful option value survives beyond three concurrently open blocks.

This is new finite structural movement, but it is **not source-metric movement**. It neither improves the explicit source-valid depth-four policy upper bound for `D_4` nor proves a new asymptotic lower base for `D_h`.

## 6. Why the source metric is unchanged

The current asymptotic lower-bound mechanism is

`D_{h+1} >= (3-beta_h) D_h`.

A source-level improvement of the upper endpoint for `sigma` requires a height-uniform theorem

`sup_h beta_h < 3/4`.

The strongest surviving candidate route is the oriented progress/Hölder inequality, whose first unproved lifted case is

`16 C_4(S4)^2 >= 9 D_4^2 (97/128)^3`,

where

`C_4(s)=D_4 - V_4(s) + A_4(s)`

is the regret-corrected oriented shortest-path progress. The K=3 computation determines only a capped version of `V_4(S4)` and does not determine unrestricted `V_4(S4)` or the minimum accumulated regret `A_4(S4)`. In fact, the width-at-least-four theorem shows that any proof of the displayed inequality must control option value from at least four simultaneously open blocks.

Therefore the rigorous exponent interval remains exactly at the predecessor values. The frozen width stays

`W_sigma = 0.083457166870867772411698563411662...`.

No auxiliary finite theorem is counted as movement on that metric.

## 7. Six unchanged runs: mandatory full stuck report and terminal rotation

This is the sixth consecutive source-metric-unchanged run after the last movement. The owner rule for a CLOSABLE target therefore fires now. C0021 is **not closed**; P13 must hand it off and rotate rather than start a seventh unchanged attack.

### Exact blocking formula

The lower-bound side still reduces to

`D_{h+1} >= (3-beta_h) D_h`,

and source movement needs `sup_h beta_h < 3/4`. Equivalently, the present oriented route needs a scale-uniform control on how unrestricted inter-block switching changes `C_h/D_h` while retaining sign orientation.

### Every route actually tried on C0021 and its decisive outcome/failure

- **B2/B6/B25 (admission run):** counterexample search, deformation, and two-way counting recovered the exact fixed-law reduction and source interval but did not determine the asymptotic constant.
- **B11/B12/B24:** dualization/conservation plus an extremal one-deviation search found a depth-four policy improvement and moved the source interval; it remained a finite block policy.
- **B3/B19/B27:** stronger statement + explicit algorithm + quantifier swap built a stationary depth-four family and moved the source interval; no matching arbitrary-height lower theorem resulted.
- **B5/B14/B18:** bias differentiation, sign group action, and finite MDP language exposed exact defect symmetries and yielded further finite policy movement; still a finite-depth construction.
- **B7/B13/B30:** limiting-state compression failed because `(p,V)` loses sign orientation; the martingale residual identity `E[R m_J]=-1/2` was proved, but the global uncertainty domination it suggested is false.
- **B3/B15/B25:** arbitrary finite-patch performance-difference and sign-orientation accounting produced more source-moving depth-four patches; no scale-free action rule emerged.
- **B10/B22/B28:** derandomized surrogate / failure-literature / occupancy weighting gave further depth-four patches; the deterministic “buy a child outright” surrogate reverses the true Bellman ordering because it misses interleaving option value.
- **B11/B17/B26:** a queried-sign dual-slack identity and prior-art correction isolated the exponential lower-bound remainder; another finite patch moved the upper-policy endpoint, but the slack lacked a recursive lower law.
- **B1/B12/B27:** stochastic-control reformulation and regret-corrected concave envelope gave finite lower bounds; a pointwise uncertainty inequality already fails at height two, while a height-uniform envelope bound remained unproved. This began the present unchanged streak.
- **B4/B16/B21:** terminal martingale laws and an exact feasible-residual three-child DP greatly sharpened finite lower bounds (`beta_2`), but exact `beta_3` had a prohibitively large raw state space and no uniform theorem followed.
- **B8/B20/B29:** a rigorous abstract quotient upper-bound was sound but nearly 1 and therefore useless; collision analysis proved missing orientation information; a `3/2`-Hölder progress candidate survived complete heights 1--3 but had no one-edge proof.
- **B2/B15/B30 (STUCK1 recovery 1):** recursively lifted the height-three extremizer to fixed magnetization, proved the oriented shortest-path representation of progress, and solved forced-block scaling. Direct unrestricted height-four exact Bellman evaluation did not finish; simple scaling was not the failure mechanism.
- **B6/B18/B24 (STUCK1 recovery 2):** exact orientation-preserving six-symbol language and width-1/2 Bellman problems showed an explicit unrestricted policy beats the entire width-2 class; the first K=3 attempt did not complete in the then-used implementation.
- **B9/B19/B23 (this run):** randomization was proved unable to lower fixed-law capped expected cost; an optimized exact algorithm solved K=3; assuming small-width sufficiency was wrong again, because an explicit unrestricted policy beats the exact entire width-3 class. This strengthens the finite obstruction to width at least four but still does not move the asymptotic exponent interval.

### Missing ingredient

A scale-independent, orientation-sensitive inequality that survives unrestricted multi-block switching. Any adequate state language must retain branch-value skew, and any proof must control option value from an unbounded or provably sufficient number of simultaneously active blocks. Posterior alone, `(p,V)`, forced block completion, width two, and now width three are all insufficient.

### Simplest unproved case

The first concrete unresolved checkpoint remains the single state `S4=L(S3)`:

`16 C_4(S4)^2 ? >= 9 D_4^2 (97/128)^3`.

The new width theorem says solving it exactly requires at least width-four interleaving geometry; a width-three reduction cannot be exact.

### Nearest solved analogues

The exact finite analogues are the completed width-1/2/3 Bellman problems above and the complete height-1/2 feasible residual DPs. The closest continuous solved-shape analogue remains the one-level three-diffusion majority scheduling problem of Jacka--Warren--Windridge; their recursive multilevel Brownian problem does not supply the missing multiplicative arbitrary-height structure.

### Exactly one mandated recovery

**HAND OFF AND ROTATE.**

No seventh C0021 research refinement is authorized for P13 under the six-unchanged-run rule. The existing canonical claim is preserved as historical evidence; this report records P13's terminal handoff and does not assert mathematical closure.

## 8. Successor admission after rotation

After the terminal handoff I re-entered the current CLOSABLE OUTSIDE admission gate rather than inventing a replacement.

- The mandatory first lead I0054 is still actively occupied by R11, including a newer 2026-09-18 23:38 UTC report; skip.
- Current coordinator/neighbor admission screens have cumulatively reconciled the populated I-series through I0130. The newest post-rotation R01 delta at `runs/R01/20260918T2206Z_post_rotation_admission_delta_9f31c6a2.md` reports that later newly created canonical claims are all owner-bound and that repository searches still do not recover a populated I0131+ source row.
- Earlier current screens already dispose of the intervening rows by active ownership, HARD lane, exact-scope exclusion, known/refuted status, or PENDING/retired lifecycle. I did not reinterpret an absent claim as a release.

Accordingly, **no lawful unowned full-source CLOSABLE successor is admitted this invocation**. P13 leaves C0021 in terminal handoff and enters

`SUCCESSOR_ADMISSION_HOLD / successor metric UNMEASURED`.

This admission hold is not a seventh unchanged mathematical run on C0021 and does not reset or rename the C0021 metric. A future run should do a delta-only admission screen for a genuinely new populated source, explicit release/reassignment, or source-status change; it should not restart C0021 or the exhausted static queue from rank 1.

No new canonical claim was created because no candidate crossed every admission gate.

## 9. Exact artifacts and execution receipt

New exact self-check source:

`proofnet24/P13-outside-successor/artifacts/2026-09-19/c0021_b9_b19_b23_2026-09-19T00-13-57Z_check.cpp`

New archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-19/c0021_b9_b19_b23_2026-09-19T00-13-57Z_check.out`

Local compilation/execution used `g++ -O3 -std=c++20`. The output ended in `ALL_EXACT_K3_WIDTH4_ROTATION_CHECKS_PASS`. The source and output are self-check artifacts, not independent audits. The previous explicit-policy value used in the strict comparison was already exact-certified in the predecessor P13 artifact; this run's checker recomputes K=1/2/3 and verifies the exact rational comparison against that certified constant.

No paper package is created because the source problem is not closed. No P26 or second-track closure audit is requested. P13's separate secondary audit duty to P14 remains whatever its current completed/handoff state already records; this run did not repeat it.

## 10. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  category: CLOSABLE_OUTSIDE
  canonical_target_before: C0021
  source: Garban-Steif Open Problem XIII.1 / Exercise VIII.5
  state_before: CLAIMED_PARTIAL_STUCK1_RECOVERY2
  state_after: C0021_TERMINAL_HANDOFF__SUCCESSOR_ADMISSION_HOLD
  metric:
    name: W_sigma
    before: 0.083457166870867772411698563411662...
    after: 0.083457166870867772411698563411662...
    movement: false
  unchanged_run_streak:
    before: 5
    after: 6
  methods_this_run: [9, 19, 23]
  method_outcomes:
    9: randomized zero-error fixed-law mixtures cannot beat the best deterministic member; no escape from capped Bellman obstruction
    19: exact orientation-preserving Bellman algorithm computes K=3 cap for S4
    23: opposite-of-small-width hypothesis wins; exact K=3 class is still beaten by a certified unrestricted policy
  finite_exact_result:
    state: S4=L(S3)
    posterior_q: 31/256
    abs_m: 97/128
    V_cap1: 2739915/131072
    V_cap2: 1377453593/67108864
    V_cap3: 2801905528867/137438953472
    cap2_minus_cap3: 19119429597/137438953472
    explicit_unrestricted_policy: 10885886259/536870912
    cap3_minus_explicit: 15118646563/137438953472
    theorem: any unrestricted optimum from S4 has interleaving width at least 4
  source_movement_from_finite_result: false
  blocking_formula: D_{h+1} >= (3-beta_h) D_h
  source_moving_requirement: sup_h beta_h < 3/4
  simplest_unproved_case: 16*C4(S4)^2 >= 9*D4^2*(97/128)^3
  rotation:
    fired: true
    reason: six consecutive unchanged CLOSABLE runs
    action: HANDOFF_AND_ROTATE
    closure_claimed: false
  successor:
    admitted: false
    status: SUCCESSOR_ADMISSION_HOLD
    metric: UNMEASURED
    I0054: peer_owned_R11
    current_populated_I_frontier: I0130
    populated_I0131_plus_seen: false
  artifacts:
    checker: proofnet24/P13-outside-successor/artifacts/2026-09-19/c0021_b9_b19_b23_2026-09-19T00-13-57Z_check.cpp
    output: proofnet24/P13-outside-successor/artifacts/2026-09-19/c0021_b9_b19_b23_2026-09-19T00-13-57Z_check.out
    checker_status: SELF_CHECK_PASS
  new_claim: null
  closure_audits_requested: 0
  paper_package: null
  shared_root_edits: none
  peer_edits: none
  scheduler_changes: none
```

## 11. Status after this invocation

C0021 is **OPEN / PARTIAL / TERMINAL HANDOFF FROM P13 AFTER SIX UNCHANGED RUNS**. The new exact finite theorem is that width three is still insufficient for the lifted height-four witness; it is preserved for any future lawful assignee. P13 itself is now **CLOSABLE OUTSIDE / SUCCESSOR_ADMISSION_HOLD / successor metric UNMEASURED**. No closure, universal novelty claim, global openness certificate, peer audit, scheduler change, email, Drive action, public post, permission change, workflow execution, force-push, or paid compute occurred.
