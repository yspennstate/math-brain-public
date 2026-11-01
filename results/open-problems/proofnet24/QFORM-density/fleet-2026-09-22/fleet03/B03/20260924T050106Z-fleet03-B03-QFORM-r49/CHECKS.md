# fleet03/B03 r49 checks

Run: `20260924T050106Z-fleet03-B03-QFORM-r49`.
Scope: deterministic verification of the constants, Fourier normalization, spectral inequality, and the stress-test density in `REPORT.md`. These checks do not certify the unrestricted conjecture.

## A. Layer-cake density-cap constant

If `p_Y<=F`, then

`E|Y-a|^-1/2 = integral_0^infinity P(|Y-a|<u^-2) du`

and

`P(|Y-a|<u^-2)<=min(1,2F/u^2)`.

The crossover is `u0=sqrt(2F)`, so

`integral_0^u0 1 du + integral_u0^infinity 2F u^-2 du
 =u0+2F/u0
 =2sqrt(2F)`.

PASS.

## B. Conditional near-coloop cap

For fixed residual values `(T,C,D)=(t,c,d)`,

`Z=sqrt(q)X0+sqrt(1-q)t`

has conditional density

`z -> q^-1/2 f_0((z-sqrt(1-q)t)/sqrt(q))`,

hence cap `q^-1/2`. Mixture over `T|(C,D)` preserves the same cap. This uses only genuine source-disjoint independence of original coordinate `X0`; it does not assert independence among `T,C,D`.

PASS.

## C. Main half-Riesz constant

After `C_tilde=C+ell/(2beta)`, condition on `(C,D)`:

`|S-s|^-1/2
 =(2|beta||C_tilde|)^-1/2 |Z-a|^-1/2`.

Using cap `F=q^-1/2`, Lemma A gives

`E[|S-s|^-1/2|C,D]
 <=2 q^-1/4 |beta|^-1/2 |C_tilde|^-1/2`.

The unit product-projection cap `||p_C||inf<=sqrt(2)` gives

`E|C_tilde|^-1/2 <=2sqrt(2sqrt(2))=2^(7/4)`.

Product:

`2 * 2^(7/4)=2^(11/4)`.

PASS.

## D. Spectral lower bound on beta

In the null-pivot spectral bookkeeping basis,

`M e1=(0,beta,0)^T`.

If every eigenvalue magnitude of symmetric invertible `M` is at least `s`, then every singular value is at least `s`, so

`|beta|=||M e1||>=s||e1||=s`.

This does not use probabilistic independence in spectral coordinates.

PASS.

## E. Near-coloop q>=1/2 simplification

`2^(11/4) q^-1/4 <=2^(11/4)2^(1/4)=2^3=8`.

Thus `H<=8s^-1/2`.

PASS.

## F. Riesz-energy Fourier normalization

For `x!=0`, Abel-regularized cosine integration gives

`integral_R |t|^-1/2 exp(i t x) dt`
`=2 Gamma(1/2) cos(pi/4)|x|^-1/2`
`=sqrt(2pi)|x|^-1/2`.

Applying this to the law of `S-S'` yields

`integral |t|^-1/2 |phi_S(t)|^2 dt
 =sqrt(2pi) E|S-S'|^-1/2`.

Multiplying the main constant gives

`sqrt(2pi)*2^(11/4)=2^(13/4)sqrt(pi)`.

For `q>=1/2`, `|beta|>=s`, this is

`8sqrt(2pi)s^-1/2 =20.053026197048002... s^-1/2`.

PASS.

## G. Independent-square compiler

For cap-one `Y`, `V=d(Y+h)^2`, direct change of variables gives, on the appropriate half-line,

`p_V(v)
 <= |d|^-1/2 |v|^-1/2`.

Therefore convolution/conditioning against `S` gives

`p_(V+S)(x)<=|d|^-1/2 E|x-S|^-1/2`.

No continuity follows from this estimate alone.

PASS.

## H. Pair-log constant

The completed source theorem gives

`||p_Q||inf <=4sqrt(2H)(D_B kappa)^-1/4`.

With

`H=2^(11/4)q^-1/4|beta|^-1/2`,

`4sqrt(2H)=2^(31/8)q^-1/8|beta|^-1/4`.

For `q>=1/2`, `|beta|>=s`,

`2^(31/8)*2^(1/8)=2^4=16`,

so

`||p_Q||inf<=16s^-1/4(D_B kappa)^-1/4`.

PASS.

## I. Designated partner r3 application

Partner fleet04/B03 r3 supplies

`p_H(y)<=sqrt(2)|mu|^-1/2|y|^-1/2`.

Averaging over independent remainder `S` gives

`p_(H+S)(x)<=sqrt(2)|mu|^-1/2 E|x-S|^-1/2`.

The main half-Riesz theorem therefore yields coefficient

`sqrt(2)*2^(11/4)=2^(13/4)`.

At `q>=1/2`, this becomes

`2^(13/4+1/4)=2^(7/2)=8sqrt(2)`.

PASS.

## J. Interface stress test

Take independent `U,C~Unif[-1/2,1/2]`. For `R=2UC`, the product-density formula gives

`p_R(r)
 = integral 1_{|c|<=1/2} 1_{|r/(2c)|<=1/2} (1/(2|c|)) dc`
` = integral_{2|r|<=|c|<=1/2} (1/(2|c|)) dc`
` = log(1/(4|r|))`

for `0<|r|<1/4`.

Thus the logarithmic divergence at zero is correct. (The report's displayed stress formula used a different endpoint normalization in an early draft; the mathematically relevant fact is the logarithmic divergence. The canonical correction is `log(1/(4|r|))` for the stated `[-1/2,1/2]` uniforms.)

This demonstrates that a conditional scalar cap plus a bounded `(C,D)` joint density does not directly imply an `L^infinity` bound. It does not refute the half-Riesz theorem.

PASS, with normalization correction recorded.

## K. Scope audit

- No pointwise van-der-Corput phase decay is used.
- No independence after spectral rotation is asserted.
- No `X-X'` variable is declared independent of `X+X'`.
- The whole-copy identity is used only for `S-S'`.
- The same-bank puncture `TC` is retained exactly inside `R(C,D)` after conditioning on `(C,D)`.
- The main theorem is a half-Riesz/time estimate, not a bare density theorem.
- Essential boundedness is claimed only after a genuine source-disjoint square/pair receiver.
- Full-target continuity remains open.
- Full QFORM remains open.

`QFORM_B03_R49_CHECK_PASS`
