from fractions import Fraction as F
from itertools import product


def eta(r, p):
    return (1 - (1 - 2*p)**r) / (2*r)

# Genuine four-input Boolean witness.
POS = {(0, 0, 0), (0, 0, 1), (0, 1, 0)}

def h(y):
    return 1 if y in POS else -1

def gate(s, y):
    return h(y) if s else -1

p_s = F(3, 8)
ps = {0: 1-p_s, 1: p_s}
mean = F(0)
alpha = [F(0) for _ in range(4)]
for s in (0, 1):
    for y in product((0, 1), repeat=3):
        x = (s,) + y
        prob = ps[s] * F(1, 8)
        val = gate(s, y)
        mean += prob * val
        for i in range(4):
            z = list(x)
            z[i] ^= 1
            if gate(z[0], tuple(z[1:])) != val:
                alpha[i] += prob

assert mean == F(-23, 32)
p_out = (1-mean)/2
assert p_out == F(55, 64)
assert alpha == [F(3,8), F(9,32), F(3,32), F(3,32)]

bias = [F(3,8), F(1,2), F(1,2), F(1,2)]
expected = {
    2: F(345,4096),
    4: F(114465,8388608),
    6: -F(6611525,4294967296),
    8: -F(93493998015,17592186044416),
    10: -F(26899150376739,4503599627370496),
    12: -F(52743128810867765,9223372036854775808),
}

print('B17 even-moment repair barrier exact verifier')
print('selector_bias=3/8; data_biases=1/2,1/2,1/2')
print('h_positive={000,001,010}')
print('alpha_selector=', alpha[0], sep='')
print('alpha_data=', tuple(alpha[1:]), sep='')
print('output_mean=', mean, sep='')
print('output_true_bias=', p_out, sep='')

for r in (2,4,6,8,10,12):
    defect = sum(a*eta(r,p) for a,p in zip(alpha,bias)) - eta(r,p_out)
    assert defect == expected[r]
    g = 2*r*defect
    closed = F(23,32)**r - F(5,32) - F(3,8)*F(1,4)**r
    assert g == closed
    print(f'r={r} defect={defect} decimal={float(defect):.18g}')

# Exact tail monotonicity identity.
for r in range(0, 42, 2):
    g = F(23,32)**r - F(5,32) - F(3,8)*F(1,4)**r
    gp = F(23,32)**(r+2) - F(5,32) - F(3,8)*F(1,4)**(r+2)
    diff = -F(495,1024)*F(23,32)**r + F(45,128)*F(1,4)**r
    assert gp-g == diff
    assert diff < 0
assert 12*expected[6] == -F(19834575,1073741824)

qcomp = F(1322305,11721216)
pcomp = F(1322305,72351744)
# Check equivalent cleared mixed-repair face.
assert F(345,4096)*F(0) + F(114465,8388608)*qcomp + expected[6] == 0
assert F(345,4096)*pcomp + expected[6] == 0
print('eta6_quartic_compensation_min=', qcomp, sep='')
print('eta6_quadratic_compensation_min=', pcomp, sep='')
print('PASS')
