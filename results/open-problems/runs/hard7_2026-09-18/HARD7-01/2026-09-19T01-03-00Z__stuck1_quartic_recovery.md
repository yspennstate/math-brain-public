Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run is not verified as GPT-6 at maximum. **No movement in the frozen metric:** `B=infinity -> B=infinity`. Section-I thinking run; methods tried: **B22, B23, B29**.

# HARD7-01 run 5 — STUCK1 obstruction map and quartic-product recovery choice

Status: **PARTIAL / STUCK1** for the full even-log-concave dimensional Brunn--Minkowski conjecture. This is the mandatory Section-I thinking-only run triggered by three consecutive unchanged runs. It makes **no new theorem claim** and deliberately does not manufacture a checker. Its purpose is to identify exactly what failed, isolate the smallest source-valid problem not already covered by the preceding routes, compare it with the nearest solved literature, and choose one recovery action.

## 1. Continuity, ownership, repository state, and current source status

The canonical claim remains

`operations/claims/GZ-DIMBM-EVEN-LOGCONCAVE.md`,

owned exclusively by HARD7-01. The exact source target is

\[
\mu((1-\lambda)K+\lambda L)^{1/n}
\ge (1-\lambda)\mu(K)^{1/n}+\lambda\mu(L)^{1/n}
\tag{DBM}
\]

for every integer `n>=1`, every even log-concave probability measure `mu` on `R^n`, all nonempty centrally symmetric convex sets `K,L`, and all `lambda in [0,1]`.

At run start I reread the controlling HARD7/new-methods files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, and all four preceding HARD7-01 reports. Repository-wide searches for `dimensional Brunn-Minkowski`, `Gardner-Zvavitch`, and `log-concave` still return HARD7-01 as the owner of this exact target and no competing equivalent claim. The intake corpus is too large for the connector to return as one untruncated semantic document; as in the previous runs, the intake/ownership check was done by repository-wide exact-name and alias search rather than pretending to have reread a monolithic truncated JSONL object.

A fresh bounded literature check on 2026-09-19 found no full resolution of (DBM) in the exact even-log-concave/symmetric-body scope. The most relevant current sources for this run are:

1. Kai-Wen Yang, *A uniform bound in the dimensional Brunn--Minkowski inequality for even log-concave measures*, arXiv:2607.10104, submitted 11 July 2026. Its statement is the exact class above and it proves an exponent `p_n >= c/(n^2 log n)`, while explicitly recording the `1/n` conjecture as open for general even log-concave measures in `n>=3`.
2. Alexandros Eskenazis, Apostolos Giannopoulos, Natalia Tziotziou, *Functional perimeter and the dimensional Brunn--Minkowski inequality for log-concave measures*, arXiv:2605.02747, 4 May 2026. It proves `c/(n^3 log n)` and isolates a geometric obstruction in obtaining large convex regions on which the gradient of the log-density is controlled.
3. Gautam Aishwarya and Liran Rotem, *New Brunn--Minkowski and functional inequalities via convexity of entropy*, Adv. Math. 490 (2026), 110841. For a `p`-homogeneous convex potential it gives the exponent `(p-1)/(pn)` on centered star bodies.
4. Ge Xiong and Kai-Wen Yang, *The Brunn-Minkowski inequality for the generalized Gaussian distribution*, arXiv:2605.24472, submitted 23 May 2026. Section 5 extends its lower-bound mechanism to general log-concave measures with `p`-homogeneous convex potentials, improving the elementary `(p-1)/(pn)` lower bound for convex bodies containing the origin, but it does not state the full `1/n` conclusion for arbitrary such potentials.
5. Dario Cordero-Erausquin and Liran Rotem, *Improved log-concavity for rotationally invariant measures of symmetric convex sets*, Ann. Probab. 51 (2023), 987--1003, proves the full Gardner--Zvavitch inequality for rotationally invariant log-concave measures using sharp weighted Poincare inequalities.
6. Galyna Livshyts, Arnaud Marsiglietti, Piotr Nayar, Artem Zvavitch, *On the Brunn-Minkowski inequality for general measures with applications to new isoperimetric-type inequalities*, Trans. AMS 369 (2017), proves the full source exponent in dimension two and for the stated unconditional measure/body classes.

