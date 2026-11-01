from pathlib import Path
from fractions import Fraction as Q
from collections import Counter,defaultdict
import json,time,itertools,sys
import kernel as k
ROOT=Path(__file__).resolve().parents[1];PILOT='--pilot' in sys.argv;k.CAP=50 if PILOT else 180;start=time.perf_counter();checks=0
def build(m,L,point,fixed):
 labels=[('y',j) for j in range(m)]
 for j in range(L):labels.extend([('x',j,h) for h in range(4)]+([] if j in fixed else [('z',j)]))
 vals=[]
 for a in range(1<<len(labels)):
  y=a&((1<<m)-1);p=(y.bit_count()%2)^(y==point);v=k.bent(y,m);off=m
  for j in range(L):
   x=(a>>off)&15;off+=4;z=fixed[j] if j in fixed else (a>>off)&1
   if j not in fixed:off+=1
   v*=k.bent(x,4)*(-1 if p and x==0 and z else 1)
  vals.append(v)
 return vals,labels
def KL(hist,N2,d,mu_factor=1):
 out=(Q(0),Q(0))
 for (b,r),count in hist.items():
  if b:out=k.add(out,k.mul(k.ratlog(Q(b,r)/d),Q(count*b,N2)/d*mu_factor))
 return out
def Lambda(hist,N2):
 out=(Q(0),Q(0))
 for (b,r),count in hist.items():
  if b:out=k.add(out,k.mul(k.ratlog(Q(r,b)),Q(count*b,N2)))
 return out
def core_l(m,point):
 carrier=[k.bent(y,m) for y in range(1<<m)];cm=[carrier[y] if (y.bit_count()%2)^(y==point) else 0 for y in range(1<<m)]
 return [Q(a,b) for a,b in zip(k.fwht(cm),k.fwht(carrier))]
