from fractions import Fraction as Q
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json,time,hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter();checks=0
def ck(v):
    global checks
    assert v
    checks+=1
def cutoff():
    if time.perf_counter()-start>55:raise RuntimeError('Frozen internal 55-second cutoff reached; no automatic continuation')
def save(name,obj):
    (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return [Q(x,len(a)) for x in a]
def inf(a):
    n=(len(a)-1).bit_length()
    return [Q(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range(n)]

# Rational coefficient vectors of logarithms of primes. Equal vectors
# certify equal entropy expressions without evaluating any logarithm.
@lru_cache(None)
def factors(n):
    out=[];d=2
    while d*d<=n:
        e=0
        while n%d==0:n//=d;e+=1
        if e:out.append((d,e))
        d+=1 if d==2 else 2
    if n>1:out.append((n,1))
    return tuple(out)
@lru_cache(None)
def logvec(q):
    out=defaultdict(Q)
    for p,e in factors(q.numerator):out[p]+=e
    for p,e in factors(q.denominator):out[p]-=e
    return {p:v for p,v in out.items() if v}
def add(*terms):
    out=defaultdict(Q)
    for scale,v in terms:
        for p,c in v.items():out[p]+=scale*c
    return {p:c for p,c in out.items() if c}
def scalar(x):return {2:Q(x)} if x else {}
def entropy(probs):
    out={}
    for p in probs:
        if p:out=add((1,out),(-p,logvec(p)))
    return out
def cross(P,R):
    out={}
    for s,p in P.items():
        if p:
            ck(R.get(s,Q(0))>0)
            out=add((1,out),(-p,logvec(R[s])))
    return out
def Lv(p):return add((-p,logvec(p))) if p else {}
def binary(p):return add((1,Lv(p)),(1,Lv(1-p)))
def activation_tax(r):
    p=Q(1,1<<r)
    return add((1,scalar(2*r*p*(2-p))),(1,Lv((1-p)**2)))
def erasure_sum(r):
    total={}
    for k in range(1,r+1):
        s=Q(1,1<<(k-1));m=1-s;q=(1+m*m)/2;e=s*s/(2*(1+m*m))
        B=add((q,binary(e)),(1,scalar((1-m*m)/2)))
        total=add((1,total),(Q(1,1<<(r-k)),B))
    return total

def witness(gh,r):
    law={(r,t,0):h*h for t,h in enumerate(gh) if h}
    for i in reversed(range(r)):
        out=defaultdict(Q);s=Q(1,1<<(r-i-1))
        for child in [{(i,0,0):Q(1)},law]:
            for (j,t,U),w in child.items():
                u=Q(1) if t==0 and U==0 else Q(0)
                v=s*gh[t] if t else (1-s if U==0 else -s)
                theta=(u-v)**2/(2*(u*u+v*v))
                for z,prob in [(0,1-theta),(1,theta)]:
                    if prob:out[(j,t,U|(z<<i))]+=w*prob/2
        law=dict(out)
    return law
def closed_W(j,t,U,gh,r):
    p=Q(1,1<<r)
    if t:return p*p*gh[t]**2 if j==r else Q(0)
    if j==r:return Q(0)
    if U>> (j+1):return Q(0)
    eps=[]
    for i in range(r):
        s=Q(1,1<<(r-i-1));eps.append(s*s/(2*(1+(1-s)**2)))
    prob=Q(1,1<<(j+1))
    if U==0:
        for i in range(j+1):prob*=1-eps[i]
        return prob
    m=U.bit_length()-1
    if m>j:return Q(0)
    prob*=eps[m]*Q(1,1<<m)
    for i in range(m+1,j+1):prob*=1-eps[i]
    return prob

# Outward intervals. Signed quotients use all four corners, including
# negative log numerators (the repaired B09 convention).
def mul_interval(c,I):return (c*I[0],c*I[1]) if c>=0 else (c*I[1],c*I[0])
def lnsmall(z,N=32):
    t=(z-1)/(z+1);ck(0<=t<=Q(1,3))
    total=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    tail=2*t**(2*N+1)/(Q(2*N+1)*(1-t*t))
    return total,total+tail
LN2=lnsmall(Q(2))
@lru_cache(None)
def logint(q):
    k=0;z=q
    while z<1:z*=2;k-=1
    while z>=2:z/=2;k+=1
    lo,hi=lnsmall(z);ka,kb=mul_interval(Q(k),LN2);lo+=ka;hi+=kb
    cs=[lo/LN2[0],lo/LN2[1],hi/LN2[0],hi/LN2[1]]
    return min(cs),max(cs)
def vint(V):
    lo=hi=Q(0)
    for prime,c in V.items():
        a,b=mul_interval(c,(Q(1),Q(1)) if prime==2 else logint(Q(prime)))
        lo+=a;hi+=b
    return lo,hi
def iv(I):return {'lo':str(I[0]),'hi':str(I[1])}
def vec(V):return {str(p):str(c) for p,c in sorted(V.items())}

fixtures=[];reviewfixtures=[];casecount=0;refcount=0;corecount=0
for n in (1,2,3):
    size=1<<n
    for positives in combinations(range(size),size//2):
        cutoff();corecount+=1
        positive=set(positives);g=[1 if x in positive else -1 for x in range(size)]
        gh=fwht(g);gp={t:h*h for t,h in enumerate(gh) if h}
        Hg=entropy(gp.values());Ig=sum(inf(g));ck(gh[0]==0);ck(sum(gp.values())==1)
        for r in (1,2,3,4,5):
            cutoff();casecount+=1;p=Q(1,1<<r);D=2*(1-p);A=activation_tax(r)
            f=[g[x>>r] if x&((1<<r)-1)==0 else 1 for x in range(1<<(n+r))]
            fh=fwht(f);P={};expected=[]
            for s,h in enumerate(fh):
                U=s&((1<<r)-1);t=s>>r
                e=p*gh[t] if t else (1-p if U==0 else -p)
                ck(h==e)
                if h:P[(U,t)]=h*h
            If=inf(f);ck(sum(If[:r])==r*p);ck(sum(If[r:])==p*Ig)
            HF=entropy(P.values());ck(HF==add((p,Hg),(1,A)))
            W=witness(gh,r);ck(sum(W.values())==1)
            marginal=defaultdict(Q);leaves=defaultdict(Q)
            for (j,t,U),w in W.items():
                ck(w==closed_W(j,t,U,gh,r));marginal[(U,t)]+=w;leaves[j]+=w
            ck(dict(marginal)==P)
            ck(leaves=={**{j:Q(1,1<<(j+1)) for j in range(r)},r:p})
            ck(entropy(leaves.values())==scalar(D))
            EW=entropy(W.values());Bsum=erasure_sum(r)
            ck(EW==add((1,scalar(D)),(p,Hg),(1,Bsum)))
            posterior=add((1,EW),(-1,HF))
            ck(posterior==add((1,scalar(D)),(1,Bsum),(-1,A)))
            refs=[gp,{t:Q(1,size-1) for t in range(1,size)}, {t:Q(1,2*(size-1)) for t in range(1,size)}]
            for ref_id,Rg in enumerate(refs):
                refcount+=1;cg=cross(gp,Rg);z=sum(Rg.values());QF={}
                for U in range(1<<r):
                    QF[(U,0)]=(1-p)**2 if U==0 else p*p
                    for t,q in Rg.items():QF[(U,t)]=p*p*q
                ck(sum(QF.values())==1-p+p*z)
                CE=cross(P,QF);ck(CE==add((p,cg),(1,A)))
                ck(add((1,CE),(-1,HF))==add((p,cg),(-p,Hg)))
                raw={}
                for U in range(1,1<<r):
                    m=U.bit_length()
                    raw[(U,0)]=sum((Q(1,4**j) for j in range(m,r+1)),Q(0))
                    ck(raw[(U,0)]>=p*p)
                for U in range(1<<r):
                    for t,q in Rg.items():raw[(U,t)]=p*p*q
                qs=sum(raw.values());v=2*p-p*p
                ck(qs==Q(2,3)-p+p*p/3+p*z);ck(0<qs<=1)
                Q13={key:v*q/qs for key,q in raw.items()};Q13[(0,0)]=(1-p)**2
                ck(sum(Q13.values())==1)
                CE13=cross(P,Q13)
                rawcost=cross({s:q for s,q in P.items() if s!=(0,0)},raw)
                ck(CE13==add((1,binary(v)),(1,rawcost),(v,logvec(qs))))
                if n==1 and positives==(0,) and ref_id in (0,2):
                    bound=add((1,binary(v)),(1,scalar(2*r*v)),(p,cg))
                    gap=add((1,bound),(-1,CE13));I=vint(gap)
                    ck(not gap or I[0]>0)
                    reviewfixtures.append({'r':r,'core_reference_mass':str(z),'q_star':str(qs),'gap_vector':vec(gap),'gap_interval':iv(I)})
            if n==1 and positives==(0,):
                fixtures.append({'r':r,'p':str(p),'D':str(D),'A_vector':vec(A),'A_interval':iv(vint(A)),'posterior_vector':vec(posterior),'posterior_interval':iv(vint(posterior)),'witness_atoms':len(W),'core_independence_verified':True})

sharp={};cr={}
for r in range(1,6):
    p=Q(1,1<<r);cr[r]=add((1/(r*p),activation_tax(r)))
    sharp[str(r)]={'vector':vec(cr[r]),'interval':iv(vint(cr[r]))}
for r in (1,2,4,5):
    gap=add((1,cr[3]),(-1,cr[r]));I=vint(gap);ck(I[0]>0)
    sharp[str(r)]['strict_gap_to_r3']=iv(I)
I3=vint(cr[3]);ck(I3[0]>Q(9,2));ck(I3[0]>Q(4536,1000));ck(I3[1]<Q(4537,1000))
sharp['analytic_tail']='For r>=6, c_r<=4+2/(r ln2)<4+3/r<=4.5<c_3, using ln2>2/3.'
save('SHARP_SELECTOR_CERTIFICATES.json',sharp)
save('POSTERIOR_FIXTURES.json',fixtures)
save('A013_REVIEW_CERTIFICATES.json',reviewfixtures)
save('EXACT_RESULTS.json',{'status':'PASS','assertions':checks,'balanced_cores':corecount,'Boolean_activation_cases':casecount,'reference_cases':refcount,'posterior_fixtures':len(fixtures),'sharp_coefficient_interval':iv(I3),'projected_reference_certificates':len(reviewfixtures),'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer FWHT, Fraction, prime-log vectors, outward rational log intervals','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
print((ROOT/'out'/'EXACT_RESULTS.json').read_text(encoding='utf-8'))
