# Tensor witness constants and a finite-mixture mismatch barrier

Bits throughout. Full FEI is OPEN. The existing fixed-witness supplier remains a hypothesis.

## Scoped reconstruction of A003

For a Boolean seed f, the m-fold disjoint product has actual law p^m,
H_m=mH and I_m=mI. Retain the ORIGINAL fixed admitted witness identity
h2(v_m)+Kref*mI+R*_m=mH+v_m D(P_m^+||U_m),
where U_m is a subprobability on nonempty sets, including its missing-mass
penalty, and Kref=3+2log2(3)+log2(6e)=4+3log2(3)+1/ln2.
Nonnegativity of this complete divergence and h2(v_m)<=1 show
mH<=(Kref+K)mI+1+r_f(m) whenever R*_m<=K*mI+r_f(m).
If the same K precedes every seed, and each seed has an unbounded sequence
with r_f(m)/m->0, division by m gives FEI(Kref+K). Neither a common rate
of convergence nor factorized witness choices are needed. Constants have
H=I=0 and are handled separately. This reconstructs A003 stage22 section4
at its stated CONDITIONAL scope and improves the earlier sufficient bound
2+Kref+K by exactly2 bits per unit influence. It supplies no witnesses.
The generic complete-source CE<=C*mI+o(m) clause likewise gives FEI(C).
Other eligibility/local-erasure clauses of the source omnibus claim are
not independently accepted by this scoped review.

## A quantitative obstruction to a proposed tensor supplier

Let p be a finite probability law, and let q_1,...,q_N be normalized
references positive on its support. Reference-only atoms are permitted.
For each j, define the BIT log loss l_j(X)=log2(p(X)/q_j(X)), X~p,
d_j=E l_j=D2(p||q_j), and V_j=Var(l_j). These are finite. For any m>=1
and any nonnegative weights w_j (allowed to depend on m) with sum w_j<=1
and at least one positive, let Q_m=sum_j w_j q_j^m, a complete
subprobability reference. Then

 D2(p^m||Q_m) >= m min_j d_j - sqrt(m sum_j V_j).        (1)

Here divergence includes any missing-mass penalty. To prove (1), put
S_j=sum_{t=1}^m l_j(X_t) and Z_j=m d_j-S_j. Pointwise,
Q_m/p^m=sum_j w_j 2^(-S_j)<=2^(-min_j S_j), hence
D>=E min_j S_j>=m min_j d_j-E max_j Z_j.
For every real vector Z, max_j Z_j<=sqrt(sum_j Z_j^2).
Cauchy-Schwarz gives E sqrt(sum Z_j^2)<=sqrt(sum E Z_j^2).
The X_t are independent and centered in each j, so E Z_j^2=m V_j.
No independence between different references is used. A zero mixture
weight is harmless; all actual denominators are positive.

For a FIXED finite dictionary, divide (1) by m and compare with the
single-source upper bound D(p^m||Q_m)<=m d_j-log2(w_j), for any fixed
positive weight. With weights fixed and positive on a minimum-d source,
lim_m D/m=min_j d_j. The lower bound holds even if weights vary with m;
it alone proves liminf D/m>=min_j d_j. A varying-weight upper limit need
not equal that minimum and is not claimed. If all dictionary laws differ
from p, every d_j>0 by Gibbs equality, so NO such mixture has o(m)
mismatch. An admitted family of subprobability components can first be
normalized: treating their masses as extra mixture weights leaves (1)
valid; missing mass cannot improve the reference cost.

For GROWING dictionaries the variance bound is sufficient when
sum_j V_j=o(m). A stronger alternative uses the uniform loss RANGE L:
if every l_j has range length at most L, then for N>=2,

 D2(p^m||Q_m)>=m min_j d_j-L sqrt(m ln(N)/2).             (2)

