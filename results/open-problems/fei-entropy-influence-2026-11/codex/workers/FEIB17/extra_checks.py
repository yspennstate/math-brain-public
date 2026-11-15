import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,math
from audit import calc,truth,make_bank,h
from pathlib import Path
out={}
for n in [4,6,7,8]:
    errab=errsq=0.;count=0
    chunks=[truth(np.arange(s,s+1024,dtype=np.uint64),4) for s in range(0,65536,1024)] if n==4 else [make_bank(n,128,17500+n)]
    for f in chunks:
        c=calc(f)['c'];B,N=f.shape;M=N//2;ids=np.arange(M)
        for i in range(n):
            a=c.reshape(B,-1,2,1<<i)[:,:,0,:].reshape(B,-1);b=c.reshape(B,-1,2,1<<i)[:,:,1,:].reshape(B,-1)
            for s in range(M):
                ab=(a*b[:,ids^s]).sum(1);ss=(a*a[:,ids^s]+b*b[:,ids^s]).sum(1)
                errab=max(errab,float(abs(ab).max()));errsq=max(errsq,float(abs(ss-(1 if s==0 else 0)).max()))
        count+=B
    out['convolution'+str(n)]=dict(functions=count,ab_residual=errab,squares_residual=errsq)
# Check exact formulas for small structured functions.
rows=[]
for w,s in [(2,2),(2,3),(2,4),(3,2),(4,2)]:
    n=w*s;ids=np.arange(1<<n);bits=((ids[:,None]>>np.arange(n))&1).reshape(-1,s,w);f=np.where(bits.all(2).any(1),-1.,1.);o=calc(f[None,:]);beta=2.**(-w);q=1-beta;delta=2*beta*q**(s-1);eta=2*beta*delta;mu0=(2*q**s-1)**2;r=(q/beta)**2;F=(1+r)*float(h(1/(1+r)));top=delta*delta;pair=(mu0+top)*float(h(top/(mu0+top)));exact=2*(delta-eta)+(eta-top)*F+pair
    rows.append(dict(w=w,s=s,I=float(o['I'][0]),E_i=float(o['E'][0,0]),pair_formula=exact,residual=abs(exact-o['E'][0,0])))
out['tribes_pair_formula']=rows
# Actual complex truth-table transform and restrictions at n=4,6,7,8.
rows=[]
for n in [4,6,7,8]:
    p=.03125;ids=np.arange(1<<n);x=1-2*((ids[:,None]>>np.arange(n))&1);f=np.prod(math.sqrt(1-p)+1j*math.sqrt(p)*x,axis=1)
    c=f.copy();step=1
    while step<len(c):
        v=c.reshape(-1,2,step);a=v[:,0,:].copy();b=v[:,1,:].copy();v[:,0,:]=a+b;v[:,1,:]=a-b;step*=2
    mu=abs(c/(1<<n))**2;H=float((-mu*np.log2(mu)).sum());I=float(sum(j.bit_count()*mu[j] for j in range(1<<n)))
    rows.append(dict(n=n,p=p,modulus_error=float(abs(abs(f)-1).max()),entropy_residual=abs(H-n*float(h(p))),influence_residual=abs(I-n*p)))
out['complex_direct']=rows
Path('extra_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
