# A014 stage20: a spectral sector pays an arbitrary core from the ORIGINAL source

All logarithms are base two. The theorem concerns ideal complete probability
cross-entropy, and supplies no unpriced application-specific query fee.

## The theorem and the reference, fixed before the core spectrum

Let a>=1 and b>=3a be integers, n=a+b. Partition the variables into X,Y
of sizes a,b. Let H be ANY simple graph on X, and let R=H join K_b:
every Y vertex is joined to every other vertex. Fix lambda=1/(n-1),
D=(1+lambda/4)^|E(R)|-1 and the ORIGINAL complete stage5 edge-occupation
mass M_R. Put F_R=D M_R, Z_F=sum_nonempty F_R, q_R=F_R/Z_F.
No graph, weight, prime table or normalizer is chosen after sampling a
Fourier set. The graph H may be chosen independently of the function below.

Let g:{0,1}^a->{0,1} be ARBITRARY, including zero and one. Define the
actual Boolean indicator and +/-1 function

 C(x,y)=g(x)1[y=0]+1[x=0]1[|y|=1],    f=1-2C.                 (1)

The two sectors have disjoint INPUT supports. No Fourier orthogonality,
monotonicity, FEI bound, paid reference or influence bound for g is assumed.
Let p=fhat^2, s=EC, v=Var(f), I=sum |S|p(S). Use the full reference
Q(empty)=1-v, Q(S)=v q_R(S) for S!=empty. Then

 CE(p,Q) <= (298/3) I <100 I.                                (2)

In particular g may be the independent-set indicator of H; then f is
EXACTLY the original graph Boolean family for R, not a substituted target.
Taking H to be r disjoint edges, a=2r,b=6r, closes stage19's precise NEXT
with the SAME original occupation reference. More generally (2) covers
every Boolean core, with no supplied core FEI constant.

## 1. One mass lower bound on the good spectral sector

For nonempty S, write u=|S intersect X|, l=|S intersect Y|, k=u+l.
Call it good if l>=a; then l>=u. Match every selected X vertex to a
distinct selected Y vertex, and match the remaining Y vertices within
their clique, leaving at most one Y vertex unmatched. These are valid
maximal matchings of R[S], regardless of H.

Put h=floor(k/2). If l-u=2t, the number of these matchings is
(l)_u (2t-1)!! >=h!, since (2t-1)!!>=t! and
(l)_u=product_{j=1}^u(2t+j)>=product_{j=1}^u(t+j).
If l-u=2t+1, the count is (l)_u (2t+1)!!>=h! by the same argument.
The double-factorial convention (-1)!!=1 handles empty residuals.

Each untouched root contributes lambda/48. If one Y vertex is unmatched,
its COMPLETE attachment factor is

 lambda[(n-k)/32+(k-1)/48] >=lambda(n-1)/48=1/48.              (3)

Thus F_R(S)>=h! (lambda/48)^h /48 in both parity cases. From stage19's
elementary factorial inequality,
log(1/[h!(lambda/48)^h])<=9n/2. Since n>=4, log48<6<=3n/2.
Stage19's complete, independently summed normalizer has log Z_F<=n/4.
Therefore good sets have log(1/q_R(S))<=25n/4. This loose constant is
already below the common base39n/4 used next. All contributions of the
original occupation law, including omitted additional matchings, remain.

## 2. A bad-sector cost with no worst-case read multiplier

The complement of R has maximum degree d<=a-1. Since n>=4a, stage19's
mass/normalizer bound applies without change:

 L(S):=log(1/q_R(S))<=19n/4+a(log n+20)
                  <=39n/4+a log n.                          (4)

Combining (3)-(4), with B={S!=empty: |S intersect Y|<a}, gives

 L(S)<=39n/4+a log n *1_B(S).                                (5)

Only the actual spectral mass of the deficient sector pays the log n term.
Define the spectral tail congestion

 kappa_tail= a log n * sum_{S in B}p(S) / I.                 (6)

This is NOT CE/I in disguise: it uses just the Fourier mass of an explicit
cardinality sector and the actual physical influence. On this family it
stays bounded even when read and stage19's defect reserve grow unboundedly.

## 3. Exact physical influence, without any core assumption

Let N=sum_x g(x), c=g(0), and e_g be the number of core cube edges on
which g changes. Counting X and Y boundary edges of (1) separately gives

 s=(N+b)/2^n,
 I=2[e_g+ab+b(N+b-2c)]/2^n
  =2[e_g+b(N+n-2c)]/2^n.                                    (7)

