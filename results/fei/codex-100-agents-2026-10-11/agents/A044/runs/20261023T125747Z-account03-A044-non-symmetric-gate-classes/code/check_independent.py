from pathlib import Path
import json,time,hashlib
import independent_base as b
F=b.F;root=b.root;start=time.perf_counter()
def vals(mask,n):return [F(1 if mask>>x&1 else -1) for x in range(1<<n)]
def descr(d):
 c,P,W,_,w,Z=d;n=len(P);E1=L1=Lhi=(F(0),F(0));Jh=F(0)
 M=sum(P[s] for s in range(1,n) if s.bit_count()>=2)
 H=sum(W[s] for s in range(1,n) if s.bit_count()>=2)
 Q=list(P)
 for s in range(1,n):
  if s.bit_count()>=2:Q[s]=M*W[s]/H if M else F(0)
  if not P[s]:continue
  k=b.cell(abs(c[s]));u=abs(c[s])*2**k
  term=b.times(P[s],b.log(1/u**2))
  if s.bit_count()==1:
   E1=b.plus(E1,b.times(P[s],b.log(1/c[s]**2)));L1=b.plus(L1,term)
  else:Lhi=b.plus(Lhi,term);Jh+=P[s]*k
 normal=b.times(M,b.log(H/M)) if M else (F(0),F(0))
 return dict(c=c,P=P,W=W,w=w,M=M,Q=Q,E1=E1,L1=L1,Lhi=Lhi,Jh=Jh,n=normal,K=b.KL(P,Q))
def eq(a,c):
 gap=b.minus(a,c);b.ck(gap[0]<=0<=gap[1])
count=0
for mask in (1,6,8):
 for l,r in ((1,6),(6,8)):
  for p in ((F(1,2),)*4,(F(1,4),F(1,3),F(2,3),F(3,4))):
   fs=[vals(l,2),vals(r,2)];ch=[descr(b.direct(fs[0],p[:2])),descr(b.direct(fs[1],p[2:]))]
   g=vals(mask,2);gd=descr(b.direct(g,tuple((1+x['c'][0])/2 for x in ch)))
   f=[g[int((fs[0][x&3]+1)/2)+2*int((fs[1][x>>2]+1)/2)] for x in range(16)]
   fd=descr(b.direct(f,p));a=[];bb=[]
   for i in range(2):
    inf=sum(gd['P'][s] for s in range(4) if s>>i&1)
    a.append(inf/ch[i]['w']);bb.append((inf-gd['P'][1<<i])/ch[i]['w'])
   T=F(0);V=(F(0),F(0));source1=gd['E1'];sourceL=gd['Lhi'];sourceJ=gd['Jh'];nt=gd['n'];kt=gd['K'];C=F(0)
   for i,child in enumerate(ch):
    s=1<<i;wt=gd['P'][s]*child['M']/child['w']
    if wt:
     j=b.cell(abs(gd['c'][s]));T+=wt*j
     V=b.plus(V,b.times(wt,b.log(1/(abs(gd['c'][s])*2**j)**2)))
    J1=sum(child['P'][s]*b.cell(abs(child['c'][s])) for s in (1,2) if child['P'][s])
    T+=bb[i]*J1;V=b.plus(V,b.times(bb[i],child['L1']))
    source1=b.plus(source1,b.times(a[i],child['E1']));sourceL=b.plus(sourceL,b.times(a[i],child['Lhi']));sourceJ+=a[i]*child['Jh']
    nt=b.plus(nt,b.times(a[i],child['n']));kt=b.plus(kt,b.times(a[i],child['K']))
   qt=[gd['Q'][0]]+[F(0)]*15
   for s in range(1,16):
    ts=[s&3,s>>2];A=int(bool(ts[0]))+2*int(bool(ts[1]));q=gd['Q'][A]
    for i in range(2):
     if ts[i]:q*=ch[i]['Q'][ts[i]]/ch[i]['w']
    qt[s]=q
    if not fd['P'][s]:continue
    base=b.cell(abs(gd['c'][A]))+sum(b.cell(abs(ch[i]['c'][ts[i]])) for i in range(2) if ts[i])
    k=b.cell(abs(fd['c'][s]))-base;b.ck(k>=0)
    if s.bit_count()>=2:C+=fd['P'][s]*k
    else:b.ck(q==fd['P'][s])
   b.ck(sum(qt)==1 and qt[0]==fd['P'][0])
   b.ck(fd['Jh']==sourceJ+C+T)
   eq(source1,b.plus(b.plus(fd['E1'],V),b.times(2*T,b.LN2)))
   eq(b.plus(sourceL,V),b.plus(fd['Lhi'],b.times(2*C,b.LN2)))
   eq(b.KL(fd['P'],qt),kt)
   eq(b.minus(fd['K'],kt),b.minus(b.plus(b.times(2*C,b.LN2),fd['n']),b.plus(V,nt)))
   count+=1
   assert time.perf_counter()-start<55
b.ck(count==12)
out={'status':'PASS','cases':count,'exact_assertions':b.checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'direct mixed differences; Fraction; rigorous 32-term atanh intervals','runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'base_sha256':hashlib.sha256((root/'code/independent_base.py').read_bytes()).hexdigest()}
(root/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
