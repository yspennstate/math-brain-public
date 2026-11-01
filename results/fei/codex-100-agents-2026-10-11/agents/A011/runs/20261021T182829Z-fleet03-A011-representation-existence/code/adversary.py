import importlib.util,json,time
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];old=R.parents[1]/'runs/20261014T074949Z-fleet05-A011-representation-existence/code/shared.py'
sp=importlib.util.spec_from_file_location('s',old);s=importlib.util.module_from_spec(sp);sp.loader.exec_module(s)
start=time.monotonic();bounds=0;tensors=0
for a in [1,2]:
 for bits in range(1,2**(2**a)-1):
  v=[1 if bits>>x&1 else -1 for x in range(2**a)]
  edges={(min(x,x^(1<<j)),max(x,x^(1<<j))) for x in range(2**a) for j in range(a) if v[x]!=v[x^(1<<j)]}
  s.ck(len(edges)>=a);s.ck(sum(s.inf(v))==F(2*len(edges),2**a));bounds+=1
for sign in [-1,1]:
 # Constant source, one padded bit, one control: actual point defect is nonconstant.
 v=[sign-2*sign*(x==0 and y==0) for x in range(2) for y in range(4)]
 P=[z*z for z in s.fw(v)];s.ck(s.entropy(P)[0]>0);s.ck(sum(s.inf([sign,sign]))==0)
 # Thus L<=1.5c+41Ig/4 fails when constant-source c=0; exclusion is essential.
for q in range(2,129):
 s.ck(F(q*q+15*q+7,2**q)<=F(41,4));s.ck((q+1)**2+15*(q+1)+7<=2*(q*q+15*q+7))
# Full tensor likelihoods, including missing reference mass. Two unequal-amplitude fixtures.
g=[-1,1,1,1];a=2;b=1;r=1;n=3;t=F(1,8);p=F(1,2);beta=6*p*t
v=[g[y%4]-2*g[0]*(x==0 and y==0) for x in range(2) for y in range(8)]
P=[x*x for x in s.fw(v)];q=[P[T]+P[8+T] for T in range(8)];Pg=[x*x for x in s.fw(g)]
for Rs in [Pg,[x/2 for x in Pg]]:
 rep=[((Rs[T] if T<4 else 0)+beta*t)/(1+beta) for T in range(8)]
 Q=[rep[T]*P[u*8+T]/q[T] for u in range(2) for T in range(8)]
 ce=s.ce(P,Q);ent=s.entropy(P);D=s.sub(ce,ent)
 for bits in range(16):
  h=[1 if bits>>x&1 else -1 for x in range(4)];Ph=[x*x for x in s.fw(h)]
  for Rh in [[x/2 for x in Ph],[F(1,8)]*4]:
   PP=[x*y for x in P for y in Ph];QQ=[x*y for x in Q for y in Rh]
   s.ck(sum(QQ)==sum(Q)*sum(Rh))
   for z,w,x,y in [(P[i],Q[i],Ph[j],Rh[j]) for i in range(len(P)) for j in range(4)]:
    if z*x:s.ck(z*x/(w*y)==z/w*x/y)
   cc=s.ce(PP,QQ);hh=s.entropy(PP);ch=s.ce(Ph,Rh);eh=s.entropy(Ph)
   s.ck(abs(cc[0]-ce[0]-ch[0])<F(1,2**80));s.ck(abs(cc[1]-ce[1]-ch[1])<F(1,2**80))
   DD=s.sub(cc,hh);Dh=s.sub(ch,eh)
   s.ck(abs(DD[0]-D[0]-Dh[0])<F(1,2**80));s.ck(abs(DD[1]-D[1]-Dh[1])<F(1,2**80))
   tensors+=1
   if time.monotonic()-start>55:raise RuntimeError('frozen cutoff')
out={'status':'PASS','exact_assertions':s.checks,'minimum_boundary_cases':bounds,'constant_exclusion_cases':2,'independent_tensor_reference_cases':tensors,'polynomial_boundary_checks':127,'seconds':time.monotonic()-start}
(R/'out/ADVERSARIAL_RESULTS.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
