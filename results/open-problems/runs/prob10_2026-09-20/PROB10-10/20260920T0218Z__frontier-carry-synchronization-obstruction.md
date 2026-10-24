Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. SOURCE-LEVEL NO MOVEMENT: `c_*: 0 -> 0`. Three materially different attacks this run were (i) a synchronized contiguous-frontier slab compiler, which yields an exact harmonic synchronization obstruction; (ii) the genuinely different asynchronous-frontier average-cost Bellman route, for which the exact missing inequality is isolated below; and (iii) a longer-memory simple-path dual, which improves the track-certified auxiliary axis bound `0.30024 -> 0.3002823` but does not prove strict convexity.**

# PROB10-10 — frontier carry, an exact synchronization obstruction, and a stronger axis ingredient

Status: **PARTIAL / OPEN**.

## 1. Frozen source problem and metric

The model is unchanged:

- nearest-neighbor **undirected** first-passage percolation on `Z^2`;
- one iid `Exp(1)` weight on each physical edge;
- `T(x,y)` is unrestricted passage time;
- `mu(v)` is the deterministic time constant in the normalization `T(0,nv)/n -> mu(v)`.

The external target is Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4, specialized to this Exp(1) square-lattice case: prove strict convexity of the whole deterministic limit shape.

The canonical repository claim is `operations/claims/PROB10-10.md`, source key `ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.

The frozen first directional milestone remains

\[
\Delta_{12}:=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ is rigorously proved in this track}\}.
\]

Before this run: `c_*=0`.  
After this run: `c_*=0` (**no source-level movement**).

The newest preceding PROB10-10 report proved the auxiliary diagonal estimate

\[
\mu(1,1)\le 0.758507818076.
\tag{1.1}
\]

The retained R08 axis certificate was

\[
\mu(e_1)\ge 0.30024.
\tag{1.2}
\]

This run improves only the *track-certified auxiliary* version of (1.2):

\[
\boxed{\mu(e_1)\ge \frac{3002823}{10^7}=0.3002823.}
\tag{1.3}
\]

Thus the sufficient diagonal threshold moves

\[
0.60048\longrightarrow
\boxed{\frac{3002823}{5\cdot10^6}=0.6005646},
\tag{1.4}
\]

an auxiliary gain of `0.0000846`.  The current certified diagonal upper bound (1.1) is still larger by

\[
0.758507818076-0.6005646=0.157943218076,
\]

so (1.3) does **not** prove `Delta_12>0`.

I do not claim (1.3) is the best lower bound in the external literature. Alm--Parviainen (2002) explicitly developed transition-matrix lower bounds and numerical results for the exponential law; the primary numerical table was not established as dominated by (1.3) in this bounded run. The only claim here is the exact repository certificate and the resulting updated sufficient threshold within this track.

## 2. Continuity, ownership, and consumed state

I did not restart the retired generic strict-convexity route.

The required HARD7-03 predecessor handoff already exists and remains immutable:

- `runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`, creation commit `e0bb680de7150739ac0c0451f1b5f890eeb865b2`.

It preserves HARD7-03's actual D0025 particle-system/four-step-atlas state. No duplicate handoff was created.

Consumed repository state included:

- `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest own report `runs/prob10_2026-09-20/PROB10-10/20260920T0127Z__selected-reversal-block.md`, previous report commit `c28e5fa02fb9b6f010adf2f43652408d03567984`;
- R08 axis report `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md` and the R08 failures preserved by the canonical claim;
- newest complementary P20 report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T01-48-00Z__sharp-bellman-gap-concentration.md`, blob `1e93d8ff66f3f62134fe37c6c19565cc344b5185`.

The P20 report sharpens its local Exp(1) Bellman toll to `1/3`, proves a unique calibrated Busemann successor at each fixed vertex under the reconstructed weak limit, and leaves the geometric positive-density predictable-pivot step unpaid. That is a complementary Busemann lane; I did not duplicate its theorem.

The preceding PROB10-10 run was already the third source-unchanged run and changed from the oriented point-to-line recursion to selected true physical-edge reversals. This run changes mechanism again: it asks what information a block compiler must carry across boundaries, rather than adding another local reversal layer.

## 3. Fresh source/literature boundary

A bounded fresh search on 20 September 2026 again found no theorem closing ordinary iid Exp(1), nearest-neighbor, undirected `Z^2` strict convexity.

Relevant distinctions checked:

1. Auffinger--Damron--Hanson, arXiv:1511.03262 remains the source navigation for the strict-convexity question.
2. Dembin--Elboim--Peled, *Coalescence of Geodesics and the BKS Midpoint Problem in Planar First-Passage Percolation* (GAFA 2024), use a nontrivial limit-shape extreme-point hypothesis in their quantitative coalescence theorem; this cannot be used to manufacture the missing shape property here.
3. Jacquet's strict unrestricted-versus-directed passage comparison (arXiv:2412.20779) is not a direction-to-direction strict triangle inequality. It would only help the present numerical route if one also had a rigorous directed diagonal upper bound below the threshold (1.4); no such bound was verified in this run.
4. Haßler's 2026 *Classification of the limit shape for 1+1-dimensional FPP* concerns a simplified model with deterministic vertical-edge weights, not the present iid undirected lattice model.
5. Marivain's 2026 Brochette FPP has weights correlated along a line and obtains an `L^1` diamond in that different model; it is not a counterexample or solution here.
6. Alm--Parviainen, *Lower and Upper Bounds for the Time Constant of First-Passage Percolation* (CPC 2002, DOI 10.1017/S0963548302005266), is directly relevant prior art for transition-matrix axis bounds. Therefore no novelty claim is made for the auxiliary mechanism in Section 7.

This is bounded current-status evidence, not a worldwide novelty certificate.

## 4. New idea before code

The idea was written before the checker in

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0218Z__idea-frontier-carry-and-axis-dual.md`

