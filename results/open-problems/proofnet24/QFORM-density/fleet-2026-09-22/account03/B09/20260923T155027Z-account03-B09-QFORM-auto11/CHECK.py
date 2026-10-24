import math
import numpy as np

Cd = 12*2**(-1/6)*math.e**0.25
Cc = 4*2**(5/8)*math.e**0.25
Cdirect = 4*math.sqrt(2)*math.e**0.25
print('Cd', repr(Cd))
print('Cc', repr(Cc))
print('Cdirect', repr(Cdirect))
print('Cc*2^-1/8', repr(Cc*2**(-1/8)))
assert Cd < 13.728
assert Cc < 7.921
assert abs(Cc*2**(-1/8)-Cdirect) < 1e-12

for eps in [0.0,1e-6,1e-3,1e-2,1e-1]:
    A=np.zeros((6,6))
    A[:2,:2]=np.array([[1.,1.],[1.,1.+eps]])
    A[0,3]=A[3,0]=1.
    A[1,4]=A[4,1]=1.
    A[2,5]=A[5,2]=1.
    vals=np.linalg.eigvalsh(A)
    large=sum(abs(v)>=1-1e-12 for v in vals)
    print('eps',eps,'spectrum',np.array2string(vals,precision=12),'large>=1',large)
    assert large>=3

# exact geometric regression for the residual after pivoting coordinate 0
mi=np.array([1.,0.,0.])
mj=np.array([0.,1.,0.])
mk=np.array([0.,0.,1.])
alpha=1.
beta=1.
cj=mj-beta*mi
ck=mk
Delta=np.linalg.det(np.array([[mi@mi,mi@mj],[mj@mi,mj@mj]]))
V=np.linalg.det(np.array([[mi@mi,mi@mj,mi@mk],[mj@mi,mj@mj,mj@mk],[mk@mi,mk@mj,mk@mk]]))
Z2=np.linalg.det(np.array([[cj@cj,cj@ck],[ck@cj,ck@ck]]))
print('Delta',Delta,'V',V,'||cj||',np.linalg.norm(cj),'Z2',Z2)
assert abs(Delta-1)<1e-12 and abs(V-1)<1e-12 and abs(Z2-2)<1e-12
assert Z2 + 1e-12 >= (cj@cj/Delta)*V
print('regression_bound',Cdirect*2**(-1/8))
print('partner_bound',3.0)
print('ALL CHECKS PASSED')
