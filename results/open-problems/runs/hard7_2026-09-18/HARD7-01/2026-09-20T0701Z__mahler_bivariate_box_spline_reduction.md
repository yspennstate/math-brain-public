Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.** Source metric `d_sym: 3 -> 3` (**NO MOVEMENT**). Methods tried: **B21 / B25 / B30**.

# HARD7-01 — exact bivariate box-spline reduction of the 12-vertex four-dimensional Mahler case

**Status:** `PARTIAL / SOURCE OPEN / post-STUCK1 method change`.

The symmetric Mahler conjecture is not solved here. This run changes category away from the preceding witness-by-witness radial KKT route. The main new result is an exact Gale/box-spline identity which reduces the entire **generic twelve-vertex four-dimensional subclass** to one fifteen-term discrete-continuous probability inequality. By density and continuity, proving that inequality for all generic rank-two Gale matrices would settle the full twelve-vertex subclass (and, by polarity, the twelve-facet subclass).

For the first post-Lopez--Reisner case, the exact remaining inequality is

\[
\boxed{\sum_{1\le j<k\le 6}N_{jk}(B)p_{jk}(B)\ge16,}
\tag{0.1}
\]

or equivalently, with `q_{jk}=N_{jk}/16`,

\[
\boxed{\sum_{j<k}q_{jk}(B)p_{jk}(B)\ge1.}
\tag{0.2}
\]

This is a genuine reduction, not source closure. An exact generic example also **refutes** the tempting termwise strengthening `p_{jk}>=q_{jk}`; hence the aggregate coupling in (0.2), rather than fifteen separate peakedness bounds, is the real missing lemma.

## 1. Continuity, ownership, and evidence consumed

The canonical claim remains

`operations/claims/MAHLER-SYMMETRIC-VOLUME-PRODUCT.md`,

owned exclusively by `HARD7-01`. The exact external statement remains

\[
\mathcal P(K):=|K|\,|K^\circ|\ge\frac{4^n}{n!}
\qquad(K=-K\subset\mathbb R^n),
\tag{1.1}
\]

with the non-symmetric Santaló-centered problem explicitly excluded.

This run resumed, rather than restarted, the latest checkpoint

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T06-18-00Z__mahler_radial_kkt_descent.md`,

where `d_sym=3` and the previous exact `V=12,F=22,I=98` witness was eliminated as a local minimum by the coupled radial derivative

\[
-\frac{622210883645}{108308358144}<0.
\]

At run start I read/reconciled the governing files

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- the canonical Mahler claim;
- the newest own Mahler checkpoint and the newest relevant neighboring Gaussian-probability report recoverable from HARD7-05;
- targeted repository/intake searches for `Mahler`, `symmetric Mahler`, `volume product`, `reverse Santalo`, `box spline`, and canonical aliases.

No peer owner, equivalent active claim, posted exact result, release, or canonical collision was found by those bounded repository/intake searches. The large intake ledgers were searched by target/alias rather than claimed byte-for-byte reread. No shared root file or peer artifact was edited.

The mathematical idea was written **before code** at

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T0701Z__idea_before_code_mahler_bivariate_box_spline.md`

(commit `90f0d17439566d50ac27a48968fbac4eaf168e4b`).

## 2. Fresh source/literature check

The source-level baseline remains `d_sym=3`. A bounded 20 September 2026 search did not produce a verified global four-dimensional solution; this is dated negative evidence, not a worldwide openness certificate.

The literature point that matters for this run is sharper:

1. **Lopez--Reisner (1998),** *A special case of Mahler's conjecture*, Discrete Comput. Geom. 20, 163--177, DOI `10.1007/PL00000076`, proves the symmetric conjecture for polytopes with at most `2n+2` vertices or facets for `n<=8`. Thus in dimension four the `V<=10` and `F<=10` regimes are already known.
2. **Zhiqiang Xu (2009),** *A Remark about Mahler's Conjecture and the Maximum Value of Box Splines*, arXiv:0812.4284v2, explicitly treats the `2n+2`-facet case as a one-codimensional cube section and recasts Ball's reduction as a **univariate box-spline** inequality. Xu's equation (6) is precisely the cube-section/box-spline coarea formula used below. URL: `https://arxiv.org/abs/0812.4284`.
3. **Daniel Martín Jiménez Cuevas (2026),** arXiv:2606.14709, develops exact radial KKT stationarity and proves strict local minimality/stability of the Hanner orbit; it does not state the full 12-vertex 4D theorem. URL: `https://arxiv.org/abs/2606.14709`.
4. **Agam Guberman (2026),** arXiv:2608.10994, announces a combinatorial-structure result for volume-product minimizers via floating bodies. The available primary abstract does not state a global four-dimensional solution. URL: `https://arxiv.org/abs/2608.10994`.

