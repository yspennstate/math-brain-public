# fleet02/B20 r44 exact checks

These are deterministic regressions for `REPORT.md`; they are not numerical evidence for the unrestricted conjecture.

## Hub global-cut constants

Take `c=1/128`, `eps=2^-12`, and the fleet03/B20 r46 inequality

`E3(W) >= (1/3) s1(W)^2 dist_F(W,rank<=2)^4`.

At `s1(W)>=c` and `dist_F>=eps`,

`delta_E3=(1/3)c^2 eps^4=2^-62/3=7.228014483236696e-20`.

With the completed marginal-free physical-E3 coefficient

`C_E3=8.45302122552817687470491804598...`,

`C_E3*delta_E3^(-1/6)=13097.109458857976... <13098`.

## Pinned D5 constant

The e5f71... D5 receiver is

`5 sqrt(2e) Z5^(-1/10)`.

At `Z5=1/1024=2^-10`, this equals

`10 sqrt(2e)=23.316439815971243... <23.317`.

## Four-bank obstruction

For `A_*=(J_4-I_4) tensor I_2`:

- `spec(J_4-I_4)={3,-1,-1,-1}`;
- therefore `spec(A_*)={3,3,-1,-1,-1,-1,-1,-1}` and `rank(A_*)=8`;
- every balanced 2+2 bank cut has cross matrix `J_2 tensor I_2`, whose singular values are `{2,2,0,0}` and whose rank is exactly two.

Thus exact rank-two on all three balanced cuts does not imply global off-diagonal rank <=6.

Terminal marker: `QFORM_B20_R44_GLOBAL_HUB_CUT_CHECK_PASS`.
