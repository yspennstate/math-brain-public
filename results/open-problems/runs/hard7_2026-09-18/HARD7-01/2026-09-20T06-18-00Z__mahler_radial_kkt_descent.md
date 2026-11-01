Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` (**NO MOVEMENT**). Methods tried: **B5 / B18 / B22**.

# HARD7-01 — STUCK1 recovery: an exact coupled-radial descent eliminates the 12-vertex equality-incidence witness

**Status:** `PARTIAL / SOURCE OPEN / STUCK1 RECOVERY EXECUTED`.

The symmetric Mahler conjecture is not solved here. This run changes method exactly as required by the previous STUCK1 report. The new result is a rigorous analytic/finite obstruction: the explicit rational `n=4,V=12,F=22,I=98` polytope from the preceding run, although it realizes every shadow-incidence/full-spark equality condition then known, is **not a local minimizer of the Mahler volume product**. A coupled radial deformation has strictly negative exact one-sided volume-product derivative.

The certified derivative is

\[
\boxed{
\frac{d}{dt}\Big|_{0+}|P_t|\,|P_t^\circ|
=-\frac{622210883645}{108308358144}<0.
}
\tag{0.1}
\]

This is auxiliary progress only. It does not establish the full twelve-vertex case and does not move the frozen source metric `d_sym`.

## 1. Continuity, ownership, and evidence consumed

The canonical claim remains

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`,

owned exclusively by `HARD7-01`. The exact external target is the origin-symmetric Mahler conjecture:

\[
P(K):=|K|\,|K^\circ|\ge \frac{4^n}{n!}
\qquad
\text{for every origin-symmetric convex body }K=-K\subset\mathbb R^n.
\tag{1.1}
\]

The non-symmetric Santaló-centered conjecture is not claimed.

I resumed from

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T06-08-00Z__mahler_V12_realizable_cube_section.md`,

which had `d_sym=3`, methods `B1/B20/B26`, and triggered STUCK1 after proving that the first post-Lopez--Reisner incidence boundary is genuinely realizable. That report's exact witness has

\[
(V,F,I)=(12,22,98),\qquad
|P|=\frac{36937}{4536},\qquad
|P^\circ|=\frac{17281169}{11938752},
\tag{1.2}
\]

and

\[
P(P)=\frac{638314539353}{54154179072}>\frac{32}{3}.
\tag{1.3}
\]

This run reread/reconciled `CONTROL.md`, `NEW_METHODS_2026-09-16.md`, `OWNER_DIRECTIVE.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `INDEX.md` and `RANKING.md`, the canonical claim, the newest own report, and the newest relevant neighboring HARD7-05 report. Targeted repository searches for `Mahler`, `symmetric Mahler`, `volume product`, `reverse Santalo`, and the exact canonical aliases surfaced no peer owner/equivalent active claim. The reserve/intake ledgers were checked through the current queue plus targeted repository/intake alias search; no Mahler intake collision surfaced. No peer claim or shared root ledger was overwritten.

