from fractions import Fraction
from itertools import combinations

m = 64
amp = Fraction(1, 8)
rows = [(Fraction(1), Fraction(0), Fraction(0))]
rows += [(Fraction(0), amp, Fraction(0)) for _ in range(m)]
rows += [(Fraction(0), Fraction(0), amp) for _ in range(m)]

def dot(u, v):
    return sum(x*y for x, y in zip(u, v))

def det3(r1, r2, r3):
    a,b,c = r1
    d,e,f = r2
    g,h,i = r3
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)

gram = [[sum(r[i]*r[j] for r in rows) for j in range(3)] for i in range(3)]
assert gram == [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]

leverage = [dot(r, r) for r in rows]
theta = Fraction(1, 16)
H = [i for i,c in enumerate(leverage) if c > theta]
L = [i for i,c in enumerate(leverage) if c <= theta]
assert H == [0]

S = [[sum(rows[k][i]*rows[k][j] for k in L) for j in range(3)] for i in range(3)]
assert S == [[Fraction(0),Fraction(0),Fraction(0)],
             [Fraction(0),Fraction(1),Fraction(0)],
             [Fraction(0),Fraction(0),Fraction(1)]]
assert det3(tuple(S[0]), tuple(S[1]), tuple(S[2])) == 0

weights = []
for I in combinations(range(len(rows)), 3):
    d = det3(rows[I[0]], rows[I[1]], rows[I[2]])
    if d:
        weights.append((I, d*d))

assert len(weights) == m*m
assert sum(w for _, w in weights) == 1
assert max(w for _, w in weights) == Fraction(1, m*m)

print('n =', len(rows))
print('Gram =', gram)
print('heavy set =', H, 'count =', len(H))
print('light covariance S =', S)
print('det(S) = 0')
print('nonzero 3-row Plucker weights =', len(weights))
print('total 3-volume-squared mass =', sum(w for _, w in weights))
print('largest individual 3-row weight =', max(w for _, w in weights))
for K in (3,5,9,17):
    s = K - 1
    k2 = s // 2
    k3 = s - k2
    exact = Fraction(k2*k3, m*m)
    print(f'K={K}: maximal determinant mass in any K-row subset = {exact}')
print('PASS')
