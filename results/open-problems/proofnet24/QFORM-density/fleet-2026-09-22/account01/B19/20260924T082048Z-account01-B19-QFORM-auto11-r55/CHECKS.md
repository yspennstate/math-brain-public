# Checks — account01/B19 r55

These are diagnostics for the exact proofs in `REPORT.md`; they are not substitutes for the algebraic arguments.

## Constants

- `8 sqrt(2) exp(1/4) = 14.52708926969255`.
- `4 sqrt(2e) (4/49)^(-1/4) = 17.448425854139767`.
- At `|a|>=2^-12`, the latter gives `<1116.699255`.
- For the account03/B19 r51 physical crossing threshold `m0=4089/458752`, the designated account02/B19 theorem gives
  `3.929131770449763*m0^(-1/4)=12.787534220150162`.
- The newer E2 half-Riesz theorem on the same block gives
  `8 exp(1/4)*m0^(-1/2)=108.80379349595039`.
- `4 sqrt(2)(11/6)^(3/4)=8.912633851935281` for the 3-frame hub/rank-two peel.

## Scalar-Schur inheritance regression

For real symmetric Gaussian test matrices of dimensions `3,...,8`, 1000 samples per dimension, a random nonzero diagonal pivot was selected and the exact scalar Schur complement formed. The inequality

`s_3(A) <= s_2(S)`

was checked numerically. There were zero violations. The smallest observed ratio `s_2(S)/s_3(A)` was `1.0000000529027206` (roundoff-scale distance from equality).

The proof in the report is exact: add the best rank-one approximation of `S` to the exact rank-one scalar completion of `A`, then apply Eckart--Young.

## Random bipartition identity

For random real symmetric matrices in dimensions `4,...,8`, the ordered disjoint-tetrad energy

`W2(S)=sum_{|I|=|J|=2,I cap J=empty} det S[I,J]^2`

was enumerated exactly. All `2^n` red/blue physical colorings were enumerated and `e_2(S[R,C]^T S[R,C])` computed. In every test the ratio

`E_coloring[e_2]/(W2/16)`

was equal to one to floating-point precision; observed range

`[0.999999999999998, 1.0000000000000016]`.

This confirms the combinatorial factor `1/16` used in Theorem 3.1.

## Zero-tetrad diffuse constant

In the exact rigidity branch `S=Delta+R`, `rank R<=2`, the target inheritance and `||Delta||<1/2` imply

`s_2(R) >= s_2(S)-||Delta|| >1/2`,

so `rank R=2` and `|det M|=s_1(R)s_2(R)>1/4` in an orthonormal rank-two representation. Under the light-Gram gate `lambda_min(G_L)>=4/7`,

`det G_L >=16/49`,

hence

`|det M_L|=det(G_L)|det M|>4/49`.

The leverage bound is

`u_j^T G_L^-1 u_j <= (7/4)(2/7)=1/2`.

If the light Gram fails, the heavy set has at most six rows and carries `>3/7` of one coefficient direction, giving one literal row amplitude squared `>1/14`.

## Hub/rank-two transverse determinant

For `V^T V=I_2` and `c=A[I,h]`, the augmented Gram is

`G=[[I_2,V^Tc],[c^TV,||c||^2]]`.

The Schur determinant is exactly

`det G=||c||^2-||V^Tc||^2=||(I-VV^T)c||^2=delta^2`.

Theorem H with one hub and two Fresnel squares gives the exact decay coefficient

`|phi(t)| <= 8 pi^2 (|det M|delta^2)^(-1/2)|t|^-2`.

Integrating `min(1,K|t|^-2)` gives `4 sqrt(K)`; Fourier inversion yields

`4 sqrt(2)(|det M|delta^2)^(-1/4)`.

Terminal marker: `QFORM_B19_R55_SCALAR_SCHUR_TETRAD_CHECK_PASS`.
