from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json,time
RUN=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0; cases=0; nonzero=0; constants_paid=0
def test(a,b):
    global assertions
    assertions+=1
    assert a==b,(a,b)
def logq(q):
    out=defaultdict(F)
    for v,sign in [(q.numerator,1),(q.denominator,-1)]:
        d=2
        while d*d<=v:
            while v%d==0: out[d]+=sign; v//=d
            d+=1
        if v>1: out[v]+=sign
    return dict(out)
def accumulate(out,q,weight):
    for p,c in logq(q).items(): out[p]+=weight*c
def clean(d):return {p:v for p,v in d.items() if v}
def entropy(p):
    out=defaultdict(F)
    for v in p.values():
        if v: accumulate(out,v,-v)
    return clean(out)
def ce(p,q):
    out=defaultdict(F)
    for a,v in p.items():
        if v: accumulate(out,q[a],-v)
    return clean(out)
def divergence(p,q):
    out=defaultdict(F)
    for a,v in p.items():
        if v: accumulate(out,v/q[a],v)
    return clean(out)
def lin(*terms):
    out=defaultdict(F)
    for weight,d in terms:
        for p,c in d.items():out[p]+=weight*c
    return clean(out)
def spectrum(values,labels):
    n=len(labels); N=1<<n; p={}
    for s in range(N):
        num=sum(value*(-1 if (x&s).bit_count()%2 else 1) for x,value in enumerate(values))
        if num:
            mask=sum(1<<labels[j] for j in range(n) if s>>j&1)
            p[mask]=F(num*num,N*N)
    test(sum(p.values()),F(1));return p
def construct(values,labels,cutoff,reference,history=()):
    p=spectrum(values,labels); n=len(labels)
    if n<=cutoff or len(set(values))==1:
        scale=F(1) if reference==0 else F(1,2 if sum(y for _,y in history)%2==0 else 4)
        q={s:scale*v for s,v in p.items()}
        jointp={(s,history):v for s,v in p.items()}
        jointq={(s,history):scale*v for s,v in p.items()}
        return p,q,jointp,jointq,ce(p,q),entropy(p),divergence(p,q),F(sum(s.bit_count()*v for s,v in p.items())),{},{}
    # Branch-dependent choice of fresh physical coordinate; directly evaluate its children.
    j=(sum(y for _,y in history)+len(history))%n; label=labels[j]
    child=[]
    for y in [0,1]:
        vals=[]
        for x in range(1<<(n-1)):
            old=(x&((1<<j)-1))|(y<<j)|((x>>j)<<(j+1))
            vals.append(values[old])
        child.append(construct(vals,labels[:j]+labels[j+1:],cutoff,reference,history+((label,y),)))
    marginal=defaultdict(F); r=defaultdict(F)
    for pp,qq,*_ in child:
        for t,v in pp.items(): marginal[t]+=v/2
        for t,v in qq.items(): r[t]+=v/2
    for t,v in marginal.items():test(v,sum(p.get(t|u,F(0)) for u in [0,1<<label]))
    jointp=defaultdict(F);jointq=defaultdict(F)
    for c in child:
        for (t,h),mass in c[2].items():
            for u in [0,1<<label]:
                theta=p.get(t|u,F(0))/marginal[t]
                if theta:jointp[t|u,h]+=mass*theta/2
        for (t,h),mass in c[3].items():
            for u in [0,1<<label]:
                theta=p.get(t|u,F(0))/marginal[t]
                if theta:jointq[t|u,h]+=mass*theta/2
    q=defaultdict(F)
    for (s,h),v in jointq.items():q[s]+=v
    for s,v in p.items(): test(v,sum(z for (t,h),z in jointp.items() if t==s))
    leafce=lin(*[(F(1,2),c[4]) for c in child]); leafh=lin(*[(F(1,2),c[5]) for c in child]); leafd=lin(*[(F(1,2),c[6]) for c in child]); leafi=sum(c[7]/2 for c in child)
    B=lin((F(1),entropy(p)),(F(-1),entropy(marginal)))
    J=lin((F(1),entropy(marginal)),*[(F(-1,2),entropy(c[0])) for c in child])
    Bsum=lin((F(1),B),*[(F(1,2),c[8]) for c in child]); Jsum=lin((F(1),J),*[(F(1,2),c[9]) for c in child])
    return p,dict(q),dict(jointp),dict(jointq),leafce,leafh,leafd,leafi,Bsum,Jsum
for n in range(4):
    for table in range(1<<(1<<n)):
        vals=[1 if table>>x&1 else -1 for x in range(1<<n)]
        for cutoff in [0,1,2]:
            for reference in [0,1]:
                p,q,jp,jq,leafce,leafh,leafd,leafi,B,J=construct(vals,list(range(n)),cutoff,reference)
                test(divergence(jp,jq),leafd)
                rootd=divergence(p,q)
                posterior=defaultdict(F)
                for (s,h),mass in jp.items():accumulate(posterior,(mass/p[s])/(jq[s,h]/q[s]),mass)
                K=clean(posterior)
                test(K,lin((F(1),leafd),(F(-1),rootd)))
                test(ce(p,q),lin((F(1),B),(F(1),J),(F(1),leafce),(F(-1),K)))
                test(entropy(p),lin((F(1),B),(F(1),J),(F(1),leafh)))
                test(lin((F(1),leafce),(F(-1),K)),lin((F(1),leafh),(F(1),rootd)))
                if K:nonzero+=1
                if reference==0:test(K,{});test(rootd,{});test(leafd,{})
                if not leafi and not leafce:test(K,{});constants_paid+=1
                cases+=1
                if time.perf_counter()-start>60:raise RuntimeError('Frozen runtime exceeded')
test(cases,1668)
out={'helper_version':'A098-global-likelihood-credit-reconstruction-v1','cases':cases,'assertions_passed':assertions,'failures':0,'nonzero_posterior_credit_cases':nonzero,'zero_cost_constant_terminal_cases':constants_paid,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction and symbolic log-prime coefficients','scope':'scaled actual leaf references; general theorem is the analytic global-likelihood argument'}
(RUN/'out/CREDIT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
