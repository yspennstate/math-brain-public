Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime exposes no authenticated applied model/effort receipt, so I do not claim GPT-6 maximum. SOURCE-LEVEL NO MOVEMENT: `c_*=0 -> 0`. Three materially different attacks were: (1) negate the recent reflected-cone metric using exact D4 norm geometry — this succeeds and shows that metric was misaligned with the canonical flat-edge obstruction; (2) attack the weighted-SAW/Chernoff route at the hard diagonal boundary — this succeeds as an exact method barrier, with the monotone-path subfamily already overwhelming first moment at the current P04 cap; (3) replace that route by a same-quadrant moving-centered diagonal-slab compiler with a completely paid finite-to-infinite error — the compiler is proved below, while its finite block has not yet crossed the source threshold.**

# PROB10-10 — source-facing reset, an exact first-moment obstruction, and a diagonal moving-slab compiler

Status: **PARTIAL / OPEN**. No claim of full strict convexity, no claim that `Delta_12>0`, and no closure request.

## 1. Frozen model, source, and source-level metric

The model remains nearest-neighbor **undirected** first-passage percolation on `Z^2` with one iid rate-one exponential weight on each physical edge. Write `T(x,y)` for unrestricted passage time and `mu` for the deterministic time-constant norm.

Primary source: Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in the limit-shape discussion: strict convexity for continuous passage-time laws. The canonical repository specialization is `Exp(1)` on the square lattice, source key

`ADH_50yearsFPP_Q4::Exp1_Z2_undirected`.

The frozen source-facing milestone is

`Delta_12 := 2 mu(e1)-mu(1,1)`

and

`c_* := sup{c>=0 : Delta_12>=c is rigorously proved in the canonical track}`.

- source metric before this run: `c_*=0`;
- source metric after this run: `c_*=0`.

A positive value would still be only a one-pair **PARTIAL** result, not global strict convexity.

## 2. Continuity, predecessor handoff, ownership, and histories consumed

The required immutable HARD7-03 predecessor handoff already exists and was directly re-read:

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`

blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`. It preserves the actual Seppalaeinen/D0025 particle-system successor, four-step sign atlas, exact predecessor artifacts, and its remaining source obstruction. Nothing in D0025 is changed here and no duplicate handoff is created.

Current state consumed before the new mathematics:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest canonical PROB10-10 report before this run:
  `runs/prob10_2026-09-20/PROB10-10/20260920T0950Z__retitled-ten-local-dual-cone16374.md`;
- newest complementary P04 update:
  `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T09-47-23Z__width7-undirected-cone1362.md`;
- newest complementary P20 update found on master:
  `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T09-18-00Z__single-edge-residual-clock-compiler.md`;
- R08's axis certificate
  `runs/R08/20260916T1528Z_fpp_axis_transition_3b7c92.md`;
