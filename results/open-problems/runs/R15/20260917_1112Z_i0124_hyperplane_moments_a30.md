Model actually run: **GPT-5.6 Sol. Reasoning: UNVERIFIED — not GPT-6 maximum. ACTIVE SUCCESSOR METRIC MOVEMENT: I0124 `H_288: 96 -> 111`; predecessor I0076 remains retired/frozen at `2/4`, and RS-2026-CL-B remains retired/frozen at `4/4`. Methods: #5 ADD A PARAMETER AND DIFFERENTIATE, #10 DERANDOMIZE, #24 FIND THE EXTREMAL OBJECT.**

# R15 run — I0124 cap-set successor admission and hyperplane-moment forcing

## 1. Continuity and exclusions

I did not reopen either predecessor.

- **I0076 / Burdzy–Scheutzow Problem 7.2** remains `OPEN / PARTIAL / RETIRED-HANDOFF`, positive-route metric `2/4`. Its exact source hypothesis is FBM + BBM plus independence, at an arbitrary finite random time, of the two complete centered half-processes. No deterministic-time or stopping-time replacement is made. Problem 7.5 remains excluded.
- **RS-2026-CL-B** remains `REFUTED AS PRINTED / RETIRED-HANDOFF / AUDIT-PENDING`, fixed metric `4/4`. A fresh repository search in this run still found no P26 source-level PASS and no distinct OTHER-track source-level PASS, so it is not called CLOSED.
- The latest visible R17 report still labels the Chvatal–Sankoff source problem `OPEN` and R17 `PARTIAL`; there is no R17 source-closure package for R15 to audit.

The previous R15 rotation-hold report reserved moves #5, #10 and #24. I used exactly those and did not repeat the preceding triple.

## 2. Successor admission: I0124

The section-J queue row I0124 is the finite cap-set problem in `AG(7,3)`. I performed the missing admission checks rather than dispatching from the pending row blindly.

**Original source.** Henry Robert Thackeray, *The cap set problem: Up to dimension 7*, arXiv:2206.09804 (2022). The source defines an `s`-cap `n`-flat as an `s`-point subset of an affine `n`-space over `F_3` with no three collinear, and asks for the maximum size. It proves two facts especially relevant here:

1. every 110-cap in dimension 6 is a 112-cap with two cap points removed;
2. there is no 289-cap in dimension 7.

The classical Calderbank–Fishburn construction supplies a 236-cap in `AG(7,3)`. Thus the current working rigorous interval recovered in this bounded pass is

`236 <= c_{7,3} <= 288`.

**Current-literature pass, dated 2026-09-17.** Queries included `Henry Robert Thackeray cap set problem up to dimension 7 289 cap`, `cap set AG(7,3) 236 2026 288 Thackeray`, `AG(7,3) cap 236`, `cap set problem dimension 7 2026`, and later-author/publication checks. I recovered Thackeray's live arXiv abstract and current university publication page, the continuing 236 Calderbank–Fishburn benchmark, and 2026 cap-set work in other finite-field regimes, but no source-matching exact solution for dimension 7. This is bounded dispatch evidence, not a claim of exhaustive worldwide novelty.

**Ownership pass.** Immediately before claiming, `operations/claims/I0124.md` returned 404 and a repository-wide search for `I0124` recovered only the pending queue row. I therefore created the claim **create-only** at commit `759745dcb77c382c5d3739418543fccfab6fd433`. No other track's file was overwritten.

For context, the same section-J sweep also showed why several superficially attractive rows should not be stolen as substitutes: I0125 is now explicitly claimed by another native task; recent literature has moved the Lonely Runner row beyond its stale `n=8` wording; recent claimed resolutions make the Seymour and Sendov rows unsuitable for immediate admission without separate adjudication.

## 3. Frozen metric

For I0124 I freeze the scalar

`H_288 := largest certified H such that every hypothetical 288-cap A subset AG(7,3) has an affine 6-flat K with |A intersect K| >= H`.

The trivial average over the three parallel hyperplanes in any direction gives `H_288 >= 96`. This run proves

`H_288 >= 111`.

So the fixed scalar moves **96 -> 111**. The global interval `[236,288]` does not yet move and is not substituted for this metric.

## 4. New idea before code

