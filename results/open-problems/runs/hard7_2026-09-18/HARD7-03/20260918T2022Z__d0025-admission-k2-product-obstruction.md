Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **metric `L <= Delta_2(Q)`: `0 -> 0` (no movement); methods B2, B12, B18.** GPT-6/maximum was requested in prompt text, but this runtime exposes no authenticated reasoning-effort setting and the scheduler exposes no binding model/reasoning selector, so I do not claim otherwise.

# HARD7-03 — admission and first attack on Seppäläinen Problem 4

Date: 2026-09-18 UTC. Repository/branch: `yspennstate/math-open-problems` / `master`.

## 1. Admission and continuity

This is the first `HARD7-03` research report. I read the controlling HARD7 policy, the new-methods policy/directive, root `POSTED.md` and `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the relevant D-intake records, the earlier substantive attempt `D0025-A001`, and the neighboring R08 report `runs/R08/20260918T0030Z_d0024_resolution_d0025_plateau_screen_c7a4e2.md`.

The selected canonical source is **D0025**, Timo Seppäläinen, *Recent Results and Open Problems on the Hydrodynamics of Disordered Asymmetric Exclusion and Zero-Range Processes*, Resenhas IME-USP 4(1) (1999), 1–15, arXiv:math/9906194, Problem 4, Section 4. In the source's site-disordered totally asymmetric capacity-`K` exclusion process, the hydrodynamic flux `f_K` is concave; Problem 4 asks for rigorous information on the phase transition and, specifically, whether `f_K(rho)` has a flat segment around `rho=K/2`.

The current-literature check was deliberately scope-sensitive. Allan Sly, *Note on the flux for TASEP with general disorder*, arXiv:1609.06589, proves the plateau for ordinary `K=1` iid site-disordered TASEP. Bahadoran–Bodineau prove a `K=1` plateau under earlier quantitative hypotheses. Bahadoran–Guiol–Ravishankar–Saada (AIHP 50 (2014)) give broad quenched hydrodynamics for bounded attractive systems in random environment but do not supply a general-`K` plateau formula. Gonçalves–Hayashi–Sasada, arXiv:2405.15142, characterize product invariant measures for a class of asymmetric partial-exclusion processes through a gradient condition; this does not turn Seppäläinen's constant-rate asymmetric `K`-exclusion into a product-equilibrium model. Ayyer–Misra's 2024 exactly solvable `K`-exclusion is a different deformed-rate model. Searches dated 2026-09-18 for `disordered K-exclusion plateau`, `site disorder K-exclusion flux`, `general K TASEP site disorder plateau`, and equivalent formulations found no theorem closing the `K>=2` source scope. This supports only `OPEN_BY_BOUNDED_SEARCH`, not a claim of exhaustive worldwide openness.

Repository collision checks found **no canonical D0025 claim** before this run. R08 explicitly left the general-`K` residual as HARD and unclaimed after recording `K=1` as known. I therefore created `operations/claims/D0025.md` create-only and read it back at commit `1d32b96ba50f4139f2223b8cc474ff5917ec39e7`.

### Frozen first case and metric

I freeze the first source-valid case at

\[
K=2,\qquad Q=\tfrac12\delta_{1/2}+\tfrac12\delta_1,
\]

for iid **site** disorder. If `f_{2,Q}` is the deterministic hydrodynamic flux, define

\[
\Delta_2(Q)=\sup\{\delta\ge0:\ f_{2,Q}\text{ is constant on }[1-\delta,1+\delta]\}.
\]

The tracked quantity is a rigorously certified lower bound `L <= Delta_2(Q)`. Admission baseline: `L=0`, the trivial degenerate interval. The metric remains `0` after this run. This is **no movement** on the plateau width, but the run produces an exact obstruction that changes the proof strategy. Even a proof with `L>0` for this binary `K=2` environment remains PARTIAL for the full source problem.

The old `D0025-A001` observation that the iid site-disorder flux is symmetric around `K/2` by the appropriate particle-hole/reflection argument, and its qualitative slow-site bottleneck heuristic, are prior work and are not claimed again here.

## 2. B2 — attack the most tempting K=1 generalization first

The first obvious route is to imitate `K=1`: find a simple product equilibrium for the homogeneous `K=2` process, compute its current-density relation, then use long slow blocks to cap the disordered current. This route fails before disorder enters.

Consider the **homogeneous** totally asymmetric `K=2` process on the directed three-cycle with three particles. A state is a triple in `{0,1,2}^3` of total mass three; a particle jumps from site `x` to `x+1` at rate one whenever the source is nonempty and the target is not full. In lexicographic state order

\[
012,021,102,111,120,201,210,
\]

the exact stationary distribution is

\[
\pi=\frac1{11}(2,1,1,2,2,2,1).
\]

In particular

\[
\pi(012)=\frac2{11}\neq\frac1{11}=\pi(021).
\]

Any iid one-site product law on a three-cycle, conditioned on total mass three, assigns equal mass to `012` and `021`, because the two configurations have the same occupancy multiset `{0,1,2}`. Hence the actual stationary law is **not** the canonical conditioning of an iid product law. The naïve truncated-geometric/product-equilibrium route that works for symmetric partial exclusion is therefore already false for the source's asymmetric `K=2` dynamics.

This is consistent with the established literature: Seppäläinen's 1999 hydrodynamics was designed to avoid needing explicit invariant measures, and later work explicitly notes that translation-invariant stationary measures of asymmetric `K`-exclusion are not known in product form. Thus this finite certificate is an obstruction/check, not a novelty claim about the literature.

### Complete finite proof

The allowed transitions are

\[
\begin{array}{c|l}
012&\to111\\
021&\to012,120\\
102&\to012,201\\
111&\to021,102,210\\
120&\to111\\
201&\to111\\
210&\to120,201.
\end{array}
\]

All displayed arrows have rate one. Let `Q` be this generator. Direct substitution gives `pi Q=0`: for example the inflow to `012` is `pi(021)+pi(102)=2/11`, equal to its rate-one outflow `pi(012)=2/11`; the inflow to `111` is `pi(012)+pi(120)+pi(201)=6/11`, equal to its three-arrow outflow `3 pi(111)=6/11`; and the other five balance equations are checked identically from the table. Since the finite chain is irreducible in this mass sector, this is its unique stationary law. The product-conditioning contradiction above follows.

The exact Fraction-arithmetic checker is

`artifacts/hard7_2026-09-18/HARD7-03/k2_cycle_exact.py`

and its executed output is archived as

`artifacts/hard7_2026-09-18/HARD7-03/k2_cycle_exact.out`.

The checker verifies the seven states, the full generator balance, the orientation-asymmetric probabilities and the stationary current exactly; no floating-point inference is involved.

## 3. B12 — conserved current survives even though product equilibrium does not

There is still a robust invariant to organize the problem. For any finite ring in stationarity, let

\[
J_x=\mathbb E\!\left[\alpha_x\,\mathbf 1\{\eta(x)>0,\ \eta(x+1)<K\}\right]
\]

be the mean current across bond `x -> x+1`. Particle-number conservation at site `x` gives

\[
\frac{d}{dt}\mathbb E[\eta_t(x)]=J_{x-1}-J_x.
\]

Consequently every stationary finite-volume current is bond-independent. In the exact homogeneous three-cycle certificate above,

\[
J_0=J_1=J_2=\frac6{11}.
\]

This identity is elementary but important for the disordered route: a long block of slow sites cannot be analyzed bond-by-bond with unrelated local currents. Whatever stationary or variational object replaces the missing product equilibrium must carry one common through-current across the entire block.

The conservation identity alone does not improve `L`: it supplies structure, not a plateau lower bound.

## 4. B18 — recast the plateau problem as a long-slow-block extremal-current problem

The exact finite obstruction suggests a replacement for the failed product-measure strategy.

For `K=1`, Sly's plateau proof can use the special last-passage/exponential representation to identify the slow-rate current ceiling and then match it. For `K=2`, the small-cycle certificate shows that even the **homogeneous** constant-rate process already has a non-product stationary law. A correct generalization therefore should not begin by guessing one-site marginals. It should begin with a current variational problem that is meaningful without explicit equilibrium.

The proposed next object is a finite-volume maximal-through-current envelope for a length-`m` homogeneous slow block, with capacity `2`, internal rate `c=1/2`, and boundary reservoirs allowed to feed and drain the block. The boundary convention must be chosen so that it dominates every restriction of the infinite iid environment. If `C_m` denotes the resulting rigorously defined maximum stationary through-current, the desired comparison architecture is:

1. **Upper comparison:** every occurrence of an `m`-site all-slow block in the iid environment forces `f_{2,Q}(rho) <= C_m` for every density `rho`.
2. **Limit:** prove `C_m` decreases/converges to a homogeneous maximal-current constant `C_infty` without assuming product equilibrium.
3. **Matching lower bound near density one:** construct a coupling/renormalization proving `f_{2,Q}(rho) >= C_infty` on a nontrivial interval around `rho=1`.

Then the interval in step 3 is exactly a positive certified contribution to `L`.

This is not yet a theorem: the correct reservoir domination and the matching lower bound are the remaining obligations. But it turns the vague instruction “generalize Sly to `K=2`” into two source-matching inequalities and deliberately avoids the false product ansatz exposed above. The most immediate mathematical target for the next run is to define `C_m` so that monotonicity/domination is actually provable in the Harris construction and to compute the first exact `m` values only after that definition is fixed.

## 5. Why this is a real obstruction rather than checker churn

The exact finite calculation changed the route. A product equilibrium would have reduced the slow-block current to a one-parameter marginal optimization. The certificate proves that this simplification is invalid already on the smallest nontrivial half-filled `K=2` ring. The current must instead encode spatial correlations/orientation. That is precisely the structural feature a general-`K` plateau proof has to control.

No claim is made that the seven-state stationary vector is new to the literature. Its role is to kill a proof architecture exactly, before spending runs developing lemmas inside it.

## 6. Status and next obligation

- Source status: `OPEN_BY_BOUNDED_SEARCH` for the `K>=2` residual; `K=1` plateau KNOWN.
- Worker status: `PARTIAL`.
- Metric: `L: 0 -> 0`, **no movement**.
- This run's genuine outputs: canonical admission/ownership, a frozen `K=2` binary-disorder metric, and an exact finite proof that the simplest product-equilibrium continuation of the `K=1` argument is impossible.
- Next methods must not repeat `[2,12,18]`.
- Next obligation: construct a source-valid finite slow-block maximal-current envelope `C_m` with a proved domination relation to the infinite iid site-disordered `K=2` process; only then compute/optimize it and seek a matching lower bound near density one.

## 7. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-03
  source: D0025
  owner_claim: operations/claims/D0025.md
  claim_commit: 1d32b96ba50f4139f2223b8cc474ff5917ec39e7
  status: PARTIAL
  current_source_status: OPEN_BY_BOUNDED_SEARCH
  known_exclusion: K=1 iid site-disorder plateau
  frozen_case:
    K: 2
    site_rate_law: "1/2 delta_{1/2} + 1/2 delta_1"
  metric: "certified lower bound L <= Delta_2(Q)"
  before: 0
  after: 0
  movement: no
  methods: [2, 12, 18]
  exact_finite_certificate:
    claim: "homogeneous K=2, L=3 ring, N=3 stationary law is (2,1,1,2,2,2,1)/11 and is not a canonical iid-product conditioning"
    checker: artifacts/hard7_2026-09-18/HARD7-03/k2_cycle_exact.py
    output: artifacts/hard7_2026-09-18/HARD7-03/k2_cycle_exact.out
  remaining_obligation: "Define and prove a slow-block maximal-current envelope that dominates the infinite disordered flux, then seek a matching lower bound near rho=1."
```
