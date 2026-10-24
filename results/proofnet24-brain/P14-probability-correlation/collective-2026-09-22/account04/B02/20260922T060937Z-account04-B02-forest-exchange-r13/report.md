# FOREST B02 attempt report — multiplicity-fiber obstruction and one-defect repair

Run: `20260922T060937Z-account04-B02-forest-exchange-r13`  
Slot: `account04/B02`  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Refuted route: `FOREST-MULTIPLICITY-PRESERVING-HALL-v1` = `CANDIDATE_REFUTED`  
Parent FOREST target: `OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`  
Model self-report: GPT-5.6 Sol. Requested reasoning effort: maximum actually supported. Configured effort and provider reasoning-token/thinking-time counters: `UNKNOWN_NOT_EXPOSED`.

## 1. Exact scope and consumed other-account results

The target is the unit-weight uniform law on all acyclic edge subsets of every finite simple graph, including the empty forest, disconnected forests, and every forest size. For distinct edges `e,f`, write the Rayleigh gap as the unnormalized count difference.

I consumed and applied the latest complete team-lead handoff available at the start of the run, account01/B01 `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`, shared Git blob `4cee205cb7d254caf785692838111988a0b8a155`. I retain its correction that the old fixed-graph Cocks weighted-globalization bridge is not admitted; the parent conjecture remains open.

I also consumed the newest complete partner result then available from account01/B03, run `20260922T052013Z-b03-forest-r11-d011c5`, report Git blob `d975b5c7b4257aee81eb4ee136b0cccce64b5033`. Its exact residual comparison is the starting point below. Its later run `20260922T055054Z-b03-forest-r12` had only a start record when inspected and was therefore not substituted for the complete report.

## 2. Partner comparison, kept exactly

Put `G0=G-{e,f}` and let `N` be the set of all forests of `G0`. Define

- `A={K in N : e is addable to K}`;
- `B={K in N : f is addable to K}`;
- `D={K in N : e and f are jointly addable to K}`.

Then

`Delta_ef = |A||B|-|N||D|`,

and cancelling `A x D` gives the exactly equivalent residual comparison

`|(N\A) x D| <= |A x (B\D)|`.                                      (R)

Call the left and right state sets `L` and `R`.

The partner's full-radius reconnection lemma constructs, for every `(F,H) in L`, at least one target `(F',H') in R` by moving a set `T` of base edges from `F` to `H`. Every moved edge crosses two `H`-components, hence is absent from `H`; in both of the partner's cases the output has

`F'=F\T`, `H'=H union T`.

Thus for every base edge `g`, the total two-coordinate multiplicity

`mu_g(F,H) = 1[g in F] + 1[g in H] in {0,1,2}`                     (M)

is invariant under every partner reconnection. This is the key exact observation for the capacity question.

## 3. New no-go theorem: full-radius multiplicity-preserving Hall is false

### Theorem
There is no unit-capacity injection, and not even a fractional unit-capacity transport, from all states in `L` to states in `R` that preserves the complete multiplicity vector `mu=(mu_g)_{g in E(G0)}`. This fails already for disjoint marked edges in `K5`.

### Exact witness
Take `G=K5` on vertices `0,1,2,3,4`, with

`e=01`, `f=23`.

Then

`E(G0)={02,03,04,12,13,14,24,34}`.

Fix the multiplicity vector `mu*` which is `1` on

`S={02,03,12,13}`

and `0` on every other base edge. Since no edge has multiplicity two, a state in this fiber is simply a two-colouring of the four-cycle `S` into `F` and `H`.

The residual left fiber `L_mu*` consists of exactly four states:

1. `F={02,03,12}`, `H={13}`;
2. `F={02,03,13}`, `H={12}`;
3. `F={02,12,13}`, `H={03}`;
4. `F={03,12,13}`, `H={02}`.

In each case `F` connects `0` to `1`, so `F notin A`; and `H+01+23` is a forest, so `H in D`.

The residual right fiber `R_mu*` consists of exactly two states:

1. `F={02,13}`, `H={03,12}`;
2. `F={03,12}`, `H={02,13}`.

In each case `e` is addable to `F`, `f` is addable to `H`, and `H+e+f` contains the unique four-cycle through `e,f`, so `H in B\D`.

Therefore

`|L_mu*|=4 > 2=|R_mu*|`.                                            (F)

