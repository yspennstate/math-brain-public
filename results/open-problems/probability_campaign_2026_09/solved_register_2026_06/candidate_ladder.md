# Candidate ladder

Date: 2026-05-31

## Easy / already cracked

1. Gaussian real phase-retrieval stability scale.
   Status: solved in `phase_retrieval_omega`; main result
   `omega(A)=4^{-m+o_P(m)}` and Dyson-index square-submatrix generalization.

2. Fixed-apex overlap combinatorics.
   Status: Lean-supported in `OmegaComb.Basic`; exact expectation
   `E[1/D]=N/(m(N-m+1))` is formalized.

3. Sign-free `K5` star-ratio relaxation for the `Gr(3,5)` base model.
   Status: solved. For nonnegative edge weights on `K5`,
   `min_d min_j w_dj/sum_{k != d,j} w_dk <= 1/3`, with equality only for
   uniform weights. This is a supporting barrier lemma, not the real Plucker
   extremal theorem.

4. Exact real `Gr(2,5)` star-ratio theorem.
   Status: solved. For every real `5 x 2` Parseval frame,
   `min_i min_j w_ij/sum_{k != i,j} w_ik <= (4-sqrt(5))/11`, with equality
   at the dual regular pentagon. This closes the first nontrivial Plucker
   base case for the deterministic Balan-Wang route.

5. Exact real rank-two `Gr(2,n)` star-ratio theorem.
   Status: solved. For every real `n x 2` Parseval frame, `n >= 3`,
   `min_i min_{j != i} w_ij/sum_{k != i,j} w_ik <= alpha_n/(1-alpha_n)`,
   where `alpha_n=(2/n)sin^2(pi/n)`, with equality at the uniform leverage
   regular projective `n`-gon. Novelty/publishability: apparently project-new
   after a quick literature smoke check; suitable as a compact proposition in
   the deterministic Plucker/Balan-Wang note after a final citation pass.

6. Bounded-density one- and two-dimensional local CLT inputs for P1.
   Status: solved as deterministic analytic lemmas. Bounded density, finite
   third moment, and RV-scale directional delocalization give the one-slab
   lower density and Gaussian pair local asymptotic at exponentially small
   slab widths; the temporary `phi_X in L^1` assumption has been removed.

## Medium

7. Non-Gaussian bounded-density universal upper bound.
   Status: reduced to two random-subset estimates: single-submatrix
   null-normal delocalization at the RV scale, and random-pair
   correlation-average/high-correlation control. Exchangeability turns the
   single-submatrix estimate into typical-good-family delocalization; no
   exponential all-subsets union bound is needed.

8. Exact subexponential law of the Gaussian minimum.
   Status: open, with a solved first-two-moment reduction. The fixed-apex
   count at first-moment threshold has the Poisson first and second factorial
   moments. The fixed-apex and all-apex first-moment threshold constants are
   now explicit; the remaining task is a Chen-Stein/local-dependence proof of
   the full Poisson law and control of the all-apex swap dependencies.

## Hard

9. Deterministic Balan-Wang exponential conjecture.
   Status: open. The project has a rigorous `1/sqrt(m)` bound, a variational
   sparse-vector formulation, a clean order-statistic width `K_m`, and a
   leverage reduction showing `K_m <= C rho^m` would imply the full conjecture.

10. Quantitative Plucker imbalance for `Gr(m,2m-1)`.
   Status: open route. A sufficiently imbalanced `(m+1)`-circuit would force an
   exponentially small critical submatrix singular value.

11. Complex phase retrieval at the true complex threshold.
   Status: not reduced yet. The existing paper proves the square-submatrix RMT
   analogue, not the full complex complement-property stability problem.
