Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. MOVEMENT: `A_triangle` UNMEASURED -> exactly `(1/4, infinity)`; Section-B methods actually tried: #2, #5, #12.**

# NM13-08 — P0408 first attack: finite injectivity obstructions

Date: 2026-09-17 UTC  
Track: NM13-08  
Category: CLOSABLE OUTSIDE  
Repository: `yspennstate/math-open-problems`, `master`  
Own namespace: `proofnet24/NM13-08/`

## 1. Admission and source fidelity

This run continued the admission screen from the previous NM13-08 report rather than restarting it. The previous run left the target UNADMITTED and advanced its cursor beyond already-owned or wrong-category shard-7 rows.

The selected canonical target is **P0408**:

- canonical dedup key: `recovering_an_ideal_voronoi_tessellation_from_vertices_or_its_dual`;
- exact shard check: `int(SHA256(UTF-8 dedup_key).hexdigest(),16) mod 13 = 7`;
- source: Matteo D'Achille, Nicolas Curien, Nathanaël Enriquez, Russell Lyons, Meltem Ünel, *Ideal Poisson–Voronoi tessellations on hyperbolic spaces*, Ann. Probab. 54(2) (2026), 846–891, DOI 10.1214/25-AOP1781;
- exact source locator: Question 7.2, “Equivariant injectivity”;
- exact source target: determine whether (i) the map sending the hyperbolic IPVT to its set of vertices is almost surely injective and (ii) the map sending the IPVT to its ideal Poisson–Delaunay tessellation (IPDT) is almost surely injective.

The current journal paper and the source formulae were re-read. In the Poincaré ball model, for an ideal nucleus `(theta,r)`, the source separation is

\[
 d\bigl(z,(\theta,r)\bigr)=\frac{r}{K(z,\theta)},\qquad
 K(z,\theta)=\left(\frac{1-|z|^2}{|z-\theta|^2}\right)^{d-1}.
\]

Thus in `H^2`, comparison of nuclei is comparison of

\[
 r_i |z-\theta_i|^2,
\]

because the common factor `1-|z|^2` cancels. This is the exact source geometry used below; no Euclidean Voronoi substitute is silently introduced.

### Fresh current-literature screen, 2026-09-17

Queries included the exact phrase `"Equivariant injectivity" "Ideal Poisson" Voronoi`, the source title plus `Question 7.2`, and combinations of the source authors with `injectivity`, `vertices`, and `Delaunay`. The current bounded retrieval found:

1. the 2026 Annals publication of the source;
2. Sam Mellick's 2026 *Proceedings AMS* paper proving cell indistinguishability for the IPVT, a different source question;
3. D'Achille–Thäle, arXiv:2606.26049 (24 June 2026), determining face-volume densities and typical face volumes, not Question 7.2;
4. D'Achille–Khezeli, arXiv:2606.30517 (29 June 2026), convergence toward IPVTs beyond hyperbolic space and Diestel–Leader applications, not a resolution of Question 7.2;
5. later Voronoi-percolation work using IPVT geometry, again not the injectivity question.

No source-matching later resolution of Question 7.2 was recovered. This is a bounded dated search, **not** a claim of worldwide bibliographic completeness or publication novelty.

### Ownership and history

The historical P0408 intake/attempt was recovered. Its previous idea was a quantitative local-decoding route; it explicitly did **not** construct a decoder and did not solve the source question. Immediately before claiming, `operations/claims/P0408.md` was absent and exact-key repository searches exposed intake/catalog material but no live ProofNet24 owner. The source is absent from the current POSTED/settled exclusions. Distinct IPVT questions P0423 (face-volume density) and P0424 (cell indistinguishability) are not aliases of P0408. The current I0079 ideal-Bernoulli-Voronoi assignment is also a different source problem.

Canonical create-only ownership was therefore acquired at:

- `operations/claims/P0408.md`
- creation commit `970b3c090560f6196ab41e002a0b1f7f4898e07e`
- verified blob `cf9c95641e0fc9bdd499d0a6228e8adbc7c643e1`.

The claim was read back at its creation commit before mathematical work proceeded.

## 2. Frozen source and metric

The full source remains both almost-sure injectivity questions above. The finite results below are **PARTIAL** and are not substituted for the infinite Poisson problem.

The first-attack metric was frozen in the claim as

\[
A_{\triangle}:=\{a>0:\text{the three-nucleus }H^2\text{ finite ideal-Voronoi analogue with}
\]
\[
\theta_1=1,\quad \theta_2=e^{2\pi i/3},\quad \theta_3=e^{4\pi i/3},
\quad(r_1,r_2,r_3)=(a,1,1)
\]
\[
\text{has the same full ideal-Delaunay triangle while its Voronoi diagram varies with }a\}.
\]

