Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum. NO SOURCE-METRIC MOVEMENT: `W_sigma = 0.083457166870867772411698563411662... -> 0.083457166870867772411698563411662...`; C0021 unchanged-run streak `3 -> 4`. Methods actually tried: B2, B15, B30.**

# P13 Outside Counterexample Research — C0021 negation recovery via oriented shortest paths

UTC report time: 2026-09-18T22:17:43Z  
Own root: `proofnet24/P13-outside-successor/`  
Canonical claim: `operations/claims/C0021.md`  
Native slot named in claim: `6aa7b253b37c8191b693d8dc79298d37`  
Status after this run: **CLAIMED / CURRENT-OPEN-LOOKING / PARTIAL / STUCK1-RECOVERY1-EXHAUSTED**.  
Closure is **not** claimed.

## 1. Continuity, ownership, exclusions, and source status

The current create-only claim still assigns C0021, the revealment exponent of iterated 3-majority, to this P13 slot and freezes the source-faithful metric as the width of one rigorous interval for the single exponent `sigma`. The retired I0051 clade-covariance target was not reopened.

The first-successor lead I0054 was checked before research and remains explicitly reserved to R11 in `operations/claims/I0054.md`. The newest R11 report recovered before this run is `runs/R11/2026-09-18T21-40-00Z_i0054-dyadic-wiener-u032-c053-6f3c.md`. P13 did not touch that claim or any R11 artifact.

The campaign `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, current claims, prior C0021 material, and targeted intake/attempt hits were checked. Root `RESULTS.md` still contains an older P13/I0051 configuration snapshot, but its own header says newer complete reports and claims control; the later create-only C0021 claim and immutable P13 reports therefore control this run. No shared root ledger was overwritten.

The inherited rigorous source interval is

`0.178402340272047101787355665273859... <= sigma <= 0.261859507142914874199054228685522...`,

so

`W_sigma = 0.083457166870867772411698563411662...`.

No theorem below changes either endpoint.

### Fresh source check, 18 September 2026 UTC

Controlling source: Christophe Garban and Jeffrey E. Steif, *Noise Sensitivity of Boolean Functions and Percolation*, author-hosted almost-final book PDF:

`https://math.univ-lyon1.fr/~garban/Fichiers/book.pdf`

This run recovered the text layer at Chapter XIII, page 187 of the book / PDF page index 188, and the page image itself successfully rendered. The page visibly states Open Problem XIII.1: find the randomized algorithm with smallest revealment for iterated majority on `n=3^k` bits and says that even the order of magnitude of the decay, i.e. the exponent, is not known although bounds are known. This corrects the preceding run's transient screenshot cache failure; it is source verification, not proof of current worldwide openness.

Dated bounded queries run this time included:

- `"iterated 3-majority" revealment exponent Garban Steif`
- `"recursive majority" expected deterministic decision tree uniform`
- `"iterated majority" revealment 2025 2026`
- `"level-p complexity" iterated majority Jansson Jansson`
- `"recursive majority" Brownian Jacka Warren Windridge`

The search again recovered Jansson--Jansson (JFP 2023), whose exact computation is for **two-level** iterated majority; Magniez--Nayak--Santha--Sherman--Tardos--Xiao, whose randomized-decision-tree problem uses the standard worst-case/randomized-complexity model rather than this iid-uniform expected-cost constant; and Jacka--Warren--Windridge's continuous diffusion-control analogue. No checked primary source in the bounded search determines the exact C0021 exponent. That is bounded negative evidence only, not a global openness or novelty certificate.

## 2. Recovery obligation carried from STUCK1

The previous run reached the third consecutive unchanged source metric and selected exactly one recovery: **ATTACK THE NEGATION** of the surviving all-height candidate

`P_h(s) >= (3/4) |m_h(s)|^(3/2)`,                                      (H)

where

`P_h(s) = (D_h - V_h(s) + A_h(s))/D_h`.