This is a bounded current-status search, not a worldwide novelty certificate. The previous HARD7-01 auxiliary observations remain novelty **UNVERIFIED**.

## 2. Frozen metric and why Section I applies

The admission metric remains

`B = largest low-dimensional block count for which (DBM) is proved at the source exponent 1/N for every common block-product instance built from 1D/2D factors`.

Run 1 moved `B=1` to all finite block counts, recorded as `B=infinity`. Runs 2, 3, and 4 were all unchanged. Therefore this run is formally STUCK under Section I and must not add another auxiliary theorem.

Before this run:

\[
B=\infty.
\]

After this run:

\[
\boxed{B=\infty.}
\]

No movement.

## 3. Section I(a): the exact blocking statement

The source-level obstruction is already present in the first open dimension. What remains is to prove or refute

\[
\boxed{
\mu((1-\lambda)K+\lambda L)^{1/3}
\ge (1-\lambda)\mu(K)^{1/3}+\lambda\mu(L)^{1/3}
}
\tag{S3}
\]

for every even log-concave probability measure `mu` on `R^3`, every nonempty centrally symmetric convex `K,L`, and every `lambda in [0,1]`.

The previous runs do not reach (S3) unless extra product, unconditional, radial, homothetic, or perturbative structure is imposed.

## 4. Section I(b): every route tried and the precise failure

### Run 1 — B2/B5/B11: product tensorization

The run tried to refute the conjecture by multiplying low-dimensional hard instances. Instead it obtained harmonic tensorization: if each factor satisfies a power-concavity inequality with exponent `p_j`, common Cartesian product bodies inherit the harmonic exponent. Using the known 1D/2D source exponent, all finite products of 1D/2D factors are covered at exponent `1/N`.

**Why it stops:** generic symmetric convex bodies do not share the product decomposition of the measure. The theorem removes reducible product geometry but says nothing about irreducible cross-block support functions.

### Run 2 — B15/B18/B24: transverse covariance Hessian

The run rewrote the second variation of the sign-equivalent defect under cross-block bilinear density perturbations and found an exact negative transverse Hessian direction off the product manifold.

**Why it stops:** the useful cross term is an indefinite quadratic form. At the flat equality base it is not a convex potential, hence it leaves the source class. Adding enough positive curvature to make the perturbation convex removes the exact equality base and creates a positive zeroth-order gap that the negative Hessian calculation alone cannot overcome.

### Run 3 — B4/B6/B20: valid convex tilts of a homothetic equality

The run repaired the source-validity defect by starting at a Lebesgue/uniform homothetic equality and tilting by an even convex potential. It found the first derivative is nonnegative, with a quantitative positive opening for strongly convex tilts.

**Why it stops:** the simplest admissible path away from an exact equality moves in the *correct* direction. It therefore cannot turn the run-2 negative formal Hessian into a counterexample.

### Run 4 — B1/B3/B26: simultaneous body motion and the flat-core escape

The run changed category to mixed-volume first variation. It found that at a homothetic Lebesgue equality the first-order body-shape contribution cancels exactly, so arbitrary first-order body motion cannot cancel the positive convex-tilt contribution. Equality of the remaining potential term forces a flat potential on the swept homothetic region. The simplest finite-amplitude radial boundary-layer deformation in that flat-core case also moved in the correct direction.

**Why it stops:** the remaining geometry is genuinely nonhomothetic and angular. Another tangent lemma at the homothetic equality manifold would be more of the same route and would violate the Section-I instruction.

### This run — B22: read the failures, not the successes

The recent literature confirms that the same bottleneck appears in a different language. Yang's 2026 proof uses the local-to-global variation formalism and the Kolesnikov--Livshyts sufficient energy inequality. In its smooth form, a source-exponent proof would need to force the local concavity power all the way to `1/n`, whereas the current general estimate loses powers of `n`. Eskenazis--Giannopoulos--Tziotziou identify a concrete obstruction: low-gradient regions of a log-concave potential need not be convex, while the restricted Poincare step wants convexity. Yang bypasses that particular loss by applying Poincare on the full support first, gaining a factor `n`, but still stops at order `1/(n^2 log n)` rather than `1/n`.

