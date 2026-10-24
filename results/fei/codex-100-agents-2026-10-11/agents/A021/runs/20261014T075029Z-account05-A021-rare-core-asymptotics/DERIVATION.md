# One symmetric data reserve for arbitrary seeds and two point edits

All entropies are in bits; c=1/ln(2). This removes the flat-reference
hypothesis from the previous run's finite payment. It does not pay an
arbitrary mixed data query or establish FEI.

## Actual family, including zero rows

Let b be ANY Boolean sign on m>=1 uniform data bits. Choose two distinct
vertices u,v and flip b at each separately, obtaining b_u,b_v. Introduce
an independent sign z and set g0=z*b, g1=z*b_u, g2=z*b_v. Let A,B be
independent fresh point blocks of positive widths r,s, with a=2^-r,
bprob=2^-s (write t=bprob below to avoid confusing it with the seed).

    h=g1+B(g2-g1), f=g0+A(h-g0),
    pi=(1-a,a(1-t),at), delta=2^-m,
    IC=2r a delta+4s at delta,
    HT=sum_j pi_j H(gj), IT=sum_j pi_j I(gj),
    Rstar=2 sum_{j<k} pi_j pi_k I(gj*gk).

All terminals are retained with their original probabilities, even if
a small-dimensional edit happens to produce a related or constant
unbalanced factor; the sign z keeps every actual terminal balanced.
The query policy resolves the controls and stops at these cores.
The actual influence is I(f)=IC+IT. Let e be one when u,v are adjacent.
Direct boundary counting gives I01=I02=2m delta and
I12=4(m-e)delta. These are independent of the seed.

## Theorem

For ALL of the above seeds, dimensions, vertices and positive widths,

    H(f)-HT <= Rstar+(11/2+3c) IC < Rstar+10 IC.       (1)

There is no assumption of flatness, Fourier support, mean, or agreement
of coefficient signs. In particular zero and unequal-amplitude rows
are included. The lower bound Rstar<=H(f)-HT from the prior flat theorem
is NOT asserted for arbitrary seeds.

If actual terminal certificates H(gj)<=Cj I(gj) are supplied, then

    H(f)<=max(10,max_j Cj+2) I(f).                      (2)

This is conditional transfer with a paid terminal bank, not universal
terminal admission. The old uniform flat-reference expansion, including
its optimal coefficient-one lower asymptotic, remains valid separately.

## Exact sectors and a delocalized row variance

At a data Fourier label T (with z included), put xj=hat(gj)(T),
q_T=sum pi_j xj^2 and xbar_T=sum pi_j xj. Let

    v_T=q_T-xbar_T^2, V=sum_T v_T.

The actual root coefficients have three control sectors:
xbar_T; a[(1-t)x1+t*x2-x0] with multiplicity a^-1-1;
at(x2-x1) with multiplicity a^-1(t^-1-1).

Put e1=b(u)chi_T(u), e2=b(v)chi_T(v). Regardless of x0,
x1=x0-2delta e1 and x2=x0-2delta e2. Thus

    C=a(1-a), D0=2a^2 t(1-t),
    v_T=4delta^2[C+D0(1-e1*e2)],
    V=4delta(C+D0), 0<v_T<=2delta V.                  (3)

The equality for V uses u!=v, so e1*e2 has mean zero over all
2^m frequencies. Equation (3) is the key replacement for pointwise
curvature: it controls where lost control mass can concentrate without
ever dividing by a seed coefficient. Also sum_T q_T=1 and q_T>=v_T>0.

The nonempty-control entropy is still EXACTLY 2mV+L, with w=1-2t,

    VA=2a(1-a)delta(1+w^2), VB=8at(1-t)delta, V=VA+VB,
    L=VA(2r-2)+VB(2r+2s-4)
        +2a(1-a)delta*w^2 log2(1/w^2),                (4)

where 0log(1/0)=0. It is independent of the base seed and edit distance.

## A signed refund that tolerates zero seed coefficients

Write E(p)=p log2(1/p). The data Fourier marginal is q=(q_T).
Define the NONNEGATIVE mixture entropy

    J=H(q)-sum_j pi_j H(gj).

The exact entropy decomposition is

    H(f)-HT=J+sum_T [E(q_T-v_T)-E(q_T)]+2mV+L.        (5)

Concavity and the tangent at the strictly positive q_T give

    E(q_T-v_T)-E(q_T)<=v_T log2(q_T)+c v_T.

The end point q_T=v_T is allowed by continuity. Jensen with weights
v_T/V and (3) now gives

    sum_T v_T log2(q_T)
      <=V log2(sum_T v_T q_T/V)
      <=V log2(2delta)=(1-m)V.                        (6)

