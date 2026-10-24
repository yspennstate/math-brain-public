from decimal import Decimal, getcontext
getcontext().prec = 90

C = Decimal('6.5218512')
THREAT = Decimal('3.846028304990334e-7')

# Rigorous upper endpoints for R_t and exact/lower-safe influences from peer certificates.
F = [
    ('F1', Decimal(68013) / Decimal(32768),
     Decimal('6.521850083658612443633672199029299526203969335')),
    ('F2', Decimal(784028312243315011737) / Decimal(295147905179352825856),
     Decimal('6.5218507635184635316691901626179398857683143881788648')),
    ('F3', Decimal(7293635508681408439604535567475568379907630049888658770829188246173012479808017893097) /
           Decimal(1942668892225729070919461906823518906642406839052139521251812409738904285205208498176),
     Decimal('6.5218509158557171794342597335463471829453334335276482')),
    ('F4', Decimal('8.9891831269165525119469526862195470748936495017444294'),
     Decimal('6.5218509485644448965496895824490791318643557898359042')),
]

rows = []
for name, I, R_hi in F:
    lower_defect = (I - 1) * (C - R_hi)
    assert C > R_hi
    assert lower_defect > THREAT
    rows.append((name, I, R_hi, lower_defect, lower_defect / THREAT))

# Tail theorem: for all t >= 5, R_t < R_infty_hi and I_t >= I5 > 200.
RINF_HI = Decimal('6.521850949550450153644489106618467838753558803161')
TAIL_DEFECT = Decimal(199) * (C - RINF_HI)  # strict lower bound because I_t - 1 > 199
assert TAIL_DEFECT > THREAT

# Balanced self-composition preserves R and raises I, so its absolute defect only increases.
minimum = min(row[3] for row in rows)
assert minimum == rows[1][3]  # F2 is the finite-stage minimum among F1..F4
assert minimum > THREAT

print('PASS')
print('C* =', C)
print('heterogeneous threat ceiling =', THREAT)
for name, I, R_hi, d, ratio in rows:
    print(name, 'I=', I, 'R_upper=', R_hi)
    print('  rigorous Delta_lower =', d)
    print('  Delta_lower / threat =', ratio)
print('t>=5 rigorous Delta_lower >', TAIL_DEFECT)
print('t>=5 ratio >', TAIL_DEFECT/THREAT)
print('uniform all-stage lower bound from F1..F4 =', minimum)
print('uniform factor over threat =', minimum/THREAT)
print('Self-composition closure: Delta(F_t^{circ d}) >= Delta(F_t) for every integer d>=1.')
