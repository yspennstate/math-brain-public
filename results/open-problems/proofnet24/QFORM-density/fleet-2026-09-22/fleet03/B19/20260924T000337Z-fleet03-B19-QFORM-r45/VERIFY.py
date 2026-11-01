import math
import numpy as np

rng=np.random.default_rng(20260924000337)
max_err=0.0
for _ in range(10000):
    n=8
    X=rng.normal(size=(n,n))
    A=(X+X.T)/2
    H=[0,1]; R=[2,3,4]; C=[5,6,7]
    B=A[np.ix_(H,H)]
    U=A[np.ix_(H,C)]
    V=A[np.ix_(R,H)]
    M=A[np.ix_(R,C)]
    adj=np.array([[B[1,1],-B[0,1]],[-B[1,0],B[0,0]]])
    K=np.linalg.det(B)*M-V@adj@U
    for ii,r in enumerate(R):
        for jj,c in enumerate(C):
            d=np.linalg.det(A[np.ix_(H+[r],H+[c])])
            scale=1+abs(d)+abs(K[ii,jj])
            max_err=max(max_err,abs(d-K[ii,jj])/scale)

viol=0
for _ in range(10000):
    s=np.sort(rng.random(20)*20)[::-1]
    F=np.linalg.norm(s)
    E2=0.5*((s@s)**2-np.sum(s**4))
    tail2=np.sum(s[1:]**2)
    if tail2>2*E2/F**2+1e-10:
        viol+=1

D0=3/4096
kappa=1/64
omega=1/144
strong=12.286*D0**(-3/10)*kappa**(-1/10)*omega**(-1/20)
Fmin=256/15
tail=5*math.sqrt(2)/128
s1=math.sqrt(Fmin**2-tail**2)
partner=34*math.sqrt(math.log(math.e*9216))

print('max normalized bordered determinant residual',max_err)
print('tail inequality violations',viol)
print('strong edge bound',strong)
print('Fmin',Fmin)
print('tailmax',tail)
print('s1 lower',s1)
print('partner bound',partner)
assert max_err<1e-12
assert viol==0
assert strong<209
assert partner<109
print('QFORM_B19_R45_CHECK_PASS')
