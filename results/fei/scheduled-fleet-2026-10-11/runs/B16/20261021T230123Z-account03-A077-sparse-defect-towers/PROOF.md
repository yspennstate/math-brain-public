# Two correlated private profiles retain a signed row collision

Entropy is in bits on the uniform cube. The full FEI conjecture remains open.

## 1. Exact two-point decomposition

Let d>=1, e=2^-d, and let h be a Boolean function on d shared bits with h(0)=h(e_1)=1. Let V,W be ANY Boolean functions on the SAME private n-cube. The private inputs are disjoint from the shared inputs. Define the actual Boolean function

    F(s,x)=V(x) if s=0, W(x) if s=e_1, h(s) otherwise.

Put b_S=hhat(S), v_T=Vhat(T), w_T=What(T), mu=v_empty, nu=w_empty, and g(a)=-a^2 log2(a^2), with g(0)=0. Direct Walsh transformation gives

    Fhat(S,empty)=b_S+e(mu-1)+e(-1)^1{1 in S}(nu-1),
    Fhat(S,T)=e[v_T+(-1)^1{1 in S}w_T], T nonempty.       (1)

The two shared vertices have equal mass; exactly half of the shared Fourier characters distinguish their signs. Consequently, with

    k(a,b)=[g(a+b)+g(a-b)]/2-g(a)-g(b),
    Xi(V,W)=e sum_{T nonempty} k(v_T,w_T),
    E(mu,nu)=sum_S g(b_S+e(mu-1)+e(-1)^1{1 in S}(nu-1)),
    H_sep=E(mu,nu)+e[H(V)+H(W)-g(mu)-g(nu)]
                         +2de[2-mu^2-nu^2],

the COMPLETE entropy identity is

    H(F)=H_sep+Xi(V,W).                                  (2)

Indeed, for each nonempty T the shared-row entropy is

    (e/2)[g(v_T+w_T)+g(v_T-w_T)]+2de(v_T^2+w_T^2).

Expanding k and applying Parseval proves (2). No zero Fourier row is removed, and E contains the entire empty-private sector. H_sep is a bookkeeping expression, not a claim of a separate Boolean realization or a permission to discard coherent cross terms.

For a private physical coordinate i,

    Inf_i(F)=e[Inf_i(V)+Inf_i(W)].                         (3)

This follows directly from disjoint physical events, or from the paired shared signs in (1). Both methods give the same answer. Private correlation does not change (3).

## 2. The collision is nonpositive, but its restriction decrement is not

For R=a^2+b^2>0 let p=(a^2,b^2)/R and q=((a+b)^2,(a-b)^2)/(2R). Both are binary probability laws. Homogeneity of g gives

    k(a,b)=R[H(q)-H(p)-1].                               (4)

Because 0<=H(p),H(q)<=1,

    -2R<=k(a,b)<=0,
    -2e[Var(V)+Var(W)]<=Xi(V,W)<=0.                      (5)

R=0 contributes zero. Formula (4) also proves continuity at every vanishing coefficient, with no division at those points. The possible sign of each amplitude is kept in q.

At an actual private split, let V_+,V_-,W_+,W_- be the restrictions on that SAME physical coordinate. Then exactly

    Delta_i H(F)=Delta_i H_sep
                     +Xi(V,W)-[Xi(V_+,W_+)+Xi(V_-,W_-)]/2.   (6)

Thus Xi<=0 is insufficient to infer that its signed decrement in (6) is nonpositive. Dropping Xi only at the parent while retaining less expensive children would silently remove a real payment. Equation (6) keeps BOTH complete actual terminal laws. The same equality telescopes over every finite adaptive private tree, with one root Xi and the expected actual terminal Xi. This is an exact identity, not a new nonnegative stopping reserve.

## 3. All-dimensional live-child obstruction to mean-bank-only payment

