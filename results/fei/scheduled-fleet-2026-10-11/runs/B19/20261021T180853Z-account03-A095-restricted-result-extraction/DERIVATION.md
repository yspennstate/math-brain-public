# A signed profile pays an unbounded-width history at rate four

All information is in bits. Let h_L=1-2 indicator(all L bits zero). Fix ANY integer w>=4, m>=0. On disjoint blocks let g=h_w h_2, k=w+2, n=k+m, delta=2^-n. A fresh fair selector chooses the padded g or its full-point flip at zero; call the resulting Boolean function M. The only changed value on the selector-one branch is g(0)=+1. No claim about arbitrary Boolean source prices is assumed.

Use the SAME A095 support-completed incoming reference Q, with source R=P_g. Its old support consists of all k-bit masks with zero dummy/selector mask. Put N=2^k, W=2delta-N delta^2. Give an old mask T mass (1-W)R(T), and EVERY other mask mass delta^2. This is normalized: there are 2^(n+1)-N new masks. All old source coefficients are nonzero for w>=3. In particular every denominator below is positive, 0<W<1, and no zero true fiber or empty atom is removed.

**Theorem (analytic author proof; independent review pending).** For every such w,m and EVERY finite adaptive restriction tree querying only previously unqueried coordinates of the width-w block, retain Q using the normalized physical-child posterior transport of A095 stage5. Then

    CE_root < 1005/256,
    E I(M_leaf) >= 63/64,
    4 E I(M_leaf) - E CE(P_leaf,Q_leaf) > 3/256.

The policy may stop on any physical branch, use any order, and query the whole width-w block. Selector, padding and width-two block remain untouched. Each leaf keeps its entire prescribed H+KL and both actual child normalizers; there is one original bank and no reference renewal. An independent arbitrary terminal with product reference retains its full additive CE and KL and funds none of these inequalities. Thus this is an all-dimensional supplied-reference history theorem, not a universal FEI theorem or a novelty assertion about FEI on this structural class.

## 1. Exact signed profile

Write q=2^(1-w), b=1-q. The width-w coefficients are b at the empty mask and -q at its other 2^w-1 masks. The width-two coefficients are +1/2 at empty and -1/2 elsewhere. Both signed sums equal -1. Write a_T=hat g(T), ell_T=log2(1/a_T^2), c=sum a_T^2 ell_T. Tensor multiplication gives

    A=sum a_T ell_T=2+2b log2 b+(2-q)(2w-2),
    B=sum ell_T=-8 log2 b+2^(w+3)w-8w+8.

These are signed identities, not inequalities obtained by ignoring phases. The old actual coefficients of M are a_T-delta and every new magnitude is delta. Hence

    CE_root=c-2delta A+delta^2 B
            -(1-W)log2(1-W)+2nW.                 (1)

The equality retains the whole original cost; no conditional normalizer is suppressed. The source entropy is

    c=2-b^2 log2(b^2)+(2q-q^2)(2w-2).           (2)

## 2. Uniform root bound, including m=0,w=4

The inequalities ln2>2/3 and -ln(1-x)<=x/(1-x) for 0<=x<1 follow respectively by the positive atanh series and integrating 1/(1-t)<=1/(1-x). Also -(1-x)ln(1-x)<=x. Since q<=1/8, (2) gives

    c < 2+(4w-1)q-(2w-2)q^2.

At w=4 this is 121/32; at w>=5 it is at most 51/16 because (4w-1)2^(1-w) decreases and its w=5 value is 19/16. Thus c<121/32 for every w>=4.

From the same log bound, A>=4w-2-(2w+1)q. Moreover B/N<=2w: its extra numerator is 8(1-w-log2 b), negative since -log2 b < (3/2)q/b <=3/14 < w-1. As delta<=1/N, delta B<=2w. Applying W<=2delta and -(1-W)log2(1-W)<(3/2)W to (1) gives

    CE_root < c+delta[4m-2w+15+(4w+2)q]
            <=c+delta(4m+37/4).                 (3)

