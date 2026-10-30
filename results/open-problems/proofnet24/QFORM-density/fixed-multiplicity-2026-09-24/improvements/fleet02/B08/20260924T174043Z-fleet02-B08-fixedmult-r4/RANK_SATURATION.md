# Exact-threshold rank saturation

For m>=101 let U=(1/m)11^T and K=[[0,1,1],[1,0,1],[1,1,0]]. For r>=1 take A block diagonal with r copies of K tensor U and r+1 copies of U.

Its nonzero spectrum is r copies of {2,-1,-1} plus r+1 copies of {1}, so s_(4r+1)(A)=1. All physical diagonals are <=1/m and all principal 2x2 determinants have modulus <=1/m^2, hence this is in both relevant no-pivot regimes.

Choose one seed row from macro-block 1 and the matching seed column from macro-block 2 in each K tensor U copy. Then B=m^{-1}I_r. Per seeded copy the exact interpolant has rank 1, the correction R-P has rank 2, R has rank 3, and R[L,L] has rank 1. The lower bounds are witnessed by the minors
m^{-1}[[0,1,1],[1,0,1],[1,1,1]] and
m^{-1}[[1,1],[1,0]],
whose determinants are m^{-3} and -m^{-2}.

Therefore simultaneously:
rank P=r; rank(R-P)=2r; rank R=3r; rank R[L,L]=r.
At r=2 this holds with s9=1; at r=4 with s17=1.

The chosen seed has residual norm squared
5r+1-(6r+1)/m+r/m^2,
so it is not a favorable small-residual seed. The result is a route obstruction only: symmetry, no-pivot and the exact high-spectrum count do not improve the support-derived rank bounds by themselves.
