# Independent reconstruction: paid pairs retain arbitrary core debt

A055 stage8. Review target: A005-PAID-PAIR-WEAK-AFFINE-CORE-HARDNESS@1,
DERIVATION Sections2--6, source run20261023T035753Z. Verdict: scoped HOLDS
without a mathematical repair. This accepts the displayed embedding,
finite-to-infinite reduction, explicit physical refund and scalar example.
It does not newly accept the source Section1 complete-reset optimum or
A002 census, and is not a proof of universal critical pair selection.

## 1. Independently reconstructed physical gadget and all terminals

Work on finite uniform F2 cubes; entropy is in bits. Write h(x)=-x^2
log2(x^2), h(0)=0. Put Q=(-1)^(ab+ac+bc+za). Summing over z forces a=0
in its mean, and summing (-1)^(bc) gives EQ=1/4. The associated bilinear
matrix is nonsingular (its kernel forces a,b,c,z all zero), so its Walsh
coefficients have magnitude1/4. Thus H(Q)=4 and every influence is1/2.

Take a nonconstant full-span affine-influence-minimal g with H0>0,
q=I(g)>0, mu=Eg, and G=Q times t independent copies of g. Let v=mu^t.
Activate the WHOLE product with k>=2 controls: F=1+A_k(G-1), p=2^-k.
Keep the original physical pair(a,b). Its four branches ordered a+2b
are g^t, chi_c chi_z g^t, chi_c g^t, -chi_z g^t. All means before
activation are therefore v,0,0,0, not four copies of the root mean v/4.
All four contain the entire g^t. In branch1 substitute old c=c+z,
old z=z. This invertible physical permutation changes its character
weight from2 to1 without changing any core bit, control or entropy.
Physical influence release in that branch is p, at ORIGINAL reach1/4.
Other branches are unchanged. Thus r=p/4, I_pair=p, I_pair+r=5p/4.
No complete-affine optimum is needed to certify this executable release.

## 2. Coefficient multiset reconstruction and signed bank

If w has mean u, nonzero data coefficient a_s appears on all 1/p control
labels with amplitude p*a_s. Nonempty control-only labels have amplitude
-p*(1-u); the unique empty amplitude is1-p*(1-u). Therefore, directly
summing h over this complete multiset gives H(activation(w))=p H(w)+R_k(u),
where

R_k(u)=h(1-p*(1-u))-p*h(u)+p*(1-p)*h(1-u)
       +2*k*p*((1-u*u)+(1-p)*(1-u)^2).

Counting physical edges gives I(activation(w))=p*(I(w)+k*(1-u)). Applied
separately to the root and EACH actual reset child, these yield

Hroot=p*(t*H0+4)+R_k(v/4),
Iroot=p*(t*q+2+k*(1-v/4)),
Hchild0=p*t*H0+R_k(v), Ichild0=p*(t*q+k*(1-v)),
Hchildb=p*t*H0+R_k(0), Ichildb=p*(t*q+1+k), b=1,2,3.

Consequently L=4p+R_k(v/4)-R_k(v)/4-3R_k(0)/4 and, for D=H-KI and
the SAME S=average(K Ichild-Hchild), D+S=L-5Kp/4. This computation keeps
the full nonlinear mean correction and signed Fourier-row interaction;
there is no omitted mixed entropy refund and no second copy of release.
All child influences are positive for H0>0, since each includes p*t*q.
Character-only centering releases nothing: every child marginal is at
most2p<=1/2. Full affine optimization can release more but is not booked.

## 3. Uniform payment and all-dimensional passage

The continuous derivative h'(x)=-2x*(ln(x*x)+1)/ln2, extended by h'(0)=0,
has absolute value below6 on[-1,1] and below14 on[0,2]. These constants
follow by bounding |x ln|x||<=1/e for |x|<=1 and evaluating the increasing
absolute derivative on[1,2]; ln2>2/3 and e>2 suffice. The quadratic bracket
in R has derivative of absolute value at most6. Because the exceptional
coefficient stays in[1/2,1], |R_k'(u)|<=p*(26+12k). Two mean-value bounds
at0 give

|L/p-4| <= (26+12k)*(|v|/4+|v|/4)=(13+6k)*|mu|^t.

For each FIXED K>16/5 the positive margin eta=5K/4-4 eventually dominates
this error when k=max(2,ceil(sqrt(t))). Thus the original proper pair plus
one explicit conditional shear is strictly paid for all sufficiently large
t. This is an analytic all-t argument, not extrapolation from the replay.

