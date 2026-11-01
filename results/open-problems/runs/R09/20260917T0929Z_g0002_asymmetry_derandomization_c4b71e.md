Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in the frozen source metric: `Delta_8 = UNMEASURED -> UNMEASURED`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported unchanged count `6`. Methods actually used: B15 BREAK THE SYMMETRY ON PURPOSE, B24 FIND THE EXTREMAL OBJECT, B10 DERANDOMIZE.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-run telemetry, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0002: asymmetry ladder and deterministic conditional-H2 witnesses

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source status, and ownership

I did **not** reopen Pengfei Tang Question 4.11. Its periodic-tree clause remains mathematically refuted, audited and packaged; its transitive-graph clause remains open; the former R09 metric remains frozen at `UNBOUNDED_ABOVE` after the six-unchanged CLOSABLE retirement threshold.

The active exclusive successor remains `G0002`, Raphaël Cerf, *theta(p_c,Z^d)=0?*, arXiv:2608.23661v1, Conjecture 53.1, under `operations/claims/G0002.md`. Its frozen source metric remains

`Delta_8 = max_{phi in {phi_2, phi_{2\1}}} [max_{outside band} phi(A) - max_{inside band} phi(A)]`

for increasing `A subset {0,1}^8`, with conjectured band

`{|omega| >= 5} subset A subset {|omega| >= 2}`.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the live G0002 claim, the newest own R09 report, the newest neighboring R08 report, and the canonical intake/attempt record for G0002. The newest R08 report explicitly treats R09's H2 reconstruction as **NOT SOURCE VERIFIED** and correctly declines to manufacture an audit of it.

A fresh dated source/current-literature search on 2026-09-17 again recovered Cerf's arXiv record, submitted 2026-08-24, and no later source-matching resolution of Conjecture 53.1 in the bounded search. This is negative search evidence only, not a novelty certificate.

The exact source formulas (51.1)-(52.1) remain inaccessible in this runtime. Repository metadata says the original intake copied statements from a downloaded local text extraction, but that raw `sources/cerf_theta_pc_2026/text.txt` is not committed at the recorded path; a direct repository fetch returns 404. Current web retrieval gives the arXiv metadata/abstract and secondary descriptions of higher-order pivots, but not a trustworthy source rendering of formulas (51.1)-(52.1). Therefore I continue to **refuse to identify the conditional H2 functional with Cerf's actual `phi_2` or `phi_{2\1}`**, and `Delta_8` remains `UNMEASURED`.

## 2. Conditional setup retained from the previous run

Only for route discovery, retain the explicit research hypothesis H2 from the previous R09 reports. If `B_i(A)` is the ordinary positive-pivotal section boundary in coordinate `i`, define the factor-two-free conditional objectives

`psi2_H2(A) = sum_i |N_1(B_i(A))|`,

`psi2m1_H2(A) = sum_i (|N_1(B_i(A))| - |B_i(A)|)`.

These are **not source claims**. Their purpose is to mine structural candidates which can be evaluated immediately against Cerf's real formula once the missing normalization is recovered.

The previous exact self-check had found:

- best `S_5 x S_3`-invariant upper-out H2 candidate: `(psi2,psi2m1,boundary)=(862,584,278)`;
- an explicit asymmetric upper-out candidate: `(924,670,254)`;
- an explicit inside-band candidate: `(910,654,256)`.

The `924>862` gap already warned that stabilizer symmetrisation is unsafe. This run asks *how much symmetry must be broken, and can the resulting object be made deterministic and compact?*

## 3. B15 — BREAK THE SYMMETRY ON PURPOSE

### 3.1 The strongest current H2 upper-out witness is genuinely fully asymmetric

I rechecked the 26-minimal-set upper-out family from the preceding run and exhaustively tested all `8! = 40320` coordinate permutations. Its coordinate-permutation automorphism group has size exactly

`1`.

So its H2 advantage is not hiding a nontrivial coordinate symmetry: among coordinate permutations, the identity is the only automorphism.

Its Hamming-level profile is exactly

`(|A cap L_0|,...,|A cap L_8|) = (0,0,0,6,34,49,28,8,1)`.

The six included weight-three states are

`158, 258, 358, 458, 568, 578`,

where e.g. `158` denotes `{1,5,8}`. The seven omitted weight-five states are

`12345, 12346, 12347, 12367, 12467, 13467, 23467`.

This exposes the candidate as a very small **middle-layer surgery** rather than a mysterious 256-bit truth table: everything below weight three is excluded, everything at weights six through eight is included, and the asymmetry lives entirely in selected states of weights three through five.

That is a stronger structural diagnosis than the previous bare list of 26 minimal sets.

### 3.2 An exact asymmetry ladder

I then interpolated between the overly symmetric `S_5 x S_3` class and the fully asymmetric witness.

Keep coordinates `1,...,5` interchangeable, but treat coordinates `6,7,8` as three distinct control bits. Write

`a = x_1+...+x_5`,

