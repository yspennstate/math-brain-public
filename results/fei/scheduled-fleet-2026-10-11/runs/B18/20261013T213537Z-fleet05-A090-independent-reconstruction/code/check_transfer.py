from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import json, time

start=time.perf_counter(); checks=cases=0
def check(v):
    global checks
    assert v
    checks+=1
def fwht(values):
    a=list(values); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for i in range(j,j+step):
                u,v=a[i],a[i+step]; a[i],a[i+step]=u+v,u-v
        step*=2
    return [F(x,len(a)) for x in a]
def put(d,x,c):
    if c and x!=1:
        d[x]=d.get(x,F(0))+c
        if not d[x]:del d[x]
def merge(d,e,c=F(1)):
    for x,y in e.items():put(d,x,c*y)
def phi(x,y):
    d={}
    if x and y:
        put(d,(x+y)/x,x);put(d,(x+y)/y,y)
    return d
def edge(a,n):
    p=[v*v for v in a]; allB={}; individual=[]; higher={}; highind=[]
    for i in range(n):
        d={};hd={}
        for t in range(len(a)):
            if t&(1<<i):continue
            ph=phi(p[t],p[t|(1<<i)])
            merge(d,ph)
            if t.bit_count()>=2:merge(hd,ph)
        merge(allB,d);merge(higher,hd);individual.append(d);highind.append(hd)
    return allB,individual,higher,highind
def influence(a,n):
    return [sum((a[s]*a[s] for s in range(len(a)) if s&(1<<i)),F(0)) for i in range(n)]

seeds=[(n,mask) for n in [0,1,2] for mask in range(2**(2**n))]
seeds += [(3,mask) for mask in [1,7,105,150]]
for n,mask in seeds:
    truth=[-1 if mask&(1<<x) else 1 for x in range(2**n)]
    ah=fwht(truth);mu=ah[0]; Is=sum(influence(ah,n),F(0)); Bs=edge(ah,n)[0]
    for m in [1,2]:
        for c in [1,2]:
            dim=m*n+c
            core=[]
            for x in range(2**dim):
                v=(-1)**((x>>(m*n)).bit_count())
                for b in range(m):v*=truth[(x>>(b*n))%(2**n)]
                core.append(v)
            ac=fwht(core); Bc=edge(ac,dim)[0]
            want={};merge(want,Bs,F(m));check(Bc==want)
            check(ac[0]==0)
            if c==2:check(all(ac[1<<i]==0 for i in range(dim)))
            check(sum(influence(ac,dim),F(0))==m*Is+c)
            for k in [1,2,3]:
                cases+=1;q=F(1,2**k);N=dim+k
                vals=[core[x%(2**dim)] if x>>dim==0 else 1 for x in range(2**N)]
                a=fwht(vals);check(sum(v*v for v in a)==1)
                B,bi,R,ri=edge(a,N); inf=influence(a,N)
                check(sum(inf)==q*(m*Is+c+k))
                check(all(t==q for t in inf[dim:]))
                data={};higherdata={};remainder={}
                for i in range(dim):merge(data,bi[i]);merge(higherdata,ri[i])
                for i in range(dim,N):merge(remainder,ri[i])
                expected={};merge(expected,Bc,q)
                for i in range(dim):
                    merge(expected,phi(F(1),ac[1<<i]**2),q*(1-q))
                    merge(expected,phi((1-q)**2,q*q*ac[1<<i]**2))
                check(data==expected)
                ct={};put(ct,F(2),2*q*(1-q));merge(ct,phi((1-q)**2,q*q))
                for i in range(dim,N):check(bi[i]==ct)
                if c==2:
                    target={};merge(target,Bs,q*m)
                    check(data==target);check(higherdata==target)
                    total={};merge(total,target);merge(total,remainder)
                    check(R==total)
                    for i in range(m*n,dim):
                        check(bi[i]=={});check(inf[i]==q)
                    b0={};t12={}
                    for i in range(N):
                        merge(b0,phi(a[0]**2,a[1<<i]**2))
                        for j in range(N):
                            if j!=i:merge(t12,phi(a[1<<j]**2,a[(1<<i)|(1<<j)]**2))
                    rootwant={};merge(rootwant,phi((1-q)**2,q*q),F(k))
                    pairwant={};put(pairwant,F(2),2*k*(k-1)*q*q)
                    check(b0==rootwant);check(t12==pairwant)
                    rwant={};merge(rwant,target);put(rwant,F(2),2*k*q*(1-k*q))
                    check(R==rwant)
                else:
                    # Fresh balancing coordinate has seed mean to the mth power.
                    bal={};merge(bal,phi(F(1),mu**(2*m)),q*(1-q))
                    merge(bal,phi((1-q)**2,q*q*mu**(2*m)))
                    check(bi[m*n]==bal);check(inf[m*n]==q)
                check(time.perf_counter()-start<60)
out={'status':'PASS','helper_version':'A090-parity-activation-v2','assertions':checks,'seed_count':len(seeds),'activation_cases':cases,'max_dimension':11,'arithmetic':'Fraction integer Walsh; formal logarithm dictionaries, exact identities only','elapsed_seconds':time.perf_counter()-start,'one_parity_extra_rows':'nonempty pure-control packets explicitly retained','two_parity_result':'all seed erasure transported into R_ge2; both relevant fresh parity coordinates have zero erasure','exact_R_ge2':'q*m*B(seed)+2*k*q*(1-k*q)'}
(Path(__file__).resolve().parents[1]/'out'/'CHECK.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
