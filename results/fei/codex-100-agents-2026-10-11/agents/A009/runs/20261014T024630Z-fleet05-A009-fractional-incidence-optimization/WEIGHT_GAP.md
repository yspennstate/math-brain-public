# Complete star posterior: occupation counts and exact global weight gaps

Fix an arbitrary finite nonempty graph prime table, both endpoint orders, pi=1/4, and a positive feasible base vector lambda0. Use A006's complete maximal-matching star family and A008's exact occupation coefficients. For every nonempty covered A the unnormalized mass W_A(lambda)=D(lambda)Q_MS(A;lambda) is a positive MULTIAFFINE polynomial in lambda: each actual event visits each used gate once. All coefficients are rational in this two-order reference. Repeated occupation vectors retain the sum of all neighbor-choice coefficients and chronological child-label factors.

Freeze eta_A to the actual event posterior at lambda0. Define v=Var f, c_e=sum_A P(A) Pr_eta(e used), C=sum_e c_e, and let K collect all size/subset/count/root-rarity factors and frozen posterior entropy. Then its complete spectral cost in natural units is

    F(lambda)=K+v ln D(lambda)-sum_e c_e ln lambda_e,
    c_e=sum_A P(A) lambda0_e partial_e W_A(lambda0)/W_A(lambda0).

This supplies c directly from the complete occupation polynomial, without replacing the exact queue by a surrogate B moment. All reference data are fixed before A. Since one actual gate owns at most two selected coordinates, I/2<=C<=I, and C>=v. The latter uses at least one visited gate for every nonempty A. In log weights t=ln lambda, F is convex and incidence constraints sum_(e incident j)exp(t_e)<=1 are convex. Optimizing this frozen posterior is therefore a global convex problem; optimizing posterior and weights jointly is not asserted convex.

## Finite positive and unique optimum for every nontrivial graph table

For every edge e={u,w}, c_e>0. A monotone Boolean function has squared singleton coefficient P({u})=Inf_u(f)^2>0 at every covered vertex (average the two coordinate values to obtain the singleton identity). On A={u}, the star family is the exact independent sector, and its root-label posterior assigns positive probability lambda0_e/r_u to e. Hence c_e>=P({u})lambda0_e/r_u>0.

If G has at least two edges, C>v. If there are adjacent edges, restrict all other coordinates negative and retain their three endpoints. The resulting graph is either the two-edge path or the triangle; direct expansion gives degree-three coefficients of magnitudes 1/4 and 1/2 respectively. If all edges are disjoint, restrict to two edges; their union has a nonzero degree-four coefficient. Restriction cannot increase Fourier polynomial degree, so the original spectrum contains a positive-mass set with at least three coordinates. Every selected star run on that set uses at least two gates, proving C>v. This does not infer a degree-three coefficient at any PARTICULAR global set from its restricted coefficient.

Consequently the objective diverges at every boundary with some weight zero. If some other weight stays bounded away from zero, D stays bounded away from zero and the positive c_e makes -c_e ln lambda_e diverge. If all weights vanish, put L=max lambda. Since D>=L/4 and sum c_e ln lambda_e<=C ln L, F>=K-v ln4+(v-C)ln L tends to infinity. The incidence polytope is bounded, so a minimizer exists with every weight positive. For N>=2 the nonempty root indicators have full affine span: singleton indicators and an indicator with two roots force any affine functional constant on their support to be zero. The Hessian of ln D in t is their positive definite covariance. Thus F is strictly convex in t and the positive global minimizer is unique. For N=1, c=v and D=lambda/4; the complete frozen cost is constant in lambda, a separately stated exception.

These all-graph statements make exact certificates feasible at a genuine optimizer, rather than assuming numerical boundary infima. They neither prove a dimension-independent payment nor claim that jointly varying posterior and weights has a unique optimum.

## Exact certificate, including negative marginal repair