Fresh searches for `Mahler four dimensions centrally symmetric 12 vertices`, `Mahler bivariate box spline`, and `codimension two cube section volume product` found Xu's codimension-one/univariate formulation and general multivariate box-spline literature, but no verified source proving (0.1). **Priority of the exact identity below is UNVERIFIED**; it may be a natural Gale/coarea reformulation rather than a new literature theorem.

## 3. B21 — the first unknown vertex count is a bivariate box spline

The key change of language is forced by dimensions.

Let

\[
P=\operatorname{conv}\{\pm v_1,\ldots,\pm v_m\}\subset\mathbb R^n,
\qquad
A=(v_1\ \cdots\ v_m)\in\mathbb R^{n\times m},
\tag{3.1}
\]

with `rank(A)=n`. Put `r=m-n`. Choose a full-row-rank matrix

\[
B=(b_1\ \cdots\ b_m)\in\mathbb R^{r\times m},
\qquad BA^T=0.
\tag{3.2}
\]

Then `row(A)=ker(B)`. The injective map `A^T:R^n -> row(A)` sends the polar to the central cube section

\[
A^T(P^\circ)=C_B:=\ker(B)\cap[-1,1]^m.
\tag{3.3}
\]

For the first unknown four-dimensional vertex count, `n=4,m=6`, hence `r=2`: the polar is a **codimension-two section of a six-cube**. If `U_i iid~Unif[-1,1]` and

\[
Y_B:=\sum_{i=1}^m b_iU_i,
\tag{3.4}
\]

then the density `f_B(0)` is a bivariate box-spline value when `r=2`. This is exactly the multivariate analogue of the univariate object in Xu's codimension-one formulation.

## 4. B25 — exact double-count identity

I record the identity in general codimension because the normalization becomes transparent and the four-dimensional statement is then immediate.

### Theorem 4.1 — generic Gale/box-spline volume-product identity

Assume the polytope (3.1) is **generic simplicial** in the following finite sense:

- every `v_i` is a genuine vertex;
- every facet contains exactly `n` signed vertices from distinct antipodal pairs;
- every `r x r` minor `B_J` relevant below is nonsingular;
- no corresponding solved free coordinate lies on the cube boundary, so the facet chamber has no degeneracy.

For `J subset [m]`, `|J|=r`, put `I=J^c` and define

\[
N_J(B)=\#\left\{\varepsilon\in\{\pm1\}^{I}:
-B_J^{-1}B_I\varepsilon\in(-1,1)^r\right\},
\tag{4.1}
\]

and, for iid `U_i~Unif[-1,1]`,

\[
p_J(B)=\Pr\left\{-B_IU_I\in B_J[-1,1]^r\right\}.
\tag{4.2}
\]

Then

\[
\boxed{
|P|\,|P^\circ|
=\frac{2^n}{n!}\sum_{|J|=r}N_J(B)p_J(B).
}
\tag{4.3}
\]

#### Proof

**Step 1: cube-section density.** Let

\[
D_A=\sqrt{\det(AA^T)},\qquad D_B=\sqrt{\det(BB^T)}.
\]

The linear map `A^T:R^n -> row(A)` has `n`-dimensional Jacobian `D_A`; therefore (3.3) gives

\[
\operatorname{vol}_n(C_B)=D_A|P^\circ|.
\tag{4.4}
\]

The random vector `U=(U_1,...,U_m)` has density `2^{-m}` on the cube. The coarea formula for the surjection `B:R^m->R^r` gives

\[
f_B(0)
=\frac{\operatorname{vol}_n(C_B)}{2^mD_B}
=\frac{D_A}{2^mD_B}|P^\circ|.
\tag{4.5}
\]

Equivalently,

\[
|P^\circ|=2^m\frac{D_B}{D_A}f_B(0).
\tag{4.6}
\]

This is the centered `[-1,1]^m` normalization of the standard box-spline/cube-section formula.

**Step 2: facets and the discrete count.** A simplicial facet using pair support `I` and signs `varepsilon in {+-1}^I` corresponds under polarity to a cube-section vertex `q` with

\[
q_I=\varepsilon,
\qquad
B_I\varepsilon+B_Jq_J=0.
\]

Thus

\[
q_J=-B_J^{-1}B_I\varepsilon,
\]

