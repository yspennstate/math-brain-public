"""Frozen A023-overlap-v1. Actual physical trees; no floating signs."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time,itertools
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); assertions=0; comparisons=0; ties=0; max_terms=0
SIGNCERTS={}
def ck(x):
    global assertions
    assert x
    assertions+=1
def budget():
    if time.perf_counter()-START>60:raise RuntimeError('frozen 60-second compute cap reached')
@lru_cache(None)
def factors(n):
    a=[];p=2
    while p*p<=n:
        z=0
        while n%p==0:n//=p;z+=1
        if z:a.append((p,z))
        p+=1
    if n>1:a.append((n,1))
    return tuple(a)
def term(v,n,c):
    if not n or not c:return
    for p,e in factors(n):
        v[p]=v.get(p,0)+c*e
        if not v[p]:del v[p]
def merge(*args):
    a={}
    for scale,v in args:
        for p,c in v.items():
            a[p]=a.get(p,F(0))+scale*c
            if not a[p]:del a[p]
    return a
def lnseries(x,N):
    z=(x-1)/(x+1); t=z;s=F(0)
    for j in range(N):s+=t/F(2*j+1);t*=z*z
    lo=2*s;hi=lo+2*t/F(2*N+1)/(1-z*z)
    return lo,hi
@lru_cache(None)
def logint(n,N):
    k=n.bit_length()-1; x=F(n,1<<k)
    lo,hi=lnseries(x,N); l2,h2=lnseries(F(2),N)
    return F(k)+lo/h2,F(k)+hi/l2
def positive(v):
    global comparisons,ties,max_terms
    comparisons+=1
    if not v:ties+=1;SIGNCERTS[()]={'vector':{},'classification':'EQUALITY'};return False,None
    for N in [24,48]:
        lo=hi=F(0)
        for p,c in v.items():
            l,h=logint(p,N)
            lo+=c*(l if c>0 else h);hi+=c*(h if c>0 else l)
        max_terms=max(max_terms,N)
        if lo>0 or hi<0:
            SIGNCERTS[tuple(sorted(v.items()))]={'vector':{str(p):str(c) for p,c in v.items()},'lower':str(lo),'upper':str(hi),'series_terms':N,'classification':'BAD' if lo>0 else 'GOOD'}
            return lo>0,(lo,hi)
    raise AssertionError('unresolved certified sign')
@lru_cache(None)
def walsh(v):
    a=list(v);s=1
    while s<len(v):
        for z in range(0,len(v),2*s):
            for j in range(z,z+s):x,y=a[j],a[j+s];a[j],a[j+s]=x+y,x-y
        s*=2
    return tuple(a)
@lru_cache(None)
def influence(v):
    N=len(v);n=N.bit_length()-1
    return F(sum(v[x]!=v[x^(1<<i)] for x in range(N) for i in range(n)),N)
@lru_cache(None)
def entropy(v):
    N=len(v);out={}
    for w in walsh(v):
        if w:term(out,N*N,w*w);term(out,w*w,-w*w)
    return {p:F(c,N*N) for p,c in out.items() if c}
@lru_cache(None)
def node(v):
    budget();N=len(v);W=walsh(v)
    ck(sum(w*w for w in W)==N*N)
    d=F(sum(W[j]**2 for j in range(1,N,2)),N*N)
    lo={}
    for j in range(0,N,2):
        A,D=W[j]**2,W[j+1]**2
        term(lo,A+D,A+D);term(lo,A,-A);term(lo,D,-D)
    B={p:F(c,N*N) for p,c in lo.items() if c}
    test=merge((1,B),(-4,{2:d}))
    bad,interval=positive(test)
    g,h=v[::2],v[1::2];cost=influence(tuple(x*y for x,y in zip(g,h)))/2
    ck(influence(v)==d+(influence(g)+influence(h))/2)
    return d,B,bad,cost,interval
@lru_cache(None)
def tree(v):
    if len(v)==1 or all(x==v[0] for x in v):return F(0),F(0),F(0)
    d,B,bad,cost,_=node(v)
    x,y=tree(v[::2]),tree(v[1::2])
    return ((cost if bad else 0)+(x[0]+y[0])/2,cost+(x[1]+y[1])/2,d+(x[2]+y[2])/2)
def stop_tree(v,c):
    N=len(v)
    if c==0 or all(all(x==v[j] for x in v[j:j+(1<<c)]) for j in range(0,N,1<<c)):
        return F(0),F(0),influence(v),entropy(v),{}
    d,B,bad,cost,_=node(v)
    x,y=stop_tree(v[::2],c-1),stop_tree(v[1::2],c-1)
    return ((cost if bad else 0)+(x[0]+y[0])/2,d+(x[1]+y[1])/2,(x[2]+y[2])/2,merge((F(1,2),x[3]),(F(1,2),y[3])),merge((1,B),(F(1,2),x[4]),(F(1,2),y[4])))
def odd_faces(v):
    N=len(v);n=N.bit_length()-1;count=0
    for i in range(n):
        for j in range(i+1,n):
            for x in range(N):
                if not(x&(1<<i) or x&(1<<j)):
                    count+=v[x]*v[x^(1<<i)]*v[x^(1<<j)]*v[x^(1<<i)^(1<<j)]==-1
    return F(2*count,N)
def reorder(v,order):
    return tuple(v[sum(((x>>j)&1)<<i for j,i in enumerate(order))] for x in range(len(v)))
def root(s,r,t,k):
    common=list(range(s));aa=list(range(s,s+r));bb=list(range(s+r,s+r+t));data=list(range(s+r+t,s+r+t+k));sel=s+r+t+k
    b=tuple((-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<k))
    core=b+tuple(-z if x==0 else z for x,z in enumerate(b))
    v=[]
    for x in range(1<<(sel+1)):
        on=all(not(x&(1<<i)) for i in common) and (all(not(x&(1<<i)) for i in aa) or all(not(x&(1<<i)) for i in bb))
        y=sum(((x>>i)&1)<<j for j,i in enumerate(data));v.append(core[y+((x>>sel)&1)*(1<<k)] if on else 1)
    return tuple(v),core,common,aa,bb,data,[sel]
def main():
    results=[];margins=[]
    for s,r,t,k in itertools.product([0,1,2],[1,2],[1,2],[2,4]):
        budget();v,g,C,A,B,X,Y=root(s,r,t,k);controls=C+A+B
        p,q,u=F(1,1<<r),F(1,1<<t),F(1,1<<s);beta=p+q-p*q;a=1-F(sum(g),len(g))
        ictrl=u*a*(s*beta+r*p*(1-q)+t*q*(1-p))
        I=influence(v);ck(I==ictrl+u*beta*influence(g))
        Q=odd_faces(v);orders={'selector-first':Y+controls+X,'control-first':controls+Y+X,'data-first':X+controls+Y,'control-data-selector':controls+X+Y}
        row={'s':s,'r':r,'t':t,'k':k,'I':str(I),'control_I':str(ictrl),'complete':{}}
        for name,order in orders.items():
            vv=reorder(v,order);bad,allq,usedI=tree(vv)
            ck(allq==Q);ck(usedI==I)
            row['complete'][name]={'bad_credit':str(bad),'bad_credit_over_I':str(bad/I),'total_odd_face_credit':str(allq)}
        stopped=stop_tree(reorder(v,controls+X+Y),len(controls))
        ck(stopped[0]==0);ck(stopped[1]==ictrl);ck(stopped[2]==u*beta*influence(g));ck(stopped[3]==merge((u*beta,entropy(g))))
        row['stopped']={'bad_credit':'0','queried_I':str(stopped[1]),'terminal_I':str(stopped[2]),'terminal_H_log_vector':{str(p):str(c) for p,c in stopped[3].items()},'sum_B_log_vector':{str(p):str(c) for p,c in stopped[4].items()}}
        results.append(row)
        # Save every completed root immediately.
        (ROOT/'out/results.json').write_text(json.dumps({'helper_version':'A023-overlap-v1','completed_roots':len(results),'results':results},indent=2),encoding='utf-8')
    # Independent exact analytic constant/correction certificates.
    cc=F(81,56);ee=F(65,24)
    ck(1+cc+2*cc/ee<4);ck(4+2*cc<7);ck(4+3*cc<9)
    ck(F(1,2)-cc/4==F(31,224))
    ck(F(65,24)+F(1,100)<F(11,4))
    (ROOT/'out/sign_certificates.json').write_text(json.dumps(list(SIGNCERTS.values()),indent=2),encoding='utf-8')
    out={'status':'PASS','roots':len(results),'complete_trees':4*len(results),'stopping_trees':len(results),'assertions':assertions,'unique_nodes':node.cache_info().currsize,'certified_sign_tests':comparisons,'exact_ties':ties,'max_series_terms':max_terms,'elapsed_seconds':time.perf_counter()-START,'max_bad_credit_over_I':{name:str(max(F(row['complete'][name]['bad_credit_over_I']) for row in results)) for name in orders},'arithmetic':'integer FWHT, Fraction, rational log intervals; no floating entropy sign'}
    (ROOT/'out/validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
