# C0090: Finite weight means fix the annealed one-edge decay exponent

Label: proof; author checked only. Independent audit: PENDING w347.

Let iid positive weights W_x have finite mean mu, and conditionally independent edges have probability 1-exp(-lambda*W_x*W_y*|x-y|^(-b)), with b,lambda>0. Then the annealed one-edge probability is asymptotic to lambda*mu^2*|x-y|^(-b) as |x-y|->infinity. In particular for Pareto weights P(W>w)=w^(-rho), w>=1, rho>1, its coefficient is lambda*(rho/(rho-1))^2. A tail exponent b*rho cannot be inferred for this finite-mean regime from the weight-tail parameter.

Assumptions: Independent identically distributed positive weights with finite mean; The displayed conditional edge law; Fixed positive b and lambda

Set V=W_x*W_y and s=lambda*|x-y|^(-b). For V>=0, 0<=(1-exp(-s*V))/s<=V, and the expression tends pointwise to V as s decreases to zero. Independence and the finite weight mean give E V=mu^2<infinity. Dominated convergence yields the asymptotic. For a Pareto variable the density rho*w^(-rho-1) on w>=1 gives E W=rho/(rho-1). This is an edge-probability calculation; it does not compute the connectedness two-point function or a critical exponent.

Limits: The annealed one-edge probability is different from the annealed connectedness function. No mean-field boundary, critical dimension or continuity of theta is deduced.

Existing card: math:probability.percolation:open-problem-c0090-critical-behaviour-of-scale-free-percolation
Source snapshot: ~/math-brain-build/export/population/nodes.jsonl:7316
