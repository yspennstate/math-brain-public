from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import math,json,time,sys
ROOT=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0
def check(a,b):
    global COUNT
    assert a==b,(a,b);COUNT+=1
def prod(xs):
    v=Q(1)
    for x in xs:v*=x
    return v
def tab(mask,n):return tuple(1 if mask>>x&1 else -1 for x in range(1<<n))
@lru_cache(None)
def rows(ps):
    n=len(ps);w=tuple(prod(ps[i] if x>>i&1 else 1-ps[i] for i in range(n)) for x in range(1<<n))
    norms=tuple(prod(ps[i]*(1-ps[i]) for i in range(n) if s>>i&1) for s in range(1<<n))
    m=[]
    for s in range(1<<n):
        row=[w[x]*prod(Q((x>>i)&1)-ps[i] for i in range(n) if s>>i&1) for x in range(1<<n)]
        den=math.lcm(*(q.denominator for q in row));m.append((den,tuple(int(q*den) for q in row)))
    return w,norms,m
@lru_cache(None)
def spec(t,ps):
    w,norms,m=rows(ps)
    raw=tuple(Q(sum(v*f for v,f in zip(r,t)),d) for d,r in m)
    P=tuple(a*a/b for a,b in zip(raw,norms));check(sum(P),Q(1))
    return raw,P
@lru_cache(None)
def factors(n):
    if n==1:return ()
    rt=math.isqrt(n)
    if rt*rt==n:return tuple((p,2*e) for p,e in factors(rt))
    out=[]
    for p in (2,3):
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
    p=5;step=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
        p+=step;step=6-step
    if n>1:out.append((n,1))
    return tuple(out)
def logform(q):
    d=dict(factors(q.numerator))
    for p,e in factors(q.denominator):d[p]=d.get(p,0)-e
    return {p:Q(e) for p,e in d.items() if e}
def add(*terms):
    d={}
    for c,x in terms:
        for p,v in x.items():d[p]=d.get(p,Q(0))+c*v
    return {p:v for p,v in d.items() if v}
@lru_cache(None)
def entropy(P):return add(*[(-q,logform(q)) for q in P if q])
def inf(P):return sum(s.bit_count()*q for s,q in enumerate(P))
def var(P):return 1-P[0]
def deficit(P):return inf(P)-var(P)
def empty(P):return add((-P[0],logform(P[0]))) if P[0] else {}
def corrected(P,ps):
    return add((1,entropy(P)),(-1,empty(P)),*[(sum(q for s,q in enumerate(P) if s>>i&1),logform(4*p*(1-p))) for i,p in enumerate(ps)])
def restrict(t,A,z):
    n=(len(t)-1).bit_length();B=[i for i in range(n) if i not in A]
    out=[]
    for b in range(1<<len(B)):
        x=sum(((z>>k)&1)<<i for k,i in enumerate(A))+sum(((b>>k)&1)<<i for k,i in enumerate(B));out.append(t[x])
    return tuple(out),B
def compressed(s,coords):return sum(((s>>i)&1)<<k for k,i in enumerate(coords))

MESH=10**30
def mesh(iv):return Q((iv[0]*MESH).__floor__(),MESH),Q((iv[1]*MESH).__ceil__(),MESH)
def scale(c,iv):return mesh(tuple(sorted((c*iv[0],c*iv[1]))))
def plus(*ivs):return mesh((sum(x[0] for x in ivs),sum(x[1] for x in ivs)))
@lru_cache(None)
def lnsmall(x):
    z=(x-1)/(x+1);N=40
    s=2*sum(z**(2*k+1)/Q(2*k+1) for k in range(N))
    return mesh((s,s+2*z**(2*N+1)/Q(2*N+1)/(1-z*z)))
LN2=lnsmall(Q(2))
@lru_cache(None)
def logprime(p):
    k=p.bit_length()-1;x=Q(p,1<<k);lo,hi=mesh((x,x))
    v=plus((lnsmall(lo)[0],lnsmall(hi)[1]),scale(k,LN2))
    ends=[a/b for a in v for b in LN2]
    return mesh((min(ends),max(ends)))
def interval(d):return plus(*[scale(c,logprime(p)) for p,c in d.items()])
def nonnegative(d):
    global COUNT
    if not d:COUNT+=1;return Q(0)
    lo,hi=interval(d);assert lo>=0,(d,lo,hi);COUNT+=1;return lo

