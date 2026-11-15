"""Exact adversarial test of the new sufficient orthogonal-minimum bound.
One process/thread, 110 seconds. No claim of global optimality.
"""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import time,json,random,math,resource,sys
from fractions import Fraction as Q
from q1_core import exact,solve,serialize
from q2_search import fork,split_leaf,random_w,log
start=time.monotonic();rng=random.Random(717144);n=7;best={};count=0
threshold=Q(sys.argv[1]) if len(sys.argv)>1 else Q(-1000000)
suffix='_above2' if threshold==2 else ''
result_path='k7_min_search'+suffix+'_results.json'
bs=[[0,1],[2,3],[4],[5],[6]]
def assess(w):
    global count
    x=exact(w);F=x['F'];T=x['t'];ti=list(map(max,F));pi=x['pi']
    V=[[row[0]-row[1],row[2]-row[3]] for row in F]
    S=[[V[0][0]-V[1][0],V[0][1]-V[1][1]],[V[2][0]-V[3][0],V[2][1]-V[3][1]]]
    qs={i:[sum(a*b for a,b in zip(v,solve(S,[-u for u in V[i]]))) for v in V] for i in (4,5,6)}
    ans=[]
    for i,j in ((4,5),(4,6),(5,6)):
        c=qs[i][j]
        if c<=0:continue
        if F[i][j]+c<threshold*T:continue
        vals=[];negs=[];details=[]
        for ii,jj in ((i,j),(j,i)):
            lam=c/qs[ii][ii]
            k=[ti[jj]-F[jj][a]-qs[jj][a]+lam*qs[ii][a] for a in range(n)]
            m=[min(lam*(ti[ii]-F[ii][a]),k[a]) for a in range(n)]
            err=-(1+1/lam)*sum(p*v for p,v in zip(pi,m))/T
            neg=(1+1/lam)*sum(p*max(0,-v) for p,v in zip(pi,k))/T
            vals.append(err);negs.append(neg);details.append(dict(i=ii,j=jj,lambda_=lam,error=err,negative=neg))
        ans.append((min(vals),dict(i=i,j=j,T=T,Fij=F[i][j],Fhat=F[i][j]+c,details=details,negative=min(negs))))
    count+=1
    return max(ans,key=lambda x:x[0]) if ans else (Q(-100),{})

inc=Q(-100);seedw=fork(1,10)
seedw=split_leaf(seedw,2);order=[1,3,2,4,0,5,6];seedw=[[seedw[i][j] for j in order] for i in order]
restart=0
while time.monotonic()-start<110:
    if restart==0:w=[row[:] for row in seedw]
    elif restart%3==0:w=random_w(n,rng)
    else:w=[[Q(v) for v in row] for row in best['w']]
    val,_=assess(w)
    for step in range(90):
        if time.monotonic()-start>110:break
        v=[row[:] for row in w];i=rng.randrange(n);j=rng.randrange(n)
        new=v[i][j]*rng.choice((Q(1,10),Q(1,2),Q(2),Q(10))) if v[i][j] else Q(10)**rng.randint(-5,9)
        if new>Q(10)**45 or (new and new<Q(10)**-35):continue
        v[i][j]=v[j][i]=new
        try:a,data=assess(v)
        except (StopIteration,ZeroDivisionError):continue
        if a>inc:
            inc=a;best=serialize(dict(value=a,w=v,partition=bs,evaluation=count,**data))
            with open(result_path,'w') as f:json.dump(best,f,indent=2)
            log(f'Orthogonal minimum adversary: best-orientation error {float(a):.15g}; exact witness saved.')
            if a>1:log('The proposed best-orientation mean bound FAILS exactly; this is a proof-method obstruction, not a factor-3 counterexample.')
        temp=.03*(1-step/90)**2
        if a>=val or rng.random()<math.exp(max(-700,float(a-val)/max(1e-8,temp))):w=v;val=a
    restart+=1
best.update(evaluations=count,seconds=time.monotonic()-start,peak_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
with open(result_path,'w') as f:json.dump(best,f,indent=2)
log(f'Orthogonal minimum adversary finished: {count} exact objectives, {time.monotonic()-start:.3f}s, best {float(inc):.15g}, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