Any coupling preserving `mu` is trapped in this fiber, so (F) violates Hall. The same count also rules out a fractional row-mass-one / target-capacity-one transport within the fiber. Because the partner's full-radius move preserves `mu`, its pointwise reconnection lemma cannot be upgraded to the required global Hall statement without adding a genuinely `mu`-changing move.

This obstruction is stronger than the previous fixed-radius obstruction: it permits arbitrary radius and arbitrary recolouring inside a fixed multiplicity fiber. The failure is not caused by too short a path.

## 4. The target inequality itself is strict on the witness

The obstruction is only to the coupling class, not to FOREST. Exact enumeration on the same `K5` instance gives

`|N|=134`, `|A|=|B|=64`, `|D|=29`,

hence

`|L|=(134-64)*29=2030`,
`|R|=64*(64-29)=2240`,
`Delta=64^2-134*29=210 > 0`.

Thus other multiplicity fibers provide the missing global capacity. In fact, summing the exact diagonal capacities over every multiplicity vector gives only

`sum_mu min(|L_mu|,|R_mu|)=1924`,

so every globally successful injection must move at least `2030-1924=106` left states across multiplicity fibers in this instance.

This gives a quantitative form of the no-go theorem, not merely one bad local fibre.

## 5. Minimal structural repair tested exactly

A natural next coupling relation is to allow one defect in the total edge-multiplicity vector. Define a fiber adjacency

`mu ~_1 nu  iff  #{g : mu_g != nu_g} <= 1`.

For this relation, keep all actual forest states and their exact component multiplicities; only the coarse transport permission changes. A capacitated fiber flow sends each left fiber `L_mu` into right fibers `R_nu` with `mu~_1 nu`, with source capacities `|L_mu|` and target capacities `|R_nu|`.

On the exact disjoint-edge `K5` witness, the maximum integral flow is

`2030/2030`.

So one multiplicity-coordinate defect is sufficient to repair the first obstruction at the coarse fiber-flow level, whereas zero defects have exact maximum `1924/2030`.

This is finite evidence only. No universal one-defect Hall theorem is claimed.

## 6. Compact conditional end-to-end route and the first unpaid implication

For an arbitrary simple graph and marked pair, partition `L` and `R` by the vector (M), writing `L_mu,R_mu`. Let `Gamma_1(U)` be the set of right multiplicity vectors at Hamming distance at most one from some `mu in U`.

The exact first missing implication for this repaired coupling is the capacitated Hall inequality

`sum_{mu in U} |L_mu| <= sum_{nu in Gamma_1(U)} |R_nu|`              (H1)

for every set `U` of left multiplicity vectors.

If (H1) were proved universally, capacitated Hall would give a state-level injection `L -> R`, because every left state in a fiber is allowed to couple to every right state in an adjacent fiber. Then (R) holds, hence `Delta_ef>=0`, which is exactly the parent pairwise negative-correlation statement.

I do **not** promote (H1) to a theorem. The proved statement this run is the prior necessary structural step: the `Gamma_0`/multiplicity-preserving version is impossible, even with full-radius and arbitrary within-fiber recolouring. Any successful direct exchange proof must cross multiplicity fibers. The `Gamma_1` formulation is a sharply specified next candidate whose first obstruction passes exactly on `K5`, not a replacement of the unpaid universal theorem by assertion.

## 7. Comparison with the lead's current route

The lead's `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1` attacks minimal counterexamples using rank-homogeneous influence budgets and isolates a STAR-2 triangle-conditioning debt. The present result is orthogonal: its counterexample to multiplicity-preserving Hall already occurs in `K5`, where triangle structure is maximal. It therefore does not compete with or weaken the lead route. It tells the exchange/coupling branch exactly what extra degree of freedom is unavoidable before any Hall argument can be universal.

## 8. Exact checker and status

The attached checker independently enumerates every forest of `K5-{01,23}`, reconstructs `A,B,D,L,R`, verifies the six witness fibre states above, computes the total multiplicity-preserving capacity, and solves the one-defect capacitated flow with an integer max-flow implementation. Its terminal line is `ALL_EXACT_ASSERTIONS_PASSED`.

Outcome: `ESSENTIAL_STEP_APPLIED`; subsidiary route `FOREST-MULTIPLICITY-PRESERVING-HALL-v1` is `CANDIDATE_REFUTED`; parent FOREST remains `OPEN`.

No brain installation/benchmark work, production-state mutation, scheduler mutation, email, Drive action, public posting, paid/remote compute, permission bypass, or unrelated private-data access was performed.
