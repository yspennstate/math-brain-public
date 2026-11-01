Independent adversarial audit of w357/ATTEMPT.md, P0017, 2026-10-10.

Verdict: KEEP L1-L6 at their stated scopes. The full target is not proved by this packet. I saved INDEPENDENT_DERIVATION.md before reading any paired proof, and POSTERIOR_BRIDGE_CHECK.md from the statement-only packet before reading w357/ATTEMPT.md. I audited the original mathematical argument, not a peer's review of it.

L1: differentiating the normalized likelihood gives grad T=Cov(f,X)/t. The posterior curvature is 1/t, so its Poincare constant and covariance are at most t. These bounds concern the conditional law. KEEP.

L2: for c=1/(1+t), the prediction-error decomposition is E[(X-cY)(X-cY)^T]=E A_Y+E[(E[X|Y]-cY)(E[X|Y]-cY)^T]. Orthogonality of the conditional residual kills the mixed term. Computing the left covariance gives t/(1+t) I. No independence between A_Y and conditional energy is used. KEEP.

L3: for affine f with gradient a, D(Tf)=E|A_Y a|^2/t^2. The pointwise positive-semidefinite inequality A_Y^2<=t A_Y and L2 give at most |a|^2/(1+t). This checks affine functions only. KEEP.

L4: independent tensorization gives CP(nu_t)<=K+t when K=CP(mu)<infinity. Total variance then gives K<=t+q(K+t), hence K<=t(1+q)/(1-q). The proof explicitly keeps finiteness, the supremum over all functions and a justified regular approximation. Conversely, D(Tf)<=E Var(f|Y)/t<=Var_mu(f)/t<=K D_mu(f)/t. If K is universally at most C, choose t=2C to get q=1/2. Thus the strict uniform bridge is equivalent to the original dimension-free problem. KEEP as a conditional equivalence, with the strict bridge unproved.

L5: Gaussian translation gives grad Tf=(1+t)^(-1)E[grad f|Y]. Jensen supplies q=(1+t)^(-2), attained by affine f. This exact Gaussian constant is not claimed for general log-concave laws. KEEP.

L6: the Laplace posterior, relative to N(y-lambda*t,t), has weight 1 on x>=0 and exp(2lambda*x) on x<0. The weight is bounded by 1; shifted Gaussian moment convergence gives A_y->t as y->infinity. Integration by parts with the continuous kinked density is valid in the weak sense; it gives A_y/t+lambda Cov(X,sign X)=1. Since the second covariance is nonnegative, 0<=A_y/t<=1. A derivative supported in [L,L+1] changes the weighting measure to that far tail. Conditional expectation makes the weighted ratio an integral of E_G[A_(L+s+sqrt(t)G)/t] against a fixed positive density in s. Dominated convergence gives limit 1, so every fixed q<1 fails for this sufficient weighted inequality. It does not refute the actual Q_t bridge. KEEP.

My separate exponential example sharpens the constant calibration without duplicating the Laplace calculation: t=1 and f(x)=exp(0.49x) give a posterior Dirichlet ratio greater than 0.7, and a tail limit gives the necessary bound q(t)>=exp(-t/4). The finite lower-bound proof is in POSTERIOR_BRIDGE_CHECK.md and still awaits the referee. It is compatible with all six kept statements; L3 covers affine functions and L5 covers Gaussian laws.

Minimal missing premise: one numerical t>0 and q<1 controlling the full nonlinear posterior Dirichlet operator uniformly over dimensions, isotropic log-concave laws and the Sobolev class. Neither pointwise posterior covariance nor its unweighted MMSE bound is this premise.

NEXT: Referee-check the exponential finite tail bound and its Sobolev approximation; retain the strict averaged contraction gap explicitly in all draft nodes.
