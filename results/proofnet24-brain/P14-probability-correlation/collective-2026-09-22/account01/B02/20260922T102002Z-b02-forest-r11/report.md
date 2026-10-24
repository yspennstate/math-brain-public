# FOREST B02 — fixed-fiber switching obstruction

Run: `20260922T102002Z-b02-forest-r11`  
Outcome: `CANDIDATE_REFUTED`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Parent FOREST target: **OPEN**.

## Scope consumed

Fresh controls were resolved at main commit `3d6b8e61a8615ae7036382df2fbb6f3cfdbdbea2`, control revision `2026-09-22.2`; the collective FOREST reallocation remains controlling and installation/benchmark work was not resumed.

Essential scientific context used:

1. Lead line: the current source-safe program localizes hard contraction/conditioning behavior and asks for a genuine multiplicity-controlled switching rather than a formal local swap.
2. Named OTHER-account result applied: account02/B03, run `20260922T094532Z-b03-forest-auto11`, handoff `FOREST-HANDOFF-account02-B03-20260922T094532Z-r11.md`. It proves every exact simple-unit two-terminal response-2 network needs at least 7 edges and 5 vertices; hence local exact STAR-2 unitization cannot preserve edge-minimality. This run combines that no-go with a second, independent no-go below: a pair injection cannot stay inside fixed union/intersection fibers either.

## Conditional switching formulation

Let `g=uv` be an edge and put `H=G-g`. Deletion of `g` is a bijection

`{F forest in G : g in F} -> {A forest in H : u and v disconnected in A}`,

by `F |-> F-g`, with inverse `A |-> A+g`. The inverse is acyclic because `u,v` lie in different components of `A`.

Fix distinct marked edges `e,f` of `H`. Let `D_ij` be the number of `u-v`-disconnected forests with indicator pair `(1_e,1_f)=(i,j)`. The conditional Rayleigh gap is

`Delta_D = D_10 D_01 - D_00 D_11`.

A direct pair-injection proof would inject

`D_00 x D_11 -> D_10 x D_01`.

A particularly natural class of switchings preserves, for an ordered forest pair `(A,B)`, both

`I=A intersect B` and `U=A union B`.

Such a map would act independently inside every `(I,U)` fiber. The result below proves that this entire mechanism is impossible, even on a tiny genuine graphic instance.

## Theorem: fixed `(intersection,union)` injection is impossible

There is a finite simple graph and marked edges for which the global Rayleigh gap is positive but one exact pair fiber has strictly more source pairs than target pairs. Therefore no injection from `D_00 x D_11` to `D_10 x D_01` can preserve both pair intersection and pair union.

### Core K4 obstruction

Take `K4` with opposite marked edges `e=01` and `f=23`. The numbers of forests in marker classes `(00,01,10,11)` are

`(15,9,9,5)`,

so the global Rayleigh gap is

`9*9 - 15*5 = 6 > 0`.

Now restrict pair counting to the fiber

`I=empty`, `U=E(K4)`.

In this fiber each ordered pair `(A,B)` consists of complementary spanning trees. There are 12 feasible colorings: the 16 spanning trees of `K4` minus the 4 stars, because the complement of a star is a triangle and hence not a forest. Classifying the 12 path trees by whether the red tree `A` contains the two opposite marked edges gives

`N_00=4, N_10=2, N_01=2, N_11=4`.

For the desired orientation, the source fiber (`A` has neither mark, `B` has both) therefore has size **4**, while the target fiber (`A` has `e` only, `B` has `f` only) has size **2**.

Hence a union/intersection-preserving injection is impossible by pigeonhole, despite the positive total gap.

The full signed fiber decomposition is also exact: the complete-edge/empty-intersection fiber contributes `-2`; eight other fibers contribute `+1` each; all remaining fibers contribute zero. Thus

`Delta = -2 + 8 = 6`.

This explicitly demonstrates that the proof must transport mass between different pair fibers.

## Source-valid connected conditional witness

To remove the objection that the preceding K4 can be embedded with a vacuous disconnection condition, take the connected simple graph `H` on vertices `0,...,5` with

`E(H)={02,03,04,15,23,25,35}`,

terminals `u=0`, `v=1`, and marks

`e=02`, `f=35`.

