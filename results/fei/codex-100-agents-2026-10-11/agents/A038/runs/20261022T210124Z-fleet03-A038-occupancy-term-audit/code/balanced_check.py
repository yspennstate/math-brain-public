import json,time,importlib.util
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('local_checker',R/'code/check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
start=time.monotonic();count=0
def check(b,label):
 global count
 count+=1
 assert b,label
 if time.monotonic()-start>55:raise RuntimeError('55 second watchdog')
check(3**12>2**19,'h quarter bound')
check(F(13,8)+F(33,32)==F(85,32),'uniform G envelope')
rows=[]
for n in range(3,11):
 G=2*m.h(F(1,4))+n*m.h(F(1,2**(n+1)))
 check(G.b<F(85,32),'strict gap envelope')
 if n==3:check(G.a>2,'outside old G<2 admission')
 e=F(n*(2*n+5),2**(n+2))
 enext=F((n+1)*(2*n+7),2**(n+3))
 check(enext<e and e<=F(33,32),'decreasing rational envelope')
 rows.append({'m':n,'G':G.out(),'uniform_owner_margin_lower':'11/32','envelope':str(e)})
base=[]
for k in range(13):
 if k==0:p=[F(1)];I=F(0)
 else:
  eps=F(1,2**k);p=[(1-2*eps)**2]+[4*eps*eps]*(2**k-1);I=2*k*eps
 H=m.entropy(p)
 check(sum(p)==1,'point-defect law normalized')
 check(H.b<=4*I,'actual point-defect base surplus')
 base.append({'k':k,'H':H.out(),'I':str(I)})
# Exact scalar bookkeeping at arbitrary rational values, independent algebra expansion.
for S,Sroot,A in [(F(2),F(3),F(1)),(F(3),F(2),F(3,2)),(F(5,2),F(7,3),F(11,8))]:
 deficit=S-Sroot;L=A+max(F(0),deficit)
 check(S-L==min(S-A,Sroot-A),'same-owner min identity')
out={'status':'PASS','assertions':count,'runtime_seconds':time.monotonic()-start,'scalar_rows':rows,'point_defect_bases':base,'all_dimensional_bridge':'ANALYTIC_PROOF.md, monotone envelope and supplied hereditary certificates; finite bases are validation only'}
(R/'out/BALANCED_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['status','assertions','runtime_seconds']}))
