Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT: `B_cat >= b7 -> B_cat >= b8`, exact `b8>b7`; diagnostic `log10(b8/b7)=31.731011526399868`. Unchanged count remains `0`. Methods actually used: B3, B15, B24.**

# R08 CLOSABLE OUTSIDE — E0011 catalyst coexistence: asymmetric seed-class regeneration

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity, exclusions, ownership, and current-source check

I did **not** reopen the native-title source Hasebe--Ueda Problem 3.11 (`I0082`). Its controlling six-run handoff is `runs/R08/20260916T2327Z_i0082_sixrun_handoff_rotation_hold_4f8c2d.md`; the old explicit-candidate metric remains frozen at `2/3`, and `operations/claims/E0011.md` explicitly records I0082 as RETIRED/FROZEN. The old R08 FPP assignment is likewise not reopened.

The active exclusive claim remains **E0011**, Rick Durrett, *Coexistence in stochastic spatial models*, Ann. Appl. Probab. 19 (2009), Problem 5: prove coexistence in the original two-dimensional catalyst/ZGB process with `r=infinity` and `q/2=1-p`, without added stirring. The frozen metric is

\[
B_{\rm cat}:=\sup_C b(C),
\]

over complete source-valid finite 1-dependent two-child Harris-block certificates at `p=1/2`.

