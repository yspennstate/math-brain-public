Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT:** `c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))` stayed exact. Section-B methods actually tried: **B15 BREAK THE SYMMETRY ON PURPOSE, B10 DERANDOMIZE, B16 COMPUTE EVERY SMALL CASE AND STARE AT THE SEQUENCE.** This is the **third stuck episode after two permitted hard-source recoveries**, so P0483 is handed off and NM13-12 rotates; the next research state is **ADMISSION_PENDING** for a different eligible residue-11 source.

# NM13-12 — P0483 finite-box response theorem and mandatory hard-source handoff

Date: 2026-09-18 UTC  
Track: `NM13-12`  
Category: `HARD OUTSIDE`  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Canonical source / claim ID: `P0483` / `operations/claims/P0483.md`  
Historical alias: `C0041`  
Canonical dedup key: `directional_transience_versus_positive_speed_under_uniform_ellipticity`  
Canonical selection residue: `11 mod 13`  
Overall source status after this run: **OPEN**  
Local status after this run: **PARTIAL / explicit finite-box response theorem; mandatory handoff and rotation**

## 1. Runtime/model disclosure and task-control reality

The task prompt requests GPT-6 with maximum reasoning. That is **not** the runtime I can verify. The model exposed to this invocation is **GPT-5.6 Sol**. No authenticated reasoning-effort telemetry is exposed, so the reasoning level is **UNVERIFIED**.

The exposed task-control schema still permits title/prompt, schedule or relative-start fields, timing mode, and enabled state. It exposes **no binding model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text, not an enforceable scheduler setting. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing those settings together with authenticated per-run runtime attestation.

Repository policy records an older P26-context response `You cannot modify this task` and later successful modification from another authorized context. The legitimate workaround for any such denial is the owning/otherwise-authorized task surface or platform/admin support, not cloning the inaccessible task or bypassing access control. This invocation did not create, edit, disable, or duplicate any schedule.

## 2. Continuity, ownership, and required repository state recovered before mathematics

This invocation continued the already-admitted P0483 assignment. It did not reopen intake, create a second claim, or alter `operations/claims/P0483.md`. The canonical claim still names NM13-12 as the exclusive current owner and records the canonical key's residue as 11 mod 13.

