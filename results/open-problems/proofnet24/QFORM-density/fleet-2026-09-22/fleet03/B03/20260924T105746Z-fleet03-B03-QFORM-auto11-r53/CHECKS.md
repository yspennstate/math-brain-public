# fleet03/B03 r53 checks

Run: `20260924T105746Z-fleet03-B03-QFORM-auto11-r53`.

These are deterministic algebra/constant checks for the proof in `REPORT.md`; they are not Monte Carlo evidence.

## 1. Slice constant

The rearrangement step gives

`int k^(4/3) <= 3*2^(-2/3) M^(2/3)m^(2/3)`.

Hausdorff-Young then gives

`||A_r||_4^2`
` <= sqrt(2 pi) [3*2^(-2/3)]^(3/2) M m |a|^(-1/2)`
` = (3/2)sqrt(6 pi) M m |a|^(-1/2)`.

Identity checked symbolically:

`sqrt(2*pi)*(3*2^(-2/3))^(3/2) = (3/2)*sqrt(6*pi)`.

## 2. Weighted-time optimizer

With

`D=(3*pi/2)*sqrt(6*pi) M N |a|^(-1/2)|b|^(-1)`,

minimize

`4 sqrt(T)+D/T`.

The critical point is `T^(3/2)=D/2`. Substitution gives

`3*2^(2/3) D^(1/3)`
` =3 sqrt(6*pi)(MN)^(1/3)|a|^(-1/6)|b|^(-1/3)`.

Numerical base constant:

`3 sqrt(6*pi) = 13.024822582048818...`.

Dividing by the Fourier-Riesz constant `sqrt(2*pi)` gives

`3 sqrt(3) = 5.196152422706632...`.

## 3. Complementary-weight compiler constant

The two-bank crossing envelope

`|phi_T(t)| <= min(1, 2*pi*|det C|^(-1/2)|t|^(-1))`

implies

`A_+(T) <= (16/3)(2*pi)^(3/2)|det C|^(-3/4)`.

Combining with the new negative-half estimate and dividing by `2*pi` gives the exact density constant

`(1/(2*pi))*sqrt(3*sqrt(6*pi)*(16/3)*(2*pi)^(3/2))`
` =4*3^(1/4)`
` =5.2642960518099695...`.

## 4. Strict target matrix

For

`A_*=[[1/2,1/2,sqrt(2)], [1/2,1/2,-sqrt(2)], [sqrt(2),-sqrt(2),1]]`,

symbolic computation gives

`det A_* = -4`,

`charpoly(A_*)=(lambda-1)(lambda^2-lambda-4)`.

Hence

`spec(A_*)={1,(1-sqrt(17))/2,(1+sqrt(17))/2}`,

and the smallest absolute eigenvalue is `(sqrt(17)-1)/2>1`.

For this example, `M=N=1`, `a=1`, `b=2`, so

`A_- <=3*sqrt(6*pi)*2^(-1/3)`
`      =10.337808534221727...`,

and

`E|Q-Q'|^(-1/2) <=3*sqrt(3)*2^(-1/3)`
`                  =4.124188910995808...`.

Adding an independent unit-determinant two-bank crossing gives

`||p||_infinity <=4*3^(1/4)*2^(-1/6)`
`                  =4.689954604468751...`.

## 5. Partner r5 conversion

Partner r5 at

`math-open-problems@fbe1dfba05eea312d8f12f22f2132476758039a8`

gives `H<=4 sqrt(2)` for its explicit `d det M_3=1` block. Whole-copy conversion gives

`A_- <=4 sqrt(pi H)`
`     <=8 sqrt(pi sqrt(2))`
`      =16.862517844086494...`.

## 6. Scope audit

- no pointwise quadratic-phase decay used;
- no independence asserted after rotating `(S,R)`;
- no conditional density cap for a conjugate sum/difference pair used;
- no marginal density cap for `R` used;
- arbitrary scalar phase `K(V)` retained exactly, including `dV^2`;
- arbitrary same-bank shear/baggage `G(R),H(R)` retained exactly;
- whole-copy identity used only for `Q-Q'`;
- one-copy density claimed only after an actually independent complementary positive-half crossing;
- full QFORM and full-target continuity remain OPEN.

`QFORM_B03_R53_CHECK_PASS`