`y = x_6 + 2 x_7 + 4 x_8 in {0,...,7}`.

Consider every monotone family of the form

`A_t = {x : a >= t(y)}`,

where `t:{0,1}^3 -> {0,...,6}` is antitone in the control-bit partial order and `t(000)=6`, the latter forcing omission of the fixed five-set `{1,2,3,4,5}`.

There are exactly **19,704** such monotone threshold maps. I exhaustively enumerated all of them in exact integer arithmetic. The exact H2 optimum in this whole class is

`(psi2_H2,psi2m1_H2,boundary) = (908,652,256)`.

There are six equivalent maximizing maps, coming from permutations of the three control coordinates. One canonical representative, with `y=x_6+2x_7+4x_8`, is

`t = (6,5,4,2,3,3,1,0)`.

The resulting family has exactly 128 states.

Hence deliberate, controlled symmetry breaking gives the rigorous conditional-H2 ladder

`S5 x S3 invariant: 862 / 584`

`S5 + three distinct controls: 908 / 652`

`fully asymmetric current witness: 924 / 670`.

The jump `862 -> 908 -> 924` for `psi2_H2` and `584 -> 652 -> 670` for `psi2m1_H2` quantifies the payoff from breaking symmetry. In particular, the first large gain comes from distinguishing only three control coordinates; the final gain requires breaking the remaining `S_5` symmetry too.

## 4. B24 — FIND THE EXTREMAL OBJECT

Within the fully enumerated 19,704-member `S_5`-core / three-control class, the object above is not merely a candidate: it is the **exact extremizer of that class** for the lexicographic pair `(psi2_H2,psi2m1_H2)`, with the primary optimum `psi2_H2=908`. Its six maximizers are precisely related by permuting the three controls.

This gives a concrete extremal template:

- one five-coordinate bulk statistic `a`;
- three distinguished control bits;
- a monotone eight-entry threshold table;
- omission of the fixed five-set built in exactly.

The template is much smaller than the arbitrary monotone-family search but already captures most of the H2 gain of the fully asymmetric 26-minimal-set family: `908/924 ~= 98.27%` of its `psi2_H2` score and `652/670 ~= 97.31%` of its `psi2m1_H2` score.

This is the candidate class I would test first against Cerf's real formulas once (51.1)-(52.1) are recovered. If the source functional preserves the same ordering, it suggests a tractable symbolic family rather than a raw MILP witness.

Again: this is an extremal statement **only for the conditional H2 search class**, not for Cerf's source functionals and not for all increasing subsets of the cube.

## 5. B10 — DERANDOMIZE

I also extracted an even more compact deterministic witness requiring no 8-entry lookup table. Define the weighted monotone threshold family

`A_w = {x in {0,1}^8 : 3(x_1+...+x_5) + 5(x_6+x_7) + 7 x_8 >= 18}`.

Because the fixed five-set has weight `15<18`, this family is upper-outside. It has 107 states and exact conditional-H2 score

`(psi2_H2,psi2m1_H2,boundary) = (902,644,258)`.

So a single integer linear threshold already captures almost all the gain of the exact control-table extremizer:

`862/584  <  902/644  <  908/652  <  924/670`.

This is a useful derandomization: instead of carrying a 26-minimal-set object discovered by search, we now have a six-number source-test witness `(3,5,7,18)` together with the fivefold/twofold multiplicities. It can be evaluated by hand or in a few lines against any recovered source-equivalent definition of second-order pivotality.

The fact that the exact 19,704-family extremizer still beats every witness in this simple weighted form found here also localizes what a proof/counterexample search must exploit: **nonlinear interaction among the three control bits**, not merely unequal coordinate weights.

## 6. Exact self-check and what it certifies

I wrote and executed

- `artifacts/R09/20260917T0929Z_g0002_h2_asymmetry_derandomization.py`
- `artifacts/R09/20260917T0929Z_g0002_h2_asymmetry_derandomization.out`.

The archived output begins `SELF_CHECK_ONLY_H2_NOT_SOURCE_VERIFIED`, recomputes the old `S_5 x S_3` benchmark rather than taking it on faith, verifies all 19,704 control-threshold maps, verifies the weighted family, verifies the full candidate's level profile, and exhaustively verifies that its coordinate automorphism group has size one. It ends `PASS` and explicitly prints `ALL_CLAIMS_CONDITIONAL_ON_H2_NOT_CERF_SOURCE_FUNCTIONALS`.

Creation/readback commits:

- checker: `b281b34ebe9080528f7012e45b1702e58e6a2d9e`;
- output: `1d72d218840ed33c25e6fb63b1d43d48d1cf126a`.

This is exactly the intended 10-percent bookkeeping: the code certifies a substantive new structural route; it does not pretend to move the frozen source metric.

## 7. What moved, and why `Delta_8` did not

The source metric did not move:

`Delta_8 = UNMEASURED -> UNMEASURED`.

