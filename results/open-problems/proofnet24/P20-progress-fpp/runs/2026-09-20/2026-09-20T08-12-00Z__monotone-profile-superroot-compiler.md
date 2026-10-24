Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied model/reasoning receipt is exposed, so I do not claim GPT-6.**

# P20 T10 — monotone target-difference profile and a super-root fresh-disagreement compiler

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent: `operations/claims/PROB10-10.md`.  
Model: undirected nearest-neighbor FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for strict convexity. The theorem arguments below are `CANDIDATE_PROVED` pending later independent review.

## 1. Exact source, ownership, and original-problem before/after

The exact source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in §2.5.1: **show that if `F` is a continuous distribution then the limit shape is strictly convex**. Section 2.8 explicitly discusses strict convexity as conjectural. The canonical repository target freezes the iid `Exp(1)`, undirected nearest-neighbor `Z^2` special case. Directed integrable models and sampled numerical curvature do not settle it.

Write `mu` for the deterministic time-constant norm and

`Delta_12 := 2 mu(e1) - mu(e1+e2) >= 0`.

The frozen source milestone is

`c_* := largest rigorously proved c>=0 with Delta_12>=c`.

- **before:** `c_*=0`;
- **after:** `c_*=0`.

So this run does not prove even the axis/diagonal strict inequality. The mathematical gain is a substantially weaker sufficient block criterion obtained by combining two already-proved P20 ingredients with the newest finite-HJB/Alexander budget:

1. the target-difference potential is monotone along the actual axis geodesic and its total increase is exactly the finite triangle residual;
2. a fixed positive conditional disagreement probability need occur on only `omega(sqrt(n log n))` fresh candidates, not linearly many;
3. without a uniform probability floor, total joint visit/disagreement mass `M_n` over only `O(n)` fresh candidates need be only

   `M_n >> n^(3/4) (log n)^(1/4)`,

   rather than order `n`.

This is a source-valid reduction: once either condition is established with controlled block loss, it forces `Delta_12>0`.

## 2. Essential dependencies consumed and failures preserved

I read only the dependencies needed for this attack:

- `operations/PROGRESS20_2026-09-20.md` and its LIVE20 pairing P20 with P04 on T10;
- `operations/claims/PROB10-10.md` and the current exclusion state inherited by the active T10 lane;
- P20 `2026-09-20T02-20-00Z__two-target-disagreement-energy.md`, especially `P20-FPP-TWO-TARGET-DISAGREEMENT-ENERGY-08` and `P20-FPP-FRESH-CANDIDATE-COMPILER-09`;
- P20 `2026-09-20T07-12-00Z__finite-hjb-flatness-budget.md`, especially the ADH/Alexander `O(sqrt(n log n))` flatness budget;
- P04's newest `2026-09-20T07-44-45Z__moving-strip8-wandering-cone1640.md`.

The R08 failure history remains binding and is not reset:

- shared bypasses invalidate multiplication of nominally independent local surgery gains;
- pointwise finite-scale strict triangle saving fails on positive-probability cylinder events;
- old fixed-corner blocks did not reach the axis/diagonal threshold;
- R07/KPZ fluctuation statements are not curvature theorems.

The present proof does not multiply independent surgeries. It charges one exact monotone potential along the actual `0`-to-`ne1` geodesic and uses expectation only after the samplewise identity.

## 3. Fresh literature boundary, 20 September 2026

The arXiv/HTML source for ADH was rechecked. Question 4 is still the literal statement above, and §2.8 states that strict convexity is conjectural.

Three nearby results were rechecked because they might plausibly interact with the new `sqrt(n log n)` threshold:

