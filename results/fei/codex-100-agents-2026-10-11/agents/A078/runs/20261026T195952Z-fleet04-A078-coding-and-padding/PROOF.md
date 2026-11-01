# Signed padding discounts at the first nonzero-erasure query

All logarithms are base two. The result is an exact transport identity and a counterexample to a proposed discount monotonicity statement, not a universal GU bound. Independent mathematical review is pending.

## Definitions and quantifiers

For every Boolean sign function f on the uniform F_2^n cube, put p_f(S)=fhat(S)^2, pi_f(S)=sum_{T containing S}p_f(T), U(f)=sum_{p_f(S)>0}p_f(S)log2(pi_f(S)/p_f(S)), and D_i U(f)=U(f)-(U(f_i0)+U(f_i1))/2. The full mean coefficient is included. G(f)=sum_i D_i U(f). Write H for full spectral entropy and I for total physical influence.

Fix ANY nonzero padding column P in F_2^n. The actual Boolean function is F(x,z)=f(x+zP). Its signed Walsh coefficients are carried injectively from S to (S, <S,P>), so H(F)=H(f), I_xi(F)=I_i(f), and I_z(F)=q_f(P)=Pr[f(x)!=f(x+P)]. Hence I(F)=I(f)+q_f(P). The elementary union bound along a path flipping precisely the support of P gives q_f(P)<=sum_{j:P_j=1}I_j(f)<=I(f), so every auxiliary influence is counted and I(F)<=2I(f).

Define the ACTUAL padding discount d_P(f)=U(f)-U(F). The image containment rule gives

 d_P(f)=sum_{S:<S,P>=1,p_f(S)>0} p_f(S) log2[pi_f(S)/sum_{T containing S,<T,P>=1}p_f(T)] >=0.       (1)

For tag zero no constraint is imposed by the extra physical coordinate; for tag one it is imposed. Each denominator is at least p_f(S)>0. The formula applies to constants and dummy variables, with empty sums zero.

## Exact uncovered-query transport

Suppose P_i=0. Delete bit i from P to obtain P'. BOTH actual restrictions satisfy F_ib=L_{P'}(f_ib), pointwise, for b=0,1. Thus

 D_i U(F)=D_i U(f)-d_P(f)+(d_{P'}(f_i0)+d_{P'}(f_i1))/2.                   (2)

This is an equality, with its sign retained. It follows simply by substituting U(L_P h)=U(h)-d_P(h) for parent and both children. The queried influence and full entropy decrement agree with their seed values. The true erasure B_i=sum_R phi(fhat(R)^2,fhat(R+i)^2), where phi(a,b)=(a+b)h2(a/(a+b)), agrees as well: P_i=0 gives both members of every pair the same tag, and the map of R to its tagged image is injective. In particular nonzero erasure is preserved at these queries. No abstract spectral law replaces an actual restriction.

If P_i=1, or the queried coordinate is z, no two occupied physical Fourier rows differ just at that coordinate. Such a query has zero erasure and nonpositive D_i U, by the upper-set projection argument of A078 stage124031Z, GU_PROOF section1. That argument is also immediate here: projection is injective on occupied rows, preserves each mass, and can only increase its upper-set mass. This does not price any arbitrary terminal.

## Exact stopped-tree transport, without a refreshed account

Let T be ANY finite adaptive physical tree that queries only seed coordinates outside supp(P), possibly stopping early. The rule is identical for F and f, since both produce the same histories on these coordinates, each with the same uniform probability w_v. Padding z stays unqueried. Let Q_T(h)=sum_{internal v}w_v D_{i(v)}U(h_v). Repeated use of (2) gives the exact identity

 Q_T(F)=Q_T(f)-d_P(f)+sum_{leaves l}w_l d_{P_l}(f_l).                       (3)

All internal discounts cancel once. Combining (3) with the full leaf potentials gives

 U(F)=Q_T(f)-d_P(f)+sum_l w_l U(f_l).                                    (4)

