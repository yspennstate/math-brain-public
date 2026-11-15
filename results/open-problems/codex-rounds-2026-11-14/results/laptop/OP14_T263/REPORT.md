VERDICT: PARTIAL exact Gaussian-mixture risk reduction and sharp even-component threshold

PROOF.md proves an exact risk formula for the nonlinear four-ReLU family f(x)=u.x+|v.x| on a balanced two-Gaussian mixture. Its error is the average of two one-dimensional Gaussian tails. Constant-factor error estimates for this family are equivalent to bounded additive error in the square of the smaller effective margin, when both margins and the proposed scale are at least one.

The example f_b(x)=x_1+b|x_2| under means +/-r e_1 has risk Q(r/sqrt(1+b^2)). Its risk is within a constant factor of Bayes risk Q(r) as r grows if and only if rb stays bounded. Taking b=r^(-1/2) gives a vanishing even-component second moment but an unbounded risk ratio despite an exactly correct odd component.

These are function-level results. No GD trajectory, interpolation construction, or matching n,d rate for the trained network is established. T263 remains unresolved in this session. Novelty of these elementary identities is not asserted.

Independent checks passed. The main command is `python -B verify_reduction.py` with OMP_NUM_THREADS=1 and BelowNormal process priority. It ran in about 19 seconds, using the Python standard library and one thread. Direct integration of the actual ReLU score checked nine cases at two resolutions; maximum refined relative discrepancy was 6.661338147750939e-15. It also checked 28 Gaussian-tail inequalities and saved 15 threshold examples. No training was performed.

The data are in risk_identity_checks.csv, tail_inequality_checks.csv and contamination_threshold.csv. The complete output is in verification_output.txt; metadata are in verification_summary.json. At r=32, the vanishing-second-moment example has risk/Bayes-risk about 5,556,655.615. The proof does not rely on approximate numerical quadrature.

The first quadrature attempt failed at a genuine cusp in a correlated example. Splitting the integration domain at that known cusp fixed convergence without relaxing tolerance. AUDIT.md records independent tail-inequality proofs, another derivation of the example's exact error, and tests of the assumptions. A guarded shared-store recall failed with MemoryError under its enforced 768 MiB process-memory cap; no result is attributed to that recall. Its exact command and failure are recorded in LOG.md and recall_output.txt.

The bounded literature check found relevant progress, including Ichiro Hashimoto's arXiv:2505.16204v3, but no result establishing the full requested constant-factor error rate. Its Gaussian-tail sandwiches leave constants in the arguments. The references actually opened and the scope distinctions are recorded in LOG.md.

What remains uncertain: whether any standard initialization and training scheme produces this family or approximates it with sufficient accuracy; whether the elementary reduction has appeared elsewhere; and whether a suitable squared-margin estimate can be proved with the required sample dependence. No solution after the stated literature cutoff was found, but the short search is not exhaustive.

The next worker should connect a specified GD output to this family or another exactly analyzable decision rule, then prove squared-effective-margin precision O(1). A function approximation via disagreement additionally needs an error at the target tail scale; ordinary o(1) approximation is insufficient when the target risk is exponentially small. For example, sharpen the Gaussian-tail argument in a concrete regime of Hashimoto's theorem rather than replacing Q(c q) by Theta(Q(q)). A high-probability result also needs a failure probability small enough before claiming an expectation rate.
