from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import time,json,hashlib

ROOT=Path(__file__).resolve().parents[1]
assert (ROOT/'out/FROZEN_SPEC.json').exists()
start=time.perf_counter();checks=0
def ck(b):
    global checks
    assert b
    checks+=1
def add(x,y):return x[0]+y[0],x[1]+y[1]
def scale(a,x):return (a*x[0],a*x[1]) if a>=0 else (a*x[1],a*x[0])
def sub(x,y):return x[0]-y[1],x[1]-y[0]
@lru_cache(None)
def ln(x):
    assert x>0
    if x==1:return F(0),F(0)
    if x<1:return scale(-1,ln(1/x))
    j=0
    while x>=2:x/=2;j+=1
    z=(x-1)/(x+1)
    l=2*sum((z**(2*k+1)/F(2*k+1) for k in range(64)),F(0))
    h=l+2*z**129/(129*(1-z*z))
    if j:
        a,b=ln(F(2));l+=j*a;h+=j*b
    return l,h
# Avoid recursive extraction on ln2 itself.
z=F(1,3)
L2lo=2*sum((z**(2*k+1)/F(2*k+1) for k in range(64)),F(0))
L2hi=L2lo+2*z**129/(129*(1-z*z))
LN2=(L2lo,L2hi)
# Seed the cache using a separate exact dyadic base.
_ln=ln
@lru_cache(None)
def log(x):
    if x==2:return LN2
    if x==1:return F(0),F(0)
    if x<1:return scale(-1,log(1/x))
    y=x;j=0
    while y>=2:y/=2;j+=1
    z=(y-1)/(y+1)
    l=2*sum((z**(2*k+1)/F(2*k+1) for k in range(64)),F(0))
    h=l+2*z**129/(129*(1-z*z))
    return l+j*LN2[0],h+j*LN2[1]

def vals(mask,n):return [F(1 if mask>>x&1 else -1) for x in range(1<<n)]
def qlaw(d):
    if not d['w']:return [F(1)]+[F(0)]*(len(d['P'])-1)
    return [d['P'][0]]+[d['w']*x/d['Z'] for x in d['W'][1:]]
def normalizer(d):
    return scale(d['w'],log(d['Z']/d['w'])) if d['w'] else (F(0),F(0))
def data(f,p):
    n=len(p);c=list(f)
    for i,q in enumerate(p):
        for x in range(1<<n):
            if x>>i&1:continue
            a,b=c[x],c[x|(1<<i)]
            c[x]=(1-q)*a+q*b;c[x|(1<<i)]=(b-a)/2
    vs=[F(1)]*(1<<n)
    for s in range(1,1<<n):
        bit=s&-s;i=bit.bit_length()-1
        vs[s]=vs[s^bit]*4*p[i]*(1-p[i])
    P=[vs[s]*c[s]*c[s] for s in range(1<<n)]
    ck(sum(P,F(0))==1)
    w=1-P[0];Delta=sum((F(s.bit_count()-1)*P[s] for s in range(1,1<<n)),F(0))
    R=sum((F(s.bit_count()-2)*P[s] for s in range(1,1<<n) if s.bit_count()>=3),F(0))
    j=[0]*(1<<n);u=[F(0)]*(1<<n);W=[F(0)]*(1<<n);mant=(F(0),F(0))
    for s in range(1,1<<n):
        t=abs(c[s]);ck(t<=1)
        if not t:continue
        a=t
        while a<=F(1,2):a*=2;j[s]+=1
        u[s]=a;W[s]=vs[s]/4**j[s]
        ck(F(1,2)<a<=1)
        ck(P[s]==W[s]*a*a)
        mant=add(mant,scale(2*P[s],log(1/a)))
    Z=sum(W,F(0));J=2*sum((P[s]*j[s] for s in range(1,1<<n)),F(0))
    I=[sum((P[s] for s in range(1<<n) if s>>i&1),F(0)) for i in range(n)]
    return dict(c=c,P=P,vs=vs,w=w,D=Delta,R=R,j=j,u=u,W=W,Z=Z,J=J,L=mant,I=I)

