# A069 stage9: private payment before core exposure

Full FEI is OPEN. The new pre-exposure/interleaving theorem is an author proof with exact certificates recorded separately, awaiting independent review. The distinct A070 literal-completion claim is independently reviewed without changing its scope.

## 1. Independent review of the supplied literal completion

A070-LITERAL-ONLY-COMPLETION-SAME-BANK@1 starts AFTER the full core exposure and u/private stopping history of A069-INHERITED-PRIVATE-STOPPING-WITHOUT-NEW-BANK@1. That source claim was independently accepted unchanged by A070. Its post-u reference has A=(1+3td)/4, B=5(1-td)/16 and r=7(1-td)/[32(2^m-1)], with d=0 or1 and t=2^-2m. At a private exit k, the inherited masses are A_k=A+(2^k-1)r, B_k=B+(2^k-1)r, tail atom r_k=2^k r. These are FULL normalized frequency marginals, including constant physical outputs.

Run private queries to first1 or exhaustion. At first1 the output is constant for d0 and a c literal for d1; at all-zero exhaustion those roles reverse. Query c only at actual literal leaves. Its influence is1, and BOTH full constant children have inherited vacuum mass A_k+B_k. Therefore

    Delta C_c=log2[(A_k+B_k)/B_k]=log2(1+A_k/B_k).

The original ratio is4/5 at d0 and4(1+3t)/[5(1-t)]<=28/15 at d1, since0<t<=1/4. Adding the same nonnegative quantity to numerator and denominator moves the ratio toward1, proving0<A_k/B_k<=28/15 at every such literal. Thus Delta C_c<=log2(43/15)<2<4Inf_c. No positive-part debit is added. Already constant children are stopped, without discarding their CE. Every final constant terminal has CE<=2: an early constant has vacuum mass A_k>=1/4; after a literal query the vacuum mass is A_k+B_k>=9/16. These bills need not vanish.

Consequently the exact nine-bit source's SAME original5/8 expected-tree earmark retains>59/2560, with all old<3/5+1/512 bookings and every terminal cost retained. The arbitrary-core statement is conditional on the same supplied reference and already paid preceding account. This reconstructs ALL parts of A070's unchanged claim, not a repaired or broadened version. It does not independently self-review A069's source theorem; A070 already supplied that source review receipt.

## 2. New target: freeze the flag and leave arbitrary cores unresolved

Let a,b be ANY Boolean functions on a finite uniform core cube Y, with no dimension, monotonicity, Fourier flatness, source-influence bound or core-complexity restriction. Put

    p=(a+b)/2, q=(a-b)/2,
    p*q=0, p^2+q^2=1 pointwise.                         (1)

Let epsilon be either physical u outcome's sign and define on disjoint c,Z

    f=q2(epsilon*p+chi_c*q),
    chi_c=(-1)^c, q2=-1 iff c=0 and Z=0, |Z|=m>=1.     (2)

This is an ACTUAL Boolean function: at each Y exactly one of p,q is nonzero, with value+/-1. It is precisely the paired-core function after u is physically queried, up to irrelevant global signs. We do not claim a universal payment for that u query before core exposure.

Supply ANY positive normalized core reference R. Independently of the current disagreement density, choose and FREEZE theta in[0,1] ONCE. With N=2^m, t=N^-2, supply the complete post-u reference

    Q=R x Q_theta,
    Q_theta(empty)=A=(1+3t theta)/4,
    Q_theta({c})=B=5(1-t theta)/16,
    Q_theta(S)=r=7(1-t theta)/[32(N-1)] otherwise.       (3)

It is positive and normalized, because A+B+2(N-1)r=1. If this is admitted as the marginal of a previously paid five-cell reference, that admission and all old debits stay explicit hypotheses. For other theta, (3) is simply a supplied post-u reference; we assert no free change from a different earlier reference or from its flag. Crucially theta NEVER changes after subsequent core queries, even when the actual disagreement density does.

Consider any finite physical tree interleaving fresh CORE coordinates and fresh PRIVATE coordinates, while c is unqueried. Stop querying private coordinates on a branch at its first private1, or earlier. Core queries may continue on that branch. Carry Q only by direct frequency marginalization, with no vacuum calibration, occupancy reset, profile reset or new normalizer. Selection depends only on actual physical history. All actual child bills remain.

