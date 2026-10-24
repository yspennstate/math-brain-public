# account03/B03 r35 deterministic checks

Run: `20260923T142318Z-account03-B03-QFORM-r35`.

The proof is analytic; these checks only verify its frame algebra and arithmetic constants.

For random orthonormal pairs `(v,q)` in dimensions `3,5,10,25`, choose the row `r` of maximum leverage `c=v_r^2+q_r^2`, rotate the spectral plane so that row becomes `(sqrt(c),0)`, and denote complement coordinates by `(a_j,b_j)`. Numerical errors in

- `sum_{j!=r} a_j^2 = 1-c`,
- `sum_{j!=r} b_j^2 = 1`,
- `sum_{j!=r} a_j b_j = 0`,

were all below `7e-16`. For independent test values `beta,m>0`, the determinant of the map `(S,Z)->(V,H)` equalled `m` to below `2e-16` in all trials.

Explicit arithmetic:

- `pi*sqrt(e) = 5.179610631848751`
- `2*sqrt(e) = 3.2974425414002564`
- `4*sqrt(e) = 6.594885082800513`
- `(16/3)*sqrt(pi)*e^(1/4) = 12.13800423716665`
- `6*sqrt(6)/2^(2/3) = 9.258491065302314`
- `[6*sqrt(6)/2^(2/3)]*e^(1/4) = 11.888137848024535`

Envelope integrals checked symbolically:

For `D>0`,

`2[ integral_0^D 1 dt + integral_D^infinity D^2 t^-2 dt ] = 4D`,

and

`2[ integral_0^D t^-1/2 dt + integral_D^infinity D^2 t^-5/2 dt ] = (16/3)sqrt(D)`.

The `L^4 -> half-Riesz` optimization is

`A R^(1/4)+R^(-1/2)`, `A=6^(3/4)||p||_4`,

with optimizer `R=(2/A)^(4/3)` and minimum

`3*2^(-2/3)*A^(2/3)`.

Using `||p||_4 <= (4S)^(3/4)` gives

`sup_z E|Q-z|^-1/2 <= [6sqrt(6)/2^(2/3)] S^(1/2)`.

`STATUS=QFORM_B03_R35_CHECK_PASS`
