import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import math,json,time,resource,sys
from pathlib import Path
import numpy as np
from experiments import calc,row,save,signs,KEYS
def phi(a,b):
    def e(x):return x*np.log2(np.maximum(x,1e-300))
    return e(a+b)-e(a)-e(b)
def cardinality():
    rows=[];neg=0;masserr=0;cross=0;start=time.time()
    for w in [2,3,4,6,8,12,16]:
        delta=2.**(1-w);q=delta**2;c=(1-delta)**2
        K=np.array([c]+[math.comb(w,k)*q for k in range(1,w+1)])
        A=np.array([c]+[math.comb(w-1,k)*q for k in range(1,w)])
        B=np.array([math.comb(w-1,k)*q for k in range(w)])
        trueE=float(phi(A,B).sum()/delta)
        for s in [1,8,64,512,4096]:
            length=(s-1)*w+1;fftlen=1<<((length+w-2).bit_length())
            Z=np.fft.irfft(np.fft.rfft(K,fftlen)**(s-1),fftlen)[:length];neg=max(neg,-float(Z.min()));masserr=max(masserr,abs(float(Z.sum())-1));Z=np.maximum(Z,0);Z/=Z.sum()
            a=np.convolve(Z,A);b=np.convolve(Z,B);val=float(phi(a,b).sum()/delta)
            if s<=8:
                exact=np.array([1.])
                for j in range(s-1):exact=np.convolve(exact,K)
                cross=max(cross,abs(val-float(phi(np.convolve(exact,A),np.convolve(exact,B)).sum()/delta)))
            rows.append(dict(w=w,s=s,n=w*s,I=s*w*delta,true_Hm_over_I=trueE,size_witness_over_I=val,limit=(-(delta*math.log2(delta)+(1-delta)*math.log2(1-delta)))/delta))
    z=dict(rows=rows,negative_mass_clipped_max=neg,normalization_residual=masserr,small_positive_convolution_ratio_residual=cross,elapsed_seconds=time.time()-start,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)
    assert neg<1e-10 and masserr<1e-9 and cross<1e-8
    Path('cardinality_dilution.json').write_text(json.dumps(z,indent=2)+'\n');print('CARDINALITY PASS',neg,masserr,cross)
def majority():
    rows=[];start=time.time()
    for n in [3,5,9,17,33,65,129,257,513,1025,2049,4097]:
        # Independent exact coefficient recurrence in logarithmic representation.
        logs=np.full(n+1,-np.inf);logs[1]=math.lgamma(n)-2*math.lgamma((n+1)/2)-(n-1)*math.log(2)
        for k in range(1,n-1,2):logs[k+2]=logs[k]+math.log(k)-math.log(n-k-1)
        # Normalize once to remove accumulated lgamma error, preserving zero even levels.
        lb=np.array([math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1) for k in range(n+1)])
        W=np.exp(lb+2*logs);W/=W.sum();delta=float(np.sum(np.arange(n+1)*W)/n)
        mu=W*np.exp(-lb);A=1-delta;B=delta;best=float('inf');br=None
        for r in range(n):
            top=n-1-r;k=np.arange(top+1);lbc=np.array([math.lgamma(top+1)-math.lgamma(int(j)+1)-math.lgamma(top-int(j)+1) for j in k])
            aa=float(np.sum(np.exp(lbc-lb[:top+1])*W[:top+1]));bb=float(np.sum(np.exp(lbc-lb[1:top+2])*W[1:top+2]))
            val=float(phi(aa,bb)+phi(max(A-aa,0),max(B-bb,0)))/delta
            if val<best:best=val;br=r
        rows.append(dict(n=n,I=n*delta,Hm_over_I=0,parity_witness_over_I=0,size_witness_over_I=0,best_meets_over_I=best,best_block_size=br))
        print('majority',n,best,br,flush=True)
    Path('majority_meets.json').write_text(json.dumps(dict(rows=rows,elapsed_seconds=time.time()-start),indent=2)+'\n')
