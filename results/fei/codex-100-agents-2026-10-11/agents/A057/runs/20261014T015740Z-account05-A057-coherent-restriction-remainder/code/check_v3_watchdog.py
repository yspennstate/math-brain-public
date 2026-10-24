from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import time,json,sys,math
import primitives as z
START=time.monotonic();PILOT='--pilot' in sys.argv;COUNTS={}
def ck(ok,name):
 assert ok,name
 COUNTS[name]=COUNTS.get(name,0)+1
 if time.monotonic()-START>(55 if PILOT else 170):raise RuntimeError('frozen watchdog')
def m(u):return Q(sum(u),len(u))
def dims(u):return len(u).bit_length()-1
def influence(t,bit):return Q(sum(t[j]!=t[j^(1<<bit)] for j in range(len(t))),len(t))
def probs(labels):return Q(labels.count(1),len(labels)),Q(labels.count(2),len(labels))
@lru_cache(None)
def ft(labels,u,v):return tuple(1 if a==0 else u[x] if a==1 else v[y] for a in labels for y in range(len(v)) for x in range(len(u)))
@lru_cache(None)
def H(t):return z.raw(z.walsh(t))
def ene(u):return z.add(H(u),z.scale(z.phi(m(u)**2),-1))
def U(labels,u,v):return z.add(*(z.scale(ene(a),q) for a,q in zip([u,v],probs(labels))))
def R(labels,u,v):return z.add(*(z.scale(z.phi(q),1-m(a)**2) for a,q in zip([u,v],probs(labels))))
def classI(labels,u,v):
 t=ft(labels,u,v);nu,nv=dims(u),dims(v)
 data=sum((influence(t,i) for i in range(nu+nv)),Q(0));ctrl=sum((influence(t,i) for i in range(nu+nv,dims(t))),Q(0))
 return data,ctrl
@lru_cache(None)
def children(labels,u,v,role):
 return tuple((labels[b::2],u,v) if role==0 else (labels,z.child(u,b),v) if role==1 else (labels,u,z.child(v,b)) for b in [0,1])
