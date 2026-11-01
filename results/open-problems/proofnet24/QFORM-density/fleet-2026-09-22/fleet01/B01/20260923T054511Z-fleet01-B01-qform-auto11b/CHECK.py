import math
import sympy as sp

M = sp.symbols('M', positive=True)
v = sp.Matrix([sp.Rational(1,2)]*4)
w = sp.Matrix([sp.Rational(1,2), sp.Rational(1,2), -sp.Rational(1,2), -sp.Rational(1,2)])
A = sp.eye(4) - (M+1)*(v*v.T) - sp.Rational(3,2)*(w*w.T)
S = [0,1]
K = [2,3]
B = A.extract(S,S)
C = sp.simplify(A.extract(K,K) - A.extract(K,S)*B.inv()*A.extract(S,K))
D = sp.factor(-B.det())
F = sp.factor(2*C[0,1]**2)
W2 = sp.factor(D**2*F)
assert sp.simplify(D - (2*M+1)/4) == 0
assert sp.simplify(C[0,1] + (4*M+1)/(2*(2*M+1))) == 0
assert sp.simplify(F - (4*M+1)**2/(2*(2*M+1)**2)) == 0
assert sp.simplify(W2 - (4*M+1)**2/32) == 0

beta = 0.25
C1 = math.sqrt(2.0)
den = beta*(1-2*beta)*math.gamma(beta)*math.cos(math.pi*beta/2)
C_BL = math.exp(beta/2)*(2*math.pi)**beta/den
C_H = (math.pi*C1)**beta * 2**(beta/2)/den
assert C_BL > C_H
C_off = 2**beta*C_BL
C_pair = 3*2**(4/3)*C_off**(2/3)

def spike_bound(m):
    Dm=(2*m+1)/4
    kappa=min(1.0,Dm)
    W=(4*m+1)**2/32
    return C_pair*(Dm*kappa)**(-1/6)*W**(-1/12)

print('D =', D)
print('C_34 =', sp.factor(C[0,1]))
print('F =', F)
print('W2 =', W2)
print('C_BL =', repr(C_BL))
print('C_H =', repr(C_H))
print('C_off =', repr(C_off))
print('C_pair =', repr(C_pair))
print('spike_bound_M_down_to_1 =', repr(spike_bound(1.0)))
print('partner_F_min_m_ge_3 = 4')
print('partner_H14_bound =', repr(C_off*4**(-1/8)))
print('STATUS=PASS')