at creation commit

`8f9f6beb85fbbc27be8d9615cd4683c870ec1898`.

The central question is whether the previous point-to-line compiler is losing too much by throwing away all but one endpoint after each block. The first exact test is deliberately stronger than needed: carry `k` consecutive frontier vertices, but synchronize their available arrival time before exposing the next fresh antidiagonal band. The calculation below shows exactly why this still fails: synchronization itself has a harmonic toll. That identifies the arrival-label *differences* as the state that a successful block method must preserve.

## 5. Exact one-level synchronization obstruction

Use rotated coordinates

\[
s=x+y,\qquad d=x-y.
\]

Suppose `k` consecutive vertices on one antidiagonal `H_s={x+y=s}` have all been reached by a common budget time `t`. Expose only the fresh oriented edges from `H_s` to `H_{s+1}`. There are `k+1` possible child vertices.

Let `Y_0,Y_k` be the arrival increments of the two boundary children. Each has only one parent, so

\[
Y_0,Y_k\stackrel{\rm iid}{\sim}{\rm Exp}(1).
\]

Each of the `k-1` interior children has two distinct incoming physical edges, so its increment is the minimum of two iid `Exp(1)` variables. Thus

\[
Y_1,\ldots,Y_{k-1}\stackrel{\rm iid}{\sim}{\rm Exp}(2).
\]

All `Y_i` are mutually independent because the incoming edge sets of distinct children are disjoint.

There are exactly two consecutive `k`-windows among the `k+1` children. The first time at which at least one complete `k`-window is available is

\[
\begin{aligned}
C_k
&=\min\left\{\max(Y_0,\ldots,Y_{k-1}),
                 \max(Y_1,\ldots,Y_k)\right\}\\
&=\max\left\{Y_1,\ldots,Y_{k-1},\min(Y_0,Y_k)\right\}.
\end{aligned}
\tag{5.1}
\]

But `min(Y_0,Y_k)~Exp(2)` and is independent of the interior variables. Therefore `C_k` is the maximum of `k` iid rate-two exponentials. Hence

\[
\boxed{\mathbb E C_k=\frac{H_k}{2},}
\qquad H_k=\sum_{j=1}^k\frac1j.
\tag{5.2}
\]

This is not simulation. It is the exact optimal one-antidiagonal completion time for the synchronized-contiguous-frontier criterion.

**Consequence.** A compiler that discards all relative arrival labels and resynchronizes a `k`-frontier after every antidiagonal has diagonal cost bound `H_k`, which is at least `1` and grows with `k`. Thus simply widening a synchronized endpoint set cannot repair the old single-endpoint reset loss. The state that must survive from one band to the next is the vector of *relative arrival times*.

The exact checker independently confirms (5.2) for `k=2,3`:

\[
q_{2,1}=\frac34=\frac{H_2}{2},
\qquad
q_{3,1}=\frac{11}{12}=\frac{H_3}{2}.
\]

## 6. A rigorous `r`-level synchronized-frontier compiler with explicit finite-to-infinite error

The one-level obstruction does not make the frontier idea useless. It says exactly which compression is too aggressive. The following theorem is a new dependence-controlled compiler that can test multi-level synchronization without confusing finite evidence with an asymptotic statement.

Fix odd `k>=1` and `r>=1`. Start from `k` consecutive centered seeds on `H_0`, all with common budget time zero. In the finite oriented slab of levels `0,1,...,r`, let

