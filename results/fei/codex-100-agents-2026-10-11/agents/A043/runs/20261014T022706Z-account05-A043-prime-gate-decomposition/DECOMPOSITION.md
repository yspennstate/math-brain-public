# Exact two-term DNF decomposition and its irreducible roots

Consider any Boolean sign equal to+1 precisely on the union of two conjunction events. Delete internally inconsistent terms, remove irrelevant coordinates, and treat a term with no literals as constant true. Repetition of a literal within a term can be deleted. No assertion about arbitrary many-term DNFs is made.

Let J be the common literal coordinates where the two terms agree, R their shared coordinates where they disagree, and U,V the coordinates private to the first and second term. These four sets are disjoint. Reflect inputs on R so the first term requires all1 and the second all0. Let c,a,b be the conjunction signs on J,U,V; an empty group means constant+1. The original positive event is exactly

    {c=+1} AND [(all R=1 AND a=+1) OR (all R=0 AND b=+1)].

This is a genuine disjoint composition: each group occupies its own physical support, and the conflicting coordinates are separate literal wires. Contract constant groups before asserting an essential outer gate.

- If r=|R|=0, the bracket is OR(a,b); both branch conjunctions, that OR and the common-factor AND are disjoint read-once compositions of binary corner gates. Corrected constant Cstar=2+4/ln2 applies at all induced biases.
- If r=1, the bracket is the three-wire mux selecting a or b by the single conflicting bit. Its all-product-bias corrected constant is Cstar, and disjoint composition with common/branch conjunctions preserves that constant. Constant branches are contracted. This consumes A044's source-complete sharp mux theorem; no equal-data-mean assumption is introduced.
- If r>=2, the bracket is an antipodal-corner gate: output+1 exactly when every R bit is1 and the first guard is+1, or every R bit is0 and the second guard is+1. There are zero, one or two actual guard wires after empty private groups are contracted. Each core is a union of two conjunction events disagreeing on r physical literals, so PROOF.md gives constant K=4+12/ln2. Branch/common conjunctions have constant Cstar<=K, and genuine composition preserves K. One-guard cores are the Fk family; the zero-guard core is all-equal on r reflected data bits.

Thus every two-term DNF sign, under every product law, satisfies Hplus<=K(I-Var), uniformly in physical arity. On uniform inputs the same K gives H<=K I. This is a proved upper bound; sharpness of K is not asserted. The r<=1 subfamily has the sharper Cstar bound. Existing disjoint identities are applied only after the four physical groups have actually been separated.

## Exact prime class for the remaining cores

For r>=2 and g in {0,1,2} free guards, define T_{r,g} as above. With g=0 both corner guards are fixed true; with g=1 the first corner is unguarded and the second has a free guard; with g=2 both corners have distinct free guards. All coordinates are essential. Each proper block of size>=2 has at least three distinct cofactor rows:

If the block contains only conflicting data bits, take its all-one, all-zero and mixed assignments. The first two rows are the corresponding complementary-corner indicators with their guards, and the mixed row is constant negative. If no complementary data remain, the first two rows are the two guard functions (one may be constant positive). They remain distinct unless both guards are absent; in that latter case the block would be the entire support and would not be proper.

If the block contains one guard and at least one data bit, use the data assignment matching that guard with guard1, the same assignment with guard0, and the opposite data assignment. These give the matching complementary-corner indicator, constant negative and the other corner indicator. They are distinct: if no data remain the first row is constant positive and the other row is the other free guard. If the block contains both guards and no data, assignments (0,0),(1,0),(0,1) give constant negative and the two opposite-corner indicators on the complementary data. If it contains both guards and some data, properness leaves a data bit outside, and all-one/all-zero block data with the corresponding guard1, and both guards0, again give the two opposite-corner indicators and constant negative. A block containing only one guard has size1 and is outside the criterion.

Therefore every T_{r,g} is a genuine essential prime, including the binary zero-guard case r=2. They are exactly the nonbinary root forms left by this explicit two-term factorization, up to input reflections, permutation and output sign convention. This does not claim uniqueness of prime decompositions or that every prime Boolean function belongs to the class.

More precisely, apart from binary primes, an essential prime represented by two conjunction terms must be a ternary mux or one of the T_{r,g}. Any nontrivial common factor or private conjunction on at least two essential coordinates supplies a proper disjoint block and prevents primality; constant branches and irrelevant groups are deleted first. The r=0 root is binary OR, and the r=1 root is mux. The exact labeled census from all ordered pairs of consistent terms gives10,52,168 primes at n=2,3,4. Adding output negation gives10,80,336. At n4 the168 are8 zero-guard T_{4,0},64 one-guard T_{3,1}, and96 two-guard T_{2,2} instances. No uniqueness of their possible decompositions is needed.

These cores can be arbitrarily large and can degenerate to composite slices. Their payment uses derivative separation, not irreducibility alone. The next missing interface is a paid coherent derivative intersection when three or more conjunction events or arbitrary Boolean cofactor profiles replace these two separated terms.
