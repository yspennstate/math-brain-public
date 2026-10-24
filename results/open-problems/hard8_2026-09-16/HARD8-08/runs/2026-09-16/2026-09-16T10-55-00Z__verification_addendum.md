# HARD8-08 — verification addendum for checkpoint 6

This file records exact readback receipts and the deterministic checks executed for:

- report `hard8_2026-09-16/HARD8-08/runs/2026-09-16/2026-09-16T10-41-50Z__report.md`;
- verifier `hard8_2026-09-16/HARD8-08/artifacts/2026-09-16T10-41-50Z__six_pair_scaffold_verifier.py`.

## 1. Exact-SHA readback receipts

### Mathematical report

Creation commit:
`fc67fa6b9957f20187fbf1e20ee62f6acdfe2398`

Exact-SHA readback succeeded. GitHub returned content blob:
`98201b7fc4e23c731c5292b0f99a1727f3242a0e`

Status: **VERIFIED**.

### Exact verifier artifact

Creation commit:
`88096f5c47151e8f13860f334da20f2b2ac3af07`

Exact-SHA readback succeeded. GitHub returned content blob:
`ce1c6b66306af40334a2bc17391bc5681b6720f0`

Status: **VERIFIED**.

## 2. Deterministic execution checks

The same standard-library logic archived in the verifier was executed during this run with exact integer/bitset arithmetic. No floating point, random sampling, external SAT solver, or timeout inference was used.

The completed checks were:

1. **Six-point exact geometry.** In Eisenstein coordinates, for the center plus five consecutive vertices of a regular unit hexagon, the 15 terminal pairs have squared-distance multiplicities
   
   `1 : 9`, `3 : 4`, `4 : 2`.

2. **Exact six-terminal completion.** All `2^6=64` subsets of the six non-unit terminal pairs were tested by exact graph colouring. The minimum number of added pair inequalities giving chromatic number at least six is exactly `6`, and the unique minimum choice is all six missing pairs.

3. **Seven-vertex complement criterion.** All
   
   `2^21 = 2,097,152`
   
   labelled graphs on seven vertices were checked in complement form. For every complement edge set `H`,
   
   `H has neither a matching of size 2 nor a triangle`
   
   held if and only if
   
   `H is a subgraph of a star`.
   
   This is the finite combinatorial core of the theorem `chi(G)>=6 iff complement(G)` is a star subgraph for seven-vertex `G`.

4. **Classified three-distance scaffolds.** The exact pair-count formula reproduced:
   
   - `R_6^+` with side/radius unit: `6` required pair constraints;
   - `R_6^+` with the `sqrt(3)` class unit: `9`;
   - `R_6^+` with the diameter class unit: `12`;
   - regular heptagon with any chord class unit: `10`.

5. **Six-point unit-distance upper-bound certificate.** Every labelled 10-edge graph on six vertices was examined. After excluding graphs containing `K_4` or `K_{2,3}`, exactly
   
   `72`
   
   labelled survivors remain, and every survivor has degree sequence
   
   `(5,3,3,3,3,3)`
   
   and is exactly the wheel `W_6` (a five-cycle plus a universal hub).

All executed assertions passed.

## 3. Self-contained finite proof of `u(6)=9`

The main report cited the standard exact value `u(6)=9`. The finite classification above gives a compact independent project certificate of the upper bound, modulo only elementary Euclidean facts.

Assume six planar points determine at least ten unit-distance pairs. Choose any ten of those pairs and form the corresponding abstract graph `G`.

A planar unit-distance graph cannot contain `K_4`, because four distinct points cannot be pairwise equidistant in `R^2`. It cannot contain `K_{2,3}`, because two distinct unit circles meet in at most two points, so two vertices cannot have three distinct common unit neighbours.

The exhaustive six-vertex graph check proves that every 10-edge graph avoiding those two forbidden subgraphs is `W_6`.

Suppose `W_6` had a planar unit-distance realization. Its hub is unit distance from all five rim vertices, so all five rim vertices lie on the unit circle centred at the hub. Each rim edge is also a unit chord of that unit circle. A unit chord in a circle of radius one subtends central angle `pi/3` in absolute value, because
\[
1=2\sin(\theta/2)
\]
with `0<theta<=pi`, hence `theta=pi/3`.

Traversing the five rim edges of the 5-cycle therefore changes the polar angle by five signed increments, each equal to `+pi/3` or `-pi/3`. To return to the starting point their signed sum would have to be an integer multiple of `2pi`, equivalently the sum of five signs would have to be divisible by `6`. But the sum of five numbers from `{+1,-1}` is one of
\[
-5,-3,-1,1,3,5,
\]
none divisible by six. Contradiction.

Therefore six planar points cannot determine ten unit distances, so `u(6)<=9`. The scaffold in the report has exactly nine, hence
\[
\boxed{u(6)=9}.
\]

This makes the six-gadget lower bound used in the report internally reproducible from a finite abstract-graph enumeration plus an exact elementary circle argument.

## 4. Status after verification

The strongest new certified reduction is now:

> If a finite 5-colour forced-different unit-distance gadget exists at terminal separation `sqrt(3)` and another exists at terminal separation `2`, then only **four** copies of the first and **two** copies of the second are needed to construct a finite planar unit-distance graph that is not 5-colourable.

Within the black-box pairwise-terminal architecture, six added non-unit constraints is optimal for every scaffold with at most seven marked terminals.

This is a partial structural advance only. No 5-colour forced-different gadget at either required separation was certified, so no six-chromatic finite unit-distance graph and no full solution of Hadwiger–Nelson is claimed.