\[
Q_{k,r}:=\inf\{t:\text{some }k\text{ consecutive vertices of }H_r
\text{ all have passage time }\le t\}.
\tag{6.1}
\]

If more than one terminal `k`-window is completed at the minimizing event, choose among them with an independent reflection-symmetric tie-breaker. Let `D_{k,r}` be the lateral `d`-coordinate shift of the center of the selected terminal window from the initial center. Then

\[
|D_{k,r}|\le r,
\qquad
\mathbb E D_{k,r}=0.
\tag{6.2}
\]

### Proposition 6.1

Let `q_{k,r}=E Q_{k,r}`. For every `N` with `Nr` even,

\[
\boxed{
\frac{\mathbb E T\!\left(0,(Nr/2,Nr/2)\right)}{Nr/2}
\le
\frac{2q_{k,r}}r
+\frac{2}{\sqrt N}
+\frac{4(k-1)}{Nr}.
}
\tag{6.3}
\]

Consequently

\[
\boxed{\mu(1,1)\le \frac{2q_{k,r}}r.}
\tag{6.4}
\]

### Proof

Connect the origin to the `k` centered seeds of `H_0` by a fixed finite tree running outward along the antidiagonal using two lattice edges per adjacent seed. The union contains at most `2(k-1)` physical edges. If `A_k` is the sum of their weights, then every seed is reached by time at most `A_k` and

\[
\mathbb E A_k\le 2(k-1).
\tag{6.5}
\]

Now run the finite slab experiment (6.1) from this synchronized budget. Having selected a terminal `k`-window, translate the same experiment to that window and the next `r` antidiagonal levels. Block `j` only inspects physical oriented edges whose lower absolute `s`-level lies in

\[
\{jr,jr+1,\ldots,(j+1)r-1\}.
\tag{6.6}
\]

These physical edge sets are disjoint between blocks. Translation invariance and the independent symmetric tie-breakers therefore make the pairs

\[
(Q_j,D_j)_{j=1}^N
\]

iid copies of `(Q_{k,r},D_{k,r})`. Waiting until all vertices in the chosen terminal window are available can only increase their individual true arrival labels, so the common-budget concatenation is a legitimate upper-bound construction even though it discards within-window label advantages.

After `N` blocks, the center of the selected frontier lies on `H_{Nr}` with lateral displacement

\[
S_N=\sum_{j=1}^N D_j.
\]

By (6.2),

\[
\mathbb E|S_N|
\le\sqrt{\mathbb E S_N^2}
\le r\sqrt N.
\tag{6.7}
\]

The center vertex itself is reached by the common budget

\[
A_k+\sum_{j=1}^N Q_j.
\]

Connect that center to `(Nr/2,Nr/2)` by alternating one step from level `Nr` to `Nr+1` and one step back to `Nr`, in the sign needed to reduce `d`. This uses exactly `|S_N|` edges. Every connector edge has lower absolute `s`-level `Nr`, whereas the block construction only exposed lower levels through `Nr-1`. Hence the connector weights are fresh iid `Exp(1)` conditional on the entire block history, and its conditional expected cost is `|S_N|`.

Therefore

\[
\mathbb E T\!\left(0,(Nr/2,Nr/2)\right)
\le 2(k-1)+Nq_{k,r}+r\sqrt N.
\tag{6.8}
\]

Divide by `Nr/2` to obtain (6.3). Let `N->infinity` through values with `Nr` even and use the standard `L^1` time-constant convergence for Exp(1) FPP to obtain (6.4). QED.

### Exact small-slab negation test

The CTMC recursion in the artifact gives, with exact rational arithmetic,

\[
\begin{array}{c|c|c|c}
(k,r)&q_{k,r}&2q_{k,r}/r&\text{exact CTMC states}\\ \hline
(2,1)&3/4&3/2&8\\
(2,2)&240439/216000&240439/216000&59\\
(2,3)&5687268454443679/3920736960000000&
5687268454443679/5881105440000000&570\\
(3,1)&11/12&11/6&16\\
(3,2)&2617979177/1944810000&2617979177/1944810000&217.
\end{array}
\]

The best displayed synchronized certificate is still about `0.967040722610081`, far worse than (1.1). This is useful negative information: **the multi-frontier idea only becomes plausible if it preserves asynchronous labels rather than synchronizing them.** No finite-size fit is promoted to an asymptotic improvement.

## 7. Auxiliary theorem: a longer-memory exact axis lower bound

This is a separate auxiliary attack, not the method change responsible for Section 5--6.

