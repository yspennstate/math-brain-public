from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import time,json,hashlib
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v;checks+=1
 if time.perf_counter()-start>55:raise TimeoutError('audit55s')
def rank(rows):
 a=[[F(x) for x in row] for row in rows];r=0
 for j in range(len(a[0])):
  pivot=next((k for k in range(r,len(a)) if a[k][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];d=a[r][j];a[r]=[v/d for v in a[r]]
  for k in range(len(a)):
   if k!=r and a[k][j]:
    d=a[k][j];a[k]=[x-d*y for x,y in zip(a[k],a[r])]
  r+=1
 return r
mobius=[];calibration=[]
for m in (1,2,3,4,5):
 N=1<<m;rows=[[int(U&T==T) for U in range(N)] for T in range(N-1)]+[[int(U==0) for U in range(N)]]
 r=rank(rows);ck(r==N);mobius.append({'residual_dimension':m,'rank':r,'columns':N})
for n in (0,1,2,3):
 N=1<<n;rows=[[1]*N,[int(S==0) for S in range(N)]]+[[int(bool(S&(1<<i))) for S in range(N)] for i in range(n)]
 r=rank(rows);ck(r==(1,2,4,5)[n]);calibration.append({'dimension':n,'rank':r,'columns':N})
def spectrum(t):
 N=len(t)
 return {s:F(v*v,N*N) for s in range(N) if (v:=sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(t)))}
def marg(p,i):
 q=defaultdict(F)
 for s,v in p.items():q[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=v
 return dict(q)
def pf(n):
 a={};k=2
 while k*k<=n:
  while n%k==0:a[k]=a.get(k,0)+1;n//=k
  k+=1
 if n>1:a[n]=a.get(n,0)+1
 return a
def kl(p,q):
 d=defaultdict(F)
 for s,v in p.items():
  z=v/q[s]
  for k,c in pf(z.numerator).items():d[k]+=v*c
  for k,c in pf(z.denominator).items():d[k]-=v*c
 return {s:v for s,v in d.items() if v}
def infl(p):return [sum(v for s,v in p.items() if s&(1<<i)) for i in range(3)]
def control(label,p,q,i):
 ck(sum(p.values())==sum(q.values())==1);ck(all(q.get(s,F())>0 for s in p));ck(p!=q)
 ck(kl(p,q)==kl(marg(p,i),marg(q,i)))
 return {'label':label,'query':i,'P':{str(s):str(v) for s,v in p.items()},'Q':{str(s):str(v) for s,v in q.items()},'root_KL_prime_log_bits':{str(s):str(v) for s,v in kl(p,q).items()},'erasure_KL':0}
mux=tuple((-1 if ((x>>(0 if not x&4 else 1))&1) else 1) for x in range(8))
p=spectrum(mux);q={1:F(5,16),2:F(3,16),5:F(3,16),6:F(5,16)}
ck(p.get(0,F())==q.get(0,F()));ck(infl(p)==infl(q));ck(len(p)==4)
controls=[control('Drop full support: actual Boolean mux3, vacuum and all influences still match',p,q,0)]
p={s:F(1,8) for s in range(8)}
q={s:F(5 if (s&3).bit_count()%2==0 else 3,32) for s in range(8)}
ck(infl(p)==infl(q));ck(p[0]!=q[0]);controls.append(control('Drop vacuum: positive law, first moments still match; not an FEI spectral claim',p,q,2))
q={s:F(1,8)+(F(1,64) if s&3==1 else F(-1,64) if s&3==2 else 0) for s in range(8)}
ck(q[0]==p[0]);ck(infl(p)!=infl(q));controls.append(control('Drop moments: positive law, vacuum still matches; not an FEI spectral claim',p,q,2))
lean='''import Lean.Elab.Tactic.Omega

theorem residual_two_bit_inversion (a b c d : Int)
    (h0 : a = 0) (hn : a + b + c + d = 0)
    (hx : b + d = 0) (hy : c + d = 0) :
    a = 0 ∧ b = 0 ∧ c = 0 ∧ d = 0 := by
  omega
'''
(R/'code/Residual.lean').write_bytes(lean.encode('utf-8'))
result={'status':'PASS','checks':checks,'mobius_ranks':mobius,'calibration_ranks':calibration,'hypothesis_drop_controls':controls,'seconds':time.perf_counter()-start,'lean_source_sha256':hashlib.sha256(lean.encode()).hexdigest(),'lean_scope':'Only residual dimension2 inversion in Int; full entropy proof remains analytic'}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','checks','seconds','lean_source_sha256']}))
