from pathlib import Path
from fractions import Fraction as Q
import time,json,sys
import exact as E
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv;start=time.perf_counter();nodes=fronts=trees=0
c=Q(1,16);m=4;a=(1+c)/2;bent=tuple((-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1))) for x in range(16))
def state(labels,cores,phase):
 nc=len(labels).bit_length()-1;ns=[len(h).bit_length()-1 for h in cores];g=[]
 for x in range(1<<sum(ns)):
  vals=[];off=0
  for h,n in zip(cores,ns):vals.append(h[(x>>off)&((1<<n)-1)]);off+=n
  g.extend(1 if j==2 else vals[j] for j in labels)
 ga=E.walsh(tuple(g));full=[]
 for v in g:
  for x in range(16):
   rare=bent[x]-int(x==0)+int(x==0)*v
   full.extend([v,rare] if phase==-1 else [v if phase==0 else rare])
 wa=E.walsh(tuple(full));density=a if phase==-1 else Q(1) if phase==0 else c
 U={};RR={}
 for j,h in enumerate(cores):
  p=density*Q(labels.count(j),len(labels));mu=Q(sum(h),len(h));hh=E.entropy(E.walsh(h))
  U=E.add(U,E.add(hh,E.cost(mu*mu),-1),p);RR=E.add(RR,E.cost(p),1-mu*mu)
 Qval=density*(21*sum(E.influence(ga,i) for i in range(nc))+5*sum(E.influence(ga,i) for i in range(nc,len(g).bit_length()-1)))
 Sval=6*E.influence(wa,0) if phase==-1 else c*m*(1-ga[0]**2) if phase==1 else Q(0)
 P=E.add(E.add(U,RR),{2:Qval+Sval})
 return wa,E.entropy(wa),P,nc,ns
roots=[[(1,-1),(-1,1)],[(-1,-1,-1,1),(1,-1)]]
for cores in (roots[:1] if pilot else roots):
 for pol in ([0] if pilot else [0,1,2]):
  trees+=1;root=state((0,1,0,2),cores,-1);mx=3+sum(root[4]);agg=[{'H':{},'P':{},'weight':Q(0)} for _ in range(mx+1)]
  def visit(labels,cs,phase,depth,w):
   global nodes
   nodes+=1;s=state(labels,cs,phase);wa,H,P,nc,ns=s
   avail=[('ctrl',j) for j in range(nc)]+[(k,j) for k,n in enumerate(ns) for j in range(n)]
   if phase==-1:avail.append(('X',0))
   terminal=not avail
   for d in (range(depth,mx+1) if terminal else [depth]):
    agg[d]['H']=E.add(agg[d]['H'],H,w);agg[d]['P']=E.add(agg[d]['P'],P,w);agg[d]['weight']+=w
   if terminal:return
   if phase==-1 and (pol==0 or (pol==1 and depth>=1) or (pol==2 and (depth>=3 or (depth>=1 and wa[0]>0)))):choice=('X',0)
   else:choice=next((x for x in avail if isinstance(x[0],int)),avail[0]) if pol==1 else next((x for x in reversed(avail) if x[0]!='X'),avail[0])
   group,j=choice;children=[]
   for v in [0,1]:
    nl=labels;cc=list(cs);ph=phase
    if group=='X':ph=v
    elif group=='ctrl':nl=E.slice_table(labels,j,v)
    else:cc[group]=E.slice_table(cs[group],j,v)
    children.append((nl,cc,ph,state(nl,cc,ph)))
   DH=E.add(H,E.add(children[0][3][1],children[1][3][1]),-Q(1,2));DP=E.add(P,E.add(children[0][3][2],children[1][3][2]),-Q(1,2))
   E.le(DH,DP,'SAME U/R/Q/source-variance local payment')
   if group=='X':E.ok(phase==-1,'source at most once')
   for nl,cc,ph,_ in children:visit(nl,cc,ph,depth+1,w/2)
  visit((0,1,0,2),cores,-1,0,Q(1))
  for z in agg:
   fronts+=1;E.ok(z['weight']==1,'both terminals')
   E.le(E.add(root[1],z['H'],-1),E.add(root[2],z['P'],-1),'original-root potential no renewal')
  E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()
  if time.perf_counter()-start>(55 if pilot else 115):raise RuntimeError('frozen cap')
out=dict(status='PASS',trees=trees,nodes=nodes,frontiers=fronts,assertions=E.checks,seconds=time.perf_counter()-start,pilot=pilot)
(R/'out'/('history_pilot.json' if pilot else 'history_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
