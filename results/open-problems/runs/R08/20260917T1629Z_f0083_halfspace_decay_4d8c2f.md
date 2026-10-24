Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in the active F0083 metric: `1/2 -> 1/2`, unchanged count `1`; I0082 remains RETIRED/FROZEN at `2/3` with retirement count `6`. New theorem-sized movement outside the frozen metric: the critical four-dimensional half-space lattice has an a.e. unique stable allocation, and its unique boundary-layer radius deficit decays geometrically with exact ratio `lambda_*`, the unique root in `(0,1)` of `9 lambda^3 - 5 lambda^2 + 11 lambda - 7 = 0`, numerically `0.6171640568067426...`. Methods actually used: B4 PROVE SOMETHING WEAKER COMPLETELY, B26 HUNT THE SPORADIC CASE, B28 REPLACE FOR ALL WITH FOR TYPICAL.** GPT-6 / maximum was requested in prompt text, but the exposed runtime has no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083 flat-boundary obstruction and exact boundary-layer decay

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The later six-unchanged immutable handoff controls operationally: I0082 stays frozen at `2/3`, retirement count `6`. The old R08 FPP strict-convexity route remains retired from this slot.

The active successor is the exclusive R08 claim `operations/claims/F0083.md`. Its source is Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), arXiv:math/0505668v4, Open problem (i). The exact source question is whether some discrete center set in `R^d` admits two stable Lebesgue allocations differing on a nonnull set.

The frozen explicit candidate remains

`m_n = floor((1+|n|)^(3/4))`,

`H = {(n,a,b,c) in Z^4 : 1 <= a,b,c <= m_n}`,

`Xi_* = Z^4 \ H`,

with appetite one. The frozen two-obligation metric remains:

1. candidate admissibility / exact local mechanism — **PROVED** in the admitting report;
2. exhibit two stable appetite-one Lebesgue allocations of this exact `Xi_*` differing on positive measure — **OPEN**.

Therefore the source-sized metric is still `1/2`. A theorem about a tangent/local model does not count as obligation 2.

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the current F0083 claim, the admitting R08 report `runs/R08/20260917T1545Z_f0083_lattice_tube_admission_82d41c.md`, the F0083 intake/attempt history, and the newest neighboring R09 state. R09 is owned on G0013 and has no ownership overlap with F0083.

The current root ledger still warns that the R-series summary is stale and must be replaced only from complete current-target reports; I therefore keep the structured update in this report and do not edit shared roots.

## 2. Source/current-literature and ownership refresh

The original 2006 source was reread. Its Open problem (i) states exactly:

> Does there exist a discrete set of centers in `R^d` which admits two stable allocations differing on a nonnull set?

The same passage records the source's necessary exclusions: by its Theorems 2 and 3 such a set must have greater-than-quadratic growth and cannot arise from a translation-invariant point process. The paper's Theorem 2 gives uniqueness when all bounded-distance graphs are recurrent. Its Lemma 15 gives the site-optimal / center-optimal sandwich, and the paper explicitly notes that both Gale--Shapley algorithms are isometry-equivariant.

Fresh bounded searches dated 2026-09-17 used the exact title/authors plus `two stable allocations`, `discrete set`, `nonuniqueness`, `Lebesgue`, and later stable-allocation terminology. They recovered the original paper, Hoffman--Holroyd--Peres' 2009 *Tail Bounds for the Stable Marriage of Poisson and Lebesgue*, and Poisson/random-appetite/percolation follow-ups, but no later primary source claiming to resolve this exact deterministic nonuniqueness question. This remains bounded negative evidence only: worldwide open status and publication novelty are **UNVERIFIED**.

Ownership is unchanged and exclusive to R08 through `operations/claims/F0083.md`.

## 3. Preserved fact from the admitting run: radius-one locality in dimension four

I use, but do not reprove, the theorem proved in the admitting report:

> If `Xi subset Z^d` has appetite one, then in **every** stable allocation every center is sated and its territory has essential radius at most `sqrt(d)/2`.

For `d=4`, every stable territory therefore lies in the radius-one ball around its center. Consequently only lattice centers at distance strictly less than two can interact on a set of positive Lebesgue measure.

I also use the earlier active-cell representation, whose short argument is recalled here because it is central to the new proof. If all centers are sated and have finite territory radii `R_xi`, then, modulo null sets,

