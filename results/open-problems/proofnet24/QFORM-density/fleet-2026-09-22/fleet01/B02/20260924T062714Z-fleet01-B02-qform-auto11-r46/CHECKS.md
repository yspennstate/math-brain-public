# Deterministic checks for fleet01/B02 r46

Run: `20260924T062714Z-fleet01-B02-qform-auto11-r46`

These checks verify only the algebra/constants in `REPORT.md`; they are not numerical evidence for the unrestricted conjecture.

## 1. Unified E2 Fourier coefficient

The three exhaustive source branches have coefficients

- diffuse: `2*pi*sqrt(e) Z^(-1/4)`;
- heavy-row/diffuse-residual: `2*pi*(alpha Z)^(-1/4)` with `alpha>1/2`, hence `<2*pi*2^(1/4) Z^(-1/4)`;
- heavy-row/concentrated-residual: `pi*sqrt(2)*S2^(-1/2)` with `S2>sqrt(Z)/2`, hence `<2*pi Z^(-1/4)`.

The diffuse coefficient dominates because

`2^(1/4)=1.189207115002721... < sqrt(e)=1.648721270700128...`

and `1<sqrt(e)`.

## 2. Live E2 constants

`Z0=247/2304=0.1072048611111111...`

`K0=2*pi*sqrt(e)*(2304/247)^(1/4)=18.103956177059132...`

`K0/pi=2*sqrt(e)*(2304/247)^(1/4)=5.762668230196026...`

`sqrt(2e/pi)*K0=23.815559678336694...`

Hence the report's rounded safe constants

`K0<18.103957`, `K0/pi<5.762669`, and `sqrt(2e/pi)K0<23.815560`

are valid.

## 3. Lp/Lr algebra

For `1<p<=2`,

`2 int_0^K 1 dt + 2 int_K^infinity (K/t)^p dt
 =2K+2K/(p-1)=2K*p/(p-1)`.

With `r=p/(p-1)`, one has `1/p=(r-1)/r`, so inverse Hausdorff--Young gives

`(2*pi)^(-1/p) [2Kr]^(1/p)
 =(Kr/pi)^((r-1)/r)`.

No endpoint `p=1` is claimed.

## 4. Gaussian small-ball algebra

With `x=(epsilon*K)^2/2`,

`2 int_0^K exp(-epsilon^2 t^2/2)dt
 +2K int_K^infinity exp(-epsilon^2 t^2/2)dt/t
 <=2K+K E1(x)`.

Thus

`P(|Q-s|<=epsilon)
 <=sqrt(e/(2*pi))*epsilon*K*[2+E1(x)]`.

If `epsilon*K<=1`, then `x<=1/2` and

`E1(x)<=log(1/x)+E1(1)<log(1/x)+1`,

so

`2+E1(x)<3+log 2+2 log(1/(epsilon K))
             <4+2 log(1/(epsilon K))`.

This is exactly

`sqrt(2e/pi)*epsilon*K*[2+log(1/(epsilon K))]`.

For `epsilon*K>1`, the report uses only the trivial probability bound one.

## 5. Newest fleet02/B02 application

`kappa=247/576=0.4288194444444444...`

`2*sqrt(pi)*kappa^(-1/4)=4.380627392825819...`

so the displayed `<4.380628` bound is safe.
