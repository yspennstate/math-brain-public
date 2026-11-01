import sympy as s
from itertools import combinations
R=s.Rational
K=s.Matrix([[R(1,10),R(1,20),R(1,25)],[R(1,20),R(2,5),R(2,25)],[R(1,25),R(2,25),R(7,10)]])
p=[]
for mask in range(8):
 N=K-s.diag(*[0 if mask&(1<<i) else 1 for i in range(3)])
 p.append(s.factor((-1)**(3-mask.bit_count())*N.det()))
ratio=s.factor(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
print('K',K,'p',p,'ratio',ratio,'ratio-1',s.factor(ratio-1))
print('minors',[[J[:i,:i].det() for i in (1,2,3)] for J in [K,s.eye(3)-K]])