`C_xi(R) = {x : |x-xi| < R_xi and |x-xi| < |x-eta| for every eta != xi with |x-eta| < R_eta}`.

Indeed, a site assigned to `xi` cannot have a closer active center `eta`, because `eta` would covet it and the site would desire `eta`. Conversely, a site in `C_xi(R)` not assigned to `xi` would desire `xi`, while `xi` covets it because its distance is below the essential territory radius. Euclidean distance ties lie in a countable union of bisectors and hence are null.

## 4. B4 — prove the flat tangent model completely

The admitting construction put the candidate's transient channel on a large flat side of the missing tube. Before trying to force two allocations there, I tested the strongest possible negation: perhaps the flat side itself is already rigid.

It is.

### Theorem 1 — uniqueness for the critical four-dimensional half-space lattice

Let

`Lambda_- = {(-j,z) : j=0,1,2,..., z in Z^3} = Z_{<=0} x Z^3 subset R^4`

with appetite one. Then `Lambda_-` has an `L`-a.e. **unique stable Lebesgue allocation**.

This result is not covered by the source's recurrent-configuration theorem: the nearest-neighbor graph of `Lambda_-` is a four-dimensional half-space and is transient.

### Proof

By the radius-one locality theorem, every stable allocation of `Lambda_-` sats every center and every territory has essential radius at most one.

Let `psi^s` and `psi^c` be the site-optimal and center-optimal Gale--Shapley allocations. The source states that both algorithms are isometry-equivariant. Since `Lambda_-` is invariant under all translations by `{0} x Z^3`, each extremal allocation is layer-symmetric: all centers in the depth-`j` layer have the same territory radius. Write that radius as `r_j in [0,1]`.

I first analyze an arbitrary layer-symmetric stable allocation.

Fix the center `(-j,0)` and a transverse fundamental cube

`Q=[-1/2,1/2]^3`.

For `y in Q`, put `s=|y|^2` and

`a_r(y)=sqrt(max(r^2-s,0))`.

At transverse coordinate `y`, the radius-`r_k` active ball of layer `k` cuts the normal line in an interval centered at `-k` with half-length `a_{r_k}(y)`. No transverse translate in the same layer can matter before the translate with transverse coordinate zero: for `y in Q`, the zero translate is the closest center in that layer; if it is inactive, all other translates are even farther and are inactive as well. Because all radii are at most one, layers separated by two or more can meet only on a null boundary. Thus every fiber is an exact one-dimensional nearest-active-center problem involving only adjacent layers.

#### Step 1: no inward decrease is possible

Suppose an interior depth `j>=1` has

`r_{j-1} >= r_j` and `r_{j+1} >= r_j`.

Whenever the depth-`j` center is active on a fiber, both adjacent-layer active intervals extend at least as far as its own. Hence its cell on that fiber is cut at the two midpoints `+/-1/2`; its fiber length is exactly

`2 min(a_{r_j}(y),1/2)`.

If `r_j<1`, then on a positive-volume neighborhood of the corners of `Q` we have `a_{r_j}(y)<1/2`, so

`int_Q 2 min(a_{r_j}(y),1/2) dy < 1`.

That contradicts the fact that every center is sated. Therefore an interior weak local minimum can occur only at radius one.

Now assume some decrease occurs: `r_{j+1}<r_j`. Since `r_{j+1}<1`, the preceding observation forces `r_{j+2}<r_{j+1}`; inductively the radii then decrease strictly forever. They converge to a limit `L<1`. The depth-`k` cell volume depends only on the three adjacent radii and is bounded by an integrable constant. Dominated convergence therefore sends its volume to the equal-radius value

`int_Q 2 min(a_L(y),1/2) dy < 1`,

again contradicting the exact appetite-one volume. Hence no decrease occurs:

`r_0 <= r_1 <= r_2 <= ... <= 1`.                                      (4.1)

#### Step 2: the volume equations are triangular

At the boundary layer there is no shallower competitor. Therefore its fiber length is

`L_0(y)=a_{r_0}(y)+min(a_{r_0}(y),1/2)`,

and its appetite equation is

`F_0(r_0):=int_Q [a_{r_0}+min(a_{r_0},1/2)] dy = 1`.                  (4.2)

The left side is continuous and strictly increasing; it is zero at `r=0` and exceeds one at `r=1` because `a_1(y)>1/2` for a.e. `y in Q`. Thus (4.2) has a unique solution `r_0 in (0,1)`.

