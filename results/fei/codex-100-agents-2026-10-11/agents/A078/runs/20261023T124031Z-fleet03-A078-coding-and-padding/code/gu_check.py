from pathlib import Path
from fractions import Fraction as Q
import json,time,hashlib
from exact import add,logvec,entropy,fwht,infl,restrict,scalar,nonneg,interval
R=Path(__file__).resolve().parents[1];O=R/'out'
spec={'version':'A078-GU-parity4','target':'G<=0 for fully row-covered systematic parity lifts; exact signed zero-erasure U drift, NOT universal GU','frozen_pair':[0,0],'family':'ALL Boolean base functions n1..3, every nonzero single parity column; actual evenized canonical bent functions k2,4,6,8','domain':{'base_n':[1,2,3],'actual_bent_k':[2,4,6,8],'algebraic_formula_k':list(range(2,129,2))},'case_count':{'base_lifts':1844,'fully_covered_base_lifts':276,'actual_bent_truth_tables':4},'symmetry':'none','arithmetic':'actual Fraction FWHT/edges and upper-set zeta transform; exact prime-log vectors with outward16-term bounds','memory_estimate_MB':60,'max_runtime_seconds':55,'helper_sha256':hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest()}
(O/'FROZEN_GU_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8',newline='\n');start=time.monotonic();checks=0
def ck(b):
 global checks
 checks+=1;assert b,checks;assert time.monotonic()-start<55
def U(v):
 p=[x*x for x in fwht(v)];pi=p[:];n=len(v).bit_length()-1
 for j in range(n):
  for s in range(len(pi)):
   if not(s>>j)&1:pi[s]+=pi[s|(1<<j)]
 return add(*[(a,logvec(pi[s]/a)) for s,a in enumerate(p) if a])
def G(v):
 uv=U(v);return add(*[(1,add((1,uv),(-Q(1,2),U(restrict(v,i,0))),(-Q(1,2),U(restrict(v,i,1))))) for i in range(len(v).bit_length()-1)])
cases=covered=0;partial_witness=None
for n in [1,2,3]:
 for mask in range(2**(2**n)):
  v=tuple(1-2*((mask>>x)&1) for x in range(2**n));u=U(v);H=entropy(fwht(v));ib=sum((infl(v,i) for i in range(n)),Q(0))
  for P in range(1,2**n):
   f=tuple(v[(x%(2**n))^(P if (x>>n)&1 else 0)] for x in range(2**(n+1)));cases+=1;uf=U(f);gg=G(f)
   ck(entropy(fwht(f))==H);ck(nonneg(add((1,u),(-1,uf))))
   directional=Q(sum(v[x]!=v[x^P] for x in range(2**n)),2**n)
   ck(infl(f,n)==directional);ck(sum((infl(f,i) for i in range(n+1)),Q(0))==ib+directional)
   for i in range(n+1):
    if i==n or (P>>i)&1:
     drift=add((1,uf),(-Q(1,2),U(restrict(f,i,0))),(-Q(1,2),U(restrict(f,i,1))))
     ck(nonneg(add((-1,drift))))
   if P==2**n-1:
    covered+=1;ck(nonneg(add((-1,gg))));theta=sum((a*a for s,a in enumerate(fwht(v)) if s.bit_count()%2),Q(0));ck(directional==theta);ck(ib+directional<=2*ib)
   if n==2 and mask==8 and P==1:
    ck(gg==scalar(1));ck(uf==scalar(1));ck(H==scalar(2));ck(ib+directional==Q(3,2))
    partial_witness={'base_values':v,'column':P,'G':'1','U':'1','I':'3/2','H':'2','physical_values':f}
ck(cases==1844);ck(covered==276);ck(partial_witness is not None)
bent=[]
for k in range(2,129,2):
 rec={'k':k,'H':str(k),'I':str(Q(k+1,2)),'U':str(Q(k-1,2)),'G':str(-Q(k+1,2)),'every_query_DeltaU':'-1/2','H_over_I':str(Q(2*k,k+1)),'U_over_I':str(Q(k-1,k+1)),'G_over_I':'-1'}
 if k in [2,4,6,8]:
  v=tuple((-1)**sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,k,2)) for x in range(2**k));f=tuple(v[(x%(2**k))^((2**k-1) if (x>>k)&1 else 0)] for x in range(2**(k+1)))
  ck(entropy(fwht(f))==scalar(k));ck(U(f)==scalar(Q(k-1,2)));ck(G(f)==scalar(-Q(k+1,2)));ck(sum((infl(f,i) for i in range(k+1)),Q(0))==Q(k+1,2))
  for j in range(k+1):ck(add((1,U(f)),(-Q(1,2),U(restrict(f,j,0))),(-Q(1,2),U(restrict(f,j,1))))==scalar(-Q(1,2)))
  rec['actual_truth_table_checked']=True
 bent.append(rec)
(O/'GU_BENT_FAMILY.json').write_text(json.dumps(bent,indent=2),encoding='utf-8',newline='\n');(O/'GU_SCOPE_GUARD.json').write_text(json.dumps(partial_witness,indent=2),encoding='utf-8',newline='\n')
result={'status':'PASS','exact_assertions':checks,'actual_base_lifts':cases,'fully_covered_GU_cases':covered,'actual_bent_k':[2,4,6,8],'formula_rows':64,'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'GU_CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8',newline='\n');print(json.dumps(result))
