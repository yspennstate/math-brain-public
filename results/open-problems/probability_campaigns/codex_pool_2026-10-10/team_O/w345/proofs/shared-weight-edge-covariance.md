# C0090: Shared vertex weights strictly correlate annealed adjacent edges

Label: proof; author checked only. Independent audit: PENDING w347.

In the same scale-free edge model, take three distinct vertices 0,1,2, independent positive weights, and positive edge coefficients a,b. Let I_01 and I_02 be their edge indicators, conditionally independent given all weights. Then Cov(I_01,I_02)=Cov(g_a(W_0),g_b(W_0)), where g_a(w)=E[1-exp(-a*w*W_1)]. This covariance is positive when W_0 is nondegenerate. Thus an independent-edge model with the same edge marginals already disagrees on two-edge events.

Assumptions: Independent positive vertex weights; Conditional edge independence; Positive edge coefficients; Nondegenerate shared weight for strict positivity

Given W_0, integrating the independent endpoint weights leaves I_01 and I_02 independent Bernoulli variables with parameters g_a(W_0) and g_b(W_0), respectively. Conditional covariance is zero, so the covariance identity follows by conditioning. Each g is strictly increasing because the other weights are positive almost surely. For an independent copy W_0', covariance equals one half of E[(g_a(W_0)-g_a(W_0'))*(g_b(W_0)-g_b(W_0'))]. The integrand is nonnegative everywhere and strictly positive on {W_0!=W_0'}, which has positive probability for a nondegenerate distribution. All quantities are bounded and hence integrable, even for infinite-mean weights.

Limits: This invalidates direct substitution by independent edges at the level of joint laws. It does not rule out proving suitable stochastic comparisons or universality by a separate argument.

Existing card: math:probability.percolation:open-problem-c0090-critical-behaviour-of-scale-free-percolation
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:7316
