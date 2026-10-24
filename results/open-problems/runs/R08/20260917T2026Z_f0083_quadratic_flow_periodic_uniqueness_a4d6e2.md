Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT in active F0083: `1/2 -> 1/2`, supported unchanged count `4 -> 5`; I0082 remains RETIRED/FROZEN at `2/3`, retirement count `6`. The STUCK1-selected simplest special case is now solved: the periodic triple-corner tangent has an a.e. unique stable allocation. New stronger result: every appetite-one stable allocation is unique for every center set `Xi subset Z^3`, and more generally for the periodic quotient class proved below. Methods actually used: B3 PROVE SOMETHING STRONGER, B13 FIND WHAT ONLY INCREASES, B30 DO ONE SCALE / ONE DIRECTION AT A TIME.** GPT-6 / maximum was requested in prompt text, but the exposed runtime has no authenticated model-family selector, reasoning-effort selector, or completed-run telemetry, so I do not claim otherwise.

# R08 CLOSABLE OUTSIDE — F0083: a quadratic disagreement-capacity law, a square-root path obstruction, and uniqueness of the triple-corner tangent

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Hasebe--Ueda Problem 3.11 / I0082. The later six-unchanged handoff remains controlling despite the stale historical wording in `operations/claims/I0082.md`: the source is frozen for this worker at metric `2/3`, retirement count `6`. The old R08 FPP strict-convexity route also remains retired from this slot.

The active exclusive claim is still `operations/claims/F0083.md`, sourced to Christopher Hoffman, Alexander E. Holroyd and Yuval Peres, *A stable marriage of Poisson and Lebesgue*, Ann. Probab. 34 (2006), 1241--1272, arXiv:math/0505668, Open problem (i). The admitted appetite-one candidate is

\[
m_n=\lfloor(1+|n|)^{3/4}\rfloor,
\qquad
H=\{(n,a,b,c)\in\mathbb Z^4:1\le a,b,c\le m_n\},
\qquad
\Xi_*=\mathbb Z^4\setminus H.
\]

The frozen F0083 metric is the number of two obligations proved for this **exact** `Xi_*`:

1. candidate admissibility plus the exact local/transient mechanism — **PROVED**;
2. two stable appetite-one Lebesgue allocations of this exact `Xi_*` differing on positive measure — **OPEN**.

Thus the source-sized metric remains `1/2`. A theorem about a tangent model, even a complete one, does not count as obligation 2.

The preceding report `runs/R08/20260917T1930Z_f0083_stuck1_corner_recovery_3d7a91.md` was the required STUCK1 thinking-only report. It chose exactly one recovery: **prove the simplest unproved special case**, namely the periodic triple-corner tangent

\[
\Xi_{\rm corner}
=\mathbb Z\times\bigl(\mathbb Z^3\setminus\mathbb N_+^3\bigr)
\subset\mathbb R^4.
\tag{1.1}
\]

This run carries out that recovery completely. The frozen candidate metric nevertheless does not move, so the supported unchanged count is `4 -> 5`. Under the closable policy, one further unchanged run reaches the six-run retirement threshold for the admitted `Xi_*` route.

At run start I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, both R08 claim files, the newest R08 report, the F0083 intake / F0083-A001 attempt material, and the newest relevant neighboring R09 state. The current root `RESULTS.md` is explicitly stale for R-series research relative to these newer current-target reports, so this worker does not overwrite it. R09 remains separately owned and has no F0083 ownership overlap.

## 2. Fresh source, later-literature and ownership check

The primary 2006 HHP paper still contains the exact deterministic nonuniqueness question: whether there exists a discrete set of Euclidean centers admitting two stable Lebesgue allocations differing on a nonnull set. The paper's own necessary exclusions are that such a set must escape the recurrent-configuration theorem, have greater-than-quadratic growth, and not arise from a translation-invariant point process.