refs=0;near_equal=[]
def reference(f,p):
    global refs
    d=data(f,p);refs+=1
    P,w,D,R,Z=d['P'],d['w'],d['D'],d['R'],d['Z']
    ck(0<=R<=D)
    ck(0<=Z-w<=9*D-6*R)
    ck(d['L'][1]<=(11*D-7*R)/2)
    if w:
        q=[P[0]]+[w*x/Z for x in d['W'][1:]]
        ck(sum(q,F(0))==1)
        for s in range(1,len(P)):
            if P[s]:ck(P[s]/q[s]==d['u'][s]**2*Z/w)
            else:ck(q[s]==0)
        normal=scale(w,log(Z/w))
        if Z==w:ck(normal==(0,0))
        else:ck(normal[1]<=9*D-6*R)
        KL=sub(normal,d['L'])
        if q==P:ck(KL[0]<=0<=KL[1])
        else:ck(KL[0]>=0)
    else:ck(Z==0 and d['J']==0 and d['L']==(0,0))
    for N in (0,1,2,3):
        partial=F(0)
        for s in range(1,len(P)):
            if not P[s]:continue
            z=(1-d['u'][s])/(1+d['u'][s])
            partial+=4*P[s]*sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
        error=sub(d['L'],(partial,partial))
        bound=(11*D-7*R)/(2*(2*N+1)*9**N)
        ck(error[0]>=0 and error[1]<=bound)
    # Independently check the physical singleton bank.
    bank=F(0)
    n=len(p)
    for i in range(n):
        second=F(0)
        for x in range(1<<n):
            if x>>i&1:continue
            wt=F(1)
            for h in range(n):
                if h!=i:wt*=p[h] if x>>h&1 else 1-p[h]
            derivative=(f[x|(1<<i)]-f[x])/2
            ck(derivative in (-1,0,1))
            second+=wt*derivative*derivative
        t=abs(d['c'][1<<i]);V=second-t*t
        ck(second>=t)
        bank+=4*p[i]*(1-p[i])*V
    ck(bank==2*D-R)

for mask in range(256):
    for p in ((F(1,2),)*3,(F(1,4),F(1,2),F(3,4))):reference(vals(mask,3),p)
frozen=[0,65535,1,32768,56067,33152,27030,38505,42405,43690,255,65280,21845,3855,4080,6996]
for mask in frozen:
    for p in ((F(1,2),)*4,(F(1,4),)*4,(F(1,4),F(1,3),F(2,3),F(3,4))):reference(vals(mask,4),p)

comps=0;positive_carries=0
for mask in range(16):
    for left in (1,6,8):
        for right in (1,6,8):
            for p in ((F(1,2),)*4,(F(1,4),F(1,3),F(2,3),F(3,4))):
                fs=[vals(left,2),vals(right,2)];children=[data(fs[0],p[:2]),data(fs[1],p[2:])]
                induced=tuple((1+x['c'][0])/2 for x in children)
                g=vals(mask,2);gd=data(g,induced)
                Fvals=[g[int((fs[0][x&3]+1)/2)+2*int((fs[1][x>>2]+1)/2)] for x in range(16)]
                fd=data(Fvals,p);aa=[gd['I'][i]/children[i]['w'] for i in range(2)]
                ck(fd['D']==gd['D']+sum((aa[i]*children[i]['D'] for i in range(2)),F(0)))
                carry=F(0);qg=qlaw(gd);qi=[qlaw(x) for x in children];qt=[qg[0]]+[F(0)]*15
                for s in range(1,16):
                    ts=[s&3,s>>2];A=int(bool(ts[0]))+2*int(bool(ts[1]));c=gd['c'][A]
                    base=gd['j'][A]
                    for i in range(2):
                        if ts[i]:c*=children[i]['c'][ts[i]];base+=children[i]['j'][ts[i]]
                    ck(fd['c'][s]==c)
                    qr=qg[A]
                    for i in range(2):
                        if ts[i]:qr*=qi[i][ts[i]]/children[i]['w']
                    qt[s]=qr
                    if fd['P'][s]:
                        k=fd['j'][s]-base;ck(k>=0);carry+=fd['P'][s]*k
                        rat=gd['P'][A]/qg[A]
                        for i in range(2):
                            if ts[i]:rat*=children[i]['P'][ts[i]]/qi[i][ts[i]]
                        ck(fd['P'][s]/qt[s]==rat)
                ck(sum(qt,F(0))==1 and qt[0]==fd['P'][0])
                nsum=normalizer(gd)
                for i in range(2):nsum=add(nsum,scale(aa[i],normalizer(children[i])))
                ck(nsum[1]<=9*fd['D'])
                ck(fd['J']==gd['J']+sum((aa[i]*children[i]['J'] for i in range(2)),F(0))+2*carry)
                residual=gd['L']
                for i in range(2):residual=add(residual,scale(aa[i],children[i]['L']))
                residual=sub(residual,fd['L']);target=scale(2*carry,LN2)
                ck(sub(residual,target)[0]<=0<=sub(residual,target)[1])
                ck(target[1]+fd['L'][1]<=F(11,2)*fd['D'])
                if carry:positive_carries+=1
                comps+=1

# Full norm-one real counterexample pinpoints Boolean admission.
ck(F(4,5)**2+F(3,5)**2==1)
ck(F(9,25)<F(3,5))
ck(F(1)-F(9,25)>0)
ck(refs==560 and comps==288)
out={'status':'PASS','reference_cases':refs,'composition_cases':comps,'positive_carry_cases':positive_carries,'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction plus64-term rigorous atanh intervals; rational coefficient-factorization and reference-ratio identities','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'full_FEI':'OPEN'}
(ROOT/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