Indeed each singleton Y slice is the X point event, contributing a edges;
the Y-empty slice contributes e_g. The Y-empty/singleton boundary has
b(N+1-2c) edges, and the singleton/doubleton boundary has b(b-1) edges.
Subtracting n*s from I and multiplying by2^n gives
2e_g+(b-a)N+b(n-4c)>=0. Thus I>=ns and v/I<=4/n.

C is supported on Y weights0 or1, so s<=(b+1)/2^b<=1/2 for b>=3.
Also s>=b/2^n>=2^-n, hence v>=2s>=2^(1-n).
The FULL binary wrapper satisfies h2(v)<=v log(e/v)<=5nv/4.
Consequently (5) yields

 CE(p,Q)<=11nv+a log n *tau <=(44+kappa_tail)I,
 tau=sum_{S in B}p(S).                                      (8)

## 4. The deficient spectral sector is paid uniformly for EVERY core

Write C=C0+C1 for the two disjoint input sectors in (1), with masses
s0=N/2^n, s1=b/2^n. Their normalized squared Fourier laws are products:
under C0 the Y Fourier set is uniform; under C1 its Y cardinality L has
probability binom(b,l)2^-b (b-2l)^2/b. Core Fourier laws are unrestricted.
When N=0 omit the zero C0 law. A direct character sum gives these facts;
we never multiply merely conditional estimates without product structure.

For L~Bin(b,1/2), put rho=2^a(3/4)^b. Markov on2^-L gives
Pr(L<a)<=rho. Differentiating its elementary binomial generating function,

 E[(b-2L)^2 2^-L]/b = [(b+8)/9](3/4)^b.                    (9)

Thus the normalized C1 bad-sector probability is at most(b+8)rho/9.
On every nonempty Fourier set, p_f(S)=4(Chat0(S)+Chat1(S))^2
<=8(Chat0(S)^2+Chat1(S)^2). Summing the bad sector, including extra empty
terms on the upper side when needed, gives

 tau<=8[s0+s1(b+8)/9]rho <=(8/9)s(b+8)rho.                   (10)

The last inequality uses b>=3, so (b+8)/9>=1. This pays cross interference
by the explicit two-sector square inequality once, not per gate or read.

Since a<=b/3, rho^3<=(27/32)^b<=(19/20)^(3b).
Set q=19/20. Then rho<=q^b<=exp(-b/20). Also n<=4b/3 and
log n<=(b+1)/2 for every integer b>=3: equality bounds the base b=3,
and sqrt2>4/3 bounds successive ratios. Elementary maximization of
t exp(-t) and t^2 exp(-t), with e>2, gives
b q^b<=10, b^2 q^b<=400. Therefore

 (b+8)log n rho <=(b^2+9b+8)q^b/2 <=249.

Using a/n<=1/4 and I>=ns in (6),(10) gives
kappa_tail <=(2/9)(b+8)log n rho <=166/3. Combining with (8) proves (2).
The elementary constants log e<3/2 and e>2 follow from the exponential
series and ln2=2(1/3+1/(3^3*3)+...)>2/3.

## 5. The same root account, including all old bookings and full terminals

Version6's full-CE projection/calibration identity applies to EVERY f and
positive complete q, so it applies here. Both children inherit
qbar(T)=[q(T)+q(T+i)]/[1-q({i})]; only actual empty/nonempty masses are
calibrated, with that calibration explicitly funded by the parent cost.
Every finite adaptive restriction tree and stopping cut has

 sum_internal reach*actual_full_CE_decrease
 +sum_terminal reach*FULL_terminal_CE = ORIGINAL_root_CE <=100I_root.

All terms are nonnegative. No child clique ratio, new core bound, retuned
table, renewed influence allowance, or discarded terminal is invoked.
These decreases are not asserted to equal arbitrary witness/query charges.

## 6. Exact solved obstruction and the next unsupported line

For H a matching of r edges, a=2r,b=6r, g its independent-set indicator,
the reference is EXACTLY stage19's R. There is an actual supported set
S=X with log(1/q_R(S))/n>=log n/8, so the pointwise shortcut still fails.
Nevertheless its entire weighted reference is now paid by (2). This is
the precise failure mode repaired, not an instancewise reference change.
Every reference edge is a necessary positive size-two minterm of this
graph family, so maximum positive-DNF read is n-1. Its old defect reserve
also diverges: I/v<=n implies kappa_def>=(2r-1)(log n+20)/(8r)
>=(log n+20)/8, whereas kappa_tail<=166/3. The new quantity therefore
closes a genuinely growing-overlap regime missed by the preceding bound.
Indeed kappa_tail<=(2/9)(6r+8)log(8r)(729/1024)^r tends to0.

