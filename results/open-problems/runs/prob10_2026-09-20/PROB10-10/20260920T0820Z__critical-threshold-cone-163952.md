Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but the available scheduler exposes no authenticated model/effort selector, so I do not claim GPT-6 maximum. SOURCE-LEVEL canonical axis/diagonal metric: NO MOVEMENT, `c_*=0 -> 0`. Auxiliary source-valid reflected strict-triangle scope improves from the closed cone `|y|>=1.64x` to the closed cone `|y|>=1.63952x`, and analytically to every slope `rho>rho_*` with `rho_* in (1.6395106841629385,1.6395106841629394)`. Three materially different attacks were: critical-envelope recombination (success), moving-centered diagonal-slab attack (threshold obstruction), and finite-target Busemann/HJB disagreement (promising but missing super-root path energy).**

# PROB10-10 — exact critical slope of the current ten-local / moving-axis mechanism

Status: **PARTIAL / OPEN** for the full Auffinger–Damron–Hanson strict-convexity question. The new restricted theorem is **CANDIDATE_PROVED** conditional only on the already recorded canonical ten-local endpoint-count theorem and P04 moving-centered axis theorem; it is not independently audited here and does not close global strict convexity.

## 1. Frozen model, source, and metrics

The model remains nearest-neighbor **undirected** FPP on `Z^2` with one iid `Exp(1)` weight on each physical edge. Let `T(x,y)` be unrestricted passage time and `mu` the deterministic time-constant norm.

The external source is Auffinger–Damron–Hanson, *50 years of first passage percolation*, arXiv:1511.03262, Question 4 in the limit-shape discussion, specialized by the canonical repository claim to the iid `Exp(1)` square-lattice case.

The canonical full-source milestone remains

`Delta_12 := 2 mu(e1)-mu(1,1)`

and

`c_* := sup{c>=0 : Delta_12>=c is rigorously proved in the canonical track}`.

- before: `c_*=0`;
- after: `c_*=0`.

So the full source problem remains **OPEN**.

A separate restricted-direction metric records the smallest slope boundary for which the reflected strict-triangle family

`mu(x,y)+mu(x,-y) > mu(2x,0)`

has been proved for all `x>0` in the exact model. Immediately before this run, P04's newest moving-centered strip theorem gave the closed range

`|y| >= (41/25)x = 1.64x`

with defect `23/125000 x`.

This run gives two sharper forms:

1. a **closed, uniformly quantified cone**

`|y| >= (10247/6250)x = 1.63952x`

with defect at least

`x/250000 = 0.000004 x`;

2. a **parametric open-cone theorem** for every slope `rho>rho_*`, where

`rho_* := ((r-1)a_* - log A)/log B`

and the exact checker brackets

`1.6395106841629385 < rho_* < 1.6395106841629394`.

Thus the current mechanism's rigorous slope infimum moves

`1.64 -> rho_* = 1.639510684162939...`,

while the convenient closed rational scope moves

`1.64 -> 1.63952`.

Neither statement asserts full strict convexity.

## 2. Consumed repository state and ownership

The required predecessor handoff remains the immutable file

`runs/prob10_2026-09-20/PROB10-10/20260919T2321Z__handoff-hard7-03-d0025.md`

(blob `1a7045aaf81930242664b944b6f0ab09f791c4c1`). It preserves HARD7-03's actual D0025 particle-system / four-step-sign-atlas state. No duplicate handoff or schedule change is made.

Consumed current state:

- `operations/PROB10_2026-09-20.md`;
- root `POSTED.md`;
- canonical `operations/claims/PROB10-10.md`, blob `6fca778a3608f973175577e9852a61dcd6754c55`;
- newest canonical owner report before this run, `runs/prob10_2026-09-20/PROB10-10/20260920T0722Z__ten-local-saw-cone-1701.md`, blob `3db52bb7ea1fde7d3bad3f260f4c4dfb8d17e28e`;
- newest complementary P04 report, `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T07-44-45Z__moving-strip8-wandering-cone1640.md`, blob `b3ec4269fb61103f65e1668b3fc5f0c3260189ab`;
- newest complementary P20 report, `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T07-12-00Z__finite-hjb-flatness-budget.md`, blob `8a925c0dd03468e7223ede86a24aacc6afe17d96`;
- the R08 obstruction chain retained by the canonical claim, including `runs/R08/20260916T1623Z_stuck_diagblock_4c19a7.md`;
- the distinct R07 fluctuation/KPZ history, not imported as curvature.

