# One early occupancy query and its continuing profile, from the same source

Uniform Boolean signs, base-two entropy, full normalized Fourier labels and
physical uniform-cube influences. Fix m>=2, A=2^-m, d=A^2, u=1+d, v=1+2d.
The source is the canonical b_m=(-1)^(sum_j Y_(2j-1)Y_(2j)),
c_m=b_m-2*1{w=0,Y=0}; G_m has original z terminals b_m,c_m of reach1/2.
Every reference is ONLY a marginal of original Q_c. Original old debit D,
S2, r=S2-D>d/8 and I_X=m+(2m+1)d/2 are those of the independently reviewed
A067 source. Choose rate3 ONCE at that source: residual r3=r+I_X.

## 1. Exact history and the previously paid invoices

Complete H quadratic pairs along the edited all-zero path as in the preceding
A088 stage: query a, stop a=1, query b on a=0, stop b=1 and continue00.
Here 0<=H<=m. Query physical w at that actual inherited state, retaining its
full w=1 clean exit, and continue on w=0. Complete T-H further pairs on that
edited zero path, stopping the two clean exits of each block, H<=T<=m.
All earlier clean exits and the original b_m sibling are retained. No query
is made inside a stopped clean exit. Pair permutations/swaps preserve the
canonical phase and origin. The w query may occur before any pair or after
every pair, but occurs once. There is no reset or new source.

Write j for the number of already completed pairs, B=2^j A=2^(-(m-j)),
alpha=A/2^j, with alpha B=d. Before w, the active original reach is
1/(2*4^j), and its actual and inherited spectra are

 P_j(W0,sigma)=B^2(1-Bsigma)^2,  P_j(W1,sigma)=B^4,
 Q_j(W0,sigma)=B^2(u-2alpha sigma), Q_j(W1,sigma)=B^2d.      (1)

The k=m-j bent signs have counts (4^k +/-2^k)/2. The previous complete
proof, A088 run20261023T070855Z PROOF2--5, gives cumulative pre-w CE
debit E_Q,pre<=0 and clean-exit KL bound
(5/12)(1-4^-H). That proof is author-checked, pending independent review;
we do not silently label it accepted. Its load-bearing moments are
M0=2alpha(alpha-B)/(u^2-4alpha^2)<=0 and
M1=2alpha^2(1-3B^2+4B^3alpha/u)/(u^2-4alpha^2).
For j=0, M1=2d/u; for j>=1, M1<=(32/15)alpha^2. Applying ln x<=x-1
and ln2>2/3 pays the first block by<-9d/4 and each later block
by<-59d/20 at their ORIGINAL reaches. Both children and every stopped
sibling occur in that argument. The present checker separately reconstructs
these complete CE decrements from the original-law states.

## 2. Pay the actual positive w profile once

At j=H the w influence is B^2. Its two physical children are b_k (w=1)
and b_k-2*1_origin on Y alone (w=0). The SAME new reference for both is

    Q'_j(sigma)=B^2(v-2alpha sigma).

The complete CE drop, including BOTH actual child bills, is

 Lw=sum_sigma n_sigma [B^2(1-Bsigma)^2 log2((v-2alpha sigma)/(u-2alpha sigma))
                       +B^4 log2((v-2alpha sigma)/d)].      (2)

Every denominator u-2alpha sigma>=(1-A)^2>=9/16. Since ln(1+x)<=x and
ln2>2/3, the first part of (2) is less than(8/3)d(1-B^2)<=(8/3)d.
For the second, v+2alpha<=1+2A^2+2A<=13/8<2, so it is strictly
less than(2m+1)B^2. Thus the ROOT-WEIGHTED rate-three w charge obeys

 W_H=(Lw-3B^2)/(2*4^H)
    < (4/3)d/4^H+(m-1)d
    <= d(m+1/3) <=7/48.                                 (3)

For the last bound, (m+1/3)4^-m decreases for m>=2, and at m=2 is7/48.
This is an explicit once-only occupancy-query allowance from the original
increment I_X. It is not an assertion that w has nonpositive CE charge.
The preceding stage proved early w has POSITIVE rate3 debit before any
pairs; that obstruction is retained, and (3) pays it instead of denying it.

## 3. The changed nonempty profile after w=0

For every subsequent completed state j>=H, there is no remaining w label.
Original reach is 1/(4*4^j). Actual and original-marginal laws are

 P'_j(sigma)=B^2(1-2Bsigma)^2,
 Q'_j(sigma)=B^2(v-2alpha sigma).                         (4)

These are normalized: mean sigma under all k-pair labels is B, and
alpha B=d. Formula(4) is derived from actual restrictions and summation
of the same original reference, not supplied as a new child spectrum.
At j=m both laws are point mass1 on the empty label: the edited completion
is the constant-1 function, with its full terminal CE/KL equal0.

For a next pair (k>=1), remaining-pair signs sigma have mean2B. After a=0,

 P_a(b0,sigma)=4B^2(1-2Bsigma)^2, P_a(b1,sigma)=16B^4,
 Q_a(b0,sigma)=2B^2(v-2alpha sigma), Q_a(b1,sigma)=2B^2v,
 Q_ab(sigma)=4B^2(v-alpha sigma).                        (5)

Physical Boolean marked edges give Inf_a=1/2+2B^2 and Inf_b|a0=4B^2.
These differ from the pre-w values and are not inherited by assumption.

