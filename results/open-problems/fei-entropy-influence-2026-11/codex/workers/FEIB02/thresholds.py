"""All thresholds in O(n^2) integer arithmetic per dimension.
Q_k(x)=(1+x)^(n-k) sum_s C(k-1,s)^2 x^s.
F_k(x)=(1+x)^(n-k)(1-x)^(k-1).
Array index r-1 corresponds to threshold at r, f_t=+1 iff t<r.
"""
import math,json,time,os,argparse
from pathlib import Path
for _thread_env in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:os.environ[_thread_env]='1'
import numpy as np
LN2=math.log(2)

def level0_ratios(n,cum,L):
    total=1<<n
    m=min(cum,total-cum)
    x=(2*m)/total
    xI=(2*m)/(n*L)
    if x==1: return 0.,0.
    # phi((1-x)^2)/x, preserving arbitrarily rare thresholds.
    factor=2/LN2 if x<1e-9 else -2*(1-x)**2*math.log1p(-x)/(x*LN2)
    return xI*factor,xI*factor/2

def all_thresholds(n):
    choose=[math.comb(n,k) for k in range(n+1)]
    base=[math.comb(n-1,r) for r in range(n)]
    L=[2*x for x in base]
    den=[(1<<n)*n*x for x in L]
    A=np.zeros(n);B=np.zeros(n);G=np.zeros(n)
    cum=0
    for j in range(n):
        cum+=choose[j]
        B[j],G[j]=level0_ratios(n,cum,L[j])
    frow=base[:];qrow=base[:];qprev=None
    for k in range(1,n+1):
        for j,F in enumerate(frow):
            if not F:continue
            F*=2;Q=qrow[j]
            wI=(choose[k]*F*F)/den[j]
            lf=math.log2(abs(F));lq=math.log2(Q)
            A[j]+=wI*(n+k-2-lq)
            B[j]+=wI*(lq+(n-k)+2-2*lf)
            G[j]+=wI*(math.log2(L[j])-lf)
        if k==n:break
        # Multiplication by (1-x)/(1+x), exactly.
        fnext=[0]*n
        for j in range(n):
            fnext[j]=frow[j]-(frow[j-1] if j else 0)-(fnext[j-1] if j else 0)
        # Legendre recurrence after clearing (1+x)^2.
        if k==1:qnext=qrow[:]
        else:
            qnext=[0]*n
            for j in range(n):
                v=(2*k-1)*(qrow[j]+(2*qrow[j-1] if j else 0)+(qrow[j-2] if j>1 else 0))
                v-=(k-1)*(qprev[j]-(2*qprev[j-1] if j else 0)+(qprev[j-2] if j>1 else 0))
                q,rem=divmod(v,k)
                if rem:raise ArithmeticError(('noninteger Q',n,k,j))
                qnext[j]=q-(2*qnext[j-1] if j else 0)-(qnext[j-2] if j>1 else 0)
                if qnext[j]<0:raise ArithmeticError(('negative Q',n,k,j))
        qprev,qrow=qrow,qnext;frow=fnext
    return {'A/I':A.tolist(),'B/I':B.tolist(),'Gamma/I':G.tolist()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--dimensions',type=int,nargs='+',default=[25,32,64,128,256,512,1000,1024,2000]);args=p.parse_args()
    for n in args.dimensions:
        out=Path(f'thresholds_{n:04d}.json')
        if out.exists():continue
        t=time.monotonic();vals=all_thresholds(n)
        row={'n':n,'family':'all thresholds r=1,...,n','ratios':vals,'wall_seconds':time.monotonic()-t,'maxima':{}}
        for name,v in vals.items():
            j=max(range(n),key=v.__getitem__)
            row['maxima'][name]={'value':v[j],'threshold':j+1}
        row['majority_or_nearest_threshold']={name:v[n//2] for name,v in vals.items()}
        out.write_text(json.dumps(row,indent=2)+'\n')
        print(n,row['wall_seconds'],row['maxima'],row['majority_or_nearest_threshold'],flush=True)
if __name__=='__main__':main()
