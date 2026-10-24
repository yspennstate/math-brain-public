Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1289727882057511/11918000000000000 = 0.10821680500566462... -> same`; supported G0013 unchanged count `3 -> 4`; this is `STUCK1`, the required Section-I thinking-only run. Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Methods used: B22 READ THE FAILURES, B26 HUNT THE SPORADIC CASE, B29 ADD THE POINTS AT INFINITY.** GPT-6 / maximum was requested in prompt text, but this runtime identifies as GPT-5.6 Sol and exposes no authenticated reasoning-effort telemetry, so I do not claim GPT-6 or maximum reasoning.

# R09 CLOSABLE OUTSIDE — G0013 STUCK1: exact obstruction ledger and one-interface graph-copula recovery choice

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only.

This is deliberately a **thinking-only stuck report**. It introduces no new theorem claim, no new numerical source bound, and no checker-only artifact.

## 1. Continuity, ownership, and run-start state

I did **not** reopen Pengfei Tang, Question 4.11. The periodic-tree clause is already source-level REFUTED in the later R09 record, with exact verification, two distinct outside audits, a paper package, and the owner's six-unchanged retirement threshold reached. The transitive-graph clause remains open, but Tang is frozen for this R09 slot at `UNBOUNDED_ABOVE`. G0002 / Cerf 53.1 remains handed off at `Delta_8=UNMEASURED`.

The controlling exclusive claim remains `operations/claims/G0013.md`: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, Remark 3. With `lambda=Unif[0,1]`, `nu=lambda tensor lambda`,
\[
M=\sup_{\pi\in\Pi(\lambda,\lambda)}W_2^2(\pi,\nu),
\]
and the source conjecture is
\[
M=\frac1{10},
\]
with the diagonal and antidiagonal as maximizers. R09's frozen metric is

`U_* = smallest rigorous source-valid global upper bound on M established by R09`.

The newest complete own report recovered before this run is

`runs/R09/20260918T0230Z_g0013_adapted_xi_pressure_7d3a9c.md`,

which left
\[
\boxed{U_*=\frac{1289727882057511}{11918000000000000}=0.10821680500566462\ldots}
\]
and advanced the supported unchanged count to `3`, thereby mandating this Section-I run.

Before diagnosis I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the G0013 claim, the newest complete R09 report, the newest searchable R08 and R10 states, and exact G0013/intake/attempt records. Root `RESULTS.md` still contains a stale historical R09 row relative to the later exclusive G0013 claim and immutable R09 reports; this attacking worker does not edit shared roots. The intake corpus is connector-large, so exact target/source/ownership queries were used rather than pretending that every JSONL row was visibly rendered.

## 2. Current-literature / historical-ownership check

The source status is unchanged in the bounded 18 September 2026 check. Catalano--Lavenant's arXiv:2510.06034 poses the uniform Euclidean quadratic-Wasserstein problem. Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1, submitted 9 September 2026, still states the uniform Catalano--Lavenant assertion as a conjecture and proves the Gaussian analogue rather than the uniform theorem. Searches by exact title, author names, `uniform copula`, `farthest from independence`, `quadratic Wasserstein`, `1/10`, and recent citing/follow-up terms found no later source-level resolution. This is bounded dated evidence, not a novelty certificate.

For the closest methodological comparison I reread Jonathan Ansari and Marcus Rockel, *The exact region and an inequality between Chatterjee's and Spearman's rank correlations*, arXiv:2506.15897v3 / J. Multivar. Anal. 214 (2026), 105630. Their Theorem 1 solves the exact `xi-rho` region by maximizing Spearman rho at fixed Chatterjee xi through one convex family of conditional CDFs; their optimization has box, nesting, mass and quadratic constraints, and its unique optimizer is clamped linear. This matters because R09's scalar box-projection route is of exactly that one-family shape. G0013 becomes harder only when the two directional families must be realized simultaneously by one Brenier / saddle potential.

No conflicting current owner for G0013 surfaced. The claim remains R09-exclusive.

## 3. Section-I(a): the exact statement that blocks

The sharp technical obstruction is now clean. In the smooth positive-density approximation class, write the Brenier map `T=grad phi=(u,v)`, let
\[
D^2\phi=\begin{pmatrix}a&b\\b&c\end{pmatrix}\succeq0,
\]
and use the conditional-CDF / partial-Legendre coordinates from the preceding reports. With
\[
S=W_2^2(\pi,\lambda^{\otimes2}),
\]
R09 has exact nonnegative spectral and determinant deficits `P_1,P_2,D_1,D_2` satisfying
\[
\boxed{
P_1+P_2+D_1+D_2=\frac13-3S.
}
\]
Consequently the value part of the Catalano--Lavenant conjecture is equivalent to proving
\[
\boxed{
P_1+P_2+D_1+D_2\ge\frac1{30}.
}
\tag{BLOCK}
\]
The scalar conditional-CDF machinery controls the `P_i`; the partial-Legendre formulation identifies the `D_i` as weighted determinant / saddle-overlap costs. What is missing is a **joint inequality** saying that the same map cannot make both types of deficit simultaneously too small.

This is the blocker. A new scalar CDF inequality, a new finite permutation search, or another integrated correlation budget does not by itself address `(BLOCK)`.

## 4. Section-I(b): every route tried, and the precise reason it stopped

The following table consolidates the actual G0013 history rather than restarting from the newest notation.

| Route | What it established | Why it did not close the source |
|---|---|---|
| Historical extreme-copula / finite permutation route (`G0013-A001/A002`, September 12 scripts) | Convexity reduction; exact finite permutation checks through `n<=7`; identity/reversal extremal in those finite models; exchange and block-reversal experiments | Nonatomic extreme copulas are not all deterministic maps, so finite permutation extremality does not imply the continuous theorem. |
| First Brenier / weighted-Hessian reduction | Source-valid `U_*: UNMEASURED -> 1/6`; exact weighted Hessian formulation; outer Kantorovich dual | The square integration-by-parts weight `x(1-x)` vanishes at the boundary, so Schrott's Gaussian unweighted-isoperimetric step does not transplant sharply. |
| Jacobi / conditional-CDF route | `U_*: 1/6 -> 1/9`; exact identity `S=I_1+I_2`; higher Jacobi modes expose spectral deficit | The first spectral gap discards box geometry and joint Hessian compatibility; equality pressure alone leaves too much room. |
| Restricted shuffle calculations | Exact half-rotation value `1/20`; all two-piece positive-orientation circular shifts certified strictly below `1/10` | These are genuine subclasses only. They do not cover mixed-orientation shuffles or arbitrary copulas. |
| Higher-mode and scalar obstacle optimization | Successive full-class bounds `1/9 -> 2221/20000 -> 0.110788... -> 0.108711...`; exact two-sided box projection solved | Even the **exact** one-level box obstacle is only a one-coordinate relaxation. Pointwise optimal CDF profiles need not arise from the same two-dimensional Brenier map. |
| Optimized scalar penalty + CDF nesting | Current source-valid `U_*=0.10821680500566462...`; nesting constraints made explicit | Nesting alone can be satisfied by the pointwise clipped-affine families. It is not the missing coupling constraint. |
| Square-symmetry / rank-correlation budget | `rho_direct` dominates both signed cross correlations; sharp nesting modulus; exact relaxation witness `S_relax=667/6480>1/10` | The witness satisfies all scalar, Jacobi, nesting and integrated D4 budgets while still exceeding `1/10`. Therefore those integrated constraints are provably insufficient. |
| Partial-Legendre saddle reformulation | One convex-concave generating potential `Psi`; exact conservation laws; determinant slack becomes `Q_t V_y`; rank-one pressure `S>1/10 => K>6/7` | This identifies the geometry but does not quantify the cost of **gluing** differently oriented near-rank-one regions under both marginal constraints. |
| Adapted/conditional Wasserstein / Chatterjee pressure | `S <= min{xi(U,V),xi(V,U)}/6`; every counterexample must have both directed `xi>3/5` and be near functional in both directions | Bidirectional near-functionality is not enough: graph copulas can have maximal directed functional dependence while still being nonmonotone. The missing issue remains orientation / cyclic-monotonicity compatibility. |
| Random near-rank-one sign cells | Tested the natural negation mechanism suggested by the rank-one pressure theorem | Law-level random mixtures cannot beat `1/10` by convexity; arbitrary local sign patches violate the Hessian integrability/Codazzi identities before the marginal constraints are even imposed. |

The recurring failure is now unambiguous: every successful route that treats one coordinate, one level, or one integrated statistic at a time loses the **source-point matching** between the two directions.

## 5. Section-I(c): what a proof must contain that no route so far contains

A proof must contain a quantitative **orientation-gluing / singular-stability theorem** for a single convex potential.

The previous two runs force any hypothetical counterexample into two simultaneous rigidity regimes: its target copula is highly functional in both directions, and its source-to-target Brenier Hessian is nearly rank one on a large weighted set. Neither condition alone is contradictory. The missing statement must say that, under uniform marginals and cyclic monotonicity, a nearly rank-one Hessian cannot change orientation often enough to encode a genuinely nonmonotone near-bijection without paying at least the missing determinant-plus-spectral amount in `(BLOCK)`.

Equivalently, one needs a theorem that promotes **local rank-one structure plus boundary/marginal data to global orientation**, up to a quantitatively controlled gluing set. None of the routes above contains such a topological/variational control of the sign geometry of `b=phi_xy`. The boundary regression identities, common `W_1` path length, CDF nesting, and rank-correlation budgets constrain this geometry but do not yet make orientation changes expensive enough.

## 6. Section-I(d): simplest special case still unproved

The smallest concrete sign-gluing family for which I found no completed R09 proof is the **one-interface mixed-orientation block reflection**
\[
g_c(s)=
\begin{cases}
s,&0\le s\le c,\\
1+c-s,&c<s\le1,
\end{cases}
\qquad 0<c<1,
\]
with target copula
\[
\pi_c=\operatorname{Law}(S,g_c(S)),\qquad S\sim\operatorname{Unif}[0,1].
\]
It is a measure-preserving involution with exactly one orientation change. The endpoints `c=1` and `c=0` are the diagonal and antidiagonal; the existing circular-shift theorem handles a different two-piece **positive-orientation** family. Repository searches recover historical `block-reversal` experimentation but no source-valid closed formula or proof for this one-interface mixed-sign family.

This family is the minimal laboratory for the obstruction in Section 5: it has one gluing interface, no diffuse copula complication, and already forces a change of orientation. A proof that
\[
W_2^2(\pi_c,\lambda^{\otimes2})\le\frac1{10}
\]
for every `c`, with strict inequality away from `c=0,1`, would be PARTIAL rather than source closure, but it would isolate the quantitative cost of one sign change in the cleanest possible setting.

## 7. Section-I(e): nearest solved literature analogue and what it has that G0013 lacks

The nearest exact analogue is Schrott's 2026 Gaussian theorem. In the Gaussian problem the quadratic cost is converted through a Brenier potential to an **unweighted** Gaussian second-derivative/Laplacian functional. Coarea and sharp Gaussian isoperimetry then supply the scalar geometric lower bound, and a positive-semidefinite matrix inequality combines coordinates. That proof has a global isoperimetric mechanism whose equality structure forces one-dimensional extremizers.

The uniform-square problem lacks precisely that mechanism in its current form. Integration by parts produces the degenerating Wright--Fisher weight `x(1-x)`, so variation can migrate toward low-weight faces, and the scalar isoperimetric step does not see the orientation-gluing constraint between the two coordinates.

The nearest methodological analogue is Ansari--Rockel's exact `xi-rho` region. Their proof succeeds because the admissible object is one nested conditional-CDF family and the optimization remains convex; a clamped-linear KKT solution can be certified globally. R09 has essentially exhausted that one-family technology: the exact scalar box obstacle is solved. G0013 lacks the decoupling that makes their problem convex at the relevant level, because the two conditional families must be projections of one cyclically monotone Brenier / saddle map.

## 8. B22 / B26 / B29 accounting

**B22 READ THE FAILURES.** This was the main work of the run. The failed routes were reduced to a single repeated loss: they discard the same-source-point matching of the two directional conditional families. The exact relaxation witness above `1/10` confirms that this is not merely a stylistic diagnosis.

**B26 HUNT THE SPORADIC CASE.** The one-interface block reflection `g_c` is the smallest unresolved mixed-orientation graph family visible in the current R09 record. It directly tests whether a single sign change has a quantitative transport penalty.

**B29 ADD THE POINTS AT INFINITY.** The conjectured extremizers are singular graph copulas, whereas the smooth Brenier machinery approaches them only through degenerating Hessians with `kappa -> 1`. Treating graph copulas as the boundary of the smooth saddle class clarifies why a stability theorem at the singular boundary, rather than another interior scalar estimate, is the natural missing ingredient. This is a research-direction diagnosis, not a new theorem claim.

## 9. Exactly one recovery choice

I choose exactly one of the owner's allowed recovery actions:

**PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM SECTION 6.**

The next research run should attack the one-interface block-reflection family `pi_c` above. It should not tune the global scalar penalty again and should not run another broad finite-permutation enumeration. If the family can be solved exactly, the result will be recorded honestly as PARTIAL and used only to extract a quantitative orientation-change mechanism for the full problem.

The next three Section-B moves for that recovery are **B1 CHANGE THE CATEGORY**, **B6 DEFORM TO A POINT YOU CAN SOLVE**, and **B11 DUALIZE**: rewrite the graph-target problem as a one-dimensional assignment / two-coordinate transport problem; deform in the interface parameter `c` from the diagonal or antidiagonal endpoint; and seek an exact Kantorovich dual certificate for the resulting one-interface family.

## 10. Metric / retirement state

There is no global metric movement in this stuck run:
\[
\boxed{
U_*^{\rm before}=U_*^{\rm after}
=\frac{1289727882057511}{11918000000000000}
=0.10821680500566462\ldots .
}
\]
The supported G0013 unchanged count is therefore `4`. This is the first formal stuck-recovery episode on G0013. R09 does **not** rotate yet: the owner gives a CLOSABLE target six unchanged runs before retirement. If the global metric reaches six unchanged runs without a source-valid improvement, R09 must leave an immutable handoff and rotate to an eligible, fully admitted outside target rather than extending this line indefinitely.

Status remains **PARTIAL / OPEN_CURRENT**.

## 11. Model / scheduler control and permissions

The exposed scheduler action schema still has title, prompt, schedule / relative start, timing mode and enabled state, but no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. GPT-6 / maximum therefore remains prompt-only here. Changing that requires a product/API or authorized owning scheduler surface that exposes model and reasoning fields together with runtime telemetry.

The root ledger records that the historical P26 `You cannot modify this task` response was authorization-context dependent: the full P26 prompt update later succeeded from another authorized context. The legitimate remedy for any denied task is the owning authorized context, ownership/admin transfer, or platform support—not cloning, bypassing permissions, or treating a repository edit as a scheduler repair. No scheduler or permission modification was attempted in this run.

## 12. Artifact decision and structured `ledger_delta`

No exact-arithmetic artifact was created because this is the mandated thinking-only stuck run and contains no new finite theorem claim. That is intentional under the 90/10 rule.

```yaml
ledger_delta:
  track: R09
  lane: CLOSABLE_OUTSIDE
  active_claim: G0013
  source: "Catalano--Lavenant, Measures of Dependence based on Wasserstein distances, arXiv:2510.06034, Remark 3"
  source_status_before: "PARTIAL / OPEN_CURRENT"
  source_status_after: "PARTIAL / OPEN_CURRENT"
  metric_name: "U_* = smallest rigorous source-valid global upper bound on M"
  metric_before: "1289727882057511/11918000000000000"
  metric_after: "1289727882057511/11918000000000000"
  movement: "NO_MOVEMENT"
  supported_unchanged_count_before: 3
  supported_unchanged_count_after: 4
  stuck_episode: 1
  stuck_mode: "Section-I thinking-only"
  methods_used:
    - "B22 READ THE FAILURES"
    - "B26 HUNT THE SPORADIC CASE"
    - "B29 ADD THE POINTS AT INFINITY"
  exact_blocker: "P1+P2+D1+D2 >= 1/30"
  simplest_unproved_special_case: "one-interface mixed-orientation block reflection pi_c=Law(S,g_c(S))"
  recovery_choice: "PROVE_SIMPLEST_UNPROVED_SPECIAL_CASE"
  next_methods:
    - "B1 CHANGE THE CATEGORY"
    - "B6 DEFORM TO A POINT YOU CAN SOLVE"
    - "B11 DUALIZE"
  nearest_exact_analogue: "Schrott 2026 Gaussian farthest-coupling theorem"
  nearest_methodological_analogue: "Ansari--Rockel 2026 exact xi-rho region via one-family convex conditional-CDF optimization"
  tang_state: "RETIRED/FROZEN; periodic-tree clause refuted; transitive clause open; metric UNBOUNDED_ABOVE; retirement count 6"
  g0002_state: "HANDED_OFF; Delta_8=UNMEASURED"
  checker_created: false
  scheduler_modified: false
  shared_roots_modified: false
  peer_files_modified: false
```
