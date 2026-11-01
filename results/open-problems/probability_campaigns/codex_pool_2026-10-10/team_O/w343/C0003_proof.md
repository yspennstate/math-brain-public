# C0003: identical moment thresholds with different Laplace corrections (proof, pending w347)

For a in [0,1], define a nonnegative random variable W_a by survival probability 1/e for 0<=t<e and 1/[t(log t)^a] for t>=e. There is an atom of mass 1-1/e at zero; the positive part is continuous, so this is a valid decreasing survival function.

For every a in [0,1] and s>0, E W_a^s = s integral_0^infinity t^(s-1) P(W_a>t) dt is finite exactly when s<1. At s=1 the integral integral_e^infinity dt/[t(log t)^a] diverges; for s>1 it also diverges.

For lambda tending to zero, let L=log(1/lambda). The survival-function identity gives

1-E exp(-lambda W_a)=lambda integral_0^infinity exp(-lambda t) P(W_a>t) dt.

Replacing the exponential by one over [e,1/lambda] costs at most O(lambda): inside the integral, 1-exp(-lambda t)<=lambda t and (log t)^(-a)<=1. The part above 1/lambda costs O(lambda), by substituting u=lambda t and bounding integral_1^infinity exp(-u)/u du. The part below e is also O(lambda). Hence for a<1 the asymptotic is lambda L^(1-a)/(1-a), and for a=1 it is lambda log L.

In particular W_0 and W_1 have the identical moment threshold s<1, but only W_0 has the lambda log(1/lambda) correction with a positive finite coefficient. W_1's ratio to that scale tends to zero. This disproves a moment-threshold-only route in C0003-A001. These scalar laws have not been shown to satisfy the DGFF Gibbs-Markov or conformal axioms, so they do not refute Conjecture 16.3.