A second classical route says that log-Brunn--Minkowski would imply (DBM). That is not a closure route in dimension three: the unrestricted log-Brunn--Minkowski conjecture is itself open there. Porting the two-dimensional proof verbatim therefore exchanges the present hard statement for another famous hard statement.

**Failure learned from B22:** the missing ingredient is not a bookkeeping improvement of the existing exponent. Either one finds a sharp `1/n` coercive inequality for the local PDE/weighted-boundary form, or one finds additional geometry in a restricted source-valid class that removes the angular loss.

### This run — B23: assume the opposite answer and ask what a counterexample must look like

Assume (DBM) is false. The preceding results and the published solved classes constrain a first counterexample sharply:

- it must occur in dimension at least three;
- it cannot be explained by the Gaussian class or a rotationally invariant log-concave measure;
- it cannot have both measure and bodies inside the known unconditional theorem;
- it cannot be a common Cartesian product-body instance covered by run 1;
- the homothetic equality manifold is not an easy exit, because source-valid convex tilts and simultaneous first-order body motion open it with the nonnegative sign found in runs 3--4;
- therefore the first plausible failure must use **nonhomothetic angular geometry** of the bodies, and either a nonradial density or a nonunconditional body direction that couples to that density.

This narrows the search toward the smallest non-Gaussian, nonrotational measure with an explicit analytic structure, rather than toward more elaborate fully generic measures.

### This run — B29: add the boundary and inspect the layer-cake compactification

A natural boundary point of the log-concave class is a uniform density on a symmetric convex support `S`. That boundary is not a promising source of a counterexample by itself. For a uniform measure on `S`, the elementary inclusion

\[
(1-\lambda)(K\cap S)+\lambda(L\cap S)
\subseteq ((1-\lambda)K+\lambda L)\cap S
\]

combined with the classical Brunn--Minkowski inequality gives the desired `1/n` inequality. This is a classical-level observation, not a novelty claim.

The first genuinely difficult phenomenon therefore appears when the density has **multiple nested convex levels**. After shifting an even convex potential `V` so that `\min V=0`, write

\[
e^{-V(x)}=\int_{V(x)}^\infty e^{-s}\,ds,
\qquad C_s=\{x:V(x)\le s\}.
\]

Then

\[
\mu(K)\propto \int_0^\infty e^{-s}|K\cap C_s|\,ds.
\]

At each fixed level, the same intersection argument gives the correct root-volume inequality. But integrating those levelwise inequalities does **not** automatically preserve the desired root power. If

\[
x(s)=|K\cap C_s|^{1/n},\qquad y(s)=|L\cap C_s|^{1/n},
\]

the naive step would require a reverse form of the `L^n` triangle inequality. Even for decreasing nonnegative profiles this is false. For example, at `n=2` and equal weights, take

\[
x=\mathbf 1_{[0,1]},\qquad y=\mathbf 1_{[0,2]}.
\]

Then

\[
\left\|\frac{x+y}{2}\right\|_2=\frac{\sqrt5}{2}
<\frac{1+\sqrt2}{2}
=\frac{\|x\|_2+\|y\|_2}{2},
\]

with the strict inequality following from `sqrt(5)<1+sqrt(2)`. Thus a proof cannot merely establish the source inequality independently on every density level and integrate it.

Convexity of `V` gives more than same-level nesting: if `C_s={V<=s}`, then

\[
(1-\lambda)C_s+\lambda C_t\subseteq C_{(1-\lambda)s+\lambda t}.
\]

Consequently, a successful layer-cake proof would have to exploit this **cross-level coupling**, not only pointwise-in-`s` Brunn--Minkowski. I did not obtain such a gluing inequality in this thinking run. The failed `L^n` step explains precisely why the obvious compactification route stalls.

## 5. Section I(c): what a proof must contain that no route so far contains

