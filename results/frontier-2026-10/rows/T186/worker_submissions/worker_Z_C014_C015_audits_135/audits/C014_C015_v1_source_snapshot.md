# C014/C015 v1: finite strong-core bounds by a stopped birth forest

Status: proof (unaudited). Target 3(d), sufficient finite positive-core bounds.
These claims are independent of the tree fixed-point candidates C005--C012.
No exact threshold, complement exponential tail, or circumference extension
is claimed. The hardest remaining threshold step is transfer of the positive
tree fixed point to a finite giant core near the tree onset.

## Certified consequences

For every integer n>=4,000,000 and every real c in [11.415,n],

    Pr(|S_4(G(n,c/n))| <= 9n/10) <= 5 exp(-n/1,000,000).  (C014)

For every integer n>=3,000,000 and every real c in [9.053,n],

    Pr(|S_3(G(n,c/n))| <= 7n/8) <= 4 exp(-n/1,000,000).   (C015)

Here S_k is the maximal strong k-core: every vertex in S_k or adjacent
to S_k has at least k neighbors in S_k. All decimal parameters below
are exact rationals. The event for a noninteger density threshold is
interpreted as the corresponding integer inequality.

| k | c0 | theta | theta_plus | u | R | delta | n0 |
|---|---|---|---|---|---|---|---|
| 4 | 11.415 | .1 | .100001 | 1.223 | .025305 | .000001 | 4,000,000 |
| 3 | 9.053 | .125 | .125001 | 1.315 | .042379 | .000001 | 3,000,000 |

The exact checks below establish (A),(B). The elementary remaining
conditions follow directly from these rational inputs. Also
4/(1-.100001)<5 and 3/(1-.125001)<4. Since
n-ceil(theta*n)=floor((1-theta)*n), criterion (C) gives the displayed
consequences, uniformly for the stated c. No monotonicity of the core
under edge addition is assumed.

## Criterion

Let k>=2 be an integer and m=k-1. Write E_m(x)=sum_(j=0)^m x^j/j!.
Suppose positive rational numbers c0,theta,theta_plus,u,R,delta satisfy

    0<theta<theta_plus<1,  u>1-theta,
    c0 >= m/(1-theta_plus),
    u exp[-c0(1-theta_plus)] E_m(c0(u+R)) <= R,           (A)
    theta log(u)+theta+(1-theta)log(1-theta)-R >= delta.  (B)

For every n with n>=k/(theta_plus-theta) and every c in [c0,n], let
G=G(n,c/n). Then, for its maximal strong k-core S,

    Pr(|S| <= n-ceil(theta*n))
        <= k/(1-theta_plus) * exp(-delta*n).             (C)

In particular, with probability tending to one, |S|>(1-theta)n.
The count is uniform over c in the stated range. The conclusion for
each fixed c>=c0 is enough for the current target.

## Peeling and the stopped witness

Begin with all vertices black. If a black or blue vertex v has fewer
than k black neighbors, color v red and color each of its current black
neighbors blue. A vertex never becomes black again; an already red
vertex need not be selected. At most n selections are possible.

At termination every black or blue vertex has at least k black
neighbors, and every red vertex has no black neighbor. Hence the black
set is strong. It is maximal: if T is any strong set contained in the
current black set, a selected vertex v cannot be in T or N(T), because
then it has at least k black neighbors. Thus no vertex of T is removed
from black. Induction from the initial all-black set proves maximality.
This argument does not use a Poisson-tree or finite-WP transfer theorem.

Whenever a black vertex is selected, mark it as a root. Whenever a
black vertex w is first turned blue by v, give w the parent v. At any
time these edges form a rooted forest on the nonblack set T: a new
child has not previously been in the forest. Roots are red, blue
vertices are leaves, and every red vertex has at most m children,
because the selected vertex has at most k-1 black neighbors.

Let i0=ceil(theta*n). If the process ever has at least i0 nonblack
vertices, stop at the first such selection. A selection adds at most
k nonblack vertices (the selected vertex, if it is black, and its
at most m current black neighbors). Thus the stopped size i is one
of i0,...,i0+k-1, and theta<=i/n<=theta_plus under the stated bound on n.

Write V_R for the stopped red set. There are no edges from V_R to
V\T: each such outside vertex is still black, whereas a red vertex
turned all its black neighbors blue when selected. The necessary
witness consists of T, its red/blue coloring, and the birth forest.
No constraints on extra edges within T are imposed in the count.

