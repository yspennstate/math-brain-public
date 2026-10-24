Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding model/effort selector is exposed.

# P0487 — the `d-1` initial-regeneration-radius bridge

Date: 2026-09-20 UTC  
Worker: C04 / R7-05  
Native ID: `6aabe805f32881919992996e1c5cfad6`  
Status: **PROVED PARTIAL**. The full Drewitz--Ramírez implication is not proved here.

## 1. Exact source target and inherited theorem

The outside target is Drewitz and Ramírez, *Selected Topics in Random Walks in Random Environment* (2014), Open Question 3.20: in an i.i.d. uniformly elliptic nearest-neighbor environment on `Z^d`, `d>=2`, does a nonzero limiting velocity with positive component in direction `ell` imply the source polynomial ballisticity condition `(P)_M|ell` at the standard effective threshold?

The preceding R7-05 work established two useful sufficient mechanisms:

1. if the pre-first-regeneration backward radius in every nearby direction has an `M`-th moment, then the asymptotic slab condition `(mathcal P^M)|ell` holds;
2. a finite cone of positive tilted correctors with any positive and negative moments yields arbitrarily high polynomial wrong-way slab decay.

The first statement was previously paired with the old `M>=15d+5` polynomial threshold. This run observes that this wastes a large amount of exponent. Enrique Guerra's 2020 renormalization theorem gives a much lower entrance point: his Definition 1.4 is exactly the asymptotic slab condition

`L^M P_0[\tilde T_{-bL}^{u}<T_L^u] -> 0`,

and Theorem 1.9 states that `(mathcal P^{d-1})|ell` implies his seed condition and, in the i.i.d. case, condition `(T)|ell`. Guerra--Ramírez then identify `(T)` with the standard finite-box polynomial condition `(P)_M` for the established range `M>=15d+5`.

Primary references checked this run:

- E. Guerra, *On the connection between transient and ballistic behaviours for RWRE*, arXiv:2006.00570v3, Definition 1.4 and Theorem 1.9.
- E. Guerra and A. F. Ramírez, *A proof of Sznitman's conjecture about ballistic RWRE*, arXiv:1809.02011.

This is a targeted literature check, not a novelty or worldwide-openness certificate.

---

## 2. Setup

Assume the annealed law satisfies

`X_n/n -> v` almost surely

for a deterministic vector `v` with `v.ell>0`.

By continuity there is an open neighborhood `U` of `ell` in the unit sphere such that

`v.u>0` for every `u in U`.

Hence the walk is directionally transient in every `u in U`.

For such a direction `u`, let `tau_1^u` be the first standard regeneration time in direction `u`. Define the **initial regeneration backward radius**

`R_u := max(0, - inf_{0<=n<=tau_1^u} X_n.u)`.

After `tau_1^u`, the defining no-backtracking property of regeneration prevents the walk from ever dropping below its positive regeneration record.

Write

`T_L^u = inf{n>=0 : X_n.u >= L}`,

`\tilde T_{-bL}^u = inf{n>=0 : X_n.u <= -bL}`.

---

# 3. Main new theorem — only a `(d-1)`-moment of the initial radius is needed

## Theorem 3.1

Suppose there is an open neighborhood `U` of `ell` such that for every `u in U`,

`E_0[R_u^{d-1}] < infinity`.                                  (3.1)

Then `(mathcal P^{d-1})|ell` holds. Consequently, for an i.i.d. uniformly elliptic environment,

`(T)|ell`

holds, and therefore the source polynomial ballisticity condition `(P)_M|ell` holds for every standard effective exponent `M>=15d+5`.

### Proof

Fix `u in U` and `b>0`. If

`\tilde T_{-bL}^u < T_L^u`,                                  (3.2)

then the hit of the negative level must occur before `tau_1^u`.

Indeed, if `tau_1^u` occurs before the walk reaches level `L`, then after `tau_1^u` the walk stays forever above the positive regeneration record and therefore cannot hit `-bL`. If instead the first regeneration record already lies at or beyond `L`, then `T_L^u<=tau_1^u`, so an event satisfying (3.2) again has its negative hit before `tau_1^u`.

Therefore

`{\tilde T_{-bL}^u < T_L^u} subset {R_u >= bL}`.              (3.3)

Put `p=d-1>0`. A standard tail consequence of `E[R_u^p]<infinity` is

`t^p P(R_u>=t) -> 0`.                                         (3.4)

For completeness,

`t^p P(R_u>=t)
 <= E[R_u^p 1_{R_u>=t}] -> 0`                                 (3.5)

by dominated convergence / tail integrability.

Using (3.3) with `t=bL`,

