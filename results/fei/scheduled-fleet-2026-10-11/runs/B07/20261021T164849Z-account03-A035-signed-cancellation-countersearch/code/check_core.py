from pathlib import Path
from fractions import Fraction as Q
from collections import Counter, defaultdict
import itertools,json,time,sys
import kernel as k
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); k.CAP=180; checks=0
def check(x):
 global checks
 assert x
 checks+=1
def build(m,L,point,fixed):
 labels=[('y',j) for j in range(m)]
 for j in range(L): labels.extend([('x',j,h) for h in range(4)]+([] if j in fixed else [('z',j)]))
 vals=[]
 for a in range(1<<len(labels)):
  y=a&((1<<m)-1);p=(y.bit_count()%2)^(y==point);v=k.bent(y,m);off=m
  for j in range(L):
   x=(a>>off)&15;off+=4;z=fixed[j] if j in fixed else (a>>off)&1
   if j not in fixed:off+=1
   v*=k.bent(x,4)*(-1 if p and x==0 and z else 1)
  vals.append(v)
 return vals,labels
def core(m,point,bit,value):
 b=[k.bent(y,m) for y in range(1<<m)]
 c=[b[y] if ((y.bit_count()%2)^(y==point)) else 0 for y in range(1<<m)]
 b=k.restrict(b,bit,value);c=k.restrict(c,bit,value)
 N=len(b)
 return [Q(a,N) for a in k.fwht(b)],[Q(a,N) for a in k.fwht(c)]
def rows(t,i):
 a=k.fwht(t);N=len(t)
 return [(s,Q(a[s],N),Q(a[s^(1<<i)],N)) for s in range(N) if not s&(1<<i)]
def KLhist(hist,scale,d):
 out=(Q(0),Q(0))
 if not d:return out
 for (b,r),count in hist.items():
  if b:out=k.add(out,k.mul(k.ratlog(Q(b,r)/d),count*b/scale/d))
 return out
def lam(hist,scale):
 out=(Q(0),Q(0))
 for (b,r),count in hist.items():
  if b:out=k.add(out,k.mul(k.ratlog(Q(r,b)),count*b/scale))
 return out
def transport(t,i,j):
 a=k.fwht(t);N=len(t);n2=N*N
 hist=Counter((a[s^(1<<i)]**2,a[s]**2+a[s^(1<<i)]**2) for s in range(N) if not s&(1<<i))
 d=Q(sum(b*c for (b,r),c in hist.items()),n2)
 collapsed=Counter();joint=Counter()
 for s in range(N):
  if s&((1<<i)|(1<<j)):continue
  a0,b0,a1,b1=(a[s],a[s^(1<<i)],a[s^(1<<j)],a[s^(1<<i)^(1<<j)])
  collapsed[(b0*b0+b1*b1,a0*a0+b0*b0+a1*a1+b1*b1)]+=1
  for sign in (1,-1):joint[((b0+sign*b1)**2,(a0+sign*a1)**2+(b0+sign*b1)**2)]+=1
 D=KLhist(hist,Q(n2),d);Db=KLhist(collapsed,Q(n2),d);Dj=KLhist(joint,Q(2*n2),d)
 delta=k.sub(D,Db);K=k.sub(Dj,Db);drift=k.sub(k.mul(lam(joint,Q(n2)),Q(1,2)),lam(hist,Q(n2)))
 check(delta[1]>=0 and K[1]>=0)
 pred=k.mul(k.sub(delta,K),d)
 check(drift[0]<=pred[1] and pred[0]<=drift[1])
 check(sum(Q(r*c,2*n2) for (b,r),c in joint.items())==1)
 kids=[k.restrict(t,j,s) for s in (0,1)]
 check(k.influence(t)==Q(sum(t[x]!=t[x^(1<<j)] for x in range(N)),N)+sum((k.influence(c) for c in kids),Q())/2)
 return dict(d=str(d),delta=k.emit(delta),K=k.emit(K),drift=k.emit(drift)),drift
def trace(s,labels,m,point,fixed,emod,pvalue,cbit,cvalue,query,B,C):
 freq={lab:(s>>i)&1 for i,lab in enumerate(labels)}
 y=sum(freq[('y',h)]<<i for i,h in enumerate(h for h in range(m) if h!=cbit))
 eps={};support={};zs={}
 for j in range(max(lab[1] for lab in labels if lab[0]=='x')+1):
  if j==emod:
   support[j]=freq[('x',j,1)]==pvalue
   eps[j]=-1 if freq[('x',j,2)] and freq[('x',j,3)] else 1
  else:
   support[j]=True;eps[j]=k.bent(sum(freq[('x',j,h)]<<h for h in range(4)),4)
  if j not in fixed:zs[j]=freq[('z',j)]
 if pvalue==1 and query==emod:return ('inactive',)
 if pvalue==0 and query==emod and not support[query]:return ('query_off',)
 others=[j for j in support if j!=query and not(pvalue==1 and j==emod)]
 if any(not support[j] or zs.get(j,0) for j in others):return ('other_off',eps[query])
 A=sum(eps[j]==1 for j in others if j not in fixed);F=sum(j not in fixed for j in others)
 E=sum(eps[j]==1 for j in others if fixed.get(j)==1);J=sum(fixed.get(j)==1 for j in others)
 w=Q(3,4)**A*Q(5,4)**(F-A)*Q(1,2)**E*Q(3,2)**(J-E)
 # Homogeneous core pair avoids division by a vanishing carrier.
 if B[y]==0:return ('zero_core',eps[query],str(w))
 return ('carrier',str(C[y]/B[y]),eps[query],str(w))
