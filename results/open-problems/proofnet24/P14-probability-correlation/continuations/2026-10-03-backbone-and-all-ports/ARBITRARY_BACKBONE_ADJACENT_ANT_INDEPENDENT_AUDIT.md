# Independent audit: adjacent twin path on an arbitrary three-port backbone

2 October 2026. Auditor: `/root/antivoter_audit`.

**PASS within the exact written scope.** I freshly read the entire
`forest_adjacent_twin_path_arbitrary_backbone_proof.md`, its actual
uncontracted-graph exact verifier and saved report. I independently
rederived the arbitrary-backbone transfer, both scalar bounds, every
marked-edge coefficient, strictness and conditioning closure. I also
created a separate literal-graph checker without author imports.

The result concerns the two added adjacent edges between three new
vertices having proportional spoke profiles to at most three common
ports of any finite weighted backbone. It is not the unrestricted forest
correlation conjecture, full negative association, or a theorem about
arbitrary marked positions in a graph. Historical novelty and external
specialist acceptance remain unverified.

## 1. Why five port states suffice for an arbitrary backbone

Every backbone edge subset appearing in a full forest is itself a
forest. Its effect on future new-terminal cycle tests is exactly the
connectivity partition of the three ports. A future spoke can create a
cycle precisely when its endpoints are already connected. The number,
shape and weights of paths inside a port component play no further role.
Therefore the vector of the five possible port-partition forest sums is
a sufficient state. Summing all backbone subsets gives a nonnegative row
v with (F=v1>0\).

For a new row x, zero spokes contributes one, and one spoke contributes
(Bx\) without changing port connectivity. Two spokes are allowed exactly
when their ports are in different blocks; their weight is
(x^2b_ib_j\), and they join those blocks. Three spokes are allowed exactly
when every port is separated; their weight is (x^3J_0\). This proves
\(T(x)=(1+Bx)I+x^2P+x^3Q\) directly, independent of any special
backbone representation.

For three separate ports, the six ordered pairs of successful P joins
have total weight

\[
2(b_1+b_2+b_3)b_1b_2b_3=2BJ_0.
\]

For two port blocks, a successful first join leaves one block, so a
second join vanishes. For one block the first join already vanishes.
Thus (P^2=2BQ\), while (PQ=QP=Q^2=0\). These operator identities hold
on every one of the five states. In particular
\(M=vP1\) and \(J=vQ1=D_{\rm sep}J_0\); the latter is not generally
(FJ_0\). The new proof retains this important distinction.

## 2. Exact four coefficients and scalar constraints

Multiplying the commuting nilpotent transfers gives formula (2),
including the pair coefficient (2BJ\). Contraction of either added
marked edge sums its two terminal rows. For a fixed original backbone
forest, two resulting parallel spokes cannot both be selected, and the
sum of their individual weights is exactly the merged spoke activity.
Thus the standard contraction formula applies without a rooted-forest
normalization or extra multiplicity. Both marked edges form a path, so
simultaneous contraction is permitted. The four marked coefficients in
(3), and their Rayleigh difference (4), are exact ordinary forest sums.

For each partition state, the P row sum is the sum of a subset of the
three products (b_ib_j\), and the separated state permits every pair.
Consequently, with (e_2=\sum_{i<j}b_ib_j\),

\[
D_{\rm sep}e_2\le M\le Fe_2\le FB^2/3.
\]

The final inequality is equivalent to
\(\sum_i b_i^2\ge\sum_{i<j}b_ib_j\), whose difference is half the
sum of squared column differences. Also

\[
Be_2=3J_0+\sum_{i\ne j}b_i^2b_j\ge9J_0
\]

by AMGM, with zero columns allowed by continuity or direct nonnegative
evaluation. It follows that (BM\ge9J\). If (B>0\),

\[
B^2F-2M\ge B^2F/3>0.
\]

These constraints hold for **every nonnegative five-partition row**, not
only rows produced by a special graph class. No backbone log-concavity
or correlation theorem is required.

## 3. Analytic Rayleigh proof and strictness

For (B>0\), set (x=Ba,y=Bb,z=Bc\),
\(u=2M/(B^2F)\), and \(v=9J/(BM)\) when (M>0\).
Then (0\le u\le2/3\) and (0\le v\le1\). The normalized transfer
coefficients are (u/2\) and (uv/18\). If (M=0\), then (J=0\), and
setting both parameters zero handles the endpoint without division by
zero.

