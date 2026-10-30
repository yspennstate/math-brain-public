# A014 stage19: nonsymmetric dense overlap, one original occupation reference

All logarithms are base two. Let G be a simple graph on n>=4 vertices,
d=max_v(deg_complement(v)), and suppose n>=4(d+1). Put delta=min deg_G,
lambda=1/(n-1), D=(1+lambda/4)^|E|-1. These ORIGINAL edge weights are
fixed before a Fourier set or restriction history is seen. Let f=1-2C,
where C is the independent-set indicator of G. Let p be its squared Fourier
spectrum, s=EC, v=Var(f), I=sum |A|p(A). Use the stage5 complete occupation
mass M(A), F(A)=D M(A), Z_F=sum_nonempty F(A), q(A)=F(A)/Z_F,
Q(empty)=1-v, Q(A)=v q(A). No normalization factor is discarded.

Define the spectral defect congestion

 kappa_G=(d+1)(log n+20) / E[|S| : S is drawn from p conditional nonempty]
        =(d+1)(log n+20) v/I.                                  (1)

THEOREM. For every such G, the ENTIRE original-reference cost satisfies

 CE(p,Q) <= (24+kappa_G) I.                                    (2)

In particular, if (d+1)(log n+20)<=n, then kappa_G<=4 and CE<=28I.
This depends on arbitrary missing-edge incidence, not clique symmetry.
It is a sufficient criterion, not a universal bound on kappa_G.

## 1. Complete mass, including every attachment

For each maximal matching M in G[A], write r=|M| and U=A\V(M).
The set U is independent. A leaf u in U chooses an external neighbor
(weight lambda/32) or an endpoint of M (weight lambda/8). If a,b leaves
choose the two endpoints of one root edge, its additional exact factor is

 J(a,b)=a!b!/[(a+b+1)^2(a+b+2)].                               (3)

The root-edge factor is (lambda/24)^r. Sum over ALL maximal matchings and
ALL choices. This is exactly F(A). It is the original stage5 mass, not a
new reference. We prove both its lower bound and its full summed upper bound.

For c=a+b, J(a+1,b)/J(a,b)=(a+1)(c+1)^2/[(c+2)(c+3)]>=1/6,
since 6(c+1)^2-(c+2)(c+3)=5c^2+7c>=0. The other endpoint is identical.
Starting at J(0,0)=1/2 gives

 (1/2)6^(-a-b) <= J(a,b) <= a!b!.                            (4)

The first bound, summed over every leaf choice, shows that EACH maximal M
contributes at least a^r b^|U|, where a=lambda/48, b=lambda*delta/48.
External choices cost lambda/32>=lambda/48; internal choices cost at least
lambda/(8*6)=lambda/48. Every neighbor of an unmatched vertex is either
external or matched. All degrees are >=delta. Notice b>=1/96 and a,b<=1.

## 2. Matching multiplicity without exchangeability

Let k=|A| and r0=max(0,floor((k-2d-1)/2)). Repeatedly take the least
remaining labelled vertex and pair it with any remaining neighbor, for r0
steps. If the remaining size is t+2j, then t is 2d+1 or 2d+2, and there
are at least t+2j-1-d>=j choices. Thus there are at least r0! distinct
prefixes. Extend each prefix deterministically to a maximal matching.
The final matching uniquely determines its prefix by replaying the least
vertex rule, so these completions are distinct. For k<=2d+2 the empty
prefix case needs no counting. Always r<=r0+d+1 and |U|<=2d+2.
Consequently

 F(A) >= r0! a^(r0+d+1) b^(2d+2).                             (5)

For r0>=1, r0!>=(r0/e)^r0, log e<3/2 and log(48e)<15/2 give
log[1/(r0!a^r0)] <= 6r0+3(n-1)/2 <=9n/2.
This uses ln u<=u-1 with u=(n-1)/r0. For r0=0 the same bound is trivial.
The remaining root factors cost <=(d+1)(log n+6); the leaves cost
<=14(d+1). Hence, for EVERY nonempty A,

 log(1/F(A)) <=9n/2+(d+1)(log n+20).                          (6)

The defect loss is necessary for this argument: a set inducing disjoint
edges need not have factorially many maximal matchings. Dense G alone
does not imply a dimension-linear lower bound for every atom.

## 3. Full original normalizer, independently bounded

We prove Z_F<=exp(n/8), without importing a queue subprobability claim.
This upper-bound lemma needs only n>=2, an arbitrary simple graph, and
the FIXED lambda=1/(n-1); the density hypothesis is not used. Zero atoms
are permitted for this lemma alone. Positivity and the normalized complete
reference in the theorem still use its stated hypotheses.
Relax maximality, all edge restrictions on leaf choices, and disjointness
when doing so only increases the sum. For fixed root matching of r edges,
let t internal leaves attach to its 2r endpoints. The upper bound in (4)
counts their choices by ordered lists on the endpoints. For each weak
composition of t into 2r counts, at most n^t such lists occur, even if
distinctness is ignored. Summing t gives the upper factor

 sum_t binom(t+2r-1,2r-1)(n lambda/8)^t
       =(1-n lambda/8)^(-2r) <=(16/9)^r <2^r.                (7)

