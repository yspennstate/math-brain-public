# The remaining arbitrary-support budget, with root credits retained

This continues the SAME fixed-reference distributed lift, not a universal payment assertion. Fix nonempty data T of size s, assignment tau with used gate sizes s_l>=1, intersections kappa_l=|T intersect R_l| between s_l and s, and a_l=s_l/s. For selected core size u>=1, retain the exact occupation sum

    Z_tau(u)=sum_(alpha:U->V) product_l
       [((s_l+v_l)/(kappa_l+u))^(gamma(s_l+v_l)) /(s_l/kappa_l)^(gamma s_l)].

Define, in bits,

    K_tau(u)=sum_l a_l [s log(s/kappa_l)
                  -(s+u)log((s+u)/(kappa_l+u))].

Then for EVERY covered assignment and integer u>=1,

    log Z_tau(u)>=-(1/5)u H(a)-gamma K_tau(u),
    0<=K_tau(u)<=[u/ln 2] sum_l a_l
                        [s/kappa_l-1-ln(s/kappa_l)].

For coincident selected supports kappa_l=s, K_tau=0 and this specializes exactly to A015's reviewed full-support envelope. It quantifies rather than silently omits the failure of that envelope on general supports.

Proof: draw the u labelled owners independently with probabilities a_l solely as a variational law on actual maps. Its entropy is u H(a), mean v_l=u a_l. The log-sum inequality gives log Z>=uH+E log weight. Convexity of x log x gives E(s_l+v_l)log(s_l+v_l)>=(s+u)a_l log((s+u)a_l). Substitute in the weight and cancel the old congestion to obtain the displayed lower bound exactly. This proof law does NOT replace eta_T or choose a new reference.

For a fixed kappa<=s, the derivative with respect to u of s ln(s/kappa)-(s+u)ln((s+u)/(kappa+u)) is d((s+u)/(kappa+u)), where d(t)=t-1-ln t>=0. The ratio decreases with u and d increases for t>=1; the derivative therefore decreases. The expression is zero at u=0, nonnegative, and bounded by its tangent u d(s/kappa). Sum with weights a_l and divide by ln2. This proves both signs and the upper bound for all u without extrapolation.

## Unequal root rarities: a valid lower credit

For an ACTUAL old forest rho with root set R, c=|R|, set

    C_root(rho)=sum_(a in R) log(1/pi_a)-max_(a in R)log(1/pi_a)>=0,
    m(u,c)=(u)_(c-1), with m(u,1)=1.

The exact distributed rooted counts m_a sum to m(u,c). For every core ownership map alpha, therefore

    sum_(a in R)m_a pi_a/prod_R pi >= m(u,c) min_R(pi)/prod_R pi
                                   =m(u,c)2^(C_root(rho)).

The largest retained root rarity is paid; all other old root rarities give a valid credit. This remains true for c=1, where both sides are one and the surviving root need not own core coordinates. No equal-width hypothesis is needed. Hence

    J_dist,U(T)>=E_eta_T [ beta^|V| m(u,c)2^(C_root(rho)) Z_tau(u) ].

Using convexity of negative log / Jensen on this SAME eta_T and the preceding envelope,

    -log J_dist,U(T)<=E_eta_T [ |V|log(1/beta)-log m(u,c)
                              -C_root(rho)+(u/5)H(a)+gamma K_tau(u) ].

For empty selected core, -log L_0<=E_eta |V|log(1/beta). Under uniform selected core u~Bin(r,1/2), combine these sectors BEFORE bounding any normalization to get

    Psi_dist <=p Var(g)log[D'/(pD)]
       +p sum_(T nonempty)P_g(T) E_eta_T [ |V|log(1/beta)
             -(1-p)C_root(rho)-E_u[1_(u>0)log m(u,c)]
             +(r/10)H(a)+gamma E_u K_tau(u) ].

Take K_tau(0)=0. All spectral weights are unconditioned, eta_T is conditional on T only, and u is the independent uniform-core subset size. The displayed cost keeps globally scaled labels, actual-event entropy, rare-root credit and the NEGATIVE signed normalizer in one ledger. It is not claimed <=K I(F). In the full-support uniform-label regime beta=1,c=1,K_tau=0, the posterior-tail theorem pays the remaining H term and recovers the closed controller correction. In arbitrary prime tables the first unsupported line is an influence-paid expectation of this complete signed budget, including K_tau and the same posterior labels; separate pointwise upper bills cannot discard the two credits.
