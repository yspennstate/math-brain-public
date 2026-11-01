# Referee audit of the additional attempt (2026-10-11)

The new route concerns global growth from singular starts, not equilibrium
of local observables. Each issue below was checked in the proof.

1. **Correct gap input.** The empty configuration is a separate absorbing
   class. Every gap used is for the nonempty class with Bernoulli law
   conditioned on nonemptiness, at fixed q. Infinite-volume equilibrium
   gap positivity alone is not substituted for this finite-cycle statement.
   Source page 27 explicitly asserts the latter. Independently checked
   book Theorem 4.8 applies to the nonempty interval component; joining
   the endpoints only increases the constraint and hence the form under
   the same conditioned law. This verifies the input uniformly in volume.
2. **Same measure in form comparison.** The FA-1f, BABP and dual finite
   generators are compared under exactly the same conditioned product law.
   When the center is occupied, conditioning nonempty is redundant and
   the two neighbors have independent Bernoulli(q) law. Unconditioned
   heat-bath projections are used only inside such centered terms.
3. **Direction and factor.** The inequalities are D_F<=D_B<=2D_Q,
   so gap(Q)>=gap(F)/2. Reversing this implication would be invalid.
   Orthogonal interaction components contribute once to D_Q and twice to
   D_B; their nonnegative squared norms prove the factor two.
4. **Infinite normalizing constant.** m is sigma-finite, not a probability
   law, and it is not pi. Its finite-cycle normalizing constant tends to
   infinity. The constant-mode term 1/Z_n is retained until AFTER the
   finite-volume limit. Dropping it at fixed volume is false.
5. **Limit order.** Only fixed-t finite-cycle coupling is needed. The
   exponential estimate is uniform in cycle size. Passing a finite sum
   to the limit, then exhausting the countable state space, is legitimate;
   simultaneous large-time and large-volume coupling is not claimed.
6. **Conservativity.** Finite-seed primal and dual chains are nonexplosive
   by the historical-hull construction. This is used in proving sigma-
   finite invariance from detailed balance, not assumed just from symmetry.
7. **Poisson comparison.** Historical, not current, hull boundaries are
   used. At most two boundary locations can extend that hull, with rate
   at most two in total. Unoccupied historic endpoints cause no difficulty.
   Each extension adds at most two sites. The common loose bound works
   for both processes, including a singleton dual adding both neighbors.
8. **Binomial entropy.** Low-cardinality states in a linear cone have
   finite m-mass. The exponential generating-function bound explicitly
   includes every k up to floor(alpha t), and theta^k>=theta^(alpha t)
   is used with the correct direction. No small-q approximation is used.
9. **All real times.** Integer-time Borel-Cantelli alone does not prove a
   continuous-time lower bound. An explicit compensator bound for
   downcrossings on unit intervals supplies the missing argument; the
   downward jump bound two and rate bound 2N are both verified.
10. **Fixed-site test fails the norm hypothesis.** Both occupation events
    have infinite m-mass; their centered indicator has infinite l2(m)
    norm. This is a concrete obstruction to reading local convergence
    out of global heat-kernel decay.
11. **Counterexample scope.** Translated deterministic growing intervals
    refute the logical implication 'growth plus finite speed implies local
    equilibrium'. They are not asserted to occur under the FA dynamics.
12. **Numerics.** Twenty-five small finite matrices check detailed balance,
    gap comparison and positive semidefinite form differences. They do
    not establish an infimum over all volumes. The 2580 weighted-binomial
    cases are exact rational tests of the algebraic bound, not a substitute
    for its proof. Lean compilation status is kept separately in CHECKS.md.
13. **Isospectrality.** Full finite generators include the empty absorbing
    class; simply discarding the empty row of the duality matrix need not
    give an invertible intertwiner. The Schur complement D'-1 1^T is
    explicitly proved invertible and intertwines the NONEMPTY generators.
14. **Walsh sums.** The infinite-volume Walsh expansion is justified as
    an absolutely convergent Bochner sum at each finite time, using the
    historical-hull exponential moment. Orthogonality then proves its
    norm identity. Point evaluation at a singular configuration remains
    unbounded; the explicit cylinder functions show this even for uniformly
    bounded local mean-zero functions.

The unresolved target remains the dual fixed-site occupation limit,
and then the all-deterministic-start extension. No counterexample to
D0026 and no complete proof are claimed.

Final reread corrected the common normalization factor in Fresh Lemma 2:
under the nonempty conditioned n-cycle law, the occupied-center weight
is q/(1-p^n), not q. The same positive factor multiplies both compared
energies, so the inequalities and every subsequent result are unchanged.

The optional HeatKernelChecks.lean submission never yielded an observed
compiler result. On resumption no matching process or wrapper completion
record was found. No new Lean-verified assertion is made. Its algebra is
proved directly: (a+b+2c)-(a+b+c)=c>=0, and
2(a+b+c)-(a+b+2c)=a+b>=0. Also
-g*t+(g*t/2)/2=-g*t+g*t/4=-(3*g/4)*t over the reals.
These finite algebra identities do not certify the stochastic theorem.

The unselected tag approach received a finite sanity check as well:
its forced-survival tag has a positive-rate one-way marked transition
on a three-site cycle. It cannot simply be assigned a reversible Palm
law. A nonreversible recurrence proof might still be possible; none is
asserted here.
