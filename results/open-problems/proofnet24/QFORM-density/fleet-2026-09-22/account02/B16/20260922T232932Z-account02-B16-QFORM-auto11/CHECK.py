import math
import numpy as np
import sympy as sp

beta, alpha, delta, gamma = sp.symbols('beta alpha delta gamma', nonzero=True, real=True)
B = sp.Matrix([[0,beta,0],[beta,alpha,delta],[0,delta,gamma]])
assert sp.factor(B.det()) == -beta**2*gamma

C3 = 16*math.sqrt(30)*2**0.25
print('C3=',repr(C3))
print('null_constant=',repr(3*(2*math.e)**(2/3)))
print('support_le_5=',repr(C3*10**(1/3)))
print('four_line_bank=',repr(2*C3*4**(1/3)))
print('nonnull_eta_1_16=',repr(16*math.sqrt(30)*2))

for m in [3,4,5,8,17]:
    th=2*np.pi*np.arange(m)/m
    rows=[np.array([1.0,0.0,0.0])]
    rows += [np.array([0.0,math.sqrt(2/m)*math.cos(t),math.sqrt(2/m)*math.sin(t)]) for t in th]
    R=np.vstack(rows)
    resid=np.linalg.norm(R.T@R-np.eye(3),ord=np.inf)
    print('m=',m,'parseval_residual=',repr(float(resid)))
    assert resid < 1e-12
print('STATUS=PASS')