Here n lambda<=2. When r=0 there are no internal lists and the factor is1.
External leaves may be chosen from any subset of the n vertices, with at
most n choices of neighbor per leaf. Their sum is at most
(1+n lambda/32)^n<=exp(n/16). Allowing external leaves to overlap roots
or internal leaves only enlarges this product upper bound. The number of
root matchings with r edges is at most |E|^r/r!. Therefore

 Z_F <= exp(n/16) sum_r (2 lambda |E|/24)^r/r!
     <= exp(n/16+n/24)=exp(5n/48)<=exp(n/8).                 (8)

We included the empty structure on the right; this is harmless. No leaf
or root factorial has been silently discarded: the endpoint factorials
are absorbed by ordered lists before (7), and the root factorial counts
unordered root edges. Since log e<2, log Z_F<=n/4. Combining (6)-(8),

 log(1/q(A)) <=19n/4+(d+1)(log n+20).                        (9)

## 4. Actual physical influence pays the entire wrapper

Every independent set has size <=d+1. The family of independent sets is
a downset, so its internal cube edges are sum_{independent B}|B|.
Counting boundary edges exactly gives

 I=2s[n-2 E(|X| | C(X)=1)] >=2s(n-2d-2)>=sn.               (10)

Also v<=4s, hence v/I<=4/n. The minimum degree >=3n/4 ensures a triangle:
the endpoints of any edge have a common neighbor. Thus s<=1/2. The empty
input and all n singleton inputs are independent, so v>=2s>=2^(1-n).
The elementary binary entropy bound h2(v)<=v log(e/v) therefore yields
h2(v)<=v(n+1/2)<=5nv/4. Using (9),

 CE(p,Q)=h2(v)+sum_nonempty p(A)log(1/q(A))
        <=6nv+v(d+1)(log n+20)<=(24+kappa_G)I.              (11)

At v=1 the entropy inequality still holds by the usual 0log0 convention.
No FEI theorem or entropy bound is used to pay the reference.

## 5. Explicit growing defect and growing unavoidable overlap

For every integer m>=6 set n=2^m, d=floor(n/(m+20))-1. Let the missing
graph be a star K_(1,d), plus n-d-1 isolated vertices (d>=1). Then its
maximum degree is exactly d, it is nonsymmetric, and
(d+1)(log n+20)<=n. Thus the original reference CE<=28I for all m>=6,
although d tends to infinity and the positive edge DNF has maximum read
n-1. Every edge is a necessary size-two positive minterm, so this read
cannot be lowered by changing the positive DNF. Arbitrary missing graphs
with the same degree condition are covered, not just this example.

## 6. Same original account along every adaptive history

Use the stage18 proved full-CE projection theorem, with BOTH children
inheriting qbar(T)=[q(T)+q(T+i)]/[1-q({i})] and their actual variance
calibrations explicitly paid by the parent categorical cost. For every
finite adaptive restriction tree and stopping cut, the sum of reached
parent-minus-average-child FULL CE decreases plus reached terminal FULL
CE equals this ORIGINAL root CE. Each summand is nonnegative. Equations
(2)/(11) therefore fund all those terminals and old delta bookings from
the SAME root account. Restricted graphs need not satisfy the density
hypothesis; no child theorem or new allowance is invoked.

## 7. Exact obstruction to deleting the spectral defect reserve

Let n=8r, let A consist of 2r vertices inducing a perfect matching, and
join A completely to a clique on the remaining 6r vertices. Here
d=2r-2 and delta=6r+1, so n>=4(d+1) and min degree is at least 3n/4.
Nevertheless G[A] has just ONE maximal matching, and exactly

 F(A)=[48(n-1)]^(-r).                                        (12)

The singleton masses give Z_F>=lambda*sum_v deg(v)/32
>=n delta/[32(n-1)]>=1 for r>=8. Thus q(A)<=n^(-r), and
log(1/q(A))/n >=(log n)/8 tends to infinity. There is NO absolute
pointwise bound log(1/q(A))<=Cn even in this uniformly dense class.
The atom is actually in the Boolean spectrum: summing the independent
inputs gives Chat(A)=[6r+(-1)^r]/2^(8r), which is nonzero. Its squared
spectral weight is tiny; this obstruction does not refute a weighted
expectation bound, (2), the original-account identity, or FEI.

## First unsupported line

Bound the ORIGINAL complete occupation expectation on graphs with large
complement degree without paying (d+1)log n per nonempty spectral event,
or replace that defect payment by a genuinely sector-specific compatible
matching estimate. The atomwise bound here loses information on small
induced matchings. The root bound is not proved for arbitrary linear
hypergraphs, and no arbitrary application-specific query charge is
identified with the actual full-CE decreases. Full FEI remains OPEN.
