# P0321 statement recovery, 2026-10-10

Primary source: Mathieu Lewin, Coulomb and Riesz gases: The known and the unknown, arXiv:2202.09240v2 (30 April 2022), section VI.2, https://arxiv.org/html/2202.09240v2#S6.SS2 . The recovered passage describes an intermediate hexatic regime by fast positional and slow sixfold orientational correlations. It highlights numerical evidence for the classical two-dimensional jellium at s=0 and s=1. It is qualitative: it specifies neither an observable nor rigorous decay constants or a universally quantified exponent range. The generated ranking title is not an exact numbered conjecture.

Source model: dimension d=2; density rho>0; inverse temperature beta>0; V_0(x)=-log|x| and V_s(x)=|x|^{-s} for s>0; dimensionless coupling Gamma=beta*rho^(s/2). For 0<=s<2 the uniform neutralizing background and a renormalized thermodynamic limit are essential. A finite-volume neutral canonical energy is

H_Omega(X)=sum_{i<j}V_s(x_i-x_j)-rho*sum_i integral_Omega V_s(x_i-y)dy+(rho^2/2)*integral_{Omega^2}V_s(x-y)dxdy,

with N=rho*|Omega| an integer and Gibbs density proportional to exp(-beta*H_Omega). Infinite-volume characterization and the necessary limit cannot simply be presumed for all s and beta.

Working mathematical target (an explicit formalization, not a quotation): fix a chosen s (the long-range cases s=0 and s=1 are the priorities) and rho. Construct a nonempty open interval of Gamma supporting a thermodynamic Gibbs point process whose suitably specified positional density-wave correlation has short-range decay, while its sixfold bond-orientational correlation has algebraic decay tending to zero. These must be infinite-volume bounds, not finite-size fits. The source does not require both boundary transitions to be continuous, and no universal exponent is assumed.

One possible bounded bond observable at particle i is psi_6(i)=|N_i|^{-1}*sum_{j in N_i}exp(6i*arg(x_j-x_i)), where N_i is the Delaunay-neighbor set under a specified nondegeneracy convention. A Palm-pair or spatially localized definition and the density-wave observable must be fixed before this becomes a complete theorem statement. In particular, short-range positional order must not be silently replaced by exponential decay of every truncated density covariance in a long-range gas.

The auxiliary elastic observables used below are C_G(x)=E exp(i*G dot (u(x)-u(0))) and C_6(x)=E exp(6i*(theta(x)-theta(0))), theta=curl(u)/2. They are mathematically explicit but are not yet identified with those Riesz-gas observables.

Current openness: UNKNOWN. A bounded primary-literature check is not a proof of the absence of a solution. The historical 2026-09-07 unsolved status and recent simulations certify neither current openness nor a rigorous phase-existence theorem.
