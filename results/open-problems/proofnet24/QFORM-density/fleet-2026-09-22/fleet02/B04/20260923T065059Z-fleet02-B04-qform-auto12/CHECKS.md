# Exact/symbolic checks for fleet02/B04 20260923T065059Z

These checks support the finite algebra in REPORT.md; they are not a proof of the full conjecture.

## Exact-star matrix

For

`M0=[[2,1,1],[1,1,1],[1,1,1]]`,

- rank = 2;
- nonzero singular values are `2+sqrt(2)` and `2-sqrt(2)`;
- their product is 2;
- `Z2=e2(M0^T M0)=4`;
- every nonzero physical 2x2 minor has determinant 1 and uses row 1 and column 1.

For `g=gamma^2`, exact symbolic multiplication gives

`K_11=(6g+4)/(g^2+12g+4)`,
`K_22=K_33=(3g+2)/(g^2+12g+4)=K_11/2`,
`tr K=2 K_11`.

Therefore the square-assisted ridge gate is impossible at every scale because admissibility requires `q>=2K_11`, while `tr K=2K_11<=q<4q/3`.

The exact-rank-two Fourier bound is

`[8 sqrt(e)/3^(1/4)] 2^(-1/4)=8.427512693903992...`.

## Near-star matrix

For

`M_eps=[[2,1,1],[1,1,1],[1,1,1+eps]]`,

`det M_eps=eps` and the squared 2x2 minors, grouped by left row pair, are

- `{1,2}`: `1,1,0`, total `2`;
- `{1,3}`: `1,(1+2eps)^2,eps^2`, total `2+4eps+5eps^2`;
- `{2,3}`: `0,eps^2,eps^2`, total `2eps^2`.

Hence

`Z2=4+4eps+7eps^2`.

At `eps=10^(-12)` high-precision scalar evaluation gives

`Z2=4.000000000004...`,
`r_C=4.999999999995...e-25`,
`L=log(1/r_C)=55.955189412418044...`,
`ell0=0.333333333333111111...`.

The strictly convex first-branch stationarity equation

`-1/ell +1/[4(1-ell)] +(1/8)log[ell(1-r_C)/(r_C(1-ell))]=0`

has the unique root

`ell*=0.14163448612643017947592939094...`,
`q*=1.71673102774713964104814121812...`.

Substitution in the exact optimized formula yields

`B_vol=61.89826829192555432664037299...`.

At fixed `q=4/3`, the exact optimized value is

`104.06624845711598...`.

## Partner k-sample evaluation

For row-pair probabilities `a=r_A,b=r_B,c=r_C`,

`delta_k=1-(a+b)^k-(a+c)^k-(b+c)^k+a^k+b^k+c^k`.

At `eps=10^(-12)`, `k=7` gives

`delta_7=3.39062499999660937499999056640625...e-24`

and fleet03/B04 r26 gives

`B_partner(7)=62.96716222831743782872098720...`.

For comparison, the evaluated values for `k=3,...,10` are approximately

`110.797, 78.699, 68.058, 64.087, 62.967, 63.309, 64.494, 66.207`.

## Same-matrix square-assisted ridge point

For `g=gamma^2`, exact symbolic algebra gives denominator

`D0=eps^2 g^2+7eps^2 g+eps^2+2eps g^2+4eps g+g^3+12g^2+4g`,

`K_11=(5eps^2g+eps^2+4eps g+6g^2+4g)/D0`,

`theta=(eps^2g^2+14eps^2g+3eps^2+2eps g^2+8eps g+12g^2+8g)/D0`,

`det(I+M_eps M_eps^T/g)=D0/g^3`.

For `0<eps<1`, symbolic subtraction gives

`K_11-K_22 = g(3eps^2+4eps+3g+2)/D0>0`,

`K_11-K_33 = -g(eps-1)(eps g+2eps+3g+2)/D0>0`,

so `K_11` is the maximum physical ridge diagonal.

At `eps=10^(-12)`, `gamma=eps/4`, and `q=2K_11`:

`K_11=0.999999999999999999999999881250...`,
`theta=2.799999999999839999999999684500...`,
`q=1.999999999999999999999999762500...`.

The square-assisted ridge gate is satisfied and its exact formula evaluates to

`1236.00288426963130196971862977...`.

## Physical rank-two excision

Conditioning on the second original left coordinate and retaining rows 1 and 3 leaves a 2x3 cross block with

`det(C_eps C_eps^T)=2+4eps+5eps^2`.

Therefore the product of its two nonzero singular values is

`sqrt(2+4eps+5eps^2)`,

and the exact-rank-two square theorem gives

`[8 sqrt(e)/3^(1/4)] (2+4eps+5eps^2)^(-1/8)`.

At `eps=10^(-12)` this equals

`9.190267759834622...`.