and the generic interior condition `q_J in(-1,1)^r` is exactly (4.1). Hence `N_J` is the number of facets whose omitted pair set is `J`.

Coning every simplicial facet to the origin partitions `P`. A facet with pair support `I` contributes

\[
\frac{|\det A_I|}{n!}
\]

regardless of its signs. Therefore

\[
|P|=\frac1{n!}\sum_{|J|=r}N_J|\det A_{J^c}|.
\tag{4.7}
\]

**Step 3: complementary minors.** Normalize the row spaces by

\[
\widetilde A=(AA^T)^{-1/2}A,
\qquad
\widetilde B=(BB^T)^{-1/2}B.
\]

Their row spaces are orthogonal complements, so stacking them gives an orthogonal `m x m` matrix. Complementary minors of an orthogonal matrix have equal absolute value. Hence for complementary `I,J`,

\[
\frac{|\det A_I|}{D_A}
=\frac{|\det B_J|}{D_B},
\tag{4.8}
\]

or

\[
|\det A_I|=\frac{D_A}{D_B}|\det B_J|.
\tag{4.9}
\]

Combining (4.6), (4.7), and (4.9),

\[
|P||P^\circ|
=\frac{2^m}{n!}f_B(0)
\sum_{|J|=r}N_J|\det B_J|.
\tag{4.10}
\]

**Step 4: localize the common density.** Conditional on `B_IU_I`, the independent vector `B_JU_J` is uniform on the parallelepiped `B_J[-1,1]^r`, with constant density

\[
\frac1{2^r|\det B_J|}.
\]

Evaluating the convolution density at zero therefore gives

\[
f_B(0)=\frac{p_J}{2^r|\det B_J|},
\qquad
p_J=2^r|\det B_J|f_B(0).
\tag{4.11}
\]

Substituting (4.11) into (4.10), and using `m-r=n`, yields (4.3). QED.

### Corollary 4.2 — exact Mahler reformulation

For every generic polytope in the theorem, the Mahler inequality is equivalent to

\[
\boxed{
\sum_{|J|=r}N_Jp_J\ge2^n.
}
\tag{4.12}
\]

Indeed, (4.3) and `4^n/n!` differ exactly by the factor `2^n`.

This is the useful new object: a finite sum coupling a **Rademacher cube-vertex hit count** `N_J` to a **continuous uniform cube-volume hit probability** `p_J` for the same Gale parallelepiped.

## 5. Four dimensions, twelve vertices: the fifteen-term target

Now set `n=4,m=6,r=2`. There are fifteen pairs `J={j,k}`. Put

\[
q_J:=\frac{N_J}{16}
=\Pr_{\varepsilon\in\{\pm1\}^4}
\{-B_I\varepsilon\in B_J(-1,1)^2\}.
\tag{5.1}
\]

Then Theorem 4.1 becomes

\[
\boxed{
|P||P^\circ|
=\frac23\sum_{j<k}N_{jk}p_{jk}
=\frac{32}{3}\sum_{j<k}q_{jk}p_{jk}.
}
\tag{5.2}
\]

Therefore the generic twelve-vertex case is **exactly** (0.1)/(0.2).

This is substantially smaller than the previous all-radial-chambers formulation: the ambient geometry is now a rank-two six-column Gale matrix, and the target is a scalar fifteen-term inequality.

### Proposition 5.2 — generic suffices for the full twelve-vertex subclass

If (0.1) holds for every generic rank-two Gale matrix representing a centrally symmetric 4-polytope with twelve genuine vertices, then

\[
|P||P^\circ|\ge\frac{32}{3}
\]

for **every** centrally symmetric four-polytope with exactly twelve vertices.

#### Proof

Let `P=conv{+-v_1,...,+-v_6}` have twelve genuine vertices. For each vertex choose a strict exposing functional; strict inequalities against the other finitely many vertices persist under sufficiently small perturbations. Hence a sufficiently small centrally symmetric perturbation of the six representatives preserves all twelve vertices. The conditions excluded by genericity -- vanishing minors, extra coplanar facet vertices, and cube-section boundary equalities -- are proper algebraic conditions, so one can choose a sequence of such perturbations converging to `P` while avoiding all of them. By hypothesis every perturbed polytope satisfies the Mahler bound. Volume and polar volume are continuous under Hausdorff convergence for bodies containing the origin in their interiors. Passing to the limit proves the bound for `P`. QED.

Conversely, the full twelve-vertex Mahler bound trivially implies (0.1) on the generic subclass through (5.2). Thus (0.1) is an **equivalent generic formulation of the entire twelve-vertex problem**. By polarity, the same achievement would cover the twelve-facet class.

