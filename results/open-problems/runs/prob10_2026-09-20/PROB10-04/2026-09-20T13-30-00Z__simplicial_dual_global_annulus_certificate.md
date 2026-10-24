Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — no authenticated applied-effort telemetry is exposed, so I do not claim GPT-6 maximum.**

# PROB10-04 run 13 — simplicial entropy-dual certificate for the global Díaz annulus

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **OPEN / PARTIAL**.

## 0. Source metric before / after

The owner-frozen target is the classical independent proper-clause random 3-SAT model:

- `n` Boolean variables;
- `m=floor(alpha n)` independent clauses;
- each clause chooses three distinct variables uniformly;
- all three signs are independent fair bits.

A fresh source check in this run supports the same directly auditable explicit-decimal bracket used by this lane:

\[
\boxed{3.52\le \liminf \alpha_n^*\le \limsup \alpha_n^*\le4.4898}.
\]

Hajiaghayi--Sorkin prove satisfiability w.h.p. below `3.52`: <https://arxiv.org/abs/math/0310193>.  Díaz--Kirousis--Mitsche--Pérez-Giménez prove a.a.s. unsatisfiability at `4.4898`: <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2008.1750>.  Gaia Carenini's ECCC TR26-145, published 16 August 2026, proves an `O(n/log n)` **scaling-window width in clause count** for every fixed `k>=3`: <https://eccc.weizmann.ac.il/report/2026/145/>.  That sharp-window statement does not locate the center and does not by itself prove convergence of the normalized center to one exact constant for `k=3`.  Ding--Sly--Sun <https://arxiv.org/abs/1411.0650> proves the threshold for all sufficiently large `k`, not automatically `k=3`.  ESA 2025 paper 103 <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2025.103> explicitly studies `k`-wise-independent clause distributions, which are not substituted for the independent-clause model here.

Therefore

\[
\boxed{W_{source}:0.9698\longrightarrow0.9698.}
\]

There is **no source endpoint movement in this run**.  The neighboring NM13-13 lane currently records a source-connected **project candidate** upper endpoint `4.38886365`, status `CANDIDATE_FULL pending later independent review`, in

`proofnet24/NM13-13/progress-3sat/runs/2026-09-20/2026-09-20T12-23-08Z__t04_product_gauss9_survey_reopt_438886365.md`.

I do not promote that candidate to the external source bracket in this PROB10-04 report.

## 1. Ownership, immutable handoff, and consumed repository evidence

I continued only the scoped PROB10-04 **cluster-aware weighted-counting / overlap-variational** route in

`operations/claims/PROB10-04.md`.

I did not overwrite the historical F0097 parent claim and did not duplicate NM13-06's constructive lower-bound route.  The current NM13-06 report read in this run is

`proofnet24/NM13-06/progress-3sat-construction/runs/2026-09-20/2026-09-20T15-29-14__t04_absorbing_makebreak_cascade.md`,

status `OPEN / PARTIAL`; it studies absorption-aware make-minus-break cascades and is complementary to the present upper/variational route.

The pre-refocus HARD7-06 history remains immutably preserved at

`runs/hard7_2026-09-18/HARD7-06/2026-09-19T23-49-30Z__handoff_to_prob10-04.md`.

That handoff correctly says HARD7-06 had actually been working on F0095/random graph 3-colourability and its binary cascade, including `Y_out=Y_1Y_2`, the numerical fixed point `0.9319<q<0.9320`, `5.03<beta_bin<5.04`, and the negative-moment obstruction.  None of it is relabeled as 3-SAT work.

Also consumed before starting the new derivation:

- current `operations/PROB10_2026-09-20.md`;
- current root `POSTED.md`;
- current scoped claim `operations/claims/PROB10-04.md`;
- own preceding report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T11-44-12Z__mean_ball_covariance_transport_compiler.md`;
- the earlier exact outer Hessian/support-oracle report `runs/prob10_2026-09-20/PROB10-04/2026-09-20T10-08-00Z__outer_covariance_compensation_and_support_oracles.md`;
- newest neighboring NM13-13 and NM13-06 reports named above.

The required mathematical idea and exact missing lemmas were frozen **before code** in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T12-47-00Z__global_annulus_three_routes_idea_before_code.md`,

