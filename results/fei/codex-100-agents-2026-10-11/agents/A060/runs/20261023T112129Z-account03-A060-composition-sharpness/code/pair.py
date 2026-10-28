from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import itertools,json,sys,time,hashlib
import exact as e
R=Path(__file__).resolve().parents[1];CHECKS=0
e.eta=lru_cache(None)(e.eta)
def ck(x):
 global CHECKS
 assert x
 CHECKS+=1
def overlap(a,b):ck(a[0]<=b[1] and b[0]<=a[1]);ck(max(a[1]-a[0],b[1]-b[0])<e.SCALE//10**25)
def restrict(v,i,s):return [v[x] for x in range(len(v)) if (x>>i)&1==s]
def inf(v,i):return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def D(v,i,tf=e.fwht):return e.add(e.H(v,tf),e.neg(e.times(e.add(*(e.H(restrict(v,i,s),tf) for s in (0,1))),Q(1,2))))
def rank(rows):
 basis={}
 for a in rows:
  while a:
   k=a.bit_length()-1
   if k in basis:a^=basis[k]
   else:basis[k]=a;break
 return len(basis)
def matrix(n,edges):
 a=[0]*n
 for i,j in edges:a[i]^=1<<j;a[j]^=1<<i
 return a
def principal(a,deleted):
 keep=((1<<len(a))-1)^sum(1<<j for j in deleted)
 return [row&keep for i,row in enumerate(a) if i not in deleted]
def truth(n,edges):return [(-1)**sum(((x>>i)&1)*((x>>j)&1) for i,j in edges) for x in range(1<<n)]
def intwalsh(v):
 a=list(v);h=1
 while h<len(a):
  for i in range(0,len(a),2*h):
   for j in range(i,i+h):u,w=a[j],a[j+h];a[j],a[j+h]=u+w,u-w
  h*=2
 return a
def flat(v,r,direct=False):
 coeff=e.direct(v) if direct else [Q(x,len(v)) for x in intwalsh(v)]
 ck(sum(x!=0 for x in coeff)==1<<r);ck(all(not x or x*x==Q(1,1<<r) for x in coeff));ck(sum(x*x for x in coeff)==1)
 return r
WITNESS=[(0,1),(2,3),(4,5),(3,4),(2,5),(0,2),(1,3)]
def graph_case(n,edges,direct=False):
 a=matrix(n,edges);r=rank(a);v=truth(n,edges);flat(v,r,direct)
 ck(v[0]==1 and all(v[1<<i]==1 for i in range(n)))
 drops=[]
 for i in range(0,n,2):
  ck(inf(v,i)+inf(v,i+1)==1)
  s=rank(principal(a,[i,i+1]));delta=r-s;ck(delta in (0,2,4));ck(delta<=4);drops.append(delta)
 return drops
def witness(direct=False):
 v=truth(6,WITNESS);tf=e.direct if direct else e.fwht;ck(rank(matrix(6,WITNESS))==6);ck(sum(v)==8)
 flat(v,6,direct);first=[];second=[]
 for s in (0,1):
  child=restrict(v,0,s);flat(child,4,direct);first.append(4)
  for t in (0,1):flat(restrict(child,0,t),2,direct);second.append(2)
  overlap(D(child,0,tf),e.times(e.ln(Q(2)),2))
 overlap(D(v,0,tf),e.times(e.ln(Q(2)),2))
 ck(inf(v,0)+inf(v,1)==1)
 return {'n':6,'edges':WITNESS,'mean':'1/8','root_H':6,'first_child_H':first,'second_child_H':second,'first_D':2,'second_D_each':2,'full_pair_D':4,'initial_owner_pair_influence':1,'necessary_incoming_rate':4,'necessary_open_child_capacity':2}
def graph_run(mode):
 t0=time.perf_counter();hist={};roots=0
 ns=(4,6) if mode=='pilot' else (6,) if mode=='main' else (4,)
 for n in ns:
  mandatory=[(i,i+1) for i in range(0,n,2)];optional=[p for p in itertools.combinations(range(n),2) if p not in mandatory]
  masks=range(1<<len(optional)) if n==4 or mode=='main' else []
  for mask in masks:
   edges=mandatory+[p for j,p in enumerate(optional) if mask>>j&1]
   for delta in graph_case(n,edges,mode=='reproduce'):hist[delta]=hist.get(delta,0)+1
   roots+=1
 w=witness(mode=='reproduce');roots+=mode!='main'
 elapsed=time.perf_counter()-t0;ck(elapsed<55)
 out={'status':'PASS','mode':mode,'checks':CHECKS,'roots':roots,'pair_drop_histogram':hist,'witness':w,'elapsed_s':elapsed,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/'out'/('CHECK_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps({k:v for k,v in out.items() if k!='witness'}))
def mixed():
 t0=time.perf_counter();m=6;g=[-1 if y==0 else 1 for y in range(8)];b=truth(6,WITNESS)
 rare=[g[y] if x==0 else b[x] for y in range(8) for x in range(64)]
 w=[g[y] for y in range(8) for x in range(64)]+rare
 dy=D(w,6);ck(dy[0]>0)
 left=restrict(w,6,0);right=restrict(w,6,1);dx=D(right,8)
 x0=restrict(right,8,0);x1=restrict(right,8,1);ck(all(v==1 for v in x0))
 overlap(e.H(x1),e.times(e.ln(Q(2)),6));ck(inf(x1,0)+inf(x1,1)==1)
 terminal=[]
 for s in (0,1):
  mid=restrict(x1,0,s);overlap(D(mid,0),e.times(e.ln(Q(2)),2))
  for t in (0,1):terminal.append(e.H(restrict(mid,0,t)))
 average_leaf=e.add(e.times(e.H(left),Q(1,2)),e.times(e.H(x0),Q(1,4)),e.times(e.add(*terminal),Q(1,16)))
 actual=e.add(e.H(w),e.neg(average_leaf));predicted=e.add(dy,e.times(dx,Q(1,2)),e.ln(Q(2)))
 overlap(actual,predicted)
 out={'status':'PASS','mode':'mixed','checks':CHECKS,'elapsed_s':time.perf_counter()-t0,'old_internal_D':e.serial(dy),'reached_source_D':e.serial(dx),'both_first_internal_children_H':[e.serial(e.H(left)),e.serial(e.H(right))],'pair_owner_incoming':4,'pair_owner_after_first_D2':2,'pair_owner_after_second_D2':0,'full_actual_leaf_average_H':e.serial(average_leaf),'full_history_D':e.serial(actual)}
 ck(out['elapsed_s']<55);out['checks']=CHECKS
 (R/'out/CHECK_mixed.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps({k:v for k,v in out.items() if k not in ['both_first_internal_children_H']}))
def failures():
 t0=time.perf_counter();rows=[]
 for m in (4,8,12):
  N=1<<m;c=Q(1,N);b=[(-1)**sum(((x>>(2*j))&3)==3 for j in range(m//2)) for x in range(N)];bm=b.copy();bm[-1]=-1
  v=[(-1)**(z.bit_count()) if x==N-1 else b[x] for z in range(4) for x in range(N)]
  ck(v[0]==1 and all(v[1<<i]==1 for i in range(m+2)));ck(inf(v,m)==c and inf(v,m+1)==c)
  total=e.add(e.H(v),e.neg(e.times(e.add(e.H(b),e.H(bm)),Q(1,2))))
  ck(e.bits(total)[0]>=c*(m-1));ck(e.bits(total)[0]>4*(2*c))
  rows.append({'m':m,'both_pair_coordinates_relevant':True,'pair_influence':str(2*c),'actual_full_pair_D_over_I_pair':e.serial(e.times(total,1/(2*c))),'both_terminal_H':[e.serial(e.H(b)),e.serial(e.H(bm))]})
 # Slice condition survives, but dropping unit normalization creates zero incoming quota.
 raw=[1,-1,-1,-1];v=[-1,-1,-1,-1];ck(raw[0]==1);ck(raw[0]*raw[1]*raw[2]*raw[3]==-1);ck(inf(v,0)+inf(v,1)==0);ck(D(v,0)==(0,0))
 # Padded four-bit history: q01+x0+x1+q23, g=-1, then exterior23=00.
 b=truth(4,[(0,1),(2,3)]);b=[val*(-1)**((x&1)+((x>>1)&1)) for x,val in enumerate(b)]
 f=b.copy();f[0]=-1;reached=restrict(restrict(f,3,0),2,0);ck(reached==v)
 elapsed=time.perf_counter()-t0;ck(elapsed<55)
 out={'status':'PASS','mode':'failures','checks':CHECKS,'elapsed_s':elapsed,'no_slice_floor':rows,'no_unit_normalization':{'actual_reached_function':v,'incoming_pair_influence':0,'incoming_literal_pair_quota':0,'prescribed_open_child_quota':2,'debit':0,'quota_drift':-2,'scope':'refutes the fixed2 conversion without origin-unit sign condition; not a universal entropy inequality'}}
 (R/'out/CHECK_failures.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps({'status':'PASS','checks':CHECKS,'elapsed_s':elapsed,'ratios':[(x['m'],x['actual_full_pair_D_over_I_pair']['display']) for x in rows]}))
if __name__=='__main__':
 mode=sys.argv[1]
 if mode in ('pilot','main','reproduce'):graph_run(mode)
 elif mode=='mixed':mixed()
 elif mode=='failures':failures()
 else:raise ValueError(mode)
