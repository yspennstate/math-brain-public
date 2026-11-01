# Independent reconstruction: phase-bin transfer

Verdict: HOLDS at the stated supplied-reference scope for A096-PHYSICAL-PHASE-FUNDED-NONEMPTY-RESET@1 and A097-NONEMPTY-PHASE-BIN-FUNDED-TRANSFER@1. This is not acceptance of a universal initial supplier. No repair to either mathematical statement is supplied by A098. Fixed-dimensional checks corroborate the proof; they do not prove its quantifiers.

Let a be ternary, b=1-a^2, and h Boolean on independent finite uniform cubes. Write A=ahat, B=bhat, m=Eh, and beta=sum B^2. For any normalized finite-CE R with R(0)=m^2 the full coherent reference is Q(U,0)=(A_U+sigma*m*B_U)^2 and Q(U,T)=B_U^2 R(T) elsewhere. Parseval and ab=0 give normalization. Actual occupied atoms have reference support; deletion preserves that property. No reference-only atom is discarded before its block is explicitly calibrated.

For a seed coordinate j let u_T=hhat(T), v_T=hhat(T+j), T not containing j. The two child coefficients are u+v and u-v. Thus their mean squared spectra equal the deleted parent spectrum. Expanding full cross entropy fiber by fiber gives

 CE(P,Q) = B_j(P) + mean CE(P_child,M_j Q) + D_occ,

where D_occ is the reached binary occupancy KL, nonnegative, including all controller frequencies and the vacuum fiber. This identity is valid for full normalized references; it is not a statement about only conditional tail entropy.

Fix a nonempty-frequency partition before the outcome. Keep every controller/vacuum atom separate, and use blocks (U,W_l) on the nonempty sector. Set q=pi M_j Q, z_plus/minus=pi P_child. Calibration multiplies each atom in a block by its actual block mass divided by its inherited reference block mass. Its exact CE decrease is D(z_tau||q). A zero actual block is set to zero, with zero contribution. Finite CE ensures every positive actual block has a positive denominator. The resulting reference is coherent with seed law Rcal(T)=P_child(W_l)*Rbar(T)/Rbar(W_l) and actual vacuum.

Pinsker in bits follows from log-sum onto {z>q} and the binary second derivative 1/[p(1-p)ln2]>=4/ln2. Consequently D(z||q)>=||z-q||_2^2/(2 ln2). With the SAME q in both outcomes, the parallelogram identity gives mean||z_tau-q||_2^2>=||(z_plus-z_minus)/2||_2^2. The latter vector has vacuum entries 2d B_U(sigma*A_U+m B_U), and nonempty-bin entries 2B_U^2 c_l, where d=v_0 and c_l=sum_Wl u_T v_T. Therefore the average calibration refund is at least

 (2/ln2)[d^2 sum B_U^2(sigma*A_U+m B_U)^2 + E4 sum c_l^2].

Write C=sum A^2B^2, D=sum AB^3, E4=sum B^4. Completing the square proves sum B^2(sigma*A+mB)^2>=Gamma=C-D^2/E4>=0. If E4=0 then B=0, all relevant terms vanish and no division is used. Thus the refund is >=2x/ln2 for x=Gamma*d^2+E4*sum c_l^2. Keeping only vacuum entries recovers A096's x=Gamma*d^2. This rederives the consumed baseline rather than assuming its controller inequality.

At either child let t=beta*(1-m_child^2). For t*x>0 mix its CURRENT conditional nonempty reference with any normalized prescribed target at epsilon=x/(t+x), keeping its actual vacuum and controller factors. On every occupied tail atom the new law is at least (1-epsilon) times the old one, so its signed full CE cost is <=t log2(1+x/t)<=x/ln2. It can be positive. If t=0 or x=0 use no mixture; constants and beta=0 have explicit zero-tail laws. Combining BOTH child costs with the full chain and calibration refund yields

 B_j + mean CE_child,new - CE_parent <= -D_occ - x/ln2.

This proves the source theorem without changing its constants. Multiplication by physical reaches and finite-tree telescoping retains every old debit and all full terminal CEs. Subsequent steps use the CURRENT changed reference. Coherent controller restoration must be an explicit paid block calibration, and controller constants must be recomputed. No arbitrary query policy is declared coherent for free; applications require the source theorem's stated restoration invariant.

For partition optimization, merging same-sign summands increases the squared sum; splitting positive and negative parts of a mixed bin also increases it. Hence two sign bins maximize sum c_l^2. At d=0, Booleanity sum_T u_T v_T=0 gives c_plus=-c_minus and sum c_l^2=(sum_nonempty |u_T v_T|)^2/2. With beta>0, x>0 exactly when the child squared spectra differ. This is the new sector closed by A097, not a bound x>=c*Inf_j.

For the displayed A079 controller, exact Walsh sums give beta=3/8, E4=21/512, Gamma=9/3584. The balanced seed x3 times a two-bit point defect, queried at its first bit, has d=0, c_plus=1/4, c_minus=-1/4. Thus x=21/4096 and both nonconstant children permit epsilon=7/519. In contrast parity3 with R=P has erasure, occupancy KL and every partition-calibration refund zero, while a 1/64 mixture to a distinct nonempty point costs (3/8)log2(64/63)>0 on each complete child. This boundary survives sign-bin refinement.

## Consequence for resource allocation

A003's mean-offset discrepancy and A004's occupancy/two-bin mismatch results are separately authored refinements read here for routing; they are not newly independently accepted by this review. They explain why zero phase alone is too broad a next target. The exact-source isospectral nullspace remains zero under all such refunds. A033 additionally gives a fixed-strength/local-influence obstruction with encoded-majority seeds, but explicitly does not prove that its off-image target is necessary. The next useful construction must name a needed conversion and its original unused owner, or construct an influence-priced arbitrary-core initial reference. An arbitrary positive target at an exactly matched source is not evidence of FEI failure.

A073's activation nonempty-occupancy refresh proof was read through its full signed ledger. It explicitly covers A050's all-width/all-load same-1/7 second reset, and any finite repetition with x unqueried. That closes a stale task subject to independent review of A073's theorem; it does not cover the next x exposure. Hence the proposed handoff is to review that exact source, then move to x exposure rather than repeat width/load searches.
