Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NATIVE I0076 METRIC NO MOVEMENT: `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE -> NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`. RETAINED-SCREEN MOVEMENT: the PSD/null/projective-fourth-order subsystem for F0111 is now characterized exactly by a Euclidean polygon condition, and at the exact middle-branch point `(delta,z)=(1/2,-3/5)` that condition strengthens the old singleton-block support bound from `M>=4` to `M>=6`. Methods #1, #18, #27.**

Problem/source governing the native R15 slot: Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Problem 7.2, intake I0076.

Retained screen used only because the native source has no surviving frozen candidate and no source-valid metric to advance: Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Problem 10.9, specialized to the `k=2` cardinality-threshold hazard. This retained screen remains **SELF_CHECK_ONLY / NOT CLAIMED / PENDING**.

## 1. Exact native source scope and continuity

I rechecked the primary Burdzy--Scheutzow PDF this run rather than relying on the scheduler title.

Definition 2.1 says:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. such that each complete centered future `(X_{S_n+t}-X_{S_n})_{t>=0}` is standard Brownian motion;
- `X` is BBM iff `(X_{-t})_{t in R}` is FBM;
- `X` is 2BM iff there is a random time `S` such that the complete centered future and complete centered past at `S` are independent standard Brownian motions.

Problem 7.2 asks whether FBM + BBM + existence of an arbitrary random real time `T` at which

`(X_{T+t}-X_T)_{t>=0}` and `(X_{T-t}-X_T)_{t>=0}`

are independent implies 2BM. The source does **not** say that `T` is a stopping time and does **not** separately assume that either seam half is Brownian. Problem 7.5 is separate and remains excluded.

The controlling R15 six-run handoff remains `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`:

- the source Theorem-6.1 construction has FBM, BBM and non-2BM, but R15 proved candidate-specifically that it has no source-required independent real seam;
- the later Brownian-prefix/BES construction has exact independent seam plus FBM and BBM, but was proved to be 2BM by finite-intensity excursion-Palm de-biasing.

Hence there is no surviving frozen counterexample candidate. The requested four-obligation counterexample score is therefore still honestly **not scoreable**; the historical `2/4` positive-route score and the eliminated candidates' diagnostic `3/4` scores are not current candidate scores.

Fresh dated source/status searches on 2026-09-19 recovered the original arXiv/PTRF paper, the University of Washington publication page and Burdzy's current open-problem page, but no accessible later primary source explicitly resolving exact Problem 7.2. This is bounded negative evidence only; I do not infer worldwide openness merely from a failed search.

## 2. Continuity from the latest retained result

The newest previous R15 report is

`runs/R15/20260919_2211Z_successor_screen_f0111_fullsupport_dimension_barrier_g92z.md`

at commit `902ab5acdb53add1d89d1862607fb52da135ee8c`.

Its strongest retained local result concerns the `k=2` hazard

`F(t)=sum_i t_i - log S(t)`,  `S(t)=sum_i exp(t_i)-(n-1)`.

Let a nonnegative-coefficient quadratic global majorant `P` be exact at an interior point `q`, put `G=P-F`, and write

`H=D^2G(q) >= 0`.

If `h` is a Hessian-null direction, `Hh=0`, then straight-line local minimality forces cubic nullity. A curved path `q+eps h+eps^2 v` gives the projective fourth-order necessary condition

`D_h^4 G(q) >= 3 b^T H^+ b`,                    (2.1)

where the cubic covector is

`b_i = D^3G(q)[e_i,h,h]`

and `H^+` is the Moore--Penrose inverse. For this hazard, derivatives of order at least three are derivatives of `log S`.

For a two-level mixed direction

`h=m(1+delta) 1_J - m(1-delta) 1_K`,  `0<=delta<1`,

with the previously derived cubic-null scalar `z`, define

`K2=((delta+z)(1-z^2))/(delta+3z)`,
`t_J=(1-z)^2-K2`,
`t_K=(1+z)^2-K2`,

and

`R=-2(delta+z)(1-z^2)(delta^2 z+3 delta z^2+delta+3z^3)/(delta+3z)^2`.

Then

`D_h^4 log S(q)=m^4 R`,
`b_i=m^2 r_i t_J` on `J`,
`b_i=m^2 r_i t_K` on `K`,
`H_ii=r_i(1-r_i)`,

