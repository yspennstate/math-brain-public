# Counterexamples to the stochastic assertion in Whitt (1983)

Complete mathematical proofs and exact reproducible certificates, 2026-10-02. Historical priority and the present literature status of the conjecture are unverified. No external expert review has occurred. The full stochastic-order assertion of Conjecture 1.1 is refuted; weaker mean waiting-time statements are not resolved here.

Start with `whitt_nine_state_proof.md`: it gives a short counterexample with two simple service laws, a nine-state finite queue used only as a lower bound, and a literal integer stationary vector. Read `whitt_light_traffic_proof.md` next: it derives a general cubic light-traffic formula and a family of counterexamples for every nondegenerate finite hyperexponential starting law. Strictly positive two-exponential target laws also suffice.

For explicit strictly positive service times at arrival rate 11/10, run `whitt_two_phase_positive_exact.py`. It proves a delay-probability reversal greater than 1/400, using a rigorous killed-chain occupation bound and a dominating M/M/2 tail, not a finite-buffer approximation. Its proof method is developed in `whitt_positive_service_proof.md`; that note first treats a three-exponential target. The two-exponential target is in `whitt_light_traffic_proof.md` and the exact script. Both service means are one. An explicit positive waiting threshold also reverses the order.

## Reproduce

The proof verifiers require only the Python standard library. Keep their files in the same directory.

    python whitt_nine_state_exact.py
    python whitt_nine_state_independent.py
    python whitt_two_phase_positive_exact.py
    python whitt_positive_service_exact.py
    python whitt_finite_independent.py
    python whitt_qbd_exact.py
    python whitt_light_traffic.py

All decisive certificate assertions use Fraction or integer arithmetic. Decimal values only display exact bounds. The nine-state independent check uses a literal matrix and vector, without the generator constructor or the linear solver. The original zero-atom pair has both a rational QBD-root enclosure and an independent finite occupation certificate. Recorded JSON outputs and mathematical audits accompany the scripts.

`whitt_counterexample_proof.md` and `whitt_qbd_exact.py` preserve the first, more elaborate counterexample and its certificate. `whitt_independent_audit.md`, `whitt_positive_service_audit_heat.md`, and `whitt_light_traffic_independent_audit.md` record independent checks. The C++ searches and `whitt_qbd_probe.py` are exploratory numerical work, not proof certificates.

Primary source: Ward Whitt, *Comparison conjectures about the M/G/s queue*, Operations Research Letters 2 (1983), 203–209, DOI https://doi.org/10.1016/0167-6377(83)90026-3. Author-hosted PDF: https://www.columbia.edu/~ww2040/comparisonConjectures1983.pdf. Conjecture 1.1 is on p.203. Section 6 explicitly permits zero-service atoms and gives the exact exponential-plus-zero benchmark. Searches of the original title, conjecture, stochastic comparisons, and later papers have not located an earlier refutation, but this is not a proof of novelty or of continuous open status through 2026.
