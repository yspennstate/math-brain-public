from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json,time,sys
import mathcore as m
ROOT=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv;m.limit=55 if pilot else 175
e_lo=sum((F(1,factorial(j)) for j in range(21)),F(0))
e_hi=e_lo+F(22,21*factorial(21));curvature=8/e_lo
cases=trees=0;max_n=0
def T(p):
 return m.add((m.entropy([(1-2*p)**2]),1),(m.entropy([p*p]),-4),({2:8*p*(1-p)},-1))
def mean_ent(pxs):
 p=sum(pxs,F(0))/len(pxs);v=m.entropy([p])
 for x in pxs:v=m.add((v,1),(m.entropy([x]),-F(1,len(pxs))))
 return v
def check(g,A):
 global cases,max_n
 cases+=1;max_n=max(max_n,len(g).bit_length()-1)
 f=tuple(1-2*v for v in g);p=m.mass(g);gc=m.children(g,A);pxs=[m.mass(v) for v in gc]
 E=m.energy(g,A);I=m.energy(f,A)
 m.ck(I==4*E);m.ck(E==m.edges(g,A));m.ck(m.spec(g)==m.direct(g))
 m.ck(m.raw(f)==m.add((m.raw(g),4),(T(p),1)))
 correction=T(p)
 for v in gc:
  pv=m.mass(v);fv=tuple(1-2*x for x in v)
  m.ck(m.raw(fv)==m.add((m.raw(v),4),(T(pv),1)))
  correction=m.add((correction,1),(T(pv),-F(1,len(gc))))
 Lg=m.ledger(g,A)[0];Lf=m.ledger(f,A)[0]
 m.ck(m.add((Lf,1),(Lg,-4))==correction)
 ent=mean_ent(pxs);m.nonneg(ent)
 m.nonneg(m.add((ent,curvature),(correction,-1)))
 m.ck(m.interval(ent)[1]<=2*E)
 m.ck(m.interval(correction)[1]<=(16/e_lo)*E)
 if E==0:m.ck(not correction and not Lg and not Lf)
 return dict(p=p,indicator_energy=E,sign_influence=I,correction=m.vec(correction),mass_tilt=m.vec(ent),sign_drop=m.vec(Lf),raw_drop=m.vec(Lg))
def tree(g,depth):
 global trees
 trees+=1;f=tuple(1-2*v for v in g)
 leaves=[(g,F(1))];cumT={};cumL={};cumH={};cumE=F(0)
 for _ in range(depth):
  nxt=[]
  for v,w in leaves:
   p=m.mass(v);ch=m.children(v,1);fv=tuple(1-2*x for x in v)
   cumE+=w*m.energy(v,1)
   cumL=m.add((cumL,1),(m.ledger(v,1)[0],w))
   cumH=m.add((cumH,1),(m.ledger(fv,1)[0],w))
   d=T(p)
   for q in ch:d=m.add((d,1),(T(m.mass(q)),-F(1,2)));nxt.append((q,w/2))
   cumT=m.add((cumT,1),(d,w))
  leaves=nxt
 rawdelta=m.raw(g);signdelta=m.raw(f);Td=T(m.mass(g));leafE=F(0)
 for v,w in leaves:
  rawdelta=m.add((rawdelta,1),(m.raw(v),-w))
  signdelta=m.add((signdelta,1),(m.raw(tuple(1-2*x for x in v)),-w))
  Td=m.add((Td,1),(T(m.mass(v)),-w));leafE+=w*m.energy(v,len(v)-1)
 m.ck(cumL==rawdelta and cumH==signdelta and cumT==Td)
 m.ck(cumE==m.energy(g,len(g)-1)-leafE)
 m.ck(m.add((signdelta,1),(rawdelta,-4))==Td)
 m.ck(m.interval(Td)[1]<=(16/e_lo)*cumE)
tables=0
for n in range(3 if pilot else 4):
 for mask in range(1<<(1<<n)):
  g=tuple(mask>>x&1 for x in range(1<<n));tables+=1
  for A in range(1,1<<n):check(g,A)
  if n:
   for depth in sorted({1,n}):tree(g,depth)
N=128;a=tuple(int((x&15).bit_count()<=1) for x in range(N));b=tuple(int(x==15) for x in range(N));brain45=tuple(x+y for x,y in zip(a,b))
for A in ([15] if pilot else range(1,127)):check(brain45,A)
if not pilot:
 N=512;a=tuple(int((x&31).bit_count()<=1) for x in range(N));b=tuple(int(x==31) for x in range(N));check(tuple(x+y for x,y in zip(a,b)),31)
base=[0]*32
for j,x in enumerate([0,1,2]):base[x]=1;base[x+16]=int(j==0)
for j,x in enumerate([12,13,14]):base[x]=1;base[x+16]=int(j==1)
rare=[]
for width in ([0,2] if pilot else range(7)):
 g=tuple(base[x] if x<32 else 0 for x in range(32*(1<<width)))
 m.ck(len(m.components(g))==2)
 rec=check(g,15);p=rec['p'];E=rec['indicator_energy'];I=rec['sign_influence']
 q=m.add((m.logv(F(3,16)),-p))
 m.nonneg(m.add((q,1),({2:2*p},-1)))
 m.ck(E>=p)
 L=m.ledger(tuple(1-2*x for x in g),15)[0]
 natural_price=m.add(({2:4*I},1),(L,-1))
 m.ck(m.interval(natural_price)[0]+(2+4/e_lo)*I>=0)
 rec.update(width=width,dimension=5+width,projection_sizes=[3,3],noncartesian=True)
 rare.append(rec)
m.ck(8/e_lo<3)
lnlo,lnhi=m.logbound(2)
c_lo=4+2/lnhi+4/(e_hi*lnhi);c_hi=4+2/lnlo+4/(e_lo*lnlo)
m.ck(c_hi<F(37,4))
m.save('PILOT_RARE.json' if pilot else 'RARE_PROFILE.json',rare)
result=dict(status='PASS',pilot=pilot,tables=tables,block_cases=cases,tree_cases=trees,max_dimension=max_n,rare_cases=len(rare),assertions=m.checks,seconds=time.perf_counter()-m.start,e_interval=[e_lo,e_hi],projection_price_interval=[c_lo,c_hi],density_hypothesis_removed=True)
m.save('PILOT.json' if pilot else 'EXACT_CHECK.json',result)
print(json.dumps({k:v for k,v in result.items() if k not in ['e_interval','projection_price_interval']},indent=2))
