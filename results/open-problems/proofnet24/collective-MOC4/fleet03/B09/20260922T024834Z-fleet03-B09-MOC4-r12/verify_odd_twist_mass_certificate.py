from fractions import Fraction as F
from itertools import permutations, product

K = [
    [F(245983,5120000), F(5030591,5120000), F(-39077,1024000)],
    [F(-5113569,5120000), F(56671,5120000), F(19643,1024000)],
    [F(-8539,1024000), F(-35819,1024000), F(5009153,5120000)],
]
X = [
    [F(-3609633,1280000), F(111173,51200), F(2385071,1280000)],
    [F(-917133,1280000), F(1431961,1280000), F(525623,256000)],
    [F(-1352967,1280000), F(1061147,1280000), F(948017,1280000)],
]

alpha = [F(2302707,5120000), F(1268991,5120000), F(-871389,5120000)]
beta = [F(-720783,640000), F(39007,640000), F(0)]

active = [
    ((1,1,1), (-1,1,1), F(2042727,2560000)),
    ((1,1,-1), (-1,1,-1), F(133141,256000)),
    ((1,-1,1), (1,1,1), F(514151,2560000)),
    ((1,-1,-1), (-1,1,1), F(98951,2560000)),
]

def coeff(i,j,s):
    return s*K[i][j] + X[i][j]/2

def endpoint(rho, signs):
    return sum(coeff(i,rho[i],signs[i]) for i in range(3))

even = []
odd = []
for rho in permutations(range(3)):
    for signs in product((1,-1), repeat=3):
        item = (endpoint(rho,signs), rho, signs)
        if signs[0]*signs[1]*signs[2] == 1:
            even.append(item)
        else:
            odd.append(item)

even_max = max(even)
odd_max = max(odd)
assert even_max[0] == F(13195057,5120000)
assert odd_max[0] == F(20773731,5120000)
assert odd_max[0]-even_max[0] == F(3789337,2560000)

for r,c,lam in active:
    assert lam >= 0
    assert r[0]*r[1]*r[2]*c[0]*c[1]*c[2] == -1

slacks = []
for i in range(3):
    for j in range(3):
        for s in (1,-1):
            cover = alpha[i] + beta[j]
            for r,c,lam in active:
                if r[i]*c[j] == s:
                    cover += lam
            slack = cover - coeff(i,j,s)
            assert slack >= 0
            slacks.append(((i,j,s),slack))

positive = [slack for _,slack in slacks if slack > 0]
assert len(positive) == 9
assert min(positive) == F(347,16000)

dual = sum(alpha) + sum(beta) + 2*sum(lam for _,_,lam in active)
assert dual == even_max[0]

print('even_max =', even_max[0], float(even_max[0]), 'rho/signs =', even_max[1], even_max[2])
print('odd_max =', odd_max[0], float(odd_max[0]), 'rho/signs =', odd_max[1], odd_max[2])
print('odd_minus_even =', odd_max[0]-even_max[0], float(odd_max[0]-even_max[0]))
print('dual_objective =', dual, float(dual))
print('minimum_positive_dual_slack =', min(positive), float(min(positive)))
print('tight_channels =', sum(1 for _,s in slacks if s == 0))
print('PASS: exact odd-twist mass dual certificate')
