# r54 quarter-power sharpening, part 1

The source non-diagonal quarter-power proof has exact coefficient
C_* = 2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8).

For Gamma(3/8), on [0,1] use
e^(-x) <= 1-x+x^2/2-x^3/6+x^4/24.
This gives
I_0 <= 8/3-8/11+4/19-4/81+1/105.

For T=int_1^infty x^(-5/8)e^(-x) dx, integration by parts gives
T=e^(-1)-(5/8) int_1^infty x^(-13/8)e^(-x) dx.
Since log x<=x-1,
x^(-13/8)>=exp(-(13/8)(x-1)),
so T<=(16/21)e^(-1)<2/7 using e>8/3.

Therefore
Gamma(3/8)<1419533/592515<12/5,
with exact slack 2503/592515.