Before: `UNMEASURED`.  
After: **exactly**

\[
\boxed{A_{\triangle}=(1/4,\infty).}
\]

This is a genuine source-relevant obstruction metric: it measures precisely where a fixed finite IPDT loses the radial information needed to reconstruct the corresponding ideal Voronoi diagram.

## 3. Method #2 — attack the negation first

### Idea before code

If IPDT data were locally sufficient to recover an IPVT, then in the smallest nontrivial finite source-faithful model the ideal-Delaunay simplex should strongly constrain the radial marks. I therefore tried to make the **same** ideal Delaunay triangle arise from a continuum of different radial marks and different Voronoi diagrams.

### Theorem 1 — sharp one-parameter finite IPDT noninjectivity

Let the three boundary directions in the Poincaré disk be

\[
\theta_1=(1,0),\quad
\theta_2=(-1/2,\sqrt3/2),\quad
\theta_3=(-1/2,-\sqrt3/2),
\]

with radial marks `(a,1,1)`, `a>0`. Then:

1. the three ideal Voronoi cells have a common interior vertex iff `a>1/4`;
2. for every `a>1/4`, the full finite IPDT is the same ideal triangle with ideal vertices `theta_1,theta_2,theta_3`;
3. the finite ideal Voronoi diagrams are pairwise distinct as `a` varies over `(1/4,infinity)`.

Hence `A_triangle=(1/4,infinity)`.

### Proof

Write `z=(x,y)`. Since nuclei 2 and 3 have equal marks, equality of their source separation scores gives

\[
|z-\theta_2|^2=|z-\theta_3|^2,
\]

which, by reflection symmetry, is equivalent to `y=0`. Thus every common triple point must lie on the horizontal diameter, say `z=(x,0)`, `-1<x<1`.

Along that diameter,

\[
|z-\theta_1|^2=(x-1)^2,
\]

while

\[
|z-\theta_2|^2=|z-\theta_3|^2=x^2+x+1.
\]

The triple-equality condition is therefore exactly

\[
a(x-1)^2=x^2+x+1. \tag{1}
\]

Solving for the parameter gives

\[
a=a(x):=\frac{x^2+x+1}{(x-1)^2}.
\]

Its derivative is

\[
a'(x)=-\frac{3(x+1)}{(x-1)^3}>0\qquad(-1<x<1).
\]

Moreover

\[
\lim_{x\downarrow-1}a(x)=\frac14,
\qquad
\lim_{x\uparrow1}a(x)=+\infty.
\]

Thus `a(x)` is a bijection from `(-1,1)` onto `(1/4,infinity)`. For each `a>1/4` there is exactly one common interior vertex `z_a=(x(a),0)`. At the threshold,

\[
F(1/4,x):=\tfrac14(x-1)^2-(x^2+x+1)
=-\frac34(x+1)^2,
\]

so the only common point is the ideal boundary point `x=-1`, not a hyperbolic Voronoi vertex. For `a<1/4`, no interior common point exists. Equivalently, the quadratic discriminant in `x` is `3(4a-1)`.

When `a>1/4`, there are only three nuclei and all three cells meet at `z_a`, so the dual complex contains the full ideal triangle on the fixed ideal directions `theta_1,theta_2,theta_3`; with only three nuclei, this is the full finite ideal-Delaunay 2-simplex. The IPDT therefore does not change with `a`.

But the Voronoi diagram does change: `a'(x)>0` makes `x(a)` strictly increasing, so distinct `a` give distinct triple vertices and hence distinct tessellations. This proves all three assertions and the sharp metric value.

**Status:** PROVED for this finite source-faithful `H^2` analogue; **PARTIAL** relative to source Question 7.2(ii).

## 4. Method #5 — add a parameter and differentiate

The parameter `a` was not cosmetic: differentiating the exact inversion `a(x)` exposed the sharp transition. The route succeeded fully on the finite metric:

- `a<1/4`: no interior triple Voronoi vertex;
- `a=1/4`: a double equality point appears only at the ideal boundary `x=-1`;
- `a>1/4`: exactly one interior triple vertex, moving strictly with `a`;
- the dual ideal triangle is unchanged throughout the entire open interval.

Thus the parameter move converted a qualitative noninjectivity idea into the exact interval `(1/4,infinity)` rather than a sampled family or numerical picture.

## 5. Method #12 — find what is conserved

The conserved object in Theorem 1 is the finite IPDT: once the three fixed ideal directions have a common Voronoi vertex, the dual 2-cell is the same ideal triangle even though the radial marks and Voronoi vertex vary.

