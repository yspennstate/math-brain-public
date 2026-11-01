#!/usr/bin/env python3
from fractions import Fraction


def B(m,S):
    return Fraction(2*m, S+m)

d = Fraction(792_665_992, 1_000_000_000)
lo = d - Fraction(1, 2_000_000_000)
hi = d + Fraction(1, 2_000_000_000)

def admissible_ms(S):
    lower = lo*S/(2-lo)
    upper = hi*S/(2-hi)
    mmin = (lower.numerator + lower.denominator - 1)//lower.denominator
    mmax = (upper.numerator - 1)//upper.denominator
    return list(range(mmin,mmax+1)), lower, upper

print('R17 lower-endpoint artifact reconstruction')
for S in (2**24,2**25,25_000_000):
    ms, lower, upper = admissible_ms(S)
    print(f'S={S}: admissible integer min_changes = {ms}')
    for m in ms:
        val=B(m,S)
        print('  m =',m)
        print('  exact B =',val)
        print('  B-d =',val-d)
    if not ms:
        center=d*S/(2-d)
        q=center.numerator//center.denominator
        print('  no exact integer in nine-decimal rounding cell')
        for m in (q,q+1):
            print('  neighbor',m,'B =',B(m,S),'B-d =',B(m,S)-d)

ms24,_,_=admissible_ms(2**24)
ms25,_,_=admissible_ms(2**25)
assert ms24 == [11_014_954]
assert ms25 == [22_029_908]
exact_power2=B(ms24[0],2**24)
assert exact_power2 == B(ms25[0],2**25)
assert exact_power2 == Fraction(11_014_954,13_896_085)
assert exact_power2 < d
power2_gap=d-exact_power2
assert power2_gap == Fraction(36_033,347_402_125_000_000)

ms25m,_,_=admissible_ms(25_000_000)
assert ms25m == []
center=d*25_000_000/(2-d)
q=center.numerator//center.denominator
assert q == 16_413_560
left=B(q,25_000_000)
right=B(q+1,25_000_000)
assert left < d < right
print('\nPower-of-two conditional reconstruction exact bound =',exact_power2)
print('Claimed decimal minus exact conditional bound =',power2_gap)
print('S=25,000,000 bracketing candidates:',q,left,q+1,right)

for g in (Fraction(3,5),Fraction(4,5),Fraction(9,10)):
    alpha=1-Fraction(1,2)/g
    bar=Fraction(1,2)/g
    assert alpha < Fraction(1,2) < bar
print('\nEntropy specialization algebra: K=2,qx=qy=1/2,H=2 => 2 <= 2 h(gamma)+gamma')
print('ALL_EXACT_CHECKS_PASS')
