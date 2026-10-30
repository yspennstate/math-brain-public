from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json, time, sys, hashlib
R=Path(__file__).resolve().parents[1]
SCALE=1<<144
def put(name,x):
    (R/'out'/name).write_text(json.dumps(x,indent=2),encoding='utf-8')
def fw(v):
    v=list(v); k=1
    while k<len(v):
        for b in range(0,len(v),2*k):
            for j in range(b,b+k):
                a,c=v[j],v[j+k];v[j],v[j+k]=a+c,a-c
        k*=2
    return v
def add(a,b,scale=Q(1)):
    d=a.copy()
    for p,v in b.items():d[p]=d.get(p,Q(0))+scale*v
    return {p:v for p,v in d.items() if v}
def mul(a,c):return {p:v*c for p,v in a.items() if v*c}
def log(q):
    q=Q(q);assert q>0;d={}
    for a,sgn in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=a:
            while a%p==0:d[p]=d.get(p,Q(0))+sgn;a//=p
            p+=1
        if a>1:d[a]=d.get(a,Q(0))+sgn
    return {p:v for p,v in d.items() if v}
@lru_cache(None)
def ln_unit(q):
    z=(q-1)/(q+1);s=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(64)),Q(0))
    return s,s+2*z**129/(129*(1-z*z))
@lru_cache(None)
def lb(p):
    if p==2:return Q(1),Q(1)
    if p=='e':
        a,b=ln_unit(Q(2));return 1/b,1/a
    x=Q(p);e=0
    while x>=2:x/=2;e+=1
    a,b=ln_unit(x);c,d=ln_unit(Q(2));return e+a/d,e+b/c
def bounds(a):return cached_bounds(tuple(sorted(a.items(),key=lambda z:str(z[0]))))
@lru_cache(None)
def cached_bounds(items):
    lo=hi=Q(0)
    for p,v in items:
        l,h=lb(p)
        lo+=v*(l if v>=0 else h);hi+=v*(h if v>=0 else l)
    return lo,hi
def enc(a):return {str(k):str(v) for k,v in a.items()}
def sgn(a):
    if not a:return 0
    l,h=bounds(a)
    assert l>0 or h<0,('undecided',enc(a))
    return 1 if l>0 else -1
checks=0
def ck(p):
    global checks
    assert p;checks+=1
def entropy(a):
    h={}
    for q in a:
        if q:h=add(h,log(q*q),-q*q)
    return h
def kval(q):return add(mul(log(q*q),-q*q) if q else {},{'e':3*q*q})
def kp(q):return add(mul(log(q*q),-2*q) if q else {},{'e':4*q})
def dataset(n):
    N=1<<n;rows=[]
    for m in range(1<<N):
        v=[1 if (m>>x)&1 else -1 for x in range(N)];a=[Q(w,N) for w in fw(v)]
        ck(a==[Q(sum(v[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)),N) for s in range(N)])
        h=entropy(a);i=Q(sum(v[x]!=v[x^(1<<j)] for x in range(N) for j in range(n)),N)
        ck(i==sum(s.bit_count()*q*q for s,q in enumerate(a)))
        rows.append((v,a,h,i))
    return rows
def main():
    start=time.perf_counter();pilot='--pilot' in sys.argv;cuts=0;classifications=[];guards=[];whole=0
    for n in range(3 if pilot else 4):
        rows=dataset(n);N=1<<n;FULL=(1<<N)-1
        # Independent direct Bregman expansion, including zero coefficients and constants.
        for m,(v,a,h,i) in enumerate(rows):
            mu=a[0];rr={}
            for c in [-1,1]:
                rem={}
                for s,q in enumerate(a):
                    t=Q(c if s==0 else 0)
                    rem=add(rem,add(add(kval(t),kval(q),-1),mul(kp(q),t-q),-1))
                expected=add(add(h,{'e':4}),add(mul(log(mu*mu),2*mu) if mu else {},{'e':-4*mu}),c)
                ck(rem==expected);rr[c]=rem;whole+=1
                # W_c expressed independently from full sign potential and physical edges.
                E=[x for x in range(N) if v[x]!=c]
                pot={}
                for x in E:
                    gx={}
                    for s,q in enumerate(a):
                        if q:gx=add(gx,log(q*q),q*(-1 if (s&x).bit_count()%2 else 1))
                    pot=add(pot,gx,v[x])
                edge=sum(v[x]*v[x^(1<<j)] for x in E for j in range(n) if x^(1<<j) not in E)
                for K in [0,2,6]:
                    W=add(add(pot,{'e':-2*len(E)}),{2:Q(-K,2)*edge})
                    D=add(h,{2:-K*i})
                    ck(add(mul(W,Q(-4,N)),rem,-1)==D)
                ck(sgn(rem)>=0)
            ck(add(rr[-1],rr[1])==add(mul(h,2),{'e':8}))
            u=abs(mu);cor=add({'e':4*(1-u)},mul(log(u*u),2*u) if u else {})
            ck(add(rr[1 if mu>=0 else -1],h,-1)==cor)
            ck(sgn(cor)>=0);ck(sgn(add({'e':4*(1-u)**2},cor,-1))>=0)
        # Exact finite monochromatic-edit versus all-edit extremality.
        for Knum in range(17):
            K=Q(Knum,2);Ds=[add(h,{2:-K*i}) for v,a,h,i in rows]
            bb=[bounds(d) for d in Ds];greatest=max(range(len(rows)),key=lambda t:bb[t][0])
            count=0;bad=[]
            for m in range(len(rows)):
                eligible=True
                for t in range(len(rows)):
                    # A one-sign edit corresponds exactly to inclusion-comparable plus sets.
                    if (m&t)==m or (m&t)==t:
                        cuts+=1;z=sgn(add(Ds[t],Ds[m],-1))
                        if z>0:eligible=False;break
                if eligible:
                    count+=1
                    if sgn(add(Ds[greatest],Ds[m],-1))>0:
                        bad.append(m)
                        if len(guards)<12:
                            edit=m^greatest;ep=edit&m;em=edit&(FULL^m)
                            ck(ep!=0 and em!=0)
                            guards.append({'n':n,'K':str(K),'mask':m,'better_mask':greatest,'plus_edit':ep,'minus_edit':em,'D':enc(Ds[m]),'gain':enc(add(Ds[greatest],Ds[m],-1))})
                ck(time.perf_counter()-start<55)
            classifications.append({'n':n,'K':str(K),'one_sign_maxima':count,'non_global':len(bad)})
        put('CHECKPOINT.json',{'completed_n':n,'checks':checks,'cuts':cuts,'guards':guards})
    out={'status':'PASS','pilot':pilot,'assertions':checks,'whole_sign_refunds':whole,'one_sign_comparisons':cuts,'elapsed_seconds':time.perf_counter()-start,'classification':classifications,'guards':guards}
    put('PILOT.json' if pilot else 'CHECK.json',out)
    print(json.dumps({k:v for k,v in out.items() if k not in ['classification','guards']}));print(json.dumps(guards[:2]))
if __name__=='__main__':main()