where `r_i=exp(q_i)/S(q)`.

The previous report used only block test vectors in (2.1), obtaining full-support dimension barriers `n>=30` on `z>1` and `n>=50` on `z<-1`. This run asks for the **sharpest possible consequence of (2.1) using only the fixed diagonal of H and the null relation Hh=0**.

## 3. Moves #1, #18, #27 — change category, translate to polygons, characterize every admissible H

The route was written before validation in

`artifacts/R15/f0111_projective_polygon_h93p_idea.md`

at commit `e3968ca0ecea13a6987e8f412265a17b408441ce`.

The change of category is from unknown Hessian matrices to Gram vectors. The key point is that the projective pseudoinverse inequality is exactly a rank-one PSD downdate condition.

### Theorem R15-PG — exact Gram-polygon criterion

Let `d=(d_i)` with `d_i>=0`, let `h,b in R^n`, and let `C>0`, with `h.b=0`. Define

`e_i = d_i - b_i^2/C`,
`ell_i = |h_i| sqrt(e_i)`.

The following are equivalent.

**(A)** There exists a symmetric matrix `H>=0` such that

- `diag(H)=d`,
- `Hh=0`,
- `b in ran(H)`, and
- `b^T H^+ b <= C`.

**(B)**

- `e_i>=0` for every `i`, and
- the lengths `ell_i` can close to a Euclidean polygon, equivalently

`2 max_i ell_i <= sum_i ell_i`.                  (3.1)

Coordinates with `h_i=0` simply contribute zero polygon length; they may still have nonzero `e_i`.

#### Proof: (A) implies (B)

For a PSD matrix `H` and `b in ran(H)`, the generalized rank-one Schur-complement identity says

`H - b b^T/C >= 0  <=>  b^T H^+ b <= C`.          (3.2)

Indeed write `b=H^(1/2)u` with the minimum-norm `u`; then `||u||^2=b^T H^+b` and

`H-bb^T/C = H^(1/2)(I-u u^T/C)H^(1/2)`.

Set

`K=H-bb^T/C`.

By (3.2), `K>=0`; its diagonal is exactly `e_i`. Since `Hh=0` and `h.b=0`, also `Kh=0`.

Choose Gram vectors `u_i` with `K_ij=<u_i,u_j>`. Then `||u_i||=sqrt(e_i)`, and

`0 = h^T K h = ||sum_i h_i u_i||^2`,

so

`sum_i h_i u_i=0`.

Thus the vectors `v_i=h_i u_i` have lengths `ell_i` and sum to zero. Any closed vector polygon satisfies the polygon inequality (3.1). Also `e_i>=0` because they are diagonal entries of a PSD matrix.

#### Proof: (B) implies (A)

The elementary polygon criterion says that nonnegative lengths `ell_i` admit vectors `v_i` in the plane with `||v_i||=ell_i` and `sum_i v_i=0` iff (3.1) holds.

For `h_i!=0`, put `u_i=v_i/h_i`; then `||u_i||=sqrt(e_i)`. For a coordinate with `h_i=0`, choose any vector of length `sqrt(e_i)` in extra orthogonal dimensions. Let `K` be the Gram matrix of the `u_i`. Then

`K>=0`, `diag(K)=e`, and `Kh=0`.

Now define

`H=K+b b^T/C`.

Then `H>=0`, `diag(H)=d`, and `Hh=0` because `h.b=0`. If `x in ker(H)`, positivity of the two summands implies simultaneously `Kx=0` and `b.x=0`; therefore `b` is orthogonal to `ker(H)` and hence belongs to `ran(H)`. Finally

`H-bb^T/C=K>=0`,

so (3.2) gives `b^T H^+b<=C`. This proves (A).

QED.

### Interpretation

This theorem is exact, not merely a new bound: it completely characterizes the local subsystem consisting of

- PSD contact Hessian,
- its prescribed diagonal,
- the specified null direction,
- and the projective fourth-order pseudoinverse budget.

Anything not ruled out by this polygon criterion requires additional information such as coefficient nonnegativity, exact value/gradient contact, or the global all-ray majorant cone. Conversely, no stronger obstruction can be extracted from **only** these four local ingredients.

