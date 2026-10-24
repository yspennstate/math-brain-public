Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied-effort telemetry is exposed, so I do not claim GPT-6 maximum.**

# PROB10-04 — finite entropy-tangent arrangement and boundary-uniform KL globalizer

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL**.

## 0. Source target and source metric before / after

The frozen source model is the classical independent proper random 3-SAT model:

- `n` Boolean variables;
- `m=floor(alpha n)` independent clauses;
- each clause chooses three **distinct** variables uniformly;
- each of the three literal signs is an independent fair bit.

A fresh bounded primary-source check in this run still supports the same directly auditable explicit rigorous bracket:

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le4.4898}.
\]

Hajiaghayi--Sorkin, <https://arxiv.org/abs/math/0310193>, prove satisfiability w.h.p. below `3.52`. Díaz--Kirousis--Mitsche--Pérez-Giménez, <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2008.1750>, prove a.a.s. unsatisfiability at clause density at least `4.4898`. A 2019 review statement and a 2026 machine-learning paper both still describe `3.52` and `4.4898` as the rigorous 3-SAT bounds; no stronger published explicit endpoint was found in the bounded current check.

Gaia Carenini, ECCC TR26-145, publication date 16 August 2026, <https://eccc.weizmann.ac.il/report/2026/145/>, proves an `O(n/log n)` scaling-window width in **clause count** for every fixed `k>=3`. This is a sharp-window theorem: normalized quantiles are separated by `O(1/log n)`. It does **not** by itself prove that the sequence of window centers converges to one limiting `alpha` for `k=3`, and it does not identify that center.

Ding--Sly--Sun, <https://arxiv.org/abs/1411.0650>, establish the limiting threshold only for all `k>=k_0` for an unspecified absolute constant `k_0`; the theorem is not automatically a `k=3` theorem. ESA 2025 paper 103, <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103>, explicitly changes the classical independence assumption to `k`-wise-independent clause distributions and is therefore not substituted for the present model.

Hence the externally validated source metric is unchanged:

\[
\boxed{W_{source}:4.4898-3.52=0.9698\ \longrightarrow\ 0.9698.}
\]

There is **no source endpoint movement in this run**.

A neighboring NM13-13 lane records a project-internal `CANDIDATE_FULL` upper endpoint `4.38886365`, pending independent review, in

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T12-23-08Z__t04_product_gauss9_survey_reopt_438886365.md`.

That is a different interpolation/survey route and is **not promoted here** into the external source bracket.

## 1. Ownership, preserved predecessor handoff, and consumed evidence

This run continued only the scoped **cluster-aware weighted-counting / overlap-variational** claim in

`operations/claims/PROB10-04.md`, blob `1095e6bfb106b53e810af56f2605521abb7143b4`.

It did not overwrite historical F0097 ownership and did not duplicate the constructive lower-bound route owned by NM13-06.

The actual pre-refocus HARD7-06 work remains preserved verbatim at

`runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`, blob `e59380417dc476970e22b72b66c59ffbffa4af3a`.

That handoff records the true predecessor target `F0095`, ordinary sparse Erdős--Rényi 3-colourability threshold-location convergence, including the binary cascade identity `Y_out=Y_1Y_2`, the fixed-point range `0.9319<q<0.9320`, `5.03<beta_bin<5.04`, and its negative-moment obstruction. None of that is relabeled as random 3-SAT progress.

Consumed before the new derivation:

1. `operations/PROB10_2026-09-20.md`, blob `6f0fcee836d93371d43b84af1a55150fedc80779`;
2. current root `POSTED.md`, blob `affe1b5f31545bb15be9ba2580548e9e88095e1b`;
3. `operations/claims/PROB10-04.md`, blob above;
4. the immutable HARD7-06/F0095 handoff above;
5. own newest preceding report
   `runs/prob10_2026-09-20/PROB10-04/2026-09-20T13-30-00Z__simplicial_dual_global_annulus_certificate.md`, blob `56c5f2ca3c3156038bebc7f2b8eeb55c8bfc76d7`;
6. the preceding analytic theorem
   `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T13-05-00Z__simplicial_entropy_dual_certificate_theorem.md`, blob `6efeff232e72d2e1ae107bf03cfe51034d55e597`;
7. neighboring upper/interpolation report
   `proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T12-23-08Z__t04_product_gauss9_survey_reopt_438886365.md`, blob `e783176779f7474442a7d666e1bb19f436511609`;
8. neighboring constructive report
   `proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T15-29-14__t04_absorbing_makebreak_cascade.md`, blob `71caa90c93a9ed3a1d550206d48c8b11ab526089`.

The mathematical idea and the exact three missing lemmas were frozen **before code** in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T13-47-00Z__tangent_bank_arrangement_three_routes_idea.md`,

