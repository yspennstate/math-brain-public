Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed. **P0336 `SEL_ID: 0 -> 0` (NO MOVEMENT); methods B4 / B9 / B20; ordinary unchanged count `5 -> 6`; status OPEN / PARTIAL / CLOSABLE retirement threshold reached.**

# P0336 six-run handoff — the selector has moved below tangent order into a renormalized gluing problem

Date: 2026-09-19 UTC  
Worker: `R7-05 Sharp Inequality Research`  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Repository: private `yspennstate/math-open-problems`, branch `master`  
Run-start snapshot: `266149e02e270206fbfbd5795b2d14332552d1aa`  
Fresh pre-delivery snapshot: `79029c57d55860a80a5d130c69875ac62d5d7b9d`  
Canonical claim: `operations/claims/P0336.md`  
Admission: `research7_2026-09-17/R7-05/admissions/2026-09-19T074900Z__P0336_admission.md`  
Previous immutable own report: `research7_2026-09-17/R7-05/runs/2026-09-19/2026-09-19T124922Z__report.md` @ `44b585da383edb65b4616b4f54cb47bb8f3a437d`.

## 1. Exact outside source and closure target

Eustasio del Barrio, Alberto González-Sanz, Jean-Michel Loubes, David Rodríguez-Vítores, *Distributional Limit Theory for Optimal Transport*, arXiv:2505.19104v2 (13 July 2026), Problem 4.

The literal source asks for the limit of the empirical Euclidean optimal-transport plan between two independent iid samples from `U([0,1]^2)` and `U([2,3]×[0,1])`. The population Euclidean problem has a large flat optimal face because the supports are horizontally separated. The frozen R7-05 metric was

`SEL_ID = 0`

and may become `1` only after complete identification/refutation of the source-level limiting empirical plan. It never moved.

A bounded current-source/follow-up check on 2026-09-19 still found v2 as the current primary source and did not surface a later exact theorem settling this empirical-plan selection question. That is negative evidence only, not a worldwide novelty/openness certificate.

## 2. Cumulative mathematics to preserve

The useful R7-05 results, in dependency order, are:

1. **Exact excess decomposition.** For a matched pair `X=(A,S)`, `Y=(B,T)`, with `D=B-A>0` and `H=T-S`,

   `|X-Y| = D + [sqrt(D^2+H^2)-D]`,

   while the sum of all `D` terms is matching-independent. Selection is entirely in the Euclidean excess.

2. **Horizontal sorting is false.** Exact 2×2 configurations show that arbitrarily small vertical perturbations can make either the horizontally monotone or crossed assignment strictly cheaper. There is no direct uncrossing proof to translation.

3. **Quadratic fiber degeneracy.** At vertical scale `Z=sqrt(n)H`, for every horizontal coupling with the prescribed uniform marginals,

   `E[Z^2/(2D)] >= m^2/4`,

   with equality exactly at the common-slope field `Z=(m/2)D`. Every horizontal coupling can attain equality.

4. **All local ray orders are flat.** Along `H=rD`, the exact Euclidean excess is `D(sqrt(1+r^2)-1)`. Because every horizontal coupling has `E[D]=2`, every Taylor coefficient along the common-slope ray is coupling-independent.

5. **Full smooth marked tangent problem is flat.** With a vertically varying bistochastic horizontal kernel `k(a,b,s)`, arbitrary smooth marked source/target perturbations, first-order edge-density correction `q` and displacement `u`, the exact tangent constraints reduce the energy-carrying part to scalar vertical flux `m(s)`. The minimum is

   `(1/4) int m(s)^2 ds`,

   attained by `u=(m/2)(b-a)` for every strictly positive `k`; an explicit `q` realizes the complete marked constraints.

6. **Two-bin singular tangent cones are also flat.** Both permutation endpoints of the two-horizontal-bin model attain the same second-order tangent energy. Boundary singularity alone does not select.

7. **A genuine sub-tangent local bias exists.** For an ordered 2×2 Gaussian microcell the quadratic monotone-minus-crossed difference has one positive and one negative eigenvalue. For horizontal marks `0,1` against `2,3`, the eigenvalues are `1/2` and `-5/6`; monotone wins with probability `1/2+arcsin(1/4)/pi` and lower mean cost.

