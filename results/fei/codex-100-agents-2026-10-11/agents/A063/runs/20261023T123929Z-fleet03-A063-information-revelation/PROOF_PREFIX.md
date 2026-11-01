# Extension: ordinary prefixes and arbitrary optional product resets

This extends PROOF.md: product reset after every query is NOT required here.
The root is the actual full product. At arbitrary adaptively chosen nodes one
may actually reset to the full product; elsewhere retain the actual normalized
reference. All zero-source rows use the same fair extension as PROOF.md.
The root bank is never renewed. Bits, rank, m, TC, E, O and W have the
definitions in PROOF.md. All logs are base two.

## 1. An invariant class of actual references

Let C be the current affine spectral support, with direction V=im A. The
current normalized reference Q is a convex mixture of uniform distributions
on affine subspaces D CONTAINING C. This is true at admission and at every
actual product reset (a product is uniform on its axis-aligned support).

For a rank-preserving active query, the child support is the erased C;
the source kernel is fair everywhere. Projection sends every uniform D to
a uniform affine subspace containing that child support, preserving mixture
weights. The same statement holds for a currently isolated queried vertex.

For a rank-dropping query, erased C splits into the two affine child supports
C_0,C_1 of equal size. Every projected uniform D contains their union.
Transport is deterministic on their union and fair off it. Its reference
outcome is fair separately for each mixture component, hence also for Q.
Fix one outcome b. The normalized predicted component has density 2/|D| on
C_b, zero on C_{1-b}, and 1/|D| elsewhere in D. It equals the average of
uniform measures on all affine hyperplanes of D which contain C_b and
exclude C_{1-b}. To check: such a hyperplane contains every point of C_b,
no point of C_{1-b}, and contains exactly half the points in that family
for any fixed x outside C_0 union C_1. Linear functionals on direction(D)
vanishing on direction(C_b), with value one on a separating vector, give
this family; a point outside direction(C_0 union C_1) leaves one independent
functional value free. If D equals C_0 union C_1 there is a single component.
Thus this is an actual normalized mixture, not a synthetic child reference.
The invariant follows by induction. It includes every reference-only row.

## 2. Ordinary-query loss, with both physical branches

Q is constant on C; write that density c. Its erased reference is constant
on the erased C, with density cbar. If erasure is injective on C, each
mixture component contributes c_D or 2c_D to cbar, depending on whether
its direction contains the erased coordinate vector. Hence c<=cbar<=2c.
The source KL loss is E=log2(cbar/c) in [0,1]. If erasure has two-point
source fibers (a rank drop), every component contains those fibers,
cbar=2c and E=0. Reference outcomes are always fair: O=0.
The two predicted source KL values coincide, as their support sizes and
their reference densities coincide. Thus K_child=K_parent-E separately
on BOTH physical branches, not just after averaging.

A vertex isolated at the START of an interval beginning with a product
reference has a fixed spectral bit throughout that interval, also in Q.
Other restrictions cannot make it active or change its linear coefficient.
Querying it releases E=0. A vertex that becomes isolated DURING the interval
may instead release E up to one; it must not be silently treated as free.

## 3. Interval payment and one original owner

Consider the interval between two actual resets, or between admission and
the first reset. At its start K_start=TC_start. Let t count queried vertices
that were active at interval start; let u count start-active vertices that
are now isolated but unqueried; and let d count rank drops in the interval.
Then m_end=m_start-t-u and r_end=r_start-2d. Among the t queries, the d
rank drops release E=0 and each other query releases at most one. Queries
of start-isolated vertices release zero. Therefore sum E<=t-d, and
  TC_end-K_predicted_end
    = (TC_end-TC_start)+sum E
    <= (-t-u+2d)+(t-d) = d-u <= d.
This is the actual signed reset price at the endpoint. It is a numerical
branchwise bound, valid when reset decisions depend on the physical history.
No local positive price is charged before an actual reset occurs.

Sum its positive parts over disjoint reset intervals along any path. Each
is paid by rank drops already achieved in that interval. At most W such
drops exist. If the last drop occurs, its interval ends with rank zero and
TC_end=0, so its reset price is -K_predicted_end<=0. That interval contains
at least one rank drop but contributes no positive price. If the last drop
has not occurred, one rank unit remains. Thus at EVERY reached cut,
  cumulative GROSS positive actual reset price <= W-1  (r_root>=2).
For r_root=0 all references are point masses and all costs are zero.

Consequently EVERY account conclusion in PROOF.md section 3 survives
arbitrary ordinary prefixes and arbitrary optional actual resets. In
particular the SAME original S=4 I_root funds initial A0=m-r once,
all gross reset charges, the entire H_root reservation (hence the full
terminal H), all reached-node source losses and terminal K via the exact
source chain, and an old relative debit omega<=S/4, with residual >=1
for positive rank. No earlier debit is removed and no descendant owner is
introduced. The sharp bent-star prefix of PROOF.md still costs W-1.

The sharp lower bound concerns the extra REFERENCE/OUTCOME reserve beyond
initial KL, without a separately supplied entropy or other reserve. It is
not an optimality assertion about the complete bank including full entropy.

## 4. Universal boundary

The superspace-mixture invariant uses affine spectral support and the
rank-preserving/equal-coset-splitting dichotomy. For arbitrary Boolean
functions these hypotheses fail. The first unsupported universal line is
that a similarly stable eligible reference cone and original nonlocal
owner bounded by O(I_root) exist. A selector between quadratic phases is
the next direct test: it already contains A063's earlier local-price
obstruction while being one step beyond the proved hereditary class.

See CONE_BOUNDARY.md: this direct test already FAILS for the literal
unweighted cone, by the exact actual dense-child reference. Its cone repair
is nonpositive, while the sparse child's product-admission gap is positive.
The next task is to price inherited admission and weighted cone repair from
the same original owner, not to assume the just-refuted cone invariance.
