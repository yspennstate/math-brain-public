Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. **NO MOVEMENT in the frozen metric** `c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`; methods actually tried this run: **B5, B21, B22**. Substantive route result: a full-bulk finite imitation of the exact inward strip controller pays an explicit i.i.d. entropy cost `<= 4^{-R(2R+1)^(d-1)}`, while every radius-`R` cube has quenched mean exit time at most `(R+1) kappa^{-(R+1)}`; in `d>=2` their product is summable in `R`. This eliminates one natural coherent-trap transfer route but does not prove P0483.

# NM13-12 — P0483 i.i.d. inward-template entropy barrier

Date: 2026-09-17 UTC  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical source / claim ID: `P0483`  
Canonical dedup key: `directional_transience_versus_positive_speed_under_uniform_ellipticity`  
Historical intake alias: `C0041`  
Overall source status after this run: **OPEN**  
Local status: **PARTIAL / route theorem; frozen metric unchanged**

## 1. Runtime/model disclosure and scheduler-control reality

The requested header asks for GPT-6 with maximum reasoning. That is **not** what I can verify ran. The actual model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The task-control interface available to this runtime still exposes prompt/title/schedule/timing/enabled fields but no binding model-family selector and no reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text, not a scheduler-enforced setting. Changing that requires an authorized scheduler/product surface that actually exposes those controls. I did not create or modify any schedule.

Repository history records a `You cannot modify this task` failure for P26/P01/P03 in one earlier scheduler context, while current `RESULTS.md` records that a later P26 full update succeeded in another authorized context. I therefore do not treat the old P26 denial as a permanent global state. If such a denial recurs for a particular task, the lawful remedy is the owning account/workspace or an authorized platform/admin surface; this worker does not bypass the ACL or create a duplicate job.

## 2. Continuity recovered before new mathematics

This is a continuation of the already-admitted P0483 source, not a new intake selection. The existing create-only claim `operations/claims/P0483.md` remains owned by NM13-12; no new claim was created or overwritten.