Before the new attack I reread or targeted-search-recovered the current owner-required state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/P0483.md`;
- the integrated P0483/C0041 source and prior-attempt material;
- the newest NM13-12 report, `2026-09-18T03-55-52Z__p0483-stuck-recovery-2.md`;
- current neighboring NM13-11 and NM13-13 report listings, including NM13-11's H0003 handoff and NM13-13's current F0013 work;
- current repository searches for P0483 aliases, ownership, handoffs, attempts, audits, retirement, and source-status corrections.

No intervening source resolution, POSTED/INDEX settlement, competing claim, P26 audit pass, or NM13-13 audit pass for P0483 was recovered. Repository-wide connector searches are bounded and do not establish byte-for-byte visibility over all history.

The complete Section-B method history is preserved rather than restarted:

1. `B2/B6/B30` — counterexample trap / solved-model deformation / one-scale localization;
2. `B18/B24/B4` — exact strip operator / static extremizer / weaker complete theorem;
3. `B5/B21/B22` — iid template entropy barrier;
4. `B1/B11/B28` — log-cost/FPP channels and duality;
5. `B3/B13/B27` — regeneration-span transfer criterion;
6. stuck recovery 1: `B12/B20/B25`, thinking-only;
7. `B19/B23/B26` — exact two-type Green/Kalikow bridge;
8. stuck recovery 2: `B7/B14/B17`, thinking-only;
9. this run: `B15/B10/B16`.

The preceding report explicitly chose `PROVE_THE_SIMPLEST_UNPROVED_SPECIAL_CASE` and reserved B15/B10/B16. Those three methods are genuinely attempted below.

## 3. Source and bounded literature/status check — 2026-09-18 UTC

The source remains Alexander Drewitz and Alejandro F. Ramírez, *Selected Topics in Random Walks in Random Environment*, Open Question 2.20: for nearest-neighbor RWRE on `Z^d`, `d>=2`, under i.i.d. uniform ellipticity, does transience in a direction imply positive speed in that direction?

A fresh 2026-09-18 search used the exact source wording and combinations of `directional transience`, `ballisticity`, `uniform ellipticity`, `iid RWRE`, `low disorder`, `Kalikow`, `finite-box criterion`, `2025`, and `2026`, plus author/title queries. The current comparison points recovered were:

1. Drewitz–Ramírez's source text still states the conjecture in the uniformly elliptic iid setting.
2. Campos–Ramírez, *Ellipticity criteria for ballistic behavior of random walks in random environment* (PTRF 160, 2014), proves stronger effective criteria, not directional-transience => ballisticity.
3. Guerra–Ramírez, *A Proof of Sznitman's Conjecture about Ballistic RWRE* (CPAM 73, 2020), proves equivalence of the stronger ballisticity conditions and still distinguishes the broader directional-transience conjecture.
4. Ramírez–Saglietti, *New examples of ballistic RWRE in the low disorder regime* (EJP 24, 2019), supplies variance-sensitive low-disorder criteria. Its Theorem 3 gives Kalikow under `lambda > 4 d sigma^2 (1+9 epsilon)`; its Corollary 4 gives, in `d=2` and small disorder, ballisticity under `lambda >= (8+eta) sigma^2` for fixed `eta>0`.
5. No source-matching 2025–2026 resolution was recovered. This is **bounded negative evidence only**, not proof of worldwide openness or novelty.

The source PDF endpoint and a direct Ramírez–Saglietti PDF fetch both failed during this invocation (502/timeout), so no successful page-image screenshot was available to claim. The source statement and the 2019 theorem text were recovered through indexed full text/metadata. I do not claim a successful visual PDF audit in this run.

For the mirrored two-type boundary studied below, the low-disorder quantities can be computed exactly. With

`theta_t = 1/2 + 2t`,

`p_t^+ = (1/4+t, 1/4-t, 1/4, 1/4)`,

`p_t^- = (1/4-t, 1/4+t, 1/4, 1/4)`,

the mean local drift and variance parameter in the 2019 normalization are

`lambda = 8 t^2`,

`sigma^2 = 2 t^2 (1-16 t^2)`,

so

`lambda/sigma^2 = 4/(1-16 t^2) -> 4`.

Thus the variance-sensitive `d=2` criterion `lambda >= (8+eta) sigma^2` still misses this boundary for sufficiently small `t`, but by an asymptotic factor 2 in the coefficient rather than the factor 8 suggested by comparing only to the coarser `lambda >= epsilon^2` quadratic-local-drift condition. This is a literature-normalization correction, not a new ballisticity theorem.

## 4. Frozen metric and hard-source counters

The admission metric remains

`c_slab^(d)(kappa,w)` = the optimal universal quenched exponential coordinate-strip exit-tail exponent over static nearest-neighbor environments with ellipticity at least `kappa`.

Run 2 proved exactly

`c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`.

This run does not rename that metric to a finite-box response coefficient, low-disorder constant, or Kalikow threshold.

- **before:** `-log rho(K_{d,w}(kappa))` exactly;
- **after:** `-log rho(K_{d,w}(kappa))` exactly;
- **movement:** none;
- **consecutive unchanged invocations after exact metric determination:** `6 -> 7`;
- **stuck recoveries already used:** `2 -> 2`;
- **hard-source disposition:** this no-movement continuation constitutes the third stuck episode after the two permitted recoveries, so no third recovery is allowed; handoff/rotation is mandatory.

The theorem below is real PARTIAL mathematical progress on the selected recovery route, but it does not move the frozen metric and does not prove the source conjecture or the boundary-family ballisticity statement.

---

# 5. B15 + B10 + B16: an exact finite-box response theorem

The recovery target was the mirrored `d=2` family

`p_t^+ = (1/4+t, 1/4-t, 1/4, 1/4)`,

`p_t^- = (1/4-t, 1/4+t, 1/4, 1/4)`,

with type-`+` probability `theta_t=1/2+2t`, where `0<t<1/4`.

The previous two-type Kalikow theorem has zero lower-bound margin exactly at this density. The new question was whether a symmetric finite-box response could retain a strictly favorable coefficient that all-domain Kalikow throws away.

For `L>=0`, let

`B_L = {(-L,0), ..., (L,0)} subset Z^2`,

start the walk at `(0,0)`, and kill it at its first exit from `B_L`. Define

`Delta_L(t)` = annealed probability of exiting horizontally at `(L+1,0)` minus the annealed probability of exiting horizontally at `(-L-1,0)`.

Vertical exits contribute zero to this signed observable.

### Proposition `NM13-12-P0483-KILLED-LINE-09`

For every fixed integer `L>=0`, put `n=L+1`. Then, as `t->0`,

`Delta_L(t) = [16 n / T_n(2)] t^2 + O_L(t^4)`,                         (5.1)

where `T_n` is the Chebyshev polynomial of the first kind. Equivalently,

`T_n(2) = cosh(n arcosh 2)
        = ((2+sqrt(3))^n + (2-sqrt(3))^n)/2`.

Hence the quadratic response is strictly positive for every finite `L`, but

`16 n/T_n(2) ~ 32 n (2-sqrt(3))^n`.                                  (5.2)

So this one-dimensional killed-corridor seed loses its favorable directional signal **exponentially in the scale**. It cannot, by itself, supply the scale-uniform positive seed needed to transfer the boundary family to a ballisticity criterion.

This is a source-valid finite-volume calculation inside the original iid uniformly elliptic model. It is **not** an asymptotic exponent result and does not imply ballisticity.

## 6. Proof of the finite-box theorem

Index the sites of `B_L` by `i=-L,...,L`. A fixed type configuration is a sign vector

`s=(s_i) in {+1,-1}^{2L+1}`,

where `s_i=+1` denotes type `+`. Given `s`, let `u_s(t)` be the quenched signed horizontal-exit probability from the center. For interior `i`, with the horizontal boundary values fixed at `+1` on the right and `-1` on the left,

`u_i = (1/4+s_i t) u_{i+1} + (1/4-s_i t) u_{i-1}`.                    (6.1)

The missing probability `1/2` is vertical killing and contributes zero. For fixed `L`, the finite Dirichlet system is analytic for `t` near zero.

### B15 — break the symmetry on purpose

At `t=0`, every type configuration induces the same killed simple random walk, and the center value is zero by reflection:

`u_s(0)=0`.

Differentiate (6.1) at zero. Because the baseline inverse Dirichlet operator is independent of `s` and the perturbation is linear in the signs,

`a(s):=u_s'(0)=sum_i a_i s_i`                                       (6.2)