That is deliberate. The missing source normalization remains the only honest reason not to plug these witnesses into Cerf's functional.

Substantive route movement this run is:

1. the strongest current H2 outside witness is proved to have trivial coordinate automorphism group;
2. its middle-layer surgery is isolated exactly (`6` selected weight-3 states, `7` omitted weight-5 states);
3. a complete 19,704-family symmetry-breaking class is solved exactly, with optimum `(908,652,256)`;
4. a very small deterministic weighted witness `(3,3,3,3,3,5,5,7; threshold 18)` achieves `(902,644,258)`;
5. the asymmetry payoff is now quantified rather than merely observed.

These results say where to look when the actual formula is available. They do **not** refute Conjecture 53.1.

## 8. Next route

The source formula remains the highest-value missing input. If it becomes accessible, evaluate in this order:

1. the Hamming-threshold normalization benchmarks from the prior report;
2. the compact weighted witness `3,3,3,3,3,5,5,7 / 18`;
3. the exact `S_5`-core control-table extremizer `t=(6,5,4,2,3,3,1,0)`;
4. the fully asymmetric 26-minimal-set witness.

That sequence will identify immediately whether H2 is right, close but directionally normalized differently, or categorically wrong.

If source access is still blocked next run, do **not** repeat B15/B24/B10. A genuinely different next triple is **B6 DEFORM TO A POINT YOU CAN SOLVE, B12 FIND WHAT IS CONSERVED, B26 HUNT THE SPORADIC CASE**: interpolate between the compact weighted family and the control-table extremizer, look for an invariant of local section neighborhoods under monotone bit-splitting, and isolate the smallest sporadic control pattern responsible for the `902 -> 908 -> 924` gains. Any claim remains conditional until the source definition is recovered.

## 9. Model / scheduler-control status

The limitation remains unchanged in the task interface available to this runtime: the controls exposed to the automation tool are title, prompt, schedule, enabled state and timing mode. There is **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. GPT-6/maximum is therefore prompt-only here.

The current root ledger adds an important authorization-context detail: P26's full update eventually succeeded in one authorized context, while a different context denied edits to all R-series IDs and some other tasks. Thus a historical `You cannot modify this task` response is not repaired by changing repository text; it is an ownership/context boundary. The lawful workaround is the task-owning authorized workspace/account, an ownership/admin transfer if the product supports it, or platform support. Actually enforcing GPT-6/maximum additionally requires the product/API to expose model and reasoning controls **and** runtime telemetry confirming what executed.

No scheduler modification was attempted.

## 10. Prohibited-action audit

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, force-push, shared-root edit, peer-file edit, or paid compute was performed.

## 11. Structured ledger_delta

```yaml
ledger_delta:
  track: R09
  run_id: 20260917T0929Z_g0002_asymmetry_derandomization_c4b71e
  predecessor:
    source: "Tang arXiv:2012.01135, source-PDF Question 4.11"
    metric: "greatest rigorous lower bound for theta'' at a certified admissible parameter in the fixed periodic-tree family"
    before: UNBOUNDED_ABOVE
    after: UNBOUNDED_ABOVE
    unchanged_count: 6
    state: RETIRED_FROZEN
  active:
    id: G0002
    source: "Raphael Cerf, arXiv:2608.23661v1, Conjecture 53.1"
    metric: Delta_8
    before: UNMEASURED
    after: UNMEASURED
    stagnation_count: UNKNOWN
    status: CLAIMED_ACTIVE_CLOSABLE
    source_normalization: NOT_YET_RECOVERED
    source_text_path_recorded_by_intake: "Downloads/.../sources/cerf_theta_pc_2026/text.txt"
    source_text_in_repository: NOT_FOUND
    conditional_H2:
      status: NOT_SOURCE_VERIFIED
      selfcheck: PASS
      fully_asymmetric_upper_out:
        score: [924, 670, 254]
        family_size: 126
        coordinate_automorphism_group_size: 1
        level_profile: [0,0,0,6,34,49,28,8,1]
      s5_control_class:
        exact_family_count: 19704
        best_score: [908,652,256]
        number_equivalent_best_maps: 6
        canonical_threshold_map: [6,5,4,2,3,3,1,0]
        family_size: 128
      weighted_threshold_witness:
        weights: [3,3,3,3,3,5,5,7]
        threshold: 18
        score: [902,644,258]
        family_size: 107
      previous_s5xs3_benchmark:
        exact_family_count: 84
        best_score: [862,584,278]
      asymmetry_chain_psi2: "862 < 902 < 908 < 924"
      asymmetry_chain_psi2m1: "584 < 644 < 652 < 670"
      warning: "All values in this block are conditional H2 search quantities, not Cerf source phi-values."
  methods_this_run: [15,24,10]
  next_methods: [6,12,26]
  new_source_level_conjecture_verdict: NONE
  overall: ACTIVE_G0002_NO_SOURCE_METRIC_MOVEMENT_ASYMMETRY_ROUTE_SHARPENED
```
