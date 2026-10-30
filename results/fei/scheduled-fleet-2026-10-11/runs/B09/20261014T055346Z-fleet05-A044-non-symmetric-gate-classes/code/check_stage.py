from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import time,json
import math_helper as M
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0; cases=0; degree3cases=0; profilechecks=0
def ck(v):
    global assertions
    assertions+=1
    assert v
def encode(x):return sum(z<<i for i,z in enumerate(x))
def vals(mask,n):return {x:Q(1 if mask>>encode(x)&1 else -1) for x in product((0,1),repeat=n)}
def certify(logs,constant=Q(0)):
    if not logs:ck(constant>=0)
    else:ck(M.interval(logs,constant)[0]>=0)
def charge(p,v):
    d={}
    if p:M.addlog(d,p,v/p)
    return M.combine((Q(1),d))
def test(mask,n,p,review=False):
    global cases,degree3cases,profilechecks
    cases+=1;f=vals(mask,n);P=M.spectrum(f,p)
    degree=max([s.bit_count() for s,z in enumerate(P) if z]+[0])
    local=[];supcost=Q(0)
    for s in range(1,1<<n):
        k=s.bit_count();S=[i for i in range(n) if s>>i&1];C=[i for i in range(n) if not s>>i&1]
        moments=[]
        for y in product((0,1),repeat=len(C)):
            total=Q(0)
            for b in product((0,1),repeat=k):
                x=[0]*n
                for i,z in zip(S,b):x[i]=z
                for i,z in zip(C,y):x[i]=z
                total+=(-1)**(k-sum(b))*f[tuple(x)]
            Z=total/2
            ck(Z.denominator==1);ck(abs(Z)<=2**(k-1))
            wt=M.prod(p[i] if z else 1-p[i] for i,z in zip(C,y))
            moments.append((Z,wt))
        mean=sum((z*w for z,w in moments),Q(0));var=sum((z*z*w for z,w in moments),Q(0))-mean*mean
        v=M.prod(4*p[i]*(1-p[i]) for i in S)
        above=sum((z for t,z in enumerate(P) if t!=s and (t&s)==s),Q(0))
        ck(P[s]==v*(mean/2**(k-1))**2)
        ck(var==Q(4**(k-1),1)*above/v)
        # Verify integer moment payment independently before scaling it back.
        h={}
        if mean:M.addlog(h,mean*mean,1/(mean*mean))
        certify(M.combine((-Q(1),h)),2*var)
        es=charge(P[s],v)
        margin=M.combine((2*(k-1)*P[s],{2:Q(1)}),(-Q(1),es))
        certify(margin,2*above)
        local.append(es);supcost+=2*above;profilechecks+=1
    D=M.delta(P);E=M.ent(P,p)
    ck(E==M.combine(*[(Q(1),d) for d in local]))
    ck(supcost==2*sum(((2**s.bit_count()-2)*z for s,z in enumerate(P) if s),Q(0)))
    certify(M.combine((2*D,{2:Q(1)}),(-Q(1),E)),supcost)
    if degree<=3:
        degree3cases+=1
        B=sum((z for s,z in enumerate(P) if s.bit_count()==2),Q(0));T=sum((z for s,z in enumerate(P) if s.bit_count()==3),Q(0))
        ck(D==B+2*T)
        single=M.combine(*[(Q(1),d) for s,d in enumerate(local,1) if s.bit_count()==1])
        pair=M.combine(*[(Q(1),d) for s,d in enumerate(local,1) if s.bit_count()==2])
        triple=M.combine(*[(Q(1),d) for s,d in enumerate(local,1) if s.bit_count()==3])
        certify(M.combine((-Q(1),single)),4*B+6*T)
        certify(M.combine((2*B,{2:Q(1)}),(-Q(1),pair)),6*T)
        certify(M.combine((4*T,{2:Q(1)}),(-Q(1),triple)))
        certify(M.combine((2*D,{2:Q(1)}),(-Q(1),E)),6*D)
    if review:
        alpha,e,d,q=p[0],1-p[1],1-p[2],p[3]
        u=4*alpha*(1-alpha);vx=4*e*(1-e);vy=4*d*(1-d);w=4*q*(1-q)
        Tx=u*vx*w/16;Ty=u*vy*w/16;T=Tx+Ty
        G={}
        for coeff,t in [(2*T,q),(2*Tx,alpha),(2*Ty,1-alpha)]:M.addlog(G,coeff*t/(1-t),1/t)
        if d!=e:M.addlog(G,u*w/4*(d-e)**2,1/(d-e)**2)
        G=M.combine((Q(1),G))
        high=M.ent([z if s.bit_count()>=2 else Q(0) for s,z in enumerate(P)],p)
        ck(high==M.combine((2*D,{2:Q(1)}),(Q(1),G)))
        ck(P[11]==Tx and P[13]==Ty)
        certify(M.combine((-Q(1),G)),6*T)
for mask in range(256):
    for p in [(Q(1,2),)*3,(Q(1,4),Q(1,2),Q(3,4))]:test(mask,3,p)
for p in product((Q(1,4),Q(1,2),Q(3,4)),repeat=4):test(56067,4,p,review=True)
for mask in [0,65535,56067,33152,32768,1,27030,38505,42405,43690]:
    for p in [(Q(1,2),)*4,(Q(1,4),)*4,(Q(3,4),)*4,(Q(1,4),Q(1,2),Q(3,4),Q(1,2))]:test(mask,4,p)
ck(cases==633)
out={'result':'PASS','helper_version':'A044-stage5-integer-profile-v1','total_cases':cases,'degree_at_most_three_cases':degree3cases,'mixed_profile_checks':profilechecks,'exact_assertions':assertions+M.checks,'runtime_seconds':time.perf_counter()-start,'review_scope':'A043 global upper bound and exact pair/triple ledger; lower joint path and polynomial witness not independently accepted','parity_congestion':'Analytic all-d formula: pair cost/Delta=d; full upper ledger2(2^d-2); actual entropy0','full_FEI':'OPEN'}
(ROOT/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
