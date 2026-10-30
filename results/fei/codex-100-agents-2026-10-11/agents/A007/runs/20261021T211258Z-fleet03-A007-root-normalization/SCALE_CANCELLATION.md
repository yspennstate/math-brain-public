# Intermediate scales cancel only with their inherited cost

All logarithms are base two. This is a finite algebraic identity for the inherited selected-lift mass, not an assertion that its cost is universally bounded. Keep one gate table, one set of orders and the same actual old forest records. For each nonempty data Fourier set T let w_rho(T)>0 be its unnormalized original record weight and k_rho its number of used gates. A common original label scaling t>0 changes this weight to t^k_rho w_rho. This hypothesis is essential: it concerns a label drawn once for each used gate, with no other scale-dependent transition factor. It is precisely the homogeneity used in the inherited L0=E beta^k and G=beta^k G0 formulas.

Write S_t(T)=sum_rho t^k w_rho, eta_t(rho|T)=t^k w_rho/S_t(T), and D_t=prod_l(1+t lambda_l pi_l)-1. Assume S_t(T)>0 whenever P_g(T)>0. D_t>0 follows from a nonempty table with a positive original lambda*pi. All sums are finite. Let p=2^-r, r>=1. For each selected control subset U, including U=empty, let H_rho,U>0 be the scale-independent distributed multiplier, with H_rho,empty=1. It includes the joint occupation/root/factorial numerator, not a product of separately averaged credits. Then

    J_t,beta,U(T)=E_eta_t [beta^k H_rho,U],
    N_alpha,U(T)=sum_rho alpha^k w_rho H_rho,U,
    S_t(T) J_t,beta,U(T)=N_(t beta),U(T).                  (1)

The identity follows term by term. It does not assume that eta_t is unchanged as t varies. That posterior generally DOES change; (1) retains this dependence exactly. Neither a Fourier-set-dependent scale nor a newly chosen witness is used.

Define the exact mass portion of the inherited old residual by

    R_t=sum_(T!=empty) P_g(T) log[D_t/S_t(T)].

Other external reference, entropy and previously paid rank envelopes are not silently identified with R_t. They must be retained separately in an application. The source signed distributed correction, expressed without conflating the scale t with the lift beta, is

    Psi_t,beta=p v log[D'_(p t beta)/(p D_t)]
       -p^2 sum_T P_g(T) sum_(U subset [r]) log J_t,beta,U(T),

where D'_(p alpha)=prod_l(1+p alpha lambda_l pi_l)-1 and v=sum_T P_g(T). The source originally writes empty and nonempty U separately; there are exactly 2^r=1/p subsets in their union. Therefore substitution of (1) gives the exact cancellation

    p R_t+Psi_t,beta
      =p v log[D'_(p alpha)/p]
         -p^2 sum_T P_g(T) sum_U log N_alpha,U(T),
    alpha=t beta.                                        (2)

Indeed the old-normalizer terms p v log D_t cancel. The coefficient of sum P_g log S_t is -p+p^2 2^r=0. These are finite logarithms of strictly positive masses, so no interchange of limits and sums or cancellation of a zero denominator occurs. Individual normalizer signs are never dropped.

Thus (2) depends on the FINAL common scale alpha only. It is invariant under every admissible factorization alpha=t beta, provided the original and final references are feasible and the same scale-independent records/multipliers are used. Feasibility is a separate hypothesis: t must obey all old packing rows, beta must meet the source lift restrictions, and p is spectral activation mass, not permission to evade the physical common-control constraint alpha sum lambda<=1.

For the exact K_m,m primes R_ij={x_i,y_j}, use baseline lambda_ij=1/m. Every t in [1/m,1] gives a feasible old table, beta=1/(mt)<=1, and final alpha=1/m. The two endpoints are the uniform saturated old reference (t=1,beta=1/m) and the normalized old reference (t=1/m,beta=1). Equation (2) proves that changing between these endpoints CANNOT reduce the combined selected-mass bill. A smaller Psi at beta=1 is exactly offset by the inherited mass cost. This consumes A015's obstruction without claiming that Psi alone is invariant, that every possible lambda is equivalent, or that a new cover/reference cannot work.

The first unpaid line is a dimension-independent bound on the right side of (2), together with the full external terms and the control-only T=empty sector, after choosing one final representation/reference. Regrouping primes, changing relative weights or enlarging the selected lift family changes that problem; merely refactoring the same final scale does not. This is a normalization/conditioning cancellation identity, not a complete FEI theorem.
