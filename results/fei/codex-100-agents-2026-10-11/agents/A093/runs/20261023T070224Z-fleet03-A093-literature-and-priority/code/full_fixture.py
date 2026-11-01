from pathlib import Path
import ast,json,time
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
(R/'out/FROZEN_FIXTURE.json').write_text(json.dumps(dict(helper='full_fixture.py v1',family='same fixed actual 7-bit wrapper and BOTH 6-bit children',domain='one point-defect-times-character seed, exact coherent incoming law, opposite-child target epsilon1/5',case_count=1,symmetry='none',arithmetic='Fraction and symbolic prime log2',memory_estimate_MB=80,max_runtime_seconds=55),indent=2),encoding='utf-8')
# Reuse only own pure definitions, without executing check.py or its search.
tree=ast.parse((R/'code/check.py').read_text(encoding='utf-8'))
ns={'F':F};names={'fw','restrict','logs','add','ce','kl'}
exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),'<own-pure-primitives>','exec'),ns)
fw,restrict,logs,add,ce=[ns[k] for k in ['fw','restrict','logs','add','ce']]
t0=time.monotonic();a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-v*v for v in a]
h=[(-1 if z<4 else 1)*(-1 if z%4==0 else 1) for z in range(8)]
truth=[a[z&15]+b[z&15]*h[z>>4] for z in range(128)]
P=[v*v for v in fw(truth)];A=fw(a);B=fw(b)
children=[[v*v for v in fw(restrict(truth,4,t))] for t in [0,1]]
seedchildren=[[v*v for v in fw(restrict(h,0,t))] for t in [0,1]]
new=[]
for t in [0,1]:
 s=[F(4,5)*x+F(1,5)*y for x,y in zip(seedchildren[t],seedchildren[1-t])]
 new.append([A[U]**2 if T==0 else B[U]**2*s[T] for T in range(4) for U in range(16)])
 assert sum(new[-1])==1
eras={}
for x in range(64):
 lo=(x&15)|((x>>4)<<5);hi=lo|16;mass=P[lo]+P[hi]
 if mass:
  cond=[P[lo]/mass,P[hi]/mass];eras=add((1,eras),(mass,ce(cond,cond)))
increment=add((1,eras),(F(1,2),ce(children[0],new[0])),(F(1,2),ce(children[1],new[1])),(-1,ce(P,P)))
assert increment==add((F(3,8),logs(F(5,8))))
assert time.monotonic()-t0<55
out=dict(status='PASS',exact_assertions=4,seconds=time.monotonic()-t0,full_signed_increment={str(k):str(v) for k,v in increment.items()},incoming_reference='exact actual complete wrapper spectrum',both_terminals='direct physical FWHT plus full new normalized references',erasure='all physical spectral fibers retained')
(R/'out/FULL_FIXTURE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
