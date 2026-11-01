# Checks for `QFORM-TRANSVERSE-VERTEX-RANDOM-SLOPE-LOCALIZATION-v1`

Run: `20260924T033822Z-fleet03-B14-QFORM-auto11`.

## Constant check

For density cap `m`,

`m integral_0^(1/m) r^(-1/2) dr = 2 sqrt(m)`.

For a probability density capped by `M`,

`M integral_{-1/(2M)}^(1/(2M)) |t|^(-1/2) dt = 2 sqrt(2M)`.

Thus

`2 K_W sqrt(K_U/|a|) * 2 sqrt(2M)
 = 4 sqrt(2) K_W sqrt(K_U M/|a|)`.

If `D=2S` and `||p_S||inf<=M_S`, then `||p_D||inf<=M_S/2`, giving

`4 sqrt(2) K_W sqrt(K_U M_S/(2|a|))
 =4 K_W sqrt(K_U M_S/|a|)`.

## Exact target family Q_*

For

`Q_*=2(W+U)^2+4US`

the symmetric matrix is

`A_*=[[2,2,0],[2,2,2],[0,2,0]]`.

Direct determinant expansion gives

`det(lambda I-A_*)=lambda^3-4lambda^2-4lambda+8`.

Its values are

`p(-2)=-8`, `p(-1)=7`,
`p(1)=1`, `p(2)=-8`,
`p(4)=-8`, `p(5)=13`.

Because the matrix is real symmetric, all three roots are real. The three disjoint sign-change intervals therefore contain the three eigenvalues, so

`spec(A_*) subset (-2,-1) union (1,2) union (4,5)`

with one eigenvalue in each interval. Hence `s_3(A_*)>1`.

Numerically the eigenvalues are approximately

`-1.6038754716, 1.1099162642, 4.4939592074`.

For arbitrary affine terms, completing the W-square gives

`2(W+U)^2 +4US +ell_W W+ell_U U+ell_S S+c
 =2(W+U+ell_W/4)^2
  +(4S+ell_U-ell_W)U
  +ell_S S+c-ell_W^2/8`.

Since `4S+constant` has density cap `1/4`, Theorem 2 gives

`4 sqrt(2) sqrt((1/4)/2)=2`.

The designated fleet04/B14 r10 comparison is

`6 sqrt(pi)/sigma_*`, `sigma_*>1`,

hence `<6 sqrt(pi)=10.634723105433096...`; the new receiver gives `2`.

## Diffuse bank family

For disjoint unit vectors `w,u,s`, the ambient matrix of

`(w dot X)^2 +2(u dot X)(s dot X)`

acts as

`[1] direct_sum [[0,1],[1,0]]`

on the orthonormal bank span, hence has nonzero spectrum `{1,1,-1}`.

If every bank has size m and constant coefficients `m^(-1/2)`, every invertible physical triple must select one coordinate from each active bank, and its principal block is

`(1/m)[[1,0,0],[0,0,1],[0,1,0]]`,

with minimum absolute eigenvalue `1/m`. Thus the fleet04/B14 physical-triple bound is `6 sqrt(pi) m` on such a triple, while the bank projection caps are at most `sqrt(2)` and the new compiler gives the dimension-free bound `8`.

## Scope guard

The proof does not allow an arbitrary residual `R(U,Z)` outside the square. If `R(U,Z)=-D(Z)U`, the transverse affine resource can be cancelled identically, leaving a single translated square and destroying any claimed universal bounded-density conclusion. This verifies that the stated structural restriction is material.