creation commit `ef8d90680a13f57cd708683bee99417de1668122`.

## 2. Inherited reduction

For the remaining Díaz outer copy masses

\[
y=(u,v,w)=(\ell_{ps},\ell_{ns1},\ell_{ns2}),
\]

the preceding runs reduce the relevant optimized exponent to

\[
\Phi(y)=K(y)+V(y)+C(y)+c_0,
\tag{2.1}
\]

where the explicit copy term is

\[
\begin{aligned}
K(y)=&\;u\log u+(\lambda_p-u)\log(\lambda_p-u)\\
&+v\log v+w\log w
 +(\lambda_n-v-w)\log(\lambda_n-v-w),
\end{aligned}
\tag{2.2}
\]

and `V,C` are variable-side and clause-side maximum-entropy values at the same mean copy vector `y`.

At interior means, with finite-support Gibbs covariance matrices `Sigma_V,Sigma_C`, the exact Hessian identity is

\[
\boxed{\nabla^2\Phi
=H_{copy}-\Sigma_V^{-1}-\Sigma_C^{-1}.}
\tag{2.3}
\]

Run 12 supplied a rigorous finite-support multiplicative covariance-transport theorem and an inverse-free fixed-split LMI, certifying a Euclidean mean ball of radius `0.0015` around a rationalized saddle surrogate.  Its precise obstruction was that one covariance-transport center is intrinsically local.  This run therefore changes method inside 3-SAT rather than repeating local rescue tuning.

## 3. Three nonexhausted approaches attempted

The three attacks, in the order frozen before code, were:

1. **mean-dependent covariance domination** using the Bhatia--Davis variance bound at the known Gibbs mean;
2. **recentered negative-Hessian balls** using the previous covariance transport at many centers;
3. **global value certification by entropy dual tangents plus simplicial interpolation of the convex copy term**.

Approach 1 is quantitatively too weak even at the favorable saddle.  Approach 2 is mathematically incapable of covering the full feasible annulus by negative-Hessian balls because the Hessian actually becomes indefinite along a feasible interior ray.  Approach 3 succeeds analytically and gives a rigorous continuum certificate independent of Hessian sign.  The rest of the run develops that result.

## 4. Approach 1 — exact obstruction to scalar mean-dependent Bhatia--Davis domination

The earlier support-only Popoviciu shortcut failed because high-degree support ranges were far wider than the actual Gibbs spread.  A natural strengthening is to retain the **actual projected Gibbs mean** in each finite block and apply Bhatia--Davis.

For a scalar projection `X=x·S` supported on `[a,b]` with mean `m`,

\[
\operatorname{Var}(X)\le(b-m)(m-a).
\tag{4.1}
\]

Summing (4.1) over the finite variable blocks and clause blocks gives directional covariance upper bounds

\[
x^T\Sigma_Vx\le B_V(y,x),
\qquad
x^T\Sigma_Cx\le B_C(y,x).
\tag{4.2}
\]

Cauchy--Schwarz supplies

\[
x^T\Sigma^{-1}x\ge{\|x\|_2^4\over x^T\Sigma x},
\tag{4.3}
\]

so this scalar relaxation could prove concavity if

\[
{\|x\|^4\over B_V}+{\|x\|^4\over B_C}
>x^TH_{copy}x
\tag{4.4}
\]

for every direction.

It does not.  At the inherited solved saddle and

\[
x=(-1,10,-6),
\]

the executed finite-support calculation gives

\[
B_V=747.5400949548297,
\qquad
B_C=332.0197251353126,
\]

whereas the actual directional variances are only

\[
x^T\Sigma_Vx=64.05001124583937,
\qquad
x^T\Sigma_Cx=106.0463376619059.
\]

Consequently the Bhatia--Davis/Cauchy inverse-curvature lower bound is only

\[
\boxed{81.63745727932044},
\]

while