### Proposition 7.1

For ordinary iid Exp(1) FPP on `Z^2`,

\[
\boxed{\mu(e_1)\ge c_0:=\frac{3002823}{10^7}=0.3002823.}
\tag{7.1}
\]

### Proof

A state is a locally self-avoiding path consisting of `L=10` remembered vertices (nine steps), translated so its current endpoint is the origin. A transition appends one nearest-neighbor step only when the new endpoint is different from all ten currently remembered vertices, then drops the oldest vertex and translates again. Every globally simple lattice path is accepted by this automaton.

Exact enumeration gives

\[
16268\ \text{states},\qquad 44100\ \text{transitions}.
\tag{7.2}
\]

Set

\[
z=\frac{1583}{500}=3.166.
\]

Weight a transition by `z^{Delta x}`, where `Delta x` is its horizontal displacement, and let `M(z)` be the resulting nonnegative rational transfer matrix. The checker first searches numerically for a positive Collatz witness `V`, but then verifies every matrix inequality using exact `Fraction` arithmetic. Its archived successful run gives

\[
M(z)V\le R V\quad\text{coordinatewise},
\tag{7.3}
\]

with

\[
R=
\frac{6329656083737289707}{1308334099314438500}
=4.837950862133765\ldots.
\tag{7.4}
\]

Let `N_{m,n}` be the number of globally simple `m`-edge paths from `0` to `ne_1`. The finitely many initial nine-step states contribute only a constant `C<infinity`. Since every such path is accepted and has tilt weight `z^n`, (7.3) implies

\[
N_{m,n}\le C z^{-n}R^{m-9},\qquad m\ge9.
\tag{7.5}
\]

For a fixed simple `m`-edge path its passage time is `Gamma(m,1)`. For `s>0`,

\[
\mathbb P\{\Gamma(m,1)\le c_0 n\}
\le e^{s c_0n}(1+s)^{-m}.
\tag{7.6}
\]

Choose the exact rational

\[
y:=1+s=\frac{2418975431067}{500000000000}
>R.
\tag{7.7}
\]

Every positive-weight geodesic is simple, so a union bound over all lengths `m>=n` gives

\[
\begin{aligned}
\mathbb P\{T(0,ne_1)\le c_0n\}
&\le C R^{-9}z^{-n}e^{(y-1)c_0n}
\sum_{m\ge n}(R/y)^m\\
&=\frac{CR^{-9}}{1-R/y}
\left[
\frac{R e^{(y-1)c_0}}{yz}
\right]^n.
\end{aligned}
\tag{7.8}
\]

The only transcendental comparison in (7.8) is certified without floating point. Put `x=(y-1)c_0`. The checker uses

\[
e^x\le
\sum_{j=0}^{14}\frac{x^j}{j!}
+\frac{x^{15}/15!}{1-x/16},
\tag{7.9}
\]

because all subsequent Taylor-term ratios are at most `x/16<1`. Substitution of the exact rationals (7.4), (7.7), and (7.9) gives an exact rational geometric base `B_exact<1`; the archived output records

\[
B_{\rm exact}=0.999999750709743\ldots<1,
\tag{7.10}
\]

with exact numerator and denominator and a positive margin about `2.4929e-7`.

Thus the right side of (7.8) is summable in `n`. Borel--Cantelli gives

\[
\liminf_{n\to\infty}\frac{T(0,ne_1)}n\ge c_0\quad\text{a.s.},
\]

and the standard time-constant limit proves (7.1). QED.

Again, this is a **track-certified auxiliary theorem**. The mechanism is related to published transition-matrix methods, so no external novelty claim is made from the bounded search.

## 8. The exact next missing lemma — asynchronous frontier, not another synchronized block

The synchronization calculation identifies a sharper target for a genuinely new block method.

Fix a finite transverse frontier width and retain its vector of arrival labels, normalized by subtracting its minimum. Let `h` denote this relative-label state. Exposing a fresh physical edge band gives

\[
(h,E)\mapsto (G(h,E),\Phi(h,E)),
\]

where `G` is the increment of the minimum budget and `Phi` is the next normalized frontier. The update may include a controlled finite family of genuine undirected within-band reversals, provided physical edge ownership remains by disjoint absolute `l1` bands as in the preceding report.

A complete average-cost certificate sufficient for the one-pair strict gap would be:

> Construct a policy, a bounded-below potential `V` on a rigorously covered frontier-state space, and a rational
> \[
> a<\frac{3002823}{10^7}
> \tag{8.1}
> \]
> such that for every admissible state `h`,
> \[
> \boxed{
> \mathbb E\bigl[G(h,E)+V(\Phi(h,E))\bigr]
> \le a+V(h).
> }
> \tag{8.2}
> \]
> The state compression, if finite, must round in the direction that preserves (8.2) for **all** continuous label vectors in each cell.

