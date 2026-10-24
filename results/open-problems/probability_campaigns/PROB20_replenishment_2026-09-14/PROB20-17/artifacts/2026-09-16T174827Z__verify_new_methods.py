from fractions import Fraction
from itertools import product

# PROB20-17 exact finite support-stratum obstruction and algebra checks.

# 1) Relaxed symmetric nonnegative kernel with loops.
K = (
    (1,1,1,0),
    (1,1,0,1),
    (1,0,1,1),
    (0,1,1,1),
)
by_support = {k:[0,0] for k in range(1,5)}
for w in product(range(4), repeat=4):
    wt = 1
    for i,j in zip(w,w[1:]):
        wt *= K[i][j]
    k = len(set(w))
    by_support[k][0] += wt
    by_support[k][1] += 1

expected = {
    1:(4,4,Fraction(1,1)),
    2:(56,84,Fraction(2,3)),
    3:(40,144,Fraction(5,18)),
    4:(8,24,Fraction(1,3)),
}
for k,(s,c) in by_support.items():
    es,ec,ea = expected[k]
    assert (s,c,Fraction(s,c)) == (es,ec,ea)
assert Fraction(by_support[4][0],by_support[4][1]) > Fraction(by_support[3][0],by_support[3][1])
wr = Fraction(sum(v[0] for v in by_support.values()),4**4)
wor = Fraction(by_support[4][0],by_support[4][1])
assert wr == Fraction(27,64)
assert wor == Fraction(1,3)
assert wor < wr

# 2) Exact polynomial identity for the two-duplicate-cluster rank-one family.
# Let c be overlap and x=t+t^{-1}. We verify the minimum-at-x=2
# factorization used in the proof by coefficient arithmetic.
# 6 + 2c + 2c^2 - 10c^3 = 2(1-c)(5c^2+4c+3).
lhs = [6,2,2,-10]  # increasing powers of c
# multiply 2*(1-c)*(3+4c+5c^2)
a = [1,-1]
b = [3,4,5]
prodcoef = [0]*(len(a)+len(b)-1)
for i,ai in enumerate(a):
    for j,bj in enumerate(b):
        prodcoef[i+j] += 2*ai*bj
assert prodcoef == lhs

# For x>=2 and 0<=c<=1, F(x,c)=3(x^2-2)+6(c+c^2)x-10(c+c^2+c^3)
# has dF/dx = 6x+6(c+c^2) > 0. This algebraic sign is immediate;
# the finite checker verifies exact endpoint values at all rational c=k/1000.
for k in range(1001):
    c = Fraction(k,1000)
    endpoint = 6 + 2*c + 2*c*c - 10*c*c*c
    factored = 2*(1-c)*(5*c*c+4*c+3)
    assert endpoint == factored
    assert endpoint >= 0

print('relaxed_kernel_support_profile:')
for k in range(1,5):
    s,cnt = by_support[k]
    print(f'  support={k}: sum={s}, count={cnt}, average={Fraction(s,cnt)}')
print(f'WOR={wor}; WR={wr}; WOR/WR={wor/wr}')
print('support_monotonicity_failure: avg_support4 > avg_support3 =', Fraction(1,3), '>', Fraction(5,18))
print('two_cluster_factorization: 6+2c+2c^2-10c^3 = 2(1-c)(5c^2+4c+3) >= 0 on [0,1]')
print('ALL ASSERTIONS PASSED')
