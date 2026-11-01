from fractions import Fraction as Q
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import argparse,json,time
RUN=Path(__file__).resolve().parents[1]
assertions=0
def ck(condition):
    global assertions
    assertions+=1
    assert condition, assertions
def fwht(values):
    w=list(values);N=len(w);step=1
    while step<N:
        for start in range(0,N,2*step):
            for j in range(start,start+step):u,v=w[j],w[j+step];w[j],w[j+step]=u+v,u-v
        step*=2
    return {i:Q(v,N) for i,v in enumerate(w) if v}
@lru_cache(None)
def factors(v):
    answer=[];d=2
    while d*d<=v:
        k=0
        while v%d==0:v//=d;k+=1
        if k:answer.append((d,k))
        d+=1
    if v>1:answer.append((v,1))
    return tuple(answer)
@lru_cache(None)
def phi(p):
    out=defaultdict(Q)
    if p:
        for v,sign in [(p.denominator,1),(p.numerator,-1)]:
            for prime,k in factors(v):out[prime]+=sign*k*p
    return tuple(sorted((k,v) for k,v in out.items() if v))
def add(*terms):
    out=defaultdict(Q)
    for factor,term in terms:
        for k,v in term:out[k]+=factor*v
    return tuple(sorted((k,v) for k,v in out.items() if v))
def E(x,y):return add((1,phi(x)),(1,phi(y)),(-1,phi(x+y)))
def H(p):return add(*[(1,phi(v)) for v in p.values()])
def Bvec(p,n):
    return [add(*[(1,E(v,p.get(s|(1<<i),Q(0)))) for s,v in p.items() if not s>>i&1]) for i in range(n)]
def B(p,n):return add(*[(1,b) for b in Bvec(p,n)])
def inf(p,n):return [sum(v for s,v in p.items() if s>>i&1) for i in range(n)]
def probabilities(a):return {s:c*c for s,c in a.items()}
def tensor(a,b,n):return {s|(t<<n):c*d for s,c in a.items() for t,d in b.items()}
def activation(a,n,s):
    p=Q(1,1<<s);d=1-a.get(0,Q(0));out={0:1-p*d}
    for u in range(1<<s):
        if u:out[u<<n]=-p*d
        for T,c in a.items():
            if T:out[T|(u<<n)]=p*c
    return {s:c for s,c in out.items() if c}
def test_activation(a,n,s,vals=None):
    p=Q(1,1<<s);mean=a.get(0,Q(0));d=1-mean;c=(1-p*d)**2
    aa=activation(a,n,s);pp=probabilities(aa);seedp=probabilities(a)
    if vals is not None:
        direct=fwht([vals[x&((1<<n)-1)] if x>>n==0 else 1 for x in range(1<<(n+s))]);ck(direct==aa)
    b=Bvec(pp,n+s);seedb=Bvec(seedp,n)
    for i in range(n):
        qi=seedp.get(1<<i,Q(0))
        expected=add((p,seedb[i]),(-p,E(mean*mean,qi)),(p*(1-p),E(d*d,qi)),(1,E(c,p*p*qi)))
        ck(expected==b[i])
    control=add((1,phi(Q(1,2))),(-1,phi(Q(1,2)))) # empty expression
    control=add((1,((2,p*(1-mean*mean)+(p-2*p*p)*d*d),)),(1,E(c,p*p*d*d)))
    for i in range(n,n+s):ck(b[i]==control)
    ck(sum(inf(pp,n+s))==p*(sum(inf(seedp,n))+s*d))
    ck(aa.get(0,Q(0))==1-p*d)
    return pp
