from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import primitives as z
import json,time,math,sys
start=time.monotonic();pilot='--pilot' in sys.argv;counts={}
def ck(ok,name):
 assert ok,name
 counts[name]=counts.get(name,0)+1
 if time.monotonic()-start>55:raise RuntimeError('frozen watchdog')
def I(t):
 return sum((Q(sum(t[j]!=t[j^(1<<i)] for j in range(len(t))),len(t)) for i in range(len(t).bit_length()-1)),Q(0))
def mean(t):return Q(sum(t),len(t))
elo=sum((Q(1,math.factorial(j)) for j in range(31)),Q(0));ehi=elo+Q(32,31*math.factorial(31))
llo,lhi=z.logint(2);cdlo=(1+2/ehi)/lhi;cdhi=(1+2/elo)/llo
ck(2<cdlo<cdhi<4,'analytic_constant')
def ftable(labels,u,v):
 return tuple(1 if h==0 else u[a] if h==1 else v[b] for h in labels for b in range(len(v)) for a in range(len(u)))
def ncap(labels,u,v,role):
 own,other=(u,v) if role==0 else (v,u);select=role+1;q=Q(labels.count(select),len(labels))
 if not q:return {},Q(0),Q(0)
 m=mean(own);V=1-m*m;t=z.walsh(own)[1]**2
 av=tuple(m if h==select else 1 if h==0 else b for h in labels for b in other)
 cv=tuple(int(h==select) for h in labels for b in other)
 aw,cw=z.walsh(av),z.walsh(cv)
 def M(s):return z.add(*(z.packet(a*a,s*c*c) for a,c in zip(aw,cw)))
 mv,mt=M(V),M(t)
 cap=z.pick_min(mv,z.add(z.scale(mv,t/V),z.scale(z.log(V/t),q*t))) if t else {}
 N=z.add(*(z.add(z.paird(a,z.walsh(own)[1]*c),z.scale(z.packet(a*a,t*c*c),-1)) for a,c in zip(aw,cw)))
 ck(z.le({},N),'coherent_JS_nonnegative')
 ck(z.interval(N)[1]<=2*q*t or not N,'coherent_JS_singleton_price')
 ck(z.le(mv,z.packet(1-q*V,q*V)),'Jensen_packet_bound')
 ck(z.le(mt,cap),'cap_dominates_actual_M')
 fw=z.walsh(ftable(labels,u,v));bit=0 if role==0 else len(u).bit_length()-1
 B=z.add(*(z.packet(fw[j]**2,fw[j|(1<<bit)]**2) for j in range(len(fw)) if not(j>>bit&1)))
 uw=z.walsh(own);inner=z.add(*(z.packet(uw[2*j]**2,uw[2*j+1]**2) for j in range(len(uw)//2)))
 ck(B==z.add(z.scale(z.add(inner,z.scale(z.packet(m*m,t),-1)),q),mt),'direct_arbitrary_selector_split')
 return cap,q*z.inf(own),t
def tree(labels,u,v,policy,depth):
 if depth==0 or len(u)==len(v)==1:return {},Q(0),Q(0),Q(0)
 roles=[j for j,a in enumerate([u,v]) if len(a)>1]
 role=roles[0] if policy==0 else roles[-1] if policy==1 else max(roles,key=lambda j:(z.inf([u,v][j]),j))
 cap,cost,t=ncap(labels,u,v,role);res=[]
 for b in [0,1]:res.append(tree(labels,z.child(u,b) if role==0 else u,z.child(v,b) if role==1 else v,policy,depth-1))
 return z.add(cap,z.scale(z.add(res[0][0],res[1][0]),Q(1,2))),cost+(res[0][1]+res[1][1])/2,(t if role==0 else 0)+(res[0][2]+res[1][2])/2,(t if role==1 else 0)+(res[0][3]+res[1][3])/2
cores=[tuple(1 if mask>>j&1 else -1 for j in range(2)) for mask in range(4)]
roots=0
for labels in product(range(3),repeat=4):
 probs=[Q(labels.count(j),4) for j in [1,2]]
 sels=[tuple(int(h==j) for h in labels) for j in [1,2]]
 for q,c in zip(probs,sels):
  ck(z.le(z.scale(z.log(1/q),q) if q else {},z.scale(z.log(2),I(c)/2)),'exact_indicator_isoperimetry')
 for u,v in product(cores,repeat=2):
  mus=[mean(u),mean(v)];Vs=[1-m*m for m in mus]
  ctrl=sum((Q(sum((1-mus[a-1]*mus[b-1])/2 if a and b else (1-mus[(a or b)-1])/2 if a or b else 0 for k,a in enumerate(labels) for b in [labels[k^(1<<i)]] if a!=b),4) for i in range(2)),Q(0))
  ck(sum(V*I(c) for V,c in zip(Vs,sels))<=4*ctrl,'single_edge_both_variances')
  reserve=z.add(*(z.scale(z.log(1/q),q*V) if q else {} for q,V in zip(probs,Vs)))
  ck(z.le(reserve,z.scale(z.log(2),2*ctrl)),'two_control_influence_reserve')
  data=probs[0]*I(u)+probs[1]*I(v)
  ck(I(ftable(labels,u,v))==data+ctrl,'actual_total_influence')
  for policy,depth in [(0,4),(1,4),(2,4),(2,1)]:
   bank,spent,V1,V2=tree(labels,u,v,policy,depth)
   rhs=z.add(z.scale(z.log(2),cdlo*spent),*(z.scale(z.log(1/q),q*V) if q else {} for q,V in zip(probs,[V1,V2])))
   ck(z.le(bank,rhs),'partial_or_complete_selector_price')
   ck(z.le(bank,z.scale(z.log(2),cdlo*data+2*ctrl)),'exclusive_general_bank')
   ck(z.le(bank,z.scale(z.log(2),cdlo*(data+ctrl))),'c_data_full_influence_bound')
   if depth==4:ck(spent==data and (probs[0]==0 or V1==Vs[0]) and (probs[1]==0 or V2==Vs[1]),'actual_variance_and_influence_telescope')
  roots+=1
  if pilot and roots==16:break
 if pilot and roots==16:break
result={'status':'PASS','roots':roots,'trees':4*roots,'counts':counts,'elapsed_seconds':time.monotonic()-start,'constant_interval_rational':[str(cdlo),str(cdhi)],'arithmetic':'exact Fraction Walsh/edge counts and rational prime-log certificates','controller_domain':'all 3^4 label partitions on two control bits; all 4^2 ordered one-bit core pairs; no symmetry reduction'}
(Path(__file__).resolve().parents[1]/'out'/('CONTROLLERS_PILOT.json' if pilot else 'CONTROLLERS.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
