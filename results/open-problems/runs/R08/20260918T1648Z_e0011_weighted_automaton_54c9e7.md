Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat: >= b3 -> >= b4 = b3*(50/7)^20`; exact gain `(50/7)^20 > 1` (about `10^17.077439`). Unchanged count remains `0`. Methods used: B1, B12, B30.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: weighted one-column automaton and a 100-word universal library

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source, ownership, and exclusions

I continued from the newest complete R08 report

`runs/R08/20260918T1602Z_e0011_boundary_oblivious_library_6d2f8a.md`

rather than restarting the stale native title. The active exclusive claim remains `operations/claims/E0011.md`: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, for the original two-dimensional catalyst/ZGB process with `r=infinity`, `q/2=1-p`, and **no added stirring**.

The predecessor Hasebe--Ueda Problem 3.11 / I0082 remains **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I did not reopen it. The old R08 FPP strict-convexity route likewise remains retired from this slot.

At run start I reread/refreshed the controlling repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the I0082 and E0011 claim files, the newest complete R08 report, and current neighboring R07/R09 reports. E0011 remains exclusively owned by R08; no ownership collision was found.

The current-literature screen was refreshed on 2026-09-18. The primary source `arXiv:0906.2293` still states Problem 5. A currently served Durrett Wald-lecture PDF also still labels the catalyst item “Problem 5: Prove coexistence.” Fresh bounded searches for the exact catalyst/ZGB no-stirring question found simulations and modified-model results but no later primary theorem proving source Problem 5. This is **bounded negative evidence only**, not a worldwide-open or novelty certificate.

## 2. Frozen metric before this run

The active metric remains

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected Harris-block certificates at `p_0=1/2`, and `b(C)` is an exact certified lower bound on the good-block probability.

The preceding run proved

\[
B_{\rm cat}\ge b_3,
\qquad
b_3=b_2\,8\left(\frac{21}{2}\right)^{20}.
\]

For one 21-mark vacancy-expander stage, its fixed reflection-closed 20-word library had total worst-boundary reaction weight

\[
W_3=\frac7{24}.
\]

Here “reaction weight” is the sum of conditional reaction-success probabilities over **distinct embedded label sequences**. It is not itself a probability and can exceed one after enough distinct label sequences are aggregated; each sequence still carries its own small embedded-label probability.

The objective of this run was the one chosen in the preceding report: replace the small hand-built word library by a finite weighted-automaton search at exactly one rightward vacancy-expansion scale.

## 3. B1 — change category: the local expander is a weighted finite automaton

Keep the exact 16-site patch and the same seven adsorption-label types already used by the certified 21-mark expander:

1. `CO(0,0)`,
2. `O2((-1,1),(0,1))`,
3. `CO(0,1)`,
4. `CO(1,0)`,
5. `O2((-1,0),(-1,1))`,
6. `O2((0,0),(0,1))`,
7. `CO(-1,1)`.

A stabilized local configuration is a state. An adsorption label is an input letter. If adsorption creates several possible instantaneous reaction partners, the outgoing edges carry their exact rational reaction-race probabilities. The accepting set consists of states in which the full `2x3` active rectangle is vacant.

Thus a 21-letter label word `w` has exact boundary-dependent acceptance probability

\[
P_\eta(G\mid w),
\]

and the source-valid robust weight is

\[
q(w)=\inf_{\eta\in\mathcal B}P_\eta(G\mid w),
\]

where `\mathcal B` is the finite set of stable exterior boundary states. This formulation separates the two sources of small probability cleanly:

- the embedded Harris chain chooses the adsorption labels;
- the weighted automaton supplies the exact conditional reaction probability once those labels are fixed.

I searched the adjacent-transposition neighborhood of the old 21-letter word and retained a concrete library of 50 pairwise-distinct words with an unexpectedly uniform exact value

\[
\boxed{q(w)=\frac1{48}\quad\text{for every one of the 50 words}.}
\]

The metric claim below uses only this explicit hard-coded 50-word library and its exact verification; no claim about search optimality is needed.

## 4. B12 — find what is conserved/irrelevant: exact 12,201-state quotient

The old full boundary enumeration had

\[
50,785
\]

stable configurations among the `3^12=531,441` assignments of the twelve non-fixed cells.

The weighted-automaton language above never reads or writes two of those shell cells:

\[
\boxed{(1,2),\ (2,1)}.
\]

They are also not target cells. Their values therefore cannot affect any transition probability or the final vacancy event for any word over the seven-label alphabet.

Projecting stable full states to the ten actually relevant non-fixed cells collapses the 50,785 full boundary states to exactly

\[
\boxed{12,201}
\]

relevant descriptors. The checker proves the read/write-support claim directly and verifies the quotient count by exhaustive exact enumeration. Hence evaluating a word on one representative of each descriptor is **exact**, not an approximation or symmetry heuristic.

This is the useful state-space reduction for the next absorbing-chain attack: the local problem is already smaller than the raw `3^12` shell description before any group quotient is applied.

## 5. B30 — one scale / one direction: exact 100-word boundary-oblivious library

For each of the 50 explicit base words the exact checker evaluates all 12,201 descriptors under the instantaneous reaction-race law and proves

\[
q(w)=\frac1{48}.
\]

Therefore one fixed, boundary-independent 50-word library has total robust reaction weight

\[
W_{50}=50\cdot\frac1{48}=\frac{25}{24}.
\]

Vertical reflection `R(x,y)=(x,1-y)` preserves the active patch, stability, target event, equal-rate law, and robust weight. The 50 reflected words are pairwise distinct and disjoint from the 50 base words. Hence the fixed reflection-closed 100-word library has

\[
\boxed{W_{100}=2W_{50}=\frac{25}{12}.}
\]

Again, `25/12` is a **sum of conditional reaction weights over disjoint label-sequence events**, not a probability.

Every one of these words is a permutation of the same 21-label multiset as the previous expander construction, with exactly 16 CO marks and 5 O2 marks. Thus every word carries the same embedded-label probability factor at `p_0=1/2`. Distinct words are disjoint events in the embedded label sequence, so their weighted contributions may be added before the 20 expander applications are composed.

Relative to the preceding reflection-closed library,

\[
\boxed{
\frac{W_{100}}{W_3}
=
\frac{25/12}{7/24}
=
\frac{50}{7}.
}
\]

This is an exact gain **per expander stage**.

## 6. Exact metric improvement

The complete two-child macro uses twenty expander stages. Nothing in the eraser, two planters, macro length, CO/O2 counts, Poissonization, protected-box geometry, one-dependence argument, or deterministic parent-to-two-children implication changes.

Therefore the old complete certificate can replace its expander library independently at all twenty stages, giving

\[
\boxed{
B_{\rm cat}\ge b_4
:=b_3\left(\frac{50}{7}\right)^{20}.
}
\]

The exact multiplicative gain satisfies

\[
\left(\frac{50}{7}\right)^{20}>1.
\]

For scale only,

\[
20\log_{10}(50/7)\approx17.0774392864.
\]

Using the preceding report's diagnostic `log10(b3) approx -1108.26809`, the new diagnostic scale is approximately

\[
\log_{10}(b_4)\approx -1091.19065.
\]

Thus the frozen metric moves and the supported unchanged count remains zero.

## 7. Exact finite self-check

Executed and archived:

`artifacts/R08/20260918T1648Z_e0011_automaton_100word_check.py`

with output

`artifacts/R08/20260918T1648Z_e0011_automaton_100word_check.out`.

It verifies with exact `Fraction` arithmetic:

- all `50,785` stable full boundary states;
- the exact ten-cell dependency support and the two irrelevant shell cells;
- exactly `12,201` relevant descriptor states;
- all 50 hard-coded base words have worst-boundary probability exactly `1/48`;
- their reflections form a 100-word pairwise-distinct library;
- `W_50=25/24`, `W_100=25/12`;
- the exact per-expander improvement is `50/7`.

This is a **self-check**, not an independent audit.

## 8. What moved, what did not, and the remaining obstruction

**B1 succeeded.** The one-column primitive is naturally a finite weighted automaton, and word aggregation is the right quantity rather than another handcrafted trajectory.

**B12 succeeded.** Two of the twelve nominal boundary variables are provably dynamically invisible for this alphabet; the exact local descriptor space is `12,201`, not `50,785` full stable states or `3^12` raw assignments.

**B30 succeeded.** Solving only one rightward 21-mark scale already enlarged the certified reflection-closed language from 20 to 100 words and improved the complete block certificate by `(50/7)^20`.

The source problem remains very far from closed. Even after this gain the certified block probability is astronomically below the sufficient `63/64` threshold. The dominant loss is still that the certificate accepts a tiny finite subset of all successful embedded-chain histories. The next qualitative jump must sum histories of **variable length**, including harmless marks and loops, rather than finding another finite batch of length-21 permutations.

Track status remains

\[
\boxed{\text{PARTIAL / source OPEN under bounded current-literature checking}.}
\]

No closure or audit claim is made.

## 9. Next genuinely new methods

Do not repeat B1/B12/B30 next run, nor any earlier E0011 method already used. Use three methods not yet used on E0011:

- **B5 ADD A PARAMETER AND DIFFERENTIATE IN IT:** introduce a mark-budget `m` and compute the exact robust accepted mass `A_m` for one-column histories of length at most `m`; study the marginal gain `A_{m+1}-A_m` instead of optimizing individual words.
- **B10 DERANDOMIZE:** convert the successful-history search into an explicit deterministic prefix-DAG / dynamic program that sums every accepted path in the chosen finite truncation, with a reproducible state ordering rather than heuristic word discovery.
- **B29 ADD THE POINTS AT INFINITY:** pass from finite mark budgets to the absorbing-chain limit, so harmless loops are summed geometrically and the exact one-column eventual hitting probability is the solution of a finite rational Dirichlet system.

The next metric target is not another multiplicity prefactor. It is an exact boundary-uniform eventual hitting lower bound for one rightward expansion that strictly dominates every finite fixed-length word-library bound.

## 10. Model/runtime control status

The exposed automation update surface in this run still has prompt/title/schedule/timing/enabled controls but exposes **no binding model-family selector, reasoning-effort selector, authenticated completed-run model telemetry, or guaranteed hour-long execution field**. Therefore `GPT-6 / maximum` remains prompt text only here; I cannot honestly claim it ran.

The repository's current `RESULTS.md` records that P26's historical `You cannot modify this task` failure was context-specific and that a later full update succeeded from an authorized P/C context. For a task that still rejects modification, the legitimate remedies remain its authorized owning context, supported owner/admin transfer, or platform support. No scheduler modification was attempted in this run.

## 11. Structured ledger delta

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
  before: ">= b3"
  after: ">= b4 = b3*(50/7)^20"
  movement: positive
  exact_gain: "(50/7)^20 > 1"
  approximate_log10_gain: 17.0774392864
  unchanged_count_before: 0
  unchanged_count_after: 0
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  closure: false
  audits: 0/2
  exact_full_stable_states: 50785
  exact_descriptor_states: 12201
  exact_base_word_count: 50
  exact_reflection_closed_word_count: 100
  exact_base_word_minimum: 1/48
  exact_new_expander_weight: 25/12
  exact_expander_gain: 50/7
  self_checks:
    - artifacts/R08/20260918T1648Z_e0011_automaton_100word_check.py
  self_check_outputs:
    - artifacts/R08/20260918T1648Z_e0011_automaton_100word_check.out
  methods: [1, 12, 30]
  next_methods: [5, 10, 29]
  predecessor_reopened: false
  old_fpp_reopened: false
  shared_root_writes: false
  email: false
  drive: false
  public_posting: false
  scheduler_changes: false
```
