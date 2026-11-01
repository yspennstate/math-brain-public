SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T17:22:11Z.
attacking: the rank-two hub/star G_*=0 and near-zero endpoint—classify leaf curvature aligned with the hub-partner plane, then spend any transverse component through source-coordinate mixed-hub/projected-crossing smoothing before a reciprocal physical minor.

# Early substantive checkpoint — G_* zero forces aligned curvature away from coloops

Let a physical rank-two hub/star have

    A[H,I] = P C^T,     P^T P = I_2,

with C an |I| x 2 rank-two matrix and arbitrary symmetric leaf block D=A[I,I]. For each k in I, use the fleet03/B09 aggregate currency

    Gamma_k^2 = sum_{J subset I\{k}, |J|=3} det([C_J^T ; D[k,J]])^2,
    G_* = sum_k Gamma_k^2.

Put G=C^T C, Z=C G^{-1/2}, and write z_k for row k of Z. Thus Z^T Z=I_2 and ell_k=|z_k|^2 is the whitened physical hub-partner leverage. For each k let P_k be the orthogonal projection in R^{I\{k}} onto the row span of C_{I\{k}}^T and set

    e_k = D[k,I\{k}](I-P_k).

A Gram determinant identity gives the exact row formula

    Gamma_k^2 = det(C_{-k}^T C_{-k}) |e_k|^2
              = det(G) (1-ell_k) |e_k|^2.                 (E1)

Indeed C_{-k}^T C_{-k}=G-c_k c_k^T, so the matrix determinant lemma gives the second equality, while adjoining the row D[k,-k] multiplies the two-row Gram determinant by the squared distance of that row from their span.

Consequently, if max_k ell_k <= 1-delta with delta>0, then

    sum_k |e_k|^2 <= G_* /(delta det G).                   (E2)

There is also a global stitching statement. Choose row vectors a_k in R^2 such that

    D[k,j] = a_k^T z_j + e_{kj},   j != k,

and let B be the |I| x 2 matrix with rows a_k. With E_{kj}=e_{kj} off the diagonal and E_{kk}=0, symmetry of D gives

    K := B Z^T - Z B^T = E^T-E,

hence ||K||_F <= 2||E||_F. Since Z^T Z=I, writing S=B^T Z and R=(S+S^T)/2 yields

    ||B-ZR||_F
      <= ||KZ||_F + (1/2)||Z^T K Z||_F
      <= 3||E||_F.

Choose a diagonal Lambda so that T=D-Lambda-ZRZ^T has zero diagonal. Then

    ||T||_F <= ||E||_F + ||(B-ZR)Z^T||_F <= 4||E||_F,

and therefore

    boxed:  D = Lambda + Z R Z^T + T,
            R=R^T,
            ||T||_F <= 4 [G_* /(delta det G)]^{1/2}.       (E3)

In particular, under the no-coloop gate max ell_k<1,

    G_*=0  iff  D = diagonal + Z R Z^T for some symmetric 2x2 R.   (E4)

The only way the deletion gate can fail exactly is ell_k=1 for a physical coloop row; there are at most two such rows because sum ell_k=2.

This is structural, not yet a density theorem for the near-zero T term: with arbitrary unbounded input laws, small ||T||_F is NOT permission to treat X^T T X as a small random perturbation. It isolates the remaining analytic debt instead of hiding it.

A target-valid exact-zero stress family already follows. Let u,v be flat orthonormal leaf vectors, let H={a,b} be two literal physical hubs, put s=sqrt(2), C=s[u,v], and

    D = u u^T - v v^T.

On span{e_a,u,e_b,v} the coefficient matrix is the direct sum of [[0,s],[s,1]] and [[0,s],[s,-1]], hence has spectrum {2,-1,1,-2}. Thus the full QFORM spectral hypothesis holds, every whitened leaf leverage is 2/m in a flat m-bank, but G_*=0 exactly. So the bare three-large-eigenvalue hypothesis does NOT force a positive or universal-scale G_* even in a diffuse no-coloop hub/star. This is an obstruction to that structural route, not a counterexample to QFORM.

Next: quantify an actual transverse Walsh perturbation, apply the completed fleet03/B09 projected-crossing closure to its exact G_*, and apply the pinned mixed-hub Theorem H to a source-coordinate two-hub star plus dense transverse square to obtain a direct O(|L|) inequality.