The natural logarithm in this one expression is deliberate. Proof:
for centered Y of range length L, F(t)=ln E exp(tY) has F(0)=F'(0)=0
and F''(t)=Var_t(Y)<=L^2/4. The variance bound follows from
(Y-a)(b-Y)>=0 and (mu-a)(b-mu)<=(b-a)^2/4 under each finite tilted law.
Twice integrating gives F(t)<=t^2 L^2/8 for either sign. Independence
across samples and exp(t max Z)<=sum exp(t Z_j) give
E max Z_j<=ln(N)/t+t*m*L^2/8 for t>0. If L>0, optimize explicitly. If L=0 every centered loss is identically
zero and the bound is immediate without division by L. All tilted
expectations are finite sums, so differentiation is legitimate. N=1
has the exact expectation E Z_1=0 and needs no division by ln(N).
Thus even subexponentially many references with uniformly bounded ranges
and a positive common mismatch gap cannot produce o(m) mismatch.
If min d_j>=delta>0 and the range bound L>0 is common, achieving D/m->0
requires liminf ln(N_m)/m>=2delta^2/L^2. No assertion about growing
dictionaries without these quantitative conditions is made.

The target CE<=C*mI+o(m) DOES allow a linear mismatch budget
m(CI-H). Hence this theorem does not exclude a dictionary with sufficient
rate slack: its necessary condition is min_j d_j<=CI-H. Only a claim that
its positive mismatch itself disappears is refuted. The AND2 fixture
requires asymptotic source rate at least9/4; it does not obstruct a larger
fixed source constant or the prescribed Kref+4 target.

## Exact Boolean fixture and endpoints

Let h be +1 only at index0 on two bits, so all four squared Walsh
coefficients are1/4. For f_m=product of m disjoint h copies,
P_m is uniform on4^m labels, H=2m and I=m. Take
q1=(1/2,1/4,1/8,1/8), q2=(1/8,1/8,1/4,1/2).
On one block the bit log-loss vectors are (-1,0,1,1) and (1,1,0,-1).
Both have d=1/4 and V=11/16, verified exactly from the Boolean law.
For ANY mixture weights of total mass in(0,1],
D(P_m||Q_m)>=m/4-sqrt(11m/8)>=m/8 for every integer m>=88.
The last inequality is exactly m>=88 after squaring nonnegative sides.
Consequently CE(P_m,Q_m)>=17m/8 at m>=88, while actual H/I=2.
This is an obstruction to amortizing dictionary mismatch, NOT FEI.
The exact finite distribution of (S1,S2) is independently compiled by
integer convolution; at m88 it also gives a rational lower bound via
E min(S1,S2), valid simultaneously for ALL mixture weights.

For a dictionary containing q=p, the gap d can be zero and the obstruction
correctly disappears; positive weight w on that source gives D<=log2(1/w).
A character or constant p is a point law: V_j=0 and the exact mixture
loss is -log2(sum_j w_j q_j(atom)^m)>=m min_j[-log2 q_j(atom)].
Neither division by I=0 nor conditioning on an empty tail is used.
Near-constant Boolean seeds are included in the small exact tensor checks.

## Same original owner and first unpaid line

Every mismatch in (1) is a part of ORIGINAL full CE=mH+D. Earlier source,
selector and reset bills U stay added. If a physical-query history also
books query-KL contractions and projection fees, those must already occur
in its complete invoice; no terminal-functional identity authorizes
omitting them. Tensor division removes bounded/sublinear TOTAL overhead,
not the strictly linear mismatch certified here. Natural-unit information
multiplies H, D and l by ln2, and variance by(ln2)^2. Formula(1) therefore
scales consistently; mixing bits with natural ln(N) in (2) is justified
by its explicit exponential-moment derivation.

FIRST UNPAID UNIVERSAL LINE: construct ORIGINAL admitted fixed witnesses
or useful full references for EVERY Boolean seed with residual<=K*mI+o(m)
at a common K, retaining the full query ledger. A finite imperfect product
dictionary cannot supply vanishing source mismatch. A successful supplier
must exploit exact Boolean structure or let its reference family become
accurate or sufficiently rich; neither is constructed here.
