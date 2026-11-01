from fractions import Fraction
from math import sqrt, pi
import numpy as np

Delta=Fraction(1,64)
assert Delta/Fraction(16,1)==Fraction(1,1024)
assert abs(sqrt(float(Delta/16))-1/32)<1e-15

R=np.array([[1.,0.,0.],
            [0.,1/sqrt(2),0.],
            [0.,1/sqrt(2),0.],
            [0.,0.,1.]])
M=np.diag([1.,1.,-1.])
assert np.allclose(R.T@R,np.eye(3))
w={}
for i in range(4):
    for j in range(i+1,4):
        w[(i,j)]=np.linalg.norm(np.cross(R[i],R[j]))**2
assert abs(sum(w.values())-3)<1e-12
ordered=sum(w[e]*w[f] for e in w for f in w if set(e).isdisjoint(f))
assert abs(ordered/9-1/9)<1e-12
S=[0,1]; T=[2,3]
Gs=R[S].T@R[S]; Gt=R[T].T@R[T]
assert np.allclose(Gs+Gt,np.eye(3))
Ast=R[S]@M@R[T].T
assert np.linalg.matrix_rank(Ast,tol=1e-12)==1
A=R@M@R.T
ev=np.linalg.eigvalsh(A)
assert np.allclose(ev,[-1,0,1,1],atol=1e-12)

r=7/8
H=(4/3)*np.array([[1,r,r],[r,1,-r],[r,-r,1]],float)
hev=np.linalg.eigvalsh(H)
assert np.allclose(hev,[-1,2.5,2.5],atol=1e-12)

print('QFORM_B11_R28_TWO_BANK_CHECK_PASS')
print('delta_threshold_middle_sq=1/1024')
print('delta_threshold_sigma2=1/32')
print('rank_collapse_Delta=1/9')
print('rank_collapse_cross_rank=1')
print('rank_collapse_spectrum=',ev.tolist())
print('partner_target_spectrum=',hev.tolist())
print('partner_eta_1_8_constant=',6*sqrt(pi))
print('grouped_same_sign_control_constant=',pi*sqrt(2))
