"""Exact adversarial singleton objectives, <=180 s per invocation, no workers.

Usage: python3 k7_search.py n [seconds]. Every objective uses Fraction.
"""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[k]='1'
import sys,time,json,random,math,resource
from fractions import Fraction as Q
from q1_core import exact,lump,solve,serialize
from q2_search import fork,random_w,correction,log

n=int(sys.argv[1]); budget=min(float(sys.argv[2]) if len(sys.argv)>2 else 160,180)
rng=random.Random(120711+n);start=time.monotonic();count=0;accepted=0
path=f'k7_search_{n}_results.json'; records={}; summary=[]
with open('q2_obstacle_results.json') as f:ob=json.load(f)['nonparallel_singleton']

def fast(w):
    """Grounded exact inverse via n-1 solves; independent final audit uses exact()."""
    d=list(map(sum,w));W=sum(d);root=max(range(n),key=lambda i:d[i]);ix=[i for i in range(n) if i!=root]
    L=[[sum(w[i][k] for k in range(n) if k!=i) if i==j else -w[i][j] for j in ix] for i in ix]
    K=[[Q(0)]*n for _ in range(n)]
    # Gauss-Jordan inversion with a multi-column right-hand side.
    A=[L[k][:]+[Q(k==l) for l in range(n-1)] for k in range(n-1)]
    for k in range(n-1):
        pivot=next(j for j in range(k,n-1) if A[j][k]);A[k],A[pivot]=A[pivot],A[k]
        a=A[k][k];A[k]=[v/a for v in A[k]]
        for j in range(n-1):
            if j!=k and A[j][k]:
                a=A[j][k];A[j]=[v-a*u for v,u in zip(A[j],A[k])]
    for k,i in enumerate(ix):
        for l,j in enumerate(ix):K[i][j]=A[k][n-1+l]
    a=[sum(K[i][j]*d[j] for j in range(n)) for i in range(n)]
    mu=sum(a[i]*d[i] for i in range(n))/W
    return [[a[i]+a[j]-mu-W*K[i][j] for j in range(n)] for i in range(n)]

def assess(w,bs,obj):
    global count
    F=fast(w);h=correction(F,bs);T=max(map(max,F));ti=list(map(max,F));count+=1
    ss=[(k,b[0]) for k,b in enumerate(bs) if len(b)==1]
    vals=[((h[k][l] if obj=='ratio' else h[k][l]-ti[i]-ti[j])/T,i,j,k,l) for k,i in ss for l,j in ss if i<j]
    val,i,j,k,l=max(vals)
    return val,dict(i=i,j=j,T=T,ti=ti[i],tj=ti[j],Fij=F[i][j],Fhat=h[k][l],ratio=h[k][l]/T,excess=(h[k][l]-ti[i]-ti[j])/T)

def save(shape,obj,w,bs,val,data):
    key=shape+'_'+obj
    if key in records and val<=Q(records[key]['value']):return
    records[key]=serialize(dict(value=val,n=n,w=w,partition=bs,evaluation=count,**data))
    with open(path,'w') as f:json.dump(dict(best=records,summary=summary),f,indent=2)
    # Every new finding is durable immediately; full exact values are in JSON.
    log(f'Adversarial n={n}, {key}: exact incumbent {float(val):.15g}, evaluation {count}; witness in {path}.')
    if data['ratio']>3:raise RuntimeError('EXACT RATIO > 3; audit saved witness')

def initial(shape):
    bs=([[0,1,2]] if shape=='triple' else [[0,1],[2,3]])
    bs += [[i] for i in range(sum(map(len,bs)),n)]
    # Fork: relabel its intended merged pairs first.
    w=fork(1,10)
    while len(w)<n:
        from q2_search import split_leaf
        w=split_leaf(w,2)
    order=[1,3,2,4,0,5]+list(range(6,n))
    wf=[[w[i][j] for j in order] for i in order]
    wo=[[Q(v) for v in row] for row in ob['w']]
    if n==6:wo=[row[:6] for row in wo[:6]]
    while len(wo)<n:
        from q2_search import split_leaf
        wo=split_leaf(wo,2)
    # Preserve the best previously probed seed of the requested shape too.
    with open('k7_probe_results.json') as f:probe=json.load(f)
    zz=probe['ratio_'+shape];extra=[]
    wp=[[Q(v) for v in row] for row in zz['w']]
    if len(wp)==n:
        bp=zz['partition'];non=[b for b in bp if len(b)>1];single=[b for b in bp if len(b)==1]
        order=[i for b in non+single for i in b]
        extra.append([[wp[i][j] for j in order] for i in order])
    return bs,[wf,wo]+extra

for phase,(shape,obj) in enumerate((('pairs','ratio'),('pairs','excess'),('triple','ratio'),('triple','excess'))):
    bs,seeds=initial(shape);end=start+budget*(phase+1)/4;restart=0;phase_count=count
    # Include a very heavy-tailed exact fork baseline.
    if shape=='pairs':
        w=fork(1,10**6)
        while len(w)<n:
            from q2_search import split_leaf
            w=split_leaf(w,2)
        order=[1,3,2,4,0,5]+list(range(6,n));w=[[w[i][j] for j in order] for i in order]
        val,data=assess(w,bs,obj);save(shape,obj,w,bs,val,data)
    while time.monotonic()<end:
        if restart<len(seeds):w=[row[:] for row in seeds[restart]]
        elif restart%4==0:w=random_w(n,rng)
        else:
            key=shape+'_'+obj;w=[[Q(v) for v in row] for row in records[key]['w']]
            # Restore moderate powers so an asymptotically sharp seed doesn't lock the search.
            fac=rng.choice((Q(1,4),Q(1,2),Q(3,4)))
            w=[[Q(0) if not v else Q(10)**round(math.log10(float(v))*float(fac)) for v in row] for row in w]
        val,data=assess(w,bs,obj);save(shape,obj,w,bs,val,data)
        for step in range(120):
            if time.monotonic()>end:break
            v=[row[:] for row in w]
            for _ in range(1 if rng.random()<.85 else rng.randint(2,4)):
                i=rng.randrange(n);j=rng.randrange(n);old=v[i][j]
                if old and rng.random()<.96:
                    new=old*rng.choice((Q(1,100),Q(1,10),Q(1,2),Q(2),Q(10),Q(100)))
                    if i==j and rng.random()<.08:new=Q(0)
                else:
                    new=Q(10)**rng.randint(-8,12)*rng.choice((0,1,1,1,2,3))
                if new>Q(10)**50 or (new and new<Q(10)**-40):continue
                v[i][j]=v[j][i]=new
            try:a,data=assess(v,bs,obj)
            except (StopIteration,ZeroDivisionError):continue
            save(shape,obj,v,bs,a,data)
            temp=.08*(1-step/120)**2;delta=float(a-val)
            if a>=val or rng.random()<math.exp(max(-700,delta/max(temp,1e-8))):w=v;val=a;accepted+=1
        restart+=1
    summary.append(dict(shape=shape,objective=obj,evaluations=count-phase_count,restarts=restart))
    log(f'Adversarial phase n={n} {shape} {obj} finished; {count-phase_count} exact evaluations.')
with open(path,'w') as f:json.dump(dict(best=records,summary=summary,evaluations=count,seconds=time.monotonic()-start,peak_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),f,indent=2)
log(f'Adversarial n={n} complete: {count} exact evaluations, {accepted} accepted, {time.monotonic()-start:.3f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
