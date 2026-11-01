import math
import numpy as np

rng=np.random.default_rng(20260923)

def trial(p,q,r,s):
    A=rng.normal(size=(p,r)); B=rng.normal(size=(p,s))
    C=rng.normal(size=(q,r)); D=rng.normal(size=(q,s))
    aa=np.linalg.norm(A); bb=np.linalg.norm(B); cc=np.linalg.norm(C); dd=np.linalg.norm(D)
    Om=0.0
    for i in range(p):
      for k in range(q):
       for j in range(r):
        for l in range(s):
         Om+=(A[i,j]*D[k,l]-B[i,l]*C[k,j])**2
    T=np.sum(B*(A@C.T@D))
    rhs=aa*aa*dd*dd+bb*bb*cc*cc-2*T
    assert abs(Om-rhs) <= 1e-9*(1+Om)
    assert Om+1e-10 >= (aa*dd-bb*cc)**2
    if aa>1e-12:
      vals=[]
      for i in range(p):
       for j in range(r):
        if abs(A[i,j])>1e-12:
         vals.append(np.linalg.norm(D-np.outer(C[:,j],B[i,:])/A[i,j])**2)
      assert min(vals) <= Om/(aa*aa)+1e-8
    if dd>1e-12:
      vals=[]
      for k in range(q):
       for l in range(s):
        if abs(D[k,l])>1e-12:
         vals.append(np.linalg.norm(A-np.outer(B[:,l],C[k,:])/D[k,l])**2)
      assert min(vals) <= Om/(dd*dd)+1e-8
    if bb>1e-12:
      vals=[]
      for i in range(p):
       for l in range(s):
        if abs(B[i,l])>1e-12:
         vals.append(np.linalg.norm(C-np.outer(D[:,l],A[i,:])/B[i,l])**2)
      assert min(vals) <= Om/(bb*bb)+1e-8
    if cc>1e-12:
      vals=[]
      for k in range(q):
       for j in range(r):
        if abs(C[k,j])>1e-12:
         vals.append(np.linalg.norm(B-np.outer(A[:,j],D[k,:])/C[k,j])**2)
      assert min(vals) <= Om/(cc*cc)+1e-8

count=0
for p in range(1,5):
 for q in range(1,5):
  for r in range(1,5):
   for s in range(1,5):
    for _ in range(8):
     trial(p,q,r,s); count+=1

K=1.076074733e6
beta=math.sqrt(63)/16
r0=16*math.sqrt(beta/4617)
h=(2*math.sqrt(2)-1)/1572864
ratio=K*r0*r0
det_ratio=ratio/8
omega_ratio=det_ratio**2
minor_count=math.floor(1024*omega_ratio)+1
assert abs(r0-0.1658498913771345)<1e-15
assert ratio>29598.7122613
assert det_ratio>3699.83903266
assert minor_count==14017340281
print(f'matrix_trials={count}')
print(f'r0={r0:.16g}')
print(f'P_over_h2={ratio:.12f}')
print(f'sqrtOmega_over_h2={det_ratio:.12f}')
print(f'min_nonzero_minor_count={minor_count}')
print('STATUS=PASS')
