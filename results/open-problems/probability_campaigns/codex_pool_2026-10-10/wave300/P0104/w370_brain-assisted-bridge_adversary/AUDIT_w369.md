# Independent adversarial audit of w369's P0104 bridge

2026-10-10. Verdict: KEEP L0-L4 as conditional abstract probability results,
with the application gaps explicitly retained. P0104 has not been solved.
This audits the proof itself, not an earlier review.

The order was primary sources and statement-only challenge, then saved
INDEPENDENT_OBSTRUCTION.md and INDEPENDENT_BRIDGE.md, then w369/ATTEMPT.md.
My log-versus-power observation was already in the September ledger and
is not new. My 3/8 countermodel was derived before seeing w369's 5/12 one.

L0: The closed-interval hypothesis must hold for every interval of the
specified positive length, with a fixed deficit epsilon>0. Centering that
interval at E X proves the stated variance lower bound directly. A bound
for just one interval is insufficient. Keep the implication direction.

L1: The two tail events are disjoint because a<b. The completion-of-square
argument and three-atom equality case are correct, including p+q=1.
The weak-limit consequence uses separated continuity points and fixed
positive tail probabilities, not convergence of moments.

L2: The independent copy is legitimate on a product probability space.
The union bound is used only for the two copies, never for dependent FPP
blocks. Cauchy-Schwarz gives the displayed inequality. With p<=1/(32K)
the coefficient is <=1, so every admissible interval has length>=sigma.
Taking an infimum requires no attaining interval. Chebyshev gives the
upper bound. The constants are conservative but valid.

L3: Tightness gives the fixed-mass interval at scale a_n. L2 bounds
sigma_n/a_n. The mean-offset estimate is valid on both sides of that
interval; it supplies the crucial bound for arbitrary deterministic m_n.
The fourth-moment bound then gives uniform integrability of first and
second normalized moments. Bounded continuous truncations justify the
limit, and Fatou supplies the limiting fourth moment. Nondegeneracy makes
Var(Z)>0. My separate symmetrization proof confirms the conclusion.

L4: Checked the four atom probabilities, positive support for n>=3, mean,
variance formula, weak and total-variation limits, kurtosis divergence,
and all three ranges of the tail parameter including atom endpoints.
The exponent is 5/12. The tail constants exp(1/3) and 1/6 are valid.
It refutes an abstract implication; it is not a lattice FPP construction.

No universal lattice kurtosis bound follows from the DHS concentration
estimate: integrating it yields a fourth-moment bound at n/log n, whose
normalization by Var(T_n)^2 is still uncontrolled. The independently
missing n^(1/3) weak scaling also remains. A rotationally invariant metric
theorem has different model hypotheses and supplies neither lattice input.

Referee: w371 must decide these claims independently. This is one named
adversary check; no cross-account identity or final admission is certified.
NEXT: w371 checks L0-L4 and the separate 3/8 countermodel, while the prover
isolates predictable quadratic variation for actual lattice passage times.