This is the signed coherent refund; no fictitious positive branch
mixture is substituted for the actual empty-control coefficient.

## Independently reconstructed A028 mixture bound

For ANY real function X on a uniform cube,

    Ent_nat(X^2)<=2 sum_i E[(X(y)-X(y^i))^2/4].        (7)

Here Ent_nat(U)=E[U ln(U/EU)]. For two real numbers a,b the one-bit
inequality is Ent_nat((a^2,b^2))<=(a-b)^2/2. Replacing a,b by their
absolute values can only decrease the right side. Normalize a^2+b^2=2,
put a^2=1+z,b^2=1-z, and use

    [(1+z)ln(1+z)+(1-z)ln(1-z)]/2 <=1-sqrt(1-z^2).

For completeness the even coefficient on the left is
1/[2k(2k-1)], while that on the right is
binom(2k,k)/(4^k(2k-1)); the required inequality is
binom(2k,k)/4^k>=1/(2k). It holds at k=1; multiplication by
(2k+1)/(2k+2) preserves it at k+1. Endpoints follow by continuity.
The two sides are invariant under scaling by the common squared scale.

Product tensorization of Ent follows from the chain identity for two
independent coordinate blocks and convexity of the one-block entropy
functional: Ent(E_block U)<=E_block Ent(U). Iterating the one-bit
inequality proves (7), without a Fourier reference or FEI premise.

Apply (7) to X_T(y)=hat(g_{L(y)})(T), where L is the actual nested
controller. Summing over T and using Parseval gives

    J<=2c IC.                                        (8)

The right side is the ACTUAL queried control influence of f. This is
the mixture/log-Sobolev step reconstructed from A028's current source;
the source's full entropy/reference theorem is not accepted wholesale.

## Uniform final payment and its original owners

Combining (5),(6),(8) gives

    H(f)-HT<=mV+L+(1+c)V+2c IC.                       (9)

The exact boundary products yield Rstar=mV-8e delta*pi1*pi2.
As in the preceding run, 0<=L<=4IC: write the logarithmic term M
in (4), use M<=VA, and obtain L<=2r V+2s VB<=4IC.
Also V<=IC. Indeed, after division by2a delta this is

    2(1-a)+4at(1-t)<=r+2st,

where 2(1-a)<=r for positive integer r, and 4at(1-t)<=2st.
Finally 8e delta*pi1*pi2<=IC/2. Substitution in (9) proves (1),
since c<3/2. All constants are independent of BOTH widths and m.

Per data edge, if d_j are the terminal pivotal indicators, let
qedge=sum pi_j d_j. Then Rstar per edge equals2qedge(1-qedge)<=2qedge.
Consequently Rstar<=2IT, proving (2) with a single marked terminal bank.

## Universal row-profile form of the refund

The signed step itself is not restricted to point edits. For ANY finite
physical controller L on independent uniform controls and ANY Boolean
cores on one n-bit data cube, set q_T=E_control x_T^2,
v_T=q_T-(E_control x_T)^2, V=sum v_T. Let Hplus be the RAW entropy
sum of all root Fourier coefficients with nonempty control label,
and IC the actual total influence on control coordinates. If V>0, then

    H(f)-E H(g_L)
      <=Hplus+V log2(||v||_infinity/V)+cV+2c IC.       (10)

Zero q rows have v=0 and are omitted from the weighted Jensen step.
The exact decomposition (5), concavity, sum q=1 and
sum v_T q_T<=||v||_infinity prove (10). Equation (7) supplies the
same JS bound for arbitrary finite labels. If V=0 the decrement is0.
Moreover V<=IC by Parseval, so (10)'s last two terms are at most3c IC.
This is a proved row-profile inequality, not an assumed payment rule.
The two-edit theorem uses ||v||_infinity/V<=2delta and exact Hplus.
For arbitrary cores the unpaid quantity is Hplus plus this SAME
profile refund, compared to one inherited terminal reserve; the two
terms cannot be bounded separately and then silently renewed.

## Downstream substitution for A025's data-query obstruction

A025 run20261014T062819Z uses a bent seed on m bits independent of
an extra bit x, and changes it at (u,x=0) or (v,x=0), where u,v are
adjacent. This is exactly the current theorem with data dimension
M=m+1 and delta_new=delta/2, despite its zero Fourier rows. At fair
controllers its physical IC=delta and root Rstar=(3m+2)delta/4.
Thus the complete control-FIRST stopping bill is now paid by

    H(F)-HT<=10delta+(3m+2)delta/4.

