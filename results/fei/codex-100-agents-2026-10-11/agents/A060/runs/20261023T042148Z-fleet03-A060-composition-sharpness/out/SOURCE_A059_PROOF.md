# Density logarithms are charged to mean variance, once

Rung: analytic proof; author validation and independent review are separate. Full FEI is OPEN. Entropy is in bits.

## 1. A wrapper transfer for any Boolean internal function

Let F=K0(Z)+C(Z)g(W), with disjoint finite uniform cubes Z,W. C is an indicator of mean 0<c<=1; K0 is zero on C and a sign off C. The internal g is ANY Boolean sign. At a physical internal coordinate i put t=Inf_i(g), mu=E g and beta=ghat({i}). Define Phi(a,b)=-a log2 a-b log2 b+(a+b)log2(a+b). Pairing the physical Fourier coefficients gives the EXACT identity

 B_i(F)=c B_i(g)-c Phi(mu^2,beta^2)
          +sum_s Phi((K0hat(s)+mu Chat(s))^2,beta^2 Chat(s)^2).       (1)

All nonempty remaining internal frequencies scale by C; ONLY the empty internal pair receives K0. Zero Chat rows contribute zero to the added packet. With P(s)=Chat(s)^2/c and beta nonzero, concavity of ln and Parseval give

 S<=c beta^2/ln2 [1+ln(1+(1-c+c mu^2)/(c beta^2))]
  <=c beta^2 log2(1/c)
       +c/ln2 [(1+ln2)beta^2+2 beta^2 ln(1/|beta|)].              (2)

For the first inequality use Phi(a,b)<=b[1+ln(1+a/b)]/ln2 and
sum_s(K0hat+mu Chat)^2=1-c+c mu^2, because K0 C=0 physically. Omitting zero-Chat rows only decreases this norm. For the second, 1-c+c mu^2<=1 and 0<c<=1 imply 1+1/(c beta^2)<=(1+1/beta^2)/c. Then 1+1/beta^2<=2/beta^2, since |beta|<=1.

The Boolean derivative is in {0,+1,-1}; hence |beta|=|E derivative_i g|<=t. Consequently beta^2<=t and beta^2 ln(1/|beta|)<=|beta|/exp(1)<=t/exp(1). Dropping the NONNEGATIVE subtracted packet in(1), and adding physical JS_i(F)<=2ct/ln2, proves the general transfer

 D_i H(F)<=c B_i(g)+c beta^2 log2(1/c)+A ct,
 A=1+(3+2/exp(1))/ln2<7.                                      (3)

At beta=0 the added packet and density tax are zero, directly, without logarithms at zero. The inequalities remain valid at c=1 and t=0. The c=0 wrapper is independent of W and has zero bill, defined separately. No lower bound on c is assumed; no independence of K0 and C is assumed. Booleanity is used precisely at |beta|<=t; arbitrary real internal vectors are excluded.

## 2. Fine private-priority controller consequence

For a private priority list g with disjoint point-test and fine-core blocks, the prior A059 last-frequency argument gives

 B_i(g)-kappa_i(g)<=K_B t, K_B=6+(3+ln10)/ln2<14

at every unfinished controller query after compatible actual restrictions. The original merged fine reserve releases kappa_i(F)=c kappa_i(g): eta(c p)=c eta(p)+p eta(c), and the second term has zero controller drift. Thus(3) implies

 D_i H(F)-kappa_i(F)<=21 ct+c beta_i(g)^2 log2(1/c).             (4)

The constants are rationally certified: ln2>2/3, ln10<7/3 and 2/exp(1)<1 give K_B<14 and A<7. The old frequent-wrapper rate<21 is unchanged. The new density term involves beta^2 rather than t. The stronger old all-c base20 can still be used where useful; no claim of improving that base constant is made.

On EVERY finite adaptive physical restriction tree of g, with arbitrary stopping and data/control interleaving,

 sum_v w_v beta_{i_v}(g_v)^2=Var(g)-E Var(g_leaf)<=1.           (5)

