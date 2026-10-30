# Global incidence optimization of a complete allocation certificate

Use natural logarithms in this section; divide costs and dual values by ln 2 for bits. Fix nonempty physical supports E_j, N_j=2^|E_j|-1, and a Boolean f with P(A)=fhat(A)^2 and v=sum_(A nonempty)P(A)>0. Choose gate activation probabilities 0<alpha_j<1 subject to ALL coordinate constraints sum_(j:i in E_j)alpha_j<=1. Independently activate the supports, draw a uniform nonempty local subset in every active support, and condition the entire tuple on at least one activation. Decode by physical UNION. This is a NEW normalized whole-set dictionary reference, not an original prime queue. Its probability is Q_alpha(A)=sum_(z:union z=A)mu_alpha(z)/Z, Z=1-product_j(1-alpha_j). No activation or allocation is silently erased.

For each nonempty A with P(A)>0 choose a fixed probability rho_A on the finite set of tuples z with union A. These witnesses certify a bound; the actual reference alpha and support dictionaries are fixed before sampling A. Define M_j=sum_A P(A)Pr_(rho_A)(z_j nonempty), and h=sum_A P(A)H_e(rho_A). The log-sum inequality, or KL against the actual allocation posterior, gives

    C_e(Q_alpha) <= B(alpha)+v ln Z <= B(alpha),
    B(alpha)=sum_j[-M_j ln alpha_j-(v-M_j)ln(1-alpha_j)+M_j ln N_j]-h. (1)

This is a complete nonempty OUTPUT cost upper bound. The negative v ln Z can be retained for a sharper final certificate, but is omitted in the convex optimization. Different witness choices change B; we do not assert convexity of the true pushforward cost or joint convexity in alpha and rho. In particular an optimizer of B is not claimed to optimize C.

With fixed witnesses, B is convex and separable on the incidence polytope. For any physical coordinate prices y_i>=0 put s_j=sum_(i in E_j)y_i and c=sum M_j ln N_j-h. Its Lagrange dual lower bound on min B is

    D(y)=c-sum_i y_i+sum_j min_(0<a<1)[-M_j ln a-(v-M_j)ln(1-a)+s_j a]. (2)

For 0<M_j<v and s_j>0 the unique minimizer is the smaller root of

    s_j a^2-(v+s_j)a+M_j=0,

or a=2M_j/[v+s_j+sqrt((v+s_j)^2-4s_j M_j)]. For s_j=0 it is M_j/v. Endpoint cases use limits. Slater holds by choosing all activations sufficiently small, so the finite convex problem has the usual strong duality when its optimum is interior to the box; alternatively the following exact certificate requires no duality theorem.

An explicitly rational feasible alpha and rational nonnegative y certify a GLOBAL optimum of B if

    (v alpha_j-M_j)/(alpha_j(1-alpha_j))+s_j=0 for every j,
    y_i*(sum_(j:i in E_j)alpha_j-1)=0 for every i.             (3)

All these tests are rational when the Boolean spectrum and witnesses are rational. By convexity phi_j(a)>=phi_j(alpha_j)-s_j(a-alpha_j); summing and using incidence feasibility and complementary slackness proves B(a)>=B(alpha). This is also equality of primal and dual. Logarithms are needed only to bound its value, not to verify optimality. Rational log intervals then give a verifiable cost/I bound for the actual finite Boolean function. The dual lower bound alone is NOT a code upper bound: the latter comes from the feasible primal and (1).

Finite common-anchor fixtures in code/check.py use uniform witnesses over ALL physical-union allocations. Clause permutation makes M_j=M. Put alpha=min(M/v,1/r), shared-coordinate price y_z=max(0,(M-v/r)/[(1/r)(1-1/r)]), and private-coordinate prices zero. If the incidence cap is inactive, y_z=0 and alpha=M/v; if active, alpha=1/r. Thus (3) certifies the optimum of this fixed-witness objective with exact rational numbers, while retaining every physical coordinate constraint and the allocation entropy refund. Only r>=2 is used in these fixtures.

The first unsupported universal line is B(alpha)<=K I(f) for an influence-paid representation and witnesses. The next proof shows this cannot follow from activation retuning alone with uniform clause-subset dictionaries, even allowing arbitrary activation dependence or mixtures.
