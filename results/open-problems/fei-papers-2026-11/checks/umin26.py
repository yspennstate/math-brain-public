from fractions import Fraction as F
from math import comb
m = [F(1), F(1), F(8,3), F(11), F(908,15), F(415), F(23840,7), F(325719,10),
     F(112135066,315), F(3065263961,700), F(69174280444,1155),
     F(5680684105259,6300), F(1112571762134554,75075), F(2032842751996209,7700)]

def det(A):
    A = [r[:] for r in A]; n = len(A); d = F(1)
    for c in range(n):
        p = next(i for i in range(c, n) if A[i][c] != 0)
        if p != c:
            A[c], A[p] = A[p], A[c]; d = -d
        d *= A[c][c]
        for i in range(c+1, n):
            f = A[i][c] / A[c][c]
            for j in range(c, n):
                A[i][j] -= f * A[c][j]
    return d

u = [(2*k+1) * m[k] for k in range(14)]
print("u:", [str(x) for x in u[:7]])
a = [det([[u[i+j] for j in range(n)] for i in range(n)]) for n in range(1, 8)]
b = [det([[u[i+j+1] for j in range(n)] for i in range(n)]) for n in range(1, 8)]
print("(u_{i+j}) leading minors 1..7 positive:", all(x > 0 for x in a), f"7x7 = {float(a[-1]):.4e}")
print("(u_{i+j+1}) leading minors 1..7 positive:", all(x > 0 for x in b))
cat = [F(comb(2*k, k), k+1) for k in range(14)]
s = [m[k] / cat[k] for k in range(14)]
sb = [det([[s[i+j+1] for j in range(n)] for i in range(n)]) for n in range(1, 8)]
print("(s_{i+j+1}) 1..7 positive:", all(x > 0 for x in sb), " s_13 =", s[13])
r = [float(m[k+1] / m[k]) for k in range(13)]
print("ratios:", [f"{x:.4f}" for x in r])
print("first differences:", [f"{r[k+1]-r[k]:.4f}" for k in range(5, 12)])
