# Orientation-aware finite arbitrary-core extraction

Uniform physical cubes, costs in bits. This is a finite strengthening of A007's source-reference reduction, not full FEI.

For every nonconstant sign Boolean g on s>=1 bits and 0<delta<=1, choose h in {g,-g} with false density q<=1/2. The squared Fourier spectrum, variance and influence of h equal those of g. Let A be the least integer with 2^A>=8s/delta and put L=2A, epsilon=2^-L. For each false core point v, form L signed clauses a_v(z) OR y_v,l with distinct positive private bits, where a_v is false exactly at v. The sign of their conjunction is F_L. The representation, orientation and core event are fixed before any spectral set.

Each displayed clause is an irredundant prime implicate: setting core=v and just its selected private bit false isolates the clause. Removing the private literal fails at v with all private bits true. Removing a core literal fails at the neighboring core point with that literal flipped and with all other relevant private groups true. This proves minimality without claiming completeness of the prime table.

An independent reconstruction of A007: F_L=h+2 sum_{v:h(v)=-1} 1_v AND(y_v). Hence E_y F_L=(1-epsilon)h+epsilon. Every nonempty core coefficient is (1-epsilon) hhat(B). A private-supported coefficient is zero if it meets two groups; otherwise, for each nonempty subset of one group and each core subset, its magnitude is 2^(1-s)epsilon. The entire private spectral mass is 4q epsilon(1-epsilon), its entropy exactly that mass times (2s+2L-2). The finitely many core probabilities converge to those of h, and the displayed private entropy tends to zero. Thus H(F_L)->H(g) without dimension-dependent continuity assumptions.

Direct physical edges give

 I(F_L)=(1-epsilon)^2 I(g)+2q epsilon[s(1-epsilon)+L].

Indeed a core edge crossing true/false disagrees with probability 1-epsilon, while a false/false edge uses TWO DISTINCT private groups and disagrees with probability 2epsilon(1-epsilon). Its total false/false oriented incidence is sq-I(g)/2. Private edges contribute 2qL epsilon. This is the physical influence, not an independent-copy surrogate.

For any fixed normalized or subprobability nonempty reference R covering F_L's spectrum, define Z=sum_{B nonempty core}R(B,empty), and r(B)=R(B,empty)/Z. The sign orientation changes no target probability. The COMPLETE equality is

 C_g(r)=C_core(F_L;R)/(1-epsilon)^2+Var(g) log2 Z.

Coverage gives 0<Z<=1. The negative normalizer is retained in the equality before using C_core<=C_total and log Z<=0. A decoder for r conditions the supplied finite alphabet on its fixed core-only event and outputs that core subset; every original branch, gate name, attachment, local-mask choice and final allocation is already included in the supplied R mass. No new free label, output-dependent prior or history reset is assumed. Its logarithmic rate is the normalized finite-alphabet rate; integral prefix overhead is not silently omitted.

Poincare gives I(g)>=Var(g)=4q(1-q)>=2q. Therefore a supplied complete nonempty cost C_total(F_L;R)<=K I(F_L), K>=0, yields

 C_g(r)<=K[1+epsilon(s+L)/(1-epsilon)^2]I(g).

The denominator is essential; omitting it is an invalid finite extraction. Here A>=3, epsilon<=1/64 and (1-epsilon)^-2<2. Put x=8s/delta. For x>=8, ceil(log2 x)<=x (on each dyadic interval the least integer exponent is <= its lower endpoint). Thus A<=8s/delta. Since delta<=1,

 epsilon<=delta^2/(64s^2),
 2epsilon(s+2A)<=delta^2/(32s)+delta/(2s)
                    <=17delta/(32s)<=delta.

Consequently C_g(r)<=(1+delta)K I(g). This is FINITE, with L=2ceil(log2(8s/delta)), reducing A007's exhibited 4s+4 choice to logarithmic per-clause private multiplicity for fixed accuracy, while preserving the full conditioning refund. It does not shrink the exponential number of false core points, price R, or prove a universal core supplier.

Independent A007 whole-claim review: the prime-clause witnesses, all spectrum sectors, exact influence, entropy limit, normalizer equality, finite 2K bound at L=4s+4, and same-constant FEI equivalence all hold as stated. For its finite bound, 5s+4<=2^(3s+2) starts at s=1 and propagates by multiplying the right side by eight; each nonconstant core has at least one changing edge, so I(g)>=2^(1-s). No substantive repair to A007 is required. Its all-positive PRIVATE literals must not be confused with all-positive CORE literals. A008's earlier obstruction is not a premise of this review.

First unsupported universal line: supply the original fixed reference R for arbitrary signed cores with complete cost<=K I(F_L) from one physical influence account. The orientation and shorter finite lift do not pay that source. Full FEI remains OPEN.