If x was already queried, the x=0 child has the two-edit seed on m
bits and remaining bank (3m-1)delta/2; x=1 has bank0. Each child
control continuation is covered with its OWN conditional bank, whose
physical average is the root bank minus3delta/4. This does not add
the remaining bank to its ancestor. The parent x-query residual is
still unpaid by this calculation: release3delta/4 alone cannot fund
it. This preserves, rather than contradicts, A025's all-constant no-go.

## An explicit unused terminal owner pays A025's mixed query

For exactly A025's quadratic bent family (even m>=4), retain the same
bad x-query and its two children. Allow ALSO a common fresh point
activation of any width k>=0, probability p=2^-k. Every original core
and both actual x children are balanced. Balanced activation gives

    H(1+V(g-1))=p H(g)+A(k), I=p(I(g)+k),
    A(k)=(4p-2p^2)k-2(1-p)^2 log2(1-p)<=p(4k+2c).

For k=0 take A(0)=0. These identities follow by lifting every nonempty
balanced data coefficient through all point frequencies and keeping the
exceptional constant coefficient1-p. The upper bound uses
-(1-p)ln(1-p)<=p. The same A(k) cancels in all entropy decrements.
Thus the conditioned control bills scale by p from the unactivated
theorem. Their ACTUAL bank has additional nonnegative activation-
direction capacity, so the same control rate10 remains valid with that
actual bank, rather than a newly issued mark.

Let ITpost, HTpost denote the probability-weighted ORIGINAL terminal
influence and entropy after the x query. Define its genuine surplus

    S8=8 ITpost-HTpost.

Each unactivated conditioned core is z times the m-bit bent seed or
one of its point flips. It has H<=m and I>=1+m/2-2m delta.
Consequently every activated conditioned core has

    8I-H >=p[3m+8-16m delta+4k-2c]
           >=p(3m+1+4k),

using m delta<=1/4 and c<3/2. Therefore the actual weighted S8 is
at least p(3m+1+4k). This is an independently certified numerical
terminal surplus, not an assumed child FEI bound.

The exact conserved bank and queried influences are

    Rroot=p(3m+2+3k)delta/4,
    Rremain=p(3m-1+3k)delta/4,
    release=3p delta/4, d_x=p delta/2, IC=p delta.

Here Rremain is the physical average of the two conditional banks.
Activation adds3pk delta/4 to both root and expected remaining bank;
none of that activation capacity is incorrectly counted as x-release.
Point-activation product boundaries give these identities directly.

Universally B_x<=h2(d_x) is valid, but the stronger useful estimate
comes from scaling the balanced original x-query: DeltaH_x scales
by p. The original d=delta/2 and JS<=2c d imply

    DeltaH_x <=p delta(m+1+3c)/2,
    max(DeltaH_x-10d_x,0)<=p m delta/2.

Book exactly TWO disjoint fractions of the SAME S8:

    Rremain <= (delta/4) S8,
    max(DeltaH_x-10d_x,0) <= (delta/6) S8.             (11)

These follow immediately from S8>=p(3m+1+4k). The sum of booked
fractions is5delta/12<=5/192<1. Both siblings and every original
terminal remain in S8. The root bank is NOT also added to Rremain;
its release is retained as an unspent part of the conservation identity.

For the actual policy x FIRST, then resolve the controls, the already
proved conditional control bounds and I(F)=d_x+IC+ITpost now give

    10I(F)-H(F)
      >=2 ITpost+S8-Rremain-(DeltaH_x-10d_x)
      >=2 ITpost+(1-5delta/12)S8>=0.                 (12)

This pays the query whose release-only ratio diverges, with the SAME
remaining bank and one genuinely unused certified terminal owner.
It does not refute that divergence: the extra terminal surplus is
essential to this payment. The debit fractions are fixed explicitly,
including all activation directions, and may not be renewed at another
query. This closes A025's stated family NEXT at rate10, not a universal
mixed-query induction. Its previously known full-family H<6I bound is
not claimed as new; the new conclusion is this specific conserved-bank
and unused-surplus payment of the obstructed physical history.

## First unsupported universal line

The controller-only theorem does not imply local entropy drift payment
at a mixed DATA query from its bank release. A025 has an explicit family
where that rule fails at every constant price. Nor does this proof bound
arbitrary multi-point differences or depth with one owner: its crucial
bound v_T<=2delta V comes from exactly two point edits to one common
seed. NEXT must price the signed continuation after a data query using
the SAME inherited bank and one genuinely unused terminal surplus. The
new theorem supplies the previously unpaid non-flat control continuation.
The explicit A025 substitution above funds ONE parent data query from a
quantified unused owner; it supplies neither arbitrary terminal surplus
nor a new copy of that owner at the next history. NEXT is to carry this
already booked fraction through a further actual core-data query.