`L^p P_0[\tilde T_{-bL}^u<T_L^u]
 <= b^{-p} (bL)^p P_0[R_u>=bL]
 -> 0`.                                                       (3.6)

The same open set `U` works for every fixed `b>0`. Thus Definition 1.4 of Guerra gives

`(mathcal P^{d-1})|ell`.                                      (3.7)

Guerra's Theorem 1.9 says `(mathcal P^{d-1})|ell` implies his finite seed condition and, under i.i.d. structure, `(T)|ell`. The Guerra--Ramírez equivalence then yields `(P)_M|ell` in the standard range `M>=15d+5`. QED.

### What changed

The old sufficient regeneration moment in this project was effectively of order `M>=15d+5`. The exact same localization argument, combined with the 2020 theorem, lowers the required initial-radius moment to

`boxed{d-1}`.                                                 (3.8)

This is a major reduction in the remaining probabilistic obligation.

---

## Corollary 3.2 — the two-dimensional problem reduces to a first moment

In `d=2`, it is enough to prove, for every `u` in one open neighborhood of `ell`,

`E_0[R_u] < infinity`.                                        (3.9)

Then the full source conclusion follows through Theorem 3.1.

A still stronger but simpler sufficient statement is

`E_0[tau_1^u] < infinity`,                                    (3.10)

because `R_u<=tau_1^u` for a nearest-neighbor walk.

Thus in dimension two a very sharp version of the remaining gap is:

> Does positive limiting speed force integrability of the *unconditioned initial* regeneration block (or merely its backward spatial radius) in every nearby direction?

This is substantially weaker than proving all moments of a regeneration time.

---

# 4. Occupation-time reduction

The radius criterion has another exact reformulation which may be more amenable to the environment-seen-from-the-particle process.

For a direction `u` with `v.u>0`, define the total nonpositive occupation count

`N_u := sum_{n>=0} 1_{ {X_n.u<=0} }`.                         (4.1)

Positive speed implies `N_u<infinity` almost surely, but gives no moment or rate by itself.

## Lemma 4.1

For every sample path with nearest-neighbor increments,

`R_u <= 1 + N_u`.                                             (4.2)

Consequently,

`E[N_u^{d-1}]<infinity`

for every `u` in a neighborhood of `ell` is sufficient for the full P0487 conclusion.

### Proof

Suppose the path reaches a point with projection at most `-r` before its first regeneration. Consider the last time before that hit at which its projection is nonnegative. From that time until the hit at `-r`, every visited endpoint has nonpositive projection. Since one nearest-neighbor step changes projection by at most one in absolute value, at least `floor(r)` such steps are needed. Hence `N_u>=floor(r)`. Taking the supremal reached depth gives (4.2), up to the harmless additive one. QED.

### Two-dimensional corollary

For `d=2`, Tonelli gives

`E[N_u] = sum_{n>=0} P_0(X_n.u<=0)`.                           (4.3)

Therefore the following concrete one-time slowdown summability condition is enough to solve the source problem in dimension two:

`sum_{n>=0} P_0(X_n.u<=0) < infinity`                         (4.4)

for every `u` in a fixed neighborhood of `ell`.

Positive speed only implies the summands tend to zero. The gap between convergence to zero and summability is exactly a quantitative initial-transient problem.

---

# 5. A failed-record tail lemma: global backtracking reduces to one local type of bad excursion

The usual regeneration construction attempts successive record points until one becomes a permanent regeneration point. The number of failed attempts has a geometric tail. The following abstract lemma isolates the additional estimate that would turn this into the radius moment required above.

## Lemma 5.1 — geometric-attempt tail compression

Let attempts be indexed by `j=0,1,2,...`, and let `K` be the first successful attempt. Suppose

`P(K>=j) <= q^j`                                              (5.1)

for some `q<1`.

For each failed attempt `j<K`, let `B_j` be the maximum downward displacement, in direction `u`, from that attempt's record level during the failed segment. Assume there is a deterministic nonincreasing function `f(r)` such that, conditionally on the history `H_j` available at the start of attempt `j`,

`P(B_j>=r, j<K | H_j) <= f(r) 1_{ {K>=j} }`.                 (5.2)

If the pre-regeneration path is covered by these failed segments, then

`P(R_u>=r) <= f(r)/(1-q)`.                                    (5.3)

### Proof

If the walk reaches global projection at most `-r` before regeneration, then on the failed segment containing that hit the downward displacement from the segment's nonnegative record level is at least `r`. Hence

`{R_u>=r} subset union_{j>=0}{K>j, B_j>=r}`.                 (5.4)

Using the union bound, conditional estimate (5.2), and (5.1),

