from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
from math import lcm
import json,time,sys
R=Path(__file__).resolve().parents[1]
def add(a,b,c=Q(1)):
 out=a.copy()
 for k,v in b.items(): out[k]=out.get(k,Q(0))+c*v
 return {k:v for k,v in out.items() if v}
def scale(a,c): return add({},a,c)
@lru_cache(None)
def factor(n):
 out={}; d=2
 while d*d<=n:
  while n%d==0: out[d]=out.get(d,0)+1; n//=d
  d+=1
 if n>1: out[n]=out.get(n,0)+1
 return out
@lru_cache(None)
def log(z):
 assert z>0
 return add({k:Q(v) for k,v in factor(z.numerator).items()},{k:Q(v) for k,v in factor(z.denominator).items()},-1)
@lru_cache(None)
def phi(z): return {} if not z else scale(log(z),-z)
def ep(s,t): return add(add(phi(s),phi(t)),phi(s+t),-1)
def sign(a):
 if not a:return 0
 den=lcm(*(v.denominator for v in a.values())); x=y=1
 for p,v in a.items():
  e=int(v*den)
  if e>0:x*=p**e
  else:y*=p**(-e)
 return (x>y)-(x<y)
def ser(a):return {str(k):str(v) for k,v in sorted(a.items())}
def table(n,c):return tuple(1 if (c>>x)&1 else -1 for x in range(1<<n))
@lru_cache(128)
def spectrum(g):
 a=list(g); width=1
 while width<len(a):
  for start in range(0,len(a),2*width):
   for i in range(width):
    x,y=a[start+i],a[start+i+width]; a[start+i]=x+y; a[start+i+width]=x-y
  width*=2
 return tuple(Q(z,len(a)) for z in a)
def hp(g):
 out={}
 for z in spectrum(g)[1:]:out=add(out,phi(z*z))
 return out
def entropy(g):return add(hp(g),phi(mean(g)**2))
def mean(g):return Q(sum(g),len(g))
def variance(g):return 1-mean(g)**2
def influence(g):
 a=spectrum(g); return sum((s.bit_count()*z*z for s,z in enumerate(a)),Q(0))
