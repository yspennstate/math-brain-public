# A060 stage 2: sharp singleton-log controls and the saturated erasure cap

Uniform Boolean signs throughout. Let

    lambda(h)=sum_i hhat({i})^2 log2(1/hhat({i})^2),
    Lambda(h)=(ln2)lambda(h), delta(h)=I(h)-1

for balanced h. Lambda is in nats, lambda/H/B/L are in bits. Zero terms
vanish. A dictator has delta=lambda=0 and is omitted when taking a ratio.
The stage does NOT prove lambda<=3delta in arbitrary dimension.

## 1. Exact finite singleton-log maximum and its equality cases

The complete finite certificates prove

    lambda(h)<=3[I(h)-1]

for every balanced h on n<=4, and for every antipodally odd h on n=5.
The maximum Lambda/(I-1) is exactly 3 ln2 in these domains (n=3,4,
and odd n=5). In n<=2 the defined ratios are zero. The domain counts are
2,6,70,12870 balanced functions in n=1,2,3,4, and 65536 odd functions
in n=5. Odd means h(-x)=-h(x), and automatically implies balance.

Certificate derivation: put N=2^n and W_S=sum_x h(x)chi_S(x). Write
D=N^2[I(h)-1]=sum_S |S|W_S^2-N^2. Exact edge counts independently give
D=2N times the number of undirected bichromatic cube edges minus N^2.
Balancedness gives W_empty=0; Parseval gives sum W_S^2=N^2. Poincare
therefore gives D>=0. After multiplying the proposed inequality by N^2,
it is equivalent to the positive-integer comparison

    2^[2n sum_i W_{i}^2]
      <= 2^(3D) product_(i:W_i!=0) |W_i|^(2W_i^2).       (1)

The helper factors only the small singleton integers, subtracts prime
exponents and compares positive integers. No floating logarithm or
uncertified approximation occurs. Identical (n,sorted |W_i|,D) signatures
reuse a sign certificate; every actual truth table is still enumerated,
including its full spectrum and physical boundary. out/integer_certificates.json
has all 97 signatures and their integer exponents/bit lengths. The maximum
integer comparison is only 12289 bits.

Complete counts:

    n=3: 6 dictators, 56 strict cases, 8 equality cases;
    n=4: 8 dictators, 12638 strict cases, 224 equality cases;
    odd n=5: 10 dictators, 65446 strict cases, 80 equality cases.

The 8 n=3 and 80 odd-n=5 equality tables are signed Maj3 juntas. At n=4,
there are TWO disjoint signed-permutation/output-sign orbits: 32 signed
Maj3 juntas with a dummy input, and 192 variants of the function below.
An independently implemented complete n=4 census uses direct singleton
character sums and direct edge counts, without FWHT. It compares (1) in
its unreduced integer form and matches the equality masks exactly to the
union of those two generated orbits. No affine transformation outside NPN
is used. Signed permutations preserve singleton magnitudes and I directly.

## 2. A four-input equality function other than Maj3

Let h(x1,x2,x3,x4) return x3 if x3=x4. If x3!=x4, return x1 when
x3=+1, and x2 when x3=-1. The four control assignments have means
+1,-1,0,0, respectively, so h is balanced. Its Fourier polynomial is

    h=(x3+x4)/2
       +(x1+x2)(1-x3*x4)/4
       +(x1-x2)(x3-x4)/4.                         (2)

Hence its singleton coefficients are (1/4,1/4,1/2,1/2). Apart from the
two coefficients of magnitude 1/2, it has eight coefficients of magnitude
1/4: two singletons, four degree-2 coefficients and two degree-3 coefficients.
Thus

    H(h)=3 bits,
    Inf(h)=(1/4,1/4,1/2,1/2), I(h)=3/2,
    lambda(h)=2*(1/16)*4+2*(1/4)*2=3/2,
    Lambda(h)/(I(h)-1)=3 ln2.                     (3)

The truth-table mask with +1 encoded by 1 and binary inputs ordered by
x_i=(-1)^(bit_i) is 1343. Its integer Walsh vector is
[0,4,4,0,8,4,-4,0,8,-4,4,0,0,-4,-4,0]. This function depends on all four
coordinates (every influence is positive), so it is not a Maj3 junta.
The finite census certificate, not a uniqueness extrapolation, establishes
that (2) and Maj3 exhaust the equality orbits in n=4.

In A059's balanced read-once gate ledger, this finite result has an exact
restricted consequence: if every internal gate has arity at most four
(or is an odd five-input gate), then its LOCAL gate-log charge satisfies

    sum_internal J(v)Lambda(g_v)
      <=3 ln2 [I(F)-1-sum_terminal J(l)(I(Sub_l)-1)].

