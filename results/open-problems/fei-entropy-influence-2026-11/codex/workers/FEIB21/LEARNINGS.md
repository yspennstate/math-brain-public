# Notes for the launching session to consider

These notes were not published to the mesh, checklist or brain. The fleet's folder-only rule takes precedence.

PROVED, pending external mathematical review: PROOFS.md (LIN) gives a coordinate erasure estimate for uniform monotone linear-hypergraph DNFs. For every fixed epsilon>0, maximum read D<=2^((1-epsilon)(w-1)) gives E_i/Inf_i ->2 at every live coordinate, uniformly in the number of terms. The proof combines a partition of the derivative into certificate-supported pieces, Harris conditioning, and a k-th mixed derivative estimate for the no-background indicator. It does not prove FEI by restriction induction. Mixed widths and D2^-w tending to zero with no exponential gap are open here.

PROVED: fixed-r mate windows can be unbounded at one root for every mate order, although its true erasure ratio tends to 2. Use the supplied two-level tree with D^2 2^(-(w-1)) tending to a positive constant. The proof yields a positive Poisson-tail coefficient times log D. All-variable interleavings and the minimum over coordinates remain open; do not retell this as a universal FWC refutation.

PROVED: the largest-influence coordinate need not have bounded erasure ratio. Start with a bent function, replace one input point by a fresh variable, then replace every other variable by a balanced low-influence majority tower. The root erasure stays of order the bent dimension while it becomes the unique maximum-influence coordinate. This refutes FLOW 7(i)'s proposed rule in general, not its threshold-specific analogue.

PROVED formula / CHECKED numerical values: keeping a fixed bottom neighborhood in a balanced PM tower has a diverging block-witness ratio. Growing the bottom depth logarithmically in total depth controls it. Its optimized one-element filtration nevertheless stays bounded. A universal witness cannot simply mean a fixed local radius.

Numerical lesson: a fixed 85-digit Decimal context was insufficient for pair-window cells at enormous D: they are much smaller than the root influence. The initial largest-width row produced impossible L2>L1. The final evaluator uses precision at least L digits and all final rows satisfy the witness ladder. Gauss-node convergence checks quadrature integration only; comparisons against direct integer sums separately measure the finite-sum approximation. Neither is a directed-rounding certificate.

Prior-work caution: Shalev and ACKSW's read-k DNF theorems in the checked passages concern min-entropy. WWW's Shannon theorem concerns read-k decision trees. The local 23 September Shannon read-k manuscript has provisional status and is not assumed by these proofs. Linearity alone puts no square-root upper bound on D as a function of width.
