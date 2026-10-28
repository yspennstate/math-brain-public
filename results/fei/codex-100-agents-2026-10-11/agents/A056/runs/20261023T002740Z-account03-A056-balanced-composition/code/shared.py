from prior import *

COUNT=0
def check(ok):
 global COUNT
 COUNT+=1
 assert ok

def pull(P,R,childP,i,zero=None):
 """Reference joint law over the fair physical outcome and remaining spectrum."""
 out=[[Q(0)]*len(childP[0]) for _ in range(2)]
 for j in range(len(childP[0])):
  j0=(j&((1<<i)-1))|((j>>i)<<(i+1));j1=j0|(1<<i)
  p=P[j0]+P[j1];q=R[j0]+R[j1]
  kernel=[x[j]/(2*p) for x in childP] if p else (zero(j0) if zero else [Q(1,2)]*2)
  check(sum(kernel)==1)
  for t in range(2):out[t][j]=q*kernel[t]
 check(sum(map(sum,out))==1)
 return out

def calibrate(P,R,labels):
 z=sum(R);check(z>0);R=[q/z for q in R];out=[Q(0)]*len(P)
 groups={}
 for j,l in enumerate(labels):groups.setdefault(l,[]).append(j)
 for ids in groups.values():
  p=sum(P[j] for j in ids);q=sum(R[j] for j in ids)
  check(not p or q>0)
  for j in ids:out[j]=R[j]*p/q if p else Q(0)
 check(sum(out)==1)
 return tuple(out),z

def phase_children(u,ru,i):
 us=[restrict(u,i,t) for t in range(2)];ps=[prob(x) for x in us]
 raw=pull(prob(u),ru,ps,i)
 refs=[];zs=[]
 for p,q in zip(ps,raw):
  rr,z=calibrate(p,q,['empty']+['nonempty']*(len(p)-1));refs.append(rr);zs.append(z)
 return us,refs,zs

def refined_label(s,idx):
 owner=s.label(idx)
 if owner[0] in ['a','b']:
  return owner+(bool(idx&((1<<s.k)-1)),)
 return owner

def shared(s,i):
 us,rus,zus=phase_children(s.u,s.ru,i);vs,rvs,zvs=phase_children(s.v,s.rv,i)
 children=[State(us[t],vs[t],rus[t],rvs[t],s.na,s.nb,s.ea,s.eb,s.z) for t in range(2)]
 for t,c in enumerate(children):check(c.f==restrict(s.f,i,t))
 def zero(j0):
  # All reference-only nonempty child-phase fibers have synchronized fair
  # phase and root zero extensions. Empty child-phase fibers are calibrated.
  return [Q(1,2)]*2
 raw=pull(s.P,s.Q,[c.P for c in children],i,zero)
 rootzs=[];calibration={};carried=[]
 for c,q in zip(children,raw):
  rr,z=calibrate(c.P,q,[refined_label(c,j) for j in range(len(c.P))]);rootzs.append(z)
  check(rr==tuple(c.Q))
  rq=[x/z for x in q];carried.append(ce(c.P,rq))
  calibration=add(calibration,add(ce(c.P,rq),c.CE,-1),Q(1,2))
  check(nonnegative(add(ce(c.P,rq),c.CE,-1)))
 check(nonnegative(calibration))
 expected_release=add(scale(add(s.du,add(children[0].du,children[1].du),-Q(1,2)),s.pi*s.a*(1-s.a)),add(s.dv,add(children[0].dv,children[1].dv),-Q(1,2)),(1-s.pi)*s.b*(1-s.b))
 release=add(s.debt,add(children[0].debt,children[1].debt),-Q(1,2))
 check(release==expected_release);check(nonnegative(release))
 # Exact outcome KL and residual conditional-erasure KL include every Z.
 outcome=scale(add(log(2*rootzs[0]),log(2*rootzs[1])),-Q(1,2))
 erased=add(add(release,outcome,-1),calibration,-1)
 # Reconstruct pair-conditional KL directly, independently of the release.
 erased_direct={}
 for j in range(len(children[0].P)):
  j0=(j&((1<<i)-1))|((j>>i)<<(i+1));ids=[j0,j0|(1<<i)]
  pm=sum(s.P[x] for x in ids);qm=sum(s.Q[x] for x in ids)
  if pm:
   for x in ids:
    if s.P[x]:erased_direct=add(erased_direct,log((s.P[x]/pm)/(s.Q[x]/qm)),s.P[x])
 check(erased==erased_direct)
 check(nonnegative(outcome));check(nonnegative(erased))
 terminals=scale(add(children[0].CE,children[1].CE),Q(1,2))
 drop=add(s.H,scale(add(children[0].H,children[1].H),Q(1,2)),-1)
 B=erasure(s.f,i);js=add(drop,B,-1)
 check(nonnegative(js))
 check(add(add(add(add(terminals,B),js),outcome),add(erased,calibration))==s.CE)
 # A complete original rate7 account, with query influence already booked,
 # retains the full H+KL terminal bills and all reference normalizers.
 complete=add(add(add(add(add(terminals,B),js),outcome),erased),calibration)
 check(nonnegative(add({2:7*s.I},complete,-1)))
 # Stronger terminal admission, separately checked, does NOT follow merely
 # from the exact conservation identity.
 inf=edge_inf(s.f,i);remain=sum((c.I for c in children),Q(0))/2
 check(s.I==inf+remain)
 terminal_margin=add({2:7*remain},terminals,-1)
 check(nonnegative(terminal_margin))
 return {'root_normalizers':[str(z) for z in rootzs],'phase_u_normalizers':[str(z) for z in zus],'phase_v_normalizers':[str(z) for z in zvs],'release':ser(release),'outcome_KL':ser(outcome),'erasure_KL':ser(erased),'categorical_savings':ser(calibration),'terminal_KL':ser(scale(add(children[0].debt,children[1].debt),Q(1,2))),'terminal_margin':ser(terminal_margin),'both_nonconstant':all(c.I>0 for c in children)},children

