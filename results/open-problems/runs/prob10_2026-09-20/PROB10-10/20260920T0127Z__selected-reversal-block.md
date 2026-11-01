Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. SOURCE-LEVEL NO MOVEMENT: `c_*: 0 -> 0` for the third PROB10-10 run. Auxiliary rigorous diagonal upper bound improves `0.762740573150706 -> 0.758507818076` by exactly `2116377537353/500000000000000 = 0.004232755074706`.**

# PROB10-10 — selected physical-edge reversals inside independent FPP blocks

Status: **PARTIAL / OPEN**.

This run changes the block mechanism rather than merely enlarging the preceding oriented state space.  It allows a certified subset of genuine undirected backtracking moves, with each reverse move using the same physical `Exp(1)` edge as its forward move.  The resulting exact-integer Bellman calculation gives a strictly better rigorous upper bound on the diagonal time constant, with a complete finite-to-infinite error.  It still does **not** prove a positive axis/diagonal triangle defect and therefore does not prove any part of global strict convexity beyond an auxiliary directional estimate.

## 1. Frozen model and source metric

Throughout:

- graph: nearest-neighbor **undirected** `Z^2`;
- physical edge weights: iid `Exp(1)`;
- `T(x,y)`: unrestricted FPP passage time;
- `mu(v)`: the deterministic time constant in the normalization `T(0,nv)/n -> mu(v)`.

Primary source target: Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in §2.5.1 / discussion §2.8, specialized to iid `Exp(1)` on the square lattice.

Canonical repository claim:

`operations/claims/PROB10-10.md`

with source key `ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.

The frozen one-pair milestone is

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ has been rigorously proved in this track}\}.
\]

Source metric before this run: `c_*=0`.  
Source metric after this run: `c_*=0` (**no movement**).

The retained R08 axis certificate is

\[
\mu(e_1)\ge\frac{3753}{12500}=0.30024.
\tag{1.1}
\]

Thus the particular axis-plus-diagonal route would prove a positive one-pair defect if it reached

\[
\mu(1,1)<\frac{3753}{6250}=0.60048.
\tag{1.2}
\]

The newest preceding PROB10-10 report, commit
`cd705a7cbf8d0dddd2111793852929a3c906c7c0`, certified

\[
\mu(1,1)
\le
\frac{381370286575353}{500000000000000}
=0.762740573150706.
\tag{1.3}
\]

The present run improves (1.3) rigorously but remains above (1.2).

## 2. Continuity, ownership, and consumed repository state

I did not restart the old generic strict-convexity route.

The required predecessor handoff already exists and remains immutable:

- `runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`;
- creation commit `e0bb680de7150739ac0c0451f1b5f890eeb865b2`.

That handoff preserves HARD7-03's actual D0025 particle-system/four-step-atlas state.  I did not duplicate or alter it.

Consumed repository evidence in this run included:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/PROB10-10.md`;
- newest own report `runs/prob10_2026-09-20/PROB10-10/20260920T0021Z__undirected-slab-rounded-bellman.md` @ `cd705a7cbf8d0dddd2111793852929a3c906c7c0`;
- R08's initial shared-bypass/linear-saving report `runs/R08/2026-09-16T1329Z_fpp-axis-gap-a1c93e.md`;
- R08's certified axis-transition report `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`;
- R08's stuck/fixed-corner report `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- the complementary neighboring Busemann report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T00-08-24Z__busemann-residual-bellman-gap.md`.

The P20 report works on the Busemann-residual/predictable-pivot route under the same parent but explicitly as a complementary lane.  I do not duplicate its residual identity or local `Exp(1)` Bellman-gap claim here.

The canonical parent ownership remains PROB10-10.  No claim file, peer report, shared ledger, schedule, permission, email, Drive item, or public posting was modified.

## 3. Fresh source/current-literature gate