creation commit `c764d2f4020d55ec9394befa3877e5d3c6ed5796`.

## 2. Why this run changes method

The preceding run proved that the remaining Díaz finite-support exponent may be written

\[
\Phi(y)=K(y)+E(y)+c_0,\qquad E=V+C,
\tag{2.1}
\]

for the three outer copy masses `y=(u,v,w)`, with `K` an explicit convex copy term and `V,C` finite-support maximum-entropy values. It also proved a one-tangent simplicial upper bound and an interior finite-cover theorem.

However, the same run found an actual feasible ray along which the Hessian of `Phi` becomes indefinite at about `t=0.68424`. Thus global negative-Hessian globalization is false even in the inherited finite-support surrogate. The interior triangulation theorem also left an awkward theoretical boundary obligation because entropy inverse-Hessian bounds can blow up on projected-polytope faces.

This run therefore does **not** repeat local covariance transport, local rescue tuning, or another finer geometric mesh. It replaces those methods by a finite **bank of entropy dual tangents**, and then treats the lower envelope of that bank exactly by its hyperplane arrangement.

## 3. Three materially different attacks

The run compared the following three approaches.

### Route A — one global mixture of tangents

For a finite bank of affine entropy majorants `L_1,...,L_J`, define

\[
\bar E_J(y)=\min_j L_j(y)\ge E(y).
\]

Since for every probability vector `p in Delta_J`,

\[
\min_jL_j(y)\le\sum_jp_jL_j(y),
\]

one obtains the valid bound

\[
\sup_{y\in R}\Phi(y)
\le c_0+
\inf_{p\in\Delta_J}\max_{v\in Vert(R)}
\left[K(v)+\sum_jp_jL_j(v)\right].
\tag{3.1}
\]

The proof is complete: `K+sum p_jL_j` is convex, so its maximum over a compact polytope occurs at a vertex.

This route is computationally attractive because it reduces to a small finite minimax/LP, but the inherited difficult ray **falsifies its usefulness**. With seven Gibbs tangents at

`0.25, 0.50, 1.00, 1.50, 2.00, 2.50, 2.70`,

the global mixture relaxation on the whole ray interval `[0.25,2.70]` still has diagnostic upper gap

\[
\boxed{+0.201933298671527}.
\]

Therefore Route A cannot even certify this one already-known suboptimal ray segment. The obstruction is precise: replacing the pointwise lower envelope by one global convex combination destroys the ability to switch active tangents with location. This is not a failure of entropy duality itself.

### Route B — exact lower-envelope hyperplane arrangement

Keep the pointwise minimum instead. For each tangent define

\[
C_j=R\cap\bigcap_k\{y:L_j(y)\le L_k(y)\}.
\tag{3.2}
\]

On `C_j`, `bar E_J=L_j`, hence

\[
K(y)+\bar E_J(y)=K(y)+L_j(y),
\]

which is convex. Therefore

\[
\boxed{
\sup_{y\in R}[K(y)+\bar E_J(y)]
=
\max_j\max_{x\in Ext(C_j)}[K(x)+L_j(x)].
}
\tag{3.3}
\]