## 3. Booleanity yields the control marginal, not spectral independence

At any node eligible for a private query, its previously queried private outcomes are all0. The restricted a,b are still Boolean on the remaining core cube. Let k be the number of private queries already made, h=2^k, M=N/h, eta=1/M, and let

    d=Pr(a!=b | current physical core restriction).

Then E p^2=1-d, E q^2=d, and E pq=0 by(1), at EVERY such physical restriction. The inherited reference is still a product of the marginalized original R and

    A_k=A+(h-1)r, B_k=B+(h-1)r, r_k=hr.                (4)

Directly Fourier-transforming (2) in c and the remaining Z gives the following core-valued coefficients:

    empty control: epsilon*(1-eta)*p-eta*q,
    {c}:          -epsilon*eta*p+(1-eta)*q,
    each other control frequency: -eta*(epsilon*p+q).

Square and sum over ALL remaining core frequencies, using Parseval and(1). The actual control-marginal squared spectrum is

    P0=(1-d)(1-eta)^2+d eta^2,
    P1=d(1-eta)^2+(1-d)eta^2,
    eta^2 at each of the2(M-1) other atoms.              (5)

Thus P0+P1=1-2eta+2eta^2 independent of d. This is a marginal calculation; the JOINT Fourier law need not factor between core and controls. In particular the vanishing cross term is the sum E pq at the actual physical node, not a rowwise assumption about products of individual Fourier coefficients.

The physical influence of any remaining private coordinate is exactly eta. On c=0 with every OTHER remaining private bit0, changing that coordinate flips q2 and hence the nonzero Boolean output; this event has probability(1/2)*2^-(log2 M-1)=eta, independently of the current core. Other inputs give no change.

## 4. Complete reference payment, uniform in current d and frozen theta

For a private query, the supplied core reference factor is unchanged, so it cancels in the reference likelihood R_Y(T)Q_theta(S) divided by its frequency marginal. This does NOT remove its full contribution from either child CE. Partial Parseval for the two physical children then gives EXACTLY

    Delta C = P0 log2(1+r_k/A_k)+P1 log2(1+r_k/B_k)
             +eta^2 log2[(1+A_k/r_k)(1+B_k/r_k)]
             +2(M-2)eta^2.                              (6)

This is C_parent-mean C_child with both complete child references; it is valid even when the actual joint spectrum is correlated.

The same hereditary reference corridor holds for EVERY frozen theta in[0,1]:

    L=8(M-1)/7 <= A_k/r_k,B_k/r_k <= U=1+10M/7.       (7)

Indeed B/r=10(N-1)/7 is independent of theta; A/r=8(N-1)(1+3t theta)/[7(1-t theta)] increases with theta, so it lies between its theta0 and theta1 endpoints. The endpoint ratios were proved algebraically in the independently accepted private-tree theorem, and are reproduced here: theta0 A/r=8(N-1)/7; theta1 A/r=8(1+3rho^2)/[7rho(1+rho)]. For0<rho<=1/2,

    1-rho <= (1+3rho^2)/(1+rho) <=5/4,

because the lower inequality reduces to4rho^2>=0, and12rho^2-5rho-1<=rho-1<0 proves the upper. Marginalization sends each ratio x to1+(x-1)/h. These facts imply(7) for all initial m and prefix k. No finite grid in theta proves this continuum assertion; the monotonicity does.

Since P0+P1=1-2eta+2eta^2, (6)-(7) give exactly the old rectangle majorant

    V_l=(1-2eta+2eta^2)log2(1+1/L)
         +2eta^2 log2(1+U)+2(M-2)eta^2, l=log2 M.

For l1,2,3 its strict bound V_l<4eta is independently rational-log certified. For l>=4, use ln2>2/3,1+U<=2/eta,2l/2^l<=1/2, and eta^2/(1-eta)<=1/240 to obtain

    V_l/eta <53/16+(2l-53/16)eta
                       +(21/16)eta^2/(1-eta)
              <=4887/1280<4.                             (8)

This proves Delta C<4Inf_private for every eligible private query BEFORE core exposure and after ANY interleaving of core restrictions, uniformly in the two DIFFERENT parameters actual d and frozen theta. The core reference may be arbitrary and nonflat. There is no newly calibrated flag or gate budget at a child.