Before research I refreshed the required repository state: campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/I0082.md`, `operations/claims/E0011.md`, the newest R08 report, neighboring R07/R09 reports, and the E0011 intake/ownership search. No competing E0011 owner or source-resolution exclusion appeared.

I also refreshed the bounded literature screen on 2026-09-18. Durrett's source remains arXiv:0906.2293 / DOI 10.1214/08-AAP590. His currently served Duke notes, Chapter 5, Section 5.4, still present the ZGB numerical coexistence window and then explicitly add fast stirring to obtain the PDE route. Searches for the exact no-stirring ZGB/catalyst coexistence target, later rigorous catalyst results, and 2025--2026 ZGB work recovered simulation or modified-model papers but no later primary theorem closing Durrett Problem 5. This is bounded negative evidence only, not a worldwide novelty certificate.

The immediately preceding R08 report was

`runs/R08/20260918T1953Z_e0011_local_interference_cone_a31f9c.md`,

which proved

\[
B_{\rm cat}\ge b_7,
\qquad
\log_{10}b_7\approx -130.96747290287607,
\]

and used B2/B17/B22. All thirty Section-B methods had appeared at least once on E0011, so the method catalog can restart; this run does not repeat the preceding triple.

## 2. Idea before code

The previous construction paid for three logically unnecessary operations: erase the incoming two-species seed, transport only vacancies, and then recreate **both** child seeds. That is symmetric but wasteful.

The new idea is to use a stronger seed statement but a less restrictive seed configuration:

> Preserve the incoming species forever, use only a nearby vacancy cursor as the mobile resource, and manufacture only the *new* right child. The unchanged parent itself is the left child.

This changes the regeneration event rather than shaving another constant from the old symmetric macro.

## 3. B3 — stronger regeneration over a whole seed class

Normalize the parent at spatial coordinate zero. Define the seed cylinder by fixing only

\[
O\text{ at }(-2,1),(-2,2),\qquad CO\text{ at }(-4,1),
\]

and the eight cursor vacancies

\[
C_0:=\{0,1\}\times\{0,1,2,3\}.
\]

Every other site is arbitrary subject only to the source stability condition (no adjacent unlike occupied pair). Thus this is not one exact canonical microstate: the block implication must work uniformly over **every stable exterior completion** of these eleven fixed sites.

The occupied sites are stable: the CO site is not adjacent to either O. More importantly, these three occupied sites are disjoint from the complete 14-cell read/write support of every accepted vacancy-expander stage below. During each stage their clocks are also inside the protected local interference set. Hence the parent O/O/CO triple survives deterministically on the good event.

For the vacancy cursor use the exact seven-label all-history `2 x 2 -> 2 x 3` expander already certified in preceding R08 reports. Its finite state reduction is unchanged: all `50,785` stable full local boundary configurations reduce to `12,201` projected descriptors, and the accepted-history probability is exact rational arithmetic.

Starting from cursor columns `0,1`, for each

\[
c=2,3,\ldots,10
\]

run one expander on rows `0,1` and then one on rows `2,3`. There are therefore only **18** expander windows, rather than the previous 20. On success the full corridor

\[
\{0,1,\ldots,10\}\times\{0,1,2,3\}
\]

has been cleared as needed, and in particular columns `9,10` form a new eight-site vacancy cursor.

At the end use just two adsorption marks:

1. `O2[((7,1),(7,2))]`,
2. `CO((5,1))`.

Their full nearest-neighbor read/write support is a 12-cell subset of the already cleared four-row corridor. Those support cells are protected from the moment they are cleared until the planter window. The CO root `(5,1)` is not adjacent to either oxygen root, so with this buffer vacant no reaction occurs. These two marks therefore produce

\[
O\text{ at }(7,1),(7,2),\qquad CO\text{ at }(5,1),
\]

while columns `9,10` remain vacant. This is exactly the original seed translated by

\[
L=9.
\]

The unchanged parent seed is the left child and the translated seed is the right child. Thus the source-valid deterministic implication is

\[
\boxed{\text{one seed-class occurrence}\Longrightarrow
       \text{two seed-class occurrences at offsets }0\text{ and }9.}
\]

No eraser and no left replanter are used.

## 4. Local protection and exact stage rates

For a protected state set `S`, retain the preceding report's exact interference family

\[
I(S)=\{a:W(a)\cap S\ne\varnothing\},
\qquad
D(S)=2N_{CO}(S)+N_{O_2}(S),
\]

so the total interference rate at `p=1/2` is `D(S)/4`.

During a top/bottom expander window I protect:

- the three parent occupied sites and the original eight-site parent cursor;
- the complete 14-cell read/write support of the current expander;
- the other row-pair's current two-column vacancy cursor;
- every final right-child planter-buffer or right-child-cursor site that has already been cleared.

This gives the exact 18-stage sequence

\[
\boxed{
174,178,195,199,220,221,242,242,260,257,271,278,281,290,302,307,324,325.
}
\]

The final two-mark planter protects the parent core, the complete right-child planter buffer, and the right-child cursor. Its exact clock count is

\[
(D,N_{CO},N_{O_2})=(308,69,170).
\]

The local projection lemma from the preceding report applies verbatim: clocks outside `I(S)` cannot alter any protected state cell in that window, because one adsorption plus its instantaneous reaction has write support `W(a)` and there is no secondary reaction cascade.

## 5. Exact finite B24 search: first admissible spacing in a frozen two-mark family

To ensure the asymmetric geometry was not hand-picked, I froze the following finite search family before comparing probabilities:

- the parent cursor is `C0` above;
- the occupied seed consists of one nearest-neighbor O2 pair and one nonadjacent CO site;
- all three occupied roots lie in rows `1` or `2` and have parent x-coordinate in `{-12,...,-1}`;
- occupied roots must avoid every accepted expander read/write support;
- after translation by `L`, the complete two-mark planter support must lie in the cleared four-row corridor;
- the full union of site and edge Poisson clocks used by blocks at spatial distance two must be disjoint.

Exact enumeration gives the number of admissible 1-dependent seeds

\[
\boxed{
L=5:0,\quad L=6:0,\quad L=7:0,\quad L=8:0,\quad L=9:3,\quad L=10:16.
}
\]

This is a statement **only about the frozen finite family**, not a global minimum-spacing theorem for the model.

At `L=9` the three candidates were then compared using their full exact block lower bounds. The winner is precisely

\[
O: (-2,1),(-2,2),\qquad CO:(-4,1),
\]

with diagnostic `log10` lower bound `-99.23646137647626`. The other two candidates give `-99.26193552993931` and `-99.26327079700076`. Hence the selected geometry is an exact extremizer within this frozen first-admissible family.

For the selected block, the union of protected CO-site clocks has x-span `[-5,12]`, while protected O2 edge endpoints have x-span `[-6,13]`. The exact checker verifies that translating the full site-clock and edge-clock sets by `2L=18` gives **disjoint clock identities**. Thus the same spatial 1-dependence mechanism used in the prior certificate survives. Time generations can again be placed in disjoint deterministic slabs.

## 6. Exact probability lower bound and metric movement

For a localized expander with interference unit `D`, let the already-certified exact all-history lower bound be

\[
c(D)=\left(\frac{32}{87}\right)^2
\min_{\eta}\sum_{n=0}^{8}
\frac{2^n}{n!}\frac{A_n(\eta)}{(36D)^n},
\]

where `eta` ranges over the `12,201` stable projected incoming descriptors and `A_n(eta)` is the exact integer reaction weight of all accepted seven-label histories of length `n` ending with the `2 x 3` target vacant. As before, the checker scans integer Poisson means `1,...,8` and verifies mean `2` is optimal for every `D` used here. The factor `32/87` is the previously certified rational lower bound for `e^{-1}`.

For the final planter, use one window with Poisson mean `2`. Require exactly two interference arrivals, first the desired O2 edge and then the desired CO site. Since their conditional label probabilities are `1/308` and `2/308`, respectively,

\[
P_{\rm plant}
>
\left(\frac{32}{87}\right)^2
\frac{2^2}{2!}\frac1{308}\frac2{308}
=
\boxed{\frac{256}{44,876,601}}.
\]

Therefore the new complete block certificate is

\[
\boxed{
 b_8=
 \frac{256}{44,876,601}
 \prod_{D\in\mathcal D_8} c(D),
}
\]

with

\[
\mathcal D_8=(174,178,195,199,220,221,242,242,260,257,271,278,281,290,302,307,324,325).
\]

The exact-arithmetic checker reconstructs the complete preceding `b7`, constructs `b8`, and proves by integer comparison

\[
\boxed{b_8>b_7}.
\]

Diagnostic decimal scales are

\[
\log_{10}b_7\approx-130.96747290287607,
\]

\[
\boxed{\log_{10}b_8\approx-99.23646137647626},
\]

so

\[
\boxed{\log_{10}(b_8/b_7)\approx31.731011526399868}.
\]

The deterministic time horizon is finite and exact:

\[
\boxed{
T_8=
\frac{15096961711209168777703329328}
     {24551648040723854903619591825}
\approx0.614906245241371.
}
\]

Thus the frozen E0011 metric genuinely moves:

\[
\boxed{B_{\rm cat}\ge b_8>b_7.}
\]

## 7. What the three methods taught

**B3 — prove something stronger.** Requiring reproduction of one exact mostly-vacant `4 x 4` microstate was counterproductive. The stronger *uniform seed-cylinder* statement — three species sites plus eight vacancies, arbitrary stable remainder — is easier to propagate because the parent itself can survive as one child.

**B15 — break symmetry.** Symmetric “erase, transport, replant twice” regeneration wasted most of the previous probability. Directional regeneration keeps the left child in place and creates only the right child. This removes the eraser, one planter, and two expander stages.

**B24 — find the extremal object.** In the frozen two-mark family, exact geometry search shows the first spacing compatible with the inherited 1-dependence test is `L=9`, with three possibilities, and the displayed vertical-O-pair seed gives the largest exact block lower bound among those three.

## 8. Status and next route

Status remains **PARTIAL / OPEN_CURRENT_BOUNDED**. This does **not** prove coexistence: `b8` is still about `10^-99`, vastly below the track's sufficient `63/64` threshold. No closure audit is requested because closure has not been reached.

The improvement does change the diagnosis. The old cost of rebuilding an exact symmetric seed was artificial; after removing it, the remaining loss is concentrated in requiring eighteen successive vacancy-expander successes against worst-case stable local boundaries.

Next nonrepeating methods:

- **B9 RANDOMIZE:** replace serial stage success by a block event that sums over many spatial growth fronts and orders, not one prescribed left-to-right corridor;
- **B20 FIND WHY THE ALGORITHM FAILS:** compute which stage/boundary descriptor dominates the `c(D)` minima and identify the exact geometric obstruction it represents;
- **B28 REPLACE FOR ALL WITH TYPICAL:** keep source validity but attempt a rigorously generated shield/interface distribution so later stages need high probability under the block's own conditional law rather than the worst stable exterior state at every stage.

A further small reduction of `D` is not enough; the next route must change the exponential-in-stage success mechanism.

## 9. Exact artifacts

Self-check (not an independent audit):

- `artifacts/R08/20260918T2029Z_e0011_asymmetric_seed_check.py`
- `artifacts/R08/20260918T2029Z_e0011_asymmetric_seed_check.out`

The checker independently:

1. re-enumerates all `50,785` stable full expander boundaries and the `12,201` projected descriptors;
2. reconstructs the previous exact `b7` from its archived formula;
3. enumerates the frozen asymmetric seed family for `L=5,...,10` and verifies counts `0,0,0,0,3,16`;
4. checks parent-species separation from every accepted expander support and protection of the parent cursor;
5. checks the right planter buffer lies inside the cleared corridor and the two species do not react;
6. constructs all localized interference sets and verifies the exact 18-stage `D` sequence and final `(308,69,170)` count;
7. verifies distance-two site-clock and edge-clock disjointness at shift `18`;
8. compares all three `L=9` candidates by exact rational block probability;
9. proves `b8>b7` by exact integer arithmetic and verifies the exact horizon `T8`.

## 10. Model / scheduler / denied-task status

The runtime request says GPT-6/maximum, but the actual model visible to this run is **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**. I therefore do not claim GPT-6 or maximum reasoning.

The exposed scheduled-task control schema still has fields for title/prompt/schedule/timing/enablement but no binding model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry. Thus GPT-6/maximum remains prompt text only. Enforcing it would require a platform/native scheduler control that binds those fields.

The repository reconciliation also still records the old P26 denial as authorization-context-specific: P26 was later fully updated from an authorized P/C context, while R-series edits were denied in another context. A task that still returns `You cannot modify this task` must be changed from its authorized owning context, through a supported ownership/admin transfer, or via platform support; repository edits are not a permission bypass. No scheduler changes were made in this run.

```yaml
ledger_delta:
  track: R08
  allocation: CLOSABLE_OUTSIDE
  predecessor_I0082: RETIRED_FROZEN_2_of_3_after_6_unchanged
  active_target: E0011_Durrett_Problem_5_no_stirring_catalyst
  metric_name: B_cat
  before: ">= b7"
  after: ">= b8"
  exact_movement: "b8 > b7"
  diagnostic_log10_before: -130.96747290287607
  diagnostic_log10_after: -99.23646137647626
  diagnostic_log10_gain: 31.731011526399868
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods: [3, 15, 24]
  status: PARTIAL_OPEN_CURRENT_BOUNDED
  closure_threshold: "> 63/64 plus percolation implication and p-continuity"
  next_methods: [9, 20, 28]
```
