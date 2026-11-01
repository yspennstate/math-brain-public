# C0006: a simple Laplace pole does not give the desired cluster-count limit

2026-10-10. Label: proof of a refuted generic route, awaiting w346 KEEP. This is not a counterexample to the DGFF cluster law.

The earlier cluster attempt records the Tonelli identity G(beta)=beta integral_0^infinity exp(-beta h) E[F_h] dh for nonnegative cluster heights, when beta>alpha and the quantities are finite. If exp(-alpha h) E[F_h] -> c, an Abelian argument yields (beta-alpha)G(beta)/beta -> c as beta decreases to alpha. The converse does not follow from monotonicity of the count alone.

An explicit counting-function control uses alpha=1. Let H(h)=exp(h)(1+(1/4)sin h) for h>=0, and F(h)=floor(H(h)). The derivative H'(h)=exp(h)(1+(1/4)sin h+(1/4)cos h) is strictly positive, because its bracket is at least 1-sqrt(2)/4. F is an integer-valued, nondecreasing, right-continuous count with F(0)=1 and finite values at every finite h. It is realized by countably many deterministic nonnegative heights: put one at zero and assign the n-th height as the unique solution H(h)=n for n>=2.

For the unrounded H,

    integral_0^infinity exp(-beta h) H(h) dh
      =1/(beta-1)+(1/4)/((beta-1)^2+1).

Rounding changes this integral by at most 1/beta. Therefore its normalized Abelian residue tends to 1. In contrast exp(-h)F(h) approaches 5/4 along h=pi/2+2 pi k and 3/4 along h=3 pi/2+2 pi k. It has no limit.

The toy height array has no Gaussian-field or DGFF-cluster structure. Its role is to show that even an integer monotone counting function and the correct real-axis pole residue need an extra Tauberian hypothesis to yield the pointwise exponential-growth limit. A claimed reduction using only those facts is incomplete; complex-boundary control or an appropriate renewal/nonoscillation theorem must be supplied.
