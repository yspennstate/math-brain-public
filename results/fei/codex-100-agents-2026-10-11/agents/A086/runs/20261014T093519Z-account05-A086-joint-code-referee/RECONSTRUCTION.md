# Independent joint-reference audit, stage 6

All costs below are ideal bits, physical influences use the uniform cube, and the single global integer-code rounding allowance is separate. Verdicts apply to the source statements, not to their unproved universal extensions. No author checker was imported. Our arithmetic helper is our own prior implementation; our new checker enumerates actual truth tables, physical restrictions and edges.

## 1. Arbitrary-core envelope reconstructed

Write p=2^-r, t=2^-n, a_T=hat(g)(T), and b_T=g(y*)chi_T(y*). Expanding the actual point edit gives Fourier coefficients a_T-2pt b_T at control frequency zero, and -2pt b_T times the control-point phase at every other frequency. Summing their squares gives

q_T=a_T^2-4pt b_T a_T+4pt^2=(a_T-2pt b_T)^2+4p(1-p)t^2>0.

Young's inequality 4pt|a_T|<=a_T^2+4p^2t^2 and p<=1/2 imply q_T<=2P_g(T)+6pt^2. Set beta=6pt. Rdag=(R+beta U)/(1+beta) has mass M=(s+beta)/(1+beta), and every entry is positive and at most one. Lift it by the ACTUAL conditional control law K, not by an envelope-component sampler. Q=Rdag K has that same mass, CE=CE(q,Rdag)+B, and D=D(q||Rdag). D is the unnormalized-reference divergence, including missing mass.

Because -log Rdag>=0, pointwise domination can be integrated. On the source support Rdag>=R/(1+beta); everywhere Rdag>=beta t/(1+beta). Thus

CE(q,Rdag)<=2c+(2+beta)log(1+beta)+beta[n+log(1/beta)].

Using log(1+beta)<=2beta, beta<=3/2, and log(1/beta)=n+r-log6 gives the upper bound 2c+beta[2n+r-log6+7]. To bound B, designate a nonzero-control-frequency event. Its probability is w=4p(1-p)t. Conditional on that event, there are at most 2^r-1 control frequencies; hence B<=h2(w)+wr. Here w<=t<=1/2 and h2(w)<=w log(1/w)+2w. Since log(1/w)=n+r-2-log(1-p) and -log(1-p)<=1<=r, this gives B<=w(n+2r-log(1-p))<=w(n+3r). For the sharper required bound, instead bound the conditional nonzero-frequency entropy by log(2^r-1)=r+log(1-p). These logarithms cancel exactly, giving B<=w(n+2r)<=4pt n+8rpt. Combining gives

CE<=2c+pt[16n+14r+42-6log6]<=2c+30pt(n+r).

The last inequality follows from log6>=2 and 14n+16r>=30. Physical point-edge surgery gives C=2pt(n-d), E=2ptd, J=2rpt and I_F=I_g+C-E+J. Therefore CE<=2c+15(C+E+J). At rate K>=15 this yields precisely S_K-c+(K-15)(C+J)-(K+15)E as a lower bound on KI_F-CE. The d incident pivotal edges are distinct, so I_g>=2td and E<=pI_g<=I_g/2. Substitution of c<=C0 I_g proves rate K=4C0+15. If I_g=0, the conditional admission requires c=0; no positive-cost constant source is admitted. This is one-operation closure, and repeated use increases the rate.

## 2. Incoming mass, decoding and expectation

For a physical coordinate j, let P_b be the two actual child spectra; their fair average is the deleted-coordinate marginal m of P. Let r be the corresponding marginal of the incoming Q, whose mass is M. On m>0 choose pi_b=P_b/(2m); on m=0 choose a normalized pair of posteriors. Retain r even there. Define raw_b=2r pi_b, Z_b=sum raw_b and R_b=M raw_b/Z_b. Each Z_b>0 by support and normalization of P_b, Z_0+Z_1=2M, and each child model has mass M. On every positive child atom,

P_b/R_b=(m/r)(Z_b/M).

Let L be the conditional divergence of the true queried spectral bit against Q's queried-bit kernel. Chain disintegration gives D_parent=D(m||r)+L, while averaging the displayed likelihood gives avg D_child=D(m||r)+avg log(Z_b/M). Thus

CE_parent=avg CE_child+Delta+L-avg log(Z_b/M),

where Delta=H_parent-avg H_child. Jensen and the EXACT sum of normalizers show L-avg log(Z_b/M)>=0. Iterating with original physical reaches telescopes to the same original cost; this signed ledger need not bound each child cost by its own influence. References and normalizers can differ between query orders. No new bank is created.

For an independent terminal P_h and prescribed R_h, choose pi on reference-only product fibers to be the retained core posterior, even when P_h vanishes. Then raw and Z factor, Z_product=M_h Z_core, M_product=M_h M_core, and R_child=R_core,child tensor R_h. All CE and D contributions of h are additive; all of its missing and off-support mass survive. This covers normalized and subprobability terminal models.

These claims construct finite positive-support reference distributions, not a rejection sampler with possible nontermination. Finite target support and positive reference mass on it permit complete prefix coding with ideal expectation CE and one separate +1 rounding allowance. Off-target symbols consume reference mass. Multiple analytical component labels do not identify multiple physical witnesses or supply an extra entropy credit; our atom-level likelihood checks never deduplicate them by dropping mass. No fresh conditional code or normalizer is silently substituted in the final expectation.

## 3. Weak unequal-amplitude two-query stress, every even k>=2

