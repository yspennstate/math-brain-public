Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; the runtime exposes no authenticated applied-model/reasoning receipt and the scheduler exposes no binding model/effort selector.

# R7-07 admission analysis — released H0008 gate and I0106 transient-tree scope

Date: 2026-09-19 UTC  
Slot: `R7-07 Hard Problem New Methods`  
Native ID: `6aabe8413f60819197825dd81ca138ae`  
Own root: `research7_2026-09-17/R7-07/`  
Run-start master: `1a783b3eb3238059a8ebc18eb766f07d59b0e204`  
Fresh prewrite master observed: `a5f112587d444e185798db147762d508dd1d9fc4`  
Target state entering this analysis: `PENDING_ADMISSION`.

This file is admission work, not a canonical claim. F0012 remains terminally handed off and is not resumed.

## 1. New shard-6 release discovered: H0008

The exact canonical ID `H0008` satisfies the R7-07 shard gate:

```text
ord('H')+ord('0')+ord('0')+ord('0')+ord('8') = 272,
272 mod 7 = 6.
```

The current canonical history file `operations/claims/H0008.md` now says:

- owner `UNASSIGNED AFTER R14 HANDOFF`;
- category `HARD OUTSIDE`;
- status `SOURCE OPEN / PARTIAL / RELEASED BY R14 AFTER SECTION-I EXHAUSTION`;
- R14 consumed both permitted stuck recoveries;
- a future reassignment must use a genuinely fresh route rather than replay the exhausted regeneration programme.

The source retained by that record is Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3 open problem (6), “Boundary fluctuations.” The source asks for the boundary fluctuation theory, including the multifractal spectrum of transmission-weighted flows and harmonic-measure/dimension-drop phenomena. R14 already saturated its finite-type multifractal interval metric but did not close the genuinely multitype harmonic-measure clause.

Fresh bounded source checking on 2026-09-19 again recovered arXiv:2608.15987v1 as the primary source and Kumar--Duddala, arXiv:2608.21125 (21 Aug 2026), as the nearby companion on front propagation/Bramson correction and the continuous-type limit theory. The companion does not advertise closure of the finite-type harmonic-exit stationary-law problem. This is bounded negative evidence, not proof of worldwide openness or novelty.

### Why R7-07 still does not acquire H0008

R7-07's owner prompt authorizes a **create-only** `operations/claims/<ID>.md` after admission and explicitly says that on a claim-path collision the worker must re-read and skip rather than overwrite. `operations/claims/H0008.md` already exists as the preserved R14 history/release record. I re-read it at the current master. Therefore R7-07 may not overwrite that canonical history file or create a shadow alias claim.

This is the same distinction recorded by neighboring terminal-admission work for released HARD sentinels: a release event is real, but release/history is not by itself an owner-authorized exclusive reassignment to another worker when that worker's acquisition rule requires a fresh canonical assignment.

**Disposition:** `H0008 = RELEASED_HARD_SHARD6_BUT_NOT_CREATE_ONLY_ACQUIRABLE_BY_R7-07`. No claim write is attempted.

If a coordinator or owner later performs an explicit canonical reassignment to R7-07, the successor must start from the R14 terminal handoff, must not inherit R14's saturated `I_mf` as a fresh metric, and must use a route genuinely different from R14's exhausted direct fixed-point/regeneration programme.

## 2. Fresh source-level analysis of I0106

`I0106` also satisfies shard 6. The intake record is:

- source id `reinforcement_matrix_2023`;
- exact locator `Open Problem 4`;
- source statement: “Extend the model to transient graphs, such as Z^d or regular trees. This could be done by putting a density of sources of food or by considering walks with a (weak) drift towards the origin, or conditioned to hit the set of sources of food.”

Primary source recovered and reread:

G. Aletti, A. Collevecchio, I. Crimaldi, M. Deijfen, S. Dereich, A. Ghiglietti, R. van der Hofstad, M. Holmes, D. Kious, V. Kleptsyn, B. Lodewijks, P. Mörters, B. Schapira, *Open Problems in Stochastic Reinforcement Models*, 2023 MATRIX–MFO workshop problems, published in the 2025 MATRIX Annals, pp. 477–498, DOI `10.1007/978-3-031-76738-8_29`; public source PDF `https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/Aletti.pdf`.

The source page was visually checked as well as text-extracted. The exact OP4 wording above appears on PDF page 2 (zero-based screenshot page 1).

Fresh 2026 follow-up screening recovered Cécile Mailler and Zoé Varin, *The two-nest ants process on triangle-series-parallel graphs*, arXiv:2601.22855 (30 Jan 2026). That paper remains a finite-graph model (two nests, one food source, triangle-series-parallel geometry); it does not provide a transient-graph OP4 extension. The original Kious--Mailler--Schapira model remains a finite-graph process. No source-matching transient-graph closure surfaced in the bounded search. Again, this is negative evidence only.

## 3. B18 — translate the conditioning suggestion into a Doob transform

The source's suggested mechanisms are not merely verbal variants. On a regular tree one can compute one of them exactly.

Let `T_d` be the infinite `d`-regular tree, `d>=3`, fix a food vertex `F`, and let `X` be simple random walk. Put

`r(x)=dist(x,F)`.

The probability that simple random walk started at `x` ever hits `F` is