Use h=+1, V(x,y)=xy, W(x,y)=y, and query x. Here x,y are sign bits; the two edited shared vertices are 0 and e_1 in binary notation. All four controller restrictions V_+,V_-,W_+,W_- are nonconstant characters of y. Both actual F children are nonconstant as well.

At the parent mu=nu=0. At BOTH x children these means are still zero, and the queried singleton coefficients Vhat(x),What(x) are zero. Therefore each inherited point-controller reserve

    R_V=de[1-(EV)^2], R_W=de[1-(EW)^2]

has EXACTLY ZERO released amount. Both inherited controller entropy drops and erasures are zero, since all controllers involved are characters. In particular retaining a quarter core erasure does not pay the new bill.

At the root, V and W occupy different Fourier labels, so Xi=0. After either x answer they occupy the SAME label y, with equal or opposite signs. Since k(1,+/-1)=-4,

    Xi_+=Xi_-=-4e,
    Delta_x H_sep=0,
    Delta_x H(F)=4e,
    Inf_x(F)=e.                                         (7)

The actual erasure and channel contributions are separately

    B_x(F)=2e, JS_x(F)=2e.                               (8)

For an independent check of B: the private nonempty label pairs y and xy have equal squared coefficient e^2 at every shared Fourier label. There are 2^d such pairs, each contributing Phi(e^2,e^2)=2e^2, giving 2e. There are no other nonzero x-pairs. Equation (7) minus this exact erasure gives JS=2e.

This disproves the candidate payment

    positive signed two-profile collision <= released(R_V+R_W)

even when both children and all four controller restrictions are nonconstant and full controller entropy/quarter-erasure decrements are retained. It also disproves the version that assumes the collision is nonincreasing merely because Xi<=0. It DOES NOT disprove the A076 price-11 common-controller theorem, nor a two-profile inequality retaining a physical-influence allowance: this witness costs exactly four units of actual queried influence for entropy, two for erasure.

## 4. Rarity, full terminals, and the absence of an FEI counterexample

The function is a point activation on r=d-1 independent shared controls of

    M(t,x,y)=y * [x if t=0, 1 if t=1].

M has four coefficients of magnitude 1/2, hence H(M)=2, I(M)=2, and mean zero. Let p=2e. Direct activation counting gives

    H(F)=2p+2r p(2-p)+g(1-p),
    I(F)=p(r+2)=(2d+2)e,
    Pr(F=-1)=e.                                         (9)

Both x terminals have the FULL entropy

    H(F_+)=H(F_-)=2r p(2-p)+g(1-p).                     (10)

Their actual influences are dp and (d+1)p respectively; the extra t-character in the second child is not erased from the influence ledger. Thus I(F)-[I(F_+)+I(F_-)]/2=e, in agreement with (3). The case d=1 has r=0, p=1, g(0)=0; root entropy is 2 and both terminal entropies are zero. All formulas include that boundary.

As d grows the root minority probability, every coordinate influence and I(F) tend to zero. Nonetheless (7)-(8) and the zero mean-bank release hold for EVERY d. The elementary inequality g(1-p)<=2p/ln2<4p follows from -(1-p)ln(1-p)<=p, including p=1 by continuity. Therefore H(F)<=[4r+6]p<=4(r+2)p=4I(F). This actual Boolean family is not an FEI counterexample. Tensoring its members adds H and I and cannot produce an unbounded ratio.

## 5. What covariance alone forgets

There are balanced orthogonal pairs with the SAME (EV,EW,E VW)=(0,0,0) and different Xi. On three private bits take the character pair V=x,W=y (ignoring z), which has Xi=0. Compare

    V=Maj3(x,y,z), W=Maj3(x,-y,-z).

Their coefficients on x,y,z,xyz are respectively (1,1,1,-1)/2 and (1,-1,-1,-1)/2. They are balanced and orthogonal, but each of the four shared labels contributes k=-1, so Xi=-4e. Thus those three physical moments do not determine the exact remaining collision or its terminal refund. This is not a refutation of every conservative bound based on moments; (5) is such a bound. It identifies the signed Fourier-label information lost by a proposed exact replacement.

