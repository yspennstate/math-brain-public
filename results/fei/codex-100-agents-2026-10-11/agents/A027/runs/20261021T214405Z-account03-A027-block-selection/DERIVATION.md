# A single signed ancestor refund pays a later positive exit

Rung: analytic proof subject to the exact scalar sign certificate below and independent review. Full FEI is OPEN. This extends the existing A027 partial-core candidate; it does not certify arbitrary core or terminal FEI.

Let u and a be Boolean signs on disjoint physical coordinates, p=Pr(a=-1), d=Pr(u=-1), and F=1+((1-a)/2)(u-1). All entropies are in bits. Put E(t)=t^2 log2(1/t^2), phi(d)=E(1-2d), eta(q)=q log2(1/q), V=4p(1-p), and

    R(p,d)=4d(1-d)eta(p^2)+2d(1-d)V+V E(d)+phi(pd)-p phi(d).

The previously reconstructed identity is H(F)=pH(u)+dHplus(a)+R(p,d). Write b=1-1/sqrt(2)=2d_star. The new sufficient endpoint criterion is:

    p in [0,1/4] union {1/2}, d_root<=1/16,
    every actual core-only tree leaf has d_leaf<=b.

Then the COMPLETE signed activation correction obeys

    Pi_H(F)-p Pi_H(u)
       =R(p,d_root)-sum_leaf w_leaf R(p,d_leaf)<=0.

In particular, positive local corrections may occur at intermediate queries and are paid from the previously earned, unspent signed ancestor refund. There is no requirement that every intermediate child lie in the old safe band d<=d_star. The complete activated leaf entropies and d_root I(a) controller influence remain at the terminals.

## 1. Controller comparison, with its actual range

The checked prior curvature formula is R_dd(p,d)=16p D(p,d)/ln(2), where

    D(p,d)=ln(1-2d)-(1-p)ln(2d)-p ln(1-2pd)+p ln(p).

For p>0 and 0<d<=b<1/3, D_p=ln(z)+z+1 with z=2pd/(1-2pd). If p<=1/4 then z<=1/5. Thus D_p<=-ln(5)+6/5<0, since ln(5)>ln(4)>=4/3>6/5. Hence D(p,d)>=D(1/4,d). Direct subtraction gives

    D(1/4,d)-D(1/2,d)
      =(1/4)ln((1-d)^2/[d(2-d)])>=0,

because 1-4d+2d^2>=0 for d<=b. Denominators are strictly positive on the stated open interval. It follows that

    C_p(d)=R(p,d)/p-2R(1/2,d)

is convex on [0,b]. Continuity closes d=0. The case p=1/2 has C_p=0. No claim for arbitrary p in (1/4,1/2) is made; the curvature comparison is not established there. All point controllers p=2^-r, r>=1, are covered.

## 2. A global supporting line extending beyond the curvature band

Set A(d)=R(1/2,d). On 0<=d<1/2,

    A(d)=4d(1-d)+E(d)+E(1-d)-(1/2)E(1-2d),
    A'(d)=4-8d+4[-d log2(d)+(1-d)log2(1-d)
                         -(1-2d)log2(1-2d)].

A is convex on [0,d_star] and concave on [d_star,3/10], directly from D(1/2,d)=(1/2)ln((1-2d)^2/[4d(1-d)]). Let s=1/16. The sole numerical-looking ingredient is the EXACT prime-log sign

    A(3/10)-A(s)-(3/10-s)A'(s)>0.

The checker records this expression and outward rational bounds using a proved atanh-series tail. Let T(d)=A(d)-A(s)-(d-s)A'(s). Convexity makes T>=0 on [0,d_star]. Concavity makes its minimum on [d_star,3/10] occur at an endpoint, both nonnegative by the preceding facts. Therefore the tangent at s supports A throughout [0,3/10], including [0,b]. Here b<3/10 follows from 1/sqrt(2)>7/10 by squaring positive numbers.

For every 0<t<=s the tangent to A at t also supports A on [0,b]. On d<=s this is convexity. For d>=s, the tangent at t lies below the tangent at s: evaluate at s using convexity, then use A'(t)<=A'(s). Adding the tangent support of convex C_p proves that the tangent to R(p,.) at t supports it on [0,b]. Averaging over the actual leaf-bias martingale proves the claimed nonpositive endpoint correction. For root d=0 all leaves have d=0. For p=0 the function is constant and the correction vanishes.

## 3. Conservation through an actual history

At a core query v let e_v=R(p,d_v)-[R(p,d_v0)+R(p,d_v1)]/2 and w_v be its original uniform-input reach. The only refund account is -sum_processed w_v e_v. Telescoping gives at every frontier R(p,d_root)-sum_frontier w R(p,d). If every frontier bias is <=b and d_root<=1/16, this quantity is nonpositive by the same supporting-line theorem. Thus this account never borrows from future controller influence. A positive query may spend a portion of an existing refund, and the final account is the same original endpoint account. This is a signed activation correction account, not a certificate of KI-H for the core or of its leaves.

Every prefix frontier of a tree whose final leaf biases are <=b automatically has biases <=b, since each frontier bias is a conditional average of its descendant leaf biases. The account therefore remains nonnegative through every ordering consistent with that actual tree. No fixed uniform physical-input event is silently replaced by a spectral reference.

The influence ledger is Pi_I(F)=p Pi_I(u), with terminal influence p E I(u_leaf)+d_root I(a). If the ACTUAL projected core partition is independently paid at K and complete activated leaves at L, this tree closes at max(K,L). Those hypotheses remain unpaid in general. A stopped positive correction does not manufacture either hypothesis.

## 4. Actual positive-exit witness with both nonconstant terminals

On four shared core bits let g be -1 on the first three inputs and h be -1 on the first four. Add one core selector choosing g,h. Its bias is 7/32 and its selector correction for a dictator controller is strictly positive (the stage6 quarter-band witness). Gate this five-bit core behind TWO additional core bits that must both pass; otherwise the core sign is +1. The resulting seven-bit core has d_root=7/128<1/16. Query the two gate bits, stopping on failure, and then query the selector. All final core leaves are constants or g,h, with biases 0,3/16,1/4<b. The final positive selector correction is paid from the prior gate-query refund; the two nonconstant terminal spectra remain present. These core gate bits are actual DATA queries, not extra copies of the independent controller bank.

The exact implementation checks r=1,2,3 controllers, individual local debits, all prefix accounts, and the complete physical terminal entropy/influence partition. For r=1 it certifies the same strict positive exit as stage6. The general theorem above permits arbitrary core complexity at every nonconstant terminal, provided its bias bound holds.

## 5. First unsupported universal line

For an arbitrary Boolean core, construct a useful proper stopping partition with independently paid core decrement and complete activated terminals, while arranging the endpoint band or paying its violation. The root bias<=1/16 assumption is not free for arbitrary cores, and sparse activation merely re-encodes their entropy. This criterion supplies a conserved signed ancestor payment, not universal FEI. Changes of p caused by interleaved controller queries require a further transfer argument; this theorem keeps the independent controller untouched throughout the core-only tree.