Take quadratic bent_k times g_AND3, add one dummy and one point selector, and edit at bent-coordinate weight k/2 inside the negative AND cell with dummy zero. Put n=k+4 and t=2^-n. The original data influence is k/2+3/4. Edge surgery gives C=t(k/2+1), E=t(k/2+3), J=t, and root influence I_g-t. Uniform data reference has cost c=n, and its true-selector lift has cost n+B. The previous conditional-event argument gives B<=nt+4t=(k+8)t. Consequently its rate-four margin is at least k-1-(k+12)t>0: at k=2 this is 25/32, and the subtracted term decreases thereafter. The single original reserve is S4=k-1.

For the entropy decrements use phi(u)=-u^2 log(u^2), phi(0)=0, and

G(w)=phi(w+1)-[phi(w)+phi(w+2)]/2.

Its triangular second-difference representation has total weight one and integrand 2log|w+1+s|+3log(e), -1<=s<=1. Also G(0)=4. For |w|>=4, |w+1+s|>=|w|/2; since ln2<3/4, this gives G(w)>2log|w|+2 (endpoint equality does not affect the strict integral). The edited-minus-source scalar step is z=t at the first weak query. Half the old coefficients are zero and contribute G(0); the other half have |a/z| equal to 4*2^(k/2) or 12*2^(k/2), at least eight. Averaging the exact coefficient pairs therefore gives Delta_first>t(k/2+5). Its influence is t and both physical children are nonconstant.

For the second query, the unedited branch contributes zero decrement. In the edited branch z=2t; all the remaining source coefficients are nonzero and |a/z|>=2*2^(k/2)>=4. The same integral yields Delta_edited>2t(k+4). With reach 1/2, total Pi_H>t(3k/2+9); total removed influence is 2t, giving price >3k/4+9/2. The true function is symmetric in the two weak point bits, so this true-entropy argument holds in either order. Inherited models are transported separately and no reference symmetry is assumed. All four leaves are nonconstant (three retain g, the fourth has its point flipped). Section 2 implies the whole-query ledger is at least the true decrement. The complete four-leaf bill plus ledger equals n+B, paid once by the original reserve; no descendant renewal is used.

## 4. Paid-root descendant obstruction, every n>=2

Now use source g=-1 on active-bit zero and +1 on active-bit one, with n-1 dummies and one fresh fair point-control. Edit its full negative zero point. P_g=delta_A, I_g=1, t=2^-n. Prescribe R(A)=1/2, R(empty)=0, and all other R(T)=1/[2(2^n-2)], so c=1. The actual marginal is q=(1-2t)delta_A+2t U_n. The floor R'=(1-2t)R+2t U_n is normalized and positive. Here calibration does nothing because the true and reference vacuum are zero. The A097 negative-cell floor cost CE<=1+10(n+1)t is the exact accepted source-bound dependency, not an assumption of cheap descendants; its complete proof is reconstructed in A094 AUDIT sections 1-3. This bound also pays the root at rate12.

The active physical query has influence 1-t. Its positive child is constant; its negative child is h=-1+2 point_zero on n bits. Write qA=1-2t+2t^2, rA=(1-2t)/2+2t^2. Exact marginalization of the SAME incoming Q gives rv=t^2+rA(1-t)^2/qA, Z_positive=rv/qA and Z_negative=2-Z_positive. Section 2 then yields

R_negative(empty)=(1-2t)^2 rv/(2qA-rv).

All denominators are positive. Put N=t^2 qA+rA(1-t)^2. The strict inequality R_negative(empty)<1/3 is equivalent to positivity of

2qA^2-[1+3(1-2t)^2]N=2t[3-18t+51t^2-79t^3+66t^4-24t^5].

On u=4t in [0,1], the bracket's degree-five Bernstein coefficients are 3,21/10,243/160,145/128,557/640,11/16, all strictly positive. Our checker reconstructs them from the power coefficients using exact rationals. This proves the inequality for every n>=2, not just the tested dimensions.

The true vacuum is (1-2t)^2. For n>=3 it is at least 9/16. Since log3>1, CE_negative>9/16, while I_h=2nt. Hence CE_negative/I_h>9*2^n/(32n), diverging. In contrast H_h<4I_h: nonvacuum coefficients have squared mass 4t^2, giving nonvacuum entropy <=4t(2n-2), and the vacuum contribution is at most 4t/ln2. Division by 2nt gives 4-4/n+2/(n ln2)<4, since ln2>1/2. This is an inherited-reference obstruction, not a Boolean FEI counterexample.

The whole root bill is paid once by the strong query: (n+1)2^-n<=3/4 and 1-t>=3/4 imply CE_root<=1+10(n+1)t<=(34/3)(1-t). Section 2 retains complete leaf costs and arbitrary independent terminal CE/D outside this core account. Neither this owner nor a terminal's cheap structural model authorizes a renewed descendant reserve.

## 5. Verdict and exact remaining line

A011-POINT-EDIT-GENERAL-ENVELOPE-ONE-USE-HISTORY@1 HOLDS at full stated scope. A094-INCOMING-PAID-FLOOR-DESCENDANT-SHOCK-AND-OWNER@1 HOLDS at full stated scope, using its explicitly accepted A097 floor dependency, with the shock, normalization, owner bound and terminal rule independently reconstructed here. No substantive repair to either source was needed. A094's full independent acceptance of our preceding neutral floor is adopted, not self-reviewed or counted as a new result.

The universal unsupported line is a FIXED-rate one-use payment of the extra source cost and erased-edge debit through a selected arbitrary-core history retaining its incoming reference. The envelope's conditional rate4C0+15 inflates under repetition. A paid root does not supply an influence-priced child reference; a weak query does not supply a constant local entropy price. The explicit bent history has a bank, but there is no universal method furnishing that bank on every Boolean core.
