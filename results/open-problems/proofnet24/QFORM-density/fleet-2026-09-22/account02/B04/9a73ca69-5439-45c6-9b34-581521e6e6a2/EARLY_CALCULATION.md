SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T07:26:12Z.
attacking: exact low-tetrad Schur-numerator geometry before any reciprocal local minor is paid.

# Early calculation — exact zero-disjoint-tetrad classification

Let N be a real symmetric m x m matrix and define

D2_disj(N)=sum det N[R,T]^2,

where R,T range over disjoint two-element subsets. Thus D2_disj(N)=0 iff every tetrad identity

N_ik N_jl = N_il N_jk

holds for four distinct indices i,j,k,l.

Define the support graph G on [m] by ij in E(G) iff i!=j and N_ij!=0.

## Lemma
If D2_disj(N)=0, then the nonzero off-diagonal support has exactly one of the following forms:

1. a star (possibly a single edge) plus isolated vertices; or
2. a clique C of size at least three plus isolated vertices, and there exist sigma in {+1,-1} and real nonzero u_i, i in C, such that

   N_ij = sigma u_i u_j for every distinct i,j in C.

Equivalently, outside the star case the off-diagonal part is a signed rank-one factor on its unique nontrivial component; the diagonal entries remain arbitrary.

## Proof
There cannot be two nontrivial connected components. Indeed, if ab and cd are nonzero edges in two distinct components, with a,b,c,d distinct, the disjoint minor with rows {a,c} and columns {b,d} is diagonal and has determinant N_ab N_cd !=0.

Assume first that G is triangle-free. If it had two disjoint edges ab and cd, the tetrad identity for rows {a,c}, columns {b,d} forces both cross entries N_ad and N_cb to be nonzero, while the identity for rows {a,d}, columns {b,c} forces N_ac and N_db to be nonzero. Hence those four vertices span K4, contradicting triangle-freeness. Thus every two edges intersect. A family of graph edges with pairwise intersection is either a star or a triangle; since triangles are excluded, G is a star.

Now suppose G contains a triangle abc. If a vertex d outside {a,b,c} is adjacent to one triangle vertex, say N_ad!=0, then the tetrads on {a,b,c,d} give

N_ac N_bd = N_ad N_bc !=0,
N_ab N_cd = N_ad N_cb !=0,

so d is adjacent to b and c as well. If d is not adjacent to the triangle but had an edge de to another outside vertex, then the minor with rows {d,a} and columns {e,b} would have determinant N_de N_ab !=0, impossible. Hence every outside vertex is either isolated or adjacent to all three triangle vertices. Two nonisolated outside vertices d,e are adjacent because

N_de N_ab = N_db N_ae !=0.

Therefore the unique nontrivial component C is complete.

Fix distinct a,b,c in C and set

kappa = N_bc/(N_ab N_ac).

For every i,j in C\{a}, i!=j, the tetrad identities (using b,c as auxiliaries when needed) give

N_ij = kappa N_ai N_aj.

This also holds for the pairs involving b,c by the definition of kappa. Put sigma=sign(kappa), u_a=|kappa|^{-1/2}, and u_i=sigma |kappa|^{1/2} N_ai for i!=a. Then N_ai=sigma u_a u_i and N_ij=sigma u_i u_j for all distinct i,j in C. QED.

## QFORM relevance
For the fresh account03/B04 r52 Schur numerator N_H=det(B)D-C adj(B) C^T, its unpaid chamber has target-scale off-diagonal energy J_2(H) but small D2_disj(N_H). The exact boundary D2_disj(N_H)=0 is therefore not an amorphous high-rank state: it is either a physical star or a diagonal-plus-signed-rank-one clique (with isolated coordinates). The new unpaid content is quantitative stability as D2_disj/J_2(H)^2 becomes small but nonzero.

This is a coefficient-geometry statement only. It does not delete a nonzero random quadratic tail, assume moments, or rotate the independent variables.
