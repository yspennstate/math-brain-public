from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import itertools,json,time,hashlib,argparse,math
ROOT=Path(__file__).resolve().parent
checks=0;start=0
def check(x):
 global checks
 checks+=1
 assert x
def save(name,obj):
 def conv(x):
  if isinstance(x,F):return str(x)
  if isinstance(x,dict):return {str(k):conv(v) for k,v in x.items()}
  if isinstance(x,(list,tuple)):return [conv(v) for v in x]
  return x
 (ROOT/'out'/name).write_text(json.dumps(conv(obj),indent=2)+'\n',encoding='utf-8')
def lnunit(x):
 t=1-F(1)/x
 a=sum((t**j/F(j) for j in range(1,41)),F(0))
 return a,a+t**41/(41*(1-t))
LN2=lnunit(F(2))
@lru_cache(None)
def logint(x):
 x=F(x);k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 if x==1:return F(k),F(k)
 a,b=lnunit(x)
 return F(k)+a/LN2[1],F(k)+b/LN2[0]
def add(v,w,q):
 a,b=q
 if w<0:a,b=b,a
 return v[0]+w*a,v[1]+w*b
@lru_cache(None)
def phi(a,b):
 if not a or not b:return F(0),F(0)
 # Enclose entropy directly through the conditional distribution, not entropy subtraction.
 q=a+b;v=(F(0),F(0))
 for mass in [a,b]:v=add(v,-mass,logint(F(mass,q)))
 return v
KFORM={2:F(16,3),3:-F(21,8),5:F(95,24),11:-F(121,24),13:F(65,24)}
def formint(d):
 v=(F(0),F(0))
 for p,w in d.items():v=add(v,w,logint(p))
 return v
KINT=formint(KFORM)
@lru_cache(None)
def factor(n):
 d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def formadd(d,z,w):
 for p,e in factor(z).items():
  d[p]=d.get(p,F(0))+e*w
  if not d[p]:del d[p]
def pointset(k,l):
 r=2*k+l
 return {0}|{1<<i for i in range(r)}|{(1<<(2*j))|(1<<(2*j+1)) for j in range(k)}
@lru_cache(None)
def character_signs(n):
 N=1<<n
 return [[(-1 if (x&s).bit_count()%2 else 1) for x in range(N)] for s in range(N)]
def spectrum(points,n):
 N=1<<n
 # Only visit actual negative points; direct Fourier sums, no butterfly transform.
 W=[(N if s==0 else 0)-2*sum(-1 if (x&s).bit_count()%2 else 1 for x in points) for s in range(N)]
 a=[w*w for w in W];check(sum(a)==N*N)
 edge=[sum((x in points)!=((x^(1<<i)) in points) for x in range(N) if not(x>>i&1)) for i in range(n)]
 for i in range(n):check(sum(a[s] for s in range(N) if s>>i&1)==2*edge[i]*N)
 return W,a,edge
def convolution(k,l):
 # Coefficients of (z^3+3z^-1)^k(z+z^-1)^l.
 d={0:1}
 for terms in ([{3:1,-1:3}]*k+[{1:1,-1:1}]*l):
  e=Counter()
  for s,m in d.items():
   for t,c in terms.items():e[s+t]+=m*c
  d=dict(e)
 return d
