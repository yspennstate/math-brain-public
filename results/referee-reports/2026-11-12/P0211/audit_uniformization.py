"""Adaptive uniformization of the count generator, with tracked lost mass.

Each step evaluates a positive Poisson series for a principal killed
subgenerator. Removing an upper tail or omitting Poisson terms loses
mass, so 1-sum(q) tracks truncation error (apart from roundoff).
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import signal,time,json,math
signal.alarm(280)
import numpy as np
from scipy.special import gammaln,logsumexp

def evolve(n,b,q,times):
    t=0.;answers=[];steps=0;terms=0
    for target in times:
        while target-t>1e-12:
            # Drop at most 1e-17 mass and keep 80 additional birth states.
            cumulative=np.cumsum(q[::-1]);drop=int(np.searchsorted(cumulative,1e-17,side='right'))
            core=len(q)-drop
            M=min(n,core+80)
            q=np.pad(q[:core],(0,M-core))
            k=np.arange(1,M+1,dtype=float);up=b*(n-k)/n;down=k*(k-1)/n
            rate=float(max(up+down));dt=min(target-t,20/rate);mean=rate*dt
            stay=1-(up+down)/rate;birth=up[:-1]/rate;death=down[1:]/rate
            vector=q.copy();weight=math.exp(-mean);acc=weight*vector
            j=0
            while True:
                j+=1
                nxt=stay*vector
                nxt[1:]+=birth*vector[:-1];nxt[:-1]+=death*vector[1:]
                vector=nxt;weight*=mean/j;acc+=weight*vector
                if j>mean and weight<1e-20:break
            q=acc;t+=dt;steps+=1;terms+=j
        answers.append((q.copy(),1-float(sum(q))))
    return answers,steps,terms

start=time.monotonic();rows=[];diagnostics=[];baseline=json.load(open('step5.json'))
for b in (.5,2.):
    for n in (100,400,1600,6400):
        k=np.arange(1,n+1,dtype=float)
        lp=gammaln(n+1)-gammaln(k+1)-gammaln(n-k+1)+k*math.log(b)-gammaln(k)
        p=np.exp(lp-logsumexp(lp));tn=math.sqrt(n)*math.log(n)/(8*math.sqrt(b))
        cs=(-4,-2,-1,0,1,2,4);valid=[(c,tn+c*math.sqrt(n)) for c in cs if tn+c*math.sqrt(n)>=0]
        for endpoint in (1,n):
            q=np.zeros(endpoint);q[-1]=1
            answers,steps,terms=evolve(n,b,q,[t for c,t in valid])
            maxerror=0.;maxloss=0.
            for (c,t),(q,loss) in zip(valid,answers):
                full=np.pad(q,(0,n-len(q)));tv=.5*sum(abs(full-p))
                base=next(x['tv'] for x in baseline if (x['b'],x['n'],x['start'],x['c'])==(b,n,endpoint,c))
                err=abs(float(tv)-base);maxerror=max(maxerror,err);maxloss=max(maxloss,abs(loss))
                assert err<1e-7 and abs(loss)<1e-8 and min(q)>=0
                rows.append(dict(b=b,n=n,start=endpoint,c=c,time=t,tv=float(tv),lost_mass=loss,BDF_error=err))
            for c in cs:
                t=tn+c*math.sqrt(n)
                if t<0:rows.append(dict(b=b,n=n,start=endpoint,c=c,time=t,tv=None,lost_mass=None,BDF_error=None))
            diagnostics.append(dict(b=b,n=n,start=endpoint,steps=steps,poisson_terms=terms,max_BDF_error=maxerror,max_mass_defect=maxloss))
            print(diagnostics[-1],flush=True)
result=dict(rows=rows,diagnostics=diagnostics,max_TV_difference_from_BDF=max(x['max_BDF_error'] for x in diagnostics),max_mass_defect=max(x['max_mass_defect'] for x in diagnostics),elapsed_seconds=time.monotonic()-start)
with open('step5_uniformization.json','w') as f:json.dump(result,f,indent=2)
print({key:val for key,val in result.items() if key not in ('rows','diagnostics')})
