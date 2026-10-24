# Two-sided giant components admit every hard core, but fail the fiber bank

Uniform finite Boolean cubes; entropy in bits. Fix a nonconstant Boolean
seed h on k essential variables. Let h_m be its disjoint m-fold tensor on
d=mk data bits, mu=E h_m. Introduce tag bits y,w and define

    U_m(y=0,w=0,x)=-1, U_m(0,1,x)=h_m(x),
    U_m(y=1,w,x)=+1.

Then activate U_m only at the all-zero assignment of r_m fresh control
bits, with output +1 otherwise, r_m=ceil(4 log2(m+1)), p=2^-r_m.
Add two dummy bits. Flip the +1 at x=0,y=w=0,dummies=0 and control
assignment having only its first bit set. Denote the resulting Boolean
function G_m on N=d+r_m+4 coordinates; s=2^-N. The edit is inactive
before the flip and adjacent to the active negative face.

## 1. Exact two-sided connectivity, primitivity and dense support

The negative set before the flip consists of the active controls, y=0,
and a full data cube at w=0, together with the h_m-negative data points
at w=1. Every such w=1 point attaches to the full w=0 face. Both dummy
bits remain free. This set is connected for arbitrary h. The edited point
has a negative neighbor by flipping its first control bit, so it merely
extends this connected component.

The entire y=1 hyperplane is positive and untouched. Every other positive
vertex connects to it by flipping y. Thus the positive level set is also
connected. This proves both sign sets connected without assuming a
connected hard seed. Their exact sizes are

    |G_m=-1|=4(2^d+|h_m=-1|)+1,
    |G_m=+1|=2^N-|G_m=-1|.

For all large m, d+1>=r_m, so the negative size exceeds
2^((N-1)/2). The positive size is at least2^(N-1), since the whole
y=1 hyperplane stays positive, so it also exceeds that giant threshold.
The negative count is odd. Any Boolean coordinate product across a
nontrivial partition has even negative count, as both factor cubes have
even size. Hence G_m is prime across every such partition.

The two dummy bits made every unnormalized Walsh coefficient divisible
by4 before the edit. The flip changes every coefficient by +-2, so all
Walsh coefficients are2 modulo4, in particular nonzero. Thus G_m has
full Fourier support and every named coordinate is essential.

## 2. Same-constant hardness with all influences small

The data Fourier coefficients of U_m are four copies of h_m's nonempty
coefficients, each of magnitude one quarter of the original. Its empty
data row has tag coefficients ((1+mu),-(1+mu),(mu-3),-(1+mu))/4.
Consequently

    H(U_m)=mH(h)/4+E_m, |E_m|<=5,
    I(U_m)=mI(h)/4+1,
    E U_m=(1+mu)/4, c=1-E U_m=(3-mu)/4 in[1/2,1].

For the entropy bound, the nonempty data contribution is
mH(h)/4+mu^2 log2(mu^2)/4+(1-mu^2). The four remaining squared
coefficients have subprobability entropy at most log2(5)<3, by adding
one missing-mass atom. Also |mu^2 log2(mu^2)|<=1/(e ln2)<1, which
establishes the displayed coarse5 bound. The tag influences are
(1+mu)/4 and(3-mu)/4, summing to1; every data influence is one quarter.

Before the edit the activated function F has

    H(F)=p T(U_m)+4rp c+A(pc),
    I(F)=p[I(U_m)+r c],
    T(U)=H(U)+(E U)^2 log2((E U)^2)-c^2 log2(c^2),
    A(v)=-(1-v)^2log2((1-v)^2)+v^2log2(v^2).

These follow by directly expanding 1+1_active(U-1). Since T(U)-H(U)
is bounded and A(pc)=O(p), r=O(log m), p<=(m+1)^-4,
H(F)/I(F)->H(h)/I(h) and I(F)->0. Each coordinate influence is at
most p before the edit. A one-point edit changes each influence by at
most2s, and squared-Fourier TV by at most2sqrt(s(1-s)). Maximal coupling
gives |H(G_m)-H(F)|=O(N sqrt(s)); these errors are exponentially small
relative to I(F). Therefore

    H(G_m)/I(G_m)->H(h)/I(h), I(G_m)->0,
    max_i Inf_i(G_m)<=p+2s->0.                       (1)

