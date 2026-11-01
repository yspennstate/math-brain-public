# Robust first-query influence on near tensors

Entropy is in bits, all measures uniform, and influence is physical influence.
Fix K>=0 and F=product_j h_j on disjoint nonempty coordinate blocks B_j.
There may be further disjoint factors; no intermediate affine mixing or phase
operation is allowed. Let G differ from F on event E of probability delta.
For each selected factor h_j on m_j bits assume H(h_j)>K I(h_j), and define
rho_j>0 as its normalized distance to the finite class H<=KI. Define
alpha_j=min_{i in B_j} Inf_i(h_j). If a dummy coordinate is allowed this
minimum can be0, and the influence assertion then gives no positive price.

A finite adaptive physical query tree queries no coordinate twice on a path.
A leaf is HEREDITARILY K-certified if its actual Boolean function and EVERY
further physical restriction satisfy H<=KI. Constants qualify. This condition
is sufficient for the argument; a weaker exact requirement is that at every
leaf leaving B_j completely untouched, all physical fibres retaining B_j
are K-certified. Ordinary leaf nonviolation or average optimized eligibility
does not automatically supply these fibres. All leaves retain original reaches.

## 1. A disjoint event partition pays the error once per factor

Let A_j be the input event that the tree ever queries B_j, p_j=Pr(A_j),
and e_j=Pr(E intersect A_j). Before the FIRST query into B_j, all answers
are outside B_j. Thus A_j is measurable on outside coordinates, and its
first-query cylinders are disjoint and invariant under flipping ANY bit in
B_j. No conditional independence of E and the query policy is assumed.

On a leaf where B_j is untouched, the comparison seed is exactly h_j times
the surviving outside factor. Fixing the remaining outside coordinates gives
a signed h_j fibre. Hereditary eligibility repairs every such fibre, so the
stage21 disjoint-fibre count, or its direct one-line reconstruction, gives

    delta-e_j >= rho_j (1-p_j).                         (1)

This is the original error mass on NO-TOUCH paths, not delta times their
probability. It is valid even when E determines the tree's stopping outcomes.

Let Q_j be the sum of original reach times ACTUAL queried influence of G,
over nodes at which B_j is queried for the first time. At such a node v,
the queried seed derivative is precisely a derivative of untouched h_j;
its pivotal probability is at least alpha_j, independent of outside answers.
The two pivotal indicators for F,G can differ only if E occurs at the input
or at its queried-coordinate neighbour. On the disjoint first-query cylinders
the coordinate flip preserves the cylinder. Thus BOTH endpoint error sums
equal e_j, not an independently estimated occupation moment. Therefore

    Q_j >= alpha_j p_j - 2 e_j.                        (2)

Equations(1)--(2) retain the SAME original E. Combining them gives

    Q_j >= alpha_j(1-delta/rho_j)
                    +(alpha_j/rho_j-2)e_j
        >= alpha_j-max(alpha_j/rho_j,2)delta.          (3)

Use Q_j>=0 as well when the right side is negative. No division by alpha_j
occurs; rho_j>0 is required and follows from the strictly violating core.
Because each node can be a first query for only one block, the actual total
spent influence Pi_I=sum_v reach(v) Inf_{i_v}(G_v) satisfies

    Pi_I >= sum_j Q_j
         >= sum_j max(0,alpha_j-max(alpha_j/rho_j,2)delta). (4)

Also sum_j p_j is the expected number of touched selected factors and
p_j>=max(0,1-delta/rho_j). This survives arbitrary adaptive stopping.
Every error occurrence can belong to several factors' occupations; the
factor sum in(4) is explicit. No false bound sum_j e_j<=delta is used.

The usual physical telescope Pi_I=I(G)-E I(actual leaf) follows by splitting
influence at each query, and is the conserved ORIGINAL influence debit.
This is a NECESSARY debit, not a payment upper bound for entropy. It supplies
no terminal entropy for free and does not remove phase Pi or old debits.

## 2. Exact examples, boundary, and strict hypothesis guard

For the two-bit point defect h2 at K=1, H=2,I=1 and each directional
influence is1/2. Every one-point flip is a character or constant, so rho=1/4.
Thus for t selected copies and arbitrary vertex edits of density delta,

    Pi_I >= t max(0,1/2-2delta).                       (5)

For the three-bit point defect h3 at K=2, H=4-(9/8)log2(3)>3/2,
I=3/4, alpha=1/4 and rho=1/8 by stage21 (all point flips repair).
The corresponding bound is t max(0,1/4-2delta). The coefficient2 in these
examples improves the naive separately charged bound: alpha/rho=2 makes
the touch and no-touch errors cancel EXACTLY in(3). It is not a numerical
change to the earlier repair radius.

At delta0, query one fixed bit in EACH h2 copy. Each remaining factor is
a one-bit character or constant, so every leaf and its restrictions have
entropy0. The debit is exactly t/2, proving sharpness at the unedited
boundary of(5). Repeated querying of a coordinate is unnecessary and may
be removed before applying the theorem. Zero-tree and full-tree cases are
included; t>=1, a proper fibre and strictly violating h are needed.

HEREDITARY cannot be dropped: G(x,y,z)=z h2(x,y) is ordinarily K1-certified
since H=2,I=2. The zero-query tree has debit0 and leaves h2 untouched at
delta0, but its z-fixed descendant h2 violates K1. The leaf is not hereditary.
Thus the new theorem must not be substituted into A055's weaker averaged
optimized-eligibility theorem without proving the added fibre condition.

## 3. Independent analytic review of A055 tensor/occupation Sections1--3

For each Boolean f, centered directional cost m_f(v) belongs to[0,1/2].
An output character sets the derivative sign independently on a chosen basis,
so the full affine/character minimum a(f) is its minimum centered basis sum.
For products, 1-2m_F(v)=product_j(1-2m_hj(v_j)); hence any cheap product
direction projects into cheap factor directions. At every threshold its span
rank is at most the sum of the factor cheap ranks. Greedy minimum bases have
rank-many cheap members at every threshold (ties included); integrating the
number above threshold proves a(F)>=sum a(h_j). The union of minimizing
factor bases gives the reverse inequality. This reconstructs exact additivity.

Physical leaves remain products of restricted factors. With seed deficit
d=H(h)-Ka(h)>0 on m bits, a touched factor with q queries has deficit
at least -K(m-q)/2, since centered costs are at most1/2. An untouched factor
has deficit d. Therefore every leaf obeys

    Daff(leaf)>=td-(d+Km/2)T+(K/2)Q.

Original-reach averaging with -E Daff(leaf)>=0 gives
(d+Km/2)E T>=td+(K/2)E Q; the denominator is positive. Conditioning
on a finite activation event multiplies every term by its SAME positive
reach, so the conditional occupation bound is unchanged. No phase or cross-
block coordinate mixing is covered. Sections1--3 HOLD at this analytic scope;
the old NAND32 seed certificate and giant embedding are NOT accepted here.

## First unsupported universal line

The robust lower debit obstructs cheap hereditary cleanup near violating
tensors; it does not give an upper entropy payment. The residual n>>K
critical class still lacks a selected ORIGINAL block paid from its exact
nonnegative complete-child reserve and unused quotient rank, including Pi,
mixed rows and old debits. Neither the new bound nor A055 occupation creates
such a supplier. A source with certified factors has rho0 and falls outside
the positive-radius statement. Universal FEI remains OPEN.