The required mathematical idea was persisted before checker construction at

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T06-12-00Z__idea_before_code_mahler_radial_kkt.md`

(commit `f21ddf4955fc4af9050ed4b3316a9f44a9bc08b4`).

## 2. Fresh bounded source/literature check

The exact source scope remains open-looking from dimension four onward under this bounded 20 September 2026 check; that is not a worldwide openness certificate.

1. **Lopez--Reisner (1998),** *A special case of Mahler's conjecture*, Discrete Comput. Geom. 20, 163--177, DOI `10.1007/PL00000076`. The primary institutional abstract states that the symmetric conjecture is proved for polytopes with at most `2n+2` vertices or facets for `n<=8`. Hence every 4D symmetric polytope with at most ten vertices or facets is already covered; the present `V=12` boundary is genuinely beyond that theorem's stated scope.
2. **Daniel Martin Jimenez Cuevas (2026),** arXiv:2606.14709, *A Discrete KKT Variational Characterization of the Local Minimality of the Mahler Volume in Centrally Symmetric Polytopes*. The primary abstract states that radial vertex immersions yield an exact KKT stationarity condition and proves strict radial local minimality/stability of the Hanner orbit. This makes a radial first-variation route especially relevant, but the available abstract does not settle arbitrary 12-vertex 4-polytopes.
3. **Agam Guberman (2026),** arXiv:2608.10994, *A connection between the Mahler conjecture and floating bodies*. The primary abstract states a combinatorial-structure result for volume-product minimizers. I did not obtain the complete theorem text from a primary full-text endpoint in this bounded run, so no detailed secondary paraphrase of that theorem is used as a premise here.
4. **Chen--Li--Xi--Xu (2026),** arXiv:2605.13795, gives a new proof of the symmetric three-dimensional theorem by admissible shadow systems; arXiv:2605.09334 concerns the non-symmetric 3D theorem. Neither abstract states a four-dimensional solution.
5. **Harrell--Henrot--Lamboley (2015),** *On the Local Minimizers of the Mahler Volume*, J. Convex Anal. 22, studies first/second variations and concavity properties of local minimizers. It supplies useful context for a variational attack but not the source-level four-dimensional conclusion.

Fresh searches for `symmetric Mahler dimension four 2026`, `Mahler conjecture four-dimensional 2026`, and `Mahler local minimizer polytope 2026` found the neighboring local/KKT work above but no verified full 4D resolution. Priority of the finite obstruction proved below remains **UNVERIFIED**.

## 3. B18 — change language: radial chambers and circuit resolutions

Write the six positive vertex representatives of the exact preceding witness as the columns `v_1,...,v_6` of

\[
A=\begin{pmatrix}
 1/6&-1&-1&1&1&1\\
 1&1/7&-1&-1&-1&1\\
 -1&1&-1/4&1&1&1\\
 -1&-1&1&-1/9&1&1
\end{pmatrix},
\tag{3.1}
\]

so

\[
P=\operatorname{conv}\{\pm v_1,\ldots,\pm v_6\}.
\]

The previous route treated the five nonsimplicial opposite facet pairs through incidence and circuit spaces. Here I instead make the circuit degeneracies themselves the parameter chambers.

For `a=(a_1,...,a_6)` define

\[
v_i(t)=(1+a_i t)v_i,
\qquad
P_t=\operatorname{conv}\{\pm v_i(t):1\le i\le6\}.
\tag{3.2}
\]

At `t=0` five opposite facet pairs have five vertices. A generic one-sided radial direction resolves each such affine circuit into a tetrahedral subdivision. Therefore `t\mapsto |P_t|` need not be differentiable through zero in the naive fixed-face-lattice sense, but its **right derivative is a finite regular-triangulation computation**.

For four signed vertices indexed by a set `F` and any fifth signed vertex `k`, let

\[
\Delta_{F,k}(t)
=\det\begin{pmatrix}
p_{i_1}(t)&1\\
\vdots&\vdots\\
p_{i_4}(t)&1\\
p_k(t)&1
\end{pmatrix},
\tag{3.3}
\]

where the rows are homogeneous affine coordinates in `R^4`. Each `\Delta_{F,k}` is a rational polynomial of degree at most four. For all sufficiently small `t>0`, `F` is a supporting tetrahedral facet exactly when the first nonzero Taylor coefficients of all nonidentically-zero `\Delta_{F,k}` for `k\notin F` have one common sign, with affine independence of `F`.

Because there are only `C(12,4)=495` candidate four-sets, the entire right chamber is finite and exact.

## 4. B5 — differentiate an exact coupled radial direction

Take

\[
\boxed{a=(-1,3,3,3,-1,-6).}
\tag{4.1}
\]

This is deliberately a **coupled** direction. Testing the six radial coordinates one at a time misses the cancellation between primal and polar first variations that matters here.

### Proposition 4.1 — exact right-hand primal chamber and derivative

For the direction (4.1), there are exactly `34` tetrahedral facets of `P_t` for every sufficiently small `t>0`. Their cone decomposition gives

\[
\boxed{
\frac{d}{dt}\Big|_{0+}|P_t|=\frac{23879}{9072}.
}
\tag{4.2}
\]

#### Proof

The exact checker expands every polynomial (3.3) using rational arithmetic, examines the first nonzero coefficient, and exhausts all 495 four-sets. Exactly 34 four-sets have the required one-sided support sign. Every remaining nondegenerate four-set has outside vertices on both sides for small positive `t`; the 15 four-sets whose five-point determinants vanish identically do not define a full 3-dimensional facet. An independent exact enumeration at `t=1/1000` obtains exactly 34 polar vertices, each saturating exactly four inequalities, and the resulting 34 primal facets agree exactly with the Taylor-sign set.

The origin is interior. Hence in this right chamber

\[
|P_t|=\sum_{F}\frac{1}{4!}
\left|\det(p_{i_1}(t),\ldots,p_{i_4}(t))\right|,
\tag{4.3}
\]

where the sum is over the 34 boundary tetrahedra. If a tetrahedron uses antipodal-pair indices `j_1,...,j_4`, its determinant is its value at zero multiplied by

\[
\prod_{r=1}^4(1+a_{j_r}t).
\]

Differentiating (4.3) from the right and summing the 34 exact determinant weights gives `23879/9072`. The same 34 tetrahedra at `t=0` sum exactly to `36937/4536`, independently reproducing the incoming primal volume. QED.

### Proposition 4.2 — exact polar first variation

For the same direction,

\[
\boxed{
\frac{d}{dt}\Big|_{0+}|P_t^\circ|=-\frac{111179}{94752}.
}
\tag{4.4}
\]

#### Proof

With the normals frozen at `v_i`, polarity gives

\[
P_t^\circ
=\left\{y:\ |\langle v_i,y\rangle|
\le h_i(t):=\frac1{1+a_i t},\quad1\le i\le6\right\}.
\tag{4.5}
\]

At `t=0` all twelve inequalities are genuine facets. Let `c_i` be the total 4-dimensional volume of the two cones from the origin to the opposite facet pair corresponding to `i`. In dimension four, one facet at support value one and Euclidean area `A_i` contributes cone volume `A_i/(4\|v_i\|)`, so the opposite pair has

\[
c_i=\frac{A_i}{2\|v_i\|}.
\]

Moving the two supporting hyperplanes by a common infinitesimal support amount `dh_i` changes volume to first order by `2A_i dh_i/\|v_i\|=4c_i dh_i`; intersections of simultaneously moving facet slabs contribute only second-order volume. Since `h_i'(0)=-a_i`,