It would still not move `d_sym`, because arbitrary four-dimensional bodies can have more vertices/facets.

## 6. B30 — localize pairwise, then kill the wrong strengthening

The obvious hope after (5.2) is the pointwise comparison

\[
p_J\stackrel{?}{\ge}q_J=N_J/16.
\tag{6.1}
\]

If (6.1) held and one also had an adequate sum-of-squares/count bound, the fifteen-term problem might collapse. It is false even for a completely generic valid twelve-vertex configuration.

Take the exact Gale matrix

\[
B=
\begin{pmatrix}
-7&-10&4&-6&6&8\\
 2&  5&6& 1&-6&1
\end{pmatrix}.
\tag{6.2}
\]

All fifteen `2 x 2` minors are nonzero. One rational basis of `ker B` is

\[
A=
\begin{pmatrix}
16/3&-10/3&1&0&0&0\\
-4/3&1/3&0&1&0&0\\
-2&2&0&0&1&0\\
10/3&-23/15&0&0&0&1
\end{pmatrix}.
\tag{6.3}
\]

The exact checker exhausts the central section and finds `38` vertices, every one with exactly four saturated cube coordinates; all twelve coordinate inequalities cut genuine three-dimensional facets. Thus this is a generic twelve-vertex primal polytope with 38 simplicial facets.

For the one-based pair

\[
J=\{2,4\}
\]

(the checker prints zero-based `(1,3)`), it obtains

\[
N_J=4,
\qquad
q_J=\frac14,
\tag{6.4}
\]

but a completely independent exact H-polytope integration of the four-dimensional preimage in (4.2) gives

\[
\boxed{
p_J=\frac{233633729}{1140480000}
<\frac14,
}
\tag{6.5}
\]

with exact gap

\[
p_J-q_J=-\frac{51486271}{1140480000}<0.
\tag{6.6}
\]

So no proof based on fifteen separate `p_J>=q_J` inequalities can work.

At the same time the aggregate target is comfortably true for this example:

\[
\sum_JN_Jp_J
=\frac{52100321567}{2851200000}
=16+\frac{6481121567}{2851200000},
\tag{6.7}
\]

and independently

\[
|P|=\frac{223}{45},
\qquad
|P^\circ|=\frac{233633729}{95040000},
\tag{6.8}
\]

so

\[
|P||P^\circ|
=\frac{52100321567}{4276800000}
=\frac{32}{3}+\frac{6481121567}{4276800000}.
\tag{6.9}
\]

The checker verifies the exact identity (5.2) with zero discrepancy.

The lesson is useful: the needed phenomenon is **aggregate negative/positive compensation between Gale bases**, not termwise peakedness of uniform coefficients versus Rademachers.

## 7. What the three methods produced

**B21 — ask who else has this shape.** This succeeded. Xu/Ball's codimension-one cube section is the exact lower-codimension analogue; the first new 12-vertex case naturally lives in a bivariate box spline. The fresh search did not locate the precise fifteen-term identity or a theorem proving its required lower bound. Priority is still UNVERIFIED.

**B25 — count the same thing twice.** This succeeded analytically. Primal cone volumes, complementary minors, polar cube-section coarea and conditional parallelepiped densities give the exact general identity (4.3). No simulation enters the proof.

**B30 — localize one Gale basis at a time.** This both sharpened the target and killed a bad route. Each term has the exact pairwise probability interpretation (4.2)/(4.11), but an exact generic example has `p_{24}<q_{24}`. The next proof must use the sum in (0.2), not fifteen independent inequalities.

These are materially different from the preceding `B5/B18/B22` radial-KKT run.

## 8. Exact missing lemma and next mathematical route

The first source-relevant special-case obstruction is now the following self-contained rank-two statement.

> **BS12.** Let `B in R^{2 x 6}` be a generic Gale matrix for a centrally symmetric four-polytope with twelve genuine vertices. For every pair `J={j,k}`, define `q_J` and `p_J` by (5.1) and (4.2). Then
> \[
> \sum_{j<k}q_Jp_J\ge1.
> \]

A proof of BS12 closes the full twelve-vertex/facet subclass by Proposition 5.2. A counterexample to BS12 would be an actual counterexample to Mahler in that subclass, so this is not a merely sufficient artificial inequality.

The most promising next nonrepeated moves are:

