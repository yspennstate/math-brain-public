# fleet02/B16 multiplicity-seven barrier

This is a proof-interface counterexample, not a counterexample to a multiplicity-seven density theorem and not a QFORM counterexample.

Set

eta=1/100,
a=99/1000,
N=3674,
b=6/sqrt(N),

and define the 2 by (N+1) physical cross block

C=[ [a,0,...,0],
    [0,b,...,b] ],

with N copies of b in the second row after the first column. Then

CC^T=diag(a^2,36),
det(CC^T)=36a^2=0.352836>8/25,

and the first complement column has leverage exactly one for the rank-two row space of C.

Form the symmetric bipartite block

A_cross = [ 0_2  C ; C^T  0 ]

and direct-sum five copies of J_101/101.

The singular values/eigenvalue moduli of A_cross are 6,6,a,a. Each J_101/101 contributes one eigenvalue 1. Therefore the full matrix has

s_7(A)=1,
s_8(A)=a=0.099.

It has no eta-pivot. Every physical diagonal is either zero or 1/101<0.01. Every principal 2-by-2 determinant has modulus below 0.01:
- anchor/leaf determinants are c^2, with a^2=0.009801 and b^2=36/3674<0.01;
- leaf/leaf and anchor/anchor determinants in A_cross vanish;
- within one diffuse J_101/101 block they vanish;
- between two diffuse blocks they equal 1/101^2<0.01;
- mixed cross/diffuse pairs have determinant zero.

Thus a no-pivot matrix can have seven unit spectral directions, a robust physical two-anchor cross determinant, and a single leverage-one near-coloop.

This shows the multiplicity-eight one-exception rank contradiction cannot descend to seven by bookkeeping alone. In the s_8 proof, rank R<=5 and s_8 force three large diagonal entries, which contradict restricted rank two. Under s_7 the same rank spending forces only two large diagonal entries, exactly compatible with restricted rank two. The example realizes the exceptional leverage as a genuine physical feature rather than an artifact of the proof.

Next obligation below eight: exploit additional same-seed/overlap structure in the single-high-leverage branch, or provide a product-safe analytic receiver that pays that branch. No multiplicity-seven theorem is claimed here.