The primary source material used below was reread at the exact disagreement-flow argument. In HHP's notation, for two stable allocations `psi_1, psi_2`, the disputed set `D(xi)`, the preferred disputed set `N(xi)`, the set `M(xi)` of disputed sites preferring `xi`, and

\[
F(\xi,\eta)=N(\xi)\cap M(\eta)
\]

define a directed capacity graph with

\[
q(\xi,\eta)=\mathcal L F(\xi,\eta).
\]

HHP Lemma 8 says `L F(xi,xi)=0`; Lemma 9 gives strict decrease of the relevant distances along a disagreement edge; Lemma 10 gives acyclicity; Lemma 11 gives increasing capacity

\[
\sum_\zeta q(\zeta,\xi)\le \sum_\eta q(\xi,\eta);
\tag{2.1}
\]

and Lemma 12 gives bounded edges and summability of `q` along a directed path. Their Proposition 13 builds a unit flow below the capacities by max-flow/min-cut and decomposes an acyclic unit flow into a probability measure on directed rays.

Fresh bounded searches dated 2026-09-17 used the exact source title/authors and the phrases `two stable allocations`, `discrete set of centers`, `Lebesgue`, `deterministic nonuniqueness`, together with later stable-allocation / balancing-allocation terminology. They recovered the original HHP source, the HHP 2009 *Tail Bounds for the Stable Marriage of Poisson and Lebesgue*, later Poisson/random-appetite work, and recent related balancing-allocation literature. I found no later primary paper claiming to resolve this exact deterministic Euclidean-Lebesgue nonuniqueness question, and no inspected source stating the lattice-subset or periodic-quotient uniqueness theorems proved below. This is **bounded negative evidence only**: worldwide open status and publication novelty remain **UNVERIFIED**.

Repository ownership remains exclusive to R08 through `operations/claims/F0083.md`. Exact-ID/source searches found no competing current owner.

## 3. Preserved theorem: every appetite-one lattice-subset territory is local

I use the theorem proved in the F0083 admitting report and do not reprove it here.

### Preserved lattice-subset radius cap

Let `Xi subset Z^d`, appetite `1`. In **every** stable allocation, every center is sated and its territory has essential radius at most

\[
R_d=\frac{\sqrt d}{2}.
\tag{3.1}
\]

The proof compares the site-optimal allocation after deleting centers with the full-lattice unit-cube allocation, using HHP Proposition 21, and then sandwiches every stable allocation using HHP Lemma 15.

For the present run, (3.1) has a second consequence not used before: it bounds HHP's disagreement threshold `r(xi)` itself. Recall

\[
r(\xi)
=\sup\left\{r:\mathcal L\bigl[(\psi_1^{-1}(\xi)\cup\psi_2^{-1}(\xi))\cap B(\xi,r)\bigr]<1\right\}.
\tag{3.2}
\]

Since each of the two territories already has volume one inside `B(xi,R_d)`, the union has volume at least one there. Therefore

\[
0\le r(\xi)\le R_d.
\tag{3.3}
\]

The bounded scalar `r(xi)` will be the monovariant in B13.

## 4. B3 + B13 — prove a stronger local law: disagreement capacity is quadratic in the drop of `r`

The previous reports used HHP's qualitative fact that distance decreases along directed disagreement paths. The new step is to quantify how much **Lebesgue capacity** can cross an edge whose `r`-drop is small.

### Theorem 4.1 — strict `r` potential and quadratic capacity law

Let `d>=3`, let `Xi subset Z^d`, appetite one, and let `psi_1, psi_2` be two stable allocations. Construct the HHP disagreement capacities

\[
q(\xi,\eta)=\mathcal L F(\xi,\eta).
\]

For every directed edge `xi -> eta` with `q(xi,eta)>0`, put

\[
\Delta_{\xi\eta}=r(\xi)-r(\eta).
\]

Then

\[
\boxed{\Delta_{\xi\eta}>0}
\tag{4.1}
\]

and