The key idea is to stop searching for a 288-cap directly and instead ask what its complete hyperplane-slice distribution would be forced to look like. A cap has no collinear triples, so its first three hyperplane-incidence moments are exactly computable. Center the three slices in each parallel class at their mean 96. The global centered cubic moment turns out to be *too negative* to be compatible with every slice being at most 110. This deterministically forces a slice of size at least 111.

This is the #5/#10/#24 route in one object:

- **#5 parameterize:** slice deviations `x=h-96` expose a moment ratio.
- **#10 derandomize:** average over all 1093 hyperplane directions instead of searching sampled slices.
- **#24 extremal object:** a hypothetical top-size 288-cap is forced into a nearly extremal 6-dimensional slice, directly adjacent to Thackeray's 110/112 rigidity theorem.

## 5. Theorem proved this run

**Theorem (R15-I0124-H111).** If `A` is a 288-cap in `AG(7,3)`, then some affine 6-dimensional hyperplane `K` satisfies

`|A intersect K| >= 111`.

### Proof

Let `h_K=|A intersect K|`, with `K` ranging over all affine hyperplanes of `AG(7,3)`.

There are

`N = (3^7-1)/(3-1) = 1093`

linear hyperplane directions and therefore `3N=3279` affine hyperplanes.

A point lies in one affine hyperplane from each direction, hence

`sum_K h_K = 288*1093 = 314784`.                                           (1)

A fixed unordered pair of distinct points is contained in

`(3^6-1)/(3-1) = 364`

affine hyperplanes: its direction imposes one homogeneous linear condition on the hyperplane normal. Therefore

`sum_K C(h_K,2) = C(288,2)*364 = 15043392`.                              (2)

Because `A` is a cap, every three distinct points of `A` are affinely independent: a dependent triple in affine dimension one would be collinear. A fixed unordered triple therefore imposes two independent conditions on the normal and lies in

`(3^5-1)/(3-1) = 121`

affine hyperplanes. Thus

`sum_K C(h_K,3) = C(288,3)*121 = 476732256`.                             (3)

Using `h^2=2 C(h,2)+h` and `h^3=6 C(h,3)+6 C(h,2)+h`, (1)–(3) give

`sum_K h_K^2 = 30401568`,

`sum_K h_K^3 = 2950968672`.                                               (4)

Now put `x_K=h_K-96`. Since there are 3279 affine hyperplanes, direct expansion of (1) and (4) gives the exact centered moments

`D2 := sum_K x_K^2 = 182304`,

`D3 := sum_K x_K^3 = -2584224`.                                           (5)

Suppose for contradiction that every affine hyperplane has `h_K <= 110`.

Fix one direction, whose three parallel slice sizes are `a,b,c`. They partition `A`, so

`a+b+c=288`.

Set `x=a-96`, `y=b-96`, `z=c-96`. Then

`x+y+z=0`, and, under the supposition, `x,y,z <= 14`.

I claim directionwise that

`x^3+y^3+z^3 >= -14(x^2+y^2+z^2)`.                                      (6)

Indeed, because `x+y+z=0`,

`x^3+y^3+z^3 = 3xyz`.

If `xyz >= 0`, the left cubic sum is nonnegative and (6) is immediate. If `xyz<0`, after relabeling write

`x=-u, y=v, z=w`,

with `u=v+w` and `v,w>0`. The upper-slice assumption gives `v,w <=14`. Hence

`-(x^3+y^3+z^3)/(x^2+y^2+z^2)`

`= 3(v+w)vw / (2(v^2+vw+w^2))`

`<= (v+w)/2`

`<= 14`,

where the first inequality is exactly `3vw <= v^2+vw+w^2`, equivalent to `2vw <= v^2+w^2`. This proves (6).

Sum (6) over all 1093 directions. Each affine hyperplane appears exactly once. We obtain

`D3 >= -14 D2`,

or

`D3 + 14 D2 >= 0`.                                                       (7)

But the exact values (5) give

`D3 + 14 D2 = -2584224 + 14*182304 = -31968 < 0`,

contradicting (7). Therefore the supposition `h_K<=110` for all `K` is impossible, and some affine 6-flat has at least 111 cap points. QED.

## 6. Exact finite certificate