1. **Lalley (2003), Strict Convexity of the Limit Shape in First-Passage Percolation.** Lalley proves strict convexity from asymptotic straightness of geodesics plus centered nondegenerate passage-time limit laws. Those hypotheses are not known for ordinary Exp(1) FPP under the hypothetical flat-face regime and therefore cannot be imported here.
2. **Pemantle--Peres, Planar first-passage percolation times are not tight.** For Exp(1), passage times have logarithmically growing variance/non-tightness. This is scalar fluctuation information; it does not provide target-policy disagreement along the optimizing axis geodesic.
3. **Elboim, Small ball probabilities for the passage time in planar first-passage percolation (arXiv:2406.10971, later ECP).** For absolutely continuous positive weights, including Exp(1), every unit interval has probability at most `C/sqrt(log |x-y|)`. This gives genuine anti-concentration but again does not anchor the target-distance difference to the supporting plane or force disagreement on the adaptive geodesic.

A bounded current search recovered no theorem closing the exact iid Exp(1), undirected nearest-neighbor `Z^2` strict-convexity target. Search misses are bounded negative evidence only; publication novelty and exhaustive worldwide openness are **UNVERIFIED**.

## 4. Exact monotone target-difference potential

The preceding P20 reports used residuals. There is a useful scalar form that exposes exactly what a block transfer must accumulate.

Let `G` be any finite connected graph with positive edge weights. Fix two targets `A,C` and define

`Phi(x) := T(x,A)-T(x,C)`.

For an oriented edge `(x,y)`, define the target residuals

`r_A(x,y) := tau_xy + T(y,A)-T(x,A) >= 0`,

`r_C(x,y) := tau_xy + T(y,C)-T(x,C) >= 0`.

Then identically

`Phi(y)-Phi(x) = r_A(x,y)-r_C(x,y)`.                         (4.1)

Let `Gamma_C=(x_0,...,x_k)` be any geodesic from `x_0=o` to `x_k=C`. Along every oriented geodesic edge,

`T(x_i,C)=tau_i+T(x_{i+1},C)`,

so `r_C(x_i,x_{i+1})=0`. Therefore (4.1) becomes

`Phi(x_{i+1})-Phi(x_i)=r_A(x_i,x_{i+1})>=0`.                  (4.2)

Thus `Phi` is samplewise nondecreasing along the `C`-geodesic.

### P20-FPP-MONOTONE-TARGET-DIFFERENCE-28 — CANDIDATE_PROVED

For every such `Gamma_C`,

`boxed{ sum_{e in Gamma_C} r_A(e)
      = Phi(C)-Phi(o)
      = T(o,C)+T(C,A)-T(o,A). }`                              (4.3)

In particular the finite triangle residual is not merely a sum of nonnegative terms: it is the **total monotone increase of one scalar target-difference potential along the actual optimizing geodesic**.

#### Proof

Equation (4.2) gives nonnegative increments and summing telescopes. Since `T(C,C)=0`,

`Phi(C)=T(C,A)`,
`Phi(o)=T(o,A)-T(o,C)`,

which gives (4.3). QED.

This formulation is useful for P04 because interface errors can be charged directly against an increase of `Phi`; they cannot cancel by sign inside a block. Internally a block may still need both continuation profiles to certify a policy disagreement, but the quantity transferred between blocks is scalar and monotone.

## 5. Specialization to the axis/diagonal defect

Set

`C_n = n e1`,
`A_n = n(e1+e2)`,

and let `Gamma_n` be the a.s.-unique `0`-to-`C_n` geodesic. Define

`D_n := T(0,C_n)+T(C_n,A_n)-T(0,A_n)`.

By (4.3),

`D_n = Phi_n(C_n)-Phi_n(0)
     = sum_{e in Gamma_n} r_{A_n}(e) >=0`.                    (5.1)

Writing `h(x)=E T(0,x)`, translation and square-lattice symmetry give

`E D_n = 2 h(ne1)-h(n(e1+e2))`.                              (5.2)

Hence

`E D_n/n -> Delta_12`.                                       (5.3)

The key point for the next section is that the same finite residual `D_n` is covered both by the old Exp-star disagreement lower bound and by the new Alexander flatness upper budget.

## 6. Alexander budget applied directly to `D_n`

ADH Theorem 3.33 records the classical mean-convergence estimate under hypotheses satisfied by Exp(1): for a finite constant `C_A` and all sufficiently large `|x|`,

