Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. GPT-6/maximum remains prompt-requested only because the exposed scheduler/runtime interface has no binding model selector, reasoning-effort selector, authenticated effort telemetry, or guaranteed run duration. **No movement in the frozen source metric: `S=5 -> 5`. Section-I state: STUCK1 thinking-only; no new mathematical claim is made. Diagnostic moves tried: B8, B13, B22.**

# HARD7-02 STUCK1 — reduce Campbell–O'Rourke Question 1.8 to an output-level axis test

Status: **PARTIAL / source Question 1.8 remains OPEN_BY_BOUNDED_SEARCH.**

This execution is intentionally a Section-I thinking run. The previous three ordinary research runs left the frozen source metric unchanged, so this report does **not** add another auxiliary lemma, checker, finite-size experiment, or certificate. Its purpose is to isolate the exact blocker, record why the routes already tried do not cross it, and choose one recovery route that can actually decide source-level dependence rather than another property of a truncation or local neighborhood.

## 1. Continuity, required repository reads, ownership, and current source check

I resumed the exclusive claim

`operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md`

and the newest own checkpoint

`runs/hard7_2026-09-18/HARD7-02/2026-09-19T05-12-00Z__rank-wedge-correlation-homogeneous-pwit-criterion.md`.

At run start I re-read:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the HARD7-02 report chain from admission through the 05:12Z checkpoint;
- the C0026--C0032 random-matrix neighborhood of `probability_1000_intake_claude_20260907/problems.jsonl` by repository search;
- the newest neighboring heavy-tail report located at `research7_2026-09-17/R7-06/runs/2026-09-19/2026-09-19T050300Z__report.md`.

Repository claim/alias searches still identify Campbell–O'Rourke Question 1.8 as owned only by HARD7-02. The neighboring R7-06/C0032 target is the distinct Bordenave–Chafaï i.i.d. heavy-tail density-identification problem. C0029 remains the excluded Bernoulli/least-singular-value family. No posted, personal-manuscript, Bernoulli-singularity, or equivalent currently claimed target was found under a canonical alias.

### Primary source and current-status check

Primary source:

Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, Electronic Journal of Probability 27 (2022), paper 127, DOI `10.1214/22-EJP849`, arXiv `2010.01261v3`.

- https://arxiv.org/abs/2010.01261
- https://arxiv.org/html/2010.01261v3

The arXiv record checked on 2026-09-19 still lists v3, revised 2022-02-02, as the latest version. Section 1.3 still asks exactly:

> “What properties of `theta_d` determine `mu_{alpha,theta_d}`?”

Theorem 1.6 still expresses the limiting ESD through the logarithmic potential of the limiting singular-value law, and Remark 1.7 still identifies the balanced axis case with the Bordenave–Caputo–Chafaï i.i.d. heavy-tail limit.

A fresh bounded 2026-09-19 search used the exact paper title/authors together with `Question 1.8`, `theta_d`, `mu_{alpha,theta_d}`, `PWIT`, `dependence measure`, `erratum`, `correction`, `rank`, `multitype`, and 2023--2026 date terms. It recovered the 2022 source, Bordenave–Caputo–Chafaï's 2011 i.i.d. paper, Campbell–O'Rourke's later Lévy–Khintchine Laplacian paper, and unrelated later elliptic/free-probability work. I found no later source claiming a full answer to Question 1.8 and no located correction that supplies the asymmetric rank-marked output recursion needed below. This is **bounded negative evidence**, not a worldwide novelty certificate.

### Scheduler/runtime capability statement

The interface exposed to this worker still offers task prompt/schedule/timing/enabled controls but no authenticated model selector or reasoning-effort selector. Therefore the requested GPT-6/maximum setting cannot be made binding from this worker. Making it binding would require a platform scheduler field for model and reasoning effort, plus runtime telemetry that authenticates what actually executed, or an authorized owner-side runtime that exposes those controls.

