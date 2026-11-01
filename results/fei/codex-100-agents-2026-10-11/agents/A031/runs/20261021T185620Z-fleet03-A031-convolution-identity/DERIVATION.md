# The disappearing private owner: a paid weak shared-reference reset

All spectra are normalized uniform Walsh spectra of actual Boolean signs. Entropy,
cross entropy and KL use bits. M is oriented erasure, not marginal entropy:

    M_i(p)=sum_T p(T+i) log2[(p(T)+p(T+i))/p(T+i)],  M=sum_i M_i.

Zero summands are zero. B_i is the full binary conditional spectral entropy.
The symbols x,a,b,c below denote distinct physical coordinates.

## 1. Exact target and source owner

For EVERY integer L>=1 let X2,X3 be disjoint blocks of L coordinates and set

    E1={x,a,c}, E2=X2 union{a,b}, E3=X3 union{b,c},
    f_L=2 product_(j=1..3)(1-1_(input_Ej=0))-1, q=2^-L.

The source-owned reserve is 17 I_private(f_L), where private means
{x} union X2 union X3 in the ORIGINAL function. First debit M(f_L).
Query x, producing actual Boolean children g_0,g_1 of reach 1/2. Let p_s be
their entire squared spectra. Prescribe, rather than optimize, the complete
fresh reference

    Q_s(T)=Q_s(T+b)=[p_s(T)+p_s(T+b)]/2, b not in T.        (1)

This is a normalized law on ALL retained labels, with p_s absolutely continuous
with respect to Q_s. Zero-derivative/reference-only cells are retained.
It is the spectrum marginalized over b and then lifted by a fair b-bit.
This stage's assertion is the single-owner inequality

    M(f_L)+B_x(f_L)+(CE(p_0,Q_0)+CE(p_1,Q_1))/2
       <17 I_private(f_L).                                (2)

Both full child bills, and the already debited original M, occur on the LEFT.
No child private influence is offered as a new reserve. This repairs the
specific previous width-exhaustion fixture, not arbitrary Boolean sources.

## 2. Signed laws, incoming reference, and the conversion price

For J subset{1,2,3}, U_J=union_(j in J)E_j. Before squaring, expand

    a_S=2 sum_J (-1)^|J| 2^-|U_J| 1_(S subset U_J)-1_(S=empty). (3)

The empty union is included. All eight SIGNED terms are added before absolute
values or squares. This is the actual Boolean clause formula; f_L^2=1 gives
every convolution sum_S a_S a_(S triangle U)=1_(U=empty).

For retained label T write u=a_T,v=a_(T+x). The physical children have
signed amplitudes u+v and u-v, NOT an independently chosen mixture.
Their squared laws normalize because they are Boolean; directly, the signed
zero-shift cancellation sum_T uv=0 and Parseval give the same normalization.
The identity [(u+v)^2+(u-v)^2]/2=u^2+v^2 supplies their mean law

    R(T)=p(T)+p(T+x).                                    (4)

R is the SAME incoming complete reference, obtained from the actual root
spectrum, not rebuilt from a surviving child's influence. The root reference
is specified explicitly here; the previous root M bound alone did not price
its entropy. Inequality (2) pays that additional cost jointly.

Write J_x=(D(p_0||R)+D(p_1||R))/2. Then

    H(f_L)=B_x+average_s H(p_s)+J_x,
    average_s CE(p_s,R)=H(R)=H(f_L)-B_x,
    CE(p_s,Q_s)=H(p_s)+1-B_b(p_s).

Thus the actual signed average reset price, including both normalizers, is

    Delta=average_s[CE(p_s,Q_s)-CE(p_s,R)]
         =1-average_s B_b(p_s)-J_x.                       (5)

This price need not be nonpositive. The exact certificates give Delta<0 for
L=1 and Delta>0 for L=2..15 and the checked tail fixtures. Section 5 proves
Delta>1/4-q(L+3/2)>0 for ALL L>=16. Hence this includes an actually PAID
positive fresh-reference conversion at an increasingly weak shared coordinate.
Equation (2), rather than generic reference sufficiency, pays the price.

