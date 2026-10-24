# Deterministic algebra and certificate checks

Run `20260923T202445Z-account02-B04-QFORM-auto11-r13`.

Let `1` denote the six-vector of ones and

`V = I_6 - (1/3) 1 1^T`, `D_L=diag(L,L,1,1,1,1)`, `M_L=D_L V`.

All computations below are exact except where a decimal is explicitly displayed.

## Householder algebra

Because `(1 1^T)^2=6 1 1^T`,

`V^2=I_6-(2/3)11^T+(1/9)6 11^T=I_6`.

Thus `V` is orthogonal. Its diagonal entries are `2/3` and off-diagonal entries are `-1/3`, so every one of the 36 physical coefficients of `M_L` is nonzero.

`M_L M_L^T = D_L^2 = diag(L^2,L^2,1,1,1,1)`.

Hence the singular values of `M_L` are `L,L,1,1,1,1`.

For the elementary symmetric polynomials of the squared singular values:

`E2 = L^4 + 8 L^2 + 6`,

`E3 = 4(L^4 + 3 L^2 + 1)`,

`E5 = 4 L^4 + 2 L^2 = 2L^2(2L^2+1)`,

`E6 = L^4`.

## Deletion and singleton currency

For the two heavy physical rows `H={1,2}`, the only triples avoiding H are the four triples among the four light rows, each of squared volume one. Thus

`Z_out(H)=4`, `delta=4/E3=1/(L^4+3L^2+1)`.

For either heavy row, projection perpendicular to that row leaves squared row norms `L^2,1,1,1,1`, so

`E2(projected residual)=4L^2+6`

and

`Z_i=L^2(4L^2+6)=4L^4+6L^2`.

The remaining heavy row has canonical projected-pair marginal

`alpha_heavy=4L^2/(4L^2+6)`.

Therefore the one-hub `ell=2` row gate `alpha<=1/2` fails exactly when `L^2>3/2`.

Promoting both heavy rows gives hub singular product `S=L^2`. Projecting their span away leaves four orthonormal light rows. For `ell=1`, `Z1=4` and every residual one-volume row marginal is `1/4`. With two literal original hub coordinates the hub projection density cap is at most one, so the grouped-crossing theorem gives exactly

`B_twohub(L)=3*sqrt(2)*L^(-2/3)`.

## Global q=1 weighted third-volume optimum

For any row triple S containing k heavy rows,

`z_S=sum_T det(M[S,T])^2 = det((MM^T)[S,S]) = L^(2k)`.

There are `N0=4,N1=12,N2=4` such triples. Conditional log-sum over columns shows that at a fixed row law p, the largest determinant-entropy currency is

`exp(H(p)+sum_S p_S log z_S)`.

Under the q=1 row gate every one of the six row marginals must equal `1/2`, because their sum is three. Therefore the expected number k of heavy rows is one, making `sum p log z_S=2 log L` fixed. Entropy is globally maximized by the uniform law on all 20 row triples, which is admissible. Hence

`G_D,opt=20L^2`.

Pinned e5 Theorem D consequently gives

`B_D(L)=6*sqrt(e)*(20L^2)^(-1/6)`.

## Global D-prime optimization

For marginal cap `h in [1/2,3/4)`, symmetry plus strict concavity reduce the exact row-law optimization to the expected number `a` of heavy rows. The constraints are

`3-4h <= a <= 2h`.

For `L>=2` the unconstrained volume law has expected heavy count at least `3/2`, so the optimum uses `a=2h`. Let `x_h>0` solve

`a=(3x+2x^2)/(1+3x+x^2)`.

Equivalently,

`x_h=[-3(1-a)+sqrt(9(1-a)^2+4a(2-a))]/[2(2-a)]`.

Then the global optimized currency over all supported row/column minor weights is

`G_h = 4(1+3x_h+x_h^2) * (L^2/x_h)^a`, `a=2h`.

The D-prime certificate is

`B_Dp(h;L)=6*sqrt(e)*(2h)^(-1/2)*(3-4h)^(-1)*G_h^(-1/6)`.

Its logarithmic derivative is

`d_h log B_Dp = -1/(2h)+4/(3-4h)-(1/3)log(L^2/x_h)`.

Since `x_h` is strictly increasing,

`d_h^2 log B_Dp = 1/(2h^2)+16/(3-4h)^2+(1/3)x_h'/x_h >0`.

Thus any root is the unique global optimum.

For `L=4096`, the unique root is

`h*=0.5898005198201123`,

`x_h*=1.5716288442514728`,

`G_h*=6393608144.046976`,

`B_Dp,opt=0.3299277319815257`.

At q=1,

`B_D=0.375266827787293`.

## Partner r40 square receiver

For the full physical crossing `M_L`,

`Z2=e2(MM^T)=L^4+8L^2+6`.

The fresh account03/B04 r40 square receiver applied to

`Q_L^+ = Z_0^2 + 2 X^T M_L Y`

gives

`B_partner(L)=8*2^(3/8)*(L^4+8L^2+6)^(-1/8)`.

At `L=4096`, this is

`B_partner=0.16210493466917075`.

## Pinned e5 fifth-volume certificate

`Z5=4L^4+2L^2`, so the pinned e5 D5 theorem gives

`B_D5(L)=5*sqrt(2e)*(4L^4+2L^2)^(-1/10)`.

At `L=4096`,

`B_D5=0.3643193710387943`.

## Direct ridge certificate

At `gamma^2=g=1/3`, write

`k_h=L^2/(L^2+1/3)`, `k_l=3/4`.

Then

`theta=2k_h+3`, `q=2k_h`,

so the leverage gate is saturated and

`theta-2q=3-2k_h>1`.

Also

`D_gamma = 256(1+3L^2)^2`.

The completed ridge theorem therefore gives the valid explicit certificate

`B_ridge=e/[sqrt(2q) gamma] * theta/(theta-2q) * D_gamma^(-1/(2theta))`.

At `L=4096`,

`B_ridge=0.19480623775069006`.

A numerical one-dimensional minimization of this exact ridge expression over its admissible regularization scale gives about `0.1947549966` at `g about 0.34485338`; this numerical observation is not used as a theorem or as a claim of exact ridge optimality.

## Stress-point hierarchy

For `L=4096`:

`B_twohub = 0.016572815184059713`,

`B_partner = 0.16210493466917075`,

`B_ridge(g=1/3) = 0.19480623775069006`,

`B_Dp,opt = 0.3299277319815257`,

`B_D5 = 0.3643193710387943`,

`B_D = 0.375266827787293`.

The integer compound values at this stress point are

`E3=1125900108169220`,

`Z_heavy_singleton=1125900007505920`,

`projected E2 after one heavy hub=67108870`,

`full E2=281475110928390`,

`E5=1125899940397056`.
