from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
import time,json,sys

run=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
pilot='--pilot' in sys.argv
def ck(t):
 global checks
 checks+=1
 assert t,checks
def subs(n):return [tuple(i for i in range(n) if (s>>i)&1) for s in range(1<<n)]
def tab(n,mask):return {x:2*((mask>>sum(b<<i for i,b in enumerate(x)))&1)-1 for x in product([0,1],repeat=n)}
def vprod(p,s):
 v=F(1)
 for i in s:v*=4*p[i]*(1-p[i])
 return v
def moment(table,p,s):
 total=F(0)
 for x in product([0,1],repeat=len(p)):
  z=F(table[x])
  for i,q in enumerate(p):z*=q if x[i] else 1-q
  for i in s:z*=x[i]-p[i]
  total+=z
 for i in s:total/=2*p[i]*(1-p[i])
 return total
def data(table,p):
 ck(all(isinstance(q,(int,F)) for q in p))
 active=[i for i,q in enumerate(p) if 0<q<1]
 labels=[s for s in subs(len(p)) if all(i in active for i in s)]
 c={s:moment(table,p,s) for s in labels}
 P={s:vprod(p,s)*z*z for s,z in c.items()}
 ck(sum(P.values())==1)
 w=1-P[()];j={};u={};W={}
 for s,z in c.items():
  if not s or not z:continue
  ck(abs(z)<=1);jj=0;uu=abs(z)
  while uu<=F(1,2):uu*=2;jj+=1
  ck(F(1,2)<uu<=1)
  j[s]=jj;u[s]=uu;W[s]=vprod(p,s)*F(1,4**jj)
  ck(P[s]/W[s]==uu*uu)
 Z=sum(W.values(),F(0));Q={s:F(0) for s in labels};Q[()]=P[()]
 if w:
  for s in W:Q[s]=w*W[s]/Z
 ck(sum(Q.values())==1)
 D=sum((len(s)-1)*z for s,z in P.items() if s)
 R=sum((len(s)-2)*z for s,z in P.items() if len(s)>=3)
 B=(11*D-7*R)/2
 ck(0<=Z-w<=9*D-6*R)
 J=sum(P[s]*jj for s,jj in j.items())
 return {'p':p,'P':P,'c':c,'w':w,'j':j,'u':u,'W':W,'Z':Z,'Q':Q,'D':D,'R':R,'B':B,'J':J}

@lru_cache(None)
def base_log(q):
 z=(q-1)/(q+1);n=20;a=z;total=F(0)
 for k in range(n):total+=2*a/F(2*k+1);a*=z*z
 err=2*abs(z)**(2*n+1)/F(2*n+1)/(1-z*z)
 return total-err,total+err
@lru_cache(None)
def log(q):
 assert q>0
 k=0
 while q>=2:q/=2;k+=1
 while q<1:q*=2;k-=1
 a,b=base_log(q);l,h=base_log(F(2))
 return (a+k*l,b+k*h) if k>=0 else (a+k*h,b+k*l)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(x,a):return (x*a[0],x*a[1]) if x>=0 else (x*a[1],x*a[0])
def sumlogs(terms):
 d={}
 for coef,q in terms:
  if coef and q!=1:d[q]=d.get(q,F(0))+coef
 out=(F(0),F(0))
 for q,coef in d.items():out=add(out,mul(coef,log(q)))
 return out
ln4=log(F(4))
def metrics(d,Q=None):
 P=d['P'];Q=d['Q'] if Q is None else Q
 E=sumlogs((z,vprod(d['p'],s)/z) for s,z in P.items() if s and z)
 L=sumlogs((P[s],1/(u*u)) for s,u in d['u'].items())
 KL=sumlogs((z,z/Q[s]) for s,z in P.items() if z)
 n=sumlogs([(d['w'],d['Z']/d['w'])]) if d['w'] else (F(0),F(0))
 ck(L[1]<=d['B'])
 ck(KL[1]<=9*d['D']-6*d['R'])
 if d['w']:
  for s,z in P.items():
   if s and z:
    # Multiplicative log identity for E=J+n-KL, independently of intervals.
    ck(F(4**d['j'][s])*d['Z']/d['w']/(z/Q[s])==vprod(d['p'],s)/z)
 if d['D']==0:ck(d['P']==d['Q'] and d['Z']==d['w'])
 return {'E':E,'L':L,'KL':KL,'n':n}

cases=[]
for n in [2,3]:
 laws=[(F(1,2),)*n,tuple([F(1,3),F(2,5),F(3,4)][:n])]
 for mask in range(1<<(1<<n)):
  for p in laws:cases.append((tab(n,mask),p))
for kind in ['and','parity','bent','mux']:
 for p in [(F(1,2),)*4,(F(1,3),F(2,5),F(3,4),F(1,4))]:
  table={}
  for x in product([0,1],repeat=4):
   b=all(x) if kind=='and' else sum(x)%2 if kind=='parity' else (x[0]*x[1]+x[2]*x[3])%2 if kind=='bent' else x[1] if x[0] else (x[2]^x[3])
   table[x]=2*int(b)-1
  cases.append((table,p))
ck(len(cases)==552)
if pilot:cases=cases[:32]
for table,p in cases:metrics(data(table,p))

