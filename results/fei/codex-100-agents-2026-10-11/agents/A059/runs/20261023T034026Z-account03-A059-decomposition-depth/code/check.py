from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time,sys,shutil,hashlib
R=Path(__file__).resolve().parents[1]
old=R.parents[1]/'runs'/'20261014T060348Z-account05-A059-decomposition-depth'/'code'/'exact.py'
target=Path(__file__).with_name('exact.py')
if not target.exists():shutil.copyfile(old,target)
import exact as E
start=time.perf_counter();pilot='--pilot' in sys.argv
wrappers=[]
for ct in itertools.product([0,1],repeat=4):
 if sum(ct)<1:continue
 outside=[i for i,x in enumerate(ct) if not x]
 for signs in itertools.product([-1,1],repeat=len(outside)):
  kt=[0]*4
  for i,v in zip(outside,signs):kt[i]=v
  wrappers.append((ct,tuple(kt)))
E.ok(len(wrappers)==65)
const=[(a,b) for a in [(-1,),(1,)] for b in [(-1,),(1,)]]
lit=[(a,b) for a in [(1,-1),(-1,1)] for b in [(1,-1),(-1,1)]]
and2=(-1,-1,-1,1)
pairs=const+lit+[(and2,tuple(-v for v in and2))]
for bit in [0,1]:
 a=E.slice_table(and2,0,bit);pairs.append((a,tuple(-v for v in a)))
E.ok(len(pairs)==11)
def state(ct,kt,labels,cores):
 widths=[len(h).bit_length()-1 for h in cores]
 nc=len(labels).bit_length()-1
 tables=[]
 for y in range(1<<sum(widths)):
  vals=[];shift=0
  for h,n in zip(cores,widths):vals.append(h[(y>>shift)&((1<<n)-1)]);shift+=n
  for lab in labels:
   v=1 if lab==2 else vals[lab]
   for c,k in zip(ct,kt):tables.append(k+c*v)
 a=E.walsh(tuple(tables));H=E.entropy(a);U={};reserve={}
 means=[Q(sum(h),len(h)) for h in cores];vs=[1-m*m for m in means]
 c=Q(sum(ct),4)
 qs=[c*Q(labels.count(j),len(labels)) for j in range(2)]
 for j,h in enumerate(cores):
  U=E.add(U,E.add(E.entropy(E.walsh(h)),E.cost(means[j]**2),-1),qs[j])
  reserve=E.add(reserve,E.cost(qs[j]),vs[j])
 return a,H,U,reserve,qs,means,vs
count=0
for ct,kt in (wrappers[:3] if pilot else wrappers):
 c=Q(sum(ct),4);ca=E.walsh(ct);ka=E.walsh(kt)
 for widths in ([(1,1)] if pilot else [(1,1),(1,2),(2,1)]):
  w0,w1=widths;nc=w0+w1
  labels=tuple(0 if (x&((1<<w0)-1))==0 else 1 if x>>w0==0 else 2 for x in range(1<<nc))
  for cores in (const if pilot else pairs):
   parent=state(ct,kt,labels,cores);a,H,U,R0,qs,means,vs=parent
   for j,idx in [(0,0),(1,w0)]:
    count+=1
    child=[state(ct,kt,E.slice_table(labels,idx,b),cores) for b in [0,1]]
    d=E.influence(a,2+idx)
    B={}
    for s,z in enumerate(a):
     if not ((s>>(2+idx))&1):B=E.add(B,E.phi(z*z,a[s|(1<<(2+idx))]**2))
    DH=E.add(H,E.add(child[0][1],child[1][1]),-Q(1,2))
    kappa=E.add(R0,E.add(child[0][3],child[1][3]),-Q(1,2))
    DU=E.add(U,E.add(child[0][2],child[1][2]),-Q(1,2));E.ok(DU=={},'U harmonic')
    E.ok(E.influence(a)==d+(E.influence(child[0][0])+E.influence(child[1][0]))/2,'physical influence')
    q=Q(1,1<<widths[j]);m=means[j]
    if j==0:
     ee=(1,);kk=(0,);e=Q(1)
     n=Q(1,1<<w1)*means[1]+1-Q(1,1<<w1)
     V=1-n*n;Z=Q(1,1<<w1)*vs[1]
    else:
     ev=tuple(int(x!=0) for x in range(1<<w0));kv=tuple(means[0] if x==0 else 0 for x in range(1<<w0))
     ee=E.walsh(ev);kk=E.walsh(kv);e=Q((1<<w0)-1,1<<w0)
     n=Q(1);V=Q(0);Z=Q(0)
    delta=m-n;M=n+q*delta;x=q*delta
    predicted=c*e*q*(1-m*n);E.ok(d==predicted,'actual influence formula')
    k=E.add(E.cost(1-q),E.cost(1-2*q),-Q(1,2))
    predicted_k=E.add({2:c*e*q*vs[j]},k,c*e*Z)
    E.ok(kappa==predicted_k,'same fine reserve')
    S={}
    for s in range(4):
     for t,(eh,kh) in enumerate(zip(ee,kk)):
      aa=ka[s]*(t==0)+ca[s]*(kh+M*eh);bb=x*ca[s]*eh
      S=E.add(S,E.phi(aa*aa,bb*bb))
    rhs=E.add({2:c*e*(q-2*q*q)*(V+delta*delta)},E.phi((1-q)**2,q*q),c*e*V)
    rhs=E.add(E.add(rhs,k,-c*e*Z),S)
    E.ok(E.add(B,kappa,-1)==rhs,'FULL coherent erasure identity')
    tax=E.add({},E.cost(c),(e*q*delta)**2)
    E.le(E.add(DH,kappa,-1),E.add({2:21*d},tax),'all-c SINGLETON tax')
    inner=state((1,1,1,1),(0,0,0,0),labels,cores)
    gg=inner[0];bb=gg[1<<(2+idx)];mm=gg[0];BG={}
    for ss,zz in enumerate(gg):
     if not ((ss>>(2+idx))&1):BG=E.add(BG,E.phi(zz*zz,gg[ss|(1<<(2+idx))]**2))
    packet={}
    for cc,kk0 in zip(ca,ka):packet=E.add(packet,E.phi((kk0+mm*cc)**2,(bb*cc)**2))
    E.ok(B==E.add(E.add(E.add({},BG,c),E.phi(mm*mm,bb*bb),-c),packet),'general EMPTY-PAIR identity')
    E.ok((e*q*delta)**2==bb*bb,'actual singleton square')
    E.le({},kappa,'nonnegative controller reserve release')
   E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()
   if time.perf_counter()-start>(55 if pilot else 175):raise RuntimeError('frozen time cap')
E.ok(count==(24 if pilot else 4290),'frozen case count')
E.ok(sum(Q(25,6)**j / __import__('math').factorial(j) for j in range(12))>57,'ln57 Taylor certificate')
E.ok(6+Q(61,6)*Q(81,56)<21,'rational constant')
out=dict(status='PASS',rung='exact finite validation of analytic claim; not independent review',query_cases=count,assertions=E.checks,seconds=time.perf_counter()-start,helper_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),max_truth_table_dimension=9,pilot=pilot)
(R/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