- R08's stuck report
  `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- R07's distinct fluctuation/KPZ report
  `runs/R07/2026-09-16T1525Z_kpz_deep_edges_03.md`.

The historical failures remain binding: shared bypasses defeat multiplication of local surgery gains; finite positive-probability cylinders can have exact finite triangle equality; old fixed-corner blocks did not pay the axis/diagonal threshold; and R07's fluctuation statements are not curvature theorems.

Ownership is still nonduplicating. PROB10-10 owns the canonical parent. P04 owns the complementary moving-slab upper constructions. P20 owns the finite-target/Busemann residual-disagreement lane. This report consumes their newest proved ingredients but does not overwrite their files or claims.

## 3. Current literature gate

A fresh bounded web search on 20 September 2026 again found no unconditional closure of strict convexity for ordinary iid `Exp(1)`, nearest-neighbor, undirected FPP on `Z^2`.

Relevant boundaries rechecked:

- Auffinger--Damron--Hanson, arXiv:1511.03262, is still the source navigation and treats strict convexity as open;
- Lalley (2003), *Strict Convexity of the Limit Shape in First-Passage Percolation*, gives sufficient conditions involving asymptotic straightness and passage-time limit laws, not an unconditional exponential-law theorem;
- Dembin--Elboim--Peled (GAFA 2024) prove quantitative coalescence under a nontrivial extreme-point hypothesis on the limit shape, so that result cannot supply the missing shape property without circularity;
- Jacquet, arXiv:2412.20779, proves strict unrestricted-versus-directed time-constant comparison, not the same-quadrant strict triangle inequality here;
- Krishnan (CPAM 2016) gives an exact HJB/duality variational formula for the time constant and an iteration for minimizers under symmetry, but the bounded search did not locate a deduction of strict convexity for this lattice exponential model;
- Alm--Parviainen (CPC 2002) is direct prior art for transition-matrix time-constant bounds, so no novelty claim is made for finite-state time-constant machinery.

Searches included 2025--2026 variants of `strict convexity first-passage percolation Exp(1) Z2`, the exact source wording, and current strict-convexity/differentiability follow-ups. This is bounded negative evidence, not a worldwide novelty certificate.

## 4. Attack 1 — the reflected-cone metric was not testing the canonical obstruction

The recent canonical/P04 chain tracked inequalities of the form

`mu(1,rho)+mu(1,-rho) > mu(2,0)`.

Those statements may be correct, but they were a poor source-facing metric. There are two exact reasons.

### Lemma 4.1 — coordinate monotonicity of a sign-symmetric norm

Let `N` be a norm on `R^2` invariant under sign changes of each coordinate. If

`0<=a<=b`,

then for every real `y`,

`N(a,y)<=N(b,y)`.

**Proof.** For `b>0`, set

`theta=(1+a/b)/2`.

Then

`(a,y)=theta (b,y)+(1-theta)(-b,y)`.

Convexity of the norm and sign symmetry give

`N(a,y)<=theta N(b,y)+(1-theta)N(-b,y)=N(b,y)`.

The case `b=0` is trivial. Repeating coordinates proves coordinatewise monotonicity in an orthant. QED.

The FPP time constant is D4-invariant by square-lattice symmetry. Therefore for `rho>=1`,

`mu(1,rho)=rho mu(1/rho,1)=rho mu(1,1/rho)>=rho mu(1,0)`.

Consequently

`mu(1,rho)+mu(1,-rho)-mu(2,0)`

`=2mu(1,rho)-2mu(e1)`

`>=2(rho-1)mu(e1)>0`

for every `rho>1`.

Thus every previously reported reflected cone whose boundary was still above `1` was already forced by elementary norm geometry; it cannot be counted as new progress toward ADH strict convexity.

There is an even more important diagnostic. R08 already identified the canonical zero-gap alternative:

`Delta_12=0` iff the D4-symmetric limit shape is the `l1` diamond, equivalently

`mu(x,y)=a(|x|+|y|)`

for some `a>0`.

But this very non-strictly-convex norm satisfies, for every `rho>0`,

`mu(1,rho)+mu(1,-rho)-mu(2,0)=2a rho>0`.

So the entire reflected family is compatible with the exact canonical obstruction. Even pushing its cone boundary all the way to zero would not prove `Delta_12>0` and would not rule out the `l1` diamond.

**Correction of track interpretation.** Earlier all-path lower bounds and P04 block bounds are not erased; their mathematical inequalities remain whatever their proofs establish. What is superseded here is their interpretation as movement of a source-relevant directional metric for the canonical flat edge. The source-facing strict triangle must compare directions **inside the same first-quadrant face**, beginning with `e1,e2`, not reflected directions across an axis.

This is why the source metric remains `c_*=0` despite the earlier cone numerics.

## 5. Attack 2 — exact obstruction to the current first-moment weighted-SAW/Chernoff architecture at the diagonal boundary

P04's newest width-7/length-4 undirected moving slab proves the rigorous axis **upper** cap

`a47 = 1035580351964689/2000000000000000`

`    = 0.5177901759823445...`.

The newest canonical report retitled the ten-local weighted self-avoiding-path transfer. Recombining that machinery with `a47` would formally move its reflected critical slope to about `1.35917`, but Section 4 shows that another `rho>1` result is source-irrelevant. Before doing more transfer-matrix tuning, test whether that architecture can even reach the hard diagonal `rho=1`.

It cannot at the current cap, for a structural reason that no longer-memory local-SAW automaton can remove.

### Proposition 5.1 — monotone-path first-moment barrier

Fix `c in (0,2)`. Consider the proof architecture that upper-bounds

`P(T(0,(n,n))<=cn)`

by summing an exponential Chernoff bound separately over all admissible paths from `0` to `(n,n)`. If

`J(c):=c-2-2 log(c/2) < log 4`,

then the contribution of the shortest monotone E/N paths alone makes that Chernoff-union expression grow exponentially. In particular the architecture cannot yield an exponentially decaying upper bound at level `cn`, regardless of how accurately longer self-avoiding paths are counted.

**Proof.** There are exactly

`binom(2n,n)`

monotone E/N paths from `0` to `(n,n)`. Every one is globally self-avoiding and has exactly `2n` distinct physical edges. For one fixed such path, its passage sum is `Gamma(2n,1)`, and for `lambda>=0`,

`P(Gamma(2n,1)<=cn) <= exp(lambda c n)(1+lambda)^(-2n)`.

Because `c<2`, the right side is minimized at

`lambda_*=2/c-1`,

where it equals

`exp[-n J(c)]`.

Therefore even the optimized per-path Chernoff sum over the monotone subfamily is

`binom(2n,n) exp[-nJ(c)]`.

Since the largest binomial coefficient is at least the average coefficient,

`binom(2n,n) >= 4^n/(2n+1)`.

Thus the expression is at least

`exp[n(log 4-J(c))]/(2n+1)`,

which diverges exponentially if `J(c)<log4`. A local self-avoidance automaton cannot delete these paths, because they are genuinely globally self-avoiding. Endpoint tilting cannot change their total endpoint count either: every such path has the same net displacement `(n,n)`. QED.

This proposition is a statement about the **first-moment/Chernoff proof architecture**, not a lower bound on the actual probability of a fast path; dependence between paths is precisely what the union bound discards.

### Proposition 5.2 — an exact rational barrier already at `c>=58/125`

For every

`58/125 <= c < 2`,

one has `J(c)<log4`.

**Proof.** The inequality `J(c)<log4` is algebraically equivalent to

`h(c):=log c-c/2+1 >0`.

For `c<2`,

`h'(c)=1/c-1/2>0`.

