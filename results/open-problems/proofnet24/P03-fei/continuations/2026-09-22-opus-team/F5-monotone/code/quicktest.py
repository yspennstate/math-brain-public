import numpy as np, time
from ltf_core import *
# Maj3
H,I,f,c = ltf_HI([1,1,1],0.0); print("Maj3",H,I)
# AND_n: f=+1 iff all x_i=+1 : sum w x > n-1
for n in [2,3,5,10,20]:
    t=time.time(); H,I,f,c = ltf_HI(np.ones(n), n-1.0); print("AND",n,H,I,H/I, time.time()-t)
# restriction step sanity: compare with direct restriction
w=np.array([3.,2,2,1,1,1]); th=0.5
H,I,f,c=ltf_HI(w,th)
for i in range(6):
    dH,JS,sp,inf = restriction_step(c,6,i)
    # direct
    b=1<<i; idx0=[x for x in range(64) if not x&b]; idx1=[x|b for x in idx0]
    f0=f[idx0]; f1=f[idx1]
    H0,I0=HI(spectrum(f0)); H1,I1=HI(spectrum(f1))
    print(i, dH, H-(H0+H1)/2, inf, influences(f,6)[i], JS, sp)
t=time.time(); H,I,f,c=ltf_HI(np.ones(23),0.0); print("Maj23",H,I,H/I,time.time()-t)
