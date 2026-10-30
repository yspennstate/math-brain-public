# One original rate-three source pays every selected completed-pair cut

Uniform finite Boolean signs, physical bit restrictions, and base-two entropy,
cross-entropy (CE) and KL throughout. The source family is EXACTLY A067's:
b_m=(-1)^(sum_j Y_(2j-1)Y_(2j)), c_m=b_m-2*1{w=0,Y=0}, with a dummy w in b_m;
G_m has z terminals b_m,c_m, each of reach 1/2; m>=2. Write A=2^-m,
d=A^2, u=1+d. Keep the ORIGINAL Q_c and its marginals, original D,
S2, I_X=m+(2m+1)d/2, and r=S2-D>d/8. Choose rate THREE at the original
source only: S3=S2+I_X, residual r3=r+I_X. No later rate increase occurs.

At a completed-pair cut h, continue only along the edited all-zero path.
Choose an intact pair (a,b), query a, stop its outcome-one child, and query b
on outcome zero, stopping b=1 and continuing only a=b=0. Stop after any
h<=m completed pairs; optionally query w after h=m. All exits, original
reaches, signed terminal CE banks and terminal KL remain. Pair/member
permutations are allowed because they preserve the specified quadratic and
the marked origin. No continuation on a clean exit, early w query, reference
reset or arbitrary phase is covered by this statement.

## 1. Independent acceptance of the first-block claim

A067-FIRST-EXPOSED-PARTNER-PAIRED-RATE3@1 has unchanged statement hash
bb00d8df81335aa5ddc86d40198cae1daf754edc077d15bf535aaaf3d74a3b53.
The source proof is reconstructed below, rather than imported as a checker.
At h=0, the first coordinate CE drop L0<=1 follows either from actual/reference
conditional equality or the moment computation below. Physical influences
are Inf_a=1/2+d and Inf_b=2d. The partner moment is exactly 2d/u, so
ln x<=x-1 and ln2>2/3 give L1<1+3d/u. Original weighted rate-three debit is

    E_Q(1) < -3d+3d/(4u) < -9d/4.

The three full c exits have KL bounds <1, <=2, <1/2 and original G reaches
1/4,1/8,1/8. Thus total K_F<9/16 and E_H(1)=E_Q(1)+K_F<9/16-9d/4.
Rate-two invoices remain explicitly E_H(2)=E_H(3)+1/4+d (similarly CE).
The original once-only increment I_X pays this amount after old D. These
are precisely the author's hypotheses and payment; no repair is supplied.
Its sharp threshold3 follows from L0,L1->1 and weighted removed influence
->1/4, hence E_Q(C)->(3-C)/4. This concerns the CE block only.
Verdict: HOLDS at the stated first-block scope, independently reconstructed.

## 2. Actual spectra after completed pairs and original references

At cut h let k=m-h, B=2^h A=2^-k, alpha=A/2^h, so alpha B=d.
The edited function is c_h=b_k-2*1_origin on its remaining pairs and w;
its original G reach is tau_h=1/(2*4^h). Let sigma be the k-pair bent
Walsh sign; its counts are (4^k +/- 2^k)/2. Direct Fourier restriction
and direct summation of the ORIGINAL Q_c give

    P_h(W=0,sigma)=B^2(1-B sigma)^2,
    P_h(W=1,sigma)=B^4,
    Q_h(W=0,sigma)=B^2(u-2alpha sigma),
    Q_h(W=1,sigma)=B^2 d.

The signed two-bit Walsh tuple is (1,1,1,-1)/2. Summing an entire pair's
four reference labels multiplies the constant terms by4 and its cross term
by2. Restricting that physical pair to00 doubles its seed amplitude and
quadruples the point amplitude. This proves the formulas by induction.
They also hold at k=0: P_m is the Fourier point mass W=1 of -chi_w;
Q_m(W=1)=d, Q_m(W=0)=1-d. In particular the final reference is NOT reset.

Before the next pair (k>=1), let sigma now denote the k-1 remaining-pair
sign, with mean 2B under its uniform Fourier labels. After fixing a=0,

    P_a(W=0,b=0)=4B^2(1-B sigma)^2,
    P_a(W=0,b=1)=P_a(W=1,b)=4B^4,
    Q_a(W=0,b=0)=2B^2(u-2alpha sigma),
    Q_a(W=0,b=1)=2B^2u, Q_a(W=1,b)=2B^2d.

