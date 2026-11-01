Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on D0039: `B_spectrum: 2 -> 2`; authoritative stagnation count remains UNKNOWN. Methods actually used: #8 GO THE OTHER WAY AND DISCRETIZE, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS.**

# R14 HARD OUTSIDE — D0039 Gaussian-quadrature cells and an exact endpoint Gibbs representation

Date: 2026-09-18 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source problem OPEN.** This run does not reopen the handed-off negative-margin spherical perceptron, H0017, or Bradley D0036. It continues the exclusive R14 hard-outside claim `operations/claims/D0039.md`: Bálint Virág, *Operator limits of random matrices*, ICM 2014 / arXiv:1804.06953, Section 4, Question 1, on the multifractal spectrum of the beta-Hermite spectral measure.

The frozen metric stays at level 2. I do **not** claim the level-3 Hausdorff-spectrum theorem. The substantive change is in the route: the preceding report treated subordinate/Weyl alignment as an apparently necessary second bridge between a Christoffel-kernel LDP and local mass. That is a valid Jitomirskaya--Last route, but it is **not logically necessary**. The exact Gaussian-quadrature mesh itself gives a direct deterministic squeeze on the true spectral mass. Moreover, at every finite level its quadrature weights admit an exact normalized Gibbs representation in terms of (i) the beta-Hermite eigenvalue cloud and characteristic-polynomial derivative and (ii) an independent Dirichlet endpoint-weight field. This reduces level 3 to a single intrinsic multiscale problem about the quadrature-weight field.

## 1. Continuity, exclusions, source and literature boundary