Ownership remains nonduplicating. PROB10-10 is the canonical parent. P04 owns the complementary moving-centered block/axis construction. P20 owns the finite-target Busemann/HJB lane. This run only optimizes the canonical owner's oblique weighted-path lower-tail compiler **against the newly available P04 axis cap**.

The old R08 failures remain binding: shared bypasses destroy naive multiplication of surgery gains; finite cylinder events can have exact triangle equality; and fixed-corner blocks did not pay the old axis/diagonal threshold. None is restarted.

## 3. Current literature boundary

A bounded fresh search on 20 September 2026 did not recover a theorem closing ordinary iid `Exp(1)`, nearest-neighbor, undirected `Z^2` strict convexity.

The source remains ADH arXiv:1511.03262. Dembin–Elboim–Peled, arXiv:2204.02332, prove their quantitative planar coalescence theorem under the extra assumption that the limit shape has more than 32 extreme points, so it cannot be used to infer the missing shape property here. Jacquet, arXiv:2412.20779, proves strict inequality between unrestricted and directed FPP time constants, which is not the direction-to-direction strict triangle inequality needed here. These scope checks are bounded current-status evidence, not an exhaustive novelty certificate.

## 4. Idea-before-code and attacks

The idea was written before the checker in

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0820Z__idea-critical-envelope-16396.md`

at creation commit `dc9c5c3f8b92b452fdcf456d6d00f835f57d703a`.

That first exact candidate used slope `1.6396`. After its sign was certified, the scalar optimization was completed analytically rather than filing another blind parameter search. The authoritative theorem below identifies the **exact critical slope of this fixed mechanism**.

### Attack A — critical-envelope recombination: SUCCESS

Consume P04's much smaller rigorous axis cap and drive the Chernoff parameter to the boundary `s downarrow r-1`. This turns the previous numerical retuning problem into a one-line variational threshold and proves the theorem in Sections 6–9.

### Attack B — moving-centered diagonal slabs: OBSTRUCTION IDENTIFIED

The genuinely different direct route is to apply moving-centered fresh slabs across antidiagonal levels and upper-bound `mu(1,1)`, which would attack `Delta_12` rather than a reflected outer cone. The retained exact axis lower bound is

`mu(e1) >= 3002823/10^7 = 0.3002823`,

so this route must rigorously produce

`mu(1,1) < 0.6005646`

to make `Delta_12>0`. The current certified diagonal upper bound in this track is `0.758507818076`, leaving a gap of `0.157943218076`. The small-strip recursions explored earlier are nowhere near this threshold. No finite fit is promoted. The exact missing lemma is therefore: **a dependence-controlled diagonal block compiler with asymptotic cost below `0.6005646`, including its endpoint-repair error**. Until that is found, more strip-width numerics are not source progress.

### Attack C — finite-target Busemann/HJB disagreement: PROMISING, NOT CLOSED

P20's newest report changes the required geometric target. Under hypothetical `Delta_12=0`, its exact finite-target mixed HJB residual along the actual axis geodesic has expectation only `O(sqrt(n log n))`. Hence it is enough to prove `omega(sqrt(n log n))` robust opposing-policy energy along that geodesic; positive linear density is stronger than necessary.

This is the strongest route toward the canonical `c_*` after the present scalar cone mechanism is exhausted. The unpaid step is still geometric: prove that the optimizing axis geodesic cannot avoid almost all blocks on which the NE/SE finite-target Bellman policies disagree with a quantitative margin. No such path-unavoidability lemma is claimed here.

## 5. Two consumed theorems

### 5.1 Canonical ten-local weighted path count

The preceding canonical report proves an all-length endpoint-count theorem with

`A = 3889/2000`,
`B = 27893/10000`,
`r = 1993/400`.

If `N_l(M,R)` denotes the number of globally self-avoiding `l`-edge paths from `0` to `(M,R)` with `M,R>=0`, then

`N_l(M,R) <= Kbar r^l A^(-M) B^(-R)`

is valid with the safe all-length constant

`Kbar = 8238929532962105878831551056872795868088655007514624 /
        617949527283939289422235868959530625`.

The ten-local Collatz certificate itself is not re-proved here.

### 5.2 P04 moving-centered axis theorem

P04's newest report proves

`mu(e1) <= a_* := 294639/500000 = 0.589278`

and, more precisely,

`E T(0,8N e1) <= 8N a_* + sqrt(N)`.

The construction adaptively recenters a three-row width-eight slab at the random previous endpoint while assigning disjoint horizontal departure-column edge sets to successive blocks. Reflection makes the transverse displacement mean zero; one final fresh-column repair costs `O(sqrt(N))`. This is consumed, not relabeled as PROB10-10 work.

## 6. General lower-tail lemma for the consumed path count

Fix `rho>0`, let `M` and `rho M` be nonnegative integers, and choose `s>r-1`. Put

`q := r/(1+s) < 1`.

For a fixed self-avoiding path of length `l`, its physical edges are distinct, so its passage sum is `Gamma(l,1)`. For any `c>0`, Chernoff gives

`P(Gamma(l,1) <= cM) <= exp(scM)(1+s)^(-l)`.

Every geodesic is self-avoiding almost surely because the Exp(1) weights are strictly positive. Every path from `0` to `(M,rho M)` has

`l >= (1+rho)M`.

Union bound and the consumed path count therefore give

`P(T(0,(M,rho M)) <= cM)`

` <= Kbar A^(-M) B^(-rho M) exp(scM)
      sum_{l >= (1+rho)M} q^l`

` <= C_s [beta_s(rho)]^M`,

where

`C_s := Kbar/(1-q)`

and

`beta_s(rho) := A^(-1) B^(-rho) exp(sc) q^(1+rho)`.

This is a genuine all-path bound; no finite-size shape sampling is used.

If `beta_s(rho)<1`, then

`E T(0,(M,rho M)) >= cM [1-C_s beta_s(rho)^M]`.

Taking multiples of a rational direction and then using homogeneity and continuity of `mu` yields

`mu(1,rho) >= c`.

## 7. Exact critical slope of the fixed mechanism

Define

`rho_* := ((r-1)a_* - log A)/log B`.

Since `A,B>1`, the denominator is positive. The authoritative exact rational log checker proves

`1.6395106841629385 < rho_* < 1.6395106841629394`.

Now fix **any** `rho>rho_*` and define

`G(rho) := log A + rho log B - (r-1)a_* > 0`.

Set

`c_rho := a_* + G(rho)/(2(r-1))`

and

`epsilon_rho := G(rho)/(4 c_rho)`,

`s_rho := (r-1)+epsilon_rho`.

Then `s_rho>r-1`. At the boundary `s_0=r-1`, where formally `q=1`,

`log beta_{s_0}(rho)`

` = (r-1)c_rho - log A - rho log B`

` = -G(rho)/2`.

Increasing `s` from `s_0` to `s_rho` changes the logarithm by

`epsilon_rho c_rho -(1+rho) log(1+epsilon_rho/r)`.

The second term is nonpositive, hence

`log beta_{s_rho}(rho)`

` <= -G(rho)/2 + epsilon_rho c_rho`

` = -G(rho)/4 < 0`.

Therefore

`mu(1,rho) >= c_rho`.

Reflection gives the same bound for `mu(1,-rho)`, while the consumed axis theorem gives `mu(2,0)<=2a_*`. Hence

`mu(1,rho)+mu(1,-rho)-mu(2,0)`

` >= 2(c_rho-a_*)`

` = G(rho)/(r-1) > 0`.

By homogeneity:

### PROB10-10-T7-CRITICAL-CONE — CANDIDATE_PROVED / PARTIAL

For every real `x>0` and every `rho=|y|/x > rho_*`,

`mu(x,y)+mu(x,-y)-mu(2x,0)`

` >= [G(rho)/(r-1)] x > 0`.

Square-lattice `D_4` symmetries give all rotated/reflected copies.

This theorem is restricted to a reflected family. It does not prove arbitrary chord strictness and does not imply the entire limit shape is strictly convex.

### Why `rho_*` is the exact barrier of this fixed scalar mechanism

At `s downarrow r-1`, the best possible lower-tail level compatible with `beta<1` approaches

`c_max(rho) = [log A + rho log B]/(r-1)`.

To beat the axis cap we require `c_max(rho)>a_*`, which is exactly `rho>rho_*`. Thus **no further scalar tuning of `s` and `c` with the same `A,B,r,a_*` can move the slope below `rho_*`**. A subsequent run must improve the weighted path transfer, improve the axis cap, or change mechanism; another micro-retuning is exhausted by this calculation.

## 8. A clean closed rational cone with uniform defect

For a closed statement choose

`rho_0 = 10247/6250 = 1.63952`,
`c = 3683/6250 = 0.58928`,
`s = 398250001/100000000 = (r-1)+10^(-8)`,
`beta_hat = 999999/1000000`.

The exact checker proves

`rho_0 > rho_*`,

`log beta_s(rho_0) < log beta_hat < 0`.

Moreover `beta_s(rho)` decreases with `rho`, because `q/B<1`. Hence the same lower-tail estimate holds for every `rho>=rho_0`.

Since

`2(c-a_*) = 1/250000`,

we obtain the clean uniform theorem:

### PROB10-10-T7-CLOSED-CONE-163952 — CANDIDATE_PROVED / PARTIAL

For every real `x>0` and `|y| >= (10247/6250)x`,

`mu(x,y)+mu(x,-y)-mu(2x,0) >= x/250000`.

This improves P04's closed slope boundary `1.64` to `1.63952`.

## 9. Explicit finite-to-infinite error

The same theorem has a fully explicit finite-scale residual.

For rational `rho>=rho_0` and lattice scale `M`, Section 6 gives

`E T(0,(M,rho M)) >= cM[1-C beta_hat^M]`,

where

`C=Kbar/(1-q)`.

For `M` divisible by 4, P04's finite block theorem with `8N=2M` gives

`E T(0,2M e1) <= 2M a_* + (1/2)sqrt(M)`.

Therefore

`R_M(rho) :=`

`[E T(0,(M,rho M)) + E T(0,(M,-rho M)) - E T(0,2M e1)]/M`

satisfies

`R_M(rho) >= 1/250000 - 2cC beta_hat^M - 1/(2 sqrt(M)).`

The exact checker proves, using rigorous rational logarithm bounds rather than a floating sign,

`beta_hat^700000 < 1/2`.

At

`M=10^12`

(which is divisible by 4 and by 6250), one may use only 120 of those half-life blocks, so `beta_hat^M <= 2^(-120)`. The exact certified bound is

`2cC 2^(-120) < 5.89002732775671e-12`,

while

`1/(2 sqrt(M)) = 5e-7`.

Consequently

`R_M(rho_0) > 3.499994109972672e-6 > 0`.

This finite statement is an **expectation inequality**, not a claim that every sampled finite environment has strict triangle inequality.

## 10. Exact artifacts and tests

The authoritative exact checker is

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0820Z__critical_threshold_163952_exact.py`

