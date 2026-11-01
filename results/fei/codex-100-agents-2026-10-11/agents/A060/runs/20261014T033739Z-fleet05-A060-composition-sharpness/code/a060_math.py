from fractions import Fraction as Q
from pathlib import Path
import json, time, sys, hashlib

ROOT=Path(__file__).resolve().parents[1]
CHECKS=0
def check(v):
    global CHECKS
    assert v
    CHECKS+=1

def fwht(vals):
    a=list(vals); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                u,v=a[k],a[k+h]; a[k],a[k+h]=u+v,u-v
        h*=2
    return [Q(v,len(a)) for v in a]

def direct(vals):
    n=len(vals)
    return [Q(sum(v*(-1 if (x&t).bit_count()%2 else 1) for x,v in enumerate(vals)),n) for t in range(n)]

def factors(n):
    out={}; p=2
    while p*p<=n:
        while n%p==0: out[p]=out.get(p,0)+1; n//=p
        p+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def add(*vectors):
    ans={}
    for vec in vectors:
        for p,c in vec.items(): ans[p]=ans.get(p,Q(0))+c
    return {p:c for p,c in ans.items() if c}

def scale(vec,c): return {p:v*c for p,v in vec.items() if v*c}
def logvector(x):
    ans={p:Q(v) for p,v in factors(x.numerator).items()}
    return add(ans,{p:-Q(v) for p,v in factors(x.denominator).items()})
def entropy(probs):
    return add(*(scale(logvector(p),-p) for p in probs if p))
def H(vals,transform=fwht): return entropy([x*x for x in transform(vals)])

def lnat(x,terms=40):
    # Range reduction and an exact positive-series tail. No floating sign.
    k=0
    while x>=2: x/=2; k+=1
    while x<1: x*=2; k-=1
    def kernel(y):
        z=(y-1)/(y+1)
        lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
        tail=2*z**(2*terms+1)/Q(2*terms+1)/(1-z*z)
        return lo,lo+tail
    lo,hi=kernel(x); a,b=kernel(Q(2))
    if k>=0: return lo+k*a,hi+k*b
    return lo+k*b,hi+k*a

LN2=lnat(Q(2))
def interval(vec):
    lo=hi=Q(0)
    for p,c in vec.items():
        a,b=lnat(Q(p)); a,b=a/LN2[1],b/LN2[0]
        if c>=0: lo+=c*a; hi+=c*b
        else: lo+=c*b; hi+=c*a
    return lo,hi

def dyadic(bounds):
    d=1<<100; lo,hi=bounds
    return {'lo_num':(lo*d).numerator//(lo*d).denominator,'hi_num':-((-hi*d).numerator//(-hi*d).denominator),'den':d}

def bent(r):
    return [(-1)**sum(((z>>j)&1)*((z>>(j+1))&1) for j in range(0,r,2)) for z in range(1<<r)]
def fixture(r):
    b=bent(r)
    f=[(1 if y==0 else -1) if z==0 else b[z] for y in range(2) for z in range(1<<r)]
    g=list(b); g[0]=-1
    return b,g,f
def influences(vals):
    n=(len(vals)).bit_length()-1
    return [Q(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals)) for i in range(n)]
def Tbits(c,s):
    return add(*(scale(logvector((1-c*sig*s)**2),(1+sig*s)/2*(1-c*sig*s)**2) for sig in [1,-1] if (1-c*sig*s)**2))

