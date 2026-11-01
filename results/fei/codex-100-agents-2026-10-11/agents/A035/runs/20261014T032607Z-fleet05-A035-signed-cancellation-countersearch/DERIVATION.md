# A signed count trace retains the whole conditional-edge refund

The cube uses binary bits and characters (-1)^(S dot x); functions take signs +/-1. All logarithms, entropy and KL divergence are in bits. We distinguish oriented erasure Lambda_i from sector mutual information M_i used in the previous A035 run.

## 1. Fixed structural family, actual histories, complete references

Resume the previous point-surgery family, not an arbitrary chosen spectral vector. For even m>=2, L>=1 and a core point y*, let b_m(y)=(-1)^(sum y_(2k)y_(2k+1)), a(y)=(-1)^|y|(1-2 1_{y=y*}), p=(1-a)/2, and pi=E p=1/2+(-1)^|y*|2^-m. On independent four-bit blocks x_j and selectors z_j,

    f=b_m(y) product b_4(x_j) (-1)^(p(y) sum 1_{x_j=0} z_j).

Set c_+=b_m 1_{p=0}, c_-=b_m 1_{p=1}, G=product b_4 and T=product h_j, h_j=b_4(x_j)(-1)^(1_{x_j=0}z_j). Then f=c_+G+c_-T is Boolean. All mixed signed convolutions follow by transforming f^2=1; no unsigned spectrum is substituted. Restrict any subset of selectors and choose one remaining selector i. No core/data variable is exposed. Let F be the number of OTHER free selectors, J the number of fixed selectors with value one; selectors fixed at zero disappear from the trace.

For retained row R define alpha=hat f(R), beta=hat f(R+i), d=Inf_i=pi/16,

    mu(R)=beta^2/d, r(R)=alpha^2+beta^2,
    Lambda_i=sum_R beta^2 log2(r(R)/beta^2)
            =d[log2(1/d)-D(mu||r)].                  (1)

Both mu and r are complete probability laws. All derivative rows are nonzero by the previous stage's full-carrier proof; we do not renormalize a support event or omit reference mass. The desired universal payment is for the remaining oriented-erasure sum, not just the existence of normalized laws.

## 2. A physically specified trace with polynomial state count

For a core frequency Y put ell=hat c_-(Y)/hat b_m(Y). The bent coefficient is +/-2^(-m/2), and point surgery changes each old c_- coefficient by a signed 2^-m. Therefore

    ell=B+sigma delta, B in {0,1}, sigma in {+1,-1}, delta=2^(-m/2). (2)

Here B is membership in the old translated-bent branch row and sigma is the product of the point character, the physical point/bent signs, and the bent frequency sign. These signs are fixed by the actual quadratic/character expansion, not selected from the likelihood ratio. Thus at most four core types suffice, with exact multiplicities N_ell. We may record ell instead of (B,sigma) because m is known and duplicates can be merged.

The queried four-bit bent Fourier sign epsilon is +/-1, occurring at 10 or 6 frequencies respectively. Let O be the event that some OTHER free selector has spectral sector one. Define trace C as follows:

    O=1: C=(O,epsilon).
    O=0: C=(O,ell,epsilon,A,B1),

where A counts positive bent signs among the F other free modules and B1 counts positive bent signs among the J fixed-one modules. This is a physical factor/sign statistic, with at most

    2+8(F+1)(J+1)                                    (3)

states, independent of m and of the number of row addresses. Repeated identical physical modules permit exact signed count compression; this is not a universal representation theorem.

When O=0, every other free module contributes the signed amplitude ratio 3/4 or5/4 (according to bent sign), every fixed-one module contributes 1/2 or3/2, and every fixed-zero module contributes1. Put

    w=(3/4)^A(5/4)^(F-A)(1/2)^B1(3/2)^(J-B1),
    U=(1-ell)+ell w(1-epsilon/4), V=ell w epsilon/4.

The actual adjacent Fourier amplitudes are a COMMON signed bent amplitude times U,V. Hence

    mu(R)/r(R)=V^2/[d(U^2+V^2)].                     (4)

For O=1 the G term vanishes at both adjacent rows and only T survives. Then

    mu(R)/r(R)=1/[d(1+(4epsilon-1)^2)],               (5)

namely 1/(10d) or1/(26d). Equations (4)-(5) prove the likelihood ratio is constant inside each physical trace fiber. Signed interference remains inside U, including negative ell and cancellations in U; we never replace U by the sum of absolute summands.

## 3. Exact coarse laws and normalization

Let n_+=10,n_-=6. For O=0, the base spectral bent mass of a trace state is

    W_C=(N_ell/2^m)(n_epsilon/16)
        binom(F,A)(10/16)^A(6/16)^(F-A)
        binom(J,B1)(10/16)^B1(6/16)^(J-B1).

Its COMPLETE laws are

    mu_C=W_C V^2/d, r_C=W_C(U^2+V^2).                (6)

Write t=1-(15/16)^F. For O=1 and queried sign epsilon,

    mu_C=t n_epsilon/16,
    r_C=pi t (n_epsilon/16)[(1-epsilon/4)^2+1/16].   (7)

These formulas include all reference mass. A direct normalization proof uses physical orthogonality c_+c_-=0:

    E_core ell^2=pi,
    E_core (1-ell)^2=1-pi,
    E_core ell(1-ell)=0.