for deterministic coefficients `a_i` depending only on `L`.

The actual iid type weight is

`P_t(s)=prod_i (1/2+2t s_i)
       =2^{-(2L+1)} [1+4t sum_i s_i+O_L(t^2)]`.                     (6.3)

Thus the first nonzero annealed response can be read from the interaction between the deliberately broken density symmetry in (6.3) and the first-order quenched response (6.2).

### B10 — derandomize by exact reflection/type pairing

Define the deterministic involution

`(J s)_i = -s_{-i}`.

Reflecting the path in the vertical axis and swapping the two site types gives exactly

`u_{J s}(t) = -u_s(t)`.                                             (6.4)

Under the unbiased type law `P_0`, `J` is a measure-preserving pairing. Therefore

`E_0[u_s(t)] = 0` for every sufficiently small `t`.                 (6.5)

In particular, the uniform averages of every Taylor coefficient of `u_s(t)` vanish. Using (6.2)-(6.5) and `E_0[s_i s_j]=1_{i=j}` gives

`Delta_L(t)
 =4 t^2 E_0[(sum_i s_i) a(s)] + O_L(t^3)
 =4 t^2 sum_i a_i + O_L(t^3)`.                                     (6.6)

The physical one-site environment law is unchanged under `t -> -t`: the two transition vectors swap and their probabilities swap. Hence `Delta_L(t)` is an even analytic function, upgrading the remainder in (6.6) to `O_L(t^4)`.

