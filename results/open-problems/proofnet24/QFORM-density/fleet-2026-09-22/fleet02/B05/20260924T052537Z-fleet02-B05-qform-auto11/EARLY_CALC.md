# fleet02/B05 early calculation — bank-gap orthogonality debt and a joint-law cancellation witness

Programme `QFORM-DENSITY-3EIG-20260922`; full target remains OPEN.

In the live exact Witt packet the residual coefficient vectors `u,v,w` are orthonormal.  For any cut `J sqcup K`, put `s=||v_J||^2 in (0,1)` and regress

`w_J=alpha_J v_J+r_J`, `w_K=alpha_K v_K+r_K`,
`u_J=beta_J v_J+p_J`, `u_K=beta_K v_K+p_K`,

with each residual perpendicular to the corresponding restriction of `v`.  Since `<v,w>=<v,u>=0`, the slope parts lie in the same one-dimensional bank-contrast line.  Define

`G=s(1-s)(alpha_J-alpha_K)^2`, `G_u=s(1-s)(beta_J-beta_K)^2`.

Then exactly

`G+||r_J||^2+||r_K||^2=1`,
`G_u+||p_J||^2+||p_K||^2=1`.

Orthogonality `<u,w>=0` gives

`sqrt(G G_u)=|<p_J,r_J>+<p_K,r_K>| <= sqrt((1-G_u)(1-G))`,

hence `G+G_u<=1` and therefore

`boxed: ||p_J||^2+||p_K||^2 >= G.`

Thus the fresh fleet03/B05 r40 regression-gap currency `G>=1/6` forces at least `1/6` of shared-shear residual energy.  In particular, its auxiliary hypothesis that both `w` (equivalently the completed `z=w+lambda v`) and `u` are bank-collinear with `v` is incompatible with `G>0` in the actual orthonormal Witt survivor: bank-collinearity would give both residuals zero, hence `G<=0`.  The theorem remains correct as a scoped statement, but its nonzero-gap collinear endpoint is empty inside the exact live orthonormal frame.

There is also a sharp reason not to replace the residual product projection by an arbitrary bounded joint density.  Fix `0<kappa<=1`.  Let `H,E,V,W` be independent `Unif[-1/2,1/2]` and define, for `V!=0`,

`U=E-W^2/(2 kappa V)`.

The map `(e,v,w)->(u,v,w)` has Jacobian one, so `(U,V,W)` has a probability density bounded by one (indeed every coordinate and coordinate-pair marginal is also bounded by one).  Yet for the target-spectrum Witt polynomial

`Q_kappa=2V(H+kappa U)+W^2`

one has identically

`Q_kappa=2V(H+kappa E)`.

Its matrix has nonzero spectrum `{1,+sqrt(1+kappa^2),-sqrt(1+kappa^2)}`, but the inputs `(H,U,V,W)` are not a scalar product law.  Since `H+kappa E` has a density bounded below in a neighbourhood of zero, the product density of `2V(H+kappa E)` diverges logarithmically at zero.  Therefore no proof of the live punctured Witt endpoint may use only a bounded three-dimensional joint density (or only bounded one-/two-dimensional residual marginals); the linear product-projection provenance is essential.
