Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the scheduler exposes no authenticated applied-effort selector, so I do not claim GPT-6 maximum.**

# PROB10-04 — exact normal-fan outer compiler and quantitative entropy-face access

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL**.

## 0. Exact source model and source metric before / after

The source model remains classical independent proper random 3-SAT: `n` Boolean variables, `m=floor(alpha n)` independent clauses, each clause uniformly choosing three distinct variables and independent fair signs.

A fresh bounded source check in this run reconfirmed the directly auditable explicit rigorous endpoints:

- Hajiaghayi--Sorkin, <https://arxiv.org/abs/math/0310193>: satisfiable w.h.p. for density below `3.52`;
- Díaz--Kirousis--Mitsche--Pérez-Giménez, <https://arxiv.org/abs/0807.3600> and the FSTTCS paper: a.a.s. unsatisfiable at density at least `4.4898`.

Gaia Carenini, ECCC TR26-145, publication 16 August 2026, <https://eccc.weizmann.ac.il/report/2026/145/>, proves an `O(n/log n)` scaling-window width in clause count for every fixed `k>=3`. This is a sharp-window statement, not identification or convergence of a limiting `k=3` center. Ding--Sly--Sun, <https://arxiv.org/abs/1411.0650>, prove the limiting threshold for all sufficiently large `k`, not automatically `k=3`. ESA 2025 paper 103, <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103>, explicitly studies `k`-wise-independent clauses and is not substituted for the iid model.

Therefore the externally validated source metric is unchanged:

\[
\boxed{[3.52,4.4898]\longrightarrow[3.52,4.4898]},
\qquad
\boxed{W_{source}:0.9698\longrightarrow0.9698.}
\]

No finite SAT/UNSAT experiment, annealed number, physics threshold, or internal candidate is counted as source endpoint movement.

## 1. Ownership, handoff preservation, and consumed evidence

This run continues only the scoped **cluster-aware weighted-counting / overlap-variational** route in

`operations/claims/PROB10-04.md`, blob `1095e6bfb106b53e810af56f2605521abb7143b4`.

It does not overwrite the historical F0097 ownership and does not claim the neighboring interpolation calculation as this lane's work.

The immutable pre-refocus HARD7-06 handoff remains

`runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, blob `e59380417dc476970e22b72b66c59ffbffa4af3a`.

That file records the actual old target `F0095` (ordinary sparse Erdos--Renyi 3-colourability threshold-location convergence), including the binary-cascade identity `Y_out=Y_1Y_2`, `0.9319<q<0.9320`, `5.03<beta_bin<5.04`, and the negative-moment obstruction. None of it is relabeled as 3-SAT progress.

Consumed before the new derivation:

1. `operations/PROB10_2026-09-20.md`, current master;
2. root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`, which creates no posted-claim collision for this scoped route;
3. `operations/claims/PROB10-04.md`, blob above;
4. the immutable HARD7-06/F0095 handoff above;
5. own newest preceding report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T14-30-00Z__finite_tangent_arrangement_KL_globalizer.md`, blob `105f39b55490154c3a36f64ee94a3fb1192363bc`;
6. newest neighboring NM13-13 report `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T12-57-34Z__t04_product_gauss11_43888619_upper.md`, blob `394823a47f8b5ae321c27aa13730ec98f79fdc2a`, status `CANDIDATE_FULL` pending later independent review;
7. newer neighboring NM13-06 report `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T16-28-51__t04_left_radau11_upper.md`, blob `25b3e197807d4878ee7edc623b60d979dd0a44ca`, which records the still-internal candidate `4.38886186` and explicitly inherits a transfer chain not independently revalidated there.

Those neighbor candidates are not promoted into the external source bracket in this report.

## 2. Method change and idea-before-checker discipline

The preceding run removed two analytic obstacles by proving a finite lower-envelope tangent arrangement and a boundary-uniform existence theorem. The remaining geometric input was nevertheless incomplete in a source-specific sense: the exact support oracles did not yet give a **finite complete list of every facet normal**, while the boundary theorem guaranteed finite tangents without a quantitative finite-normal-tilt rate.

After repeated source-metric nonmovement, this run changes method from local Hessian/covariance balls and hand-placed tangent meshes to the **normal fan of the finite-support incidence polytopes**.

The idea and exact missing lemmas were written before the persisted checker in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T14-45-00Z__normal_fan_boundary_compiler_idea_before_checker.md`,

