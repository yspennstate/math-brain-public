# Stage20 working derivation: exact noninvariant orbit invoice

All logarithms are base two. Let a finite group act on a finite label set, with orbit partition O. Let P be an actual probability distribution and Q a normalized reference supporting P. Write Qbar for the average of the pushforwards of this ORIGINAL Q. For each orbit A with P(A)>0 let p_A=P(.|A), q_A=Q(.|A), and u_A be uniform on A. Then

CE(P,Qbar)-CE(P,Q)
 = sum_A P(A) [D(p_A||u_A)-D(p_A||q_A)].                 (1)

Proof: Qbar(s)=Q(A)/|A| on A. The pointwise log ratio is log(|A|q_A(s)); summing against P gives (1). No Booleanity, invariance, fresh source, or change of orbit mass is assumed. In particular the conversion debit is at most

Phi(P)=sum_A P(A)D(p_A||u_A),

and this bound is sharp over normalized supporting Q, by taking Q conditional profiles equal to P conditional profiles (zero probabilities are permitted away from supp P). Empty orbits of P contribute zero. If strict positivity is required, the same upper bound is a supremum by a positive approximation. When P is orbit invariant Phi=0, recovering the free invariant return. For noninvariant P the mismatch term is a real credit; discarding it can waste the original account.

For joint actual spectral P(s,t) and product reference Q(s) C(t), converting only Q to Qbar gives exactly (1) for the s marginal, irrespective of s,t dependence. Thus the control FULL bill cancels exactly; it has not been discarded.

At a node with original signed account a=K I(f)-CE(P_f,Q), conversion gives a'=a-Delta. For a frontier with reaches pi, all prior query debits retained, conversion changes its total balance by exactly -sum pi Delta. Thus sum pi Phi<=unused original balance is sufficient, and the exact necessary/sufficient condition is sum pi Delta<=unused original balance. This is an accounting identity, not a proof that the sufficient condition holds universally.

## Rank-local source return, frozen bounded blocks

Partition physical coordinates into blocks of size at most b. The product of GL(B,2) acts on frequency labels independently in each block, fixing the empty label there. Its orbits are indexed by active-block sets J: all frequency sets S meeting precisely those blocks. Orbit size is product_{B in J}(2^{|B|}-1). For any Boolean f,

Phi(P_f) <= E_{S~P_f} log |orbit(S)|
 <= sum_B log(2^{|B|}-1) Pr(S meets B)
 <= b E|S| = b I(f).                                  (2)

Consequently ONE conversion of an ORIGINAL paid full reference CE(P_f,Q)<=c I(f) yields the actual averaged source Qbar with complete bill <=(c+b)I(f). This is a rank-reference source regularization for arbitrary Boolean f; it does not assert a universally paid original source. More sharply, use the exact Phi or exact signed Delta in (1), rather than b I.

Every physical frequency marginal of Qbar remains invariant under the product GL of the remaining coordinates of each block. To prove this, extend any invertible linear map on the remaining coordinates by identity on erased coordinates. It commutes with erasure, and Qbar is invariant under that extension. Therefore a second averaging of any inherited marginal over any such residual group changes it by EXACTLY ZERO. The statement holds along every adaptive coordinate-query path. It regularizes conditional shape, but does not calibrate vacuum/occupancy masses or pay physical query/channel costs. No renewed bI charge is taken at descendants.

## Necessary NONINVARIANT return with a real paid prefix, SAME K

This extends A066's consumed stage10 invariant Maj3 transaction, rather than claiming it as new. Take h=Maj5, independent arbitrary Boolean core g with a SUPPLIED original complete Qg of cost Cg<=K Ig, integer K>=4, and F=t*x*h*g on disjoint coordinates. Let M=31, epsilon=2^(-3K). On the 31 nonempty h-frequency labels prescribe ORIGINAL q(A0)=1-30epsilon for A0={1}, and q(A)=epsilon elsewhere; q(empty)=0. The actual h spectrum has SIX atoms of weight9/64 (five singletons and the five-set) and TEN atoms of weight1/64 (three-sets). Thus Ih=15/8, w=P_h(A0)=9/64, and

c=CE(P_h,q)=165K/64 -(9/64)log(1-30epsilon),
165K/64<c<165K/64+9/64.                              (3)

The upper bound uses 30epsilon<1/2. The spectrum is genuinely noninvariant under GL5: a linear frequency transvection sends a positive singleton to a zero two-set. Full GL5 averaging of THIS q gives qbar uniform on the 31 nonempty labels; the new cost is log31, not H(h). In particular the positive target defect Phi=log31-H(h) has NOT been omitted. Formula(1) gives its exact payment against the legitimate conditional mismatch credit: Delta=Phi-D(P_h||q)=log31-c<0.

Keep the original owner A=K(Ig+31/8) and an eligible old booking tau=(K Ig-Cg)+1/4. This is an explicit booking hypothesis/encumbrance; no unnamed old policy is certified. The initial full reference is delta_{t,x} times q times Qg. After the actual t query both physical children have the SAME squared spectrum and full cost Cg+c, and the actual influence invoice is K. With tau kept, the remaining owner is

S_before_x=23K/8-c-1/4>(19K-25)/64>=51/64>0.          (4)

Literal x completion with the unchanged source would give

S_literal=15K/8-c-1/4<0.                              (5)

Both queries are isospectral, all means/vacuum masses are zero, and all singleton/nonempty phase-change terms are zero. Vacancy calibration cannot refund anything. Some nonempty source change is necessary for this specified same-rate x continuation with tau retained; this is NOT necessity for all FEI proofs.

Before x, average the inherited ORIGINAL q under GL5. The exact legitimate refund is c-log31. The SAME original balance after the full x query and BOTH full terminal bills becomes

S_final=15K/8-log31-1/4>15K/8-21/4>=9/4.              (6)

At the conversion node its balance is K+S_final, so there is no temporary overdraft. The exact original-owner conservation equation is

A=2K+(Cg+log31)+tau+S_final.

The core reference is untouched. Signs of t,x and g do not alter the squared spectra or complete bills. No extra influence, phase energy, occupancy ghost credit, normalization refund, fresh supplier, or restarted rate is used. The source has 15 zero-actual-weight nonempty labels before AND after the change; their legitimate source mass is explicit in the complete cost, and is never treated as a payer.

The same proof gives a conditional general criterion: for any balanced Boolean h with J=Ih, supported on one nonempty orbit of size M, with the ORIGINAL supporting reference ALSO normalized on that same orbit (total source mass there exactly1), if its cost c satisfies KJ-1/4<c<K(J+1)-1/4 and log M<KJ-1/4, then the same t,x continuation is insolvent unchanged and is paid by orbit return, with final balance KJ-log M-1/4. If the source has only mass qO on that orbit, the target bill is log M-log qO instead, and every displayed target-capacity condition must retain that normalizer. Actual invariance is unnecessary. These are genuine source/capacity hypotheses, not a theorem that arbitrary cores satisfy them.

## First unsupported line toward universal FEI

There is no proof here that the exact noninvariant invoice of a necessary unbounded-orbit return is paid by the SAME unused original ancestor balance after all old debits and both full terminal costs. Also no arbitrary-Boolean initial paid source is supplied. Formula (2) is useful with bounded blocks but cannot silently replace b by an absolute constant when block size grows. The sharp character guard below tests that limitation.