def families():
    rows=[]
    for n in range(2,15):
        X=signs(n);f=np.ones(1<<n,dtype=np.int8);f[0]=-1
        rows.append(row(f,f'AND_{n}',1 if n<=10 else 3))
        if n%2:rows.append(row(np.where(X.sum(axis=1)>=0,1,-1),f'MAJ_{n}',1 if n<=10 else 3))
    for w in range(2,5):
        for s in range(2,11//w+1):
            n=w*s;t=np.arange(1<<n);f=np.ones(1<<n,dtype=np.int8)
            for j in range(s):f[((t>>(j*w))&((1<<w)-1))==0]=-1
            rows.append(row(f,f'tribes_{w}x{s}'))
    # AND of majority blocks and OR of parity blocks require different information.
    for w,s in [(3,2),(3,3),(5,2)]:
        n=w*s;X=signs(n);f=np.ones(1<<n,dtype=np.int8)
        for j in range(s):f=np.minimum(f,np.where(X[:,j*w:(j+1)*w].sum(axis=1)>0,1,-1))
        rows.append(row(f,f'AND_MAJ_{w}x{s}'))
    save('families',rows)
def symmetric_audit():
    # FEIB02 exact finite-difference core, read-only import; never write its __pycache__.
    sys.dont_write_bytecode=True;sys.path.insert(0,'../FEIB02');from symmetric import integer_data
    rng=np.random.default_rng(141431);zs=json.loads(Path('symmetric.json').read_text());errors=[];truth=[]
    for z in zs:
        n=z['n']
        for key,maskkey in [('Hm_over_I','value_mask'),('half_norm_over_I','half_norm_mask'),('parity_over_I','parity_mask')]:
            mask=int(z[maskkey],16);f=[1]+[-1 if mask>>(t-1)&1 else 1 for t in range(1,n+1)];D=integer_data(f);F=[a[0] for a in D]
            I=sum(k*math.comb(n,k)*F[k]**2 for k in range(n+1));A=[math.comb(n-1,k)*F[k]**2 for k in range(n)];B=[math.comb(n-1,k)*F[k+1]**2 for k in range(n)]
            if key=='Hm_over_I':val=n*sum(math.comb(n-1,k)*float(phi(float(F[k]**2),float(F[k+1]**2))) for k in range(n))/I
            elif key=='half_norm_over_I':val=n*sum(math.comb(n-1,k)*abs(F[k]*F[k+1]) for k in range(n))/I
            else:val=n*sum(float(phi(float(sum(A[p::2])),float(sum(B[p::2])))) for p in [0,1])/I
            errors.append(abs(val-z[key]))
        if n<=10:
            mask=int(z['value_mask'],16);v=[1]+[-1 if mask>>(t-1)&1 else 1 for t in range(1,n+1)];f=np.array([v[x.bit_count()] for x in range(1<<n)],dtype=np.int8);o,_=calc(f,0);errors.append(abs(o['Hm']/o['I']-z['Hm_over_I']));truth.append(row(f,f'symmetric_extreme_{n}',0))
    # All representative vectors through dimension 12, independent finite differences.
    census=[]
    for n in range(1,13):
        best=-1;bm=0
        for mask in range(1,1<<n):
            v=[1]+[-1 if mask>>(t-1)&1 else 1 for t in range(1,n+1)];D=integer_data(v);F=[a[0] for a in D];I=sum(k*math.comb(n,k)*F[k]**2 for k in range(n+1));E=n*sum(math.comb(n-1,k)*float(phi(float(F[k]**2),float(F[k+1]**2))) for k in range(n));r=E/I
            if r>best:best=r;bm=mask
        errors.append(abs(best-zs[n-1]['Hm_over_I']));census.append(dict(n=n,best=best,mask=hex(bm)))
    assert max(errors)<1e-9
    Path('symmetric_audit.json').write_text(json.dumps(dict(maximum_ratio_residual=max(errors),independent_census=census,truth_tables=truth,seed=141431),indent=2)+'\n');print('SYMMETRIC AUDIT PASS',max(errors))
if __name__=='__main__':
    globals()[sys.argv[1]]()