Summing (8.2) over fresh bands telescopes the potential and yields asymptotic diagonal cost at most `2a`; combining with (7.1) gives

\[
\Delta_{12}
\ge 2\left(\frac{3002823}{10^7}-a\right)>0.
\tag{8.3}
\]

This is the first point in the current block line where the target is an exact source-relevant positive defect rather than “make a finite block a bit smaller.” It also explains why an oriented-only frontier may be insufficient: the current proof needs the certified average cost per antidiagonal level to cross `0.3002823`; selected undirected reversals are available within the same physical-band independence framework.

No such `V,a` certificate is claimed this run. The unresolved issue is a rigorous finite compression of the continuous, unbounded relative-label state with controlled rounding error.

## 9. Three attacks and what happened

### Attack A — synchronized contiguous-frontier carry

**Result:** mathematically complete, but quantitatively negative. Proposition 6.1 gives an unconditional finite-to-infinite transfer with explicit `2/sqrt(N)` plus startup error; (5.2) proves the one-level harmonic synchronization toll exactly; small exact slabs remain far above the needed diagonal threshold.

**Lesson:** endpoint-set width is not the missing state variable. Relative arrival labels are.

### Attack B — asynchronous frontier / average-cost Bellman

**Result:** no theorem yet, but the unpaid obligation is now the precise inequality (8.2), with a numerical-free crossing target (8.1). This is materially different from the old fixed-corner, point-to-line, and selected-reversal finite-block resets because it carries the full local timing state between bands.

**Failure mode found:** a naive finite state consisting only of the infected/available frontier set is invalid; two configurations with the same set but different arrival-label gaps have different next-band laws and costs. Any checker that forgets those label gaps would not certify the continuous model.

### Attack C — longer-memory axis dual

**Result:** exact auxiliary success, Proposition 7.1. It improves the track's retained axis ingredient from `0.30024` to `0.3002823`, thereby raising the diagonal crossing target to `0.6005646`.

**Qualification:** this is in the same broad transition-matrix family as Alm--Parviainen/R08 and is not claimed externally novel. It is auxiliary movement, not source-level movement.

A fourth natural bridge, Jacquet's unrestricted-versus-directed strict inequality, was checked but does not by itself furnish the needed direction-to-direction defect. P20's Busemann/predictable-pivot route was also read but deliberately not duplicated.

## 10. Exact tests and artifacts

The checker is

`artifacts/prob10_2026-09-20/PROB10-10/prob10_fpp_frontier_axis_exact_20260920T0218Z.py`

creation commit

`4aec072073c82360dc466d55098f0c3121cdaf6f`.

It was executed in this run. The archived stdout is

`artifacts/prob10_2026-09-20/PROB10-10/prob10_fpp_frontier_axis_exact_20260920T0218Z.out`

creation commit

`a08c9a250d203dbbe0dd1f81e6a2c5099c804308`.

The run ends

`ALL_EXACT_CHECKS_PASS = True`.

The code uses floating sparse linear algebra only to *find* a positive Collatz witness. Every finite claim promoted to the proof — CTMC fractions, matrix row inequalities, `R<y`, Taylor tail bound, and geometric base `<1` — is rechecked with exact rational arithmetic before the pass line. Thus the finite certificate is exhaustive for the generated automaton; it is not a sampled curvature calculation.

## 11. Source-level before/after, auxiliary delta, and remaining full gap

| Quantity | Before | After | Meaning |
|---|---:|---:|---|
| source defect `c_*` | `0` | `0` | **NO MOVEMENT / OPEN** |
| rigorous diagonal UB | `0.758507818076` | `0.758507818076` | unchanged |
| track-certified axis LB | `0.30024` | `0.3002823` | auxiliary exact improvement |
| sufficient diagonal threshold `2 L_axis` | `0.60048` | `0.6005646` | auxiliary `+0.0000846` |
| remaining UB-to-threshold gap | `0.158027818076` | `0.157943218076` | auxiliary reduction only |

The nearest concrete source-relevant objective is now (8.2) with `a<0.3002823`, or any other rigorous argument implying

\[
\mu(1,1)<0.6005646.
\]

Even proving this one-pair strict inequality would be only **PARTIAL**. Full source closure still requires strict convexity for every pair of distinct boundary directions, a complete proof at that full scope, current prior-art verification, and the repository's independent-validation requirements. None of those closure conditions is claimed here.