## 7. Exact all-relevant obstruction to transferring the terminal to its own influence

Choose H empty, b=3a, a>=3. The ORIGINAL reference is invariant under ALL
permutations of X. After every Y variable is physically revealed to be0,
the inherited nonempty law q_X is the original q_R projected onto X and
conditioned on nonempty image; it is still invariant under those
permutations. Hence q_X({i})<=1/a for every i. The branch has positive
reach2^-b, not a hypothetical reference selected off the Boolean family.

Choose its core sign function
 F_a(z)=z_1 [1-2 AND(z_2,...,z_a)],
where AND is the indicator that all last a-1 bits have a fixed sign.
Take g=(1-F_a)/2 in (1). Then every core variable is relevant, F_a is
balanced, and
 p_a({1})=(1-2^(2-a))^2>=1/4,
 I(F_a)=1+(a-1)/2^(a-2)<=2.
Therefore the FULL inherited terminal reference, with its actual empty
mass0, satisfies

 CE(F_a,q_X)/I(F_a)>=(log a)/8 ->infinity.                    (11)

This is an ACTUAL Boolean family and ALL core variables remain relevant.
It refutes a universal inherited-terminal bound CE_terminal<=K I_terminal
from the root payment alone. It does NOT refute FEI, the root100I bound,
or the original-account stopping identity. The parent source includes the
physical auxiliary influence and the terminal is reach-weighted in that
account; neither may be silently removed. Exposing irrelevant bits is not
needed for this obstruction.
Indeed H(F_a)=H(1-2 AND on a-1 bits)<=1+4(a-1)/2^(a-1)<=3,
by its exact equal nonempty Fourier masses and the binary-entropy bound1.
Since I(F_a)>=1, this same family has H/I<=3. The upper bound I<=2 above
follows at a=3 and decreases thereafter because a/[2(a-1)]<=3/4.

## 8. Exact profile enumeration used by the certificates

The Y-clique symmetry is the only computational reduction. Every maximal
matching has either an independent unmatched set U in selected X and no
unmatched Y, or exactly one unmatched Y and no unmatched X. In the first
case enumerate its internal-X root matching on selected X minus U; let
c be the number of remaining X vertices, all matched across to Y. Its
Y multiplicity is (l)_c times the perfect-matching count on l-c vertices,
when that number is nonnegative and even. All choices have the same
canonical attachment integral since U sees every Y endpoint identically.
In the second case the multiplicity is l(l-1)_c times the perfect-matching
count on l-1-c vertices; its sole leaf factor is exactly(3). These cases
are disjoint and exhaustive, and unmatched independence is precisely the
maximality condition. Multiplying every profile by binom(b,l) retains
ALL labelled Fourier sets in the full Z_F. Core subsets/H are not quotiented.

## 9. Rigorous arithmetic in the final checker

The final certificate log evaluator uses integer-directed intervals at
scale2^64. For z=(x-1)/(x+1),1<=x<=2, floor/ceiling enclose z and z^2;
successive directed products enclose each z^(2j+1), and directed divisions
by2j+1 enclose its series term. Eighteen terms give lower/upper finite
sums; the omitted tail is at most2(1/3)^37/[37(1-1/9)]
=9/[148*3^37]. Computing ln2 by this same enclosure, dividing positive
intervals in the appropriate directions, and adding the exact power-of-two
normalization exponent encloses log2 of EVERY positive rational input.
Final endpoints are rounded outward to denominator2^40. Python integers
are unbounded, so intermediate products do not overflow. This arithmetic
change affects efficiency only; all claimed signs use rational endpoints.

## First unsupported line

For arbitrary core g the theorem proves a paid activation family, not
full FEI: the b private auxiliary variables supply substantial physical
influence. Remove the auxiliary padding in the ORIGINAL root payment,
or fund an intrinsic whole-set/profile reference from the actual unpadded
function's influence. The naive bound by the reached core's OWN influence
is now refuted by (11), so it is not listed as an open lemma. Arbitrary
linear hypergraphs/Boolean functions still lack the universal root payment.
Full FEI remains OPEN.
