# A global joint weight/posterior lower bound from root-law coordinates

Fix any finite actual once-per-gate partition event family with positive output mass on the positive spectrum. The table/covers/rarities and family are fixed from f. For a used gate subset T, let k_AT be the sum of the COMPLETE unnormalized coefficients of all distinct actual runs producing A with exactly used subset T. It includes their actual root pi, size/subset/count/multiset and chronological factors. Each run has positive probability k_r product_(e used)lambda_e/D. Thus

    W_A(lambda)=sum_(nonempty T) k_AT product_(e in T)lambda_e,
    D(lambda)=sum_(nonempty T) pi_T product_(e in T)lambda_e,
    pi_T=product_(e in T)pi_e.

Run/occupation aggregation retains the sum of every actual event coefficient, not one description per used subset. Define the original nonempty initial-root law

    p_lambda(T)=pi_T product_(e in T)lambda_e/D,
    K_AT=k_AT/pi_T.

Then the complete output mass with its event posterior already optimized is EXACTLY

    Q_A(lambda)=sum_T K_AT p_lambda(T).                         (1)

The set T on the left coefficient is a USED-gate subset; T in p is an INITIAL-root subset. Equality is an algebraic reindexing of the same monomials, not a bijection identifying roots with used gates of a run. It does not introduce a new generator.

On the full probability simplex of p define G(p)=-sum_(A!=empty)P_f(A)ln(sum_T K_AT p(T)). This is convex wherever every positive-spectral output mass is positive, and +infinity otherwise. The physical p_lambda with packing constraints form a subset of that simplex, usually a nonlinear one. Therefore minimizing G over the full simplex gives a global LOWER bound on the joint lambda/posterior infimum for this fixed event family. Do not claim K is a stochastic channel: column sums can exceed one, and a general relaxed p need not yield an output subprobability or a physical code. The relaxed lower bound is an optimization bound, not an entropy-reference construction.

## A rational global certificate at any physical reference

At a positive feasible lambda, put Q_A=Q_A(lambda), v=sum_nonempty P_f(A), and

    h_T=sum_A P_f(A) K_AT/Q_A,
    Gamma=max_T h_T-v.

The derivative of G with respect to p(T) is -h_T, and sum_T p_lambda(T)h_T=v. Hence Gamma>=0. The supporting hyperplane and min of a linear function on the simplex give

    G(p_lambda)-Gamma <= inf_p G(p) <= inf_feasible_lambda G(p_lambda)
                                            <=G(p_lambda).         (2)

Thus the complete BIT cost at this physical reference is globally within 2*Gamma of the infimum over ALL positive feasible global weights AND all actual posteriors in this SAME event family, using ln2>1/2. No frozen posterior is assumed. For rational k,pi,lambda,P, Gamma is exactly rational; no logarithm or numerical optimizer is needed for this gap. Reporting the cost value still needs a logarithm enclosure.

This certificate may be loose: it drops all multiplicative root-law and packing constraints. It cannot be compared as a lower bound for a larger event family, including all forests, without recomputing that family's coefficients. Computing the full k_AT table or all 2^N-1 root subsets can be exponential. The zero/one-gate cases and zero coefficient columns are allowed. For one gate h=v and Gamma=0, consistent with the conditional constant cost.

The one-gate slice theorem in JOINT_EDGE_SLICE.md is the sharper exact restriction of (1) with the other weights fixed. For two or more varying gates, the root-law manifold is nonlinear; convexity of the relaxation does not make the original joint problem convex. NEXT can compare the global root-law gap to the exact coordinate gaps and occupation-credit ledger on overlapping degree scales. No influence-paid universal K follows from a lower bound or a finite numerical gap.
