# The first occupancy-changing paired block at one globally fixed rate

All logarithms are base two. Fix an integer m>=2 and the canonical Boolean
quadratic b_m(Y)=(-1)^(sum_j Y_(2j-1)Y_(2j)). A dummy w is adjoined. Write
A=2^-m, d=A^2, delta=d/2 and c_m=b_m-2*1{w=0,Y=0}.
The actual G_m z terminals are b_m,c_m, each of original reach 1/2.
On c_m query a=Y1, stop a=1, and query its exposed partner b=Y2 on a=0.
Retain all three resulting c terminals, of original reaches 1/4,1/8,1/8,
and retain the unchanged b_m terminal. Every reference below is ONLY a
marginal of the original full squared Fourier spectrum Q of c_m.

## 1. Source consumption and the rate chosen before the history

Use the prior independently accepted quantities
D=H(G)-(H(b_m)+H(c_m))/2, I_X=(I(b_m)+I(c_m))/2,
S2=2I_X-(H(b_m)+H(c_m))/2 and r=S2-D>delta/4.
For this entire experiment choose rate3 at the original source. Then
S3=S2+I_X and its original residual is r3=r+I_X. The additional reserve
is exactly the once-only original rate increment I_X, not a new child bank.
Old D is unchanged. Since I_X=m+(2m+1)delta, this reserve exceeds m.

Let L0 be the complete CE drop at a with BOTH children using Q1=marg_a Q.
Let L1 be the complete CE drop at b on a=0 with BOTH children using
Q2=marg_b Q1. The original-reach source debit at rate C is

E_Q(C)=(L0-C Inf_a(c_m))/2+(L1-C Inf_b(c_m|a=0))/4.

The old rate-two invoices are retained explicitly: with the ORIGINAL
reach-weighted removed influence J=Inf_a/2+Inf_b/4=1/4+d,
E_Q(3)=E_Q(2)-J and E_H(3)=E_H(2)-J. This is the single stated
upfront rate change, not a hidden renewal at the partner node.

Stage18's conditional-source theorem gives L0<=1. Its Boolean physical
edge calculation gives Inf_a=1/2+d, Inf_b=2d. These identities use the
specified Boolean incident jet; they are not valid for arbitrary real cores.

## 2. A new bound on the positive partner cost

Put u=1+d. Let sigma be a remaining (m-1)-pair Walsh sign, with counts
n_+=(4^(m-1)+2^(m-1))/2 and n_-=(4^(m-1)-2^(m-1))/2.
For W=0 the actual partner-parent spectrum P1 and inherited reference are

 P1(b=0,sigma)=4d(1-A sigma)^2, P1(b=1,sigma)=4d^2,
 Q1(b=0,sigma)=2d(u-2A sigma), Q1(b=1,sigma)=2du,
 Q2(sigma)=4d(u-A sigma).

For W=1 they are P1=4d^2, Q1=2d^2 and Q2=4d^2 for each b.
Their complete CE drop is L1=sum P1 log2(Q2/Q1), including multiplicities.
This expression includes both full child CE bills by the Boolean square
sum identity for physical restrictions; no child is discarded.

Define R=Q2/(2Q1). Since (1-A sigma)^2=u-2A sigma and
sum n_sigma sigma=1/(2A), direct rational cancellation gives

 sum P1(R-1)
 =sum_sigma n_sigma [4A^3 sigma-4A^5 sigma/u]
 =2d/u.

The W=1 terms vanish. Using ln R<=R-1 and ln2>2/3 gives

 L1=1+sum P1 log2 R <=1+2d/(u ln2)<1+3d/u.

This bounds the actual positive occupancy-changing profile, rather than
assuming the intact-coordinate conditional equality persists. Consequently

 E_Q(3)<(1-3(1/2+d))/2+(1+3d/u-6d)/4
       =-3d+3d/(4u)<-9d/4.

Thus a rate fixed at3 at the original source pays this CE block with a
strict negative signed debit. It does not make the partner's individual
debit nonpositive. No reset, renewed quota or clipping is used.

## 3. Full terminal KL is paid separately from original unused reserve

The stopped a=1 leaf is a character on b times b_(m-1), with w dummy.
Its actual/inherited likelihood ratio on its support is 2/u<2; thus its
full KL is <1. The a=0,b=1 leaf is b_(m-1), with w dummy. Its ratio is
1/(u-A sigma)<=16/13, since 0<A<=1/4 and 1-A+A^2>=13/16.
Since (16/13)^2<2, its full KL is <1/2.
At the a=b=0 edited leaf the ratios are 4 on W=1, and

 (1-2A sigma)^2/(u-A sigma)=4-3/(u-A sigma)<4

on W=0. Its full KL is <=2. The unchanged original b_m terminal has KL0.
Therefore the ENTIRE original-reach terminal bill satisfies

 K_F < (1/4)*1+(1/8)*2+(1/8)*(1/2)=9/16.

At the original c_m source KL is zero. Hence the actual entropy debit of
this entire block, with the SAME influence pricing, is

 E_H(3)=E_Q(3)+K_F <9/16-9d/4<9/16.

This debit is positive in the checked m=2,3,4,5 cases; no claim E_H(3)<=0
is made. It is funded by earmarking 9/16 of the ORIGINAL additional
reserve I_X. In particular

r3-E_H(3)>r+I_X-9/16>m-9/16>0.

Even the unchanged legacy actual-entropy invoice is uniformly bounded:
E_H(2)=E_H(3)+J<13/16-5d/4<13/16. Thus its positive cost is smaller
than the originally supplied extra reserve I_X, without deleting any old
rate-two debit. One must NOT infer S_Q(F)=S3+E_Q(2): the exact rate-three
account uses E_Q(3), and its terminal influence increment is I_X-J.

This is an explicit withdrawal inequality for a named original reserve,
with all old debits and full terminal KL retained. It is stronger than
merely rewriting the no-reset identity. Increasing the rate at each future
node would be a different and unauthorized argument.

For completeness, if S_Q(F)=sum_leaf reach*(3I_leaf-CE(P_leaf,Q_leaf)),
then S_Q(F)=S3+E_Q(3). With S_H(F)=S_Q(F)+K_F,
S_H(F)-(D+E_H(3))=r3. These signed identities are background accounting;
the new payment is the quantitative bound and original-reserve withdrawal
above. Signed negative inherited banks remain in these sums.

## 4. Sharpness and the first unpaid line

A088 independently proved e0(2)->0 and e1(2)->1 for these SAME source
profiles, retaining both actual children and original references. Thus
L0->1, L1->1 and Inf_a/2+Inf_b/4=1/4+d->1/4. For every fixed real C,

 lim_(m->infinity) E_Q(C)=(3-C)/4.

No C<3 makes this SAME two-query CE block nonpositive in all dimensions.
This sharpness concerns the source-block debit, not an optimal FEI constant
or the full entropy debit. The full terminal bill tends to1/4, consistent
with the displayed finite checks; that limit is not needed for payment.

The source-specific theorem survives the normalized real phase relaxation
of A088 on an untouched pair: the same squared spectra and physical
Dirichlet energies occur there. We make no claim of a new universal
Boolean-convolution inequality. Its scope is a concrete Boolean edit regime
whose occupancy-changing query was previously unpaid at the frozen rate2.

The first unsupported line for an arbitrary continuing tree is that the
remaining originally earmarked reserve uniformly funds the next necessary
changed-profile block and its full KL after this withdrawal. The first
paired block has a definite paid bill; the process has not been iterated,
and no arbitrary initial-source supplier or full FEI proof follows.
