# Two reference-price obstructions, independently reconstructed

All entropy and cross entropy use bits. The inputs are independent fair bits;
chi_s(u)=(-1)^{popcount(s&u)}. CE(P,Q)=sum P log2(1/Q), including every reference-only
atom in normalizers. A complete terminal is charged with its physical reach.
Neither obstruction supplies an unbounded Boolean H/I family.

## 1. A085: full support does not make absolute reference error affordable

Let n>=2, t=2^-n, and let f on n+1 bits be negative exactly at vertices 0,1,3.
The queried coordinate j is least significant. For nonempty s, direct character
summation gives

    fhat(s)=-t[1+(-1)^s_j+(-1)^(s_j+s_y1)],   fhat(0)=1-3t.

The bracket never vanishes, and 1-3t>=1/4. Thus P=fhat^2 has full support.
The three negative vertices have two internal edges, so the boundary has
3(n+1)-4 edges. Each boundary edge contributes 2^-n to total influence:

    I(f)=(3n-1)t,       Inf_j=t.

The j=0 child g has one negative point; the j=1 child h has two adjacent negative
points. Both are nonconstant for every n>=2. Put Q=P at the root and inherit
q(T)=Q(T)+Q(T+j) at BOTH children. The true child laws average to q by
((a+b)^2+(a-b)^2)/2=a^2+b^2. In particular, for a={y1},

    Pg(0)=(1-2t)^2=p0, Pg(a)=4t^2=p,
    q(0)=1-6t+10t^2=q0, q(a)=2t^2=qa.

Every q atom is positive. Also q0>=p0/2>0 (their difference is
(1-4t+8t^2)/2>0). Put M=2^(2n-2), so pM=1. Prescribe exactly one reset:

    qnew(a)=qa*2^-M,
    qnew(0)=q0+qa(1-2^-M),
    qnew(T)=q(T) otherwise.

The reference stays positive and normalized. Its total variation is
d=qa(1-2^-M)<2^(1-2n). The unchanged h terminal and the previously booked
erasure stay in the account. The complete, physically weighted reset bill is

    Z=(CE(Pg,qnew)-CE(Pg,q))/2
     =[1-p0 log2(1+d/q0)]/2.

For n=2 this is 1/2-log2(31/16)/8>3/8, since 31<32. For n>=3,
ln(1+u)<=u, ln2>1/2, p0/q0<=2, and d<qa give

    0<=p0 log2(1+d/q0)<4qa<=1/8.

Thus Z>7/16>3/8. The same bound tends to zero with t, proving Z->1/2,
whereas TV->0, I->0, and Z/Inf_j>(3/8)2^n diverges. These are analytic
statements for every integer n>=2, not extrapolations from the finite checks.

The original matching account is genuinely inexpensive. Nonempty root masses
are t^2 or 9t^2, their total is 6t-9t^2, and each positive nonempty atom has
log reciprocal at most 2n. Therefore nonempty entropy is at most 12nt.
For z=(1-3t)^2, -z ln z<=1-z and ln2>1/2 bound the empty contribution
by 2(1-z)<=12t. Consequently

    H(f)<=12(n+1)t<=8(3n-1)t=8I(f), n>=2.

The last inequality is equivalent to 12n>=20. No denominator or limit at zero
has been canceled. At a matching root conditional reference KL is EXACTLY
zero in each occupied fiber. Root H equals its booked erasure plus BOTH full
expected inherited terminal CE costs, so an account equal to root H has no
unused credit. The prescribed reset overspends it by Z. More generally, for
every fixed K and every positive absolute tolerance epsilon, sufficiently
large n has TV<epsilon but the post-reset total bill exceeds K I(f), since
it is at least Z>3/8 and K I(f)->0. This is a failure of uniform absolute-TV
admission, not a claim that useful resets must take this adverse form.

