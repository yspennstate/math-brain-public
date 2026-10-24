from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from itertools import product
import json,time,sys
import primitives as z
START=time.monotonic();PILOT='--pilot' in sys.argv;LOCAL='--local' in sys.argv;COUNTS={}
CHUNK=next((int(a.split('=')[1]) for a in sys.argv if a.startswith('--chunk=')),None)
def ck(ok,key):
 assert ok,key
 COUNTS[key]=COUNTS.get(key,0)+1
 if time.monotonic()-START>(55 if PILOT else 170):raise RuntimeError('frozen watchdog')
def m(t):return Q(sum(t),len(t))
def n(t):return len(t).bit_length()-1
def inf(t,i):return Q(sum(t[j]!=t[j^(1<<i)] for j in range(len(t))),len(t))
def Phi(a,b):return z.packet(a,b)
def H(t):return z.raw(z.walsh(t))
def E_ne(t):return z.add(H(t),z.scale(z.phi(m(t)**2),-1))
def prob(r):return Q(0) if r<0 else Q(1,1<<r)
@lru_cache(None)
def labels(x,r,s,o):
 nr,ns=max(0,r),max(0,s);nx=int(x<0)
 out=[]
 for k in range(1<<(nx+nr+ns)):
  X=(k&1) if nx else x
  A=r>=0 and ((k>>nx)&((1<<nr)-1))==0
  B=s>=0 and (k>>(nx+nr))==0
  out.append(1 if X==0 and A else 2 if X==o and B else 0)
 return tuple(out)
@lru_cache(None)
def ft(x,r,s,u,v,o):return tuple(1 if h==0 else u[i] if h==1 else v[j] for h in labels(x,r,s,o) for j in range(len(v)) for i in range(len(u)))
def U(st):
 x,r,s,u,v,o=st;l=labels(x,r,s,o)
 return z.add(*(z.scale(E_ne(t),Q(l.count(j),len(l))) for j,t in [(1,u),(2,v)]))
def R(st):
 x,r,s,u,v,o=st;l=labels(x,r,s,o)
 return z.add(*(z.scale(z.phi(Q(l.count(j),len(l))),1-m(t)**2) for j,t in [(1,u),(2,v)]))
def bit(st,role):
 x,r,s,u,v,o=st;nu,nv=n(u),n(v)
 return 0 if role=='u' else nu if role=='v' else nu+nv if role=='X' else nu+nv+int(x<0) if role=='A' else nu+nv+int(x<0)+max(0,r)
def kids(st,role):
 x,r,s,u,v,o=st
 return tuple((b,r,s,u,v,o) if role=='X' else (x,r-1 if b==0 else -1,s,u,v,o) if role=='A' else (x,r,s-1 if b==0 else -1,u,v,o) if role=='B' else (x,r,s,z.child(u,b),v,o) if role=='u' else (x,r,s,u,z.child(v,b),o) for b in [0,1])
