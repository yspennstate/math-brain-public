from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
root=Path(__file__).resolve().parents[1]
assert (root/'out/FROZEN_SPEC.json').exists()
start=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x;checks+=1
    if checks%1000==0:assert time.perf_counter()-start<55
@lru_cache(None)
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
@lru_cache(None)
def log(x):
    assert x>0
    a=dict(factors(x.numerator))
    for p,e in factors(x.denominator).items():a[p]=a.get(p,0)-e
    return {p:F(e) for p,e in a.items() if e}
def scale(x,a):return {p:x*c for p,c in a.items() if x*c}
def add(*args):
    out={}
    for a in args:
        for p,c in a.items():out[p]=out.get(p,0)+c
    return {p:c for p,c in out.items() if c}
def sub(a,b):return add(a,scale(-1,b))
def j(t):
    k=0
    while t<=F(1,2):t*=2;k+=1
    return k
def vals(mask,n):return [F(1 if mask>>x&1 else -1) for x in range(1<<n)]
def data(f,p):
    n=len(p);N=1<<n;c=list(f);v=[F(1)]*N
    for i,q in enumerate(p):
        for x in range(N):
            if x>>i&1:continue
            a,b=c[x],c[x|1<<i]
            c[x]=(1-q)*a+q*b;c[x|1<<i]=(b-a)/2
    for S in range(1,N):
        bit=S&-S;i=bit.bit_length()-1
        v[S]=v[S^bit]*4*p[i]*(1-p[i])
    P=[v[S]*c[S]**2 for S in range(N)]
    js=[j(abs(c[S])) if S and c[S] else 0 for S in range(N)]
    u=[abs(c[S])*2**js[S] for S in range(N)]
    W=[v[S]/4**js[S] if S and c[S] else F(0) for S in range(N)]
    D=sum((S.bit_count()-1)*P[S] for S in range(1,N))
    R=sum((S.bit_count()-2)*P[S] for S in range(1,N) if S.bit_count()>=3)
    M=sum(P[S] for S in range(1,N) if S.bit_count()>=2)
    H=sum(W[S] for S in range(1,N) if S.bit_count()>=2)
    E1={};L1={};Lhi={};J1=Jhi=F(0)
    Q=list(P)
    for S in range(1,N):
        if S.bit_count()>=2:Q[S]=M*W[S]/H if M else F(0)
        if not P[S]:continue
        ck(F(1,2)<u[S]<=1)
        if S.bit_count()==1:
            E1=add(E1,scale(P[S],log(1/c[S]**2)))
            L1=add(L1,scale(P[S],log(1/u[S]**2)));J1+=P[S]*js[S]
        else:
            Lhi=add(Lhi,scale(P[S],log(1/u[S]**2)));Jhi+=P[S]*js[S]
    I=[sum(P[S] for S in range(N) if S>>i&1) for i in range(n)]
    ck(sum(P)==sum(Q)==1);ck(M==D-R)
    ck(sum(I[i]-P[1<<i] for i in range(n))==2*D-R)
    for i,q in enumerate(p):ck(I[i]/(4*q*(1-q))>=abs(c[1<<i]))
    normal=scale(M,log(H/M)) if M else {}
    K={}
    for p0,q0 in zip(P,Q):
        if p0:K=add(K,scale(p0,log(p0/q0)))
    ck(K==sub(normal,Lhi))
    return dict(c=c,P=P,j=js,u=u,W=W,w=1-P[0],D=D,R=R,M=M,H=H,Q=Q,E1=E1,L1=L1,Lhi=Lhi,J1=J1,Jhi=Jhi,I=I,n=normal,K=K)

