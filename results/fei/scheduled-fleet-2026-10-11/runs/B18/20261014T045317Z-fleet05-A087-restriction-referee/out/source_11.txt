# Exact failure of reset payment by the owned rarity release

Units are bits. This stage tests the explicit proposed substitution rho<=kappa at a physical controller query after data exposure. Here rho is A039's source-compatible Bayes product-reference reset and kappa is A038/A059's owned selector rarity release. This substitution is a new test frozen by A038, not a claim attributed to A039, A059 or the lead. No new definition of K_occ is used.

## 1. Actual ancestor and essential exposure

Use independent fair controls x,a,b and disjoint two-bit Boolean cores u,v. Select u when x=0,a=1; else select v when x=1,b=1; else output +1. Thus the two nominal rare events share x, with opposite orientations and an exclusive priority partition. Let u have table (-1,-1,-1,+1). Expose its first data coordinate at value 0. This query is essential: Inf_data(u)=1/2, and its ancestor F influence is (1/4)(1/2)=1/8. The reached u core is now constant -1. Take any nonconstant Boolean v on its independent data cube; it is not exposed or replaced.

At this actual descendant define G=1+1_{b=1}(v-1), with mean m=EG=(1+Ev)/2 in (0,1). Then F=-1 on x=0,a=1, F=+1 on x=0,a=0, and F=G on x=1. Query a. Its actual children are f0=+1 on x=0 and G on x=1, and f1=-1 on x=0 and G on x=1. Both retain the same nonconstant v branch, with physical probability 1/4. Each child's complete Fourier entropy and influence remain terminal obligations.

The selector of v remains {x=1,b=1} in both children. The only changed other selectors have constant outputs and variance zero. Hence the owned selector reserve R=sum_j q_j log2(1/q_j) Var(u_j) has kappa=R-E R_child=0 exactly. The queried physical influence is 1/2.

## 2. Exact source-compatible Bayes reset for the whole family

Let A=(1+m)^2/4 and B=(1-m)^2/4. At the empty and {x} residual Fourier masks, the child squared coefficients are (A,B) and (B,A). All other child spectral masses are identical. Other coordinate influences are identical; Inf_x(f0)=(1-m)/2 and Inf_x(f1)=(1+m)/2. Therefore

    Gamma=1-h2((1-m)/2),
    JS=(A+B)[1-h2(A/(A+B))].                              (1)

Erase a and let q=(P_f0+P_f1)/2. Use precisely the same kernel k(y|T)=P_fy(T)/(2q(T)) on the source q and its product-of-marginals reference Q, with fair fallback on zero fibers. The residual x marginal is 1/2 under Q, independently of every other coordinate. Q therefore puts equal mass on the two exceptional masks. Their kernel probabilities sum to one; on all other nonzero fibers the two child spectra coincide, and on zero fibers the fallback is fair. Thus Q(Y=0)=Q(Y=1)=1/2. The outcome KL O is zero exactly, not discarded.

A039's reset is rho=O+JS-Gamma, so here rho=JS-Gamma. Writing r(m)=rho gives

    r(m) ln2 = {m[(1+m)ln(1+m)-(1-m)ln(1-m)]
                         -(1+m^2)ln(1+m^2)}/2.             (2)

It is strictly positive for every 0<m<1. A direct calculus proof: r is continuous, r(0)=r(1)=0, r'(0)=0, and

    (ln2) r''(m)=1+ln((1-m^2)/(1+m^2))
                     -m^2/(1-m^2)-2m^2/(1+m^2).

The right side strictly decreases from 1 to -infinity. Consequently r' first increases and then strictly decreases, with r'(1-)=-infinity. It has exactly one zero in (0,1), r has one interior maximum, and the endpoint values imply r(m)>0 throughout the interior. No finite census is used to infer this continuum statement.

This family refutes rho<=kappa and [rho]_+<=kappa even after an essential nonconstant-core exposure. It does not refute a price rho<=kappa+K Inf_a, the unchanged reserve theorem, or universal FEI. In this family rho<=JS<=2 Inf_a/ln2; the missing positive price is finite.

## 3. Exact quantitative fixture with retained terminals

