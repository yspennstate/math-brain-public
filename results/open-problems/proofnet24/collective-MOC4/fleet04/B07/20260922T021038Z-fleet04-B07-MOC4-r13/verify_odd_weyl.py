from fractions import Fraction as F
from itertools import permutations, product

# Exact structured K,X from fleet01/B07 r11b, eqs. (16)-(17).
K = [
    [F(245983,5120000), F(5030591,5120000), -F(39077,1024000)],
    [-F(5113569,5120000), F(56671,5120000), F(19643,1024000)],
    [-F(8539,1024000), -F(35819,1024000), F(5009153,5120000)],
]
X = [
    [-F(3609633,1280000), F(111173,51200), F(2385071,1280000)],
    [-F(917133,1280000), F(1431961,1280000), F(525623,256000)],
    [-F(1352967,1280000), F(1061147,1280000), F(948017,1280000)],
]

wp = [[K[i][j] + X[i][j]/2 for j in range(3)] for i in range(3)]
wm = [[-K[i][j] + X[i][j]/2 for j in range(3)] for i in range(3)]

vals = []
for rho in permutations(range(3)):
    for bits in product((0,1), repeat=3): # 0 = complex-linear q+, 1 = anti-linear q-
        score = sum((wm if bits[i] else wp)[i][rho[i]] for i in range(3))
        vals.append((score, rho, bits, sum(bits) % 2))

even = max(v for v in vals if v[3] == 0)
odd = max(v for v in vals if v[3] == 1)
expected_even = F(13195057,5120000)
expected_odd = F(20773731,5120000)
assert even[0] == expected_even
assert odd[0] == expected_odd
assert even[1:] == ((1,2,0),(0,0,0),0)
assert odd[1:] == ((1,0,2),(0,1,0),1)
assert odd[0] - even[0] == F(3789337,2560000)

print('even_max =', even[0], float(even[0]))
print('even_argmax rho,bits =', even[1], even[2])
print('odd_max =', odd[0], float(odd[0]))
print('odd_argmax rho,bits =', odd[1], odd[2])
print('odd_minus_even =', odd[0]-even[0], float(odd[0]-even[0]))
print('PASS: exact 48-state colored-matching enumeration')
