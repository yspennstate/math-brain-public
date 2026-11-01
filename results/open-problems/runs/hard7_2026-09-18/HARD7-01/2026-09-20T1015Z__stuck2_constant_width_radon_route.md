Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` (**NO MOVEMENT**). This is the required **STUCK2 thinking run**. Methods tried: **B3 / B12 / B23**.

# HARD7-01 — STUCK2: freeze the central symmetral and port the normed Blaschke–Lebesgue/Radon route

**Status:** `PARTIAL / SOURCE OPEN / STUCK2 THINKING-ONLY`.

Per Section I of the owner directive, this invocation does **not** register a new theorem-sized claim, does not manufacture a new checker, and does not call the symmetric Mahler conjecture closed. Its purpose is to identify a genuinely different route after the source metric and remaining source obligation have failed to move for the required number of runs.

## 1. Continuity, ownership, and required reads

The canonical claim remains

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`,

owned exclusively by `HARD7-01`. The external source target is still

\[
 |K|\,|K^\circ|\ge \frac{4^n}{n!}
 \qquad(K=-K\subset\mathbb R^n),
\]

and the frozen source metric is still

`d_sym = 3`.

This run resumed from the newest checkpoint

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T0940Z__mahler_DF6_pyramid_quadrilateral.md`,

which explicitly triggered STUCK2 and identified the first still-unproved pyramidal case as the planar pentagon inequality `(P5)` below.

At the start of the run I reread/reconciled the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- root `POSTED.md` and `RESULTS.md`,
- the canonical Mahler claim and the newest HARD7-01 checkpoints,
- the newest relevant neighbouring HARD7-05 checkpoint found in the repository (`2026-09-19T2250Z__triple_orthant_trace_164800.md`),
- repository/intake alias searches for `Mahler`, `symmetric Mahler`, `volume product`, `reverse Santalo`, and the present difference-body obstruction.

No competing canonical owner, posted equivalent result, or source-level resolution was found. This is a bounded repository/literature check, not a worldwide priority certificate.

## 2. The exact blocker required by Section I

The simplest source-relevant obstruction reached by the current reduction is

\[
\boxed{
 (|B-B|+2|B|)\,|(B-B)^\circ|\ge 12
 \quad\text{for every convex pentagon }B\subset\mathbb R^2.
}
\tag{P5}
\]

The preceding run proved the same inequality for every triangle and every convex quadrilateral. It also found, only as route-finding evidence, that the naive operation “delete one pentagon ear monotonically until a quadrilateral remains” is not monotone in generic floating-point tests. Those samples were not and are not promoted to a theorem.

## 3. Routes already tried and the precise reason each stopped

1. **Higher-dimensional admissible-shadow incidence debt.** It gave necessary local-minimizer inequalities, but no volume lower bound strong enough to move `d_sym`.
2. **Antipodal circuit/full-spark quotient.** It sharpened the local combinatorics, but an equality-pattern configuration survived.
3. **Cube-section realizability.** The hoped-for contradiction was false: an exact rational `V=12,F=22,I=98` centrally symmetric four-polytope realizes the entire previous incidence boundary.
4. **Coordinate-sensitive radial KKT.** It successfully eliminated that explicit witness as a local minimum, but did not control the whole continuous twelve-vertex family.
5. **Gale/box-spline reformulation.** It reduced the generic `V=12` family to one aggregate bivariate inequality, but a tempting termwise inequality is false.
6. **Six-vertex-facet reduction.** It reduced the first local-minimizer frontier to the three-dimensional difference-body inequality `(DF6)`.
7. **Pyramidal dimension drop.** It reduced pyramidal `(DF6)` exactly to the planar inequality
   \[
   (|B-B|+2|B|)|(B-B)^\circ|\ge12.
   \tag{DF2}
   \]
   The triangle and complete quadrilateral families are now done; the pentagon is the first unproved polygonal case.
8. **Naive pentagon ear deletion.** The route is not monotonically compatible with `(DF2)` even in generic exploratory examples, so repeating it with more local lemmas would violate the stuck rule.

The common missing feature is now clear: the successful earlier methods mainly constrain combinatorics or one chosen deformation. None of them first optimizes over **all bodies with the same difference body**.

## 4. Fresh route search: fix the central symmetral instead of the pentagon

Set

\[
M:=\frac12(B-B).
\]

Then the exact algebra already implicit in the previous checkpoint is

\[
|B-B|=4|M|,\qquad |(B-B)^\circ|=\frac14|M^\circ|,
\]

so `(DF2)` is equivalent to

\[
\Bigl(|M|+\frac12|B|\Bigr)|M^\circ|\ge12.
\tag{4.1}
\]

The key conceptual change is that fixing `M` fixes the relative norm of `B`: `B` is a body of constant Minkowski width two in the norm whose unit disk is `M`. Thus for fixed `M`, the only variable in (4.1) is `|B|`.

A fresh literature check on 20 September 2026 found a directly relevant solved extremal problem:

- Z. Lángi, *On a normed version of a Rogers–Shephard type problem*, Israel J. Math. 212 (2016), 203–217, DOI `10.1007/s11856-016-1284-y`, repository copy `https://real.mtak.hu/167370/`.
- H. Martini and Z. Mustafaev, *On Reuleaux triangles in Minkowski planes*, Beiträge Algebra Geom. 48 (2007), 225–235, `https://eudml.org/doc/226148`.
- M. Spirova, *On a theorem of G. D. Chakerian*, Contributions to Discrete Mathematics 5 (2010), DOI `10.55016/ojs/cdm.v5i1.62034`.
- Z. Lángi, *Variants of a theorem of Macbeath in finite-dimensional normed spaces*, Mathematika 72 (2026), e70078, DOI `10.1112/mtk.70078`.
- K. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies—lower estimates with stability*, Studia Sci. Math. Hungar. 50 (2013), 159–198, DOI `10.1556/SScMath.50.2013.2.1235`.

