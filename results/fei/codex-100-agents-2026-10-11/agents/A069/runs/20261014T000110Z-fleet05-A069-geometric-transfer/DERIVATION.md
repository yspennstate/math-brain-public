# A069 stage 3: simultaneous Boolean mask ledger

All cubes are uniform, signs are actual Boolean signs, code lengths are bits. Fix the complete singleton-leaf hierarchy from A069 v1: L_T(S)=1+sum_v b_v 1{S meets C_v}. Write W_T(u)=Gamma_T(u)-1 for a Boolean sign u. No hierarchy is chosen after the sampled Fourier set.

## 1. Exact cell-resampling ownership

For each internal cell C_v, independently resample its coordinates while retaining the outside assignment. Denote the resulting coupled input by X^(v), and define D_v(u)=1{u(X)!=u(X^(v))}. Conditional independent copies give

    P(D_v(u)=1)=E Var(u | X_outside C_v)/2,
    W_T(u)=2 sum_v b_v P(D_v(u)=1).                    (1)

This is finite Parseval: conditional expectation drops the Fourier coefficients whose sets meet C_v, so averaged conditional variance equals their mass. For Boolean signs u,w, D_v(uw)=D_v(u) XOR D_v(w). Therefore,

    W_T(uw)=W_T(u)+W_T(w)-R_T(u,w),
    R_T(u,w)=4 sum_v b_v P(D_v(u)=D_v(w)=1)>=0.        (2)

In particular Gamma_T(uw)<=Gamma_T(u)+Gamma_T(w)-1, EVEN when physical variables are shared. This is an inequality for this particular complete code cost, not Fourier entropy subadditivity (which is false for arbitrary shared-variable products). Every cell contribution and empty/root convention is retained.

For a Boolean seed g and two Boolean phase masks q1,q2, the final f=g*q1*q2 has disagreement parity D_v(f)=D_v(g) XOR D_v(q1) XOR D_v(q2). Let M_v count these three disagreements. Since M_v is 0,1,2 or 3, M_v minus its parity is 2*1{M_v>=2}. Thus the exact ledger is

    Gamma_T(f)=Gamma_T(g)+W_T(q1)+W_T(q2)-R3,
    R3=4 sum_v b_v P(M_v>=2)>=0.                      (3)

There is ONE refund event per resampled cell pair; it is not charged once for each positive Fourier cross term. Equivalent two-step decompositions are

    R3=R_T(q1,q2)+R_T(g,q1*q2)
      =R_T(g,q1)+R_T(g*q1,q2).                        (4)

The two events in the first decomposition are mutually exclusive for any fixed resampled pair: if both mask disagreements occur their product has no disagreement. This is exact ownership of the complete simultaneous edit cost. No individual signed Fourier cross term is asserted nonpositive.

## 2. Genuine overlapping subcube masks: one influence budget

Split controller coordinates into disjoint nonempty blocks C,U,V with sizes r,s,t>=1 and leave a nonempty physical core Y. Choose fixed assignments c*,u*,v*. Let A=1{C=c*,U=u*}, B=1{C=c*,V=v*}, and q1=1-2A, q2=1-2B. These are compatible overlapping subcubes; the final edit is sequential flipping/XOR, NOT flipping the union once. In particular q=q1*q2=1-2A-2B+4AB and the intersection is correctly flipped twice.

Use any balanced binary singleton trees inside C,U,V,Y, and the fixed binary topology

    T=(T_Y, (T_C, (T_U,T_V))).

For a codimension-k event, rho=2^{-k}, its mask has

    P(S_mask meets E)=4rho(1-2^{-|E intersects fixed coordinates|}),
    I(mask)=2k*rho.                                    (5)

For q1, only the internal C and U trees and at most three join cells are occupied. Thus the sum of 2*(1-2^{-intersection size}) is at most 2[(r-1)+(s-1)+3]=2(r+s+1). Equation (5) gives

    W_T(q1)<=8rho1(r+s+1)<=6I(q1),
    W_T(q2)<=8rho2(r+t+1)<=6I(q2),                     (6)

since both codimensions are at least two. Labels in Y and in the unused exclusive block cost zero. These estimates concern one fixed all-set reference, not separate geometry choices per sample.

Put c=2^{-r}, a=2^{-s}, b=2^{-t}. From the actual controller q=1+1{C=c*}[(1-2*1{U=u*})(1-2*1{V=v*})-1], pivotal edges give exactly

    I(q)=2c[sa+tb+r(a+b-2ab)],
    I(q1)+I(q2)=2c[sa+tb+r(a+b)].                      (7)

The exclusive blocks are unchanged by multiplication of the two masks. On C the combined mismatch is the XOR of the exclusive events; its probability is a+b-2ab, counted once. Because a,b<=1/2, 2ab<=(a+b)/2, so

    I(q1)+I(q2)<=2I(q).                                (8)

Combining (3), (6), (8), for EVERY Boolean g on the same coordinates, even with arbitrary controller/core dependence,

    Gamma_T(g*q1*q2)<=Gamma_T(g)+12I(q).                (9)

The constant is independent of all four block sizes, the signs selected in the events, and the ambient dimension. This pays the complete two-mask surcharge using the net controller's physical influence once. It does not replace Gamma_T(g) by an unpaid entropy assumption. Nor does it imply a bound by I(f) for arbitrary g: choosing g=q makes f constant and can cancel that influence budget entirely.

For the conditional application g=h(Y), I(f)=I(h)+I(q) because this is a disjoint physical product. Also Gamma_T(g)=Gamma_(T_Y)(h)+2*(1-(Eh)^2). If the source core has a paid complete reference Gamma_(T_Y)(h)<=K I(h), then the elementary spectral Poincare bound Var(h)<=I(h) gives

    H(f)<=Gamma_T(f)
         <=(K+2)I(h)+12I(q)
         <=max(K+2,12)I(f).                            (10)

A root-bit core reference cannot satisfy that hypothesis for constant h; this case is not silently included. No claim of a new disjoint-product FEI theorem is made: that closure is baseline. The mathematical advance is the shared-variable code-cost ledger (3), with one simultaneous refund, and its nongeometric two-mask surcharge payment (9) retaining arbitrary source cost.

## 3. A070 obstruction consumed, not repeated

A070's physically disjoint positive-cross witness is valid: on N=2 let g=x1 and flip (+,+) and (-,+). Although their edit-support intersection is empty, the weighted difference cross is +1/2. The final sign is -x1*x2. Here W(g)=W(f)=2, each one-point mask has W=3/2, and R3=3. Equation (3) gives Gamma(f)=3+3-3=3 exactly. The ledger keeps the source/edit rebate instead of bounding only the positive difference cross by physical overlap. This reconstructs the witness to validate the new ownership rule, not as a new refutation of A069 or FEI.

For overlap itself, the difference is delta=e1+e2-2e12 with ej=-2g*1_event and e12=-2g*1_intersection. The checker verifies that identity before transforming. Equations (1)-(4) are reconstructed directly, so no unreviewed A070 new cross theorem is needed as a proof premise.

## 4. First unsupported line

For arbitrary g depending on controller coordinates, the actual final influence I(g*q) need not dominate either I(g) or I(q), and no universal separating-source Gamma(g)<=K I(g) theorem has been proved. In addition, bound (8) uses nonempty private blocks and compatible common assignments; identical masks can cancel to q=1 and violate any positive input-mask-to-net-influence comparison. The next mechanism must retain signed cancellation to transport source cost to final source influence, not reinstate a physical-overlap-only Fourier cross bound. Universal FEI remains OPEN.
