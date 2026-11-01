# Early calculation — principal-minimal near-threshold transfer model

Take disjoint original-coordinate banks `U+`, `U-`, `V`, each of size `m>=2`, and one original hub coordinate `h`. Let `u+`,`u-`,`v` be the flat unit vectors on the three leaf banks and let `e_h` be the hub basis vector. For `0<delta<=1/2` define

`A = u+u+^T - u-u-^T +(1-delta)vv^T + sqrt(delta)(e_h v^T+v e_h^T)`.

In the orthonormal basis `(u+,u-,v,e_h)` the only nonzero block is

`diag(1,-1) direct_sum [[1-delta,sqrt(delta)],[sqrt(delta),0]]`.

The final 2-by-2 characteristic polynomial is

`lambda^2-(1-delta)lambda-delta=(lambda-1)(lambda+delta)`,

so

`spec_nonzero(A)={1,1,-1,-delta}`.

Thus `N_A(1)=3` exactly. For the physical partition `H={h}`, `L=U+ union U- union V`, the untouched base

`D=A[L,L]`

has nonzero spectrum `{1,-1,1-delta}`, hence `N_D(1)=2` and `s_3(D)=1-delta`. The carrier is exact rank two, with

`||A[H,L]||_op=sqrt(delta)`, `||K||_op=sqrt(delta)`, `E=0`.

Therefore the base threshold deficit and the carrier scale satisfy the exact relation

`1-s_3(D)=delta=||A[H,L]||_op^2`.

This already rules out any deduction, from the r39/r43 carrier hypotheses alone, of either a universal positive base spectral gap `1-s_3(D)>=c` or a universal positive collar `||A[H,L]||>=c`.

The family is also principal-minimal. Deleting `h` leaves only target modes `+1,-1`. Deleting one `U+` coordinate changes the `+1` leaf eigenvalue to `1-1/m`; deleting one `U-` coordinate changes the `-1` leaf eigenvalue to `-(1-1/m)`. Deleting one `V` coordinate replaces the `(v,h)` block by

`[[a(1-delta),sqrt(a delta)],[sqrt(a delta),0]]`, `a=1-1/m`.

At `lambda=1` its characteristic polynomial equals `1-a=1/m>0`, while at `lambda=0` it is `-a delta<0`, so its positive root is `<1`. At `lambda=-1` the polynomial is `1+a(1-2delta)>0`, so its negative root lies in `(-1,0)`. Hence every one-coordinate deletion has at most two eigenvalues of modulus at least one; by interlacing, so does every proper physical principal submatrix.

Local physical pivots may simultaneously vanish: every diagonal has magnitude at most `1/m`, every physical 2-by-2 principal determinant has magnitude at most `max(1/m^2,delta/m)`, and every physical 3-by-3 principal determinant has magnitude at most `max((1-delta)/m^3,delta/m^2)`.

Finally this is not a bad-law construction. Apply the completed source-pinned Fresnel--Brascamp--Lieb Theorem F with source bank `I=L`, coefficients `(1,-1,1-delta)`, source vectors `(u+,u-,v)`, and residual `B=sqrt(delta)(e_h v^T+v e_h^T)`. On `I`, `B_II=0` is diagonal; the source Gram is `G_I=I_3`; every normalized row leverage is exactly `1/m<=1/2`. Hence

`||p_Q||_infinity <= 12(1-delta)^(-1/3) <= 12*2^(1/3) < 15.12`.

So the near-threshold/vanishing-collar geometry is uniformly paid in this diffuse exact model. The next analytic gap must distinguish genuinely non-diagonal/overlapping base residual structure from this three-Fresnel packet; it cannot be solved by demanding a fixed threshold gap or fixed carrier norm.