## 6. The complete mean sector is paid by the SAME original bank

The two-point case allows the rest of the correlated-profile extension to be closed. Keep R=de(2-mu^2-nu^2), the SUM of the two original point-event banks; do not renew it. Write

    J_sep=E(mu,nu)-H(h)+de(2-mu^2-nu^2)-e[g(mu)+g(nu)].

Then H_sep=e[H(V)+H(W)]+H(h)+R+J_sep. For every actual private split, let a=Vhat(i), b=What(i), D=Inf_i(V)+Inf_i(W). The mean-sector bound is

    Delta_i H_sep <= e[Delta_i H(V)+Delta_i H(W)]
                               +R_parent-E R_child+12eD.    (11)

Here is a reconstruction of its critical curvature step, keeping correlated controllers. Along any segment in [-1,1]^2 with direction (a,b), the shifted empty-private rows y_S have derivative e[a+(-1)^1{1 in S}b]. Its total squared derivative mass is t=e(a^2+b^2). If t>0, the normalized squared derivative law w has entropy

    H(w)=d-1+h2((a+b)^2/[2(a^2+b^2)])>=d-1.

The shifted rows have total squared mass M=1-e(2-mu^2-nu^2)<=1. For M>0, weighted log concavity, equivalently Gibbs applied to w and y_S^2/M, gives

    E''=2t[H(w)+D_2(w||y^2/M)-log2 M]-6t/ln2
                                             >=2t(d-1)-6t/ln2.

Thus A=E+de(2-mu^2-nu^2) satisfies A''>=-(2+6/ln2)t along that segment. At every row zero g is C1; the finitely many singularities glue by continuity of the corrected derivative. A zero M occurs only at an isolated all-zero row state (possible for d=1); it is covered the same way. If t=0 both directions vanish and the estimate is exact. No infinite sum or moved limit is used.

The midpoint inequality yields Delta A<=(1+3/ln2)e(a^2+b^2). The scalar derivative bound |g'|<=6, reconstructed in REVIEW_A076.md, yields

    Delta J_sep <= e[(1+3/ln2)(a^2+b^2)+6(|a|+|b|)]
                  <=12eD,

because |a|<=Inf_i(V), |b|<=Inf_i(W), both influences are <=1, and ln2>=2/3. Substitution proves (11). The exact original bank release is de(a^2+b^2), even when both controllers depend on the queried coordinate. Both actual child means lie on the allowed segment, so that side condition is used precisely here.

Combining (6) and (11) gives the complete unconditional residual inequality

    Delta_i H(F) <= e[Delta_i H(V)+Delta_i H(W)]
       +R_parent-E R_child+12Inf_i(F)+Delta_i Xi.         (12)

This is an extension of the existing bank accounting, not a third independent source of capacity. It holds in every dimension and telescopes over every adaptive PRIVATE stopping tree, retaining R_leaf, Xi_leaf and both complete inherited controller entropies. An actual shared query changes h and the event geometry and still needs its own payment. The finite scan certifies Delta_i Xi<=4Inf_i(F) through n=3 private bits, but section7 below disproves EVERY finite universal K at larger private dimension. The finite certificate must not be extrapolated.

## 7. The remaining collision has NO universal physical-query price

The already used bent/point-defect mechanism survives intact in the new exact residual. This is a specialization of A077's earlier bad-private-query family, not a newly discovered FEI counterexample.

Let k>=4 be even, a=2^-k, b=2^(-k/2), and take ANY d>=1. On k private bits z and a further private bit i, set

    V(z,i)=(-1)^(z1*z2+...+z(k-1)*zk),
    W(z,i)=1-2*1{z=0,i=0}.

Use h=+1 and the two shared vertices of section1. V is bent, with all private z Fourier coefficients of magnitude b and Vhat(T+i)=0. Every nonempty coefficient of W is -a and its mean is 1-a. At the i=0 child W becomes a k-bit point defect, whose nonempty coefficients are -2a; at i=1 it is the constant +1. Both ACTUAL F children remain nonconstant because they still contain bent V at the other shared vertex. All their full controller entropies remain in (12).

