# Audit of the centered packing argument

## The two kinds of intersection

The conflict graph used for packing joins two k-sets as soon as they
share a vertex. The comparison theorem instead uses intersections of
their graph-edge constraints, so it joins them only if they share at
least two vertices. Confusing these two graphs would invalidate the
argument above phase 1/2: the expected number of one-vertex conflicts
need not vanish. The proof applies the comparison theorem only to the
second graph, then studies the first graph inside the independent model.

For a fixed common vertex, choose the other k-1 vertices of the first
set, then the other k-1 vertices of the second set from outside the
first. This gives
\[
 \mathbb EY_1=\frac n2\binom{n-1}{k-1}\binom{n-k}{k-1}q^2.
\]
The factor 1/2 removes the ordering of the two sets. Using
\(n\binom{n-1}{k-1}=k\binom nk\) gives exactly the predecessor's
ratio \(\binom{n-k}{k-1}/\binom{n-1}{k-1}\) after division by
\(\mu^2k^2/(2n)\). This independently reproduces the previous
leading coefficient and explains why deleting all conflicts costs too
much without centering when \(3t/2-1>0\).

The expected number of pairs sharing graph-edge constraints is instead
\[
 \Delta=\frac12\binom nk\sum_{j=2}^{k-1}
 \binom kj\binom{n-k}{k-j}q^2 2^{\binom j2}.
\]
It excludes both j=1 and the diagonal j=k. Multiplying the predecessor's
conditional-overlap bound by mu/2 gives exponents 2t-2 and t-1,
which are strictly negative on every fixed interior phase band. The
normalization here is absolute o(1), stronger than merely an overlap
contribution of o(mu) to the count variance.

## Independent derivations of the variance normalization

Resample one Bernoulli hyperedge coordinate, independently of all the
others. Conditional on the other coordinates, the squared change in
loss is its squared add-one change times the indicator that the two
Bernoulli variables differ. The latter has probability 2q(1-q).
The Efron–Stein factor 1/2 cancels that 2. The result is
\(q(1-q)\sum_A\mathbb E\delta_A^2\), exactly the bound obtained
by the Doob/Jensen derivation in PROOF.md.

The add-one change is 1 minus the add-one matching gain. The matching
gain is either 0 or 1. If the new edge is disjoint from all old edges,
the gain is 1 and the loss change is zero. Thus an add-one loss change
requires at least one occupied neighbor. The occupied-neighbor
probability is 1-(1-q)^R, where R counts OTHER intersecting candidate
edges. Counting the edge itself would be an unnecessary overcount and
would lose the useful zero bound when there are no neighbors.

There are NR/2 candidate unordered conflicts. Hence their independent
model expectation is NRq^2/2. The union-bound version of the variance
bound is exactly twice this expectation, times 1-q. This second count
checks both the absence of an extra factor 2 and the power q^2.

The inequality \(R\le Nk^2/n\) follows in a different way by
double counting vertex incidences: the total number of incidences
\((v,B)\) with \(v\in A\cap B\) is
\(k\binom{n-1}{k-1}=Nk^2/n\). Each intersecting B accounts for
at least one incidence. This even counts A itself, so excluding it
preserves the upper bound. Dividing the resulting variance bound by
mu gives \(\mu k^2/n=n^{t-1+o(1)}\), not
\(\mu^{3/2}k^2/n\). That change of normalization is precisely why
centering extends the allowed phase range.

## Closed forms checking the exhaustive computations

If 2k>n, at most one edge can be in a packing. For the independent
model, X has distribution Bin(N,q), M=1_{X>0}, and
\[
 D=X-1+\mathbf1_{\{X=0\}}.
\]
Writing p0=(1-q)^N, direct expectation and covariance give
\[
 \mathbb ED=Nq-1+p0,\qquad
 \operatorname{Var}D=Nq(1-q)+p0(1-p0)-2Nq\,p0.
\]
Indeed Cov(X,1_{X=0})=-Nq p0. The script checks both closed forms
against exact enumeration for (n,k)=(5,3),(5,4),(6,4), at all tested q.

For n=6,k=3, the twenty triples form ten complementary pairs. A
matching has size two exactly when at least one complementary pair is
fully present. These ten pair-occupancy events are independent.
Consequently
\[
 \mathbb ED=20q-2+(1-q^2)^{10}+(1-q)^{20}.
\]
The script checks this expression and checks each family's matching
size directly by the complementary-pair criterion, independently of its
family-subset recurrence. For n<=5 it also uses a vertex-subset dynamic
program, which enumerates different choices from the family recurrence.

## Distributional transfer and limits of the conclusion

The event \(|D-c_n|>\varepsilon\sqrt\mu\) depends only on the
labelled k-set family. Total variation controls its probability even
though the event and the centering depend on n. Chebyshev in the
independent model then supplies (16). No equality of expectations
between the two models is used.

Once this event has vanishing probability in the ORIGINAL graph, the
error may be inserted alongside any other original-graph statistic.
In particular the joint count theorem from round 4 is sufficient for
the joint packing limit. It would be incorrect to infer that the two
full adjacent-size families are close to independent hypergraphs from
the present comparison; no such assertion is needed or made.

A bounded-probability discrepancy can still carry a substantial first
moment. Therefore the correction c_n is retained as the independent
model expectation. Neither centering at the actual expectation nor
variance convergence for M follows from this proof. An explicit
additive approximation to c_n at scale o(sqrt(mu)) is also not supplied.
The upper bound on c_n alone cannot replace it by zero above phase 2/3.

At t approaching 1, the uniform o(1) bounds used here need not persist;
at t approaching 0, the growing-mean input for the inherited Gaussian
limit requires separate attention. Fixed bands strictly inside (0,1)
are essential to the stated theorem.

The comparison input is an existing theorem of Robert Morris and Oliver
Riordan, not a new family approximation. Its application and the packing
loss variance bound extend the preceding local report. No claim of
novelty in the literature or of a new chromatic concentration theorem
is made.