Three root dimensions are minimal under the simultaneous additional conditions
of full Fourier support and two nonconstant children. In dimension two both
one-bit children must be signed characters. Their parent is a signed monomial
(either the retained character or its product with the queried character),
which lacks full support. In dimension one both children are constant.
The independent checker exhausts all 4+16 truth tables in these dimensions
and every coordinate; the eight eligible splits in dimension two all fail
full support. Minimality is not asserted outside these additional conditions.

The safe comparison retained from A085 is also correct: if qnew(s)>=(1-eta)q(s)
on every occupied true atom, 0<=eta<1, then termwise log monotonicity gives
CE(P,qnew)-CE(P,q)<=-log2(1-eta). Average this with the actual terminal reaches.
It still must be paid from the original unused bank, after every old debit
and the complementary full terminal. The adverse reset has relative ratio
2^-M, so it does not satisfy a small-relative-error hypothesis.

Verdict: A085-ABSOLUTE-TV-RESET-OBSTRUCTION@1 HOLDS unchanged, including its
all-n scope, endpoint, support, matching-root price and minimality clauses.
A099's exact reset criterion is not refuted; its entire chain was not reviewed.

## 2. A047: the complete canonical coordinate-product price has no finite rate

This review accepts ONLY the all-r no-finite-K substatement of
A047-CANONICAL-FULL-SOURCE-PRICE-OBSTRUCTION@1. It does not independently accept
the separate m64 numerical excess, the fixed-r asymptotic constant, or the
whole A050 scoped-repair theorem bundled in that source run.

For width r>=2 let each point sign be negative at its block's all-one vertex,
and form h as the product on m disjoint blocks. Set delta=2^-r,
mu=(1-2delta)^m, t=(1-mu)/2. The actual root is

    F(x,a,b,z)=(-1)^a if x=0; h(z) if x=b=1; +1 otherwise.

Direct Boolean differentiation gives marginals (influences)
d=(1/2,1/2,t/2,delta/2 repeated mr times) and
I0=1+t/2+mr delta/2. Root mean is (1-t)/2, so p0=(1-t)^2/4,
v=1-p0 in (3/4,15/16). Every d_i/v is strictly between zero and one.
Furthermore sum d_i/v>1: the two initial influences already sum to1>v.

For c in (0,1) solve 1-c=product_i(1-c d_i/v). The function
[1-product_i(1-c r_i)]/c=sum_i r_i product_{j<i}(1-c r_j), r_i=d_i/v,
is continuous and strictly decreasing, with value sum r_i>1 at zero and
1-product_i(1-r_i)<1 at one. Strict decrease follows because there are at
least two positive r_i and every product factor stays positive on [0,1].
Thus the positive root c exists uniquely; the trivial c=0 is excluded.

Define theta_i=c d_i/v and the prescribed normalized reference

    Q(0)=p0,
    Q(s)=(v/c) product_i theta_i^s_i (1-theta_i)^(1-s_i), s nonempty.

Its nonempty mass is (v/c)c=v, and its marginals are d_i. Every atom is
positive, so every true source atom is dominated. On nonempty atoms log Q
is affine in membership. Matching empty mass and marginals therefore give
the exact complete price

    CE(P,Q)=-p0 log p0-v log(v/c)
      -sum_i[d_i log(c d_i/v)+(v-d_i)log(1-c d_i/v)].

Take the explicit integer m=2^(r+2). Then mr delta/2=2r. At c=1/2 the data
product alone bounds the full product by

    (1-delta/(4v))^(mr)
       <=1/[1+mr delta/(4v)]<=1/(1+r)<1/2.

Here 0<delta/(4v)<1, and (1-u)^(-k)>=(1+u)^k>=1+ku for integer k>=1.
The displayed decreasing function is therefore >1 at 1/2, so its root
c>1/2. In the CE formula all grouped terms are nonnegative except possibly
-v log(v/c)=v log c-v log v>-1, since log c>-1 and v<1.
The selected-data terms alone exceed

    (mr delta/2) log(2v/(c delta))>2r^2,

because 2v/c>1. Thus CE>2r^2-1, while I0<2r+5/4. Both comparison
quantities are positive. Hence

    CE/I0>(2r^2-1)/(2r+5/4)>r-1,

