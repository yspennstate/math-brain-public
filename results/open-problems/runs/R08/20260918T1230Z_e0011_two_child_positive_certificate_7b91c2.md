Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat: 0 -> >= 1/(3^432 * 1204^328 * 19264^104)`; unchanged count `2 -> 0`. Methods used: B3, B20, B25.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst/ZGB: exact positive two-child block certificate

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, source, ownership, and what I did not reopen

I continued from the newest R08 state on `master`,

`runs/R08/20260918T1122Z_e0011_vacancy_bulldozer_f1c7d9.md`.

The active source remains **E0011**, Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5, under the exclusive R08 claim `operations/claims/E0011.md`. The source model has states `0=vacant`, `1=CO`, `2=O`; `0 -> 1` occurs at rate `p`, neighboring `00 -> 22` at rate `q/4`, and unlike neighboring particles react at rate `r/4`. The ZGB normalization in Problem 5 takes `r=infinity` and `q/2=1-p`. The source asks for `0<p1<p2<1` such that coexistence occurs for every `p in (p1,p2)`.

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. Its R08 metric remains frozen at `2/3`, retirement count 6, under the immutable handoff. I also did not reopen the retired FPP strict-convexity route.

Before doing new mathematics I refreshed the campaign INDEX/RANKING, root POSTED/RESULTS, QUEUE, the E0011 ownership file, the newest R08 report, the E-intake entry and attempts history. No competing E0011 owner appeared. A fresh bounded web search on 2026-09-18 for combinations of `ZGB`, `catalyst`, `Durrett Problem 5`, `coexistence`, `no stirring`, and later rigorous results recovered the 2009 source, the older Durrett--Swindle catalyst paper, and simulation/modified-model literature, but no later primary theorem settling the original zero-stirring Problem 5. This is bounded negative evidence only, not a worldwide-open certificate.

The source itself records the simulated coexistence window `0.389 <= p <= 0.525` and separates Problem 5 from the known large-polymer and fast-stirring results. I retain those exclusions.

## 2. Frozen metric before this run

The E0011 metric is

\[
B_{\rm cat}=\sup_C b(C),
\]

where `C` ranges over **complete finite source-valid protected Harris-block certificates at `p0=1/2`**: one finite incoming two-species seed, a finite protected space-time block, a deterministic implication reproducing that seed into both forward oriented children, translated good-block indicators arranged to be 1-dependent, and `b(C)` an exact certified lower bound on the good-block probability.

The previous run had

\[
B_{\rm cat}=0,
\]

because it found a boundary-uniform vacancy translation word but not yet a two-child reproduction certificate.

The main result of this run is that the missing deterministic branching primitive does exist, and it can be embedded in a genuinely finite 1-dependent Harris block. The resulting probability is astronomically small, so this is **PARTIAL**, not coexistence.

## 3. B3 — PROVE SOMETHING STRONGER: a boundary-uniform vacancy expander

The preceding 12-mark word only shifted a `2 x 2` vacancy cursor. I searched instead for the stronger synchronizing property

\[
\text{vacant }2\times2\quad\Longrightarrow\quad\text{vacant }2\times3,
\]

uniformly over every stable one-neighborhood.

Use local coordinates

\[
A=\{-1,0,1\}\times\{0,1\},
\]

and assume only that the left two columns

\[
\{-1,0\}\times\{0,1\}
\]

are vacant. Every other site in the nearest-neighbor closure of `A` is arbitrary subject to source stability (no adjacent CO/O pair).

Condition instantaneous reaction choices on the same fixed legal priority used in the previous exact finite work: `E,W,N,S` for the newly adsorbed particle; for an O2 mark process the first endpoint before the second. The probability of realizing these finitely many tie outcomes is accounted for later rather than silently treating them as deterministic source dynamics.

The following **21-mark word** leaves all six sites of `A` vacant:

1. `CO(0,0)`
2. `O2[(-1,1),(0,1)]`
3. `CO(0,0)`
4. `CO(0,1)`
5. `CO(0,0)`
6. `CO(0,1)`
7. `CO(1,0)`
8. `CO(0,1)`
9. `CO(0,0)`
10. `O2[(-1,0),(-1,1)]`
11. `O2[(0,0),(0,1)]`
12. `CO(1,0)`
13. `CO(0,0)`
14. `CO(0,1)`
15. `CO(0,1)`
16. `CO(1,0)`
17. `CO(0,0)`
18. `O2[(-1,0),(-1,1)]`
19. `CO(1,0)`
20. `O2[(0,0),(0,1)]`
21. `CO(-1,1)`.

### Exact finite lemma

For every stable local configuration on the 16-site one-neighborhood with the prescribed incoming `2 x 2` vacancy square, this same 21-mark word leaves **all six active sites vacant**.

There are `3^12=531441` raw assignments of the 12 free sites and exactly **50,785** stable ones. The exact checker exhausts all of them and passes every case.

Why the 16-site patch is sufficient: every prescribed adsorption occurs in `A`; an instantaneous reaction can inspect only a nearest neighbor of a newly attached particle, hence only the one-neighborhood of `A`. Boundary sites are never newly occupied by the word. Consequently no state beyond that one-neighborhood can influence the finite transition map during this primitive.

This is stronger than translation: the parent cursor survives while a new vacant column is created. Repeating the primitive therefore grows a vacancy rectangle one column at a time.

Archived checker:

`artifacts/R08/20260918T1230Z_e0011_two_child_certificate_check.py`

Archived clean output:

`artifacts/R08/20260918T1230Z_e0011_two_child_certificate_check.out`

The relevant output is

```text
PASS exact R08/E0011 two-child certificate core
expander_stable_environments=50785
eraser_stable_environments=625
expander_word_length=21
eraser_word_length=6
planter_word_length=3
L=10
macro_marks=432 CO=328 O2=104
protected_sites=144 protected_edges=314
protected_total_rate=301/2
blocks_i_and_i_plus_2_have_disjoint_protected_clock_sets=True
b0_exact=1/(3^432 * 1204^328 * 19264^104)
b0_positive=True
```

This is a self-check, not an independent audit.

## 4. A canonical two-species seed, exact eraser, and exact planter

A vacancy block alone is not enough for the frozen metric: the incoming and outgoing seed must contain **both** species. I therefore freeze the following stable seed in a `4 x 4` box `Q_x=[x,x+3] x [0,3]`:

- `O` at `(x+1,2)`,
- `CO` at `(x+2,1)`,
- the other 14 sites vacant.

The two occupied sites are diagonal, so the seed is stable. The occupied sites also have a one-site vacant buffer inside `Q_x`.

### Boundary-uniform seed eraser

In local `2 x 2` coordinates with

\[
(-1,1)=O,\qquad (0,0)=CO,
\]

and the other two sites vacant, the 6-mark word

1. `CO(0,1)`
2. `O2[(-1,0),(-1,1)]`
3. `CO(0,1)`
4. `CO(0,0)`
5. `O2[(-1,0),(-1,1)]`
6. `CO(0,1)`

makes all four active sites vacant for **every** stable one-neighborhood. The checker exhausts all **625** stable compatible environments and passes them all. Since the other twelve sites of `Q_x` are already vacant in the canonical seed, this erases the entire `4 x 4` seed box without any friendly-boundary assumption.

### Three-mark planter

Conversely, in an all-vacant `4 x 4` box, the three marks

1. `O2[(x+1,1),(x+1,2)]`,
2. `CO(x+2,1)`,
3. `CO(x+2,1)`

produce exactly the canonical seed. The first CO reacts with the lower oxygen, and the second CO then remains; the upper oxygen is diagonal from it. Because all deposition sites lie one lattice step inside the vacant `4 x 4` box, arbitrary states outside the box cannot interfere with this three-mark construction.

Thus the seed can be erased to a vacancy resource and recreated after the resource has branched.

## 5. Complete deterministic two-child reproduction

Fix child spacing

\[
L=10.
\]

Let

\[
Q_i=[10i,10i+3]\times[0,3]
\]

carry the incoming canonical seed. Define the active rectangle

\[
A_i=[10i,10i+13]\times[0,3].
\]

The deterministic block word is:

1. Apply the 6-mark eraser to the incoming seed in `Q_i`. Since all other sites of `Q_i` are vacant, `Q_i` is now all vacant.
2. For each new column from `10i+4` through `10i+13`, apply the 21-mark vacancy expander once on rows `0,1` and once on rows `2,3`. Induction on the newly added column shows that the entire `4 x 14` rectangle `A_i` becomes vacant. There are `L=10` new columns and therefore `2L=20` expander applications.
3. Apply the three-mark planter in `Q_i`.
4. Apply the three-mark planter in
   \[
   Q_{i+1}=[10i+10,10i+13]\times[0,3].
   \]

The two child boxes are disjoint. The final state contains an exact copy of the incoming two-species seed in **both** forward child boxes.

The total number of prescribed adsorption marks is

\[
M=6+20\cdot21+2\cdot3=432.
\]

Counting by mark type gives

\[
N_{CO}=328,\qquad N_{O_2}=104,
\]

and indeed `328+104=432`. The checker verifies both counts.

The deterministic implication is therefore source-matching:

\[
\boxed{\text{one canonical two-species seed}\Longrightarrow
       \text{two separated canonical two-species seeds}.}
\]

The only remaining issue for a finite Harris certificate is to assign a protected region and a strictly positive exact probability to realizing this finite word without interfering marks.

## 6. Protected Harris block and 1-dependence

Take the conservative protected spatial box

\[
B_i=[10i-2,10i+15]\times[-2,5].
\]

It has width 18 and height 8, hence

\[
N_v=18\cdot8=144
\]

site clocks. Protect every O2 edge clock having at least one endpoint in `B_i`. The number of such undirected nearest-neighbor edges is

\[
N_e=(17\cdot8+18\cdot7)+(2\cdot8+2\cdot18)=262+52=314.
\]

The first term counts internal edges and the second edges crossing the boundary. The checker independently enumerates these incident edges and obtains 314.

At `p=1/2`, the source normalization gives `q=1`. Thus protected CO site clocks have rate `1/2` and protected O2 edge clocks rate `1/4`, so the total protected adsorption rate is exactly

\[
\Lambda=\frac{144}{2}+\frac{314}{4}=\frac{301}{2}.
\]

The two-layer padding is more than enough for locality: an uncontrolled mark outside `B_i` cannot directly modify the active rectangle or any site consulted by an instantaneous reaction produced by the prescribed word. There is no reaction cascade: an adsorption can trigger only the immediate unlike-pair removal(s).

For spatial blocks `i` and `i+2`, the protected boxes are disjoint:

\[
B_i\subset[10i-2,10i+15]\times[-2,5],
\]

while

\[
B_{i+2}\subset[10i+18,10i+35]\times[-2,5].
\]

Moreover their **incident edge-clock sets are disjoint**: an edge incident to the first box can reach at most `x=10i+16`, while an edge incident to the second can reach at least `x=10i+17`. The checker verifies disjointness explicitly. Adjacent blocks are allowed to overlap. Across disjoint time slabs, Poisson increments are independent. Therefore the translated good-block indicators can be arranged as the intended **1-dependent oriented block field**.

## 7. Exact strictly positive probability lower bound

Split the block time horizon into `M=432` slots of equal length

\[
\delta=\frac1\Lambda=\frac{2}{301}.
\]

Thus the total block time is finite,

\[
T=M\delta=\frac{864}{301}.
\]

In each slot require:

- exactly one protected adsorption mark in total;
- that mark is the next prescribed clock in the deterministic word;
- whenever an instantaneous reaction has several legal unlike neighbors, the reaction clocks realize the fixed priority outcome used by the finite transition map.

Because the total protected adsorption rate times `delta` equals 1, a specified CO site is the unique protected mark in its slot with probability

\[
e^{-1}\frac{(1/2)}{301/2}=\frac{e^{-1}}{301},
\]

and a specified O2 edge is the unique protected mark with probability

\[
e^{-1}\frac{(1/4)}{301/2}=\frac{e^{-1}}{602}.
\]

For a CO adsorption, at most four unlike reaction edges can compete, so a desired legal reaction partner has conditional probability at least `1/4`. For an O2 adsorption, the two adjacent new oxygen atoms have no common CO neighbor on the square lattice. At most eight unlike reaction edges compete for the first instantaneous reaction and at most four for the second; hence any desired legal sequential outcome used by the checker has conditional probability at least

\[
\frac18\cdot\frac14=\frac1{32}.
\]

If fewer or no reaction choices are present these bounds only improve. This is precisely the standard equal-rate `r -> infinity` resolution of the source reaction clocks; no favorable deterministic reaction rule is inserted for free.

Therefore the block-good event has probability at least

\[
e^{-432}\,1204^{-328}\,19264^{-104}.
\]

For an entirely rational certificate, use `e<3`, hence `e^{-1}>1/3`. Define

\[
\boxed{
 b_0:=\frac{1}{3^{432}\,1204^{328}\,19264^{104}}.
}
\]

Then

\[
\Pr_{p=1/2}(\text{good block})>b_0>0.
\]

Numerically only to indicate scale,

\[
\log_{10} b_0\approx -1662.1755.
\]

The exact result is the rational expression above, not the decimal.

This is the first R08 E0011 construction satisfying **all parts of the frozen finite-certificate definition**: two-species parent seed, finite protected block, deterministic two-child reproduction, 1-dependence geometry, finite time horizon, and an exact certified positive success lower bound.

Consequently

\[
\boxed{
B_{\rm cat}\ge b_0
=\frac{1}{3^{432}1204^{328}19264^{104}}>0.
}
\]

This is genuine metric movement.

## 8. B20 — FIND WHY THE ALGORITHM FAILS: exact-path synchronization is far too expensive

The construction above also diagnoses the present route's failure to prove coexistence. The preceding run supplied the very crude but explicit sufficient criterion

\[
\Pr(\text{good block})>\frac{63}{64}
\]

for domination/percolation of the standardized 1-dependent oriented block field. The present exact-path event has probability around `10^-1662`, so shortening this particular prescribed word by a modest constant factor cannot bridge the gap.

The obstruction is therefore no longer “can one branch the seed?” The answer is yes. The obstruction is:

\[
\boxed{\text{convert branching from one rare synchronizing trajectory into a high-probability robust block event.}}
\]

A successful continuation must count or absorb **many** admissible Harris histories, or identify a monotone/coarse event that succeeds under typical local evolution. Optimizing the exact one-mark-per-slot event alone is not a plausible closure route.

## 9. B25 — COUNT THE SAME THING TWICE

I used two independent finite counts at the points where an indexing mistake would invalidate the probability certificate.

First, the macro length is counted structurally as

\[
6+2L\cdot21+2\cdot3=432,
\]

and separately by mark type as

\[
328+104=432.
\]

Second, the protected O2 clocks are counted geometrically as

\[
(17\cdot8+18\cdot7)+(2\cdot8+2\cdot18)=314
\]

and independently by explicit set enumeration in the checker. The same enumeration verifies that the protected clock sets for blocks `i` and `i+2` are disjoint.

These duplicate counts are not an audit; they make the finite Harris lower bound internally checkable and exposed the exact rate

\[
\Lambda=301/2.
\]

## 10. Status, what is proved, and what is not

**Proved in this run, conditional only on the source's standard `r=infinity` equal-rate reaction-clock limit:**

- a 21-mark boundary-uniform `2 x 2 -> 2 x 3` vacancy expander;
- a 6-mark boundary-uniform eraser for a stable two-species seed;
- a 3-mark exact planter for that seed;
- a complete finite two-child seed-reproduction Harris block with child spacing 10;
- 1-dependence of translated good-block events under the displayed protected geometry;
- the exact positive lower bound
  \[
  b_0=(3^{432}1204^{328}19264^{104})^{-1}.
  \]

**Not proved:** coexistence, any nontrivial lower bound near the percolation threshold, or Durrett Problem 5 itself. A positive block probability is not enough. The track therefore remains

\[
\boxed{\text{PARTIAL / source OPEN under bounded current-literature checking}.}
\]

No closure or novelty claim is made. The synchronizing-word mechanism may well be finite-state/control folklore; novelty is UNVERIFIED.

## 11. Next distinct methods

Do not repeat B3/B20/B25 next run. The next research triple is:

- **B9 RANDOMIZE.** Replace a single prescribed Harris word by a large family of successful local histories and seek a coarse event with probability bounded away from zero, then toward one as block size grows.
- **B13 FIND WHAT ONLY INCREASES.** Search for a vacancy/interface “capacity” or protected-width functional that typically grows under the unbiased `p=1/2` dynamics, so a block can succeed without clock-by-clock synchronization.
- **B28 REPLACE FOR ALL WITH FOR TYPICAL.** Keep the deterministic implication uniform over exterior states, but stop requiring one universal internal trajectory; permit typical internal evolution and isolate a small exceptional internal-history set whose probability can be bounded exactly.

Because the frozen metric moved this run, its unchanged count resets to zero; the Section-I stuck protocol is not triggered.

## 12. Structured ledger delta (own immutable report only)

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
  before: "0"
  after: ">= 1/(3^432 * 1204^328 * 19264^104)"
  movement: positive
  unchanged_count_before: 2
  unchanged_count_after: 0
  source_status: OPEN_CURRENT_BOUNDED
  track_status: PARTIAL
  methods: [3, 20, 25]
  research_delta:
    - exact_boundary_uniform_21_mark_vacancy_expander_2x2_to_2x3
    - exact_boundary_uniform_6_mark_two_species_seed_eraser
    - exact_3_mark_two_species_seed_planter
    - finite_432_mark_parent_to_two_children_macro_certificate
    - exact_1_dependent_protected_geometry_L10
    - exact_positive_rational_good_block_lower_bound
  finite_core:
    checker: artifacts/R08/20260918T1230Z_e0011_two_child_certificate_check.py
    output: artifacts/R08/20260918T1230Z_e0011_two_child_certificate_check.out
  audits: []
  remaining_obligation: raise_a_source_valid_two_child_block_probability_to_a_certified_supercritical_1_dependent_level_then_use_parameter_continuity_to_open_a_nontrivial_p_interval
  next_methods: [9, 13, 28]
```

## 13. Model / reasoning / task-control status

The actual model visible to this run is **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so I report `UNVERIFIED` and do not claim GPT-6 maximum.

The currently exposed task-management surface still contains fields for prompt, title, schedule/timing and enabled state, but no binding model-family selector, no reasoning-effort selector, no guaranteed execution-duration control, and no authenticated completed-run model telemetry. Thus the requested GPT-6/maximum setting remains prompt text rather than something this interface can enforce.

The root RESULTS ledger now records that P26's earlier `You cannot modify this task` failure was context-specific: the full P26 update later succeeded from an authorized P/C context. For any task still refusing modification, the lawful fix is to operate from its authorized owning context, use a supported ownership/admin transfer, or ask platform support. Duplicating a task or changing GitHub text does not enforce its runtime model.

I made **no scheduler changes** in this run, consistent with the owner instruction.
