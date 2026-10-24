Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `W_sigma = 0.083457166870867772411698563411662... -> 0.083457166870867772411698563411662...`; C0021 unchanged-run streak `4 -> 5`. Methods actually tried: B6, B18, B24.**

# P13 Outside Counterexample Research — C0021 recovery 2: interleaving width of the first unresolved height-4 witness

UTC report time: 2026-09-18T23:50:42Z  
Own root: `proofnet24/P13-outside-successor/`  
Canonical claim: `operations/claims/C0021.md`  
Native slot named in claim: `6aa7b253b37c8191b693d8dc79298d37`  
Status after this run: **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / STUCK1-RECOVERY2**.  
Closure is **not** claimed.

## 1. Continuity, ownership, exclusions, and source status

The create-only C0021 claim still assigns the revealment exponent of iterated 3-majority to this P13 slot and freezes the mathematical metric as the width of one rigorous interval for the single source exponent `sigma`. I did not reopen retired I0051, handed-off P0082, or six-run-handed-off D0093.

The first-successor lead I0054 was checked before research and remains owned by R11 in `operations/claims/I0054.md`. The newest recovered R11 report is `runs/R11/2026-09-18T22-40-00Z_i0054-prime-cut-u033-c054-8f21.md`; it continued I0054 and moved that track's own metric `53 -> 54`. P13 did not touch the claim or any R11 artifact.

