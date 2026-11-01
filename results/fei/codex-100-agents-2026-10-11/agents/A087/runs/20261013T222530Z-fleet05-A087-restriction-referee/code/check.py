"""Independent physical truth-table referee, no imports from source agents."""
import sys,json,time,itertools,hashlib
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
@lru_cache(None)
def factors(n):
    ans={}; p=2
    while p*p<=n:
        while n%p==0: ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans
def add(*vs):
    ans={}
    for v in vs:
        for p,c in v: ans[p]=ans.get(p,Q(0))+c
    return tuple(sorted((p,c) for p,c in ans.items() if c))
def scale(v,c): return tuple((p,x*c) for p,x in v if x*c)
@lru_cache(None)
def phi(x):
    if not x:return ()
    return add(tuple((p,-x*k) for p,k in factors(x.numerator).items()),tuple((p,x*k) for p,k in factors(x.denominator).items()))
def packet(a,b):return add(phi(a),phi(b),scale(phi(a+b),-1))
def dpacket(a,b):return add(phi(a*a),phi(b*b),scale(add(phi((a+b)**2),phi((a-b)**2)),Q(-1,2)))
@lru_cache(None)
def walsh(f):
    a=list(f);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h): a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
        h*=2
    return tuple(Q(x,len(a)) for x in a)
