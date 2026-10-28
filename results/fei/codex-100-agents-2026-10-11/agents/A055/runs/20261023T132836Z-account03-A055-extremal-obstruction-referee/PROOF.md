# Rare arbitrary cores are already cubic-phase orbit extrema

Finite uniform Boolean signs; entropy H is in bits. Let a(f) be minimum
influence over the complete finite affine-input/output-character orbit,
and D_K^aff(f)=H(f)-K a(f). No positive witness is asserted to exist.

## 1. Three elementary ingredients

For a Boolean phase P=(-1)^p, let r be the affine dimension of its Fourier
support. The directions with constant derivative P(x+v)/P(x) form the
linear subspace Z_P of codimension r. Indeed Fourier translation has
constant sign precisely when (-1)^(s dot v) is constant on the support;
thus Z_P annihilates all support differences. Every basis of input
directions contains at least r vectors outside Z_P. These are quotient
directions, not separately bookable copies of one parity exchange.

If p has GF2 degree at most d>=1, every nonconstant directional derivative
has degree at most d-1. A nonzero multilinear polynomial of degree at
most b is1 on at least2^-b of the cube: induct on variables, splitting
q=q0+x_j q1; if q1 is nonzero, at least one of q0,q0+q1 is1 wherever
q1=1, giving half its weight; if q1=0, discard that variable. The same
bound for q+1 shows a nonconstant derivative has centered disagreement

m_P(v)=min(Inf_v(P),1-Inf_v(P)) >= q_d:=2^(1-d).             (1)

This lower bound is needed only off Z_P. On Z_P the derivative is exactly
constant. In particular q_3=1/4. Linear characters have r=0 and require
no strict phase improvement or artificial nonlinear cost.

Finally, for ANY Boolean f,P with the above affine spectral rank r,

H(fP)-H(f)<=r.                                            (2)

To see this, multiply P by an output character to move its Fourier
support into a linear r-dimensional space W. This character only
translates the resulting spectrum. Multiplication by that adjusted P
is an orthogonal convolution on Fourier coefficients, block diagonal
on cosets of W. Each coset squared mass is preserved. The coset entropy
is unchanged; conditional entropy inside each size2^r coset can increase
by at most r. This proves (2), including zero-mass cosets, without any
FEI or continuity assumption. Affine rank, rather than the number of
physical coordinates appearing in p, is the correct entropy allowance.

## 2. A full-affine influence comparison, not a physical-only test

Suppose delta=P(f=-1) and gamma=q_d-4delta>=0. The union bound gives
Inf_v(f)<=2delta for EVERY input direction v, including all noncoordinate
parities. Since delta<=q_d/4<=1/4, this is its own minority cost m_f(v).
The derivative of fP is the XOR of those of f and P, so

m_(fP)(v)>=m_P(v)-Inf_v(f).

Off Z_P this gives

m_(fP)(v)-m_f(v)>=q_d-2 Inf_v(f)>=gamma.                   (3)

On Z_P multiplication just flips or preserves the derivative event,
so m_(fP)(v)=m_f(v) EXACTLY. A full affine influence minimum is the
minimum, over independent directional bases B, of sum_(v in B)m(v).
The output character centers all chosen rows simultaneously. Therefore
for an optimizing basis of fP, using (3) and its at least r active
quotient directions, with gamma NONNEGATIVE,

a(fP)>=a(f)+r gamma.                                      (4)

The sign of gamma is essential when replacing the count of active basis
rows by r. We make no such replacement for negative gamma. Combining
(2),(4), for K>=0,

D_K^aff(fP)<=D_K^aff(f)-r*(K gamma-1).                     (5)

This is the main all-dimensional lemma. For d=3, if K>4 and delta is
small enough that K*(1/4-4delta)>1, every non-character cubic phase
strictly lowers the fully affine-optimized deficit. Character phases
have r=0 and leave H and a unchanged. Degree<=d has the analogous fixed
threshold K>2^(d-1); only the cubic application is used below.

## 3. Exact joint cubic/affine extremality of the rare embedding

If f is already affine-influence-minimal, a(f)=I(f), equation(5) proves
that f is a GLOBAL maximum of D_K over the joint finite group generated
by affine input maps and all cubic output phases. Any group element
can be written as f times one cubic phase, followed by an affine input
map and a character: affine substitution preserves GF2 degree<=3.
Its entropy is H(fP) and influence is at least a(fP). Thus this is the
joint orbit used by A052, not merely phase stationarity in one chart.

