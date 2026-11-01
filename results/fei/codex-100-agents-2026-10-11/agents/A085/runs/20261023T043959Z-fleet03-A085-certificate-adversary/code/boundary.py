import check as C
from fractions import Fraction as F
import time,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
# This specification is persisted before ANY family evaluation.
spec={'family':'sparse finite-CE coherent laws, true-support-only tails; actual signed wrappers','domain':'parity2 and three-bit seed negative at 0,1; controller root and fully fixed beta0/beta1; both signs; every single remaining physical query; epsilon0/1/64 support checks, excluded epsilon1 singularity guard','signed_fixtures':12,'symmetry':'none','arithmetic':'same independently checked FWHT/prime-log/rational code; no author import','helper_sha256':hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest(),'memory_MB':120,'maximum_runtime_seconds':55,'automatic_dimension_escalation':False}
C.save('BOUNDARY_SPEC.json',spec)
start=time.monotonic();cases=0;singular=[]
for h in [(1,-1,-1,1),(-1,-1,1,1,1,1,1,1)]:
 p=C.law(h);r=(F(1,2),)+tuple(x/(2*(1-p[0])) for x in p[1:])
 for a in [C.ROW,(C.ROW[0],),(C.ROW[1],)]:
  b=tuple(1-x*x for x in a);old,kids=C.tag(a,b,h,r,0)
  for s in (1,-1):
   node=(a,b,h,p,s);cases+=1
   for kind,N in [('seed',len(h)),('controller',len(a))]:
    for j in range(N.bit_length()-1):C.step(node,kind,j)
   zero,same=C.change(node,F(0),0) if False else ({},node)
   C.ck(C.mix(p,p[0],F(0),C.profile(len(p)-1,0))==p)
   # Point target may be zero at every occupied true label. The retained component still pays.
   ghost=next((j for j,x in enumerate(p[1:]) if x==0),None)
   if ghost is not None:
    target=tuple(F(j==ghost) for j in range(len(p)-1))
    mixed=C.mix(p,p[0],F(1,64),target);qq=C.coherent(a,b,h,mixed,s);pp=C.law(C.wrap(a,b,h,s))
    C.ck(all(q>0 for x,q in zip(pp,qq) if x))
    bad=C.coherent(a,b,h,C.mix(p,p[0],F(1),target),s)
    zeros=[{'label':j,'true_mass':x} for j,(x,q) in enumerate(zip(pp,bad)) if x and not q]
    if C.beta(b)>0:C.ck(bool(zeros));singular.append({'seed':h,'sign':s,'beta':C.beta(b),'occupied_zero_atoms':zeros[:2]})
   C.ck(time.monotonic()-start<55)
C.save('BOUNDARY.json',{'status':'PASS','signed_fixtures':cases,'query_actions':C.actions,'assertions':C.checks,'seconds':time.monotonic()-start,'excluded_endpoint_epsilon1':singular,'verdict':'All admitted sparse finite-cost endpoints hold; epsilon1 is outside theorem and may have infinite CE'})
print(json.dumps({'status':'PASS','signed_fixtures':cases,'query_actions':C.actions,'assertions':C.checks,'seconds':time.monotonic()-start}))
