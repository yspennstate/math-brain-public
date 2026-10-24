# A013 stage 2: exact averaged queue-rank obstruction and a single-use reserve

All logarithms are in bits. These are author proofs, pending independent
review. The B03 lead v2 asks whether its exact (L),(S),(R) functionals
decrease under physical restriction. The answer is negative even after
averaging the two children. This corrects the proposed monotonicity
direction, not the lead's refined entropy bound. No full FEI claim follows.

## 1. Function family, cover, and actual restricted children

Let m=4t, t>=1. In binary coordinates use the genuine Boolean quadratic
bent sign b_m(z)=(-1)^(z1 z2+z3 z4+...+z_(m-1) z_m).
Its squared Fourier law is uniform on all subsets of the m core bits.
Proof: each two-bit factor has four coefficients of magnitude 1/2,
and disjoint products multiply coefficients. Each core influence is 1/2,
H(b_m)=m and I(b_m)=m/2. No campaign claim is needed for this calculation.

For d>=0 set f_(m,d)=chi_[d](x) b_m(z), on d fresh prefix coordinates.
Its spectrum consists of [d] union T, with T uniform on the core cube.
Its entropy is m and influence d+m/2. Querying the first remaining prefix
coordinate gives the two actual children +f_(m,d-1) and -f_(m,d-1), with
probability 1/2 each. Their spectra, subset and rank/rarity charges coincide.
At the terminal d=0 their minterm counts and root normalizers differ;
the label and normalizer account below averages them explicitly.
The queried physical influence is exactly one. All coordinates are
relevant to the function.

Take the positive full-minterm DNF of each sign. For n=m+d with d>=1
its number of gates is N=2^(n-1); each gate has support all n coordinates, probability
2^-n, clipped probability pi=2^-n, M=1, and maximum read k=N. Restriction
deletes false gates and removes the queried literal from surviving gates.
For d>=2 there are N/2 survivors. The final children have
N_+=2^(m-1)+2^(m/2-1), N_-=2^(m-1)-2^(m/2-1) minterms,
since the bent core has mean 2^(-m/2). No merging or
replacement by an arbitrary-function gate is assumed.

All conjunctions use the same physical order: remaining prefix first,
then z1,...,zm. Orientations differ with minterm signs, but conjunction
coordinates are equally desirable after orientation, so every chosen
order is legal. All candidate gate rank/rarity costs coincide for a fixed
coordinate and Fourier set. The proof's fixed-tie rule can therefore
assign every occupied coordinate to its first gate. This is the actual
minimum gate count, yields s=kappa=|A|, and is consistent with minimizing
G_j. The witness uses one gate as one root and has no forest edges.

## 2. Exact Theorem R functionals, including rarity

Write B~Bin(m,1/2), a=6/5, Gamma=120/11. Empty sets contribute zero.
For d>=1, the spectral nonempty mass v_d is one. For d=0,
v_0=1-2^-m. The label and subset functionals are exactly

    L_d=m+d-1 for d>=1,              S_d=0,
    average L_0=(1-2^-m)[m-1+(1/2)log2(1-2^-m)].

Here S is the unscaled subset sum; multiplying it by 6/5 still gives zero.
The rank part of R is

    T_d=a[ (1/2) log2(d!)+(1/2) log2((d+m)!)
                              - E log2((d+B)!) ].             (1)

This also holds at d=0 with 0!=1. The rank cost of a set A is
sum_(j in A) log2(rank(j)) - log2(|A|!). Prefix membership is deterministic
and each core coordinate is present with probability 1/2. This proves (1).
Among COMMON orders, this order minimizes the rank expectation: the
factorial expectation is order-independent, and assigning higher marginal
influences to lower ranks minimizes sum_j Inf_j log2(rank(j)) by a direct
two-coordinate exchange. The deterministic prefix influences are one
and every core influence is 1/2. This does not optimize independently
chosen orders for each gate or alternative covers.