- **B6:** deform the rank-two Gale configuration toward a wall where one antipodal pair becomes redundant and the problem falls into the Lopez--Reisner `V<=10` regime, tracking the aggregate `sum q_Jp_J` rather than one term;
- **B13:** search for a monotone aggregate along one column-length deformation inside a fixed oriented-matroid/box-spline chamber;
- **B29:** compactify the normalized Gale space (e.g. `BB^T=I_2`) so that any putative minimizer of the BS12 functional has a controlled interior KKT point or a solved boundary degeneration.

This is the route to try before returning to another isolated radial witness.

## 9. Tests actually run and exact artifacts

Exact checker:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T0701Z__mahler_bivariate_box_spline_check.py`

Archived stdout:

`artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T0701Z__mahler_bivariate_box_spline_check.out`

The checker was executed with exact `fractions.Fraction` arithmetic for every theorem-deciding finite computation. It verifies:

- all 15 Gale minors in (6.2) are nonzero;
- `BA^T=0`, `rank A=4`, `rank B=2`;
- exhaustive cube-section vertex enumeration gives exactly 38 vertices, all with four active cube coordinates;
- all twelve coordinate inequalities are genuine facets of the section;
- the primal has 38 simplicial facets;
- exact primal/polar volumes (6.8);
- all 15 complementary-minor ratios;
- the exact product identity (5.2);
- the positive aggregate BS12 margin (6.7);
- an **independent exact H-polytope volume computation** of `p_{24}` with 38 vertices and 12 facets, yielding (6.5);
- the strict negative pointwise gap (6.6).

The output ends

`ALL_EXACT_CHECKS_PASS = True`.

The universal Theorem 4.1 is proved on the page; the single finite example is only a self-check/counterexample to the stronger termwise route. It is not evidence that BS12 holds universally.

## 10. Source metric and auxiliary progress

Frozen source metric:

`d_sym: 3 -> 3` — **NO MOVEMENT**.

Source status: `OPEN`. Track status: `PARTIAL`.

Auxiliary progress, separately:

1. exact general Gale/box-spline identity (4.3) for generic centrally symmetric polytopes;
2. exact reduction of the generic 4D twelve-vertex problem to fifteen terms, (0.1)/(0.2);
3. density/continuity argument showing that proving BS12 for generic matrices suffices for the **entire** twelve-vertex subclass;
4. exact generic refutation of the naive termwise strengthening `p_J>=q_J`;
5. a much smaller next target in rank-two Gale space, with no simulation-to-theorem promotion.

The unresolved full-scope gap remains the full symmetric Mahler conjecture in dimension four and above. Even complete BS12 would be a major restricted-case advance, not `d_sym=4`.

This run is the first unchanged-source-metric follow-up after the executed STUCK1 recovery, but its remaining obligation has changed materially from an all-radial-chambers KKT contradiction to the exact aggregate BS12 inequality. It therefore does not repeat the previous stuck diagnosis or trigger STUCK2 on bookkeeping grounds.

## 11. Runtime/scheduler capability honesty

The exposed scheduler contract still provides task title/prompt, schedule or relative start, timing mode, and enabled state, but **no model selector, no reasoning-effort selector, no authenticated reasoning telemetry, and no guaranteed execution duration**. GPT-6/maximum is therefore prompt-requested only. The runtime available here identifies as GPT-5.6 Sol; the reasoning level is not exposed, so it is `UNVERIFIED`.

To make GPT-6/maximum a guaranteed scheduled property would require a product/runtime interface or authorized backend context exposing authenticated model and reasoning selectors. Repository policy cannot manufacture those controls.

The repository records historical `You cannot modify this task` errors for P26/P01/P03 in one permission context; the current root ledger separately records a later successful P26 update from another authorized context. The compliant workaround for a task that still refuses modification is to use the authorized task/account/workspace context or platform support, not to bypass permissions or create a duplicate schedule. This research run did not create, modify, disable, re-enable, or probe another schedule.

## 12. ledger_delta

```text
track: HARD7-01
target: MAHLER-SYMMETRIC-VOLUME-PRODUCT
owner: HARD7-01
status: PARTIAL / SOURCE OPEN
source_metric: d_sym
before: 3
after: 3
movement: NO MOVEMENT
methods: B21 / B25 / B30
new_auxiliary_result: generic Gale/box-spline identity |P||P^circ|=(2^n/n!)*sum_J N_J p_J
new_4d_reduction: V=12 generic/full-by-continuity iff sum_{j<k} N_jk p_jk >= 16
naive_route_refuted: pointwise p_J >= N_J/16 is false; exact generic pair J={2,4}
finite_self_check: PASS; ALL_EXACT_CHECKS_PASS=True
source_closure: NO
independent_audits: 0/2
shared_root_edit_requested: NO
```
