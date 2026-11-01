Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No source-metric movement: `D_B=2 -> D_B=2`. This is the required STUCK1 thinking-only run; no new theorem claim is made. Methods tried: B18 / B22 / B29.**

# HARD7-01 run 13 — STUCK1: cone-spectral reformulation and a route to geometric anti-bimodality

Status: **PARTIAL / source OPEN / STUCK1 recovery chosen**.

## 1. Continuity, current source, ownership, and required reads

This invocation resumes the exact current HARD7-01 target from

`runs/hard7_2026-09-18/HARD7-01/2026-09-19T08-02-26Z__weakB_cone_variance_stuck1_trigger.md`.

That report recorded the third consecutive unchanged value of the frozen source metric and therefore required the next invocation to be a Section-I **thinking-only STUCK1 report**, rather than another lemma-producing run. I follow that instruction here.

The active create-only canonical claim remains

`operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`,

owned by HARD7-01, status `CLAIMED / source OPEN / research PARTIAL only`. Repository-wide claim/alias searches recovered no competing owner. Other workers' current reports explicitly recognize this claim as HARD7-01-owned.

Before this analysis I reread/reconciled:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/claims/B-WEAK-EVEN-LOGCONCAVE.md`;
- the newest own HARD7-01 checkpoint above;
- the newest materially neighboring R02 report available in the repository, `runs/R02/20260919T0716Z_successor_admission_r13_pair_lift_obstruction_17_10_20_9f2c6a41.md`;
- repository-wide indexed claim/intake/alias searches for the weak `(B)` target and its standard names.

The connector does not expose a trustworthy byte-for-byte streaming read of every large append-only intake JSONL in one bounded response. I therefore do not falsely claim one. The current root/campaign surfaces, canonical claim, neighboring state, and indexed intake/alias searches were checked directly.

### Exact source target retained

For every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, and every origin-symmetric convex body `K`, prove that

\[
t\longmapsto \mu(e^tK)
\]

is log-concave on `R`.

The frozen source metric remains

\[
D_B:=\max\{d:\text{the exact statement is proved for every admissible }(\mu,K)
\text{ in every }n\le d\}.
\]

Saroglou's planar theorem gives the verified baseline

\[
\boxed{D_B=2.}
\]

This thinking run deliberately does not relabel a structured subclass as a dimension-three proof, so

\[
\boxed{D_B:2\longrightarrow2.}
\]

**No movement.**

## 2. Fresh source/current-literature sentinel — 2026-09-19

I rechecked the exact weak statement and its principal equivalent formulations against current primary/current literature. The bounded search recovered no paper claiming the unrestricted all-dimensional theorem. This remains bounded negative evidence, not a worldwide novelty certificate.

The sources most relevant to this recovery are:

1. D. Cordero-Erausquin and L. Rotem, **Several results regarding the (B)-conjecture**, *Geometric Aspects of Functional Analysis*, LNM 2256 (2020), 247--262, DOI `10.1007/978-3-030-36020-7_11`. Theorem 7 gives the homogeneous correlation formulation. The same source explicitly remarks that in dimension at least two the radial derivatives need not be correlated under an arbitrary probability law and that the difficulty is to exploit the special Gibbs law proportional to `exp(-phi-psi)`.
2. C. Saroglou, **More on logarithmic sums of convex bodies**, *Mathematika* 62 (2016), arXiv:1409.4346. Log-Brunn--Minkowski in a dimension implies `(B)` there, yielding the verified planar baseline.
3. D. Cordero-Erausquin and L. Rotem, **Improved log-concavity for rotationally invariant measures of symmetric convex sets**, *Ann. Probab.* 51 (2023), 987--1003, arXiv:2111.05110. This proves `(B)` for rotationally invariant log-concave measures using sharp weighted Poincare inequalities; it does not prove the unrestricted source.
4. D. Cordero-Erausquin and A. Eskenazis, **Concavity principles for weighted marginals**, arXiv:2506.16941 (2025). It supplies substantial structured classes, not the full source.
5. S. Armeniakos and J. Ulivelli, **A strengthening of the dimensional Brunn-Minkowski conjecture implies the (B)-Conjecture**, arXiv:2602.23350 (submitted 2026-02-26). It proves a strengthened-dimensional-BM implication and the hereditarily-convex class, not all even log-concave measures.
6. E. Putterman, **Sharp stability for the (B)-theorem**, arXiv:2608.08472 (2026-08-09). This concerns the Gaussian theorem and strong/functional stability, not unrestricted weak `(B)`.
7. G. Aishwarya and L. Rotem, **New Brunn--Minkowski and functional inequalities via convexity of entropy**, arXiv:2311.05446. Its homogeneous-potential dimensional Brunn--Minkowski theorem is a nearby solved homogeneous result, but it is not the weak `(B)` conjecture.

The Cordero-Erausquin--Rotem 2020 source is especially useful here because the published reverse implication constructs the same-degree pair

\[
\phi_m(x)=\|x\|_K^m,\qquad \psi_m(x)=\|x\|_T^m,
\]

and sends `m` to infinity. Thus a common-degree homogeneous correlation program is source-relevant rather than an unrelated strengthening.

## 3. Required Section-I obstruction map

### (a) The exact statement that blocks

The previous run isolated the obstruction as geometric realizability of the angular law. Rewriting the same obstruction through the homogeneous correlation formulation makes the missing inequality more explicit.

Take even convex `C^2` functions `phi,psi` that are positively homogeneous of the **same** degree `p>=2`, set

\[
H=\phi+\psi,\qquad K_H=\{x:H(x)\le1\},
\]

let `nu_H` be cone probability measure on `partial K_H`, and define

\[
U(z)=\phi(z),\qquad z\in\partial K_H,
\]

so `0<=U<=1` and `psi(z)=1-U(z)`. Put `m=E_{nu_H}U`. The sharp angular inequality whose absence blocks this route is

\[
\boxed{
\operatorname{Var}_{\nu_H}(U)
\le \frac{p}{n+p}\,m(1-m).
}
\tag{3.1}
\]

Equivalently,

\[
\boxed{
\mathbb E_{\nu_H}[U(1-U)]
\ge \frac np\operatorname{Var}_{\nu_H}(U).
}
\tag{3.2}
\]

This is not asserted here as a newly proved theorem. Section 4 below derives it as the exact scratch target obtained by unpacking the already-published homogeneous correlation formulation in the common-degree family used by its reverse approximation.

### (b) Every route tried on the current weak-`(B)` target, and why it stopped

The current target has had exactly three ordinary research runs before this STUCK1 analysis.

**Run 10: B2 / B5 / B24.**

- **B2, attack the negation:** for a `p`-homogeneous potential the curvature became `p^2 s(s Var_s(V)-E_sV)`. This gave an exact counterexample criterion but no mechanism forcing its sign in the full class.
- **B5, parameter differentiation:** divergence converted the sign to boundary-flux mean versus interior tilted mean. The identity is exact, but convexity alone did not supply the required boundary/interior ordering.
- **B24, extremal object:** low- and high-scale safe regions trapped any homogeneous counterexample in a compact intermediate window. That controls where failure can occur, not whether it can occur, and it says nothing by itself about a general nonhomogeneous potential.

**Run 11: B1 / B3 / B6.**

- **B1, change category:** weak `(B)` became monotonicity of the reverse hazard of `log ||X||_K`. An exact rectangle example killed the stronger shell-density-logconcavity route. Reverse-hazard language did not produce the missing monotonicity theorem.
- **B3, prove something stronger:** a radial-elasticity plus angular-oscillation hypothesis closed a source-valid restricted theorem. The extra hypotheses are much stronger than even log-concavity and cannot be inserted into the source.
- **B6, deform from a solvable point:** a mixed-degree nonradial three-dimensional family survived a deformation from a homogeneous model. This established robustness of one restricted class, not the unrestricted dimension-three theorem.

**Run 12: B11 / B20 / B30.**

- **B11, dualize:** cone/ray disintegration gave
  `log Q'' = angular reverse-hazard variance - average ray damping`. Every individual ray was already log-concave. The entire problem moved into controlling angular mixing.
- **B20, find why the algorithm fails:** an exact two-atom angular relaxation inside the homogeneous kernel family made the mixture curvature positive. Therefore no generic theorem saying “a mixture of the good rays is good” can work. The witness was deliberately not source-realizable.
- **B30, one scale/direction at a time:** the homogeneous problem was scalarized to a gamma transform of a realizable pushforward law. The remaining word “realizable” contains precisely the convex geometry not captured by one-dimensional mixture inequalities.

The common failure is now clear: all algebraic/radial reductions eliminate everything except a **quantitative restriction on angular heterogeneity imposed jointly by convexity of both pieces**. No prior route contains such a theorem.

### (c) What a proof must contain that the tried routes do not contain

A successful continuation must use more than:

- log-concavity of each ray;
- ordinary log-concavity of a scalar pushforward;
- arbitrary-mixture closure;
- low/high-scale truncation;
- pointwise radial monotonicity.

It must exploit the fact that `U` is not an arbitrary `[0,1]` random variable: it is the **split of one convex homogeneous potential into two convex homogeneous summands on the unit level surface of their sum**. Quantitatively, it must rule out the almost two-phase angular laws that defeat B20.

In the common-degree language, the needed mechanism can be phrased as a sharp cone-measure variance/Poincare inequality with product/subspace splittings as the calibration case. In the published rotationally invariant proof, the analogous missing ingredient is supplied by a sharp weighted Poincare inequality after radial/spherical decomposition. That is the piece the unrestricted geometry currently lacks.

### (d) Simplest source-valid special case still unproved by this track

The smallest clean test case for the new route is

\[
n=3,\qquad p=2,
\]

with `phi,psi` smooth, even, convex, two-homogeneous and nonquadratic in general. The angular target becomes

\[
\boxed{
\operatorname{Var}_{\nu_H}(U)\le \frac25 m(1-m).
}
\tag{3.3}
\]

Pure quadratic pairs reduce to Gaussian linear algebra and therefore are not the point. The unresolved test is the genuinely nonquadratic squared-norm geometry. Proving (3.3) for this whole class would still be a **restricted partial theorem**, not `D_B=3`, but it would test exactly the spectral/cone mechanism needed by the full source rather than another radial sufficient condition.

### (e) Nearest solved problem and what its proof has that this problem lacks

The nearest solved all-dimensional analogue is Cordero-Erausquin--Rotem's rotationally invariant theorem. Their proof separates radial and spherical contributions and establishes sharp weighted Poincare inequalities for even measures log-concave relative to a rotationally invariant reference.

The unrestricted common-degree pair has no fixed spherical reference: the angular measure is cone measure of the arbitrary body `K_H={H<=1}`, and the observable `U=phi/H` is coupled to that same geometry. The missing object is therefore not “a Poincare inequality somewhere”; it is a **sharp angular inequality compatible with the varying cone geometry and the convex split**.

This comparison determines the recovery choice in Section 7.

## 4. B18 — SAY IT IN ANOTHER LANGUAGE: homogeneous correlation becomes a cone variance target

This section is a **route calculation only**, not a new theorem claim and not metric movement.

Cordero-Erausquin--Rotem Theorem 7 asks, for homogeneous even convex `phi,psi`, for nonnegative covariance under

\[
d\mu(x)=Z^{-1}e^{-\phi(x)-\psi(x)}dx.
\]

Restrict to the common-degree `p` family used in their reverse approximation and write `H=phi+psi`. Cone polar coordinates for `K_H={H<=1}` separate a point as

\[
X=RZ,
\qquad Z\sim\nu_H,
\]

where `Z` is independent of `R`. Since `H` is `p`-homogeneous and `H(Z)=1`,

\[
Y:=R^p\sim\operatorname{Gamma}(k,1),\qquad k=\frac np.
\]

On the level surface set `U=phi(Z)`, so `psi(Z)=1-U`. Then

\[
\phi(X)=YU,\qquad \psi(X)=Y(1-U).
\]

Writing `m=EU` and `v=Var(U)`, the gamma identities `EY=k` and `EY^2=k(k+1)` give the diagnostic algebra

\[
\operatorname{Cov}(\phi(X),\psi(X))
=k\big[m(1-m)-(k+1)v\big].
\tag{4.1}
\]

Thus the published homogeneous correlation target in this common-degree slice asks for exactly (3.1). The same calculation gives a second useful language:

\[
\operatorname{Cov}(\phi,H)=\mathbb E\phi,
\]

and hence

\[
\operatorname{Cov}(\phi,\psi)
=\mathbb E\phi-\operatorname{Var}(\phi).
\tag{4.2}
\]

So the desired correlation is the spectral-looking inequality

\[
\operatorname{Var}_{\mu}(\phi)\le \mathbb E_{\mu}\phi.
\tag{4.3}
\]

This explains why the rotational Poincare method is not merely adjacent literature: it is pointed at exactly the missing quantity.

There is also a calibration check. For the product model

\[
H(x)=\sum_{i=1}^n |x_i|^p,
\qquad
\phi(x)=|x_1|^p,
\qquad
\psi(x)=\sum_{i=2}^n|x_i|^p,
\]

the cone coordinate `U=|Z_1|^p` has the standard beta law with parameters `1/p` and `(n-1)/p`. Its variance-to-Bernoulli-variance ratio is exactly

\[
\frac{\operatorname{Var}(U)}{m(1-m)}=\frac{p}{n+p}.
\tag{4.4}
\]

So the coefficient in (3.1) is calibrated by a natural product splitting; there is no obvious slack to buy by weakening the constant.

Finally, ordinary Brascamp--Lieb indicates the size of the spectral gap. Formally, for smooth strictly convex `H` and `phi`,

\[
\operatorname{Var}_{\mu}(\phi)
\le \mathbb E\langle(\nabla^2H)^{-1}\nabla\phi,\nabla\phi\rangle
\le \frac{p}{p-1}\mathbb E\phi,
\tag{4.5}
\]

using `nabla^2 H >= nabla^2 phi` and Euler homogeneity. The source target wants the factor `1`, not `p/(p-1)`. For `p=2` this is exactly a missing factor of two, matching the familiar even-function improvement in Gaussian spectral inequalities. This is a strong reason to port the **even weighted Poincare** mechanism rather than continue scalar hazard algebra.

**Outcome B18:** a useful language change. The obstruction is a sharp angular/even-spectral inequality, not another radial calculus identity. No source claim is advanced in this thinking run.

## 5. B22 — READ THE FAILURES, NOT THE SUCCESSES

The 2020 Cordero-Erausquin--Rotem note states the failure mode unusually clearly: in dimension `n>=2`, the relevant radial derivatives need not be correlated for an arbitrary probability measure, even under a related log-concavity condition; the unresolved issue is how to use the **special choice** of Gibbs measure proportional to `e^{-phi-psi}`.

That statement lines up exactly with the fleet's B20 stress test from the previous run. There an arbitrary two-atom angular law, inserted into the exact homogeneous ray kernel, produced positive curvature and destroyed log-concavity. The calculation was an exact self-check, but the law was not claimed geometrically realizable.

Taken together, these failures rule out a large class of tempting continuations:

1. **Generic positive-mixture closure is false.**
2. **One-dimensional log-concavity of every ray is insufficient.**
3. **A generic scalar log-concavity assumption on the angular pushforward is too weak unless it encodes the joint convex split.**
4. **Pure radial deformation can certify neighborhoods of solvable models but does not prevent angular phase separation in the full class.**

The right counterexample search is therefore not “find a bad scalar law.” It is “find a convex homogeneous split whose cone law is as close as possible to the bad bimodal relaxation.” Conversely, the right proof search is a theorem forbidding that approximation at the exact scale (3.1).

This is the concrete lesson from the failed routes; it is more restrictive than the previous generic statement that “geometry matters.”

**Outcome B22:** the literature's explicit failure mechanism and the fleet's exact relaxed witness point to the same missing ingredient: quantitative anti-bimodality forced by convex realizability.

## 6. B29 — ADD THE POINTS AT INFINITY: the `p -> infinity` boundary layer looks like an interface inequality

The reverse direction in Cordero-Erausquin--Rotem uses

\[
\phi_p(x)=\|x\|_K^p,
\qquad
\psi_p(x)=\|x\|_T^p,
\]

and sends the common degree `p` to infinity. In the angular formulation, (3.2) becomes

\[
\mathbb E[U(1-U)]
\ge \frac np\operatorname{Var}(U).
\tag{6.1}
\]

For a gauge-power pair, `U` is a logistic-type function of the ratio of the two gauges. Away from the angular interface where the gauges are comparable, `U` is exponentially close to `0` or `1`; the overlap term `U(1-U)` is concentrated in a boundary layer of width of order `1/p` around that interface.

Therefore the large-`p` form of (6.1) suggests the following **route**, not a claimed limit theorem:

- `Var(U)` measures the macroscopic mass split between the two angular phases;
- `p E[U(1-U)]` measures the first-order interface layer separating them;
- the desired inequality asks the interface layer to dominate `n` times the phase variance.

This is a much more geometric target than arbitrary gamma-transform log-concavity. It resembles a Cheeger/isoperimetric lower bound, but only for partitions generated by comparing two convex gauges, not for arbitrary subsets of the cone boundary. That restriction may be exactly what avoids importing a full general isoperimetric conjecture such as KLS, which is excluded from this lane.

The product/Beta equality model again gives the correct first-order constant, so any successful interface argument must be sharp on subspace/product decompositions.

This also clarifies why merely taking the limit is not a proof: at `p=infinity` the coefficient `p/(n+p)` tends to `1`, and the trivial bound `Var(U)<=m(1-m)` loses exactly the first-order `n/p` information needed at finite degree. The missing theorem is the **boundary-layer deficit**, not the limiting Bernoulli inequality.

**Outcome B29:** the point at infinity identifies a plausible geometric quantity to control in the recovery: interface mass between competing gauges, at first order in `1/p`.

## 7. Exactly one recovery choice

Section I requires one choice. I choose:

> **PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The technique to port is the sharp even weighted-Poincare/spherical decomposition from the rotationally invariant `(B)` theorem, but applied first to the smallest unresolved common-degree cone problem (3.3), not to the full conjecture at once.

The next bounded run should therefore ask whether the cone geometry of

\[
H=\phi+\psi\quad (n=3,p=2)
\]

supports a weighted angular Dirichlet form for `U=phi/H` whose sharp constant is `2/5`, with equality on quadratic/product splittings. If the direct cone operator is too weak, the run should locate the exact extra curvature term that rotational invariance supplied and test whether convexity of both `phi` and `psi` controls it.

The **next three Section-B moves** will be fresh on this current target:

- **B4 — PROVE SOMETHING WEAKER, COMPLETELY:** attack only the full `n=3,p=2` common-degree class first;
- **B14 — FIND THE GROUP ACTING:** quotient the cone operator by the natural linear/symmetry normalizations and isolate genuine nonquadratic modes;
- **B25 — COUNT THE SAME THING TWICE:** derive the angular variance once from cone integration and once from boundary/flux integration, looking for the missing positive curvature term.

No other recovery action is chosen in this run.

## 8. Capability honesty and the model/scheduler question

The current exposed native automation schema still has fields for task title, prompt, schedule/timing mode and enabled state, but **no model selector and no reasoning-effort selector**, and it does not guarantee an execution duration. Therefore GPT-6/maximum remains request text only. This invocation actually runs as **GPT-5.6 Sol**; the reasoning level is **UNVERIFIED**.

Changing that would require the platform/native scheduler to expose a model and reasoning-effort field (or an authorized runtime policy that pins them). A repository edit cannot do it.

The repository now contains two historically different scheduler-permission observations that must not be conflated: `NEW_METHODS_2026-09-16.md` records probes where P26/P01/P03 returned `You cannot modify this task`, while the newer compact `RESULTS.md` records that a P26 update later succeeded in a different exposed/authorized context and explicitly says the historical denial is not a universal current failure. I did not probe or modify P26 in this run, because HARD7-01 is not authorized to alter other schedules. If a task still returns the denial in a given context, the permitted workaround is to use the task's authorized owner/workspace/native context or platform support; **not** to bypass the permission and **not** to create a duplicate schedule.

## 9. Stuck counter and next obligation

This is **STUCK1 recovery 1** on the current weak-`(B)` target. It does not reset the source metric merely because the route changed. The target remains OPEN/PARTIAL at `D_B=2`.

If subsequent runs again accumulate three unchanged iterations or the identical remaining obligation, Section I permits one second recovery cycle. A third stuck episode on this hard target requires a handoff and rotation to a fresh admissible source.

## 10. Ledger delta and persistence

```text
ledger_delta:
  worker: HARD7-01
  target: weak (B)-conjecture for all even log-concave measures
  canonical_claim: operations/claims/B-WEAK-EVEN-LOGCONCAVE.md
  metric: D_B
  before: 2
  after: 2
  movement: no movement
  status: PARTIAL / source OPEN / STUCK1 recovery 1
  methods_this_run: [B18, B22, B29]
  recovery_choice: port technique from nearest solved problem
  next_methods: [B4, B14, B25]
  shared_root_write: none
```

No checker/artifact is created in this invocation because Section I requires a thinking-only run and I make no new finite exhaustive claim. The earlier B20 exact self-check remains archived in the preceding report; it is not rerun merely to manufacture another certificate.