@lru_cache(None)
def entropy(f):return add(*(phi(c*c) for c in walsh(f)))
def dimension(f):return len(f).bit_length()-1
@lru_cache(None)
def child(f,i,b):
    return tuple(f[(z&((1<<i)-1))|((z>>i)<<(i+1))|(b<<i)] for z in range(len(f)//2))
@lru_cache(None)
def inf(f,i):return Q(sum(child(f,i,0)[z]!=child(f,i,1)[z] for z in range(len(f)//2)),len(f)//2)
def erasure(f,i):
    c=walsh(f)
    return add(*(packet(c[s]**2,c[s|(1<<i)]**2) for s in range(len(f)) if not s&(1<<i)))
def decrement(f,i):return add(entropy(f),scale(add(entropy(child(f,i,0)),entropy(child(f,i,1))),Q(-1,2)))
def priority(u,v,o):
    out=[]
    for z in range(8*len(u)*len(v)):
        x=z&1;A=(z>>1)&1;B=(z>>2)&1;ui=(z>>3)&(len(u)-1);vi=z>>(3+dimension(u))
        out.append(u[ui] if x==0 and A==0 else v[vi] if x==o and B==0 else 1)
    return tuple(out)
def selector(u,v,o,j):
    other=v if j==0 else u;C=[];W=[]
    for z in range(8*len(other)):
        x=z&1;A=(z>>1)&1;B=(z>>2)&1;idx=z>>3
        c=x==0 and A==0;d=x==o and B==0 and not c
        active=c if j==0 else d
        C.append(int(active));W.append(0 if active else other[idx] if (d if j==0 else c) else 1)
    return tuple(C),tuple(W)
@lru_cache(None)
def ln_interval(x):
    # Range reduction to [1,2); rational atanh series and explicit tail.
    k=0;y=Q(x)
    while y>=2:y/=2;k+=1
    while y<1:y*=2;k-=1
    def unit(t):
        z=(t-1)/(t+1);s=sum((z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))*2
        return s,s+2*z**49/(49*(1-z*z))
    lo,hi=unit(y);a,b=unit(Q(2))
    return (lo+k*a,hi+k*b) if k>=0 else (lo+k*b,hi+k*a)
def log_bounds(v):
    lo=hi=Q(0)
    for p,c in v:
        a,b=ln_interval(p)
        if c>=0:lo+=c*a;hi+=c*b
        else:lo+=c*b;hi+=c*a
    # Natural logarithm vector: same sign as bit units.
    return lo,hi
def serial(v):return {str(p):str(c) for p,c in v}
checks=0;negative=None
def require(x):
    global checks
    checks+=1
    assert x
@lru_cache(None)
def audit_node(u,v,o):
    global negative
    f=priority(u,v,o);P=Q(1,4);R=Q(1,8) if o==0 else Q(1,4)
    mu=walsh(u)[0];nu=walsh(v)[0];a=1-mu;b=1-nu
    own=(P*a+R*b,Q(1,2)*((1-Q(1,2))*a/2+Q(1,2)*(1-mu*nu)/2),R*b) if o==0 else ((Q(1,2)*a+Q(1,2)*b-Q(1,4)*a*b)/2,P*a,R*b)
    for i in range(3):require(inf(f,i)==own[i])
    reserve=P*2*(1-mu*mu)
    # Same orientation R=1/8, so log2(1/R)=3 exactly; opposite =2.
    reserve+=R*(3 if o==0 else 2)*(1-nu*nu)
    require(reserve<=4*sum(own))
    for j,h in enumerate((u,v)):
        C,W=selector(u,v,o,j);cw=walsh(C);ww=walsh(W);q=P if j==0 else R;m=walsh(h)[0]
        require(sum(c*c for c in cw)==q)
        require(all(c*w==0 and w*w==1-c for c,w in zip(C,W)))
        aa=tuple(w+m*c for w,c in zip(ww,cw));var=1-m*m
        require(sum(z*z for z in aa)==1-q*var)
        for i in range(dimension(h)):
            fi=3+i+(dimension(u) if j else 0);beta=walsh(h)[1<<i];t=beta*beta
            M=add(*(packet(a*a,t*c*c) for a,c in zip(aa,cw)))
            J=add(*(add(dpacket(a,beta*c),scale(packet(a*a,t*c*c),-1)) for a,c in zip(aa,cw)))
            correction=add(M,scale(packet(m*m,t),-q))
            require(erasure(f,fi)==add(scale(erasure(h,i),q),correction))
            require(decrement(f,fi)==add(scale(add(decrement(h,i),scale(dpacket(m,beta),-1)),q),M,J))
            require(inf(f,fi)==q*inf(h,i))
            require(t<=var and abs(beta)<=inf(h,i))
            mv=walsh(child(h,i,0))[0];mw=walsh(child(h,i,1))[0]
            require(mv==m+beta and mw==m-beta)
            require(var-((1-mv*mv)+(1-mw*mw))/2==t)
            lo,hi=log_bounds(J)
            require(lo>=0 or J==())
            require(hi<=2*q*t or J==())
            if negative is None and log_bounds(correction)[1]<0:
                negative={'u':list(u),'v':list(v),'orientation':o,'core':j,'coordinate':i,'q':str(q),'m':str(m),'beta':str(beta),'corrected_outer_erasure_bits':serial(correction),'natural_interval':[str(x) for x in log_bounds(correction)]}
    return True
def faces(f):
    for pat in itertools.product((None,0,1),repeat=2):
        out=[];free=[i for i,b in enumerate(pat) if b is None]
        for z in range(1<<len(free)):
            index=sum((pat[i] if pat[i] is not None else ((z>>free.index(i))&1))<<i for i in range(2))
            out.append(f[index])
        yield tuple(out)
def run(pilot):
    started=time.monotonic();roots=0;nodes=0
    fs=list(itertools.product((-1,1),repeat=4));domain=itertools.product(fs,fs,(0,1))
    for u,v,o in domain:
        for hu,hv in itertools.product(faces(u),faces(v)):audit_node(hu,hv,o);nodes+=1
        roots+=1
        if time.monotonic()-started>(55 if pilot else 180):raise RuntimeError('frozen runtime reached')
        if pilot and roots==8:break
    result={'status':'PASS','roots':roots,'physical_data_faces_with_multiplicity':nodes,'distinct_nodes':audit_node.cache_info().currsize,'exact_assertions':checks,'seconds':time.monotonic()-started,'negative_correction_witness':negative,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'units':'bits (interval comparisons use natural logs)'}
    (ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='negative_correction_witness'}))
if __name__=='__main__':run(sys.argv[1]=='pilot')