A bounded fresh search on 20 September 2026 did not find a theorem closing ordinary iid `Exp(1)` nearest-neighbor **undirected** square-lattice strict convexity.  In particular I separated the target from:

1. Auffinger--Damron--Hanson, arXiv:1511.03262, the source survey and Question 4.
2. Dembin--Elboim--Peled, arXiv:2204.02332, whose quantitative planar coalescence theorem assumes that the limit shape has more than 32 extreme points; this cannot be used to establish the missing shape property here.
3. Jacquet, arXiv:2412.20779 (30 December 2024), which proves strict unrestricted-versus-directed time-constant comparison.  That is not the required direction-to-direction strict triangle inequality.
4. Hassler, arXiv:2511.06166 (8 November 2025), on lower bounds for non-random fluctuations in planar FPP.  Its arbitrary-direction fluctuation result does not state strict convexity of the ordinary Exp(1) limit shape.
5. Basu--Sidoravicius--Sly, arXiv:2604.01214 (1 April 2026), on a rotationally invariant Riemannian FPP model, not this lattice model.
6. Bakhtin--Dow, arXiv:2406.09652, on differentiability in other continuous-action FPP models.

This is bounded negative search evidence, not a worldwide novelty certificate.  I also do **not** assert that the retained numerical axis lower bound (1.1) is best in the complete literature; R08 already labels that novelty question unverified.

No current result found in this search makes the frozen axis/diagonal defect known, so the selected directional regime remains a legitimate partial milestone.

## 4. Third unchanged source run: precise obstruction and method change

This is the third PROB10-10 execution for which the actual source defect remains

\[
\boxed{\Delta_{12}>0\quad\text{unproved}.}
\tag{4.1}
\]

The old `m=4` oriented block gives only (1.3), while the retained sufficient target is (1.2).  The exact auxiliary gap before this run was

\[
0.762740573150706-0.60048
=0.162260573150706.
\]

Blindly extending the same oriented Bellman recursion is not a satisfactory recovery: the reachable state count had already jumped to `8,289,216` at `m=4`, while the bound remained far from (1.2).

The method change in this run is therefore **not** `m=5` oriented enumeration.  It is to exploit the prior compiler's key structural observation: cross-block independence comes from disjoint *physical edge level bands*, not from monotonicity of paths inside each block.  This permits selected true undirected reversals without giving up exact dependence control.