def series(r):
    q=Q(1,1<<r); s=Q(1,1<<(r//2))
    part=sum((Q(4*(2**(k-1)-1),k*(k-1)*(k-2))*s**(k+k%2) for k in range(3,43)),Q(0))
    tail=Q(1,3)*(2*s)**43/(1-2*s)
    lo=(3-(part+tail)/q)/LN2[1]; hi=(3-part/q)/LN2[0]
    check(lo>0)
    check(part>=Q(19,6)*q*q)
    check(part+tail<=8*q*q/(1-4*q))
    check(hi<3/LN2[1])
    return lo,hi

def table_case(r,transform=fwht):
    b,g,f=fixture(r); q=Q(1,1<<r); s=Q(1,1<<(r//2)); size=len(b)
    bs,gs,fs=transform(b),transform(g),transform(f)
    check(all(abs(x)==s for x in bs)); check(sum(x>0 for x in bs)==((1<<r)+(1<<(r//2)))//2)
    for t,x in enumerate(bs):
        check(gs[t]==x-2*q); check(fs[t]==x-q); check(fs[t+size]==q)
    check(sum(x*x for x in fs)==1)
    inf=influences(f); check(inf[-1]==q); check(inf[:-1]==[Q(1,2)+q]*r)
    check(sum(inf)==r*(Q(1,2)+q)+q)
    check(influences(b)==[Q(1,2)]*r); check(influences(g)==[Q(1,2)+2*q]*r)
    hb,hg,hf=H(b,transform),H(g,transform),H(f,transform)
    t1,t2=Tbits(Q(1),s),Tbits(Q(2),s)
    check(hb=={2:Q(r)})
    check(hg==add({2:Q(r)},scale(t2,-1)))
    check(hf==add({2:Q(r)+q*r},scale(t1,-1)))
    delta=add(hf,scale(hb,-Q(1,2)),scale(hg,-Q(1,2)))
    residual=add(delta,{2:-q*r})
    check(residual==add(scale(t2,Q(1,2)),scale(t1,-1)))
    if r>=4:
        lo,hi=interval(scale(residual,1/q)); a,c=series(r)
        check(not (hi<a or c<lo))
        check(lo>= (3-8*q/(1-4*q))/LN2[1])
        check(hi<= (3-Q(19,6)*q)/LN2[0])
    return {'r':r,'influence':str(sum(inf)),'spent_data_influence':str(q),'residual_per_spent_influence':dyadic(interval(scale(residual,1/q))),'terminal_entropy':dyadic(interval(scale(add(hb,hg),Q(1,2))))}

def tensor_case(k):
    r=2; b,g,f=fixture(r); base=len(f)
    vals=[1]*(base**k)
    for x in range(len(vals)):
        t=x
        for j in range(k): vals[x]*=f[t%base]; t//=base
    check(H(vals)==scale(H(f),k)); check(sum(influences(vals))==k*sum(influences(f)))
    terminal={}
    for ys in range(1<<k):
        tv=[1]*(len(b)**k)
        for x in range(len(tv)):
            t=x
            for j in range(k):
                tv[x]*=(g if (ys>>j)&1 else b)[t%len(b)]; t//=len(b)
        terminal=add(terminal,scale(H(tv),Q(1,1<<k)))
    check(terminal==scale(add(H(b),H(g)),Q(k,2)))
    residual=add(H(vals),scale(terminal,-1),{2:-Q(k*r,1<<r)})
    single=add(H(f),scale(add(H(b),H(g)),-Q(1,2)),{2:-Q(r,1<<r)})
    check(residual==scale(single,k))
    return {'copies':k,'dimension':3*k,'spent_data_influence':str(Q(k,4)),'additive_reserve':str(Q(k,2))}

def run(mode):
    t=time.perf_counter()
    if mode=='pilot': tables=[table_case(4)]; compressed=[]; tensors=[]
    elif mode=='reproduce':
        tables=[table_case(r,direct) for r in [2,4,6]]; compressed=[]; tensors=[]
    else:
        tables=[table_case(r) for r in [2,4,6,8]]
        compressed=[{'r':r,'residual_per_spent_influence':dyadic(series(r))} for r in [4,6,8,10,12,16,24,32,64]]
        tensors=[tensor_case(k) for k in [1,2,3]]
    elapsed=time.perf_counter()-t; check(elapsed<55)
    result={'mode':mode,'assertions':CHECKS,'seconds':elapsed,'status':'PASS','tables':tables,'compressed':compressed,'tensors':tensors,'ln2_interval':dyadic(LN2),'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'out'/('checks_'+mode+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'mode':mode,'assertions':CHECKS,'seconds':elapsed,'status':'PASS'}))

if __name__=='__main__': run(sys.argv[1] if len(sys.argv)>1 else 'main')
