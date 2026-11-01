from pathlib import Path
from fractions import Fraction as F
from math import lcm
import json,time,hashlib
R=Path(__file__).resolve().parents[1]
spec={'version':'A085-direct-character-integer-power-v1','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'both original signed 7-bit wrappers and first seed children; 4 exact dyadic budget boundaries each at k-1,k; floor denominator24 including one ghost atom','case_count':'2 roots,4 converted children;8 integer budget inequalities; all positive support allocations with target>=8, total nonempty18 plus optional ghost','arithmetic':'direct character sums only, Fraction and integer powers; imports NO primary or author helper','symmetry':'none','memory_MB':50,'max_runtime_seconds':20}
(R/'out'/'AUDIT_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.monotonic();checks=0
def ck(x):
 global checks
 checks+=1;assert x
 if time.monotonic()-start>20:raise TimeoutError('frozen 20s cap')
def coeff(v):return tuple(F(sum(y*(-1 if (x&s).bit_count()%2 else 1) for x,y in enumerate(v)),len(v)) for s in range(len(v)))
def law(v):return tuple(x*x for x in coeff(v))
def restrict(v,j,b):return tuple(v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2))
def product(terms):
 M=lcm(*(e.denominator for _,e in terms));n=d=1
 for x,e in terms:
  e=int(e*M)
  if e<0:x=1/x;e=-e
  n*=x.numerator**e;d*=x.denominator**e
 return n,d,M
row=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);b=tuple(1-x*x for x in row)
h=tuple(-1 if x in (0,7) else 1 for x in range(8))
ac,bc=coeff(row),coeff(b)
source={};full=[]
for s in (1,-1):
 v=tuple(a+s*bb*z for z in h for a,bb in zip(row,b));p=law(v);source[s]=p
 ck(sum(p)==1 and all(abs(x)==1 for x in v))
 ck(all(coeff(v)[i]*coeff(v)[i^16]==0 for i in range(0,len(v),32) for i in range(i,i+16)))
 for bit in (0,1):
  hh=restrict(h,0,bit);vv=restrict(v,4,bit);pp=law(vv);m=F(sum(hh),len(hh));rr=(F(1,4),F(5,24),F(5,24),F(1,3))
  qq=tuple((ac[u]+s*m*bc[u])**2 if t==0 else bc[u]**2*rr[t] for t in range(4) for u in range(16))
  ck(sum(qq)==1)
  terms=[(x/y,x) for x,y in zip(pp,qq) if x]
  n,d,M=product(terms)
  ck(F(n,d)==F(27,25)**int(F(3,32)*M))
  full.append({'sign':s,'first_outcome':bit,'clearing_denominator':M,'cost':'(3/32)log2(27/25)'})
rows=json.loads((R/'out'/'FLOOR_FRONTIER.json').read_text())['rows'];boundaries=[]
for row in rows:
 s=row['sign'];old=F(row['old_booking']);k0=row['first_unpaid_k_within_fixed_dyadic_family'];p=source[s]
 for k in (k0-1,k0):
  ell=F(3,4)-F(1,1<<k)
  terms=[(x,-x) for x in p if x]+[(F(2),old-F(35,4)+F(3,32)*(2*k-4)),(ell,-F(3,32))]
  n,d,M=product(terms);ck((n>d)==(k==k0));ck(n!=d)
  boundaries.append({'sign':s,'old_booking':str(old),'k':k,'unpaid':n>d,'clearing_denominator':M,'numerator_bits':n.bit_length(),'denominator_bits':d.bit_length(),'integer_comparison_sha256':hashlib.sha256(n.to_bytes((n.bit_length()+7)//8,'big')+b'|'+d.to_bytes((d.bit_length()+7)//8,'big')).hexdigest()})
best=0;arg=[];cases=0
for z in range(8,19):
 for x in range(1,19-z):
  for y in range(1,19-z-x):
   ghost=18-z-x-y;ck(ghost>=0);cases+=1;v=z*x*y
   if v>best:best=v;arg=[(x,y,z,ghost)]
   elif v==best:arg.append((x,y,z,ghost))
ck(best==200 and arg==[(5,5,8,0)])
out={'status':'PASS','assertions':checks,'seconds':time.monotonic()-start,'budget_boundaries':boundaries,'full_cost_checks':full,'floor_lattice_cases':cases,'unique_floor_minimizer_numerators':arg,'primary_helper_imported':False,'author_helper_imported':False}
(R/'out'/'INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:out[k] for k in ('status','assertions','seconds','floor_lattice_cases')}))
