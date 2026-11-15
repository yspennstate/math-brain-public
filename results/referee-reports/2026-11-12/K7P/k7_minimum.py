"""Test and audit the orthogonal minimum-potential refinement exactly."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import time,json,random,resource
from fractions import Fraction as Q
from q1_core import exact,solve,serialize
from q2_search import partitions,correction,random_w,fork,split_leaf,log
start=time.monotonic();rng=random.Random(117027);best={};count=0
def rec(key,val,data):
    if key not in best or val>Q(best[key]['value']):
        best[key]=serialize(dict(value=val,**data))
        with open('k7_minimum_results.json','w') as f:json.dump(dict(best=best,checks=count),f,indent=2)
        if val>1 and not key.startswith('max_'):
            log(f'Orthogonal minimum test rejects sufficient bound {key}: {float(val):.15g}; exact witness saved.')

seq=[]
for n in (6,7,8):
    for t in (10,1000):
        w=fork(1,t)
        while len(w)<n:w=split_leaf(w,2)
        seq.append(('fork',w))
    for k in range(20):seq.append(('random',random_w(n,rng)))
with open('q2_obstacle_results.json') as f:z=json.load(f)['nonparallel_singleton']
seq.append(('obstacle',[[Q(v) for v in row] for row in z['w']]))
for source,w in seq:
    n=len(w);x=exact(w);F=x['F'];T=x['t'];ti=list(map(max,F));pi=x['pi'];W=x['W']
    L=[[sum(w[i][k] for k in range(n) if k!=i) if i==j else -w[i][j] for j in range(n)] for i in range(n)]
    def energy(a,b):return sum(a[i]*sum(L[i][j]*b[j] for j in range(n)) for i in range(n))
    for bs in partitions(n,n-2):
        h=correction(F,bs);ss=[(k,b[0]) for k,b in enumerate(bs) if len(b)==1]
        dif=[(a,b[0]) for b in bs for a in b[1:]]
        V=[[F[i][a]-F[i][b] for a,b in dif] for i in range(n)]
        S=[[V[a][k]-V[b][k] for k in range(2)] for a,b in dif]
        qs={i:[sum(a*b for a,b in zip(v,solve(S,[-u for u in V[i]]))) for v in V] for _,i in ss}
        for p,i in ss:
            for q,j in ss:
                if j<=i:continue
                cross=h[p][q]-F[i][j]
                if cross<=0:continue
                vals=[];negvals=[];data=[]
                for ii,jj in ((i,j),(j,i)):
                    ai=qs[ii][ii];lam=cross/ai;gamma=[a-lam*b for a,b in zip(qs[jj],qs[ii])]
                    k=[ti[jj]-F[jj][a]-gamma[a] for a in range(n)]
                    g=[lam*(ti[ii]-F[ii][a]) for a in range(n)]
                    m=list(map(min,g,k));mean=sum(a*b for a,b in zip(pi,m))
                    error=-(1+1/lam)*mean/T
                    neg=(1+1/lam)*sum(a*max(0,-b) for a,b in zip(pi,k))/T
                    bound=ti[ii]+ti[jj]-(1+1/lam)*mean
                    assert h[p][q]<=bound
                    assert gamma[ii]==0
                    assert all((g[b[0]]-k[b[0]])==(g[a]-k[a]) for b in bs for a in b)
                    assert all((m[b[0]]-k[b[0]])==(m[a]-k[a]) for b in bs for a in b)
                    # Full energy audits on the first 1000 orientations, then exact final bound throughout.
                    if count<1000:
                        assert energy(gamma,m)==0
                        assert energy(gamma,k)==0
                        assert energy(m,m)>=lam*lam*W*ai
                        assert energy([a-b for a,b in zip(g,m)],[a-b for a,b in zip(k,m)])<=0
                    vals.append(error);negvals.append(neg)
                    data.append(dict(i=ii,j=jj,lambda_=lam,gamma=gamma,k=k,m=m,mean=mean,bound=bound,error=error,negative_part_bound=neg))
                    count+=1
                common=dict(source=source,w=w,partition=bs,T=T,ti=ti[i],tj=ti[j],Fij=F[i][j],Fhat=h[p][q],orientations=data)
                rec('max_error',max(vals),common);rec('max_negative_part',max(negvals),common)
                rec('max_best_orientation_error',min(vals),common)
                rec('max_best_orientation_negative_part',min(negvals),common)
                if min(vals)>1:rec('both_orientations_error_exceeds_1',min(vals),common)
                if min(negvals)>1:rec('both_orientations_negative_part_exceeds_1',min(negvals),common)
    if time.monotonic()-start>170:break
with open('k7_minimum_results.json','w') as f:json.dump(dict(best=best,checks=count,seconds=time.monotonic()-start,peak_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),f,indent=2)
for key,z in best.items():print(key,float(Q(z['value'])),flush=True)
log(f'Orthogonal minimum refinement audit passed: {count} orientations, {time.monotonic()-start:.3f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes. This audits a conditional inequality, not factor 3.')
