# Deterministic checks — account01/B02 20260924T082047Z

Theorem labels:
- `QFORM-PIVOT-ABS-ACTUAL-MODULATION-L1-FALSE-v1`
- `QFORM-TWIST-COVER-CONDITIONING-RECEIVER-v1`

## Fresnel obstruction constants
For `m in [1,2]`, two integrations by parts give

`|J(t,m)| <= (1/(2t))(1+1/8)+(3/(2t))*int_1^2 y^(-4)dy`

and `int_1^2 y^(-4)dy=7/24`, hence

`|J(t,m)| <= 9/(16t)+7/(16t)=1/t`.

The leading boundary term has modulus at least

`(1/(2t))(1/m-1/(m+1)) =1/(2tm(m+1)) >=1/(12t)`.

Thus

`|G(t,m)| >=1/(12t)-1/(2t^2) >=1/(24t)` for `t>=12`.

Therefore `int_12^infinity E_M |G(t,M)|dt=infinity`.

## Exact-target embedding

`A=[[1,1,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]]` has eigenvalues `{2,1,1,0}`.

For every cap-one probability density `f`, the square pushforward density `g` obeys

`||g||_(3/2) <=2`.

With Fourier convention `hat g(t)=int exp(itu)g(u)du`, Hausdorff--Young gives

`||hat g||_3 <=2(2*pi)^(1/3)`.

Three independent cap-one square variables therefore satisfy

`||product_j hat g_j||_1 <= [2(2*pi)^(1/3)]^3 =16*pi`

with

`16*pi = 50.26548245743669`.

## Live r47 constants

`kappa=247/576=0.4288194444444444`

`sqrt(kappa)=0.6548430685625712`.

Exact-untwisted partner payment:

`2*sqrt(pi)*kappa^(-1/4)=4.380627392825819`.

Twist-cover payment when the retained singular product is at least `(1/2)*sqrt(kappa)`:

`2*sqrt(2*pi)*kappa^(-1/4)=6.195142670637365`.

Partner physical-2x2 Fourier constant before determinant scaling:

`16*pi*sqrt(60)=389.35475289346675`.

All arithmetic is deterministic; no Monte Carlo or histogram is used.
