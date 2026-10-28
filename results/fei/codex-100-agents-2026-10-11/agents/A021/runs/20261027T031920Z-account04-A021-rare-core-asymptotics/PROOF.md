# The original mark pays any balanced dependent pair at the same rate 256

Author proof; independent-person review pending. Units are bits. Full FEI remains open.

Let g be negative only at 000 on three DATA bits, b=g tensor g on six bits,
delta=1/64, and let a,c be arbitrary balanced Boolean functions on the SAME
finite uniform control cube. They need not be independent, distinct, symmetric,
or monotone. Set F(0,z)=a(z), F(e0,z)=-c(z), and F(x,z)=b(x) elsewhere.
Let h(y,z)=a(z) at y=0 and -c(z) at y=1, where y is a fresh marked bit.

For any Boolean f, put P_f(S)=fhat(S)^2, pi_f(S)=sum_{T superset S}P_f(T),
and V(f)=sum_{S nonempty}P_f(S)log2(pi_f(S)/P_f(S)). Zero terms are zero.
For h retain the SAME marked potential

    W(h)=V(h)-P_h({y})log2(pi_h({y})/P_h({y})).

Every physical z query keeps this mark in BOTH children. At the y query,
remove the mark and retain the full V(a), V(c) in its two children. Define

    Gmark(h)=sum_j[W(h)-E_{z_j}W(h|z_j)]
                         +W(h)-(V(a)+V(c))/2.

This is a signed transition functional, not GV of an unmarked Boolean
function. No new reserve is allocated at a child. The result is

    GV(F)-2delta Gmark(h) <=321 <256 I_DATA(F).                 (1)

The same source coefficient 2delta, both original controller children,
and the same rate 256 as the earlier shared-controller repair suffice.
The endpoint V(F)>=2delta W(h) also holds. Neither statement supplies an
influence-priced original marked owner for arbitrary Boolean functions.

## 1. Exact three-moment remainder, including correlation

This subsection does not assume balance. Write s=Ea, t=Ec, r=E(ac).
For each DATA frequency S set epsilon=(-1)^{1_{0 in S}}, H=bhat(S),
B=H-delta(1-epsilon), and

    A_S=B+delta(s-epsilon t),
    M_S=B^2+2delta B(s-epsilon t)+delta^2(2-2epsilon r),
    Z_S=sum_{R superset S} M_R,  p_S=A_S^2.

A is the empty-control Fourier row; M is the COMPLETE DATA spectral
marginal. In particular M, Z are affine in (s,t,r), not functions of
(s,t) alone. Since M_S=E[B+delta(a-epsilon c)]^2, M_S>=p_S.
These facts also hold for every realizable joint law of the signs (a,c),
including mixtures of actual restriction laws. Such a law gives sum M=1,
sum p<=1, and p<=Z<=1.

Summing the NONEMPTY-control rows gives the exact factorization

    V(F)=2delta W(h)+T(s,t,r),                               (2)
    T=sum_{S nonempty}p_S log2(Z_S/p_S)
                            +(5delta/2)(2-s^2-t^2).

Indeed a nonempty-control row is 2delta times the corresponding h Fourier
coefficient, on each of the 32 equally weighted frequencies of the other
five DATA bits. Its upper-tail logarithm is the h logarithm plus the number
of missing DATA bits. Their average is 5/2. Excluding empty-control rows
from h removes exactly the vacuum and marked singleton; this is W, not V.
Their total nonempty-control spectral mass is delta(Var a+Var c).
The remaining nonempty DATA/empty-control terms are exactly the sum in T.
This proves (2), with all cross rows and both sectors retained.

T>=0 throughout the realizable moment domain. At a balanced root,

    0<=T(0,0,r)<=13, for every -1<=r<=1.                    (3)

For the six-bit tensor seed H is one of 36delta,-12delta,4delta.
If epsilon=-1, H is -12delta or 4delta, so B is -14delta or 2delta.
Otherwise B=H. Thus |B|>=2delta and at s=t=0 every nonempty p>=4delta^2.
Using the weaker bound p>=delta^2, log2(Z/p)<=12 and sum p<=1 gives
T<=12+5delta<13. These estimates include r=1 and r=-1 without division
by a variance or an assumption that the joint sign law has full support.

## 2. A uniform curvature bound on all light directions

Let u=ahat({j}), v=chat({j}), w=(ac)hat({j}), L=u^2+v^2+w^2.
The two actual restriction moment triples are (u,v,r+w) and (-u,-v,r-w)
at a balanced root. The full path (lambda u,lambda v,r+lambda w),
-1<=lambda<=1, is realizable: it is the convex mixture of these two laws.
For |u|,|v|<=1/2, every point of the path satisfies |s|,|t|<=1/2.
Here |A|>=|B|-delta>=delta, so every denominator below stays positive.
Derivatives are along lambda. Since x/(x-1)^2<=2 for x>=2,

    |M'_S|/M_S <=4(|u|+|v|)+2|w| <=6 sqrt(L).