## 5. What is and is not paid in an interleaved tree

Every private positive excess(Delta C-4Inf)_+ is exactly0. Consequently, for any such physical tree, its entire expected positive-excess sum equals the sum over its CORE queries alone. All old bookings and full terminal bills remain. If an admitted original ledger independently funds those ACTUAL core-query excesses, the private steps consume no additional capacity from that SAME owner. No negative private excess is deposited as a renewed bank.

This theorem does NOT re-use the nine-bit account's old<3/5 core invoice after changing its query order or references. Core invoices must be recomputed for the actual interleaved history. It does not assert that a previously paid u query can be moved before exposure for free. It supplies a previously missing BEFORE-exposure local payment, not the universal paid common source or arbitrary cumulative core selection.

## 6. A nonconstant-core obstruction at the very next control query

The private proof must not be mistaken for payment of any next control. Take a=b=chi_y on one still-unqueried core bit, m2, frozen theta0, epsilon=1, and after a first private outcome1. The actual remaining Boolean output is chi_y, so querying c has influence0 and BOTH physical c children remain nonconstant with influence1 on y. The inherited control masses are

    A_1=31/96, B_1=37/96, remaining tail atom r_1=14/96.

The complete c-query decrement, with any supplied positive core reference retained, is

    Delta C_c=log2[(A_1+B_1)/A_1]=log2(68/31)>1.      (9)

Both full child CEs remain in this exact identity. Thus the tempting extension that every remaining control is locally influence-paid BEFORE core exposure is FALSE even for a one-bit nonconstant Boolean core and two nonconstant physical children. It is not an FEI counterexample or a refutation of A070's LITERAL-ONLY policy: this output is a y literal, not a c literal.

More generally at a first1 exit with unresolved core disagreement d, the actual control spectrum has masses1-d,d at empty/{c}, and its complete c-excess is

    (1-d)log2(1+B_k/A_k)+d log2(1+A_k/B_k)-4d.

At d0 the positive reference-only label cost survives while physical c influence vanishes. This identifies exactly where a source-profile conversion or different selection, funded from old unused surplus, is required.

## 7. Honest universal bridge

The indispensable Boolean facts are pointwise unit norms and pq=0 at every physical restriction. Mere root L2 normalization does not supply these after restriction; the earlier real pair a(y)=(3+4y)/5,b(y)=1 has child paired norms13/25,37/25. An arbitrary normalized subset law or degree-one real control does not meet the hypotheses. The proof uses no spatial arm estimate, exact-support trick or independence of Fourier labels.

The first unsupported universal line is still: construct for arbitrary Boolean cores a justified influence-priced common reference, or a once-owned selection/payment bound for their actual cumulative positive core excess and required profile conversions. What changed here is that the entire private local payment now survives unresolved, nonflat Boolean cores and arbitrary physical core interleaving with a FROZEN reference flag. The early-c cost(9) requires payment or avoidance, not a new universal local estimate. Section8 shows avoidance while retaining an ACTUALLY unchanged core invoice in the specific nine-bit account.

## 8. Exact core-invoice conservation and a stronger SAME-owner continuation

The preceding local result has a stronger conservation corollary. At any core restriction and ANY fixed control/private history, the squared CORE-frequency marginal is exactly(P_a+P_b)/2. Before u, each physical c,u,Z assignment selects a signed a or b equally often. After u the same is true when averaging the still-unqueried c, whether private outcomes have stayed0 or already hit1. Thus its complete core reference cost is always B=(CE(P_a,R)+CE(P_b,R))/2.

The CONTROL marginal is an affine mixture of the two sign types, with mixing weight d. This holds before u, on a continuing zero prefix, and after a first1 (then its only occupied control atoms have masses1-d,d). Therefore for the SAME frozen product reference,

    C_Q=B+L0+(L1-L0)d,                                (10)

where L0,L1 depend only on the fixed reference and control/private history, not the unresolved core. At a physical CORE query both children receive precisely the same frequency-marginal core reference, the SAME control reference and same private history. Actual d_parent is the mean of d_children, so the second term cancels exactly. Also Inf_core(f)=mean(Inf_core(a),Inf_core(b)). Hence

    Delta C_core-4Inf_core(f)=Delta B-4j_core.          (11)