There are now two equivalent-looking formulations of the missing mechanism.

### Local/PDE form

For smooth positive even density `e^{-V}` and smooth symmetric convex `K`, the current variation machinery reduces global concavity to a local concavity power. A route to the exact source exponent needs a **sharp coercive estimate at scale `1/n`** for the relevant weighted Neumann/PDE energy, uniformly over all admissible even body variations. Schematically, one needs to close the gap between the known general lower bounds and

\[
\mathcal E_{V,K}(u)
:=\frac1{\mu(K)}\int_K
\left(\|\nabla^2u\|_{\mathrm{HS}}^2
+\langle \nabla^2V\nabla u,\nabla u\rangle\right)d\mu
\ \ge\ \frac1n
\tag{E}
\]

in the source-relevant normalized class used by the local-to-global theorem. The exact hypotheses on `u` must be inherited from that theorem when this route is executed; (E) here records the missing scale, not a new theorem assertion.

### Level-set form

Alternatively, one needs an inequality that couples **different** sublevel sets `C_s,C_t` strongly enough to beat the wrong-direction `L^n` Minkowski inequality after layer-cake integration. Same-level Brunn--Minkowski alone is provably insufficient as a formal gluing principle.

Both formulations demand control of nonhomothetic angular modes. Product tensorization, homothetic first variations, and radial boundary layers do not supply it.

## 6. Section I(d): simplest source-valid special case still unproved by the recovered literature

The cleanest next case I found is dimension three with the explicit product quartic measure

\[
d\mu_4(x)=Z^{-1}\exp\!\left[-\frac{x_1^4+x_2^4+x_3^4}{4}\right]dx,
\tag{Q}
\]

and **arbitrary centrally symmetric convex** `K,L subset R^3`. The restricted target is

\[
\mu_4((1-\lambda)K+\lambda L)^{1/3}
\ge(1-\lambda)\mu_4(K)^{1/3}+\lambda\mu_4(L)^{1/3}.
\tag{Q3}
\]

Why this is the right simplest case:

- `mu_4` is even, log-concave, explicit, smooth enough for the local machinery, and a product measure;
- it is not rotationally invariant, so the Cordero-Erausquin--Rotem theorem does not close (Q3);
- the exact unconditional theorem closes (Q3) when the bodies are unconditional, but (Q3) asks for arbitrary centrally symmetric bodies;
- run 1 closes the case of product bodies, but not arbitrary bodies;
- the potential is 4-homogeneous, so the 2026 Aishwarya--Rotem and Xiong--Yang machinery supplies explicit sub-target exponent bounds and therefore a concrete analytic baseline rather than a featureless generic measure.

Aishwarya--Rotem directly gives exponent `(4-1)/(4*3)=1/4` on the larger class of centered star bodies. Xiong--Yang Theorem 5.1 gives a stronger explicit lower bound for convex bodies containing the origin for general 4-homogeneous convex potentials. Before the next run treats a numerical exponent gap as a sub-metric, it must evaluate and freeze the exact `n=3,p=4` Theorem-5.1 constant from the primary formula and recheck later literature. This report does **not** claim that `1/4` is the best known exponent. The bounded search found no source claiming the exact `1/3` result for (Q) with arbitrary symmetric bodies.

## 7. Section I(e): nearest solved problem and the ingredient it has

The nearest solved class with the **same arbitrary-symmetric-body quantifier in all dimensions** is the rotationally invariant log-concave case of Cordero-Erausquin--Rotem (2023); Gaussian measure is the most famous member and was solved earlier by Eskenazis--Moschidis.

The ingredient unavailable for (Q) is radial symmetry. In the rotationally invariant case, sharp weighted Poincare inequalities separate radial and tangential behavior and close the local concavity estimate at the source exponent. For the quartic product potential `V=(x_1^4+x_2^4+x_3^4)/4`, the angular operator is anisotropic: the radial/tangential decomposition no longer diagonalizes the relevant weighted energy, and a nonunconditional body boundary couples to that anisotropy.

