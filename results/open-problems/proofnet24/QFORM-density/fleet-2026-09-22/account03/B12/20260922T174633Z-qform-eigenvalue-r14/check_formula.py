import math

G = math.gamma(4.0/3.0)

def J(m):
    return (m**(2.0/3.0))*G*math.gamma(m)/math.gamma(m+1.0/3.0)

def M(m):
    return J(m)**3

print('gamma_4_3_cubed', G**3)
for m in [2,3,5,10,20,50,100]:
    jm = J(m)
    mm = M(m)
    lower = (G**3)*m
    assert mm + 1e-12 >= lower
    print(m, jm, mm, mm/m, lower)

# Physical-triple bound for the additional-eigenvalue family.
for m in [3,4,10,100]:
    for tau in [1.0,2.0,10.0]:
        a = tau - (tau-1.0)/m
        det_b3 = tau*tau*(tau - 3.0*(tau-1.0)/m)
        assert a >= 1.0 - 1e-12
        assert det_b3 >= tau*tau - 1e-12
        bound = 2.0*math.sqrt(math.pi)/(a*det_b3)**0.25
        assert bound <= 2.0*math.sqrt(math.pi)/math.sqrt(tau) + 1e-12
        print('triple', m, tau, a, det_b3, bound)

print('QFORM_CONDITIONAL_MOMENT_CHECK_PASS')
