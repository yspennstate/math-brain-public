# transverse drift of log Phi per unit u at lam e1 e1^T (attention noise only), worst direction over random transverse blocks
import numpy as np
from trans_gen2 import dr
rng=np.random.default_rng(8); s=1e-4
for m in (3,4,5,6,8):
    row=[]
    for g2 in (0.25,0.5,0.75,0.8,0.9,1.0):
        vals=[]
        for _ in range(60):
            L=np.zeros((m,m)); L[0,0]=1.0
            Q=rng.standard_normal((m-1,m-1)); L[1:,1:]=s*Q   # purely transverse (no e1 component)
            vals.append(dr(L+1e-14*np.eye(m),g2,m))
        row.append("g2 %.2f %+.3f..%+.3f"%(g2,min(vals),max(vals)))
    print("m",m,"|"," | ".join(row),flush=True)