def parity_sign(x,mask):return -1 if (x&mask).bit_count()%2 else 1
def run(nmax):
    started=time.perf_counter();seeds=0;balanced_tensor_cases=0;correlated_cases=0
    for n in range(nmax+1):
        for truth in range(1<<(1<<n)):
            seeds+=1;vals=[1 if truth>>x&1 else -1 for x in range(1<<n)]
            a=fwht(vals);p=probabilities(a);b=B(p,n);h=H(p)
            ck(sum(p.values())==1)
            aa=tensor(a,a,n);ck(B(probabilities(aa),2*n)==add((2,b)))
            bal={s|(1<<n):c for s,c in a.items()};ck(B(probabilities(bal),n+1)==b)
            for s in [1,2]:test_activation(a,n,s,vals)
            # Balanced M_g with g=z f. Label bits have zero erasure.
            mux={1<<(n+1):Q(1,2),1<<(n+2):Q(1,2)}
            for S,c in bal.items():mux[S|(1<<(n+1))]=c/2;mux[S|(1<<(n+2))]=-c/2
            mp=probabilities(mux);mb=Bvec(mp,n+3)
            ck(mb[-1]==() and mb[-2]==())
            ck(B(mp,n+3)==add((Q(1,2),b),(Q(1,2),E(1,p.get(0,Q(0))))))
            ck(H(mp)==add((1,((2,Q(2)),)),(Q(1,2),h)))
            # Two systematic codes: all columns nonzero, and one zero column.
            for columns in [[1]*n,[0]+[1]*(max(0,n-1))]:
                columns=columns[:n];code={}
                for S,c in a.items():
                    z=0
                    for i,col in enumerate(columns):
                        if S>>i&1:z^=col
                    code[S|(z<<n)]=c
                direct=[]
                for x in range(1<<(n+1)):
                    y=x&((1<<n)-1)
                    for i,col in enumerate(columns):
                        if col and x>>n&1:y^=1<<i
                    direct.append(vals[y])
                ck(fwht(direct)==code)
                cp=probabilities(code);cb=Bvec(cp,n+1);orig=Bvec(p,n)
                for i,col in enumerate(columns):ck(cb[i]==(() if col else orig[i]))
                ck(cb[-1]==())
            for r in [1,2]:
                bentvals=[(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(r)) for x in range(1<<(2*r))]
                bt=fwht(bentvals);bp=probabilities(bt);pad=probabilities(tensor(a,bt,n))
                ck(H(bp)==((2,Q(2*r)),));ck(B(bp,2*r)==H(bp));ck(sum(inf(bp,2*r))==r)
                ck(H(pad)==add((1,h),(1,H(bp))))
                ck(B(pad,n+2*r)==add((1,b),(1,H(bp))))
                ck(add((1,H(pad)),(-1,B(pad,n+2*r)))==add((1,h),(-1,b)))
            if n==2 and a.get(0,Q(0))==0:
                for m in [2,3]:
                    at={0:Q(1)}
                    for j in range(m):at=tensor(at,a,n*j)
                    hp=probabilities(at);ck(not any((1<<i) in hp for i in range(n*m)))
                    for s in [1,2,3]:
                        balanced_tensor_cases+=1;pp=test_activation(at,n*m,s)
                        pp0=Q(1,1<<s);control=add((1,((2,2*pp0-2*pp0*pp0),)),(1,E((1-pp0)**2,pp0*pp0)))
                        ck(B(pp,n*m+s)==add((pp0*m,b),(s,control)))
    for t in [2,3]:
        for r in [1,2]:
            correlated_cases+=1;N=2*t+2*r;vals=[]
            for x in range(1<<N):
                u=(x&((1<<t)-1)).bit_count()%2;v=((x>>t)&((1<<t)-1)).bit_count()%2
                exponent=u*v+sum(((x>>(2*t+2*j))&1)*((x>>(2*t+2*j+1))&1) for j in range(r))
                vals.append((-1)**exponent)
            aa=fwht(vals);p=probabilities(aa);ii=inf(p,N)
            ck(H(p)==((2,Q(2+2*r)),));ck(B(p,N)==((2,Q(2*r)),));ck(sum(ii)==t+r)
            ck(aa.get(0,Q(0))==Q(1,1<<(r+1)))
            ck(all(i==Q(1,2) for i in ii))
            uniform=Q(1,1<<N);tv=sum(abs(p.get(S,Q(0))-uniform) for S in range(1<<N))/2
            ck(tv==1-Q(1,1<<(2*t-2)))
    cert=dict(seed='three-bit one-point defect',H='4-(9/8)log2(3)',I='3/4',B='3+(15/8)log2(5)-(27/8)log2(3)',H_gt_2I=dict(left=3**9,right=2**20,strict=3**9<2**20),D_gt_zero=dict(left=2**8*3**18,right=5**15,strict=2**8*3**18>5**15))
    ck(cert['H_gt_2I']['strict']);ck(cert['D_gt_zero']['strict'])
    (RUN/'out/SIGN_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n',encoding='utf-8')
    out=dict(helper_version='A002-erasure-ledgers-v1',nmax=nmax,seeds=seeds,balanced_tensor_cases=balanced_tensor_cases,correlated_cases=correlated_cases,assertions=assertions,failures=0,seconds=time.perf_counter()-started,arithmetic='Integer FWHT/Fraction/formal prime-log identities/exact integer comparisons',max_correlated_dimension=10)
    (RUN/'out'/f'EXACT_CHECK_n{nmax}.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--nmax',type=int,choices=[2,3],required=True);run(ap.parse_args().nmax)
