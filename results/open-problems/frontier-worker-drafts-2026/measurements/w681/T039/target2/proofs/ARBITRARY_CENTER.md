# Slabwise arbitrary additive centers

Heilman Appendix A before (150) explicitly permits any additive center: it vanishes from the mean-zero quadratic form. For each rho slab we choose a quartic ell(x)=sum_{n=0}^4 c_n x^n, with exact binary64 coefficients fixed over the entire slab. A double-precision fit only proposes those coefficients. Its accuracy, optimality and discretization are not assumed.

The certificate records every c_n as a hexadecimal binary64 literal. All subsequent evaluations use directed interval Horner bounds, including the source analytic polynomial-center tail with these same coefficients. Thus a poor numerical fit can cause a failed certificate, but cannot establish a false upper bound. The underlying mean-zero weighted operator is unchanged.

The fit minimizes a numerical Frobenius residual against the source kernel in the five quartic directions D_j u^T+u D_j^T. Its normal matrix is 2||u||^2 D^T D+2(D^T u)(D^T u)^T. This formula is used only for witness selection and is not a step in the proof of the certified bound.