At `c0=58/125`,

`h(c0)=log(58/125)+96/125`.

It is enough to prove `exp(96/125)>125/58`. The positive Taylor series gives

`exp(96/125) > sum_{k=0}^6 (96/125)^k/k!`

`= 41111306974109/19073486328125`,

and exact subtraction gives

`41111306974109/19073486328125 - 125/58`

`= 270013482697/1106262207031250 >0`.

Hence `log(125/58)<96/125`, so `h(c0)>0`; monotonicity gives the claim for all `c>=c0`. QED.

The consumed P04 cap lies well above this exact barrier:

`a47-58/125`

`=107580351964689/2000000000000000`

`=0.0537901759823445... >0`.

Therefore no amount of further loop-exclusion memory or anisotropic retitling inside the **same first-moment per-path Chernoff architecture** can prove a diagonal lower bound above the current P04 axis cap. Before that architecture can even become competitive at `rho=1`, the axis cap would at minimum have to fall below `0.464`; that is only a necessary condition, not a sufficient one.

The exact checker additionally certifies the stronger margin at the actual `a47` value:

`log 4-J(a47) > eta`,

with

`eta = 0.16583945510667997... >0`.

Artifacts:

- idea-before-code:
  `artifacts/prob10_2026-09-20/PROB10-10/20260920T1018Z__idea-hard-cone-reset-and-first-moment-barrier.md`;
- exact checker:
  `artifacts/prob10_2026-09-20/PROB10-10/20260920T1018Z__first_moment_barrier_exact.py`;
- executed output:
  `artifacts/prob10_2026-09-20/PROB10-10/20260920T1018Z__first_moment_barrier_exact.out`.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

## 6. Attack 3 — rotate the dependence-controlled block method to the actual same-quadrant defect

The barrier above says the next block method should not be paired with another lower bound on an oblique endpoint. The source-facing orientation is instead:

- retain a rigorous **lower** bound on `mu(e1)`;
- construct a rigorous **upper** bound on `mu(1,1)`;
- compare them directly in `Delta_12=2mu(e1)-mu(1,1)`.

The canonical track currently has the exact auxiliary lower certificate

`mu(e1) >= b := 3002823/10000000 = 0.3002823`,

