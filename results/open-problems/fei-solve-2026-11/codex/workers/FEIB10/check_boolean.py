"""Exhaust all 65536 four-bit Boolean functions, plus seeded six-bit cases."""
import json, time
from pathlib import Path
import numpy as np
from common import tables,fwht

def run(n,F):
    pc,z,rows,fac,meta=tables(n); m=1<<n
    hat=fwht(F)/m; mu=hat**2; up=np.einsum('bu,ru->br',mu,z,optimize=False)
    worst={'C':0.,'C_sharp':0.,'size_norm43':0.,'norm_support':0.,'p_granularity':0.,'mean_granularity':0.,'up_parseval':0.,'derivative_square_l1':0.,'derivative_level1':0.,'square_fourier':0.}
    stats={}; rbest=0.; best=None
    for r in range(m):
        # Inverse transform of the derivative Fourier coefficients on complement.
        comp=np.array([v for v in range(m) if not (v&r)])
        g=fwht(hat[:,comp|r])
        p=np.mean(g!=0,axis=1); ug=np.mean(g*g,axis=1)
        norm=np.mean(np.abs(g)**(4/3),axis=1)**1.5
        worst['up_parseval']=max(worst['up_parseval'],float(np.max(np.abs(up[:,r]-ug))))
        worst['norm_support']=max(worst['norm_support'],float(np.max(norm-ug*np.sqrt(p))))
        if r:
            delta=2.**(1-pc[r])
            worst['p_granularity']=max(worst['p_granularity'],float(np.max(delta*delta*p-ug)))
            worst['mean_granularity']=max(worst['mean_granularity'],float(np.max(np.sqrt(mu[:,r])-ug/delta)))
            for k in range(n-pc[r]+1):
                cols=((np.arange(m)&r)==r)&(pc<=pc[r]+k)
                left=mu[:,cols].sum(axis=1)
                rhs=3.**k*2.**pc[r]*ug**1.5
                worst['C']=max(worst['C'],float(np.max(left-rhs)))
                worst['C_sharp']=max(worst['C_sharp'],float(np.max(left-rhs/2)))
                worst['size_norm43']=max(worst['size_norm43'],float(np.max(left-3.**k*norm)))
        # |g|<=1 => ||g^2||_2^2<=||g||_2^2; independently computed in truth values.
        worst['derivative_square_l1']=max(worst['derivative_square_l1'],float(np.max(np.mean(g**4,axis=1)-ug)))
        # Fourier coefficients of g^2, independently of the original spectral coefficients.
        c=fwht(g*g)/len(comp)
        worst['square_fourier']=max(worst['square_fourier'],float(np.max(np.sum(c*c,axis=1)-ug)))
        ir=np.einsum('bu,u->b',mu[:,comp|r],pc[comp],optimize=False)
        lev=np.zeros(len(F))
        for v in comp:
            if not v: continue
            kids=[r|(1<<i) for i in range(n) if (v>>i)&1]
            mn=np.min(up[:,kids],axis=1)
            use=mu[:,r|v]>0
            lev[use]+=mu[use,r|v]*np.log2(1/mn[use])
        K=4*np.log2(3)+4/(3*np.e*np.log(2))
        bound=K*ir+8*(pc[r]+1)*(up[:,r]-mu[:,r])
        worst['derivative_level1']=max(worst['derivative_level1'],float(np.max(lev-bound)))
    logs=np.zeros_like(up); np.log2(up,out=logs,where=up>0)
    A=-(mu*logs).sum(axis=1); I=np.einsum('bu,u->b',mu,pc,optimize=False)
    ratios=np.divide(A,I,out=np.zeros_like(A),where=I>0)
    j=int(np.argmax(ratios))
    return worst,float(ratios[j]),F[j].astype(int).tolist()

def main():
    start=time.time(); results=[]
    for n in (4,6):
        rng=np.random.default_rng(10010)
        if n==4:
            batches=[1-2*((np.arange(lo,min(lo+1024,65536))[:,None]>>np.arange(16))&1) for lo in range(0,65536,1024)]
            count=65536
        else:
            F=1-2*rng.integers(0,2,(2048,64))
            q=rng.uniform(.01,.5,(2048,1))
            biased=1-2*(rng.random((2048,64))<q)
            structured=[]
            for mask in range(64):
                structured.append([(-1)**((x&mask).bit_count()) for x in range(64)])
            for t in range(1,65):
                structured.append([1-2*(x<t) for x in range(64)])
            structured.extend([[1-2*(x.bit_count()>=t) for x in range(64)] for t in range(8)])
            whole=np.vstack((F,biased,structured)); count=len(whole)
            batches=[whole[i:i+512] for i in range(0,count,512)]
        worst={}; best=-1.; witness=None
        for F in batches:
            w,b,f=run(n,F)
            for k,v in w.items(): worst[k]=max(worst.get(k,0.),v)
            if b>best: best=b; witness=f
        results.append({'n':n,'functions':count,'worst':worst,'max_A_I':best,'witness_truth_values':witness})
        print(json.dumps(results[-1]),flush=True)
    out={'results':results,'seconds':time.time()-start,'seed':10010}
    Path('boolean_output.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__': main()
