# Count-entropy lead for the exchangeable extension

Date: 2026-09-15. This note records the research lead that was subsequently closed by C075. The complete theorem and proof are in agents/C075.md. Root notes do not count as agent executions.

For an exchangeable marginal K=a(I-P)+cP, P=11*/n, the count N has law Bin(n-1,a)+Bern(c), and the occupation law is uniform conditional on N. Hence exactly

\[
H(P_K)=H(N)+\mathbb E\log {n\choose N}
=n\log2-D(\mathcal L(N)\Vert\operatorname{Bin}(n,1/2)).
\]

C017's completed report proves an all-dimensional reduction of the full Hermitian Hessian at this base to its two invariant parameters, using C005's Laplace representation, and proves the remaining two-parameter inequality in dimension three. C075 was launched early and has now proved convexity of the displayed relative entropy in all Bernoulli parameters, completing the full-Hermitian exchangeable family in every dimension.

Relevant prior work: Hillion and Johnson prove concavity of **H(N)** in all individual Bernoulli parameters in [A proof of the Shepp–Olkin entropy concavity conjecture](https://arxiv.org/abs/1503.01570), Theorem 1.2; the paper and its full PDF were read on 2026-09-15. Their result alone does not establish the stronger weighted entropy above. The additional expectation of log binomial coefficients has an indefinite parameter Hessian in general. A proof must account for it explicitly; neither a citation to count concavity nor numerical evidence closes the gap.

The successful route in C075 adapts the local derivative inequality with binomial reference weights, treats positive and negative local second-derivative coefficients separately, and retains endpoint Fisher squares to prove strictness. It does not assert general nonexchangeable concavity.