## 3. Exact finite certificates and why compression is lossless

The unqueried-private hit flags and shared spectral mask fix each signed term
in (3). A hit in a width-r retained private block has multiplicity 2^r-1.
For root/child rows and entropies this gives at most 64 exact cells, independently
of L. Physical restriction is performed on amplitudes before their squares;
multiplicities remain the exact number of labels represented by each cell.

The fixed finite domain L=1..15 is checked by Fraction arithmetic. Each logarithm
uses the finite atanh expansion of ln(z), reduced to 1<=z<2, with 32 terms and
positive geometric remainder bounded by

    2 t^65/[65(1-t^2)], t=(z-1)/(z+1).

Division by a positive certified ln(2) interval is outward. Zero masses are
omitted only from entropy sums, never from reference normalization. A sign is
accepted only when a rational interval endpoint determines it. The finite
certificate plus the analytic tail below prove (2) for all integers L; no
all-dimensional inference is made from samples. L=16,32,64 are additional
fixed checks of tail estimates, not an automatically enlarged search.

## 4. All-width tail: full entropy plus old oriented debit

Let h be the three-bit point defect on {x,a,c}, with all other coordinates
dummy. Its Fourier support A has eight labels, with amplitudes 3/4 at empty
and -1/4 elsewhere. Each remaining clause triggers with probability q/4, so

    Pr(f_L!=h)<=q/2, |a_f(S)-a_h(S)|<=q,
    sum_(S notin A) p_f(S)<=E(f_L-h)^2<=2q.               (6)

No non-Boolean approximation is substituted for the actual function: (6)
is only an error estimate between two specified Boolean signs.

On A each squared mass moves by at most 3q. For L>=16 every interpolated
mass is >=1/64. The derivative of -t log2(t) has absolute value <8 there.
The eight core atoms therefore change entropy by at most 192q. The tail
mass t<=2q lies on at most 2^(2L+4) atoms; concavity gives tail entropy
<=t log2(2^(2L+4)/t)<=(6L+6)q. This last scalar function is increasing
throughout 0<=t<=2q. Consequently

    H(f_L)<=H(h)+(6L+198)q.                               (7)

For each core coordinate i in{x,a,c}, four root rows have both labels in A.
For F(a,b)=b log2(1+a/b), the partial derivatives obey

    |dF/da|<3/2, |dF/db|<8

on each interpolating core row (a,b>=1/64, a,b<=1). The four rows contribute
at most 4*(3/2+8)*3q=114q error. Off-core rows contribute at most their total
reference mass 2q, because t log2(1/t)<=1 on[0,1]. Thus these three coordinates
have M at most M(h)+348q.

For the remaining 2L+1 coordinates, every influence is at most q. This follows
either from direct pivotal supports or (3). In fact

    e_x=(2-2q+q^2)/8,
    e_b=3q/4-q^2/8,
    e_private-in-X2-or-X3=q(3-q)/8.

Use M_i<=B_i<=h2(e_i)<=q(L+log2(e))<q(L+3/2), since h2 is increasing on
[0,q] and ln(2)>2/3. Hence

    M(f_L)<=M(h)+(2L^2+4L+350)q,
    H(f_L)+M(f_L)<=H(h)+M(h)+P(L)q,
    P(L)=2L^2+10L+548.                                  (8)

The source lower bound is I_private>=e_x>=1/4-q/4. This is a bound on the
ORIGINAL owner, not on either descendant's remaining private influence.

## 5. A retained channel credit and a positive weak-coordinate reset

After x=0, the limiting child h_0 has empty Fourier mass 1/4; after x=1,
h_1 is constant with empty Fourier mass 1. The child amplitudes differ from
these limiting amplitudes by at most 2q, by (6) and u+/-v. Therefore the two
actual empty masses differ by at least 3/4-8q>23/32 for L>=16.

Applying the map 'is the retained frequency empty?' cannot increase mutual
information. Binary entropy has h2''(t)=-1/[ln(2)t(1-t)]<=-4 on(0,1).
Its midpoint Jensen gap is at least half the squared difference of its two
parameters (endpoints follow by continuity). Therefore

    J_x> (23/32)^2/2 >1/4.                               (9)