Equivalently U(F)=Q_T(F)+sum_l w_l U(F_l). These formulas include BOTH children at every query, all leaves (including constant leaves), and the same original root discount. No discount is renewed at a child. Query influences telescope identically in the two trees. At each leaf the residual unqueried padding influence q_{f_l}(P_l) remains in I(F_l). A universal payment for Q_T(f) and these full leaf terms is not supplied by (3).

## The discount is not a supermartingale, even at nonzero erasure

Let n=3, little-endian integer order x=x0+2x1+4x2, and set

 f=(-1,+1,+1,-1,-1,+1,+1,+1), P=(1,0,1), i=1.

The actual lift has the sixteen values

 F=(-1,+1,+1,-1,-1,+1,+1,+1,+1,-1,+1,+1,+1,-1,-1,+1).

Its full root and BOTH child discounts are

 d_P(f)=3/4-(17/16)log2(3)+(1/2)log2(5),
 d_{P'}(f_i0)=0,   d_{P'}(f_i1)=1/2.

Consequently the signed correction in (2) is

 c=-1/2+(17/16)log2(3)-(1/2)log2(5)
  =(1/16)log2(3^17/(2^8*5^8))>0,                                     (5)

because 3^17=129140163>100000000=2^8*5^8. Both increments are positive, with

 D_i U(f)=13/16-log2(3)+(9/16)log2(5),
 D_i U(F)=5/16+(1/16)log2(3)+(1/16)log2(5),  I_i(F)=3/4.

The exact checker independently verifies an occupied pair differing at i in both f and F. This is an actual first nonzero-erasure physical query, not merely the zero-erasure sign example. Therefore the putative inequality E[d(child)]<=d(parent), and the resulting claim D_i U(F)<=D_i U(f), are FALSE at their stated full Boolean hypotheses. The counterexample refutes neither full FEI nor any universal admissible GU pair (a,b).

For comparison, f=(+1,+1,+1,-1,-1,+1,+1,+1), P=(1,1,0), i=2 has d_root=0, both child discounts 1/2, seed increment -1/2 and lifted increment 0. This second example has zero erasure and is kept separate from (5).

The negative correction example in out/WITNESSES.json shows that replacing (2) by its positive part also discards a real cancellation. All examples satisfy Booleanity, nonzero P, and P_i=0.

## All-parameter Boolean amplification and exact limitation

Take m disjoint copies of the witness (5), each with its own padding bit, and multiply their Boolean signs. Spectra are products, and pi is also a product on disjoint coordinates. Therefore H,I,U are additive, G is additive, and each untouched tensor factor cancels from the queried D_i U. Query the designated uncovered coordinate in each block, in any adaptive order. The total signed correction is EXACTLY m*c; all physical query influences sum to 3m/4. The root discount and expected terminal discount are m*d_root and m/4. This gives an actual family witnessing linearly accumulating correction with no constant additive repair. It gives no unbounded correction/influence or H/I ratio: c/(3/4) is constant. Padding does not manufacture an FEI counterfamily here.

## Checks that can fail and the remaining unpaid line

Checks target the bit deletion convention, commutation of both restrictions with padding, signed log cancellation, inclusion of the empty row, nonzero-erasure preservation, all auxiliary influences, all complete child potentials, constants/dummy bits, and stopped-tree weights. The finite census covers all seeds n<=3, every nonzero P, and every uncovered query with exact arithmetic. An independent direct-Walsh implementation reconstructs the explicit witnesses without importing the earlier helper. Its rational sign certificate reduces to the integer comparison in (5). A Lean attempt for that integer comparison is separately recorded; a setup hold is not a Lean proof.

The first unsupported universal line remains a dimension-independent bound for the selected signed increments and complete terminal U on arbitrary Boolean cores, funded from the same original influence. Equations (2)-(4) identify the exact missing correction; they do not bound it universally. Further enumeration of fully covered roots cannot pay this line. A076/A077 should independently reconstruct (1)-(5); A092/A094 should check the stopped-tree terminal and tensor scope.
