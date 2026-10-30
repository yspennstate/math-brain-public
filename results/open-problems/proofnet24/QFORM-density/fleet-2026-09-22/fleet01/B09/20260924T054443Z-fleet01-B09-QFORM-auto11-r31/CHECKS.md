# Deterministic checks for fleet01/B09 r31

These are regression checks only; they are not proof premises.

## 1. Exact fixed-hub rank-one minor factorization

Seed `20260924`; eight leaf coordinates. Choose a random unit vector `v`, random star `c`, arbitrary random physical diagonal `D`, hub scalar `a=-0.7`, and `lambda=2.3`. Form

`A=[[a,c^T],[c,D+lambda vv^T]]`.

For every ordered pair of disjoint unordered leaf edges `I={i,j}`, `J={k,l}`, compare the direct determinant

`det A[{h} union I,{h} union J]`

with

`-lambda(c_i v_j-c_j v_i)(c_k v_l-c_l v_k)`.

Observed maximum absolute error:

`6.661338147750939e-16`.

## 2. Plucker normalization and aggregate identity

Put

`theta=||c-(c^Tv)v||`,
`z=(c-(c^Tv)v)/theta`,
`p_{ij}=(v_i z_j-v_j z_i)^2`.

Observed:

`sum p_I = 1.0000000000000002`,

`rho = sum_{I cap J=empty} p_I p_J = 0.4082919436249993`.

Direct ordered fixed-hub one-overlap currency:

`Omega_direct = 175.99627343944675`.

Exact-formula side:

`lambda^2 theta^4 rho = 175.99627343944638`.

Absolute discrepancy:

`3.694822225952521e-13`.

The largest physical row leverage of the augmented plane in this random regression was

`max_i(v_i^2+z_i^2)=0.5167990336413519`,

while `(1-rho)/2=0.29585402818750034`, consistent with the proved collision inequality.

## 3. Constants

For the `delta=1/4` fork,

`3 e^(2/3) delta^(-1/6)
 =3*2^(1/3)*e^(2/3)
 =7.361973353764773`.

At `Omega=13/48`,

`7.361973353764773*(13/48)^(-1/6)
 =9.1525874838...`.

The raw `r=1` one-hub constant is

`3e^(2/3)=5.843202123164027`.

## 4. Target-valid partner example

For

`Q_*=2UV+5X^2+2XZ_1+3Z_2^2`,

the coefficient matrix in coordinates `(U,V,X,Z_1,Z_2)` is

`[[0,1,0,0,0],
  [1,0,0,0,0],
  [0,0,5,1,0],
  [0,0,1,0,0],
  [0,0,0,0,3]]`.

Its spectrum is exactly

`{1,-1,3,(5+sqrt(29))/2,(5-sqrt(29))/2}`

with

`(5+sqrt(29))/2 = 5.192582403567252`,
`(5-sqrt(29))/2 = -0.19258240356725187`.

Thus at least three eigenvalues have modulus at least one. The fleet02/B09 r17 pair-log splice has `D_B=1`, `kappa=1`, `||m||=1`, so its coefficient is

`4 sqrt(2) e^(1/4) Gamma(1/4)^(1/2)
 =13.830540321993613`.

## 5. Scope checks

- `D` is diagonal only in the original independent leaf coordinates; no random-source rotation is made.
- The deterministic change from `(v,c)` to the orthonormal plane `(v,z)` is used only to identify Plucker weights; the fleet02/B09 theorem itself is explicitly source-coordinate/product-preserving.
- The final small-ball estimate is linear in interval length in the paid branch.
- Continuity is proved for the new rank-one fixed-hub branch because the fleet02/B09 r13 receiver has an integrable Fourier envelope.
- Continuity is not inferred from the separate r17 pair-log partner application.
- Full QFORM remains open.