def child_trace(s,m,L,point,fixed,emod,bit,value,query,labels,lrows):
 freq={lab:(s>>i)&1 for i,lab in enumerate(labels)}
 y=sum(freq[('y',h)]<<h for h in range(m));xs={};support={};eps={};zs={}
 for j in range(L):
  if j==emod:
   # The restricted quadratic pair leaves a mate frequency and one intact pair.
   mate=bit^1;support[j]=freq[('x',j,mate)]==value
   intact=[h for h in range(4) if h//2!=bit//2]
   eps[j]=-1 if all(freq[('x',j,h)] for h in intact) else 1
  else:
   xs[j]=sum(freq[('x',j,h)]<<h for h in range(4));support[j]=True;eps[j]=k.bent(xs[j],4)
  if j not in fixed:zs[j]=freq[('z',j)]
 if value==1 and query==emod:return ('inactive',)
 if value==0 and query==emod and not support[query]:return ('query_off_carrier',)
 others=[j for j in range(L) if j!=query and not (value==1 and j==emod)]
 O=any(not support[j] or zs.get(j,0) for j in others)
 if O:return ('other_off',eps[query])
 A=sum(eps[j]==1 for j in others if j not in fixed)
 B=sum(eps[j]==1 for j in others if fixed.get(j)==1)
 return ('coherent',str(lrows[y]),eps[query],A,B)
roots=[(2,2,1)] if PILOT else list(itertools.product((2,4),(1,2),(0,1)))
Hp4=k.entropy_table([k.bent(x,4)*(-1 if x==0 else 1) for x in range(16)])
Hp3=k.entropy_table([k.bent(x>>1,2)*(-1 if x==0 else 1) for x in range(8)])
records=[]
for m,L,point in roots:
 pi=Q(1,2)+(-1 if point.bit_count()%2 else 1)*Q(1,1<<m);lr=core_l(m,point)
 exposed=[0] if PILOT else range(L);bits=[0] if PILOT else range(4)
 for emod,bit,query in itertools.product(exposed,bits,range(L)):
  statuses=[None] if PILOT or L==1 else [None,0,1]
  for status in statuses:
   k.clock();fixed={} if status is None else {1-query:status};parent,labels=build(m,L,point,fixed);N=len(parent);N2=N*N
   i=labels.index(('z',query));j=labels.index(('x',emod,bit));ft=k.fwht(parent)
   parenthist=Counter((ft[s^(1<<i)]**2,ft[s]**2+ft[s^(1<<i)]**2) for s in range(N) if not s&(1<<i))
   d=Q(sum(b*c for (b,r),c in parenthist.items()),N2);assert d==pi/16;checks+=1
   collapsed=Counter();joint=Counter();children=[]
   for s in range(N):
    if s&((1<<i)|(1<<j)):continue
    a,b=ft[s],ft[s^(1<<i)];c,e=ft[s^(1<<j)],ft[s^(1<<i)^(1<<j)]
    collapsed[(b*b+e*e,a*a+b*b+c*c+e*e)]+=1
    for sign in (1,-1):joint[((b+sign*e)**2,(a+sign*c)**2+(b+sign*e)**2)]+=1
   D=KL(parenthist,N2,d);Db=KL(collapsed,N2,d);Dj=KL(joint,N2,d,Q(1,2));lost=k.sub(D,Db);physical=k.sub(Dj,Db)
   assert lost[1]>=0 and physical[1]>=0;checks+=2
   price=Lambda(parenthist,N2);avg=k.mul(Lambda(joint,N2),Q(1,2));drift=k.sub(avg,price);pred=k.mul(k.sub(lost,physical),d)
   assert drift[0]<=pred[1] and drift[1]>=pred[0];checks+=1
   Ic=[];Hc=[];terminal=[]
   for value in (0,1):
    child=k.restrict(parent,j,value);childlabels=labels[:j]+labels[j+1:];ic=childlabels.index(('z',query));n=len(child);a=k.fwht(child)
    dc=Q(sum(v*v for s,v in enumerate(a) if s&(1<<ic)),n*n)
    expected=(pi/8 if value==0 else Q(0)) if query==emod else pi/16
    assert dc==expected;checks+=1
    hist=Counter((a[s^(1<<ic)]**2,a[s]**2+a[s^(1<<ic)]**2) for s in range(n) if not s&(1<<ic))
    groups=defaultdict(lambda:[Q(0),Q(0)]);ratios={};row_witness=[]
    for s in range(n):
     if s&(1<<ic):continue
     b2=a[s^(1<<ic)]**2;r=a[s]**2+b2;lab=child_trace(s,m,L,point,fixed,emod,bit,value,query,childlabels,lr)
     mu=Q(b2,n*n)/dc if dc else Q(0);rr=Q(r,n*n)
     groups[lab][0]+=mu;groups[lab][1]+=rr
     if mu:
      ratio=mu/rr
      if lab in ratios:assert ratios[lab]==ratio
      ratios[lab]=ratio;checks+=1
    assert sum(r for u,r in groups.values())==1;checks+=1
    if dc:assert sum(u for u,r in groups.values())==1;checks+=1
    else:assert sum(u for u,r in groups.values())==0;checks+=1
    if value==0 and query==emod:
     off=groups[('query_off_carrier',)];assert off==[Q(1,2),pi/8];checks+=1
     assert ratios[('query_off_carrier',)]==1/(2*dc);checks+=1
    Ic.append(k.influence(child));Hc.append(k.entropy_table(child))
    TI=Q(0);TH=(Q(0),Q(0))
    for h in range(L):
     zprob=Q(fixed[h]) if h in fixed else Q(1,2)
     if h==emod:
      TI+=Q(2) if value else Q(1)+Q(3,4)*pi*zprob
      TH=k.add(TH,(Q(2),Q(2)) if value else k.add((Q(2),Q(2)),k.mul(k.sub(Hp3,(Q(2),Q(2))),pi*zprob)))
     else:
      TI+=Q(2)+pi*zprob/2;TH=k.add(TH,k.add((Q(4),Q(4)),k.mul(k.sub(Hp4,(Q(4),Q(4))),pi*zprob)))
    assert TH[1]<=2*TI;checks+=1
    terminal.append(dict(I=str(TI),H=k.emit(TH)))
    children.append(dict(value=value,physical_reach='1/2',d=str(dc),trace_states=len(groups),full_reference_mass='1',derivative_mass='1' if dc else '0',Lambda=k.emit(Lambda(hist,n*n)),trace={str(lab):dict(mu=str(u),r=str(r),likelihood=str(ratios[lab]) if lab in ratios else None) for lab,(u,r) in groups.items()}))
   Ip=k.influence(parent);dk=Q(sum(parent[x]!=parent[x^(1<<j)] for x in range(N)),N)
   assert Ip==dk+(Ic[0]+Ic[1])/2;checks+=1
   rec=dict(m=m,L=L,point=point,exposed_module=emod,private_bit=bit,queried_selector=query,other_selector_status=status,source_reach='1' if status is None else '1/2',parent_d=str(d),query_influence=str(dk),parent_I=str(Ip),child_I=[str(c) for c in Ic],parent_H=k.emit(k.entropy_table(parent)),child_H=[k.emit(c) for c in Hc],parent_Lambda=k.emit(price),mean_child_Lambda=k.emit(avg),Lambda_drift=k.emit(drift),parent_collapse_KL=k.emit(lost),physical_child_KL=k.emit(physical),incoming_reference_mass='1',physical_joint_zero_derivative_branch_reference_mass='1/2' if query==emod else None,terminal=terminal,children=children)
   records.append(rec)
   with (ROOT/'out'/('pilot_cases.jsonl' if PILOT else 'cases.jsonl')).open('a',encoding='utf8') as fp:fp.write(json.dumps(rec)+'\n')
out=dict(helper_version='A035-private-query-reference-v1',runtime_seconds=time.perf_counter()-start,root_count=len(roots),parent_context_count=len(records),child_context_count=2*len(records),checks=checks,records=records)
(ROOT/'out'/('pilot.json' if PILOT else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({a:b for a,b in out.items() if a!='records'}))
print('pilot examples',[(r['queried_selector'],r['Lambda_drift'],r['parent_collapse_KL'],r['physical_child_KL']) for r in records[:4]])
