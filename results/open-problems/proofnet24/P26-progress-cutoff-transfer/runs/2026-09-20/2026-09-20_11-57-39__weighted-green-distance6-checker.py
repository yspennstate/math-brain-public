from fractions import Fraction

# Exact sanity check for P26 T08 weighted-Green / distance-six biregular-half theorem.
# Concrete Eisenstein parameters: (K+1,k+1)=(9,3), hence K=8,k=2.

K = 8
k = 2
q = K * k
D1 = (K + 1) * k
D2 = D1 * q
D3 = D2 * q
assert (D1, D2, D3) == (18, 288, 4608)

# Let B=MM^T.  A1=B-(K+1)I and, for m>=2,
# A1 A_m = A_{m+1} + (k-1) A_m + Kk A_{m-1}.
# A2 numerator in B is x^2-(2K+k+1)x+K(K+1).
# Therefore A3=(A1-(k-1)I)A2-Kk A1.

def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c

# Coefficients low-to-high.
A1 = [-(K + 1), 1]
A2 = [K * (K + 1), -(2 * K + k + 1), 1]
A1_minus = [-(K + k), 1]  # A1-(k-1)I = B-(K+k)I
A3 = poly_mul(A1_minus, A2)
for i, ai in enumerate(A1):
    A3[i] -= q * ai
assert A3 == [-576, 246, -29, 1]


def f(x):
    return x**3 - 29 * x**2 + 246 * x - 576

# Perron point b0=(K+1)(k+1)=27.
assert f(27) == D3
# Adj-Ramanujan nontrivial B-spectrum lies in [2,18], with a possible zero mode.
assert Fraction(f(0), D3) == Fraction(-1, 8)
assert Fraction(f(2), D3) == Fraction(-1, 24)
assert Fraction(f(18), D3) == Fraction(1, 16)

# f'(x)=3x^2-58x+246 has critical points (29 +/- sqrt(103))/3.
# At them q3 equals (-62 +/- 103 sqrt(103))/62208.
# Since sqrt(103)<11, both absolute values are <1195/62208<1/8.
assert 103 < 11**2
assert 62 + 103 * 11 < 7776  # 7776/62208 = 1/8

# Interior half-radius increments for an exact bigraph-distance-six step.
counts = {
    -3: 1,
    -2: k - 1,
    -1: (K - 1) * k,
     0: (k - 1) * q,
     1: (K - 1) * k * q,
     2: (k - 1) * q**2,
     3: q**3,
}
assert counts == {-3: 1, -2: 1, -1: 14, 0: 16, 1: 224, 2: 256, 3: 4096}
assert sum(counts.values()) == D3

v = Fraction(sum(delta * c for delta, c in counts.items()), D3)
M2 = Fraction(sum(delta * delta * c for delta, c in counts.items()), D3)
tau2 = M2 / (v**3)
assert v == Fraction(1445, 512)
assert M2 == Fraction(12713, 1536)
assert tau2 == Fraction(3332636672, 9051588375)

# Long-range-expansion obstruction: output degree D3 has tree branching D3-1,
# but one output step moves at most 3 half-radii in the ancestor, whose branching is q.
assert q**3 == 4096
assert D3 - 1 == 4607
assert q**3 < D3 - 1

print('P26_T08_WEIGHTED_GREEN_DISTANCE6_EXACT')
print(f'K={K} k={k} q=Kk={q}')
print(f'degrees D1={D1} D2={D2} D3={D3}')
print('q3 numerator = x^3 - 29 x^2 + 246 x - 576')
print(f'q3(27)=1, q3(0)={Fraction(f(0),D3)}, q3(2)={Fraction(f(2),D3)}, q3(18)={Fraction(f(18),D3)}')
print('critical points=(29+-sqrt(103))/3; |q3(critical)|<1/8 by sqrt(103)<11')
print('nontrivial spectral modulus <= 1/8; gap >= 7/8')
print('radial counts', counts)
print(f'drift v={v}')
print(f'raw second moment M2={M2}')
print(f'profile tau^2={tau2}')
print(f'branching mismatch (Kk)^3={q**3} < D3-1={D3-1}')
print('ALL_CHECKS_PASS')
