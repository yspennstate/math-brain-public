# Deterministic checks — fleet01/B04 r30

Marker: `QFORM_B04_R30_OPT_ROWCAP_CHECK_PASS`.

The checks below were carried out with exact algebra where indicated and ordinary high-precision arithmetic only for displayed decimal values.

## Threshold and constants

Take

`h0=324/625=0.5184`.

For the D' branch,

`A(h)=6 sqrt(e) (2h)^(-1/2)(3-4h)^(-1)`.

At `h0`,

`2h0=648/625`, `3-4h0=579/625`, hence

`A(h0)=15625 sqrt(e)/(1737 sqrt(2))=10.487028558565074...`.

For the one-hub projected-E2 branch,

`C_E2=3*2^(7/6)*e^(1/3)=9.39913188784886...`,

so

`C_E2 h0^(-1/6)=10.486814313156756... < A(h0)`.

The previous generic E3 constant is

`C_old=3*2^(4/3)*e^(1/3)=10.550168831164775...`,

so

`C_E2 h0^(-1/6) < A(h0) < C_old`.

## Tuned dense carrier

The heavy marginal formula is

`alpha_H(y)=y(y+3)/[(y+1)(y+4)]`.

Solving `alpha_H(y)=324/625` gives the exact polynomial

`301 y^2+255 y-1296=0`,

with positive root

`y0=(-255+sqrt(1625409))/602=1.69421144734834...`.

Direct substitution gives `alpha_H(y0)=0.5184`.

The total third-volume is

`Z(y)=(y+1)^2(y+4)=4+9y+6y^2+y^3`,

so

`Z(y0)=41.333001538086286...`.

The new bound is

`A(h0) Z(y0)^(-1/6)=5.639876923233456...`,

whereas the previous generic E3 constant gives

`C_old Z(y0)^(-1/6)=5.673833478645989...`.

## Designated partner inequality

For the first two heavy rows,

`W_12=2y0^2+y0^3=y0^2(y0+2)=10.603688798646596...`.

The fleet02/B04 r20 pair-anchored E3 theorem therefore gives

`3*2^(5/6) W_12^(-1/6)=3.606368399164259...`.

## Dense right rotation

Let

`Vnum=[[14,-2,-3,-4],[-2,11,-6,-8],[-3,-6,6,-12],[-4,-8,-12,-1]]`.

Direct integer multiplication gives

`Vnum^T Vnum=225 I_4`,

so `V=Vnum/15` is orthogonal. Multiplying the eight light Hadamard rows by `Vnum` gives no zero coordinate, so every light physical crossing coefficient is nonzero. The three heavy rows also have no zero crossing coefficient because every entry in the first three rows of `Vnum` is nonzero.

For the Sylvester `H_8`, the first four columns divided by `sqrt(8)` satisfy `U^T U=I_4`. Therefore the row-frame identity is

`R_y^T R_y=diag(y+1,y+1,y+1,1)`.

## Exact row-triple face masses

Cauchy-Binet on the light Parseval frame yields, by number of distinguished heavy rows in the triple,

- zero heavy: total mass `4`;
- exactly one specified heavy row: `3y`, hence total `9y`;
- exactly one specified heavy pair: `2y^2`, hence total `6y^2`;
- all three heavy rows: `y^3`.

Their sum is exactly `4+9y+6y^2+y^3=(y+1)^2(y+4)`.

All identities above are consistent with the formulas in `REPORT.md`.