def compressed(k,l):
 r=2*k+l;N=1<<r;a=1+3*k+l
 mass=Counter()
 for z,m in convolution(k,l).items():mass[4*(1+z)**2]+=m
 mass[4*a*a]-=1;mass[(N-2*a)**2]+=1
 mass={q:m for q,m in mass.items() if m};check(sum(mass.values())==N);check(sum(q*m for q,m in mass.items())==N*N)
 rows=[]
 for kind in ['paired','isolated']:
  if kind=='paired' and not k:continue
  if kind=='isolated' and not l:continue
  c=4 if kind=='paired' else 2;delta=a-c
  if not delta:continue
  check(delta>0)
  residual=convolution(k-1,l) if kind=='paired' else convolution(k,l-1)
  packets=Counter()
  for z,m in residual.items():
   u=1+z
   if kind=='paired':
    packets[(4*(u+3)**2,4*(u-1)**2)]+=m
    packets[(4*(u-1)**2,4*(u-1)**2)]+=m
   else:packets[(4*(u+1)**2,4*(u-1)**2)]+=m
  old=(4*a*a,4*delta*delta);packets[old]-=1;packets[((N-2*a)**2,4*delta*delta)]+=1
  packets={q:m for q,m in packets.items() if m};check(sum(packets.values())==N//2)
  B=(F(0),F(0))
  for (x,y),m in packets.items():
   v=phi(*sorted((x,y)));B=add(B,F(m,N*N),v)
  inf=F(2*delta,N);E=(B[0]/inf,B[1]/inf)
  equality=k==3 and l==0
  if equality:
   d={}
   for (x,y),m in packets.items():
    if not x or not y:continue
    for z,w in [(x+y,x+y),(x,-x),(y,-y)]:formadd(d,z,F(m*w,N*N)/inf)
   check(d==KFORM)
  else:check(E[1]<KINT[0])
  rows.append({'type':kind,'influence':inf,'packets':[{'unnormalized_joint':list(q),'multiplicity':m} for q,m in packets.items()],'B_interval':B,'ratio_interval':E,'exact_K6_equality':equality})
 return {'k':k,'l':l,'r':r,'a':a,'squared_walsh_histogram':mass,'rows':rows}
def directB(a,n,i):
 N=1<<n;v=(F(0),F(0))
 for s in range(N):
  if not(s>>i&1):v=add(v,F(1,N*N),phi(*sorted((a[s],a[s|(1<<i)]))))
 return v
def restricted(points,n,history):
 free=[i for i,z in enumerate(history) if z==-1]
 actual=set()
 for x in points:
  if all(z==-1 or (x>>i&1)==z for i,z in enumerate(history)):
   actual.add(sum(((x>>i)&1)<<j for j,i in enumerate(free)))
 return actual,free
def classify(k,l,history,free):
 ones=[i for i,z in enumerate(history) if z==1];pair={i:i^1 for i in range(2*k)}
 if not ones:
  predicted={0}|{1<<j for j in range(len(free))}
  predicted|={ (1<<free.index(i))|(1<<free.index(i+1)) for i in range(0,2*k,2) if i in free and i+1 in free}
  return predicted,'matching'
 if len(ones)==1:
  predicted={0};partner=pair.get(ones[0])
  if partner in free:predicted.add(1<<free.index(partner))
  return predicted,'point_dummy' if len(predicted)==2 else 'point'
 if len(ones)==2 and pair.get(ones[0])==ones[1]:return {0},'point'
 return set(),'constant'
def verify_restrictions(maxr,cap):
 histories=0;classes=Counter();tree_checks=0
 for r in range(maxr+1):
  for k in range(r//2+1):
   l=r-2*k;points=pointset(k,l);rootW,roota,rootedge=spectrum(points,r)
   comp=compressed(k,l);check(Counter(roota)==comp['squared_walsh_histogram'])
   for i in range(r):
    if rootedge[i]:
     kind='paired' if i<2*k else 'isolated';row=next(q for q in comp['rows'] if q['type']==kind)
     packets=Counter((roota[s],roota[s|(1<<i)]) for s in range(1<<r) if not(s>>i&1))
     check(packets==Counter({tuple(q['unnormalized_joint']):q['multiplicity'] for q in row['packets']}))
   cache={}
   for history in itertools.product([-1,0,1],repeat=r):
    histories+=1;actual,free=restricted(points,r,history);predicted,cls=classify(k,l,history,free)
    check(actual==predicted);classes[cls]+=1
    key=(len(free),tuple(sorted(actual)))
    if key not in cache:cache[key]=spectrum(actual,len(free))
    W,aa,ee=cache[key];n=len(free);N=1<<n
    for i in range(n):
     if ee[i]:
      v=directB(aa,n,i);inf=F(2*ee[i],N)
      if not(r==6 and k==3 and all(z==-1 for z in history)):check(v[1]/inf<KINT[0])
    # Every actual split conserves retained influence and the signed spectral law.
    for i in range(n):
     childdata=[]
     for z in [0,1]:
      hh=list(history);hh[free[i]]=z;pp,ff=restricted(points,r,hh)
      ck=(len(ff),tuple(sorted(pp)))
      if ck not in cache:cache[ck]=spectrum(pp,len(ff))
      childdata.append(cache[ck])
     w0,b0,e0=childdata[0];w1,b1,e1=childdata[1]
     for s in range(1<<(n-1)):
      lift=(s&((1<<i)-1))|((s>>i)<<(i+1))
      check(2*w0[s]==W[lift]+W[lift|(1<<i)])
      check(2*w1[s]==W[lift]-W[lift|(1<<i)])
      check(2*(b0[s]+b1[s])==aa[lift]+aa[lift|(1<<i)])
     other=[j for j in range(n) if j!=i]
     for j,t in enumerate(other):check(ee[t]==e0[j]+e1[j])
     tree_checks+=1
    check(time.perf_counter()-start<cap)
   save(f'restrictions_r{r}_k{k}.json',{'r':r,'k':k,'l':l,'histories':3**r,'negative_set':sorted(points),'closure_predicate':'all simultaneous assignments matched explicit classification','distinct_child_tables':len(cache),'failures':0})
 result={'histories':histories,'classes':dict(classes),'physical_split_checks':tree_checks,'failures':0};save('restrictions_summary.json',result);return result
def structural(maxg,maxp,cap):
 graphs=paths=0
 for n in range(maxg+1):
  pairs=list(itertools.combinations(range(n),2));N=1<<n
  for mask in range(1<<len(pairs)):
   edgepairs=[p for j,p in enumerate(pairs) if mask>>j&1];points={0}|{1<<i for i in range(n)}|{(1<<i)|(1<<j) for i,j in edgepairs}
   W,a,ee=spectrum(points,n);size=len(points)
   for i in range(n):
    deg=sum(i in e for e in edgepairs);check(ee[i]==size-2*(1+deg));check(W[1<<i]==-2*ee[i])
   graphs+=1;check(time.perf_counter()-start<cap)
  save(f'graphs_n{n}.json',{'graphs':1<<len(pairs),'degree/singleton/influence_formula':'all exact matches','failures':0})
 for n in range(maxp+1):
  N=1<<n
  for m in range(n+1):
   points={ (1<<j)-1 for j in range(m+1)};W,a,ee=spectrum(points,n)
   for i in range(n):
    check(ee[i]==(m-1 if i<m else m+1))
    check(W[1<<i]==-2*(2*(i+1)-m-1 if i<m else m+1))
   paths+=1
 save('structural_summary.json',{'graphs':graphs,'paths':paths,'failures':0});return graphs,paths
def cutoffs():
 U=lambda r:F(2)+F(8,r-3)+F((3*r+2)*(4*r+3),2*(1<<r))
 G=lambda n:F(2)+F(8,n-4)+F((n*n+n+2)*(4*n+3),2*(1<<n))
 P=lambda n:F(2)+F((n+1)*(4*n+3),1<<n)
 Q=lambda n:F(2)+F(4,n-1)+F(4*n+3,(n-1)*(1<<n))
 check(U(13)==F(240651,81920));check(U(13)<F(368,125));check(F(368,125)<KINT[0])
 check(G(16)==F(551825,196608));check(G(16)<F(368,125))
 check(P(10)==F(2521,1024));check(Q(10)==F(22571,9216));check(max(P(10),Q(10))<F(368,125))
 # Exact coefficients prove the positive monotonicity polynomial identities.
 def pm(r):return F((3*r+2)*(4*r+3),2)
 def pg(n):return F((n*n+n+2)*(4*n+3),2)
 def pp(n):return F((n+1)*(4*n+3))
 for r in [13,14,20,64]:check(2*pm(r)-pm(r+1)==6*r*r-F(7,2)*r-F(23,2))
 for n in [16,17,20,64]:check(2*pg(n)-pg(n+1)==2*n**3-F(5,2)*n*n-F(15,2)*n-8)
 for n in [10,11,20,64]:check(2*pp(n)-pp(n+1)==4*n*n-n-8)
 result={'matching_tail_start':13,'matching_U13':U(13),'graph_tail_start':16,'graph_G16':G(16),'path_tail_start':10,'padded_path_P10':P(10),'full_path_Q10':Q(10),'K6_interval':KINT,'failure_count':0};save('analytic_cutoffs.json',result);return result
def main():
 global start
 parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
 (ROOT/'out').mkdir(exist_ok=True);start=time.perf_counter();cap=55 if args.pilot else 180
 allrows=[]
 for r in range(13):
  for k in range(r//2+1):
   obj=compressed(k,r-2*k);allrows.append(obj);save(f'compressed_r{r}_k{k}.json',obj)
 check(len(allrows)==49)
 cutoff=cutoffs();restrictions=verify_restrictions(4 if args.pilot else 6,cap)
 graphs,paths=structural(3 if args.pilot else 5,3 if args.pilot else 6,cap)
 if not args.pilot:check(restrictions['histories']==3964);check(graphs==1100);check(paths==28)
 result={'pilot':args.pilot,'compressed_parameters':len(allrows),'compressed_orbits':sum(len(o['rows']) for o in allrows),'exact_K6_orbits':sum(row['exact_K6_equality'] for o in allrows for row in o['rows']),'restriction_validation':restrictions,'graphs':graphs,'paths':paths,'exact_assertions':checks,'runtime_seconds':time.perf_counter()-start,'log_precision_refinements':0,'failures':0,'original_code_imported':False}
 save('pilot_summary.json' if args.pilot else 'summary.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
