# Exact algebra and constant checks

Run `20260922T194010Z-account03-B05-QFORM-r16`.

These are supporting checks for the analytic proof in `REPORT.md`; they are not finite certificates of the full conjecture.

## Stress-family pair

For

`B_a=[[a,sqrt(1+a)],[sqrt(1+a),0]]`,

`det(lambda I-B_a)=lambda^2-a lambda-(1+a)=(lambda-(1+a))(lambda+1)`.

Thus the eigenvalues are `1+a,-1`, so

`D=|det B_a|=1+a`, `kappa=sigma_min(B_a)=1` for `a>0`.

The third scalar block is `1`, hence `spec(A_a)={1+a,-1,1}` and `s_3(A_a)=1`.

## Scalar-square small ball

For any `beta,t` and `rho>0`, the set

`{x: |(x+beta)^2-t|<rho}`

has Lebesgue length at most `2 sqrt(2rho)`. Translation removes `beta`. If `t<rho`, the set is contained in `[-sqrt(t+rho),sqrt(t+rho)]`, whose length is at most `2sqrt(2rho)`. If `t>=rho`, its length is

`2(sqrt(t+rho)-sqrt(t-rho))`,

which decreases for `t>rho` and at `t=rho` equals `2sqrt(2rho)`.

Therefore a cap-one scalar input gives `H=2sqrt(2)` in the pair-log smoothing theorem.

## New bound

The pair-log smoothing constant is

`4 sqrt(2H)(D kappa)^(-1/4)`.

With `H=2sqrt(2)`, `D=1+a`, `kappa=1`,

`4 sqrt(4sqrt(2))=8*2^(1/4)`.

Hence

`||p||_infinity <= 8*2^(1/4)*(1+a)^(-1/4) <=8*2^(1/4)`.

Decimal reference only:

`8*2^(1/4) = 9.513656920021768...`.

## Arbitrary-rank pair-extension optimizer

The reviewed source reduces to

`F(r)=A/r+B sqrt(r)`

with

`A=2sqrt(2)`,

`B=20*2^(1/4)D^(-1/2)kappa^(-1/4)s^(-1/4)`.

Differentiation gives `r=(2A/B)^(2/3)` and

`min F=3(A B^2/4)^(1/3)`.

Now

`A B^2/4
 =(2sqrt(2))/4 * 400sqrt(2) * D^(-1) kappa^(-1/2) s^(-1/2)
 =400 D^(-1) kappa^(-1/2) s^(-1/2)`.

Thus

`min F=3*400^(1/3)D^(-1/3)kappa^(-1/6)s^(-1/6)`,

exactly the source theorem.

For the stress family this gives the weaker but still uniform value

`3*400^(1/3)*(1+a)^(-1/3) <=3*400^(1/3)`,

with decimal reference

`3*400^(1/3)=22.104188991842317...`.
