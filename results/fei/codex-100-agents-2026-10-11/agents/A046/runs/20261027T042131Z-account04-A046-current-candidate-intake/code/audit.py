from pathlib import Path
from fractions import Fraction as F
import json,time
run=Path(__file__).resolve().parents[1];start=time.perf_counter(); checks=0
def eq(a,b):
 global checks
 checks+=1
 assert a==b,(checks,a,b)
def test(a):
 global checks
 checks+=1
 assert a,checks
def fwht(t):
 a=t[:];h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return [F(x*x,len(t)**2) for x in a]
# Polynomial Walsh expansion, a distinct lane from the direct-sum main checker.
m={1:F(1,2),2:F(1,2),5:F(1,2),6:-F(1,2)}
coeff={}
for T,c in m.items():coeff[2*T]=c/2;coeff[2*T+1]=c/2
coeff[14]=F(1,2);coeff[15]=-F(1,2)
table=[]
for w in range(16):
 a,x,y,z=[(w>>i)&1 for i in range(4)]
 table.append((-1)**(x if z==0 else y) if a==0 else (-1)**(x+y+z))
P=fwht(table);eq(P,[coeff.get(i,F(0))**2 for i in range(16)])
children=[fwht(table[b::2]) for b in [0,1]]
records=[]
for i in range(1,16):
 alpha=F(i,16);q=[(1-alpha)*x+(alpha if j==15 else 0) for j,x in enumerate(P)]
 erased=[q[j]+q[j+1] for j in range(0,16,2)];p_erased=[P[j]+P[j+1] for j in range(0,16,2)]
 for b,pc in enumerate(children):
  raw=[e*x/(2*p) if p else e/2 for x,e,p in zip(pc,erased,p_erased)]
  Z=sum(raw);eq(Z,(1+(-alpha if b==0 else alpha))/2)
  eq([x/Z for x in raw],pc)
 # Exact exponentiated identities: 4*K, 4*erasure and 4*outcome.
 K4=1/((1-alpha)**3*(1+3*alpha));O4=1/(1-alpha**2)**2
 E4=(1+alpha)**2/((1-alpha)*(1+3*alpha))
 eq(K4,E4*O4);test(K4>1);test(E4>1);test(O4>1)
 for j in range(1,16):
  gamma=F(j,16);invoice2=1/(1-gamma)
  test(invoice2>1);test(K4*invoice2**2>K4)
  for r in [F(1),F(8,7),F(2),F(4)]:
   # M=(1/2)log2(r): F_gamma<=M iff r(1-gamma)>=1.
   eq(invoice2<=r,gamma<=1-1/r)
   eq(invoice2<=r,r*(1-gamma)>=1)
  records.append([str(alpha),str(gamma),str(K4),str(invoice2)])
# Complete <=2 residual classification with independent butterfly transform.
tables=0
for n in range(3):
 for mask in range(1<<(1<<n)):
  s=fwht([-1 if mask>>j&1 else 1 for j in range(1<<n)]);tables+=1
  test(sum(x>0 for x in s)==1 or all(x==F(1,4) for x in s))
# Correct source statement and report sign comparison.
source=json.loads((run/'out'/'CHECK.json').read_text(encoding='utf-8'))
eq(source['witness_truth_table'],table);eq(source['witness_spectrum'],[str(x) for x in P])
r={'status':'PASS','exact_assertions':checks,'alpha_gamma_pairs':len(records),'reserve_comparisons':len(records)*4,'small_residual_tables':tables,'seconds':time.perf_counter()-start,'arithmetic':'independent FWHT/Fraction; exponentiated rational KL identities; no imports from main','samples':records}
(run/'out'/'AUDIT.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in r.items() if k!='samples'}))
