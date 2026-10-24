# Exact mathematical-card comparison

Read-only source: math-brain-build/local/population/brain.sqlite3, targeted node IDs only. Full records are saved under evidence/. No evaluation items or answer material were accessed.

Gaussian integration by parts, logical ID `math:probability.gaussian:gaussian-integration-by-parts-and-steins-characterisation`: the multivariate statement requires a centered Gaussian vector, its covariance matrix, differentiability, and appropriate integrability. The finite bridge uses a centered finite Gaussian X, differentiable F_beta at fixed beta, and bounded gradients/Hessians. The representation X=C^(1/2)G handles singular covariance without any independent-coordinate premise for X. It supplies the finite response identity; it does not supply a network-size-uniform bound or evaluate the response.

Gaussian Poincare, logical ID `math:probability.gaussian:gaussian-poincare-inequality`: full statement requires standard Gaussian measure, local Lipschitz regularity, and f and grad f in L^2. Apply it to f(g)=min_p log sum_v a_pv exp(xi (C^(1/2)g)_v). This is a finite minimum of globally Lipschitz functions with common Lipschitz constant xi sqrt(v). Its absolute value is bounded by a deterministic constant plus xi max_v |(C^(1/2)g)_v|, hence f is in L^2; its almost-everywhere gradient is bounded, hence also in L^2. The card therefore proves Var(log D_xi)<=xi^2 v even at path ties. This only transfers mean/median exponents.

P0297 problem card, logical ID `math:probability.core:open-problem-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity`: its dated status is explicitly unverified and its source is the 2025 Rhodes-Vargas survey, Section 3, PDF page 4. It does not certify current openness.

P0297 attempt card, logical ID `math:probability.core:attempt-p0297-exact-hausdorff-dimension-of-liouville-quantum-gravity`: the full text says constant shifts give the necessary relation xi*d=gamma, but do not compute xi. My initial algebraic obstruction agrees with that record and is not a new solution. The missing bridge for this lane is evaluation of the signed LFPP response and control of smoothing error on a growing network.

Retrieval limitation: the targeted title/source query `(title contains Liouville quantum OR metadata contains 1905.11790)` returned the problem, attempt, and vocabulary entries only. This is a precisely scoped lookup miss, not a claim that the theorem is absent everywhere in the store. The primary metric KPZ theorem was read separately, with its independence premise intact.

NEXT: Carry the Gaussian-card dependencies into typed draft edges and have w527 check the diagonal-limit and dependent-set obstructions.
