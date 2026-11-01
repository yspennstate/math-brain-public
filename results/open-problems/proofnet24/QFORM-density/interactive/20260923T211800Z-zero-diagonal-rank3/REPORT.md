# A zero physical diagonal gives a three-input rank-three receiver

Status: proved scoped corollary of the conditioned planar-bank RW2 theorem. This applies to any physical principal three-input block and arbitrary couplings to the remaining originals. It does not prove the unrestricted QFORM/RMT density theorem.

## Theorem

Let X_1,X_2,X_3 be independent real random variables, each with density bounded by one. Let A be a symmetric 3 by 3 matrix with at least one zero diagonal entry and s_3(A)≥sigma>0. For every b in R^3,

Q=X^T A X+b·X

has a density bounded by

||p_Q||_infinity ≤ (1/2+4sqrt(2))/sigma < 6.157/sigma.

If A is a physical principal three-input submatrix of a larger quadratic form in independent density-cap-one originals, the same bound holds for the full form, even with arbitrary couplings from this triple to all remaining originals. Condition the complement: its couplings become arbitrary affine coefficients on the triple and its own quadratic value becomes a target shift.

## Proof

Relabel so A_11=0. Write w=(A_12,A_13) and D=A_{2:3,2:3}. Since s_3(A)>0, w is nonzero. Set t=||w|| and let e=w/t and f be a perpendicular unit vector in the light plane. The orthogonal coordinate change

L=e·(X_2,X_3),  V=f·(X_2,X_3)

produces a joint (L,V) density bounded by one: it is merely a rotation of the product density f_{X_2}f_{X_3}. It is independent of H=X_1. In coordinates (H,L,V), the quadratic matrix is

[[0,t,0],
 [t,beta,epsilon],
 [0,epsilon,lambda]],

where lambda=f^T D f.

Two rank-two approximations give t≥sigma and |lambda|≥sigma. First, deleting the hub-to-light entries changes the matrix by operator norm t and leaves a zero hub row, hence rank at most two. Second, changing only lambda to zero changes the matrix by operator norm |lambda| and makes the determinant zero, again leaving rank at most two. The Eckart–Young singular-value inequality therefore gives s_3(A)≤min(t,|lambda|).

Multiply Q by sign(lambda)/sigma. Let H'=H, define L'=(sign(lambda)t/sigma)L and V'=sqrt(|lambda|/sigma)V. Then the normalized quadratic has the form

2H'L'+beta' L'^2+V'^2+2epsilon' L'V'

plus an arbitrary affine form. The pair (L',V') has joint density bounded by

M=sigma^(3/2)/(t sqrt(|lambda|))≤1.

The arbitrary-affine version of the conditioned planar-bank RW2 theorem applies with bank B={2,3} and P'=V'. It gives

||p_{sign(lambda)Q/sigma}||_infinity ≤ 1/2+4sqrt(2)M
 ≤ 1/2+4sqrt(2).

Scaling back proves the bound. The same reasoning works after conditioning all original inputs outside the physical triple.

## Source theorem and boundary

The planar-bank theorem used above is proved at
https://github.com/yspennstate/math-open-problems/blob/d9a9e74e807d3c4687802a347de2006e130b3938/proofnet24/QFORM-density/interactive/20260923T205000Z-conditioned-planar-bank-rw2/REPORT.md

This receiver needs a physical three-input principal block with both a zero diagonal and its own third singular value at least sigma. A global condition s_3(A_full)≥sigma does not force one specified principal triple to have this property. Matrices with all physical diagonal entries nonzero remain outside this argument unless another receiver applies.