creation commit `e956354c8ea87fe822798a03bf26a8a12d6a6042`.

Its archived executed output is

`artifacts/prob10_2026-09-20/PROB10-10/20260920T0820Z__critical_threshold_163952_exact.out`

creation commit `4a3baca02bfee6ba2c583a035d3b016d3b0133f8`.

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

It verifies with exact `Fraction` arithmetic:

- a width `<9.3e-16` rational enclosure of `rho_*`;
- `rho_*<1.639511`;
- the exact Chernoff sign at `rho_0=1.63952`;
- the uniform defect `delta=1/250000`;
- the half-life logarithmic inequality for `beta_hat`;
- lattice divisibility at `M=10^12`;
- the positive finite expected residual above.

An earlier exploratory exact point at slope `1.6396` is preserved in

`20260920T0820Z__critical_envelope_16396_exact.py/.out`

(commits `b519f610b9d218a168f7f97190b2793a13ee30f7` and `18d6d379890e295fc8fec6bfb099f11a87620894`). It is **superseded by the stronger analytic threshold and closed `1.63952` theorem**, not counted as a separate research claim.

## 11. Before/after and unresolved full-scope gap

### Source-level metric

`c_*: 0 -> 0` — **no movement** on the canonical axis/diagonal milestone.

### Auxiliary source-valid direction metric

