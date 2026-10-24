# account01/B03 r40 checks

These are deterministic algebra/constant checks for `REPORT.md`; they are not numerical evidence for the full conjecture.

## Pair-factor determinant normalization

Indefinite normalization uses `J=[[0,1/2],[1/2,0]]`, so `det J=-1/4`. If `B=L^T J L`, then

`|det B|=(det L)^2/4`, hence `|det L|=2 sqrt(D)`.

For `gamma(s)=L^{-1}(sigma e^s, sigma t e^{-s})`,

`det(gamma'(s),gamma'(r)) = det(L^{-1})[-2t sinh(s-r)]`,

hence

`|det(gamma'(s),gamma'(r))|=(|t|/sqrt D)|sinh(s-r)|`.

With threshold `a=K^(1/3)`, `K=|t|/sqrt D`, the two hyperbola branches contribute at most

`8/a+4a^2/K=12K^(-1/3)`.

Multiplication by `(2sqrt D)^(-1)` gives exactly

`6 D^(-1/3)|t|^(-1/3)`.

## Definite normalization

If `B=L^T L`, then `|det L|=sqrt D`. For the circle parameterization at level `t>0`,

`p_T(t)=(2sqrt D)^(-1) int_0^(2pi) f(x(theta))g(y(theta))dtheta`.

The tangent determinant is

`|det(gamma'(theta),gamma'(phi))|=(t/sqrt D)|sin(theta-phi)|`.

For `K=t/sqrt D>=8` and `a=K^(1/3)`, the slow-tangent set has measure at most `4pi K^(-1/3)` and the two derivative-large pieces contribute at most `4K^(-1/3)`. Hence

`p_T(t)<=2(1+pi)D^(-1/3)t^(-1/3)`.

For `K<8`, the elementary cap `p_T<=pi/sqrt D` is dominated by the same envelope since `2(1+pi)/2>pi` at `K=8` and the required right side increases as `K` decreases.

## Half-Frostman to one-third Riesz

At `rho_0=H^-2`,

`(H/3) int_0^rho0 rho^(-5/6)d rho =2H^(2/3)`,

and

`(1/3) int_rho0^infty rho^(-4/3)d rho=H^(2/3)`.

Total: `3H^(2/3)`.

## Overlap-two cancellation

From `Z_1>=J_2/(4D^2)`,

`H<=H_1 Z_1^(-1/4)<=sqrt(2)H_1 D^(1/2)J_2^(-1/4)`.

Therefore

`D^(-1/3)H^(2/3)
 <=2^(1/3)H_1^(2/3)J_2^(-1/6)`,

so the physical-pair determinant cancels exactly.

Using

`H_1=sqrt(2e)Gamma(1/4)=8.453631522124514356...`,

numerical evaluation gives

- all invertible signatures: `C_2=3(2+2pi)2^(1/3)H_1^(2/3)=129.924435862525374...`;
- indefinite only: `18*2^(1/3)H_1^(2/3)=94.1119371673922894...`;
- at `J_2=1/144`: `C_2 J_2^(-1/6)=297.45270437507936...`;
- posterior whole-copy coefficient: `4sqrt(2pi C_2)=114.28660859120921...`.

## Whole-copy Riesz normalization

With characteristic-function convention `phi(t)=E exp(itY)`, Gaussian regularization of

`int_R |t|^(-1/2) exp(itx)dt`

gives `sqrt(2pi)|x|^(-1/2)`. Therefore for `Y=Q-Q'`, whose characteristic function is `|phi_Q|^2`,

`int |t|^(-1/2)|phi_Q(t)|^2dt=sqrt(2pi)E|Q-Q'|^(-1/2)`.

If `||p_Q||inf<=M`, then `||p_(Q-Q')||inf<=M`; splitting at `R` gives `4M sqrt(R)+R^(-1/2)`, optimized at `R=(4M)^(-1)`, hence `E|Q-Q'|^(-1/2)<=4sqrt(M)`.
