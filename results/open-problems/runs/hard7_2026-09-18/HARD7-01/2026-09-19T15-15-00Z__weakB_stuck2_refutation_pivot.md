Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. This is the required second Section-I thinking-only recovery run; no new theorem claim is promoted. Methods tried: B8 / B23 / B26.**

# HARD7-01 run 19 — STUCK2: finite max-of-quadratics refutation pivot for weak `(B)`

Status: **PARTIAL / source OPEN / STUCK2 recovery chosen**.

## 1. Continuity, ownership, and required repository reads

This invocation resumes the exact admitted target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T14-02-00Z__mixed_lq_lr_deformation.md`

at report commit `182876c9de825b70c576f7e385dace21f0f8c125`. That report explicitly recorded a second unchanged-metric lifecycle trigger, so this invocation is a Section-I **thinking-only STUCK2 report**, not another lemma-producing run.

The create-only canonical claim remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owner **HARD7-01**, status `CLAIMED / source OPEN / research PARTIAL only`. No claim file is modified in this run.

At run start I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the active weak-`(B)` claim;
- the newest own checkpoint above and the current run-14--18 recovery chain;
- the newest visible neighboring R02 state, including its 2026-09-19 successor-gate report;
- repository-wide indexed aliases for `(B)-conjecture`, `B-conjecture`, logarithmic concavity of dilates, Cordero--Erausquin/Rotem, and the canonical claim ID. The indexed search covers relevant intake aliases. The connector does not expose a credible one-shot byte-for-byte rendering of every large append-only `probability_1000_intake_*/problems.jsonl`, so I do not falsely claim such a rendering.

No competing current owner or posted/settled equivalent was recovered. The source target therefore remains the same.

## 2. Exact source target and frozen metric

For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that

\[
t\longmapsto \mu(e^tK)
\]

is log-concave on `R`.

The frozen source metric is

`D_B = largest integer d such that the exact statement is proved for every admissible (mu,K) in every dimension n<=d`.

Saroglou's planar theorem remains the verified baseline, so

\[
\boxed{D_B:2\longrightarrow2.}
\]

This is **no movement**. None of the structured homogeneous results in runs 14--18 is relabeled as the unrestricted dimension-three theorem.

## 3. Fresh current-literature sentinel — 2026-09-19

I reran a bounded current search rather than relying on the admission search.

- Saroglou, *More on logarithmic sums of convex bodies*, Mathematika 62 (2016), DOI `10.1112/S0025579316000061`, proves that log-Brunn--Minkowski in dimension `n` implies `(B)` there and establishes the full even-log-concave `(B)` conjecture in the plane.
- Cordero-Erausquin--Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), DOI `10.1214/22-AOP1604`, proves `(B)` for rotationally invariant log-concave measures using sharp weighted Poincare inequalities, not for arbitrary even log-concave measures.
- Armeniakos--Ulivelli, arXiv:`2602.23350`, v2 dated 2026-03-12, proves that a strengthened dimensional Brunn--Minkowski hypothesis implies `(B)` and recovers hereditarily convex measures; it does not state the unrestricted theorem.
- Yang, arXiv:`2607.10104`, submitted 2026-07-11, proves a positive dimensional Brunn--Minkowski exponent `p_n >= c/(n^2 log n)` for all even log-concave measures. This is a substantial general inequality but is not the exact logarithmic dilation-concavity source statement.
- Putterman, arXiv:`2608.08472`, submitted 2026-08-09, concerns sharp stability for the Gaussian `(B)` theorem and Gaussian strong/functional variants rather than unrestricted weak `(B)`.

A bounded search for a 2026 unrestricted weak-`(B)` proof or counterexample returned no such resolution. This is bounded negative evidence, not a worldwide openness or novelty certificate.

## 4. Required Section-I STUCK2 obstruction map

### (a) Exact statement that blocks

The source-sized obstacle is still dimension three. The cleanest source-relevant test isolated by the homogeneous correlation formulation is the following `p=2` common-degree problem.

Let `phi,psi` be smooth even convex positively two-homogeneous functions on `R^3\{0}`, put

\[
H=\phi+\psi,\qquad S_H=\{H=1\},
\]

let `nu_H` be cone probability on `S_H`, and set

\[
U=\phi|_{S_H},\qquad m=\mathbb E_{\nu_H}U.
\]

The exact angular inequality required by the common-degree covariance criterion is

\[
\boxed{
\operatorname{Var}_{\nu_H}(U)
\le \frac25\,m(1-m).
}
\tag{4.1}
\]

The full source is stronger than this special case. Proving (4.1) would therefore remain `PARTIAL`, not `D_B=3`. Conversely, a source-valid violation of the corresponding homogeneous covariance formulation would be a genuine route toward refuting the source, so this is a useful counterexample laboratory.

A second way to see what a counterexample must accomplish is to work at a smooth point. Write

\[
A=\nabla^2H,\qquad B=\nabla^2\phi,
\qquad C=A^{-1/2}BA^{-1/2}.
\]

Convex complementarity gives `0 <= C <= I`. On `S_H`, define

\[
e=\frac{A^{1/2}x}{\sqrt2},
\]

so `||e||=1` by two-homogeneity. Then the basic pointwise quantities take the scratch form

\[
U=e^TCe,
\]

and for the inverse-Hessian angular energy of the degree-zero extension `phi/H`,

\[
\Gamma_H(U)=2\big(e^TC^2e-U^2\big).
\tag{4.2}
\]

Thus the generic bounded-variable energy estimate has the exact defect decomposition

\[
\boxed{
\Gamma_H(U)=2U(1-U)-2\Delta,
\qquad
\Delta:=e^TC(I-C)e\ge0.
}
\tag{4.3}
\]

This is recorded only as a route calculation, not promoted as a new theorem. It makes the obstruction sharper: a bad split must arrange both substantial angular variation of `U` and a Hessian contraction `C` that is nearly projection-valued in the radial direction on the same high-mass regions. Merely making the body anisotropic is not enough.

If an angular Poincare estimate with gap `lambda` is available for the same inverse-Hessian form, then writing

\[
V=\operatorname{Var}(U),\quad M=m(1-m),\quad D=\mathbb E\Delta
\]

formally gives

\[
(\lambda+2)V\le 2(M-D).
\tag{4.4}
\]

For the dimension-three target `V<=2M/5`, a gap near `lambda=2` would need roughly the compensating condition `D/M>=1/5`. The previous `l_q^2` work obtained the needed compensation by special coordinate-face structure; no analogue is known for general `H`.

### (b) Routes tried on this target and why each stopped

The current weak-`(B)` target has now gone through the following genuinely different routes.

1. **B2/B5/B24:** negate the homogeneous curvature inequality, differentiate in scale, and isolate extremal scales. This produced an exact boundary-flux/counterexample criterion and compactified where failure could occur, but gave no control of the angular law.
2. **B1/B3/B6:** reverse-hazard reformulation, a stronger sufficient radial-score theorem, and deformation from solvable cases. These proved restricted classes but inserted hypotheses absent from the source.
3. **B11/B20/B30:** cone/ray dualization and one-scale scalarization. An explicit two-atom *relaxation* showed arbitrary mixtures of individually safe rays need not be safe; the unresolved word became geometric **realizability** by a convex split.
4. **B18/B22/B29 (STUCK1):** rewrite as a cone-measure variance/Poincare problem, read the failed routes in the literature, and include the missing angular boundary. This identified (4.1) as the simplest common-degree test and selected the weighted-Poincare port.
5. **B4/B15/B27:** prove a complete structured theorem first, break symmetry, and swap the order of optimization. For the quartic cone, the naive spectral gap alone was too weak; the obstruction moved into how convex splits can occupy the first angular eigenspace.
6. **B7/B14/B17:** pass to the simplex/Dirichlet scaling limit, quotient by the sign group, and recognize the Wright--Fisher spectrum. This produced an exact spectral margin on the `l_4^2` cone, but only for that special cone geometry.
7. **B12/B16/B25:** exploit conserved Euler structure, compute the first eigenspace exactly, and double-count the split. Convex complementarity made the deficient first eigenspace safe, but did not control arbitrary nonlinear higher-mode mixtures.
8. **B13/B9/B10:** find the monotone coordinate derivative shares, randomize them, then derandomize through bounded conditional variance. This closed the whole smooth `l_q^2` cone for arbitrary globally-even convex complementary splits, but the key coordinate-face Hessian degeneracy is absent for a generic two-homogeneous `H`.
9. **B5/B6/B30:** deform the *total* potential to `H_q+eps H_r`. The mechanism survives on a nonzero mixed family, proving it is not an isolated algebraic coincidence, but the result is still a neighborhood of an axis-separable cone rather than an arbitrary three-dimensional even convex potential.

The common remaining failure is now more specific than at STUCK1: every successful proof route supplies either a strong angular spectral gap or a strong pointwise non-projection defect. Nothing tried so far proves that **every** admissible three-dimensional split must supply enough of one when the other is weak.

### (c) What a proof would need that no route currently contains

A proof through this homogeneous route would need an **integrated spectral-defect dichotomy** of the following qualitative form:

> For every admissible split, either the relevant even angular Poincare gap is large enough to imply (4.1), or the low-gap component forces a quantitatively positive average of `Delta=e^T C(I-C)e` large enough to make (4.4) close.

Equivalently, it must rule out a configuration in which the angular law is simultaneously low-gap and nearly two-phase while the local Hessian split is simultaneously projection-like on those phases.

The rotationally invariant proof has a fixed radial/spherical reference and a sharp weighted Poincare inequality. The arbitrary cone has neither. Runs 17--18 manufactured a substitute only from coordinate-face degeneracy. A full proof needs a coordinate-free replacement.

### (d) Simplest source-valid special case still unproved

The simplest test remains exactly (4.1) in `n=3,p=2`, but it is useful now to freeze a concrete finite-complexity subfamily inside it:

\[
\phi(x)=\max_{1\le i\le r} x^TA_i x,
\qquad
\psi(x)=\max_{1\le j\le s} x^TB_j x,
\tag{4.5}
\]

with `A_i,B_j` positive semidefinite and with enough positive definiteness in the sums to make `H=phi+psi` coercive. The first genuinely nonquadratic case is already small (`r,s>=2`). It preserves evenness, convexity and two-homogeneity exactly.

On each conic cell where one `A_i` and one `B_j` are active,

\[
H(x)=x^T(A_i+B_j)x,
\qquad
U(x)=\frac{x^TA_i x}{x^T(A_i+B_j)x}.
\tag{4.6}
\]

Thus a fixed finite candidate reduces to finitely many semialgebraic spherical cells with explicit rational-quadratic integrands. This is the smallest class in which a genuine counterexample search can be both non-Gaussian and eventually exact-certifiable.

### (e) Nearest solved problem and what its proof uses that this problem lacks

The nearest solved all-dimensional analogue remains Cordero-Erausquin--Rotem's rotationally invariant theorem. Its proof has a radial/spherical decomposition against a fixed rotationally invariant reference plus sharp weighted Poincare inequalities. Those ingredients provide global control of angular oscillation independently of the test body.

Here the angular measure itself is cone measure of `H=phi+psi`, and the observable `U=phi/H` changes with the same split. There is no fixed spherical background and no known universal weighted gap at the needed constant. Putterman's 2026 Gaussian stability result is also suggestive because its near-equality analysis forces covariance principal components toward `0` or `1`; in the present local language the analogous dangerous regime is exactly `C` near a projection. What is missing is a theorem coupling that local projection structure to the global cone measure for arbitrary even log-concave geometry.

## 5. B8 — GO THE OTHER WAY AND DISCRETIZE

Rather than approximate the source by another smooth perturbation of `l_q`, I moved the counterexample problem into the finite max-of-quadratics class (4.5).

This changes the research object in a useful way. For fixed matrices, the active-index inequalities

\[
x^T(A_i-A_k)x\ge0,
\qquad
x^T(B_j-B_l)x\ge0
\]

cut the sphere into finitely many semialgebraic cells. On each cell both the total potential and the split observable have the explicit form (4.6). The cone-density relative to Euclidean spherical measure is proportional to

\[
H(\theta)^{-3/2}
\]

in dimension three. Therefore the exact refutation question for a fixed candidate becomes a finite sum of explicit cell integrals for `1,U,U^2`.

**Outcome B8.** This is a materially different route from the previous smooth spectral perturbations. It gives a finite-complexity search space in which failure, if found, can in principle be upgraded from numerics to exact semialgebraic integration/certification. No such candidate is certified in this thinking run, so no checker is created yet.

## 6. B23 — DO WHAT THE PROPOSER DID NOT EXPECT: force angular phase separation

The most direct way to violate (4.1) is to make `U` nearly Bernoulli on cone measure. For the balanced case `m=1/2`, a violation requires

\[
\operatorname{Var}(U)>\frac1{10}.
\tag{6.1}
\]

I therefore attacked the conjecture with a maximally anisotropic, nonquadratic, involution-symmetric pair:

\[
\phi_L(x)=\max\{L^2x_1^2,x_2^2,x_3^2\},
\]

\[
\psi_L(x)=\max\{x_1^2,L^2x_2^2,x_3^2\},
\qquad L\ge1.
\tag{6.2}
\]

Both functions are even, convex and two-homogeneous. Swapping coordinates `x_1,x_2` exchanges `phi_L` and `psi_L` while preserving `H_L=phi_L+psi_L`, so cone symmetry forces `m=1/2` exactly.

The obvious hope is that `L->infinity` makes `U` concentrate near `0` and `1`. The cone weight works against that hope. A scratch rescaling around the two low-energy poles, with

\[
y_1=Lx_1,\qquad y_2=Lx_2,
\]

leads to the candidate limiting density on `R^2`

\[
\big(A(y_1)+A(y_2)\big)^{-3/2}dy_1dy_2,
\qquad A(y)=\max\{1,y^2\},
\tag{6.3}
\]

and

\[
U_\infty=\frac{A(y_1)}{A(y_1)+A(y_2)}.
\tag{6.4}
\]

I am **not** promoting convergence to (6.3) as a theorem in this STUCK2 run; the purpose is to test whether the most obvious phase-separated geometry points toward a counterexample.

The limiting integral itself can be evaluated by hand. On one quadrant, the normalizing integral decomposes into the four regions split by `y_1=1,y_2=1` and equals

\[
Z_Q
=\frac1{2\sqrt2}
+2\left(1-\frac1{\sqrt2}\right)
+(2-\sqrt2)
=\frac{16-7\sqrt2}{4}.
\tag{6.5}
\]

The centered second-moment numerator is zero on `[0,1]^2`. On one mixed strip it is

\[
I=\int_1^\infty
\frac{(x^2-1)^2}{4(x^2+1)^{7/2}}\,dx
=\frac{7-4\sqrt2}{60},
\tag{6.6}
\]

and the two mixed strips plus the outer quadrant contribute `4I`. Hence the scratch limiting variance ratio is

\[
\frac{\operatorname{Var}(U_\infty)}{(1/2)(1/2)}
=
\frac{16(7-4\sqrt2)}{15(16-7\sqrt2)}
\approx0.23484757,
\tag{6.7}
\]

well below the required failure threshold `2/5=0.4`.

**Outcome B23.** The simplest attempt to create two angular phases appears to fail badly even at infinite anisotropy. Cone measure migrates into the low-energy transition region and destroys the intended Bernoulli split. This is exactly the geometric anti-bimodality phenomenon that the arbitrary-mixture relaxation in run 12 could not see.

No source theorem is claimed from (6.7): a rigorous family limit and its source implications would require a separate proof, and this run is deliberately thinking-only.

## 7. B26 — HUNT THE SPORADIC CASE: what a genuine counterexample must look like

The failed family above shows that raw dynamic range is not the right extremal parameter.

For a balanced split with `m=1/2`, if one only knows that

\[
U\in\left[\frac1{1+\kappa},\frac{\kappa}{1+\kappa}\right],
\]

then the largest possible variance allowed by that interval is

\[
\left(\frac{\kappa-1}{2(\kappa+1)}\right)^2.
\]

To even make the dimension-three violation `V>1/10` possible from range alone, one needs

\[
\kappa>
\frac{1+\sqrt{2/5}}{1-\sqrt{2/5}}
=rac{7+2\sqrt{10}}3
\approx4.4415.
\tag{7.1}
\]

The weighted-box family has arbitrarily large pointwise contrast, so it easily passes this necessary range test, yet the cone-weight diagnostic (6.7) stays far below threshold. Therefore the sporadic object to hunt is more constrained:

1. it needs **large split contrast** so `U` can approach `0/1`;
2. those high-contrast regions must carry **large cone measure**, not merely Euclidean angular area;
3. the local contraction `C` must be nearly projection-valued there so the defect `Delta` in (4.3) stays small;
4. the global angular operator must still have a sufficiently low mode aligned with the same phase split.

A quadratic total potential cannot be that sporadic case: after linear change of variables it lies in the Gaussian theorem. The first plausible place to search is therefore a genuinely nonquadratic max-of-quadratics total potential whose active cells keep `H` comparable across the two high-contrast phases instead of making the phases expensive.

**Outcome B26.** This narrows the refutation search from “make an anisotropic norm” to “engineer simultaneous high contrast, high cone mass, low projection defect and a low angular mode.” The weighted-box involution is a useful failed extreme because it satisfies the first requirement but visibly loses the second.

## 8. Recovery choice — exactly one

Under Section I I choose exactly one recovery action:

**REFUTE INSTEAD OF PROVE.**

The next ordinary research run will not continue extending the safe `l_q^2+eps l_r^2` neighborhood. It will search the finite max-of-quadratics class (4.5) for a source-valid negative homogeneous covariance witness, beginning with involution-symmetric `2+2` and `3+3` active-cell patterns designed to keep total `H` nearly level across opposite `U` phases.

The next three unused Section-B methods reserved for that run are:

- **B19 — MAKE IT AN ALGORITHM:** turn active quadratic cells into an exact candidate-generation / cell-integration pipeline;
- **B21 — ASK WHO ELSE HAS THIS SHAPE:** compare the projection-defect dichotomy with Gaussian `(B)` stability and extremal Hessian-splitting problems;
- **B28 — REPLACE FOR ALL WITH TYPICAL:** determine whether a random finite max-of-quadratics split generically has enough cone anti-bimodality, so any counterexample must live on an exceptional algebraic stratum.

This is the **second** stuck-recovery cycle for the current weak-`(B)` target. If the same source obligation reaches the next Section-I trigger unchanged after this recovery, the owner rule requires a handoff and rotation to a fresh eligible problem rather than a third recovery on weak `(B)`.

## 9. Why there is no new checker/artifact in this run

This is the mandated STUCK2 thinking run. No finite counterexample candidate was promoted and no theorem-sized claim was asserted. Creating a checker merely to recertify the unchanged `D_B=2` baseline or the previously certified mixed `l_4+l_6` subclass would violate the 90/10 rule.

The only new numerical-looking value in this report, (6.7), is an analytically evaluated **scratch limiting integral** used to reject a route; it is not a certified statement about the finite-`L` source family. Accordingly no `artifacts/hard7_2026-09-18/HARD7-01/` file is created in this run.

## 10. Model / scheduler-control truth

Actual model visible to this invocation: **GPT-5.6 Sol**.  
Reasoning-effort telemetry: **UNVERIFIED**.  
I do not claim GPT-6 maximum.

The exposed scheduled-task interface still provides task title/prompt, schedule or relative-start configuration, timing mode, enabled state and task identity/list/update operations. It exposes **no binding model-family selector, no binding reasoning-effort selector, no guaranteed run-duration field, and no authenticated per-run applied-model/applied-effort receipt**. Thus `GPT-6 / maximum` remains prompt-requested only on this surface.

Making that request binding would require a product/workspace/API/admin scheduling surface that persists explicit model-family and reasoning-effort fields into inference routing and returns trustworthy runtime attestation.

The historical native response `You cannot modify this task` for P26 is an authorization-context boundary, not a mathematical issue. Repository continuity records later successful P26 updates from an authorized context. The compliant workaround is to use the owning/authorized account, workspace, API/admin surface for the same native task, or platform support. It is **not** to create a duplicate schedule, bypass permissions, or substitute another task identity.

No scheduler, permission, email, Drive, public-posting or workflow mutation was attempted.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: HARD7-01
  lane: HARD_OUTSIDE
  source: weak_B_conjecture_even_logconcave
  canonical_claim: operations/claims/B-WEAK-EVEN-LOGCONCAVE.md
  source_status: OPEN_IN_BOUNDED_2026_09_19_CHECK
  research_status: PARTIAL_STUCK2
  metric:
    field: D_B
    before: 2
    after: 2
    movement: false
  methods: [8, 23, 26]
  recovery_choice: REFUTE_INSTEAD_OF_PROVE
  simplest_unproved_case: >-
    n=3, p=2 smooth/even/convex/two-homogeneous common-degree split;
    target Var_nu(U) <= (2/5) m(1-m).
  counterexample_search_next: >-
    finite max-of-quadratics splits with involution symmetry and total potential
    kept comparable across opposite high-contrast angular phases
  new_theorem_claim: false
  new_finite_claim: false
  new_checker_created: false
  source_metric_movement: false
  next_methods: [19, 21, 28]
  lifecycle: >-
    second stuck-recovery cycle on current weak-B target; next unchanged
    Section-I trigger forces handoff/rotation rather than a third recovery
  scheduler_model_selector: NOT_EXPOSED
  scheduler_reasoning_selector: NOT_EXPOSED
  actual_model: GPT-5.6_Sol
  actual_reasoning_level: UNVERIFIED
```

## 12. Disposition

**HARD7-01 remains PARTIAL on the source, with `D_B=2`.** The previous proof-oriented spectral route has reached its second allowed stuck recovery. The next bounded run is a counterexample search in the finite max-of-quadratics class, not another extension of the same safe cone family.