The current root `RESULTS.md` corrects an older operational fact: P26 historically returned `You cannot modify this task`, but a later authorized native context successfully updated P26. Historical denials for P01/P03 and other contexts do not imply a current universal denial. This run made **no scheduler modification**. For any task that still returns a permission error, the compliant workaround is the authorized owner/account/workspace interface or platform support/ownership transfer; do not bypass the permission boundary and do not create a duplicate task.

## 2. Frozen metric and why Section I is active

The canonical claim freezes

`S = number of exact nontrivial full-source transformation laws for theta_d -> mu_{alpha,theta_d}`

proved by HARD7-02 under the source hypotheses.

Before this run: `S=5`.

After this run: **`S=5` (no movement).**

The five retained source-level laws are the three finite-matrix covariance laws from run 1, opposite-coordinate-phase invariance / relative-phase mixing from run 4, and positive mass/scaling covariance from run 6. Runs 7, 8, and 9 were three consecutive ordinary no-movement runs. Therefore this execution is **STUCK1**, the first of at most two Section-I recovery episodes permitted on this hard target. This thinking run does not reset the streak by inventing a different metric.

No exact-arithmetic artifact is created in this run because Section I requires no new claim. The existing artifact/checker archive is unchanged.

## 3. (a) The exact statement that now blocks progress

The cleanest source-valid obstruction is already present inside the one-parameter axis family. Fix `0<alpha<2` and

\[
\boxed{\quad
\theta_p=p\,\delta_{(1,0)}+(1-p)\,\delta_{(0,1)},\qquad 0<p<1:\qquad
\text{decide whether }\mu_{\alpha,\theta_p}=\mu_{\alpha,\theta_{1/2}}\text{ for all }p,
\text{ or exhibit an interior }p\text{ for which they differ.}
\quad}
\]

This is not a reformulation invented to make the source easier. Every `theta_p`, `0<p<1`, is C2-admissible after choosing a standard heavy-tail realization, while `p=0,1` are excluded boundary points because one coordinate degenerates. Transposition already gives the exact symmetry `p <-> 1-p`, so only `0<p<=1/2` matters.

Why this is the right blocker:

- all `theta_p` have the same product pushforward under `pi(z,w)=zw`, namely a point mass at zero;
- run 5 proved product-only universality for the entire **subcritical hard-edge truncation**, but did not prove it for the full source limit;
- run 4 proved the stronger safe upper bound that the quotient `q(z,w)=(|z|^2,zw)` is sufficient for the full source limit, so the unresolved question is whether the first coordinate of that quotient still contains genuine output information;
- Campbell–O'Rourke Remark 1.7 identifies `p=1/2` with the solved i.i.d. Bordenave–Caputo–Chafaï law;
- therefore the axis family is the smallest test that can decide whether the full limiting ESD forgets the rank/orientation imbalance that survives every local correction made in runs 2--9.

A finite directed cycle, a finite SAT-style witness, a sampled ESD, or a fixed hard-edge cutoff cannot decide the displayed statement.

## 4. (b) Routes already tried and the precise reason each stopped

This list is deliberately about failures, not accomplishments.

### Route R1 — exact finite-matrix symmetries

Runs 1 and 6 used transpose, common phase, conjugation, and positive scalar multiplication. These gave exact source-level laws and moved `S`, but they only quotient obvious global matrix operations. They provide no map carrying `theta_p` to `theta_q` when `q` is neither `p` nor `1-p`.

**Failure mode:** the remaining axis imbalance is not generated by a deterministic spectral identity of the original finite matrix.

### Route R2 — the printed homogeneous PWIT recursion

Run 2 tested the source's homogeneous PWIT description away from swap symmetry. A uniformly rerooted matrix remembers the normalized original rank `u`; edges to higher and lower ranks see `theta` and `tau#theta` in different proportions. The homogeneous depth-one law therefore fails for asymmetric `theta`.

**Failure mode:** using Proposition 4.12 verbatim for `p!=1/2` discards a latent rank variable that is visible already in exact root-edge counts.

### Route R3 — repair the local limit by retaining rank

Run 3 supplied the corrected rank-marked local operator with type kernel

`K_u(dv,dy)=1_{v>u} dv nu(dy)+1_{v<u} dv (tau#nu)(dy)`.

This repairs the local convergence route and gives the right object to analyze.