Before new mathematics I reread/recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the controlling `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, the active D0039 claim, the newest R14 D0039 report, and the neighboring R15 D0039 source screen. I preserved all prior handoffs and exclusions.

I also refreshed the source/literature boundary on 2026-09-18. Virág's Section 4 still says:

- the zeros of the degree-`n` orthogonal polynomial of the semi-infinite beta-Hermite measure `mu_beta` are distributed as the `n`-point beta-Hermite ensemble;
- these eigenvalues are **exactly the Gaussian quadrature points** for `mu_beta`;
- `dim_H(mu_beta)=(1-2/beta)^+` almost surely;
- Question 1 asks whether this beta-Hermite measure has the same fractal spectrum as a Gaussian multiplicative cascade with the same Hausdorff dimension.

The bounded fresh search again found no source-matching later full solution. Lambert--Paquette (arXiv:2508.01458, 2025) remains the closest Gaussian-beta input: it gives a bulk description of the characteristic polynomial capturing both the local Sine-beta field and global/mesoscopic log-correlated structure. The exact circular-beta/GMC literature is not a closure of Virág's real-line beta-Hermite question. Classical Chebyshev--Markov--Stieltjes (CMS) separation inequalities are old orthogonal-polynomial/moment theory; modern reviews and Gilboa--Peled's 2015 differential paper explicitly treat the classical inequalities as the baseline. I make no novelty claim for CMS, Gaussian quadrature, the endpoint resolvent residue, or Dirichlet spectral weights. The combination below is a research route; priority is **UNVERIFIED / folklore-adjacent** until a proper citation graph is checked.

## 2. Frozen metric and prior state

The claim freezes

`B_spectrum in {0,1,2,3}`.

The previous R14 run retained `B_spectrum=2`: at beta 4 and `E=0`, a speed-`log N` LDP for the positive Christoffel kernel had bulk rate

\[
I_{\rm bulk}(x)=(x-\tfrac34)^2,\qquad x\ge0.
\tag{2.1}
\]

It also proved a two-phase tangent CGF and the exact logarithmic-overlap sum, but found that a **fixed deterministic energy** Christoffel exponent alone does not identify local spectral dimension by the Jitomirskaya--Last route: a subordinate projective direction enters that formulation.

Level 3 still requires a proved nonzero-width interval of local-dimension level sets for `mu_4` with the correct Hausdorff dimensions. This run gives a direct quadrature-cell conversion mechanism, but it does not yet prove the necessary quenched multiscale count/Frostman theorem. Hence

`B_spectrum: 2 -> 2`.

The shared numerical stagnation counter remains `UNKNOWN`; I do not replace it by a guessed number.

## 3. Method #8 — DISCRETIZE: use the *intrinsic* Gaussian-quadrature mesh

Let `p_n` be the degree-`n` orthonormal polynomial for a probability measure `mu` with all moments, and let

\[
\xi_{1,n}<\cdots<\xi_{n,n}
\]

be its zeros. Define the Gaussian quadrature / Christoffel weights

\[
q_{j,n}:=\frac1{K_{n-1}(\xi_{j,n},\xi_{j,n})},
\qquad
K_{n-1}(x,x)=\sum_{k=0}^{n-1}p_k(x)^2,
\tag{3.1}
\]

and cumulative sums `S_{j,n}=sum_{k<=j}q_{k,n}`.

For `mu=mu_beta`, Virág's Theorem 4.1 identifies the nodes `xi_{j,n}` exactly with the eigenvalues of the `n`-point beta-Hermite ensemble. Thus there is no reason to impose an external `n^{-1/2}` mesh: the source itself supplies the right random mesh.

### Proposition 3.1 — exact CMS cell-mass squeeze

For every interior index `2 <= j <= n-1`,

\[
\boxed{
q_{j,n}
\le
\mu\bigl((\xi_{j-1,n},\xi_{j+1,n}]\bigr)
\le
q_{j-1,n}+q_{j,n}+q_{j+1,n}.
}
\tag{3.2}
\]

Boundary variants use the obvious one-sided cells.

#### Proof

The classical Chebyshev--Markov--Stieltjes separation theorem gives, with `F(x)=mu((−infty,x])`,

\[
F(\xi_{j,n})\le S_{j,n}\le F(\xi_{j+1,n}-).
\tag{3.3}
\]

For the lower bound in (3.2), (3.3) at indices `j` and `j-1` gives

\[
F(\xi_{j+1,n})\ge S_{j,n},
\qquad
F(\xi_{j-1,n})\le S_{j-1,n},
\]

and therefore

\[
F(\xi_{j+1,n})-F(\xi_{j-1,n})
\ge S_{j,n}-S_{j-1,n}=q_{j,n}.
\]

For the upper bound, (3.3) at `j+1` and `j-2` gives

\[
F(\xi_{j+1,n})\le S_{j+1,n},
\qquad
F(\xi_{j-1,n})\ge F(\xi_{j-1,n}-)\ge S_{j-2,n},
\]

hence

\[
F(\xi_{j+1,n})-F(\xi_{j-1,n})
\le S_{j+1,n}-S_{j-2,n}
=q_{j-1,n}+q_{j,n}+q_{j+1,n}.
\]

This is (3.2). No regularity, density, subordinacy or probabilistic input is used. ∎

### Consequence for local dimensions

Suppose along a nested sequence of interior quadrature cells around an energy `E` one has

\[
\xi_{j_n+1,n}-\xi_{j_n-1,n}=n^{-1/2+o(1)}
\tag{3.4}
\]

and the three neighboring quadrature weights satisfy

\[
q_{j_n+r,n}=n^{-x+o(1)},\qquad r=-1,0,1.
\tag{3.5}
\]

Then (3.2) implies

\[
\mu_\beta\bigl((\xi_{j_n-1,n},\xi_{j_n+1,n}]\bigr)
=n^{-x+o(1)}.
\tag{3.6}
\]

Consequently, **provided the nested/all-scale control needed for a true pointwise limit is established**, the local dimension is

\[
\boxed{\alpha=2x.}
\tag{3.7}
\]

This is the key route correction. The subordinate/Weyl projective point remains relevant to the Jitomirskaya--Last formulation, but it is not required for the direct Gaussian-quadrature-cell formulation: CMS compares the finite quadrature weights directly with the true infinite-measure mass.

The words “provided the nested/all-scale control” are essential. A one-scale collection of good cells is not yet a local-dimension theorem.

## 4. Exact endpoint Gibbs representation for the quadrature weights

The discretization above becomes substantially more useful because the whole weight vector has an exact finite-dimensional representation.

Let `J_n` be any real Jacobi matrix with diagonal entries arbitrary and positive off-diagonals

\[
c_1,\ldots,c_{n-1}>0,
\]

let

\[
D_n(z)=\det(zI-J_n),
\qquad
C_n=\prod_{k=1}^{n-1}c_k^2,
\tag{4.1}
\]

and let `xi_1<...<xi_n` be its eigenvalues. For a normalized eigenvector `v^(j)` at `xi_j`, put

\[
q_j=|v^{(j)}_1|^2,
\qquad
r_j=|v^{(j)}_n|^2.
\tag{4.2}
\]

For the principal minor of `J_beta`, `q_j` is exactly the Gaussian quadrature weight (3.1).

### Proposition 4.1 — endpoint residue identity and normalized Gibbs form

For every `j`,

\[
\boxed{
q_j r_j=\frac{C_n}{D_n'(\xi_j)^2}.
}
\tag{4.3}
\]

Consequently

\[
\boxed{
q_j=
\frac{\bigl[r_jD_n'(\xi_j)^2\bigr]^{-1}}
{\displaystyle\sum_{\ell=1}^{n}\bigl[r_\ell D_n'(\xi_\ell)^2\bigr]^{-1}}.
}
\tag{4.4}
\]

Equivalently, since `D_n'(xi_j)=prod_{ell != j}(xi_j-xi_ell)`, the quadrature measure is an exact normalized discrete Gibbs measure on the eigenvalue cloud with unnormalized weights