Combining (5), B_b>=0 and (7)-(9), the LEFT side of (2) is at most

    H(h)+M(h)+3/4+P(L)2^-L.                             (10)

Here

    H(h)=-(9/16)log2(9/16)+(7/16)*4,
    M(h)=(3/16)log2(10)+9/16.

For L>=16, P(L)2^-L decreases, because
2P(L)-P(L+1)=2L^2+6L+536>0. P(16)=1220. The single rational logarithm
certificate in out/CHECK.json establishes

    H(h)+M(h)+3/4+1220/65536 <17(1/4-1/(4*65536)).       (11)

The left side of (10) is no larger than the left side of (11), and the original
bank is no smaller than its right side. This proves the tail of (2).

To check that this is not merely a free reset, use concavity
average B_b(p_s)<=h2(average e_b(g_s))=h2(e_b(f_L))<=q(L+3/2).
The standard physical one-bit channel bound J_x<3 e_x<=3/4 follows from
J_x<=(2/ln2)e_x and ln2>2/3; its elementary two-point log-Sobolev proof is
reproduced in the read source BLOCK_RESTRICTION_IDENTITY, section 2.
Thus (5) gives Delta>1/4-q(L+3/2)>0 for every L>=16. For L=2..15 positivity
is separately certified. L=1 is retained as a negative-price boundary.

## 6. Continuation, non-Boolean control, and unpaid scope

After (1), any finite adaptive physical continuation can CARRY Q_s by
marginalizing each newly queried spectral coordinate, without a further reset.
For a current source p and supplied complete Q, let pbar,Qbar denote their
query-coordinate marginals. Signed physical child laws average to pbar. Then

    CE(p,Q)=B_i(p)+average CE(p_child,Qbar)
              +sum_T pbar(T)D(p(bit|T)||Q(bit|T)).        (12)

The final term is nonnegative. Summing (12) with original physical reaches
shows that (2) pays the old M, the first x erasure, all later erasure bills,
and both full expected terminal CE bills at the SAME rate17 owner. Every
descendant uses a carried reference; (12) does not pay a second prescribed
fresh reset. This continuation is an application of A096's established
no-reset identity, rederived here, not a new universal transfer theorem.
Physical phase-channel costs at later queries remain separate from erasure.

The payment has genuine Boolean admission. Set n=2^18=2L+4, L=131070, and
take the normalized non-Boolean vector psi_n=n^-1/2 sum_j character_j.
Its first x physical restrictions STILL have norm one (the cross term is
zero), and their squared spectra have n equal atoms (empty plus n-1 singletons).
Here M(root)=B_x(root)=0 and fresh b-row lifting gives each full terminal
CE=log2(n)+1-2/n=19-2/n, whereas 17 I_private=17(n-3)/n.
The proposed payment fails: after multiplying by n, the difference is 2n+49>0.
Its nonempty convolution at {i,j} is 2/n, violating full Booleanity. Generic
normalization, zero-shift orthogonality, or the reference identity alone do not
prove the paid inequality. The clause structure and its signed cancellations
are used in (6)-(8) and in the exact finite admission.

An arbitrary untouched Boolean spectator g retains M(g)+CE(g,Q_g) with
coefficient ONE on both sides of the tensorized account. The triangle bank
does not pay it. Constants, zero-mass cells and reference-only sectors obey
the conventions above. No denominator is cancelled at a zero-mass cell.

First unpaid general line: after this paid b-reference reset, fund a specified
NEXT fresh reference (or admit an arbitrary signed core) from the same remaining
ancestor bank, keeping previous debits and the complementary complete terminal.
There is no assertion of a universal constant, a FEI counterfamily, independent
acceptance or literature priority.

Certificate strengthening: the finite minimum and the analytic tail endpoint both leave more than1/16 bit. out/SCHEMA_CHECK records the exact rational comparison; therefore (2) remains strict after adding1/16 to its left side.