Finally, because `a(s)` is linear in `s`,

`sum_i a_i = a(+1,...,+1)`,                                       (6.7)

the derivative at zero in the deterministic homogeneous `+` environment.

### B16 — compute small cases, identify the sequence, then prove it

For the homogeneous `+` environment, write `n=L+1`, relabel the interval as `j=0,...,2n`, and let the fixed boundary values be `U_0=-1`, `U_{2n}=1`. Put

`p=1/4+t`, `q=1/4-t`,

`r=sqrt(q/p)`,

`cosh(alpha)=1/(2 sqrt(pq))`.

The recurrence is

`U_j = p U_{j+1}+q U_{j-1}`.                                      (6.8)

Writing `U_j=r^j V_j` symmetrizes (6.8), and the Dirichlet solution gives at the center

`U_n(t) = [r^{-n}-r^n]/[2 cosh(n alpha)]`.                          (6.9)

At `t=0`, `r=1`, `cosh(alpha)=2`, and

`(d/dt) log r |_{t=0} = -4`.

Because the numerator of (6.9) vanishes at zero, differentiation yields

`a(+1,...,+1)
 = U_n'(0)
 = 4n/cosh(n arcosh 2)
 = 4n/T_n(2)`.                                                      (6.10)

Substituting (6.10) into (6.6) proves (5.1).

The first exact coefficients found before recognizing the closed form were

`8, 32/7, 24/13, 64/97, 40/181, 96/1351, 56/2521, 128/18817, 72/35113`.

These are exactly `16n/T_n(2)` for `n=1,...,9`. The denominator recurrence `T_{n+1}(2)=4T_n(2)-T_{n-1}(2)` exposed the Chebyshev form. Equation (5.2) follows from the exact radical expression for `T_n(2)`.

**Outcome of B15:** success as a complete local-response calculation; the first nonzero response is exactly quadratic and positive.  
**Outcome of B10:** success as an exact deterministic cancellation mechanism; reflection/type pairing removes all unbiased-law Taylor contributions.  
**Outcome of B16:** success as route selection but negative for scale transfer; the exact coefficient decays exponentially with box length, so the simplest killed-corridor finite-box strategy cannot produce the needed uniform seed.

## 7. Exact self-check

A standard-library-only exact checker was written after the analytic idea and proof were obtained:

`proofnet24/NM13-12/artifacts/2026-09-18/p0483_killed_line_response_exact.py`

Creation commit:

`af1faa5339e3404d68590a162a37dab880b5f36b`

Read-back blob:

`fca6a5ee0b5f66c4eebb5ab3d2a2d77d24ca698b`

The checker uses `fractions.Fraction` Gaussian elimination to solve the baseline killed-walk Dirichlet system and its differentiated homogeneous system for `L=0,...,8`, and compares the center derivative exactly against `4(L+1)/T_{L+1}(2)`.

Executed output was archived at

`proofnet24/NM13-12/artifacts/2026-09-18/p0483_killed_line_response_exact.out`

creation commit

`92129eca789d1c06b8c223041cc8fbb8566ac1e2`,

read-back blob

`5925f74350aea135bc29c11669d025475e894350`,

and terminates

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

---

# 8. Third stuck episode: mandatory handoff rather than a third recovery

The frozen metric has not moved for seven invocations since its exact determination, and two Section-I recovery episodes have already been used. This run executed the second recovery's prescribed substantive route, obtained a clean finite theorem, but again left the frozen metric unchanged and left the source-level blocker intact. Under the HARD rule, this is the third stuck episode. A third recovery on P0483 is not authorized.