\[
\frac{d}{dt}\Big|_{0+}|P_t^\circ|
=-4\sum_{i=1}^6 a_i c_i.
\tag{4.6}
\]

The exact barycentric facet/ridge/edge decomposition used in the preceding run gives

\[
(c_1,\ldots,c_6)=
\left(
\frac{757}{5292},
\frac{1147331}{3411072},
\frac{1353}{5264},
\frac{3025}{11844},
\frac{587}{4704},
\frac{7900217}{23877504}
\right).
\tag{4.7}
\]

Substitution of (4.1) into (4.6) gives `-111179/94752`. The same exact facet decomposition reproduces `|P^circ|=17281169/11938752`. QED.

### Theorem 4.3 — the exact equality-incidence witness is not a Mahler local minimizer

For `P_t` defined by (3.2) and (4.1),

\[
\frac{d}{dt}\Big|_{0+}
\left(|P_t|\,|P_t^\circ|\right)
=-\frac{622210883645}{108308358144}<0.
\tag{4.8}
\]

Consequently the explicit rational `V=12,F=22,I=98` polytope of the preceding run is not a local minimizer of the volume product.

#### Proof

Combine (1.2), (4.2), and (4.4):

\[
M'_+(0)
=\frac{23879}{9072}\frac{17281169}{11938752}
+\frac{36937}{4536}\left(-\frac{111179}{94752}\right),
\]

which simplifies exactly to the negative rational in (4.8). A strictly negative right derivative implies `M(P_t)<M(P_0)` for all sufficiently small positive `t`. QED.

As a completely independent finite sanity check, the checker evaluates `t=1/1000` exactly and finds

\[
M(P_{1/1000})-M(P_0)
=-\frac{4044467634694812921161540885361006323}
{686213964562459819622396928968363212800}<0.
\tag{4.9}
\]

The fixed-point inequality (4.9) is not used in place of the derivative proof.

## 5. B22 — what the literature route teaches and where it stops

The 2026 radial-KKT paper makes it natural to test radial stationarity, but the incoming witness is deliberately far from the Hanner orbit and lies on nonsimplicial circuit walls. The useful adaptation here is therefore not a smooth Hessian test: it is a **one-sided piecewise-linear secondary-fan stationarity test**.

This run also shows why the preceding combinatorial route stopped. The witness passes the shadow-incidence debt and both full-spark conditions, and it is a genuine cube-section realization, but coupled radial KKT detects a descent direction immediately. The missing condition for the whole `V=12,F=22,I=98` class is therefore analytic stationarity of the circuit-resolved volume, not another scalar incidence count.

A promising next reduction is finite in form: each of the five nonsimplicial opposite facet pairs has a one-dimensional circuit. For an arbitrary equality-class polytope, the signs of the five circuit evaluations on a radial direction choose a chamber, and the primal directional derivative is a linear functional in that chamber; the polar derivative is always the linear support-variation term (4.6). A hypothetical local minimizer must make the resulting piecewise-linear functional nonnegative on **every** radial chamber. Turning that into a contradiction uniformly is the next source-relevant obligation.