`P(R_u>=r)
 <= sum_j E[1_{K>=j} P(B_j>=r,j<K | H_j,K>=j)]
 <= f(r) sum_j P(K>=j)
 <= f(r) sum_j q^j
 = f(r)/(1-q)`.                                                (5.5)

QED.

## Corollary 5.2

If for every nearby direction `u` the usual regeneration-attempt construction admits (5.2) with

`r^{d-1} f_u(r) -> 0`,                                       (5.6)

then P0487 follows in full.

Indeed (5.3) gives the exact tail condition needed in (3.6), without even assuming a finite `(d-1)`-moment.

### Why this is a useful narrowing

The number of failed record attempts is not the difficult part; it is already geometric in the classical i.i.d. regeneration construction. The missing estimate is **uniform control of the depth of one failed attempt conditional on its past**.

This pinpoints why a naive use of i.i.d. independence fails. A failed attempt can descend into an already explored lower region. The environment in that region is no longer fresh under the attempt history, so its deep-backtracking tail cannot simply be replaced by the unconditional tail from the origin. Any proof has to show that explored-region recycling is harmless, or force a deep failure to cross enough genuinely fresh spatial material to regain multiplicative decay.

---

# 6. Noncircularity check: conditioned regeneration means do not control this initial radius

A standard ballistic regeneration formula concerns the post-regeneration law, equivalently a law conditioned on a no-backtracking event. Positive speed can therefore provide finite mean information for the **successful conditioned regeneration block**.

That does not control the variable in Theorem 3.1. `R_u` is generated precisely by the unsuccessful pre-regeneration attempts, i.e. by trajectories on which backtracking occurs. Conditioning on no backtracking deletes those trajectories.

This is not a cosmetic distinction. The previous R7-05 run constructed a bounded-step regenerative process with positive asymptotic speed and trivial later regeneration blocks but an arbitrarily heavy initial backward excursion. The present theorem shows exactly where such a pathology would break the RWRE proof: it violates (3.1)/(5.6), while leaving the successful regeneration law benign.

Therefore the remaining P0487 implication cannot be closed by quoting only:

- positive speed;
- existence of regenerations;
- finite mean of the successful conditioned block; or
- geometric number of regeneration attempts.

One must use i.i.d. **spatial** structure to control failed-attempt depth.

---

# 7. Fixed source metric and obligation ledger

Fixed full-source metric:

`FULL_SOURCE_IMPLICATION: 0 -> 0`.

Status: **PROVED PARTIAL**, not a full solution.

Obligation ledger after this run:

- `O1` finite-periodic exponential corrector: DONE (earlier run).
- `O2` integrable multiplicative corrector => polynomial back-face control: DONE (earlier run).
- `O3` finite directional star removes lateral exits: DONE (earlier run).
- `O4` initial regeneration radius localizes wrong-way slab event: DONE (earlier run).
- `O5` required radius exponent reduced from the old `15d+5` scale to exactly `d-1` via Guerra 2020: **DONE THIS RUN**.
- `O6` occupation-time criterion `E N_u^{d-1}<infinity`: **DONE THIS RUN**.
- `O7` geometric-attempt reduction to a uniform failed-attempt depth tail: **DONE THIS RUN**.
- `O8` derive `r^{d-1} f_u(r)->0` (or `E R_u^{d-1}<infinity`) from positive speed using i.i.d. spatial independence: OPEN, principal source gap.

---

# 8. Next mathematical attack

The next attack should work directly on `O8`, not return to finite-periodic examples.

For a fixed nearby direction `u`, define the worst conditional failed-attempt tail

`F_u(r) = ess sup_history P(B_j>=r, j<K | H_j, K>=j)`.

A sufficient target is the two-scale recursion

`F_u(2r) <= C F_u(r)^{1+eta} + exp(-c r)`                     (8.1)

for some `eta,c>0`, uniformly for all large `r` and for `u` in a small cone. Once `F_u(r)` is below a fixed threshold, (8.1) bootstraps to super-polynomial decay and hence (5.6).

The geometric picture to test is: a failed attempt reaching depth `2r` must either (a) cross two suitably separated fresh `r`-scale slabs, which should yield a product after environment exposure, or (b) recycle inside a previously explored tube for anomalously long, which needs a separate elliptic escape estimate. The proof must track the sigma-fields carefully; treating the two crossings as independent without a fresh-space separation would be circular.

In dimension two the immediate minimal target is even sharper:

`E_0[R_u] < infinity`                                        (8.2)

for every nearby `u`, or equivalently any stronger estimate such as the summability (4.4). Establishing (8.2) would already complete the source implication in `d=2` through the chain proved above.