Consume the already independently reconstructed A005 paid-pair family:
from a positive-entropy canonical full-span affine-minimal seed g with
H0,q=I(g)>0,mu=Eg, put G_t=Q times t copies of g, where
Q=(-1)^(ab+ac+bc+za), and F_t=1+A_k(G_t-1),
k=max(6,ceil(sqrt(t))), p=2^-k.

Every negative output is inside A_k, hence delta_t<=p->0. These same
roots are full-span affine minima. For every FIXED K>4, eventually
K*(1/4-4delta_t)>1. Therefore the unmodified rare roots already maximize
D_K on the ENTIRE joint cubic-phase/affine orbit. No new normalization
is performed, and no old debit is reset. Every quadratic alignment and
A052 original-pair cubic alignment(9) holds automatically at rate K.

The original pair(a,b), its actual one-branch shear and all four complete
seed-core terminals remain as in A005: I_pair=p, executable release p/4,
|L_pair/p-4|<=(13+6k)|mu|^t, and

D_K(F_t)+S_pair^reset=L_pair-5Kp/4.                       (6)

For K>4 this pair is eventually strictly paid. The whole nonlinear
mean-profile entropy correction in L_pair is retained, not discarded
in its signed bank. H(F_t)/I(F_t)->H0/q and I(F_t)->0.
All proper-block expected positive optimized-terminal debt and absolute
signed banks tend uniformly to0 by A055 stage9's bound
N_A*<=4p(n_t+k), -4p(n_t+k)<=S_A*<=K I(F_t), n_t=dim(g)t+4+k.

## 4. Ratio extremality for hard seeds; exact failed condition

Suppose an actual seed violates a FIXED K>4; canonicalization cannot
decrease its ratio, so H0/q>K. Then F_t also violates K eventually.
Write R_t=H(F_t)/I(F_t)>K. Since R_t*gamma_t>K*gamma_t>1,
equation(5) applies at comparison rate R_t. Its root deficit is zero,
so every competitor with positive influence has ratio at most R_t.
Thus these violating roots are ALSO joint cubic/affine RATIO maxima.
Constants have H=I=0 and are omitted from ratios. This is an initial
orbit extremality statement, not permission to change a spent rate.

At fixed K, all FOUR explicit reset terminals retain the full t-copy
seed and have positive deficit eventually. The full affine optima can
only increase those deficits. Equation(6) gives exactly

S_pair*<=S_pair^reset<-D_K(F_t)<0.                         (7)

This is the failed genuine-critical condition. At rate R_t the pair is
still paid and the root deficit is0, so S_pair,R_t*<0 as well. At least
one complete optimized terminal therefore violates R_t. We do NOT claim
that all four violate R_t; the all-four conclusion is at fixed K.
All original physical partitions, reaches, mixed rows and terminals
remain, including those rare children carrying large conditional debt.

Consequently, for every fixed K>4 and epsilon>0, FEI(K) restricted to
full-span affine minima with I<epsilon, an original proper pair paid by
an executable non-character reset, ALL-block N_A*,abs(S_A*)<epsilon,
and global D_K maximality in the joint cubic/affine orbit is equivalent
to full FEI(K) at the SAME K. The reduction remains true if joint-orbit
RATIO maximality is required as well: if full FEI(K) fails, start with
a violating seed and use the preceding construction. The reverse
implication is immediate. This does not assert an actual violating
seed for unknown high K; it refutes no registered source theorem.

## 5. Exact finite scope and validation

code/cubic.py freezes its specification before any search. It exhausts
degree<=3 four-bit phases modulo output affine characters. The quotient
is exact: these characters preserve H,a,centered directional costs and
affine spectral rank. There are1024 nonlinear representatives, each
covering2^5 phases. Pilot uses16 representatives on3bits.

Separate actual rare roots use whole activation at k6: pilot Q on10bits;
full Q times point2 on12bits. Full tests cover48 three-coordinate phase
representatives,48 explicit output-character copies and40 branch-controlled
original-pair character comparisons, retaining BOTH signs. It checks all
directional root rarity costs, entropy rank allowance, optimized-basis
rank count and influence increment(4), full optimized deficit comparison,
and A052 physical two-neighbor influence formula(8)/alignment(9) at K6.
Root negative mass is measured from the actual table, not replaced by
an inferred floating rarity. Integer Walsh, separate physical derivatives,
integer cost sorting and binary independent bases, Fraction, exact
prime-log vectors and64-term rational atanh tails decide every sign.
The all-dimensional argument is Sections1--4, not extrapolation.