\[
\boxed{
q(\xi,\eta)
\le C_d\,\Delta_{\xi\eta}^{\,2},
\qquad
C_d=\sigma_{d-2}R_d^{\,d-1},
\qquad R_d=\frac{\sqrt d}{2},
}
\tag{4.2}
\]

where `sigma_{d-2}` is the surface area of the unit sphere `S^{d-2}`. In particular, for `d=4`,

\[
C_4=4\pi,
\qquad
q(\xi,\eta)\le4\pi\,[r(\xi)-r(\eta)]^2.
\tag{4.3}
\]

#### Proof of the strict potential

Take a.e. `x in F(xi,eta)`. Since `x in N(xi)`,

\[
|x-\xi|<r(\xi).
\tag{4.4}
\]

Since `x in M(eta)`, and HHP Lemma 8 says `N(eta) cap M(eta)` is null, we may also require `x notin N(eta)`. But `M(eta) subset D(eta)`, hence

\[
|x-\eta|\ge r(\eta).
\tag{4.5}
\]

HHP Lemma 9(i) gives

\[
|x-\xi|>|x-\eta|.
\tag{4.6}
\]

Combining (4.4)--(4.6),

\[
r(\xi)>|x-\xi|>|x-\eta|\ge r(\eta),
\]

which proves (4.1). Thus the already-existing HHP acyclicity has, for lattice subsets, a concrete bounded potential `r` that decreases strictly on every positive-capacity edge.

#### Proof of the quadratic capacity bound

Write

\[
a=|x-\xi|,
\qquad b=|x-\eta|,
\qquad L=|\xi-\eta|.
\]

The preceding inequalities imply

\[
r(\eta)\le b<a<r(\xi),
\tag{4.7}
\]

so both `a` and `b` lie in an interval of length `Delta_{xi eta}`. Since the centers are distinct lattice points,

\[
L\ge1.
\tag{4.8}
\]

Use bipolar coordinates with `xi=0` and `eta=(L,0,...,0)`. Write a point as `(s,z)` with `rho=|z|`. Then

\[
a^2=s^2+\rho^2,
\qquad
b^2=(s-L)^2+\rho^2.
\]

The Jacobian of `(s,rho) -> (a,b)` is

\[
\left|\frac{\partial(a,b)}{\partial(s,\rho)}\right|
=\frac{\rho L}{ab}.
\tag{4.9}
\]

The Euclidean volume element is

\[
dx=\sigma_{d-2}\rho^{d-2}\,d\rho\,ds,
\]

so for `d>=3`,

\[
dx
=\frac{\sigma_{d-2}}{L}\,ab\,\rho^{d-3}\,da\,db.
\tag{4.10}
\]

By the inherited radius cap and (4.7),

\[
a,b,\rho\le R_d,
\]

and by (4.8), `1/L<=1`. Hence the density in (4.10) is bounded above by

\[
\sigma_{d-2}R_d^{d-1}=C_d.
\tag{4.11}
\]

The set `F(xi,eta)` is contained, modulo null sets, in the bipolar rectangle

\[
(a,b)\in[r(\eta),r(\xi)]^2,
\]

whose area is `Delta_{xi eta}^2`. Integrating (4.11) gives (4.2). QED.

### Corollary 4.2 — a square-root path budget

For every directed HHP disagreement path

\[
\xi_0\to\xi_1\to\xi_2\to\cdots,
\]

we have

\[
\boxed{
\sum_{i\ge0}\sqrt{q(\xi_i,\xi_{i+1})}
\le
\sqrt{C_d}\sum_{i\ge0}[r(\xi_i)-r(\xi_{i+1})]
\le
\sqrt{C_d}\,R_d.
}
\tag{4.12}
\]

This is strictly stronger than the source's `sum q < infinity` conclusion for this lattice-subset setting. The point is not the numerical constant: it is the exponent `1/2` on the capacity.

### A second useful consequence: uniformly bounded edge length

