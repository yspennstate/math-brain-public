from fractions import Fraction
import math
import sympy as sp

# Exact trace-three contraction example: K=H diag(9/10,4/5,7/10,3/5) H^T.
H = sp.Matrix([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]])/2
D = sp.diag(sp.Rational(9,10), sp.Rational(4,5), sp.Rational(7,10), sp.Rational(3,5))
K = sp.simplify(H*D*H.T)
P=[0,1]; R=[2,3]
Kpp=K.extract(P,P); Kpr=K.extract(P,R); Krp=K.extract(R,P); Krr=K.extract(R,R)
S=sp.simplify(Krr-Krp*Kpp.inv()*Kpr)
g=sp.factor(Kpp.det())
M1=sp.factor(sum(K.extract(P+[k],P+[k]).det() for k in R))
M2=sp.factor(K.det())
assert sp.trace(K)==3
assert sp.factor(M1-g*sp.trace(S))==0
assert sp.factor(M2-g*S.det())==0
assert sp.trace(S)>=1

# Sharpened bounded-cardinality determinant-law constant.
tau=33/16
beta=1-math.exp(-tau)-math.exp(4-tau)*(tau/4)**4
c_new=beta/16
c_old=(31/64-math.exp(-1))/16
assert beta>0 and c_new>c_old

print('K=', K)
print('g=', g)
print('S=', S)
print('trS=', sp.factor(sp.trace(S)))
print('M1=', M1, 'g*trS=', sp.factor(g*sp.trace(S)))
print('M2=', M2, 'g*detS=', sp.factor(g*S.det()))
print('beta_star=', repr(beta))
print('c_new=', repr(c_new))
print('c_old=', repr(c_old))
print('improvement_factor=', repr(c_new/c_old))
print('rank1_partner_O0_bound=', repr(3*math.e*256**(1/6)))
print('STATUS=QFORM_PAIR_SCHUR_HIERARCHY_CHECK_PASS')
