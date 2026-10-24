# Independent audit: arbitrary weighted core and four spoke terminals

Auditor: heat_entropy agent. Date: 2026-10-02.

**Verdict: PASS for the stated restricted high-fugacity theorem.** I checked
the complete analytic argument in `FOUR_TWINS_ARBITRARY_CORE_H2.md` and the
existing exact audit. I also wrote an independent exact full-graph enumeration
that does not use core contraction, the five partition shapes, or the stated
hub formulas. No algebraic or probabilistic error was found.

## Definitions and fugacity powers

The measure is the unrooted spanning-forest measure: all acyclic edge subsets
are allowed, including the empty forest and isolated vertices, and the weight
of a forest is the product of its edge activities. The graph has s+4 vertices.
Core edges and all terminal-to-core spokes are multiplied by the common
parameter lambda; the two marked matching edge activities z_e,z_f remain
arbitrary positive numbers. This convention is sufficient, since the
multi-affine Rayleigh difference is independent of the two marked activities.

The terminal symmetry is that of the graph with the marked edges deleted:
all four terminals have exactly the same weighted core neighbors. It ensures
the two single-marked coefficients agree, giving
Z=A+z_e B+z_f B+z_e z_f D and R=B^2-AD. Differentiation gives
Cov(X_e,X_f)=-z_e z_f R/Z^2; thus R>0 gives strict negative correlation.

Without marked edges, a spanning tree contributes degree s+3 to A; forcing
one marked edge contributes degree s+2 to B after its activity is removed;
forcing both contributes degree s+1 to D. Their prospective product degrees
are therefore 2s+4, 2s+3, and 2s+2, exactly the powers labeled H0,H1,H2.
If the marked activities are also specialized to lambda, the Rayleigh
difference stays the same; its covariance prefactor changes but not its sign.

## Core contraction and hub transfer

Restriction to core edges of a forest gives a core forest F. Contracting each
core tree does not lose information relevant to acyclicity. A terminal can
use at most one spoke to a given core component: two spokes from the same
terminal to that core tree create a cycle. The sum over choices of that one
spoke is lambda*c_j, c_j=sum_{v in C_j} a_v. Upon forced marked-edge
contraction or earlier hub connections, selected spokes at a new hub must
meet distinct current terminal components. If two meet one component, they
create a cycle; if all meet different components, no cycle is created.
This proves the transfer criterion in the note, including its multiplicities.

I separately derived its transition counts. For shape 211, merging the
double block with either singleton has four choices, merging the two
singletons has one choice, and joining all three blocks has two choices.
For shapes 22 and 31, joining the two blocks has respectively four and three
choices. Every diagonal has four singleton-spoke choices plus the empty
choice, hence 1+4x. From shape 1111, the two successive binary merges have
weight 30, the mixed binary/ternary paths have weight 12 for each ordered
pair of distinct hubs, and the three successive binary merges have total
weight 72+24=96. The note's exact A/P, B/P, D/P formulas follow.

The core factor lambda^(s-r) times the hub leading powers lambda^(r+3),
lambda^(r+2), lambda^(r+1) gives the common degrees s+3,s+2,s+1. This is why
the rooted core-forest average can combine all core component counts without
an additional r-dependent fugacity factor.

## Coefficient and variance algebra

The leading hub coefficients are a0=d^3/4, b0=d^2/2, d0=d. The displayed
next two coefficient formulas are consistent with the transfer expansion
t_j=lambda*c_j/4-1/16+1/(64*lambda*c_j)+O(lambda^-2), including unequal c_j.
I checked both the r=1 specialization against the exact single-hub polynomial
and the universal cancellation algebra. In particular:

* beta=(alpha+delta)/2 holds pointwise;
* b0^2=a0*d0=d^4/4;
* alpha-delta=(7-r)/(2d);
* 2*b2/b0-a2/a0-d2/d0=(-r^2+15r-50)/(16d^2).

The reciprocal-component-sum and q1,q2 terms cancel exactly in the last
identity. After averaging, the remaining combination is

    E[-r^2+15r-50] + (7-E[r])^2
      = E[r]-1-Var(r).

Thus H0=H1=0 and
H2=d^2 W^2 (E[r]-1-Var(r))/64 as claimed. This uses the square of the
averaged first-order coefficients, not the average of their squares; the
note handles that distinction correctly.

## Rooted-forest normalization and strict positivity

