# P0321 statement and a declared benchmark

The exact recovered intake asks: “Prove or refute the intermediate hexatic phase predicted in two-dimensional Riesz-gas phase diagrams, distinguished by orientational order and absence of crystalline positional order.” Its citation is Lewin 2022, Section VI.B, printed pages 66-67, https://arxiv.org/abs/2202.09240v2. The dated ranking assigns tier 5 and unsolved; present openness is UNKNOWN.

The primary description separates a hexatic phase with fast positional and slow sixfold orientational decay from a solid with slow positional decay and long-range orientational order. It discusses short-range exponents s>2 and numerical long-range examples s=0,1. It does not give exact decay quantifiers, a universal exponent range, or a rigorous hexatic Gibbs construction. A theorem with those extra choices must declare them rather than attribute them to the survey.

For a concrete possible future target, fix s=1 and density rho=1. In a square D_N of area N, with N particles and uniform background, define

    H_N(x_1,...,x_N) = sum_{i<j}|x_i-x_j|^{-1}
      - sum_i integral_{D_N}|x_i-y|^{-1}dy
      + (1/2) integral_{D_N x D_N}|x-y|^{-1}dx dy.

The canonical finite-volume probability is proportional to exp(-beta H_N) on D_N^N. An infinite-volume law in the benchmark must be a stationary unit-intensity bulk limit of these neutral canonical laws and satisfy a specified renormalized Gibbs specification; neither existence nor that specification is supplied by our Gaussian model.

Here is one explicit, deliberately stronger benchmark, not a quotation or a claimed equivalent of every physical formulation. Ask for a nonempty open interval J of beta>0 such that for each beta in J there exists such a rotation-invariant law P_beta with a locally finite, almost-surely nondegenerate Delaunay triangulation and finite Delaunay degrees. Define the microscopic bond observable at a particle x by

    psi_6(x) = (1/degree(x)) sum_{y: Delaunay neighbor of x} exp(6 i arg(y-x)).

Assume a two-point factorial density g_beta(x)=rho_beta^(2)(0,x) exists and is positive almost everywhere at sufficiently large separation, so the corresponding two-point Palm observable

    C_6,beta(r) = E_beta^{0,r e_1}[psi_6(0) conjugate(psi_6(r e_1))]

is defined almost everywhere. Require positive constants c_beta,C_beta,r_beta and an exponent 0<eta_beta<2 such that

    c_beta r^{-eta_beta} <= Re C_6,beta(r) <= C_beta r^{-eta_beta}

for almost every r>=r_beta, and impose the fast positional criterion

    integral_{|x|>=1}|g_beta(x)-1| dx < infinity.

Absolute integrability is a chosen positional benchmark, and the exponent range above is a chosen slow-decay benchmark; the survey does not assert those precise inequalities. A Gibbs phase claim would additionally need a declared extremality criterion. Those formalization choices remain for the target's reviewers, rather than being silently substituted for the historical problem.

Our auxiliary results do not furnish P_beta, g_beta, Delaunay observables, an interval J, or a microscopic-to-effective correlation transfer. Their scope is the failure of a compatible positive-shear Gaussian field to provide the asserted phase, and the failure of an exact additive Gaussian density to be a nonnegative particle smoothing.
