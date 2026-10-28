# Original source ownership: all nonconstant capacity is already in B

Work in bits. Let A be ANY event, p=Pr(A) in(0,1/4], with independent sign u, h0=u and h1=(1-A)u+A. Select by q and activate at a fresh gate using the exact mean1/2 nonlinear two-bit mask. Original Qb=(P_hb+delta_empty)/2, q-parent conditional lift, and prescribed complete activation lifts are as in stages18/19. Write c1=CE(P_h1,Q1), H1=H(h1), J=I(1-2A), c0=1. Then

B=7/4-p+J/2-c1/4,
4I(F)=6+J/2-p/2.

Let eta(x)=-x log2 x, f(p)=eta((1-p)^2), phi(b)=Psi(b/2), and Aref(a,z)=[a log2(a/z)+(1+a)log2((1+z)/(1+a))]/2. Psi is the exact gate entropy profile from preceding stages. Put

Delta(p)=f(p/2)-f(p)/2+eta(p^2)/4+2p-p^2/2,
D(p)=p^2/2 log2((2+p^2)/(1+p^2)),
R(p)=Aref(p^2/16,(2+p^2)/32).

Actual Fourier rows give H(h)=H1/2+Delta(p). Nonempty data rows have Qb=P_b/2 and therefore zero label-KL loss; the EMPTY row alone gives D(p). Hence parent core CE=(1+c1)/2+Delta(p)-D(p), and full root CE is

Croot=5/4+c1/4+Delta(p)/2-D(p)/2+phi(p/2)-R(p).

Thus the ENTIRE actual root surplus W=4I(F)-Croot decomposes exactly as

W=B+Omega(p),
Omega(p)=3+p/2-Delta(p)/2+D(p)/2-phi(p/2)+R(p).

In particular no event dimension, entropy or influence remains outside B. This is an ownership identity, not a claim that B and W can both be spent. A newly proposed J/2 credit is already included in B.

Delta>=0 by Fourier marginal entropy/concavity. D(p)<p^2/2. With V=2-phi convex and V(1)=a=9log2(3)/8-1<1, phi(p/2)>=2-p/2. Since 0<=p^2/16<z=(2+p^2)/32<=33/512, R(p)<=Aref(0,z)=log2(1+z)/2<1/16; certify545^8<2*512^8. Therefore

Omega(p)<17/16+p+p^2/4<=85/64.

For every original old debit U, W-U=B-U+Omega(p); no unused part of THIS complete original root surplus can exceed85/64. This is not a lower bound on arbitrary local inherited surplus after influence retirement.

The COMPLETE first q-query excess Tq also depends ONLY on p. Explicit child costs are C_u=7/2-Aref(0,1/8) and C_A=1+c1/2+phi(p)-Aref(p^2/4,(1+p^2)/8). Define Tq=Croot-(C_u+C_A)/2-p. The c1 terms cancel. Moreover Tq<1/4 uniformly for ALL event geometries with p<=1/4. Proof: exact radial ledger gives Tq=Delta(p)/2-p+curvature+Lambda. The first term equals [f(p/2)-f(p)/2]/2+p^2(log2(1/p)-1)/4. On[0,1/4], |f''|<12 gives the first summand<3p^2/4<=3/64. The second is increasing in p<=1/4 (ln2>1/2), hence<=1/64. Profile curvature<=a*p/2<1/8. Radial mean contrast nu1/2 gives Lambda<=log2(290/273)/2<1/16, certified290^8<2*273^8. Therefore Tq<1/4. This extends the previously checked dyadic point-density full bill to every Boolean event at these densities.

Consume A019-NO-NEW-INFLUENCE-TENSOR-OBSTRUCTION@1: for k8,m16384 the SAME B and full original-marginal event-query bill S obey B-S<-2, with genuinely eligible initial cores and root. Therefore even replacing B by the ENTIRE original root surplus W cannot fund that SAME no-later-credit expense ledger:

W-U-(Tq)_+-S < -2+85/64 = -43/64 for EVERY U>=0.

This is a source-ownership obstruction, not an FEI disproof or a failure of an arbitrary influence-retiring signed potential. It rules out rescuing this specific complete expense ledger merely by discovering an unused part of the original root slack: all of it was included in W. Both full endpoints and every query conversion remain in S. A different potential must change which influence is retired and which descendant costs remain obligations, rather than re-add J/2.

## The corrected physical retirement account, retaining all endpoints

The negative expense ledger above is NOT the physical signed reserve. Complete event-query CE release S is a CREDIT in that reserve, and its original event influence J/2 is retired exactly ONCE. If ALL event bits are queried with every outcome retained, then

W_finish=W_root+Tq+S-J/2-U.

Here EVERY event coordinate is queried, including any physically irrelevant coordinates left after A is determined. Indeed after the q query the exact signed change is Tq; after event queries it is S-4*Pi_event, and 4*Pi_event=J/2. The equality follows either by physical influence conservation or by summing the original event-bit influences through their disjoint reaches. It is not permission to add a new J/2 to B. The terminal average is explicitly

W_finish=6-3p/2-[C_u+L]/2-U,

where q0 retains its complete original code C_u and L=(1-p)C_u,final+p*C_const,final. The final q1 core marginal is ((1+p)/2,(1-p)/2). Its u cost is log2(2/(1-p))<=log2(8/3)<3/2, so its complete activation cost is<15/4 and its full signed reserve>9/4. The constant core cost is<=1; phi(1)=Psi(1/2)<5/4, so its full activation cost<11/4 and reserve>1/4. The refund Aref is nonnegative also when its second argument is smaller: for fixed first argument a, its derivative in z is (z-a)/(2 ln(2) z(1+z)), with global minimum0 at z=a. The q0 full reserve is>5/2. Consequently average terminal reserve before U exceeds9/4-p>=2; more precisely (5/2+9/4-2p)/2=19/8-p>=17/8. After any SAME old U<=1/8, W_finish>2 for ALL event geometries with p<=1/4. The scalar profile endpoint is integer-certified in CERTIFICATES.json. This endpoint proof needs no tensor independence, no local leaf eligibility assumption and no renewed source influence.

Thus the tensor has BOTH a negative proposed expense ledger, even after all original unused root slack is offered, and a positive complete physical signed reserve. These are different quantities with opposite signs on the CE release S. A prefix can still have negative complete reference deficits, and no universal stopping-prefix bound or influence-priced initial supplier is obtained. The next unpaid line is an averaged prefix potential controlling necessary interacting source conversions before completion, or a new initial reference construction; repeating bounded capacity cases cannot settle it.

Independent review of A019 capacity theorem and tensor bound is reconstructed in REPORT.md; the endpoint/prefix distinction preserves both original results without repair.