def edge_inf(g,i):return Q(sum(g[x]!=g[x^(1<<i)] for x in range(len(g))),len(g))
def restrict(g,i,bit):
 n=len(g).bit_length()-1
 return tuple(g[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(1<<(n-1)))
def erasure(g,i):
 a=spectrum(g); out={}
 for s,z in enumerate(a):
  if not (s>>i)&1:out=add(out,ep(z*z,a[s|(1<<i)]**2))
 return out
def selector(a,u,v):
 na=len(a).bit_length()-1; nu=len(u).bit_length()-1; nv=len(v).bit_length()-1
 return tuple(u[(x>>na)&(len(u)-1)] if a[x&(len(a)-1)]==-1 else v[x>>(na+nu)] for x in range(1<<(na+nu+nv)))
def correction(a,u,v):
 p=(1-mean(a))/2; va=variance(a); m=mean(u); n=mean(v); vu=variance(u); vv=variance(v)
 d=(1-m*n)/2; z=(m-n)**2/4; mixed=p*m+(1-p)*n
 G=add(scale(phi(p*p),vu),scale(phi((1-p)**2),vv))
 G=add(G,{2:va*(vu+vv)/2})
 if z:G=add(G,log(z),-va*z)
 corr=add(add(add(G,phi(mixed*mixed)),phi(m*m),-p),phi(n*n),-(1-p))
 return p,d,z,va,corr
def check_selector(a,u,v):
 f=selector(a,u,v); p,d,z,va,corr=correction(a,u,v)
 path=add(add(entropy(f),entropy(u),-p),entropy(v),-(1-p))
 assert path==add(scale(hp(a),d),corr)
 assert z<=d*d
 assert variance(u)+variance(v)==4*(d-z)
 assert sign(add({2:6*d*va},corr,-1))>=0
 assert influence(f)==d*influence(a)+p*influence(u)+(1-p)*influence(v)
 for i in range(len(a).bit_length()-1):assert edge_inf(f,i)==d*edge_inf(a,i)
 return f,path,corr
def priority(a,b,u,v):
 # Layout shared s, private A, private B, u block, v block.
 assert len(a)==len(b)==2
 n=3+(len(u).bit_length()-1)+(len(v).bit_length()-1)
 nu=len(u).bit_length()-1
 out=[]
 for x in range(1<<n):
  if x&1:out.append(1)
  elif a[(x>>1)&1]==-1:out.append(u[(x>>3)&(len(u)-1)])
  elif b[(x>>2)&1]==-1:out.append(v[x>>(3+nu)])
  else:out.append(1)
 return tuple(out)
def check_priority(a,b,u,v):
 p=(1-mean(a))/2; q=(1-mean(b))/2; du=(1-mean(u))/2; dv=(1-mean(v))/2
 g=selector(b,v,(1,)); mg=mean(g); da=(1-mean(u)*mg)/2
 active=selector(a,u,g)
 ds=p*du+(1-p)*q*dv
 # Three local selector transports, no tree identity assumed for the path sum.
 _,pb,cb=check_selector(b,v,(1,))
 _,pa,ca=check_selector(a,u,g)
 shared=(1,-1)
 _,ps,cs=check_selector(shared,(1,),active)
 full=priority(a,b,u,v)
 leaf=add(scale(entropy(u),p/2),entropy(v),(1-p)*q/2)
 path=add(entropy(full),leaf,-1)
 assert path==add(add(ps,pa,Q(1,2)),pb,(1-p)/2)
 qs=ds; qa=da*influence(a)/2; qb=(1-p)*dv*influence(b)/2
 terminals=p*influence(u)/2+(1-p)*q*influence(v)/2
 assert influence(full)==qs+qa+qb+terminals
 assert edge_inf(full,0)==qs
 assert edge_inf(full,1)==qa
 assert edge_inf(full,2)==qb
 rhs=add(scale(hp(a),da/2),hp(b),(1-p)*dv/2)
 rhs=add(rhs,{2:6*(qs+da*variance(a)/2+(1-p)*dv*variance(b)/2)})
 assert sign(add(rhs,path,-1))>=0
 return {'path':ser(path),'terminal_entropy':ser(leaf),'shared_influence':str(qs),'private_A_influence':str(qa),'private_B_influence':str(qb),'terminal_influence':str(terminals),'root_influence':str(influence(full))}
def cap_review(core,r,reverse):
 p=Q(1,1<<r)
 def visit(g):
  if len(g)==1:
   if g[0]==1:return {}
   point=( -1, )+(1,)*((1<<r)-1)
   def suffix(f):
    if len(f)==1:return {}
    return add(erasure(f,0),add(suffix(restrict(f,0,0)),suffix(restrict(f,0,1))),Q(1,2))
   return suffix(point)
  i=len(g).bit_length()-2 if reverse else 0
  m=mean(g); vv=variance(g); t=spectrum(g)[1<<i]**2
  charge={}
  if vv and t:
   C=1-p+p*m
   Mv=add(ep(C*C,p*p*vv),ep((1-m)**2,vv),p*(1-p))
   alt=add(scale(Mv,t/vv),log(vv/t),p*t)
   charge=Mv if sign(add(Mv,alt,-1))<=0 else alt
  return add(charge,add(visit(restrict(g,i,0)),visit(restrict(g,i,1))),Q(1,2))
 bank=visit(core); a0=1-mean(core); I=p*influence(core)+r*p*a0
 assert sign(add({2:5*I},bank,-1))>=0
 return bank
def main():
 start=time.perf_counter(); pilot='--pilot' in sys.argv; ns=np=nr=0
 for ac in range(16):
  for uc in ([7] if pilot else range(16)):
   for vc in ([1] if pilot else range(16)):
    check_selector(table(2,ac),table(2,uc),table(2,vc)); ns+=1
 if not pilot:
  for ac in range(4):
   for bc in range(4):
    for uc in range(16):
     for vc in range(16):check_priority(table(1,ac),table(1,bc),table(2,uc),table(2,vc)); np+=1
  for n in [2,3]:
   for c in range(1<<(1<<n)):
    for r in [1,2]:
     for rev in [False,True]:cap_review(table(n,c),r,rev); nr+=1
 fixture=check_priority(( -1,1 ),(-1,1),table(2,7),table(2,1))
 result={'helper_version':'A056-selector-ownership-v1','pilot':pilot,'selector_cases':ns,'priority_cases':np,'A057_review_trees':nr,'exact_assertions':'ALL PASS','runtime_seconds':time.perf_counter()-start,'priority_fixture':fixture}
 (R/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