The 2016/2007 sources record the normed Blaschke–Lebesgue/Chakerian mechanism: among plane convex bodies with fixed central symmetral `M`, minimum area is attained by a Reuleaux triangle in the norm of `M`. In the notation used there, if `H` is a largest-area affine-regular hexagon inscribed in `M`, the minimum-area formula is

\[
 |B|_{\min}=2|M|-\frac43|H|.
\tag{4.2}
\]

This is an existing literature theorem, not a HARD7-01 claim.

Substituting the literature bound (4.2) into the already-existing identity (4.1) shows what a successful port would have to prove about the *symmetric* body `M` alone:

\[
\boxed{
  (3|M|-|H|)|M^\circ|\ge18,
  \qquad H=\text{a largest-area affine-regular hexagon in }M.
}
\tag{C}
\]

Equivalently,

\[
\Bigl(|M|-\frac13|H|\Bigr)|M^\circ|\ge6.
\tag{C'}
\]

I am recording `(C)`/`(C')` as the **candidate recovery target produced by the stuck analysis**, not as a newly proved theorem in this thinking-only run.

### Why this route is materially different

The old pentagon route tried to control five moving vertices of `B`. The new route first integrates out *all* asymmetry of `B` at fixed `M` using a solved constant-width extremal theorem. If `(C)` holds for every origin-symmetric planar `M`, then `(DF2)` follows for **every plane convex body**, not merely pentagons. Thus the route deliberately strengthens the immediate obligation in order to remove the awkward polygon parameterization.

### A strong endpoint sanity check that should be formalized next, not claimed here

The same literature contains an especially suggestive Radon-norm calculation. Let `P` be a largest-area parallelogram inscribed in `M`. For a Radon norm, the published identities/inequalities give

\[
 |M^\circ|=\frac{4|M|}{|P|^2},
 \qquad \frac{2|M|}{|P|}\ge3,
\]

and every affine-regular hexagon `H` contains a parallelogram of area `2|H|/3`, hence `|P|\ge2|H|/3`. Formally combining those established ingredients gives

\[
 (3|M|-|H|)|M^\circ|
 =4\frac{|M|}{|P|}
   \left(3\frac{|M|}{|P|}-\frac{|H|}{|P|}\right)
 \ge 4\cdot\frac32\cdot\left(\frac92-\frac32\right)=18.
\tag{4.3}
\]

Because this invocation is the mandated STUCK2 thinking run, (4.3) is **not promoted here to a new track theorem** and no certificate is manufactured for it. Its value is diagnostic: it says the proposed one-body target `(C)` is already aligned with the exact extremal constants on the Radon locus. The non-Radon-to-Radon reduction is therefore the precise missing bridge, not the endpoint estimate.

The 2026 Lángi paper is unusually relevant to that bridge: its planar Holmes–Thompson extremal proof uses vertex/shadow deformations to reduce minimizers of a polar-area/maximal-inscribed-parallelogram functional to Radon curves, then to affine-regular polygons. That is much closer in shape to `(C)` than any route previously tried on HARD7-01.

## 5. Why the standard separate inequalities are not enough

The point of `(C)` is that it couples three quantities. Applying planar symmetric Mahler and the trivial `|H|\le|M|` separately gives only

\[
(3|M|-|H|)|M^\circ|\ge2|M||M^\circ|\ge16,
\]

short of `18`.

Likewise, Eggleston’s sharp inequality

\[
 |B|\,\left|\left(\frac{B-B}{2}\right)^\circ\right|\ge6
\]

is an endpoint theorem for the asymmetric part but, when combined separately with symmetric Mahler, does not recover the missing coupled two units. The recovery therefore needs a **single deformation or stability statement coupling the hexagon defect to polar area**, not another independent lower bound.

This also explains why finite pentagon sampling would have low value: the bottleneck is now an affine-invariant variational statement on `M`, not evidence about isolated pentagons.

## 6. Section-B outcomes

### B3 — PROVE SOMETHING STRONGER

**Promising.** Replace pentagon-only `(P5)` by the stronger all-planar `(DF2)`. Fixing the central symmetral turns that stronger problem into the one-body candidate `(C)`. The stronger formulation is structurally easier because it admits the full constant-width machinery.

### B12 — FIND WHAT IS CONSERVED

**Strongest move of the run.** Under all deformations of `B` preserving `M=(B-B)/2`, both `|M|` and `|M^\circ|` are conserved. The original two-body-looking functional then asks only for the least possible area of a constant-width body, which is a solved normed Blaschke–Lebesgue problem.

### B23 — DO WHAT THE PROPOSER DID NOT EXPECT

**Promising.** Do not parameterize a pentagon at all. Replace it by the whole fixed-central-symmetral constant-width class, minimize there by Chakerian’s theorem, and attack the residual symmetric functional using Radon-curve methods. This is the opposite of the previous increasingly fine polygonal case split.

No checker was built because the purpose of this STUCK2 run is route selection rather than certifying another unchanged finite quantity.

## 7. Required five-part STUCK2 report

### (a) Exact blocking statement

\[
\boxed{
 (|B-B|+2|B|)|(B-B)^\circ|\ge12
 \quad\text{for every convex pentagon }B\subset\mathbb R^2.
}
\]

### (b) Every route tried and why it failed

The complete route list is in Section 3. In short: combinatorial shadow/circuit constraints do not control volume; exact cube-section realizability kills the hoped-for combinatorial contradiction; one radial KKT direction is not uniform; the box-spline termwise shortcut is false; and naive pentagon ear deletion is not monotone. The successful dimension-drop only moves the obstruction into `(P5)`.

### (c) What a proof must contain that no route so far contains

It must couple the loss of affine-regular-hexagon area inside the central symmetral to a compensating gain in polar area. In the new language this is exactly the missing global step behind `(C)`: a deformation principle showing that a minimizer of

\[
\Psi(M):=(3|M|-H_6(M))|M^\circ|
\]

(where `H_6(M)` is the maximum affine-regular-hexagon area) may be reduced to a Radon curve or to an explicitly controlled boundary body without increasing `\Psi`. None of the previous HARD7-01 arguments controls the variation of `H_6(M)` simultaneously with polar area.

### (d) Simplest special case still unproved

The source-facing simplest special case is still the full convex-pentagon `(P5)`. In the new coordinates, a generic pentagon produces a centrally symmetric decagonal central symmetral `M`; therefore a practical first recovery test is `(C)` on centrally symmetric decagons, with all continuous parameters retained. A finite sample or one combinatorial type is not enough.

### (e) Nearest solved problem and the ingredient it has that this problem lacks

The nearest solved problems are the normed Blaschke–Lebesgue/Chakerian fixed-symmetral minimization (Lángi 2016; Martini–Mustafaev 2007) and Lángi’s 2026 Holmes–Thompson inscribed-polytope extremal problem. They have two ingredients the previous HARD7-01 route lacked:

1. **optimize over the entire fixed-relative-norm class first**, replacing the asymmetric body by a Reuleaux extremizer; and
2. **Radonization by deformation**, reducing an affine-invariant polar-area functional to Radon curves before classifying the remaining extremizers.

Our new residual functional additionally contains the nonsmooth term `H_6(M)`. Controlling that term under the Radonizing deformation is the exact new obligation.

## 8. Exactly one Section-I recovery choice

**Chosen action: PORT THE TECHNIQUE FROM (e).**

The next HARD7-01 recovery invocation should not return to pentagon ear deletion. It should take the specific deformation used in the planar part of Lángi 2016/2026, write the one-sided variation of

\[
\Psi(M)=(3|M|-H_6(M))|M^\circ|,
\]

and determine whether the deformation can be chosen so that `\Psi` does not increase until `M` is Radon (or lands on a controlled polygonal boundary). If yes, the Radon endpoint calculation (4.3) becomes the closure mechanism for the all-planar `(DF2)` route. If no, the first sign-indefinite term in `H_6(M)` is the precise obstruction to archive and the track should use the remaining allowed recovery to attack that obstruction directly.

Fresh Section-B moves reserved for that recovery: **B8 / B15 / B27**.

Because STUCK1 and STUCK2 are now both consumed for this Mahler target, a later third stuck episode on the same target must trigger handoff/rotation under Section I rather than another recovery cycle.

## 9. Fresh literature/current-status check

Queries on 20 September 2026 included combinations of `difference body Mahler planar polar`, `constant width normed plane Chakerian`, `largest area affine-regular hexagon polar`, `Holmes-Thompson inscribed parallelogram`, and `Radon curve affine regular hexagon`. They located the sources above and did **not** locate a published statement of `(P5)`, `(DF2)`, or `(C)` in the exact form needed here. That negative search is bounded and does not establish novelty.

The full four-dimensional symmetric Mahler conjecture therefore remains labelled **OPEN** in this track; `d_sym` does not move.

## 10. Runtime / scheduler capability honesty

The automation interface exposed to this runtime still provides prompt/schedule/enabled controls but **no model selector, no reasoning-effort selector, no authenticated runtime-model telemetry field, and no guaranteed run-duration field**. Therefore `GPT-6 / maximum` remains only a prompt request. Actual conversation runtime is `GPT-5.6 Sol`; reasoning level is `UNVERIFIED`.

The repository records the historical P26 error `You cannot modify this task`, while a later authorized context successfully updated P26. The valid workaround remains an authorized owning account/workspace/interface or platform support. It is not permission bypass and not creation of a duplicate schedule. No schedule was modified in this run.

## 11. Final label and ledger delta

**`PARTIAL / SOURCE OPEN / STUCK2 THINKING COMPLETE`.**

```text
ledger_delta:
  track: HARD7-01
  source_target: MAHLER-SYMMETRIC-VOLUME-PRODUCT
  owner: HARD7-01
  status: PARTIAL
  stuck_state: STUCK2_THINKING_COMPLETE
  source_metric: d_sym
  before: 3
  after: 3
  movement: NO
  methods: [B3, B12, B23]
  exact_blocker: (|B-B|+2|B|)|(B-B)^circ| >= 12 for every convex pentagon B
  chosen_recovery: port fixed-symmetral Chakerian + Radonization technique
  candidate_reduction: (3|M|-H_6(M))|M^circ| >= 18
  next_methods: [B8, B15, B27]
  finite_checker_built: false
  closure: false
```