This follows by multiplying the certified gate inequalities by nonnegative
ancestor influence weights and using the already proved deficit stopping
identity. It improves the local constant from 4+6/e to 3ln2 in that gate
library only. It does not bound recharged whole subformulas, biased gates
after physical restriction, or terminal entropy, and does not advertise a
new generic read-once FEI closure.

The global lower bound on any universal Lambda<=K(I-1) is at least
K=3 ln2. A finite maximum does not supply the all-dimensional upper bound.
The first unsupported line for that sharpness question is precisely
lambda(h)<=3(I(h)-1) for every balanced h in all dimensions. Even all
balanced n=5 is outside the certified domain.

## 3. Independent review of the monotone/concave cap (B12 L1)

Use phi(A,V)=(A+V)log2(A+V)-Alog2 A-Vlog2 V. For an outer Boolean
g=a+z_j b, in the uniform basis put A_T=a_T^2, V_T=b_T^2,
q=sum V_T and L_j(x)=sum phi(A_T,xV_T). The paired spectral form of
erasure gives L_j(1)=B_j(g), and L_j(0)=0. For x>0,

    L_j'(x)=sum_T V_T log2(1+A_T/(xV_T))>=0,
    L_j''(x)=-(1/ln2)sum_T A_T V_T/[x(A_T+xV_T)]<=0.     (4)

Terms with A_T V_T=0 vanish by continuity. Thus L is nondecreasing and
concave. Applying concavity of -s log2 s to A+xV=(1-x)A+x(A+V) gives

    L_j(x)<=xB_j(g)+q x log2(1/x),
    L_j(x)<=min{B_j(g),xB_j(g)+q x log2(1/x)}.       (5)

The disjoint balanced erasure split B_i(g(h))=qB_i(h)+L_j(alpha_i^2)
is used only at its reviewed scope: A057 v1, independently accepted by
A087 stage2. In a residual nonempty inner frequency sector erasure is q
times the corresponding inner packet; in the inner empty sector balanced
h has zero absent mass and singleton mass alpha_i^2, yielding (4)'s packet.
This reconstructs the B identity directly as well. Biased descendants
require the different recentered A056 v2 interface, which is not assumed
to follow from this balanced identity.

Verdict on B12-L1-MONOTONE-ERASURE v1: HOLDS at source scope. In the
lead's natural-unit formulas remove the factor 1/ln2 in (4) and replace
log2 by ln. No source repair is made. This is a review of the already
stated lemma, not a new generic closure claim.

## 4. The cap cannot have a uniform strict multiplicative improvement

Let m>=2 be even, N=2^m, d=1/N, r=sqrt(d), and
b(y)=(-1)^(y1*y2+...+y_(m-1)*y_m) on binary data bits. Let D(y)=1_(y=0),
z be a fresh sign selector, and set

    g_m(z,y)=D(y)+z[b(y)-D(y)].                    (6)

At y=0 this is +1, and elsewhere it is z b(y), so it is genuinely Boolean.
This is the X009 bent splice multiplied by its selector character, which
exchanges the two selector Fourier sectors. Importantly, ordinary selector
influence is now q=1-d, rather than d. It is not a low-influence query.
Its mean is d, and its data influences are 1/2+d.

Every a_T=d, and b_T=sign_T r-d, with sign counts
N_+=(N+sqrt(N))/2, N_-=(N-sqrt(N))/2. Write v_+=(r-d)^2,
v_-=(-r-d)^2. The exact expressions are

    B_j(g_m)=N_+ phi(d^2,v_+)+N_- phi(d^2,v_-),
    L_j(x)=N_+ phi(d^2,xv_+)+N_- phi(d^2,xv_-),
    I(g_m)=1-d+m(1/2+d),
    H(g_m)=2md+sum_sigma N_sigma v_sigma log2(1/v_sigma).  (7)

For every 0<x<1, monotonicity gives L_j(x)<B_j(g_m), but the following
rigorous ADDITIVE loss bound is sufficient to determine the supremum:

    0<B_j(g_m)-L_j(x)<=d log2(1/x).                (8)

Indeed (4) and ln(1+t)<=t give L_j'(s)<=sum_T A_T/(s ln2)=d/(s ln2).
Integrate from x to 1. At least one v_T is positive, so the left inequality
is strict. The right inequality is strict at finite parameters too, although
the nonstrict form covers all endpoints needed here.

For completeness a lower bound for B, independent of heuristic asymptotics:
the rare selector spectral event has probability d and conditionally uniform
data spectrum. Its data marginal M_T=d(1+2d-2 sign_T sqrt(d)) obeys

    sum_T d^2/M_T=(1+4d)/(1+4d^2),
    chi^2(P||P_selector tensor P_data)=4d^2/(1+4d^2).      (9)

The selector character merely complements the spectral selector bit, so
erasure and mutual information agree with the original X009 values. More
directly, the binary-mixture chi-square formula with rare weight d gives
(9) after subtracting 1 and multiplying by d/(1-d). Relative entropy in
bits is at most log2(1+chi^2)<=chi^2/ln2 (Jensen on the likelihood ratio).
Consequently

    B>=h2(d)-4d^2/ln2.

