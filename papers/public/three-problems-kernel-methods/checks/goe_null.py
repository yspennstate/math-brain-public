# Null for (L-b): d * E Tr(U^4) for U a Frobenius-normalised GOE matrix (uniform direction in Sym_d)
import numpy as np, time, sys
rng=np.random.default_rng(20260916)
N=200000
for d in (20,30,40):
    t=time.time(); vals=np.empty(N)
    B=2000
    for i in range(0,N,B):
        G=rng.standard_normal((B,d,d)); G=(G+np.swapaxes(G,1,2))/np.sqrt(2)
        fro2=np.einsum('bij,bij->b',G,G)
        G2=np.einsum('bij,bjk->bik',G,G)
        tr4=np.einsum('bij,bij->b',G2,G2)
        vals[i:i+B]=d*tr4/fro2**2
    print(f"d={d} N={N} d*E Tr(U^4) = {vals.mean():.4f} +- {vals.std(ddof=1)/np.sqrt(N):.4f}  [{time.time()-t:.0f}s]", flush=True)