@lru_cache(None)
def node(st,role):
 x,r,s,u,v,o=st;f=ft(*st);w=z.walsh(f);i=bit(st,role);d=inf(f,i)
 cs=kids(st,role);kappa=z.add(R(st),z.scale(z.add(*(R(c) for c in cs)),Q(-1,2)))
 du=z.add(U(st),z.scale(z.add(*(U(c) for c in cs)),Q(-1,2)))
 D=z.add(H(f),z.scale(z.add(*(H(ft(*c)) for c in cs)),Q(-1,2)))
 B=z.add(*(Phi(w[j]**2,w[j|(1<<i)]**2) for j in range(len(w)) if not(j>>i&1)))
 if role in ['X','A','B']:
  ck(not du,'controller_U_harmonic')
  ck(z.le({},kappa),'fine_release_nonnegative')
  ck(z.interval(z.add(D,z.scale(kappa,-1),z.scale(z.log(2),-8*d)))[1]<=2*d or D==kappa,'same_tree_controller_price')
  if x<0 and role in ['A','B']:
   p,q=prob(r),prob(s);a,b=1-m(u),1-m(v);Z=p*a+(1-p)*b*q
   if o==0 and role=='B':
    expected=z.add(z.scale(z.log(2),b*b*q*(1-2*q)*(1-p)/2),Phi((1-Z/2)**2,d*d),Phi((Z/2)**2,d*d),z.scale(Phi((a-b*q)**2,(b*q)**2),p*(1-p)/2))
    ck(d==(1-p)*q*b/2,'unresolved_X_later_influence')
    ck(kappa==z.scale(z.log(2),(1-p)*q*(1-m(v)**2)/2),'unresolved_X_later_release')
    ck(z.add(B,z.scale(kappa,-1))==expected,'unresolved_X_later_exact_residual')
    ck(z.le({},expected) and z.le(expected,z.scale(z.log(2),6*d)),'unresolved_X_later_six_price')
   elif o==0 and role=='A':
    ng=1-q*b;Vg=1-ng*ng;h=m(u)-ng
    expected=z.add(z.scale(z.log(2),p*(1-m(u)**2)/2+(p-2*p*p)*(Vg+h*h)/2),z.scale(Phi((1-p)**2,p*p),Vg/2),Phi((1-Z/2)**2,p*p*h*h/4),Phi((Z/2)**2,p*p*h*h/4))
    expectedK=z.add(z.scale(z.log(2),p*(1-m(u)**2)/2),z.scale(z.add(z.phi(1-p),z.scale(z.phi(1-2*p),Q(-1,2))),q*(1-m(v)**2)/2))
    ck(B==expected,'unresolved_X_earlier_exact_erasure')
    ck(kappa==expectedK,'unresolved_X_earlier_release')
    ck(d==p*(1-m(u)*ng)/2,'unresolved_X_earlier_influence')
    ck(z.le(z.add(B,z.scale(kappa,-1)),z.scale(z.log(2),8*d)),'unresolved_X_earlier_eight_price')
   else:
    c,t=(a,p) if role=='A' else (b,q)
    expected=z.add(z.scale(z.log(2),c*c*t*(1-2*t)/2),Phi((1-(a*p+b*q)/2)**2,(c*t/2)**2),Phi(((a*p-b*q)/2)**2,(c*t/2)**2))
    ck(z.add(B,z.scale(kappa,-1))==expected,'unresolved_X_opposite_exact_residual')
    ck(d==c*t/2,'unresolved_X_opposite_influence')
    ck(z.le({},expected) and z.le(expected,z.scale(z.log(2),4*d)),'unresolved_X_opposite_four_price')
  if x==0 and o==0 and role=='B':
   p,q=prob(r),prob(s);a,b=1-m(u),1-m(v)
   expected=z.add(z.scale(z.log(2),b*b*q*(1-2*q)*(1-p)),Phi((1-a*p-b*q*(1-p))**2,(b*q*(1-p))**2),z.scale(Phi((a-b*q)**2,(b*q)**2),p*(1-p)))
   ck(d==(1-p)*q*b,'later_query_physical_influence')
   ck(kappa==z.scale(z.log(2),(1-p)*q*(1-m(v)**2)),'later_query_exact_fine_release')
   ck(z.add(B,z.scale(kappa,-1))==expected,'later_query_exact_residual')
   ck(z.le({},expected) and z.le(expected,z.scale(z.log(2),6*d)),'later_query_six_price')
  if x==0 and o==0 and role=='A':
   p,q=prob(r),prob(s);mu,nu=m(u),1-q*(1-m(v));Vg=1-nu*nu;delta=mu-nu
   expected=z.add(z.scale(z.log(2),p*(1-mu*mu)+(p-2*p*p)*(Vg+delta*delta)),z.scale(Phi((1-p)**2,p*p),Vg),Phi((nu+p*delta)**2,p*p*delta*delta))
   expectedK=z.add(z.scale(z.log(2),p*(1-mu*mu)),z.scale(z.add(z.phi(1-p),z.scale(z.phi(1-2*p),Q(-1,2))),q*(1-m(v)**2)))
   ck(B==expected,'A059_direct_earlier_erasure')
   ck(kappa==expectedK,'A059_direct_fine_release')
   ck(z.le(z.add(B,z.scale(kappa,-1)),z.scale(z.log(2),8*d)),'A059_eight_price')
  return Q(0),d
 l=labels(x,r,s,o);j=1 if role=='u' else 2;own=u if j==1 else v;q=Q(l.count(j),len(l));sq=z.walsh(own)[1]**2
 ck(kappa==z.scale(z.phi(q),sq),'data_exact_log_variance_drop')
 ck(z.interval(z.add(D,z.scale(du,-1),z.scale(kappa,-1)))[1]<=3*q*sq or not z.add(D,z.scale(du,-1),z.scale(kappa,-1)),'signed_data_three_price')
 return q*sq,Q(0)
