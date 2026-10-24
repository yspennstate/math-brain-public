# Solved-problem register

Date: 2026-06-01

This register is the explicit solved-results list for the Downloads snapshot.
Novelty/publishability labels are conservative: "publishable" means suitable
for a manuscript or serious note after normal literature and referee checks,
not a claim that no adjacent result exists under different language.

## Fully solved / manuscript-grade

1. Gaussian real phase-retrieval stability scale.
   - Result: for iid Gaussian `A in R^{(2m-1) x m}`,
     `omega(A)=4^{-m+o_P(m)}`.
   - Novelty: appears novel against the project literature bank and the
     Randomstrasse/Balan-Wang framing.
   - Publishability: yes; already written as the main `phase_retrieval_omega`
     manuscript.

2. Dyson-index square-submatrix minimum law.
   - Result: for real/complex Gaussian tall matrices with `n/m -> gamma`,
     the minimum square-submatrix least singular value has exponential base
     `c_gamma^{-1/d_F}`.
   - Novelty: appears novel as a clean extension of the fixed-apex method.
   - Publishability: yes as part of the main manuscript.

3. Fixed-apex overlap combinatorics.
   - Result: exact overlap law and `E[1/D]=N/(m(N-m+1))`, with Lean support
     for the redundancy-two identities and second-moment envelopes.
   - Novelty: method-specific but reusable.
   - Publishability: yes as a supporting lemma/formal appendix.

4. Deterministic qualitative Balan-Wang bound.
   - Result: every full-spark `A in R^{(2m-1) x m}` obeys
     `omega(A) <= max_i ||a_i|| / sqrt(m)`.
   - Novelty: appears to be a clean elementary deterministic bound in this
     stability language.
   - Publishability: yes as a remark/proposition; it is not the exponential
     conjecture.

5. Exact real `Gr(2,5)` star-ratio theorem.
   - Result: for every real `5 x 2` Parseval frame,
     `min_i min_j w_ij / sum_{k != i,j} w_ik <= (4-sqrt(5))/11`, with equality
     at the dual regular pentagon.
   - Novelty: appears novel relative to the local Plucker/Grassmannian
     literature bank; final external literature check still needed.
   - Publishability: yes as a small theorem/supporting base case for the
     deterministic Plucker route.

6. Exact real rank-two `Gr(2,n)` star-ratio theorem.
   - Result: for every real `n x 2` Parseval frame, `n >= 3`,
     `min_i min_{j != i} w_ij/sum_{k != i,j} w_ik <= alpha_n/(1-alpha_n)`,
     where `alpha_n=(2/n)sin^2(pi/n)`, with equality at the uniform leverage
     regular projective `n`-gon.
   - Novelty: appears project-new after a quick literature smoke check; final
     external citation pass still needed.
   - Publishability: yes as a compact proposition in the deterministic
     Plucker/Balan-Wang note.

## Solved supporting increments

7. Sign-free `K5` star-ratio relaxation.
   - Result: arbitrary nonnegative `K5` edge weights satisfy the weaker sharp
     bound `<= 1/3`, equality only for uniform weights.
   - Novelty: elementary barrier lemma.
   - Publishability: supporting lemma, not a standalone main result.

8. Plucker inverse-leverage equivalence.
   - Result: the best squared circuit ratio `C(Q)` satisfies
     `K(Q) <= C(Q) <= (m-1)K(Q)/(1-K(Q))`.
   - Novelty: project-specific bridge between Plucker circuits and the
     order-statistic width problem.
   - Publishability: yes as a reduction lemma.

9. Bounded-density one- and two-dimensional local CLT inputs for P1.
   - Result: RV-scale directional delocalization gives the one-slab lower
     density, and the auxiliary pair-CLT assumption `phi_X in L^1` can be
     removed; bounded density gives the needed Fourier tail control.
   - Novelty: appears to be a clean analytic closure of this project's P1
     local-CLT side.
   - Publishability: supporting lemma; the random-matrix delocalization and
     correlation-average inputs remain open.

10. P1 averaged-delocalization fixed-apex criterion.
   - Result: the all-subsets RV-scale delocalization target is stronger than
     needed and inaccessible by a union-bound route; the fixed-apex proof only
     needs a large good family plus an averaged correlation kernel.
   - Novelty: route-correction/reduction for the non-Gaussian universality
     problem.
   - Publishability: supporting proof-strategy proposition.

