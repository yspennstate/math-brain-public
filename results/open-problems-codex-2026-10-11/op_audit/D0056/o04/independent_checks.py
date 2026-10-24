from fractions import Fraction as F
from pathlib import Path
import mpmath as mp

mp.mp.dps = 60
A = mp.polylog(3, mp.mpf('0.5')) - mp.mpf('0.5')
B = mp.zeta(2) - mp.zeta(3)
c = 1 / (A+B)
g0 = c*(B+mp.zeta(3)-1)
h0 = c*(mp.zeta(2)-1)
assert abs(g0-h0) < mp.mpf('1e-55')
assert abs(c*(A+B)-1) < mp.mpf('1e-55')
count = 0
# Exact generating-function identity, including independently enumerated laws.
for weights in [(2,0,1), (1,2,3,4), (5,1,0,2,3), (0,1)]:
    p = [F(w,sum(weights)) for w in weights]
    q = 1-p[0]
    e = sum(v*2**i for i,v in enumerate(p))-1
    next_g = sum(a*b*2**max(i+j-1,0) for i,a in enumerate(p) for j,b in enumerate(p))
    assert next_g-1 == e+e*e/2-q+q*q/2
    count += 1
for n in range(2,151):
    b = F(3,2*n)
    # Independently compute the largest admissible e update and barrier gap.
    # r=q-q^2/2>=3/n^2; r=3/n^2 is the worst case.
    for j in range(101):
        e = b*F(j,100)
        next_e = e+e*e/2-F(3,n*n)
        next_b = F(3,2*(n+1))
        assert next_e-next_b <= e-b-F(3,8*n*n)
        count += 1
report = '\n'.join([
    f'Exact rational checks passed: {count}',
    f'A={mp.nstr(A,55)}', f'B={mp.nstr(B,55)}',
    f'c={mp.nstr(c,55)}', f'p0={mp.nstr(c*B,55)}',
    f'p2={mp.nstr(c/32,55)}',
    f'E[2^X0]={mp.nstr(g0,55)}',
    f'E[X0 2^X0]={mp.nstr(h0,55)}',
    'These checks supplement the infinite-series and barrier arguments; they do not estimate survival asymptotics.'
])+'\n'
Path('independent_checks.txt').write_text(report,encoding='utf-8')
print(report)