where the last numerator difference is (3r+1)/4>0. The actual dimension is
3+r*2^(r+2), finite for each r. Choosing r>K+1 refutes every proposed finite
constant K for THIS complete reference; no limit exchange is needed.

For completeness this Boolean family has H(F)<=4I(F). A point factor has
nonempty entropy 8(r-1)delta(1-delta), while its empty entropy is at most
4delta(1-delta)/ln2<=8delta(1-delta). Consequently H(point_r)<=4I(point_r).
Widths zero and one are constant/character. Disjoint tensor additivity gives
H(h)<=4I(h), also after any data restriction. Expanding F gives the exact
root spectral multiplicities: p0 at empty and x; 1/4 at a and xa; t^2/4
at b and xb; and four copies of each nonempty core mass divided by16.
Therefore

    H(F)=1-2p0 log p0-2(t^2/4)log(t^2/4)
          +[H(h)+mu^2 log(mu^2)]/4+1-mu^2.

For p in [0,1/4], -p log2 p<=1/2 (its derivative is positive there).
The negative mu^2-log term can be dropped and 1-mu^2<=1, giving
H(F)<=4+H(h)/4<=4+I(h)<=4I(F). All restrictions needed for the source's
data-only terminal certificates preserve disjoint point factors.

At any fixed rate C>=4 the root obstruction remains even with the complete
terminal surplus available. Set A=CE-H0, e=H0-Hterm-C(I0-Iterm),
S=C Iterm-Hterm>=0. Then S-(A+e)=C I0-CE. Thus the sharp full-source
admission max(A+e,0)<=S is equivalent to CE<=C I0. Choosing r>C+1 defeats
it, with no earlier debit and no fresh reset. A smaller selected transaction
or a reference preserving the core correlations has not been refuted.

Verdict: A047's all-r no-finite-K substatement HOLDS unchanged. This disproves
the blanket canonical-price route in the previous A092 NEXT, not FEI.

## 3. Verification scope and remaining obligation

The scripts are new implementations; no peer helper is imported or run.
review.py uses direct character sums, direct physical edge disagreement counts,
exact Fraction normalization and independently implemented log enclosures.
For a unit mantissa, ln(m)=2 sum_{i>=0} z^(2i+1)/(2i+1), z=(m-1)/(m+1)
in [0,1/3]. Forty-four terms have remainder at most
9/[4(89)3^89]. Each term rounds downward at scale2^112; the upper bound
adds all term-rounding errors and that analytic tail. A 100-bit dyadic
mantissa enclosure avoids taking long series on the reset's huge denominator.
Only positive ln2 division is used; signed range-reduction exponents are added
afterward. Interval overlap is only a consistency check; algebra above supplies
the identities. The signs themselves use strict outward bounds.

canonical.py reconstructs the root and actual stopped terminal spectra on
three complete small truth tables, checks the all-r normalizer inequality on
four exact tensor summaries, and checks the cleared rational final comparison
for r=2..128. These finite checks are not substitutes for the analytic all-r
proof. The unchanged complementary branch and all physical reaches remain.

Potential failures explicitly checked: Fourier sign convention and Parseval;
physical versus spectral influence; root and descendant support; zero refund
versus a numerically canceled refund; total variation's half-L1 convention;
the n=2 endpoint; nonconstant children; normalization with reference-only atoms;
strict positivity of all logarithm arguments; uniqueness excluding c=0;
the sign of the exceptional normalizer term; full versus selected source cost;
and the dependence of the explicit witness dimension on the proposed constant.

Rung: independent analytic proof reconstruction plus exact finite certificates.
The fresh memok admission returned1, so no Lean compiler was started. No
Lean-checked claim, external adoption or universal FEI constant is asserted.

The unpaid universal step is to choose a complete correlation-preserving source
reference, or a genuinely selected inherited reset, whose signed likelihood is
paid from ONE unused ancestor account after old bookings, channel bills and
both complete terminal debts. Absolute-TV accuracy and blanket canonical
coordinate-product pricing cannot replace that step.
