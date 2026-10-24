# Referee audit of the second attempt

The full proof is in SECOND_ATTEMPT.md. Its scope is a stronger
nearest-neighbor extinction special case. It does not prove the general
unequal-death competitive-exclusion conjecture.

1. **Birth-rate normalization.** b is the total normalized birth rate;
   each of four incoming edges has rate b/4. The time normalization is
   s=delta_2 t. No per-edge threshold is presented as a total-rate threshold.
2. **Pair factor.** q is E[I_0 N]/4. The center and neighbor birth
   contributions are equal only after the symmetric neighbor sum and
   translation invariance. Their combined factor is b/8, not b/4 or b/16.
   Exact periodic generator enumeration checks the resulting equation.
3. **Fork multiplicity.** N(N-1) counts ordered pairs of distinct
   neighbors. Filling one vacant neighbor changes this by 2N. Each
   occupied fork has three distinct sites for the death term -3H.
   All 8192 radius-two patterns and 40960 site changes were checked.
4. **Shared event.** The center birth contribution T is added to H'
   and subtracted from U'. It cannot be treated as independent noise.
   Since u-h>=0, T<=bU has the required direction in the combined drift.
   The stronger local inequalities and finite drift were checked exactly.
5. **Nonnegative Lyapunov function.** A negative formal drift alone
   proves nothing if G can be negative. H<=12q, U<=12(r-q) give
   m r<=G<=r, with m>0 by explicit polynomial bounds. The new
   coefficients require their own positivity check; the earlier
   coefficient values are not reused.
6. **Algebraic root.** The refined numerator is 48-12b-17b^2.
   Rational arithmetic at 109/80 gives kappa=46640/57637989>0.
   Both root expressions and rate conventions are stated explicitly.
   No extinction rate is inferred from decimal approximations.
7. **Controlled graphical event.** The five-site star has twenty
   distinct incoming directed edges. Two are allowed only for a
   quarter-unit window. The forbidden edge time is 39/2, not 18 or 20.
   No-death site time is 7/2. Counts and all rational margin constants
   are checked in check_forcing_constants.py / forcing_checks.json.
   The event isolates the star from every outside initial state.
8. **Stationary contradiction.** In a stationary law, the bounded
   cylinder expectation G has derivative zero. The event forces a
   strictly negative contribution if r>0, including at the algebraic
   endpoint. The tiny extension uses an explicitly positive rational
   margin, not an unquantified continuity assertion.
9. **Convergence.** Merely ruling out a positive stationary density
   would not prove extinction of an arbitrary nonmonotone process.
   Here it is applied to the single-type process started all occupied:
   attractiveness makes its laws decreasing, and the Feller property
   makes the limiting upper law stationary. This supplies the needed
   limit before comparing back to the two-type process.
10. **Quantifiers and decay.** The dominating single-type process is
    translation invariant even if the competing process's initial law
    is not. Thus the final special case holds for every initial law.
    Exponential decay is proved below the refined algebraic root.
    Only local extinction, without a claimed rate, is proved in the
    endpoint extension. No assertion is made for the two-supercritical
    birth/death tradeoff region left open in ATTEMPT.md.

Lean is limited to the algebraic identities and rational linear
certificates; it does not formalize the graphical construction, the
stationary forcing event, or the infinite-volume limit. Success or
failure is recorded in the separate Lean logs, never inferred from
the presence of a .lean file.
