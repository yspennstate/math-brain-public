# Rank-preserving deletion pays a near-coloop exact-rank-three branch

Status: PROVED CONDITIONAL STRUCTURAL AND DENSITY THEOREM; full unrestricted QFORM OPEN.

## Theorem

Let A=U Lambda U^T be real symmetric of exact rank three, where U^T U=I_3, Lambda invertible, and s3(A)>=1. Let S be a set of original physical coordinates and J its complement. Assume
eta=||U_S||op^2<1.
Suppose an original coordinate h in J is essential for the retained row rank:
rank U_{J\{h}}=2
(and therefore rank U_J=3).
Finally assume |A_hh|<(1-eta)/64. For any independent original-coordinate random vector X with coordinate densities at most one, X^TAX has density satisfying
||p_{X^TAX}||infinity < 65/(1-eta).                        (1)
In particular, eta<=1/2 and |A_hh|<1/128 imply ||p||infinity<130.

This is an exact-rank-three theorem. It does not assume bounded supports, moments, a rank-three-crosscut lower bound, or small coefficients on the removed block.

## Spectral and Schur proof

Write B=A[J,J], C=A[J,S], D=A[S,S]. Since
G=U_J^T U_J=I_3-U_S^T U_S >=(1-eta)I_3,
B has rank three, and its nonzero eigenvalues are those of G^(1/2) Lambda G^(1/2). The smallest singular value therefore satisfies
s3(B)>=(1-eta)s3(A)>=sigma:=1-eta.                        (2)
This follows from the product lower bound for smallest singular values, valid also for indefinite Lambda.

Because rank A=rank B, the symmetric block-matrix rank formula gives C in range B and D=C^T B^+ C, where B^+ is the Moore--Penrose inverse. Direct expansion now yields the exact identity
X^T A X=(X_J+B^+ C X_S)^T B (X_J+B^+ C X_S).             (3)
For each fixed X_S=y, the shifted coordinates X_j+(B^+Cy)_j, j in J, remain independent and have densities bounded by one. The conditional bound below is uniform in y, so averaging preserves it. This is why even unbounded fragmented laws permit the deletion: no quadratic tail is dropped.

## Original-coordinate two-dimensional receiver

The condition rank U_{J\{h}}=2 says that the entire retained light block B[J\{h},J\{h}] and the hub-to-light row are carried by a two-dimensional linear space of original-coordinate vectors. Choose an orthonormal basis e,v of that light space. The two projections (L,V)=(e^T X_light,v^T X_light) have a joint density at most two by the product-projection theorem; the original physical coordinate X_h is independent of the entire light product source.

The quadratic B/ sigma acts on exactly the three variables (X_h,L,V); its 3x3 core has smallest singular value at least one by (2). Its physical hub diagonal has modulus |A_hh|/sigma<1/64. Apply the completely written four-region coarea theorem and its general-3D-core addendum at
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T191000Z-small-hub-square-coarea/REPORT.md
and
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T191000Z-small-hub-square-coarea/GENERAL_3D_CORE.md .
They give ||p_{(X_J+shift)^T(B/sigma)(X_J+shift)}||infinity<65 for each conditioned shift. Scaling the output by sigma and averaging over X_S proves (1).

The survivor outside this theorem is a rank-three crossing state whose departures from every rank-two light row flat cannot be deleted with total frame energy eta bounded away from one. A quantitative matroid or analytic receiver is still needed there, as well as an extension beyond exact rank three.