\[
x^TH_{copy}x=222.6993692116383
\]

and the actual two-sided inverse covariance contribution is

\[
755.2591974316147.
\]

Thus even mean-dependent scalar support/mean information loses the crucial anisotropy by almost an order of magnitude.  This is a precise obstruction to this **scalar Bhatia--Davis relaxation**, not a theorem that every possible mean-dependent matrix inequality must fail.

## 5. Approach 2 — recentered negative-Hessian balls cannot be the whole global proof

The exact covariance-transport theorem remains useful locally, so I tested whether repeated recentering could in principle cover the whole high-value feasible region by regions with `nabla^2 Phi<0`.

The solved saddle is

\[
y_0\approx(5.856667999143169,
0.5364470108663394,
1.153411776660165),
\]

with

\[
\lambda_{max}(\nabla^2\Phi(y_0))
\approx-0.07447425717764061.
\]

Along the normalized interior direction

\[
d\approx(-0.67804166,0.60629724,-0.41552757),
\]

the Gibbs inverse maps remain numerically well-conditioned over the tested range, but the largest Hessian eigenvalue crosses zero at

\[
\boxed{t_*\approx0.6842404327681848}
\tag{5.1}
\]

for `y=y_0+t d`.  At that crossing the exponent has already fallen by

\[
\Phi(y_0+t_*d)-\Phi(y_0)
\approx-0.2362873738878157.
\tag{5.2}
\]

At `t=1`,

\[
\lambda_{max}(\nabla^2\Phi)\approx+0.02071633992898771,
\qquad
\Phi-\Phi(y_0)\approx-0.4578834490027681.
\]

So **global concavity is false in the exact finite-support surrogate being studied**.  A recentered-ball proof based solely on strict negative Hessian cannot cover the annulus.  The correct hybrid must use local curvature near the saddle and direct value upper bounds outside it.

This is the main method-changing obstruction of the run.

## 6. Approach 3 — a global simplicial entropy-dual theorem

The successful replacement is to bound **values**, not Hessians.

Write the two finite-support log partitions as `A_V(theta)` and `A_C(phi)`.  Maximum-entropy duality gives

\[
V(y)=\inf_\theta\{A_V(\theta)-\theta\cdot y\}+c_V,
\qquad
C(y)=\inf_\phi\{A_C(\phi)-\phi\cdot y\}+c_C.
\tag{6.1}
\]

Therefore for any fixed finite trial parameters `theta,phi`, globally on the feasible set,

\[
V(y)\le A_V(\theta)-\theta\cdot y+c_V,
\qquad
C(y)\le A_C(\phi)-\phi\cdot y+c_C.
\tag{6.2}
\]

Now let

\[
Q=\operatorname{conv}\{z_0,\ldots,z_d\}
\]

be a simplex contained in the open copy domain, and let

\[
y=\sum_i\lambda_i z_i,
\qquad \lambda_i\ge0,
\qquad\sum_i\lambda_i=1.
\]

Because the explicit copy term `K` is convex,

\[
K(y)\le\sum_i\lambda_iK(z_i).
\tag{6.3}
\]

Define

\[
U_i=K(z_i)+A_V(\theta)-\theta\cdot z_i
+A_C(\phi)-\phi\cdot z_i+c_0+c_V+c_C.
\tag{6.4}
\]

Combining (6.2)--(6.3),

\[
\Phi(y)
\le\sum_i\lambda_iU_i
\le\max_iU_i.
\]

Hence the exact continuum theorem is

\[
\boxed{
\sup_{y\in Q\cap\mathcal P}\Phi(y)
\le\max_i U_i.
}
\tag{6.5}
\]

Here `mathcal P` is the intersection of the variable-side and clause-side projected feasibility polytopes.  The existing exact support-function oracles can first discard a simplex with empty intersection; otherwise (6.5) upper-bounds the entire continuum simplex.

This is not a grid heuristic.  It is valid even if the full Hessian of `Phi` is indefinite inside `Q`.