Direct bounds on the five scalar entropy terms give |R_k(u)|<=p*(10k+20)
uniformly on[-1,1]: h(exceptional)<=8p, |h(u)|<=1, |h(1-u)|<=8, bracket<=5.
Hence Hroot/Iroot tends H0/q, while Iroot tends0; q>0 and k=o(t) keep the
ratio denominator positive. Full FEI(K) follows at SAME K from FEI(K) on
this paid-pair class with I<epsilon, by taking the limit for each seed.
Constants have zero entropy and need no ratio argument.

## 4. Affine admission, including full span

For the squared spectral law S, a finite centered parity basis minimizes
influence iff coordinate marginals p_i<=1/2 and every nonzero parity v
has minority cost >=max_{i:v_i=1} p_i. Necessity replaces one used row;
sufficiency follows by threshold rank counting, or greedy minimum-weight
basis exchange. Canonical compression exists in the finite affine orbit:
choose a minimizing basis and shift, remove its zero-cost coordinate
labels, and restrict the associated dummy physical variables. Entropy is
unchanged and influence cannot rise. Nonconstant entropy remains positive.

For a product of independent spectral laws, parity biases multiply. The
minority cost of a mixed parity is at least every used factor's minority
cost, so tensor affine minimality and full span are preserved. Q has
uniform full spectrum and is an affine minimum, so G has these properties.
For activation, pure data parity costs are p*w_G(u), while every direction
using a control has cost p*(1-EG). These are physical edge identities, so
not an assumption of a block-diagonal optimizer. Physical sign counting
bounds each old coordinate influence by1-|EG|<=1-EG. All activated costs
are at most2p<=1/2. The minimum-basis criterion now proves full affine
minimality of F. Nonzero old data coefficients crossed with every control
label, together with the nonzero empty coefficient, preserve full affine
span. Equivalently the raw G-1 spectrum contains all old nonzero labels
and a nonzero empty coefficient; its data span is full, and the full
control cube adds independent control directions. No constant+1 exception
arises because G includes the nonconstant bent gadget Q.

## 5. Exact failed critical condition and finite certificate

If d=H0-Kq>0, each COMPLETE reset terminal satisfies

Dchild >= p*(t*d-K*(1+2*k)-10*k-20)>0

for sufficiently large t. Further affine minimization only increases
this deficit for K>=0. Thus even the stronger paid-pair weak affine class
fails genuine smaller-Boolean-child nonviolation. If the root violates
and the pair is strictly paid, D+S<0 gives S<-D<0 exactly; a small negative
bank cannot be declared nonnegative as p tends0.

Independently re-evaluate the eight-bit point defect: mu=127/128,
q=1/16, H=h(127/128)+255*h(1/128), full spectral support and affine
minimality. Rational atanh bounds in the own-stage helper show
H-(15/4)*q>1/256. With t=100000000, k=10000, K=15/4, Bernoulli gives
|mu|^t<=128/(128+t), without forming that power. The replay certifies
paid margin/p >7633553/12500016 and all four terminal deficits/p
>862405/4. The root lower deficit/p is also positive. The construction
is an actual finite Boolean function; no enormous truth table is stored.
It is a fixed-constant negative-bank example, not a full FEI disproof.

## 6. Independent replay and review boundary

code/review.py was written from physical evaluations and this derivation,
without copying the source's implementation. It uses the pre-existing own
exact.py only for integer Walsh and rational prime-log arithmetic. It
exhausts all22 labelled seeds n0..2, four frozen(t,k) profiles, all original
terminals, and actual physical shear permutations. Root affine minimality
is checked by a separate Walsh transform of squared integer coefficients
for all parity costs; full span uses binary elimination. Every profile
also checks the exact signed bank at K=16/5,15/4,8 and the error bound.
No finite check substitutes for Sections3--4 analytic limit arguments.

Full:88 roots,352 physical plus352 reset terminals,40 qualified full-span
affine-minimal root profiles,4382 exact assertions PASS in18.778413s.
Pilot:22 roots,1118 assertions PASS in1.634170s, excluded from full count.
The run stays below the estimated100MB and55s cap; peak RAM unmeasured.
No Lean or external literature/novelty claim is made.

Verdict is scoped HOLDS without repair for A005 DERIVATION Sections2--6
and the explicit source claim's paid-pair-hardness conclusions. It is not
an independent recheck of all prior source dependency censuses or a full
universal proof-chain endorsement. A055 previously contributed a weaker
activation guard; this review supplies no repair or new statement version
to A005 and reconstructs the new paid-pair bridge independently.

FIRST UNSUPPORTED UNIVERSAL LINE: on a genuine least-dimensional positive
K-witness, force one ORIGINAL proper pair whose signed bill is paid from
the SAME unused affine-child reserves, using their nonnegativity and
quotient-rank release, with all terminals and mixed interaction retained.
Neither paid-pair existence on arbitrary roots nor weak affine admission
supplies this critical selection. No universal constant improves.
