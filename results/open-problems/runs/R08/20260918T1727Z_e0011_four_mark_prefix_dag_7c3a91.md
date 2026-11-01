Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b4 -> B_cat >= b5`, where `b5/b4` is an exact factor larger than one with diagnostic `log10` gain `880.3352727773`; unchanged count remains `0`. Methods actually used: B5, B10, B29.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: the 21-mark expander collapses to an exact four-mark all-path certificate

Date: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity, ownership, source, and exclusions

I continued from the newest immutable R08 report

`runs/R08/20260918T1648Z_e0011_weighted_automaton_54c9e7.md`

rather than restarting from the stale native task title.

The predecessor Hasebe--Ueda Problem 3.11 / I0082 remains **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I did not reopen it. The old R08 FPP strict-convexity route likewise remains retired from this slot.

The active exclusive claim remains `operations/claims/E0011.md`: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, for the original two-dimensional catalyst/ZGB process with `r=infinity`, `q/2=1-p`, and no added stirring. At the fixed anchor `p0=1/2`, `q=1`.

Before research I refreshed the controlling repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current owner directive, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest R08 report, the current neighboring R07 and R09 reports, and the exact E0011 intake row in `probability_1000_intake_E_20260908/batches/b02_durrett.json`. The large intake collection is not sensibly renderable row-by-row through the connector, so I do not claim a literal display of every approximately 780 intake rows; the exact active row and its ownership/source trail were recovered. No ownership collision was found.

I also refreshed the literature check on 2026-09-18. The primary source is still available at `https://arxiv.org/abs/0906.2293`. Searches for combinations of `Durrett Problem 5`, `catalyst`, `ZGB`, `no stirring`, and `coexistence` recovered Durrett's source and modified-model/simulation work but no later primary theorem proving the source's original no-stirring coexistence interval. This is **bounded negative evidence only**, not a worldwide novelty certificate.

## 2. Frozen metric entering this run

