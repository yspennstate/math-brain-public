"""Every numerical claim of the five-eigenvalue paper, evaluated at 50 digits.

Each line prints the exact value, the claimed bound, the margin, and PASS/FAIL.
"""
from mpmath import mp, mpf, sqrt, log, pi, e

mp.dps = 50
eta, zeta, a0 = mpf(1) / 12, mpf(1) / 256, mpf(5) / 48
C3 = 3 * sqrt(2) * e * (mpf(9) / 2) ** (mpf(1) / 6)
C2 = 8 * sqrt(e) * mpf(2) ** (-mpf(1) / 8)
L0 = 2 + 2 * log(19)
gamma = {m: (44 - 5 * sqrt(2) * (2 * m - 1)) / 96 for m in (1, 2, 3)}

results = []


def claim(name, value, bound, kind='<'):
    ok = value < bound if kind == '<' else value > bound
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name:58s} value={mp.nstr(value, 12):>16s} {kind} {mp.nstr(bound, 8):>10s}  margin={mp.nstr(abs(bound - value), 6)}")


# (6.1)-(6.2)
claim('eta^2 + zeta == a0^2 (difference)', abs(eta ** 2 + zeta - a0 ** 2), mpf(10) ** -45)
for m in (1, 2, 3):
    k = 2 * m - 1
    claim(f'identity (1 - eta - sqrt2 a0 k)/2 == gamma_{m} (difference)', abs((1 - eta - sqrt(2) * a0 * k) / 2 - gamma[m]), mpf(10) ** -45)
claim('gamma_1 > 0.38', gamma[1], mpf('0.38'), '>')
claim('gamma_2 > 0.237', gamma[2], mpf('0.237'), '>')
claim('gamma_3 > 0.09', gamma[3], mpf('0.09'), '>')
claim('sqrt2 < 1.4143', sqrt(2), mpf('1.4143'))
claim('(44 - 7.0715)/96 > 0.38', (44 - mpf('7.0715')) / 96, mpf('0.38'), '>')
claim('(44 - 21.2145)/96 > 0.237', (44 - mpf('21.2145')) / 96, mpf('0.237'), '>')
claim('(44 - 35.3575)/96 > 0.09', (44 - mpf('35.3575')) / 96, mpf('0.09'), '>')
# Proposition 7.1
claim('C3 < 15', C3, 15)
claim('C2 < 12.2', C2, mpf('12.2'))
claim('1/gamma_3 < 100/9', 1 / gamma[3], mpf(100) / 9)
claim('15*100/9 < 167', 15 * mpf(100) / 9, 167)
claim('exact no-pivot density C3/gamma_3 < 167', C3 / gamma[3], 167)
claim('0.237^(-1/2) < 2.055', mpf('0.237') ** -0.5, mpf('2.055'))
claim('12.2*2.055 < 26', mpf('12.2') * mpf('2.055'), 26)
claim('exact no-pivot half moment C2 gamma_2^(-1/2) < 26', C2 / sqrt(gamma[2]), 26)
# Proposition 7.2
claim('16 zeta^(-1/4) == 64 (difference)', abs(16 * zeta ** (-mpf(1) / 4) - 64), mpf(10) ** -45)
S = pi + 4 * log(2) + 2 * L0
claim('pi + 4 log2 + 2 L0 < 21.7', S, mpf('21.7'))
claim('rational: 3.1416 + 4 + 4*0.6932 + 4*2.9445 < 21.7', mpf('3.1416') + 4 + 4 * mpf('0.6932') + 4 * mpf('2.9445'), mpf('21.7'))
claim('sqrt(12) < 3.465', sqrt(12), mpf('3.465'))
claim('3.465*21.7 < 76', mpf('3.465') * mpf('21.7'), 76)
claim('exact diagonal-pivot half moment < 77', eta ** -0.5 * S + 1, 77)
claim('pi < 3.1416', pi, mpf('3.1416'))
claim('log 2 < 0.6932', log(2), mpf('0.6932'))
claim('log 19 < 2.9445', log(19), mpf('2.9445'))
claim('e > 2.7', e, mpf('2.7'), '>')
# Theorem 1.1 branches
claim('scalar branch sqrt(12)*77 < 267', sqrt(12) * 77, 267)
claim('definite branch 16 pi < 51', 16 * pi, 51)
ind = 16 * (8 + 4 * log(2) + 2 * log(19)) + 1 / e
claim('indefinite branch 16(8+4log2+2log19)+1/e < 267 (exact)', ind, 267)
claim('indefinite with rational bounds < 267', 16 * (8 + 4 * mpf('0.6932') + 2 * mpf('2.9445')) + 1 / mpf('2.7'), 267)
claim('6 + log16 + L0 == 8 + 4log2 + 2log19 (difference)', abs(6 + log(16) + L0 - (8 + 4 * log(2) + 2 * log(19))), mpf(10) ** -45)
claim('sup_D D^(-1/2) log D = 2/e: value at D = e^2', (e ** 2) ** -0.5 * log(e ** 2), 2 / e + mpf(10) ** -40)
claim('final constant 267 <= 270', mpf(267), mpf(270) + mpf(10) ** -40)
# Remark 8.2
claim('Remark 8.2: 1/N < zeta for N = 257', mpf(1) / 257, zeta)
claim('sqrt(pi) e^(1/4) 2 sqrt2 == 2 sqrt(2 pi) e^(1/4) (difference)', abs(sqrt(pi) * e ** 0.25 * 2 * sqrt(2) - 2 * sqrt(2 * pi) * e ** 0.25), mpf(10) ** -45)
claim('(2 sqrt(2pi) e^(1/4))^2 == 8 pi sqrt(e) (difference)', abs((2 * sqrt(2 * pi) * e ** 0.25) ** 2 - 8 * pi * sqrt(e)), mpf(10) ** -40)
claim('(1/(2pi)) 8 pi sqrt(e) == 4 sqrt(e) (difference)', abs(8 * pi * sqrt(e) / (2 * pi) - 4 * sqrt(e)), mpf(10) ** -45)
claim('int_{-1/2}^{1/2} |u|^(-1/2) du == 2 sqrt 2 (difference)', abs(2 * 2 * sqrt(mpf(1) / 2) - 2 * sqrt(2)), mpf(10) ** -45)
print('ALL PASS' if all(results) else 'SOME FAIL', f'({sum(results)}/{len(results)})')