The previous complete enumeration established (H) for every canonical state through height 3 and identified its height-3 worst state. The present run therefore began by recursively lifting that exact sign-oriented witness and trying to make (H) fail at the first new scale, rather than trying to prove (H).

For clarity retain the notation

- `V_h(s)`: optimal iid-uniform expected remaining query cost from child state `s`;
- `D_h=V_h(o_h)` at the untouched state;
- `r_h(s,a)=1+(V_h(s^+)+V_h(s^-))/2-V_h(s)` for Bellman regret;
- `A_h(s)`: minimum accumulated Bellman regret over legal paths from `o_h` to `s`;
- `W_h(s)=V_h(s)-A_h(s)`;
- `q_h(s)=P(Y_h=+1|s)`, `m_h(s)=2q_h(s)-1`;
- `C_h(s)=D_h-W_h(s)=D_h-V_h(s)+A_h(s)`.

Then (H) is equivalently

`C_h(s) >= (3/4) D_h |m_h(s)|^(3/2)`.

## 3. B2 — attack the negation with the recursively lifted extremal witness

### Idea before code

The complete height-3 search found the minimum coefficient of `P/|m|^(3/2)` at the sign-oriented state

`S_3 = ( (-,U,U), (b,b,b), (b,b,U) )`,

where `U=(u,u,u)` and `b=(-,u,u)`, with canonical reordering understood. Its exact data are

`q(S_3)=31/256`, `|m(S_3)|=97/128`,

`V_3(S_3)=547983/65536`,

`A_3(S_3)=170249/131072`,

`W_3(S_3)=925717/131072`,

`C_3(S_3)=8390315/1048576`.

Define a lift `L` that leaves terminal `+/-` nodes fixed and replaces every unresolved macro-leaf `u` by an untouched `MAJ_3` block `(u,u,u)`, recursively through the state. Put

`S_h=L^(h-3) S_3`,  `h>=3`.

This is the most literal recursively sign-oriented family suggested by the exact minimizer.

### Proposition 3.1 — the dangerous magnetization does not dilute under lifting

For every `h>=3`,

`q_h(S_h)=31/256`, hence `|m_h(S_h)|=97/128`.

#### Proof

A terminal sign remains a deterministic sign under the lift. Every unresolved leaf `u` is replaced by an untouched recursive-majority block, whose output is unbiased by global sign symmetry, hence has posterior `1/2`, exactly the posterior of `u`. The posterior of every nonterminal majority node is the polynomial

`M(a,b,c)=ab+ac+bc-2abc`

in its three independent child posteriors. Replacing each unresolved leaf by a new unbiased block therefore leaves the posterior at every ancestor unchanged, by induction from the leaves to the root. Applying this to `S_3` gives the claim. QED.

The exact checker instantiated this lift through heights 3,4,5,6 and obtained `q=31/256` every time.

### What the negation attack did and did not achieve

This family is a genuine fixed-magnetization stress test: the right-hand side of (H), after normalization by `D_h`, stays at the same positive threshold for every lift. It therefore cannot escape (H) merely because the posterior tends to zero.

However, a naive exact Bellman recursion for the first unrestricted lifted state `S_4` has unresolved rank 57 and exceeded the available 60-second exact-computation window without returning `V_4(S_4)`. No value from that interrupted computation is used anywhere in this report. Therefore B2 **did not produce an exact counterexample** to (H), and no height-4 truth claim about unrestricted `C_4(S_4)` is made.

## 4. B15 — break symmetry: the missing orientation coordinate is an exact shortest-path cost

B20 in the preceding run showed empirically that `(q,W)` forgets which posterior direction carries which continuation value. B15 turns that observation into an exact theorem.

### Theorem 4.1 — oriented-path representation of progress

Fix a height `h`. Consider any legal path

`s_0=o_h -> s_1 -> ... -> s_k=s`.

At step `j`, a query at `s_{j-1}` has two successors: the actually chosen successor `s_j` and the sibling successor `t_j` corresponding to the opposite observed bit. Define the **oriented edge cost**

`c_j = 1 + (V_h(t_j)-V_h(s_j))/2`.