pilot='--pilot' in sys.argv
roots=[(2,1,0),(4,1,1)] if pilot else list(itertools.product((2,4),(1,2),(0,1)))
records=[]; witness=None; parents=0
for m,L,point in roots:
 for emod,query in itertools.product(range(L),repeat=2):
  for status in ([None] if L==1 or pilot else [None,0,1]):
   fixed={} if status is None else {1-query:status}
   root,labs=build(m,L,point,fixed);pi=Q(1,2)+(-1 if point.bit_count()%2 else 1)*Q(1,1<<m)
   i=labs.index(('z',query));j=labs.index(('x',emod,0));first,drift1=transport(root,i,j)
   secondavg=(Q(),Q());parents+=1
   for pv in (0,1):
    par=k.restrict(root,j,pv);pl=labs[:j]+labs[j+1:];ii=pl.index(('z',query))
    # Both core coordinates in one quadratic pair; remaining pairs are symmetric.
    for cb in ([0] if pilot else [0,1]):
     jj=pl.index(('y',cb));trans,drift2=transport(par,ii,jj)
     if cb==0:secondavg=k.add(secondavg,k.mul(drift2,Q(1,2)))
     for cv in (0,1):
      child=k.restrict(par,jj,cv);cl=pl[:jj]+pl[jj+1:];ci=cl.index(('z',query));B,C=core(m,point,cb,cv)
      rr=rows(child,ci);d=sum((v*v for s,u,v in rr),Q());groups=defaultdict(lambda:[Q(),Q()]);ratios={};offmu=Q();offr=Q()
      active=cv==((point>>cb)&1)
      offnorm=sum((c*c for b,c in zip(B,C) if not b),Q())
      check(offnorm==(Q(1,4)-Q(1,1<<m) if active else Q(1,4)))
      for s,u,v in rr:
       lab=trace(s,cl,m,point,fixed,emod,pv,cb,cv,query,B,C)
       mu=v*v/d if d else Q();r=u*u+v*v;groups[lab][0]+=mu;groups[lab][1]+=r
       if r:
        ratio=mu/r
        if lab in ratios:check(ratios[lab]==ratio)
        ratios[lab]=ratio
       freq={lab:(s>>h)&1 for h,lab in enumerate(cl)}
       y=sum(freq[('y',h)]<<a for a,h in enumerate(h for h in range(m) if h!=cb))
       if B[y]==0:
        offmu+=mu;offr+=r
        if v and witness is None:
         witness=dict(m=m,L=L,point=point,emod=emod,query=query,status=status,private_value=pv,core_bit=cb,core_value=cv,frequency=s,alpha=str(u),beta=str(v),core_carrier=str(B[y]),core_minus=str(C[y]),mu=str(mu),reference=str(r),likelihood=str(mu/r),trace=list(lab))
      check(sum(r for u,r in groups.values())==1)
      check(sum(u for u,r in groups.values())==(1 if d else 0))
      # Reference-only labels with zero derivative must still be retained.
      check(len(groups)<=3+12*L*L)
      Hp=k.entropy_table(par);Hc=k.entropy_table(child)
      rec=dict(m=m,L=L,point=point,emod=emod,query=query,status=status,private_value=pv,core_bit=cb,core_value=cv,d=str(d),zero_core_mu=str(offmu),zero_core_reference=str(offr),zero_core_cminus_norm=str(offnorm),trace_states=len(groups),transport=trans,terminal_H=k.emit(Hc),terminal_I=str(k.influence(child)))
      records.append(rec)
      with (ROOT/'out'/('pilot_cases.jsonl' if pilot else 'cases.jsonl')).open('a',encoding='utf-8') as f:f.write(json.dumps(rec)+'\n')
   check(time.perf_counter()-START<180)
out=dict(helper='A035-shared-core-v1',pilot=pilot,roots=len(roots),private_query_parents=parents,descendants=len(records),checks=checks,runtime_seconds=time.perf_counter()-START,witness=witness,zero_core_positive_descendants=sum(Q(r['zero_core_mu'])>0 for r in records))
(ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