For every fixed K, these functions eventually satisfy the numerical
necessary weak-influence test maxInf<exp(3)2^-K. If H(h)/I(h)>K their
roots also eventually violate K. A uniform FEI(C) on this two-sided
connected/giant, prime, full-support, weak-total-influence class would
therefore imply unrestricted FEI(C) at the SAME constant. This is
hardness admission, not a criticality-preserving reduction or a disproof.

## 3. Exact failed fiber condition and actual child eligibility

Choose the proper block A of the r controls only. The negative set has
one component, so its inherited component label is constant. All retained
fibers contain either zero or one negative control assignment, except
the edited retained fiber, which contains the active assignment and the
adjacent added assignment. Thus, with eta=|G_m=-1|/2^N,

    eta H(X_A|Y,G_m=-1)=2s,
    W_A=eta[r-H(X_A|Y,G_m=-1)]=r eta-2s.             (2)

Whenever r|G_m=-1|>=4 this satisfies W_A>=r eta/2. The constructed
functions satisfy this for all m>=1. Thus the all-proper-block high
within-component conditional entropy condition of a high-K critical
source is exactly what this wrapper fails. Giant components alone,
even when connected on both sides and spectrally full, do not repair it.

Independently of A054's raw/sign transfer theorem, the same control block
has a proved uniform price. Before the edit L_A(F)=H(F)-pH(U_m) and
I_A(F)=rp c. Because E U_m>=0 and c<=1,

    T(U_m)-H(U_m)<=c^2 log2(1/c^2)<=2c/(e ln2),
    A(pc)<=2pc/ln2,
    L_A(F)/I_A(F)<=4+(2+2/e)/(r ln2)<6  (r>=2).     (3)

The A inequality uses -ln(1-v)<=v/(1-v), and drops the nonpositive
v^2log(v^2) term. The rational strict6 follows from ln2>69/100 and
1/e<3/8: at r=2 the remainder is less than275/138<2. The first
inequality follows from ln2>842/1215>69/100, using the first three
positive atanh terms; e>65/24>8/3 follows from its first five
exponential-series terms. These are
analytic bounds, not floating decisions.

After the flip the exact control influence is
I_A(G_m)=rp c+2s(r-2): the first control loses a pivotal edge, each
other control gains one. The active child is U_m with two dummies;
one inactive child is a point defect on d+4 retained bits, with
control reach p; all other children are constant. Its additional mean
entropy is O(p(d+4)2^-(d+4))=O(Ns). Root entropy moves by O(Nsqrt(s)).
Relative to rp c these changes vanish; hence L_A(G_m)/I_A(G_m)->4,
and it is <6 for all sufficiently large m. Exact finite controls below
check the stronger named instances without a continuity approximation.

For any violating seed D_K(h)>0, retain instead the proper block B of
controls, both tags and both dummies. Active children contain h_m
with total probability p/4; all other unedited children are constants.
The single edited inactive child is a point defect v_d on d data bits
with weight2^-(r+4). Exactly,

    S_B=-E D_K(child)=-p m D_K(h)/4-2^-(r+4)D_K(v_d). (4)

The second term is exponentially smaller than the first for fixed K,
because H(v_d),I(v_d)=O(d2^-d). Thus S_B<0 eventually. Smaller
violating physical h_m children remain explicit. For K>=6 the paid
control block also gives S_A=L_A-KI_A-D_K(G_m)<0 whenever the root
violates K and m is sufficiently large. No terminal is discarded.

## 4. Scoped review and universal gap

A054 OVERLAP_PAYMENT sections1 and its physical fiber identities are
independently reconstructed: uniform occupied fibers give
W=eta[r-H(X|Y,L,U)]; disjoint connected components have exactly
additive boundary energy; induction gives E_A(1_U)>=W/2. This elementary
geometry is accepted at scope. Its bundled raw/sign transfer and
all-dimensional constant are not fully audited here, so the entire
claim is not accepted. Equations(1)--(4) require none of that pending
transfer: (3) independently proves the paid block for this construction.

The new A052 Gibbs bank is consulted to locate the intended relative
target, not assumed as a proof premise or counted as independently
reviewed. Neither of its two singleton banks is spent as new capacity.

First unsupported line: choose/pay an actual signed pair/block on a
genuine minimal witness that satisfies the *all-block* fiber/Gibbs
constraints. Two-sided giants, connectivity, primitivity, full spectral
support and weak influences all coexist with arbitrary hard cores, but
the wrapper's small control-fiber entropy and negative actual child bank
prevent critical admission. NEXT must retain the all-block condition and
the same D+S bank rather than replace it by component sizes or density.
