from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time,sys,math
import primitives as z
START=time.monotonic();PILOT='--pilot' in sys.argv;COUNTS={}
def ck(a,key):
 assert a,key
 COUNTS[key]=COUNTS.get(key,0)+1
 if time.monotonic()-START>(55 if PILOT else 170):raise RuntimeError('frozen watchdog')
e0=sum((Q(1,math.factorial(j)) for j in range(31)),Q(0))
lnlo,lnhi=z.logint(2)
cdlo=1/lnhi+2/((e0+Q(32,31*math.factorial(31)))*lnhi)
def totalI(t):
 n=len(t).bit_length()-1
 return sum((Q(sum(t[j]!=t[j^(1<<i)] for j in range(len(t))),len(t)) for i in range(n)),Q(0))
def mean(t):return Q(sum(t),len(t))
@lru_cache(None)
def controls(r,s,o):
 C=[];D=[]
 for j in range(1<<(1+r+s)):
  x=j&1;A=((j>>1)&((1<<r)-1))==0;B=(j>>(1+r))==0
  c=x==0 and A;d=x==o and B and not c
  C.append(int(c));D.append(int(d))
 return tuple(C),tuple(D)
@lru_cache(None)
def Ftable(u,v,r,s,o):
 C,D=controls(r,s,o)
 return tuple(u[i] if c else v[j] if d else 1 for c,d in zip(C,D) for j in range(len(v)) for i in range(len(u)))
@lru_cache(None)
def node(u,v,r,s,o,role):
 own,other=(u,v) if role==0 else (v,u)
 C,D=controls(r,s,o);S=C if role==0 else D;O=D if role==0 else C
 q=Q(sum(S),len(S));m=mean(own);var=1-m*m;beta=z.walsh(own)[1];t=beta*beta
 aa=tuple(m*c+d*b+(1-c-d) for c,d in zip(S,O) for b in other)
 cc=tuple(c for c in S for b in other)
 aw=z.walsh(aa);cw=z.walsh(cc)
 ck(sum(a*a for a in aw)==1-q*var,'Parseval_recentered')
 ck(sum(c*c for c in cw)==q,'Parseval_selector')
 def M(h):return z.add(*(z.packet(a*a,h*c*c) for a,c in zip(aw,cw)))
 mt,mv=M(t),M(var)
 hb=z.packet(1-q*var,q*var)
 ck(z.le(mv,hb),'Jensen_selector_entropy')
 cap=z.pick_min(mv,z.add(z.scale(mv,t/var),z.scale(z.log(var/t),q*t))) if t else {}
 ck(z.le(mt,cap),'exact_cap_envelope')
 # Bound in nats by a rational lower enclosure of its analytic RHS.
 rhs=z.add(z.scale(z.log(1/q),q*t),z.scale(z.log(2),cdlo*q*z.inf(own)))
 ck(z.le(cap,rhs),'local_selector_variance_price')
 return cap,mt,q,t
