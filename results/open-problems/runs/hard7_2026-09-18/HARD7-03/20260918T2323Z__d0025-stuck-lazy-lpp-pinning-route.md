Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **no movement in the frozen metric `L <= Delta_2(Q)`: `0 -> 0`; SECTION-I STUCK RECOVERY 1; methods B6, B22, B27.** GPT-6/maximum was requested in prompt text, but this runtime exposes no authenticated GPT-6/maximum selector or reasoning-effort telemetry, so I do not claim otherwise.

# HARD7-03 — Section-I stuck recovery 1: the K=2 problem as columnar lazy LPP, why the direct K=1 port fails, and the pinning route that remains

Date: 2026-09-18/19 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source residual remains OPEN_BY_BOUNDED_SEARCH.** This is the mandatory thinking/stuck run after three consecutive executions with unchanged source metric. It records no new source-level theorem and creates no checker-only artifact. The mathematical work is a route diagnosis and a change of mechanism.

Canonical target: `D0025`, Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), Problem 4, Section 4. The active claim remains `operations/claims/D0025.md`, owned by `HARD7-03`.

Frozen case:
\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]
with hydrodynamic flux `f_{2,Q}` and
\[
\Delta_2(Q)=\sup\{\delta\ge0:f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]
The fixed metric remains a rigorous certified lower bound `L <= Delta_2(Q)`.

## 1. Continuity, repository reads, ownership, and current-source status

I resumed the exact admitted target and the newest checkpoint rather than restarting a literature survey. Before research I reread:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/D0025.md`;
- all three earlier HARD7-03 checkpoints, newest first: `20260918T2242Z__d0025-height-c3-five-site-current-bound.md`, `20260918T2121Z__d0025-two-slow-site-bellman-envelope.md`, and `20260918T2022Z__d0025-admission-k2-product-obstruction.md`;
- the relevant neighboring D0025 status screen `runs/R08/20260918T0030Z_d0024_resolution_d0025_plateau_screen_c7a4e2.md`;
- newest neighboring HARD7-02 and HARD7-04 reports;
- the D-intake/source entries for `disordered_asep_open_1999`, including canonical dedup key `disordered_asep_open_1999::problem_4`.

Repository searches still identify D0025 as exclusively owned by HARD7-03. I found no release, conflicting canonical owner, posting, or equivalent source closure. The R08 source screen independently records the same status split used here: the ordinary `K=1` site-disordered plateau is known, while the general-capacity residual is not thereby closed.

The primary source remains Seppäläinen 1999, arXiv `math/9906194`, Problem 4. Its central explicit question is:

> “Does the flux function \(f_K(\rho)\) have a flat segment on an interval around \(\rho=K/2\)?”

The source model is the totally asymmetric nearest-neighbor `K`-exclusion process: `eta(x) in {0,...,K}` and a particle jumps from `x` to `x+1` at rate `alpha_x` when `eta(x)>=1` and `eta(x+1)<=K-1`, in an iid site-rate environment.

A bounded current-literature refresh dated 2026-09-18/19 again found no theorem closing this `K>=2` site-disordered plateau residual. The check included the source title/Problem 4 aliases, `disordered K-exclusion plateau`, `site disorder K-exclusion flux`, and later `K`-exclusion papers. The 2024 Ayyer–Misra exactly-solvable `(q,t)`-deformed model is a different rate model. The known `K=1` plateau papers remain outside new-credit scope. This is a bounded negative search, not a claim that worldwide literature has been exhaustively ruled out.

## 2. Frozen metric and why this run is Section I

Before this run,
\[
L=0.
\]
After this run,
\[
\boxed{L:0\longrightarrow0.}
\]
This is the fourth consecutive execution with no movement in the fixed metric and the first mandatory Section-I recovery run. The previous three method triples were

- run 1: B2 / B12 / B18;
- run 2: B8 / B11 / B19;
- run 3: B1 / B24 / B30.

This run uses the new triple B6 / B22 / B27 and chooses exactly one Section-I recovery action at the end.

## 3. Section-I (a): the exact statement that blocks

By the source-level convex duality between the `K=2` growth shape and hydrodynamic flux, the obstruction can be stated without asking for an exact formula for either object. Let `g=g_{2,Q}` be the convex dual growth function in Seppäläinen's notation, so
\[
f_{2,Q}(\rho)=\inf_x\{\rho x+g(x)\}.
\]
Particle-hole symmetry centers the desired flat interval at `rho=1`. The exact blocking statement is
\[
\boxed{
\exists\,\delta>0:\qquad [-1-\delta,-1+\delta]\subseteq \partial g(0).
}
\tag{3.1}
\]
Equivalently,
\[
\boxed{
f_{2,Q}(\rho)=f_{2,Q}(1)\quad\text{for every }|\rho-1|\le\delta.}
\tag{3.2}
\]
Thus the source metric moves as soon as one proves a strict zero-slope corner of the correct deterministic growth shape. No exact value of the plateau current is needed for the first movement.

## 4. Section-I (b): every route tried and the precise reason it did not close (3.1)

### Route 1 — product/invariant-measure closure (run 1, B12/B18)

The most tempting analogue of ordinary exclusion is a translation-invariant product law parameterized by density. The exact finite-ring check from run 1 showed that the naive constant-parameter product candidate is not stationary for asymmetric `K=2` exclusion. This is not a small normalization problem: later blocking-measure literature likewise distinguishes asymmetric product blocking measures from the missing translation-invariant equilibrium structure. Therefore a direct formula `current = E[c(eta_0,eta_1)]` under a known one-parameter product family is unavailable.

**Failure mode:** no explicit stationary family that both spans densities near one and computes the correct current.

### Route 2 — attack the negation on finite rings (run 1, B2)

Finite rings can falsify proposed invariant formulas and can expose false local identities, but a finite SAT/Markov-chain witness does not refute or prove the infinite-volume hydrodynamic plateau. The finite-ring obstruction did its job by killing the wrong route; it did not decide (3.1).

**Failure mode:** wrong quantifier and wrong scale for an asymptotic quenched shape statement.

### Route 3 — controlled slow-block capacity (runs 2–3, B8/B11/B19/B24)

The exact Bellman calculations produced
\[
C_2=\frac{71}{219},\qquad
C_3=\frac{3224554983}{11275278979},
\]
for two and three consecutive rate-`1/2` sites under arbitrary adapted exterior forcing, and proved the monotone bottleneck hierarchy. These are genuinely source-relevant upper-current mechanisms.

**Failure mode:** bottleneck capacities prove `f(\rho)<=C_m`; they do not prove that one common bottleneck value is attained for a nontrivial interval of densities. An upper ceiling alone cannot create a flat segment.

### Route 4 — local-stationarity LP (run 3, B30)

The five-site exact primal/dual LP gave homogeneous unit-rate current at most `24/47` in the local relaxation and consequently
\[
C_\infty\le \frac{12}{47},
\qquad
f_{2,Q}(\rho)\le \frac{12}{47}.
\]
This avoided guessing an infinite-volume invariant measure.

**Failure mode:** local stationarity describes necessary local identities, not dynamic selection of the extremal infinite-volume state at a specified density. It supplies another upper bound, not the matching lower-current mechanism required by (3.1).

### Route 5 — height/interface recoding (run 3, B1)

For `xi_x=eta_x-1 in {-1,0,1}` and `H_x-H_{x-1}=xi_x`, a source jump lowers exactly one weak local maximum `H_x` by one. The plateau becomes a zero-tilt facet problem for a columnar-disordered interface.

**Failure mode:** the recoding exposes the right geometry but by itself has no quantitative pinning or regeneration estimate forcing a facet.

### Route 6 — direct port of Sly's K=1 homogeneous-slow coupling (this run, B6/B22)

This is the new route that I tried first because it is the nearest source-level solved case. It fails for a precise geometric reason, not because the algebraic coupling is unavailable. The details are in Sections 5–6 below.

## 5. B6 — deform to the solvable minimum-rate environment: the exact K=2 lazy-LPP representation

Seppäläinen's 1999 hydrodynamic construction for simple `K`-exclusion uses `K`-admissible lattice paths with increments
\[
(1,0),\qquad (0,1),\qquad (K,-1),
\]
and site passage times `alpha_j^{-1} lambda(i,j)`, where the `lambda(i,j)` are iid mean-one exponentials and the random environment `alpha_j` is attached to the second coordinate.

For the frozen case `K=2`, make the exact coordinate change
\[
t=i+j-1,\qquad y=j.
\]
Then the three admissible increments become
\[
(\Delta t,\Delta y)=(1,0),\qquad(1,+1),\qquad(1,-1).
\]
Hence the `K=2` growth problem is exactly a directed last-passage problem over **lazy nearest-neighbor paths** `y_t` with increments in `{-1,0,+1}`. At space-time point `(t,y)` the passage variable is
\[
V(t,y)=\alpha_y^{-1}\lambda(t+1-y,y),
\tag{5.1}
\]
so, conditional on the static row environment, the `V(t,y)` are independent exponentials of rate `alpha_y`. The disorder is columnar/transverse: the whole row `y` has one random rate `alpha_y`.

This gives a useful exact dictionary:

- density/height tilt near `rho=1` corresponds to a small endpoint velocity of the lazy path;
- the desired plateau corresponds to a strict corner of the point-to-point time constant at zero velocity;
- a successful proof needs a **pinning or localization advantage** at zero velocity that is lost linearly when the endpoint is tilted.

This is an exact reparameterization of the already admitted source model, not a new source theorem and not metric movement.

## 6. B22 — read the successful K=1 proof for the step it uses that K=2 lacks

Allan Sly's `K=1` paper, *Note on the flux for TASEP with general disorder* (arXiv:1609.06589), proves a plateau for iid site disorder with positive infimum rate `r`. Its LPP proof couples the disordered passage variable on row `i`,
\[
Y\sim \operatorname{Exp}(\alpha_i),
\]
to the homogeneous minimum-rate variable
\[
Z\sim \operatorname{Exp}(r)
\]
by writing
\[
Z=Y+U,
\]
where one convenient coupling is
\[
U=B\,E,
\qquad
B\sim\operatorname{Ber}(1-r/\alpha_i),
\qquad
E\sim\operatorname{Exp}(r).
\]
Consequently
\[
\mathbb E[U\mid\alpha_i]=\frac1r-\frac1{\alpha_i}\ge0.
\tag{6.1}
\]
The decisive geometric input in the ordinary TASEP path set is that every admissible path between the relevant endpoints is forced to visit one site in each of a macroscopic interval of disorder coordinates. Summing (6.1) over those forced coordinates gives a deterministic linear correction after a law of large numbers. This creates the strict slope change that dualizes to the plateau.

The same coupling exists algebraically for the frozen `K=2` lazy-LPP representation, with `r=1/2`. For the binary law,
\[
\mathbb E[U\mid\alpha_y]
=2-\frac1{\alpha_y}
=\begin{cases}
0,&\alpha_y=1/2,\\
1,&\alpha_y=1.
\end{cases}
\tag{6.2}
\]
But the **forced-coverage step collapses exactly at the central direction**. A lazy path ending at zero velocity is allowed to remain on a single row `y` for all times. If that row is slow (`alpha_y=1/2`), then every coupling reward on that path has conditional mean zero. More generally a path ending at transverse displacement `m` is forced to cross only the rows between its start and endpoint, so the deterministic forced-row contribution is only `O(|m|)` and gives no strictly positive extensive correction at zero velocity.

Therefore Sly's direct quantifier

> every admissible path receives a positive macroscopic coupling bonus

is false in the `K=2` geometry precisely where the desired corner must be proved.

This is the main substantive conclusion of the stuck run: **the K=1 proof cannot be ported by replacing its path set and replaying the same coverage inequality.** A proof must instead use the behavior of maximizing or near-maximizing paths.

## 7. B27 — swap the quantifier: from every path to the optimizing path

The failed K=1 port suggests the correct quantifier change. Do not try to prove that every lazy path samples a positive density of fast rows. That is false. Instead seek a statement of the form:

> for a typical binary row environment, a zero-velocity maximizing/near-maximizing path pins to an unusually favorable slow row or slow-row cluster, while a path constrained to nonzero small velocity must pay a linear-in-displacement escape cost.

The strongest useful form would be a quenched estimate that, for sufficiently small `v`, separates point-to-point shape values by a linear term,
\[
G(0)-G(v)\ge c|v|+o(|v|)
\qquad(c>0),
\tag{7.1}
\]
with the sign/convention translated to `g` as in (3.1). I am **not** claiming (7.1); it is the missing shape estimate a proof would need.

This quantifier swap has a close solved analogue. Bakhtin–Khanin–Mészáros–Voltz, *Last passage percolation in a product-type random environment* (arXiv:2310.08379, revised 2025), study `1+1` dimensional lazy-walk LPP with static spatial randomness and prove a corner/flat-edge phenomenon through localization at favorable locations. Its geometry is much closer to (5.1) than ordinary up/right `K=1` LPP.

The paper does **not** settle D0025: its potential is product-type/separable and supports estimates unavailable verbatim for exponential row-rate disorder (5.1). In particular our time noise is unbounded exponential and the row environment changes the entire exponential rate rather than multiplying a bounded signed temporal factor. But it supplies the missing category of argument: control the optimizer's visits to favorable spatial sites and quantify the cost of forcing endpoint velocity.

## 8. Section-I (c): what a successful proof must contain that no route so far contains

Every successful route so far gives an upper current bound or a reformulation. None supplies the following object:

**a source-valid, infinite-volume, density-sensitive lower mechanism that selects the true optimizer/state and produces a strict first-order cost for leaving zero tilt.**

Concretely, one needs at least one of these equivalent mechanisms in the frozen binary `K=2` model:

1. a quenched geodesic-pinning theorem for (5.1) with a positive linear endpoint-tilt penalty;
2. a regeneration construction whose asymptotic speed/current is pinned at the same bottleneck value for a whole tilt interval;
3. a direct proof that the one-sided derivatives of `g` at zero are separated.

The finite bottleneck and local-stationarity arguments do not contain dynamic optimizer selection, which is why they cannot be iterated into (3.1).

## 9. Section-I (d): simplest special case still unproved

The simplest source-valid special case that would move the fixed metric is **not** an exact flux formula. It is only the strict zero-slope corner for the already frozen binary environment:
\[
\boxed{
 g'_{-}(0)<-1<g'_{+}(0)
}
\tag{9.1}
\]
(or the equivalent statement that `partial g(0)` has positive width around `-1`). By convex duality and particle-hole symmetry, (9.1) already implies `Delta_2(Q)>0` and hence `L>0`.

This is now the precise milestone. Solving the full source Problem 4, determining the plateau height, treating all `K>=2`, or giving an explicit invariant family are all strictly stronger than what is needed for first metric movement.

## 10. Section-I (e): nearest solved problems and exactly what their proofs have that this problem lacks

### Nearest source-level solved case: K=1 disordered TASEP

Sly's 2016 plateau theorem has the exact exponential-rate coupling and, crucially, a path geometry in which the optimizing path cannot avoid a macroscopic set of independent disorder coordinates. That forced coverage turns a one-site mean gain into an extensive deterministic gain. The `K=2` lazy path can stay on one favorable row, so this ingredient is absent.

### Nearest geometric solved analogue: product-type lazy-walk LPP

Bakhtin–Khanin–Mészáros–Voltz have the **same lazy nearest-neighbor path geometry with static spatial disorder**, and their proof develops a favorable-location pinning/localization mechanism that produces a corner/flat edge. What their model has that (5.1) does not is a product/separable potential structure with stronger direct control of the reward obtained by dwelling at favorable sites. The frozen D0025 model has unbounded exponential time noise and row-dependent rate modulation, so those estimates must be rebuilt rather than cited as a transfer theorem.

This identifies a genuinely new route, not another finite bottleneck certificate.

## 11. Chosen Section-I recovery action and next-run methods

I choose exactly one recovery action:

**PORT THE TECHNIQUE FROM (e).**

Specifically, port the favorable-site pinning/endpoint-cost mechanism from the solved lazy-walk product-environment LPP problem to the exact exponential row-rate model (5.1). I am **not** choosing “prove another finite special case,” “reduce to another finite computation,” or “refute instead.”

The next run, if D0025 remains active and no literature/ownership change supersedes it, should try the new triple:

- **B3 — PROVE SOMETHING STRONGER:** formulate a pinned-geodesic localization estimate strong enough to imply the derivative gap, rather than aiming directly at the flux plateau;
- **B15 — BREAK THE SYMMETRY ON PURPOSE:** condition on a distinguished exact slow row near the origin and compare constrained paths that stay with it versus paths forced to exit to the left/right;
- **B28 — REPLACE FOR ALL WITH FOR TYPICAL:** prove the pinning/exit-cost statement for almost every binary row environment instead of seeking an impossible deterministic statement over all environments/paths.

If the fixed metric remains unchanged through the allowed second hard-target stuck recovery, the third stuck episode must hand off and rotate according to Section I rather than create another certificate around the same obstruction.

## 12. Scheduler/model capability honesty

The actual model exposed in this execution is `GPT-5.6 Sol`; reasoning effort is not authenticated and is therefore `UNVERIFIED`. The exposed native automation interface still offers prompt/title/schedule/timing/enablement fields but no binding model selector, no reasoning-effort selector, and no guaranteed execution duration. GPT-6/maximum remains a text request only.

Changing this would require the platform/native scheduler API to expose an authorized model field and reasoning-effort field (or an account/workspace/product change that grants such controls). A GitHub edit cannot change scheduler runtime selection.

The repository policy also records historical native task edits that returned `You cannot modify this task` (including a P26 probe in one context). The lawful workaround is to resolve scheduler ownership/account/workspace authorization through the product interface or platform support. It is not to bypass the refusal by creating a duplicate task. No schedule was created, modified, reactivated, or disabled in this run.

## 13. Why there is no new checker artifact this run

This is intentionally a Section-I thinking run. The new work is an exact change of path coordinates, a route-failure diagnosis, and the identification of the missing optimizer-level estimate. There is no new finite exhaustive claim whose value justifies spending the run on a certificate. Creating another checker while `L` stays at zero would violate the new-methods-first instruction.

## 14. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  source: D0025
  owner_claim: operations/claims/D0025.md
  status: PARTIAL
  current_source_status: OPEN_BY_BOUNDED_SEARCH
  frozen_case:
    K: 2
    site_rate_law: "1/2 delta_{1/2} + 1/2 delta_1"
  metric: "certified lower bound L <= Delta_2(Q)"
  before: 0
  after: 0
  movement: no
  consecutive_no_movement_runs: 4
  section_I_recovery_count: 1
  methods: [6, 22, 27]
  new_route_results:
    - "Exact K=2 Seppalainen growth paths become lazy nearest-neighbor paths under t=i+j-1, y=j; row disorder remains columnar exponential-rate disorder."
    - "The direct Sly K=1 forced-coordinate coupling route fails at zero tilt because a K=2 lazy path can remain on one slow row, where the homogeneous-slow coupling bonus has zero conditional mean."
    - "The needed quantifier changes from every admissible path to the maximizing/near-maximizing path; the closest geometric transfer target is favorable-site pinning in product-type lazy-walk LPP."
  exact_blocker: "find delta>0 with [-1-delta,-1+delta] subset partial g_{2,Q}(0)"
  simplest_unproved_case: "strict zero-slope corner g'_-(0)<-1<g'_+(0) for frozen binary K=2 disorder"
  chosen_recovery: "port the favorable-site pinning/endpoint-cost technique from the nearest solved lazy-walk LPP analogue"
  next_methods: [3, 15, 28]
  remaining_obligation: "prove a quenched optimizer-pinning / linear endpoint-tilt cost that yields positive subgradient width at zero"
  new_exact_artifacts: none
```