For ANY nonempty root-subset probability law nu, let r_e=Pr_nu(e in R), b_e=c_e-v r_e. Require b_e>=0. Choose nonnegative coordinate prices y_j and q_e=y_u+y_v, with q_e>0 whenever b_e>0. For any positive feasible lambda put z_e=lambda_e q_e and let omega_lambda(R)=product_(e in R)(lambda_e/4)/D(lambda). Then the following NATURAL-unit quantity is a rigorous primal-minus-global-lower-bound certificate:

    G=v KL(nu || omega_lambda)
       +sum_j y_j(1-sum_(e incident j)lambda_e)
       +sum_e [b_e ln(b_e/z_e)-b_e+z_e].                 (1)

Use 0 ln(0/z)=0, and the limit zero if b=z=0. Every term is nonnegative. Consequently F(lambda)-G<=inf_feasible F<=F(lambda); division by ln2 gives bit units. Proof: the log-sum variational lower bound at nu gives v[H(nu)+sum r ln pi+sum r ln lambda]. Subtracting the incidence prices reduces each edge to -b t+q exp(t), whose infimum is b[1+ln(q/b)] (or 0 if b=0). Subtraction from the primal yields exactly (1). K cancels; the root KL identity retains the full signed normalizer D. This extends the earlier fixed-law dual to a checkable complete-cost GAP, using the actual occupation usage counts and a root law chosen to avoid negative b.

There is always a rational admissible root law when c is rational and C>=v: use the singleton law sigma({e})=c_e/C. It has b_e=c_e(1-v/C)>=0. For a sharper certificate at a proposed rational lambda, mix its rational normalized root law omega with sigma:

    nu=(1-delta)omega+delta sigma.

If c_e-v omega_e<0, delta must be at least (v omega_e-c_e)/(v omega_e-v c_e/C); other edges need no repair. Every ratio is rational and lies in [0,1] (with equality possible at C=v). Choose a rational delta satisfying all these inequalities. Then b>=0 exactly. The root KL is evaluated on distinct ROOT SETS, including all multi-root sets, rather than using their marginals alone. This mixture is certificate side information; it does not change the frozen actual posterior or the globally fixed reference.

Rational proposed lambda, root-law probabilities, c and y make all log arguments rational. Range-reduced atanh intervals therefore certify G and the complete primal cost without a floating-point sign. A numerical optimizer can suggest lambda and y; its convergence declaration is not proof. An exact gap bounded by epsilon I proves global epsilon-optimality for this frozen posterior. A source-complete proof of a universal influence payment would still need to bound K plus this optimized objective on arbitrary graph spectra.

In fact the optimization GAP needs no logarithm certificate. The elementary inequality ln x<=x-1 gives KL(nu||omega)<=delta^2 chi^2(sigma||omega) and b ln(b/z)-b+z<=(b-z)^2/z. Since sigma is supported on singleton root sets,

    chi^2(sigma||omega)=sum_e (c_e/C)^2/[lambda_e/(4D)]-1.

Thus G is at most the entirely RATIONAL quantity

    G_rat=v delta^2 [sum_e (c_e/C)^2 4D/lambda_e-1]
          +sum_j y_j(1-row_j(lambda))
          +sum_e (b_e-lambda_e q_e)^2/(lambda_e q_e).       (2)

Choose strictly positive q so the last denominator is valid even if b=0. Equation (2) proves G_bit<=2 G_rat using ln2>1/2. It avoids enumeration of every root subset and any logarithm in the gap checker, while retaining their full KL cost through the exact mixture identity. It does not factor occupation expectations or modify the frozen posterior. Only the reported complete primal cost uses certified logarithm intervals.

## Scope and unpaid line

The certificate holds for every finite graph and every frozen maximal-matching star posterior; no bounded-read hypothesis. The exact occupation coefficients already cover unmatched non-independent sectors. Finite graph certificates do not establish an all-graph K, and a frozen-posterior lower bound is not a lower bound for jointly optimized PI-J. The first unsupported universal line remains a dimension-independent complete expected-cost bound under one globally fixed reference, with the occupation/factorial, matched-label and unmatched-row terms paid on the same Boolean spectrum.
