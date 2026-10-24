# Uniform-scale posterior failure versus the weight infimum

Bits, gamma=6/5. The table is exactly the positive width-two edge primes of a finite graph; both full endpoint orders are fixed for every gate (M_e=2), pi_e=1/4. All lambda are fixed before sampling a Fourier set. W_B(A) is the FULL surrogate sum over distinct once-per-gate source-SCC partition events; D=product_e(1+lambda_e/4)-1. Q_part(A) is the exact conditioned probability of those same events. The scalar residual is R=E_{A nonempty} log2[D/W_B(A)]. Full queue cross-entropy is C_part=E[-log2 Q_part(A)]. Neither is an infimum over weight vectors until explicitly stated.

## A pointwise negative-credit guard

For one event, g used gates own a nonempty partition of A, and e child edges satisfy g<=|A|, e<=g. Its exact numerator Dq is product_used(lambda_e pi_e^{root} t(S_e)) times all count/multiset probabilities. Both-order width-two draw probabilities are t(singleton)=1/4 and t(pair)=1/6, including the subset choice. For s=1 or2 the count/multiset denominator is at most (c+1)^2(c+2)<=2*6^c. Surrogate 2^-B has the same lambda/root factors, times alpha_e=2^-s(s/kappa)^(gamma s) with kappa=|A intersect edge|. The minimum rank term is zero since either endpoint can be first. Therefore 0<alpha_e<=1 and

    2^-B/(Dq) <=12^g 6^e <=72^|A|.

Also alpha_singleton>=2^(-6/5)/2>=1/8, and alpha_pair=1/4; these dominate t(S)/2, which is an upper bound on t(S) times any count/multiset probability. Thus 2^-B>=Dq. Summing the SAME disjoint actual events yields

    Q_part(A) <= W_B(A)/D <=72^|A| Q_part(A)<=72^|A|.

In particular C_part-(log2 72)I<=R<=C_part. This is a bounded additive difference for width-two/two-order partition references, not a universal cost payment. It lets a selected positive log-weight debt be isolated without assuming that the residual on all other sets is nonnegative. Every size/subset/count/attachment/label/root term was compared, not dropped.

## Actual Boolean family

Let U_m=x0 AND (OR_{i=1}^m xi), V=y AND z on fresh signs, and f_m=U_m OR V, viewed as a +/-1 sign. Its graph is the m-edge star disjoint from the edge yz; these m+1 edges are exactly its positive primes. Put u=2^-m, q_m=P(U_m=false)=(1+u)/2. The exact total influence is

    I_m=(3/4)[1+(m-1)u]+q_m=5/4+(3m-1)u/4<=25/16   (m>=2).

For each selected singleton {y} or {z}, P_f(A)=q_m^2/4, so their combined mass is q_m^2/2>=1/8. These coefficients and all influences are checked on actual truth cubes, not assigned as an abstract set law.

## Failure even after optimizing the whole posterior at the uniform scale

Set ALL m+1 weights lambda=1/m. It is positive and packing-feasible. D_m=(1+1/(4m))^(m+1)-1>=1/4 by Bernoulli. An isolated-edge singleton has exactly one partition event, W_B=1/(8m). Its residual cost is log2 D_m+log2(8m)>=log2 m. All other sets have cost >=-|A|log2 72 by the guard. Consequently

    R_uniform >=(1/8)log2 m-(log2 72)I_m,
    R_uniform/I_m >=(2/25)log2 m-log2 72.

This already uses the fully optimized conditional posterior over ALL partition forests at that fixed table, not one selected tree. For the actual Boolean sequence m=2^(25t), t>=1, the ratio is >2t-7 and is unbounded. This refutes a universal claim that the max-read uniform scale lambda=1/Delta always pays the complete posterior residual. It does NOT refute the variational infimum over weights, PI-J, or FEI.

There is a stronger exact transfer that keeps the SAME conditional posterior. Every partition event for A with A intersect {y,z} nonempty uses the isolated edge exactly once; events for all other A do not use it. Changing only its weight from1 to1/m therefore multiplies W_B(A) by1/m in precisely that first sector, without changing its conditional run posterior. Let eta=3q_m/4 be that sector's actual spectral mass and V_m=3q_m(1-3q_m/4) the full variance. Then

    R_uniform-R_repaired=eta log2 m+V_m log2(D_uniform/D_repaired).

Here eta/I_m>=7/25: after clearing denominators this is (42m-89)<=5*2^m, verified at m=2,3,4 and by the adjacent-ratio induction for m>=4. D_uniform>=1/4 and D_repaired<2/3, while V_m<=1 and I_m>=5/4. The negative-credit guard applied to the repaired table and log2 72<7 therefore give

    R_uniform/I_m > (7/25)log2 m-9.

