from pathlib import Path
from fractions import Fraction as F
import sys,importlib.util,json,time
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
sp=importlib.util.spec_from_file_location('bounds',R.parent/'20261014T023633Z-fleet05-A083-formal-core/code/occupancy_check.py')
E=importlib.util.module_from_spec(sp);sp.loader.exec_module(E)
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
 if time.perf_counter()-start>60:raise TimeoutError('frozen60s')
def spec(t):
 N=len(t)
 return [F(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(t)),N)**2 for s in range(N)]
def influence(t):
 return F(sum(t[x]!=t[x^(1<<j)] for j in range(len(t).bit_length()-1) for x in range(len(t))),len(t))
def logs(x):
 out=dict(E.factors(x.numerator))
 for p,e in E.factors(x.denominator).items():out[p]=out.get(p,0)-e
 return {p:F(e) for p,e in out.items() if e}
def ce(p,q):
 out={}
 for a,b in zip(p,q):
  if a:ck(b>0);out=E.add(out,E.mul(logs(1/b),a))
 return out
def iv(v):
 lo=hi=F(0)
 for p,c in v.items():
  a,b=E.scale(E.log2_interval(F(p)),c);lo+=a;hi+=b
 return lo,hi
def act(s):return (2 if s&1 else 0)^(4 if s&2 else 0)^(7 if s&4 else 0)
ck([act(s) for s in range(8)]==[0,2,4,6,7,5,3,1])
for a in range(8):
 ck(act(act(act(act(a))))==a)
 for b in range(8):ck(act(a^b)==act(a)^act(b))
majority=tuple(1 if s.bit_count()>=2 else -1 for s in range(8))
pm=spec(majority);W=[1,2,4,7]
ck(pm==[F(1,4) if s in W else F(0) for s in range(8)])
ck(influence(majority)==F(3,2))
fixtures=[];excluded=[]
cores=[(2,k) for k in range(16)]+[(3,k) for k in [0,1,23,105,128,150,232,255]]
for n,bits in cores:
 g=tuple(1-2*((bits>>x)&1) for x in range(1<<n));pg=spec(g);Ig=influence(g)
 for K in [4,5,8]:
  eps=F(1,1<<(3*K));q=[F(0)]*8
  q[1]=1-3*eps
  for s in [2,4,7]:q[s]=eps
  c=ce(pm,q);ck(iv(c)[0]>F(9*K,4) and iv(c)[1]<F(9*K+1,4))
  avg=[F(0)]*8
  for s,v in enumerate(q):
   cur=s
   for r in range(4):avg[cur]+=v/4;cur=act(cur)
  ck(avg==pm)
  for mode in ['matched','ghost']:
   qg=pg if mode=='matched' else [(a+F(1,len(pg)))/2 for a in pg]
   Cg=ce(pg,qg);Bg=E.add({2:K*Ig},E.mul(Cg,-1))
   if iv(Bg)[1]<0:
    excluded.append({'n':n,'truth_index':bits,'K':K,'mode':mode,'reason':'supplied CE<=K I hypothesis false'});continue
   ck(iv(Bg)[0]>=0)
   # Literal full five-control+core truth table. Little-endian t,x,y0,y1,y2,z.
   t=tuple((-1)**((s&1)+((s>>1)&1))*majority[(s>>2)&7]*g[s>>5] for s in range(1<<(n+5)))
   p=spec(t);ck(influence(t)==Ig+F(7,2))
   expected=[F(0)]*len(t);Q=[F(0)]*len(t);Qavg=[F(0)]*len(t)
   for z in range(len(pg)):
    for y in range(8):
     mask=3+(y<<2)+(z<<5);expected[mask]=pm[y]*pg[z];Q[mask]=q[y]*qg[z];Qavg[mask]=avg[y]*qg[z]
   ck(p==expected and sum(Q)==sum(Qavg)==1)
   ck(ce(p,Q)==E.add(Cg,c));ck(ce(p,Qavg)==E.add(Cg,{2:F(2)}))
   # Delete t then x on all physical branches; every source/ref atom has both frequencies.
   for bt in [0,1]:
    child=tuple(v for s,v in enumerate(t) if s&1==bt)
    pc=spec(child);qp=[F(0)]*len(child)
    for s,v in enumerate(Q):qp[s>>1]+=v
    ck(ce(pc,qp)==E.add(Cg,c));ck(pc==[p[2*s]+p[2*s+1] for s in range(len(child))])
    for bx in [0,1]:
     leaf=tuple(v for s,v in enumerate(child) if s&1==bx)
     pl=spec(leaf);ql=[F(0)]*len(leaf)
     for s,v in enumerate(Qavg):ql[s>>2]+=v
     ck(ce(pl,ql)==E.add(Cg,{2:F(2)}));ck(pl==[pc[2*s]+pc[2*s+1] for s in range(len(leaf))])
   # Exact symbolic original-owner cancellation, preserving Bg and old quarter.
   A={2:K*(Ig+F(7,2))};tau=E.add(Bg,{2:F(1,4)})
   St=E.add(A,{2:-K},E.mul(E.add(Cg,c,tau),-1))
   ck(St==E.add({2:F(5*K,2)-F(1,4)},E.mul(c,-1)));ck(iv(St)[0]>0)
   raw=E.add(St,{2:-K});ck(iv(raw)[1]<0)
   refund=E.add(c,{2:F(-2)})
   Smid=E.add(St,refund);final=E.add(Smid,{2:-K})
   ck(Smid=={2:F(5*K,2)-F(9,4)});ck(final=={2:F(3*K,2)-F(9,4)})
   ck(E.add({2:2*K},Cg,{2:F(2)},tau,final)==A)
   fixtures.append({'n':n,'truth_index':bits,'K':K,'reference':mode,'final':str(F(3*K,2)-F(9,4))})
 # Save results immediately after each core.
 (R/'out/CHECKPOINT.json').write_text(json.dumps({'cores_completed':cores.index((n,bits))+1,'fixtures':len(fixtures),'checks':checks})+'\n',encoding='utf-8')
# Noninvariant Boolean control: dictatorship on the majority register.
K=4;eps=F(1,4096);before=logs(1/(1-3*eps));ck(iv(before)[1]<1)
ck(iv(E.add({2:F(2)},E.mul(before,-1)))[0]>1)
result={'status':'PASS','fixtures':len(fixtures),'proposed':144,'excluded':excluded,'checks':checks,'seconds':time.perf_counter()-start,'C4':[act(s) for s in range(8)],'minimum_final':'15/4','noninvariance_control':'actual dictator averaging costs>1bit; invariance required','formal_scope':'Separate admission and Lean checker receipt only','full_FEI':'OPEN'}
(R/'out/RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