8. **Strict Monge expected residual.** For a fixed horizontal permutation under independent unit-variance vertical jitter, expected quadratic residual is `sum 1/(b_pi-a)`. The effective cost `1/(b-a)` is strictly Monge, and its continuum relaxation

   `J(kappa)=int (b-a)^(-1) d kappa`

   has unique minimizer `b=a+2` (translation). Exact benchmarks: translation `1/2`, product `log(27/16)`, antimonotone `(1/2)log 3`.

9. **Exact two-bin contingency reduction.** In the balanced two-bin empirical model every horizontal contingency is one integer `k=N_02=N_13`, with `N_03=N_12=m-k`. Exact vertical-cut conservation shows how cross-horizontal edges absorb prefix imbalance. Matching is Monge only *within a fixed horizontal cell*, not globally.

10. **Penalty-value representation.** If `C_m(k)` is the constrained residual value, `Phi_m(h)=min_k[C_m(k)+hk]` has a nonincreasing optimizer in `h`. The empirical selected contingency is the zero-field sensitivity. Every nontrivial macroscopic competition lies inside an `O(1/m)` conjugate-field window.

11. **Brownian endpoint limit is random.** Pure monotone versus pure crossed in the balanced two-bin model satisfies

   `C_m(m)-C_m(0) => Delta=(1/2)I_+-(5/6)I_-`,

   where `I_+,I_-` are iid `int_0^1 B^2`; `E Delta=-1/18`, `Var Delta=17/810`, and both signs occur. One macroscopic block does not self-average.

12. **Fixed-orientation innovation homogenization.** After coarse endpoints are frozen and Brownian bridges are decomposed into `K` equal independent bridge innovations,

   `G_M(K)-G_C(K) =_d K^{-2} sum_{j=1}^K Delta_j`,

   so `K(G_M-G_C) -> -1/18` in `L^2`. This proves deterministic local bias only when the orientation is fixed in advance.

13. **Smooth cubic density reweighting is flat.** The most obvious next Taylor correction vanishes after integration by parts, so `J(kappa)` is not generated by that smooth cubic route.

14. **Terminal-run adaptive-block theorem.** Let `q_*=P(Delta<0)`. The Brownian bridge energy has a nonatomic full-support law, hence `1/2<q_*<1`. If each independent mesoscopic block may choose monotone or crossed after seeing its local innovation, the optimizer chooses monotone exactly on `{Delta_j<0}` and the monotone block fraction converges almost surely to `q_*`. The associated two-bin coupling parameter converges to

   `p_*=q_*/2 in (1/4,1/2)`,

   a strict interior mixture rather than translation.

15. **Exact constrained adaptive homogenization.** If exactly `r_K~alpha K` blocks must be monotone, the minimum is the sum of the `r_K` smallest innovations and

   `(1/K)V_K(r_K) -> G(alpha)=int_0^alpha F_Delta^{-1}(u)du` a.s.

   The unique minimizer is `alpha=q_*`, and the adaptive mixture beats pure translation by

   `G(1)-G(q_*)=E[Delta_+]>0`.

16. **Conditioned/restricted empirical realization.** In a source-faithful balanced two-bin surrogate, condition each horizontal line to have exactly `q` points in each of `K` vertical slabs and restrict matching to each slab. For fixed `K`, then `q->infinity`, the slab endpoint differences times `K^2` converge jointly to iid `Delta_j`; then `K->infinity` yields the same strict interior adaptive effective functional. Thus random/local adaptation is not an artificial Gaussian-only phenomenon.

The terminal derivation is archived at

`research7_2026-09-17/R7-05/artifacts/2026-09-19/2026-09-19T135100Z__P0336_adaptive_block_homogenization_obstruction.md`

creation commit `9ddeaa10fde3133f9382f2ac189068ecb480f80f`, exact-commit readback completed.

## 3. Exact remaining blocker

The previous preferred route to translation is now invalid unless a global compatibility term defeats adaptive block choice.

The genuine empirical problem has random per-slab marked counts and allows cross-slab edges. Its marked-prefix constraints couple local horizontal orientations. The leading cost of correcting those count imbalances is largely the universal coarse/common-slope term already proved flat in the horizontal kernel, so raw rerouting counts are not the selector.

The exact remaining object is the **kernel-dependent renormalized gluing defect after subtracting the universal coarse-prefix energy**. At a valid joint mesoscopic scale it must be compared with the adaptive innovation gain. In the terminal block normalization, pure translation loses to locally adaptive orientation by

`E[Delta_+]/K + o(1/K)`.

Therefore a future proof of translation must show either:

- the global prefix/permutation constraints force the horizontal orientation to be essentially constant, or
- the renormalized gluing penalty of a sign-adaptive orientation field is at least `E[Delta_+]/K` at the same scale.