For `x in F(xi,eta)`,

\[
|\xi-\eta|
\le |x-\xi|+|x-\eta|<2R_d.
\tag{4.13}
\]

Thus the disagreement graph is automatically finite-range in the ambient lattice, with a range depending only on `d`.

This completes B13: the bounded potential `r` is not merely monotone; its total variation controls the **square root** of every edge capacity.

## 5. B30 — localize the flow obstruction by ambient dimension

The new square-root budget interacts sharply with the number of possible ways a finite-range path can cross a large box. This produces a dimension threshold that the original `sum q` argument does not see.

### Lemma 5.1 — no increasing-capacity flow with a square-root path budget in lattice dimension at most three

Let `D<=3`. Let `H=(V,E)` be a locally finite directed graph with `V subset Z^D`, uniformly bounded edge range, no directed cycles, and a nonzero capacity function `q:E->[0,infinity)` such that

\[
\sum_{u:(u,v)\in E}q(u,v)
\le
\sum_{w:(v,w)\in E}q(v,w)
\tag{5.1}
\]

at every non-source vertex of the forward component, and suppose there is a constant `K<infinity` such that every directed ray in that component obeys

\[
\sum_{e\in\gamma}\sqrt{q(e)}\le K.
\tag{5.2}
\]

Then such a nonzero `q` cannot exist.

#### Proof

Choose a positive-capacity edge entering a vertex `rho`, and take the forward-reachable directed component from `rho`. All outgoing edges of a reached vertex are included, so deleting outside incoming edges preserves (5.1). Let

\[
Q_0=\sum_{w:(\rho,w)\in E}q(\rho,w)>0.
\]

Normalize capacities by `Q_0`. The max-flow/min-cut step used in HHP's proof of Proposition 13 yields a unit flow `f` dominated by the normalized capacities. Since the graph is acyclic, the path-decomposition step used in the same proof yields a probability measure `mu` on infinite directed rays from `rho` and an acyclic unit flow `f_0<=f` with

\[
f_0(e)=\mu\{\gamma:e\in\gamma\}.
\tag{5.3}
\]

Consequently

\[
q(e)\ge Q_0 f_0(e)
=Q_0\,\mu\{\gamma:e\in\gamma\}.
\tag{5.4}
\]

Because the graph is locally finite and acyclic, every such infinite ray eventually exits every finite box.

Let `B_n` be the `ell_infinity` ball of radius `n` around `rho`, and let `E_n(gamma)` be the first edge by which the ray `gamma` exits `B_n`. Let `mathcal E_n` denote the set of possible first-exit edges and

\[
p_e=\mu\{E_n=e\},\qquad e\in\mathcal E_n.
\]

If the edge range is at most `B`, the tail of a first-exit edge lies in the thickness-`B` lattice shell of `B_n`. Hence, for a constant depending only on `D` and `B`,

\[
N_n:=|\mathcal E_n|\le C_{D,B}(1+n)^{D-1}.
\tag{5.5}
\]

Since `{E_n=e}` implies that the ray uses `e`, (5.4) yields

\[
q(e)\ge Q_0 p_e.
\tag{5.6}
\]

Therefore

\[
\begin{aligned}
\mathbb E_\mu\sqrt{q(E_n)}
&=\sum_{e\in\mathcal E_n}p_e\sqrt{q(e)}\\
&\ge \sqrt{Q_0}\sum_{e\in\mathcal E_n}p_e^{3/2}\\
&\ge \sqrt{Q_0}\,N_n^{-1/2}\\
&\ge c(1+n)^{-(D-1)/2}.
\end{aligned}
\tag{5.7}
\]

The penultimate inequality is the convexity/Hölder bound `sum p_e^(3/2)>=N_n^(-1/2)`.

For `D<=3`,

\[
\sum_{n\ge1}(1+n)^{-(D-1)/2}=\infty.
\tag{5.8}
\]