`mu(x) <= h(x) <= mu(x)+C_A sqrt(|x| log |x|)`.

For the two terms in (5.2), it is enough to use the upper error only on the two axis copies and the deterministic lower bound on the diagonal term. Thus, after enlarging `C_A` harmlessly to absorb the norm convention,

`E D_n <= n Delta_12 + 2 C_A sqrt(n log n)`.                  (6.1)

Equivalently,

`boxed{ n Delta_12 >= E D_n - 2 C_A sqrt(n log n). }`         (6.2)

Under the contradiction hypothesis `Delta_12=0`, the *entire monotone increase* of `Phi_n` along the axis geodesic has expectation only `O(sqrt(n log n))`.

This scalar version is slightly cleaner than the symmetric mixed-HJB formulation of the preceding run: no averaged cocycle is needed and the local Exp-star theorem from the 02:20 report applies to exactly the same residual `D_n`.

## 7. Combine with the Exp-star fresh-candidate inequality

Recall the proved local theorem from P20's 02:20 report. A candidate star `X_j` is selected while its four incident Exp(1) edges are still fresh. Let

`D_j = { X_j lies on Gamma_n and the A_n- and C_n-Bellman winners at X_j disagree }`,

let `F_j` be the information available before exposing that star, and put

`p_j := P(D_j | F_j)`.

The identity of the candidate must be fresh, but **the visit event and disagreement event may depend on the revealed star**. Define

`g(p) = [p+(1-p) log(1-p)]/3`, `0<=p<1`, and `g(1)=1/3`.

The earlier exact Exp-star argument proves

`g(p) >= p^2/6`                                               (7.1)

and, for pairwise edge-disjoint candidate stars whose charged geodesic residuals are not double-counted,

`E D_n >= E sum_j g(p_j)`.                                   (7.2)

The old report used (7.2) only at *linear* scale. Combining it with (6.2) yields a much weaker sufficient condition.

### P20-FPP-SUPERROOT-FRESH-DISAGREEMENT-COMPILER-29 — CANDIDATE_PROVED

For every fresh-candidate family as above,

`boxed{
 n Delta_12
 >= E sum_j g(p_j) - 2 C_A sqrt(n log n).
}`                                                                  (7.3)

More generally, if a P04 block proxy loses a nonnegative amount `L_n` and proves only

`D_n >= sum_j charged_j - L_n`,

then

`boxed{
 n Delta_12
 >= E sum_j g(p_j) - E L_n - 2 C_A sqrt(n log n).
}`                                                                  (7.4)

#### Proof

Use (7.2) (or its loss version) in (6.2). No independence between different disagreement events is needed beyond the fresh-star hypothesis used to obtain each local charge; candidate residuals are a subset of the nonnegative terms in the single exact sum (5.1). QED.

### Corollary 29A: only super-root many robust blocks are needed

Suppose `G_n` candidates satisfy `p_j>=p0` for a fixed `p0>0`. Then

`n Delta_12 >= g(p0) E G_n - E L_n - 2 C_A sqrt(n log n)`.     (7.5)

Therefore

`g(p0) E G_n - E L_n = omega(sqrt(n log n))`

already implies `Delta_12>0`.

With exact transfer (`L_n=0`), P04 no longer needs a positive linear density of robust disagreement blocks: **any `omega(sqrt(n log n))` expected count suffices**.

### Corollary 29B: total disagreement mass threshold

Assume there are at most `C n` candidates almost surely and put

`M_n := E sum_j p_j`.

By (7.1), Cauchy--Schwarz, and Jensen,

`E sum_j g(p_j)
 >= (1/6) E sum_j p_j^2
 >= M_n^2/(6 C n)`.                                          (7.6)

Therefore

`boxed{
 n Delta_12
 >= M_n^2/(6 C n) - E L_n - 2 C_A sqrt(n log n).
}`                                                                  (7.7)

In particular, with negligible loss relative to `M_n^2/n`,

