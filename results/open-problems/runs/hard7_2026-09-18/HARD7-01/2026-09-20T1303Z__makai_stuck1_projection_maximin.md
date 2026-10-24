Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_Makai: 2 -> 2` (**NO MOVEMENT; STUCK1 thinking/recovery run, no new theorem claim**). Methods: **B12 / B21 / B22**.

# HARD7-01 — STUCK1: the one-projection route is blocked exactly by a Busemann–Petty maximin problem; next recovery will port planar Eggleston stability

**Status:** `PARTIAL / SOURCE OPEN / CLAIMED / STUCK1`.

This invocation is deliberately a Section-I thinking run. The preceding Makai run was the third consecutive run with unchanged frozen source metric, so I do **not** manufacture another restricted theorem/checker merely to show activity. Instead I isolate the exact obstruction in the strongest projection route found so far, identify the closest literature, and choose exactly one recovery action for the next active iteration.

## 1. Continuity, exclusions, ownership, and required reads

I resumed the existing exclusive claim

`operations/claims/MAKAI-POLAR-DIFFERENCE-BODY.md`

owned by `HARD7-01`; no alias was minted and no other owner's file was modified.

At run start I reread/reconciled the required control and fleet material:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the current Makai claim;
- newest own checkpoint `runs/hard7_2026-09-18/HARD7-01/2026-09-20T1212Z__makai_affine_circuits_cube_sections.md`;
- the newest surfaced neighboring HARD7 Gaussian/probability state (HARD7-05 remains on integrated-fBM persistence, not this convex-geometric target);
- repository/intake searches for `Makai`, `difference body`, `polar difference body`, `Makai Jr`, and the source constants.

A literal byte-for-byte scan of every duplicated/archived intake JSONL is not exposed as one bounded connector operation, so I do not claim one. I did query the intake/repository index across the canonical aliases and found no competing owner, release, posting, or source-resolution record. `POSTED.md` and the settled campaign registry still contain no posted/full resolution of the Makai source statement. The claim therefore remains valid and exclusive to this track.

Fresh public-literature checks on **20 September 2026** again found no full three-dimensional resolution. Aliev's arXiv:2511.14991 proves the `2/3` bound only under tetrahedral symmetry, and the current MathDB entry still labels the unrestricted Makai difference-body conjecture open. These are bounded current-status checks, not a worldwide novelty certificate.

## 2. Runtime/model capability honesty

The automation interface exposed in this run still offers task title/prompt, schedule or relative start, timing mode, and enabled state. It exposes **no model selector, no reasoning-effort selector, and no authenticated guaranteed execution duration**. Therefore `GPT-6 / maximum` remains prompt text only; the actual runtime identity above is GPT-5.6 Sol and the reasoning level is honestly recorded as `UNVERIFIED`.

Changing this would require the product/runtime to expose authenticated model/reasoning fields (or an authorized task context that does). A repository edit cannot do it. The historical P26 `You cannot modify this task` result was a permissions/context failure. The current root ledger records that P26 was later editable from a different authorized context. The compliant workaround is therefore the authorized account/workspace task interface or platform support, never a permission bypass or a duplicate replacement task. This run did not create, modify, disable, re-enable, or probe another schedule.

## 3. Frozen source statement and metric

The controlling external source is Arkadiy Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991v1 (19 November 2025), Conjecture 1.3 (attributed there to Makai Jr.):

\[
\boxed{
 |K|\,|(K-K)^\circ|\ge \frac{n+1}{n!}
 \quad\text{for every convex body }K\subset\mathbb R^n,
}
\tag{M}
\]

with equality conjectured only for simplices.

The frozen metric is

`d_Makai = largest d for which (M) is rigorously established for every convex body in R^d`.

Incoming and outgoing values are

\[
\boxed{d_{\rm Makai}:2\longrightarrow2.}
\]

Thus this is **NO MOVEMENT**. In dimension three the unsolved source obligation is

\[
\boxed{
\inf_{K\subset\mathbb R^3\ \mathrm{convex}}
 |K|\,|(K-K)^\circ|\stackrel{?}{\ge}\frac23.
}
\tag{BLOCK}
\]

Aliev records the general available lower bound `8/15`, so the source gap is real and not a bookkeeping artifact.

## 4. Section-I(a): exact statement that blocks

The exact source blocker is `(BLOCK)` above. The new-method investigation this run shows that the most tempting one-projection proof route has its own exact blocker.

For a fixed three-dimensional convex body `K`, put

\[
D:=K-K,\qquad C:=D^\circ.
\]

For `u\in S^2` define

\[
A_C(u):=|C\cap u^\perp|,
\qquad
w_C(u):=\lambda_1(C|l_u)=2h_C(u),
\]

and let

\[
L_u:=P_{u^\perp}K.
\]

Because projection commutes with Minkowski difference,

\[
L_u-L_u=P_{u^\perp}D,
\]

and polarizing inside `u^perp` gives the exact identity

\[
(L_u-L_u)^\circ=C\cap u^\perp.
\tag{4.1}
\]

Choose the radial boundary point `x=\rho_D(u)u\in\partial D`. Zang's lemma gives

\[
|K|\ge \frac13\rho_D(u)|L_u|.
\tag{4.2}
\]

Since `C=D^circ`,

\[
\rho_D(u)=\frac1{h_C(u)}=\frac2{w_C(u)}.
\tag{4.3}
\]

Define the two dimensionless directional quantities

\[
E_K(u):=|L_u|\,A_C(u),
\qquad
R_C(u):=\frac{A_C(u)w_C(u)}{|C|}.
\tag{4.4}
\]

Then (4.1)--(4.3) yield the exact one-direction lower estimate

\[
\boxed{
 |K|\,|C|\ge \frac23\frac{E_K(u)}{R_C(u)}.
}
\tag{4.5}
\]

Eggleston's planar theorem gives

\[
E_K(u)\ge\frac32
\quad\text{for every }u.
\tag{4.6}
\]

Consequently a one-projection proof closes immediately if there is a direction with

\[
R_C(u)\le\frac32.
\tag{4.7}
\]

But the universal existence of such a direction is exactly the three-dimensional instance of the centered-body maximin problem

\[
\boxed{
\min_{u\in S^2}
\frac{|C\cap u^\perp|\,\lambda_1(C|l_u)}{|C|}
\stackrel{?}{\le}\frac32,
}
\tag{BP-maximin}
\]

with equality for ellipsoids.

Martini--Mustafaev--Zarbaliev, *Some new minimax inequalities for centered convex bodies*, Aequationes Math. 99 (2025), 1143--1152, DOI `10.1007/s00010-024-01109-6`, explicitly describes the maximin value of this same `section × width / volume` quantity as a challenging open problem and says it is reasonable to conjecture ellipsoids are extremal. Thus the naive `Zang + one planar Eggleston projection` strategy does not solve Makai; it imports another hard open convex-geometric problem.

This is an obstruction diagnosis, not a claim that `(BP-maximin)` is equivalent to Makai. It is only a sufficient route to `(M)`.

## 5. Section-B methods used in this thinking run

### B12 — FIND WHAT IS CONSERVED

The normalized blocker

\[
m(C):=\min_u \frac{A_C(u)w_C(u)}{|C|}
\]

is in fact affine invariant. This kills the possible escape of putting `C` in a clever linear position before applying Zang.

Indeed, let `S\in GL(3)` and fix a unit target direction `u`. Put

\[
n:=\frac{S^Tu}{|S^Tu|}.
\]

The hyperplane-section Jacobian is

\[
|SC\cap u^\perp|
=\frac{|\det S|}{|S^Tu|}\,|C\cap n^\perp|,
\]

while

\[
w_{SC}(u)=|S^Tu|\,w_C(n),
\qquad |SC|=|\det S|\,|C|.
\]

Therefore

\[
\frac{|SC\cap u^\perp|w_{SC}(u)}{|SC|}
=
\frac{|C\cap n^\perp|w_C(n)}{|C|}.
\]

As `u` ranges over the sphere, so does `n`, hence `m(SC)=m(C)`. Affine normalization does not remove `(BP-maximin)`.

**Outcome:** useful negative progress. The missing constant cannot be obtained merely by choosing John's, isotropic, or another affine position.

### B21 — ASK WHO ELSE HAS THIS SHAPE

Searching the section-width expression led directly to the Busemann--Petty minimax literature. The 2025 Martini--Mustafaev--Zarbaliev paper discusses both Busemann--Petty Problem 6 and the maximin quantity `(BP-maximin)` above. This is the exact geometric shape appearing in (4.7), not a loose analogy.

**Outcome:** successful obstruction identification. The route has landed on a named open neighboring problem rather than on an elementary missing estimate.

### B22 — READ THE FAILURES, NOT THE SUCCESSES

The same 2025 paper proves a sharp nearby theorem: after volume normalization,

\[
\min_u |B\cap u^\perp|\,\lambda_1(B^\circ|l_u)
\le 2\epsilon_{d-1},
\]

with equality only for ellipsoids. Its proof uses Busemann's intersection inequality: a hypothetical reverse inequality converts to an inclusion of a dilate of `B` inside the intersection body `IB`, and volume gives a contradiction.

For `(BP-maximin)`, however, the width is that of the **same** body `B`, not `B^circ`. The same algebra would give a dilate of `B^circ` inside `IB`, and Blaschke--Santaló allows `|B^circ|` to be strictly smaller than the ellipsoid value. The contradiction disappears. This is the precise polarity mismatch, not a missing constant-factor optimization.

**Outcome:** the closest solved minimax theorem cannot simply be substituted; it explains exactly why the one-body inclusion proof fails.

## 6. Section-I(b): routes tried on the Makai target and why each stops

### Route 1 — B2/B5/B11: refute-first + deformation + duality on pyramids

This produced an exact all-parameter proof for every three-dimensional pyramid by reducing the 3D product to Eggleston's planar inequality.

**Why it stops:** a general body has no distinguished apex/base decomposition. The exact fibre factorization that makes the pyramid collapse to one planar body disappears.

### Route 2 — B6/B18/B24: prismoid support fibres and homothetic frusta

For

\[
K=\operatorname{conv}(A\times\{0\},C\times\{1\}),
\]

the run obtained exact formulas

\[
|K|=\frac{|A|+V(A,C)+|C|}{3}
\]

and

\[
|(K-K)^\circ|
=
\int_{(A-A)^\circ\cap(C-C)^\circ}
\bigl(2-h_{A-A}-h_{C-C}\bigr).
\]

This proves the conjectured bound sharply for all positive-homothety frusta, including pyramids and prisms.

**Why it stops:** for non-homothetic bases, the primal term is a mixed area while the dual term lives on an intersection of two polar difference bodies. No monotone inequality found so far couples those two data at the sharp `2/3` constant.

### Route 3 — B1/B16/B25: change category to affine circuits / exact cube slices

This proved Makai's bound in every dimension for every affine-circuit polytope with exactly `n+2` vertices. In dimension three, together with the pyramid theorem, it covers every polytope with at most five vertices.

**Why it stops:** circuit decompositions do not add under the polar difference-body functional. Adding or triangulating vertices changes `(K-K)^circ` globally, so a sum of certified five-vertex pieces does not preserve the target product.

### Route 4 — B12/B21/B22 this run: one-projection Zang + Eggleston

Equation (4.5) exposes the exact two-defect ratio. Replacing the numerator only by Eggleston's universal `3/2` reduces the problem to `(BP-maximin)`.

**Why it stops:** `(BP-maximin)` is itself recorded as open in current convex-geometry literature. The nearest sharp solved minimax theorem has the polar width instead of the same-body width.

## 7. Section-I(c): what a successful proof now has to contain

The new diagnosis is that **one projection plus only the bare planar constant is not enough** unless one also solves the independent maximin problem `(BP-maximin)`.

Equation (4.5) shows a more promising way around that obstacle. A full proof would follow if one could show that for at least one direction

\[
\boxed{E_K(u)\ge R_C(u).}
\tag{DEFECT-COUPLING}
\]

The bare estimates give `E_K(u)>=3/2`; therefore the only hard regime is when `R_C(u)>3/2` for every direction. In that regime a proof needs a **quantitative surplus** in the planar Eggleston product that compensates for the section-width excess:

\[
E_K(u)-\frac32
\quad\text{must dominate}\quad
R_C(u)-\frac32
\]

for at least one direction.

This coupling is exactly what none of the preceding routes contains. It would use genuine three-dimensional compatibility between the family of planar projections `P_{u^perp}K` and the transverse widths of `C=(K-K)^circ`, instead of treating each projection independently.

The key literature opportunity is K. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies — Lower estimates with stability*, Studia Sci. Math. Hungar. 50 (2013), 159--198, DOI `10.1556/SScMath.50.2013.2.1235` / arXiv:1507.01481. They prove stability variants of Eggleston's planar inequality in Banach--Mazur distance from triangles. That supplies exactly the type of positive surplus on the left of `(DEFECT-COUPLING)` that the bare `3/2` theorem discards.

## 8. Section-I(d): simplest special case still unproved

The first clean finite-parameter family beyond the current coverage is a **six-vertex triangular prismoid with non-homothetic bases**:

\[
K=\operatorname{conv}(A\times\{0\},C\times\{1\}),
\qquad A,C\subset\mathbb R^2\text{ triangles},
\]

where `A` and `C` are not positively homothetic.

Why this is the first natural frontier:

- every 3D polytope with at most five vertices is already covered by the pyramid/affine-circuit results;
- homothetic triangular bases are already covered by the frustum theorem;
- two arbitrary triangles give the first genuinely non-homothetic six-vertex prismoid family.

The exact remaining inequality for this family is

\[
\boxed{
\frac{|A|+V(A,C)+|C|}{3}
\int_{(A-A)^\circ\cap(C-C)^\circ}
\bigl(2-h_{A-A}(y)-h_{C-C}(y)\bigr)\,dy
\ge\frac23.
}
\tag{TRI-PRISMOID}
\]

No current report proves `(TRI-PRISMOID)` for the full relative affine parameter family.

## 9. Section-I(e): nearest solved analogue and the ingredient it has that the full problem lacks

There are two immediately adjacent literature landmarks.

1. **Closest open obstruction:** Martini--Mustafaev--Zarbaliev (Aequationes Math. 2025) explicitly identifies the centered-body `section × same-body width / volume` maximin as a challenging open problem, with the ellipsoid conjectured extremal. This is `(BP-maximin)` in our dimension.

2. **Closest solved transferable mechanism:** Böröczky--Makai--Meyer--Reisner (2013) prove the sharp planar Eggleston inequality together with stability: distance of a planar body from the triangle class forces a quantitative increase above the `3/2` minimum.

What the full 3D Makai problem lacks is not the planar surplus itself. It lacks a theorem forcing **some projection** to be sufficiently far from a triangle whenever the corresponding centered section-width ratio `R_C(u)` is too large. Aliev's tetrahedral-symmetry proof gets the needed multi-direction compatibility from a 14-piece symmetry decomposition. An arbitrary body has no such finite orbit of equivalent directions.

## 10. Exactly one recovery action selected

**Recovery action selected: PORT THE TECHNIQUE FROM (e).**

The next active Makai iteration will port the 2013 planar Eggleston stability mechanism into the exact directional formula (4.5), rather than trying another bare constant estimate. The concrete target is a quantitative version of `(DEFECT-COUPLING)` linking triangle-distance of `P_{u^perp}K` to the section-width excess of `C` in at least one direction.

The next method triple is deliberately new on this target:

- **B3 — PROVE SOMETHING STRONGER:** target an explicit defect inequality, not merely the `2/3` endpoint;
- **B15 — BREAK THE SYMMETRY ON PURPOSE:** study perturbations away from simplex/triangle projections without assuming tetrahedral symmetry;
- **B30 — ONE SCALE / ONE DIRECTION AT A TIME:** freeze a direction, write the exact projection/fibre defects, then determine what prevents gluing them over the sphere.

If this first recovery does not produce source-metric movement and the same obligation persists to the next stuck threshold, the Section-I rules will trigger STUCK2; this report does not reset the unchanged count by relabeling a reduction as a theorem.

## 11. Current-status / literature record used this run

Fresh searches on 20 September 2026 included:

- `Makai Jr difference body conjecture 2026`;
- `Makai Jr (K-K) 2/3 convex body 2026`;
- `Makai polar difference body convex body 2026`;
- `Busemann-Petty maximin central section width convex body`;
- `min central section width volume ellipsoid maximin`;
- `Eggleston Banach-Mazur stability triangle difference body polar`;
- `Makai prismoid two triangles difference body`.

The relevant records recovered were:

- Arkadiy Aliev, arXiv:2511.14991 (2025): unrestricted planar theorem; 3D theorem under tetrahedral symmetry only; source Conjecture 1.3.
- MathDB, `Makai Jr.'s non-symmetric difference-body volume-product conjecture`: currently labels the conjecture open.
- Horst Martini, Zokhrab Mustafaev, Sakhavet M. Zarbaliev, Aequationes Math. 99 (2025), 1143--1152, DOI `10.1007/s00010-024-01109-6`: exact same-body section-width maximin posed as open; sharp neighboring polar-width inequalities proved using Busemann intersection/Petty machinery.
- K. Böröczky, E. Makai Jr., M. Meyer, S. Reisner, Studia Sci. Math. Hungar. 50 (2013), 159--198, DOI `10.1556/SScMath.50.2013.2.1235`, arXiv:1507.01481: planar Eggleston stability in Banach--Mazur distance from triangles.