For an interior layer put `p=r_{j-1}` and `r=r_j`, so `p<=r` by (4.1). The deeper neighbor has radius at least `r`; whenever it can compete on the left, it is active by the time the midpoint is reached, so the left extent is `min(a_r,1/2)`.

The shallower neighbor has half-length `a_p`. On the right it starts blocking at the midpoint when `a_p>=1/2`, and otherwise starts blocking only when the normal coordinate reaches `1-a_p`. Define

`beta_p(y) = 1/2                    if a_p(y)>=1/2,`

`beta_p(y) = 1-a_p(y)              if a_p(y)<1/2.`

The exact fiber length is

`L(r,p;y)=min(a_r(y),1/2)+min(a_r(y),beta_p(y))`,

so the appetite equation is

`F_p(r):=int_Q L(r,p;y) dy = 1`.                                     (4.3)

For every `p<1`,

`F_p(p)=2 int_Q min(a_p(y),1/2) dy < 1`,                            (4.4)

while

`F_p(1)>1`.                                                           (4.5)

For (4.5), the first term is `1/2` a.e.; the second is at least `1/2` everywhere and strictly larger on the positive-volume corner set where `a_p<1/2<a_1`. Also `F_p(r)` is continuous and strictly increasing in `r` on `[p,1]`: for every `r<1` a positive-volume corner region remains unsaturated, so increasing `r` strictly increases the integrand there.

Consequently there is a unique map

`T(p) in (p,1)` with `F_p(T(p))=1`,                                  (4.6)

and every layer-symmetric stable radius profile must satisfy

`r_j=T(r_{j-1})` for `j>=1`.                                         (4.7)

In particular the profile is unique. It is strictly increasing and has limit one: if `r_j -> L<1`, dominated convergence in (4.3) would give `F_L(L)=1`, contradicting (4.4).

#### Step 3: the two Gale--Shapley extremals coincide

Both `psi^s` and `psi^c` are layer-symmetric, so Steps 1--2 give them the same unique radius sequence `(r_j)`. The active-cell representation then gives exactly the same territories a.e. Hence

`psi^s = psi^c` a.e.

Finally apply the source's Lemma 15(i). For any stable allocation `psi` and a.e. site `x`, for every `r`,

`g_x(psi^s,r) >= g_x(psi,r) >= g_x(psi^c,r)`.

Since the extremals coincide, all three distance-indicator functions coincide. Thus `psi(x)` is at the same distance from `x` as the common extremal allocation. Except on the null union of pairwise bisectors, two distinct centers cannot have the same distance. Therefore `psi` equals the extremal allocation a.e.

This proves Theorem 1. QED.

### Meaning for F0083

The source's recurrent criterion is only sufficient, and the half-space graph is transient, yet uniqueness still holds. Thus **transience by itself is far from enough**. More specifically, the locally flat part of the admitted tube candidate does not automatically carry a nonunique boundary condition.

This is the B4 outcome: a complete negative result on the simplest source-relevant tangent model.

## 5. B26 — the dimension-four boundary layer has an exact geometric attenuation constant

Dimension four is sporadic for this construction because the universal lattice radius is exactly one: `sqrt(4)/2=1`. That puts the intact lattice precisely at the face-neighbor contact scale and makes the boundary layer singular at fourth order.

The unique half-space profile from Theorem 1 lets us compute that singular relaxation exactly.

### Theorem 2 — exact asymptotic radius-deficit ratio

For the unique half-space profile `(r_j)`,

`(1-r_j)/(1-r_{j-1}) -> lambda_*`,                                  (5.1)

where `lambda_*` is the unique root in `(0,1)` of

`9 lambda^3 - 5 lambda^2 + 11 lambda - 7 = 0`.                       (5.2)

Numerically,

`lambda_* = 0.6171640568067426...`.                                  (5.3)

### Proof

Write

`epsilon_j = 1-r_j`, `d=2 epsilon_j`, `D=2 epsilon_{j-1}`.

Since `r_j>r_{j-1}` and `r_j->1`, we have `0<d<D->0`.

Only neighborhoods of the eight corners of `Q` contribute to the difference between the volume in (4.3) and one. At one corner write

`y_i=1/2-z_i`, `z_i>=0`, `S=z_1+z_2+z_3`.

