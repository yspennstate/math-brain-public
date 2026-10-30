from pathlib import Path
from fractions import Fraction as F
from math import comb
from functools import lru_cache
from collections import Counter
import json,time,hashlib
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0
def ck(t):
    global assertions
    assert t
    assertions+=1
def fw(v):
    v=list(v); k=1
    while k<len(v):
        for i in range(0,len(v),2*k):
            for j in range(k):
                a,b=v[i+j],v[i+j+k];v[i+j]=a+b;v[i+j+k]=a-b
        k*=2
    return v
def char(s,x):return 1-2*((s&x).bit_count()%2)
small=0
for n in range(4):
    N=1<<n
    for mask in range(1<<N):
        values=[1-2*((mask>>x)&1) for x in range(N)]
        W=fw(values);small+=1
        ck(W==[sum(values[x]*char(s,x) for x in range(N)) for s in range(N)])
        for u in range(N):
            for v in range(N):
                ck(sum(W[u^s]*W[s^v] for s in range(N))==(N*N if u==v else 0))
        for s in range(1,N):
            if W[s]:
                d=max(t.bit_count() for t in range(N) if t&s==s and W[t])
                ck((W[s]*(1<<(d-1)))%N==0)
        # Reconstruct physical restriction joint by direct child transforms.
        if n:
            child=[fw(values[y::2]) for y in [0,1]]
            childp=[[F(w*w,(N//2)**2) for w in c] for c in child]
            ck(all(sum(c)==1 for c in childp))
            for t in range(N//2):
                q=F(W[2*t]**2+W[2*t+1]**2,N*N)
                ck(q==(childp[0][t]+childp[1][t])/2)
                if q:ck(sum(childp[y][t]/(2*q) for y in [0,1])==1)
        if time.perf_counter()-start>60: raise RuntimeError('frozen runtime exceeded')
# A032 independent exhaustive census via Gray-code point-flip updates.
N=16; W=[16]+[0]*15; laws=set(); prev=0
for k in range(1<<N):
    if k:
        g=k^(k>>1); flipped=(g^prev).bit_length()-1
        old=1-2*((prev>>flipped)&1)
        W=[w-2*old*char(s,flipped) for s,w in enumerate(W)];prev=g
    laws.add(tuple(w*w for w in W))
ck(len(laws)==2261)
# Ten-atom coupled obstruction: independent partitions and common phases.
mag=[8,8]+[4]*8+[0]*6; separate=[]; rejections=[]
for u in range(1,16):
    products=[mag[s]*mag[s^u] for s in range(16) if s<(s^u) and mag[s]*mag[s^u]]
    reachable={0}
    for v in products: reachable|={x+v for x in list(reachable)}
    ck(sum(products)%2==0 and sum(products)//2 in reachable)
    separate.append({'xor':u,'pair_products':products})
for phase in range(512):
    a=[mag[0]]+[mag[s]*(1-2*((phase>>(s-1))&1)) for s in range(1,10)]+[0]*6
    bad=[(u,sum(a[s]*a[s^u] for s in range(16))) for u in range(1,16)]
    bad=[z for z in bad if z[1]];ck(bool(bad));rejections.append({'phase':phase,'xor':bad[0][0],'integer_convolution':bad[0][1]})
(ROOT/'out/COUPLED_PHASE_CERTIFICATE.json').write_text(json.dumps({'partitions':separate,'rejections':rejections},indent=2),encoding='utf-8')
# Rational log intervals, independently implemented from first principles.
def ln(x):
    x=F(x);k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    def core(q):
        z=(q-1)/(q+1); b=2*sum((z**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
        return b,b+2*z**41/(41*(1-z*z))
    l,h=core(x);l2,h2=core(F(2))
    return (l+k*l2,h+k*h2) if k>=0 else (l+k*h2,h+k*l2)
ln2=ln(F(2))
@lru_cache(None)
def log2(x):
    l,h=ln(x);return min(l/ln2[0],l/ln2[1]),max(h/ln2[0],h/ln2[1])
def ent(prob):
    l=h=F(0)
    for p,count in Counter(prob).items():
        if p:
            a,b=log2(1/p);l+=count*p*a;h+=count*p*b
    return l,h
def short(x):
    # Outward lower rounding prevents enormous serialized denominator strings.
    q=F((x*10**12).__floor__(),10**12)
    return str(q.numerator)+'/'+str(q.denominator)
factor_results=[]
for m in range(2,13):
    d=F(1,1<<(m-1));a=4*d*(1-d);I=m*d
    p0=(1-d)**2;H=ent([p0]+[d*d]*((1<<m)-1));h=ent([d,1-d]);B=(m*h[0],m*h[1]);K=(B[0]-H[1],B[1]-H[0])
    v=[F(1)]+[a**k*(1-F(1,1<<max(k-2,0))*(1 if k>=2 else 2)*(1-d)**(m-k))**2 for k in range(1,m+1)]
    # Independent direct binomial expression: bracket is 1-2^(2-k)(1-d)^(m-k).
    ck(all(v[k]==a**k*(1-F(2)**(2-k)*(1-d)**(m-k))**2 for k in range(1,m+1)))
    Z=sum(comb(m,k)*v[k] for k in range(m+1));Tl=Th=F(0)
    for k in range(1,m+1):
        if v[k]:
            l,h=log2(1/v[k]);Tl+=comb(m,k)*v[k]*l/Z;Th+=comb(m,k)*v[k]*h/Z
    ck(H[1]<=4*I);ck(K[0]>=Th/4-8*I);ck(B[1]<=Tl/4+8*I)
    factor_results.append({'m':m,'Z':short(Z),'payment_margin_lower':short(K[0]-Th/4+8*I),'recovery_margin_lower':short(Tl/4+8*I-B[1])})
# Strong full-support non-Boolean product relaxation of A036 payment.
d=F(1,65536);v=4*d*(1-d);l,h=log2(1/v)
margin=v*l/(4*(1+v))-8*d;ck(margin>0)
# Rational two-atom relaxation: f=3/5+4/5*x, norm1, no Boolean phase.
a=[F(3,5),F(4,5)];ck(sum(x*x for x in a)==1)
conv=2*a[0]*a[1];ck(conv==F(24,25));ck(conv*conv==F(576,625))
energies=[(a[0]+a[1])**2,(a[0]-a[1])**2];ck(energies==[F(49,25),F(1,25)])
branch=[x/2 for x in energies];ck(branch==[F(49,50),F(1,50)])
# Uniform singleton law on four variables is real, has H=2,I=1,U=0,
# and passes all one-coordinate singleton-XOR convolution constraints.
sup=[1,2,4,8];amp={s:F(1,2) for s in sup}
for u in [1,2,4,8]:ck(sum(amp.get(s,F(0))*amp.get(s^u,F(0)) for s in range(16))==0)
ck(sum(amp.get(s,F(0))*amp.get(s^3,F(0)) for s in range(16))==F(1,2))
ck(sum(s.bit_count()*x*x for s,x in amp.items())==1)
out={'status':'PASS','assertions':assertions,'seconds':time.perf_counter()-start,'small_boolean_tables':small,'n4_tables':65536,'n4_distinct_laws':len(laws),'coupled_phase_rejections':512,'factor_intervals':factor_results,'nonBoolean_product_payment_margin_lower':short(margin),'real_two_atom_child_probabilities':[short(x) for x in branch],'uniform_singleton_control':{'n':4,'H_bits':2,'I':1,'U':0}}
(ROOT/'out/VALIDATION.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ['factor_intervals','nonBoolean_product_payment_margin_lower']}))
