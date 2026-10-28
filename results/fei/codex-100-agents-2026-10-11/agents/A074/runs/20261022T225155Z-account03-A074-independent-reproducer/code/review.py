"""A074 independent donor audit: binary differences, conditional entropy, no peer imports."""
from pathlib import Path
import importlib.util,sys,json,time,itertools,hashlib
from fractions import Fraction as F
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
own=R.parent/'20261021T152214Z-account03-A074-independent-reproducer/code/reproduce.py'
spec=importlib.util.spec_from_file_location('a074_own',own);c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
c.K=F(4)
START=time.perf_counter();COUNT=0
def ck(x):
 global COUNT
 COUNT+=1
 if not x:raise AssertionError(COUNT)
def save(n,z):(R/'out'/n).write_text(json.dumps(z,indent=2,default=str)+'\n',encoding='utf-8')
def avg(xs):return c.scale(c.add(*xs),F(1,len(xs)))
def overlap(x,y):ck(max(x[0],y[0])<=min(x[1],y[1]))
def clean(p):return {k:v for k,v in p.items() if v}
def pa(*ps):
 z={}
 for p in ps:
  for k,v in p.items():z[k]=z.get(k,F(0))+v
 return clean(z)
def pm(p,r):return clean({k:v*r for k,v in p.items()})
def ps(p,q):return pa(p,pm(q,-1))
def pe(masses):
 z={}
 for x in masses:
  if x and x!=1:z[x]=z.get(x,F(0))-x
 return clean(z)
def const(v):return {None:v} if v else {}
def meanp(ps):return pm(pa(*ps),F(1,len(ps)))
def digestp(p):return hashlib.sha256(json.dumps(sorted((str(k),str(v)) for k,v in p.items())).encode()).hexdigest()
def form(P,j):
 # Entropy conditioned on occupied blocks, not source's H(mask)-sum q*h2 path.
 hp=pe(P['masses'])
 hc=[];sc=[]
 for q,z in zip(P['q'],P['cs']):
  masses=[F(w*w,len(z['t'])**2) for w in z['W']]
  h=pe(masses);hc.append(h);sc.append(ps(const(4*z['I']),h))
  if z['v']:
   hp=pa(hp,pm(pe([x/z['v'] for x in masses[1:] if x]),q*z['v']))
 sp=ps(const(4*P['I']),hp);up=pm(sc[j],P['q'][j]);ap=pa(*(pm(s,q) for k,(s,q) in enumerate(zip(sc,P['q'])) if k!=j))
 cp=ps(hp,pa(*(pm(h,q) for h,q in zip(hc,P['q']))));mp=ps(ap,cp)
 ck(sp==pa(up,mp))
 return dict(H=hp,S=sp,U=up,A=ap,C=cp,M=mp)
def split(P,tables,j,i):
 ts=[];children=[]
 for bit in (0,1):
  z=list(tables);z[j]=c.restrict(z[j],i,bit);z=tuple(z);ts.append(z);children.append(c.packet(z))
 # Distinguish an inner dummy from an outer gate that ignores this block.
 d=P['q'][j]*P['cs'][j]['inf'][i]
 ck(P['I']-sum(z['I'] for z in children)/2==d)
 for k in range(6):ck(sum(z['q'][k] for z in children)/2==P['q'][k])
 dh=c.sub(P['H'],avg([z['H'] for z in children]))
 if not d:
  if P['cs'][j]['inf'][i]==0:ck(ts[0][j]==ts[1][j])
  else:
   ck(P['q'][j]==0)
   for x in range(64):
    if x>>j&1:continue
    prob=F(1)
    for k in range(6):
     if k!=j:prob*=P['p'][k] if x>>k&1 else 1-P['p'][k]
    if prob:ck(c.J[x]==c.J[x|(1<<j)])
  # The full physical functions coincide by the checked support condition.
  c.zero(dh);dh=c.point(0)
 e=c.sub(dh,c.point(4*d));edge=dict(d=d,e=e,e4=e)
 return ts,children,edge
def components(P,j):
 U=c.scale(c.sub(c.point(4*P['cs'][j]['I']),P['cs'][j]['H']),P['q'][j]);M=c.sub(P['S'],U)
 if M[0]>0:V,W=U,M
 elif M[1]<0:V,W=P['S'],c.point(0)
 else:ck(M==c.point(0));V,W=U,c.point(0)
 ck(V[0]>=0);ck(W[0]>=0);c.pos(P['S']);return U,M,V,W