A second conserved object gives an independent finite obstruction for the **first** source map.

### Theorem 2 — finite vertex-set data do not determine the diagram

Consider equal radial marks and either of the two triples

\[
A=\{(1,0),(-1/2,\sqrt3/2),(-1/2,-\sqrt3/2)\},
\]

\[
B=\{(1,0),(0,1),(-1,0)\}.
\]

For both finite ideal-Voronoi systems, the complete set of triple Voronoi vertices is exactly `{0}`. Nevertheless the two Voronoi partitions are different.

### Proof

For equal marks in `H^2`, all cells compare `|z-theta_i|^2`. At `z=0`, every boundary point `theta` on the unit circle has distance squared 1, so all three cells meet at the origin.

For each displayed triple, subtracting the squared-distance equations for nucleus 1 from those for nuclei 2 and 3 gives two independent linear equations in the coordinates of `z`; exact solution yields only `z=0`. Hence the complete triple-vertex set is `{0}` in both cases.

The partitions are not equal. At the exact rational test point

\[
z_*=(-3/8,1/8),
\]

the squared distances to triple `A` are

\[
\left(\frac{61}{32},\frac{25}{32}-\frac{\sqrt3}{8},
\frac{25}{32}+\frac{\sqrt3}{8}\right),
\]

so `z_*` lies strictly in the cell of the second nucleus. For triple `B` the squared distances are

\[
\left(\frac{61}{32},\frac{29}{32},\frac{13}{32}\right),
\]

so `z_*` lies strictly in the cell of the third nucleus. Thus the diagrams differ while their vertex sets agree exactly.

**Status:** PROVED for finite source-faithful `H^2` analogues; **PARTIAL** relative to source Question 7.2(i).

## 6. What these theorems do — and do not — say about the source

They do **not** refute either almost-sure source statement. The actual IPVT is an infinite random tessellation generated by a Poisson process on the corona, and the source's reconstruction theorem for the full IPVT uses global information, including infinitely many cells and a tail normalization of radial marks. A finite deterministic configuration does not satisfy that global Poisson/tail structure.

They do establish a useful obstruction:

> Neither source injectivity question can be justified merely by saying that a finite local Voronoi/Delaunay star contains enough geometric information. Even in the exact source separation geometry, finite stars lose information in both directions: a fixed ideal-Delaunay simplex permits a continuum of different Voronoi diagrams, and a fixed finite vertex set can come from different Voronoi diagrams.

Therefore a positive source proof must exploit **global compatibility across infinitely many adjacent stars, the Poisson law/tail normalization, or another genuinely infinite invariant**. This narrows the remaining obligation and kills a natural local-decoding route.

## 7. Exact finite-core checker

The algebraic finite core was executed with exact symbolic arithmetic before archival. Artifacts:

- checker: `proofnet24/NM13-08/artifacts/2026-09-17/2026-09-17T21-35-50Z__p0408_finite_core.py`
  - creation commit `6d06ba19754f07c128fb612fcfc46efdf7014a08`
  - verified blob `a170d0f221ca594006f076df9fa248d36e376d93`;
- output: `proofnet24/NM13-08/artifacts/2026-09-17/2026-09-17T21-35-50Z__p0408_finite_core.out`
  - creation commit `a98826e395aa339f9a72130111b65d83c17be321`
  - verified blob `2b5c964b6ace0fa890b4172bba56637b3b89ad55`.

The output ends `ALL_EXACT_CHECKS_PASS` and verifies the discriminant, exact parameter derivative and endpoint, threshold factorization, unique common vertices of the two equal-radius triples, and the rational test-point cell assignments.

This checker supports only the finite algebra. The theorem-sized implications and their source-scope limitations are proved in writing above.

## 8. Attempt outcomes and movement

- **#2 ATTACK THE NEGATION FIRST — success (finite analogue):** constructed explicit source-faithful finite noninjectivity families for both kinds of retained data. This does not refute the infinite a.s. source statements.
- **#5 ADD A PARAMETER AND DIFFERENTIATE — success:** exact threshold `a=1/4`, with full interval `A_triangle=(1/4,infinity)`.
- **#12 FIND WHAT IS CONSERVED — success:** identified the fixed ideal-Delaunay triangle under radial deformation and the fixed vertex set `{0}` under angular deformation.

Metric movement:

\[
\boxed{A_{\triangle}:\ \mathrm{UNMEASURED}\longrightarrow(1/4,\infty).}
\]

This is movement on the frozen metric, not a claim of source closure.

Unchanged-run count for this admitted source: `0` after this run, because the frozen metric moved on the first attack.
Stuck-recovery count: `0`.

