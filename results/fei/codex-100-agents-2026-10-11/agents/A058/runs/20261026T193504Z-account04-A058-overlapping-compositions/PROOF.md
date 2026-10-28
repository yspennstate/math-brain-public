# Original slack pays a selector outside the v9 surplus criterion

All cubes are finite and uniform; all spectral entropies use bits. This extends the existing A058 ledger, with independent review pending. Full FEI remains open.

## Statement and original owner

Let A,B be arbitrary Boolean functions of the SAME data coordinates, delta=Pr(A!=B), and E=I(AB). Let s be any balanced Boolean selector phase on independent coordinates, and let t be a fresh fair bit. Define F to choose A when t=1 and s=-1, and B otherwise. Put

    K=H(A)/4+3H(B)/4,  D=H(F)-K,
    B0=4 Inf_t(F)+I(F_t+ F_t-)=E/2+delta[2+I(s)].

The identity for B0 follows from Inf_t(F)=delta/2 and I(F_t+ F_t-)=E/2+delta I(s). No inner source is supplied later.

For every such s satisfying H(s)<=6[I(s)-1]+7/5,

    0<=D<=3B0-9E/8-3delta/5.                       (1)

At delta>0 the upper bound is strict with the estimates below. Both complete inherited core entropies remain in K. This is a universal-over-cores assertion, conditional only on the displayed selector bound. Section 4 gives an explicit actual Boolean selector OUTSIDE v9's criterion, for which the new hypothesis is certified exactly.

## 1. Coherent posterior and the tax

For a general indicator a with probability alpha, write u=Ahat(T), b=Bhat(T), d=u-b, R=alpha u^2+(1-alpha)b^2, v=alpha(1-alpha)d^2/R on a nonzero data row. The selector-empty amplitude is b+alpha d; each nonempty selector amplitude is ahat(U)d. Thus the row marginal is R, and conditional nonempty-selector probability is v. With q(U)=ahat(U)^2/[alpha(1-alpha)],

    H(B+a(A-B))-[alpha H(A)+(1-alpha)H(B)]
      =sum_T R h(v)+4alpha(1-alpha)delta H(q)
       +sum_T {alpha u^2 log2(u^2/R)+(1-alpha)b^2 log2(b^2/R)}.       (2)

All terms are nonnegative: the final bracket is the convexity gap of x log x. Rows with R=0 contribute zero. This accounts for signed coherent addition at the empty selector sector; no disjoint-core rule is used. Formula (2) also proves nonnegative D for every actual restricted selector probability, including endpoints by direct substitution.

Let Dflat be the overhead of a two-bit point selector, with the SAME A,B. For a=1_(t=1,s=-1), the empty coefficient and total nonempty mass agree with the point selector. The nonempty entropy tax is exactly

    D=Dflat+delta H(s)/2.                           (3)

Indeed the balanced event indicator (1-s)/2 has nonempty squared coefficients shat(U)^2/4 and zero empty s coefficient. Adding t halves the selector-phase entropy excess relative to the two-bit point phase. Equivalently substitute these coefficients into (2). This is the v9 exact tax specialized to a balanced child.

## 2. Recovering unused ORIGINAL flat slack

For alpha=1/4, the nonempty-selector law of the flat point is uniform on three labels. Put V=3delta/4. Concavity in (2) gives

    Dflat<=h(V)+V log2(3)+sum_T J_(1/4)(u,b).

Entropy tensorization for the input indicator 1_(A!=B) gives delta log2(1/delta)<=E/2. Its one-bit conditional entropy is 1/2 on each mixed fiber and zero otherwise. This inequality uses physical Booleanity, not FEI. At delta=0 all quantities vanish.

Using h(x)<=x log2(1/x)+x/ln2, log2(4/3)<1/2, log2(3)<8/5 and 1/ln2<3/2,

    h(V)<=3E/8+3delta/2,
    V log2(3)<=6delta/5.

The first logarithm bound follows from (4/3)^2<2; the second from 3^5<2^8. For the third, ln2=2 atanh(1/3)>2/3.

The v8 rowwise Taylor inequality is

    J_alpha(u,b)<=alpha[log2(1/alpha)+2/ln2](u-b)^2.

For completeness, scale b to1, differentiate the natural-log gap phi twice: phi''(x)=2alpha ln(x^2/r)+4alpha(1-alpha)/r <=2alpha ln(1/alpha)+4alpha. Here r=alpha x^2+1-alpha>0. Taylor around x=1, where phi=phi'=0, proves the bound on either side; the logarithmic singularity at zero is integrable. At b=0 use continuity. Parseval gives sum_T(u-b)^2=4delta. Therefore

    sum_T J_(1/4)(u,b)<=5delta,
    Dflat<=3E/8+77delta/10.                         (4)

Since 3B0=3E/2+9delta+3delta[I(s)-1], (3)-(4) imply the more general actual-surplus estimate

    3B0-D >=9E/8+delta{13/10-[H(s)-6(I(s)-1)]/2}.  (5)

This proves (1). The v9 criterion required H(s)<=6(I(s)-1); (5) uses the already present flat slack instead. No budget is renewed, and no positive old debit is removed.

## 3. Physical stopping trees and the old debit