## Exact labelled-forest count

Put p=c/n and z=exp[-c(1-theta_plus)]. A specified witness forest on
a specified i-set, with e forest edges and r red vertices, requires
all its e edges and forbids r(n-i) red-to-outside edges. These are
disjoint edge sets in the Erdos-Renyi model. Its probability is at most

    p^e (1-p)^(r(n-i)) <= p^e z^r.                     (1)

Let A(x) be the exponential generating series of rooted labelled
red-rooted trees, with a factor p per edge and z per red vertex.
A blue vertex is a leaf; a red vertex has an unordered set of at most
m children, each a blue leaf or another red-rooted tree. Consequently

    A(x)=x z E_m(p(x+A(x))).                           (2)

The forest is an unordered set of such red-rooted components, so its
exponential generating series is exp(A(x)). For a fixed labelled
i-set the total weight is i! [x^i]exp(A(x)); after choosing the i-set,
it is (n)_i [x^i]exp(A(x)). This counts every birth witness, possibly
many times for one graph, which is harmless for an upper bound.

For any c>=c0, condition (A) remains valid with c in place of c0:
for w=u+R, the logarithmic derivative of
exp[-c(1-theta_plus)]E_m(cw) is at most

    -(1-theta_plus)+m/c <= 0.

The polynomial inequality used here is x E_m'(x)<=m E_m(x) for x>=0.
Now put x=n u. Truncate (2) by the height of red-rooted subtrees,
starting at zero. The resulting nonnegative sums, divided by n,
are iterates of a -> u z E_m(c(u+a)); (A) bounds every iterate by R.
Monotone convergence therefore gives A(nu)<=nR. Nonnegative
coefficients yield the exact bound

    Pr(exists an i-vertex stopped witness)
       <= (n)_i n^(-i) u^(-i) exp(nR).                (3)

No independent red-vertex probabilities or unproved conditional
probabilities have been multiplied. Equation (1) is a single
independent-edge event for each fixed witness.

## Falling factorial and the exponential bound

For t=i/n<1, the left and right Riemann sums for log(1-x) give

    log((n)_i/n^i)
       <= n[-t-(1-t)log(1-t)]-log(1-t).              (4)

Let H(t)=t log(u)+t+(1-t)log(1-t). Its derivative is
log(u/(1-t))>0 for t>=theta. Combining (3),(4),(B), for every stopped
size i in the specified range, bounds the probability by

    (1-theta_plus)^(-1) exp[n(R-H(i/n))]
       <= (1-theta_plus)^(-1) exp(-delta*n).

There are at most k sizes, proving (C). Outside this event the final
nonblack set has fewer than ceil(theta*n) vertices, so its black set
has size at least n-ceil(theta*n)+1>(1-theta)n.

## Verification and scope

The certificate generator uses exact Fraction arithmetic, an alternating
exponential series with an explicit remainder, integer outward rounding
and seven squarings, and a rational atanh logarithm with its tail bounded.
The independent replay uses a positive exponential series and reciprocal,
and separate log(1+x) and log(1-theta) series. Their strict lower margins
for (A) and (B) minus delta are, respectively, at least

* k=4: .000004863729 and .000000221578;
* k=3: .000006408567 and .000009614657.

The displayed margin decimals are consequences of the integer enclosures;
the decisions use those enclosures rather than ordinary floating point.
Both implementations reject invalid parameters; a real one-unit
certificate alteration is rejected. The independent direct forest count
enumerates all 1100 graphs through five vertices, all forest rootings and
admissible colors, comparing 35 (k4) and 34 (k3) weighted coefficients.
An omitted unordered-component factorial is detected by a negative control.
These finite checks corroborate the generating series; the all-size proof
is the argument above and still requires external audit.

Rebuild certificates from exact inputs without reading any saved numerical
certificate, run alternative arithmetic, and repeat the direct enumeration:

    python -B -X utf8 scripts/target3_global_forest_reproduce.py

Every run preserves its fresh certificates in its own timestamped folder.
The frozen manifest identifies the particular successful run and all code
hashes. The numerical search is not used in the proof. Exact equality of the
finite threshold with a tree onset and a finite-graph exponential-tail
transfer remain open. These sufficient density bounds do not change
C003's reviewed target-1 cutoff c1=13.962.
