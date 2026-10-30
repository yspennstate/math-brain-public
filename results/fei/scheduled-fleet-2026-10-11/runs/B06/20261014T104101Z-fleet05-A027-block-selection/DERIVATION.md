# Signed activation correction: sharp low-bias band

Uniform Boolean signs, normalized Fourier entropy in bits. Let u be a core sign, a an independent controller sign, p=Pr(a=-1), d=Pr(u=-1), F=1+((1-a)/2)(u-1). Assume 0<=p<=1/2. No FEI certificate for u or a is assumed. Write E(t)=t^2 log2(1/t^2), phi(d)=E(1-2d), eta(t)=t log2(1/t), V=4p(1-p), and Hplus(a) for the unnormalized nonempty spectral entropy. Previously proved exact activation identity:

    H(F)=pH(u)+d Hplus(a)+R(p,d),
    R=4d(1-d)eta(p^2)+2d(1-d)V+V E(d)+phi(pd)-p phi(d).

Define d_star=(1-1/sqrt(2))/2. This stage proves R(p,.) convex on [0,d_star], uniformly for p in [0,1/2]. It therefore proves a nonpositive SIGNED activation surcharge for core partitions whose leaf biases stay in that band. The controller entropy is retained at terminals, not discarded or spent twice.

## Curvature calculation and exact convexity proof

For 0<p<=1/2 and 0<d<1/2, let b=1/ln(2). Direct differentiation gives E''(t)=-4log2(t)-6b and phi''(d)=-16log2(1-2d)-24b. Substituting in R'' cancels every b term, yielding

    R_dd(p,d)=16p D(p,d)/ln(2),
    D=ln(1-2d)-(1-p)ln(2d)-p ln(1-2pd)+p ln(p).

The constant -4V in the second derivative is included in the ln(2d) term; dropping it would give a wrong band. For fixed d,

    D_p=ln(2d)-ln(1-2pd)+2pd/(1-2pd)+ln(p)+1,
    D_pp=2d/(1-2pd)+2d/(1-2pd)^2+1/p >0.

Thus D_p is increasing in p. At p=1/2 it equals ln(z)+z+1 where z=d/(1-d). We have d_star<1/6: this is equivalent to 1/sqrt(2)>2/3, verified by squaring positive numbers. Consequently z<1/5 for d<=d_star, and

    D_p(1/2,d)< -ln(5)+6/5 < -ln(4)+6/5 <= -4/3+6/5 <0.

Here ln(2)>=2/3 follows from the positive atanh series at 1/3; this is an exact inequality, not a decimal estimate. Hence D decreases in p on (0,1/2] and

    D(p,d)>=D(1/2,d)
            =(1/2)ln((1-2d)^2/(4d(1-d))) >=0

precisely when 1-8d+8d^2>=0 in the lower interval, i.e. d<=d_star. R is continuous at d=0 and has a finite right derivative there, so the interior convexity extends to the closed interval. At p=0 R is identically zero. All endpoint conventions are actual limits of the exact entropy identity.

## Core-only signed refund and first proper query

For ANY finite adaptive core-only restriction tree U with actual leaf weights w_l and leaf negative probabilities d_l<=d_star, bias is a martingale and exact entropy cancellation gives

    Pi_H(F;U)-p Pi_H(u;U)
        =R(p,d_root)-sum_l w_l R(p,d_l) <=0.

The linear d Hplus(a) term cancels; it remains in the actual terminal entropies. The nonnegative refund is sum_l w_l R(p,d_l)-R(p,d_root), a single endpoint quantity. This proves no renewal of a positive future-control capacity. At a single core query it suffices that both children have negative probabilities <=d_star. In particular, if the parent has d<=d_star/2, EVERY first core coordinate meets this condition, since each child probability is <=2d. For m>=2 this is a proper one-coordinate block. It pays ONLY the activation surcharge, leaving the core entropy decrement and actual child entropies explicit.

## Interleaved point controls, no core surcharge

Use the already proved projected-tree construction from A027 version3. A physical active node with r_v remaining point controls has p_v=2^-r_v, and controls that fail yield constant +1 terminals. Project by conditioning the ORIGINAL INPUT on all controls passing; active projected weight is w_v p_v/p_root. Actual core-query costs sum to Q_core=p_root Pi_I(u;U).

Assume at every active CORE query both actual core-child negative probabilities lie in [0,d_star]. If r_v>=1, p_v<=1/2 and the preceding convexity makes its signed activation correction nonpositive. If r_v=0 the correction is zero. The point-activation correction G_r(d)=d Hplus(a_r)+R(p,d) differs from R by a linear function, so the same sign applies. Control nodes keep the previously reconstructed A028 bound Delta_control H<=C0 times their OWN queried influence, C0=2+2/ln(2)+1/(sqrt(e)ln(2))<6. Summing actual nodes ONCE yields

    Pi_H(F;T)<=p_root Pi_H(u;U)+C0 Q_control.

If this actual projected proper tree has Pi_H(u;U)<=K Pi_I(u;U) and every actual terminal has H<=L I, K,L>=0, the exact influence partition proves

    H(F)<=max(K,C0,L) I(F).

This removes the prior kappa=4+12/ln(2) core surcharge under the stated bias-band condition. Neither K nor L is automatically certified. Arbitrary-controller CORE-ONLY partitions need no controller FEI hypothesis for the sign, but their complete terminal entropy still has to be paid.

## Sharpness is witnessed by actual Boolean shared-core children

At p=1/2, R_dd<0 everywhere on (d_star,1/2). Therefore no larger uniform initial bias interval has this convexity property. For any interval extension, select distinct dyadic d0,d1 inside its overlap with (d_star,1/2), realized as nested negative sets on a COMMON finite core. Add one selector core coordinate with children g,h and one independent dictator control. Strict concavity gives a positive signed activation correction. Both children are nonconstant, and the selector is proper. This is an actual Boolean witness, not a vector proxy.

A fixed certificate below uses 4 shared child-core bits with nested negative sets of sizes3 and4 (biases3/16 and1/4), one selector and one dictator control. Its signed correction is R(1/2,7/32)-(R(1/2,3/16)+R(1/2,1/4))/2>0. Exact prime-log rational intervals certify it. It refutes only the helper 'all children with negative probability<=1/4 have nonpositive activation surcharge'; it is not an FEI counterexample.

## First unsupported line

Produce for every Boolean core a proper projected tree with paid core decrement K, paid actual terminal allowance L, and either this safe band at each live core query or a NONRENEWING certified child surplus paying the first band exit. The low-bias first-query guarantee alone does not supply K or L. Rare gates retain their encoded core difficulty. At an exit, exact signed correction R(parent)-average R(children) must be used, not the refuted unsigned rp epsilon renewal. Shared core/controller variables remain outside the representation.