Uniformly for `z=O(D)`, Taylor expansion around the critical value `a=1/2` gives

`a_{r_j}(y)-1/2 = S-d + O(D^2)`,

`a_{r_{j-1}}(y)-1/2 = S-D + O(D^2)`.                                (5.4)

Indeed `|y|^2=3/4-S+O(D^2)` and `r^2=1-2 epsilon+O(D^2)`, while the derivative of `sqrt(.)` at `1/4` is one.

Relative to the critical fiber length one, the leading fiber defect is therefore

`2(S-d)` for `0<=S<d`,

`min(S-d,D-S)` for `d<=S<=D`,

`0` for `S>=D`.                                                       (5.5)

The three-dimensional simplex slice `{z_i>=0, sum z_i=S}` has volume density `S^2/2 dS`. Hence the negative contribution from one corner is exactly, at leading order,

`N(d)=int_0^d 2(S-d)(S^2/2)dS = -d^4/12`,                           (5.6)

and the positive tent contribution is

`J(D,d)`
` = int_d^((D+d)/2) (S-d)(S^2/2)dS`
`   + int_((D+d)/2)^D (D-S)(S^2/2)dS`
` = (D-d)^2(7D^2+10Dd+7d^2)/192`.                                  (5.7)

The Taylor remainder in (5.4) is `O(D^2)` on a region of volume `O(D^3)`; the induced switching-surface displacement gives the same or smaller order. Thus the exact appetite equation has the uniform expansion

`-d^4/12 + (D-d)^2(7D^2+10Dd+7d^2)/192 + O(D^5)=0`.                 (5.8)

Put `lambda_j=d/D`. Dividing (5.8) by `D^4` shows that every subsequential limit `lambda in [0,1]` must satisfy

`(1-lambda)^2(7+10lambda+7lambda^2)=16lambda^4`.                    (5.9)

The left-minus-right side factors exactly as

`-(lambda+1)(9lambda^3-5lambda^2+11lambda-7)`.                       (5.10)

Let

`P(lambda)=9lambda^3-5lambda^2+11lambda-7`.

Then `P(0)=-7`, `P(1)=8`, and

`P'(lambda)=27lambda^2-10lambda+11`

has discriminant `100-4*27*11=-1088<0` and positive leading coefficient. Hence `P'` is positive on the real line and `P` has exactly one root in `(0,1)`. Since every subsequential limit of `lambda_j` must be that root, the full sequence converges, proving (5.1)--(5.3). QED.

### Exact finite self-check

The finite algebraic core was checked and archived at

- `artifacts/R08/20260917T1629Z_halfspace_ratio_exact.py`
- `artifacts/R08/20260917T1629Z_halfspace_ratio_exact.out`

The output begins `PASS exact symbolic checks` and verifies (5.6), (5.7), the factorization (5.10), the derivative discriminant `-1088`, endpoint signs, and the displayed numerical root. This is a **self-check of the finite algebra only**, not an independent audit of Theorems 1--2.

This is the B26 outcome: the critical dimension-four flat boundary has a sharp attenuation constant rather than a free boundary mode.

## 6. B28 — what is typical on the admitted tube, and what must be exceptional

The large flat faces of the deleted tube in `Xi_*` have an exact local half-space limit. Fix a face, stay a bounded lattice distance away from its edges/corners, and let `|n|` grow. Because `m_n -> infinity` and `m_{n+1}-m_n in {0,1}`, every fixed-radius neighborhood of such a face center eventually agrees with the corresponding neighborhood of `Lambda_-` after an isometry.

Theorem 1 therefore changes the construction strategy materially:

- a **typical locally flat face patch is rigid**, not a ready-made carrier of two stable allocations;
- the finite-energy channel proved in the admission report is still a necessary-looking graph structure, but graph transience alone does not turn into allocation nonuniqueness;
- any actual difference between the two Gale--Shapley extremals for `Xi_*` must exploit information not present in the flat tangent model: the slow change of `m_n`, the tube edges/corners, the two-ended geometry, or a boundary condition transmitted through those exceptional regions.

Theorem 2 supplies a quantitative scale for such a transmission. In the flat model, a radius deficit is attenuated by approximately `lambda_*` per lattice layer, so influence at depth `L` is naturally of order

`lambda_*^L`.