The weighted diagonal matrix-forest identity is
det(L_H+4z D_a)=sum_F w_F (4z)^r product_j c_j.
It follows directly by selecting one root of weight 4z*a_v in each core
tree component. In particular the note's probability nu is normalized by
W=det(L_H+4D_a)>0.

Writing K=D_a^(-1/2)L_H D_a^(-1/2), its eigenvalues mu_i are nonnegative,
because the conductance Laplacian is positive semidefinite. The ratio
det(K+4zI)/det(K+4I) factors as a product of Bernoulli generating functions
with p_i=4/(4+mu_i). At least one mu_i is zero, so at least one p_i is one;
every other p_i is strictly positive. For s>=2,

    E[r]-1-Var(r)=sum_i p_i^2-1 > 0.

This also works for disconnected or edgeless cores: their additional zero
eigenvalues only strengthen the inequality. Core connectedness is not needed.

The matrix Q=4D_a^(1/2)M^(-1)D_a^(1/2) is positive definite with eigenvalues
p_i. The unit vector u=(sqrt(a_v))/sqrt(d) satisfies Qu=u, since L_H*1=0.
Consequently ||Q-uu^T||_F^2=tr(Q^2)-1. Substitution of M^(-1)=adj(M)/W gives
the exact claimed polynomial sum of squares

    H2 = (1/64) sum_{v,w} a_v a_w (4d adj(M)_{vw}-W)^2.

Strictness also follows from rank(Q)=s while rank(uu^T)=1. For s=1 this sum
vanishes. The full graph is then a one-vertex amalgamation of two triangles;
its forest polynomial factors over those two edge blocks, giving R=0 at all
fugacities. For s>=3 the spanning K_(4,s) has vertex connectivity at least
three, so simultaneous H0,H1 vanishing is not restricted to cut vertices or
two-vertex separators.

## Independent exact computation

`four_twins_full_graph_audit_heat.py` recursively enumerates all acyclic
subsets of the full unmarked graph on s+4 vertices using rollback union-find.
At each forest it tests whether inserting e, f, or both preserves acyclicity.
It obtains A,B,C,D directly and checks B=C. It constructs the full Rayleigh
polynomial by exact Fraction convolution and independently computes the
adjugate formula via a dense rational inverse/determinant calculation.

Seven cases passed: s=1, two unequal-spoke s=2 cases with and without a
rational core edge, weighted s=3 path and triangle cores, a disconnected
s=3 core, and an s=4 path core. Rational spoke/core conductances are included.
The full coefficient lists are saved in
`four_twins_full_graph_audit_heat.json`. The H2 values, in case order, are

    0, 144, 225/256, 488592, 8706955417/73483200, 601344, 249088.

The two higher coefficients vanish exactly in every case and H2 equals the
independent matrix sum of squares. These finite checks support the audit;
the analytic matrix-forest argument proves the infinite family.

## Current primary-source comparison and novelty limit

I opened and inspected Çiçeksiz-Ravichandran,
https://arxiv.org/html/2610.00549v1 , in particular Theorem 1.5, Theorem 4.8,
Example 4.11, Example 4.13, and its conclusion. The paper proves high-fugacity
negative correlation when H0 or H1 is nonzero. Section 4.2 explicitly says
the simultaneous equality class requires investigation of H2 or the whole
Rayleigh difference. Example 4.11 has marked endpoints in four different
complete-join parts and gets H1>0; our matching edges lie within one
four-terminal part, have H1=0, and are not that example. Its K4 chains give
a different separator family with long strings of leading zeros. The present
arbitrary-core H2 formula is not stated or directly covered in that paper.

The current manuscript therefore supports presenting this as a proved
restricted continuation beyond its nonvanishing criterion, not as a solution
of the general forest conjecture. It does not establish full publication
priority. Targeted searches found no duplicate formula, but a complete
literature review remains outstanding.

For status completeness I downloaded and checked the primary PDF
https://arxiv.org/pdf/2609.26134 (Anish Gupta). Theorem 1.2 proves pairwise
negative correlation only for uniform forests of simple complete graphs
K_n. Section 1.4 explicitly leaves general finite graphs, the multigraph
form, and full negative association even on K_n open. This recent result
does not cover the present noncomplete, arbitrarily weighted graph family.

The note correctly limits its assertion to sufficiently large lambda for
this one matching pair with identical spoke profiles. Nonnegative full
Rayleigh coefficients seen in finite tests are not an all-fugacity theorem.
The general q<1 random-cluster conjecture is also not solved by this result.