Every gate rarity b is n=m+d. Thus the exact rarity part is

    Q_d=(m+d) E[(d+B) 1{120(d+B)<11(m+d)}],
    R_d=T_d+Q_d.                                          (2)

The quantity R_d is exactly sum_j Inf_j E_(nu_j) G_j of B03's
B03-R-REFINED-WITNESS-BOUND@1: since nu_j(T)=fhat(T+j)^2/Inf_j,
it equals sum_A fhat(A)^2 sum_(j in A) G_j(A). This equality is
proved by substituting the definition, not an assumption about derivative
piece independence. All gates have the same rank and sparse indicator,
so assignment ambiguity does not affect (2).

For d>=1 the original queue at lambda=1/k has root odds o_n=2^(1-2n),
root probabilities q_n=o_n/(1+o_n)=1/(1+2^(2n-1)), and normalizer

    Lambda_n=2^(n-1) log2(1+2^(1-2n)).                       (3)

For terminal sign children the exact odds are pi_m/N_+ and pi_m/N_-,
probabilities pi_m/(N_++pi_m) and pi_m/(N_-+pi_m), and
Lambda_(m,+/-)=N_+/- log2(1+pi_m/N_+/-), pi_m=2^-m.
The terminal normalization term is the average of v_0 Lambda_(m,+/-).
The vacuum and child sign probabilities are retained. This is the original uniform-label queue normalizer,
not the normalized sector law of the separate A012 activation reference.

## 3. Exact averaged rank jump and an unbounded local obstruction

For d>=1, subtract (1) to get

    T_(d-1)-T_d
      =a[ E log2(d+B) - (1/2)log2 d - (1/2)log2(d+m) ]
      =(a/2) E log2(1+B(m-B)/(d(d+m))).                    (4)

The second equality uses symmetry B and m-B and the identity
(d+B)(d+m-B)=d(d+m)+B(m-B). It proves that every rank jump is
nonnegative, and is strictly positive for m>=2. Both fair physical
children have exactly this jump. Jensen also gives the exact useful bound

    0 <= T_(d-1)-T_d
       <=(a/2)log2(1+m(m-1)/(4d(d+m))).                  (5)

For d=1, Chebyshev gives Pr(B<m/4)<=4/m. Since log2(1+B)>=0,

    T_0-T_1 >= a[(1-4/m)log2(1+m/4)-(1/2)log2(m+1)].       (6)

Its right side tends to infinity like (a/2)log2 m. Rarity cannot
cancel this: with rho=81/128, for m divisible by four,

    Q_1 <= (m+1)^2 rho^(m/4).                            (7)

Indeed sparse membership implies B<m/4. Markov applied to 2^-B gives
Pr(B<m/4)<=2^(m/4)(3/4)^m=rho^(m/4), and the gate rarity cost is
at most (m+1)^2. Therefore

    R_0-R_1 >= RHS(6)-(m+1)^2 rho^(m/4) -> infinity.       (8)

The averaged label jump is
-1-(m-1)2^-m+(1/2)(1-2^-m)log2(1-2^-m), lying between
-1-m*2^-m and -1-(m-1)2^-m. The lower bound uses
-(1-u)ln(1-u)<=u and ln2>1/2. S is zero. Hence the
combined averaged (L+S+R) jump also tends to infinity, while removed
physical influence is one. No fixed C repairs the proposed averaged
monotonicity by adding C Inf_(queried)(f) for this inherited cover, even
when its common order minimizes the rank term on both sides.

For m=256, entirely rational bounds already certify a positive combined
jump exceeding 1/2: log2(65)>6, log2(257)<9 give rank jump >27/16;
subtract 1+256*2^-256 and 257^2 rho^64, obtaining a lower bound >1/2.
No floating log is used in this sign certificate. The actual functions
have H/I tending to two; this is not an FEI counterexample.

## 4. Single-use nonlocal reserve for arbitrary prefix depth

Summing (4) over d=D,...,1 telescopes the NONNEGATIVE rank inflation:

    sum_(d=1)^D (T_(d-1)-T_d)=T_0-T_D<=T_0<=a*m/2.        (9)