The mathematical idea was written before the checker at

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0127Z__idea-selected-reversal-block.md`

creation commit `c0bd07e9d47058730d4a28b80c6cdf1895bc4816`.

## 5. Three materially different attacks compared

### 5.1 Selected reversible physical edges inside the block — chosen and successful at the auxiliary level

Allow all forward edges of the triangular antidiagonal block, but permit backward traversal on a small symmetric set of physical edge layers.  This keeps the same absolute-level independence between blocks while exploiting genuinely undirected paths.  The finite infection process remains exactly computable because exponential memorylessness makes the infected vertex set a Markov state even though the allowed graph now has cycles.

This is the route executed below.

### 5.2 Busemann residual/predictable pivots — promising but deliberately not duplicated

The newest P20 companion report rewrites `Delta_12/2` as the asymptotic rate of a nonnegative Busemann residual metric and proves a uniform local `Exp(1)` Bellman toll.  Its unpaid step is geometric: a positive density of predictably chosen forced departures along a residual-minimizing route.  That is materially different from finite block optimization, but another worker already owns that scoped mechanism.  Re-proving it here would violate the nonduplication requirement.

### 5.3 Stationary frontier carry instead of block reset — next recovery mechanism

The finite random-endpoint block compiler still throws away all arrival-time information except one winning exit.  A stronger route is to carry an entire bounded transverse frontier across successive independent `l1` bands.  After subtracting the minimum arrival time, the frontier differences form a Markov-additive state driven by fresh band weights.  A rigorous average-cost supersolution for this chain would avoid paying the single-point reset every `2m` levels.

This route is mathematically attractive because the current numerical obstruction is consistent with reset loss, not with the finite-to-infinite transfer itself.  The missing ingredient is a finite rigorous compression of the continuous frontier-difference state (for example interval-rounded cells plus an average-cost Bellman inequality).  No claim from this route is made in the present report.

The selected-reversal calculation is therefore both a genuine method change and a diagnostic for the next one: local backtracking helps, but the remaining `0.158...` gap is too large to justify simply adding more local reverse layers one at a time.

## 6. Partially reversible block model

Fix `m>=1`.  In relative coordinates define transient vertices

\[
V_m=\{(x,y)\in\mathbb Z_{\ge0}^2:x+y<2m\}
\]

and the absorbing top boundary

\[
H_{2m}=\{(x,y)\in\mathbb Z_{\ge0}^2:x+y=2m\}.
\]

Every nearest-neighbor physical edge in this triangle joins a lower vertex of level
`s=x+y` to an upper vertex of level `s+1`.  Give each physical edge one iid `Exp(1)` weight.

For a fixed set

\[
J\subset\{0,1,\ldots,2m-1\},
\]

allow traversal of every physical edge from its lower endpoint to its upper endpoint.  If its lower level `s` belongs to `J`, also allow traversal in the reverse direction, using the **same physical-edge weight**.  There is no independent directed copy.

Let `tau_{m,J}` be the minimum passage time from `(0,0)` to `H_{2m}` in this allowed-traversal graph.  With continuous weights the minimizing first hit of `H_{2m}` is a.s. unique.  Write the hit point as

\[
(m+D,m-D).
\]

Set

\[
q_{m,J}=\mathbb E\tau_{m,J},
\qquad
\sigma_{m,J}^2=\mathbb E D^2.
\]

For the actual certificate below,

\[
m=4,
\qquad
J=\{1,2\}.
\tag{6.1}
\]

This choice is coordinate-swap symmetric.

## 7. Complete finite-to-infinite proof for the selected-reversal block

### Proposition 7.1

For every `m`, every coordinate-swap-symmetric set `J`, and every integer `n>=1`,

\[
\boxed{
\frac{\mathbb E T(0,nm(1,1))}{nm}
\le
\frac{q_{m,J}}m
+
\frac{2\sigma_{m,J}}{m\sqrt n}.
}
\tag{7.1}
\]

Consequently

\[
\boxed{
\mu(1,1)\le\frac{q_{m,J}}m.
}
\tag{7.2}
\]

### Proof

Start from `X_0=0`.  Given an endpoint `X_k` on absolute level

\[
X_{k,1}+X_{k,2}=2mk,
\]

translate the partially reversible block by `X_k`, use fresh physical edge weights in that translated block, and take its minimum allowed path to the translated top boundary.  Denote its passage cost by `tau_k` and endpoint displacement by

\[
X_{k+1}-X_k=(m+D_k,m-D_k).
\tag{7.3}
\]

The crucial dependence point is physical-edge ownership.  Every edge used by block `k`, including every backwards traversal, is a physical nearest-neighbor edge whose lower **absolute** `l1` level lies in

\[
\{2mk,2mk+1,\ldots,2m(k+1)-1\}.
\tag{7.4}
\]

These bands are disjoint for different `k`.  The fact that a path may traverse a selected edge backward does not change which physical edge it is or which band owns it.  Since `X_k` is measurable from previous bands and the untouched edge environment in the next band is iid and translation invariant, the pairs

\[
(\tau_k,D_k)_{k\ge0}
\]

are iid copies of `(tau_{m,J},D)`.

Coordinate swap preserves both the triangular block and the rule `s in J`, and sends the unique exit displacement `D` to `-D`.  Therefore

\[
\mathbb E D=0.
\tag{7.5}
\]

Put

\[
S_n=\sum_{k=0}^{n-1}D_k.
\]

Concatenating the `n` block minimizers gives an admissible path in the true unrestricted undirected FPP environment from `0` to

\[
X_n=(nm+S_n,nm-S_n)
\]

of expected cost `n q_{m,J}`.

Connect `X_n` to `(nm,nm)` by `2|S_n|` nearest-neighbor edges alternating between levels `2nm` and `2nm+1`: if `S_n>0`, repeat north then west; if `S_n<0`, use east then south.  Every connector edge has lower absolute `l1` level `2nm`, while all block edges had lower levels at most `2nm-1`.  Thus conditional on the full block history these connector weights are fresh iid `Exp(1)`, and

\[
\mathbb E[\text{connector cost}\mid S_n]=2|S_n|.
\tag{7.6}
\]

By (7.5) and independence,

\[
\mathbb E|S_n|
\le
\sqrt{\mathbb ES_n^2}
=\sigma_{m,J}\sqrt n.
\tag{7.7}
\]

Hence

\[
\mathbb E T(0,nm(1,1))
\le
n q_{m,J}+2\sigma_{m,J}\sqrt n,
\]

which is (7.1).  Divide by `nm` and use standard `L^1` convergence to the FPP time constant (valid for Exp(1)) to obtain (7.2).  QED.

This is an **unconditional** finite-to-infinite transfer for the frozen model.  The only quantity left to certify for a concrete block is the finite pair `(q_{m,J},sigma^2_{m,J})`.

## 8. Exact Bellman recursion despite reverse traversals

The partially reversible graph has path cycles, but the infection process does not have state cycles.

At a transient infection state `S subset V_m`, enumerate each physical edge once from its lower-level endpoint `u` to its upper-level endpoint `v`.

A physical edge is a currently usable boundary edge exactly in one of these cases:

1. `u in S`, `v notin S`: forward traversal is always allowed;
2. `u notin S`, `v in S`, and the lower level of `u` belongs to `J`: selected reverse traversal is allowed;
3. `u in S` and `v in H_{2m}`: it is an absorbing target edge.

No edge is counted twice.  In particular, when both orientations are allowed they share one physical `Exp(1)` weight.

### Lemma 8.1 — infected-set Markov recursion

Conditional on the present infected set, the residual waiting times of all usable boundary physical edges are independent `Exp(1)` variables.  If `b(S)` is their number and `r_S(v)` is the number leading to a transient uninfected head `v`, then

\[
E(S)=\frac1{b(S)}+
\sum_v\frac{r_S(v)}{b(S)}E(S\cup\{v\}),
\tag{8.1}
\]

where `E(S)` is expected remaining time to hit the target boundary.

If an absorbing target edge ends at `(x,2m-x)`, put `d=x-m`.  The conditional second moment `M(S)` of the eventual exit displacement satisfies

\[
M(S)=
\frac{1}{b(S)}
\left[
\sum_{\text{absorbing target edges}} d^2
+
\sum_v r_S(v)M(S\cup\{v\})
\right].
\tag{8.2}
\]

### Proof

Whenever a usable physical edge first becomes active, its unrevealed weight is exponential.  If another infection occurs before that edge rings, conditioning on its survival only subtracts elapsed time; exponential memorylessness leaves an independent `Exp(1)` residual.  Hence at every infection epoch the usable boundary edges have independent rate-one residual clocks.  The next waiting time has mean `1/b(S)`, and each boundary physical edge is the next one with probability `1/b(S)`.  Grouping transient edges by their head gives (8.1); conditioning on whether the next edge is absorbing gives (8.2).

Every nonabsorbing transition adds one vertex to `S`.  Thus, although allowed paths can contain geometric backtracking, the recursion graph on infection states is a finite DAG ordered by `|S|`.  QED.

### Lemma 8.2 — upward integer rounding is rigorous

Fix integer scale `Q`.  Define recursively

\[
U(S)=
\left\lceil
\frac{Q+\sum_v r_S(v)U(S\cup\{v\})}{b(S)}
\right\rceil,
\tag{8.3}
\]

and

\[
V(S)=
\left\lceil
\frac{Q\sum_{\rm abs}d^2+\sum_v r_S(v)V(S\cup\{v\})}{b(S)}
\right\rceil.
\tag{8.4}
\]

Then

\[
E(S)\le U(S)/Q,
\qquad
M(S)\le V(S)/Q.
\tag{8.5}
\]

### Proof

Backward induction on the number of uninfected transient vertices.  Insert the child upper bounds into (8.1)--(8.2); every coefficient is nonnegative; the final ceiling rounds in the safe direction.  QED.

This proof is the certificate semantics implemented in the archived checker.

## 9. Concrete `m=4`, `J={1,2}` certificate

Artifacts:

- idea before code:
  `artifacts/prob10_2026-09-20/PROB10-10/20260920T0127Z__idea-selected-reversal-block.md`
  @ `c0bd07e9d47058730d4a28b80c6cdf1895bc4816`;
- checker:
  `artifacts/prob10_2026-09-20/PROB10-10/selected_reversal_m4_20260920T0127Z.cpp`
  @ `7cd19c80698a712e3a3d4fb711192095715a93c4`;
- executed output:
  `artifacts/prob10_2026-09-20/PROB10-10/selected_reversal_m4_20260920T0127Z.out`
  @ `81f7122dcd9c2b65b998310a7884d62cef497a84`.

The checker uses

\[
Q=10^{12},\qquad m=4,\qquad J=\{1,2\}.
\]

It explores exactly `13,078,872` reachable infection states and certifies

\[
q_{4,J}
\le
\frac{3034031272304}{10^{12}},
\tag{9.1}
\]

and

\[
\mathbb E D^2
\le
\frac{2349351617189}{10^{12}}.
\tag{9.2}
\]

Therefore Proposition 7.1 gives the explicit finite-`n` inequality

\[
\boxed{
\frac{\mathbb E T(0,4n(1,1))}{4n}
\le
\frac{189626954519}{250000000000}
+
\frac{1}{2\sqrt n}
\sqrt{\frac{2349351617189}{10^{12}}}.
}
\tag{9.3}
\]

The asymptotic consequence is

\[
\boxed{
\mu(1,1)
\le
\frac{189626954519}{250000000000}
=0.758507818076.
}
\tag{9.4}
\]

The finite-to-infinite error coefficient is explicitly

\[
\frac12\sqrt{\frac{2349351617189}{10^{12}}}
=0.766379738965775\ldots .
\tag{9.5}
\]

No convergence-rate hypothesis, KPZ exponent, sampled curvature, or simulation enters (9.3)--(9.4).

### Exact auxiliary improvement

Subtracting the new rational upper certificate from the previous one gives

\[
\frac{381370286575353}{500000000000000}
-
\frac{189626954519}{250000000000}
=
\boxed{\frac{2116377537353}{500000000000000}}
=0.004232755074706.
\tag{9.6}
\]

Thus the repository's rigorous diagonal upper bound improves strictly:

`0.762740573150706 -> 0.758507818076`.

The endpoint-variance correction coefficient is slightly worse than the preceding oriented block's `0.7584369582...`; this is reported rather than hidden.  The asymptotic constant nevertheless improves by the exact amount (9.6).

## 10. Negation checks and implementation failure modes

The idea-before-code artifact listed five checks; all are paid explicitly here.

### 10.1 No independent reverse-edge copy

The checker enumerates each physical edge exactly once.  If both directions are permitted, the edge contributes one rate-one clock according to which endpoint is infected.  It is never replaced by two exponential variables.

### 10.2 Reverse traversal does not leak across blocks

Block ownership is by the lower absolute `l1` level of the physical edge, equation (7.4).  Traversal orientation does not change that ownership.

### 10.3 No endpoint linear drift

`J={1,2}` depends only on `x+y` and is invariant under coordinate swap.  Hence `D` is symmetric and `ED=0` exactly.

### 10.4 Geometric graph cycles do not create Bellman cycles

Every infection transition adds one transient vertex.  The dynamic program is acyclic in infected-set inclusion, which is why the upward induction is valid.

### 10.5 The checker does not silently cross the source threshold

It includes an exact cross-multiplication test that the new ratio is strictly below the prior certified ratio, and a guard confirming it remains **above** `3753/6250`.  The output ends

`ALL_EXACT_INTEGER_CHECKS_PASS = True`.

An exploratory attempt to add another reversible layer caused the enlarged state recursion not to finish within the bounded local execution window.  No value from that timed-out run is preserved or used.  This is evidence of computational state growth only, not a theorem that additional reverse layers fail mathematically.

## 11. Source-level before/after versus auxiliary progress

### Source-level metric

Frozen source quantity:

\[
c_* = \sup\{c\ge0:2\mu(e_1)-\mu(1,1)\ge c\text{ proved}\}.
\]

Before: `0`.  
After: `0`.  
Change: **none**.

Direction range of proved strict curvature/triangle defect: **empty**.  The run proves no positive strict-triangle defect in any direction and therefore certainly not global strict convexity.

### Auxiliary source-relevant quantity

Rigorous diagonal upper bound:

\[
0.762740573150706
\longrightarrow
0.758507818076.
\]

Exact improvement: (9.6).

The remaining distance from this particular certificate to the retained sufficient threshold (1.2) is

\[
\frac{189626954519}{250000000000}-\frac{3753}{6250}
=
\boxed{\frac{39506954519}{250000000000}}
=0.158027818076.
\tag{11.1}
\]

This `0.158...` is **not** a certified lower bound on the true triangle defect or on any impossibility.  It is only the remaining gap in this sufficient axis-lower/diagonal-upper proof route.

## 12. What this run teaches and the next nonduplicating route

The selected reversals show rigorously that one can exploit true undirected backtracking while preserving exact block independence and a complete finite-size correction.  However, the improvement is only about `0.00423`, whereas the current sufficient-target gap remains about `0.15803`.  Combined with the state-count increase from the preceding `8,289,216` oriented states to `13,078,872` states here, this makes repeated local layer additions a poor next move.

The most plausible different next mechanism within PROB10-10 is the **stationary frontier-carry compiler** from §5.3:

1. fix a finite transverse strip and retain all arrival labels on its active top frontier;
2. normalize by subtracting the minimum label, turning the process into an additive cost plus a frontier-difference state;
3. expose one fresh absolute level band at a time, giving an exact Markov-additive recursion with no cross-band dependence;
4. construct a finite interval-rounded supersolution to the average-cost Bellman equation;
5. convert its certified average drift directly to an upper bound for `mu(1,1)`, with an explicit truncation/rounding error.

This attacks the reset loss rather than simply increasing block size.  It is distinct from P20's Busemann-pivot geometry and from the retired R08 local-surgery/fixed-corner route.

## 13. Validation and closure state

Actual executed finite test: the archived `m=4`, `J={1,2}`, `Q=10^12` exact-integer upward-rounding checker.  It terminates with

`ALL_EXACT_INTEGER_CHECKS_PASS = True`.

This is a **self-check**, not an independent audit.  No external-track audit of the new selected-reversal theorem/certificate is recorded in this run.

Accordingly:

- source target: **OPEN**;
- present contribution: **PARTIAL auxiliary progress**;
- global strict convexity: **not proved**;
- one-pair defect `Delta_12>0`: **not proved**;
- source closure: **not claimed**;
- novelty of the numerical diagonal constant relative to all literature: **not claimed**.

The complete remaining full-scope gap is still to obtain positive strict support separation for every distinct boundary direction of the iid Exp(1) limit shape (or an equivalent full strict-convexity theorem), with current literature/prior-art verification and the repository's required independent validation.