def rootdirect(u,v,r,s,o,role):
 cap,mt,q,t=node(u,v,r,s,o,role)
 own=u if role==0 else v
 fw=z.walsh(Ftable(u,v,r,s,o));bit=0 if role==0 else len(u).bit_length()-1
 actual=z.add(*(z.packet(fw[j]**2,fw[j|(1<<bit)]**2) for j in range(len(fw)) if not (j>>bit&1)))
 uw=z.walsh(own);inner=z.add(*(z.packet(uw[2*j]**2,uw[2*j+1]**2) for j in range(len(uw)//2)))
 ck(actual==z.add(z.scale(z.add(inner,z.scale(z.packet(mean(own)**2,t),-1)),q),mt),'direct_signed_split')
@lru_cache(None)
def tree(u,v,r,s,o,policy,depth):
 if (len(u)==1 and len(v)==1) or depth==0:return {},Q(0),Q(0),Q(0)
 choices=[j for j,a in enumerate([u,v]) if len(a)>1]
 role=choices[0] if policy=='u_first' else choices[-1] if policy=='v_first' else max(choices,key=lambda j:(z.inf([u,v][j]),j))
 cap,mt,q,t=node(u,v,r,s,o,role)
 own=[u,v][role];l=[]
 for b in [0,1]:
  uu,vv=(z.child(u,b),v) if role==0 else (u,z.child(v,b))
  l.append(tree(uu,vv,r,s,o,policy,depth-1))
 return (z.add(cap,z.scale(z.add(l[0][0],l[1][0]),Q(1,2))),q*z.inf(own)+(l[0][1]+l[1][1])/2,
         (t if role==0 else 0)+(l[0][2]+l[1][2])/2,(t if role==1 else 0)+(l[0][3]+l[1][3])/2)
def checkroot(u,v,r,s,o):
 p=Q(1,1<<r);k=Q(1,1<<s);P=p/2;Qv=k/2;R=(1-p)*Qv if o==0 else Qv
 mu,nu=mean(u),mean(v);a,b=1-mu,1-nu
 X=P*a+R*b if o==0 else P*a+Qv*b-p*k*a*b/2
 A=p*((1-k)*a/2+k*(1-mu*nu)/2) if o==0 else P*a
 B=R*b
 ctrl=X+r*A+s*B;data=P*totalI(u)+R*totalI(v)
 ft=Ftable(u,v,r,s,o)
 ck(totalI(ft)==ctrl+data,'direct_exclusive_total_influence')
 n=len(u).bit_length()-1;nv=len(v).bit_length()-1
 for j,target in [(n+nv,X)]+[(n+nv+1+i,A) for i in range(r)]+[(n+nv+1+r+i,B) for i in range(s)]:
  ck(Q(sum(ft[h]!=ft[h^(1<<j)] for h in range(len(ft))),len(ft))==target,'direct_exclusive_coordinate_influence')
 reserve=z.add(z.scale(z.log(1/P),P*(1-mu*mu)),z.scale(z.log(1/R),R*(1-nu*nu)))
 ck(z.le(reserve,z.scale(z.log(2),4*ctrl)),'exclusive_variance_reserve')
 rootdirect(u,v,r,s,o,0);rootdirect(u,v,r,s,o,1)
 for policy in ['u_first','v_first','adaptive_inf']:
  bank,spent,Vu,Vv=tree(u,v,r,s,o,policy,20)
  ck(spent==data,'complete_data_influence_telescope')
  ck(Vu==1-mu*mu and Vv==1-nu*nu,'two_variance_telescope')
  rhs=z.add(z.scale(z.log(2),cdlo*spent),z.scale(z.log(1/P),P*Vu),z.scale(z.log(1/R),R*Vv))
  ck(z.le(bank,rhs),'complete_capped_selector_bank')
  ck(z.le(bank,z.scale(z.log(2),4*(ctrl+data))),'complete_four_influence_bank')
 bank,spent,Vu,Vv=tree(u,v,r,s,o,'adaptive_inf',1)
 rhs=z.add(z.scale(z.log(2),cdlo*spent),z.scale(z.log(1/P),P*Vu),z.scale(z.log(1/R),R*Vv))
 ck(z.le(bank,rhs),'partial_actual_leaf_variance_bound')
 ck(z.le(bank,z.scale(z.log(2),4*(ctrl+data))),'partial_four_influence_bank')
cores=[tuple(1 if mask>>i&1 else -1 for i in range(4)) for mask in range(16)]
roots=0
for u in cores:
 for v in cores:
  for r,s in [(1,1),(1,2),(2,1)]:
   for o in [0,1]:
    checkroot(u,v,r,s,o);roots+=1
    if PILOT and roots==16:break
   if PILOT and roots==16:break
  if PILOT and roots==16:break
 if PILOT and roots==16:break
result={'status':'PASS','roots':roots,'trees':4*roots,'counts':COUNTS,'elapsed_seconds':time.monotonic()-START,'arithmetic':'integer Walsh/Fraction prime-log equalities; 48-term rational atanh log intervals and factorial e bounds','c_data_lower':str(cdlo),'maximum_physical_dimension':8,'helper':'selector-cap-v1'}
(Path(__file__).resolve().parents[1]/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
