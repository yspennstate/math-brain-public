# transverse drift at the rank-one stratum near e1: Phi = (tr V - V11)/V11, drift of log Phi per |W|^2 (attention noise only = large-scale limit)
import numpy as np
from gen import bdrift, noise_basis
rng=np.random.default_rng(21)
for m in (3,4,6):
    P=np.eye(m)-1.0/m
    for g2 in (0.5,1.0):
        out=[]
        for _ in range(400):
            eta=1e-7
            L=np.zeros((m,m)); L[0,0]=1.0
            L[1:,:]=np.sqrt(eta)*rng.standard_normal((m-1,m))*np.exp(rng.uniform(-1,1,(m-1,1)))
            V=L@L.T+1e-30*np.eye(m)
            b=bdrift(V,g2); E=noise_basis(V,g2,att=True,lin=False)
            l=np.trace(V)-V[0,0]; a=V[0,0]
            dl=np.trace(b)-b[0,0]; da=b[0,0]
            ql=sum((np.trace(Ej)-Ej[0,0])**2 for Ej in E); qa=sum(Ej[0,0]**2 for Ej in E)
            dr=dl/l-da/a-0.5*ql/l**2+0.5*qa/a**2
            W=P@V@P; out.append(dr/np.sum(W*W))
        out=np.array(out)
        print("m %d g2 %.1f: drift(log Phi)/|W|^2 at Phi~1e-7: min %+.4f med %+.4f max %+.4f"%(m,g2,out.min(),np.median(out),out.max()),flush=True)