The active metric is

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` is a complete source-valid finite protected Harris-block certificate at `p0=1/2` and `b(C)` is an exact certified lower bound on its good-block probability.

The previous report proved

\[
B_{\rm cat}\ge b_4.
\]

It is useful to rewrite the same recorded `b4` in stage-factor form. The post-library one-expander factor was

\[
s_{21}=\frac{25}{12}\,301^{-16}602^{-5},
\]

and the full macro had 432 protected arrivals. Hence

\[
 b_4=
 \binom{20}{10}
 \;128\;\frac{35}{486}\;301^{-8}602^{-4}
 \;s_{21}^{20}
 \left(\frac{32}{87}\right)^{432}
 \frac{432^{432}}{432!}.
\tag{2.1}
\]

The outside factor `128=4*4*4*2` is the already-certified four eraser variants, four variants for each of the two planters, and two child-planter orders; `binom(20,10)` is the interleaving of the two ten-expander row chains. Formula (2.1) is algebraically the same `b4` as in the preceding immutable report.

## 3. B5 — vary the mark budget instead of accepting 21 as intrinsic

The previous local expander language inherited a 21-mark word. There was no proof that 21 was remotely close to the shortest useful budget. I therefore introduced the exact protected-arrival budget

\[
m=0,1,2,\ldots
\]

as a parameter and asked for the worst-stable-boundary probability of having the target vacant `2x3` rectangle after **exactly `m` protected arrivals**, while accepting all histories over the same seven local clock labels.

The seven local labels are the ones already frozen in the previous automaton report:

- four specified CO-site clocks, each having embedded protected-arrival probability `1/301`;
- three specified O2-edge clocks, each having embedded protected-arrival probability `1/602`.

All other protected clock labels are sent to a cemetery state for this lower bound. Thus the computation is a genuine subevent of the full Harris process, not a renormalized conditional probability.

The surprise is large: the first uniformly positive budget is not 21 but

\[
\boxed{m_*=4.}
\]

For the same 50,785 stable full boundary environments and the exact 12,201-state projected initial quotient from the previous run, the exact minima satisfy

\[
a_0=a_1=a_2=a_3=0,
\qquad
\boxed{a_4=\frac{19}{32,834,164,804}}>0.
\tag{3.1}
\]

Here `a_m` is the minimum, over every stable initial boundary compatible with the incoming vacant `2x2` square, of the total weighted mass of all accepted `m`-arrival histories whose final state has the `2x3` target rectangle vacant.

The finite checker also evaluates the exact integer numerators through `m=24`; every `m>=4` in that tested range has strictly positive worst-boundary mass. The theorem-sized use in this run needs only (3.1).

Important scope: `m*=4` is the first positive budget for **this frozen seven-label alphabet and this local patch certificate**. I do not claim that four is globally minimal among every conceivable catalyst block or alphabet.

## 4. B10 — exact prefix-DAG dynamic programming over all histories

This is not a finite sample or a search over a hand-picked word library. It exactly sums all `7^m` label prefixes and every instantaneous reaction branch.

Let `S` be the 14-cell projected state space from the preceding run; the two omitted cells `(1,2)` and `(2,1)` are neither read nor written by the seven labels and are not target cells. A projected initial descriptor is retained iff it has at least one stable full completion. There are exactly 12,201 such descriptors.

Let `G` be the set of projected states in which the active `2x3` rectangle is vacant. At `p=1/2`, conditional on a protected arrival, a specified CO-site label has probability

\[
\frac1{301}=\frac2{602},
\]

and a specified O2-edge label has probability `1/602`.

For a CO arrival, the reaction-race denominator is at most four; for an O2 arrival the two endpoint choice counts are each at most three. Hence

\[
H=602\cdot36=21,672
\]

is a common exact denominator for every one-step weighted transition. Write `w(s,l,t)` for the corresponding nonnegative integer numerator for transition `s -> t` under one of the seven labels `l`.

Define integers recursively by

\[
A_0(s)=\mathbf 1_{\{s\in G\}},
\qquad
A_m(s)=\sum_{l=1}^7\sum_t w(s,l,t)A_{m-1}(t).
\tag{4.1}
\]

Then, by induction on `m`,

\[
\frac{A_m(s)}{H^m}
\]

is exactly the subprobability that the next `m` protected arrivals all lie in the seven-label alphabet, with the exact instantaneous reaction-race law at each step, and that the final projected state lies in `G`.

Taking the minimum over all 12,201 admissible initial descriptors therefore proves

\[
a_m=\min_s\frac{A_m(s)}{H^m}.
\]

The executed exact checker gives

\[
\min_s A_4(s)=127,650,816,
\]

and reduces

\[
\frac{127,650,816}{21,672^4}
=
\boxed{\frac{19}{32,834,164,804}}.
\]

The worst projected initial descriptor found at budget four is

`(0,0,0,0,0,0,0,0,0,0,0,0,1,0)`

in the frozen state-cell ordering recorded by the checker. No floating point enters the certificate.

## 5. Replace every 21-mark expander by the four-mark all-path expander

The deterministic macro logic only requires that each expander stage end with the `2x3` vacancy target. It does not require the particular old 21-mark word. Therefore the exact boundary-uniform factor (3.1) may replace `s21` at each of the twenty expander applications.

The eraser remains six protected arrivals and the two planters remain three arrivals each. Hence the complete macro length drops from

\[
432
\]

to

\[
\boxed{M_5=6+20\cdot4+2\cdot3=92.}
\tag{5.1}
\]

The protected box geometry is unchanged: 144 protected site clocks and 314 incident O2-edge clocks, giving total protected arrival rate

\[
\Lambda=144\cdot\frac12+314\cdot\frac14=\frac{301}{2}.
\]

Choose the shorter horizon

\[
T_5=\frac{M_5}{\Lambda}=\boxed{\frac{184}{301}}.
\]

Then the protected-arrival count has mean 92. Using the already-certified rational inequality `e^{-1}>32/87`,

\[
\Pr\{N(T_5)=92\}
=e^{-92}\frac{92^{92}}{92!}
>
\left(\frac{32}{87}\right)^{92}\frac{92^{92}}{92!}.
\tag{5.2}
\]

The eraser and planters together still consume exactly eight specified CO labels and four specified O2 labels, hence their embedded-label factor outside the expander stages is `301^{-8}602^{-4}`.

Combining the unchanged row-chain shuffle, eraser library, planter libraries, (3.1), and (5.2) yields the new exact certificate

\[
\boxed{
 b_5=
 \binom{20}{10}\;128\;\frac{35}{486}\;301^{-8}602^{-4}
 \left(\frac{19}{32,834,164,804}\right)^{20}
 \left(\frac{32}{87}\right)^{92}\frac{92^{92}}{92!}.
}
\tag{5.3}
\]

Therefore

\[
\boxed{B_{\rm cat}\ge b_5.}
\]

## 6. Exact comparison with the entering metric

The new one-stage factor relative to the old 100-word 21-mark stage is

\[
R_s
=
\frac{19/32,834,164,804}
     {(25/12)301^{-16}602^{-5}}
=
\boxed{
\frac{2,492,615,315,137,221,969,298,104,660,522,488,742,975,064,224}{25}
}
>1.
\tag{6.1}
\]

The Poisson-at-the-mean factor also improves when the macro length drops to 92:

\[
R_t=
\frac{(32/87)^{92}92^{92}/92!}
     {(32/87)^{432}432^{432}/432!}
>1.
\tag{6.2}
\]

Consequently

\[
\boxed{\frac{b_5}{b_4}=R_s^{20}R_t>1.}
\tag{6.3}
\]

This is exact metric movement. For scale only,

\[
\log_{10}R_s\approx43.99871525,
\qquad
\log_{10}R_t\approx0.36096777,
\]

so

\[
\boxed{
\log_{10}(b_5/b_4)\approx880.33527278.
}
\]

The exact formula (5.3) has diagnostic scale

\[
\log_{10}b_5\approx-210.85538322.
\]

This is an enormous improvement over the entering `b4`, but it is still nowhere near the sufficient block-percolation threshold `63/64`. The source problem therefore remains **PARTIAL / OPEN under bounded current-literature checking**, not solved.

A small secondary benefit of the shorter horizon is that the earlier parameter-continuity coupling now has coefficient

\[
T_5\left(N_v+\frac{N_e}{2}\right)
=\frac{184}{301}(144+157)
=\boxed{184},
\]

rather than the much larger old-horizon coefficient. This does not by itself imply coexistence because the good-block probability is still far below the percolation threshold.

## 7. B29 — the point at infinity is now an absorbing hitting problem, but it is not yet used as a claim

The budget family `a_m` exposes the correct compactification of the local calculation. Let `Q` be the substochastic transition operator of the seven-label automaton, with all other protected labels sent to a cemetery state. The fixed-budget quantities are matrix coefficients of `Q^m`. If the vacancy target is made absorbing, the **eventual** hit probability is the finite Dirichlet/absorbing-chain solution

\[
h=Q_T h+q,
\qquad
h=(I-Q_T)^{-1}q,
\]

whenever the transient inverse is justified.

That object would sum arbitrary harmless loops and variable-length successful histories. I did **not** use it in (5.3), because composing random stopping times through twenty stages while retaining a finite protected block horizon requires a separate duration/generating-function argument. Thus B29 found the next boundary object but produced no unsupported infinite-horizon claim.

The striking finite-budget result also changes the strategic diagnosis: the old 21-mark language was not merely sparse; it was structurally wasteful. The current bottleneck is now the tiny probability that four consecutive protected arrivals fall into a useful local pattern, repeated twenty times, plus the remaining macro architecture—not local deterministic reachability.

## 8. Exact finite self-check

The substantive checker was executed before this report and archived as

`artifacts/R08/20260918T1727Z_e0011_budgeted_prefix_dag_check.py`

with output

`artifacts/R08/20260918T1727Z_e0011_budgeted_prefix_dag_check.out`.

It independently:

- enumerates all 50,785 stable full boundary states;
- verifies the 12,201 projected admissible initial descriptors and the two ignored cells;
- constructs every exact one-step integer transition under common denominator `H=21672`;
- performs the prefix-DAG recursion for every budget `m=0,...,24`;
- proves the first uniformly positive tested budget is exactly four for the frozen alphabet;
- proves `a4=19/32834164804`;
- reconstructs the direct `b4` and `b5` formulas and checks `b5/b4>1` exactly.

This is a **self-check**, not an independent audit. Closure still requires the source-level theorem, a complete finite core, prior-art record, and two OTHER-track audits.

## 9. Method report

**B5 ADD A PARAMETER AND DIFFERENTIATE IN IT — succeeded strongly.** Treating the protected-arrival budget as a parameter immediately exposed that 21 was artificial. Exact computation gives zero worst-boundary mass for budgets 0 through 3 and positive mass at budget 4, reducing every expander from 21 arrivals to four.

**B10 DERANDOMIZE / make the existence calculation explicit — succeeded.** The prefix-DAG recurrence (4.1) deterministically sums every one of the `7^m` label prefixes together with every exact reaction branch, replacing heuristic sampling and hand-picked word libraries by an exact finite algorithm.

**B29 ADD THE POINTS AT INFINITY — partially succeeded.** The finite-budget family identifies the absorbing-chain Dirichlet problem as the natural infinite-history limit. I did not yet use that limit in a certificate because random stage durations must be glued into the finite Harris block rigorously.

## 10. What remains and next methods

The source is not closed. The explicit bound (5.3) is still of scale about `10^-211`, while this track's simple sufficient one-dependent oriented-percolation threshold is `63/64`.

The next run should **not** repeat B5/B10/B29 or any preceding E0011 triple. The next three moves are:

- **B6 DEFORM TO A POINT YOU CAN SOLVE:** introduce a generating parameter `z` for stage duration, solve the finite absorbing automaton for `z<1`, and control the limit toward first-hit stopping rather than fixing exactly four arrivals;
- **B21 ASK WHO ELSE HAS THIS SHAPE:** port exact phase-type / absorbing Markov-chain generating-function machinery used in reliability and probabilistic automata so variable stage durations can be composed without union bounds;
- **B23 DO WHAT THE PROPOSER DID NOT EXPECT:** abandon deterministic stage lengths entirely and define each vacancy expansion by its first successful hitting time, then seek a certified tail bound strong enough to fit twenty stages inside one finite block horizon.

A useful next measurable subtarget is therefore an exact rational or certified algebraic lower bound on

\[
\inf_{s\in S_0}\Pr_s(\tau_G\le L<\tau_\dagger)
\]

for a variable-duration stage, together with a tail bound that can be composed across twenty stages. The frozen fleet metric remains `B_cat`; no new metric is substituted.

## 11. Model/runtime-control truth

The requested `GPT-6 / maximum` setting is **not enforceable from the task surface exposed to this run**. This invocation identifies as GPT-5.6 Sol, and there is no authenticated reasoning-effort receipt, so the reasoning level is UNVERIFIED. The available task controls still expose title/prompt/schedule/timing/enabled state, but no binding model-family selector, no binding reasoning-effort selector, no authenticated completed-run model/effort telemetry, and no guaranteed-hour field. Making GPT-6/maximum enforceable would require a product/workspace/API/admin surface that exposes persistent model and effort controls plus per-run attestation.

The historical P26 `You cannot modify this task` error remains understood as an authorization-context boundary: a later full update succeeded from an authorized P/C context. For any task that still refuses modification, the legitimate remedies are the authorized owning context, a supported owner/admin transfer, or platform support—not GitHub edits or task duplication. I made no scheduler or permission changes.

## 12. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  predecessor: I0082
  predecessor_state: RETIRED_FROZEN
  predecessor_metric: 2/3
  predecessor_retirement_count: 6
  target: E0011
  source: Durrett_2009_Problem_5
  allocation: CLOSABLE_OUTSIDE
  owner: R08
  metric: B_cat
  before: ">= b4"
  after: ">= b5"
  b5: "C(20,10)*128*(35/486)*301^-8*602^-4*(19/32834164804)^20*(32/87)^92*92^92/92!"
  exact_gain: "b5/b4 = Rs^20*Rt > 1"
  stage_ratio: "2492615315137221969298104660522488742975064224/25"
  approximate_log10_gain: 880.3352727773
  approximate_log10_b5: -210.8553832183
  old_macro_marks: 432
  new_macro_marks: 92
  first_positive_local_budget_for_frozen_alphabet: 4
  unchanged_count_before: 0
  unchanged_count_after: 0
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  closure: false
  audits: 0/2
  self_check: artifacts/R08/20260918T1727Z_e0011_budgeted_prefix_dag_check.py
  self_check_output: artifacts/R08/20260918T1727Z_e0011_budgeted_prefix_dag_check.out
  methods: [5, 10, 29]
  next_methods: [6, 21, 23]
  predecessor_reopened: false
  old_fpp_reopened: false
  shared_root_writes: false
  peer_file_writes: false
  email: false
  drive: false
  public_posting: false
  scheduler_changes: false
```