Because `E<=bar E_J`, the right side upper-bounds the true exponent. This is an **exact continuum reduction for the finite bank**, not a grid.

If `R` has affine dimension `r`, every cell extreme point is obtained from `r` linearly independent active equations drawn from original facets and tangent-equality hyperplanes `L_j=L_k`, followed by inequality checks. In the Díaz outer problem `r=3`, so three active hyperplanes generate every candidate.

This route succeeds where Route A fails. Using the same seven tangents on the inherited difficult ray, all active-envelope candidates are contained among only `23` endpoints/pair-intersections, and the largest diagnostic surrogate gap is

\[
\boxed{-0.03778010193775572}
\]

at `t=0.25`. Thus the **entire** ray interval `[0.25,2.70]` is certified by one finite lower-envelope arrangement in the floating surrogate, replacing six hand-cut one-tangent segments from the prior run.

In the prior three-dimensional radius-`0.15` tetrahedron centered where the Hessian is already indefinite, the old center-tangent bound was

\[
-0.2976150596259224.
\]

Adding tangents at the center and four vertices and enumerating the cell candidates gives `36` feasible floating candidates and improves the worst upper gap to

\[
\boxed{-0.3334846267828482},
\]

an improvement of

\[
0.0358695671569258.
\]

These Díaz numbers are **diagnostic floating calculations only**. They are not outward interval certificates and do not move a threshold endpoint.

### Route C — KL/Bregman geometry and a boundary-uniform finite bank

For one finite-support log partition

\[
A(\theta)=\log\sum_s w_s e^{\theta\cdot s}
\]

and an interior mean `y=nabla A(theta_y)`, the entropy value is

\[
E_A(y)=A(\theta_y)-\theta_y\cdot y.
\]

The tangent generated by finite parameter `theta_c` is

\[
L_{\theta_c}(y)=A(\theta_c)-\theta_c\cdot y.
\]

Direct subtraction gives the exact identity

\[
\begin{aligned}
L_{\theta_c}(y)-E_A(y)
&=A(\theta_c)-A(\theta_y)
 -\nabla A(\theta_y)\cdot(\theta_c-\theta_y)\\
&=D_A(\theta_c,\theta_y)\\
&=KL(P_{\theta_y}\|P_{\theta_c})\ge0.
\end{aligned}
\tag{3.4}
\]

Thus the tangent-bank error has a genuine information-geometric meaning: for the weighted variable/clause decomposition it is the sum of weighted block KL divergences.

More importantly, the boundary problem can be removed without a Hessian estimate.

Assume only that a compact region `R` has continuous entropy value `E` and an affine dual representation

\[
E(y)=\inf_{\eta}L_\eta(y)
\tag{3.5}
\]

with finite affine `L_eta`. For any `epsilon>0` and any `y in R`, choose a finite `eta(y)` with

\[
L_{\eta(y)}(y)<E(y)+\epsilon/3.
\]

Because `L_{eta(y)}-E` is continuous, there is a neighborhood `U_y` on which it is `<epsilon`. Compactness gives finitely many such neighborhoods covering `R`; retain their finite parameters. Hence

\[
\boxed{
0\le\min_{1\le j\le J}L_j(x)-E(x)<\epsilon
\quad\forall x\in R.
}
\tag{3.6}
\]

No dual attainment at a boundary point, differentiability, inverse covariance, or uniform Hessian bound is required.

A separate supplement proves the needed closed-boundary continuity for finite-support maximum entropy from first principles. Writing the negative entropy/relative-entropy program as

\[
I(y)=\min\{f(p):p\in\Delta_N,\ Ap=y\},
\]

`I` is convex by mixing minimizers and lower semicontinuous by compactness of the simplex and continuity of `f`. At any chosen `y` in the mean polytope, triangulate the polytope with `y` as a vertex. All sufficiently close points lie in one of finitely many simplices incident to `y`; barycentric convexity then gives `limsup I(x)<=I(y)`, while lower semicontinuity gives the reverse inequality. Thus `I`, and hence the entropy value, is continuous on the whole closed mean polytope.

