from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1]; O=R/'out'
pilot='--pilot' in sys.argv
spec={'helper':'A041-adaptive-complete-reference-v1','family':'all three-variable Boolean signs; disjoint binary gate of a two-bit gate and a literal; four fixed four-bit formula controls','domain':'two labelled laws: all 1/3 and (1/4,1/2,3/4); four-bit controls at (1/3,1/4,1/2,3/4)','case_count':{'flat':32 if pilot else 512,'formula':32 if pilot else 512,'mandatory_controls':2 if pilot else 6},'symmetry':'none; all truth tables retained','arithmetic':'Fraction direct centered-product sums, rational dyadic indices, exact total variation and integer carry; 20-term rational atanh log intervals','memory_estimate_MB':100,'maximum_runtime_seconds':60,'mode':'pilot' if pilot else 'main'}
(O/('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.monotonic(); assertions=0; flat_count=formula_count=0
def ck(v):
 global assertions
 assert v
 assertions+=1
def mul(xs):
 v=Q(1)
 for x in xs:v*=x
 return v
def series(x):
 z=(x-1)/(x+1); z2=z*z; power=z; a=Q(0)
 for k in range(20):a+=2*power/Q(2*k+1);power*=z2
 return a,a+2*power/(41*(1-z2))
L2,U2=series(Q(2))
@lru_cache(None)
def logint(x):
 assert x>0
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 l,u=series(x)
 return (l+k*L2,u+k*U2) if k>=0 else (l+k*U2,u+k*L2)
def scale(c):
 a=abs(c);j=0
 assert 0<a<=1
 while a<=Q(1,2):a*=2;j+=1
 return j,a
def spectrum(ps,vals):
 n=len(ps);vs=[4*p*(1-p) for p in ps];P={};cs={};js={};W={}
 for mask in range(1<<n):
  inds=[i for i in range(n) if mask>>i&1];v=mul(vs[i] for i in inds)
  a=Q(0)
  for x in range(1<<n):
   prob=mul(ps[i] if x>>i&1 else 1-ps[i] for i in range(n))
   centered=mul((2*((x>>i)&1)-1)-(2*ps[i]-1) for i in inds)
   a+=prob*vals[x]*centered
  c=a/v;cs[mask]=c;P[mask]=v*c*c
  if mask and c:
   j,u=scale(c);js[mask]=j;W[mask]=v/Q(4**j)
 w=1-P[0];Z=sum(W.values(),Q(0));delta=sum((Q(s.bit_count()-1)*p for s,p in P.items() if s),Q(0));r=sum((max(0,s.bit_count()-2)*p for s,p in P.items()),Q(0))
 ref={s:(P[0] if s==0 else (w*W.get(s,0)/Z if Z else Q(0))) for s in P}
 ck(sum(P.values())==1 and sum(ref.values())==1)
 ck(w<=Z<=w+9*delta-6*r)
 tv=sum((abs(P[s]-ref[s]) for s in P),Q(0))/2
 ck(tv<=9*delta-6*r)
 return {'ps':ps,'vals':vals,'P':P,'c':cs,'j':js,'Q':ref,'w':w,'Z':Z,'D':delta,'R':r,'mean':cs[0]}
def literal(p):return spectrum((p,),(-1,1))
def gate(table,ps):return spectrum(tuple(ps),tuple(Q(1 if table>>s&1 else -1) for s in range(1<<len(ps))))
def tv(P,T):return sum((abs(P[s]-T[s]) for s in P),Q(0))/2
def build(table,left,right):
 children=(left,right);nl=len(left['ps']);nr=len(right['ps']);ps=left['ps']+right['ps']; vals=[]
 for x in range(1<<(nl+nr)):
  a=int(left['vals'][x&((1<<nl)-1)]==1);b=int(right['vals'][x>>nl]==1)
  vals.append(Q(1 if table>>(a+2*b)&1 else -1))
 f=spectrum(ps,tuple(vals));active=[i for i in range(2) if children[i]['w']]
 gp=[(children[i]['mean']+1)/2 for i in active];gv=[]
 for x in range(1<<len(active)):
  ab=[int(c['mean']==1) if not c['w'] else 0 for c in children]
  for k,i in enumerate(active):ab[i]=(x>>k)&1
  gv.append(Q(1 if table>>(ab[0]+2*ab[1])&1 else -1))
 g=spectrum(tuple(gp),tuple(gv));T={s:Q(0) for s in f['P']};T[0]=g['Q'][0]
 jsum={};rt=g['R'];nt=Q(0);lt=Q(0)
 weights=[]
 for k,i in enumerate(active):
  a=sum((p for s,p in g['P'].items() if s>>k&1),Q(0))/children[i]['w']; weights.append((i,a));rt+=a*children[i].get('Rt',children[i]['R'])
 for am,qp in g['Q'].items():
  if not am or not qp:continue
  occupied=[active[k] for k in range(len(active)) if am>>k&1]
  lists=[[s for s,p in children[i]['P'].items() if s and p] for i in occupied]
  for parts in product(*lists):
   lab=0;prob=qp;c=g['c'][am];j=g['j'][am]
   for i,s in zip(occupied,parts):
    lab|=s if i==0 else s<<nl
    ch=children[i];prob*=ch.get('T',ch['Q'])[s]/ch['w'];c*=ch['c'][s];j+=ch.get('jsum',ch['j'])[s]
   T[lab]+=prob;jsum[lab]=j;ck(c==f['c'][lab])
 f['T']=T;f['jsum']=jsum;f['Rt']=rt
 ck(sum(T.values())==1 and T[0]==f['P'][0]);ck(f['D']==g['D']+sum((a*children[i]['D'] for i,a in weights),Q(0)))
 f['local']=(g,weights,children)
 return f
def klint(P,T):
 lo=hi=Q(0)
 for s,p in P.items():
  if p:
   l,u=logint(p/T[s]);lo+=p*l;hi+=p*u
 return lo,hi
def check_formula(f):
 global formula_count
 P=f['P'];F=f['Q'];T=f['T'];d=f['D'];r=f['R'];rt=f['Rt'];w=f['w'];b0=9*d-6*r;bt=9*d-6*rt
 ck(tv(P,F)<=b0 and tv(P,T)<=bt);dist=tv(F,T);ck(dist<=b0+bt)
 if w:
  raw={s:max(F[s],T[s]) for s in P if s};z=sum(raw.values(),Q(0));ck(z==w+dist)
  M={s:(P[0] if not s else w*raw[s]/z) for s in P};ck(sum(M.values())==1)
  ck(w*logint(z/w)[1]<=b0+bt or z==w)
  upper=Q(0);carry=Q(0)
  for s,p in P.items():
   if p and s:
    lo,hi=logint(F[s]/T[s]);upper+=p*max(abs(lo),abs(hi))
    k=f['j'][s]-f['jsum'][s];ck(k>=0);carry+=p*k
  ck(upper<=(Q(47,2)*d-6*r-Q(19,2)*rt) or d==0)
  # The same signed conversion as source, with independently computed spectra.
  kl0=klint(P,F);klt=klint(P,T)
  ck(kl0[1]<=b0 or d==0);ck(klt[1]<=bt or d==0)
  # Every atom selects a different reference according to a fixed physical mask rule.
  sel={s:(F[s] if s.bit_count()%2 else T[s]) for s in P if s};zs=sum(sel.values(),Q(0));ck(zs<=w+dist and zs>0)
  if zs>w:ck(w*logint(zs/w)[1]<=b0+bt)
 else:ck(F==T==P)
 formula_count+=1
 if time.monotonic()-start>60:raise RuntimeError('frozen runtime exceeded')
laws=[(Q(1,3),)*3,(Q(1,4),Q(1,2),Q(3,4))]
for ps in laws:
 for table in range(16 if pilot else 256):gate(table,ps);flat_count+=1
 for root in range(4 if pilot else 16):
  for child in range(4 if pilot else 16):check_formula(build(root,gate(child,ps[:2]),literal(ps[2])))
# Mandatory source witness, separately instantiated from the exhaustive cases.
f=build(8,gate(8,(Q(1,3),Q(1,3))),literal(Q(1,3)));check_formula(f)
ck(f['Q'][1]==Q(104,12267));ck(f['T'][1]==Q(256,10521));ck(f['R']==Q(32,729));ck(f['Rt']==0)
witness={'flat_singleton':str(f['Q'][1]),'tree_singleton':str(f['T'][1]),'TV':str(tv(f['Q'],f['T'])),'Delta':str(f['D']),'R_flat':str(f['R']),'R_tree':str(f['Rt'])}
ck(Q(1,9)!=Q(49,81)) # Actual repeated-wire X versus fictitious independent AND(X,X).
controls=2
if not pilot:
 for tables in [(8,8,14),(14,8,14),(6,6,8),(8,6,14)]:
  rt,lt,rr=tables;ps=(Q(1,3),Q(1,4),Q(1,2),Q(3,4));check_formula(build(rt,gate(lt,ps[:2]),gate(rr,ps[2:])));controls+=1
out={'status':'PASS','helper':spec['helper'],'flat_cases':flat_count,'formula_cases_including_controls':formula_count,'control_records':controls,'assertions':assertions,'runtime_seconds':time.monotonic()-start,'source_AND3':witness,'scope':'analytic universal reference bounds; finite tests do not pay universal J or prove FEI'}
(O/('PILOT_CHECKS.json' if pilot else 'CHECKS.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