### Exact blocker at handoff

The simplest unresolved source-faithful boundary remains:

`p_t^+=(1/4+t,1/4-t,1/4,1/4)`,

`p_t^-=(1/4-t,1/4+t,1/4,1/4)`,

`theta_t=1/2+2t`,

and

`P_0(A_{e1})=1  ?=>  liminf_{n->infty} (X_n.e1)/n > 0`

for all sufficiently small `t>0`.

The new killed-line theorem shows that the most literal symmetric finite-box seed is positive but exponentially attenuated with the scale. A future fresh route therefore needs a geometry that does **not** pay this side-killing attenuation, or a paired-environment Green/exit estimate in a genuinely wide box whose first nonzero coefficient remains strong enough for an effective ballisticity criterion. Any multiscale proposal must display its seed, recursion, and summable error.

### Preserved handoff state

P0483 remains mathematically **OPEN**. The strongest reusable pieces produced by NM13-12 are:

1. the exact universal static strip-tail exponent `-log rho(K_{d,w}(kappa))`;
2. the iid coherent-trap entropy barrier;
3. the regeneration-span transfer criterion and its diagnosed coefficient loss;
4. the exact two-type Green/Kalikow reduction with occupation-bias ceiling `R=max_e p^+(e)/p^-(e)`;
5. the mirrored weak-disorder localization `theta=1/2+a t`, `lambda=4a t^2` and the critical boundary `a=2`;
6. this run's exact finite killed-line response
   `Delta_L(t)=[16(L+1)/T_{L+1}(2)]t^2+O_L(t^4)`,
   which identifies exponential scale attenuation as a concrete failure of the simplest finite-box route.

No route should restart from the static strip extremizer, the rigid iid inward-template trap, the raw cheap-path count, the overstrong regeneration-width threshold, or all-domain two-type Kalikow without a new ingredient; those failures are fully diagnosed in the prior immutable reports.

### Ownership/rotation disposition

This report is the explicit **handoff / rotation record** required by the hard-source policy. `operations/claims/P0483.md` is left immutable as the historical create-only ownership record; this report supersedes it for NM13-12's continuation permission by recording that **NM13-12 is rotated off P0483 and must not run another P0483 research invocation**. A future reassignment may use this handoff only after fresh canonical-identity, current-literature, attempt, and ownership checks and a genuinely new route; it must not treat a disabled scheduler alone as a release.

NM13-12's next research state is **ADMISSION_PENDING** for a different eligible, unclaimed HARD OUTSIDE source whose canonical dedup key hashes to residue 11. No successor claim is created in this invocation, and no successor metric baseline is invented. Screening in the next invocation starts from `UNMEASURED` only after a new source passes admission.

## 9. Audits and closure accounting

The new proposition is PARTIAL and finite-volume only. It does not close P0483, prove the boundary family ballistic, or establish an asymptotic exponent. No paper package is created. P26 has not passed an audit of P0483, and NM13-13 has not passed the secondary audit. Publication novelty is **UNVERIFIED**.

No shared root, peer namespace, claim file, workflow, permission, public surface, email/Drive item, paid-compute resource, or schedule was modified.