def allocation_grid():
 n=0;vertices=0
 for v0,v1,w0,w1 in itertools.product(range(3),repeat=4):
  V=[F(v0),F(v1)];W=[F(w0),F(w1)];S=[V[i]+W[i] for i in range(2)]
  for k in range(int(sum(S))+1):
   T=F(k,2);bv=sum(V)/2;bw=sum(W)/2
   # Every breakpoint is integer in this frozen domain. Exhaust ALL integer
   # feasible d0 values rather than the source's targeted breakpoint list.
   values=[]
   for a in range(int(S[0])+1):
    b=2*T-a
    if 0<=b<=S[1]:values.append((max(F(a)-V[0],F(0))+max(b-V[1],F(0)))/2);vertices+=1
   ck(bool(values));opt=min(values);ck(opt==max(F(0),T-bv))
   if T<=bv:debit=[T*z/bv if bv else F(0) for z in V]
   else:debit=[V[i]+(T-bv)*W[i]/bw for i in range(2)]
   ck(sum(debit)/2==T);ck(all(0<=debit[i]<=S[i] for i in range(2)))
   ck(sum(max(debit[i]-V[i],F(0)) for i in range(2))/2==opt)
   if T==sum(S)/2:ck(debit==S)
   if T:
    old=[(T+1)*x/T for x in debit];credit=[-x/T for x in debit]
    ck(sum(old)/2==T+1 and sum(credit)/2==-1);ck(all(old[i]+credit[i]==debit[i] for i in range(2)))
   n+=1
 ck(n==405)
 # Hypothesis-breaking controls from rational account definitions.
 for V,W,T in [([F(1),F(0)],[F(-1),F(1)],F(1,2)),([F(-1),F(1)],[F(1),F(0)],F(0))]:
  S=[V[i]+W[i] for i in range(2)];d=[F(0),2*T]
  ck(all(0<=d[i]<=S[i] for i in range(2)))
  ck(sum(max(d[i]-V[i],F(0)) for i in range(2))/2!=max(F(0),T-sum(V)/2))
 return dict(cases=n,feasible_integer_vertices=vertices,hypothesis_controls=2)
def setup():
 ts=(c.G,)*6;root=c.packet(ts)
 t1,ch1,r1=split(root,ts,0,2)
 t2,ch2,r2=split(ch1[0],t1[0],0,0)
 U=[components(z,0)[0] for z in ch2];B=avg(U)
 old={'root_e1':c.scale(r1['e4'],2),'second_e2':r2['e4']}
 labels=[{k:c.mul(v,c.div(u,B)) for k,v in old.items()} for u in U]
 # Surviving original bits are1,3,4,5; index1 is ORIGINAL coordinate3.
 t3,ch3,r3=split(ch2[0],t2[0],0,1)
 U3=[components(z,0)[0] for z in ch3];M=[c.sub(z['S'],u) for z,u in zip(ch3,U3)]
 ck(M[0][1]<0 and M[1][0]>0);ck(U3[1]==c.point(0))
 T=c.add(*labels[0].values(),r3['e4']);c.pos(T)
 tau=c.sub(T,c.scale(ch3[0]['S'],F(1,2)));c.pos(tau)
 debits=[ch3[0]['S'],c.scale(tau,2)];c.pos(c.sub(ch3[1]['S'],debits[1]))
 incoming=dict(labels[0]);incoming['third_e3']=r3['e4']
 labels3=[{k:c.mul(v,c.div(d,T)) for k,v in incoming.items()} for d in debits]
 for d,l in zip(debits,labels3):overlap(c.add(*l.values()),d)
 stopped=[dict(P=ch1[1],reach=F(1,2),labels={}),dict(P=ch2[1],reach=F(1,4),labels=labels[1])]
 return root,t3,ch3,debits,labels3,stopped,tau