so the direct diagonal target is

`mu(1,1) < 2b = 3002823/5000000 = 0.6005646`.

Old R08 fixed-corner square blocks did not reach this target. The following compiler removes the fixed-corner interface loss by allowing the endpoint to wander and recentering the next block, exactly in the dependence-controlled spirit that made P04's axis construction stronger.

### Proposition 6.1 — moving-centered diagonal-slab compiler

Fix integers `L>=1` and `W>=1`. Use rotated coordinates

`s=x+y`, `d=x-y`.

Let `G_{L,W}` be the finite strip of lattice vertices with

`0<=s<=2L`, `|d|<=W`, and the lattice parity condition `s=d (mod 2)`,

with every nearest-neighbor physical edge whose two endpoints lie in this strip. Start at `(s,d)=(0,0)` and stop at the first hit of the terminal antidiagonal `s=2L`. Let

`tau_{L,W}` be this restricted passage time and let `xi_{L,W}` be the `d`-coordinate of the terminal vertex selected by the a.s.-unique first hit. Put

`q_{L,W}=E tau_{L,W}`,
`v_{L,W}=E xi_{L,W}^2`.

Then for every integer `N>=1`,

`E T(0,(LN,LN))`

`<= N q_{L,W} + sqrt(N v_{L,W})`

and consequently

`mu(1,1) <= q_{L,W}/L`.

In particular, if an exact finite-state computation proves

`q_{L,W}/L < 3002823/5000000`,

then the canonical metric moves to the explicit positive value

`c_* >= 3002823/5000000 - q_{L,W}/L >0`.

**Proof.** Suppose block `j` begins at a vertex whose absolute rotated coordinates are

`s=2Lj`, `d=D_j`.

Translate `G_{L,W}` so that its center is that vertex, use the restricted optimal passage to the first terminal hit, and let `(tau_j,xi_j)` be the cost and relative terminal displacement. Set

`D_{j+1}=D_j+xi_j`.

Every physical edge used by block `j` joins absolute `s`-levels with lower level in

`{2Lj,2Lj+1,...,2L(j+1)-1}`.

These level bands are disjoint between different blocks. Hence, conditional on the complete past, the next block sees untouched iid `Exp(1)` physical edges. Translation invariance makes `(tau_j,xi_j)` iid copies of `(tau_{L,W},xi_{L,W})`.

Reflection `d -> -d` preserves the finite strip and the edge law, so

`E xi_j=0`.

After `N` blocks the reached center lies on `s=2LN` with transverse coordinate

`S_N=sum_{j=1}^N xi_j`.

Therefore

`E S_N^2=N v_{L,W}`

and

`E|S_N|<=sqrt(N v_{L,W})`.

In ordinary coordinates the endpoint is

`(LN+S_N/2, LN-S_N/2)`.

Because `S_N` has the correct even parity, it can be connected to `(LN,LN)` by a staircase of exactly `|S_N|` nearest-neighbor edges alternating between absolute levels `s=2LN` and `s=2LN+1`: for positive `S_N`, alternate north then west; for negative `S_N`, alternate east then south. Every such correction edge has lower absolute `s`-level `2LN`, while the block construction exposed only edges with lower level at most `2LN-1`. Thus the correction edges are fresh conditional on the entire block history, and their conditional expected total weight is exactly `|S_N|`.

Concatenating the `N` restricted block paths and the terminal correction gives

`E T(0,(LN,LN))`

`<= N q_{L,W}+E|S_N|`

`<= N q_{L,W}+sqrt(N v_{L,W})`.

Divide by `LN` and let `N->infinity`; the standard `L^1` time-constant convergence gives

`mu(1,1)<=q_{L,W}/L`. QED.

The finite-to-infinite error is therefore completely explicit:

`E T(0,(LN,LN))/(LN) - q_{L,W}/L`

`<= sqrt(v_{L,W})/(L sqrt N)`.

No independence between neighboring passage choices is assumed; independence is obtained only from disjoint physical-edge `s`-bands. This is a genuine moving-frontier construction, not the retired fixed-corner block route.

The finite core is also exact in principle for `Exp(1)`: for an infected vertex set `S` with no terminal hit, if `m_j(S)` is the number of boundary physical edges from `S` to an uninfected vertex `j` and `m(S)=sum_j m_j(S)`, then