`h(x)=(d-1)^(-r(x))`.

Proof: the radial distance process has probability `1/d` to step toward `F` and `(d-1)/d` to step away. The bounded solution of the harmonic recurrence with `h(0)=1` and `h(r)->0` is `(d-1)^(-r)`.

Conditioning `X` to hit `F` is the Doob `h`-transform

`P^h(x,y)=P(x,y) h(y)/h(x)`.

At distance `r>=1` there is one neighbor toward `F` and `d-1` neighbors away. Hence

- inward step probability:

  `P^h(r -> r-1) = (1/d)(d-1) = (d-1)/d`;

- probability of each outward child:

  `P^h(x -> y_out) = (1/d)(1/(d-1)) = 1/[d(d-1)]`;

- total outward probability: `1/d`.

Thus the conditioning suggestion is **exactly one particular radial-drift chain**. A generic nearest-neighbor radial drift with inward probability `q` agrees with the conditioned walk if and only if

`q=(d-1)/d`.

So “weak drift” and “conditioning to hit the food” are not one canonical model: they overlap at one parameter value in this simplest tree case and otherwise define different laws.

## 4. B27 — swapping the quantifier exposes a false notion of source closure

The broad OP4 wording can be read informally as “find some meaningful transient extension.” If that existential reading were accepted without fixing the reinforcement rule and success observable, a source-valid-looking branch can become nearly tautological.

For the two path-reinforcing variants described immediately before the source's open-problem list, take the regular tree `T_d`, fixed nest `N`, fixed food vertex `F`, and run each ant under any law conditioned to reach `F`.

### Lemma: deterministic reinforcement on a tree for the simple-path update rules

For every finite walk from `N` to `F` on a tree:

1. its chronological loop erasure is the unique simple path `[N,F]`;
2. every connected visited subgraph containing `N,F` has the same unique shortest `N-F` path `[N,F]`.

Therefore either source path-update rule — reversed loop erasure, or selecting a shortest `N-F` path inside the visited subgraph — reinforces **exactly `[N,F]` at every ant**, independently of the excursions of the conditioned walk.

Consequently, if edge weights start at `w_e(0)` and each path update adds one unit,

`w_e(k)=w_e(0)+k` for `e in [N,F]`,

and

`w_e(k)=w_e(0)` for `e notin [N,F]`.

This is a complete proof for that narrowly specified branch, but it does not close OP4. In fact it shows why simply choosing one suggested mechanism is an unsafe admission rule: one natural combination of “regular tree + conditioning” with a path-erasing update makes the extension deterministic and removes the difficult transient behavior entirely.

No novelty is claimed for this elementary observation.

## 5. B30 — isolate the genuinely nontrivial source direction

The calculation above separates three different mathematical objects hidden in OP4:

1. random food-source environments (density of sources), where the absorbing set itself is random and may be infinite;
2. a family of drifted walks, with an unspecified drift parameter/kernel;
3. conditioned walks, i.e. a Doob transform depending on the current food set and, in a weighted reinforced model, on the current conductance environment.

It also separates at least three reinforcement updates discussed in the source section: shortest-path-in-trace, loop-erased path, and full trace reinforcement. On a tree the first two collapse to deterministic geodesic reinforcement after conditioning, whereas the full-trace rule retains excursion information and is genuinely different.

Therefore OP4 does not currently supply one source-native tuple

`(transient graph class, food configuration, base walk, conditioning/drift rule, reinforcement update, success observable, quantifiers)`

from which a unique closure theorem and stable metric can be frozen. Selecting that tuple is mathematical model design by the worker, not recovery of a missing source quantifier.

**Disposition after fresh analysis:** `I0106 = SOURCE_CURRENT_IN_BOUNDED_SEARCH / MATHEMATICALLY_PROGRAMMATIC / NOT_READY_FOR_EXCLUSIVE_SOURCE_CLAIM`.

This strengthens the prior `PENDING_EXACT_EXTENSION_MODEL` diagnosis with an exact calculation: two of the source's suggested mechanisms coincide only at one special drift on a regular tree, and one path-reinforcing branch becomes deterministic. A future admission would need an explicit source/author clarification or a repository-level coordinator decision that a particular branch is the canonical residual target. R7-07 does not make that choice itself.

## 6. Other current shard-6 deltas

The current repository also contains two obvious non-I shard-6 IDs, but both are already owned:

- `MOLCHAN-2025-THETA2H`: shard 6, HARD OUTSIDE, owner `HARD7-05`;
- `P0257`: shard 6, HARD OUTSIDE, owner `proofnet24/NM13-11`.

The previous I-series screen remains in force for claimed/excluded/retired rows. No current source-clean, ownership-clear, create-only-acquirable shard-6 HARD target crossed all gates in this bounded pass.

## 7. Admission result

R7-07 remains **PENDING_ADMISSION**.

No canonical claim is created. No predecessor metric is inherited. Source-level mathematical metric remains `UNMEASURED -> UNMEASURED`, with stagnation count `NOT_STARTED` because no research target is admitted.

The next run should first check for an explicit canonical reassignment mechanism for released shard-6 H0008 or a newly populated/released shard-6 source row. It must not overwrite H0008's preserved claim history, shadow-claim it under an alias, revive F0012, or silently select one I0106 model branch as the full source question.