Before doing mathematics I recovered/read the controlling/current material:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- the later NM13 deployment record `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md` and targeted searches for later owner-authorized corrections;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/P0483.md`;
- the P0483 campaign/catalog record and intake alias/dedup material;
- the newest two prior NM13-12 reports, especially `proofnet24/NM13-12/runs/2026-09-17/2026-09-17T21-50-29Z__p0483-exact-strip-operator.md`;
- newest neighboring reports `proofnet24/NM13-11/runs/2026-09-17/2026-09-17T21-48-00Z__H0003-pf-coboundary-critical-stability.md` and `proofnet24/NM13-13/runs/2026-09-17/2026-09-17T21-55-54Z__f0013-exact-n5-modular-certificate.md`;
- targeted repository searches for `P0483`, `C0041`, the canonical dedup key, source title, prior finite-trap attempt, current claims, handoffs and assignments.

The campaign catalog preserves the prior attempt: if every point of a finite set has an escape path of length at most `m`, uniform ellipticity gives a geometric block-exit bound and `E tau_A <= m kappa^{-m}`; the unresolved obstruction was the random size/shape of regeneration excursions. No newer conflicting owner, release, handoff, retirement, posted result, or source closure was recovered. Large ledgers are connector-bounded, so this is a targeted/current continuity recovery rather than a claim of byte-for-byte omniscience.

## 3. Fresh bounded source/literature status check

Dated search: **2026-09-17 UTC**. Queries covered the exact source phrase and combinations of `directional transience`, `positive speed`, `uniformly elliptic`, `iid`, `RWRE`, `ballisticity`, `2025`, `2026`, together with Drewitz–Ramírez, Guerra–Ramírez, Fribergh–Kious, later regeneration-tail work, and citing literature.

The source remains Drewitz–Ramírez Open Question 2.20: for nearest-neighbor i.i.d. uniformly elliptic RWRE on `Z^d`, `d>=2`, does directional transience imply ballisticity / positive limiting speed in that direction?

The current bounded check recovered the following controlling neighbors:

1. **Guerra–Ramírez, CPAM 2020, DOI 10.1002/cpa.21877.** Their abstract still states that in uniformly elliptic i.i.d. RWRE it is *believed* that directional transience implies ballisticity; their theorem proves equivalence of the standard stronger ballisticity conditions rather than P0483.
2. **Fribergh–Kious, PTRF 2016, DOI 10.1007/s00440-015-0646-4.** Their introduction states the same conjecture and pinpoints the difficulty: uniform ellipticity controls local trapping, while the missing issue is global exploration / ruling out large-scale zig-zagging. Their non-uniformly-elliptic results show how local hypercube traps can force zero speed, so they are a close failure-mechanism comparator rather than a source resolution.
3. **Guerra, arXiv:2006.00570 (2020).** The stronger transience-to-`(T)` program proves `(T)` from a polynomial condition of degree greater than `d-1`; qualitative directional transience alone still does not provide that quantitative slab estimate.
4. **Tal Peretz, 2025 version of arXiv:2204.12238.** This gives invariant-environment and regeneration-tail results in low dimensions under ballisticity condition `(T)`, not from directional transience alone.

No 2025–2026 source-matching theorem closing P0483 was recovered in the bounded search. This is **bounded negative evidence only**, not proof of worldwide openness and not a novelty certificate for the elementary route lemma below.

## 4. Frozen metric — deliberately unchanged

The frozen task metric is still

`c_slab^(d)(kappa,w)` = the optimal universal exponential exit-tail rate from subsets of a coordinate strip of width `w`, over all static nearest-neighbor environments with transition probabilities at least `kappa`.

The preceding run proved exactly

`c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`,

where `K_{d,w}(kappa)` is the explicit finite inward-control birth-death operator.

**Before this run:** `= -log rho(K_{d,w}(kappa))` exactly.  
**After this run:** `= -log rho(K_{d,w}(kappa))` exactly.  
**Movement:** none.

I do not rename the new entropy quantity below as the task metric. The exact strip metric is saturated; the purpose of this run is to test whether its extremal mechanism can survive the source's i.i.d. constraint.

This is the first unchanged run after the preceding movement, so `unchanged_runs = 1`. Hard stuck-recovery episodes used remain `0`.

---

# 5. B5 — deform from the solved correlated model and parameterize the transfer error

The source itself contains the right diagnostic endpoint: a two-dimensional uniformly elliptic **ergodic but transversely correlated** environment can be constant in the transverse direction and reduce its longitudinal coordinate to a one-dimensional RWRE. With the usual one-dimensional choice satisfying negative mean log-bias but critical/nonintegrable speed criterion, the walk is transient in the longitudinal direction and has zero speed. This is classical/source material, not a new counterexample and not admissible for P0483 because the environment is not i.i.d. over sites.

That solved endpoint identifies the exact structural resource used by the one-dimensional trap: **transverse coherence**. A bad longitudinal stretch is repeated across an entire transverse line, so the walk cannot bypass it by stepping sideways into an independently resampled site.

The preceding exact strip extremizer `omega_*` has the same kind of coherence in a different form: on one side of the strip center it gives the maximal admissible bias toward the center, and on the other side it reverses that bias. For `kappa<1/(2d)`, its inward/outward longitudinal ratio is

`r_* = [1-(2d-1)kappa]/kappa > 1`.

I first tried the literal B5 proposal from the previous report: impose a deterministic defect `delta` from `omega_*` and seek a uniform Perron–Frobenius penalty. For a fixed finite operator this does give strict spectral loss whenever a positive entrywise defect is imposed, but it does **not** transfer to the source: an i.i.d. environment has random defects at random sites, not a uniform rowwise defect. The missing input immediately becomes a large-deviation estimate for maintaining small defect over a whole trapping region.

So I parameterize that missing input directly. Fix one coordinate `e_1` and a bias threshold `r>1`. For a one-site transition vector `p`, define the two opposing local classes

`A_+(r) = { p(e_1) >= r p(-e_1) }`,

`A_-(r) = { p(-e_1) >= r p(e_1) }`.

They are disjoint for every `r>1`. If `1<r<=r_*`, the two noncentral halves of the exact strip controller lie in `A_+` and `A_-`, respectively. The i.i.d. transfer problem can therefore be asked without requiring exact equality to `omega_*`: how expensive is it merely to maintain the **sign-reversing fixed-strength bias** throughout a finite bulk region?

That question has an exact answer.

---

# 6. B21 — import the product-template entropy calculation

The relevant shape is the elementary method-of-types / product-template entropy bound. I record it because it makes the i.i.d. cost explicit and distribution-free.

### Lemma `NM13-12-P0483-TEMPLATE-ENTROPY-03`

Let `(omega_x)_{x in Z^d}` be i.i.d. with one-site law `mu`. Let `B_1,...,B_K` be pairwise disjoint measurable one-site events with probabilities `q_i=mu(B_i)`. Let `V` be a finite set of `N` sites and let `a:V->{1,...,K}` be a prescribed template using label `i` exactly `n_i` times, with `p_i=n_i/N`. Then

`P[ omega_x in B_{a(x)} for every x in V ]
 = product_i q_i^{n_i}
 <= product_i p_i^{n_i}
 = exp[-N H(p)]`,

where `H(p)=-sum_i p_i log p_i` and zero-count labels are omitted.

#### Proof

Independence gives the equality. Since the `B_i` are disjoint,

`sum_i q_i <= 1`.

For all `p_i>0`, weighted AM-GM gives

`product_i (q_i/p_i)^{p_i}
 <= sum_i p_i (q_i/p_i)
 = sum_i q_i
 <= 1`.

Multiplying by `product_i p_i^{p_i}` and raising to the power `N` proves the result. `square`

This is standard product-measure entropy machinery; I make **no novelty claim** for the general lemma.

## 6.1 Exact inward-template specialization

Let

`Q_R(z) = z + [-R,R]^d intersect Z^d`, `R>=1`,

and define `I_R(z;r)` to be the event that

- every `x in Q_R(z)` with `x_1<z_1` has `omega_x in A_+(r)`, and
- every `x in Q_R(z)` with `x_1>z_1` has `omega_x in A_-(r)`.

The center hyperplane `x_1=z_1` is left unconstrained. Each half contains exactly

`M_R = R(2R+1)^(d-1)`

constrained sites. Put `q_+=mu(A_+)`, `q_-=mu(A_-)`. Because `A_+` and `A_-` are disjoint,

`q_+ + q_- <= 1`, hence `q_+ q_- <= 1/4`.

Therefore, exactly by site independence,

`P[I_R(z;r)]
 = (q_+ q_-)^{M_R}
 <= 4^{-M_R}
 = exp[-(log 4) R(2R+1)^(d-1)].`                 (6.1)

The constant `1/4` is the sharp distribution-free product bound for two disjoint local classes; when the two classes each have mass `1/2`, equality holds in the one-site entropy optimization. The statement is not that such a law is directionally transient; only the product penalty is sharp.

For `kappa<1/(2d)` and any `1<r<=r_*`, every exact finite realization of the previous run's sign-reversing strip controller inside `Q_R(z)` is a subset of `I_R(z;r)`. Thus (6.1) bounds a **broader** approximate-controller event, not just exact equality to one transition vector.

## 6.2 Encounter bound in an `n`-step accessible region

There are at most `(2n+1)^d` possible cube centers in `[-n,n]^d`. No independence between translated cubes is needed for the union bound:

`P[ exists z in [-n,n]^d : I_R(z;r) ]
 <= (2n+1)^d 4^{-R(2R+1)^(d-1)}.`                (6.2)

If `R=ceil(a log n)` for any fixed `a>0` and `d>=2`, then the logarithm of the right side is

`d log(2n+1) - Theta((log n)^d)`,

so the bound decays faster than every negative power of `n`. In `d=1` the entropy exponent is only linear in `R`, exactly the scale on which one-dimensional trapping can compete. This is the first clean dimension-sensitive obstruction produced by the transfer route.

---

# 7. Exact quenched lifetime comparison

The previous campaign attempt used a general escape-path block argument. For the centered cube the path length can be taken slightly more sharply than the old `2R+1` choice.

### Lemma `NM13-12-P0483-CUBE-EXIT-04`

For every nearest-neighbor environment with all transition probabilities at least `kappa`, every center `z`, every `R>=1`, and every `x in Q_R(z)`, if `tau_R` is the first exit time from `Q_R(z)`, then

`P_{x,omega}[tau_R > m(R+1)] <= (1-kappa^(R+1))^m`,                  (7.1)

and hence

`E_{x,omega} tau_R <= (R+1) kappa^{-(R+1)}.`                         (7.2)

#### Proof

From any point of `Q_R(z)`, choose a coordinate whose absolute displacement from `z` is maximal and walk in the nearer outward direction until leaving the cube. The required path has length at most `R+1`. Its quenched probability is at least `kappa^(R+1)`. Conditional on survival to the beginning of each block of `R+1` steps, the same statement applies from the current point. The strong Markov property gives (7.1); summing the geometric block tail gives (7.2). `square`

Combining (6.1) and (7.2), for a fixed center,

`E[ 1_{I_R(z;r)} E_{z,omega} tau_R ]
 <= (R+1) kappa^{-(R+1)} 4^{-R(2R+1)^(d-1)}.`                       (7.3)

For every `d>=2`,

`sum_{R>=1} (R+1) kappa^{-(R+1)} 4^{-R(2R+1)^(d-1)} < infinity`,     (7.4)

because the positive lifetime exponent is only `O(R)` while the i.i.d. template penalty is `-Theta(R^d)`.

Equation (7.4) is a rigorous **route exclusion**, not a regeneration theorem: a family of full-bulk, fixed-strength, sign-reversing inward cubes cannot create an infinite annealed delay merely by summing its occurrence probability times the worst possible cube mean exit time over scales. It does **not** rule out sparse traps, anisotropic corridors, surface-supported barriers, dynamically selected regions, or large-scale zig-zagging. In particular it does not prove finite mean regeneration time.

No numerical or floating-point claim is needed here, so I did not manufacture a checker artifact for this analytic argument.

---

# 8. B22 — read the failures: why the source obstruction survives

The literature and the calculation above now line up unusually cleanly.

Fribergh–Kious explicitly describe P0483 as a tension between a **global** directional-transience hypothesis and the **local** anti-trapping effect of uniform ellipticity; their stated difficulty is ruling out large-scale zig-zagging. The previous exact strip theorem solved a local coherent-control problem. The present entropy calculation shows why simply implanting that coherent controller into an i.i.d. bulk is too expensive in `d>=2`: the environment pays a volume-order product penalty while uniform ellipticity bounds the mean lifetime of a radius-`R` finite trap by an exponential in only `R`.

Guerra's 2020 work exposes the same gap from the other side. A sufficiently strong polynomial unlikely-exit estimate (degree `>d-1`) can be promoted to `(T)`, but qualitative transience does not supply that estimate. The present route does not bridge the gap: it controls one rigid family of adverse environments, not the full unlikely-exit event.

The more recent low-dimensional regeneration-tail work recovered in the bounded search assumes condition `(T)`. It therefore cannot be used circularly to derive `(T)` or finite regeneration mean from directional transience.

**Precise failure of this route:** after eliminating coherent full-bulk inward traps, the hard source-level possibility is an environment/walk geometry in which delay is produced with much less than volume-order environmental organization — for example a sparse sequence of barriers, a thin anisotropic cutset, or repeated large-scale backtracking/zig-zagging. None of B5/B21/B22 supplies a quantitative bound on those mechanisms.

This is why I stop this trap-template route here rather than add another local lemma to the exact strip calculation.

## 9. Source status, counters, audits, and next route

P0483 remains **OPEN**. The new lemmas are **PARTIAL route information** and do not change the exact frozen strip metric.

- frozen metric: `-log rho(K_{d,w}(kappa)) -> -log rho(K_{d,w}(kappa))` (**no movement**);
- unchanged-run count: `0 -> 1`;
- hard stuck-recovery episodes used: `0`;
- P26 audit: not requested / not passed;
- NM13-13 secondary audit: not requested / not passed;
- closure: false.

The next run should not continue optimizing a bulk inward trap. It should attack the global-exploration obstruction directly with three methods not yet used on P0483:

- **B1 — change category:** recast a bad regeneration excursion / unlikely slab exit as a random directed-network or cutset problem, so sideways bypasses are explicit objects rather than an informal objection;
- **B11 — dualize:** seek a max-flow/min-cut or harmonic-flow certificate showing that every adverse longitudinal barrier requires a sufficiently large low-conductance transverse cutset;
- **B28 — replace for-all with typical:** first prove a high-probability i.i.d.-environment bypass statement at one scale, with explicit error, before attempting a multiscale induction.

A useful one-scale target is: in a source slab of length `L`, certify that every transverse cutset capable of forcing a backward/slow excursion must contain at least `c L^{d-1}` sites from an explicitly adverse local class, then combine site independence with a counted family of cutsets. If this cannot be made source-valid without assuming the desired ballisticity condition, record that failure and rotate method rather than hiding it in a multiscale assertion.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: P0483
  claim_id: P0483
  canonical_dedup_key: directional_transience_versus_positive_speed_under_uniform_ellipticity
  source_status: OPEN
  local_result_status: PARTIAL
  metric: c_slab(kappa,w)
  metric_scope: fixed source dimension d>=2; all static nearest-neighbor kappa-uniformly elliptic environments; all subsets of a coordinate strip of width w
  before: "= -log rho(K_{d,w}(kappa)) exactly"
  after: "= -log rho(K_{d,w}(kappa)) exactly"
  movement: false
  unchanged_runs: 1
  stuck_recoveries_used: 0
  hard_recovery_limit: 2
  theorem_ids:
    - NM13-12-P0483-TEMPLATE-ENTROPY-03
    - NM13-12-P0483-CUBE-EXIT-04
  route_result: "For a full-bulk fixed-strength sign-reversing inward template in a radius-R cube, P(event)<=4^{-R(2R+1)^(d-1)}; every kappa-UE cube has mean exit <=(R+1)kappa^{-(R+1)}; the product is summable for d>=2."
  novelty_label: "elementary product-entropy / escape-path route lemma; no general-method novelty claim"
  methods_actual:
    - B5
    - B21
    - B22
  methods_outcome:
    B5: "partial success — a uniform spectral-defect interpolation does not match random iid defects; threshold parameter r>1 exposes the exact sign-reversal coherence event"
    B21: "success as route diagnostic — product-template/method-of-types entropy gives an exact distribution-free iid cost and a superpolynomial log-scale encounter bound in d>=2"
    B22: "success as obstruction diagnosis — current failure literature and the new bound agree that local/coherent traps are not the missing step; sparse/global zig-zagging remains uncontrolled"
  audits:
    P26: not_requested
    NM13-13: not_requested
  closure: false
  next_methods:
    - B1
    - B11
    - B28
  next_step: "attack global zig-zagging via a one-scale transverse cutset/bypass formulation; obtain an explicit cutset size and iid rarity bound before any multiscale induction"
  literature_check_date_utc: 2026-09-17
  literature_scope: "exact P0483 phrase; Drewitz-Ramirez; Guerra-Ramirez; Fribergh-Kious; Guerra transience-to-(T); bounded 2025-2026 later/citing work including Peretz"
  literature_limit: "bounded repository/web search; not proof of worldwide openness or publication novelty"
```

**End of complete run report.**