FIRST UNSUPPORTED UNIVERSAL LINE: use genuinely NONNEGATIVE complete
smaller-child affine reserves, jointly with the original-pair signed
alignment, to force enough independent cheap-parity rank AFTER an actual
original proper-pair restriction to pay its full bill in the SAME unused
bank. Cubic-phase initial extremality, even global orbit ratio optimality,
does not supply that eligibility: the exact failure is (7). No universal
constant improves, and full FEI remains OPEN. K<=4 is outside this new
cubic admission theorem, including the A052 genuine K3 point-defect guard.

## 6. An explicit positive cubic-extremal example at K=17/4

This is an actual finite Boolean formula, not an assumed high-K seed.
Start with the one-bit input sign g0. On two disjoint copies define
g_(j+1)=1 if BOTH child signs are -1, and -1 otherwise. Thus g5 is the
complete depth-five NAND tree on32 variables, in this sign convention.
Let mu=E g_j, alpha=(1-mu)/2, q=1-mu^2, H=H(g_j), I=I(g_j), and
h(x)=-x^2 log2(x^2). Direct Fourier expansion of
1-2*((1-g)/2)*((1-hchild)/2), followed by output sign inversion, gives

mu_new=2alpha^2-1,  I_new=2alpha I,
H_new=h(mu_new)+2alpha*(H-h(mu))+2q*h(alpha)+q^2/2.          (10)

For clarity the coefficient classes before inversion are: empty mean
1-2alpha^2; each one-child nonempty label has coefficient alpha times
its child coefficient; each two-child nonempty label has coefficient
-1/2 times their product. Summing their scalar entropies yields (10).
The starting values are mu0=0,I0=1,H0=0. The exact interval certificate
uses32-term rational atanh expansions with a proved geometric tail,
normalizing logarithm arguments into[1,2] and rounding outwards to100
binary places at every entropy step. It checks all five profiles and
direct Walsh/edge agreement through depth3 (eight inputs). It proves

H(g5)-(17/4)I(g5)>1/8,
1/2<=|E g5|<=7/8, I(g5)<=32.                              (11)

The original seed itself is full-span affine-minimal; no enormous orbit
optimization or unspecified canonical representative is used. Here is
the proof. Every NAND leaf is essential and the tree is unate, since
each gate reverses each child's orientation. For any unate-in-i Boolean
function and any flip direction v containing i, Inf_v>=Inf_i. Pair the
remaining flipped bits y with their antipodes and write the four values
a=f(0,y),b=f(1,y),c=f(0,-y),d=f(1,-y). After reversing output if needed,
a<=b and c<=d. The elementary nine-case inequality

1[a!=d]+1[b!=c]>=1[a!=b]+1[c!=d]

proves the influence comparison on averaging; code checks all nine
ordered pairs. Bias |mu|>=1/2 also gives Inf_v<=1-|mu|<=1/2, so these
are the centered costs themselves. The finite minimum-basis criterion
therefore gives affine minimality. Essentiality makes each nonzero
direction cost positive, so the constant-derivative subspace is zero
and the spectral affine span is full. This argument also proves the
general admission fact for biased unate functions with essential inputs.

Now use THIS seed in the same formula F=1+A_k(Q*g5^t-1), choosing
t=100000000,k=10000,K=17/4. The dimension is3200010004. All quantities
below are certified by code/nand_certificate.py without constructing
the large truth table or evaluating the large mean power. The lower
seed gap in (11) gives

D_K(F)/p > t/8+4-K(2+2k)-10k-20 >0,
D_K(each of four explicit reset terminals)/p
          > t/8-K(1+2k)-10k-20 >0.                        (12)

Bernoulli bounds |mu|^t<=8/(8+t). The pair's paid margin divided by p
is greater than5K/4-4-(13+6k)*8/(8+t)>1. Also p<=1/512 and
K*(1/4-4/512)=527/512>1. Theorems(5)--(7) thus certify GLOBAL joint
cubic/affine deficit extremality, own-ratio extremality, a paid original
pair, and negative complete optimized terminal reserve for an ACTUAL
positive17/4 source. Equation(12) is at fixed K; at the own ratio only
the negative-average/at-least-one-terminal conclusion is asserted.

Finally4(n+k)<2^34 and K*(tI(g5)+2+2k)<2^34 give, for every original
proper block simultaneously, N_A*,abs(S_A*)<2^-9966. This is a stronger
fixed-constant obstruction satisfying even all-block absolute approximate
eligibility. It is not a disproof of full FEI: no unbounded-ratio family
is supplied, and the exact smaller-child condition remains false.
