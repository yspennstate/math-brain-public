from pathlib import Path
from fractions import Fraction as F
import json,sys,time,hashlib
from functools import lru_cache
from sympy import factorint
R=Path(__file__).resolve().parents[1]; O=R/'out'
# Rational linear combinations of logs of primes, not floating logarithms.
class L:
 def __init__(self,d=None):self.d={p:c for p,c in (d or {}).items() if c}
 def __add__(self,b):
  d=self.d.copy()
  for p,c in b.d.items():d[p]=d.get(p,F(0))+c
  return L(d)
 def __neg__(self):return self*F(-1)
 def __sub__(self,b):return self+-b
 def __mul__(self,c):return L({p:v*c for p,v in self.d.items()})
 __rmul__=__mul__
 def __eq__(self,b):return self.d==b.d
@lru_cache(maxsize=10000)
def lg(x):
 assert x>0
 d={}
 for n,sg in [(x.numerator,1),(x.denominator,-1)]:
  for p,k in factorint(n).items():d[int(p)]=d.get(int(p),0)+sg*int(k)
 return L(d)
def ce(p,q):
 ans=L()
 for a,b in zip(p,q):
  if a:assert b>0;ans=ans-lg(b)*a
 return ans
def ent(p):return ce(p,p)
def div(p,q):return ce(p,q)-ent(p)
def walsh(tab):
 n=len(tab);return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(tab)),n)**2 for s in range(n)]
def marg(p):return [p[2*i]+p[2*i+1] for i in range(len(p)//2)]
checks=0
def ck(v):
 global checks
 checks+=1
 assert v,checks
def query(tab,q):
 p=walsh(tab);m=marg(p);r=marg(q);s=sum(q)
 children=[];zs=[]
 for b in range(2):
  tb=tab[b::2];pb=walsh(tb)
  raw=[r[i]*pb[i]/m[i] if m[i] else r[i] for i in range(len(m))]
  z=sum(raw);ck(z>0);qb=[s*x/z for x in raw]
  ck(sum(qb)==s);children.append((tb,pb,qb));zs.append(z)
 ck(zs[0]+zs[1]==2*s)
 ck(all((children[0][1][i]+children[1][1][i])/2==m[i] for i in range(len(m))))
 contraction=div(p,q)-(div(children[0][1],children[0][2])+div(children[1][1],children[1][2]))*F(1,2)
 expected=div(p,q)-div(m,r)-(lg(zs[0]/s)+lg(zs[1]/s))*F(1,2)
 ck(contraction==expected)
 return children,contraction
def tree(tab,q,depth,reset):
 p=walsh(tab)
 if not depth or len(tab)==1:return L(),L(),div(p,q)
 children,d=query(tab,q);ed=L();ld=L();desc=L()
 for tb,pb,qb in children:
  s=sum(qb)
  # Arbitrary signed conversion retaining scalar mass; may retain ghosts.
  rb=[(1-reset)*x+reset*s*y for x,y in zip(qb,pb)]
  e=ce(pb,rb)-ce(pb,qb)
  ee,dd,tt=tree(tb,rb,depth-1,reset)
  ed=ed+(e+ee)*F(1,2);desc=desc+dd*F(1,2);ld=ld+tt*F(1,2)
 ck(ce(p,q)+ed==ent(p)+d+desc+ld)
 return ed,d+desc,ld
def witness(b):
 e=F(1,2**(1+b));N=1/e
 # Two exact multiplicity classes of actual data frequencies.
 As=[F(1),F(0)];mult=[1,int(N)-1]
 p=[(a-e)**2+e*e for a in As]
 ref=[(a*a+3*e*e)/(1+3*e) for a in As]
 clean=[a*a for a in As];edit=[(a-2*e)**2 for a in As]
 zs=[sum(k*r*x/y for k,r,x,y in zip(mult,ref,c,p)) for c in [clean,edit]]
 zformula=(1+3*e*e)/((1+3*e)*(1-2*e+2*e*e))
 ck(zs[0]==zformula);ck(sum(zs)==2);ck(0<zs[0]<1);ck(zs[0]*zs[1]<1)
 ck((1+3*e)*(1-2*e+2*e*e)-(1+3*e*e)==e*(1-e)*(1-6*e))
 ck(1-zs[0]*zs[1]==(1-zs[0])**2)
 def weighted_ce(a,b):
  out=L()
  for k,x,y in zip(mult,a,b):
   if x:out=out-lg(y)*(k*x)
  return out
 def weighted_d(a,b):return weighted_ce(a,b)-weighted_ce(a,a)
 inherited=[[r*x/y/z for r,x,y in zip(ref,c,p)] for c,z in zip([clean,edit],zs)]
 target=[clean,[(a*a+6*e*e)/(1+6*e) for a in As]]
 root_d=weighted_d(p,ref)
 contraction=root_d-(weighted_d(clean,inherited[0])+weighted_d(edit,inherited[1]))*F(1,2)
 ck(contraction==lg(zs[0]*zs[1])*F(-1,2))
 # Full parent H includes the true selector kernel; it cancels in root D.
 fullp=[];fullq=[];fullmult=[]
 for a,pr,qr,k in zip(As,p,ref,mult):
  for x in [(a-e)**2,e*e]:fullp.append(x);fullq.append(qr*x/pr);fullmult.append(k)
 rootce=L();rooth=L()
 for x,y,k in zip(fullp,fullq,fullmult):rootce=rootce-lg(y)*(k*x);rooth=rooth-lg(x)*(k*x)
 resets=L();terminal=L()
 for c,qi,t in zip([clean,edit],inherited,target):
  resets=resets+(weighted_ce(c,t)-weighted_ce(c,qi))*F(1,2)
  terminal=terminal+weighted_d(c,t)*F(1,2)
 ck(rootce+resets==rooth+contraction+terminal)
 ck(rootce+resets!=rooth+terminal)
 return {'b':b,'epsilon':str(e),'Z_clean':str(zs[0]),'normalizer_product':str(zs[0]*zs[1]),'strict_positive_contraction_certificate':'product<1; delta=-log2(product)/2'}
def run(pilot=False):
 global checks
 checks=0;start=time.perf_counter();transactions=0
 for n in ([1,2] if pilot else [0,1,2,3]):
  for bits in range(2**(2**n)):
   if pilot and bits>5:break
   tab=[-1 if bits>>i&1 else 1 for i in range(2**n)];p=walsh(tab)
   for s in [F(1),F(1,2)]:
    for alpha in ([F(1)] if pilot else [F(1),F(1,2)]):
     q=[s*(alpha*x+(1-alpha)*F(1,len(p))) for x in p]
     tree(tab,q,min(n,2),F(1,3));transactions+=1
     if alpha==1:
      _,dd,_=tree(tab,q,min(n,2),F(0));ck(dd==L())
   if time.perf_counter()-start>55:raise RuntimeError('frozen 55 second cap')
 ws=[witness(b) for b in ([12] if pilot else [12,13,14,15,16])]
 out={'status':'PASS','checks':checks,'transactions':transactions,'witnesses':ws,'seconds':time.perf_counter()-start,'arithmetic':'Fraction and exact prime-log normal forms; no floats in sign decisions','scope':'finite checks plus analytic finite-tree identity; not full FEI'}
 (O/('PILOT.json' if pilot else 'ACCOUNT_REVIEW.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k!='witnesses'}))
if __name__=='__main__':run('--pilot' in sys.argv)
