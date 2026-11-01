# Complete maximal-matching mass as an occupation polynomial

For any finite nonempty simple graph G, fixed strictly positive feasible edge weights lambda, both endpoint orders per prime gate, pi=1/4, D=product_e(1+lambda_e/4)-1, and a covered nonempty set A, fix an inclusion-maximal matching M of G[A]. Write U=A minus matched vertices, m=|M|. Index an indeterminate z_v by every matched endpoint v. Define

    P_M(z) = product_(u in U) [ (1/32)sum_(v outside A, uv edge)lambda_uv
                             +(1/8)sum_(v matched, uv edge)lambda_uv*z_v ].

No neighbor of u is in U, by maximality. For a monomial z^h and edge e={v,w} in M put c_e=h_v+h_w. Define the linear operator

    J_M(z^h)=product_(e={v,w} in M) h_v!h_w!/[(c_e+1)^2(c_e+2)].

The complete original conditioned star mass of A006 is exactly

    Q_M(A)=D^-1 product_(e in M)(lambda_e/24) J_M(P_M).                 (1)

This replaces enumeration of individual unmatched neighbor choices by polynomial convolution while retaining all output ambiguity. Different neighbor choices can yield the same occupation monomial; their coefficients MUST be summed, not identified as one event. In an implementation this is one polynomial multiplication per unmatched coordinate followed by exact integer factorial/rational evaluation. The number of occupation vectors can still be exponential in m; no polynomial complexity for arbitrary graphs is asserted. Assignments/root decisions are not chosen for free: (1) aggregates a subfamily of one fixed original queue, whose decodability and event disjointness are reviewed in REVIEW_A006.md.

## Proof, moments and a collision credit

Choose the external term for an isolated singleton root, with exact probability lambda/32; choose internal z_v for a singleton child attached at v, with exact probability lambda/8 before the parent's count/multiset choices. The parent has two owned coordinates and c children, so its count/multiset cost is 1/[(c+1)(c+2)(c+1)]. At each endpoint h! actual child-label orders are possible. Expanding P and applying J gives every factor in A006's formula. The matching root factor lambda*pi*t_pair=lambda/24 excludes its child-count factor, which is inside J. At c=0, J contributes 1/2. Empty matching and empty product conventions recover independent A exactly.

Alternatively, independently per matching edge take T uniform on [0,1], B with density 2(1-b), and two rate-one independent exponentials Y_v,Y_w. Put X_v=TB Y_v and X_w=TB Y_w. Integer beta and exponential integrals give

    J_M(P)=2^(-m) E P(X).

The two endpoint variables share TB. Their dependence retains the chronological factorial credit. Gate/edge triples are independent; arbitrary factorization across endpoints is false.

There is a useful quantitative correction to A006's discarded-factor lower mass. For integers a,b>=0, c=a+b,

    a!b!/[(c+1)^2(c+2)] >= (1/2)*6^(-c)*2^max(c-1,0).                (2)

To prove it, a!b! is minimized at floor(c/2)!ceil(c/2)!: moving one unit from the larger part to the smaller reduces their factorial product until balanced. At c=0 and 1, (2) is equality. At c=2 the ratio of the left side to (1/2)6^-c is 2. Thereafter its consecutive minimal ratio is

    6*ceil((c+1)/2)*(c+1)^2/[(c+2)(c+3)] >= 2  (c>=2).

Indeed ceil((c+1)/2)>=2 for c>=2 and (c+2)(c+3)<3(c+1)^2 there. Thus induction proves (2). (The exact factorial ratio is ceil((c+1)/2).)

Writing P=sum_h p_h z^h, k(h)=sum_e c_e and d(h)=number of matching edges with c_e>0 gives the computable lower mass

    Q_M(A) >= D^-1 product_(e in M)(lambda_e/48)
               *sum_h p_h*6^(-k(h))*2^(k(h)-d(h)).                  (3)

Discarding 2^(k-d) recovers the simpler internal-child factor lambda/48. External-root factor lambda/32 remains exact in P. A further coarsening to lambda/48 for external choices yields A006's row-sum bound. The collision credit in (3) is zero for a sole child on each parent and positive when a parent absorbs at least two children. It is not a universal label-payment theorem; (1) retains the stronger exact factorial credit for that purpose.

## First unpaid line

One still needs an absolute K and one fixed feasible lambda for every graph such that the true spectral expectation of -log sum_maximal_M Q_M(A) is <=K I(f_G). Positivity, the local credit (2), and finite n=4 costs do not prove that expectation inequality. The next shortest test is whether occupation-weighted factorial credit, coupled to physical graph Fourier coefficients, pays unmatched-row imbalance and matched labels in non-independent sectors; arbitrary-density raw indicator-sum error is not assumed small.