The last inequality is proved directly. For a core coordinate of rank r,
its occupied-predecessor count given membership is Bin(r-1,1/2).
Jensen and the elementary binomial reciprocal identity give

    E log2(r/(1+Bin(r-1,1/2)))
       <= log2[r E(1/(1+Bin(r-1,1/2)))]
       = log2[2(1-2^-r)] <=1.

The identity follows by integrating ((1+t)/2)^(r-1) on [0,1].
Each coordinate is occupied with probability 1/2. Sum and multiply by a.

Rarity need not be monotone at every step. For FIXED B, sparse membership
is (Gamma-1)d+Gamma B<m. As d decreases there is at most one entry
into this condition. After entry, (m+d)(d+B) decreases. Thus the sum
of positive rarity increments, BEFORE taking expectations, is at most
the largest sparse value for that B. In a sparse state,
d<11m/109 and (m+d)(d+B)<(1320/11881)m^2. Moreover B<11m/120<m/4.
Taking expectations and applying the same rho bound gives

    sum_d (Q_(d-1)-Q_d)_+
      <= (1320/11881)m^2 rho^(m/4)
      <= (84480/106929) I(b_m) < (4/5) I(b_m).             (10)

The first inequality uses (E X)_+<=E(X_+) for each difference.
For the second, m=4t and rho<2/3, while t(2/3)^t<=8/9:
t=1,2,3 are direct, and consecutive ratios are <=1 for t>=2.
This is a bound on positive increments, not an illicit cancellation of
unpaid negative terms.

The positive normalizer changes obey

    sum_depth (average child vacuum-weighted Lambda - parent Lambda)_+
       <=average Lambda_(m,+/-)<=2^(1-m)<= I(b_m)/16.     (11)

For n>=m>=4, Lambda_n increases as n decreases: writing x=2*pi^2,
the derivative sign reduces to 2x/(1+x)-ln(1+x)>0 for x<1,
using ln(1+x)<=x. For the actual terminal states,
(1-2^-m) Lambda_(m,+/-)>Lambda_(m+1): the lower bound
ln(1+u)>=u/(1+u) gives a child value at least
(1-2^-m) pi_m/[(1+pi_m/N_+/-)ln2], whereas the parent is at most
pi_m/(2 ln2). Since pi_m<=1/16 and N_+/- >=1, the former exceeds
the latter. Hence all normalization increments are positive and telescope
to the averaged terminal value. The upper bound uses ln2>1/2 and
log2(1+u)<=u/ln2. Its last inequality holds at m=4 and then improves.

Labels decrease at each prefix removal, and S remains zero. Equations
(9)-(11) show, for every finite D,

    sum_(d=1)^D [positive R jump + positive v Lambda jump]
       < (33/16) I(b_m).                                (12)

This is one retained-core reserve for the ENTIRE tree. All nodes at the
same depth have identical spectra and metadata; their physical visit
weights sum to one. No ancestry influence is spent again at descendants.
If a terminal entropy bill is included, H(b_m)=2 I(b_m); allocate the
additional reserve and terminal bill together, at coefficient 65/16 on
the retained core influence, not as two independent uses of the same
unit budget. Prefix query influence D is separate. This is a transport
account for a known bent family, not a new class-FEI claim.

## 5. Exact remaining gap and change in mechanism

The v2 request for decreasing exact functionals is mathematically false
in both pointwise and averaged forms; the source-bound counterexample
above explains the departure from that direction. A local linear
restriction surcharge is false as well. The productive replacement is
a history-dependent, single-use retained-core reserve, with all root
normalizers and the terminal vacuum kept. The first unsupported universal
line is construction of such a reserve for arbitrary covers/Boolean
cores and actual restrictions that change the spectrum, without assuming
an absolute core FEI bound or reusing the terminal influence budget.

The common-order optimum and the one-root full-minterm cover are explicit
hypotheses. Optimizing all independently chosen gate orders, changing the
cover, or describing the output with an unrelated reference may remove
this obstruction; no no-go for those operations is asserted.