This suggests a better next construction than working directly on the tube face. Put the comparison channel on a **retreating shell** at depth

`L_n = floor(c log(2+|n|))`

inside the surviving lattice. Then the flat-boundary forcing is only polynomially large/small,

`lambda_*^(L_n) = (2+|n|)^(-c |log lambda_*| + o(1))`,

while `L_{n+1}-L_n` is eventually in `{0,1}`, so the local-interaction edges remain uniformly bounded. The cross-section still has order `m_n^2 ~ n^(3/2)` channels, whose finite-energy property was already proved in the admission report.

This is **not** yet obligation 2. The missing theorem is a comparison/barrier statement transferring the exact half-space attenuation to the slowly varying finite tube and then showing that the two opposite ends induce different limiting extremal profiles at one fixed central center. But the obstruction is now sharper: a direct flat-face harmonic mode is ruled out, and the only plausible source of nonuniqueness in this candidate is a genuinely global/exceptional geometric mode.

This is the B28 outcome: replacing the global candidate by its typical far-face tangent model does not solve the source; it proves that the typical region is unique and identifies where any counterexample must live.

## 7. Metric, stuck counter, and honest status

Frozen metric before: `1/2`.  
Frozen metric after: `1/2`.  
Movement: **NO MOVEMENT**.  
Unchanged count since F0083 admission: `1`.

Status:

`F0083 = OPEN_CURRENT_BOUNDED / ACTIVE R08 / PARTIAL / metric 1/2`.

I do not call the source solved, refuted, or closed. The half-space theorem is a proper restricted result and therefore remains PARTIAL relative to the source question.

The new result is nevertheless useful negative progress: it kills the simplest interpretation of the admitted finite-energy channel and replaces it with an exact attenuation law.

## 8. Next route

The next run should not repeat B4/B26/B28. The most promising source-sized route is now:

1. prove upper/lower comparison barriers for the radius profile of a face center of `Xi_*` in terms of the exact half-space profile, uniformly as `|n|->infinity` away from tube edges;
2. move the flow/channel to a depth `L_n ~ c log n` where the local radii are provably in the near-critical regime and the quartic defect-mass expansion from the admission report applies uniformly;
3. derive an effective one-dimensional two-ended boundary recursion for the defect masses on that retreating shell and determine whether its center-optimal and site-optimal boundary conditions yield distinct central limits.

A finite truncation discrepancy or simulation will not count as obligation 2 unless accompanied by a uniform positive lower bound surviving the truncation limit.

## 9. Model / scheduler controls

The model-control limitation is unchanged in the exposed interface: task controls include title, prompt, schedule/timing and enabled state, but no model-family selector, reasoning-effort selector, authenticated completed-run telemetry, or guaranteed hour-long execution. Therefore `GPT-6 / maximum` remains a prompt request only here.

The repository policy records historical `You cannot modify this task` responses for some authorization contexts, including P26, and also records that P26 was later modifiable from another authorized context. The legitimate workaround is the owning/authorized context, supported ownership/admin transfer, or platform support; duplicating a task or editing repository text does not change the native runtime model. No scheduler change was attempted in this run, consistent with the current R08 instruction.

## 10. Structured ledger delta

```yaml
ledger_delta:
  track: R08
  active_target: F0083
  source: Hoffman-Holroyd-Peres 2006, Open problem (i)
  owner: R08
  metric_name: frozen obligations proved for explicit Xi_*
  before: 1/2
  after: 1/2
  movement: no movement
  unchanged_count: 1
  status: PARTIAL
  source_status: OPEN_CURRENT_BOUNDED
  theorem_added:
    - critical half-space lattice Z_{<=0} x Z^3 has a.e. unique stable appetite-one Lebesgue allocation
    - unique half-space radius deficit ratio tends to lambda_*=0.6171640568067426..., root of 9x^3-5x^2+11x-7
  finite_self_check:
    script: artifacts/R08/20260917T1629Z_halfspace_ratio_exact.py
    output: artifacts/R08/20260917T1629Z_halfspace_ratio_exact.out
    result: PASS
    scope: finite symbolic algebra only
  methods: [4, 26, 28]
  prior_target_I0082:
    state: RETIRED_FROZEN
    metric: 2/3
    retirement_count: 6
  next_obligation: prove positive-measure nonuniqueness for the exact Xi_* candidate; no finite-sample surrogate
```