Then along that path,

`D_h - V_h(s) + sum_{j=1}^k r_j = sum_{j=1}^k c_j`,                  (4.1)

where `r_j` is the Bellman regret of the queried action at `s_{j-1}`. Consequently

`boxed: C_h(s) = min_{legal paths o_h -> s} sum c_j`.              (4.2)

Thus the candidate Hölder barrier (H) is exactly a lower bound on an **oriented shortest-path metric**, not on posterior alone.

#### Proof

For one edge, the Bellman-regret definition gives

`r_j = 1 + (V_h(s_j)+V_h(t_j))/2 - V_h(s_{j-1})`.

Rearranging,

`V_h(s_{j-1})-V_h(s_j)+r_j
 = 1 + (V_h(t_j)-V_h(s_j))/2
 = c_j`.

Summing over `j=1,...,k` telescopes the value differences:

`sum_j (V_h(s_{j-1})-V_h(s_j)) = V_h(o_h)-V_h(s)=D_h-V_h(s)`.

This proves (4.1). The term `D_h-V_h(s)` is path-independent, while by definition `A_h(s)` is the minimum of `sum_j r_j` over all legal paths from `o_h` to `s`. Minimizing (4.1) therefore yields

`min_path sum c_j = D_h-V_h(s)+A_h(s)=C_h(s)`.

QED.

### Exact exhaustive self-check

The artifact independently computes shortest oriented-path costs and minimum Bellman-regret costs and verifies (4.2) on **every reachable canonical child state** through height 3:

- height 1: 6 states;
- height 2: 46 states;
- height 3: 17,206 states.

For `S_3` it reproduces

`P_3=C_3/D_3=8390315/15796051`

and

`P_3^2/|m_3|^3
 = 147634018423616307200 / 227725810949378078473`,

whose square-root coefficient is approximately `0.8051690855`, still above `3/4`.

This theorem is movement in structural understanding, but not source-metric movement. It makes precise what the missing orientation variable must measure: the signed difference between the value of the unobserved sibling branch and the value of the observed branch.

## 5. B30 — one scale and one direction: forced-block lifting is exactly scale-neutral

The B2 family still leaves one ambiguity: is simple recursive scaling itself capable of driving the `0.805169...` coefficient below `3/4`, or must a counterexample exploit interleaving between the newly inserted blocks?

To separate those mechanisms, impose a **forced-block-completion restriction** after one lift: whenever the macro-policy chooses one newly inserted height-1 block, it must finish determining that block before it may query a different block. Each macro-leaf determination then has the same expected cost `D_1=5/2`.

### Theorem 5.1 — block-completion scaling

For any fixed macro partial state `s`, if each unresolved macro-leaf is replaced by an independent block that costs a constant expected amount `b` to determine and switching between blocks is forbidden until the chosen block is complete, then the macro Bellman quantities scale as

`V^(b)(s)=b V(s)`,

`A^(b)(s)=b A(s)`,

`W^(b)(s)=b W(s)`,

`C^(b)(s)=b C(s)`.

In particular the normalized progress `P=C/D` is invariant under such a block lift.

#### Proof

Under forced completion, one macro query has deterministic expected cost `b` and reveals exactly one unbiased macro bit. The macro transition graph and the two equiprobable successor states are therefore identical to the unit-cost Bellman problem, with every one-step cost multiplied by `b`. Backward induction on unresolved macro rank gives `V^(b)=bV`.

For any macro action, its Bellman regret is

`b + (bV(s^+)+bV(s^-))/2 - bV(s) = b r(s,a)`.

Hence every path regret sum scales by `b`, and taking the minimum gives `A^(b)=bA`. The formulas for `W=V-A` and `C=D-W` follow immediately. Since the untouched value `D` also scales by `b`, `P=C/D` is unchanged. QED.

### Exact first-lift benchmark

For `S_3` and one height-1 block lift, `b=D_1=5/2`, so

`C_4^block = (5/2) C_3 = 41951575/2097152
             = 20.004069805145264...`,

