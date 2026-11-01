"""Independent literal-character transform and exact prime-log identities."""
from fractions import Fraction as R
from pathlib import Path
import json,time

start=time.monotonic();checks=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
    assert time.monotonic()-start<55
def merge(a,b,scale=R(1)):
    c=dict(a)
    for p,x in b.items():c[p]=c.get(p,R(0))+scale*x
    return {p:x for p,x in c.items() if x}
def logvec(q):
    result={}
    for number,sign in [(q.numerator,1),(q.denominator,-1)]:
        p=2
        while p*p<=number:
            while number%p==0:
                result[p]=result.get(p,0)+sign;number//=p
            p+=1
        if number>1:result[number]=result.get(number,0)+sign
    return {p:R(x) for p,x in result.items() if x}
def entropy(p):
    v={}
    for x in p:
        if x:v=merge(v,logvec(x),-x)
    return v
def divergence(p,q):
    v={}
    for x,y in zip(p,q):
        if x:v=merge(v,logvec(x/y),x)
    return v
def spectrum(tab):
    return [R(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(tab))**2,len(tab)**2) for s in range(len(tab))]
def marg(p):
    return [sum(x for s,x in enumerate(p) if s>>j&1) for j in range((len(p)-1).bit_length())]
def product(ds):
    out=[]
    for s in range(1<<len(ds)):
        q=R(1)
        for j,d in enumerate(ds):q*=d if s>>j&1 else 1-d
        out.append(q)
    return out
def tc(p):return divergence(p,product(marg(p)))
def ph(m):
    d=R(2,2**m)
    return entropy([(1-d)**2]+[d*d]*(2**m-1))
def hb(d):return entropy([d,1-d])
def ln_iv(q):
    e=0
    while q>=2:q/=2;e+=1
    while q<1:q*=2;e-=1
    def series(x):
        z=(x-1)/(x+1);lo=sum((2*z**(2*j+1)/R(2*j+1) for j in range(60)),R(0))
        return lo,lo+2*z**121/(121*(1-z*z))
    a,b=series(q);l,u=series(R(2))
    if e>=0:return a+e*l,b+e*u
    return a+e*u,b+e*l
def bounds(v):
    l,u=ln_iv(R(2));a=b=R(0)
    for p,c in v.items():
        x,y=ln_iv(R(p));lo,hi=x/u,y/l
        a+=c*(lo if c>=0 else hi);b+=c*(hi if c>=0 else lo)
    return a,b

# First conversion reconstructed independently from literal Walsh character sums.
n=3;N=n+3
tab=[(-1 if x&2 else 1) if not x&1 else (-1 if x&4 and x>>3==0 else 1) for x in range(1<<N)]
P=spectrum(tab);Q=product(marg(P))
children=[[tab[(t&1)|(a<<1)|((t>>1)<<2)] for t in range(1<<(N-1))] for a in [0,1]]
ps=[spectrum(t) for t in children]
actual=merge(merge({},tc(ps[0]),R(1,2)),tc(ps[1]),R(1,2));actual=merge(actual,tc(P),-1)
d=R(1,16);formula=merge(merge(hb(d),ph(4),R(1,2)),ph(5),-1)
ck(actual==formula);ck(bounds(actual)[0]>0)

reset_results=[]
for m in [2,3,4,5]:
    d=R(2,2**m);P=spectrum([-1]+[1]*(2**m-1));Q=product(marg(P))
    ps=[spectrum([-1]+[1]*(2**(m-1)-1)),spectrum([1]*2**(m-1))]
    q=[(x+y)/2 for x,y in zip(*ps)]
    qr=[Q[2*s]+Q[2*s+1] for s in range(2**(m-1))]
    # Physical coordinate 0 of point defect; literal transforms use that coordinate.
    kp=[[p[s]/(2*q[s]) for s in range(len(q))] for p in ps]
    out=[sum(x*y for x,y in zip(qr,k)) for k in kp]
    pred=[[x*y/o for x,y in zip(qr,k)] for k,o in zip(kp,out)]
    sigma={}
    for p,pr in zip(ps,pred):
        sigma=merge(sigma,merge(tc(p),divergence(p,pr),-1),R(1,2))
    beta=2*d*(1-d)
    phi=lambda t:merge(hb(t),hb(2*t),R(-1,2))
    expected=merge(divergence([R(1,2)]*2,out),phi(beta));expected=merge(expected,phi(d),-(m-1))
    ck(sigma==expected)
    if m==2:ck(not sigma)
    else:ck(bounds(sigma)[1]<0)
    reset_results.append({'m':m,'prime_log_identity':True,'strict_negative':bool(sigma)})

for m in range(4,10):
    d=R(2,2**m);D=merge(merge(hb(d),ph(m-1),R(1,2)),ph(m),-1)
    a,b=bounds(D)
    ck(b<0 if m==4 else a>0)

# Countercontrols: dropping the a=1 certificate allows insufficient bank;
# allowing x to be queried can reach a constant with zero terminal surplus.
twisted=[-1,-1,1,-1]
constant_x_child=[twisted[1],twisted[3]]
cp=spectrum(constant_x_child)
ck(constant_x_child==[-1,-1])
ck(entropy(cp)=={} and sum(marg(cp))==0)
result={'status':'PASS','checks':checks,'runtime_seconds':time.monotonic()-start,'direct_character_masks':250,'reset_identities':reset_results,'first_conversion_exact_log_vector':{str(k):str(v) for k,v in actual.items()},'independence':'no imports from exact.py or check.py; literal Walsh transform and prime-log cancellation; independent Fraction atanh intervals'}
root=Path(__file__).resolve().parent.parent
(root/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','runtime_seconds']}))
