Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. Movement: the previously proved strip exponent lower bound is sharpened to the exact extremal value `c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))`; methods actually tried this run: B18, B24, B4.

# NM13-12 — P0483 exact strip-survival operator

Date: 2026-09-17 UTC  
Track: NM13-12  
Category: HARD OUTSIDE  
Repository: `yspennstate/math-open-problems`, branch `master`  
Canonical source / claim ID: **P0483**  
Canonical dedup key: `directional_transience_versus_positive_speed_under_uniform_ellipticity`  
Historical intake alias: **C0041**  
Overall source status after this run: **OPEN**  
Local result status: **PARTIAL relative to P0483; exact auxiliary metric proved**

## 1. Runtime/model disclosure and scheduler interface

The requested task header asks for GPT-6 with maximum reasoning. That is **not** what I can verify ran. The actual model exposed to this run is **GPT-5.6 Sol**. No binding reasoning-level metadata is exposed, so the reasoning level is **UNVERIFIED**.

The scheduling/task interface exposed in this runtime still has fields for prompt/title/schedule/timing/enabled state, but **no model selector and no reasoning/thinking selector**. Therefore the repository's earlier statement remains true for this interface: `GPT-6 / maximum` can be requested in prompt text but cannot be bound by the scheduler fields available here. Changing that would require a scheduler/platform API that exposes binding model and reasoning fields, or an owner-authorized migration to a task surface that does. I did not create or modify any schedule in this run.

The owner history also records that a P26 scheduler ID once returned `You cannot modify this task`. I did not retry or bypass that access control. The legitimate workaround is an edit by an account/owner with permission or an owner-authorized recreation/migration of the task; this worker cannot infer that a disabled/inaccessible task is unowned and cannot bypass the ACL.

## 2. Continuity and repository state recovered before doing mathematics

This is the second NM13-12 invocation, so no new admission was performed and no new ownership file was created. The canonical create-only claim remains `operations/claims/P0483.md`, owned by NM13-12.

At the start of this run I recovered the controlling repository state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md` and targeted searches for later owner-authorized amendments;
- `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- `operations/claims/P0483.md`;
- the newest NM13-12 report, `proofnet24/NM13-12/runs/2026-09-17/2026-09-17T20-52-42Z__p0483-first-attack.md`;
- neighboring ProofNet24 reports for NM13-11 and NM13-13;
- targeted source/attempt/intake searches for `P0483`, `C0041`, the canonical dedup key, and the exact source question, including the probability-1000 surfaces and the campaign catalog entry recording historical attempt C0041-A001.

The earlier report established the canonical alias/dedup/shard mapping and recovered the previous campaign attempt rather than restarting it. No newer claim, handoff, retirement, posted result, or conflicting owner for P0483 was found in the bounded repository read. The source target therefore continues under the existing claim.

Large root/campaign files and code-search responses are connector-bounded; I recovered the controlling sections and exact P0483 records by path and targeted search, but I do **not** claim a byte-for-byte reread of every repository object.

## 3. Fresh bounded source / literature check

Dated search: **2026-09-17 UTC**. Search scope included the exact phrase `directional transience` with `positive speed`, `uniformly elliptic`, `RWRE`, `ballisticity`, `2025`, and `2026`; author/title searches for Drewitz–Ramírez and Guerra–Ramírez; and a bounded citing-literature search around the 2020 ballisticity-conditions paper.

The source remains the Drewitz–Ramírez open question: in a nearest-neighbor i.i.d. uniformly elliptic environment on `Z^d`, `d>=2`, does directional transience imply ballisticity / positive limiting speed in that direction?

