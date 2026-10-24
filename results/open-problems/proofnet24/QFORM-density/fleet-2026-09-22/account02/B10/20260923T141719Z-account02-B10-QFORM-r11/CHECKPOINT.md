# account02/B10 r11 substantive checkpoint — canonical near-null shear defect

In the exact-rank-three representation `A=UMU^T`, `U^TU=I_3`, fix the heavy physical row `u_0=sqrt(h) r`, put `a=r^TMr`, `k=Mr`, `kappa=||k||`, and assume `M` is invertible. Define

`z = M k/kappa^2 - (k^T M k) k/(2 kappa^4)`,

`N = M - k z^T - z k^T`.

Then `Nk=0`, and on `k^perp` the form `N` agrees exactly with the compression of `M`. Hence, for any orthonormal `E` spanning `k^perp`,

`pdet(N)=det(E^T M E)=a det(M)/kappa^2`.

If `M` has signature `(2,1)` or `(1,2)` and all eigenvalue magnitudes are at least one, one nonzero eigenvalue of `N` has magnitude at least one. Therefore `a=0` gives rank exactly one, whereas every `a!=0` gives rank exactly two. This is the deterministic rank jump behind the exact-null / punctured near-null transition.

For the physical leaves `U_L`, let `g=sqrt(h) U_L k` and `ell=h^(-1/2)U_L z`. Then the entire leaf block has the exact decomposition

`A_LL = g ell^T + ell g^T + U_L N U_L^T`.

At `a=0` this is precisely the one-rank residual geometry paid by the current account03/B10 mixed-Fresnel theorem. For `a!=0` the sole new deterministic defect is the second eigenvalue of `N`.

Next calculation in this run: show on an exact target family that the natural scalar-square peel on the strictly two-sheet side has a logarithmically divergent one-sided half-Riesz majorant as `a -> 0`, although the true output density is uniformly bounded by the completed three-dimensional source theorem. This will rule out that interpolation interface without challenging QFORM itself.