**Failure mode:** correctness of the local object is not a classification theorem. The Hermitized root law is now a continuum-type recursive distribution, not the scalar/homogeneous RDE solved in the i.i.d. case.

### Route R4 — tree gauge and quotient reduction

Run 4 proved that opposite coordinate phase is pure gauge on the corrected tree and reduced the full source dependence to the pushforward under

`q(z,w)=(|z|^2,zw)`.

**Failure mode:** `q` is a sufficient statistic, but no argument proves it is minimal. On the axis family, `q#theta_p` still remembers `p` through the masses at `|z|^2=1` and `0`.

### Route R5 — product-only matching polynomial

Run 5 observed that a finite weighted tree's characteristic polynomial sees only the unoriented edge products and used this to prove product universality throughout the subcritical hard-edge truncation.

**Failure mode:** the full matrix cannot be reached by a forest argument. Once the cutoff passes the cycle threshold, directed cycle holonomy/orientation information survives; removing cyclic components then costs a positive fraction of vertices.

### Route R6 — directed-cycle threshold and boundary layer

Runs 7 and 8 converted the axis truncation to an order-biased sparse directed graph and obtained the exact cycle threshold/window. Run 8 then found the threshold mechanism already in the classical directed-random-graph literature and correctly downgraded novelty.

**Failure mode:** these are cutoff statements. The source asks for the full heavy-tailed ESD after all scales are restored, and no uniform cutoff-removal estimate was obtained. Finite-cutoff spectral collapse does not imply full-source collapse.

### Route R7 — random relabeling / symmetrize the orientation

Run 9 attacked the idea that random relabeling might average `theta` to `(theta+tau#theta)/2`. It found the exact rank-wedge defect for two incident edges and proved that, after forgetting rank, the corrected local marks become independently homogeneous only in the swap-symmetric case.

**Failure mode:** one-edge marginals symmetrize, but higher incident-edge laws retain a shared-rank correlation. A proof that sees only the one-edge marginal is therefore insufficient.

### Route R8 — infer ESD dependence from local dependence

The rank-wedge covariance, mixed-Poisson excess variance, and cycle counts all depend on `p`.

**Failure mode:** none of those quantities is a functional of the limiting eigenvalue measure. Nonnormal matrices can have very different local/singular structures with the same eigenvalue law. The missing bridge must pass through Hermitization/logarithmic potential or an equivalent Brown-measure object.

## 5. (c) What a successful proof must contain that no route so far contains

A source-level decision of the axis blocker needs an **output-level statistic**. Concretely, the corrected rank-marked operator should produce a type-dependent Hermitized root resolvent `R_u(z,eta)`. After averaging the uniform root type, define the limiting symmetrized singular-value transform through

`F_p(z,eta) = integral_0^1 E[ (1/2) Tr R_u(z,eta) ] du`.

The exact normalization can be chosen to match the source's bipartization convention; this line records the object that must be controlled, not a new theorem.

A decisive argument must do all of the following:

1. derive the correct **type-dependent** recursion for `R_u` from the rank-marked tree, rather than importing the homogeneous Proposition 4.12 outside its valid symmetric regime;
2. show that the `p`-dependence survives or cancels **after averaging over `u`**, not merely before averaging;
3. transfer that information from the regularized Hermitized resolvent to
   `L_p(z)=int log(t) d nu_{alpha,z,theta_p}(t)`;
4. control the `eta -> 0` / logarithmic singularity using the same uniform-integrability level required by Girko Hermitization, rather than a fixed positive regularizer;
5. finally show either that `L_p-L_{1/2}` has nonzero Laplacian somewhere (hence different ESDs) or that the whole potential agrees after the normalization at infinity (hence identical ESDs).

The key point is item 5. A difference in a singular-value law at one regularization parameter is not by itself enough, because two logarithmic potentials that differ only by a harmonic term determine the same planar measure.

## 6. (d) Simplest special case still unproved

The recovery should not attack every `alpha` and every `p` at once. The simplest decisive interior comparison is

`alpha=1`, `p=1/4` versus `p=1/2`.

Reasons for this choice:

