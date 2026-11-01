Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# PROB10-10 idea before code — selected physical-edge reversals inside independent antidiagonal blocks

The source metric remains the frozen one-pair defect
\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),\qquad c_*=\sup\{c\ge0:\Delta_{12}\ge c\text{ proved here}\}.
\]
The current certified source value is still `c_*=0`.  This is the third PROB10-10 run with the same source obligation, so the method must change inside FPP rather than simply increase the old oriented Bellman block size.

## New mechanism selected for this run

The preceding block compiler proved that independence comes from assigning physical edges to disjoint absolute `l1` level bands; it does **not** require paths inside a block to be monotone in `x+y`.  The previous numerical certificate nevertheless optimized only the oriented subgraph.  I now exploit that distinction.

For a finite triangular block `0<=x+y<=2m`, retain every forward nearest-neighbor traversal (increasing `x+y`) and additionally permit the reverse traversal of a specified, coordinate-swap-symmetric subset of physical edges.  The reverse traversal uses the **same Exp(1) physical-edge weight**, not an independent directed copy.  A convenient family selects a set `J` of lower `l1` levels: a physical edge joining levels `s` and `s+1` may be traversed backward exactly when `s in J`.

Let `tau_{m,J}` be the minimum passage time from the origin to level `2m` in this partially undirected block, and let the exit be `(m+D,m-D)`.  Because the allowed path family is a genuine subfamily of unrestricted undirected FPP and because different translated blocks still use disjoint physical-edge level bands, the random-endpoint compiler should give
\[
\frac{\mathbb E T(0,nm(1,1))}{nm}
\le \frac{q_{m,J}}m+\frac{2\sigma_{m,J}}{m\sqrt n},
\qquad q_{m,J}=\mathbb E\tau_{m,J},\quad \sigma^2_{m,J}=\mathbb E D^2,
\]
and hence `mu(1,1)<=q_{m,J}/m`.

The key computational point is that graph cycles do not destroy the exponential infection Bellman recursion: a state is the infected vertex set, and each transition infects one new vertex.  A physical edge with exactly one infected endpoint contributes rate one iff traversal from the infected endpoint to the uninfected endpoint is allowed.  Thus the state recursion remains a finite DAG ordered by infected-set cardinality even though admissible paths may backtrack in `l1`.

## Negation / failure tests to pay before accepting this route

1. **Double-counting an undirected edge.** A selected reversible physical edge must contribute a single Exp(1) clock when exactly one endpoint is infected; the code must never treat the two orientations as independent edges.
2. **Cross-block leakage.** A reverse traversal may lower `x+y` locally, but its physical edge still joins two consecutive levels inside the same deterministic band.  Blocks are independent only if *all* selected reverse edges have lower absolute level in that block's band.
3. **Endpoint drift.** The selected level set `J` is coordinate-swap symmetric, so reflection `x<->y` still sends `D` to `-D`; therefore `E D=0` and the final connector remains `O(sqrt n)`.
4. **Finite graph cycles.** The infection-state recursion is acyclic in the number of infected vertices.  If an implementation recurses on path position instead, it is the wrong object.
5. **Source overclaim.** Even a better diagonal upper bound is auxiliary progress until it crosses the retained sufficient threshold `0.60048`; a one-pair positive gap would itself remain only PARTIAL toward global strict convexity.

## Three materially different attacks compared

### Attack 1 — selected-reversal Bellman block (chosen)

Use a sparse symmetric set of reverse layers to capture a real undirected advantage while controlling state growth.  This is a new mechanism relative to the previous purely oriented `m=4` certificate and relative to the retired fixed-corner R08 blocks.

### Attack 2 — Busemann residual / predictable pivots (not duplicated here)

The newest complementary P20 report already proves the exact residual identity for `Delta_12` and an Exp(1) local Bellman toll, leaving a positive-density predictable-pivot geometry lemma.  Re-deriving that route would duplicate a neighboring owner.  This run therefore treats it as a comparison point only.

### Attack 3 — moving-front soft potential

One can compress an oriented infection front by the soft minimum `-(1/beta) log sum exp(-beta T_i)` and seek a uniform one-step drift inequality over all front weight vectors.  The obstruction is that a useful theorem needs a worst-case variational bound over the complete front simplex, not sampled typical fronts; preliminary algebra shows boundary-concentrated states are the dangerous configurations.  No certified all-state drift improvement is presently available, so this route is not promoted to a claim.

## Exact missing lemma targeted by the checker

For one explicit symmetric reversal set `J` at `m=4`, certify by upward-rounded integer Bellman recursion both
\[
q_{4,J}\le U/Q
\quad\text{and}\quad
\mathbb E D^2\le V/Q,
\]
with exact integers `U,V,Q`, and require `U/(4Q)` to be strictly below the preceding certified `m=4` oriented bound
\[
381370286575353/500000000000000=0.762740573150706.
\]
This would be a rigorous auxiliary improvement with explicit finite-to-infinite error.  It would not by itself move `c_*` unless the ratio is below `3753/6250=0.60048`.