The complete proof is frozen in

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T13-05-00Z__simplicial_entropy_dual_certificate_theorem.md`,

creation commit `582d6e6dcc0723749962eb235059cc15aef124d6`.

## 7. Quantitative finite-cover theorem

There is also a useful stopping theorem.  On a compact interior region suppose

\[
\|\nabla^2K\|_{op}\le M_K,
\qquad
\|-\nabla^2(V+C)\|_{op}\le M_E.
\]

Choose the dual tangent at a simplex center `c`.  If `U_Q(y)` is the barycentric certificate obtained from the vertex values in (6.4), Taylor's theorem gives

\[
\boxed{
0\le U_Q(y)-\Phi(y)
\le {M_K\over2}\operatorname{diam}(Q)^2
+{M_E\over2}\|y-c\|^2.
}
\tag{7.1}
\]

The proof has two independent pieces:

1. for `K`, Taylor-expand each vertex around `y`; the barycentric first-order terms cancel exactly, leaving at most `(M_K/2)diam(Q)^2`;
2. for the concave entropy value `E=V+C`, the Gibbs dual at `c` is its supporting tangent, whose excess over `E(y)` is the integrated negative Hessian and is at most `(M_E/2)||y-c||^2`.

Therefore, if a compact interior annulus actually has a strict gap

\[
\sup_R\Phi\le\Phi_* -\eta,
\qquad\eta>0,
\]

then every sufficiently fine finite triangulation is eventually certified by (6.5).  This provides a mathematical termination criterion for a future branch-and-bound certificate, rather than merely hoping a mesh is dense enough.

Boundary pieces require direct dual choices/exposed-face treatment because uniform entropy Hessian bounds may diverge there; theorem (6.5) itself remains valid with arbitrary finite dual parameters.

## 8. Executed diagnostic: value certificates work beyond the Hessian sign change

Only after freezing the three approaches and proving (6.5)--(7.1) did I execute the finite-support diagnostic.  The archived checker is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T13-10-00Z__global_annulus_dual_simplex_diagnostic.py`,

creation commit `1f92431d4a7b9a39b36bf0263178b24bd924e196`,

and the archived output is

`artifacts/prob10_2026-09-20/PROB10-04/2026-09-20T13-10-00Z__global_annulus_dual_simplex_diagnostic.out`,

creation commit `91d0b49ed581c3d84903e6abe6210af95ebea576`.

### 8.1 Segment certificates

Using at each interval the entropy tangent at its midpoint and the exact convex chord for `K`, theorem (6.5) gives the following numerical upper gaps relative to the saddle value:

\[
\begin{array}{c|c}
[t_0,t_1]&\text{dual upper gap}\\ \hline
[0.25,0.50]&-0.0238112268551\\
[0.50,1.00]&-0.0887902783727\\
[1.00,1.50]&-0.416335431504\\
[1.50,2.00]&-0.874380433409\\
[2.00,2.50]&-1.45557879995\\
[2.50,2.70]&-2.28550841157
\end{array}
\]

Thus the **same ray remains value-certified well after the Hessian became indefinite at `t≈0.68424`**.

### 8.2 A genuinely three-dimensional indefinite tetrahedron

To ensure the mechanism is not merely one-dimensional, take the center

\[
c=y_0+d,
\]

where

\[
\lambda_{max}(\nabla^2\Phi(c))
\approx+0.02071633992898671>0.
\]

Around `c`, take the regular tetrahedron of Euclidean radius `0.15` with the four standard sign directions

\[
{1\over\sqrt3}(1,1,1),\quad
{1\over\sqrt3}(1,-1,-1),\quad
{1\over\sqrt3}(-1,1,-1),\quad
{1\over\sqrt3}(-1,-1,1).
\]

Use the entropy Gibbs tangent at `c`.  The four vertex upper gaps in theorem (6.5) are

\[
-0.473846150904,
\quad-0.429630941699,
\quad-0.580127775925,
\quad-0.297615059626.
\]

Therefore the theorem diagnostically excludes the **entire three-dimensional continuum tetrahedron** with upper gap

\[
\boxed{-0.2976150596259224}
\tag{8.1}
\]