Here -2w<=-8 and (4w+2)q<=9/4; the latter holds at w=4 and decreases, because its next-to-current ratio is (4w+6)/(8w+4)<=1. The integer inequality 16m+37<=37*2^m holds at m=0; its induction step uses 16<=16m+37. Consequently the last correction is at most (37/4)2^(-w-2)<=37/256. Combining with 121/32=968/256 proves CE_root<1005/256. No asymptotic or unproved infinite summation is involved.

## 3. Exact adaptive physical debit

Let Pi_g be the queried original influence summed with actual physical reaches, and let t<=w be the number of queried coordinates on the all-zero edited path. Every original incident core edge at that point is pivotal, including the width-two coordinates. The exact A095 edge identity therefore gives

    E I(M_leaf)=1+wq-Pi_g+delta(m-w-1+t).        (4)

The original remaining width-w influence is wq-Pi_g. At the edited-path leaf, each of its w-t remaining coordinates has conditional influence 2^t q; multiplying by that leaf's physical reach 2^-t shows

    wq-Pi_g >= (w-t)q.                         (5)

Every other leaf contributes nonnegatively. This is a direct edge count, not independence of branch events. Insert (5) into (4):

    E I(M_leaf)>=1+delta[m-1+(w-t)(q/delta-1)]
                 >=1-delta>=63/64.            (6)

Here q/delta=2^(m+3)>1 and n>=6. All edge deletions stay charged. In fact the untouched width-two factor prevents constant original leaves; M's selector-zero restriction contains that factor at every leaf, so the actual leaves are nonconstant as well.

## 4. Complete reference transport and terminal ownership

At a physical query with child laws P_0,P_1, let p=(P_0+P_1)/2 and r be Q's spectral marginal. On p(T)>0 use pi_b=P_b(T)/(2p(T)); on p=0 use 1/2. Set raw Q_b=2r pi_b and normalize by Z_b. Then Z_b>0 and Z_0+Z_1=2. Conditional KL disintegration and log concavity give

    CE_parent-mean CE_child=Delta+L-mean log2 Z_b>=0.

Here Delta=H_parent-mean H_child=B_query+JS_query>=0 and L is the conditional membership KL. Telescoping over a finite adaptive physical tree gives E CE_leaf<=CE_root. This is the A095 mechanism independently accepted by A094; its use does not claim a fresh universal history lemma. Combining with (3),(6) gives 4 E I_leaf-E CE_leaf>1008/256-1005/256=3/256.

With an untouched independent terminal h and supplied R_h, choose product-compatible posteriors also on zero true fibers. Every transported reference remains Q_core,leaf times R_h; complete CE and divergence both add. Its whole c_h remains outside the core bank. The theorem bounds terminal average, not every individual leaf ratio. Querying h_2, choosing a different source reference or resetting descendants falls outside the proof.

## 5. Independent review of A094's fixed-core profile

At w=3, the tensor coefficients are one +3/8, three -3/8, seven -1/8, twenty-one +1/8. Direct character sums verify these without importing its checker. Thus c=6-(9/8)log2 3, A=6+(3/2)log2 3, B=192-8log2 3. Substitution in (1), with log2 3>3/2 and delta<=1/32, reproduces CE_root<301/64. First original query and second zero-branch query leave mean influences 3/2+delta(m-3) and 5/4+delta(m-2), respectively, whose all-m minima are 45/32 and 19/16. The induction 8m+25<=25*2^m bounds the root correction. Hence A094's whole named profile theorem HOLDS, with its exact policies and reference; this does not accept an arbitrary inherited-profile extension.

## First unsupported universal line

The cancellation in A is proved for this prescribed product source spectrum, not for an arbitrary inherited reference. A full proof still needs either a universally influence-priced complete source reference, or payment of a specified fresh descendant reference plus complementary full terminals from unused ancestor capacity. The theorem removes dimension, padding and depth admission inside one explicit family, but does not supply that universal bridge. The shortest next step is to expose a width-two coordinate in this SAME account and price its specified reset, retaining the spent debit and all current terminals.
