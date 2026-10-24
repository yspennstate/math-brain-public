# Deterministic checks for account01/B09 20260923T154646Z

Status: finite arithmetic/algebra checks only; not an independent proof review.

## Constants

With `gamma=1/12`,

`c_gamma=2^(1-gamma) Gamma((1-gamma)/2)/(2 sqrt(pi) Gamma(gamma/2))`

has value

`c_(1/12)=0.0438556136991933256451916375282...`.

For the `k=1,q=2` fractional compiler and an exposed cross block satisfying `||C||_F>=s/4`,

`K_off
 =36 c_(1/12)e^(1/12)pi^(1/12)2^(1/8)
 =2.05862292994977906750128053550...`.

The scalar-diagonal branch gives

`K_diag=(6/5)2^(1/3)
 =1.51190525987384779772065272873...`,

so `K_0=K_off<2.059` safely covers both cases.

The logarithm-to-fractional coefficient before optimization is

`B_factor=(12/e)2^(1/12)K_0
 =9.62829532971563421454788832570...`.

For `A=2sqrt(2)` and exponent `m=1/6`,

`K_pair
 =(7/6)(6A)^(1/7) B_factor^(6/7)
 =12.1803572687653121188425544731...<12.181`.

The designated-partner base coefficient is

`5*2^(4/5)*sqrt(e)
 =14.3529523092629812937297227017...`.

At `s=243=3^5`, multiplication by `s^(-1/5)=1/3` gives

`4.78431743642099376457657423392...<4.785`.

## Cross-partition identity

For `O=S-diag(S)` and an iid Bernoulli half/half partition `(I,J)`,

`E ||S[I,J]||_F^2
 =sum_(i!=j) P(i in I,j in J) S_ij^2
 =(1/4)||O||_F^2`.

Thus `||O||_F>=s/2` implies the existence of a physical cut with `||S[I,J]||_F>=s/4`.

## Scalar quadratic sublevel length

After completing the square, the inverse image of

`|a y^2-c|<u`

has total length at most

`2 sqrt(2u/|a|)`.

If `|a|>=s/2`, this is at most `4s^(-1/2)u^(1/2)`. For a cap-one scalar density this is also a probability bound.

For a generic small-ball estimate

`P(|R-t|<u)<=min(1,L u^(1/2))`,

layer cake gives for `0<gamma<1/2`

`E|R-t|^(-gamma)
 <=[1/(1-2gamma)]L^(2gamma)`.

At `gamma=1/12`, `L=4s^(-1/2)`, this is the stated `K_diag s^(-1/12)`.

## Schur rank-two approximation identity

For

`A=[[E,K^T],[K,D0]]`, `E=E^T` invertible,

let

`L=[I_2;K E^(-1)]`.

Then exactly

`L E L^T
 =[[E,K^T],[K,K E^(-1)K^T]]`,

whose rank is at most two, and

`A-L E L^T
 =diag(0,D0-K E^(-1)K^T)`.

Therefore Eckart--Young yields

`sigma_3(A)<=||D0-K E^(-1)K^T||_op`.

## Regression matrix

For

`A0=[[0,1,0],[1,0,0],[0,0,1]]`,

the characteristic polynomial is

`(1-lambda)(lambda^2-1)`,

so its eigenvalues are `{-1,1,1}`. The pair `P={1,2}` has

`E=[[0,1],[1,0]]`, `|det E|=1`, `sigma_min(E)=1`,

and its exact Schur complement is `[1]`. Hence all normalization parameters in the new theorem equal one and the theorem returns `<12.181`.

## Scaling

Under matrix scaling `A -> uA`,

`D -> u^2 D`, `kappa -> |u| kappa`, `rho -> |u| rho`.

Thus

`D^(-3/7)(kappa rho)^(-1/14)`

scales as

`|u|^(-6/7)|u|^(-1/7)=|u|^(-1)`,

which is the required density scaling.
