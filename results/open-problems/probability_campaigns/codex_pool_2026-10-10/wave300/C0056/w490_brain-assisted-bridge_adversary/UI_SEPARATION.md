# The higher-moment criterion is sufficient, not necessary

Derived after reading w489's conditional L3--L5, 2026-10-10. Independent referee w491 pending. This supplements INDEPENDENT.md without changing its sealed bytes.

Define g(E)=1/[E(log(1/E))^2] for 0<E<exp(-1), and g(E)=0 otherwise. Substitution u=log(1/E) gives integral g = integral_1^infinity u^(-2)du=1. Thus g(E)dE is a probability measure. The bounded self-adjoint multiplication operator Hf(E)=Ef(E) on L2(g(E)dE), with unit vector 1, has precisely this absolutely continuous spectral measure.

For every p>1, integral g(E)^p dE = integral_1^infinity exp((p-1)u)u^(-2p)du = infinity. The exponential factor dominates the polynomial denominator. Consequently, for an interval J whose interior contains [0,exp(-1)], Fatou and almost-everywhere Poisson convergence imply liminf_{eta->0} integral_J (P_eta*g)^p = infinity.

Nevertheless the Poisson convolutions converge to g in L1(R), and are locally uniformly integrable. This gives an explicit absolutely continuous spectral measure that satisfies the joint-uniform-integrability bridge but no uniform p>1 Poisson moment estimate. Thus inability to prove w489's stronger moment hypothesis would not refute absolute continuity or C0056. The example is a scalar spectral construction, not an Anderson-model result.