After the proof was fixed, I wrote and executed an exact-integer checker rather than using floating point. It verifies all incidence constants and centered moments above, and also enumerates all 946 integer slice triples `(a,b,c)` with `0<=a,b,c<=110` and `a+b+c=288`, checking directionwise that

`(a-96)^3+(b-96)^3+(c-96)^3 + 14[(a-96)^2+(b-96)^2+(c-96)^2] >= 0`.

The checker reports minimum gap zero, while the global exact moment value is `-31968`, so the contradiction is exact.

Artifacts:

- `artifacts/R15/20260917_1112Z_i0124_hyperplane_moments_exact.py`
- `artifacts/R15/20260917_1112Z_i0124_hyperplane_moments_exact.out`

The archived output begins `PASS exact hyperplane-moment checker` and ends with the source-valid H111 conclusion.

## 7. What this does and does not prove

This is real movement but **not** a solution of the dimension-7 cap problem. The rigorous global interval remains `[236,288]`.

The new bridge is that any hypothetical 288-cap must contain a 111-point cap in an affine 6-flat. Thackeray's source theorem classifies all 110-caps in dimension 6 as a 112-cap minus two points. The natural next research question is therefore not another global brute-force search: it is whether the forced 111-slice and the two complementary parallel slices can be made compatible with the rigid 6-dimensional near-extremal structure. A source-valid contradiction would eliminate size 288 and lower the global upper endpoint to 287.

I do **not** infer that every 111-cap has a unique 112-cap extension; that would require a separate proof. I also do not count numerical candidate caps as evidence.

## 8. Current obstruction and next-method direction

Remaining obligation for this active top case:

`classify / obstruct the extension data of a forced >=111 affine 6-flat slice inside a hypothetical 288-cap`.

The most promising next attack is to exploit the line-completion restrictions between the three parallel slices after putting the 111-slice into a near-112-cap normal form. This should use actual 6D extremal structure, not manufacture a fourth raw moment unless that moment couples to the classified slice geometry.

## 9. Model / scheduler control status

The model-control limitation is still unchanged. This run actually reports GPT-5.6 Sol with reasoning telemetry UNVERIFIED. The exposed scheduler/task surface provides title/prompt, schedule, timing mode and enabled state, but no writable model-family selector, no reasoning-effort selector, no authenticated applied-run model telemetry, and no guaranteed hour-long duration control. Prompt text requesting GPT-6/maximum therefore cannot verify that setting.

Changing this requires an authorized product/backend or owner/admin task surface that exposes and persists model and effort fields and provides run telemetry. The historical P26 `You cannot modify this task` response is an authorization/context boundary; the legitimate workaround is to act from the owning authorized context, change ownership/permissions where supported, or use platform support. It is not legitimate to duplicate the task or bypass permissions.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  source:
    canonical_id: I0124
    author: Henry Robert Thackeray
    title: "The cap set problem: Up to dimension 7"
    year: 2022
    locator: "arXiv:2206.09804"
    target: "determine c_{7,3}, the maximum cap size in AG(7,3)"
  ownership:
    status: CLAIMED_CREATE_ONLY
    claim_path: operations/claims/I0124.md
    claim_commit: 759745dcb77c382c5d3739418543fccfab6fd433
  metric:
    name: H_288
    definition: "largest certified H such that every hypothetical 288-cap has an affine 6-flat slice of size at least H"
    before: 96
    after: 111
    movement: "+15"
  global_context:
    cap_interval_before: "[236,288]"
    cap_interval_after: "[236,288]"
  status: PARTIAL
  unchanged_count: 0
  tried_moves: [5, 10, 24]
  remaining_obligation: "use the forced >=111 six-flat slice plus exact near-extremal 6D structure to obstruct or classify a hypothetical 288-cap"
  evidence:
    - artifacts/R15/20260917_1112Z_i0124_hyperplane_moments_exact.py
    - artifacts/R15/20260917_1112Z_i0124_hyperplane_moments_exact.out
    - "full theorem proof in this immutable report"
  audits: []
  predecessors:
    I0076: "OPEN/PARTIAL/RETIRED-HANDOFF; 2/4"
    RS-2026-CL-B: "REFUTED-AS-PRINTED/RETIRED-HANDOFF/AUDIT-PENDING; 4/4"
```

No email, Gmail, Drive, public posting, purchase, permission change, scheduler modification, shared-root edit, or other-track edit was performed.