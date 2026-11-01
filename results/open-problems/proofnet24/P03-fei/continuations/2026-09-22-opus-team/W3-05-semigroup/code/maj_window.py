"""(P') for majority at large n via the closed-form level spectrum (all influences equal I/n)."""
import math, numpy as np
from fei_core import lowprio
from majority_tilt import maj_levels
lowprio()
out=[]
for (b,c) in [(2.0,1.0),(0.0,0.0),(1.0,0.0)]:
    out.append("# b=%g c=%g : n, sup_{t in [0,1]} a*(t), argmax t"%(b,c))
    for n in [21,51,101,301,1001,3001,10001,30001,100001]:
        ks,lw,lc,W = maj_levels(n)
        I=float((W*ks).sum()); li=math.log(n/I)
        best=-1e300; tb=None
        for t in np.concatenate([np.linspace(0,0.02,41),np.linspace(0.02,1,99)]):
            dec=W*np.exp(-2*t*ks)
            G=float((ks*dec*(-lw)).sum()); M=float((ks**2*dec).sum()); N=float((ks*dec).sum()); Kr=N*li
            v=(G-b*Kr-c*N)/(math.exp(2*t)*M)
            if v>best: best,tb=v,t
        out.append("%7d %.5f %.4f"%(n,best,tb))
txt='\n'.join(out); print(txt)
open('../logs/maj_window.log','w').write(txt+'\n')