To check the first inequality, M'=2delta B(u-epsilon v)-2epsilon delta^2 w,
M>=A^2>0, 2delta|B|/(|B|-delta)^2<=4, and
2delta^2/(|B|-delta)^2<=2. Summing positive M shows the same bound for
|Z'/Z|. No independence of a and c is used.

The 32 frequencies of each epsilon give

    sum_{S nonempty}p'' <=L/32,
    sum_{S nonempty}p'^2/p <=L/16.

For E=sum p log2(Z/p), direct differentiation, using Z''=0, gives

    E''=sum p''log2(Z/p)-c0 sum p''
           -c0 sum[p'/sqrt(p)-sqrt(p)Z'/Z]^2,
    c0=1/ln2<3/2.

The logarithms lie in [0,12], sum p<=1, and (x-y)^2<=2x^2+2y^2.
The bonus in T has second derivative -5delta(u^2+v^2). Therefore

    -110L<T''<110L.                                       (4)

Explicitly, its lower bound is
 -[(3/2)(1/32+1/8+72)+5/64]L >-110L,
and its upper bound is (12/32)L<110L. The positive atanh series at 1/3
gives ln2>2/3, justifying c0<3/2 without numerical logarithms.
The midpoint Taylor inequality, integrated on the compact path, now gives

    T(0,0,r)-[T(u,v,r+w)+T(-u,-v,r-w)]/2 <=55L.             (5)

There is no exchange of an infinite sum and a limit; the control cube is
finite, and all denominators on each light path have the uniform floor.

## 3. All controller coordinates, not just a chosen policy

Parseval gives sum_j u_j^2<=1, sum_j v_j^2<=1, sum_j w_j^2<=1.
At most three coefficients of each of a,c have magnitude greater than1/2.
Thus there are at most six heavy coordinates. Each heavy midpoint cost is
at most13 by (3) and nonnegativity of T at both actual child laws.
Summing (5) for light coordinates and this bound for heavy ones yields

    G_z V(F)-2delta G_z W(h) <=3*55+6*13=243.              (6)

This includes constant controller children and completely dependent or
opposite controllers. The centered moment of ac, which can vary independently
of the two controller means, is explicitly charged through its Parseval sum.

## 4. The DATA query cancels exactly the marked query

Put R=W(h)-(V(a)+V(c))/2. For every DATA bit other than0, the adjacent pair
survives in exactly one child, with doubled density delta'=2delta.
The other child has no controlled edit. The same exact row factorization
gives V(active child)>=2delta' W(h); the inactive child's V is nonnegative.
Consequently its averaged child potential is at least2delta W(h), and
that DATA decrement is at most T(0,0,r).

At DATA bit0, there is one edit in each five-bit child, of density2delta.
For a one-point edit with an arbitrary seed, its nonempty-control Fourier
rows are uniform on DATA frequencies. Summing them gives
delta' V(a) plus a nonnegative fair-frequency bonus; its empty-control
nonempty DATA terms are also nonnegative. Hence the two child potentials
average to at least delta[V(a)+V(c)]. This decrement is at most
2delta R+T(0,0,r). These are both complete physical outcomes, not a choice
of the cheaper branch. It follows that

    G_DATA V(F)-2delta R <=6T(0,0,r)<=78.                  (7)

By definition Gmark=G_z W+R, so (6)+(7) gives the bound321 in (1).
Keeping the sign of R is essential: an absolute price or an unmarked
owner loses the cancellation in (7).

## 5. Physical influence and the precise boundary

Balance gives Pr(F!=b)=delta even when a,c are dependent. For any DATA
coordinate, changing a function on probability delta changes its influence
by at most2delta, by the union bound on the two endpoints of an edge.
I(b)=2*(3/4)=3/2, hence

    I_DATA(F)>=3/2-12delta=21/16,
    321<336=256*(21/16).

This proves (1); T>=0 proves the stated endpoint. The previous majority
examples still refute an unmarked owner. The new claim extends the SAME
marked transition repair from identical controllers and the special a,a*w
family to ALL balanced dependent pairs, for this fixed six-bit tensor seed.

The first unsupported universal line is an influence-priced ORIGINAL marked
source admitting arbitrary Boolean cores and the necessary restriction
histories, with every old debit retained. Balance is used at (3), in the
centered light/heavy Parseval payment, and in the DATA influence floor.
An arbitrary restriction need not preserve balance. No hereditary theorem,
arbitrary-seed transfer, or renewed bank at an unbalanced child is asserted.
The small exact checks corroborate the identities; the all-dimensional
claim follows from (2)--(7), not from finite enumeration. Independent review
by A029/A087/A094 is requested through the saved handoff, not assumed.
