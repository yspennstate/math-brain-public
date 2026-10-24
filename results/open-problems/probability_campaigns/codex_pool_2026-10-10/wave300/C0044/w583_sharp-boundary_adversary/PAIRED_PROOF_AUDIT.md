# Audit of w582's escape-floor route

Auditor w583, 2026-10-10. Read ~/brain_workers/w582/ATTEMPT.md after saving INDEPENDENT.md. This audits the mathematical proof itself, not a prior review. Served identities and different-model review gates are unverified.

L1 verdict: KEEP, exactly as stated. For each fixed environment and starting point, q(X_n)=P_x^omega(A_ell | F_n) is a bounded martingale. Directional divergence is unchanged by a finite time prefix; Levy upward convergence therefore gives q(X_n)->1_(A_ell). The assumed global infimum c>0 excludes zero. Irreducibility and ellipticity are unnecessary for that implication. The conclusion is a sufficient-condition lemma, not a proof that the condition follows from iid.

L2 verdict: KEEP under the stated ellipticity and, for its final paragraph, stationarity and ergodicity. Finite-path comparison q(x)>=p q(y) follows by forcing the path then applying the Markov property; its complementary-tail analogue is valid. Propagation of positivity and of strict inequality from one is valid. L1 applied to q and 1-q gives inf q=0 and sup q=1 in the mixed alternative. The shift relation q_(theta_z omega)(0)=q_omega(z) makes the positivity events shift invariant after restricting to the common full-measure elliptic set. Thus a mixed annealed probability forces mixed quenched probabilities almost everywhere. Deriving a positive global infimum in that setting is equivalent to excluding the mixed case, not an already proved consequence of ergodicity.

L3 and L4: no verdict in this audit; the assigned stress test focuses on L1/L2 and their global-infimum premise. The referee can check the two drift subclasses separately.

Independent obstruction: INDEPENDENT.md uses arbitrary kappa<1/(2d) and a reflection-symmetric interface, giving q(0)=1/2, whereas w582's CE1 has an asymmetric interface and q(0)=3/4. The calculations were independently derived. My version adds the full range of admissible ellipticity constants and the sharp maximal-ellipticity endpoint. Both explicitly violate stationary iid hypotheses and only refute a stronger auxiliary bridge.

Minimal missing premise for applying L1 to C0044: a proof, from the exact iid strictly elliptic law with positive annealed escape, that almost every fixed environment has inf_x q_omega(x)>0 (or another argument preventing the martingale from tending to zero). Neither pointwise positivity, the distance-dependent kappa^|x-y| comparison, nor environment ergodicity supplies this.

No parent-problem solved claim. Current openness UNKNOWN because a recent manuscript claims a solution and its actual proof has not been audited here.

NEXT: Referee checks the independent arbitrary-kappa construction; coordinator reviews the source-card correction about quenched versus annealed martingales.
