SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B04, 2026-09-23T16:47:47Z.
attacking: apply the newly published arbitrary-rank grouped projected-crossing theorem to the same regular-simplex target matrix, with every rank/volume/marginal gate checked exactly.

# Addendum after current owner/source refresh

This addendum acknowledges `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and consumes the current supporting theorem

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a:proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

The current Claude continuation at `c4c23b784395630c094ba299a50712209921d1ae` was also read. Its new `(SP)` conditional-adaptation estimate is explicitly OPEN and is not used as a premise.

## Actual physical partition on the same target matrix

Keep the matrix from `REPORT.md`:

`M=2U`, where `U^T U=I_4` and `UU^T=I_5-J_5/5`,

and

`A_*=[[J_5/100,M],[M^T,J_4/100]].`

Use the fifth left coordinate as a one-dimensional hub `H={5}`. The light coordinates are the first four left coordinates together with all four right coordinates. In the notation of the grouped-crossing theorem take

`k=1`, `ell=2`, `I={left rows 1,2,3,4}`, `J={all four right coordinates}`.

The hub-to-`J` row is

`M_J=(2/sqrt(5))(1,1,1,1)`,

so it has rank one and singular-value product

`S=||M_J||_2=4/sqrt(5)`.                                      (A.1)

The hub variable itself is one original scalar, so its one-dimensional projection-density cap is

`M_H<=1`.                                                      (A.2)

Let `Pi` be projection onto the row span of `M_J`, namely `span{(1,1,1,1)}`. The retained light crossing is

`C=M[{1,2,3,4},:] (I-Pi)`.

Using the explicit Householder frame from the report,

`M[{1,2,3,4},:]=2(I_4-cJ_4)`,

and `J_4(I-Pi)=0`, hence the projected crossing simplifies exactly to

`boxed: C=2(I_4-J_4/4).`                                      (A.3)

Thus `C` has singular values `2,2,2,0`; in particular its rank is three, so this is genuinely an arbitrary-rank crossing remainder rather than an exact-rank-two packet.

Its second-volume currency is

`Z_2=e_2(CC^T)=3*4*4=48`.                                    (A.4)

For canonical squared two-volume sampling the three nonzero squared singular values are all four. Each spectral direction has inclusion probability

`4*(4+4)/48=2/3`.

The range projection of `C` is `I_4-J_4/4`, whose diagonal is `3/4`. Therefore every physical row marginal is exactly

`boxed: alpha_i=(2/3)*(3/4)=1/2.`                             (A.5)

So the new theorem's marginal gate is met exactly, not approximately.

## Explicit grouped-crossing bound

The grouped theorem (GC) with `k=1`, `ell=2`, `d=3`, `M_H<=1`, (A.1), and (A.4) gives

`||p_Q||_infinity
 <=3*2^(7/6)*e^(1/3)*S^(-1/3)*Z_2^(-1/6)`

`=5^(1/6) 6^(5/6) e^(1/3)/2`

`=4.061525718962569... .`                                    (A.6)

All within-hub functions, all terms internal to `I` or `J`, both physical self blocks, diagonal terms and linear terms are allowed by the theorem. Hence (A.6) is a valid all-product-law estimate for the exact target-valid dense indefinite matrix `A_*` in the report.

This newly published grouped-crossing certificate is weaker numerically on this matrix than the run's new exact-q third-volume estimate

`5sqrt(15)/6=3.227486121839514...`,

but it certifies the same form through a genuinely different one-hub-plus-rank-three-projected-crossing decomposition. It also verifies the owner-requested rank, projected crossing volume, and row-marginal gates on an actual physical partition.

The unrestricted QFORM conjecture remains OPEN. The new crossing theorem still does not imply that an arbitrary three-large-eigenvalue matrix has a partition with `S` and `Z_ell` uniformly bounded below. That global structural routing remains the first unpaid implication for this slot.