On the other hand, a fixed directed edge of range at most `B` can be the first exit edge for at most `B` consecutive integer radii `n`. Therefore every ray satisfies

\[
\sum_{n\ge1}\sqrt{q(E_n(\gamma))}
\le B\sum_{e\in\gamma}\sqrt{q(e)}
\le BK.
\tag{5.9}
\]

Taking `mu`-expectations in (5.9) contradicts the divergent lower bound obtained by summing (5.7). QED.

### Why the threshold is exactly three

The shell estimate in dimension `D` contributes

\[
N_n^{-1/2}\asymp n^{-(D-1)/2}.
\]

This is non-summable exactly for `D<=3`. In `D=4` it is `n^{-3/2}`, which is summable. Thus the new quadratic capacity law naturally singles out **four dimensions as the first lattice dimension in which the HHP disagreement-flow mechanism can evade this argument**.

That is not a proof of nonuniqueness in dimension four. It is a sharp explanation of why the present `Z^4` candidate sits at the first dimension not automatically eliminated by this route.

## 6. Stronger theorem: every `Z^3` lattice subset is stable-allocation unique

The preceding two results immediately close an entire deterministic class.

### Theorem 6.1 — arbitrary lattice subsets in dimensions at most three

Let

\[
\Xi\subset\mathbb Z^3
\]

be arbitrary, with appetite one. Then its stable Lebesgue allocation is unique a.e.

The same conclusion holds for subsets of `Z` and `Z^2`; those lower dimensions can also be reached by older recurrence/one-dimensional arguments.

#### Proof in `Z^3`

Suppose two stable allocations differ on positive measure. Their HHP disagreement graph has a positive-capacity edge. By Theorem 4.1, its capacities satisfy the uniform square-root path budget (4.12), and by (4.13) its edges have uniformly bounded lattice range. HHP Lemma 11 gives the increasing-capacity inequality (5.1), and Theorem 4.1 gives strict decrease of `r`, hence acyclicity. The forward component of any positive edge is therefore a graph of the type excluded by Lemma 5.1 with `D=3`. Contradiction. QED.

### Precise strengthening of the source's geometric exclusion

HHP's recurrent-graph theorem does **not** cover arbitrary subsets of `Z^3`: the full three-dimensional lattice and many deterministic subgraphs are transient. The new proof is different. It uses the quantitative coupling between capacity and the bounded disagreement potential.

A useful formulation of the new necessary condition is:

> In the appetite-one lattice-subset class, a deterministic counterexample cannot be embedded with finite-range disagreement geometry in an ambient lattice of dimension at most three. More generally, a forward disagreement component whose thickness-`B` box shells contain only `O(n^2)` possible crossing-edge tails is impossible.

I deliberately do **not** replace this by the looser slogan “growth must be supercubic”: an `O(R^3)` ball-volume statement alone does not automatically give the required `O(R^2)` shell bound without additional regularity. The shell formulation above is the proved statement.

## 7. Solve the STUCK1 special case: periodic quotient dimension at most three is unique

The selected corner tangent (1.1) is four-dimensional, so Theorem 6.1 does not apply directly. But it has one exact translation symmetry. Quotienting that symmetry leaves a three-dimensional lattice subset. The new capacity estimate survives this quotient.

### Theorem 7.1 — periodic-quotient uniqueness

Let `d>=3` and suppose

\[
\Xi=\mathbb Z^k\times Q\subset\mathbb Z^d,
\qquad
Q\subset\mathbb Z^D,
\qquad
D=d-k\le3,
\tag{7.1}
\]

with appetite one. Then `Xi` has an a.e. unique stable Lebesgue allocation.

#### Step 1: it suffices to compare the two Gale--Shapley extremals

Let `psi^s` and `psi^c` be the site-optimal and center-optimal HHP allocations. HHP Lemma 15 sandwiches every stable allocation between them in site distance and center radial cumulative territory. If `psi^s=psi^c` a.e., then every stable allocation has the same allocated distance at a.e. site. Away from the countable union of pairwise bisectors, equal distance determines the same center. Thus equality of the two extremals implies full a.e. uniqueness.