11. P1 random-subset exchangeability reduction.
   - Result: single-submatrix null-normal delocalization implies
     typical-good-family delocalization by exchangeability; random-pair kernel
     expectations control empirical fixed-apex kernel averages.
   - Novelty: proof-strategy reduction turning the P1 family problem into a
     single-matrix estimate plus a random-pair estimate.
   - Publishability: supporting proposition for the non-Gaussian universality
     route.

12. Top-top Plucker template scalar Lean lemma.
   - Result: Lean verifies the scalar numerator inequality behind the
     top-top dyadic partner-capacity template.
   - Novelty: local proof infrastructure for the Plucker route.
   - Publishability: proof infrastructure, not standalone.

13. Fixed-apex Poisson first-two-moment reduction.
   - Result: at the first-moment threshold `L_m p(t_m)=lambda`,
     `E Z_{t_m}=lambda` and
     `E[Z_{t_m}(Z_{t_m}-1)]/lambda^2 = 1+O(1/m)+exp(-(log 4+o(1))m) poly(m)`.
   - Novelty: appears to be a new subexponential-law reduction inside this
     project.
   - Publishability: supporting lemma; the full Poisson/Chen-Stein theorem is
     still open.

14. Subexponential distance-threshold constants.
   - Result: the fixed-apex distance proxy has first-moment scale
     `2 sqrt(2) pi lambda sqrt(m) 4^{-m}`, while the all-apex distance
     incidence proxy has scale `sqrt(2) pi lambda 4^{-m}/sqrt(m)`.
   - Novelty: project bookkeeping, but it sharpens the P2 target constants.
   - Publishability: supporting calculation; it identifies the scale a future
     Poisson/swap-control proof must reach.

15. P1 conditional good-family second-moment reduction.
   - Result: a fixed-apex good family with asymptotic one-slab probabilities
     and averaged pair probability at most the Gaussian product scale yields
     conditional success probability `1-o(1)`.
   - Novelty: project-new deterministic reduction.
   - Publishability: supporting proposition for the non-Gaussian universality
     route; the random-matrix good-family input remains open.

16. P1 single-normal delocalization and D-stratified pair target.
   - Result: Nguyen--Vu's normal-vector theorem supplies the needed
     single-submatrix RV-scale delocalization for bounded-density subgaussian
     entries after the exchangeability reduction; the remaining random-pair
     theorem is sharpened to a conditional-overlap estimate
     `E[(1-rho_ST^2)^(-1/2) | D] <= 1+C/D+eta_m(D)` for `D>=3`, with
     `D<=2` treated as high-overlap error.  The kernel estimate is further
     reduced to a Gaussian-scale even-moment hierarchy
     for conditional residual null lines, plus a no-near-parallel tail bound.
     The near-parallel edge is now reduced further to deterministic slab,
     tail-to-kernel, least-squares/cap, Gaussian calibration, and
     determinant-tilted density formulations, with a constant audit showing
     that rowwise slabs alone overcount in `D` and a density probe supporting
     Cauchy-scale `z=-B^{-1}a` small balls for tested bounded-density laws.
     The determinant-tilted coefficient is further factored into a one-row
     slice density and sliced determinant moment, with direct diagnostics
     showing Gaussian-scale coefficients for tested laws.  The scalar slice
     density is reduced to a frame-leverage radius-window condition, while the
     determinant factor is reduced to a sliced covariance determinant bound.
   - Novelty: route-sharpening reduction plus diagnostic evidence.
   - Publishability: supporting proof infrastructure for the non-Gaussian
     universality route; not standalone.

## Not solved yet

- Non-Gaussian bounded-density universal upper bound; for subgaussian entries
  the single-submatrix input is covered, and the main remaining input is
  rigorous conditional residual-line angular universality and a Haar-comparable
  anti-alignment/cap bound, benchmarked by the exact Haar beta law for
  `1-rho^2`, with the edge reduced to determinant-aware least-squares density
  targets plus slab/projection-density fallback estimates.
- Deterministic Balan-Wang exponential conjecture.
- Full quantitative Plucker imbalance for `Gr(m,2m-1)`.
- Full Poisson limit and exact subexponential law for the Gaussian minimum.
- Complex phase retrieval at the true complex threshold.