comps=positiveT=positiveV=positiveC=0
for mask in range(16):
 for l in (1,6,8):
  for r in (1,6,8):
   for p in ((F(1,2),)*4,(F(1,4),F(1,3),F(2,3),F(3,4))):
    fs=[vals(l,2),vals(r,2)];cs=[data(fs[0],p[:2]),data(fs[1],p[2:])]
    g=vals(mask,2);gd=data(g,tuple((1+d['c'][0])/2 for d in cs))
    f=[g[int((fs[0][x&3]+1)/2)+2*int((fs[1][x>>2]+1)/2)] for x in range(16)]
    fd=data(f,p)
    aa=[gd['I'][i]/cs[i]['w'] for i in range(2)]
    bb=[(gd['I'][i]-gd['P'][1<<i])/cs[i]['w'] for i in range(2)]
    T=F(0);V={};B={};C=F(0)
    E1source=gd['E1'];Lhisource=gd['Lhi'];Jhisource=gd['Jhi'];ntree=gd['n'];Ktree=gd['K']
    for i,ch in enumerate(cs):
        s=1<<i;weight=gd['P'][s]*ch['M']/ch['w']
        T+=weight*gd['j'][s]+bb[i]*ch['J1']
        if weight:
            V=add(V,scale(weight,log(1/gd['u'][s]**2)))
            B=add(B,scale(weight,log(1/gd['c'][s]**2)))
        V=add(V,scale(bb[i],ch['L1']));B=add(B,scale(bb[i],ch['E1']))
        E1source=add(E1source,scale(aa[i],ch['E1']))
        Lhisource=add(Lhisource,scale(aa[i],ch['Lhi']))
        Jhisource+=aa[i]*ch['Jhi']
        ntree=add(ntree,scale(aa[i],ch['n']));Ktree=add(Ktree,scale(aa[i],ch['K']))
    ck(T>=0);ck(sub(E1source,fd['E1'])==B)
    ck(B==add(scale(2*T,{2:F(1)}),V))
    qt=[gd['Q'][0]]+[F(0)]*15
    for S in range(1,16):
        ts=[S&3,S>>2];A=int(bool(ts[0]))+2*int(bool(ts[1]))
        coeff=gd['c'][A];q=gd['Q'][A];base=gd['j'][A]
        for i in range(2):
            if ts[i]:
                coeff*=cs[i]['c'][ts[i]];q*=cs[i]['Q'][ts[i]]/cs[i]['w'];base+=cs[i]['j'][ts[i]]
        ck(coeff==fd['c'][S]);qt[S]=q
        if not fd['P'][S]:continue
        k=fd['j'][S]-base;ck(k>=0)
        if S.bit_count()>=2:C+=fd['P'][S]*k
        if S.bit_count()==1:ck(q==fd['P'][S])
    ck(sum(qt)==1 and qt[0]==fd['P'][0])
    ck(fd['Jhi']==Jhisource+C+T)
    ck(add(scale(2*C,{2:F(1)}),fd['Lhi'])==add(Lhisource,V))
    Kactual={}
    for p0,q0 in zip(fd['P'],qt):
        if p0:Kactual=add(Kactual,scale(p0,log(p0/q0)))
    ck(Kactual==Ktree)
    ck(sub(fd['K'],Ktree)==add(scale(2*C,{2:F(1)}),scale(-1,V),fd['n'],scale(-1,ntree)))
    ck(fd['D']==gd['D']+sum(aa[i]*cs[i]['D'] for i in range(2)))
    comps+=1;positiveT+=T>0;positiveV+=bool(V);positiveC+=C>0

towers=[]
for d in range(1,13):
    Delta=F(3,2)**d-1;E1=F(d)*F(3,4)**d
    T=F(3,2)*Delta-E1;Rtree=Delta/2
    singleton_source=F(3,2)*Delta
    ck(T+E1==singleton_source)
    ck(T>=0 and 2*(T+E1)<=4*Delta-2*Rtree)
    if d==4:ck(T-Delta==F(49,64))
    towers.append({'depth':d,'Delta':str(Delta),'T_over_ln4':str(T),'E1_over_ln4':str(E1),'mantissa_refund':'0'})
ck(comps==288)
out={'status':'PASS','composition_cases':comps,'compressed_tower_depths':12,'positive_import_cases':positiveT,'positive_import_refund_cases':positiveV,'positive_high_carry_cases':positiveC,'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction; exact prime-exponent logarithm vectors; support and likelihood identities checked pointwise','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'full_FEI':'OPEN'}
(root/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
(root/'out/TOWERS.json').write_text(json.dumps(towers,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