def main():
 pilot='--pilot' in sys.argv
 journal=R/'out'/('PILOT_JOURNAL.jsonl' if pilot else 'CASE_JOURNAL_V2.jsonl')
 if journal.exists():raise RuntimeError('Existing case journal must be reconciled, not replayed: '+str(journal))
 grid=allocation_grid();save('ALLOCATION_GRID.json',grid)
 root,tables,parents,D,labels,stopped,tau=setup()
 choices=list(itertools.product(range(2),range(1,6),range(6)))
 if pilot:choices=choices[:2]
 records=[];fail={0:0,1:0};sources=Path(r'agents\A072\runs\20261021T225156Z-account03-A072-exact-walsh-engine\out')
 source=json.loads((sources/'COMPONENT_CASES.json').read_text(encoding='utf-8'));source={(x['terminal'],x['block'],x['coordinate']):x for x in source};Q=1<<192
 def compare(ours,encoded):overlap(ours,tuple(F(int(x),Q) for x in encoded))
 for b,j,i in choices:
  P=parents[b];ts,children,row=split(P,tables[b],j,i)
  pf=form(P,j);cf=[form(z,j) for z in children]
  ep=ps(ps(pf['H'],meanp([z['H'] for z in cf])),const(4*row['d']))
  ck(meanp([z['S'] for z in cf])==pa(pf['S'],ep))
  ck(meanp([z['A'] for z in cf])==pf['A'])
  ck(ps(ep,ps(meanp([z['U'] for z in cf]),pf['U']))==ps(pf['C'],meanp([z['C'] for z in cf])))
  banks=[components(z,j) for z in children];vs=[z[2] for z in banks];ws=[z[3] for z in banks]
  T=c.add(D[b],row['e4']);c.pos(T);B=avg([z['S'] for z in children]);av=avg(vs);aw=avg(ws)
  sf=c.sub(T,av);ck(sf[0]>0 or sf[1]<0)
  if sf[0]>0:fail[b]+=1
  if b==0:
   # Primitive incoming D is EXACTLY S_parent; use this equality, not overlap.
   allocation=[z['S'] for z in children];donors=ws;kind='forced full saturation'
   ck(aw[0]>0);overlap(sf,aw)
  elif sf[0]>0:
   theta=c.div(sf,aw);ck(0<theta[0]<=theta[1]<1)
   donors=[c.mul(theta,w) for w in ws];allocation=[c.add(v,d) for v,d in zip(vs,donors)];kind='selected plus required donor'
  else:
   theta=c.div(T,av);ck(0<theta[0]<=theta[1]<1)
   allocation=[c.mul(theta,v) for v in vs];donors=[c.point(0)]*2;kind='selected only'
  overlap(avg(allocation),T)
  overlap(avg(donors),aw if b==0 else sf if sf[0]>0 else c.point(0))
  outgoing=[]
  for z,a in zip(children,allocation):
   ls={k:c.mul(v,c.div(a,T)) for k,v in labels[b].items()};ls['next_e']=c.mul(row['e4'],c.div(a,T))
   overlap(c.add(*ls.values()),a);outgoing.append(ls)
   if b==1:c.pos(c.sub(z['S'],a))
  for name,val in dict(labels[b],next_e=row['e4']).items():overlap(avg([l[name] for l in outgoing]),val)
  # All five terminal functions and their old signed labels survive.
  leaves=stopped+[dict(P=parents[1-b],reach=F(1,8),labels=labels[1-b])]+[dict(P=z,reach=F(1,16),labels=l) for z,l in zip(children,outgoing)]
  ck(sum(z['reach'] for z in leaves)==1)
  mean_remaining=c.add(*(c.scale(c.sub(z['P']['S'],c.add(*z['labels'].values())),z['reach']) for z in leaves))
  overlap(mean_remaining,root['S'])
  original=source[b,j,i];compare(row['e4'],original['query_excess']);compare(D[b],original['incoming_debit']);compare(sf,original['selected_shortfall'])
  for k in range(2):
   for ours,key in [(vs[k],'child_V'),(ws[k],'child_W'),(children[k]['S'],'child_full_S'),(allocation[k],'optimal_child_debits'),(donors[k],'optimal_child_donors')]:compare(ours,original[key][k])
  rec=dict(terminal=b,block=j,coordinate=i,physical_influence=row['d'],incoming=D[b],T=T,e=row['e4'],child_S=[z['S'] for z in children],V=vs,W=ws,shortfall=sf,allocation=allocation,donors=donors,rule=kind,old_labels=labels[b],child_labels=outgoing,root_mean_remaining=mean_remaining,root_remaining=root['S'],exact_profile_digest=digestp(ep),saturated_unused_W_exactly_zero=(b==0),terminal_reaches=[z['reach'] for z in leaves],full_terminal_H=[z['P']['H'] for z in leaves],full_terminal_I=[z['P']['I'] for z in leaves])
  records.append(rec)
  with journal.open('a',encoding='utf-8',newline='\n') as output:output.write(json.dumps(rec,default=str)+'\n')
  ck(time.perf_counter()-START<55)
 if not pilot:ck(len(records)==60);ck(fail=={0:30,1:6})
 # Direct small/boundary coefficient evidence was already closed at stage6;
 # do not rerun that census. This stage's seven unique core tables are directly
 # reconstructed by the reused independent character implementation.
 result=dict(passed=True,cases=len(records),allocation_grid=grid,checks=COUNT,helper_checks=c.COUNT,selected_only_failures=fail,runtime_seconds=time.perf_counter()-START,core_tables=c.core.cache_info().currsize,root_surplus=root['S'],prefix_tau=tau,source_interval_scale_bits=192,our_log_fractional_bits=112,peer_code_imports=False,universal_fei='OPEN',rung='independently reconstructed exact finite certificate plus algebraic conditional theorem')
 save('PILOT_CASES.json' if pilot else 'CASES.json',records)
 save('PILOT.json' if pilot else 'VALIDATION.json',result);print(json.dumps(result,default=str))
if __name__=='__main__':main()
