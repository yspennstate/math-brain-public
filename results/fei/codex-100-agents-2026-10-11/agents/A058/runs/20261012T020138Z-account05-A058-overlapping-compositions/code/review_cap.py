from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,time,math
from check_coherent import walsh,table,ent,factors,add
R=Path(__file__).resolve().parents[1]
checks=0
def ck(c):
    global checks
    checks+=1
    if not c:raise AssertionError(checks)
def scale(sig,w):return {p:Q(v)*w for p,v in sig.items() if v}
def log_sig(x):
    out={p:Q(v) for p,v in factors(x.numerator)}
    return add(out,dict(factors(x.denominator)),-1)
def phi(a,b):
    if not a or not b:return {}
    return add(add(scale(log_sig(a+b),a+b),scale(log_sig(a),-a)),scale(log_sig(b),-b))
def bi(u,i):
    w=walsh(u);D=len(u)**2
    pr=[w[S]**2+w[S|(1<<i)]**2 for S in range(len(u)) if not S&(1<<i)]
    return scale(add(ent([a*a for a in w],D),ent(pr,D),-1),Q(1,D))
# Explicit ln2 kernel avoids recursion on the normalized endpoint.
z=Q(1,3);L2=2*sum(z**(2*j+1)/Q(2*j+1) for j in range(24));U2=L2+2*z**49/(49*(1-z*z))
@lru_cache(None)
def ln_prime(p):
    x=Q(p);k=0
    while x>=2:x/=2;k+=1
    z=(x-1)/(x+1)
    l=2*sum(z**(2*j+1)/Q(2*j+1) for j in range(24));h=l+2*z**49/(49*(1-z*z))
    return l+k*L2,h+k*U2
def interval(sig):
    l=h=Q(0)
    for p,w in sig.items():
        lp,hp=ln_prime(p)
        l+=w*(lp if w>=0 else hp);h+=w*(hp if w>=0 else lp)
    corners=[l/L2,l/U2,h/L2,h/U2]
    return min(corners),max(corners)
E=sum(Q(1,math.factorial(j)) for j in range(21));EU=E+Q(22,21*math.factorial(21))
Klow=4+Q(2)/(EU*U2);Khigh=4+Q(2)/(E*L2)
ck(Klow>5 and Khigh<Q(5062,1000))
def activate(u,r):
    n=len(u).bit_length()-1
    return [u[x&((1<<n)-1)] if x>>n==0 else 1 for x in range((1<<n)*(1<<r))]
def restrict(u,i,v):
    return [u[(y&((1<<i)-1))+((y>>i)<<(i+1))+(v<<i)] for y in range(len(u)//2)]
def physI(u,i=None):
    n=len(u).bit_length()-1
    if i is not None:return Q(sum(u[x]!=u[x^(1<<i)] for x in range(len(u))),len(u))
    return sum(physI(u,j) for j in range(n))
@lru_cache(None)
def suffix(u):
    if len(u)==1:return {}
    return add(bi(u,0),scale(add(suffix(tuple(restrict(u,0,0))),suffix(tuple(restrict(u,0,1)))),Q(1,2)))

def tree(u,r,order,rem):
    if not order:return Q(0),Q(0),Q(0),Q(0)
    i=rem.index(order[0]);p=Q(1,1<<r);w=walsh(u);N=len(u)
    m=Q(w[0],N);beta=Q(w[1<<i],N);v=1-m*m;t=beta*beta;d=physI(u,i)
    C=1-p+p*m
    def M(s):return add(phi(C*C,p*p*s),scale(phi((1-m)**2,s),p*(1-p)))
    # Actual physical Fourier erasure verifies the source pair including its subtraction.
    actual=bi(activate(u,r),i)
    rhs=add(scale(add(bi(u,i),phi(m*m,t),-1),p),M(t))
    ck(actual==rhs);ck(physI(activate(u,r),i)==p*d)
    if t and v:
        low1,up1=interval(M(v))
        second=add(scale(M(v),t/v),scale(log_sig(v/t),p*t))
        low2,up2=interval(second)
        low,up=min(low1,low2),min(up1,up2)
    else:low=up=Q(0)
    nextrem=[x for x in rem if x!=order[0]]
    child=[tree(restrict(u,i,b),r,order[1:],nextrem) for b in [0,1]]
    return low+(child[0][0]+child[1][0])/2,up+(child[0][1]+child[1][1])/2,d+(child[0][2]+child[1][2])/2,t+(child[0][3]+child[1][3])/2

start=time.perf_counter();count=0
for tcode in range(16):
    u=table(tcode,2);mu=Q(sum(u),4);a=1-mu
    for r in [1,2,3]:
        p=Q(1,1<<r);defect=[-1]+[1]*((1<<r)-1);tail=suffix(tuple(defect));lt,ut=interval(tail)
        ck(ut<=3*physI(defect))
        for order in [(0,1),(1,0)]:
            low,up,pi,vd=tree(u,r,list(order),[0,1])
            ck(pi==physI(u) and vd==1-mu*mu)
            IA=physI(activate(u,r));ck(IA==p*(physI(u)+r*a))
            totalupper=up+(a/2)*ut
            ck(totalupper<=Klow*IA)
            ck(up<=Klow*p*physI(u)+2*r*p*a)
            count+=1
ck(count==96)
result={'status':'PASS','tree_cases':count,'exact_assertions_and_certificates':checks,'elapsed_seconds':time.perf_counter()-start,'K_interval':[str(Klow),str(Khigh)],'method':'fresh actual physical activation spectra and prime-log pair identities; rational atanh/factorial sign certificates','reviewed_claim':'A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK@1','verdict':'ACCEPT_AT_STATED_SCOPE'}
(R/'out/review_results.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='K_interval'}))