`E(S)=1/m(S)+sum_j [m_j(S)/m(S)] E(S union {j})`.

The same positive recurrence with terminal reward `xi^2` computes `v_{L,W}`. P04's fixed-point upward rounding method can therefore be ported without a new dependence argument. This run proves the transfer first; it does **not** manufacture a large finite certificate before a promising block is identified.

## 7. Busemann/HJB comparison — what remains after the route reset

P20's newest one-edge residual-clock theorem remains the other genuinely source-facing route. For

`C_n=n e1`, `A_n=n(e1+e2)`,

and the unique geodesic `Gamma_n` from `0` to `C_n`, its exact identity is

`D_n := T(0,C_n)+T(C_n,A_n)-T(0,A_n)`

`     = sum_{e in Gamma_n} r_{A_n}(e)`.

P20's reserved single-edge exponential residual-clock argument gives local disagreement energy

`f(p)=p+(1-p)log(1-p) >= p^2/2`

and a compiler of the form

`n Delta_12 >= E sum_j f(p_j) - O(sqrt(n log n))`,

with the mean-convergence term recorded there.

This run tested the obvious geometric shortcut: use mere endpoint separation, or the two symmetric targets `n(e1+e2)` and `n(e1-e2)`, to force a positive density of local policy disagreements along the actual axis geodesic. That implication is not valid from endpoint geometry alone. A horizontal edge can be locally calibrated toward both symmetric targets, and long common initial portions are not ruled out without exactly the curvature/coalescence information being sought. Thus there is no source movement from this attack.

The unpaid Busemann obligation is now stated without the obsolete cone distraction: construct a predictable family of distinct reserved edges on the **actual** axis geodesic for which the total conditional disagreement energy exceeds the finite-to-infinite error, e.g. prove

`E sum_j f(p_j) = omega(sqrt(n log n))`

under P20's existing compiler, or prove a stronger positive-density version. A proof must come from a new geometric/variational input, not from a constructed P04 competitor path.

Krishnan's HJB variational formula is the most natural literature bridge for this lane because it already places the time constant in a dual optimization framework; no claim is made here that its known results supply the missing disagreement estimate.

## 8. Before/after ledger and exact remaining gap

### Source level

`c_* : 0 -> 0`.

Full ADH Exp(1) strict convexity remains **OPEN**.

### Corrected auxiliary interpretation

The earlier reflected-cone boundary is **retired as a source-progress metric**. The statements can remain as auxiliary inequalities, but they do not test the `l1`-diamond obstruction and the `rho>1` part is automatic from D4 norm geometry.

### New proved mechanism facts

1. **Exact method obstruction:** the current first-moment weighted-SAW/Chernoff architecture cannot reach the diagonal boundary at any threshold `c>=58/125=0.464`; the current P04 cap exceeds that barrier by exactly

   `107580351964689/2000000000000000`.

2. **Quantitative exact certificate at the actual cap:**

   `log4-J(a47) > 0.16583945510667997...`.

3. **Direct source-facing block compiler:** for every finite moving-centered diagonal slab,

   `mu(1,1)<=q_{L,W}/L`

   with finite-scale error at most

   `sqrt(v_{L,W})/(L sqrt N)`.

### Next exact finite target

Find one finite `(L,W)` with a rigorous upward certificate

`q_{L,W}/L < 3002823/5000000 = 0.6005646`.

If such a block exists, Proposition 6.1 plus the retained axis lower certificate gives an explicit positive `c_*` immediately. If increasingly wide/long blocks fail numerically before exact certification, do not file receipt-only checkers; return to the P20/Krishnan dependence-aware variational lane.

## 9. Persistence / execution record

Idea-before-code was persisted first at commit

`e33b6c6e088e4aa57edd01475ce73bcac1d0bf39`.

Exact checker creation commit:

`d43c9f4170709ff090344e32dedf32bd38a91ae0`.

Executed exact output creation commit:

`30a81b07fddd2d19739e4916eb7c0013669bfbfc`.

No Gmail, Drive, public posting, schedule modification, force push, claim overwrite, or other-track edit occurred. The hourly cadence/enabled state was left untouched.