def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;nr=nt=both=0;examples=[]
 domains=[(2,uc,vc,na,nb,w) for uc in ([7] if pilot else range(16)) for vc in ([1] if pilot else range(16)) for na,nb in ([(1,1)] if pilot else [(1,1),(2,1)]) for w in [False,True]]
 if not pilot:
  for uc in range(256):
   u=table(3,uc)
   v=tuple(u[((x<<1)&7)|(x>>2)^1] for x in range(8))
   vc=sum((1<<x) for x,a in enumerate(v) if a==1)
   domains.extend((3,uc,vc,1,1,w) for w in [False,True])
 lane=int(sys.argv[sys.argv.index('--lane')+1]) if '--lane' in sys.argv else None
 if lane is not None:domains=[x for j,x in enumerate(domains) if j%4==lane]
 for k,uc,vc,na,nb,w in domains:
  check(time.perf_counter()-start<55)
  u=table(k,uc);v=table(k,vc);ru=phase_ref(u,w);rv=phase_ref(v,w)
  check(nonnegative(add({2:6*influence(u)},ce(prob(u),ru),-1)))
  check(nonnegative(add({2:6*influence(v)},ce(prob(v),rv),-1)))
  s=State(u,v,ru,rv,na,nb);nr+=1
  for i in range(k):
   try:rec,cs=shared(s,i)
   except Exception:
    (R/'out/FAILURE.json').write_text(json.dumps({'k':k,'uc':uc,'vc':vc,'na':na,'nb':nb,'weighted':w,'i':i,'assertions_before_failure':COUNT},indent=2),encoding='utf-8');raise
   nt+=1;both+=rec['both_nonconstant']
   if k==3 and w and rec['both_nonconstant'] and rec['terminal_KL'] and len(examples)<4:examples.append(dict(k=k,uc=uc,vc=vc,i=i,**rec))
 result={'helper_version':'A056-shared-phase-query-v1','pilot':pilot,'roots':nr,'shared_transports':nt,'both_nonconstant_child_cases':both,'assertions':COUNT,'status':'PASS','runtime_seconds':time.perf_counter()-start,'nonflat_terminal_debt_examples':examples}
 (R/'out'/('lane'+str(lane)+'.json' if lane is not None else 'pilot.json' if pilot else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
