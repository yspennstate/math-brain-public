from pathlib import Path
from fractions import Fraction as Q
import json,time,hashlib

ROOT=Path(__file__).resolve().parents[1]
spec=json.loads((ROOT/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
start=time.perf_counter();checks=0
def ck(b):
    global checks
    assert b
    checks+=1
    if checks%1000==0:assert time.perf_counter()-start<55
def cell(t):
    assert 0<t<=1
    j=0
    while t<=Q(1,2):t*=2;j+=1
    return j
def data(f,p):
    n=len(p);c=list(f);v=[Q(1)]*(1<<n)
    for i,q in enumerate(p):
        for x in range(1<<n):
            if x>>i&1:continue
            a,b=c[x],c[x|1<<i]
            c[x]=(1-q)*a+q*b;c[x|1<<i]=(b-a)/2
    for s in range(1,1<<n):
        bit=s&-s;i=bit.bit_length()-1
        v[s]=v[s^bit]*4*p[i]*(1-p[i])
    P=[v[s]*c[s]**2 for s in range(1<<n)]
    j=[cell(abs(c[s])) if s and c[s] else 0 for s in range(1<<n)]
    W=[v[s]/4**j[s] if s and c[s] else Q(0) for s in range(1<<n)]
    w=1-P[0];D=sum((s.bit_count()-1)*P[s] for s in range(1,1<<n))
    R=sum((s.bit_count()-2)*P[s] for s in range(1,1<<n) if s.bit_count()>=3)
    A=sum(P[1<<i] for i in range(n));M=w-A;Z=sum(W)
    flat=[P[0]]+[w*W[s]/Z if w else Q(0) for s in range(1,1<<n)]
    high=sum(W[s] for s in range(1,1<<n) if s.bit_count()>=2)
    star=[P[s] if s==0 or s.bit_count()==1 else M*W[s]/high if M else Q(0) for s in range(1<<n)]
    return dict(c=c,v=v,P=P,j=j,W=W,w=w,D=D,R=R,A=A,M=M,Z=Z,H=high,flat=flat,star=star,J=sum(P[s]*j[s] for s in range(1,1<<n)))
def refs(d):
    P=d['P'];w=d['w'];M=d['M'];A=d['A'];Z=d['Z'];H=d['H']
    ck(sum(P)==sum(d['flat'])==sum(d['star'])==1)
    ck(M==d['D']-d['R'])
    ck(0<=Z-w<=9*d['D']-6*d['R'])
    ck((M<=H<4*M) if M else H==0)
    Z1=Z-H
    for s in range(len(P)):
        ck(bool(P[s])==bool(d['flat'][s])==bool(d['star'][s]))
        if not s or not P[s]:continue
        u2=P[s]/d['W'][s]
        ck(Q(1,4)<u2<=1)
        ck(P[s]/d['flat'][s]==u2*Z/w)
        if s.bit_count()>=2:ck(P[s]/d['star'][s]==u2*H/M)
        else:ck(P[s]/d['star'][s]==1)
        # KL_flat-KL_star chain rule checked by the exact atom ratio.
        if s.bit_count()==1:
            within=(P[s]/A)/(d['W'][s]/Z1)
            sector=(A/w)/(Z1/Z)
            ck(d['star'][s]/d['flat'][s]==within*sector)
        else:ck(d['star'][s]/d['flat'][s]==(M/w)/(H/Z))

seeds=acts=dyadic=positive=0
laws=[(Q(1,2),)*3,(Q(1,4),Q(1,2),Q(3,4))]
for mask in range(256):
    f=[Q(1 if mask>>x&1 else -1) for x in range(8)]
    for p in laws:
        gd=data(f,p);refs(gd);seeds+=1
        a=(1-gd['c'][0])/2;V=gd['w']
        for e in (Q(1,4),Q(1,2),Q(3,4),Q(7,8)):
            # Physical ordering: seed bits first, selector last.
            fd=data([Q(1)]*8+f,p+(e,));refs(fd);acts+=1
            ck(fd['c'][0]==1-2*a*e)
            ck(fd['c'][8]==-a)
            ck(fd['w']==4*a*e*(1-a*e))
            Do=e*(1-e)*V
            ck(fd['D']==e*gd['D']+Do)
            if not V:
                ck(a in (0,1));ck(fd['D']==fd['J']==0)
                continue
            b=cell(e);d=cell(a);C=Q(0)
            # Gate sign ordering: selector is bit0, seed sign bit1 (+ sign=1).
            gate=[Q(1),Q(-1),Q(1),Q(1)]
            od=data(gate,(e,1-a));refs(od)
            ck(od['D']==Do and od['w']==fd['w'])
            ck(od['J']==e*e*V*b+4*e*(1-e)*a*a*d+Do)
            ck(od['J']<=3*Do)
            ck(b*e<=1-e and d*a<=1-a)
            qt=[od['flat'][0]]+[Q(0)]*15;qt[8]=od['flat'][1]
            Zformula=4*e*(1-e)/4**d+e*(1-e)*gd['Z']
            for T in range(1,8):
                ck(fd['c'][T]==e*gd['c'][T])
                ck(fd['c'][8|T]==gd['c'][T]/2)
                ck(fd['P'][T]==e*e*gd['P'][T])
                ck(fd['P'][8|T]==e*(1-e)*gd['P'][T])
                qt[T]=od['flat'][2]*gd['flat'][T]/V
                qt[8|T]=od['flat'][3]*gd['flat'][T]/V
                if not gd['P'][T]:continue
                k=fd['j'][T]-b-gd['j'][T]
                ck(k in (0,1));C+=e*e*gd['P'][T]*k
                ck(fd['j'][8|T]==1+gd['j'][T])
                ck(fd['W'][T]==gd['W'][T]/4**(b+k))
                ck(fd['W'][8|T]==e*(1-e)*gd['W'][T])
                Zformula+=gd['W'][T]/4**(b+k)
                # Complete tree KL chain rule, checked before taking logs.
                ck(fd['P'][T]/qt[T]==od['P'][2]/od['flat'][2]*gd['P'][T]/gd['flat'][T])
                ck(fd['P'][8|T]/qt[8|T]==od['P'][3]/od['flat'][3]*gd['P'][T]/gd['flat'][T])
            ck(sum(qt)==1 and qt[0]==fd['P'][0])
            ck(fd['P'][8]/qt[8]==od['P'][1]/od['flat'][1])
            ck(fd['Z']==Zformula)
            ck(fd['J']==e*gd['J']+od['J']+C)
            ck(0<=C<=e*e*V)
            if e in (Q(1,4),Q(1,2)):
                ck(C==0);dyadic+=1
                ck(fd['Z']==e*gd['Z']+4*e*(1-e)/4**d)
            if C:positive+=1

rows=[]
for m in range(3,27):
    t=Q(1,2**m);e=1-2*t;q=(1+t)/2;v=1-t*t
    seed=[Q(-1),Q(-1),Q(-1),Q(1)]
    gd=data(seed,(q,q));fd=data([Q(1)]*4+seed,(q,q,e))
    V=4*q*q*(1-q*q);Do=e*(1-e)*V
    C=2*e*e*v*q*q
    ck(gd['c'][1]==gd['c'][2]==q and gd['c'][3]==Q(1,2))
    ck(gd['j'][1]==gd['j'][2]==0 and gd['j'][3]==1)
    ck(fd['j'][1]==fd['j'][2]==fd['j'][3]==1)
    ck(cell(e)==0 and fd['D']==e*gd['D']+Do)
    observed=sum(fd['P'][s]*(fd['j'][s]-cell(e)-gd['j'][s]) for s in (1,2,3))
    ck(observed==C)
    ck(C/Do==e*(1+t)/(t*(3+t)))
    ck(C/Do>=Q(6,25)/t)
    rows.append({'m':m,'carry':str(C),'outer_deficit':str(Do),'ratio':str(C/Do),'lower_bound':str(Q(6,25)/t)})
ck(seeds==512 and acts==2048 and len(rows)==24)
(ROOT/'out/ADVERSARY.json').write_text(json.dumps({'status':'PASS','rows':rows,'all_dimension_proof':'PROOF.md equations (4)-(5)'},indent=2)+'\n',encoding='utf-8')
out={'status':'PASS','seed_reference_cases':seeds,'activation_cases':acts,'adversary_cases':len(rows),'dyadic_nonconstant_cases':dyadic,'positive_carry_cases':positive,'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction only; exact coefficient, reference normalization, atom likelihood and scale identities; logarithms handled analytically in PROOF.md','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'full_FEI':'OPEN'}
(ROOT/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