After marginalizing b, Q_ab(W=0)=4B^2(u-alpha sigma), Q_ab(W=1)=4B^2d.
Every denominator is positive since alpha<=A<=1/4. The physical influences
are Inf_a=1/2+B^2, Inf_b(c_h|a=0)=2B^2. This uses the nonpivotal marked
incident seed edges of this particular Boolean phase.

## 3. The next two CE drops: conditional equality is unnecessary

At a binary Fourier erasure with incoming actual law P and reference Q,
let Q' be its marginal. The complete CE drop, INCLUDING BOTH physical
child CE bills, is L=sum P log2(Q'/Q). This follows because the mean
of the two actual child spectra is marginal P. Consequently

    L <= 1 + M/ln2,  M=sum P[Q'/(2Q)-1].

Unlike the preceding intact-pair proof, no equality of actual and reference
conditionals is assumed here. Direct finite sums of the profiles in section2 give

    M0 = 2alpha[alpha(1+B^2)-Bu]/(u^2-4alpha^2)
       = 2alpha(alpha-B)/(u^2-4alpha^2) <=0,
    M1 = 2alpha^2[1-3B^2+4B^3 alpha/u]/(u^2-4alpha^2).

For completeness, at the first query only partner Fourier occupancy b=1
contributes to M0: pair the two signs of a, add their rational fractions,
and use 4^(k-1)=1/(4B^2). For M1 pair b=0 and1 and use mean sigma=2B.
These two calculations yield the displayed identities without a logarithmic
approximation. The checker verifies both identities by exact rational sums.

Thus L0<=1 for EVERY completed-prefix state, even though P_h and Q_h
generally have different conditionals. At h=0, M1=2d/u, as in section1.
For h>=1, B<=1/2 and alpha=B/4^h<=B/4<=1/8, so

    u^2-4alpha^2 >=15/16,
    1-3B^2+4B^3 alpha/u <=1,
    M1 <=(32/15)alpha^2 <=(2/15)B^2.

Using ln2>2/3 gives L1<1+B^2/5. Therefore the original-reach rate-three
debit of any subsequent completed block satisfies

    tau_h[(L0-3(1/2+B^2))+(L1-6B^2)/2]
       < tau_h*(-59B^2/10) = -59d/20,       h>=1.

Together with the first block, cumulative CE debit for H completed pairs is

    E_Q(H) < -d(59H-14)/20 <0,             1<=H<=m.       (A)

This is an actual payment inequality for the same inherited profile. It is
stronger than the generic signed no-reset telescope. No owner or rate is renewed.

## 4. One global terminal KL cap, retaining every stopped sibling

The first-one exit of any block is a character times b_(k-1). On its full
actual support P/Q=2/u<2, so its KL<1. The second-one exit is b_(k-1), with
P/Q=1/(u-alpha sigma)<=16/13; since (16/13)^2<2 its KL<1/2.

At the current edited completed-prefix state, P_h/Q_h<=4^h everywhere.
For W=1 this is equality. For W=0, after cancelling the cross terms, the
required inequality is exactly 1+B^2<=4^h(1+d), equivalently 1<=4^h.
Hence its FULL KL<=2h. These estimates include the h=m character case.

The clean-exit original reaches at block j are 1/(4*4^j),1/(8*4^j).
The active reach after H blocks is 1/(2*4^H). Thus the full frontier bill is

    K_F(H) < (5/16)sum_(j=0)^(H-1)4^-j + H/4^H
           =5/12+(H-5/12)/4^H <=9/16.                  (B)

The right side equals9/16 at H=1 and strictly decreases thereafter: its
successive difference is (9/4-3H)/4^(H+1)<0 for H>=1. The clean exits
make the actual bound strict. KL of the unchanged original b_m terminal is0.
Crucially this is ONE bound on the ENTIRE current frontier, not a sum of
9/16 bookings per block and not a refund with terminals omitted.

## 5. Same diminished reserve, old invoices, and the final w

With original-source rate3, original D remains unchanged. Equations(A),(B) give

    E_H(H)=E_Q(H)+K_F(H)<9/16,
    r3-E_H(H)>r+I_X-9/16>m-9/16.

After the first paid block, call the actually remaining original account
R1=r3-E_H(1). For every later cut,

    RH = R1 - [E_H(H)-E_H(1)] = r3-E_H(H).

This keeps the first invoice in place; it does not reissue the original
reserve. Signed credits and all original reaches are retained. With the
full signed frontier bank S_Q(H)=sum reach(3I-CE), one also has
S_Q(H)=S3+E_Q(H) and S_H(H)-(D+E_H(H))=r3. These identities are background;
the withdrawal bound above is supplied by the new moment and KL estimates.

The cumulative removed influence is exactly

    J_H=(1/3)(1-4^-H)+H d,
    E_H,rate2(H)=E_H,rate3(H)+J_H,

and similarly for CE. Thus every old rate-two invoice has an explicit place.
J_H<1/2 for H<=m: H d<=m d and (m+1/2)4^-m<=5/32<1/6 for m>=2.
The unchanged legacy total invoice is therefore <17/16 and also fits the
single original increment I_X>m. These are alternative representations of
the same debits, not two independent charges or funding sources.

After H=m, querying w gives two actual constant children with reference1,
parent CE=2m, Inf_w=1, and original reach d/2. Its signed CE charge is
d(2m-3)/2, which is positive for every m>=2. But(A) already supplies credit:

    E_Q(final) < -d(59m-14)/20 + d(m-3/2)
               = -d(39m+16)/20 <0.

All active KL disappears into the two constant leaves, without discarding
their full bills. Retained clean-exit KL is <(5/12)(1-4^-m)<5/12.
Consequently E_H(final)<5/12. The original reserve and earlier invoices
are unchanged. Even with w, removed influence J_m+d/2<1/2, and the legacy
rate-two invoice remains <17/16. This pays the suggested second pair AND
every further selected pair AND the final positive w query at one original rate.

## 6. Booleanity scope and precise next unpaid line

The specified Boolean quadratic/point jet establishes the exact initial and
restricted laws and physical influences. The new moment cancellation itself
is rational probability algebra; it does not enforce every Boolean XOR
convolution identity. For a proper prefix leaving an untouched pair R,
the real orthogonal operator T=Id-2 E_R commutes with all physical queries
in that prefix and preserves every squared Fourier coefficient, child norm,
full reference and Dirichlet energy, while destroying Booleanity. A separate
direct-character guard at m=3 through TWO completed pairs checks eleven
actual root/child nodes against that normalized real relaxation. This is a
literal real-function test, stronger than testing only formal masses.

The commuting-pair argument does NOT include the final block in which no
untouched pair remains, nor the final w query. Those final profiles are
checked on actual Boolean functions and by the analytic character formulas;
no nonBoolean full-history extension is asserted. Their estimates still
require only the displayed profiles once those are supplied. The full FEI
proof still lacks an arbitrary-core supplier or a universal phase inequality.

The first unpaid continuation of THIS stopped tree is an ordinary query
inside a retained clean exit, or a premature w query before all pairs have
been completed, with the SAME diminished bank and inherited nonflat Q.
Indeed before ANY pairs the actual w influence is d. With Q=P, its full
CE drop is the true binary erasure B_w. The W=1 entries have total mass d,
and every corresponding marginal/entry ratio is at least (9/16)/d, since
(1-A sigma)^2+d>=(1-A)^2>=9/16. Retaining also the positive W=0 terms gives

    B_w > d(2m-log2(16/9)) > d(2m-1),
    e_w,rate3 = B_w-3d > d(2m-4) >=0,       m>=2.

Thus premature w genuinely defeats an unregistered claim that every query
has nonpositive CE debit at rate3. The separate literal guard verifies the
four actual m=2..5 examples with both full children; this is not a failure
of original source funding and does not claim that early w cannot be paid.
These alter the currently used profile/conditional structure. The nearest
useful next action is to price the first such actual query from RH, retaining
old D, J_H and all full terminal KL, and then isolate which arbitrary-core
phase control replaces the quadratic moment cancellation. Generic transport
or a new class-level H/I estimate would not pay that step. Full FEI is OPEN.