creation commit `fbe02d2e302afb867c21e86c27f6e950147c3968`.

## 3. Three materially different approaches

### Route A — generic support-oracle cutting planes: rejected as incomplete

The existing variable/clause support oracles can feed a generic separation or convex-hull routine. This produces useful floating cuts but does not prove that an unsampled supporting direction is absent. It therefore cannot serve as the finite source compiler required by the previous run's arrangement theorem.

**Precise obstruction:** no finite completeness theorem ties an arbitrary sampled direction set to all facets of the projected mean polytopes.

### Route B — exact normal-fan facet compiler: succeeds analytically

For light variable block `(i,j)`,

\[
S_{ij}=\{(i,0,0)\}\cup\{(0,k,j-k):1\le k\le j\}.
\]

For direction `xi=(a,b,c)`, the false-state score `bk+c(j-k)` is affine in `k`; hence its maximum is always at `k=j` when `b>=c` and at `k=1` when `b<c`. Therefore all possible variable maximizer walls are represented by the primitive integer vectors

\[
(0,1,-1),\qquad (i,-j,0),\qquad(i,-1,1-j),
\quad1\le j\le i\le M.
\tag{3.1}
\]

If `xi` supports a facet of a positive weighted Minkowski sum, the exposed face has dimension two. Its direction space is the span of tied-state differences from exposed summand faces, so there must be two linearly independent maximizer-wall vectors orthogonal to `xi`. Thus every facet-normal ray is a primitive nonzero cross product of two walls in (3.1). Conversely a candidate direction is a facet normal exactly when the tied exposed-direction span has rank two.

The clause side is identical, using state differences within each of the four fixed syntactic-positive clause classes.

This gives a **complete finite integer compiler**, not a direction sample. The full proof is in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T14-52-00Z__normal_fan_facet_and_face_tilt_theorem.md`,

creation commit `1ff8806587a8cc5f844633165d5f950ef10f4777`.

A further corollary is source-geometric completeness: after attaching the already-proved exact support offsets, the common feasible region

\[
P=P_V\cap P_C\cap\{0\le u\le\lambda_p,\ v,w\ge0,\ v+w\le\lambda_n\}
\]

has a complete finite H-representation formed from the compiled variable facets, clause facets, and five copy-simplex inequalities. Intersecting with tangent-order halfspaces `L_j<=L_k` creates no new *input* facet normal; every three-dimensional arrangement-cell extreme point is an intersection of three hyperplanes from this finite source-plus-tangent list.

### Route C — quantitative normal tilt to boundary entropy faces: succeeds analytically

For a finite log partition

\[
A(\theta)=\log\sum_s w_s e^{\theta\cdot s},
\]

fix integer normal `xi`, exposed score `h=max_s xi dot s`, exposed state set `F`, and positive score gap

\[
\Delta=\min_{s\notin F}(h-\xi\cdot s).
\]

For `theta=t xi+eta`, direct factorization gives

\[
A(t\xi+\eta)=th+A_F(\eta)+\log(1+R_t(\eta)),
\]

with

\[
0\le R_t(\eta)\le R_0(\eta)e^{-t\Delta}.
\]

For a mean `y` on the exposed face, `xi dot y=h`, so the ambient finite tangent differs from the face-restricted tangent by at most

\[
\log(1+R_t)\le R_0e^{-t\Delta}.
\tag{3.2}
\]

Because the Diaz incidence states and primitive compiled normals are integral, every nonzero score gap is an integer and therefore

\[
\boxed{\Delta\ge1.}
\]

Thus finite normal tilt approaches every proper incidence face at least exponentially in `t`, without inverse-covariance control. Recursing on lower-dimensional faces supplies a constructive complement to the previous abstract boundary compactness proof.

## 4. Exact checker and new finite geometry

Only after the idea/theorem artifacts above were written did I persist and execute

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T15-02-00Z__normal_fan_compiler_exact.py`,

creation commit `64617584e3d66f9734a887bc6b45b4ff054881ee`.