Choose v=(-1,+1,+1,+1), Ev=1/2, so m=3/4. The remaining dummy u data coordinate is retained in the physical table with influence zero. Direct Walsh coefficients yield parent spectral masses: two masses 1/4, two masses 9/64, and fourteen masses 1/64. The two child spectra each have one mass 49/64 and fifteen masses 1/64, with the heavy atom at empty for f0 and at {x} for f1. Thus

    Gamma=-2+(7/8)log2(7),
    JS=(49/32)log2(7)-(25/16)log2(5),
    rho=2+(21/32)log2(7)-(25/16)log2(5),  kappa=O=0.

Integer certificates give

    2^1428 * 7^525 < 5^1250 < 2^1432 * 7^525,

which is equivalent to 21/100<rho<43/200 bits. No floating sign is required. The query influence is 1/2. Parent total influence is 11/8; expected child influence is 7/8. Exact entropy is

    H(F)=4-(9/16)log2(3),
    E H(child)=6-(49/32)log2(7)>17/10,

where the terminal lower bound follows from 7^245<2^688. The family is an actual Boolean route obstruction with finite H/I, not a FEI disproof. The fixture itself has H(F)<4<4I(F).

## 4. Canonical occupancy account is retained distinctly

The archived source-exact Brain definition remains K_occ=D(P_nonempty||Q_r)=Hmax(r)-H(P_nonempty). Q_r is the nonempty maximum-entropy law with r_j=d_j/v, v=P(S!=empty). The full product KL satisfies TC=v K_occ+Delta, Delta=sum_j h2(d_j)-h2(v)-v Hmax(r). The selector reserve R and its release kappa are not either occupancy quantity.

In the fixture, after ignoring the actual dummy coordinate, parent d=(1/2,1/2,1/8,1/8,1/8), v=55/64, r=(32/55,32/55,8/55,8/55,8/55). Its positive normalization root solves

    1-c=(1-32c/55)^2(1-8c/55)^3.

Child f0 has v0=15/64 and r0=(8/15,8/15,8/15,8/15). Its nonempty spectrum is uniform, c0=15/16, theta_j=1/2, and K_occ(f0)=0 exactly. Child f1 has v1=63/64 and r1=(8/9,8/63,8/63,8/63), with normalization root

    1-c=(1-8c/9)(1-8c/63)^3.

No unproved sign for the parent/child occupancy change is inferred from this algebraic specification. It is the source-complete occupancy ledger accompanying the reset counterexample; neither child entropy nor the child1 occupancy reference is replaced by that of child0.

There is, however, a quantitative LOWER bound paying the explicit reset debt at this fixture. Let E be the event that the spectral set includes a and at least one of {b,v0,v1}. Its actual probability under the parent's nonempty spectrum is zero, as directly shown by the Fourier supports above. Under Q_r its probability is

    M_Q=(32/55)[1-(1-8c/55)^3].

The positive normalization root satisfies c>3/4: at c=3/4 the product in its equation is (31/55)^2(49/55)^3<1/4, equivalently 4*31^2*49^3<55^5; uniqueness of the positive crossing then gives the strict lower bracket. Therefore

    M_Q>M0=(32/55)[1-(49/55)^3]=1559232/9150625.

Binary coarsening of the KL yields K_occ>=-log2(1-M_Q). For 0<=z<1, -ln(1-z)>=z+z^2/2. Also ln2<7/10: strict convexity of 1/t bounds its integral from 1 to 2 by the three equal-interval trapezoids, whose sum is (1+2*(3/4)+2*(3/5)+1/2)/6=7/10. Thus the original root-weighted occupancy credit, not a reset to a new reference, satisfies

    v K_occ(F) > L=(55/64)(10/7)(M0+M0^2/2)
               >43/200>rho>21/100.                        (3)

Both comparisons in (3) are exact rational/integer certificates in FIXTURE.json. This is an explicit source-exact occupancy lower bound for the audit's positive reset debt, even though kappa=0. It supplies a feasible root credit at this one fixture, not a new free controller account, a bound on the change of K_occ, or simultaneous payment of all reset/control/terminal bills. Universal ownership of this credit is the remaining problem.

## 5. Exact open line and dispatch

The rejected first line is the explicit substitution rho<=kappa: the actual fixture has rho>21/100 and kappa=0. A039's identity, A038's reserve and A059's signed data payment remain valid. The first unsupported universal line is a single-use influence/terminal-slack payment for the combined product/occupancy reset, controller decrement minus kappa, and actual H-U-R terminal profile at arbitrary unfinished two-core histories. The next mechanism must retain the signed mean-controller spectral profile together with the rarity release; separately replacing the product reset by the nonnegative rarity release loses the exact positive debt exposed here.
