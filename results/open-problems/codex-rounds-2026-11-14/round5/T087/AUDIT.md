# Independent checks of the rectangular criterion

## Face extraction checked by an integer-valued walk

For a path ending on a signed outer face, write a_t=sigma*x_i(t).
It is an integer-valued sequence with |a_{t+1}-a_t|<=1, starting
at a_0<=n and ending at 2n. Let t_* be its last index with a_t=n.
Such an index exists by the discrete intermediate-value property.
If a later a_t were below n, reaching the final value 2n would require
another visit to n after t_*, a contradiction. Thus its retained
segment has a_t in [n,2n]. All transverse coordinates remain in
[-2n,2n] because the original path is inside B_{2n}.

This recovers the rectangle extraction without using any monotonicity
of the path itself. The starting vertex can be on the inner face;
the endpoint can be at an outer corner, where any maximizing signed
coordinate can be selected. The proof also works for n=1.

## The count and BK checked separately

There are d choices of the coordinate and two choices of its sign.
For each original component, exactly one signed face is selected. In
each class, its chosen paths belong to different B_{2n} components,
so their vertex sets are disjoint. Their edge sets therefore witness
disjoint copies of the increasing rectangle-crossing event. This
checks the deterministic factor 2d in (8).

No application of BK to {K_n>=u} is legitimate in general: opening
an edge between two crossing components merges them and can reduce
the count. The maximal edge-disjoint-path count D is a different,
increasing variable. Two parallel crossings joined by an extra open
edge can have component count one and disjoint-path count at least
two. The proof uses the inequality from component count to path count
in the correct direction, never equality.

For a rectangle with crossing probability R, BK gives P(D>=k)<=R^k.
An independent derivation of its expectation bound uses stochastic
domination by a geometric variable G with tail P(G>=k)=R^k,
k=0,1,2,... . If e=E G, its memoryless decomposition gives
e=R(1+e), hence e=R/(1-R). Thus E D<=R/(1-R), agreeing with the
tail sum in PROOF.md. Taking the expectation of the deterministic
sum of 2d path counts gives exactly 2d R/(1-R); summing the union
bound instead would lose an unnecessary factor 2d.

For integer u and M summands, if all summands are below ceil(u/M)
then their sum is at most M(ceil(u/M)-1)<u. This checks the ceiling
in both tail bounds. With u=floor(n^epsilon)+1, u>n^epsilon;
the conversion from >= to > in (13) has the correct integer threshold.

The inequality R^k=(1-delta)^k<=exp(-delta*k), with
k>=u/(2d), independently confirms the sign and denominator in (1).
If delta>=n^{-epsilon/2}, its exponent at u>n^epsilon is at most
-n^{epsilon/2}/(2d), exactly the displayed rate.

## The shell cover checked coordinatewise

Put q=n/m>=8 and h=floor(3q/2). Then

    3n/2-m < mh <= 3n/2.

A center z on the m-grid shell has every coordinate at most mh in
absolute value, so every coordinate of z+B_{2m} is bounded by
mh+2m<=7n/4. At least one center coordinate has absolute value mh;
that coordinate in the entire small box has absolute value at least
mh-2m>3n/2-3m>=9n/8. Thus the small box is inside B_{2n} and
outside B_n. These are separate coordinatewise checks of (9)–(10).

If an original path hits the intermediate shell at y, rounding y/m
changes every coordinate by at most 1/2 and leaves a coordinate equal
to h or -h fixed. The rounded center is on the required shell, and
y is within m/2 of it. At the outer endpoint, a coordinate attaining
2n differs from the corresponding center coordinate by at least
2n-mh>=n/2>=4m. The path therefore crosses the small box before its
endpoint. A first boundary hit keeps its initial part inside that box.

Two different original box components cannot be mapped to the same
small-box component, because that small box is contained in B_{2n}.
Connections outside the original box are irrelevant. Splitting of one
component under restriction to a small box only enlarges the possible
right side. No independence among covering boxes is assumed.