formula_count=0;different_count=0;counterexample=None
laws=[(F(1,2),)*3,(F(1,3),F(2,5),F(3,4))]
for gm,hm,p in product(range(16),range(16),laws):
 if pilot and formula_count>=8:break
 g=tab(2,gm);h=tab(2,hm)
 ht=data(h,p[:2]);lit=data({(0,):-1,(1,):1},p[2:])
 pg=((1+ht['c'][()])/2,p[2]);gd=data(g,pg)
 ft={x:g[(int(h[x[:2]]==1),x[2])] for x in product([0,1],repeat=3)}
 fd=data(ft,p);Qtree={s:F(0) for s in fd['P']};Qtree[()]=gd['Q'][()]
 ck(fd['P'][()]==Qtree[()])
 C=F(0)
 for s,pp in fd['P'].items():
  if not s:continue
  T=tuple(i for i in s if i<2);U=(0,) if 2 in s else ()
  A=tuple(i for i,b in enumerate([T,U]) if b)
  prediction=gd['P'].get(A,F(0));q=gd['Q'].get(A,F(0));coef=gd['c'].get(A,F(0))
  js=gd['j'].get(A,0)
  for i,z in enumerate([T,U]):
   if not z:continue
   child=[ht,lit][i]
   if child['w']==0:prediction=q=coef=F(0);break
   prediction*=child['P'][z]/child['w'];q*=child['Q'][z]/child['w'];coef*=child['c'][z];js+=child['j'].get(z,0)
  Qtree[s]=q
  ck(prediction==pp);ck(coef==fd['c'][s])
  if pp:
   carry=fd['j'][s]-js;ck(carry>=0);C+=pp*carry
 ck(sum(Qtree.values())==1)
 weights=[]
 for i,child in enumerate([ht,lit]):
  inf=sum(z for a,z in gd['P'].items() if i in a)
  weights.append(inf/child['w'] if child['w'] else F(0))
 ck(fd['D']==gd['D']+sum(a*d['D'] for a,d in zip(weights,[ht,lit])))
 ck(fd['J']==gd['J']+sum(a*d['J'] for a,d in zip(weights,[ht,lit]))+C)
 fm=metrics(fd);gmtr=metrics(gd);hmtr=metrics(ht);lmtr=metrics(lit)
 treeKL=sumlogs((z,z/Qtree[s]) for s,z in fd['P'].items() if z)
 ck(treeKL[1]<=9*fd['D'])
 # Verify KL chain rule before logarithms by every complete-label likelihood.
 for s,z in fd['P'].items():
  if not z:continue
  if not s:ck(z/Qtree[s]==1);continue
  T=tuple(i for i in s if i<2);U=(0,) if 2 in s else ();A=tuple(i for i,b in enumerate([T,U]) if b)
  ratio=gd['P'][A]/gd['Q'][A]
  for child,t in zip([ht,lit],[T,U]):
   if t:ratio*=child['P'][t]/child['Q'][t]
  ck(ratio==z/Qtree[s])
 if Qtree!=fd['Q']:
  different_count+=1
  if counterexample is None:
   counterexample={'outer_mask':gm,'inner_mask':hm,'biases':list(map(str,p)),'P':{str(s):str(z) for s,z in fd['P'].items()},'Qflat':{str(s):str(z) for s,z in fd['Q'].items()},'Qtree':{str(s):str(z) for s,z in Qtree.items()},'expected_carry':str(C)}
 # Exact pointwise ratio underlying CE_tree-CE_flat=KL_tree-KL_flat.
 for s,z in fd['P'].items():
  if z:ck((vprod(p,s)/Qtree[s])/(vprod(p,s)/fd['Q'][s])==(z/Qtree[s])/(z/fd['Q'][s]))
 formula_count+=1

# A mandatory nonflat source: AND3 on three p=1/3 inputs, via AND2 then AND2.
p=(F(1,3),)*3;g=tab(2,8);h=tab(2,8);ht=data(h,p[:2]);gd=data(g,((1+ht['c'][()])/2,p[2]));fd=data({x:2*int(all(x))-1 for x in product([0,1],repeat=3)},p)
T=(0,);A=(0,);qtree=gd['Q'][A]*ht['Q'][T]/ht['w']
ck(qtree!=fd['Q'][(0,)])
ck(fd['Z']==F(1363,5832))
# Shared-wire exclusion: AND(X,X) is X, not the independent two-child gate.
ck((2*F(1,3)-1)**2==F(1,9))
ck((2*F(1,3)**2-1)**2==F(49,81))
ck(F(1,9)!=F(49,81))
assert time.perf_counter()-start<60
result={'status':'PASS','pilot':pilot,'standalone_cases':len(cases),'formula_cases':formula_count,'different_flat_tree_references':different_count,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction plus20-term rational log enclosures','nonflat_AND3_Qflat_singleton':str(fd['Q'][(0,)]),'nonflat_AND3_Qtree_singleton':str(qtree),'new_claim_scope':'flat/tree signed reference conversion, not a universal scale payment'}
stem='PILOT' if pilot else 'CHECKS'
(run/'out'/(stem+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='')
if counterexample:(run/'out'/('PILOT_REFERENCE_DIFFERENCE.json' if pilot else 'REFERENCE_DIFFERENCE.json')).write_text(json.dumps(counterexample,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(result))
