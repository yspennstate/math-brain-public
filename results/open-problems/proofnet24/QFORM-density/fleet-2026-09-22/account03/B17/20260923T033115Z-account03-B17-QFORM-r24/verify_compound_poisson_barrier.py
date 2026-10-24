from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 50

M = [
    [F(6,7), F(-2,7), F(-3,7)],
    [F(-2,7), F(3,7), F(-6,7)],
    [F(-3,7), F(-6,7), F(-2,7)],
]
J = [[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(-1)]]

def trans(A): return [list(x) for x in zip(*A)]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def ident(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

OT_O = mm(trans(M),M)
assert OT_O == ident(3)
B = mm(mm(trans(M),J),M)
assert mm(B,B) == ident(3)
assert all(B[i][j] != 0 for i in range(3) for j in range(3))

rho = 4*mp.sqrt(mp.pi)/(mp.gamma(mp.mpf(1)/4)**2)
rho2 = (mp.sqrt(2)*mp.gamma(mp.mpf(3)/4)/
        (2*mp.sqrt(mp.pi)*mp.gamma(mp.mpf(5)/4)))
assert abs(rho-rho2) < mp.mpf("1e-45")
assert rho < 1

c = mp.mpf(1)
a = mp.mpf(1)
q = mp.e**(-c)*(mp.besseli(0,c) + 2*mp.nsum(
    lambda k: mp.besseli(k,c)*mp.e**(-6*a*a*k*k), [1, mp.inf]))
factor = rho + (1-rho)*q**3
C0 = 3*mp.sqrt(2)
bound = C0*factor
assert q < 1
assert factor < 1
assert bound < C0

print("B =")
for row in B:
    print([str(x) for x in row])
print("rho =", mp.nstr(rho, 30))
print("q(c=a=1) =", mp.nstr(q, 30))
print("factor =", mp.nstr(factor, 30))
print("compound-Poisson global density ceiling =", mp.nstr(bound, 30))
print("3sqrt(2) =", mp.nstr(C0, 30))
print("strict gap =", mp.nstr(C0-bound, 30))
