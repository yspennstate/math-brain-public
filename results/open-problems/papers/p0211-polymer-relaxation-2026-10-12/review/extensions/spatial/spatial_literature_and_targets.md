# Spatial extensions: priority, scope, and further targets

Primary-source review updated 12 October 2026. The mathematical results written in `spatial_diffusion.tex` and `critical_scaling.tex` are proved within this project. The review below calibrates their relation to existing work; a bounded search cannot certify universal priority.

## Position of the proved result

The exact formula

\[
 \gamma_{\rm sp}=\min\{\gamma_Q,\eta_1+D\lambda_G\}
\]

uses two specific features: exchangeable cut reactions and a higher-degree spectral barrier. It controls every finite weighted graph, all positive reaction parameters, and bounded reversible changes of the reaction conductances. Its graph dependence is explicit, and the new critical functions separate the count and degree-one modes. This is a substantial extension of the model-specific relaxation analysis. It does not solve relaxation for arbitrary spatial coagulation and fragmentation.

### Most relevant comparisons and citation placement

- **Exclusion with reservoirs.** Salez's [2023 paper](https://arxiv.org/pdf/2201.03463), especially its setup and spectral-gap/cutoff corollaries, treats independent Bernoulli resets at sites. Its [2024 paper](https://arxiv.org/pdf/2305.04688), Theorem 2, gives the gap identity for heterogeneous reservoir densities. These belong beside the exact graph formula in the introduction. Here the death rate depends on the total occupancy, and the invariant law is not the reservoir product law. Thus their stated generators do not directly give the present formula. The reaction chain at (D=0) also fails monotonicity in the inclusion order: ({x}\subset{x,y}), but the common particle can die only in the upper state. This last observation is specific to the reaction chain; fast diffusion can alter the order comparison.

- **Recent inclusion results.** [Kim–Sau (2026)](https://link.springer.com/article/10.1007/s00220-026-05728-9) provide related one- and two-particle reductions. This is appropriate contemporary context, not a theorem for the present count-dependent reactions.

- **Conservative interchange.** [Caputo–Liggett–Richthammer (2010), Theorem 1.1](https://arxiv.org/pdf/0906.1238), proves equality between the interchange gap and the graph random-walk gap. That equality is established prior work. The present spatial proof needs only the explicit degree-one graph action, because the reaction barrier controls all higher degrees.

- **A genuinely spatial interval model.** [Bernardin–Toninelli (2012)](https://arxiv.org/pdf/1107.3227), Sections 2–3, uses interval partitions with pinning/renewal weights. For a tail (K(j)\propto j^{-1-\alpha}), (0<\alpha<1), their heat-bath process has distinct localized, delocalized, and critical regimes. For fixed pinning parameter above criticality, TV mixing lies between constants times (L^\alpha) and (L^\alpha(\log L)^C); below criticality the relaxation time is bounded and TV mixing is bounded between logarithmic and polylogarithmic scales. At criticality their displayed bounds include (cL^\alpha\le T_{\rm rel}\le CL^{1+\alpha}). This is the best comparison when explaining the limits of the exchangeable stationary law used here.

The paired reaction-factor corollary is a direct Dirichlet-form comparison. Its value is that it transfers the exact base scales to configuration-dependent environments; it should be described as a corollary, not as a general kernel theorem.

## Further target 1: sharp mixing for the present spatial process

The exact gap does not by itself identify worst-case TV mixing. A precise next target is a matching mixing-time estimate for the cycle or torus, uniform across the count/diffusion crossover, starting with fixed (b>0), (eta=b/n), or with (n^2\beta\to b). The current arbitrary-start polymer argument gives a near-matching TV bound for the unlabelled chain; it does not automatically give cutoff for the spatial cut process or remove the extra logarithm.

This target is concrete and closest to the new results. It requires controlling transient densities and spatial-mode multiplicities, not only their smallest eigenvalues. The existing reservoir cutoff theorem illustrates how much additional information is needed beyond a spectral-gap identity.

## Further target 2: a nonexchangeable renewal equilibrium

In the Bernardin–Toninelli model, determine the critical relaxation exponent

\[
 z(\alpha)=\lim_{L\to\infty}\frac{\log T_{\rm rel}(L,1)}{\log L},
\]

if the limit exists. A concrete hypothesis to test is (T_{\rm rel}(L,1)=L^{\alpha+o(1)}); a strict improvement of the cited upper exponent would already change the known conclusion of that paper. A related target is a uniform estimate for pinning parameters approaching criticality, for example in the candidate window (lambda=1+cL^{-\alpha}).

These are research targets, not claims established here. This review checked the original bounds but did not certify the absence of every subsequent improvement as of 2026. The proposed (z(\alpha)=\alpha) hypothesis should be tested before being called a conjecture supported by evidence. This direction is less symmetric and more physically spatial than the proved cut model.

## Further target 3: graph-local cycle splitting with an Ewens bias

On permutations of a graph's vertices, transpose an edge at rate (c_{xy}\vartheta) if it splits a permutation cycle and at rate (c_{xy}) if it merges two cycles. The law proportional to (artheta^{\#\mathrm{cycles}}) is reversible. For a fixed compact interval of positive (artheta), a precise question is whether its spectral gap is comparable to (lambda_G), uniformly over graphs and their sizes, and what replaces such a comparison if it fails.

The parameter-one case is the established interchange theorem. On the complete graph, [Jiang (2015), Theorem 2.1](https://arxiv.org/pdf/1204.1671), already proves cutoff from the identity for a fixed-parameter Metropolis transposition chain converging to an Ewens law. Jiang's parameter is the reciprocal of the Ewens parameter. This substantially limits novelty claims for that special case; the graph-local statement above is a separate, unproved target.

[Ioffe–Tóth (2020)](https://arxiv.org/html/1909.06188v2) proves convergence of stationary torus cycle dynamics to canonical split–merge dynamics on an appropriate time scale. Their stationary theorem is not a mixing theorem from arbitrary initial conditions. The elementary calculation in `interchange_projection_obstruction.md` explains why stationary averaging of local transpositions is insufficient to identify the actual cycle-process relaxation.

## Logarithmic Sobolev scope

[Salez (2021)](https://ahl.centre-mersenne.org/articles/10.5802/ahl.99/) concerns fixed-color-count multislices and gives sharp logarithmic Sobolev estimates there. It should be cited when comparing entropy methods with harmonic methods, without transferring a fixed-layer result to variable-cardinality reactions.

There is also a direct obstruction to a uniform ordinary logarithmic Sobolev constant comparable to the polymer gap over all (eta). With the convention (alpha_{\rm LS}=\inf \mathcal E(f,f)/\operatorname{Ent}_\pi(f^2)), test the indicator of the all-monomer state (A). Its exit rate is (n-1), so

\[
 \alpha_{\rm LS}\le\frac{n-1}{\log(1/\pi_M(A))}.
\]

For fixed (n\ge2), (pi_M(A)\sim(\beta n)^{n-1}/n!) as (eta\downarrow0). The bound tends to zero while the gap tends to (2/n). This does not rule out an appropriate modified logarithmic Sobolev estimate or a restricted-parameter entropy theorem.

## Bibliography and source-check limits

Verified BibTeX is in `spatial_references.bib`. The substantive comparison sources above were read at the theorem/model level, not merely identified by titles. Searches for creation/deletion with stirring, spatial coagulation–fragmentation gaps, and exchangeable birth–death models did not identify the exact new minimum formula. That is a limited negative search result. The manuscript should state the theorem and its proof plainly and avoid claiming to settle an established named open problem without further expert review.
