Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat: >= b2 -> >= b3 = b2 * 8 * (21/2)^20`; exact gain `8*(21/2)^20 > 1` (about `10^21.326876`). Unchanged count remains `0`. Methods used: B8, B14, B27.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: exact boundary-oblivious local word libraries

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source, ownership, and exclusions

I continued from the newest complete R08 report

`runs/R08/20260918T1425Z_e0011_poissonized_jumpchain_5e72b1.md`

rather than restarting the stale native title. The active exclusive claim remains `operations/claims/E0011.md`: Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, for the original two-dimensional catalyst/ZGB process with `r=infinity`, `q/2=1-p`, and **no added stirring**.

Hasebe--Ueda Problem 3.11 / I0082 remains **RETIRED/FROZEN at `2/3` after six supported unchanged runs**. I did not reopen it. The old R08 FPP strict-convexity route likewise remains retired from this slot.

At run start I reread/refreshed the controlling repository state: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest R08 report, current neighboring R07/R09 reports, and the relevant intake/claim records. E0011 remains exclusively owned by R08; no ownership collision was found.

I also refreshed the literature screen on 2026-09-18. Searches for exact combinations of `Durrett Problem 5`, `Coexistence in stochastic spatial models`, `ZGB`, `catalyst`, `no stirring`, and `coexistence` recovered Durrett's 2009 source and modified-model/simulation papers, including later ZGB variants, but no later primary theorem settling the original no-stirring Problem 5. This is **bounded negative evidence only**, not a claim of worldwide bibliographic completeness or novelty.

## 2. Frozen metric before this run

The active metric remains

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over complete source-valid finite protected Harris-block certificates at `p_0=1/2`, and `b(C)` is an exact certified lower bound on the good-block probability.

The preceding run proved

\[
B_{\rm cat}\ge b_2,
\]

where

\[
 b_2=
K\,\frac{35}{486}\left(\frac1{72}\right)^{20}
\left(\frac{32}{87}\right)^{432}
\frac{432^{432}}{432!}
\left(\frac1{301}\right)^{328}
\left(\frac1{602}\right)^{104},
\]

and

\[
K=2^{24}\binom{20}{10}=3,099,691,319,296.
\]

The factor `K` included only two geometric variants of each vacancy expander, two eraser variants, two planter variants per child, the two planter-child orders, and the row-chain shuffle count. The present run asks whether a **fixed, boundary-independent library of several successful local label orders** can replace those sparse two-word libraries.

## 3. B8 — discretize the one-column primitives completely enough to find new words

### 3.1 Vacancy expander

The already certified expander starts from a vacant `2x2` square and produces a vacant `2x3` rectangle. Its active patch has 16 sites, with 12 boundary variables. Exactly

\[
50,785
\]

of the `3^12=531,441` raw boundary assignments are stable.

I exhaustively checked the old 21-mark word and every **one-adjacent-swap** neighbor of it. Nine nontrivial adjacent swaps produce distinct words with positive boundary-uniform success. Including the original gives ten base words. Under the exact instantaneous reaction-race law their worst-boundary success probabilities are

\[
\boxed{
\frac1{72},\ \frac1{48},\ 
\underbrace{\frac1{72},\ldots,\frac1{72}}_{8\text{ further words}}
}
\]

in the checker ordering.

Thus the sum of the exact individual worst-boundary lower bounds over the ten base words is

\[
\frac1{48}+9\frac1{72}=\frac7{48}.
\]

This is a genuine finite-state computation with exact rational arithmetic; no simulation or floating-point comparison enters the claim.

### 3.2 Eraser

For the canonical two-species `2x2` seed, the six-mark eraser has multiset

`3 x CO(0,1), 2 x O2((-1,0),(-1,1)), 1 x CO(0,0)`.

There are exactly

\[
\frac{6!}{3!2!}=60
\]

distinct label orders. I exhaustively solved all 60 over all 625 stable boundary environments. Exactly **two** base orders have positive worst-boundary success, and both have the same exact minimum

\[
\boxed{35/486}.
\]

The old certificate used only one of these base orders and its geometric mirror.

### 3.3 Planter

The three-mark planter has multiset `O2, CO, CO`, hence three distinct orders. In the all-vacant `4x4` box their exact target-seed success probabilities are

\[
\boxed{0,1,1}.
\]

So there are two successful base orders, not one.

## 4. B14 — close each library under exact lattice symmetries

For the expander use vertical reflection

\[
R(x,y)=(x,1-y).
\]

It preserves the active patch, the set of stable boundary states, adjacency, the target vacancy event, and the equal-rate `p=1/2` reaction-race law. Therefore for every label word `w` and boundary state `eta`,

\[
P_{R\eta}(G\mid Rw)=P_\eta(G\mid w),
\]

and taking the infimum over all stable boundaries proves

\[
q(Rw)=q(w).
\]

The ten reflected expander words are pairwise distinct from each other and from the ten base words, giving a fixed 20-word library. Its summed worst-boundary reaction weight is therefore

\[
2\left(\frac1{48}+9\frac1{72}\right)=\boxed{\frac7{24}}.
\]

The old two-word expander library had weight

\[
2\frac1{72}=\frac1{36},
\]

so the exact gain **per expander application** is

\[
\boxed{\frac{7/24}{1/36}=\frac{21}{2}}.
\]

The eraser diagonal reflection used in the previous certificate fixes the canonical seed up to swapping its two vacant sites and preserves the reaction law. Reflecting the two newly certified base eraser orders gives four pairwise distinct variants, so the eraser library weight doubles relative to the previous two-variant library.

Likewise the planter diagonal reflection of the `4x4` box fixes the target O and CO sites. The two successful base orders and their reflections give four pairwise distinct successful planter words instead of the previous two; hence each child planter gains a factor `2`.

## 5. B27 — swap the boundary/word quantifiers with one fixed universal library

The important logical point is that I am **not** choosing a favorable word after seeing the boundary. Let `B` be the finite set of stable boundary states and, for a label word `w`, let

\[
q(w)=\inf_{\eta\in B}P_\eta(G\mid w).
\]

For the single fixed boundary-oblivious library `L` above, for every boundary `eta`,

\[
\sum_{w\in L}P_\eta(G\mid w)
\ge
\sum_{w\in L}q(w).
\]

The label-sequence events for distinct `w` are disjoint. Moreover every expander library word is only a permutation of the same 16 CO and 5 O2 labels, so all have the same embedded-label probability factor in the `p=1/2` protected process. The same is true within the eraser and planter libraries. Hence their lower-bound weights may be summed exactly before the 20 expander stages are composed.

This is the useful quantifier swap: one **fixed** finite library works uniformly over every stable exterior boundary.

## 6. Exact metric improvement

Nothing about the 432-mark macro length, its `328` CO labels, its `104` O2 labels, the Poisson count factor, the row-chain shuffle count, or the deterministic two-child implication changes.

Relative to `b_2`:

- the eraser library contributes a factor `2`;
- each of the 20 expander applications contributes a factor `21/2`;
- each of the two child planters contributes a factor `2`.

Therefore

\[
\boxed{
B_{\rm cat}\ge b_3:=b_2\,8\left(\frac{21}{2}\right)^{20}.
}
\]

The exact multiplicative gain is strictly larger than one. For scale only,

\[
\log_{10}\left(8(21/2)^{20}\right)
\approx 21.3268759684.
\]

Using the previous run's diagnostic `log10(b2) approx -1129.59497`, the new scale is about

\[
\log_{10}(b_3)\approx -1108.26809.
\]

The metric therefore moves exactly; the unchanged count remains zero.

## 7. Exact finite self-checks

Two substantive exact-arithmetic checks were executed before this report and their outputs archived:

1. `artifacts/R08/20260918T1602Z_e0011_expander_library_check.py`  
   output: `artifacts/R08/20260918T1602Z_e0011_expander_library_check.out`

   It enumerates all 50,785 stable expander boundaries, verifies the ten exact minima, checks reflection-closed pairwise distinctness, and proves the per-stage gain `21/2`.

2. `artifacts/R08/20260918T1602Z_e0011_eraser_planter_library_check.py`  
   output: `artifacts/R08/20260918T1602Z_e0011_eraser_planter_library_check.out`

   It enumerates all 60 eraser label orders over all 625 stable boundaries, proves exactly two base orders have worst-boundary minimum `35/486`, and checks the planter probabilities `0,1,1` and the reflected libraries.

These are **self-checks**, not independent audits.

## 8. What succeeded, what failed, and what remains

**B8 succeeded:** the smallest local components contain many more successful label orders than the previous single-word construction exposed. The complete six-mark eraser permutation scan and the one-swap expander neighborhood both yielded new exact routes.

**B14 succeeded:** reflection closes those routes into larger boundary-independent libraries without any loss in reaction probability.

**B27 succeeded partially:** the universal quantifier over exterior boundaries can be placed outside one fixed finite word library, and the disjoint word probabilities can be summed uniformly. This materially improves the certificate. It does **not** yet sum the full hitting probability of the local embedded chain.

The source problem is still very far from closed. The new bound remains astronomically below the track's sufficient `63/64` block threshold. The dominant remaining loss is now even more clearly the sparse accepted language of embedded adsorption labels: the current certificate accepts only finitely many 21-mark expander words instead of all label histories that eventually reach the vacancy target.

The next genuinely new objective is therefore to replace a word library by an exact **finite automaton / absorbing Markov-chain hitting computation** for one column. That can sum infinitely many successful histories with loops and harmless marks rather than only fixed-length permutations.

Track status remains

\[
\boxed{\text{PARTIAL / source OPEN under bounded current-literature checking}.}
\]

No audit or closure claim is made.

## 9. Next new methods

Do not repeat B8/B14/B27 next run, nor any earlier E0011 triple already used.

Use:

- **B1 CHANGE THE CATEGORY:** turn the one-column Harris evolution into a weighted finite automaton / absorbing Markov chain whose accepting states are vacancy expansion states and whose transition labels are actual local adsorption clocks.
- **B12 FIND WHAT IS CONSERVED:** identify the smallest state descriptor preserved by lattice symmetries and instantaneous stabilization (vacancy pattern plus interface data) so the exact Dirichlet system is much smaller than the raw `3^n` configuration space.
- **B30 ONE SCALE / ONE DIRECTION AT A TIME:** solve the exact one-column rightward expansion hitting probability first, with worst stable boundary, before composing ten columns and two rows.

The next metric target is an exact boundary-uniform one-column hitting probability strictly larger than `7/24` after the common embedded-label normalization, not another timing or finite multiplicity prefactor.

## 10. Model/runtime control status

The exposed automation update surface still provides only prompt/title/schedule/timing/enabled controls and exposes **no binding model-family selector, reasoning-effort selector, authenticated completed-run model telemetry, or guaranteed hour-long execution field**. Therefore `GPT-6 / maximum` remains prompt text only in this context; I cannot honestly claim it ran.

The repository's current `RESULTS.md` records that P26's historical `You cannot modify this task` failure was context-specific and that a later full update succeeded from an authorized P/C context. For a task that still rejects modification, the legitimate remedies remain its authorized owning context, supported owner/admin transfer, or platform support. I did not attempt any scheduler modification in this run.

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
  before: ">= b2"
  after: ">= b3 = b2 * 8 * (21/2)^20"
  movement: positive
  exact_gain: "8*(21/2)^20 > 1"
  approximate_log10_gain: 21.3268759684
  unchanged_count_before: 0
  unchanged_count_after: 0
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  closure: false
  audits: 0/2
  self_checks:
    - artifacts/R08/20260918T1602Z_e0011_expander_library_check.py
    - artifacts/R08/20260918T1602Z_e0011_eraser_planter_library_check.py
  self_check_outputs:
    - artifacts/R08/20260918T1602Z_e0011_expander_library_check.out
    - artifacts/R08/20260918T1602Z_e0011_eraser_planter_library_check.out
  methods: [8, 14, 27]
  next_methods: [1, 12, 30]
  predecessor_reopened: false
  old_fpp_reopened: false
  shared_root_writes: false
  email: false
  drive: false
  public_posting: false
  scheduler_changes: false
```