`D_4^block = (5/2) D_3 = 78980255/2097152
             = 37.660720348358154...`,

and

`P_4^block=P_3=8390315/15796051`.

Thus **pure recursive scaling does not move this family toward a counterexample at all** in the forced-block model. The only structural difference between this surrogate and the real height-4 problem is the option to interleave queries across blocks.

For the fixed magnetization `|m|=97/128`, write

`theta=(3/4)|m|^(3/2)`, so exactly

`theta^2 = 8214057/33554432`,

and numerically `theta=0.4947706284986058...`.

The inherited rigorous height-4 cost interval is

`545085503/15728640 <= D_4 <= 1332467382289843607/36028797018963968`,

i.e. approximately

`34.6556029638 <= D_4 <= 36.9833991845`.

Therefore the absolute Hölder threshold `theta D_4` lies between approximately `17.1465744594` and `18.2982996585`. The block benchmark `C_4^block≈20.0040698051` stays above even the harder upper-end threshold. The checker verifies this with no square roots via the exact strict inequality

`(C_4^block)^2 - theta^2 U_4^2
 = 2845742272172431865507464677849501547278407
   /43556142965880123323311949751266331066368
 > 0`.

The numerical gap from the block benchmark to `theta U_4` is about `1.7057701466`. This is a **surrogate separation**, not a comparison theorem for unrestricted `C_4`: no monotonic relation between the block-model `C` and unrestricted `C` is asserted. What is proved is that any failure of (H) in this lifted family must use a mechanism absent from forced block completion — precisely the inter-block option value that earlier depth-4 policy improvements already exposed.

B30 therefore succeeds as a localization of the obstruction, but it does not prove or disprove (H) for `S_4`.

## 6. Exact checker and execution record