The full proofs are archived in:

- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T14-02-00Z__finite_tangent_arrangement_and_KL_cover_theorem.md`, creation commit `1ad073dfa858daac862d73373853f4dbf57aef51`;
- `artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T14-18-00Z__finite_support_entropy_boundary_continuity_lemma.md`, creation commit `1e013d6b0e6a20fcd967c29a206586e2eda7b29b`.

## 4. New finite-certificate existence theorem

Combining Routes B and C gives the main analytic advance of this run.

### Theorem

Let `R` be a compact polytope, `Phi=K+E+c_0`, with `K` continuous convex and `E` continuous with representation `E=inf_eta L_eta` by finite affine majorants. Suppose

\[
\sup_{y\in R}\Phi(y)\le\Phi_*-\eta
\quad\text{for some }\eta>0.
\tag{4.1}
\]

Then there exists a **finite** bank of finite dual parameters for which the exact lower-envelope arrangement certificate satisfies

\[
\max_j\max_{x\in Ext(C_j)}[K(x)+L_j(x)+c_0]<\Phi_*.
\tag{4.2}
\]

### Proof

Apply the boundary-uniform finite-bank theorem with `epsilon=eta/2`. Then, pointwise on `R`,

\[
K+\bar E_J+c_0
\le K+E+c_0+\eta/2
\le\Phi_*-\eta/2.
\]

Taking the supremum and applying the exact arrangement identity (3.3) yields (4.2). QED.

This is the method change that matters: **if the full finite-support Díaz outer region at a candidate density truly has a strict exponent gap, then some finite arrangement of entropy tangents certifies the entire compact region, including entropy-polytope boundaries.** Global Hessian negativity and an arbitrarily fine geometric triangulation are not logically necessary.

It is an existence/architecture theorem; it does not assert that the needed source-specific strict gap has already been proved below `4.4898`.

## 5. Executed checks

The checker is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T14-14-00Z__tangent_arrangement_diagnostic.py`,

creation commit `f22c53acc03a36a49b139244f67bb22481bd28b8`.