The strongest directly relevant recovered primary result remains Guerra–Ramírez, *A Proof of Sznitman's Conjecture about Ballistic RWRE*, CPAM 2020, DOI `10.1002/cpa.21877`: it proves equivalence of the standard ballisticity conditions `(T)`, `(T')`, `(T)_gamma` and the polynomial condition, while its abstract still distinguishes the broader directional-transience-implies-ballisticity statement as believed rather than proved. Campos–Ramírez, PTRF 2014, DOI `10.1007/s00440-013-0527-7`, likewise states the broader assertion as Conjecture 1.1 and proves results under stronger criteria. A bounded 2025–2026 scan recovered later work on ballistic RWRE, dynamic environments, balanced environments, sparse environments, and slowdown, but no source-matching theorem proving the full P0483 implication.

This is a bounded literature check, **not** proof of worldwide openness and **not** a novelty certificate. The source question therefore remains labeled OPEN in this track.

## 4. Frozen metric and previous certified value

The first run froze the following auxiliary source-relevant metric. Fix the source dimension `d>=2`, a nonvacuous uniform ellipticity constant `0<kappa<=1/(2d)`, and integer strip width `w>=1`. Let

`S = {x in Z^d : a <= x_j <= a+w-1}`

be any coordinate strip. Define `c_slab(kappa,w)` to be the supremum of all `c>=0` for which there is a finite constant `C=C(d,kappa,w,c)` such that, uniformly over every nearest-neighbor environment `omega` with `omega(x,e)>=kappa`, every `A subseteq S`, and every `x in A`,

`P_{x,omega}(tau_A > n) <= C exp(-c n)` for all `n>=0`.

The dependence on fixed source dimension `d` was implicit in the previous notation. In this report I sometimes write `c_slab^(d)` only to expose that already-present dependence; the process, hypotheses, and normalization are unchanged.

Previous certified value, with `m=ceil(w/2)`, was

`c_slab^(d)(kappa,w) >= c_old := -log(1-kappa^m)/m`.                    (4.1)

The previous run explicitly made no sharpness claim. This run attacks that sharpness question rather than filing another consequence of (4.1).

## 5. B18 — say the strip problem in another language

The key change of language is to treat worst-case strip survival as a finite robust-control / Perron–Frobenius problem.

Index strip levels by `1,...,w`, and put `f_0=f_{w+1}=0`. Consider the cone `C_w` of nonnegative vectors `f=(f_1,...,f_w)` that are reflection symmetric and nondecreasing toward the center:

`f_i = f_{w+1-i}` for all `i`,

and

`f_1 <= f_2 <= ... <= f_ceil(w/2)`.

For a state on level `i`, the total probabilities of a step in the `-e_j`, transverse, and `+e_j` classes can be denoted `p_-`, `p_0`, `p_+`. Uniform ellipticity implies

`p_- >= kappa`, `p_+ >= kappa`, `p_0 >= 2(d-1)kappa`,

and `p_-+p_0+p_+=1`.

When `f` increases toward the strip center, the one-step expectation of `f` is maximized by placing the mandatory minimum mass on the worse directions and all remaining mass on the best available coordinate value. This defines the following substochastic `w x w` matrix `K=K_{d,w}(kappa)`.

For a level strictly left of the center, `i < (w+1)/2`,

`K(i,i-1) = kappa` when `i>1`,

`K(i,i)   = 2(d-1)kappa`,

`K(i,i+1) = 1-(2d-1)kappa`;                                            (5.1)

at `i=1`, the omitted outward `kappa` is killing at the strip boundary.

For a level strictly right of the center, use the mirror image of (5.1).

If `w` is odd and `m=(w+1)/2` is the unique center level,

`K(m,m-1)=kappa`, `K(m,m+1)=kappa`, `K(m,m)=1-2kappa`,                 (5.2)

with nonexistent neighbors omitted when `w=1`, so `K=[1-2kappa]` in that case.

For even `w` there is no special center row: the two central levels use the left/right rules above. Boundary row sums are `1-kappa`; all interior row sums are one.

The matrix is feasible because `kappa<=1/(2d)` implies `1-(2d-1)kappa>=kappa` and, in the odd-center row, the transverse total `1-2kappa` can be split among the `2(d-1)` transverse directions with each at least `kappa`.

## 6. Exact theorem — the finite operator gives the sharp strip exponent

### Claim `NM13-12-P0483-STRIP-EXACT-02` — PROVED, PARTIAL relative to P0483

Let `rho_{d,w}(kappa)` be the spectral radius of `K_{d,w}(kappa)` above. Then, for the **same frozen metric**,

`c_slab^(d)(kappa,w) = -log rho_{d,w}(kappa)`.                         (6.1)

More precisely, if `1` is the all-ones vector and a starting point `x` has strip level `i`, then for every `kappa`-uniformly elliptic static environment,

`P_{x,omega}(tau_S > n) <= (K^n 1)_i`,                                (6.2)

and hence the same bound holds for every `A subseteq S`. Conversely there is an explicit deterministic `kappa`-uniformly elliptic environment `omega_*` for which equality holds in (6.2) for every `n` and every starting level. Thus (6.1) is an exact worst-environment exponent, not just another lower bound.

### Proof, Step 1: `K` preserves the symmetric-unimodal cone

Reflection symmetry is immediate from the definition of `K`. It remains to check monotonicity on the left half.

Write

`Delta_i = f_{i+1}-f_i >= 0`

and set `f_0=0`, so `Delta_0=f_1>=0`.

For two successive ordinary left-half rows, direct subtraction gives

`(Kf)_{i+1}-(Kf)_i
 = kappa Delta_{i-1}
   + 2(d-1)kappa Delta_i
   + [1-(2d-1)kappa] Delta_{i+1} >= 0`.                                (6.3)

At the final step into an odd center `m`, using reflection symmetry `f_{m+1}=f_{m-1}` and (5.2),

`(Kf)_m-(Kf)_{m-1}
 = kappa[Delta_{m-2} + (2d-3)Delta_{m-1}] >= 0`.                       (6.4)

At the final step into the left central level `m` when `w=2m` is even, reflection gives `f_{m+1}=f_m`, and

`(Kf)_m-(Kf)_{m-1}
 = kappa Delta_{m-2} + 2(d-1)kappa Delta_{m-1} >= 0`.                  (6.5)

The small widths `w=1,2` are immediate directly. Therefore

`K C_w subseteq C_w`.                                                   (6.6)

In particular `u_n:=K^n 1` belongs to `C_w` for every `n>=0`.

### Proof, Step 2: one-step Bellman domination

Fix `f in C_w` and a site `x` at level `i`. Since `f` depends only on the strip coordinate, every transverse step has value `f_i`; the two longitudinal steps have values `f_{i-1}` and `f_{i+1}`, with value zero outside the strip.

On the left half, `f_{i+1}>=f_i>=f_{i-1}`. Subject to the lower bounds `p_-,p_+>=kappa` and the `2(d-1)` mandatory transverse probabilities, the one-step expected value is maximized by assigning exactly `kappa` to the outward longitudinal direction, exactly the mandatory total `2(d-1)kappa` to the transverse directions, and all remaining mass to the inward longitudinal direction. This is exactly row `i` of `K`. On the right half the argument is mirrored. At an odd center the two neighboring coordinate values are equal and no larger than the center value, so the maximizing allocation puts only `kappa` on each longitudinal direction and the remaining `1-2kappa` on transverse moves, exactly (5.2). At an even central pair the inward coordinate value equals the present value, so the chosen row again attains the maximum.

Hence for every admissible `omega`, every `f in C_w`, and every strip site `x` at level `i`,

`E_x^omega[f(level(X_1)); tau_S>1] <= (Kf)_i`.                         (6.7)

Now induct on `n`. The case `n=0` is equality. If strip survival for `n-1` further steps is bounded by `u_{n-1}=K^{n-1}1`, then the Markov property and (6.7), using `u_{n-1} in C_w`, give

`P_x^omega(tau_S>n)
 <= E_x^omega[u_{n-1}(level(X_1)); tau_S>1]
 <= (K u_{n-1})_i
 = (K^n 1)_i`.

This proves (6.2). Since `tau_A<=tau_S` for `A subseteq S`, it also bounds every set in the frozen metric.

### Proof, Step 3: construct the extremal environment

Define a deterministic environment `omega_*` depending only on the strip coordinate.

On the left half, set the outward longitudinal probability to `kappa`, each of the `2(d-1)` transverse direction probabilities to `kappa`, and the inward longitudinal probability to

`1-(2d-1)kappa`.

On the right half use the reflected assignment. At an odd center, put probability `kappa` on each longitudinal direction and distribute the remaining `1-2kappa` among the transverse directions with each transverse direction receiving at least `kappa`; feasibility is exactly `2d kappa<=1`. Outside the strip choose any `kappa`-uniformly elliptic probabilities.

Under `omega_*`, the strip-coordinate process killed on exit has transition matrix **exactly `K`**. Therefore

`P_{x,omega_*}(tau_S>n) = (K^n 1)_i`                                  (6.8)

for every level `i` and every `n`. Thus the Bellman upper envelope is attained by a single static environment; no time-dependent controller was smuggled into the argument.

### Proof, Step 4: extract the exact exponential rate

For `w>=2`, `K` is finite, irreducible and aperiodic: neighboring levels communicate in both directions with positive probability, every level has a positive self-loop, and a boundary row loses positive mass. Hence its Perron–Frobenius eigenvalue satisfies

`0 < rho := rho_{d,w}(kappa) < 1`.                                     (6.9)

For `w=1`, `rho=1-2kappa` directly and the same conclusion holds.

Let `h>0` satisfy `Kh=rho h`. Since `1 <= h/h_min`,

`K^n 1 <= (h/h_min) rho^n <= (h_max/h_min) rho^n`.                    (6.10)

Equations (6.2) and (6.10) prove the frozen metric with exponent `-log rho`, including at the endpoint exponent with finite constant `h_max/h_min`.

Conversely, primitivity gives positive Perron–Frobenius asymptotics for (6.8): for every level `i`, `(K^n1)_i` is a positive constant times `rho^n` up to a multiplicative factor tending to one. Therefore no bound with exponent `c>-log rho` can hold uniformly over environments, because it would fail for `omega_*` as `n->infinity`.

This proves (6.1). QED.

## 7. Certified improvement over the previous block bound

Let `m=ceil(w/2)` and `q=1-kappa^m`. The previous theorem applies in particular to the extremal environment `omega_*`, so

`K^m 1 <= q 1`.                                                        (7.1)

Taking exponential growth rates (or applying Collatz–Wielandt) gives

`rho_{d,w}(kappa)^m <= 1-kappa^m`.                                    (7.2)

Therefore

`-log rho_{d,w}(kappa)
 >= -log(1-kappa^m)/m = c_old`.                                        (7.3)

Thus the new value is a certified non-worsening of the frozen metric and, except in some small/special cases, is strictly sharper.

Two exact small-width checks make the movement concrete:

- `w=1`: `K=[1-2kappa]`, so
  `c_slab^(d)(kappa,1)=-log(1-2kappa)`,
  strictly improving the previous `-log(1-kappa)`.
- `w=2`: every row has survival mass `1-kappa`, so
  `rho=1-kappa`; the previous bound was already sharp.

For `w=3`, symmetry reduces `K` to a `2 x 2` Perron block. Its Perron eigenvalue is the larger root of

`lambda^2 - [1+2(d-2)kappa] lambda + 2kappa(d-2+kappa)=0`.             (7.4)

In dimension `d=2`, this is

`rho_{2,3}(kappa) = [1+sqrt(1-8kappa^2)]/2`.                           (7.5)

At the maximal `d=2` ellipticity value `kappa=1/4`,

`c_old = -(1/2)log(15/16) ~= 0.03226926`,

whereas

`c_slab^(2)(1/4,3)
 = -log((2+sqrt(2))/4) ~= 0.15834718`.                                 (7.6)

So on this concrete source-valid ellipticity scale, the certified exponent is about `4.91` times the previous block exponent.

No floating-point computation is used to justify the theorem or (7.4)–(7.5); those values come from the displayed exact finite matrix and its characteristic polynomial. The decimals in (7.6) are only explanatory evaluations of exact expressions.

## 8. B24 — identify the extremal object and what it says about the source

The extremal strip environment `omega_*` is now explicit. It continually biases the walk **toward the center of the strip**, while paying only the mandatory `kappa` probability toward the nearer exit and in each transverse direction. This exactly maximizes confinement among all static `kappa`-uniformly elliptic environments for the frozen strip problem.

This also identifies an important source-level obstruction: `omega_*` is highly position dependent and **not an i.i.d. environment**. It needs the longitudinal bias to reverse sign across the center of the strip. Therefore it cannot itself be a counterexample to P0483, and the sharp worst-environment strip tail is not automatically the correct i.i.d. trap tail.

That distinction is useful rather than cosmetic. The auxiliary worst-case local problem is now saturated: there is no point spending another run improving `c_slab` under only uniform ellipticity. Any further source movement must use the missing i.i.d./directional-transience structure to show that the centered inward-control pattern cannot persist with the frequency and scale needed to destroy speed, or must discover a different trap geometry not controlled by one strip coordinate.

## 9. B4 — prove the weaker quantitative problem completely

Instead of pretending that the local strip estimate proves P0483, this run closes the weaker finite-state extremal problem completely:

> Among all static nearest-neighbor `kappa`-uniformly elliptic environments, what is the slowest possible exponential exit rate from a coordinate strip of width `w`?

Answer: exactly `-log rho(K_{d,w}(kappa))`, attained by `omega_*`.

This is a complete theorem with explicit quantifiers, an explicit extremizer, and matching upper/lower rates. Relative to the source it remains **PARTIAL** because P0483 assumes an i.i.d. environment plus directional transience and asks for positive limiting speed, neither of which follows from the strip theorem.

## 10. What moved and what did not

**Frozen metric before:**

`c_slab^(d)(kappa,w) >= -log(1-kappa^ceil(w/2))/ceil(w/2)`.

**Frozen metric after:**

`c_slab^(d)(kappa,w) = -log rho(K_{d,w}(kappa))` exactly.

The metric was not silently changed: the dimension `d` was already fixed by the source `Z^d`; this run only makes that implicit dependence visible in the notation.

**Source statement:** no closure. Directional transience => positive speed in i.i.d. uniformly elliptic RWRE remains OPEN in this track after the bounded current-literature check.

**Run movement:** yes. The unchanged-run counter resets to `0`.

**Stuck-recovery episodes used on P0483:** `0`.

**Outside audits:** none counted. P26 audit = not requested; NM13-13 secondary audit = not requested. No closure label is asserted.

## 11. Next source-level step — leave the saturated strip problem

The next run should **not** manufacture another strip certificate. The exact operator has done its job. It should be used as a transfer lemma while moving back to the i.i.d. source.

The concrete missing quantity is a bound on the occurrence and persistence of source-valid trapping regions whose local dynamics approximate the inward-control profile `omega_*`. A useful target would have the following shape: for a longitudinal block of scale `L`, quantify the probability that an i.i.d. uniformly elliptic environment creates a connected region whose killed coordinate operator stays within a specified defect `delta` of `K` over enough sites to cause delay `exp(aL)`, and compare that occurrence exponent with the exact confinement exponent above. Any multiscale use must display the recursion and summable error; the exact finite operator alone does not provide that transfer.

Proposed next Section-B methods, deliberately different from this run and the preceding B2/B6/B30 run:

- **B5 — add a parameter and differentiate/interpolate:** introduce a defect parameter measuring distance from the extremal inward-control transition profile and seek a quantitative spectral penalty `rho(delta)<rho(0)`.
- **B21 — ask who else has this shape:** compare the exact strip operator with robust Markov decision processes / controlled birth-death chains and with RWRE trap arguments where an environment must realize a spatially reversing drift pattern.
- **B22 — read the failures, not the successes:** locate explicit failed or incomplete routes from directional transience to regeneration-time integrability and identify exactly which environmental rarity estimate they lack.

If those routes do not move the source-relevant quantity, abandon them rather than extending the already-solved strip calculation.

## 12. Structured ledger delta for P26

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
  before: ">= -log(1-kappa^ceil(w/2))/ceil(w/2)"
  after: "= -log rho(K_{d,w}(kappa)) exactly"
  theorem_id: NM13-12-P0483-STRIP-EXACT-02
  extremizer: deterministic inward-to-center strip environment omega_*
  methods_actual:
    - B18
    - B24
    - B4
  methods_outcome:
    B18: "success — recast worst strip survival as a finite robust-control/Perron-Frobenius operator"
    B24: "success — explicit static extremal environment attains the Bellman envelope; its non-i.i.d. nature isolates the source transfer obstruction"
    B4: "success — exact auxiliary strip exponent proved with matching upper and lower rate"
  unchanged_runs: 0
  stuck_recoveries_used: 0
  hard_recovery_limit: 2
  audits:
    P26: not_requested
    NM13-13: not_requested
  closure: false
  next_methods:
    - B5
    - B21
    - B22
  next_step: "quantify the i.i.d. rarity/spectral penalty for approximate inward-control trap regions and connect it to regeneration-time tails; do not spend another run sharpening the now-exact strip metric"
  literature_check_date_utc: 2026-09-17
  literature_scope: "exact source phrase; uniformly elliptic RWRE directional transience/ballisticity; Drewitz-Ramirez; Guerra-Ramirez; bounded 2025-2026 later/citing work"
  literature_limit: "bounded web/repository search; not proof of worldwide openness or novelty"
```

**End of complete run report.**
