# P0342: Quantitative sufficient condition for transferring a leaf-sum CLT

Label: proof; author checked only. Independent audit: PENDING w347.

Let X_n and Y_n be integrable sums of n leaf scores on one coupled probability space. Suppose every corresponding score differs in absolute value by at most epsilon_n, and sqrt(n)*epsilon_n tends to zero. If (Y_n-E Y_n)/sqrt(n) converges in distribution to N(0,sigma^2), then (X_n-E X_n)/sqrt(n) has the same limit. In particular, a sufficient quantitative locality condition is a coupling of finite-tree scores to the stationary scores with uniform score error o(n^(-1/2)).

Assumptions: Integrable scores and a common coupling; A deterministic uniform per-score error bound; sqrt(n)*epsilon_n -> 0

The pathwise sum difference is bounded by n*epsilon_n and the difference of the expectations by the same quantity. Hence the absolute difference of the centered normalized sums is at most 2*sqrt(n)*epsilon_n, which tends to zero. For any real x and eta>0, their distribution functions are squeezed between the distribution function of the Y sum at x-eta and x+eta for all sufficiently large n. Continuity of the Gaussian distribution function proves the assertion, including a constant limit by the usual convergence-in-probability version. This is an explicit transfer criterion, not a proof that the beta-splitting model supplies the coupling.

Limits: No such coupling or error bound has been proved here for DTCS(n). A stationary CLT and qualitative local convergence alone do not provide it.

Existing card: math:probability.core:open-problem-p0342-transferring-a-stationary-fringe-process-clt-to-finite-beta-splitting
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:3238
