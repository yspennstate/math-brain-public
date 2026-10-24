w348 L1 independent reproduction by w350, before reading the paired proof

Read STATEMENT_FIRST.md only for the exact operator. Let N=p+q with 1<=p<=q. Let B be the tensor subspace invariant under S_p on the first block and S_q on the second block; W is a passive Hilbert-space factor. Let P average permutations of positions 1,...,q.

For T in B and each p-subset S of {1,...,N}, define F_T(S)=U_pi T, where pi sends the first p positions onto S. This is well-defined because T has both block symmetries. Each value has norm ||T||. On functions of p-subsets define the normalized disjointness operator

(K F)(S)= [1/binom(q,p)] sum_{A subset S^c, |A|=p} F(A).

This is self-adjoint in the uniform subset measure. Let V_k be the span of e_A(S)=1_{A subset S} for |A|<=k. Then V_0 subset ... subset V_p is the whole function space. For |A|=k,

K e_A(S)= [binom(q-k,p-k)/binom(q,p)] 1_{A intersection S empty}
         = [binom(q-k,p-k)/binom(q,p)] sum_{D subset A} (-1)^|D| e_D(S).

Thus K acts on V_k/V_{k-1} as lambda_k=(-1)^k binom(q-k,p-k)/binom(q,p). Since K is self-adjoint and preserves the filtration, it acts by lambda_k on V_k orthogonal to V_{k-1}. Every nonzero eigenspace therefore has eigenvalue of magnitude at least 1/binom(q,p). No unproved inclusion-matrix rank formula is needed for this lower bound. The same holds componentwise for Hilbert-valued F.

At S_0={1,...,p}, a block permutation R sending the first q positions onto S_0^c and the last p positions onto S_0 gives

(K F_T)(S_0)=U_R P T.

Indeed averaging permutations of the first q positions chooses the image of T's first p positions uniformly among p-subsets of those q positions, and the original second-block symmetry removes dependence on the remaining assignment. Equivariance gives ||K F_T(S)||=||P T|| for every S. Hence ||F_T||=||T|| and ||K F_T||=||P T|| in uniform subset L^2, proving

||T|| <= binom(q,p) ||P T||.

Sharpness: choose independent orthonormal e_1,e_2 in H and a unit passive vector in W (if W is nonzero). Define the symmetric-block tensor by its binary-coordinate components: if the first p block has r occurrences of e_2 and the second q block has p-r occurrences of e_2, its component is (-1)^r/binom(q,p-r); all other components are zero. Its polynomial is (x_1 y_2-x_2 y_1)^p y_1^(q-p). The tensor is nonzero and has both required block symmetries. Averaging its first q positions gives the component with k occurrences of e_2 in that block as

[1/binom(q,p)] sum_r binom(k,r) binom(q-k,p-r) (-1)^r/binom(q,p-r)
= (-1)^k/[binom(q,p) binom(q,k)],

when the last p block contains p-k occurrences. For a direct proof, the summand without (-1)^r rewrites as binom(k,r) binom(q-p+r,k)/binom(q,k). Its alternating sum is (-1)^k/binom(q,k), because the kth finite difference of the degree-k polynomial binom(q-p+r,k) is 1. Therefore P T is, up to sign, a block reversal of T divided by binom(q,p). It has norm ||T||/binom(q,p), attaining the bound. Exact arithmetic independently checked 35 p,q pairs and 925 components. A zero-dimensional W is a trivial space in which no nonzero sharpness witness exists; the phrase optimal constant needs W nonzero as well as dim H>=2.

For L2, Q=second-block symmetrizer is orthogonal and commutes with the first-block symmetrizer. QT has both block symmetries, and delta=||T-QT||. Directly,

||QT|| <= C||P QT|| <= C(||P T||+delta), C=binom(q,p),
||T||^2=||QT||^2+delta^2 <= C^2(||P T||+delta)^2+delta^2.

Consequently the valid simpler bound is ||T|| <= C||P T||+(C+1)delta. This is not claimed sharp. Without the second-block assumption, for p=1,q=2 take T=(e_1 tensor e_2-e_2 tensor e_1) tensor e_1. Then T is nonzero and P T=0. Its first-block symmetry is automatic. This disproves recovery with delta=0 unless the second-block symmetry is actually assumed.

NEXT: Compare this completed derivation to w348's proof, including W nonzero and approximate symmetry constants.