Assume for contradiction that the extremals differ.

#### Step 2: the disagreement data are periodic

HHP's two Gale--Shapley constructions are isometry-equivariant. Since `Xi` is invariant under translation by `Z^k` in the first coordinates, both extremal allocations are invariant under those translations. Therefore `D,N,M,r,F`, and the capacities `q`, are periodic in the same directions.

Write a center as `(z,u)` with `z in Z^k` and `u in Q`. For transverse quotient vertices `u,v in Q`, define

\[
\bar q(u,v)
=
\sum_{z\in\mathbb Z^k}
q\bigl((0,u),(z,v)\bigr).
\tag{7.2}
\]

By (4.13), a positive lift has Euclidean length `<2R_d`, so only finitely many `z` can contribute. In fact the number of possible contributing periodic displacements is bounded uniformly by a constant `M=M(d,k)`.

Similarly define the quotient potential

\[
\bar r(u)=r((0,u)).
\]

#### Step 3: increasing capacity descends to the quotient

Translation invariance lets us regroup the HHP Lemma 11 sums by quotient orbit. For every `v in Q`,

\[
\sum_u\bar q(u,v)
\le
\sum_w\bar q(v,w).
\tag{7.3}
\]

Every positive quotient edge has

\[
\bar r(u)>\bar r(v),
\tag{7.4}
\]

because every positive lift has the strict `r` drop of Theorem 4.1. In particular there are no quotient self-loops or directed cycles.

#### Step 4: the square-root path budget also descends

Every lift contributing to the quotient edge `u->v` has the same potential drop

\[
\Delta=\bar r(u)-\bar r(v).
\]

By Theorem 4.1, each lift has capacity at most `C_d Delta^2`, and at most `M` lifts contribute. Hence

\[
\bar q(u,v)\le M C_d\,[\bar r(u)-\bar r(v)]^2.
\tag{7.5}
\]

Therefore every directed quotient path obeys

\[
\sum_i\sqrt{\bar q(u_i,u_{i+1})}
\le
\sqrt{M C_d}\sum_i[\bar r(u_i)-\bar r(u_{i+1})]
\le
\sqrt{M C_d}\,R_d.
\tag{7.6}
\]

The quotient graph has finite range in `Q subset Z^D`. Since the original disagreement is nonzero, `bar q` has a positive edge. Choose such an edge and restrict to its forward component. Equations (7.3)--(7.6) put that component exactly under Lemma 5.1. But `D<=3`, so Lemma 5.1 says no nonzero capacity can exist. Contradiction.

Thus the two Gale--Shapley extremals coincide, and Step 1 gives a.e. uniqueness of every stable allocation. QED.

### Corollary 7.2 — the periodic triple-corner tangent is unique

Take

\[
d=4,
\qquad k=1,
\qquad
Q=\mathbb Z^3\setminus\mathbb N_+^3.
\]

Then (7.1) is exactly

\[
\Xi_{\rm corner}
=\mathbb Z\times(\mathbb Z^3\setminus\mathbb N_+^3).
\]

Therefore

\[
\boxed{
\Xi_{\rm corner}\text{ has an a.e. unique stable appetite-one Lebesgue allocation.}
}
\tag{7.7}
\]

This completely resolves the special case selected in the preceding STUCK1 report. In the notation of that report,

\[
D_{\rm corner}=0.
\tag{7.8}
\]

The conclusion is stronger than the previous symmetry-reduced recurrence test. That earlier test stopped at the corner because the three-dimensional quotient is transient. The present argument does **not** need recurrence: it combines the lattice radius cap with the quadratic capacity law, and the resulting square-root path budget is still too strong to support a nonzero increasing flow in three quotient dimensions.

