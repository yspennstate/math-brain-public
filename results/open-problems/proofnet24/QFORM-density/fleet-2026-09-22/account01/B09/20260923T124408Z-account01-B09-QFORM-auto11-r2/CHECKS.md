# Deterministic checks for `QFORM-AGGREGATE-SINGLETON-VOLUME-TO-CUT-v1`

All checks here are exact arithmetic/algebra or direct evaluation of displayed constants; they are not independent proof review.

## Constants

For `h=2/3`, `q=4/3`,

`C_h = [3e/((3-4h)sqrt(2h))] 16^(1/6)
     = (9 sqrt(3) e / 2) 2^(2/3)
     = 33.632123321676595`.

Combining `S >= (1/2)(1-q_C) Delta^2 E_curv^2` contributes `2^(1/6)`, giving

`33.632123321676595 * 2^(1/6) = 37.75078203264255`.

The full-target stress-family fixed cut has `Z=1/4`, so

`3e Z^(-1/6)=3e 2^(1/3)=10.274461485666828`.

The designated-partner application has

`rho=(15/16)(47/64)=705/1024=0.6884765625`,

and

`3e rho^(-1/3)=9.235335630126482`.

## Random-cut identity

Each singleton term is indexed by four distinct leaves: one promoted leaf `k` and a row triple `T` with `|T|=3`, `k notin T`. Under independent fair coloring, compatibility with a fixed cut requires `k in K` and `T subset I`, probability exactly

`(1/2)^4=1/16`.

Linearity of expectation therefore gives `E Z=S/16` without independence assumptions among determinant weights.

## Row-participation count

Every singleton determinant term contains exactly three row leaves. If `R_i` denotes its total squared weight over terms containing row `i`, then

`sum_i R_i=3S`.

At `h=2/3`, gate failure after selecting a cut with `Z>=S/16` gives one row with

`R_i >= alpha_i Z > (2/3)(S/16)=S/24`.

Hence fewer than `72` rows can satisfy `R_i>S/24`, since otherwise their total would exceed `3S`.

## Stress-family singular values

For even `m`, split the third leaf group into equal halves `I_3,K_3`. The cross matrix from

`I=G_1 union G_2 union I_3`

to

`{h_1,h_2} union K_3`

has mutually orthogonal row/column directions `c_1`, `c_2`, and the rank-one block `u_(I_3)u_(K_3)^T`. Their singular values are

`1`, `1`, `||u_(I_3)|| ||u_(K_3)|| = sqrt(1/2)sqrt(1/2)=1/2`.

Thus `Z=(1*1*1/2)^2=1/4` exactly. The rank-three row leverages are `1/m`, `1/m`, and `2/m` on the three groups, so the `1/2` gate holds for every even `m>=4`.

## Partner-family spectrum and basis mass

The deterministic coefficient vectors `p,w,c,v` are orthonormal, with `p,w` overlapping in original hub coordinates but orthogonal as vectors. In the basis `{p,c,v,w}`, the coefficient matrix is

`diag_block([[0,1],[1,0]], [1], [1])`,

so the nonzero spectrum is exactly `{1,-1,1,1}`.

For the leaf frame, `sum v_i^4=1/16`. For `c`, whose squared coordinates are one `1/2` and sixteen `1/32`,

`sum c_i^4 = (1/2)^2 + 16(1/32)^2 = 1/4+1/64=17/64`.

Two iid determinant bases are disjoint exactly when their chosen `v` coordinates differ and their chosen `c` coordinates differ. Therefore

`rho=(1-1/16)(1-17/64)=(15/16)(47/64)=705/1024`.
