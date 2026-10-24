# T336 Transformers as amortized Bayesian inference: approximation and generalization

Lead: unassigned. Dossier written 2026-10-16 by claude-99aebc7f from the row and the arXiv records below (abstracts read 16 Oct
08:2x, the 16 Oct 06:21 audit (status PARTLY, KL diagnostic) and codex-w687's note that population cross-entropy is not a uniform posterior KL).

## STATEMENT
Repaired statement (the audit: uniform-over-datasets KL is far stronger than the source's prior-averaged objective, noiseless
posteriors have atoms with infinite KL against densities, and the prior, noise floor, query law, KL direction, output family,
architecture and training must be named): fix a Gaussian-process prior with a bounded kernel on a compact input domain, a positive
observation-noise floor sigma^2 > 0, labels bounded by B on the context, and forward KL KL(posterior predictive || model) at a query
in the domain. Bound the size (depth, width, heads) of a transformer whose output (a Gaussian, mean and variance) is within eps in
that KL uniformly over contexts of length <= n, and give an ERM generalization bound for the prior-averaged objective. SGD
convergence is a separate task.

## FRONTIER
- Muller, Hollmann, Arango, Grabocka, Hutter arXiv:2112.10510: PFNs.
- Nagler arXiv:2305.11097: frequentist account; variance vanishes with sample sensitivity, bias needs localization at the test point,
  which current PFN transformers do not ensure.
- Kobialka, Hulskamp, Nagler, Rugamer arXiv:2610.14989: PFN priors are non-separable; the pretraining target conditions on the query
  features too.
- Bai, Chen, Wang, Xiong, Mei arXiv:2306.04637: transformers implement ridge regression and other algorithms in context with explicit
  size bounds, via in-context gradient descent.

## ARCHITECTURE
For a kernel with a finite feature map phi of dimension p (or its rank-p truncation), the GP posterior predictive at x is Gaussian
with mean m = phi(x)' (Phi'Phi + sigma^2 I/tau^2)^(-1) Phi'y and variance v = sigma^2 + sigma^2 phi(x)'(Phi'Phi + sigma^2 I/tau^2)^(-1)
phi(x). Both are ridge-type quantities, so 2306.04637's in-context GD construction gives them with depth O(kappa log(1/delta)) where
kappa is the condition number of the regularized Gram, at most 1 + n R^2 tau^2/sigma^2 with R = sup |phi|. For Gaussians,
KL = log(v'/v)/2 + (v + (m - m')^2)/(2v') - 1/2, so errors delta_m, delta_v give KL <= delta_m^2/(2 sigma^2) + C delta_v^2/sigma^4
once v' >= sigma^2/2; with |y| <= B the mean error scales with B. So a uniform bound holds on {|y| <= B} with depth
O((1 + n R^2 tau^2/sigma^2) log(B n R/(sigma eps))) (sketch, constants not written).

## FAILURE POINT
Infinite-rank kernels (RBF) need a rank truncation whose error depends on the input domain and n; gradient-descent depth grows
linearly in n through kappa unless an accelerated or Newton-type in-context solver is built.

## SHAPE
Days for the finite-rank bound above written out; weeks for an accelerated in-context solver with depth O(sqrt(kappa) log(1/eps)) and
the RBF truncation.

## OBSTRUCTION
Conditioning. Moves: Chebyshev-accelerated iterations in attention layers; the truncation error of Mercer expansions on compact
domains.

## TARGETS
1. Finite-rank GP, sigma^2 > 0, |y| <= B: explicit transformer size for eps forward KL uniformly over contexts of length <= n.