## 8. What this does — and does not — say about the admitted `Xi_*`

This run closes the recovery special case but **does not** prove obligation 2 for the nonperiodic expanding tube `Xi_*`.

The implications for the route are now unusually sharp:

1. the flat half-space tangent is unique;
2. periodic face and edge tangents are unique;
3. the periodic triple-corner tangent is now unique as well;
4. in fact every product-periodic tangent whose symmetry quotient has dimension at most three is unique;
5. every arbitrary appetite-one subset of `Z^3` is unique;
6. the first ambient lattice dimension not excluded by the square-root flow obstruction is `4`.

Thus no autonomous periodic local tangent of the tube supplies the missing second phase. If the exact admitted `Xi_*` is nonunique, the mechanism must be genuinely **nonperiodic and four-dimensional**, using the slowly varying tube width, its two ends, or another global boundary-at-infinity feature that disappears under every periodic tangent limit.

This also explains why the earlier finite-energy channel was insufficient. Finite electrical energy is a graph-level transience condition. Stable-allocation disagreement in a lattice subset must obey the stronger nonlinear constraint

\[
q(e)\lesssim [\Delta r(e)]^2,
\qquad
\sum_{e\in\gamma}\sqrt{q(e)}<\infty.
\tag{8.1}
\]

In effective dimensions at most three, (8.1) and increasing capacity are incompatible. In effective dimension four, the shell lower bound becomes summable, so the contradiction disappears exactly where `Xi_*` lives.

## 9. Method accounting

### B3 — PROVE SOMETHING STRONGER

Instead of merely deciding the corner tangent, I asked whether the source's HHP flow could be ruled out on **every** lattice subset of effective dimension at most three. The answer is yes: Theorems 4.1, 6.1 and 7.1 prove the stronger class statement, and the corner tangent becomes an immediate corollary.

### B13 — FIND WHAT ONLY INCREASES

The key monovariant is HHP's own threshold `r(xi)`, now bounded globally by the inherited lattice radius cap. Along every positive disagreement edge it decreases strictly. Bipolar coordinates upgrade this qualitative drop into the quadratic estimate `q<=C(Delta r)^2`. This is the decisive new ingredient.

### B30 — ONE SCALE / ONE DIRECTION AT A TIME

I localized the resulting flow at successive `ell_infinity` box boundaries. The count of possible first-exit edges is `O(n^{D-1})`; the square-root capacity lower bound on a random first-exit edge is therefore `Omega(n^{-(D-1)/2})`. Summing scale by scale creates the exact `D=3` versus `D=4` threshold.

These methods are distinct from the preceding run's B2/B18/B24 triple.

## 10. Validation, limitations, and novelty discipline

No finite enumeration or finite arithmetic claim is central to the new result, so I did **not** manufacture a checker merely to create an artifact. The proof is analytic and is written on the page.

Important limitations:

- The quadratic bound (4.2) uses lattice separation `|xi-eta|>=1`; it is not asserted for arbitrary discrete sets with no uniform separation.
- The bounded bipolar density argument is stated for `d>=3`. Lower dimensions are not needed for the new threshold theorem.
- Lemma 5.1 uses a finite-range embedding in `Z^D` with `D<=3`; arbitrary cubic ball-growth alone is not substituted for the proved shell-count hypothesis.
- The periodic quotient theorem applies to exact product-periodic center sets. It does not automatically transfer to the slowly varying nonperiodic tube.
- None of these restricted uniqueness theorems resolves the HHP source question, which is existential over all discrete Euclidean center sets.
- I found no inspected prior source stating these exact results, but the mechanism combines the source's disagreement flow with standard bipolar coordinates and standard flow/path decomposition. Publication novelty is therefore **UNVERIFIED**, not claimed.

## 11. Metric, stagnation, and next allowed move

The frozen source-sized F0083 metric remains

\[
\boxed{1/2\to1/2}.
\]

Supported unchanged count is now