Since -(1-d)ln(1-d)>=d(1-d), this implies, for all even m>=4,

    B>=d m+d(1-5d)/ln2>=d m,
    1-log2(1/x)/m <= L_j(x)/B_j(g_m)<1.           (10)

In particular, for x=1/4 and m=100 the ratio is at least 49/50, and for
every fixed x>0 it tends to 1. No finite enumeration of a 100-bit cube is
needed: (8)--(10) are complete analytic proofs with exact parameters.

For each 0<c<1 choose a fixed alpha=2^-k in (0,1-c] and x=alpha^2.
It is realizable by a balanced Boolean inner: take v on k+1 fresh bits
with 2^k+1 positive truth-table entries and 2^k-1 negative entries, so
Ev=2^-k=alpha, and set h(s,w)=s v(w). Then h is balanced, its queried
singleton is alpha, Inf_s(h)=1, and B_s(h)=0 because every occupied
Fourier set contains s. Use g_m(h(s,w),y) on disjoint blocks. Directly,
the only mixed erasure packets for s have masses d^2 and alpha^2 v_T,
so the physical B_s is exactly L_j(alpha^2). All other packets have one
zero mass. Thus the asymptotic saturation is realized by actual Boolean
composition with |alpha|<=1-c, not arbitrary real amplitudes.

Stronger: take k=ceil(log2 m), alpha_m=2^-k->0. From (10),

    L_j(alpha_m^2)/B_j(g_m)>=1-2ceil(log2 m)/m ->1.       (11)

Therefore even coefficients tending to zero do not produce a uniform
relative gap in the monotone cap, without control of the packet imbalance
A_T/V_T. Here that ratio is of order d and collapses exponentially.
The often loose second branch of (5) must not replace the first globally:
for fixed x its qx log2(1/x) stays positive while the actual B tends to zero.

For a compact fixed inner h=Maj3, alpha_i=1/2 and B_i(h)=0. The composite
has mean d, query influence (1-d)/2 and singleton (sqrt(d)-d)/2. It has

    H(g_m(h,y))=H(g_m)+2(1-d),
    I(g_m(h,y))=I(g_m)+(1-d)/2,
    B_i(g_m(h,y))=L_j(1/4).                        (12)

FWHT tests verify (7), (8), (12) exactly; independent direct character
sums also verify the alpha=1/4 dictator-times-v realization. Nothing here
gives unbounded H/I: m data coordinates have influences near 1/2 and
the changed selector query has influence near 1 (or near 1/2 in (12)).

## 5. Tensorization scope: the two constants behave differently

Let g be any outer and u a Boolean spectator on disjoint coordinates.
At a selected coordinate j of g, outer a,b coefficients for g tensor u
are a_T uhat(R),b_T uhat(R). Homogeneity of phi and Parseval give

    B_j(g tensor u)=B_j(g), L_j^(g tensor u)(x)=L_j^g(x).  (13)

Tensoring k independent copies of g_m and selecting the corresponding
coordinate in each gives total B=k B_j and total L=k L_j. Hence the sharp
cap coefficient 1 survives tensorization. Any proposed universal
sum L<=kappa sum B+D0 with fixed D0 and kappa<1 fails: divide by k,
then choose m so the individual ratio exceeds kappa. A loss charged per
factor does not vanish; a packet imbalance hypothesis may change this scope.

H, I and aggregate B are additive under disjoint tensor products. However,
Lambda is NOT additive on balanced functions: if h and u are balanced,
every singleton Fourier coefficient of h tensor u vanishes. For instance
Maj3 tensor Maj3 is balanced with I=3 and Lambda=0, although each factor
has Lambda=(3/2)ln2. Thus ordinary tensorization does not remove an
additive term from a Lambda-versus-deficit inequality or amplify its ratio.
The necessary local coefficient 3ln2 is forced by (3), not by pretending
that this singleton functional is tensor additive. For A059's per-gate
ledger, the local gate charges and influence deficits still telescope at
whatever valid local constant is proved; identifying them with physical
biased-descendant costs is a separate unresolved step.

## 6. Remaining universal line and shortest continuation

The sharp universal singleton inequality is unresolved beyond the finite
domains above; no all-dimensional K=3ln2 is adopted. The monotone cap's
coefficient 1 is fully resolved as an all-dimensional supremum even under
fixed singleton gaps. Therefore a universal physical-tree payment cannot
be obtained merely by reducing that coefficient. What remains is a
source-valid common reserve for current biased outer packet charges,
nonempty inner decrements and actual terminal entropies, with each
physical influence spent once. The next useful sharpness test is the first
two-core priority activation with overlapping controls, preserving the
terminal-core entropies and exposing packet imbalance; another singleton
census alone would not pay that universal residual.
