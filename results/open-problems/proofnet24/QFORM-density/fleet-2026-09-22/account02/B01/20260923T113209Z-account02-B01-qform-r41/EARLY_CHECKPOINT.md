SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T11:32:09Z.
attacking: an exact Schur-cancellation obstruction for an overlapping indefinite physical pair and a strong rank-two diffuse bicore, then routing it before elimination through joint Fresnel/Brascamp-Lieb.

# Early checkpoint: strong original bicore can vanish after exact pair Schur elimination

Let H0=[[0,1],[1,0]]. Let U,V be m x 2 matrices with orthonormal columns and flat row leverage 2/m (two Walsh columns suffice). Fix sigma>=1, eps>0, and c=sqrt(sigma eps). On ORIGINAL coordinates P (two physical coordinates), I (m coordinates), J (m coordinates), define

A = [[eps H0, c U^T, c H0 V^T],
     [c U,      0,     sigma U V^T],
     [c V H0,   sigma V U^T, 0]].

The P-block B=eps H0 is invertible indefinite and B^{-1}=eps^{-1}H0. The original I-J bicore K=sigma U V^T has rank two with singular values sigma,sigma and singular product Delta=sigma^2. Nevertheless the exact post-P Schur cross block is

K_S = K - (cU) B^{-1} (c H0 V^T)
    = sigma U V^T - (c^2/eps) U H0^2 V^T
    = 0.

Thus a quantitatively strong rank-two ORIGINAL cross bicore need not survive an overlapping indefinite physical-pair elimination at all. Any routing theorem that feeds the pre-Schur Delta directly into a pair-plus-rank2-Schur receiver is false without an overlap control.

The obstruction is target-valid. On span(P,U,V), diagonalise H0 only for deterministic spectral computation. The two h=+/-1 mode blocks are
M_h=[[eps h,c,c h],[c,0,sigma],[c h,sigma,0]], c^2=sigma eps.
For h=+1 the characteristic polynomial factors as (lambda+sigma)(eps lambda+eps sigma-lambda^2+lambda sigma), and the h=-1 block is its sign reflection. Hence the six nonzero eigenvalues are

{-a,-sigma,-b,b,sigma,a},
a=(sigma+eps+sqrt(sigma^2+6 sigma eps+eps^2))/2 > sigma,
b=(sqrt(sigma^2+6 sigma eps+eps^2)-(sigma+eps))/2 >0.

So sigma>=1 gives at least four eigenvalues of modulus >=1.

Before Schur elimination the leaf principal block on I union J is pure rank four,
[[0,sigma U V^T],[sigma V U^T,0]],
with eigenvalues +sigma,+sigma,-sigma,-sigma. Its four-dimensional eigenframe has physical row leverage 2/m. Conditioning on P turns the P-leaf couplings into arbitrary linear terms, which the current Fresnel/Brascamp-Lieb theorem allows. For m>=4, Theorem F in its rank-r form therefore gives the actual inequality

||p_(X^T A X)||_infinity <= 8/sigma.

This is a joint averaged-frequency payment, not a scalar law-uniform pointwise Fresnel estimate.

For sigma=1 all physical diagonals are zero. Every physical 2x2 principal determinant equals -A_rs^2. The off-diagonal entries have magnitudes at most eps, sqrt(eps/m), and 2/m. Therefore for any fixed strict-N3 threshold tau>0, choosing eps^2<tau and then m so large that eps/m<tau and 4/m^2<tau puts the family in strict N3 while the density remains <=8.

Next: turn this into a source-pinned full report, apply the newest account03/B01 bounded-remainder compiler on an overlapping extension with an independent two-square packet, and record the exact structural correction: pre-Schur bicore strength does not lower-bound post-Schur bicore strength under unrestricted overlap.