If instead that defect is `o(1/K)`, the independent-block theorem rules out the naive translation-selector mechanism and points to an interior/nonlocal selector.

The simplest unresolved laboratory remains the genuine unconditioned two-horizontal-bin empirical model with random slab counts and unrestricted cross-slab matching. Its scalar contingency `k` is source-faithful enough to expose the gluing mechanism while retaining exact marked-prefix conservation.

## 4. Why R7-05 stops P0336 here

Frozen metric accounting:

```text
SEL_ID before: 0
SEL_ID after:  0
movement: NO MOVEMENT
ordinary unchanged count: 5 -> 6
```

This is the sixth ordinary no-movement research iteration in the CLOSABLE P0336 cycle. The owner protocol requires retirement/handoff rather than indefinite equivalent refinement.

Therefore **R7-05 retires P0336 from further source research now**. This is an operational worker-local handoff. It is not a source-level proof, refutation, known-result determination, posting, or protocol closure. Mathematical status remains **OPEN / PARTIAL**. No independent P26 full-source audit and no distinct OTHER-track full-source audit exist. The canonical claim file is preserved and not overwritten; stale scheduler state or this retirement must not be treated as ownership release by another worker without the owner protocol.

## 5. Fresh shard-4 successor screen

The case-sensitive shard predicate is `sum(ord(c) for c in ID) % 7 == 4`. The partition is not ownership.

The current ranked queue and the remaining F/G/H cursor were rechecked after retirement. No lawful fresh CLOSABLE successor was found:

- Queue-facing `I0066`, `I0113`, `I0032`, `I0075`, `RS-2026-CL-B` have canonical ownership/history and are unavailable.
- `I0048` and `I0050` were previously source-reconciled by this worker: their clean clauses are later-known or their surviving residuals are HARD, not a newly frozen CLOSABLE endpoint.
- `D0012` remains a broad/scope-held aggregation problem; the exact Bernoulli subclass proved earlier by R7-05 does not close the outside source.
- Remaining F residue-4 entries after the prior cursor `F0080`: `F0087` has a strong later-literature lead to Dubedat electric-correlator results and is not safe as fresh inventory; `F0096` Hamiltonicity at all densities `c>=3/2`, `F0100` Talagrand ultimate matching, `F0116` critical census reconstruction for general channels, and `F0125` the entropy criterion for scenery reconstruction are theorem-sized HARD targets; `F0107` has later positive literature/campaign resolution evidence; `F0134` is resolved in the literature/source itself.
- The complete current G intake has one residue-4 row, `G0007`, and `operations/claims/G0007.md` exists; unavailable.
- The current H residue-4 rows are `H0006` (broad finite-size-scaling programme, HARD), `H0015` (duplicate of `C0091`), and `H0024` (previously retired by this same native worker and still canonically claimed); none is a lawful fresh successor.

No stale queue row, disabled task, missing report, or retired target was treated as release. No successor claim is created in this handoff. R7-05 returns to **PENDING_ADMISSION** with successor metric `UNKNOWN/UNMEASURED` and no inherited stagnation count.

## 6. ledger_delta

```yaml
ledger_delta:
  track: R7-05
  native_id: 6aabe805f32881919992996e1c5cfad6
  target_id: P0336
  report_kind: sixth_ordinary_research_and_terminal_handoff
  input_snapshot_sha: 266149e02e270206fbfbd5795b2d14332552d1aa
  fresh_pre_delivery_sha: 79029c57d55860a80a5d130c69875ac62d5d7b9d
  previous_report_path: research7_2026-09-17/R7-05/runs/2026-09-19/2026-09-19T124922Z__report.md
  previous_report_commit: 44b585da383edb65b4616b4f54cb47bb8f3a437d
  fixed_metric: SEL_ID
  before: 0
  after: 0
  movement: NO_MOVEMENT
  ordinary_unchanged_count_before: 5
  ordinary_unchanged_count_after: 6
  methods: [B4, B9, B20]
  new_terminal_result: adaptive_independent_block_effective_functional_has_unique_interior_minimizer
  mathematical_status: OPEN_PARTIAL
  operational_status_after: RETIRED_HANDOFF_PENDING_FRESH_ADMISSION
  audits:
    p26: none
    other: none
  successor_state: PENDING_ADMISSION
  successor_metric: UNKNOWN_UNMEASURED
  successor_stagnation_count: NOT_STARTED
  successor_claim_created: false
```
