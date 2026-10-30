import math

# Algebraic checks for fleet01/B03 r12. These are regression checks,
# not substitutes for the analytic proof in REPORT.md.

def general_constant(s,q,theta,gamma,D):
    Lq=math.pi*math.e*math.sqrt(2.0/q)
    return (2*math.gamma(1-s)*math.sin(math.pi*s/2)/(math.pi*s)
            *theta/(theta-2*q*s)*(Lq/(2*gamma))**s
            *D**(-s/(2*theta)))

def half_constant(q,theta,gamma,D):
    return (2**(5/4)*math.sqrt(math.e)*q**(-1/4)*gamma**(-1/2)
            *theta/(theta-q)*D**(-1/(4*theta)))

for q in (1.0,1.2,1.8):
    theta=1.7*q
    gamma=.73
    D=5.2
    a=general_constant(.5,q,theta,gamma,D)
    b=half_constant(q,theta,gamma,D)
    assert abs(a-b) <= 1e-12*max(1,abs(a),abs(b))

rank2=2**(9/4)*math.sqrt(math.e)
assert abs(rank2-7.842684263091678) < 1e-12

coef=(2**(5/4)*math.sqrt(math.e)*3*(3**.25)*16**(-1/6))
assert abs(coef-9.75325637240399) < 1e-12

worst=0.0
for m in range(3,1001):
    a=(m+1)//2
    b=m//2
    sigma=math.sqrt(a*b)/m
    assert sigma+1e-15 >= math.sqrt(2)/3
    kappa=.75
    theta=2*kappa
    max_diag=kappa/a
    D=(1+3)**2
    assert theta>1 and max_diag<=.5 and D==16
    bound=coef/math.sqrt(sigma)
    worst=max(worst,bound)
assert abs(worst-14.205377148462466) < 1e-12

partner_m2=16*math.sqrt(2)*math.sqrt(2)
assert abs(partner_m2-32.0) < 1e-12

# Rotated-cube slice: for z in (0,1/2), V(z)=8 z^3/3 and
# p_Z(z)=V(z), so conditional sup=1/V(z) diverges.
for z in (.25,.1,.01):
    V=8*z**3/3
    cond=1/V
    assert abs(V*cond-1)<1e-12
assert 3/(8*(1e-3)**3) > 1e8

print('QFORM_B03_FRACTIONAL_RIDGE_PASS')
print('rank2_constant',rank2)
print('hard_family_coefficient',coef)
print('hard_family_m_ge_3_uniform',worst)
print('hard_family_m2_partner',partner_m2)