- both parameters are strictly inside C2;
- `p=1/2` is the exact Bordenave–Caputo–Chafaï case singled out by source Remark 1.7;
- `alpha/2=1/2`, so the positive stable variables appearing in the Hermitized recursion are the explicit one-sided `1/2`-stable (Lévy) law, the most tractable stable index available here;
- transpose symmetry already handles `p=3/4`;
- the existing relative-phase mixing law allows the axis phases to be put in a convenient gauge without changing the limiting ESD, so phase bookkeeping should not be the obstruction.

The first decisive statement to target next is therefore not “classify every `theta`,” but

`mu_{1,theta_{1/4}} ?= mu_{1,theta_{1/2}}`.

An inequality would refute product-only full-source universality immediately. Equality would not settle all `p`, but it would force the next attack to look beyond the most obvious imbalance witness.

## 7. (e) Nearest solved problem and the ingredient it has that this one lacks

The nearest solved problem is:

Charles Bordenave, Pietro Caputo, Djalil Chafaï, *Spectrum of Non-Hermitian Heavy Tailed Random Matrices*, Communications in Mathematical Physics 307 (2011), 513--560, arXiv `1006.1713`.

- https://arxiv.org/abs/1006.1713
- DOI `10.1007/s00220-011-1331-9`

That paper treats the i.i.d. heavy-tail model. Campbell–O'Rourke Remark 1.7 identifies its limiting singular/eigenvalue measures with the balanced axis dependence measure `theta_{1/2}`.

What their proof has that the asymmetric axis model lacks is **homogeneous recursive closure**. In the i.i.d./balanced case, the bipartized PWIT has identically distributed child messages and the root resolvent can be described by a type-free recursive distributional equation. Rotational symmetry then reduces the Brown-measure calculation further. In the corrected `p!=1/2` model, the normalized rank `u` is a genuine type; child laws depend on whether `v<u` or `v>u`, and run 9 shows that marginalizing `u` does not restore independence of incident marks. Thus the Bordenave–Caputo–Chafaï scalar recursion cannot simply be copied.

A secondary technique lead, not a solved substitute, is the literature on triangular/elliptic operators and operator-valued Brown measures (including Dykema–Haagerup type triangular operators and later triangular-elliptic Brown-measure work). Its relevance is conceptual: `p` interpolates between a balanced bidirectional regime and a nearly triangular regime. No located theorem, however, covers this alpha-stable rank-marked continuum kernel under the Campbell–O'Rourke hypotheses, so citing that literature is not a solution.

## 8. Section-B diagnostic moves used in this thinking run

### B8 — GO THE OTHER WAY AND DISCRETIZE

I tested the route of replacing the continuum rank type `u in [0,1]` by `m` bins. This would convert the corrected rank-marked recursion into a finite `m`-type cavity system, where each type sees explicit upper/lower transition weights. At fixed positive Hermitization parameter this is a plausible finite-dimensional object on which contraction/implicit-function methods could be attempted.

**Why it does not yet solve the blocker:** the needed estimates must be uniform in `m`, stable under `m -> infinity`, and strong enough to survive the logarithmic `eta -> 0` passage. None of those uniform estimates is currently in the track. Therefore no discretized calculation is promoted to a theorem or checker in this run.

### B13 — FIND WHAT ONLY INCREASES

I looked for a source-level scalar that should vary monotonically with the imbalance `|2p-1|`: a radius, a regularized logarithmic potential, a root-resolvent trace, or a stable scale parameter. The order-biased cycle threshold from runs 7--8 strongly suggests that imbalance has a natural monotone spectral scale at the truncation level.

**Why it does not yet solve the blocker:** no monotonicity principle for the full nonnormal Hermitized recursion is known here. Entrywise stochastic domination is destroyed by the matrix inverse in the cavity equation, and a monotone hard-edge cycle scale need not be monotone for the full Brown measure. The run therefore records this only as a search direction.

### B22 — READ THE FAILURES, NOT THE SUCCESSES