Executed exact-arithmetic self-check:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_b2_b15_b30_2026-09-18T22-17-43Z_check.py`

Local SHA-256 before upload:

`a44402886babd9e00627279b486fb186b63b7c3bd95772ad84e957904aa301aa`

GitHub creation commit:

`956672a6c80a5a7d64d354261d7884f3841cc299`

Read-back Git blob at that exact commit:

`700a12e25333038b9faf3d108bfd227e20b102f7`

Archived output:

`proofnet24/P13-outside-successor/artifacts/2026-09-18/c0021_b2_b15_b30_2026-09-18T22-17-43Z_check.out`

Local SHA-256 before upload:

`49c1c72b7a6e250e599ac5c4d8cfa2300c9072ca736ab95695860299c5abaa6d`

GitHub creation commit:

`a1663a74c976cfb7eeed83dd818bd41b7728e2ad`

Read-back Git blob at that exact commit:

`b3037734861f30741c583ad19b9d563bff257635`

The output ends

`ALL_EXACT_B2_B15_B30_CHECKS_PASS`.

This is a **P13 self-check**, not an independent audit.

## 7. Stuck/recovery report after the failed negation attack

The source metric is unchanged for a fourth consecutive run, and the same asymptotic obstruction remains, so the five-part stuck analysis is refreshed rather than hidden.

### (a) Exact blocking formula

The lower-bound route remains blocked at

`D_{h+1} >= (3-beta_h)D_h`,

where source movement requires a height-uniform theorem

`sup_h beta_h < 3/4`.

The specific surviving sufficient route is the all-height inequality

`C_h(s) >= (3/4)D_h |m_h(s)|^(3/2)`.

By Theorem 4.1, this is now exactly an oriented-shortest-path lower bound.

### (b) Routes tried in this recovery and precise failures

1. **B2 / attack the negation:** the recursively lifted exact height-3 extremizer keeps the dangerous magnetization `97/128` at every height, so it is a serious candidate. But the first unrestricted height-4 Bellman computation did not finish within the available exact-computation window; no counterexample was certified.
2. **B15 / break symmetry:** the missing orientation coordinate was isolated exactly as `1+(V(sibling)-V(chosen))/2` and gives a full shortest-path representation. This identifies the right object but supplies no all-height lower bound on its path sum.
3. **B30 / one scale, one direction:** forced block completion is exactly scale-neutral and stays strictly on the safe side at the lifted height-4 benchmark. Hence simple recursive scaling is not the counterexample mechanism; unrestricted inter-block option value is the remaining issue.

### (c) Missing ingredient

A proof must control how much **unrestricted inter-block switching can reduce the oriented shortest-path progress** relative to the forced-block macro problem, while retaining the sign of the branch-value skew. No previous scalar posterior, `(q,V)`, `(q,W)`, concave-envelope, or coarse quotient contains this orientation-sensitive gluing information.

### (d) Simplest unproved case

The simplest unproved case is now one single explicit state, not all height-4 states:

`S_4=L(S_3)`.

Decide exactly whether

`16 C_4(S_4)^2 >= 9 D_4^2 (97/128)^3`.                         (S4)

A counterexample to (S4) kills the Hölder route. A proof of (S4) does not prove the all-height theorem, but it decides the first scale that complete enumeration could not reach and directly tests the only mechanism absent from the block surrogate.

### (e) Nearest solved analogue

The nearest exact analogue is the forced-block theorem above together with complete unrestricted enumeration through height 3. The closest literature analogue is Jansson--Jansson's exact two-level level-`p` optimization, which uses finite-state thinning/memoization; it does not address the height-uniform oriented-path bound or arbitrary interleaving at this scale.

### Exactly one next recovery selected

**Recovery selected: SOLVE THE SIMPLEST UNPROVED CASE (S4).**

The next run should not return to a global proof of (H). It should decide the single lifted state `S_4` by a finite orientation-aware reduction. The planned nonrepeating method triple is **B6, B18, B24**: deform from forced-block completion by an exact bounded-switch parameter, rewrite the oriented shortest-path problem in the smallest state language that retains branch skew, and identify the extremal interleaving pattern for this one state. If this does not move the source metric, the unchanged-run streak becomes five; rotation still occurs only at six unchanged runs for this closable target.

## 8. Source metric verdict

Before:

`W_sigma = 0.083457166870867772411698563411662...`

After:

`W_sigma = 0.083457166870867772411698563411662...`

**NO SOURCE-METRIC MOVEMENT.**

The oriented-shortest-path theorem and block-lift separation are substantive, source-relevant structural progress, but neither changes a rigorous endpoint for `sigma`. C0021 therefore remains **PARTIAL**.

## 9. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: P13
  native_slot: 6aa7b253b37c8191b693d8dc79298d37
  canonical_claim: C0021
  own_root: proofnet24/P13-outside-successor
  classification: CLOSABLE_OUTSIDE
  status: CLAIMED_CURRENT_OPEN_LOOKING_PARTIAL_STUCK1_RECOVERY1_EXHAUSTED
  source_metric:
    name: rigorous_interval_width_for_single_sigma
    before: 0.083457166870867772411698563411662...
    after: 0.083457166870867772411698563411662...
    movement: false
  unchanged_run_streak:
    before: 3
    after: 4
  methods_tried: [B2, B15, B30]
  recovery_executed: attack_negation
  mathematical_additions:
    - exact oriented-shortest-path representation C_h(s)=min_path sum[1+(V_sibling-V_chosen)/2]
    - exhaustive exact verification of that identity on all 6,46,17206 states at heights 1,2,3
    - recursively lifted extremal family S_h with invariant q=31/256 and |m|=97/128
    - forced-block-completion scaling theorem preserving normalized progress P
    - exact height-4 block benchmark remains strictly above the Hölder threshold even at rigorous U4
  finite_counterexample_found: false
  failed_exact_computation:
    target: unrestricted_V4_of_S4
    outcome: exceeded_available_60_second_exact_window_no_value_used
  next_recovery_selected_exactly_one: solve_simplest_unproved_case_S4
  next_methods: [B6, B18, B24]
  rotation: false
  closure_claimed: false
  independent_audit_claimed: false
  self_check_only: true
  peer_claims_touched: false
  retired_i0051_reopened: false
```