The terminals have no common neighbor, so identifying `0` and `1` creates no parallel edge. Exact enumeration of `u-v`-disconnected forests gives marker counts

`(D_00,D_01,D_10,D_11)=(30,18,18,10)`,

and therefore

`Delta_D = 18*18 - 30*10 = 24 > 0`.

Consider the fiber with empty intersection and union

`U={02,03,15,23,25,35}=E(H)-{04}`.

After identifying `0~1`, this union is exactly a `K4` on the four vertices `{0~1,2,3,5}`. Consequently the same exact deficit occurs:

`source fiber size = 4`, `target fiber size = 2`.

An explicit source pair is

`A={03,15,23}`,

`B={02,25,35}`.

Both are acyclic; `0` and `1` are disconnected in both; `A` contains neither mark; `B` contains both marks; their intersection is empty and their union is the displayed six-edge fiber.

Adding `g=01` gives an actual simple parent graph

`G=H+01`.

For the unconditioned forest law on this parent, the marker counts are `(62,42,42,26)` and the Rayleigh gap is `42^2-62*26=152>0`. Thus the obstruction is source-valid inside the exact contraction/conditioning geometry of a simple parent; it is not an abstract non-graphic count table.

## Multiplicity consequence

The standard one-edge symmetric exchange remains valid as an existence primitive: when `A+e` creates a unique cycle, deleting a cycle edge can restore acyclicity, and deleting `e` from `B` cannot create a cycle. But the K4 fiber proves that no deterministic refinement that always preserves the pair multiplicity profile (`A intersect B`, `A union B`) can be globally injective. The failure is cardinal, not a tie-breaking defect.

Therefore any successful pair injection/signed switching must deliberately change at least one unmarked edge's pair multiplicity: it must move to a different `(I,U)` fiber. Equivalently, one must create/delete an overlap or a gap and then charge the resulting cross-fiber multiplicity.

## Application of account02/B03 result

Account02/B03 (`20260922T094532Z-b03-forest-auto11`) independently proves that exact local two-terminal unitization of a doubled edge needs at least seven unit edges, so a local STAR-2 gadget cannot close an edge-minimal argument. The present theorem rules out the other natural locality principle: keeping the two-forest union/intersection fixed.

Combined conclusion:

**the next viable mechanism must be both parent-specific and cross-fiber.**

It cannot be (i) a universal local terminal replacement, nor (ii) a union/intersection-preserving recoloring of a forest pair.

## First essential missing implication

Construct a bounded-multiplicity cross-fiber map or signed charge

`Phi: D_00 x D_11 -> D_10 x D_01`

for the lead's relevant minimal-parent class, where `Phi` is explicitly allowed to change `I=A intersect B` and/or `U=A union B`. The accounting must show that every deficit fiber is paid by surplus fibers, with the K4 pattern (`-2` paid by eight `+1` fibers) as the smallest exact test case.

A promising normalization is to charge by the first edge whose pair multiplicity changes along the unique fundamental cycle/cut certificate, rather than requiring a symmetric exchange that returns the displaced edge to the other forest. The reverse map must reconstruct that certificate, which is exactly the unresolved multiplicity issue.

## Computation

`fiber_counterexample_check.py` was executed in the native runtime. It verifies exactly:

- K4 counts `(15,9,9,5)`, global gap `6`, bad full fiber `4` versus `2`;
- signed fiber distribution: one `-2` deficit and eight `+1` surpluses;
- connected conditional witness counts `(30,18,18,10)`, gap `24`, bad fiber `4` versus `2`;
- the explicit source pair's acyclicity and terminal disconnection;
- parent counts `(62,42,42,26)`, gap `152`.

Output terminates `STATUS=PASS`.

A separate exhaustive search performed during the run found no fixed-fiber deficit for the analogous `u-v` conditional search on graphs through five vertices; on six vertices, no deficit occurs with fewer than six edges in the unrestricted search, while the connected/no-common-neighbor class first exhibits the seven-edge witness above among edge counts below seven. These finite-minimality observations are auxiliary only; the explicit exact witness is the theorem-level obstruction.

## Status

`CANDIDATE_REFUTED`: the candidate class of union/intersection-preserving forest-pair injections is impossible. This does **not** refute FOREST; the parent conjecture remains open.