For either query, its complete CE drop is L=sum P log2(Q_marg/Q).
Writing M=sum P[Q_marg/(2Q)-1] gives L<=1+M/ln2. Direct finite sums of
(4),(5), with their exact sign counts, give

 M0=2alpha(alpha-2B)/(v^2-4alpha^2)<0,
 M1=2alpha[-Bv+alpha(1-4B^2)+16B^3alpha^2/v]/(v^2-4alpha^2)<0.    (6)

To check the second sign, alpha<=B and B<=1/2 imply

 -Bv+alpha(1-4B^2)+16B^3alpha^2/v
 <=-B(1+2d)+B(1-4B^2)+16B^5/v
 =B[-2d-4B^2(1-4B^2/v)]<0,

since 4B^2<=1<v. Thus BOTH post-w CE drops are strictly less than1,
even though conditional equality with the inherited reference is absent.
The paired ORIGINAL-reach rate-three debit is strictly less than

 (1/(4*4^j))[1+1/2-3(1/2+2B^2+(4B^2)/2)] = -3d.        (7)

All further selected paired continuations therefore add negative CE credit
at the same original rate. Combining (3), pre-w credits and (7), the ENTIRE
cumulative CE debit at every (H,T) cut is E_Q(H,T)<7/48. This is not a
separate funding allowance per block. The earlier debit is part of this sum.

## 4. One full terminal KL bill, including all old siblings

Before w, stopped first-one exits have KL<1, second-one exits KL<1/2;
their entire old contribution is<(5/12)(1-4^-H). At w the clean b_k exit
has P/Q=1/(v-2alpha sigma)<=8/5<2, hence KL<1; its original reach is
1/(4*4^H). This retains its complete entropy and reference alphabet.

After w, the new first-one exits have ratio2/v<2, KL<1. New second-one
exits have ratio1/(v-alpha sigma)<=8/7, KL<1/2 since(8/7)^2<2. Their
original reaches at block j are 1/(8*4^j),1/(16*4^j), respectively.
At the active post-w state, (4) satisfies P'/Q'<=2*4^T: cancel the common
cross term and the required inequality is 1+4B^2<=2*4^T(1+2d), or1<=2*4^T.
Thus its full KL<=1+2T, at original reach1/(4*4^T).

Adding EVERY terminal gives

 K_F(H,T)<(5/12)(1-4^-H)+1/(4*4^H)
           +(5/24)(4^-H-4^-T)+(1+2T)/(4*4^T)
         =5/12+4^-H/24+(1+12T)/(24*4^T)
         <=19/32.                                      (8)

For the last inequality, 4^-H<=1 and (1+12T)4^-T has its integer maximum
13/4 at T=1 (its T=0 value is1 and it decreases for T>=1). Strictness
comes from actual clean-exit bounds, including H=T=0. The unchanged
original b_m terminal has KL0. Individual inherited terminal banks may be
negative; none is clipped or independently re-certified.

## 5. Original reserve after all previously booked costs

From (3),(7),(8), complete actual entropy debit is

    E_H(H,T)=E_Q(H,T)+K_F(H,T)<7/48+19/32=71/96<3/4.

Therefore the single ORIGINAL increment I_X pays this whole history,
after unchanged old D, with remaining reserve

    R(H,T)=r+I_X-E_H(H,T)>m-71/96.                      (9)

If the incoming cut had already booked E_H,pre(H), its actual remaining
account was R_pre=r+I_X-E_H,pre(H). The new charge is EXACTLY
E_H(H,T)-E_H,pre(H), so (9) is R_pre minus that charge. No initial bank
is renewed and no old invoice is erased. Using the full original reference,
S_Q(final)=S3+E_Q and S_H(final)-(D+E_H)=r+I_X. The latter telescope is
existing background; the new funding is the quantitative bound(9).

Legacy rate-two invoices remain explicitly. Original-reach removed influence is

 J(H,T)=1/3-4^-H/6-4^-T/6+(T+1/2)d <1/2.

This adds the old pre-w influence, w's original weighted d/2, and every
post-w physical query. Indeed (m+1/2)4^-m<=5/32<1/6, m>=2.
Hence E_H,rate2=E_H,rate3+J<119/96<5/4, also smaller than I_X>m>=2.
These are alternative representations of the SAME old invoices, not two
new reserves. The rate3 source was chosen once before the history.

## 6. Booleanity test and first unsupported universal line

The actual canonical phase/marked jet establishes (1),(4),(5) and the
physical influences. The new payment step (6) is rational likelihood algebra,
not an estimate enforcing all Boolean phase-convolution equations. For a
proper history avoiding one quadratic pair R, the real orthogonal filter
Id-2 E_R commutes with all queries INCLUDING early w, preserves every
actual restricted norm, squared Fourier spectrum, full marginal reference
and Dirichlet influence, and destroys Booleanity. A literal m=3 guard at
H=0, w exposed, T=1 tests nine actual root/child nodes. This is stronger
than a formal nonBoolean probability relaxation. It does not claim that the
full all-pair history admits such a commuting real filter after R is queried.

The first unpaid continuation is now a physical data query inside a stopped
clean exit with inherited nonflat reference, or a different noncanonical
Boolean core whose actual incident phase does not give the moment signs(6).
The arbitrary-core source supplier remains unpaid. An all-dimensional FEI
claim would first need a universal replacement for these phase-specific
moments/source pricing. NEXT should test one actual retained-exit query
from the diminished account(9), preserving D,J and all terminal KL; a new
no-reset telescope, a renewed source or another class H/I bound would not
close that universal gap. Full FEI remains OPEN.
