from fractions import Fraction
from math import isqrt

D = 10**12

def invsqrt_upper(n: int) -> Fraction:
    # least integer a with a^2 n >= D^2, so a/D >= 1/sqrt(n)
    a = isqrt(D*D // n)
    while a*a*n < D*D:
        a += 1
    while a > 0 and (a-1)*(a-1)*n >= D*D:
        a -= 1
    assert a*a*n >= D*D
    return Fraction(a, D)

max_ratio = Fraction(0)
max_k = None
for K in range(1,64):
    qK = invsqrt_upper(K)
    S = Fraction(0)
    for r in range(1,K):
        qr = invsqrt_upper(r)
        aa = qK + Fraction(4,9)*qr
        S += (K-r)*aa**3
    ratio = S/Fraction(K)
    assert ratio <= Fraction(26,25), (K, ratio)
    if ratio > max_ratio:
        max_ratio, max_k = ratio, K

large = Fraction(1,16)+Fraction(1,3)+Fraction(52,135)+Fraction(56,243)
assert large == Fraction(19663,19440)
assert large < Fraction(26,25)
final_constant = Fraction(2197,27) + 648*Fraction(26,25)
assert final_constant == Fraction(509821,675)
assert final_constant < 756

print('max_K_1_63 =', max_k)
print('max_exact_upper_ratio =', max_ratio)
print('max_decimal <', float(max_ratio))
print('large_K_bound =', large, '< 26/25 =', Fraction(26,25))
print('final_constant =', final_constant, '< 756')
print('ALL_EXACT_CHECKS_PASS')
