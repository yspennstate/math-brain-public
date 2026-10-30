# Early checkpoint — diffuse rank-three diagonal-twist family kills single 3×bank kernel currency

Run: `20260923T050036Z-fleet02-B01-qform-r37`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: fleet02/B01 Oscillatory replacement.

Let the original coordinates be three disjoint banks U,V,W, each of size m>=3. Let u,v,w be their normalized constant vectors, and set

A_m = u u^T - 2 v v^T + w w^T + m^{-1} I.

Then A_m has eigenvalues `1+1/m, -2+1/m, 1+1/m` and `1/m` on the remaining `3m-3` directions, so it is in the exact QFORM target for every m>=3. Every physical diagonal has modulus at most `2/m`, and every physical 2x2 principal determinant has modulus at most `4/m^2`; hence this is strict N3 for every fixed no-pivot threshold once m is large.

For any three-coordinate set I and any disjoint original-coordinate bank J such that `K=A_m[I,J]` has rank two, write

`Delta=sigma_1(K)sigma_2(K)` and let z be a unit generator of `ker(K^T)`, `d=|z^T A_m[I,I] z|`.

The diagonal twist contributes nothing to K. Each row of K has squared norm at most `4/m`, hence `||K||_F^2<=12/m` and

`Delta <= ||K||_F^2/2 <= 6/m`.

Moreover `A_m[I,I]=m^{-1}I+B_0`, where the low-rank bank block B_0 has operator norm at most `6/m`. Therefore

`d <= 7/m`, and consequently

`Delta^2 d <= 252/m^3`.

Thus no strict-N3 structural theorem can force a universal positive lower bound on the fleet03/B01 rank-two cross-kernel currency `Delta^2 d` for one three-physical-coordinate packet.

The same family is nevertheless uniformly paid by the newest Fresnel–Brascamp–Lieb Theorem F: the rank-three frame `[u v w]` has row leverage `1/m<=1/2`, the remainder `m^{-1}I` is diagonal, and `|det diag(1,-2,1)|=2`. Hence for every independent cap-one input law,

`||p_{X^T A_m X}||_infty <= 12 * 2^(-1/3) < 9.525`,

uniformly in m. This is a joint averaged-frequency estimate, not the refuted scalar pointwise quadratic-phase decay.

Next: apply the completed fleet03/B01 cross-transverse L4 theorem to an explicit rank-two packet in this same family and quantify its certificate deterioration; then record the structural conclusion as an immutable report/correction if the calculation survives the final correction sweep.
