# Retrieved theorem versus the proof need

The exact retrieved covariance card is claim_25c5933eb4eeace1fc2a65fb1aba685df634054eba10e9f383b0eeb7c1ba32f7, logical id math:harvest.arxiv.mathematics:arxiv-2405-06616-theorem-3-13-68d962. Its complete body is saved in BRAIN_CARDS.json by an exact-ID read-only query. Primary arXiv:2405.06616v2 Theorem 3.13 states the same result.

It needs a density proportional to exp(-V) and one fixed positive-definite matrix Gamma with Hess V(z)>=Gamma for every z. Its conclusion is a covariance bound Cov<=Gamma^-1. A log-concave isotropic prior supplies Hess V>=0 in the smooth case and Cov=I; it does not supply any positive Gamma. Isotropic Laplace tails have zero curvature, so uniform curvature cannot be inferred from isotropy. The Gaussian likelihood supplies Hess(V+|x-y|^2/(2t))>=I/t for the posterior. That is the valid use in ATTEMPT.md L1. It does not produce an unconditional KLS bound.

The related standard log-concave Lichnerowicz result, arXiv:2303.14938 equation (1.7), gives C_P<=1/kappa only for kappa-uniformly log-concave measures with kappa>0. Theorem 1.3 improves the bound to sqrt(||Cov||_op/kappa), still with that positive curvature assumption. In this packet kappa=1/t belongs to the posterior; neither bound licenses kappa=0 on the prior.

The returned Gaussian semigroup card claim_3a7f53cc4f4c10093c8e4e07c223f18d52212a9c7d6f98c1196f104f16111a3d has the standard Gaussian as its invariant law. Its Hermite diagonalization cannot be carried over to an arbitrary log-concave measure. The PDE Poincare card uses domain/boundary assumptions and sometimes C_P as a norm coefficient; its diameter bound is not the requested covariance bound. For the variance-one cube [-sqrt(3),sqrt(3)]^n, diam^2=12n, so that route retains dimension dependence.

Measured serving failure: existing recall JSON exposes titles and scores, without the full statement containing Gamma>0 and uniformity. The bounded proposed repair is an optional --with-statements recall projection that returns the selected card's complete body and its stored review status. Ranking and mathematical status remain the retrieval engine's responsibility. Validation uses only these four captured cards, not a blind bank or an entire-store export.

NEXT: Run the full-statement projection comparison on the captured Brascamp-Lieb card, then hand the scoped CLI diff to the reviewer.
