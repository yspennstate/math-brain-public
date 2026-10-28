"""Independent direct-character representation and scalar interval reconstruction."""
from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1];START=time.perf_counter();COUNT=0
arith=ROOT/'runs/20261023T022946Z-account03-A023-amortized-rarity-budget/code/independent.py'
source=arith.read_text(encoding='utf-8');prefix=source.split('rows=json.loads')[0]
ns={'__file__':str(__file__)};exec(compile(prefix,str(arith),'exec'),ns)
scatter=ns['scatter'];b=ns['b'];spectrum=ns['spectrum'];entropy=ns['entropy'];cross=ns['cross'];combo=ns['combo'];edge=ns['edge']
def ck(ok):
 global COUNT
 assert ok
 COUNT+=1
 assert time.perf_counter()-START<60
rows=json.loads((RUN/'out/rows.json').read_text(encoding='utf-8'));lookup={(r['m'],r['w'],tuple(sorted((int(i),v) for i,v in r['fixed'].items())),r['z']):r for r in rows}
cases=[(4,1,{}),(4,3,{0:0}),(6,1,{7:1}),(6,3,{0:1,8:0}),(10,1,dict.fromkeys(range(9),0))]
for m,w,fix in cases:
 data=[i for i in range(m) if i not in fix];ctrl=[i for i in [m+1,m+2] if i not in fix];indices=data+ctrl;corefix={i:v for i,v in fix.items() if i<m}
 seed=[b(scatter(x,data,corefix),m) for x in range(1<<len(data))];ps=spectrum(seed);q={s:(ps.get(s,F(0))+F(1,len(seed)))/2 for s in range(len(seed))}
 nu={s:F(0) for s in range(1<<len(ctrl))};delta=F(1,1<<m)
 for mask,a in enumerate([1-3*delta/2]+[delta/2]*3):nu[sum(((mask>>(i-m-1))&1)*(1<<j) for j,i in enumerate(ctrl))]+=a
 pi=[F(0)]*3
 for x in range(1<<len(ctrl)):
  y=scatter(x,ctrl,{i:v for i,v in fix.items() if i>m});A=(y>>(m+1))&1;B=(y>>(m+2))&1;pi[0 if A==0 else 1+B]+=F(1,1<<len(ctrl))
 cores=[[v*(-1 if j and scatter(x,data,corefix)==(0 if j==1 else w) else 1) for x,v in enumerate(seed)] for j in range(3)]
 R=F(0)
 for j in range(3):
  for k in range(j):
   prod=[a*c for a,c in zip(cores[j],cores[k])];R+=2*pi[j]*pi[k]*sum(edge(prod,i) for i in range(len(data)))
 for z in [0,1]:
  t=[]
  for x in range(1<<len(indices)):
   y=scatter(x,indices,fix);c=y% (1<<m);A=(y>>(m+1))&1;B=(y>>(m+2))&1;f=b(c,m)*(-1 if z else 1)
   if A and ((not B and c==0) or (B and c==w)):f=-f
   t.append(f)
  p=spectrum(t);H=entropy(p);ref={mask:q[mask%len(seed)]*nu[mask>>len(data)] for mask in p};C=cross(p,ref);K=combo((1,C),(-1,H))
  influences=[edge(t,i) for i in range(len(indices))];ID=sum(influences[:len(data)]);IC=sum(influences[len(data):]);bank=combo((1,{2:4*ID-F(m,8)-R}),(-1,C))
  row=lookup[(m,w,tuple(sorted(fix.items())),z)]
  for n,v in [('H',H),('C',C),('K',K),('B',bank)]:ck(v=={int(p):F(c) for p,c in row[n].items()})
  for n,v in [('ID',ID),('IC',IC),('R',R)]:ck(v==F(row[n]))
def atanh_twice_interval(z,terms=24):
 total=F(0);power=z
 for j in range(terms):total+=power/(2*j+1);power*=z*z
 return 2*total,2*total+2*power/((2*terms+1)*(1-z*z))
lo2,hi2=atanh_twice_interval(F(1,3));ck(lo2>F(2,3));certs=[]
for m in range(10,65):
 delta=F(1,1<<m);t=3*delta/2;lo,hi=atanh_twice_interval(t/(2-t));entropy_upper=(1-t)*hi/lo2+t*(m+1)
 envelope=(F(3*m,2)+F(15,4))*delta;ck(entropy_upper<envelope)
 bank_lower=F(m,8)-1-(7*m+F(15,4))*delta;ck(bank_lower>=F(729,4096));ck(7*m-F(13,4)>0)
 certs.append({'m':m,'controller_entropy_upper':str(entropy_upper),'analytic_envelope':str(envelope),'bank_lower':str(bank_lower)})
result={'status':'PASS','actual_boolean_cases':10,'scalar_cases':55,'checks':COUNT+ns['COUNT'],'elapsed_seconds':time.perf_counter()-START,'arithmetic_source_sha256':hashlib.sha256(arith.read_bytes()).hexdigest(),'scope':'Separate implementation/representation, same author; independent-person proof review pending.'}
(RUN/'out/independent_scalar_certificates.json').write_text(json.dumps(certs,indent=2)+'\n',encoding='utf-8');(RUN/'out/independent_validation.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