Its actual output is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T14-14-00Z__tangent_arrangement_diagnostic.out`,

creation commit `b72b2ed3f2a29e7a821fc476a20b74360e8b9920`.

There are two deliberately separated test classes.

### Exact finite arithmetic sanity test

For `R=[0,1]`, `K(x)=x^2`, `L_1=0`, `L_2=1-2x`, the arrangement has only candidates `0,1/2,1`. Exact `Fraction` arithmetic verifies surrogate values

\[
0,\quad1/4,\quad0
\]

and maximum exactly `1/4`. This tests the arrangement-candidate logic, not random 3-SAT.

### Floating Díaz diagnostic

The checker reconstructs the inherited `M=23`, `alpha=4.4898` finite-support surrogate and obtains

- `q=0.9987915696623344`;
- `lambda_p=8.150767890649966`;
- `lambda_n=5.269860599061735`;
- saddle surrogate
  `y0=(5.856667999143169, 0.5364470108663393, 1.153411776660164)`.

The numerical checks then give:

1. global tangent-mixture route fails on the hard ray with upper gap `+0.201933298671527`;
2. exact-envelope arrangement with the same seven tangents certifies the full ray, max diagnostic gap `-0.03778010193775572`;
3. the KL/Bregman identity at an independent target/center pair has
   `D_V=0.01303739110101204`, `D_C=0.01374342983715007`, absolute identity error `2.498001805406602e-16`;
4. the indefinite tetrahedron has `36` feasible enumerated arrangement candidates, worst gap `-0.3334846267828482`, improving the old one-tangent `-0.2976150596259224` by `0.0358695671569258`.

The execution ends

`ALL_TANGENT_ARRANGEMENT_DIAGNOSTIC_CHECKS_PASS = True`.

Again, the Díaz computations use ordinary floating root solving / convex-hull geometry and are **not interval-certified source claims**.

## 6. Mechanism progress vs source progress

### Source-level progress

None:

\[
[3.52,4.4898]\to[3.52,4.4898],\qquad
W:0.9698\to0.9698.
\]

### Auxiliary/mechanism progress

The remaining outer variational certification problem is now structurally smaller in a meaningful way:

- a global convex-mixture shortcut has been quantitatively falsified, so it should not consume another run;
- the finite bank can instead be evaluated **exactly on a finite hyperplane arrangement** while retaining the copy entropy `K` exactly;
- the tangent error is exactly a KL/Bregman divergence at attained Gibbs means, giving a principled center-selection geometry;
- finite tangent banks approximate the entropy value uniformly on compact regions **including boundaries**, removing the previous need for uniform boundary Hessian control;
- any true compact strict gap admits a finite arrangement certificate in principle.

This is stronger than another local numerical improvement because it removes two previous theoretical blockers: loss of global Hessian negativity and entropy-boundary curvature blowup.

## 7. Hypotheses and scope

The abstract arrangement theorem requires only:

1. compact polyhedral region `R`;
2. a continuous convex explicit term `K`;
3. a continuous entropy value `E` represented as the infimum of finite affine dual majorants.

The finite-support Díaz variable/clause entropy programs satisfy item 3 on their closed projected mean polytopes by the continuity lemma above. The exact KL identity additionally assumes an interior attained Gibbs parameter at the point where it is invoked; the boundary-uniform finite-bank theorem itself does **not** require attainment.

What has **not** been proved here is that the complete source exponent at any `alpha<4.4898` is already reduced with all errors to exactly this finite compact problem with a certified negative gap. Therefore the theorem remains auxiliary.

## 8. Precise unresolved full-scope gap and next method

To convert this lane into an actual upper-endpoint improvement below `4.4898`, the next run should not return to local Hessian balls or one-tangent hand segmentation. It should compile a **source-specific outward-certified tangent arrangement**.

The exact missing source lemma is:

> **Full outer arrangement lemma at improved density.** Find one `alpha<4.4898` and a finite collection of outward-certified variable/clause dual parameters such that, after incorporating the already-derived rescue correction and all truncation terms, every feasible extreme point of every lower-envelope arrangement cell has exponent strictly below the reference saddle value, with one uniform rational/interval margin.

That requires:

1. outward interval enclosures for the source reduction parameters at the chosen `alpha`;
2. exact/support-oracle description of the full projected feasible copy region;
3. finite enumeration of all three-hyperplane arrangement candidates, including lower-dimensional faces;
4. outward evaluation of `K` and all affine dual values at every candidate;
5. rescue/truncation/configuration-model error accounting with a margin that survives transfer to the proper iid clause model;
6. a final proper-clause fixed-count transfer;
7. independent validation under the repository standard.

The neighboring `4.38886365` interpolation candidate may ultimately render this Díaz lane unnecessary if independently validated, but until that happens it remains a separate project candidate rather than a source baseline.

## 9. Persistence/readback

Conflict-safe unique-path writes only were used; no force push, shared-root edit, scheduler change, email, Drive, public posting, permission change, or workflow change was made.

Readback at returned commits succeeded for:

- idea-before-code: `c764d2f4020d55ec9394befa3877e5d3c6ed5796`;
- finite tangent-arrangement/KL theorem: `1ad073dfa858daac862d73373853f4dbf57aef51`;
- diagnostic checker: `f22c53acc03a36a49b139244f67bb22481bd28b8`;
- diagnostic output: `b72b2ed3f2a29e7a821fc476a20b74360e8b9920`;
- boundary continuity supplement: `1e013d6b0e6a20fcd967c29a206586e2eda7b29b`.

Parent status remains **OPEN / PARTIAL**.