even though the full Hessian is already indefinite at its center.

This is the key mechanism gain of the run.  These decimals are floating diagnostics, not interval-certified threshold data.

## 9. Actual checks

The finite-support computation reconstructed the `M=23`, `alpha=4.4898` Díaz saddle, the variable and clause log partitions, means and covariances, and the Gibbs inverse maps.  Consolidated executed assertions checked:

- stationarity residual below `1e-10`;
- negative definite Hessian at the inherited saddle;
- the Bhatia--Davis obstruction `81.6374572793 < 222.6993692116 < 755.2591974316`;
- Hessian sign change on the test ray;
- strict negativity of all six segment dual certificates;
- positive largest Hessian eigenvalue at the tetrahedron center;
- strict negativity of all four tetrahedral vertex dual upper bounds.

The executed diagnostic concluded

`ACTUAL_CONSOLIDATED_CHECKS_PASS = True`,

and the archived matching output ends

`SEGMENT_DUAL_CERTIFICATES_NEGATIVE = True`,

`INDEFINITE_TETRA_DUAL_CERTIFICATE_NEGATIVE = True`,

`DIAGNOSTIC_CHECKS_PASS = True`.

No finite SAT/UNSAT instance, simulation, annealed estimate, or unchecked physics threshold is counted as asymptotic progress.

## 10. Before / after mechanism ledger

**Source metric:**

\[
[3.52,4.4898]\to[3.52,4.4898],
\qquad W:0.9698\to0.9698.
\]

**Auxiliary mechanism before:**

- inner rescue aggregate deviations had been paid;
- exact outer Hessian/covariance formula was known;
- exact support oracles were known;
- a single covariance-transport center certified only a local radius-`0.0015` ball;
- no rigorous continuum method covered a nonconcave outer annulus.

**Auxiliary mechanism after:**

- scalar mean-dependent Bhatia--Davis domination is quantitatively ruled out as too weak at the saddle;
- pure global negative-Hessian covering is ruled out by an explicit interior Hessian sign change at `t≈0.68424043`;
- theorem (6.5) gives a rigorous continuum simplex upper bound requiring no Hessian sign;
- theorem (7.1) gives an `O(diam(Q)^2)` certificate-overpayment bound and a finite-cover termination principle on compact strict-gap interior regions;
- a radius-`0.15` three-dimensional simplex centered in an **indefinite** region is already excluded by the new value certificate in floating diagnostic arithmetic.

This is a real method advance but not yet a threshold endpoint advance.

## 11. Exact unresolved full-scope gap

The remaining source-level lemma is now more concrete than in the preceding run:

\[
\boxed{
\begin{array}{l}
\text{At some }\alpha<4.4898,\text{ construct an outward-certified finite cover of the entire}\\
\text{rescue-adjusted outer feasible set by (i) the local covariance-transport ball,}\\
\text{(ii) support-separated empty simplices, and (iii) simplices satisfying (6.5),}\\
\text{with every non-saddle cell uniformly below the required exponent level.}
\end{array}}
\tag{11.1}
\]

The required implementation cannot be a blind floating mesh.  It must outward-certify the source parameters, natural-parameter dual values, `K` vertex values, feasibility/support separation, truncation/tail errors, and the rescue-adjusted exponent.  Boundary cells where Gibbs parameters diverge need explicit finite dual choices or exposed-face limits.  The configuration-model / independent-proper-clause transfer and an independent review remain part of repository completion standards.

A sensible next run is therefore a **certified simplicial branch-and-bound compiler** using the exact support oracles and fixed finite dual tangents, first at `alpha=4.4898` to close the global annulus without numerical assumptions, and only then moving `alpha` downward.  Repeating local Hessian-radius enlargement is no longer the right priority.

## 12. Repository actions

This run made only conflict-safe unique-path writes on private `master`; no force push was used.  It changed no scheduler state, email, Drive, public posting, permissions, or workflows.

Readback was performed at the returned creation commits for the idea artifact, theorem artifact, checker, output, and this report.  Parent status remains **OPEN / PARTIAL**.