The archived output is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T15-02-00Z__normal_fan_compiler_exact.out`,

creation commit `612a03a9dcf431d6950d276778a1ae2f7ef07596`.

The checker uses exact integer arithmetic for every normal-fan count and facet test. At `M=23` it obtains:

- `426` primitive variable maximizer walls;
- `52,373` primitive unoriented candidate rays;
- exactly `17,646` **oriented variable facet normals**;
- orientation asymmetry is substantial: among candidate lines, `173` are facets in both orientations, `3,319` only in the canonical positive orientation, `13,981` only in the negative orientation, and `34,900` in neither;
- `12` primitive clause walls, `24` candidate lines, exactly `13` oriented clause facet normals;
- adding the five copy-simplex facets gives

\[
\boxed{17,664}
\]

component facet inequalities before redundancy created by intersecting the component polytopes.

The checker also performs `200,928` exhaustive integer comparisons of the false-state endpoint formula on the direction cube `[-4,4]^3\setminus\{0\}` and all `1<=j<=i<=23`. It verifies the face-tilt identity on an independent finite-state toy example with `Delta=1`, numerical identity error `8.882e-16`, and ends

`ALL_EXACT_NORMAL_FAN_CHECKS_PASS = True`.

One important implementation lesson is now explicit: **testing only one canonical orientation of a candidate ray and then blindly doubling is wrong**. The exposed maximizing face depends on orientation; the exact checker tests `xi` and `-xi` separately.

## 5. Mechanism progress versus source progress

### Source-level progress

None:

\[
[3.52,4.4898]\to[3.52,4.4898],\qquad W:0.9698\to0.9698.
\]

### Auxiliary/mechanism progress

The remaining Diaz outer certification problem has changed in a concrete way:

1. the former support-oracle description is upgraded to a **finite complete facet-normal compiler**;
2. source geometry plus a finite tangent bank now yields a finite, complete hyperplane candidate set for every arrangement cell;
3. entropy boundaries no longer need qualitative `t->infinity` language: finite normal tilt has an explicit `O(e^{-t})` leakage rate on integral incidence faces;
4. the exact `M=23` combinatorial size is known (`17,664` component inequalities before intersection redundancy), so the next interval implementation can be designed against the true finite workload rather than an unknown continuum.

This is still auxiliary. It does not prove that the rescued/truncated exponent is negative on that full finite geometry at any improved density.

## 6. Hypotheses and scope

The facet theorem requires positive weights on the finite Minkowski summands. That holds for the inherited finite-support Diaz reduction at the densities under consideration. The integer gap `Delta>=1` uses integral incidence states and primitive integral normals; it is a statement about the compiled incidence faces, not an arbitrary entropy model.

The H-representation theorem is for the fixed truncation `M`; truncation/tail transfer to the original untruncated proper-clause model remains a separate source obligation.

## 7. Precise unresolved full-scope gap and next method

The exact missing source lemma is now sharper:

> **Outward full-arrangement lemma at an improved density.** Find `alpha<4.4898`, outward interval enclosures for all source parameters and support offsets, and a finite entropy tangent bank such that every extreme point of every lower-envelope cell over the complete compiled outer polytope has rescued/truncated exponent below the reference value by one uniform positive margin. Then pay the truncation/configuration-model/proper-clause transfer without exhausting that margin.

The next run should therefore implement **facet redundancy elimination plus outward interval arrangement evaluation** using the exact 17,664-inequality compiler, rather than returning to local Hessian balls or another sampled support-direction mesh. The quantitative face-tilt theorem gives the needed finite parameter choice near boundary strata.

The neighboring internal candidate `4.38886186` may eventually supersede this Diaz lane if its inherited transfer receives the required independent validation; until then it remains separate and is not a source baseline here.

## 8. Persistence and readback

Conflict-safe unique-path writes only were used. No force push, shared-root mutation, scheduler change, email, Drive, public posting, permission change, or workflow change was made.

Readback at returned commits succeeded for:

- idea-before-checker: `fbe02d2e302afb867c21e86c27f6e950147c3968`;
- theorem: `1ff8806587a8cc5f844633165d5f950ef10f4777`;
- exact checker: `64617584e3d66f9734a887bc6b45b4ff054881ee`;
- exact output: `612a03a9dcf431d6950d276778a1ae2f7ef07596`.

Parent status remains **OPEN / PARTIAL**.