The rank-one Schur complement and the polygon closure criterion are classical linear algebra/geometry. I make no novelty claim for those mechanisms. The F0111 specialization/application below has not been matched to prior literature in this bounded search; novelty is **UNVERIFIED**.

## 4. Exact specialization to the F0111 two-level null curve

At an isolated Hessian-null candidate the preceding work has strict `R>0`. In (2.1) take

`C = (1/3) D_h^4G(q) = m^4 R/3`.

Cubic nullity gives `h.b=D_h^3G(q)=0`, so Theorem R15-PG applies.

Define

`A_J = 1 + 3 t_J^2/R`,
`A_K = 1 + 3 t_K^2/R`.

Then the residual diagonal from Theorem R15-PG is exactly

`e_i = r_i(1-A_J r_i)` for `i in J`,
`e_i = r_i(1-A_K r_i)` for `i in K`.              (4.1)

Therefore the entire local PSD/null/projective subsystem is feasible **if and only if**

`r_i <= 1/A_J` on `J`,  `r_i <= 1/A_K` on `K`,    (4.2)

and

`2 max { (1+delta)sqrt(r_i(1-A_J r_i)) : i in J ;
         (1-delta)sqrt(r_i(1-A_K r_i)) : i in K }
 <=
 sum_{i in J}(1+delta)sqrt(r_i(1-A_J r_i))
 +sum_{i in K}(1-delta)sqrt(r_i(1-A_K r_i))`.       (4.3)

The common factor `m` cancels.

Condition (4.2) recovers the previous coordinate caps and hence the aggregate block-size inequalities

`|J| >= A_J x`, `|K| >= A_K y`,

where `x=sum_{i in J}r_i`, `y=sum_{i in K}r_i`. Equation (4.3) is the genuinely new non-aggregated constraint.

## 5. A strict new support-size consequence when one sign block is a singleton

Suppose `K` consists of one coordinate, so its mass is exactly `r_K=y`. Put `M=|J|`. The polygon condition forces the singleton `K` length to be no larger than the total `J` length:

`(1-delta)sqrt(y(1-A_K y))
 <= (1+delta) sum_{i in J} sqrt(r_i(1-A_J r_i))`.     (5.1)

By Cauchy and `sum_J r_i=x`,

`(sum_J sqrt(r_i(1-A_J r_i)))^2
 <= M sum_J r_i(1-A_J r_i)
 = Mx - M A_J sum_J r_i^2
 <= Mx - A_J x^2`.                                   (5.2)

Combining (5.1)--(5.2) yields the new necessary bound

`boxed:
M >= A_J x
   + ((1-delta)/(1+delta))^2 * y(1-A_K y)/x.`        (5.3)

The symmetric statement, when `J` is a singleton, is

`boxed:
|K| >= A_K y
      + ((1+delta)/(1-delta))^2 * x(1-A_J x)/y.`     (5.4)

These strictly refine the old mass/cap count whenever the singleton has positive residual polygon length.

### Exact rational middle-branch point

Take

`delta=1/2`, `z=-3/5`.

This lies on the positive-constant middle branch. Exact simplification gives

`k=256/325`,
`x=1/325`, `y=68/325`,
`K2=16/325`,
`t_J=816/325`, `t_K=36/325`,
`R=1936/105625 > 0`,
`A_J=124969/121`, `A_K=364/121`.

The old coordinate-cap counts alone give

`A_J x = 9613/3025`,
`A_K y = 1904/3025 < 1`.

Thus with a singleton `K`, the old local test only forces the integer bound

`M>=4`.

The polygon correction (5.3) is exactly

`A_J x + (1/9) y(1-A_K y)/x = 269/45`,

so

`boxed: M>=6.`

Hence every local two-level candidate at this exact scalar point with active block sizes `(M,|K|)=(4,1)` or `(5,1)` is ruled out by the projective Gram-polygon condition even though it passes the preceding coordinate-cap count. This is a strict mathematical strengthening, not a renamed version of the earlier block bound.

The finite rational specialization was checked with exact `Fraction` arithmetic in

`artifacts/R15/f0111_projective_polygon_checker_h93p.py`

and the archived execution

`artifacts/R15/f0111_projective_polygon_checker_h93p.out`

ends