@lru_cache(None)
def local(labels,u,v,role):
 state=(labels,u,v);cs=children(*state,role)
 release=z.add(R(*state),z.scale(z.add(*(R(*c) for c in cs)),Q(-1,2)))
 bit=dims(u)+dims(v) if role==0 else 0 if role==1 else dims(u)
 t=ft(*state);d=influence(t,bit)
 Delta=z.add(H(t),z.scale(z.add(*(H(ft(*c)) for c in cs)),Q(-1,2)))
 du=z.add(U(*state),z.scale(z.add(*(U(*c) for c in cs)),Q(-1,2)))
 if role==0:
  ck(not du,'control_U_no_reset')
  ck(z.le({},release),'control_R_nonnegative_release')
  ck(z.le(release,z.scale(z.log(2),2*d)),'control_R_local_two_influence')
  # Independent probability-slice formula for the exact reserve release.
  exact=z.add(*(z.scale(z.add(z.phi(q),z.scale(z.add(z.phi(qp),z.phi(qm)),Q(-1,2))),1-m(a)**2) for a,q,qp,qm in zip([u,v],probs(labels),probs(cs[0][0]),probs(cs[1][0]))))
  ck(release==exact,'exact_controller_release_formula')
  return {},{},release,{}, {},{},d,Delta
 own,other=(u,v) if role==1 else (v,u);q=probs(labels)[role-1];V=1-m(own)**2;beta=z.walsh(own)[1];sq=beta*beta
 ck(release==z.scale(z.phi(q),sq),'exact_data_reserve_drop')
 ck(d==q*z.inf(own),'physical_data_influence')
 av=tuple(m(own) if a==role else 1 if a==0 else b for a in labels for b in other)
 cv=tuple(int(a==role) for a in labels for b in other)
 aw,cw=z.walsh(av),z.walsh(cv)
 def M(s):return z.add(*(z.packet(a*a,s*c*c) for a,c in zip(aw,cw)))
 mt,mv=M(sq),M(V)
 cap=z.pick_min(mv,z.add(z.scale(mv,sq/V),z.scale(z.log(V/sq),q*sq))) if sq and q else {}
 N=z.add(*(z.add(z.paird(a,beta*c),z.scale(z.packet(a*a,sq*c*c),-1)) for a,c in zip(aw,cw)))
 fw=z.walsh(t);B=z.add(*(z.packet(fw[j]**2,fw[j|(1<<bit)]**2) for j in range(len(fw)) if not(j>>bit&1)))
 uw=z.walsh(own);Bi=z.add(*(z.packet(uw[2*j]**2,uw[2*j+1]**2) for j in range(len(uw)//2)))
 ck(B==z.add(z.scale(z.add(Bi,z.scale(z.packet(m(own)**2,sq),-1)),q),mt),'direct_signed_erasure')
 sing=z.scale(z.phi(sq),q)
 ck(Delta==z.add(du,z.scale(sing,-1),mt,N),'direct_signed_decrement')
 ck(z.le(mt,cap),'cap_dominates_M')
 ck(z.le({},N) and (not N or z.interval(N)[1]<=2*q*sq),'unnormalized_N_price')
 ck(z.le(cap,z.add(z.scale(z.log(2),cdlo*d),release)),'local_cap_variance_price')
 return cap,N,{},release,sing,z.add(mt,N),d,Delta
elo=sum((Q(1,math.factorial(j)) for j in range(31)),Q(0));ehi=elo+Q(32,31*math.factorial(31));llo,lhi=z.logint(2)
cdlo=(1+2/ehi)/lhi;cdhi=(1+2/elo)/llo
# Rational lower prices permit rigorous sufficient-sign comparisons in natural units.
crlo=cdlo+2/lhi
@lru_cache(None)
def tree(labels,u,v,policy,depth):
 state=(labels,u,v)
 if depth==0 or len(labels)==len(u)==len(v)==1:
  return ({},{},{},{},{},{},Q(0),Q(0),H(ft(*state)),U(*state),R(*state),classI(*state)[0],classI(*state)[1],{})
 roles=[i for i,a in enumerate(state) if len(a)>1]
 if policy=='control_first':role=roles[0]
 elif policy=='data_first':role=next((a for a in roles if a>0),0)
 elif policy=='one_reset':role=1 if depth==2 and 1 in roles else 0 if 0 in roles else roles[0]
 else:
  f=ft(*state)
  role=max(roles,key=lambda a:(influence(f,dims(u)+dims(v) if a==0 else 0 if a==1 else dims(u)),a))
 cap,N,L,Dr,Sing,outer,d,Delta=local(*state,role)
 sub=[tree(*c,policy,depth-1) for c in children(*state,role)]
 # cap, N, controller release, data reserve spend, singleton, outer data,
 # spent data I, spent ctrl I, expected leaf H/U/R/dataI/ctrlI; ctrl Delta separately below.
 out=[z.add(x,z.scale(z.add(sub[0][i],sub[1][i]),Q(1,2))) for i,x in enumerate([cap,N,L,Dr,Sing,outer])]
 out.extend([(d if role else 0)+(sub[0][6]+sub[1][6])/2,(d if role==0 else 0)+(sub[0][7]+sub[1][7])/2])
 out.extend([z.scale(z.add(sub[0][i],sub[1][i]),Q(1,2)) for i in [8,9,10]])
 out.extend([(sub[0][i]+sub[1][i])/2 for i in [11,12]])
 out.append(z.add(Delta if role==0 else {},z.scale(z.add(sub[0][13],sub[1][13]),Q(1,2))))
 return tuple(out)
@lru_cache(None)
def ctrl_delta(labels,u,v,policy,depth):
 return tree(labels,u,v,policy,depth)[13]
def root(labels,u,v):
 data,ctrl=classI(labels,u,v);rr=R(labels,u,v)
 ck(z.le(rr,z.scale(z.log(2),2*ctrl)),'root_exclusive_reserve')
 for policy,depth in [('control_first',99),('data_first',99),('adaptive_inf',99),('one_reset',2)]:
  a=tree(labels,u,v,policy,depth)
  ck(rr==z.add(a[10],a[2],a[3]),'exact_interleaved_R_telescope')
  ck(data==a[6]+a[11] and ctrl==a[7]+a[12],'exact_block_influence_telescope')
  ck(H(ft(labels,u,v))==z.add(a[8],U(labels,u,v),z.scale(a[9],-1),z.scale(a[4],-1),a[5],a[13]),'exact_interleaved_signed_entropy_ledger')
  rhs=z.add(z.scale(z.log(2),cdlo*a[6]),rr,z.scale(a[10],-1),z.scale(a[2],-1))
  ck(z.le(a[0],rhs),'stopped_cap_no_reset_price')
  rhsN=z.add(z.scale(z.log(2),crlo*a[6]),rr,z.scale(a[10],-1),z.scale(a[2],-1))
  ck(z.le(z.add(a[0],a[1]),rhsN),'stopped_coherent_no_reset_price')
  ck(z.le(a[0],z.scale(z.log(2),cdlo*data+2*ctrl)),'root_cap_interleaved_price')
  ck(z.le(z.add(a[0],a[1]),z.scale(z.log(2),crlo*data+2*ctrl)),'root_coherent_interleaved_price')
  if policy=='data_first' and depth==99:
   # All data nodes precede controls; the exact controller entropy term is actual leaf entropy at that frontier.
   ck(z.le({},ctrl_delta(labels,u,v,policy,depth)),'controller_entropy_decrements_nonnegative')
  if PILOT and COUNTS.get('root_cap_interleaved_price',0)>=64:return
cores1=[tuple(1 if k>>j&1 else -1 for j in range(2)) for k in range(4)]
roots=0
for labels in product(range(3),repeat=4):
 for u,v in product(cores1,repeat=2):
  root(labels,u,v);roots+=1
  if PILOT and roots==16:break
 if PILOT and roots==16:break
if not PILOT:
 cores2=[tuple(1 if k>>j&1 else -1 for j in range(4)) for k in range(16)]
 for o in [0,1]:
  labels=tuple(1 if (x&1)==0 and (x>>1&1)==0 else 2 if (x&1)==o and (x>>2&1)==0 else 0 for x in range(8))
  for u,v in product(cores2,repeat=2):root(labels,u,v);roots+=1
sharp_labels=(1,2);sharp_u=sharp_v=(1,-1)
release=local(sharp_labels,sharp_u,sharp_v,0)[2]
ck(release==z.log(2),'sharp_control_release_one_bit')
ck(influence(ft(sharp_labels,sharp_u,sharp_v),2)==Q(1,2),'sharp_control_half_influence')
result={'status':'PASS','roots':roots,'trees':4*roots,'counts':COUNTS,'elapsed_seconds':time.monotonic()-START,'constant_interval_rational':[str(cdlo),str(cdhi)],'arithmetic':'integer Walsh/Fraction prime-log equality, rational 48-term atanh logs and factorial e enclosures','sharp_release_bits':'1','sharp_control_influence':'1/2','max_physical_dimension':7,'helper_version':'interleaved-selector-v3-controller-slot-correction'}
(Path(__file__).resolve().parents[1]/'out'/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