\[
\boxed{4\to5}.
\]

The STUCK1 recovery itself succeeded — the selected corner tangent is decided — but the fixed candidate obligation did not move. Under the closable policy, the next unchanged run would be the sixth and therefore must retire/handoff the exact `Xi_*` route rather than generate another tangent lemma.

Accordingly, the next research invocation should attack the **actual nonperiodic `Xi_*`** directly. The most informative distinct triple would be:

- **B6 DEFORM TO A POINT YOU CAN SOLVE:** treat the slowly varying tube as long blocks of product-periodic geometries and quantify the defect introduced at the rare width-change layers;
- **B12 FIND WHAT IS CONSERVED:** use the new square-root path budget together with HHP increasing capacity to derive a global flux inequality across tube-axis cuts;
- **B29 ADD THE POINTS AT INFINITY:** determine whether a genuine four-dimensional end flow can survive the blockwise screening and produce a positive extremal-allocation separation.

If that direct attack leaves obligation 2 unchanged, write the immutable six-run handoff and rotate to the next eligible closable outside target rather than extending `Xi_*` again.

## 12. Model / scheduler-control status

The exposed task-management surface still provides prompt/title/schedule/timing/enabled controls but **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. I therefore cannot truthfully certify GPT-6/maximum from this runtime and made no scheduler modification.

The repository's current operations note records that historical `You cannot modify this task` responses, including the old P26 probe in one context, are authorization-context boundaries; a later authorized context succeeded for P26. The legitimate remedies are the authorized owning context, supported ownership/admin transfer, or platform support. Repository edits or duplicate tasks do not enforce a model selection and are not a workaround.

## 13. Structured ledger delta

```yaml
ledger_delta:
  worker: R08
  original_target:
    id: I0082
    source: Hasebe_Ueda_Problem_3_11
    state: RETIRED_FROZEN
    metric_before: "2/3"
    metric_after: "2/3"
    retirement_count: 6
    reopened: false
  active_target:
    id: F0083
    source: Hoffman_Holroyd_Peres_2006_Open_problem_i
    owner: R08
    claim: operations/claims/F0083.md
    candidate: "Xi_* = Z^4 minus expanding m_n^3 positive-octant tube"
    status_before: PARTIAL_OPEN_STUCK1
    status_after: PARTIAL_OPEN
    source_status: OPEN_CURRENT_BOUNDED
    novelty: UNVERIFIED
    metric_name: "frozen obligations proved for exact Xi_*"
    metric_before: "1/2"
    metric_after: "1/2"
    movement: false
    supported_unchanged_before: 4
    supported_unchanged_after: 5
    closure: false
    audits_requested: false
  stuck_recovery:
    selected_special_case: "Xi_corner = Z x (Z^3 minus N_+^3)"
    result: PROVED_UNIQUE_AE
    recovery_episode: 1
    source_metric_movement: false
  new_theorem_claims:
    - "For Xi subset Z^d, d>=3, HHP disagreement edges satisfy r(source)>r(target) and q<=C_d (Delta r)^2."
    - "Hence every directed disagreement path has a uniform sum sqrt(q) budget."
    - "No nonzero increasing-capacity finite-range acyclic flow embedded in Z^D, D<=3, can have a uniform sum sqrt(q) path budget."
    - "Every appetite-one stable allocation for every Xi subset Z^3 is unique a.e."
    - "Every product-periodic Xi=Z^k x Q subset Z^d with quotient dimension d-k<=3 is unique a.e."
    - "In particular the periodic triple-corner tangent selected at STUCK1 is unique a.e."
  methods_actual:
    - B3
    - B13
    - B30
  finite_claim_checker_created: false
  reason_no_checker: "new core is theorem-sized analytic geometry/flow argument, not a finite enumeration"
  shared_roots_edited: false
  peer_files_edited: false
  next_if_unchanged: "six-run immutable handoff and rotate; do not add another tangent lemma"
```