- previous best closed reflected cone: `rho>=1.64`;
- new closed cone: `rho>=1.63952`;
- new exact mechanism infimum: every `rho>rho_*`, with
  `rho_* in (1.6395106841629385,1.6395106841629394)`.

### Defect/error

- uniform closed-cone infinite-volume defect: `>= x/250000`;
- at `rho=1.63952`, `M=10^12`, explicit normalized finite expected residual: `>3.499994109972672e-6`;
- general open-cone defect: `G(rho)x/(r-1)` with the explicit finite error from Section 9 after substituting the corresponding `s_rho,c_rho,C_rho`.

### Remaining full problem

Global strict convexity is still open. In particular this report does not prove `Delta_12>0`, does not rule out a flat segment near the diagonal, and does not prove strictness for arbitrary nonsymmetric chord pairs.

The present scalar cone mechanism is now **analytically exhausted below `rho_*` for its fixed constants**. The next genuine source-level route should therefore change mechanism. The most concrete current obligation is the P20 finite-HJB one:

> Under `Delta_12=0`, prove that the actual axis geodesic accumulates `omega(sqrt(n log n))` mixed opposing-policy Bellman energy.

A dependence-controlled P04-style block decomposition carrying the two finite-target value profiles is a plausible way to attack that obligation. Repeating Chernoff parameter tweaks with the same `A,B,r,a_*` cannot improve the slope barrier proved here.