\[
W_j=\frac1{r_j}\prod_{\ell\ne j}|\xi_j-\xi_\ell|^{-2}.
\tag{4.5}
\]

#### Proof

The `(1,n)` entry of the resolvent is obtained by the tridiagonal cofactor formula:

\[
[(zI-J_n)^{-1}]_{1n}
=\frac{\pm\prod_{k=1}^{n-1}c_k}{D_n(z)}.
\tag{4.6}
\]

On the other hand, spectral decomposition gives

\[
[(zI-J_n)^{-1}]_{1n}
=\sum_{j=1}^n\frac{v^{(j)}_1v^{(j)}_n}{z-\xi_j}.
\tag{4.7}
\]

Taking the residue at `z=xi_j` in (4.6)--(4.7) and squaring yields (4.3). Thus

\[
q_j=\frac{C_n}{r_jD_n'(\xi_j)^2}.
\tag{4.8}
\]

Summing (4.8) over `j` and using `sum_j q_j=1` gives

\[
C_n^{-1}=\sum_{\ell=1}^n\frac1{r_\ell D_n'(\xi_\ell)^2},
\]

which substituted back into (4.8) is (4.4). ∎

This identity is elementary linear algebra; it is not claimed as new. Its significance for D0039 is that the entire fractal-mass approximation is now an explicit random Gibbs field rather than an implicit boundary-value event.

## 5. Beta-Hermite specialization: the endpoint factor is independent Dirichlet

In the source-normalized increasing beta-Hermite coupling, the `n x n` principal minor of `J_beta` has iid Gaussian diagonal entries and increasing chi off-diagonal degrees. Reversing the coordinate order converts it to the standard finite Dumitriu--Edelman beta-Hermite tridiagonal with decreasing chi degrees. Under this reversal, the original last coordinate `e_n` becomes the standard first coordinate.

Virág's finite beta-Hermite discussion records that the first-coordinate spectral weights of the standard tridiagonal are independent of the eigenvalues and have

\[
\operatorname{Dirichlet}(\beta/2,\ldots,\beta/2)
\tag{5.1}
\]

distribution. Therefore, in (4.4), conditional on the ordered eigenvalue vector,

\[
\boxed{(r_1,\ldots,r_n)\ \perp\ (\xi_1,\ldots,\xi_n),
\qquad
(r_1,\ldots,r_n)\sim\operatorname{Dirichlet}(\beta/2,\ldots,\beta/2).}
\tag{5.2}
\]

At the frozen test value `beta=4`, one may write

\[
r_j=\frac{G_j}{\sum_{\ell=1}^nG_\ell},
\qquad
G_1,\ldots,G_n\stackrel{\rm iid}{\sim}\Gamma(2,1),
\tag{5.3}
\]

independently of the eigenvalue cloud.

Combining (4.4) and (5.3) gives the exact beta-4 finite-level representation

\[
\boxed{
q_j=
\frac{\bigl[G_jD_n'(\xi_j)^2\bigr]^{-1}}
{\displaystyle\sum_{\ell=1}^{n}\bigl[G_\ell D_n'(\xi_\ell)^2\bigr]^{-1}}.
}
\tag{5.4}
\]

(The common factor `sum G_ell` cancels.)

This is the strongest new route-level fact in this run. The derivative term is a functional of the beta-Hermite point cloud; the independent gamma factor is explicit; and Lambert--Paquette's 2025 bulk characteristic-polynomial analysis is designed precisely to split characteristic-polynomial behavior into a local Sine-beta part plus a global/mesoscopic log-correlated field. Their published theorem does not, however, state the quenched multifractal theorem for the normalized weights (5.4), so I do not treat level 3 as imported from that paper.

## 6. Method #13 — FIND WHAT ONLY INCREASES: cumulative quadrature mass

The useful monovariant is not an EFGP amplitude. It is the cumulative mass itself.

Both

\[
F(x)=\mu_\beta(( -\infty,x])
\quad\text{and}\quad
S_{j,n}=\sum_{k\le j}q_{k,n}
\tag{6.1}
\]

are monotone, and CMS interlaces them in the strong deterministic sense (3.3). In parallel, Sturm oscillation makes the eigenvalue-counting / Prüfer phase monotone in energy. Thus a candidate exceptional energy need not be tracked through an unstable arbitrary projective boundary direction: it can be trapped between neighboring quadrature nodes whose cumulative weights already bracket the true distribution function.

This is a real change in the obstruction. The preceding report's statement

> “the missing variable is the subordinate/Weyl projective direction”

remains correct **for that JL conversion route**, but it is no longer a necessary global blocker for D0039. The direct CMS route bypasses it.

## 7. Method #27 — SWAP THE QUANTIFIERS: control one whole random quadrature field

The previous route asked, effectively:

> for each exceptional energy `E`, can one prove that the fixed boundary direction aligns with the subordinate direction and then control a second solution?

The quadrature route asks instead:

> can one prove, on one high-probability/quenched environment event, simultaneous multiscale estimates for the complete vector `{(xi_{j,n},q_{j,n})}` over all bulk indices and a hierarchy of `n`?

That quantifier swap is favorable because both pieces are finite-dimensional source objects. There is no union over arbitrary deterministic energies and no separate Weyl variable. The exact weight field is (5.4), and the true measure is deterministically squeezed by (3.2).

## 8. Exact match of the candidate rate with the GMC parabola — still conditional on a multiscale theorem

Suppose the beta-4 quadrature field is proved to have, on a compact bulk interval, the following quenched exponent count:

\[
\#\{j:\ \xi_{j,n}\in I,\ q_{j,n}=n^{-x+o(1)}\}
=n^{1/2-I_{\rm bulk}(x)+o(1)},
\tag{8.1}
\]

with enough neighbor consistency and two-scale correlation to select nested cells. The factor `n^{1/2}` is the natural number of unscaled beta-Hermite eigenvalues in a fixed bulk energy interval, because the local spacing there is `n^{-1/2+o(1)}`.

Then Proposition 3.1 gives local dimension `alpha=2x`, and the Hausdorff dimension of the resulting energy set is

\[
\frac{\frac12-I_{\rm bulk}(x)}{\frac12}
=1-2I_{\rm bulk}(x).
\tag{8.2}
\]

Using the level-2 rate (2.1) and `x=alpha/2`, this becomes

\[
\boxed{
f(\alpha)
=1-\frac12(\alpha-\tfrac32)^2,
}
\tag{8.3}
\]

on its admissible range. This is exactly the beta-4 GMC parabola targeted in the preceding report. At the source-typical dimension `alpha=1/2`, one has `x=1/4`, `I_bulk(x)=1/4`, and (8.2) gives `1/2`, consistent with the known Hausdorff dimension of `mu_4`. At the Lebesgue-typical kernel exponent `x=3/4`, (8.3) has `alpha=3/2` and ambient dimension one; this is not a contradiction because those energies need not carry positive `mu_4` mass.

Equations (8.1)--(8.3) are **not** counted as a proved level-set theorem. What is proved this run is the deterministic implication from a sufficiently strong quadrature-weight multiscale theorem to the local-mass exponent, plus the exact finite-level Gibbs representation to which the missing stochastic theorem can be applied.

## 9. The new single stochastic blocker

The earlier two-blocker formulation was:

1. an actual-energy exponentially tilted phase-overlap theorem; and
2. subordinate/Weyl alignment plus exponent saturation.

The CMS/Gibbs route replaces those by one more intrinsic target.

### QUAD-GMC_4

On some compact unscaled bulk interval `I` and some nonzero-width exponent interval corresponding, for example, to a closed `alpha`-interval strictly inside `(1/2,1)`, prove simultaneously across a geometric hierarchy of `n` that:

1. **cell scale:** the selected beta-Hermite Gaussian-quadrature cells have diameter `n^{-1/2+o(1)}`;
2. **weight exponent/count:** the number of nodes with `q_{j,n}=n^{-x+o(1)}` is `n^{1/2-I_bulk(x)+o(1)}`;
3. **neighbor consistency:** `q_{j-1,n},q_{j,n},q_{j+1,n}` have the same exponent on the selected cells, or an alternative CMS-compatible finite-neighbor condition holds;
4. **nesting/Frostman control:** enough two-scale joint control holds to construct nested exceptional cells and matching upper/lower Hausdorff bounds.

Because of (5.4), this can be attacked directly through the joint field

\[
\left\{\log|D_n'(\xi_j)|,\ \log G_j\right\}_{j:\xi_j\in I},
\tag{9.1}
\]

rather than through arbitrary-energy JL alignment. Lambert--Paquette's characteristic-polynomial asymptotics provide the closest published machinery for the first term, including local Sine-beta structure and a log-correlated global field. The missing step is to transfer that machinery, at the necessary quenched exponential strength and uniformly at the random zeros, to the normalized derivative field in (5.4), then perform the multiscale count/Frostman argument.

If QUAD-GMC_4 is proved on any nonzero-width alpha interval with (8.3), the frozen metric moves `2 -> 3`. Until then it stays 2.

## 10. What happened to the three methods

- **#8 succeeded strongly as a route change.** Replacing an external energy mesh by the exact Gaussian-quadrature nodes produces the CMS cell squeeze (3.2) and the exact endpoint Gibbs representation (4.4)/(5.4).
- **#13 succeeded.** Cumulative quadrature weights and the true spectral CDF are monotone and interlaced by CMS; this gives direct local-mass brackets without tracking a second Jacobi solution.
- **#27 succeeded diagnostically and structurally.** The hard quantifier is now simultaneous control of one finite random quadrature field across scales, rather than a separate subordinate-alignment assertion for every candidate energy.

The metric nevertheless has **no movement**, because no nonzero-width local-dimension level-set theorem has yet been completed.

## 11. Next nonrepeating methods

The next D0039 run should not return to another fixed-energy cumulant lemma. Use three methods not yet used on D0039:

- **#4 PROVE SOMETHING WEAKER, COMPLETELY:** prove QUAD-GMC_4 first on a single compact exponent interval safely inside the second-moment regime, not the full parabola;
- **#14 FIND THE GROUP ACTING:** exploit the exchangeability of the independent Dirichlet/Gamma endpoint factors and ordering symmetry of the beta-Hermite cloud to isolate the genuinely spatial part of (5.4);
- **#19 MAKE IT AN ALGORITHM:** formulate an explicit nested-cell selection/Frostman construction on the random Gaussian-quadrature tree, so every stochastic estimate needed for level 3 is visible and finite-scale checkable.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R14
  lane: HARD_OUTSIDE
  target: D0039
  source: "Balint Virag, Operator limits of random matrices, ICM 2014 / arXiv:1804.06953, Section 4, Question 1"
  status: PARTIAL
  metric:
    name: B_spectrum
    before: 2
    after: 2
    movement: false
  authoritative_stagnation_count: UNKNOWN
  methods_used: [8, 13, 27]
  proved_this_run:
    - "exact CMS cell-mass squeeze q_j <= mu((xi_{j-1},xi_{j+1}]) <= q_{j-1}+q_j+q_{j+1}"
    - "exact endpoint-resolvent identity q_j r_j = prod(c_k^2)/D_n'(xi_j)^2"
    - "exact normalized endpoint Gibbs representation q_j proportional to [r_j D_n'(xi_j)^2]^{-1}"
    - "for beta-Hermite increasing coupling, terminal endpoint weights r are independent Dirichlet(beta/2,...,beta/2) after reversal; beta=4 gives iid Gamma(2,1) normalization"
    - "direct quadrature-cell route bypasses the subordinate/Weyl alignment blocker required by the prior JL route"
  conditional_not_counted:
    - "alpha=2x as a pointwise local dimension requires nested/all-scale cell-width and neighbor-weight control"
    - "f(alpha)=1-(alpha-3/2)^2/2 requires the quenched multiscale quadrature-weight count/Frostman theorem QUAD-GMC_4"
  remaining_obligation:
    - "prove QUAD-GMC_4 on any nonzero-width alpha interval, via the derivative-at-random-roots field in the exact Gibbs representation"
  literature_boundary:
    checked_utc_date: "2026-09-18"
    no_source_matching_full_solution_found_in_bounded_search: true
    classical_components_not_claimed_novel: ["Gaussian quadrature", "CMS inequalities", "resolvent cofactor identity", "Dirichlet beta-Hermite spectral weights"]
  next_methods: [4, 14, 19]
```

## 13. Model / scheduler-control note

The exposed task-management surface still provides prompt/title/schedule/timing/enabled controls but no binding model-family selector, reasoning-effort selector, guaranteed-duration field, or authenticated completed-run model telemetry. Thus GPT-6/maximum remains prompt-only in this environment, and this report truthfully records GPT-5.6 Sol with reasoning level UNVERIFIED. A task that returns `You cannot modify this task` must be changed from an authorized owning/admin context or by platform support; no permission bypass, duplicate scheduler, or scheduler change was attempted here.
