SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-24T05:11:22Z.
attacking: the partner's pair-resource-or-routing debt; test whether the three-large-eigenvalue hypothesis can force a universal scalar-star resource after optimizing over every literal physical pair and every remaining scalar coordinate.

# Early substantive checkpoint

## First unpaid implication

`QFORM-PAIRRESOURCE-OR-MIXEDFRAME-COMPILER-v1`: after fleet03/B09 r44 paid the near-Schur-null scalar/star interpolation for an invertible indefinite physical pair, determine whether the bare target forces a universal-scale quantity

`|det B| sigma_min(B) (|s|+||m||)`

for some literal physical pair `B` and some literal scalar in its Schur complement, or whether a source-coordinate aggregate/mixed-frame exit must be compiled before reciprocal pair payment.

The first alternative is false. For every Sylvester-Walsh size `m>=16`, take flat orthonormal `c,d,w in R^m` and the literal-source form

`Q_m = 2 U <c,Y> + 2 V <d,Y> + <w,Y>^2`.

Its active spectrum is exactly `{-1,-1,1,1,1}`. The same-side leaf block `ww^T` is dense.

The pinned completed mixed-hub Theorem H applies with two hubs, one leaf square, mixed rows `(w_i,c_i,d_i)`, Gram `I_3`, and leverage `3/m<=1/2`. Hence

`|phi_Q(t)| <= 8 pi^(5/2) |t|^(-5/2)`

and exact Fourier integration gives

`||p_Q||_infinity <= (5/3) 2^(6/5) = 3.8289945166...`.

Now classify every invertible physical `2x2` principal pair. Hub-hub is zero and every leaf-leaf pair has rank one. The only invertible pairs are `{U,Y_i}` and `{V,Y_i}`. For `{U,Y_i}`,

`B_i = [[0,c_i],[c_i,1/m]]`,
`|det B_i|=1/m`,
`kappa_m=sigma_min(B_i)=(sqrt(4m+1)-1)/(2m)`.

Put `alpha=d_i/c_i in {+1,-1}` and `beta=w_i/c_i in {+1,-1}`. Exact Schur completion of `{U,Y_i}` leaves on `(V,Y_{-i})`

`S_i = [[0,(d-alpha c)_{-i}^T],[(d-alpha c)_{-i},(w-beta c)_{-i}(w-beta c)_{-i}^T]]`.

Both displayed vectors vanish in coordinate `i`; `||d-alpha c||=||w-beta c||=sqrt(2)`. If the remaining scalar is `V`, then `s=0` and the whole scalar-star norm is exactly `sqrt(2)`. If the remaining scalar is a leaf `Y_j`, then

`|s| <= 4/m`,
`||m|| <= sqrt(12/m)`,

so for `m>=16`, `|s|+||m||<sqrt(2)`. Thus, after maximizing over every possible remaining literal scalar,

`max_k |det B_i| kappa_m (|s_{ik}|+||m_{ik}||)
 <= (sqrt(2)/m) kappa_m
 = sqrt(2)(sqrt(4m+1)-1)/(2m^2)
 -> 0`.

The `{V,Y_i}` pairs are identical. Hence **every** invertible physical pair and **every** scalar choice has vanishing r44 resource, even though the same matrices have a uniform density bound `3.829` from the undecoupled mixed-hub theorem. In fact the sum over the `2m` physical invertible pairs of their best scalar-star resources is at most

`2 sqrt(2) kappa_m -> 0`.

Therefore no structural lemma of the form “three large eigenvalues force one universal-scale r44 pair resource” can be true, even after optimization over all literal pairs/scalars; not even the sum of those best pair resources is bounded below. This is a source-valid obstruction to that proof branch, not a QFORM counterexample.

The sharpened debt is now the routing half of the fork: compile small physical-pair resources into a universal aggregate mixed-frame / grouped-crossing currency before any reciprocal pair determinant is paid.