`boxed{
 M_n >> n^(3/4) (log n)^(1/4)
   ==> Delta_12>0.
}`                                                                  (7.8)

The exponent `3/4` is exactly the cost of the quadratic small-`p` modulus `g(p)~p^2/6` combined with the `sqrt(n log n)` mean-convergence error.

### Corollary 29C: polynomially vanishing per-block disagreement is allowed

Suppose at least `alpha n` fresh candidates satisfy

`p_j >= n^(-1/4+epsilon)`

for fixed `alpha,epsilon>0`, and the block loss is `o(n^(1/2+2epsilon))`. Then

`E sum_j g(p_j)
 >= (alpha/6) n^(1/2+2epsilon)`,

which dominates `sqrt(n log n)`. Hence `Delta_12>0`.

So P04 may allow the per-block joint visit/disagreement probability itself to tend to zero polynomially, as long as it decays more slowly than `n^(-1/4)` on linearly many fresh candidates.

## 8. What this changes for P04

P04's newest moving-centered strip report proves a genuine but different T10 partial theorem:

- a rigorous axis upper bound `mu(e1) <= 294639/500000 = 0.589278`;
- a reflected strict-triangle cone down to slope `41/25=1.64` with defect coefficient `23/125000`;
- block independence by assigning disjoint physical horizontal slabs, while an adaptive vertical center is allowed;
- only an `O(sqrt N)` final endpoint repair.

Those are source-valid restricted-direction gains, but the constructed moving-strip path is **not** the actual `0`-to-`ne1` geodesic. It therefore cannot simply be substituted for `Gamma_n` in (5.1)--(7.7).

The useful part for the P20 interface is the physical-edge ownership architecture. The next P04-compatible target is:

1. adapt the slab bookkeeping to an exploration/proxy that retains fresh candidate stars relevant to the actual `C_n` geodesic;
2. certify either a robust count `G_n` or the total conditional joint mass `M_n`;
3. charge any mismatch between the block proxy and the true monotone `Phi_n` increase as an explicit `L_n`;
4. beat one of the two thresholds

   `g(p0) E G_n - E L_n >> sqrt(n log n)`,

   or

   `M_n^2/(6 C n) - E L_n >> sqrt(n log n)`.

This is materially weaker than the pre-07:12 demand of a linear residual density. In particular, a block construction that only produces `n^(1/2+epsilon)` robust disagreements is now enough.

A practical state reduction is also available: the transferred quantity across a block can be the scalar `Phi_n=T(.,A_n)-T(.,C_n)`, whose rise along the true `C_n` geodesic is nonnegative. A block solver may still need richer continuation data internally to certify policy disagreement, but its output obligation is only a lower bound on scalar monotone rise plus a controlled loss.

## 9. A fresh alternate attack that fails honestly: scalar anti-concentration is not yet curvature

The new Elboim small-ball theorem is tempting because Exp(1) is absolutely continuous and it forces the passage-time distribution to spread over a growing number of unit intervals. It indeed implies fixed interquantile ranges grow at least on the order of `sqrt(log n)`: an interval of length `L` is covered by at most `ceil(L)` unit intervals.

But this does **not** fill (7.3). The missing event is joint and pathwise: a candidate must be visited by the optimizing `C_n` geodesic and the `A_n,C_n` Bellman policies must disagree there. Scalar anti-concentration of `T(x,y)` does not control that event. Nor does it place a high passage-time quantile within `o(sqrt(log n))` of `n mu`, which would be needed to reproduce Lalley's negative conditional-mean block mechanism from anti-concentration alone.

Thus no fluctuation theorem is mislabeled as curvature here. The useful conclusion from this failed route is precise: **the next missing input is path-conditioned target-policy separation, not more scalar passage-time anti-concentration.**

## 10. Exact finite-graph sanity check

I executed a supplementary exact-rational checker on a 35-vertex undirected grid with 58 positive rational edge weights. It computes exact shortest paths by `Fraction` arithmetic and verifies along an actual `C`-geodesic that