This is exact: child means are mu+beta and mu-beta, so Var(g)-E_child Var(g_child)=beta^2. Every term is nonnegative. A subset of queried controller nodes has a bill no larger than this whole sum. Consequently, at a FIXED exterior wrapper, the ENTIRE descendant density surcharge is at most c log2(1/c)Var(g), independent of spent controller influence and depth. This is a mean-variance reserve with literal residual c log2(1/c)Var(g_leaf), not an independently renewed local allowance. Formula(3) and(5) apply to arbitrary g; only the baseline K_B in(4) requires the private-priority structure.

## 3. One source account pays all descendant density costs

Use A057's actual nonflat source: even m>=4, c=2^-m, paired-quadratic bent b with b(0)=1 and E b=sqrt(c), C=1_{x=0}, and

 W_0=g, W_1=b-C+Cg, a=(1+c)/2.

The actual source bit X has d_X=[1-c-mu(sqrt(c)-c)]/2>=3/8. For ANY Boolean physical split, 0<=D_X<=2 since erasure and JS are each at most1. Book this actual D_X from the SAME source account6d_X. Allocate to the rare child the variance reserve Z_1=cm Var(g), with Z_0=0. Its ROOT-weighted cost is at most cm/2<=1/8. Therefore

 D_X+E_child Z <=17/8 <=(17/3)d_X,
 6d_X-D_X-E_child Z >=d_X/3.                                (6)

This funds ALL later density charges by(5), with no assumption that spent controller influence<=1 and without increasing a descendant controller rate by m. The old A057 source-only obstruction concerns the larger surrogate tax (mc/2)sum w Inf_i(g_v); it remains a valid counterexample to THAT surrogate. It does not refute the smaller exact sufficient tax derived here. In particular its constant-core tribes family, whose controller influence diverges, still has total new tax at most1/8 at m=4. Base21 controller costs, signed DATA costs and inherited core entropy remain separate and explicitly retained.

For the complete all-history ledger, take actual fine U,R and the SAME incoming internal ticket Q=a[21 I_ctrl(g)+5 I_data(g)] while X is hidden. It is the unspent remainder of the original ticket after prior debits. Let source S=6 Inf_X(W). If X is exposed, use Q_0=21 I_ctrl(g)+5 I_data(g), Q_1=c[21 I_ctrl(g)+5 I_data(g)], and S_0=0, S_1=cm Var(g). The Q expectation is exactly Q_parent; no new capacity is assigned. At this exposure U is harmonic, R has nonnegative release, and(6) pays D_X plus the assigned S from the old6d_X. While X is hidden its influence is harmonic under any other internal physical query, so S has zero expected drift. On the rare branch S drops by cm beta^2 and pays(4)'s density term; after X=0 no density term is needed. Q block influences drop by the queried block's actual influence and are harmonic under all other queries. DATA uses the previously accepted signed fine-profile price3/ln2<5; extra variance release is not counted twice. Exterior bent variables remain unqueried.

It follows, for EVERY finite adaptive internal query history, optional X exposure at any stopping frontier, and arbitrary subsequent internal history, that

 H_root<=U_root+R_root+Q_root+S_root
                  +E[H_leaf-U_leaf-R_leaf-Q_leaf-S_leaf].     (7)

Both actual children, all prior booked debits, and residual variance/source tickets appear literally. Arbitrary inherited nonflat g is allowed as far as(3),(5),(6) go; to use the fine-controller baseline in(7), g must have the specified private point-priority representation and disjoint fine cores.

An explicit growing-depth family sets g_r to the OR of 2^r independent r-bit point events, outputs +/-1, and all fine cores/default constants. Then I(g_r)=2r(1-2^-r)^(2^r-1)>2r/3, so no bounded controller-influence premise is possible. Still(5),(6) fund the entire new surcharge from the SAME source6d_X for every r, with arbitrary adaptive continuations and original U=R=0. No enormous table is enumerated; this all-r claim follows from the exact variance identity.

## 4. First unpaid line

An actual exterior bent-data query changes C,K0 and c. Then the old reserve c log2(1/c)Var(g) need not have the same scale in both children. A dimension-independent payment of that scale/profile conversion after old internal debits, from the SAME remaining source ticket with both terminals, is not proved. Generic initial core entropy and exterior bent terminal entropy also remain unpaid. Full FEI is OPEN. Independent review is required for the new transfer and the stopped assembly.