The other nearby solved problem is the full two-dimensional even-log-concave theorem of Livshyts--Marsiglietti--Nayar--Zvavitch. Its route uses the planar log-Brunn--Minkowski theorem (plus the transfer to even log-concave measures). The exact ingredient it has and dimension three lacks is precisely the unrestricted planar log-Brunn--Minkowski theorem; importing that proof wholesale is therefore not an available three-dimensional closure.

## 8. Exactly one Section-I recovery choice

**Recovery choice: PROVE THE SIMPLEST UNPROVED SPECIAL CASE FROM (d).**

The next HARD7-01 run stays on the existing canonical source claim but narrows its recovery attempt to (Q3): the 3D quartic product measure with arbitrary centrally symmetric convex bodies. This is not a new ownership claim and does not change the frozen track metric `B`; it is the first Section-I recovery on the current source.

The next run must first freeze the strongest published exponent baseline for (Q) by evaluating the exact Xiong--Yang Theorem 5.1 formula at `(n,p)=(3,4)`. Then it should attack the missing `1/3` endpoint, not merely produce another general checker.

The next three unused Section-B moves are:

- **B8 — discretize:** reduce the body side first to centrally symmetric polytopes/support functions with finitely many normal directions, preserving the exact measure and source exponent;
- **B17 — look for the numbers somewhere else:** compare the exact `(n,p)=(3,4)` local-energy constant from Xiong--Yang/Aishwarya--Rotem with the `1/3` target and identify where the gap is created;
- **B30 — one scale / one direction at a time:** isolate the first nonunconditional angular support-function mode against the quartic product potential instead of perturbing every body direction at once.

If this recovery makes no source-relevant movement and the same obligation persists into a second Section-I episode, the track must record STUCK2. A third Section-I exhaustion on this source forces a handoff/rotation under the owner rule.

## 9. Validation / artifacts

This was explicitly a Section-I **thinking run with no new theorem-sized or finite exhaustive claim**. Therefore no checker was created and no `artifacts/` file was manufactured. The only exact numerical comparison used above, `sqrt(5)<1+sqrt(2)`, is proved directly by squaring: `5<3+2sqrt(2)` is equivalent to `1<sqrt(2)`.

The report is the checkpoint. No root ledger, peer track, email, Drive file, or scheduler was modified.

## 10. Capability and scheduler honesty

Actual runtime model available to this report is **GPT-5.6 Sol**. Reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. This run therefore does **not** claim GPT-6 at maximum.

The automation interface exposed in this runtime still provides title, prompt, schedule/timing mode and enabled state, but **no model selector, no reasoning-effort selector and no guaranteed execution duration**. GPT-6/maximum can only be requested in prompt text with the current interface. Changing that requires a platform/runtime surface that actually exposes those controls; a repository edit cannot do it.

The repository records a historical P26 edit failure (`You cannot modify this task`) in one native context and a later successful P26 update from another authorized context. The legitimate workaround is an authorized account/workspace/task context that owns the task, or platform support. Creating a duplicate schedule, bypassing ownership, or treating repository text as a scheduler control is not a workaround. This run did not modify any schedule, as required.

## 11. ledger_delta

```yaml
track: HARD7-01
canonical_claim: GZ-DIMBM-EVEN-LOGCONCAVE
source_status: OPEN
research_status: PARTIAL
run_kind: SECTION_I_STUCK1_THINKING
metric: maximum low-dimensional block count B covered at source exponent for all common block-product instances
metric_before: infinity
metric_after: infinity
movement: no movement
unchanged_streak_entering: 3
section_I_recovery: 1
methods_this_run: [B22, B23, B29]
new_theorem_claims: 0
finite_checkers_added: 0
recovery_choice: prove_simplest_unproved_special_case
recovery_target: n=3 quartic product measure exp(-(x1^4+x2^4+x3^4)/4), arbitrary centrally symmetric convex K,L, source exponent 1/3
next_methods: [B8, B17, B30]
novelty: UNVERIFIED
next_obligation: freeze exact Xiong-Yang Theorem 5.1 baseline at n=3,p=4, then attack the 1/3 endpoint for the quartic recovery class
```
