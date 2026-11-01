# fleet02/B01 r42 early checkpoint — exterior three-volume before Schur

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains OPEN.

This checkpoint attacks the r41 unpaid routing step before any Schur elimination.

## Exterior-energy identity

For a real symmetric `A`, for `r=0,1,2,3` define

`W_r(A)=sum det(A[I,J])^2`,

over ordered triples `|I|=|J|=3` with `|I intersect J|=r`.

Cauchy--Binet applied to the principal `3 x 3` minors of `A^2` gives the exact identity

`sum_{r=0}^3 W_r(A)=e_3(A^2)=sum_{i<j<k} lambda_i(A)^2 lambda_j(A)^2 lambda_k(A)^2`.

Hence the owner hypothesis of three eigenvalues of modulus at least one implies

`W_0+W_1+W_2+W_3 >= 1`.

For a uniformly random coordinate cut `S`,

`E e_3(A[S,S^c]^T A[S,S^c]) = W_0/64`,

because a fixed ordered disjoint pair `(I,J)` of triples is oriented `I subset S, J subset S^c` with probability `2^-6`.
Thus if `W_0>=1/4`, some cut has three-volume `Z_3>=1/256`.

Apply the proved D' theorem from the required decoupling/Brascamp--Lieb source to that cut or its reverse. If one side has volume-sampling marginal maximum at most `h=2/3`, then

`||p_Q||_infinity <= 6 sqrt(e) (4/3)^(-1/2) (1/3)^(-1) (256)^(1/6)`
`                    = 9 sqrt(3e) 2^(4/3) < 64.763`.

Therefore every target matrix lies in one of the following source-valid states:

1. a universal D'-paid disjoint-volume branch (`<64.763`);
2. `W_0>=1/4` and a strong cut `Z_3>=1/256` whose row and column three-volume marginals are both `>2/3` (two-sided volume-coloop endpoint);
3. `W_0<1/4`, hence `W_1+W_2+W_3>3/4` (overlap-dominated exterior energy).

This is a genuine pre-Schur structural reduction; no post-rotation independence is used.

## r41 destructive-Schur family has hidden disjoint volume

For the r41 conditional leaf block

`L=[[0, sigma U V^T],[sigma V U^T,0]]`,

where `U,V` are `m x 2` orthonormal frames, let `ell_i=||U_i||^2`, `m_j=||V_j||^2`. Direct Laplace expansion of the nonzero disjoint `3 x 3` minors gives

`W_0(L)=2 sigma^6 sum_{i,j}(1-ell_i)(1-m_j)(U_i dot V_j)^2`.

Since `sum_{i,j}(U_i dot V_j)^2=2`,

`W_0(L)>=4 sigma^6(1-max ell_i)(1-max m_j)`.

For the flat r41 frames, `ell_i=m_j=2/m`, hence

`W_0(L)=4 sigma^6(1-2/m)^2`.

Thus the natural bank cut having rank two does not mean global three-volume is absent. For the two-Walsh-column specialization and `m` divisible by four, split each of the four sign classes `I+,I-,J+,J-` evenly across a cut. The resulting cross block is the orthogonal direct sum of four rank-one rectangles, with four singular values exactly `sigma/2`. Hence

`Z_3=sigma^6/16`, and every row three-volume marginal is exactly `3/m <=1/2` for `m>=8`.

The required Theorem D then gives the concrete all-law inequality

`||p_Q||_infinity <= 6 sqrt(e) (sigma^6/16)^(-1/6)`
`                    = 6*2^(2/3)*sqrt(e)/sigma < 15.704/sigma`.

The physical pair may still annihilate the natural post-Schur bicore exactly; the point is that an interleaved pre-Schur cut recovers volume currency before elimination. This corrects only the overly narrow interpretation of the r41 natural-cut obstruction, not the exact Schur-cancellation theorem itself.

Next: identify the overlap-dominated / two-sided-coloop survivor and test it against the newest fleet03/B01 rank-one-bilinear-plus-square receiver and Theorem H.
