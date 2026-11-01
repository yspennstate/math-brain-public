from fractions import Fraction as F
from pathlib import Path
from itertools import product
import time,json,hashlib
ROOT=Path(__file__).resolve().parents[1];START=time.monotonic();checks=0;fixtures=0;wrappers=0;proper=0
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
 if time.monotonic()-START>55:raise TimeoutError('frozen55s cap')
def fw(tt):
 w=list(tt);k=1
 while k<len(w):
  for s in range(0,len(w),2*k):
   for j in range(s,s+k):a,b=w[j],w[j+k];w[j],w[j+k]=a+b,a-b
  k*=2
 return tuple(F(z,len(w)) for z in w)
def law(tt):return tuple(z*z for z in fw(tt))
def fixture(p,q,t,delta,lam,zero):
 global fixtures
 ck(sum(p)==sum(q)==1)
 for k,w in enumerate(((0,1),(2,3))):
  ck(sum(q[i]*t[i] for i in w)==delta[k])
  for i in w:
   if p[i]:ck(abs(t[i])<1 and p[i]*t[i]/(1-t[i]*t[i])==lam[k]*q[i])
   elif lam[k]:ck(t[i]==(1 if lam[k]>0 else -1))
  ghost=sum(q[i] for i in w if not p[i]);ck((abs(delta[k])<=ghost)==zero)
 Rp=tuple(q0*(1+t0) for q0,t0 in zip(q,t));Rm=tuple(q0*(1-t0) for q0,t0 in zip(q,t))
 ck(sum(Rp)==sum(Rm)==1 and all(z>=0 for z in Rp+Rm))
 ck(tuple((x+y)/2 for x,y in zip(Rp,Rm))==q)
 ck(all(not p0 or (x>0 and y>0) for p0,x,y in zip(p,Rp,Rm)))
 ck(all(not p0 or t0==0 for p0,t0 in zip(p,t))==zero)
 fixtures+=1
for delta in (F(0),F(1,16),F(1,4)):
 fixture((F(1,2),0,F(1,2),0),(F(1,4),)*4,(0,4*delta,0,-4*delta),(delta,-delta),(0,0),True)
for t in (F(1,8),F(1,4),F(1,2),F(3,4)):
 d=(1+t)/4;lam=2*t/(1-t*t)
 fixture((F(1,2),0,F(1,2),0),(F(1,4),)*4,(t,1,-t,-1),(d,-d),(lam,-lam),False)
fixture((F(1,4),)*4,(F(9,50),F(16,50),F(9,50),F(16,50)),(F(1,3),F(1,2),F(-1,3),F(-1,2)),(F(11,50),F(-11,50)),(F(25,48),F(-25,48)),False)
for a in product((-1,0,1),repeat=4):
 b=tuple(1-z*z for z in a);A=fw(a);B=fw(b);beta=sum(z*z for z in B)
 for sig in (1,-1):
  tt=tuple(a[U]+sig*b[U]*(-1 if s.bit_count()%2 else 1) for s in range(16) for U in range(4));P=law(tt)
  ck(all(abs(z)==1 for z in tt))
  seed={9:F(1,2),10:F(1,4),15:F(1,4)}
  Q=tuple(A[U]**2 if T==0 else B[U]**2*seed.get(T,0) for T in range(16) for U in range(4))
  ck(sum(Q)==1 and all(not p or q>0 for p,q in zip(P,Q)))
  # Queried physical bit5 is the high seed bit; deterministic occupancy exactly matches at actual atoms.
  ck(all(not P[s] or (s>>5)==1 or s<4 for s in range(64)))
  qm=tuple(Q[s]+Q[s+32] for s in range(32))
  pm=tuple(P[s]+P[s+32] for s in range(32))
  rp={1:F(5,8),2:F(1,8),7:F(1,4)};rm={1:F(3,8),2:F(3,8),7:F(1,4)}
  refs=[tuple(A[U]**2 if T==0 else B[U]**2*seed0.get(T,0) for T in range(8) for U in range(4)) for seed0 in (rp,rm)]
  ck(all(sum(z)==1 for z in refs));ck(tuple((x+y)/2 for x,y in zip(*refs))==qm)
  for o in (0,1):
   child=tt[o*32:(o+1)*32];pc=law(child)
   ck(pc==pm)
   ck(all(not p or q1==q0 for p,q0,q1 in zip(pc,qm,refs[o])))
   ck(all(not P[s] or Q[s]==qm[s%32] for s in range(64)))
  edge=F(sum(tt[s]!=tt[s^32] for s in range(64)),64);ck(edge==beta)
  ck((refs[0]!=qm)==(beta>0));ck((refs[1]!=qm)==(beta>0))
  wrappers+=1;proper+=int(beta>0)
ck((fixtures,wrappers)==(8,162))
out={'status':'PASS','helper':'A033-independent-A031-capacity-v1','generic_exact_KKT_fixtures':fixtures,'actual_complete_wrappers':wrappers,'proper_free_profile_changes':proper,'exact_assertions':checks,'runtime_seconds':time.monotonic()-START,'source_statement_sha256':'5154fe677197066ec18283a4b119a2c82855bc0ccf5a5d4a924d1df395e44cc1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/review_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
