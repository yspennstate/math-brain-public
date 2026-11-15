"""Matrix-exponential action by inverse-Laplace (Talbot) resolvents.

Uses only complex tridiagonal solves, independent of the BDF evolution.
The inverse Laplace transform of (zI-Q^T)^(-1) is exp(t Q^T).
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import signal,time,json,math
signal.alarm(280)
import numpy as np
from scipy.linalg import solve_banded,expm
from scipy.special import gammaln,logsumexp

def action(up,down,t,M):
    n=len(up);rhs=np.zeros((n,2),complex);rhs[0,0]=1;rhs[-1,1]=1
    r=2*M/5;result=np.zeros((n,2),complex)
    for j in range(M):
        if j==0:delta=r;weight=.5
        else:
            theta=j*math.pi/M;cot=1/math.tan(theta)
            delta=r*theta*(cot+1j)
            weight=1+1j*theta*(1+cot*cot)-1j*cot
        band=np.zeros((3,n),complex)
        band[0,1:]=-down[1:];band[1,:]=delta/t+up+down;band[2,:-1]=-up[:-1]
        resolvent=solve_banded((1,1),band,rhs,check_finite=False)
        result+=np.exp(delta)*weight*resolvent
    return (2/(5*t))*result.real

start=time.monotonic();baseline=json.load(open('step5.json'));rows=[];errors=[];masses=[];negative=[];quaderrors=[];denseerrors=[]
for b in (.5,2.):
    for n in (100,400,1600,6400):
        k=np.arange(1,n+1,dtype=float);up=b*(n-k)/n;down=k*(k-1)/n
        lp=gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)+k*math.log(b)-gammaln(k)
        p=np.exp(lp-logsumexp(lp));tn=math.sqrt(n)*math.log(n)/(8*math.sqrt(b))
        for c in (-4,-2,-1,0,1,2,4):
            t=tn+c*math.sqrt(n)
            if t<0:
                for endpoint in (1,n):rows.append(dict(b=b,n=n,start=endpoint,c=c,time=t,tv=None))
                continue
            q24=action(up,down,t,24);q32=action(up,down,t,32)
            quaderrors.append(float(np.max(np.sum(abs(q24-q32),axis=0))))
            masses.append(float(max(abs(q24.sum(axis=0)-1))));negative.append(float(np.min(q24)))
            tv=.5*np.sum(abs(q24-p[:,None]),axis=0)
            for j,endpoint in enumerate((1,n)):
                base=next(x['tv'] for x in baseline if (x['b'],x['n'],x['start'],x['c'])==(b,n,endpoint,c))
                errors.append(abs(float(tv[j])-base))
                rows.append(dict(b=b,n=n,start=endpoint,c=c,time=t,tv=float(tv[j]),BDF_error=abs(float(tv[j])-base)))
print('diagnostics',max(errors),max(quaderrors),max(masses),min(negative))
print('worst_rows',sorted([x for x in rows if x.get('BDF_error') is not None],key=lambda x:x['BDF_error'],reverse=True)[:4])
assert max(errors)<1e-7
assert max(quaderrors)<1e-7
assert max(masses)<1e-7
assert min(negative)>-1e-8
result=dict(rows=rows,max_TV_difference_from_BDF=max(errors),max_L1_quadrature_difference=max(quaderrors),max_mass_error=max(masses),min_probability=min(negative),elapsed_seconds=time.monotonic()-start)
with open('step5_exponential.json','w') as f:json.dump(result,f,indent=2)
print({k:v for k,v in result.items() if k!='rows'})