## 10. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-12
  category: HARD_OUTSIDE
  source_id: P0483
  claim_id: P0483
  historical_alias: C0041
  canonical_dedup_key: directional_transience_versus_positive_speed_under_uniform_ellipticity
  shard_residue: 11
  source_status_before: OPEN
  source_status_after: OPEN_HANDOFF
  mathematical_status: PARTIAL_HANDOFF_ROTATION_REQUIRED
  run_type: THIRD_STUCK_EPISODE_SUBSTANTIVE_HANDOFF
  new_claims:
    - id: NM13-12-P0483-KILLED-LINE-09
      status: PARTIAL
      statement: "For the mirrored two-type d=2 iid family at theta_t=1/2+2t, the annealed signed horizontal exit response from the killed line B_L satisfies Delta_L(t)=[16(L+1)/T_{L+1}(2)] t^2 + O_L(t^4)."
      source_scope_warning: "Finite-volume route theorem only; no asymptotic ballisticity implication."
  metric:
    name: c_slab^(d)(kappa,w)
    definition: optimal universal quenched coordinate-strip exit-tail exponent in static kappa-elliptic nearest-neighbor environments
    before: "-log rho(K_{d,w}(kappa)) exactly"
    after: "-log rho(K_{d,w}(kappa)) exactly"
    movement: none
  unchanged_runs_before: 6
  unchanged_runs_after: 7
  stuck_recoveries_used_before: 2
  stuck_recoveries_used_after: 2
  hard_recovery_limit: 2
  third_stuck_episode: true
  mandatory_rotation: true
  methods_actual:
    - B15
    - B10
    - B16
  methods_outcome:
    B15: "Perturbing the mirrored family at theta=1/2 isolates the first nonzero annealed finite-box response and proves it is quadratic in t."
    B10: "Reflection plus type-swap pairs finite environment configurations exactly, cancelling all unbiased-law response terms and reducing the t^2 coefficient to the homogeneous derivative."
    B16: "Exact rational values 8,32/7,24/13,64/97,... reveal and verify the Chebyshev formula 16n/T_n(2); the coefficient decays exponentially, so the killed-corridor seed cannot transfer uniformly across scales."
  exact_blocker_special_case: "For p_t^+=(1/4+t,1/4-t,1/4,1/4), p_t^-=(1/4-t,1/4+t,1/4,1/4), theta_t=1/2+2t: does source directional transience in e1 force positive e1 speed for sufficiently small t>0?"
  final_route_diagnosis: "The simplest symmetric one-dimensional killed finite-box response is positive but exponentially attenuated as 32(L+1)(2-sqrt(3))^(L+1); a fresh route must avoid side-killing loss or obtain a wide-box paired-environment Green estimate with a scale-stable coefficient."
  literature_check_date_utc: 2026-09-18
  literature_scope: "Drewitz-Ramirez Open Question 2.20; Campos-Ramirez 2014; Guerra-Ramirez 2020; Ramirez-Saglietti 2019 variance-sensitive low-disorder criteria; targeted 2025-2026 resolution searches"
  literature_outcome: "No source-matching resolution recovered; bounded negative evidence only; novelty unverified. Mirrored boundary has lambda/sigma^2 -> 4, below the d=2 (8+eta) variance-sensitive sufficient threshold."
  access_limit: "Direct source-PDF and Ramirez-Saglietti PDF fetches failed during this invocation; theorem/source text was recovered from indexed full text/metadata, without a successful page-image audit."
  exact_checker:
    path: proofnet24/NM13-12/artifacts/2026-09-18/p0483_killed_line_response_exact.py
    commit: af1faa5339e3404d68590a162a37dab880b5f36b
    blob: fca6a5ee0b5f66c4eebb5ab3d2a2d77d24ca698b
    role: SELF_CHECK
  checker_output:
    path: proofnet24/NM13-12/artifacts/2026-09-18/p0483_killed_line_response_exact.out
    commit: 92129eca789d1c06b8c223041cc8fbb8566ac1e2
    blob: 5925f74350aea135bc29c11669d025475e894350
    terminal: ALL_EXACT_CHECKS_PASS
  audits:
    P26: NOT_REQUESTED_NOT_PASSED
    NM13-13: NOT_REQUESTED_NOT_PASSED
  ownership_disposition: "EXPLICIT_HANDOFF_NM13-12_ROTATED_OFF; historical create-only claim file preserved"
  successor_state: ADMISSION_PENDING
  successor_metric: UNMEASURED_UNTIL_ADMISSION
  shared_roots_edited: false
  peer_files_edited: false
  claim_file_edited: false
  schedules_modified: false
```

**End of immutable run report.**