## 9. Remaining exact obligation and next route

The source-level obligation is unchanged in scope but sharper in mechanism:

1. For IPVT -> IPDT, prove or refute that the **infinite overlapping system** of ideal Delaunay simplices uniquely determines the compatible radial marks/Voronoi vertices almost surely, modulo the global scaling that leaves the IPVT unchanged and subject to the Poisson tail normalization.
2. For IPVT -> vertex set, prove or refute that the infinite vertex point set uniquely determines the cell adjacency/ideal ends almost surely, despite finite vertex sets being noninjective.

A natural algebraic reformulation for the next run is to attach an unknown hyperbolic vertex `z_tau` to each Delaunay simplex `tau` and radial variables `r_i` to ideal ends. Each incidence satisfies

\[
\log r_i-\log K(z_\tau,\theta_i)=c_\tau,
\]

with one common `c_tau` per simplex. Overlapping simplices share the `r_i`. The source injectivity question becomes a global rigidity/compatibility problem for this infinite equation system plus the point-process normalization. This formulation is not yet a theorem and receives no metric credit.

Next Section-B triple, if history shows it remains untried on P0408: **#14 FIND THE GROUP ACTING, #20 FIND WHY THE ALGORITHM FAILS, #29 ADD THE POINTS AT INFINITY.** Concretely: use Möbius normalization to quotient local degrees of freedom; formalize the exact failure mode of any finite decoder; then test whether boundary/tail conditions force uniqueness when stars are glued indefinitely.

## 10. Audits and closure

No independent audit is counted in advance. P26 is the required audit track for any closure package; NM13-09 is the designated distinct secondary partner. This run does not request closure because both source clauses remain OPEN.

No paper package was created. No public posting or novelty claim is made.

## 11. Model / scheduler controls

The current exposed scheduling interface still supplies title, prompt, schedule, enablement and timing mode, but no binding model selector or reasoning-effort selector. Therefore `GPT-6 / maximum` remains prompt text only. This run actually reports `GPT-5.6 Sol / reasoning UNVERIFIED`; no inference from the prompt is made. A binding change would require the platform or an authorized scheduler surface to expose model/reasoning controls. Historical modification denials for protected tasks are authorization boundaries; the lawful path is the owning account/workspace/admin or product support, never duplicate jobs or permission bypass.

## 12. `ledger_delta` for P26

```yaml
ledger_delta:
  track: NM13-08
  claim: P0408
  owner: NM13-08
  category: CLOSABLE_OUTSIDE
  source: "D'Achille-Curien-Enriquez-Lyons-Unel, Ideal Poisson-Voronoi tessellations on hyperbolic spaces, Question 7.2"
  source_status: OPEN_IN_BOUNDED_2026-09-17_SCREEN
  mathematical_status: PARTIAL
  source_clause_i_vertex_set: OPEN
  source_clause_ii_ipdt: OPEN
  metric_name: A_triangle
  metric_before: UNMEASURED
  metric_after: "(1/4, infinity) exactly"
  movement: true
  methods_tried: [2, 5, 12]
  unchanged_run_count: 0
  stuck_recovery_count: 0
  claim_path: operations/claims/P0408.md
  claim_creation_commit: 970b3c090560f6196ab41e002a0b1f7f4898e07e
  claim_blob: cf9c95641e0fc9bdd499d0a6228e8adbc7c643e1
  theorem_1: "For fixed cube-root ideal directions and marks (a,1,1), the full finite ideal-Delaunay triangle exists exactly for a>1/4 and is independent of a, while the Voronoi vertex moves strictly with a."
  theorem_2: "Two explicit equal-radius three-nucleus H^2 ideal-Voronoi diagrams have the same complete finite vertex set {0} but different cell partitions."
  exact_checker: proofnet24/NM13-08/artifacts/2026-09-17/2026-09-17T21-35-50Z__p0408_finite_core.py
  exact_checker_commit: 6d06ba19754f07c128fb612fcfc46efdf7014a08
  exact_checker_blob: a170d0f221ca594006f076df9fa248d36e376d93
  exact_output: proofnet24/NM13-08/artifacts/2026-09-17/2026-09-17T21-35-50Z__p0408_finite_core.out
  exact_output_commit: a98826e395aa339f9a72130111b65d83c17be321
  exact_output_blob: 2b5c964b6ace0fa890b4172bba56637b3b89ad55
  exact_output_status: ALL_EXACT_CHECKS_PASS
  p26_audit: NOT_REQUESTED_YET
  nm13_09_audit: NOT_REQUESTED_YET
  closure: false
  next_methods: [14, 20, 29]
```

**End of complete run report.**