Under the bent base mass, E epsilon=1/4, E(1-epsilon/4)^2=15/16, and E(1-epsilon/2)^2=1. Therefore E w^2=(15/16)^F regardless of J. The O=0 derivative mass is (15/16)^F, while its reference mass is 1-pi+pi(15/16)^F; (7) supplies exactly the complementary masses t and pi t. Thus both coarse laws sum to1 for EVERY finite parameter, not just those enumerated.

By the KL chain rule and (4)-(5),

    D(mu||r)=D(mu_C||r_C),
    Lambda_i=d[log2(1/d)-D(mu_C||r_C)].               (8)

The probability identity is generic; the nontrivial family-specific statement is that this independently specified polynomial-size signed trace satisfies it. This does not imply that the remaining price is universally influence-paid. Even a normalized real product law can have a lossless simple statistic and a large Lambda/I; A031's Bernoulli(1/64) real control has Lambda/I=6. No new Boolean-specific inequality is claimed from compression alone.

## 4. Count deletion loses genuine conditional KL

Consider the constant-size trace C0 obtained by dropping A,B1 but retaining O,ell,epsilon. Its correct ledger is

    D(mu||r)=D(mu_C0||r_C0)
             +E_(mu_C0) D(mu_(A,B1|C0)||r_(A,B1|C0)). (9)

The second term is nonnegative and cannot be set to zero without a sufficiency proof. Our actual twelve-bit witness m=2,L=2,y*=1, first selector queried, has d=1/64. Two retained rows in the SAME C0 fiber have core ratio ell=1/2, queried bent sign +1 and O=0. With the other bent sign positive, A=1 and w=3/4, giving U=25/32,V=3/32. With that sign negative, A=0 and w=5/4, giving U=31/32,V=5/32. Thus their exact likelihood ratios are

    288/317 and 800/493,                              (10)

which are different. Both derivative probabilities are positive, so strictness of the KL chain-rule equality condition proves a STRICT conditional debt. Independent direct complete-root character sums produce signed Walsh pairs (100,12) and (-124,-20), verifying (10) without using the count formula. The second common bent sign is negative; both signs are retained until the probability squares.

Exact rational log intervals from the full signed spectrum certify the total omitted divergence is in [0.126000433969,0.126000433970] bits. Thus the count-deleted oriented price overcharges by d times this quantity; the error is a lost refund, not an FEI counterexample. After the first selector is physically fixed to one, the analogous omitted fixed-one-sign count loses [0.495464588559,0.495464588560] bits in that child's normalized row divergence. Its true physical reach is1/2. Fixed-zero histories have no such count debt when no other free selector remains. Counts cannot be dropped merely because derivative influence, boundary bill and carrier mass remain unchanged.

## 5. One physical influence normalizer, spectators and terminals

For a nonconstant actual source node let I=sum_i d_i. For selector coordinates use C_i above; for other coordinates retain the full row label as a placeholder for their unpaid conditional reference. Define complete joint laws

    P(i,c)=(d_i/I)mu_(C_i)(c),
    Q(i,c)=(d_i/I)r_(C_i)(c).

Both laws have total1 and the same physical coordinate marginal d_i/I, so

    I D(P||Q)=sum_i d_i D(mu_i||r_i),
    sum_i Lambda_i=sum_i d_i log2(1/d_i)-I D(P||Q).   (11)

Selector compression changes neither side of (11); it spends no additional whole I per state or count. The full rows on other coordinates explicitly mark the unclosed part, not a free universal code. At physical histories, the entire node expression must be weighted by that history's actual reach; in particular the fixed-one child's debt mentioned above is multiplied by1/2.

Tensoring ANY genuine Boolean terminal spectator on fresh variables tensors each OLD selector's mu and r with the SAME normalized spectator spectrum. The trace can ignore that spectator, (8) stays exact, and its entropy and influence remain additive in the full source/terminal ledger. No conditional product-law admission or dummy-coordinate loophole is used.

After core and selectors are fixed, the terminal data blocks are b_4 or its one-point flip. With H*=6-(27/16)log2(3), the true physically averaged terminal costs remain

    I_terminal=L[2+pi/4],
    H_terminal=L[4+(pi/2)(H*-4)].                    (12)

A spectator adds I(g),H(g) to the terminal ledger, even though it disappears from OLD row likelihood ratios. Equation (12), proved in the previous A035 stage, is not paid or removed by sufficient-statistic compression. The elementary family guard H<=4I is credited to that stage and merely rules out falsely reporting this diagnostic as an unbounded FEI family.

## 6. Honest unsupported line and next mechanism

This stage proves lossless structural compression for coherently overlapping shared-phase modules, and exactly identifies a count-deletion failure. It does not settle C018. The first unsupported universal line is an influence payment of the remaining conditional log price for arbitrary overlapping signed derivative factors and arbitrary terminal cores, with one complete reference. For the present family, repeated equal-width factors allow the counts A,B1 and a polynomial state bound; arbitrary unequal factors can force a substantially larger collision trace. NEXT should test the same count/likelihood criterion on three pairwise-overlapping conjunctions with no common activation block, as A031 requests, or on one unequal module splice if that fixture is already being worked. Preserve the conditional KL in (9), both terminals and the coordinate weights in (11); do not convert the state count to a paid code-length bound.
