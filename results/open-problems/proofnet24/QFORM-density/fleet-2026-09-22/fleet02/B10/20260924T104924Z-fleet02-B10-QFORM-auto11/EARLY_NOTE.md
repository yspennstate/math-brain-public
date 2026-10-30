# fleet02/B10 early calculation — rank-one leaf compiler

Programme: QFORM-DENSITY-3EIG-20260922. Full conjecture remains open.

First unpaid implication after this calculation: **QFORM-STAR-PARALLEL-SECOND-CURVATURE-RECEIVER-v1** — control the near-null hub family when the two-dimensional leaf quadratic block has rank two, without post-rotation independence, a conditional-density supremum, or a loss as the hub Rayleigh coefficient tends to zero.

Let the original hub variable `H` be independent of the original leaf bank, and let `x,y` be orthonormal coefficient vectors on that leaf bank with `max_i(x_i^2+y_i^2)<=1/2`. Put `L=x·X`, `V=y·X`. Consider the exact three-aggregate matrix

`M=[[alpha,s,0],[s,b,k],[0,k,d]]`

and assume the leaf block `N=[[b,k],[k,d]]` has rank one. Write `N=lambda u u^T`, `u=(cos theta,sin theta)`. The leaf rank-one direction is `z=cos(theta)x+sin(theta)y`, while the physical star is `C=s x`.

For the mixed-Fresnel theorem at the required source pin, the augmented Gram is

`Gamma=Gram(C,z)=[[s^2,s cos(theta)],[s cos(theta),1]]`,

so `det Gamma=s^2 sin(theta)^2`. Its normalized row leverage is exactly `x_i^2+y_i^2`, because `[C,z]=[x,y] [[s,cos(theta)],[0,sin(theta)]]` and leverage is invariant under an invertible change of columns.

Since `det N=0`, direct expansion gives

`det M=-s^2 d=-s^2 lambda sin(theta)^2`.

Therefore the mixed-Fresnel density constant collapses to the invariant product `|lambda| det Gamma=|det M|`; if all three eigenvalues of `M` have modulus at least one, this product is at least one. The resulting all-level density bound is

`||p_Q||_infty <= 3*2^(4/3) |det M|^(-1/3) <= 3*2^(4/3) < 7.560`.

No independence of `(L,V)` is used. The full proof, the ruled-side application, and the rank-two obstruction are recorded in the final report for this run.