At every actual adaptive physical restriction v define K_v=alpha_v H(A_v)+(1-alpha_v)H(B_v) and D_v=H(F_v)-K_v. Equation (2) ensures D_v>=0. At a selector query the expected K does not change; at a data query retain its signed inherited-core difference Delta K exactly. For any finite adaptive selector/data stopping tree the signed coherent debit is

    sum_v w_v[Delta H_v-Delta K_v]=D_root-sum_leaves w_leaf D_leaf.

Consequently the expected remaining ORIGINAL cash after any prefix equals

    3B0-D_root+sum_live w_v D_v
       >=9E/8+3delta/5+sum_live w_v D_v.

Both complete actual terminal entropies and all inherited data-core entropy differences remain; this does not price arbitrary core FEI. Individual path costs need not be bounded: the assertion is about reach-weighted signed payment.

There is an actual earlier positive debit. Take A=1,B=x on one data bit, so E=1 and delta=1/2. Revealing t first costs

    Droot-Dchild/2=3-(9/8)log2(3)>0.

The child tax cancels in this decrement by (3). The nonflat surviving child then has its FULL overhead paid from the remaining original account. Both final core entropies are zero in this control; the theorem itself allows arbitrary nonzero inherited core entropies.

## 4. Explicit certified selector violating the old criterion

Let b0 on three bits be1 on integer vertices0,1,2,3,4 and0 otherwise. On disjoint copies define b_(d+1)=1-b_d^(left)b_d^(right), and g_d=1-2b_d. Let g=g12 (12288 coordinates), and s=x0*g with one independent sign x0. This balanced selector has H(s)=H(g), I(s)=1+I(g). Thus its old surplus criterion is exactly H(g)<=6I(g).

The following exact recurrences define a short certificate, without a truth table of dimension12288. Write p=Pr(b_d=1), v=4p(1-p), m=1-2p^2; let Ent4 be entropy of the FOUR displayed masses. Then

    p_next=1-p^2, I_next=2p I,
    H_next=Ent4(m^2,p^2v,p^2v,v^2/4)+2p[H-h((1-2p)^2)].          (6)

To derive this, expand the NAND output in the centered normalized child basis. The empty squared mass is m^2; the two single-child masses are p^2v, and the double-child mass is v^2/4. Conditional on a child being spectrally active its normalized nonempty entropy is [H-h((1-2p)^2)]/v. The expected number of active children is 2pv, proving (6); physical edges independently give I_next=2pI. All iterates have0<p<1; constant endpoints are checked separately in code.

code/certify.py uses exact rational p,I and outward integer logarithm intervals. It certifies

    139/100 < H(g)-6I(g) < 7/5.

Numerically H(g)=88.806551131716..., I(g)=14.568587054702..., excess=1.395028803502.... The decimals are explanatory only. Thus the old criterion fails strictly, while (1) pays the actual necessary child for EVERY A,B from the SAME original account, leaving at least9E/8+3delta/5. This is a concrete enlargement, not an assumed FEI bound for arbitrary selectors.

## 5. What remains unpaid

The sufficient criterion cannot hold universally. More strongly, the actual original price3 itself FAILS for an explicit Boolean continuation. Let g^[m] be the product of m independent copies of the certified g, and s_m=x0*g^[m]. Keep A=1,B=x, E=1,delta=1/2. Exact tensor additivity and (3) give

    B0(m)=2+m I(g)/2,
    Droot(m)=4-(9/8)log2(3)+m H(g)/4,
    Droot(m)-3B0(m)=m[H(g)-6I(g)]/4-2-(9/8)log2(3).           (7)

For m=11 this is >11*139/400-19/5=9/400>0, using log2(3)<8/5. For1<=m<=10 it is <10*(7/5)/4-2-(9/8)*(4/3)=0, using log2(3)>4/3 (27>16). Thus the first failure among these integer tensor repetitions is EXACTLY m=11. The actual Boolean F has135171 nominal coordinates (11*12288 for g copies, one balancing bit, one outer selector, one data bit). The old first debit is still3-(9/8)log2(3)>0. Therefore the reached nonflat child really exceeds the diminished original account, even with both core entropies zero. The counterexample is to this source price, not to FEI. At m=1 the previous theorem certifies payment for all A,B, beyond v9's old criterion.

Finally let P(K) mean Droot<=K B0 for ALL balanced Boolean s and ALL shared cores A,B. If P(K) holds, substitute s=x0*product_(j=1)^m g_j with independent copies of an ARBITRARY Boolean g into (7)'s untuned formulas and divide by m, then let m tend to infinity. This gives H(g)<=2K I(g) (constants g are immediate). Conversely FEI(C) bounds H(s)<=C I(s). Balanced s has I(s)>=1 by Parseval, so Bflat=E/2+3delta<=B0 and delta I(s)<=B0. The v8 Dflat<=3Bflat and (3) yield P(3+C/2). Thus existence of any universal finite price for this arbitrary-selector ticket is FEI-equivalent, with explicit constant conversion. This is a route boundary, not a new route to a full proof.

NEXT must change the source mechanism or exploit necessary selected profiles instead of asserting universal price3 or universal fixed-additive surplus. The exact first unpaid line is a noncircular INITIAL payment of the arbitrary selector's tensor-additive entropy tax from unused physical influence. Both arbitrary inherited core entropy bills also remain. Full FEI remains OPEN.