Define L_b(t)=[g(b+t)+g(b-t)]/2-g(b). Evenness of k in both arguments and (1) give EXACTLY

    Delta_i Xi / Inf_i(F)
       = (a^-1-1)/a * [k(b,a)-k(b,2a)/2],
    Inf_i(F)=ea,
    k(b,a)-k(b,2a)/2=L_b(a)-L_b(2a)/2+g(a)-4a^2.        (13)

There is no omitted empty-private contribution: labels containing i have V coefficient zero, hence k=0; the empty label is excluded at the parent and both children by the definition of Xi. The remaining a^-1-1 labels all give (13), regardless of their bent signs.

For k>=4, b<=1/4 and b-2a>=b/2>0. Since g''(u)=-4log2 u-6/ln2 is decreasing on positive u, the integral midpoint formula yields

    L_b(a)>=a^2 g''(b+a)/2,
    L_b(2a)<=2a^2 g''(b-2a).

Consequently the bracket in (13) is at least

    a^2[k-4+3/ln2+4log2(1-2b)-2log2(1+b)]
                                                  >=a^2(k-5).   (14)

For the last line: 1-2b>=1/2 gives 4log2(1-2b)>=-4; (1+b)^2<=25/16<2 gives -2log2(1+b)>=-1; and ln2<=3/4 gives 3/ln2>=4. The logarithm bound follows from the trapezoid upper bound for the convex function1/t on[1,2]. Every interval stays strictly positive, so no cancelled denominator or differentiation crosses zero.

For even k>=6, (13)-(14) imply

    Delta_i Xi / Inf_i(F)>=(1-a)(k-5)>=k-6.              (15)

The last step uses a(k-5)<=1, for instance k<=2^k. Thus NO absolute K pays Delta_i Xi alone by K Inf_i(F), even in the two-vertex geometry. At d=k the edited region and all root influences tend to zero, so imposing rarity does not repair this collision-price claim. The original mean-bank release is only de a^2, while Inf_i(F)=ea; it is not a hidden new linear-log budget unless a valid original source payment is supplied.

This does not disprove FEI. At d=1 the core M is the one-bit multiplexer of bent V and point W. Proposition8.6, or binary Hadamard entropy directly, gives H(M)<=2+[H(V)+H(W)]/2. Here H(V)=k, I(V)=k/2, H(W)<=4I(W)=4(k+1)a, and I(M)>=k/4. Hence H(M)/I(M)<=2+8/k+8(1+1/k)a<5 for k>=4. For arbitrary d, F is a point activation of M on r=d-1 controls. A self-contained coarse bound is H(F)<=10I(F): writing p=2^-r, u=1-EM, exact sector counting gives

    H(F)=pH(M)-p g(EM)+p(1-p)g(u)+g(1-pu)
                                +2rp[Var(M)+(1-p)u^2],
    I(F)=p[I(M)+ru].

For r>=1, pu<=1; use g(EM)>=0, g(u)<=2u/ln2 (also true when u>1, where g(u)<=0), g(1-pu)<=2pu/ln2, and Var(M)+(1-p)u^2=2u-pu^2<=2u. This gives H(F)<=pH(M)+4rpu+6pu<=10I(F). For r=0 the preceding core bound applies. These inequalities include all zeros by continuity. The family reproduces a local-payment obstruction, with bounded global H/I.

### All controller children can remain nonconstant and balanced

Multiply BOTH controllers by one fresh private character y, leaving i as the queried coordinate: V*=yV and W*=yW. Every controller mean at the parent and both children is now ZERO. Both W* children are nonconstant (one is y times a point defect and the other is y); V* remains nonconstant on both sides. Thus both original mean banks release exactly zero, and no point-exit based merely on core nonconstancy is available.

