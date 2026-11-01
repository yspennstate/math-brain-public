# Hostile-referee audit (2026-10-11)

The full conjecture is NOT proved. These checks assess the scope of the
claims in ATTEMPT.md, not just the correctness of finite computations.

1. **Spin convention.** Infection is primal spin 0, while dual membership
   is coded by 1. pi has spin-1 parameter p=1-q. The finite Python masks
   encode infection, so their stationary weights are q^N p^(n-N).
2. **Arbitrary initial law.** Dominated convergence requires convergence
   at every nonempty deterministic start, not pi-almost every start. The
   latter does not cover Dirac masses. Proposition 1 retains this quantifier.
3. **Last infection.** Healing requires another infection at a distinct
   neighbor. The birth-chain bound proves nonexplosion before invoking the
   impossible last-infection deletion; an infinite accumulation of flips
   is not silently excluded.
4. **Regularization.** Proposition 2 supplies an event of pi-probability
   zero supporting every finite-seed law at any finite time. Thus even
   nonuniform finite-time global absolute continuity is impossible for
   these starts. This does not obstruct weak local convergence.
5. **Absolutely continuous case.** Proposition 3 relies on the published
   stationary classification. Harmonic truncations are justified by zero
   conditional variance, not by an unjustified assertion that every
   nonlinear transform commutes with a Markov kernel. Jensen equality
   and invariance give that zero variance. The final L1 truncation does
   not presume an L2 density or a logarithmic Sobolev inequality.
6. **Sign of generator.** The generator in the source formulas is negative
   semidefinite. A=-L is the nonnegative operator in spectral calculus.
7. **Stationary versus convergent.** Weak limits of time-averaged laws
   are stationary by an explicit telescoping identity plus Feller continuity.
   Weak limits of arbitrary time slices are not thereby stationary.
   No fixed-time conclusion is drawn from Proposition 4.
8. **Escape to infinity.** Nonextinction of the infection set does not
   preclude a local all-healthy weak limit. Its supporting event is not
   closed in the product topology. The stationary mixture coefficient
   remains an actual unknown for singular starts.
9. **Finite boundaries.** The one-site computation explicitly falsifies
   replacing the true exterior by a permanently infected boundary.
   Finite-volume equilibrium and mixing cannot be used after swapping
   large-volume and long-time limits without uniform estimates.
10. **Duality integrability.** The duality function can grow exponentially
    in dual set size when q<1/2. Boundedness cannot be presumed. The
    historical hull grows only at two boundary vertices, yielding a
    Poisson exponential-moment bound and uniform square-integrability.
    This permits the finite-cycle to infinite-line limit for fixed t.
11. **Duality scope.** One-site dual occupations determine the primal
    single-infection cylinder basis, not all primal deterministic starts.
    No monotone domination by a single infection is available.
12. **Finite verification.** Exact rational tests cover all configurations
    at the stated finite sizes; they cannot detect long-time/infinite-volume
    failures. Lean certifies a combinatorial obstruction and preservation
    fact only. Its compiler result is tracked in CHECKS.md.
13. **Literature certainty.** Two services repeatedly rate-limit requests.
    Absence of a found resolution is not proof of worldwide open status.
    Later different-model or perturbative papers are not solutions in print.

No step in the current proof attempt bridges the singular-start dual
occupation limit or the all-healthy Cesaro mixture coefficient. This is
why the final verdict must remain PARTIAL.