This is an equality of the ACTUAL invoices under changed interleaving; it is not an assumption that an old invoice survives. It would generally fail for recalibrated or arbitrary nonproduct references. Both complete children occur in(10)-(11), including irrelevant core queries and constant core restrictions.

Now return to the nine-bit g2/one-point-edit source and original all-set core reference R. Let d_root=theta=1/512. Start with the original normalized PRE-u five-cell law with its root flag t theta. Query Y0 FIRST, so the original donor Y0=0 is an actual first child at its original weight1/2. Carry the ENTIRE joint reference by direct marginalization, and NEVER update theta at children. Query u next on both children. Then allow ANY adaptive interleaving of Y1,...,Y8 in that relative order with distinct private queries until first1/exhaustion. Continue every core coordinate on every path, even if irrelevant. After both processes finish, query c only at c-literal leaves and stop constant leaves.

First check the owner against this genuinely inherited, uncalibrated flag. On donor Y0=0, actual d_child=1/256, whereas theta remains1/512. Its matched-flag control surplus was proved in stage7 to exceed1-t h2(d_child). The elementary inequality-log2(1-x)<=x/[(1-x)ln2] and1/ln2<3/2 give

    h2(1/256)<(8+3/2)/256=19/512<1/16.

So matched control surplus>63/64. The extra FULL cross entropy from the frozen flag is exactly KL2(Ber(t/256)||Ber(t/512))<t/256<=1/1024: its nonempty term is negative and its empty term is(t/256)log2 2. The previously independently certified CORE surplus at this donor exceeds1/2. Its actual inherited full surplus is therefore>1519/1024, and at original weight1/2 the once-owned donor capacity is

    >1519/2048>5/8.                                    (12)

Earmark the SAME5/8 once before any charge. No revaluation of a spent child, discarded complementary child, flag refresh or terminal refund is used.

Next pay u BEFORE the remaining core exposure. At each of its two actual parents, d is0 or1/256, theta is the SAME1/512, rho=2^-m,t=rho^2. Inf_u=1-d. Write ell=log2(5/4). The two sign-type full decrements are

    U0=(1-rho)^2 log2[(1+3t theta)/(1-t theta)]
                  +(2rho-t)log2 5,
    U1=t log2[(1+3t theta)/(4t theta)]+(1-t)ell.

The actual decrement is(1-d)U0+dU1 by the Boolean mixture, including both physical children. Both U0,U1<13/4 uniformly in m: for U0, the first ratio<2 and(2rho-t)<=3/4 with log2 5<3; for U1, use(1+3t theta)/4<1, t log2(1/t)<=1/2, t log2(1/theta)=9t<=9/4, and ell<1/2. Thus

    Delta C_u<13/4<4*(255/256)<=4Inf_u.                (13)

The root Y0 query and EVERY later core query satisfy(11). The relative core order and all actual outcomes are unchanged. Splitting a fixed core prefix across arbitrary u/private histories only partitions its original reach: since every path eventually queries all cores in that order, the total reach of the next core query at each prefix remains2^-depth. Therefore the cumulative expected POSITIVE core bill is EXACTLY the old independently certified P_core<7/12, not merely a newly assumed ceiling.

All private excesses are negative by Sections3-4, and the final literal-c excesses are negative by the uniform ratio argument of Section1, which also holds for any theta in[0,1]. Already constant leaves are stopped with full inherited CE. There are no other queries. Therefore the ENTIRE adaptive all-width completion has

    total expected positive excess=P_core<7/12,
    SAME original earmark remainder>5/8-7/12=1/24,     (14)

at every chronological expected-history prefix. All final Boolean outputs are constant, and all inherited terminal CEs remain<=2; they are not reset to zero. This improves the old>59/2560 remainder and admits genuinely interleaved private queries while cores remain unresolved. It does not prove a paid invoice for arbitrary core orders or arbitrary core sources. The early-c obstruction(9) is AVOIDED by waiting for actual c literals, not declared free.

The universal next unpaid line is now sharply the common-core positive invoice/selection itself: establish an arbitrary-core analogue of the old finite P_core payment, or a justified source profile/order that makes it payable from one unused original source bank. Private geometry, frozen-flag transport and nonconstant early-u continuation no longer require a new allowance in this account.