Multiplication shifts every old Fourier label by y. The previously excluded empty z label now contributes an additional signed decrement

    J=k(b,1-a)-[k(b,1-2a)+k(b,1)]/2.

For t>b, differentiation gives d^2 k(b,t)/dt^2=-2log2(1-b^2/t^2)>=0. On t in[1-2a,1], k>=4 gives b^2/t^2<=4/49<1/2, so this second derivative is <=2. The midpoint formula therefore gives -a^2<=J<=0. The SAME signed-row calculation now yields

    Delta_i Xi(V*,W*)/Inf_i(F*)
       >=(1-a)(k-5)-a=k-5-a(k-4)>=k-6, even k>=6.       (16)

The guarded controllers are balanced; their entropies equal those of V,W and their total influences each increase by one. All controller quarter-erasures and complete terminal costs remain in(12). The activated wrapper still satisfies the coarse H<=10I bound just derived (its unactivated core has H<=5I). The point-defect bound used there follows directly from H(W)=g(1-a)+(2/a-1)g(a)<=2a/ln2+4ka<=4(k+1)a. At d=k its minority probability is e, total influence tends to zero, and all means and mean-bank releases stay zero. This meets the live-child and rare/rare guards without repairing the false local collision price.

## 8. One collision CAN use an actual unused bent child surplus

The guarded example supplies an explicit signed donor, rather than a new selector reserve. At target C=5 the unchanged bent controller V*=yV has the ACTUAL certified surplus

    S=e[5I(V*)-H(V*)]=e(3k/2+5).

By(5), Delta_i Xi<=4e for any two balanced controller children, since Xi_parent<=0 and each Xi_child>=-4e. In particular S>=11e at k>=4, so this one collision can be debited by 4e from S and leave at least7e. With an inherited nonnegative old debit D0, the precise eligibility condition is 0<=D0<=S-4e. Define K_parent=S-D0 and put K_child=S-D0-4e on BOTH actual children, preserving their complete entropies and their original selector/mean banks. Then(12) gives the concrete stopped-node payment

    Delta_i H(F*)+E K_child
       <=e[Delta_i H(V*)+Delta_i H(W*)]
                       +12Inf_i(F*)+K_parent.            (17)

Here the mean-bank release is zero. The inherited V* entropy decrement is also zero, but its FULL terminal entropy k is retained; its certified C=5 surplus, not its entropy, funds the donation. The quarter-erasure terms are neither erased nor declared paid by this transfer. A carried scalar selector-influence reserve remains unchanged in conditional average until actual selector revelation. Once 4e is booked, it is not assigned again: the next collision receives K_child, NOT S. This is a source-owned one-collision transfer for the actual balanced bent/defect family, conditional on the stated unused-balance test; it does not certify that every next history has that balance.

For an explicitly erasure-valued handoff, use Delta H=B+JS and e[JS_i(V*)+JS_i(W*)]<=(2/ln2)Inf_i(F*). The same transfer yields

    B_i(F*)+E K_child<=e[B_i(V*)+B_i(W*)]
                     +(12+2/ln2)Inf_i(F*)+K_parent.       (18)

Thus the inherited core erasures remain present in full, and the physical price is <15. No terminal entropy or source debit is removed in passing from(17) to(18).

## 9. First unsupported universal line

For arbitrary correlated V,W, pay the SIGNED decrement in (6) from one genuinely unused ancestor source after old debits, retaining both full controller terminals and all existing erasure/reference costs. A dimension-independent physical-query price for DeltaXi alone is now REFUTED by(16); further constant searches for that claim are retired. Section8 pays one guarded collision from the actual bent C5 surplus and records the spent amount. The next unsupported step is maintaining an eligibility condition for a further unequal correlated split from that SAME remaining S-D0-4e, without assuming the next child's certificate afresh. No all-dimensional bound for that nonlocal payment is asserted here. The identity is compatible with the known retained-KL/FEI equivalence and does not make an unrestricted leaf free.
