# C023 v1: integrable canonical weights for stationary histories

Status: proof (unaudited), auxiliary ideal-tree result for target 3. The conditioning below includes a limiting tree message; it is not an observable, predictable finite-graph exploration filtration.

Assume C005's top-initialized monotone Poisson tree process has an interior limiting law pi and that C009's stationary change matrix T has spectral radius below one. For each of the six pairs a>b, on the stationary tree let C_ab count the total progeny, including the initial particle, of a boundary perturbation a->b. The root reverse message has its unconditioned limiting law pi. By C009,

    E C_ab = sum_j pi_j * [1^T (I-T)^(-1)]_(a,b,j) < infinity.

Let H_t=(X_0,...,X_t,X_infty) be the root reverse history, F_t=sigma(H_t), and define

    w_t(a,b,d) = E[C_ab | H_t=d]

on positive-probability history values d. These are finite, at least one, and do not depend on the other coordinates of the incoming boundary history A, as C_ab depends on its limiting boundary value a and the new value b only.

For the compatible stationary history matrix B_t of C022, use weight w_t(a,b,d) on type (A,a,b,d). Then

    w_t^T B_t = w_t^T - 1^T.

Proof. Conditional on the parent history d, total progeny is one plus the sum of total progenies below its children. Given each child's outgoing reverse history and incoming boundary terminal pair, its descendant law is the corresponding conditional tree law in C022. The conditional expected child progeny is exactly its displayed weight. Take conditional expectations of this decomposition. The incoming trace A affects history labels but not the terminal cascade or its total count, so the same decomposition holds for every compatible A.

The family of random weights w_t(a,b,H_t), over all t, is uniformly integrable, and

    E[w_t(a,b,H_t) * 1{X_t != X_infty}]
      = E[C_ab * 1{X_t != X_infty}] -> 0.

Proof. For any integrable nonnegative C and any sigma-field F, put W=E[C|F]. On {W>K}, split C at K/2 to obtain W<=K/2+E[C*1{C>K/2}|F]<W/2+E[C*1{C>K/2}|F]. Therefore

    E[W*1{W>K}] <= 2 E[C*1{C>K/2}] -> 0,

uniformly over F. This proves uniform integrability. The late-trace event belongs to F_t, so the weighted-event identity is the defining conditional-expectation identity. Since the top-initialized messages decrease in a finite ordered alphabet, X_t equals X_infty eventually at each fixed root, almost surely. Dominated convergence with the integrable C_ab proves the limit. Summing these identities over the six pairs also gives a vanishing budget uniform over the choice of pair, by replacing the maximum with a sum.

Consequences and limits. This controls the mean canonical weight of late reverse histories without multiplying their probability by the worst refined weight. It strengthens the fixed-t subcriticality statement in C022. It supplies no rate, no uniform bound on the largest weight, and no uniform finite-inventory depletion constant. A finite-graph argument must still remove unobservable limiting labels, prove concentration/transfer of the weighted inventories, and choose exploration gates consistently with their depletion and multiple-hit errors. The vanishing expectation alone does not show it is smaller than a history-dependent exploration gate; a circular parameter choice remains invalid. No degree-weighted estimate is asserted without additional integrability. No finite-graph threshold follows here.
