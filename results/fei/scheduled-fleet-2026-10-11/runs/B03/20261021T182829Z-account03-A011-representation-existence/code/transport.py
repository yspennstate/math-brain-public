from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,time
R=Path(__file__).resolve().parents[1];old=R.parents[1]/'runs/20261014T074949Z-account05-A011-representation-existence/code/shared.py'
sp=importlib.util.spec_from_file_location('s',old);s=importlib.util.module_from_spec(sp);sp.loader.exec_module(s)
start=time.monotonic();cases=0
for g in [[-1,1,1,1],[-1,-1,-1,1,-1,1,1,1]]:
 a=len(g).bit_length()-1;Pg=[x*x for x in s.fw(g)]
 for model in [Pg,[x/2 for x in Pg],[F(1,len(g))]*len(g)]:
  for depth in [0,1]:
   b=2-depth;r=2;n=a+b;t=F(1,2**n);p=F(1,4);beta=6*p*t;N=2**n
   v=[g[y%len(g)]-2*g[0]*(x==0 and y==0) for x in range(4) for y in range(N)]
   P=[x*x for x in s.fw(v)];q=[sum(P[u*N+T] for u in range(4)) for T in range(N)]
   rep=[((model[T] if T<len(g) else 0)+beta*t)/(1+beta) for T in range(N)]
   Q=[rep[T]*P[u*N+T]/q[T] for u in range(4) for T in range(N)];M=sum(Q)
   Pc=[]
   for bit in [0,1]:
    child=[v[s.insert(W,a,bit)] for W in range(len(v)//2)];Pc.append([x*x for x in s.fw(child)])
   marg=[P[s.insert(W,a,0)]+P[s.insert(W,a,1)] for W in range(len(v)//2)]
   ref=[Q[s.insert(W,a,0)]+Q[s.insert(W,a,1)] for W in range(len(v)//2)]
   s.ck(all(marg[W]==(Pc[0][W]+Pc[1][W])/2 for W in range(len(marg))))
   pi=[[Pc[bit][W]/(2*marg[W]) if marg[W] else F(1,2) for W in range(len(marg))] for bit in [0,1]]
   raw=[[2*ref[W]*pi[bit][W] for W in range(len(ref))] for bit in [0,1]];Z=[sum(x) for x in raw]
   s.ck(Z[0]+Z[1]==2*M);s.ck(Z[0]*Z[1]<=M*M)
   for bit in [0,1]:
    inherited=[M*x/Z[bit] for x in raw[bit]];s.ck(sum(inherited)==M)
    for W in range(len(marg)):
     if Pc[bit][W]:s.ck(Pc[bit][W]/inherited[W]==marg[W]/ref[W]*Z[bit]/M)
   # Fresh unedited source model mass is s, not M. Active floor has doubled beta.
   fresh_mass=(sum(model)+2*beta)/(1+2*beta)
   s.ck(0<fresh_mass<=1);s.ck(M==(sum(model)+beta)/(1+beta));cases+=1
out={'status':'PASS','actual_query_cases':cases,'inherited_references':2*cases,'exact_assertions':s.checks,'seconds':time.monotonic()-start,'normalized_Z_over_M_preserved':True}
(R/'out/TRANSPORT_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
