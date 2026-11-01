from fractions import Fraction
import math

tau = Fraction(1, 8192)
eps = math.sqrt(float(tau + tau*tau))
c = 0.5*math.sqrt(3/5)
beta = (3/16)*math.sqrt(3/5)
h = 5/8
C_Dprime = 6*math.sqrt(math.e)*(2*h)**(-0.5)*(3-4*h)**(-1)/beta
C_Dprime_simplified = 128*math.sqrt(math.e/3)

gate36 = float(tau) + 35*eps
gate37 = float(tau) + 36*eps
assert gate36 < c < gate37
assert abs(C_Dprime-C_Dprime_simplified) < 1e-12

m = 32768
assert 3/m < float(tau)
assert 18/m**2 < float(tau)
assert 3/(2*m) < 1/48

for k in (0,1,2):
    p = [Fraction(9,10)]*k + [Fraction(1,5)]*(3-k)
    plus = [Fraction(1,1)]*3
    minus = [2*x-1 for x in p]
    child = p
    cross = [1-x for x in p]
    assert sum(abs(float(x)) >= 1 for x in plus+minus) == 3
    assert sum(float(x) >= c for x in child) == k
    assert sum(float(x) >= beta for x in cross) == 3-k

incident_effective_count = (beta/eps)**6/108
assert incident_effective_count > 47758

print("QFORM_B08_ACTUAL_SPECTRAL_GATE_CHECK_PASS")
print(f"tau={float(tau):.15g}")
print(f"eps_tau={eps:.15g}")
print(f"c={c:.15g}")
print(f"beta={beta:.15g}")
print(f"gate36={gate36:.15g}")
print(f"gate37={gate37:.15g}")
print(f"Dprime_bound={C_Dprime:.15g}")
print(f"incident_effective_count_lower={incident_effective_count:.15g}")
for k in (0,1,2):
    product=(0.8**k)*(0.6**(3-k))
    C=6*product**(-1/6)
    print(f"k={k} theoremF_bound={C:.15g}")
print(f"m={m} entry_bound={3/m:.15g} det2_bound={18/m**2:.15g} selected_leverage={3/(2*m):.15g}")
