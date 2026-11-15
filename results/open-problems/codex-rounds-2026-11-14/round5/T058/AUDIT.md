# Audit of the packing lemma

## An independent count for the leading constant

First choose the unique common vertex v. Then choose two disjoint
(k-1)-sets A',B' outside v, and divide by two for the order of the pair.
There are

    (n/2) binom(n-1,k-1) binom(n-k,k-1)

such pairs. The edge constraints inside {v} union A' and {v} union B'
are disjoint, so the probability both sets are independent is q^2.
Using n binom(n-1,k-1)=k binom(n,k), this is exactly the j=1 term
in PROOF.md. Replacing the two binomial coefficients by their leading
ratios gives mu^2 k^2/(2n), including the factor 1/2.

There is also an incidence count. For a fixed graph let d_v be the
number of its independent k-sets containing v. Then

    sum_v binom(d_v,2) = sum_(j=1)^(k-1) j Y_j.

Every pair is counted once for each of its common vertices. In
particular the incidence expression is not equal to Y if pairs can
share more than one vertex. The verification script checks this
identity graph by graph as well as counting pairs directly.

## A second deletion argument

Build a packing greedily from all independent k-sets. Each rejected set
intersects a retained set, hence can be assigned such a conflicting
pair. Different rejected sets give different pairs, so their number is
at most Y. If the greedy packing has size g, then X-g<=Y and M>=g,
which gives X-M<=Y. This does not require the greedy packing to be
maximum. The script computes the maximum independently by vertex-subset
dynamic programming and by enumeration of subfamilies.

## Threshold and centering

The leading deletion bound is mu^2 k^2/(2n). Dividing by the standard
deviation scale sqrt(mu) leaves mu^(3/2) k^2/(2n). Its decay condition is
equivalently mu=o((n/k^2)^(2/3)). Substituting mu=n^(t+o(1)) gives
3t/2-1<0, hence t<2/3 with a fixed margin. Equivalently, the expected
number of conflicts per set has size mu k^2/n; multiplying this by
sqrt(mu) gives the same normalized loss. These two calculations check
both the sign and the exponent.

This is an upper bound on X-M, not an equality. Divergence of EY/sqrt(mu)
above 2/3 would not prove divergence of (X-M)/sqrt(mu), even in
probability. The proof states no claim at phase 2/3. Its uniform o(1)
terms need fixed separation from phase 0, as the bound for the larger
intersections is divided by mu. The exact mean condition is useful
without replacing mu by a phase power, but no moving-phase extension of
the preceding joint count theorem is asserted.

Centering is checked from E M=mu-E(X-M). Thus (E M-mu)/sqrt(mu) tends
to zero in precisely the same range. The joint limit follows either
by the explicit characteristic-function comparison in PROOF.md or by
Slutsky's theorem applied to the rechecked count limit and
(X-M)/sqrt(mu)->0 in probability. The two arguments agree. An L1
approximation does not imply variance asymptotics or conditional
independence of raw counts, and neither is claimed.

## Bounds and small cases

The exact sum for EY excludes j=k (equal sets) and includes j=1
(one shared vertex). At j=k-1 the conditional expectation is exactly
k(n-k)2^(-(k-1)), which agrees with the s=1 version of the large-overlap
formula. The bound w_1=2kn2^(-k) is larger by n/(n-k), with the correct
direction. At the small-overlap endpoint, v_2=2k^4/(n-k)^2, so multiplying
by O(k) gives the k^5 factor in the proof. The direct endpoint values
and full sums are compared with the convexity bounds in exact rational
arithmetic.

For the empty graph, X=binom(n,k), M=floor(n/k), and Y counts all
intersecting set pairs. For the complete graph, X=M=Y=0 when k>=2.
For k=n there is at most one independent k-set and X=M, Y=0.
The exhaustive checks include these cases, all k=2,...,n and every
graph on n=5 and n=6. The asymptotic proof only uses k>=4, which holds
eventually. The definition k=floor(f(n)) need not match these small
sizes: finite enumeration tests the combinatorial identities, not the
Gaussian limit.

## What this leaves open

The independent numerical audit uses logarithms of each conditional
overlap term and sums with log-sum-exp. It agrees with the nine exact
rational scales within 3.13e-9 in log10 units. At the largest inputs the
finite-population error is too small to represent as a positive double;
its bound is therefore stored in logarithmic units. The extended values
are diagnostics with rounding and finite-population error, not certified
finite-n bounds. In particular phase 5/8 at n near 2^320 still has
EY/sqrt(mu) approximately 20,003; the asymptotic theorem gives no claim
of a small error at that n.

The packing uses o_p(n) vertices on fixed interior bands. To control
the chromatic number one must also control the optimum colouring of
the remaining graph and its dependence on which packing was selected.
The existence of Gaussian packing fluctuations alone supplies no
upper or lower concentration-width bound for chi. The literature
check found no full solution, and no novelty in the published
literature is claimed for this elementary packing transfer.