I reread/recovered the controlling owner directive, `operations/NEW_METHODS_2026-09-16.md`, campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`, current claims, the newest P13 report, and the relevant C0021 artifacts. `RESULTS.md` still contains an older P13/I0051 configuration row but explicitly instructs workers to recover newer reports and claims; the later create-only C0021 claim and immutable P13 reports therefore control. No shared root ledger was edited.

The inherited rigorous source interval remains

`0.178402340272047101787355665273859... <= sigma <= 0.261859507142914874199054228685522...`,

hence

`W_sigma = 0.083457166870867772411698563411662...`.

Nothing below changes either endpoint.

### Fresh source/literature check, 18 September 2026 UTC

The author-hosted Garban--Steif book PDF was recovered again. Its Chapter XIII, Open Problem XIII.1, asks for the randomized algorithm with smallest revealment for iterated majority on `n=3^k` bits and explicitly says that even the exponent of the decay is not known. The text layer was accessible. The required screenshot attempt on the relevant PDF failed in this run with a cache miss, and that failure is recorded rather than represented as visual verification.

Fresh bounded searches included the exact iterated-majority revealment wording, Jansson--Jansson level-`p` complexity, and recursive-majority randomized decision-tree complexity. They again recovered Julia Jansson and Patrik Jansson, *Level-p-complexity of Boolean functions using thinning, memoization, and polynomials* (JFP, published online 12 December 2023), whose advertised application is **two-level** iterated majority, and Magniez--Nayak--Santha--Sherman--Tardos--Xiao, whose published recursive-majority work is the different worst-case randomized-decision-tree model. The latter is structurally relevant because its upper-bound algorithm also uses interleaving, but it does not determine the iid-uniform expected-cost exponent C0021 asks for. No checked source-matching determination appeared in the bounded search. This is bounded negative evidence only, not a worldwide-openness or novelty certificate.

## 2. Recovery target carried into this run

The preceding run exhausted the first STUCK1 recovery and selected exactly one second recovery: **SOLVE THE SIMPLEST CASE**. The simplest unresolved state is the lifted height-4 state

`S4 = L(S3)`,

where `L` replaces every unresolved macro-leaf of the exact height-3 extremizer by an untouched bottom `MAJ_3` block. The lift preserves

`q(S4)=31/256`,  `|m(S4)|=97/128`.

The surviving all-height candidate is

`C_h(s) >= (3/4) D_h |m_h(s)|^(3/2)`,                         (H)

where

`C_h(s)=D_h-V_h(s)+A_h(s)`

and `A_h` is minimum accumulated Bellman regret. The preceding run proved that `C_h` is an oriented shortest-path cost and that forced block completion preserves normalized progress, but an unrestricted exact Bellman computation of `V_4(S4)` was too large for that route.

This run does not settle (H) at `S4`. It does, however, identify and exactly quantify the first genuinely unavoidable source of difficulty: **at least three bottom blocks must be simultaneously partially exposed by any optimal unrestricted policy at this state**.

## 3. B18 — say it in another language: the six-state bottom-block automaton

Let an untouched bottom majority gate be

`U=(u,u,u)`.

Modulo child permutation and immediate majority collapse, every nonterminal partial bottom gate reached from `U` is one of

`U=(u,u,u)`,
`P=(+,u,u)`,
`M=(-,u,u)`,
`X=(+,-,u)`.

Together with terminal outputs `+,-`, this is a six-symbol alphabet. Its complete transition graph under one legal leaf query is

`U -> P or M`,
`P -> + or X`,
`M -> X or -`,
`X -> + or -`.

### Proposition 3.1 — exact orientation-preserving language

Every descendant of `S4` under leaf queries has a unique canonical description obtained by labeling each surviving bottom block by one of `U,P,M,X,+,-` and then recursively applying the ordinary majority collapse whenever two children of a higher gate are equal terminal signs. Conversely every state produced by the six-symbol transitions and recursive majority collapse is a genuine descendant under legal leaf queries.

#### Proof

A bottom `MAJ_3` gate begins at `U`. One query produces one observed sign and two unresolved leaves, hence `P` or `M`. From `P`, a second query either produces the second `+` and determines the gate or produces `X`; the sign-reversed statement holds for `M`. From `X`, the final unresolved bit determines the gate. These are all possibilities because no other number or pattern of observed leaves can occur in a three-leaf gate before its output is determined.

A query anywhere in the lifted formula changes exactly one bottom symbol according to this transition graph. All higher effects are deterministic applications of `MAJ_3`: once two child roots agree, the parent is terminal and the unused third child is irrelevant and is canonically discarded. Induction on the number of queried leaves proves the forward statement. Reversing the same one-symbol transitions realizes every generated state by a legal query sequence, proving the converse. QED.

This language keeps the sign orientation `P` versus `M` and the disagreement state `X`; those are precisely the features lost by the posterior-only and `(q,W)` quotients that failed in earlier runs.

## 4. B6 — deform to a solvable point: cap the interleaving width

Call a bottom block **active** if its symbol is `P`, `M`, or `X`: it has been entered but not yet determined. For a state `s`, let `a(s)` be the number of active bottom blocks. For a zero-error policy `pi`, define its interleaving width

`I(pi) = max a(s)`

over states reachable with positive probability from `S4` under `pi`.

For `K>=1`, let `V^(K)(s)` be the minimum expected remaining query cost among policies that never exceed interleaving width `K`.

### Theorem 4.1 — exact capped Bellman recursion

On the six-symbol state graph,

`V^(K)(s) = 0` for terminal `s`, and otherwise

`V^(K)(s) = min_a { 1 + (V^(K)(s_a^+)+V^(K)(s_a^-))/2 }`,           (4.1)

where the minimum is over legal leaf queries `a` for which both successor states satisfy `a(s_a^+)<=K` and `a(s_a^-)<=K`.

Equation (4.1) is exactly the optimum over all zero-error policies of width at most `K`; it is not a heuristic restriction.

#### Proof

The state graph is acyclic under the number of still-relevant unresolved leaves. If a policy has width at most `K`, every action used at a reachable state must have both successors within the cap, because either fair-bit outcome has positive probability. Conversely, if every chosen action has both successors within the cap, induction from the initial state shows the whole policy remains within the cap. Conditioning on the next queried fair bit therefore gives (4.1), and backward induction on the acyclic state graph proves optimality. QED.

For `K=1`, entering a second untouched bottom block while another is active is forbidden. Hence once a bottom block is entered it must be determined before another block is entered. Thus width one is exactly the forced-block-completion model of the preceding run. Since one bottom `MAJ_3` costs `D_1=5/2` in expectation,

`V^(1)(S4) = (5/2) V_3(S3)
            = 2739915/131072
            = 20.90389251708984375.`

The exact width-two dynamic program gives

`V^(2)(S4) = 1377453593/67108864
            = 20.52565802633762359619140625.`

Therefore allowing a second simultaneously active block has exact option value

`V^(1)(S4)-V^(2)(S4)
 = 25382887/67108864
 = 0.37823449075222015380859375.`

The checker evaluates 53,157 memoized capped states for `K=1` and 410,001 for `K=2`, using integer expectations scaled by `2^81`; every halving is asserted exact. This is an executed finite exact-arithmetic result, not floating-point enumeration.

## 5. B24 — find the extremal object: interleaving width at least three is unavoidable

To test whether width two already captures unrestricted optimal behavior, I constructed a completely specified unrestricted zero-error policy `pi_*`. At each top-level state it chooses a leaf query that is optimal within the selected height-3 child and minimizes an exact whole-child lottery continuation value; ties are resolved by the checker's canonical integer-state order. This policy is explicit and deterministic once the state is fixed.

Its exact expected remaining cost from `S4` is

`E_{pi_*}(S4)
 = 10885886259/536870912
 = 20.27654323540627956390380859375.`

Hence

`V^(2)(S4) - E_{pi_*}(S4)
 = 133742485/536870912
 = 0.24911479093134403228759765625 > 0.`

### Theorem 5.1 — every unrestricted optimum has width at least three

No optimal unrestricted zero-error policy from `S4` can have interleaving width at most two.

#### Proof

By Theorem 4.1, every width-at-most-two policy has expected cost at least `V^(2)(S4)`. The explicit unrestricted policy `pi_*` has strictly smaller cost. Therefore the unrestricted optimum is at most `E_{pi_*}(S4)<V^(2)(S4)`. If an unrestricted optimal policy had width at most two, its cost would be at least `V^(2)(S4)`, a contradiction. QED.

Thus the first lifted Hölder witness cannot be understood by forced completion or by allowing only one extra open block. At least three simultaneously partial bottom blocks are structurally necessary for optimality.

The same checker gives a second exact description of how strongly `pi_*` uses this resource. The probability that it ever reaches width at least three is

`2054614931/2147483648
 = 0.9567546336911618709564208984375`.

Its reachable policy DAG contains 3,495 canonical states, with active-width histogram

`0:54, 1:290, 2:638, 3:848, 4:752, 5:515, 6:276, 7:95, 8:24, 9:3`.

The maximum reachable width is nine. These figures describe this explicit policy only; they are not claimed as properties of every optimum. The theorem-sized universal conclusion is solely the lower bound `I(pi_opt)>=3` for every unrestricted optimum from `S4`.

## 6. Why this still does not move the source metric

The source-moving lower-bound route requires control of

`C_4(S4)=D_4-V_4(S4)+A_4(S4)`,

not merely an upper bound on `V_4(S4)`. The cap-two computation proves that unrestricted interleaving matters, but it gives neither the exact unrestricted `V_4(S4)` nor the minimum-regret term `A_4(S4)`. The explicit policy gives only

`V_4(S4) <= 10885886259/536870912`.

That is not enough, together with the inherited interval for `D_4`, to prove or refute

`16 C_4(S4)^2 >= 9 D_4^2 (97/128)^3`.

An exact `K=3` capped computation was also attempted. It did not complete within the permitted local execution call, and no partial value or state count from that interrupted computation is used. Thus no finite claim about `V^(3)(S4)` is made.

Accordingly the frozen source interval and `W_sigma` remain unchanged.

## 7. Mandatory stuck/thinking report — same residual obstruction, now sharpened

The exact source-side blocking formula remains

`D_{h+1} >= (3-beta_h) D_h`.                                      (7.1)

A source-metric improvement on the lower-bound side requires a height-uniform theorem

`sup_h beta_h < 3/4`.                                             (7.2)

The strongest surviving candidate would follow from the all-height Hölder barrier (H). If (H) held for every state at every height, the already proved terminal identity `E[R m_J]=-1/2` and Jensen would give a uniform constant strictly below `3/4` and hence improve the upper endpoint of `sigma`.

The routes tried against this obstruction now have precise failure modes. A posterior-uncertainty pointwise bound already fails at height two. A posterior-only concave envelope gives useful finite `rho_h` values but no height-uniform theorem. The exact feasible-residual control DP improves the finite envelope but its raw height-3 outer state space is enormous. A coarse finite quotient is sound but inflates the bound to nearly one because it loses branch orientation. A positive linear progress barrier is impossible by a one-observation scaling family. The `3/2`-Hölder barrier survives exhaustive enumeration through height three, but a one-edge scalar-potential proof already fails. The first negation lift preserves the dangerous magnetization, while forced block completion is scale-neutral and stays safely above the Hölder threshold. The present run now proves that even width-two interleaving is insufficient: every unrestricted optimum at the first lifted state must open at least three bottom blocks simultaneously.

The missing ingredient is therefore no longer merely “handle interleaving.” It is a **width-independent lower bound on oriented shortest-path progress under multi-block option value**, or an exact finite computation strong enough to expose a counterexample. Any successful compact state must preserve the sign-oriented sibling-value information from the preceding B15 theorem; posterior, value, and active-count scalars alone cannot certify the needed inequality.

The simplest unproved case remains the single explicit state `S4=L(S3)` and the exact inequality

`16 C_4(S4)^2 ? >= 9 D_4^2 (97/128)^3`.                           (7.3)

The nearest solved analogue is the width-one forced-block model, where all Bellman quantities scale exactly by `D_1=5/2`; the newly solved next analogue is the exact width-two DP above. The closest external structural analogue is the Magniez et al. worst-case recursive-majority algorithm, which also gains power from interleaving but lives in a different complexity model and cannot be imported as a C0021 bound.

Exactly one next recovery is selected: **REDUCE TO AND EXECUTE A FINITE COMPUTATION**. The next run should use the six-symbol orientation-preserving automaton to compute or certify the `K=3` frontier with branch-and-bound/dual lower certificates, and in the same computation target the oriented quantity needed for (7.3), rather than merely another upper policy. If the frozen source metric is unchanged again, the closable-target streak will reach six and the owner-mandated rotation/handoff rule applies; the metric or target must not be renamed to reset that counter.

## 8. Exact checker, execution, and read-back receipts

Executed exact-arithmetic self-check:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_b6_b18_b24_2026-09-18T23-50-42Z_check.py`