`OLD_COORDINATE_CAP_ALLOWS_M_GE_4_WHEN_N_EQ_1`
`PROJECTIVE_POLYGON_FORCES_M_GE_6_WHEN_N_EQ_1`
`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent audit.

## 6. What this does and does not solve

This run does **not** solve Talagrand Problem 10.9, and it does not justify admission/ownership of F0111. It completes one local linear-algebra layer of the retained `k=2` first-bifurcation program.

What is now exact:

- once `q,h` and the cubic/quartic data are fixed, there is no remaining mystery about whether some PSD matrix with the correct diagonal/null direction can satisfy the projective fourth-order inequality: the answer is exactly the polygon test (4.2)--(4.3);
- the earlier block-size inequalities are only projections of that exact polygon criterion;
- singleton active blocks acquire the stronger support constraints (5.3)--(5.4).

What remains genuinely outside this completed layer:

1. coefficient nonnegativity, i.e. the off-diagonal constraints tying `H_ij` to the quadratic coefficients;
2. exact value and gradient contact at `q`;
3. global majorization on the positive orthant / the exact all-ray cone;
4. non-two-level mixed-sign null directions;
5. the distinct second-contact bifurcation mechanism;
6. passage from the specialized `k=2` hazard to the full source Problem 10.9.

The most useful next attack is therefore **not another generic PSD estimate**. The theorem proves that this local PSD/projective subsystem is finished. The next route should intersect the polygon-feasible Gram data with coefficient nonnegativity and the exact all-ray cone, or prove a compression theorem reducing arbitrary mixed-sign null directions to two levels.

## 7. Current primary literature check for the retained screen

I rechecked Talagrand's primary STOC paper this run. Problem 10.9 asks whether there is a universal `gamma>0` such that every cardinality up-class `{X subset S: card X >= k}` belongs to `C_gamma`.

Current 2026 primary literature found in the dated search:

- Ruben Ascoli, Xiaoyu He, Jinyoung Park and Michel Talagrand, arXiv:2608.11183 (2026-08-11), reformulate the discrete Convexity Conjecture via `k`-thresholds and prove substantial graph-property classes;
- Chen Li, arXiv:2609.08967 (2026-09-08), proves the fractional version in the `p`-spread formulation;
- Jinyoung Park, arXiv:2609.14681 (2026-09-13), proves a dimension-free comparison between expectation and fractional expectation thresholds and explicitly derives a dimension-independent bound **toward** the conjecture.

These sources do not state a full resolution of Talagrand Problem 10.9. Failure to find a later full resolution is bounded negative evidence only. The Gram-polygon application here has not undergone a publication-priority search deep enough to support a novelty claim.

## 8. Structured ledger delta

```yaml
ledger_delta:
  worker: R15
  native_source: "Burdzy--Scheutzow, Forward Brownian Motion, Problem 7.2 / I0076"
  native_metric_before: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_metric_after: "NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "retired after six-run handoff; do not increment"
  retained_screen: "Talagrand Problem 10.9 / F0111, k=2; SELF_CHECK_ONLY / NOT CLAIMED / PENDING"
  retained_movement: "exact Gram-polygon characterization of the PSD/null/projective subsystem; singleton-block support inequality; exact point delta=1/2,z=-3/5 improves M>=4 to M>=6 when |K|=1"
  tried_moves: [1, 18, 27]
  remaining_obligation: "native I0076 still has no surviving frozen candidate; retained F0111 still needs coefficient/global constraints, arbitrary mixed-sign compression and second-contact elimination"
  evidence:
    idea_commit: "e3968ca0ecea13a6987e8f412265a17b408441ce"
    checker_commit: "1a5cfae17c4d3e9de372152ce4ac17635adc9f5f"
    checker_output_commit: "ca2624bd520db4996b869ecf6f8a6a28d83712d6"
  audit_ids: []
  audit_status: "SELF_CHECK_ONLY; no independent audit requested or counted"
```

## 9. Model / scheduler boundary

The currently exposed scheduler/task surface still has no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt and no guaranteed full-hour execution field. `GPT-6 / maximum` therefore remains prompt-only here; I do not report it as the model actually run.

The historical P26 `You cannot modify this task` response was authorization-context-specific. Repository implementation records show a later successful P26 update from an authorized P/C context. The compliant workaround for an edit-denied task is the owning/authorized workspace/account/API/admin context or platform support, not a permission bypass or duplicate task. No scheduler or permission change was attempted in this run.