- `r_C=0` edge by edge;
- `Phi(y)-Phi(x)=r_A(x,y)>=0` edge by edge;
- the total monotone increase equals the finite triangle residual exactly.

The nonzero test instance gives

`triangle_residual = 278/97`,
`Phi(C)-Phi(0) = 278/97`,
`sum_{Gamma_C} r_A = 278/97`.

The archived output ends

`P20-T10-MONOTONE-TARGET-DIFFERENCE-SANITY: ALL_EXACT_CHECKS_PASS`.

Artifacts:

- `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T08-12-00Z__monotone_target_difference_sanity.py` @ creation commit `edabb862e6569ed41d39128589a462d3fdbb8a0b`;
- matching output @ creation commit `9bbbbfdb3e759934861fbea16a73286f88cbbf18`.

This checker is supplementary only; the theorem proof is the exact telescoping argument above.

## 11. Residual obstruction and next attack

The obstruction is no longer the size of a local Exp toll and no longer the need for linear density. It is **fresh path-conditioned policy separation**.

The old shared-bypass problem survives in one precise form: the true axis geodesic may, under hypothetical flatness, follow a long route on which the `A_n`- and `C_n`-target policies mostly agree. The monotone-potential identity shows that this is exactly what flatness would have to do: keep the expected total increase of `Phi_n` below `O(sqrt(n log n))`.

The next attack should therefore be a reserved-frontier/Dijkstra exploration, exploiting exponential memorylessness rather than demanding fully untouched deterministic stars. P04's moving-strip calculation already formulates Exp FPP as a finite-state Richardson/Dijkstra infection process and proves that adaptively recentered physical slabs can remain independent. The concrete objective is to expose a `C_n`-directed shortest-path frontier while reserving a bounded set of not-yet-raced edges, and prove one of:

- `omega(sqrt(n log n))` frontier states with conditional disagreement probability bounded below; or
- total conditional joint mass `M_n >> n^(3/4)(log n)^(1/4)` with only `O(n)` charged states.

If the Dijkstra conditioning destroys the four-fresh-edge Exp-star law, the failure should be stated exactly and the local theorem re-derived for the residual exponential clocks actually left on the frontier. That is the next genuinely model-specific step.

## 12. Short cyclic-interval handoff

The displaced P20 source `FOKAM-BITJOKA-2026-CYCLIC-INTERVAL` remains preserved and is not reopened. The source-literal YES proof candidate `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` and its supplementary exact finite sanity artifact remain intact. P26's full-proof/source-quantifier audit remains PASS; the last recovered independent-audit gate remained `1/2`. No completed certification or publication-novelty claim is implied, and no research time in this run was spent waiting for the missing audit.

## 13. `ledger_delta`

- `PROB10-10`: **OPEN / PARTIAL**; full strict convexity not proved.
- Original axis/diagonal metric: `c_* : 0 -> 0`.
- Add `P20-FPP-MONOTONE-TARGET-DIFFERENCE-28 = CANDIDATE_PROVED`: on a target-`C` geodesic, `Phi=T(.,A)-T(.,C)` is nondecreasing and its total increase is exactly the finite triangle residual.
- Add `P20-FPP-SUPERROOT-FRESH-DISAGREEMENT-COMPILER-29 = CANDIDATE_PROVED`: `n Delta_12 >= E sum g(p_j) - E L_n - 2 C_A sqrt(n log n)`.
- New P04 success regime: fixed-`p0` robust blocks need only `omega(sqrt(n log n))` count; with `K_n<=Cn`, total joint mass `M_n >> n^(3/4)(log n)^(1/4)` suffices when losses are lower order.
- Consumed P04 moving-strip8 theorem as complementary restricted-direction progress only; did not substitute its explicit path for the actual axis geodesic.
- Fresh anti-concentration/Lalley route checked and rejected as insufficient without path-conditioned target-policy separation.
- Cyclic-interval proof/audit history preserved unchanged; no certification claim.
- Next attack: Exp-memoryless reserved-frontier/Dijkstra version of the fresh-disagreement compiler.

END OF P20 FPP RUN REPORT