Creation commit: `38732312497a5181da6ed45305ac3b6f872b0f67`.  
Read-back Git blob at that exact commit: `ce9c9f176468089caebdd6cd7c6ca1dbc6538147`.

Archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_b6_b18_b24_2026-09-18T23-50-42Z_check.out`

Creation commit: `8a327cc187392d2f5b69d21be36a8cb988b47602`.  
Read-back Git blob at that exact commit: `6b00f34fa7e47ca8e59dd13db99295494b773709`.

The output ends

`ALL_EXACT_B6_B18_B24_CHECKS_PASS`.

This is a **P13 self-check**, not an independent closure audit.

## 9. Scope and verdict

New proved finite facts this run are: the exact six-symbol bottom-block automaton representation; the exact capped Bellman theorem; the exact values of the width-one and width-two optima at `S4`; and the theorem that every unrestricted optimum at `S4` has interleaving width at least three. These materially sharpen the simplest unresolved finite case but do not determine `C_4(S4)`, do not prove (H), do not improve either rigorous endpoint for `sigma`, and do not close the source problem.

C0021 remains **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / STUCK1-RECOVERY2**, with unchanged-run streak five.

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  own_root: proofnet24/P13-outside-successor
  canonical_target: C0021
  source: "Garban-Steif, Noise Sensitivity of Boolean Functions and Percolation, Open Problem XIII.1 / Exercise VIII.5"
  status_before: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / STUCK1-RECOVERY1-EXHAUSTED"
  status_after: "CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / STUCK1-RECOVERY2"
  metric_name: rigorous sigma interval width W_sigma
  metric_before: "0.083457166870867772411698563411662..."
  metric_after: "0.083457166870867772411698563411662..."
  movement: false
  unchanged_streak_before: 4
  unchanged_streak_after: 5
  methods_used: [6, 18, 24]
  recovery_selected_for_next_run: "REDUCE TO AND EXECUTE A FINITE COMPUTATION"
  simplest_unproved_case: "16*C_4(S4)^2 >= 9*D_4^2*(97/128)^3"
  finite_new_claims:
    - "V_cap1(S4)=2739915/131072"
    - "V_cap2(S4)=1377453593/67108864"
    - "every unrestricted optimal policy at S4 has bottom-block interleaving width at least 3"
  exact_checker: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_b6_b18_b24_2026-09-18T23-50-42Z_check.py"
  exact_checker_commit: 38732312497a5181da6ed45305ac3b6f872b0f67
  exact_output: "proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_b6_b18_b24_2026-09-18T23-50-42Z_check.out"
  exact_output_commit: 8a327cc187392d2f5b69d21be36a8cb988b47602
  closure_claimed: false
  independent_audit_claimed: false
  source_global_openness_claimed: false
  peer_claim_touched: false
```