def totalI(f):return sum((inf(f,i) for i in range(n(f))),Q(0))
@lru_cache(None)
def tree(st,policy,depth):
 x,r,s,u,v,o=st;l=labels(x,r,s,o)
 if depth==0 or len(set(l))==1:
  profile=z.add(H(ft(*st)),z.scale(U(st),-1),z.scale(R(st),-1))
  I=totalI(ft(*st))
  if len(set(l))==1:ck(z.interval(profile)[1]<=I or not profile,'resolved_terminal_profile')
  return Q(0),Q(0),profile,I,1
 controllers=(['X'] if x<0 else [])+[a for a,k in [('A',r),('B',s)] if k>0]
 data=[a for a,t in [('u',u),('v',v)] if len(t)>1]
 if policy=='priority':role=controllers[0]
 elif policy=='reverse':role=controllers[-1]
 elif policy=='alternate':
  role=max(data,key=lambda a:(abs(m(u if a=='u' else v)),a)) if data and depth%2 else controllers[-1]
 else:
  f=ft(*st);role=max(controllers+data,key=lambda a:(inf(f,bit(st,a)),a))
 T,P=node(st,role);rs=[tree(c,policy,depth-1) for c in kids(st,role)]
 return T+(rs[0][0]+rs[1][0])/2,P+(rs[0][1]+rs[1][1])/2,z.scale(z.add(rs[0][2],rs[1][2]),Q(1,2)),(rs[0][3]+rs[1][3])/2,rs[0][4]+rs[1][4]
def globalroot(st):
 for policy,depth in [('priority',99),('reverse',99),('adaptive',99),('alternate',99),('adaptive',2)]:
  T,P,profile,I,leaves=tree(st,policy,depth)
  remaining=z.add(H(ft(*st)),z.scale(U(st),-1),z.scale(R(st),-1),z.scale(profile,-1),z.scale(z.log(2),-8*P))
  ck(z.interval(remaining)[1]<=3*T+2*P or not remaining,'global_stopped_same_tree_payment')
  if depth==99:ck(z.interval(profile)[1]<=I or not profile,'global_resolved_terminal_profile')
roots=0;cores1=[tuple(1 if k>>i&1 else -1 for i in range(2)) for k in range(4)]
if LOCAL:
 cores=[tuple(1 if k>>i&1 else -1 for i in range(4)) for k in range(16)]
 for wid,(r,s) in enumerate([(1,1),(2,1),(2,2)]):
  if CHUNK is not None and wid!=CHUNK:continue
  for u,v in product(cores,repeat=2):
   for x,o in [(0,0),(-1,0),(-1,1)]:
    st=(x,r,s,u,v,o);node(st,'B');node(st,'A');roots+=1
else:
 for r,s in [(1,1),(2,1),(2,2)]:
  for o in [0,1]:
   for u,v in product(cores1,repeat=2):
    globalroot((-1,r,s,u,v,o));roots+=1
    if PILOT and roots==16:break
   if PILOT and roots==16:break
  if PILOT and roots==16:break
 if not PILOT:
  cores=[tuple(1 if k>>i&1 else -1 for i in range(4)) for k in [0,1,3,15]]
  for o in [0,1]:
   for u,v in product(cores,repeat=2):globalroot((-1,2,1,u,v,o));roots+=1
out={'status':'PASS','roots':roots,'trees':0 if LOCAL else 5*roots,'counts':COUNTS,'counted_assertions':sum(COUNTS.values()),'elapsed_seconds':time.monotonic()-START,'arithmetic':'exact Fraction Walsh and prime-log identities, rigorous48-term atanh log interval signs','helper_version':'all-order-v2-explicit-shared-rows','scope':'Arbitrary order of X/A/B controller bits and data interruptions','chunk':CHUNK}
(Path(__file__).resolve().parents[1]/'out'/(f'LOCAL_{CHUNK}.json' if LOCAL else 'PILOT.json' if PILOT else 'GLOBAL.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
