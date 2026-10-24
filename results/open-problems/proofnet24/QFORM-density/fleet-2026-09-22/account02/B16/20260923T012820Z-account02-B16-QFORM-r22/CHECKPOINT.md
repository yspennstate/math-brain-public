# B16 r22 substantive checkpoint

Status: supporting calculation; full QFORM remains open.

Let `X_L` be an original-coordinate product source with cap-one independent densities, and let `Z=C^T X_L in R^2`, where `C` has rank two. The source-valid two-dimensional projection theorem gives

`||p_Z||_infinity <= 2 / sqrt(det(C^T C))`.

Let `H` be any random object independent of `X_L`, and suppose

`Q = h(H) + ell(H)^T Z + Z^T B Z`,

where `B` is a fixed definite symmetric `2 x 2` matrix. Conditional on `H`, complete the square only in the two projected VALUE variables. Translation preserves the joint-density cap. After the linear change by `|B|^{1/2}`, the planar density cap is at most

`2 / sqrt(det(C^T C) det|B|)`.

For any planar density `rho<=M`, the pushforward by `w -> |w|^2` has interval probabilities at most `pi M h`, because an annulus `{s<|w|^2<s+h}` has area at most `pi h`. Therefore

`||p_Q||_infinity <= 2 pi / sqrt(det(C^T C) det|B|)`.

This uses no independence between the two projected coordinates. It identifies a sign-sharp safe interface: the cap-only abstraction is valid for a definite two-dimensional curved receiver, whereas account03/B16 r20 proves it is false for an indefinite/hyperbolic receiver at a nonzero scalar pivot.

Target-class near-null test: for even `m`, balanced `eps_j`,

`Y=m^(-1/2) sum X_j`, `Z=m^(-1/2) sum eps_j X_j`,

and for `-1<delta` put `c_delta=sqrt(2(1+delta))` and

`Q_delta = delta X_0^2 + 2 c_delta X_0 Y + Y^2 + Z^2`.

The spectral matrix on `(X_0,Y,Z)` is `[[delta,c_delta,0],[c_delta,1,0],[0,0,1]]`, with spectrum `{delta+2,-1,1}`. Thus it is in the three-large-eigenvalue target class for every `delta>-1`. The two leaf projections are generally dependent, but their joint density is capped by `2`; the theorem above gives the uniform full-output bound

`||p_{Q_delta}||_infinity <= 2 pi`,

including every nonzero `delta` arbitrarily close to zero. This is the new branch to prove fully in REPORT.md.
