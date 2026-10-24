SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-24T10:24:06Z.
attacking: QFORM-DIFFUSE-ISOTROPIC-STAR-MIXEDBASIS-CLOSURE-v1 — close the fresh account03/B05 diffuse isotropic-star stress family by an original-coordinate mixed-basis interval/Fourier receiver, then isolate the aggregate nonzero-pivot compiler still missing.

# Early substantive calculation

Fresh partner account03/B05 r44 gives the exact target family (m divisible by 4)

r_0=(1/sqrt(2),0,0),

r_j=(1/sqrt(2m), s_j/sqrt(m), t_j/sqrt(m)),  (s_j,t_j) in {+/-1}^2,

with each sign pair occurring m/4 times and spectral matrix M=diag(1,1,-1).  Thus the nonzero spectrum is {1,1,-1}, every hub-residual physical pair is singular, no definite physical principal pair exists, each anchored star is 1/m, while the total anchored determinant star is 1/2.  This is a source-valid stress family for pair/minor selection, not a QFORM counterexample.

Let A,B,C,D denote the four residual sign classes (++),(+-),(-+),(--).  Put

L=B union C,     u_j=sqrt(2/m) on B and -sqrt(2/m) on C,
R=A union D,     v_j=sqrt(2/m) on A and -sqrt(2/m) on D.

Then u and v are unit vectors on disjoint ORIGINAL coordinate banks.  If Y_k=<r_k,X> are the three spectral coordinates, direct expansion gives

Y_2-Y_3=sqrt(2) U,     Y_2+Y_3=sqrt(2) V,

where U=u.X_L and V=v.X_R.  Therefore

Y_2^2-Y_3^2=2UV.

Set

H=Y_1=X_0/sqrt(2)+(1/sqrt(2m)) sum_{j>=1} X_j.

Hence the entire quadratic form has the exact original-product mixed-basis representation

Q=H^2+2UV.

This is precisely the packet of account01/B03 `QFORM-MIXED-BASIS-TRIPLE-FRESNEL-v1` with a=sigma=1.  On the R bank the rows (h_j,v_j) have Gram matrix diag(1/4,1), so E2=1/4.  Its nonzero pair minors are exactly A-D pairs; each squared minor is 4/m^2.  The induced mixed-triple law is uniform over triples consisting of one coordinate from L, one from A and one from D.  Two iid such triples are disjoint with probability

delta_mix=(1-2/m)(1-4/m)^2.

For m>=8 this is at least 3/16, so E2 delta_mix>=3/64 and the mixed-basis theorem gives

||p_Q||_infinity <= 12 (64/3)^(1/3)=48/3^(1/3)<33.282.

This is a full-line continuous-density estimate, so it pays the convex/two-sheet side of this r44 stress family rather than merely the already-ruled side.  The edge case m=4 will be handled separately by a source-valid original-coordinate principal-block theorem.
