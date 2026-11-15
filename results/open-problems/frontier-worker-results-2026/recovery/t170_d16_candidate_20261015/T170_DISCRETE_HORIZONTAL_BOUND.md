# A finite exact horizontal boundary bound for the high-dimensional screen

Proposed auxiliary lemma,15 October2026, codex-term-362ebe34. Independent
proof review pending. No dimension16 FPP result is claimed by this note.

Let N=10000 and f(n)=sum_{j=0}^{n-1} popcount(j), f(0)=0. The accompanying
finite certificate checks every integer n in[2,N] and every split
1<=b<=floor(n/2):

 f(n-b)+f(b)+b <= f(n).

These are integer inequalities, with no sampled split or floating point.
Symmetry covers the other half of the splits and zero sides are equality.
The f table is independently specified by f(n+1)-f(n)=popcount(n).

For every dimension D and every subset of at most N vertices of the
binary hypercube Q_D, its number of induced edges is at most f(n).
Proof is induction on D. The D=0 cases n=0,1 have no edges. Split a
set along the last binary coordinate into sizes a,b. The cross edges
form a matching, so there are at most min(a,b). Induction on the two
Q_(D-1) slices and the certified split inequality prove the claim.
This induction requires the finite inequalities only at sizes<=N;
the hypercube dimension itself is unrestricted.

Every finite S subset Z^m admits an isometric unary embedding into a
finite hypercube: choose a finite coordinate box containing S, translate
each coordinate to0,...,L_j, and replace k by the length-L_j string of
k leading ones followed by zeros. Concatenate the m strings. Hamming
distance of two embedded points is their lattice L1 distance. The map
is injective and preserves exactly the nearest-neighbor edges, so
the same induced-edge bound applies to S.

Counting incident degrees in the full lattice therefore proves

 |boundary_edges(S)|=2m|S|-2|internal_edges(S)|
 >= 2mn-2f(n),             n<=10000.

This is a valid horizontal infection-rate lower bound for every finite
slab configuration, including disconnected sets. When m>=14, the
initial binary segment of n vertices embeds in {0,1}^m for all n<=10000,
and has exactly f(n) internal edges: vertex j has popcount(j) earlier
neighbors, obtained by clearing its1 bits. Thus the boundary bound is
actually attained within this cardinality range at m>=14.

The physical count-supremum comparison of audited T170-C004v1 accepts
any valid lower horizontal boundary rate. Its sign argument uses the
monotonicity of the TRUE count supremum, not numerical table monotonicity.
Consequently this discrete rate may replace the previous Loomis--Whitney
rate at every retained count<=10000 without changing the cap/drop/slab
restart argument. A complete FPP result would additionally need a new
rigorous upward-rounded full profile evaluation and two required
independent exact-content audits. Current double-precision screening is
only a measurement to decide whether that evaluation is worth doing.

The proof above is an elementary finite alternative to citing a global
hypercube edge-isoperimetric theorem. No literature priority is asserted
for this boundary inequality or for its FPP application.