def experiment(t,ps,A):
    n=len(ps);raw,P=spec(t,ps);B=[i for i in range(n) if i not in A]
    q=[Q(0)]*(1<<len(B))
    for s,v in enumerate(P):q[compressed(s,B)]+=v
    pw=rows(tuple(ps[i] for i in A))[0];joint=[];kids=[]
    for z,wz in enumerate(pw):
        child,_=restrict(t,A,z);cp=tuple(ps[i] for i in B);cr,PP=spec(child,cp);kids.append((wz,child,cp,PP))
        joint.extend(wz*v for v in PP)
        # Rational reconstruction of the transform, without square roots or U-code reuse.
        for T in range(1<<len(B)):
            val=Q(0)
            for R in range(1<<len(A)):
                parentS=sum(((T>>k)&1)<<i for k,i in enumerate(B))+sum(((R>>k)&1)<<i for k,i in enumerate(A))
                evalR=prod(Q((z>>k)&1)-ps[i] for k,i in enumerate(A) if R>>k&1)
                normR=prod(ps[i]*(1-ps[i]) for k,i in enumerate(A) if R>>k&1)
                val+=raw[parentS]*evalR/normR
            check(val,cr[T])
    for T in range(1<<len(B)):check(q[T],sum(wz*PP[T] for wz,_,_,PP in kids))
    for z,wz in enumerate(pw):check(sum(joint[z*(1<<len(B)):(z+1)*(1<<len(B))]),wz)
    M=add((1,entropy(P)),(-1,entropy(tuple(q))))
    EH=add(*[(w,entropy(PP)) for w,_,_,PP in kids])
    J=add((1,entropy(tuple(q))),(-1,EH))
    L=add((1,entropy(P)),(-1,EH))
    check(L,add((1,M),(1,J)))
    HZcond=add((1,entropy(tuple(joint))),(-1,entropy(tuple(q))))
    check(J,add((1,entropy(pw)),(-1,HZcond)))
    tax=add(*[(1,entropy((p,1-p))) for i,p in enumerate(ps) if i in A],*[(1,logform(max(ps[i],1-ps[i]))) for i in A])
    margin=add((1,M),(1,tax),(-1,J));nonnegative(margin);nonnegative(J);nonnegative(M)
    I_A=sum(s_in.bit_count()*v for s,v in enumerate(P) for s_in in [s&sum(1<<i for i in A)])
    Vdrop=sum(v for s,v in enumerate(P) if s and all(not(s>>i&1) for i in B))
    check(inf(P)-sum(w*inf(PP) for w,_,_,PP in kids),I_A)
    check(var(P)-sum(w*var(PP) for w,_,_,PP in kids),Vdrop)
    spent=I_A-Vdrop;assert spent>=0
    check(deficit(P)-sum(w*deficit(PP) for w,_,_,PP in kids),spent)
    normlog=add(*[(sum(v for s,v in enumerate(P) if s>>i&1),logform(4*ps[i]*(1-ps[i]))) for i in A])
    rhs=add((1,L),(1,normlog),(-1,empty(P)),*[(w,empty(PP)) for w,_,_,PP in kids])
    check(add((1,corrected(P,ps)),* [(-w,corrected(PP,cp)) for w,_,cp,PP in kids]),rhs)
    return kids,L,M,J,tax,I_A,spent,normlog

def tree(t,ps,rule,depth=0,history=0):
    _,P=spec(t,ps)
    if len(ps)==0 or deficit(P)==0:
        return {'EH':entropy(P),'EE':corrected(P,ps),'E0':empty(P),'I':inf(P),'D':deficit(P),'L':{},'M':{},'J':{},'tax':{},'norm':{},'spent':Q(0),'spentI':Q(0),'nodes':0}
    i=0 if rule==0 else (len(ps)-1 if rule==1 else (depth+history)%len(ps))
    kids,L,M,J,tax,I_A,spent,norm=experiment(t,ps,[i])
    sub=[(w,tree(child,cp,rule,depth+1,history*2+z)) for z,(w,child,cp,PP) in enumerate(kids)]
    out={}
    for k,local in [('L',L),('M',M),('J',J),('tax',tax),('norm',norm)]:out[k]=add((1,local),*[(w,v[k]) for w,v in sub])
    for k in ['EH','EE','E0']:out[k]=add(*[(w,v[k]) for w,v in sub])
    for k in ['I','D']:out[k]=sum(w*v[k] for w,v in sub)
    out['spent']=spent+sum(w*v['spent'] for w,v in sub)
    out['spentI']=I_A+sum(w*v['spentI'] for w,v in sub)
    out['nodes']=1+sum(v['nodes'] for _,v in sub)
    check(inf(P),out['I']+out['spentI']);check(deficit(P),out['D']+out['spent'])
    check(entropy(P),add((1,out['EH']),(1,out['L'])))
    check(corrected(P,ps),add((1,out['EE']),(1,out['L']),(1,out['norm']),(1,out['E0']),(-1,empty(P))))
    return out

def main():
    pilot='--pilot' in sys.argv
    laws={1:[(Q(1,2),),(Q(1,8),),(Q(1,64),),(Q(63,64),)],2:[(Q(1,2),)*2,(Q(1,8),Q(1,4)),(Q(1,64),Q(63,64))],3:[(Q(1,2),)*3,(Q(1,8),Q(1,4),Q(3,4)),(Q(1,64),Q(1,2),Q(63,64))]}
    domain=[(n,ps) for n in [1,2] for ps in laws[n]] if pilot else [(3,laws[3][int(sys.argv[sys.argv.index('--law')+1])])]
    blocks=trees=0;nodes=0
    for n,ps in domain:
        lo=int(sys.argv[sys.argv.index('--start')+1]) if '--start' in sys.argv else 0
        hi=int(sys.argv[sys.argv.index('--end')+1]) if '--end' in sys.argv else 1<<(1<<n)
        for mask in range(lo,hi):
            if time.perf_counter()-START>58:raise RuntimeError('frozen watchdog')
            t=tab(mask,n)
            for Amask in range(1<<n):experiment(t,ps,[i for i in range(n) if Amask>>i&1]);blocks+=1
            if not pilot:
                for rule in range(3):v=tree(t,ps,rule);trees+=1;nodes+=v['nodes']
    out={'status':'PASS','blocks':blocks,'adaptive_trees':trees,'visited_internal_nodes':nodes,'exact_assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'arithmetic':'Fraction direct centered moments; rational prime-log equality; rational log sign enclosures','domain':[(n,[str(p) for p in ps]) for n,ps in domain]}
    out['mask_range']=[lo,hi]
    name='PILOT.json' if pilot else 'LAW'+sys.argv[sys.argv.index('--law')+1]+('_'+str(lo)+'_'+str(hi) if '--start' in sys.argv else '')+'.json'
    (ROOT/'out'/name).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
