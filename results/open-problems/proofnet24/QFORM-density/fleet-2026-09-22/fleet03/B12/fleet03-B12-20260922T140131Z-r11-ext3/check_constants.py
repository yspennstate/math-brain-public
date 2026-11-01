import math

# Deterministic arithmetic checks for REPORT.md.

def beta(a,b):
    return math.gamma(a)*math.gamma(b)/math.gamma(a+b)

def K(m,q):
    assert m > 2*q
    return math.e/(2*m*math.sqrt(2*q))*beta(1/(2*m), 1/(4*q)-1/(2*m))

def delta(rho):
    return 0.5-math.sqrt(2*rho)-rho

rho3=(39-6*math.sqrt(30))/98
rho4=(2-math.sqrt(3))/4

# Boundary equations: q_min=2 rho/delta.
assert abs(2*rho3/delta(rho3)-1.5) < 1e-12
assert abs(2*rho4/delta(rho4)-2.0) < 1e-12

rho=1/16
d=delta(rho)
q=2*rho/d
assert q < 1.5
assert abs(d-(7-4*math.sqrt(2))/16) < 1e-15
assert abs(q-2/(7-4*math.sqrt(2))) < 1e-14

# m=3, q=1 aggregate exterior-power constant.
K31=K(3,1)
assert abs(K31-5.65576377338724) < 1e-12
rho32=1/32
d32=delta(rho32)
assert abs(d32-7/32) < 1e-15
C32=K31/d32
assert abs(C32-25.8549201069131) < 1e-11

# The sharper individual-three-singular-value gamma envelope at rho=1/16.
def individual_three(q):
    return (math.e*math.sqrt(math.pi)/(2*math.sqrt(2*q))
            * math.gamma(3/(4*q)-0.5)/math.gamma(3/(4*q)))
C_ind_16=individual_three(q)/d
assert 2562 < C_ind_16 < 2563

print('QFORM_EXT3_CHECK_PASS')
print('rho3_star=',repr(rho3))
print('rho4_star=',repr(rho4))
print('rho_1_16_delta=',repr(d))
print('rho_1_16_q=',repr(q))
print('K_3_1=',repr(K31))
print('C_rho_1_32_aggregate=',repr(C32))
print('C_rho_1_16_individual=',repr(C_ind_16))
