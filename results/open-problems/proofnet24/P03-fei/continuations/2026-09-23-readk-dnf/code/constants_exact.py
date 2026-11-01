"""Exact / high-precision checks of every numerical constant used in the proofs."""
from fractions import Fraction as Fr
from math import comb
import mpmath as mp
mp.mp.dps = 40
ok = True
def check(name, cond, detail=''):
    global ok
    ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name + ('  ' + detail if detail else ''))

# C_3 = sup_m m Pr[Bin(m-1,1/2) < m/3 - 1], attained at m = 13 with value 13*299/4096
def tau(m, beta):
    thr = Fr(m, 1) / beta - 1
    return Fr(sum(comb(m - 1, j) for j in range(m) if j < thr), 2 ** (m - 1))
vals = [(Fr(m) * tau(m, Fr(3)), m) for m in range(1, 3001)]
best = max(vals)
check('C_3 = 13*299/4096 at m=13 (m<=3000)', best == (Fr(13 * 299, 4096), 13), f'{float(best[0]):.10f}')
# tail beyond 3000 is negligible: m*exp(-(m-1)/18) < 1e-60 for m > 3000
check('Chernoff tail beyond m=3000 negligible', 3001 * mp.e ** (-mp.mpf(3000) / 18) < mp.mpf('1e-60'))
# Theorem 2.3 slope 2 + 2*3 + 2*C_3
slope = 2 + 6 + 2 * best[0]
check('Theorem 2.3 slope <= 9.898', slope <= Fr(9898, 1000), f'{float(slope):.6f}')
# Lemma 1.5 constant: 4a(log(1/a)-1) + 4a log2 e <= 2I + 1.771 a, and 1.771/2 + 2 <= 2.886
check('1.5: 4(log2 e - 1) <= 1.771', 4 * (1 / mp.log(2) - 1) <= mp.mpf('1.771'), mp.nstr(4 * (1 / mp.log(2) - 1), 8))
# B, L1
B = 3 * mp.sqrt(3 / mp.pi); L1 = 2 * mp.log(B) + 2
check('L_1 = 4.1511...', abs(L1 - mp.mpf('4.1511')) < 1e-4, mp.nstr(L1, 10))
# exponential moment B^{2 lam}/(1-2 lam) at lam=1/4 equals 2 sqrt(B); 4 ln 2 + 2 ln B < 4.93
check('4 ln2 + 2 ln B < 4.93', 4 * mp.log(2) + 2 * mp.log(B) < mp.mpf('4.93'), mp.nstr(4 * mp.log(2) + 2 * mp.log(B), 10))
# the integral bound: int_0^inf lam e^{lam u} min(1, B e^{-u/2}) du + 1 = B^{2 lam}/(1-2 lam)
lam = mp.mpf(1) / 4
integ = 1 + mp.quad(lambda u: lam * mp.e ** (lam * u) * min(1, B * mp.e ** (-u / 2)), [0, 2 * mp.log(B), mp.inf])
check('exp-moment integral identity', abs(integ - B ** (2 * lam) / (1 - 2 * lam)) < 1e-20, mp.nstr(integ, 12))
# Theorem 3.7 constants at a = 1.2
a = mp.mpf('1.2')
c0 = 3.886 + (1 + mp.log(a / (a - 1)) + mp.mpf('4.93') * a) / mp.log(2); c1 = (1 + 4 * a) / mp.log(2)
check('Thm 3.7: 3.886 + ... <= 16.5 and slope <= 8.4', c0 <= 16.5 and c1 <= 8.4, f'{mp.nstr(c0, 8)} + {mp.nstr(c1, 8)} ln m')
# Theorem 1.2 constant at a = (1+sqrt(1+4/L1))/2
a2 = (1 + mp.sqrt(1 + 4 / L1)) / 2
lem15 = 3 + 2 * (1 / mp.log(2) - 1)
check('Lemma 1.5: 1 + 2 + 1.7708/2 <= 3.8854', lem15 <= mp.mpf('3.8854'), mp.nstr(lem15, 10))
c12 = mp.mpf('3.8854') + (1 + mp.log(a2 / (a2 - 1)) + a2 * L1) / mp.log(2)
check('Thm 1.2 constant <= 15.1', c12 <= 15.1, mp.nstr(c12, 8))
# Lemma 4.2 case constants
check('4.2 case 1: min_{alpha in [1/(4e),1/4]} alpha log2(1/alpha) >= 0.316', (1 / (4 * mp.e)) * mp.log(4 * mp.e, 2) >= mp.mpf('0.316'), mp.nstr((1 / (4 * mp.e)) * mp.log(4 * mp.e, 2), 8))
check('4.2 case 1: 0.531 <= 1.7*0.316 and (log2 e)/e < 0.531', mp.log(mp.e, 2) / mp.e < 0.531 and 0.531 <= 1.7 * 0.316)
w0 = mp.mpf('0.012'); d = mp.mpf('0.024')
check('4.2 case 2: (1/2)log2(1/w0) < 3.2 and w0 log2(1/w0) < 3.2 delta', mp.log(1 / w0, 2) / 2 < 3.2 and w0 * mp.log(1 / w0, 2) < 3.2 * d,
      f'{mp.nstr(mp.log(1/w0,2)/2,6)}, {mp.nstr(w0*mp.log(1/w0,2),6)} vs {mp.nstr(3.2*d,6)}')
check('4.2 case 3: delta/(1-2delta) < 3/4, 2(1-2delta) > 1+delta, 12 delta < 1/e', d / (1 - 2 * d) < 0.75 and 2 * (1 - 2 * d) > 1 + d and 12 * d < 1 / mp.e)
check('4.2 case 3: sqrt(1-3delta) >= 1-3delta', mp.sqrt(1 - 3 * d) >= 1 - 3 * d)
# Theorem 4.4 constants
check('4.4(a): 2/ln2 + 8 <= 10.9', 2 / mp.log(2) + 8 <= 10.9, mp.nstr(2 / mp.log(2) + 8, 8))
ok_a = all(4 * k + 6 * k + 2 * max(mp.log(k, 2) + 2, 2 * k * float(best[0])) <= 14 * k for k in range(1, 200))
check('4.4(a): 4k+6k+2max(log k+2, 2k C3) <= 14k for k<=200 (and linear beyond)', ok_a)
a3 = mp.mpf('1.1087')
c4b = 2 / mp.log(2) + 9 + mp.log(mp.e * a3 / (a3 - 1), 2) + 2 * a3 * L1 / mp.log(2)
check('4.4(b) bracket < 30', c4b < 30, mp.nstr(c4b, 8))
c4c0 = 2 / mp.log(2) + 9 + mp.log(mp.e * a / (a - 1), 2) + a * mp.mpf('9.86') / mp.log(2)
c4c1 = 1 / mp.log(2) + a * 8 / mp.log(2)
check('4.4(c): <= 33 + 15.3 ln m', c4c0 <= 33 and c4c1 <= 15.3, f'{mp.nstr(c4c0,8)} + {mp.nstr(c4c1,8)} ln m')
check('4.4(c): 2(4 ln m + 4.93) and 2 ln(2m) <= 8 ln m + 9.86', all(2 * (4 * mp.log(m) + 4.93) <= 8 * mp.log(m) + 9.86 + 1e-12 and 2 * mp.log(2 * m) <= 8 * mp.log(m) + 9.86 for m in range(1, 1000)))
print('ALL PASS' if ok else 'SOME FAILED')
