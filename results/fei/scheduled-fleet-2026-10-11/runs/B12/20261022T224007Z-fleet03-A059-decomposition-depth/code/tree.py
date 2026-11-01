from pathlib import Path
from fractions import Fraction as Q
import time,json,sys
import exact as E
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
nodes=0;fronts=0;trees=0
def st(labels,cores):
 nc=len(labels).bit_length()-1;ns=[len(h).bit_length()-1 for h in cores];tt=[]
 for x in range(1<<sum(ns)):
  vals=[];off=0
  for h,n in zip(cores,ns):vals.append(h[(x>>off)&((1<<n)-1)]);off+=n
  for lab in labels:tt.append(1 if lab==4 else vals[lab])
 a=E.walsh(tuple(tt));H=E.entropy(a);U={};RR={}
 for j,h in enumerate(cores):
  p=Q(labels.count(j),len(labels));m=Q(sum(h),len(h))
  U=E.add(U,E.add(E.entropy(E.walsh(h)),E.cost(m*m),-1),p)
  RR=E.add(RR,E.cost(p),1-m*m)
 return a,H,U,RR,nc,ns
labels=[]
for x in range(32):
 y,a,b,t0,t1=[(x>>i)&1 for i in range(5)]
 labels.append(0 if y and a else 1 if y and b else 2 if t0 else 3 if t1 else 4)
roots=[[(1,-1),(-1,1),(1,-1),(-1,1)],[(1,-1),(-1,1),(-1,-1,-1,1),(-1,1)]]
for cores in (roots[:1] if pilot else roots):
 for policy in ([0] if pilot else [0,1,2]):
  trees+=1;root=st(tuple(labels),cores);depthmax=4+sum(root[5]);ag=[dict(H={},U={},R={},B={},I=Q(0),P=Q(0)) for _ in range(depthmax+1)]
  E.le(root[3],{2:2*sum(E.influence(root[0],i) for i in range(5))},'once-funded root R')
  ctrl_ids=(0,1,2,3,4);data_ids=tuple(tuple(range(n)) for n in root[5])
  def visit(labs,cs,ci,di,depth,weight,bill,spent):
   global nodes
   nodes+=1;s=st(labs,cs);a,H,U,RR,nc,ns=s
   if time.perf_counter()-start>(55 if pilot else 175):raise RuntimeError('frozen cap')
   available=[(0,j,idx) for idx,j in enumerate(ci) if j!=0]
   available +=[(k+1,j,nc+sum(ns[:k])+idx) for k,ids in enumerate(di) for idx,j in enumerate(ids)]
   terminal=not available or (policy==2 and depth>=3 and abs(a[0])==1)
   for t in ([depth] if not terminal else range(depth,depthmax+1)):
    z=ag[t]
    for k,value in [('H',H),('U',U),('R',RR),('B',bill)]:z[k]=E.add(z[k],value,weight)
    z['I']+=weight*E.influence(a);z['P']+=weight*spent
   if terminal:return
   if policy==0:chosen=min(available,key=lambda v:(0 if v[0]==0 and v[1]>=3 else 1 if v[0]>0 else 2,-v[1]))
   elif policy==1:chosen=min(available,key=lambda v:(0 if v[0]==3 else 1 if v[0]==0 and v[1]==2 else 2 if v[0]==0 else 3,v[1]))
   else:chosen=max(available,key=lambda v:(E.influence(a,v[2]),v[0] if a[0]<0 else -v[0]))
   group,identifier,physical=chosen;children=[]
   for val in [0,1]:
    ncs=list(cs);nci=ci;ndi=list(di);nl=labs
    if group==0:
     idx=ci.index(identifier);nl=E.slice_table(labs,idx,val);nci=ci[:idx]+ci[idx+1:]
    else:
     k=group-1;idx=di[k].index(identifier);ncs[k]=E.slice_table(cs[k],idx,val);ndi[k]=di[k][:idx]+di[k][idx+1:]
    children.append((nl,ncs,nci,tuple(ndi),st(nl,ncs)))
   DH=E.add(H,E.add(children[0][4][1],children[1][4][1]),-Q(1,2))
   DU=E.add(U,E.add(children[0][4][2],children[1][4][2]),-Q(1,2))
   DR=E.add(RR,E.add(children[0][4][3],children[1][4][3]),-Q(1,2))
   d=E.influence(a,physical);res=E.add(E.add(DH,DU,-1),DR,-1)
   E.ok(E.influence(a)==d+(E.influence(children[0][4][0])+E.influence(children[1][4][0]))/2)
   if group==0:
    E.ok(DU=={});E.le({},DR);price={2:21*d};E.le(res,price,'controller SAME reserve')
   else:price=None;E.leconst(res,3*d,'signed fine DATA residual')
   newbill=E.add(bill,price) if price is not None else E.add(bill,{})
   # DATA charge3d nats is accumulated through a separate rational marker key -1.
   if price is None:newbill[-1]=newbill.get(-1,Q(0))+3*d
   for nl,ncs,nci,ndi,child in children:visit(nl,ncs,nci,ndi,depth+1,weight/2,newbill,spent+d)
  visit(tuple(labels),cores,ctrl_ids,data_ids,0,Q(1),{},Q(0))
  for z in ag:
   fronts+=1
   E.ok(E.influence(root[0])==z['P']+z['I'],'same-tree influence identity')
   # Exact actual terminal profile with one initial bank, no replenishment.
   residual=E.add(E.add(E.add(E.add(root[1],root[2],-1),root[3],-1),z['H'],-1),E.add(z['U'],z['R']))
   bill=dict(z['B']);rational=bill.pop(-1,Q(0));E.leconst(E.add(residual,bill,-1),rational,'stopping full terminals')
  E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()
out=dict(status='PASS',trees=trees,visited_nodes=nodes,frontiers=fronts,assertions=E.checks,seconds=time.perf_counter()-start,pilot=pilot)
(R/'out'/('tree_pilot.json' if pilot else 'tree_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
