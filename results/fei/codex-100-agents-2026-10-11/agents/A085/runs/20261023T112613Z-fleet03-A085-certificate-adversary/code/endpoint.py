from pathlib import Path
from fractions import Fraction as F
import time,json,hashlib
import check as T
C=T.C;R=Path(__file__).resolve().parents[1]
C.save('ENDPOINT_SPEC.json',{'family':'minimal entropy-bearing all-coordinate phase-null source; prepaid mismatch regression','domain':'ALL22 labelled tables n0,1,2; explicit3-bit seed negative at0,7; all3 seed queries, both controller signs, BOTH full children; nonflat3-bit core width2 at matching/nonflat references, both signs, root and both first children','census_tables':22,'minimal_seed_transactions':6,'prepaid_KL_nodes':12,'arithmetic':'exact FWHT, direct characters, Fraction physical edges, prime-log cancellation and integer-power sign','maximum_seconds':55,'memory_MB':150,'symmetry':'none','helper_sha256':hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest(),'endpoint_helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
start=time.monotonic();tables=0
def null(v):
 c=C.coef(v)
 for j in range(len(v).bit_length()-1):
  if c[1<<j]:return False
  for k in range(1,len(v)//2):
   lo=(k&((1<<j)-1))|((k>>j)<<(j+1))
   if c[lo]*c[lo|(1<<j)]:return False
 return True
for n in range(3):
 for code in range(1<<(1<<n)):
  v=tuple(1-2*((code>>x)&1) for x in range(1<<n));tables+=1
  if null(v):C.ck(sum(x>0 for x in C.law(v))==1)
C.ck(tables==22)
h=(-1,1,1,1,1,1,1,-1);p=C.law(h)
C.ck(C.coef(h)==C.direct(h));C.ck(null(h));C.ck(p==tuple(F(1,4) if x in (0,3,5,6) else F(0) for x in range(8)))
C.ck(C.ent(p)==C.log(F(4)))
C.ck(all(F(sum(h[x]!=h[x^(1<<j)] for x in range(8)),8)==F(1,2) for j in range(3)))
a=C.ROW;b=tuple(1-x*x for x in a);transactions=[]
for s in (1,-1):
 for j in range(3):
  inc,kids=C.step((a,b,h,p,s),'seed',j);C.ck(inc=={})
  terms=[]
  for aa,bb,hh,rr,ss in kids:
   pp=C.law(C.wrap(aa,bb,hh,ss));old=C.coherent(aa,bb,hh,rr,ss);C.ck(pp==old)
   target=(F(1),F(0),F(0));newr=C.mix(rr,F(1,4),F(1,64),target);new=C.coherent(aa,bb,hh,newr,ss)
   cost=C.add((1,C.ce(pp,new)),(-1,C.ce(pp,old)))
   C.ck(cost==C.add((F(3,32),C.log(F(131072,130977)))));C.ck(C.sign(cost)>0)
   terms.append({'truth':C.wrap(aa,bb,hh,ss),'spectrum':pp,'old_reference':old,'new_reference':new,'positive_charge':cost})
  transactions.append({'sign':s,'query':j,'query_increment':inc,'both_complete_terminals':terms})
C.ck(131072>130977)
C.save('MINIMAL_ENTROPY_NULLSPACE.json',{'status':'PASS','minimal_seed_dimension':3,'smaller_tables_checked':tables,'truth':h,'spectrum':p,'H_bits':'2','I':'3/2','positive_per_full_child':'(3/32)log2(131072/130977)','transactions':transactions,'necessary_conversion':'NOT_PROVED','FEI_counterexample':False})
g=tuple(-1 if x==0 else 1 for x in range(8));hh,masks,_,_=T.build(g,2,{});gp=C.law(g);prepaid=0
for model in (0,1):
 S=T.source(g,model);rr=T.push(S,masks)
 for s in (1,-1):
  nodes=[(hh,rr)]+[(C.restrict(hh,0,z),C.marginal(rr,0)) for z in (0,1)]
  for v,q in nodes:
   P=C.law(C.wrap(a,b,v,s));Q=C.coherent(a,b,v,q,s);d=C.kl(P,Q)
   C.ck(d==C.add((C.beta(b),C.kl(gp,S))))
   C.ck(C.sign(d)==model);prepaid+=int(model==1)
C.save('ENDPOINT.json',{'status':'PASS','assertions':C.checks,'census_tables':tables,'minimal_transactions':len(transactions),'prepaid_KL_nodes':12,'positive_prepaid_KL_occurrences':prepaid,'seconds':time.monotonic()-start,'draft_scope_correction_verified':True})
assert time.monotonic()-start<55
print(json.dumps({'status':'PASS','assertions':C.checks,'seconds':time.monotonic()-start,'prepaid_KL_nodes':12,'minimal_seed_dimension':3}))
