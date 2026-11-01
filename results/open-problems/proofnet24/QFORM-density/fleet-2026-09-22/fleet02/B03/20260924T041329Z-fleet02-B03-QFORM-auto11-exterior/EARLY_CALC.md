# Early calculation — disjoint exterior mass

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains open.

For a real symmetric matrix A define

E_r(A)=sum_{|S|=|T|=3, |S∩T|=r} det(A[S,T])^2,  r=0,1,2,3.

Cauchy–Binet and symmetry give the exact identity

sum_{r=0}^3 E_r(A)
 = sum_{|S|=3} det((A^2)[S,S])
 = e_3(A^2)
 = sum_{i<j<k} lambda_i(A)^2 lambda_j(A)^2 lambda_k(A)^2.

Hence the owner hypothesis of at least three eigenvalues of modulus at least one implies

sum_r E_r(A) >= 1.

For a random physical bipartition I|J obtained by assigning each coordinate independently to I or J with probability 1/2, put

Z_3(I,J)=e_3(A[I,J]^T A[I,J]).

Cauchy–Binet gives

Z_3(I,J)=sum_{S⊂I,T⊂J, |S|=|T|=3} det(A[S,T])^2.

Only disjoint S,T can appear. Each ordered disjoint pair is captured with probability 2^-6. Therefore

E_{I|J} Z_3(I,J)=E_0(A)/64,

so some literal original-coordinate cut satisfies Z_3>=E_0/64.

This is the structural exit to be combined with the completed marginal-free physical-E3 density receiver. It uses no probabilistic rotation and makes no claim of post-rotation independence.