For m=2^(25t) this is >7t-9; at t>=3 the uniform reference exceeds11I even though the same-prime-table repaired reference below is <=11I.

The whole positive isolated-edge weight continuum can also be settled exactly with the star weights fixed. Put D_star=(1+1/(4m))^m-1 and let its weight be beta in (0,1]. Every conditional posterior is independent of beta, and

    R(beta)=constant+V_m log2[D_star+(1+D_star)beta/4]-eta log2 beta.

Differentiation has the sign of (V_m-eta)(1+D_star)beta/4-eta D_star. Since V_m-eta=(9/4)q_m(1-q_m)>0, the unique GLOBAL minimizer on this one-dimensional admissible slice is the rational value

    beta_star=4 eta D_star/[(1+D_star)(V_m-eta)]
             =(4/3)D_star/[(1+D_star)(1-q_m)].

Bernoulli and the geometric-series bound give 1/4<D_star<1/3, and 3/8<=1-q_m<1/2; hence 8/15<beta_star<8/9. The zero boundary has infinite cost. This is exact joint posterior/weight optimization on the isolated-edge slice, not an optimum over all star weights or arbitrary table orders. Its cost is at most the beta=1 repaired cost.

## Same primes and orders, globally admissible repair

Keep star-edge weights 1/m and change ONLY the isolated-edge weight to1. Packing remains feasible because the components are physically disjoint. Use all maximal-matching star events, with exact numerator N(A)=D Q_MS(A). Disjoint components factor this unnormalized mass: root conditioning remains one GLOBAL D; no reference is selected after A. Owned subsets, source SCCs and neighbor choices split, and chronological child sequences are uniquely recovered componentwise even though the BFS queue is global. Thus N(A)=N_star(A_star)N_pair(A_pair), with N_component(empty)=1. Root orders are fixed and no root-permutation credit is added.

The single edge with weight1 has N_pair(singleton)=1/32 and N_pair(pair)=1/48. For the star, N_star({hub})=1/32. For any other nonempty A_star, the coarse maximal-matching row-sum lower bound gives N_star(A_star)>=(48m)^(-|A_star|): every leaf has row mass1/m, a matching uses lambda=1/m, and all singleton/matched factors are retained. If selected hub and k>=1 leaves occur, the stronger exact numerator is

    N_star(A_star)=(k-1)!/[3*8^k*m^k*k*(k+1)].

A leaf-only k-set has N_star=(1/(32m))^k. These formulas agree with the occupation operator; they are for complete queue mass, not surrogate B.

The star sign spectrum has singleton-hub mass (1-u)^2 and every set with a nonempty leaf part has mass u^2 (with or without the hub). Its total degree mass outside {hub} is (m+1)u-u^2. Therefore, since log2 48<6 and log2 m<=m,

    E_{P_star}[-log2 N_star] <=5(1-u)^2+(m+1)2^-m(6+m)<=11,

because (m+1)(m+6)2^-m<=6 for m>=2; equality of this latter upper bound is at m=2 and the consecutive ratio decreases thereafter. I_star=1+(m-1)u>=1, so the same cost is <=11 I_star. For the pair, E[-log2 N_pair]<=6 I_pair with I_pair=1.

The OR-composition Fourier law, derived directly from false-indicator products, scales the star numerator bill by3/4 and the pair bill byq_m. Cross-sector and terminal component spectra are retained. The repaired global D=(5/4)(1+1/(4m))^m-1<2/3<1, since the binomial expansion is bounded by sum_j(1/4)^j=4/3. Its signed normalization contribution is nonpositive. Thus

    C_MS(f_m)<=11[(3/4)I_star+q_m I_pair]=11 I_m.

The pointwise lower side Q_part<=W_B/D, and Q_MS<=Q_part, imply R_repaired<=C_MS<=11I_m. Hence the infimum over ALL admissible positive weights on this SAME both-order prime table is <=11I_m for every m. Broader representations can only decrease that infimum. This is a quantifier separation and a necessary multiscale weighting diagnostic; it is not a new FEI theorem for the already read-once Boolean family.

## Honest universal boundary

The uniform-scale mechanism fails on an actual family after full posterior optimization, while weight optimization repairs the same family. Any genuine PI-J falsifier must defeat every globally admissible weight choice, including independent component scales. For arbitrary overlapping graph prime tables, the complete spectral expectation of matched-label and unmatched-row occupation costs remains unpaid; component factorization and the rare star-tail bound cannot be assumed there. NEXT should test those same terms on overlapping degree scales, using the reviewed occupation operator and whole-domain weight certificates before reporting growth of the infimum.
