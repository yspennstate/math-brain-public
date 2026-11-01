# C0073: added conductance can slow a constant-speed walk

Label: proof of a periodic-network example and a normalization check, pending w347. It neither proves nor disproves the high-dimensional percolation exponent or monotonicity conjecture.

Take the integer spine Z with conductance one between neighbours. At every spine vertex n attach one leaf with conductance a>0. Project the walker to the integer coordinate, putting the leaf at the same coordinate as its parent. Define D=lim_{t->infinity} Var(X_t)/t, with the initial internal type in its stationary law.

For the continuous-time constant-speed walk (total jump rate one), the transitions from a spine vertex are left and right at rate 1/(2+a) each and to its leaf at rate a/(2+a); from a leaf the return rate is one. The two-type stationary spine probability is (2+a)/(2+2a), by balance. The projected coordinate is a martingale and its quadratic-variation rate is 2/(2+a) at a spine vertex and zero at a leaf. Thus

    D_CS = [(2+a)/(2+2a)] * [2/(2+a)] = 1/(1+a).

In stationary type, the variance identity holds exactly for every t. Ergodicity of the two-state type chain gives the same limiting growth from any initial type, and bounded martingale jumps yield the invariance-principle variance by the martingale central-limit argument.

For the variable-speed walk with each edge jump rate equal to its conductance, the spine-to-leaf and leaf-to-spine rates are both a. The stationary spine fraction is 1/2 and the projected quadratic-variation rate there is two, hence D_VS=1 for every a>0.

The electrical conductivity per spatial cell is kappa=1: all macroscopic current uses the spine and no current flows into a dangling leaf. The constant-speed speed-measure mass per cell is m_CS=2+2a, while the variable-speed counting mass is two. Therefore D_CS=2*kappa/m_CS and D_VS=2*kappa/2. Increasing a leaves kappa unchanged and strictly decreases D_CS. Rayleigh monotonicity of conductivity cannot, without a separate speed-measure argument, imply monotonicity of a normalized walk diffusion coefficient.

The prior C0073 attempt explicitly mentions "times the degree normalisation" but also abbreviates the product as theta(p)*sigma^2(p). Which mass is correct depends on whether the cluster walk is constant speed or variable speed. The periodic example makes that dependency concrete. It is not an iid percolation environment and gives no counterexample to the source's specific conjecture.

Checks: balance of the two-type invariant law; zero projected drift; quadratic variation under both clocks; conductivity unchanged by a dangling edge; the a>0 condition when using the two-type variable-speed invariant law.