The seven Q polynomials displayed in this new proof agree term by term
with the previously audited scalar Bernstein identity. My independent
checker `adjacent_bernstein_ant_independent_check.py` had reconstructed
every one by exact nine-grid interpolation and symmetric elimination,
not by importing author expansion code. That identity therefore gives

\[
R=F^2xz\sum_{i,j=0}^2\beta_i(u)\beta_j(v)Q_{ij}(x+z,xz,y)\ge0.
\]

Summing its i=0 row gives the explicit bound

\[
R\ge F^2xz(1-u)^2(1+x+z+xz)
\ge\frac{F^2xz}{9}(1+x)(1+z).
\]

This is strictly positive for (a,c>0\) and (B>0\), independently of
the middle row and of whether any ports are already connected. In the
(M=J=0\) case the exact scalar identity reduces to
(R=F^2xz(1+x)(1+z)\), so strictness persists.

If (B=0\), all spokes vanish and the added path is a separate tree whose
edge indicators are independent. A zero outer row makes its new outer
vertex a leaf, so its sole marked edge is an independent bridge.
These equality cases are correct and cover all stated degeneracies.
Positive marked activities cancel from the Rayleigh numerator's sign
and leave its strictly positive covariance-denominator factors.

## 4. Conditioning and fields

Conditioning backbone indicators simply restricts the sum defining v to
allowed backbone forests. Positive conditional probability makes that
restricted total positive. The proof still works even if separated-port
weight is zero, including required present edges connecting all ports.
There is no need to contract ports and assume they remain three distinct
vertices. Keeping the original port labels with their connectivity
partition is the clean direct representation.

Arbitrary positive fields on backbone edges change only the nonnegative
weights in v; fields on the marked edges change only their permitted
activities. Individual spoke fields would generally destroy proportional
profiles and are properly excluded. Extra edges incident to the new
vertices are also excluded; they would invalidate this transfer model.
The conditioning closure in the written statement is therefore justified
without an unstated rank-one requirement on the backbone itself.

## 5. Actual author checker and independent literal-graph checks

I inspected the full
`forest_adjacent_twin_path_arbitrary_backbone_exact.py` and its complete
saved results. It enumerates actual uncontracted unmarked graphs by
union-find, then tests each added edge by connectivity. Both added path
edges are permissible exactly when the three new vertices are initially
in different components; otherwise their two contractions would create
a cycle. This condition in the checker is necessary and sufficient.
It independently enumerates the backbone partition row and compares the
four coefficients under every positive-probability partial backbone
conditioning. The saved counts (1,968, 224, 26 and 26 conditionings) and
the strict/equality branches are consistent with its loops. No imported
scalar formula is used in its original-graph enumeration.

My separate
`arbitrary_backbone_adjacent_ant_independent_check.py` imports no author
module. It enumerates the literal graph INCLUDING each marked edge
selection, so it checks all four coefficients through direct cycle tests
instead of using the author's connectivity shortcut. It separately
computes the five port weights and compares the scalar formula. Its
backbone is a complete four-vertex graph with six nonuniform activities,
including a non-port vertex; all rows and columns below retain their
specified exact rational values.

| Independent case | Four exact coefficients agree | Rayleigh difference |
|---|---|---:|
| Rational rows ((1/2,2/3,3/5)\), columns ((2,3,5)\) | Yes | (7069120468791/125\) |
| Zero middle row and a zero column, required edges connect all ports | Yes | (582120000\) |
| Positive rows/columns, required edges connect all ports, another edge absent | Yes | (186674544\) |
| Zero outer row | Yes | (0\) |
| All columns zero | Yes | (0\) |

The all-connected-port cases independently exercise (D_{\rm sep}=0\)
and (M=J=0\). Complete coefficients, forest counts and parameters are
saved in `arbitrary_backbone_adjacent_ant_independent_checks.json`.
These exact checks support the analytic proof; the argument for arbitrary
backbone size is the nonnegative-partition-row reduction, not an
extrapolation of finite examples.

## Verdict and boundary

All reductions and inequalities close, including arbitrary nonnegative
backbone activities, arbitrary backbone size, zero columns/rows and the
stated conditioning and fields. The theorem is a strict pairwise
correlation result for this proportional-neighborhood added path with
at most three common ports. It does not imply negative association of
all indicators, permit nonproportional spoke profiles, or resolve the
full arbitrary-graph forest conjecture. No mathematical gap was found
within that scope.
