# Independent check of T090's constant J = sum_n (1/n) (int_0^{1/3} x^{n-1}/(1+x) dx)^2
# and the claimed coefficient J/(16 pi^2) in (0.00053090572038263670, ...671). an agent, 15 Nov.
from mpmath import mp, mpf, quad, pi, nsum, inf, polylog
mp.dps = 40
a = mpf(1) / 3

def I(n):
    # direct quadrature, independent of the report's series
    return quad(lambda x: x ** (n - 1) / (1 + x), [0, a])

# terms decay like a^(2n)/n^3, so 60 terms reach far below 1e-30
J = sum(I(n) ** 2 / n for n in range(1, 61))
c = J / (16 * pi ** 2)
print("J            =", mp.nstr(J, 25))
print("J/(16 pi^2)  =", mp.nstr(c, 25))
print("in report bracket:", mpf("0.00053090572038263670") < c < mpf("0.00053090572038263671"))
D = polylog(2, mpf(1) / 4)
rel = (J + D ** 2 / 2) / (16 * pi ** 2)
print("relative b^4 coeff =", mp.nstr(rel, 16), "(report 0.0007577319825377)")
