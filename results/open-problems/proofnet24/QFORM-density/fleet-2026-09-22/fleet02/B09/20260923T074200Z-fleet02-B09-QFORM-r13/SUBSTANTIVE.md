# fleet02/B09 substantive checkpoint — arbitrary leaf curvature via disjoint pivots

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

First unpaid implication attacked: `QFORM-STAR-LOW-DISJOINT5-STABILITY-OR-ALIGNED-MIXEDFRAME-v1`.

## Exact algebraic completion lemma
Let B be any real symmetric matrix on an original-coordinate leaf bank T. Define its disjoint rank

k = max{|S| : S,R subset T, S cap R=empty, |S|=|R|, det B[S,R] != 0}.

Choose disjoint S,R attaining k and put L=T\(S union R), P=B[S,R]. Maximality gives, for distinct i,j in L,

0 = det [[P, B[S,j]],[B[i,R],B[i,j]]]
  = det(P) ( B[i,j] - B[i,R] P^{-1} B[S,j] ).

Therefore with

C = B[L,R] P^{-1} B[S,L],

all off-diagonal entries of C equal those of B[L,L]. Since B[L,L] is symmetric, C is symmetric, rank(C)<=k, and

B[L,L] = D + C

for a diagonal D. In particular, if every disjoint 5x5 minor of B vanishes, then k<=4; after conditioning at most 8 original leaf coordinates, the remaining exact within-bank curvature is diagonal plus symmetric rank <=4.

## Quantitative disjoint-five-volume exit
Define

Omega_5(B)=sum_{S cap R=empty, |S|=|R|=5} det(B[S,R])^2.

For a uniformly random original-coordinate bipartition T=I disjoint-union J,

E e_5(B[I,J]^T B[I,J]) = 2^{-10} Omega_5(B).

Hence some deterministic source-coordinate partition has Z_5 >=2^{-10}Omega_5. Applying the completed D_5 theorem from math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837 yields, for the FULL quadratic form with arbitrary hub self-term, star couplings, dense A_II/A_JJ blocks, outside couplings, and affine terms,

||p_Q||_infinity <= 10 sqrt(2e) Omega_5(B)^(-1/10),

and P{Q in interval L} <= same_constant * |L|.

This is a direct linear small-ball estimate; the Fourier decoupling in D_5 does not create a square-root loss in interval length.

## Analytic continuation on the exact low-disjoint-rank branch
After the completion lemma, write C=sum_{a=1}^r lambda_a v_a v_a^T, 1<=r<=4, and let c=A[L,h] be the literal source-coordinate hub star. Put W=[v_1,...,v_r,c], G=W^T W, d=r+1, whiten U=W G^{-1/2}, and let rho be the determinant-weighted probability that two iid Pluecker bases of U are disjoint. Combining the completed mixed-hub Fresnel reduction at e5f71d79... with `QFORM-PLUCKER-ENTROPY-BL-v1` (math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a) gives the new one-hub bound

||p_Q||_infinity <= ((r+2)/r) exp((r+1)/(r+2))
  [rho det(G) prod_a |lambda_a|]^(-1/(r+2)).

All conditioned pivot coordinates only generate affine terms; all outside blocks are retained. If v_a are orthonormal eigenvectors of C, the resource is

det(G) prod |lambda_a| = |pdet(C)| dist(c,range(C))^2.

Remaining gap: positive-but-tiny Omega_5 cannot be discarded as a small random quadratic error, and the exact Omega_5=0 branch can still have r=0 or a degenerate/aligned mixed frame. Those are now the explicit survivors.
