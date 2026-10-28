from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261014T054454Z-account05-A014-overlap-beyond-worst-case-read/code/check.py'
exec(compile(OLD.read_text(encoding='utf-8').split('rows=[];candidates=0;sets=0;wins=')[0],str(OLD),'exec'),globals())
budget=300
def clique_mass(n,k):
 r=k//2;lam=F(1,n-1)
 val=F(math.factorial(2*r),2**r*math.factorial(r))*(lam/48)**r
 if k%2:val*=(2*r+1)*lam*F(3*n-k-2,96)
 return val
scalar=[];masspairs=0;costs=[]
for n in range(3,65):
 fs=[clique_mass(n,k) for k in range(1,n+1)]
 Z=sum(F(math.comb(n,k))*fs[k-1] for k in range(1,n+1));ck(Z>0 and Z**12<=2**n)
 for val in fs:ck(val>0 and val**4*2**(27*n)>=1);masspairs+=1
 s=F(n+1,2**n);v=4*s*(1-s);I=F(n*(n-1),2**(n-1))
 weights=[F(4*math.comb(n,k)*(n+1-2*k)**2,4**n) for k in range(1,n+1)]
 ck(sum(weights)==v);ck(sum(F(k)*a for k,a in enumerate(weights,1))==I);ck(v/I<=F(4,n))
 if n<=16:
  CEfull=CE([v,1-v],[v,1-v])
  for k,val in enumerate(fs,1):
   p=F(4*math.comb(n,k)*(n+1-2*k)**2,4**n)
   if p:
    a,b=lg(Z/val);CEfull=(CEfull[0]+p*a,CEfull[1]+p*b)
  ck(CEfull[1]<32*I)
  costs.append({'n':n,'I':str(I),'normalized_full_CE_over_I':outward((CEfull[0]/I,CEfull[1]/I))})
 scalar.append({'n':n,'Z_F':str(Z),'min_F':str(min(fs))})
directsets=0
for n in (3,4,5):
 edges=list(itertools.combinations(range(n),2));lam=F(1,n-1);D=(1+lam/4)**len(edges)-1
 for A in range(1,1<<n):
  ck(D*occupation(n,edges,A,lam,D)==clique_mass(n,A.bit_count()));directsets+=1
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def half(a):return a[0]/2,a[1]/2
def intersects(a,b):return a[0]<=b[1] and b[0]<=a[1]
def direct_spectrum(vals):
 return tuple(F(sum(val*(-1 if (z&A).bit_count()%2 else 1) for z,val in enumerate(vals))**2,len(vals)**2) for A in range(len(vals)))
@lru_cache(None)
def policies(vals,q):
 n=(len(vals)-1).bit_length();p=direct_spectrum(vals);v=1-p[0]
 if not n:return (((F(0),F(0)),(F(0),F(0))),)
 parent=CE(p,(1-v,)+tuple(v*a for a in q[1:]))
 results=[((F(0),F(0)),parent)]
 for i in range(n):
  private=[u for u in range(n) if u!=i]
  if n==1:qbar=(F(0),)
  else:
   qbar=(F(0),)+tuple((q[sum(((T>>j)&1)<<u for j,u in enumerate(private))]+q[sum(((T>>j)&1)<<u for j,u in enumerate(private))|(1<<i)])/(1-q[1<<i]) for T in range(1,1<<(n-1)))
   ck(sum(qbar)==1)
  cvs=[tuple(vals[(b<<i)+sum(((z>>j)&1)<<u for j,u in enumerate(private))] for z in range(1<<(n-1))) for b in (0,1)]
  childcost=[]
  for cv in cvs:
   cp=direct_spectrum(cv);cvv=1-cp[0]
   childcost.append(CE(cp,(1-cvv,)+tuple(cvv*a for a in qbar[1:])))
  debit=sub(parent,half(add(*childcost)));ck(debit[0]>=0)
  for a in policies(cvs[0],qbar):
   for b in policies(cvs[1],qbar):
    booked=add(debit,half(add(a[0],b[0])));terminal=half(add(a[1],b[1]));ck(intersects(add(booked,terminal),parent))
    results.append((booked,terminal))
 return tuple(results)
vals=tuple(1-2*int(z.bit_count()<=1) for z in range(8));fs=[F(0)]+[clique_mass(3,A.bit_count()) for A in range(1,8)];z=sum(fs);q=tuple(t/z for t in fs)
history=policies(vals,q);ck(len(history)==244)
out={'helper':'A014-clique-closed-mass-and-original-history-v1','mass_pairs':masspairs,'scalar_n':[3,64],'full_cost_n':[3,16],'direct_occupation_sets':directsets,'adaptive_stopping_policies':len(history),'distinct_restriction_states':policies.cache_info().currsize,'assertions':assertions,'elapsed_seconds':time.monotonic()-start,'costs':costs,'scalar':scalar}
(R/'out/extension.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('costs','scalar')}))