I re-read the point where the Campbell–O'Rourke proof invokes the homogeneous PWIT/Proposition 4.12 and compared it with the Bordenave–Caputo–Chafaï i.i.d. recursion. The precise lost ingredient is now clear: iid child messages are replaced by a continuum-type family coupled through the order kernel. A bounded literature search for `multitype PWIT`, `inhomogeneous Levy matrix`, `operator-valued heavy-tail resolvent`, and `triangular elliptic Brown measure` found analogies but no theorem that directly supplies the missing alpha-stable type-dependent Brown measure.

**Outcome:** useful diagnosis, no new claim. The next run should stop searching globally and attack the axis output recursion itself.

## 9. Exactly one Section-I recovery choice

**RECOVERY CHOICE: REFUTE INSTEAD OF PROVE.**

The tempting stronger conjecture to attack is:

`(H_pi)  pi#theta_1 = pi#theta_2  =>  mu_{alpha,theta_1}=mu_{alpha,theta_2},  where pi(z,w)=zw.`

The axis family is the minimal test because `pi#theta_p` is identical for every `p`. The next execution should try to refute `(H_pi)` by proving an output-level difference between `p=1/4` and `p=1/2` at `alpha=1`. It should not return to finite-cutoff cycle counts unless they are explicitly converted into a logarithmic-potential statement.

The most promising local perturbation parameter is

`delta = p-1/2`.

The known transpose law makes the final ESD an even function of this imbalance whenever a differentiable parametrization is justified, so the first potentially informative perturbative term is second order. The corrected rank kernel can be written in the form “balanced part + `delta` times the rank-order sign kernel”; the recovery should linearize the **Hermitized type recursion**, not the raw adjacency matrix.

### Three moves precommitted for the recovery run

- **B21 — ASK WHO ELSE HAS THIS SHAPE:** extract the usable part of triangular-elliptic / operator-valued Dyson or Brown-measure techniques and see whether the continuum rank kernel admits an operator-valued fixed-point formulation.
- **B5 — ADD A PARAMETER AND DIFFERENTIATE:** differentiate the regularized type-resolvent system in `delta` at `delta=0`; by transpose symmetry, target the second variation rather than wasting time on a forced first-order zero.
- **B11 — DUALIZE:** work on the Hermitized/logarithmic-potential side. A nonzero, non-harmonic second variation of the limiting log potential is an output-level certificate that the ESD depends on `p`.

This triple differs from the immediately preceding B9/B10/B26 run. B21 is fresh on this target; B5/B11 are deliberately reused only after reducing to the new axis-output problem, because they now act on a different object than in runs 4 and 1.

## 10. Handoff condition if STUCK1 recovery fails

The next run gets one honest attempt at the displayed axis-output problem. If it cannot produce either (i) a controlled second-variation formula with a route through `eta -> 0`, or (ii) a rigorous equality mechanism washing out `p`, then the second Section-I episode must state that failure explicitly and choose one final recovery. A third stuck episode on Campbell–O'Rourke Question 1.8 requires a handoff and rotation to a fresh eligible sparse/correlated non-Hermitian source problem; the schedule itself must remain enabled.

## 11. Ledger delta

```yaml
ledger_delta:
  track: HARD7-02
  target: Campbell-O'Rourke 2022 Question 1.8
  canonical_claim: operations/claims/CAMPBELL-OROURKE-2022-Q1.8.md
  metric: S
  before: 5
  after: 5
  movement: none
  status: PARTIAL
  source_status: OPEN_BY_BOUNDED_SEARCH
  protocol_state: STUCK1
  ordinary_no_movement_runs_triggering_stuck: 3
  stuck_recovery_count: 1/2
  new_theorem_claims_this_run: 0
  new_artifacts_this_run: 0
  recovery_choice: REFUTE_INSTEAD_OF_PROVE
  recovery_target: refute product-only full-source universality via alpha=1 axis p=1/4 versus p=1/2
  next_methods: [B21, B5, B11]
  shared_root_files_modified: []
  scheduler_changes: []
```

No root ledger was edited in this worker run; the structured delta above is for the designated reconciler. No email, Drive, public posting, scheduler creation, scheduler modification, permission bypass, or other-track file edit was performed.