## 6. Tests actually run and artifacts

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T06-14-00Z__mahler_radial_kkt_check.py`

Archived stdout:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T06-14-00Z__mahler_radial_kkt_check.out`

The script was executed under Python 3 and returned exit code `0`. It uses `fractions.Fraction` throughout for all theorem-deciding arithmetic; no floating-point acceptance test, Qhull, random search, or numerical optimizer appears in the certificate. It verifies, among other things,

- all 495 candidate four-sets through Taylor-sign support determinants;
- exactly 34 right-hand tetrahedral facets;
- exact reconstruction of both incoming volumes;
- all six opposite polar-facet cone volumes;
- `d|P_t|/dt|_{0+}=23879/9072`;
- `d|P_t^circ|/dt|_{0+}=-111179/94752`;
- the negative exact product derivative (4.8);
- an independent exact `t=1/1000` product decrease.

The archived output ends

`ALL_EXACT_CHECKS_PASS = True`.

A platform-level spreadsheet-runtime warmup warning appeared on stderr during the local Python startup, unrelated to this standalone checker; the checker itself exited `0` and its exact stdout is what is archived.

## 7. Source metric, auxiliary progress, and remaining gap

Frozen source metric:

`d_sym: 3 -> 3` — **NO MOVEMENT**.

Source status remains `OPEN`; track status remains `PARTIAL`.

Auxiliary progress, kept separate from the source metric:

1. the preceding exact `V=12,F=22,I=98` equality-incidence realization is now rigorously eliminated as a local minimizer;
2. a nonsmooth/circuit-degenerate radial local-minimum test is reduced to a finite right-chamber determinant census plus polar support first variation;
3. an exact coupled radial descent direction is certified;
4. the reason scalar/full-spark incidence conditions are insufficient is now analytic rather than merely empirical.

The unresolved full-scope gap is still the first post-Lopez--Reisner four-dimensional class, beginning with

\[
\inf\{|P||P^\circ|:\ P=-P\subset\mathbb R^4,\ P\text{ a polytope},\ V(P)=12\}
\stackrel{?}{\ge}\frac{32}{3}.
\tag{7.1}
\]

No uniform proof of (7.1) is claimed.

## 8. Section-I state after this recovery

The previous report already supplied the five-part STUCK1 diagnosis. This run executes its method-change recovery rather than repeating that diagnosis. The recovery is mathematically nontrivial but does not move `d_sym`; therefore it does **not** reset the source metric by relabeling auxiliary progress.

The exact blocking statement is now sharper: even after the explicit equality-boundary witness is eliminated, one must prove that **every** hypothetical `V=12` local minimizer violates either the shadow/circuit condition or the all-radial-chambers stationarity inequalities.

The simplest unproved special case remains the equality-incidence subclass `V=12,F=22,I=98`, but the surviving obligation is now a uniform piecewise-linear radial-KKT contradiction, not realizability. The nearest solved restricted theorem remains Lopez--Reisner's `V<=10`/`F<=10` theorem; what it has that the present class lacks is a complete low-complexity classification/reduction strong enough to control the volume product globally.

If another full unchanged cycle reaches the owner's next stuck trigger, the next recovery must use a materially different route (for example the uniform secondary-fan/KKT system, not another isolated witness). This report does not rotate away from Mahler prematurely.

## 9. Runtime/scheduler capability honesty

The current exposed scheduler contract still has task title/prompt, schedule/relative start, timing mode, and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed execution duration**. Thus GPT-6/maximum remains prompt-requested only. The actual runtime identifies as GPT-5.6 Sol; reasoning telemetry is unavailable, so it is `UNVERIFIED`.

The repository records historical native modification errors `You cannot modify this task` for P26/P01/P03, while later `RESULTS.md` records that P26 succeeded from a different authorized context. The compliant workaround is an authorized task/account/workspace context or platform support. A research worker cannot fix that by repository edits, permission bypass, or duplicate schedules. This run did not create, edit, disable, re-enable, or probe any other schedule.

## 10. ledger_delta

- track: `HARD7-01`
- target: symmetric Mahler volume-product conjecture
- canonical claim: `operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`
- source metric: `d_sym: 3 -> 3`
- movement: `NO MOVEMENT`
- status: `PARTIAL / SOURCE OPEN / STUCK1 RECOVERY EXECUTED`
- methods: `B5 / B18 / B22`
- new auxiliary theorem: explicit prior `V=12,F=22,I=98` witness is not a local Mahler minimizer; exact right derivative `-622210883645/108308358144`
- source closure: `NO`
- independent audits: `0/2` for this new auxiliary theorem; self-check only
- shared root edit requested: `NO`
