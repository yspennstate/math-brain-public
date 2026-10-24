# r54 quarter-power sharpening, part 2

Exact elementary bounds:
2^(5/8)<1543/1000 because
1543^8-32*1000^8=131234262969485620561601>0.

pi^(-1/4)<19/25 follows from pi>3 and
3*19^4-25^4=338>0.

e^(3/8)<291/200: first use the convergent series certificate e<271829/100000, then
291^8*100000^3-200^8*271829^3
=1963569748421281000000000000000>0.

Hence
C_* <
(1543/1000)(19/25)(291/200)(12/5)
=25593741/6250000
<41/10,
with slack 31259/6250000.

The source diagonal branch is already <=2*(rho/L)^(1/4). Therefore for every nonzero symmetric quadratic part S, L=||S||,
P{|R-a|<rho} <= min(1,(41/10)(rho/L)^(1/4)).
