# Deterministic checks for account01/B19 r54

These checks are algebraic sanity checks for the constants and the designated-partner specialization. They are not independent proof review.

## Theorem H inversion constant

For one hub and one Fresnel square,

`K=((4*pi)^(3/2)/2)(|lambda| det G)^(-1/2)`

in `|phi(t)|<=min(1,K|t|^(-3/2))`. Since

`integral_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3)`,

Fourier inversion gives

`(1/(2*pi))*6*K^(2/3)
 = 12*2^(-2/3)(|lambda|detG)^(-1/3)`.

Numerically

`12*2^(-2/3)=7.559526299369239...`.

## Six-leaf peel constant

If `lambda_min(M_L)>=4/7`, then

`det G_L >= (4/7)^2 det G`.

Hence the receiver constant is at most

`12*2^(-2/3)*(49/16)^(1/3)
 =12*(49/64)^(1/3)
 =10.977917130068915...`.

If the light Gram fails, the heavy set has at most six rows and carries `>3/7` in one direction, so one row has squared directional mass `>(3/7)/6=1/14`, i.e. amplitude `>1/sqrt(14)`.

## account02/B19 r53 specialization

For

`A_a=a(l1 l2^T+l2 l1^T)+w w^T`,
`l1=e_h+v1`, `l2=u+v2`,

with the five supports `{h},U,V1,V2,W` pairwise disjoint except for the declared sums, take

`H={h}`, `I=V2 union W`, `J=U union V1`.

Then

`A[I,I]=w w^T`,
`c=A[I,h]=a v2`,
`G=diag(1,a^2)`,
`detG=a^2`.

Each row in `V2` or `W` has normalized leverage `1/m`, so for `m>=2` the exact Theorem H gate is satisfied. Thus

`||p||_infinity <=12*2^(-2/3)|a|^(-2/3)`.

At the principal-minimal threshold `|a|=1/2`, this equals exactly `12`. At `|a|=1`, it equals `7.559526299369239...`.

The core eigenvalues are `+2a,-2a`, and the disjoint `w` mode contributes `+1`; hence `|a|>=1/2` is indeed in the three-large-eigenvalue target.

Terminal marker: `QFORM_B19_R54_HUB_SQUARE_CONSTANT_CHECK_PASS`.
