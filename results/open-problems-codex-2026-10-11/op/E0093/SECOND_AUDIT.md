# Hostile-referee audit of the second attempt — 2026-10-12

Verdict for E0093: PARTIAL. The endpoint is a proved sparse-generator
special case S_3 x C_p, not an answer for arbitrary finite groups.

## Proof checks

1. **Generator conditioning.** Generation is exactly the intersection of
   S_3 generation and nonzero cyclic pair for prime p>3. The sixth-power
   argument proves sufficiency without assuming a product subgroup is
   automatically the full product. There are 18 generating S_3 pairs.
   The two conditioning events concern initially independent coordinates;
   no independence is assumed between cyclic coordinates after excluding
   (0,0). The upper bound handles this by dividing by 1-p^-2.
2. **Model conventions.** The walk is symmetric and half-lazy, with four
   increment labels each of weight 1/8. Labels and multiplicities remain.
   Normal-subgroup comparisons use this same normalization throughout.
3. **Projection.** Pi is the orthogonal average over a normal subgroup,
   commutes with every right translation, and gives an exact quotient law
   from a subgroup-uniform initial law. Only the residual density uses L2;
   the quotient contribution remains its full TV profile.
4. **Dirichlet form.** The factor is 1/(4k), giving gap at least
   1/(2kD^2). The proof applies the energy inequality to eigenvectors.
   A lower bound on an energy does not itself give an absolute operator
   norm bound for a nonlazy chain; half-laziness is essential here.
5. **Finite S_3 spectrum.** The right coset-coordinate Fourier calculation
   supplies all six dimensions, with precisely four in the fiber complement.
   The transposition and cycle matrices are unitary in that basis.
   The two cases exhaust generating pairs. Squaring the traceless 2x2
   blocks and weighted Cauchy–Schwarz give the claimed rho.
6. **Density normalization.** n-q=4p, so the TV prefactor is sqrt(p),
   not p, 2p, or sqrt(6p). Uniform coset-fiber laws have exactly quotient TV.
7. **Gaussian grid bound.** Both signs are covered by a shifted circular
   grid. Removing the point closest to zero and integrating disjoint
   adjacent intervals bounds the infinite grid by 1 plus the Gaussian
   integral divided by spacing. The finite grid is a subset, including
   the half-shifted odd-p case. No continuous approximation is assumed.
8. **Fourier moment bound.** For each nonzero frequency the unconditioned
   cyclic phases are independent uniform roots. The nontrivial zero-
   frequency parity character has eigenvalue at most 1/2, since at least
   one generator is odd. Markov is applied to squared quotient TV with
   the explicit fiber error subtracted from epsilon.
9. **Typical vs uniform.** An O(1/u) tail makes t_mix/p tight; it does
   not make it concentrate at a constant. The exceptional a=b pair has
   quadratic mixing and probability O(1/p), consistent with the tail.
10. **No cutoff.** Pigeonholing p points into fewer than p squares yields
    a nontrivial slow character. Its identity-start real part has norm
    at most one and mean zero under uniform measure, proving the TV lower
    bound. Tight mixing times also make any proposed random cutoff centers
    tight; this yields a positive post-center TV with probability at least
    3/4. Both deterministic and random centers are addressed under the
    exact convergence-in-probability definition in SECOND_ATTEMPT.md.
11. **Worst case.** The quotient either has a single generating odd/nonzero
    element, or is the product-coordinate walk after an automorphism.
    These cases exhaust all generating pairs. Direct Fourier sums give
    the uniform O(p^2) upper bound and the cycle projection gives the
    matching lower bound. This concerns this family, not alternating groups.
12. **Scope.** No published-solution verdict and no novelty claim are made.
    The normal-subgroup mechanism is known. A bounded commutator fiber
    does not generalize automatically to an arbitrary growing group.
13. **Lower tails.** Primitive integer vectors in a small positive box have
    distinct projective directions modulo p because their determinants
    have magnitude less than p. The nonzero cyclic pair is uniform over
    projective directions even after conditioning on generation. A divisor
    union bound gives at least R^2/4 primitive directions, and Bernoulli's
    inequality gives a uniform TV lower bound of 3/8 on their event.
14. **Mean vs typical.** The lower-tail bound is finite and uniform over
    integer times from p to p^2/(4C), not just a pointwise limiting bound.
    This justifies summing it for the mean lower bound. The mean upper bound
    uses the deterministic worst-case order-p^2 upper bound to truncate the
    tail sum; tightness alone would not justify it. Therefore order p log p
    for the mean and order p in probability are logically distinct results.

## Computation completed

- `second_checks.py`, `second_checks.json`: all 900 ordered pairs on
  S_3 x C_5 enumerated by exact subgroup BFS; exactly 432 generated,
  agreeing with 18(p^2-1). All generating S_3 pair commutators generated A_3.
- 41,472 phase-block evaluations (18 pairs, a 48x48 angular grid) checked
  complement invariance, nonnegative spectrum, and the upper bound rho.
  The maximal grid eigenvalue was 0.9330127018922195, equal to rho up to
  floating-point rounding. This grid is a numerical test; the continuous
  bound is proved algebraically.
- 45 exact finite sums evaluated with floating-point arithmetic checked
  the quotient first-moment bound for p=5,7,11,17,31, all three possible
  sign patterns, at t=1,p,3p.
- 24 direct full-group recursions for p=5,11,31,101 checked projection TV,
  the fiber bound and the mixing lower bound at every time up to 8p.
  Arrays had at most 606 entries. The rerun including both worst-case
  quotient upper bounds (15),(16) passed in 4.385 seconds.
- `second_boundary_checks.py`, `second_boundary_checks.json`: checked the
  pigeonhole spectral bound on all cyclic pairs for p=5,7,11,23 and 150
  sampled pairs each at p=101,1009. Exceptional-pair cyclic mixing matched
  the quadratic lower bound at p=5,11,23,101.
- The same script illustrates quotient tails with 100 correctly conditioned
  samples each at p=101,503,1009. The observed failure fractions at time 4p
  were .05,.07,.13. These small Monte Carlo samples are illustrative only;
  no limiting distribution or concentration claim depends on them. Sampling
  excludes (0,0) by rejection, preserving the specified conditioned law.

The numerical jobs are seconds long and use arrays far below 1 GB. Lean
verification completed; its exact scope is recorded below.

`tail_checks.py` and `tail_checks.json` checked 12 primitive-vector boxes
at p=101,503,1009,5003 and u=1,2,4. Distinct slopes and coprimality counts
are exact integer computations; the eigenvalue power bound uses floating
point. Every check passed. No Monte Carlo result is used to prove the
nonconcentration or mean-order statements in Theorem 10.

## Completed Lean verification

FiberAlgebra.lean kernel-checks six integral 2x2 matrix identities for
the standard S_3 representation, using Matrix.ext and decide +kernel.
I2 and Z2 are the explicit identity and zero matrices. The successful
command is recorded in lean_second.log, run from ~/lean_verify
with a 3600-second timeout. No sorry or native_decide is used.
Only the finite algebra is formalized; the operator bounds, Gaussian
grid estimate, probability formulas and asymptotic conclusions are
complete paper proofs, not Lean-verified theorems.

The first finite matrix attempts failed on missing instance/import
requirements; these errors did not establish any result. Only the
corrected exit-zero run is called checked.
