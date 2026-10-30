# Deterministic audit — rough Z-curvature aggregate routing

All identities below are for the family and cut defined in REPORT.md.

## Walsh frame

For `m=2^r`, `r>=4`, let

`u_z=m^(-1/2)`, `r_z=m^(-1/2)(-1)^(z_1)`, `s_z=m^(-1/2)(-1)^(z_2)`.

Summation over the hypercube gives

`<u,r>=<u,s>=<r,s>=0`, `||u||=||r||=||s||=1`.

For `L={z:z_3=0}` one has

`||r_L||^2=||s_L||^2=1/2`, `||1_L||^2=m/2`,

and the three restricted vectors remain pairwise orthogonal.

## Target spectral check

At `beta=eta=0`, the only nonzero crossing is

`E=[2r^T;2s^T]`,

so `E E^T=4 I_2`, and the symmetric bipartite block has spectrum

`{2,2,-2,-2,0^(m-1)}`.

The `h-N` perturbation is the rank-two star with vector `(beta,beta)`, hence operator norm `sqrt(2) beta`. The Z-block

`G=(eta/m)(11^T-I)`

has eigenvalues `eta(1-1/m)` and `-eta/m` with multiplicity `m-1`, so

`||G||=eta(1-1/m)<eta`.

Thus Weyl gives four eigenvalues of the full matrix with modulus at least

`2-sqrt(2) beta-eta`.

For `beta<=1/8`, `eta<=1/2`, this is at least

`2-sqrt(2)/8-1/2 = 1.323223304703363... >1`.

At the audit point `(m,eta,beta)=(64,1/2,1/8)`, direct diagonalization gives the four large eigenvalues approximately

`-2.0116771276, -2.0039100647, 1.9960975647, 2.0039251896`.

The proof uses the Weyl estimate, not the numerical diagonalization.

## Local principal determinants

Every principal triple containing `h` is singular.

For a triple `{n_i,z_j,z_k}`, `j!=k`, the matrix is

`[[0,a_j,a_k],[a_j,0,g],[a_k,g,0]]`

with `|a_j|=|a_k|=2/sqrt(m)` and `g=eta/m`. Its determinant is

`2 a_j a_k g`,

so the magnitude is exactly

`D_NZZ = 8 eta/m^2`.

For `{n_1,n_2,z}` the determinant is zero. For three Z coordinates, the off-diagonal entries all equal `g`, so the determinant is

`2 g^3 = 2 eta^3/m^3`.

Under `eta<=1/2`, `m>=16`, this is smaller than `8 eta/m^2`. Therefore the largest nonzero physical principal-triple determinant is exactly

`D_local=8 eta/m^2`.

Applying fleet03/B04 `QFORM-ZERO-PIVOT-3COORD-LINEAR-SQUARE-v1` gives

`3*2^(2/3) D_local^(-1/3)
 =3*2^(-1/3) m^(2/3) eta^(-1/3)`.

At `m=64`, `eta=1/2`, `D_local=1/1024` and the bound equals exactly `48`.

## Half-cut singular values and volume

For

`B=[2r_L,2s_L,(eta/m)1_L 1_R^T]`,

with `|R|=m/2`, the first two rank-one terms have singular values

`2||r_L||=sqrt(2)`, `2||s_L||=sqrt(2)`.

The third rank-one term has singular value

`(eta/m)||1_L||||1_R|| = eta/2`.

The left singular directions are pairwise orthogonal, so these are exactly the three positive singular values. Hence

`Z_3=e_3(B^T B)=2*2*(eta^2/4)=eta^2`.

Each normalized left singular vector has squared coordinate `2/m` on every row of L. Therefore the rank-three leverage, and hence canonical squared-minor row marginal, is exactly

`alpha_z=3*(2/m)=6/m`.

For `m>=16`, `alpha_z<=3/8<1/2`.

## Global q=1 weight optimization

Let `nu` be the canonical squared-minor probability law

`nu_(S,T)=det(B_(S,T))^2/Z_3`.

For any supported probability weight `w`, the determinant-entropy currency is

`log G(w)=sum w log det(B_(S,T))^2 + H(w)
        =log Z_3 - D_KL(w||nu)`.

Thus `G(w)<=Z_3=eta^2`, with equality only at `w=nu` on the support. Since `nu` satisfies the row gate, this is the global optimum over all q=1 admissible weights.

## Ridge quantities on the identical cut

The nonzero singular squares are

`2, 2, eta^2/4`.

Set

`k=2/(2+gamma^2)`, `h=eta^2/(eta^2+4 gamma^2)`, `theta=2k+h`.

Because the three normalized left singular vectors are flat on L, every diagonal of the ridge projector is

`(K_gamma)_(zz)=(2/m)(2k+h)=2 theta/m <6/m<=3/8<1/2`.

The determinant factor is

`D_gamma=(1+2/gamma^2)^2(1+eta^2/(4 gamma^2))`.

As `gamma->0`,

`theta->3`,
`D_gamma ~ eta^2 gamma^(-6)`,
`D_gamma^(-1/(2theta)) ~ eta^(-1/3) gamma`.

Therefore the determinant-retaining q=1 ridge expression

`[e/(sqrt(2) gamma)] [theta/(theta-2)] D_gamma^(-1/(2theta))`

converges to

`(3e/sqrt(2)) eta^(-1/3)`.

At `eta=1/2`, this is

`7.265141389555023...`.

The pinned e5 Theorem D value at the same point is

`6 sqrt(e) eta^(-1/3)=12.46355180618709...`.

Thus the concrete certified hierarchy is

`7.265141389555023... < 12.46355180618709... < 48`.