No search result found a theorem matching the full unrestricted 3D source claim or the full non-homothetic triangular-prismoid family. That is negative search evidence only, not proof of priority.

## 12. Verification / bookkeeping scope

This is a Section-I thinking run with **no new theorem-sized or finite exhaustive claim**, so no checker was manufactured. The exact formulas above are algebraic reductions from Zang's lemma, projection-polar duality, and the published planar Eggleston theorem; the report deliberately spends its validation budget on source/literature/ownership checks rather than on another unchanged-metric certificate.

No Gmail, Drive, public posting, schedule mutation, other-track edit, or shared-root ledger rewrite was performed.

## Ledger delta

```text
track: HARD7-01
source_target: MAKAI-POLAR-DIFFERENCE-BODY
owner: HARD7-01
status: PARTIAL / SOURCE OPEN / CLAIMED / STUCK1
metric: d_Makai
before: 2
after: 2
movement: NO MOVEMENT
methods_this_run: B12 / B21 / B22
new_theorem_claim: NONE (thinking run)
exact_blocker: unrestricted 3D Makai >= 2/3
projection_route_blocker: centered-body section-width maximin <= 3/2, itself open
recovery_action: PORT TECHNIQUE — planar Eggleston stability
next_methods: B3 / B15 / B30
next_concrete_obligation: derive a quantitative directional defect coupling E_K(u) >= R_C(u) for some u, or isolate the exact obstruction to such a coupling
```
