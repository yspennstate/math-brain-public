# fleet03/B02 r33 early mathematical checkpoint

Live predecessor: fleet03/B02 r32, `yspennstate/math-open-problems@3cc1145d1fb015deed33085d536db7156d918225`.

On its residual anchored-second-volume branch, reorder the literal residual block as

`N=[[b,rho^T],[gamma,M]]`, and split the original anchor vectors as `r=(u,r0)`, `c=(v,c0)` in

`B=[[a,r^T],[c,N]]`, with `a!=0`.

Write

`K=bM-gamma rho^T`,
`P=[[a,u],[v,b]]`,
`R=[[r0^T],[rho^T]]`,
`C=[c0,gamma]`,
`L=det(P)M-C adj(P)R`.

Direct expansion gives the exact identity

`aK = L + u(vM-c0 rho^T) + (b c0-v gamma) r0^T`.              (CP1)

Therefore, by the Frobenius triangle inequality, at least one of

`||L||_F^2`,
`u^2 ||vM-c0 rho^T||_F^2`,
`||b c0-v gamma||_2^2 ||r0||_2^2`

is at least `a^2 ||K||_F^2/9`.

In the r32 H2 branch, `||K||_F^2 > E2(N)/8 >= J/(32a^2)`, hence one of these three explicit physical packets is `>J/288`; on the live r30 heavy-anchor branch `J>Z/3`, one is `>Z/864`.

The first packet is exactly the double-anchor incident third-volume `G3^(x,i;y,j)(B)=||L||_F^2`. Thus the former H2 alternative is reduced to a known double-anchor packet or one of two concrete one-sided strip products. This is algebraic and uses no Schur-independence claim.

A seeded 1000-instance dense-matrix regression verified (CP1) to relative error below `1.8e-15`; the symbolic expansion above is the proof.