## Shell cardinalities and constants checked without calculus

Counting the shell by subtracting its interior gives

    S=(2h+1)^d-(2h-1)^d.

Independently, partition by the first coordinate attaining absolute
value h. The count is

    S=2 sum_{i=1}^d (2h-1)^{i-1}(2h+1)^{d-i}
      <=2d(2h+1)^{d-1}.

This proves the same bound as the derivative argument in PROOF.md.
Since 2h+1<=3q+1<=4q, multiplying by 2d rectangles per covering box
gives N<=4d^2 4^{d-1}q^{d-1}. Thus the covering loss has exponent
d-1, rather than d, because the centers lie on a shell.

In d=3, expanding the difference of cubes gives S=24h^2+2 and
N=144h^2+12. A separate face/edge allocation gives

    S=2(2h+1)^2+2(2h-1)(2h+1)+2(2h-1)^2,

which expands to the same polynomial. At the extremal ratio n=8m,
h=12 and the two counts give

    S=25^3-23^3=15625-12167=3458,
    S=2*25^2+2*23*25+2*23^2=1250+1150+1058=3458,
    N=6*3458=20748=144*144+12.

The dimension-three general constant is
C_3=4*9*16=576. Independently, the direct count uses at most
6*(2h+1)^2 covering centers and then six path counts per center;
with 2h+1<=4q this gives 36*16*q^2=576q^2. At q=8 this upper
bound is 36864, larger than the exact 20748, as required.
These numbers are exact arithmetic, not percolation measurements.

## Interpolation on logarithmic scales

For the chosen largest m_j<=n/8, let b_j=log m_j. Then
b_j<=log(n/8)<b_{j+1} and b_{j+1}/b_j->1. Dividing by b_j
shows log(n/8)/b_j->1, hence log m_j/log n->1. This independently
checks the squeeze in Corollary 3. The logarithm of the expectation
bound, divided by log n, is bounded by

    o(1)+(d-1)[1-log m_j/log n]
        +[log(1/delta(m_j))/log m_j] [log m_j/log n].

Both nonconstant terms tend to zero separately. This confirms the
result at every n, including n just before the next selected scale.

For the example m_j=floor(exp(j^2)), log m_j=j^2+o(1), so the
successive logarithm ratio tends to one. The ordinary successive
ratio has logarithm 2j+1+o(1), and is unbounded. This explains what
the sparse-scale corollary permits.

Arbitrary sparse scales would not suffice for this estimate. If
m_j=2^{2^j} and n is of order m_j^{3/2}, the largest selected scale
below n/8 is m_j, and n/m_j=n^{1/3+o(1)}. The covering bound then
loses n^{(d-1)/3+o(1)}, a polynomial. This is a limitation of the
argument; it is not a counterexample to (P) for percolation.

## Limits of the criterion

The bound delta(n)>=(log n)^{-b} implies
log(1/delta(n))/log n<=b log log n/log n->0. More generally a
subpolynomial reciprocal deficit suffices. A bound of the form
delta(n)>=n^{-c}, with a fixed c>0, yields only
E K_n<=2d n^c by this argument and does not establish (H).
The criterion is sufficient, and necessity is not asserted.

Finiteness of every rectangle ensures delta(n)>0 at p<1, but this
alone is far too weak: the explicit cut closure only gives
delta(n)>=(1-p)^{(4n+1)^{d-1}}. It supplies no subpolynomial bound.
The parameter p=1, where the deficit is zero, is excluded throughout.

No one-arm exponent, two-point exponent, or near-critical exponent
is proved to exist on critical Z^3. The predecessor equivalence and
volume-tail formula are invoked only after their hypotheses have
been supplied conditionally. The rectangle aspect ratio is exactly
4 in this proof; no unproved conversion from the classical aspect-3
criterion is used. Literature priority is not claimed.

No invalid step was found in this audit. No numerical program was run.
