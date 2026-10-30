from pathlib import Path
from fractions import Fraction as F
import itertools,math,time,json,sys
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(v):
 global checks
 assert v
 checks+=1
 if checks%500==0 and time.monotonic()-start>55:raise RuntimeError('55-second frozen limit')
def fwht(a):
 a=a[:];s=1
 while s<len(a):
  for st in range(0,len(a),2*s):
   for i in range(st,st+s):u,v=a[i],a[i+s];a[i],a[i+s]=u+v,u-v
  s*=2
 return a
def pgf_upper(t,K=16):return sum(F(t**c,(c+1)*(c+2)) for c in range(K+1))+t**(K+1)/F(K+2)
def moment():
 cert=pgf_upper(F(17,20));ck(cert<F(4,5))
 toys=[]
 for j in range(8,17):
  lam=[F(1,1<<j),F(1,4),F(1,8)];pi=F(1,1<<12);xs=[l*pi for l in lam];A=sum(xs);D=math.prod(1+x for x in xs)-1
  t=lam[0];z=1/(16*(t+A));ck(z>=1 and z*t<=F(1,16) and z*A<=F(1,16))
  f=F(0)
  for h in range(1,4):
   child=f*(sum(lam)+(z-1)*t)
   # Explicit finite subset of runs: height<=h, at most2 children per visit.
   f=sum(child**c/F((c+1)*(c+2)) for c in range(3));ck(f<=F(4,5))
   root_product=(math.prod(1+z*x*f for x in xs)-1)/(z*D)
   root_sum=sum(z**(mask.bit_count()-1)*math.prod(xs[i]*f for i in range(3) if mask>>i&1)/D for mask in range(1,8))
   ck(root_product==root_sum<=F(16,19))
  ck((math.prod(1+F(4,5)*z*x for x in xs)-1)/(z*D)<=F(16,19))
  toys.append({'j':j,'z':str(z)})
 for w in range(32,129):
  r=1<<w;ck((48*w)**2<=r);ck(r-1>=F(w*w,8));ck(F(w,2)-1>=F(w,4))
  ck(sum(math.comb(w,k) for k in range((w+1)//2,w+1))>=r//2)
 for w in range(1,9):
  r=1<<w;p=F(r-1,r);a=p**r;q=p**(r-1)
  ck(q>F(1,3));ck(F(1,2)*q**4>F(1,162));ck(2*w*q<2*w)
 return {'pgf_upper':str(cert),'pgf_bound':'4/5','toy_references':len(toys),'scalar_w_cases':97,'product_w_cases':8}
def family(w):
 r=1<<w;dim=r*w;n=2*dim;M=1<<n;mask=(1<<w)-1
 def u(x):return all((x>>(c*w))&mask for c in range(r))
 def v(y):return any(((y>>(c*w))&mask)==mask for c in range(r))
 truth=[2*int(u(x&((1<<dim)-1)) and v(x>>dim))-1 for x in range(M)]
 walsh=fwht(truth);ck(sum(z*z for z in walsh)==M*M)
 p=F(r-1,r);I=F(sum(a.bit_count()*z*z for a,z in enumerate(walsh)),M*M)
 ck(I==2*w*p**(r-1))
 physical=F(sum(truth[x]!=truth[x^(1<<i)] for i in range(n) for x in range(M)),M);ck(I==physical)
 joint=0
 for C in range(r):
  for D in range(r):
   for sx in range(1,1<<w):
    for sy in range(1,1<<w):
     a=(sx<<(C*w))|(sy<<(dim+D*w));ck(F(walsh[a]**2,M*M)==4*F(1,r)**4*p**(4*(r-1)));joint+=1
 # Independent actual prime sufficiency and minimality via completions and neighboring witnesses.
 positives=[]
 for choices in itertools.product(range(w),repeat=r):
  tx=sum(1<<(c*w+j) for c,j in enumerate(choices))
  for D in range(r):positives.append(tx|(mask<<(dim+D*w)))
 negatives=[mask<<(C*w) for C in range(r)]+[sum(1<<(dim+c*w+j) for c,j in enumerate(choices)) for choices in itertools.product(range(w),repeat=r)]
 for polarity,primes in [(1,positives),(-1,negatives)]:
  for fixed in primes:
   free=[i for i in range(n) if not fixed>>i&1]
   for z in range(1<<len(free)):
    x=(fixed if polarity==1 else 0)|sum(1<<free[j] for j in range(len(free)) if z>>j&1)
    ck(truth[x]==polarity)
   for i in range(n):
    if fixed>>i&1:
     ck(any(truth[((fixed if polarity==1 else 0)^ (1<<i))|sum(1<<free[j] for j in range(len(free)) if z>>j&1)]!=polarity for z in range(1<<len(free))))
 return {'w':w,'n':n,'truth_points':M,'joint_sector_sets':joint,'positive_candidate_primes':len(positives),'negative_candidate_primes':len(negatives),'influence':str(I)}
def structure(maxn):
 funcs=targets=disconnected=0
 for n in range(1,maxn+1):
  M=1<<n;allpoints=(1<<M)-1;faces=[]
  for pat in itertools.product((-1,0,1),repeat=n):
   support=sum(1<<i for i,v in enumerate(pat) if v!=-1)
   points=sum(1<<x for x in range(M) if all(v==-1 or (x>>i&1)==v for i,v in enumerate(pat)))
   faces.append((pat,support,points))
  for truthmask in range(1,allpoints):
   funcs+=1;tables=[]
   for signmask in [truthmask,allpoints^truthmask]:
    valid={pat for pat,s,pts in faces if pts&signmask==pts}
    tables.append([s for pat,s,pts in faces if pat in valid and all(tuple(-1 if j==i else pat[j] for j in range(n)) not in valid for i in range(n) if pat[i]!=-1)])
   walsh=fwht([1 if truthmask>>x&1 else -1 for x in range(M)])
   for A in range(1,M):
    if not walsh[A]:continue
    targets+=1;graphs=[];comps=[]
    for table in tables:
     adj={i:1<<i for i in range(n) if A>>i&1}
     for support in table:
      meet=support&A
      for i in adj:
       if meet>>i&1:adj[i]|=meet
     components=[];remaining=A
     while remaining:
      block=remaining&-remaining
      while True:
       grow=block
       for i in adj:
        if block>>i&1:grow|=adj[i]
       if grow==block:break
       block=grow
      components.append(block);remaining&=~block
     graphs.append(adj);comps.append(components)
    ck(len(comps[0])==1 or len(comps[1])==1)
    if len(comps[0])>1:
     disconnected+=1
     for c in comps[0]:
      for d in comps[0]:
       if c==d:continue
       for i in range(n):
        if c>>i&1:ck(graphs[1][i]&d==d)
    orient=0 if len(comps[0])==1 else 1;table=tables[orient]
    first=next(s for s in table if s&A);selected=[first];owned=[first&A];used=owned[0]
    while used!=A:
     support=next(s for s in table if (s&used) and (s&A&~used))
     fresh=support&A&~used;selected.append(support);owned.append(fresh);used|=fresh
    # FULL ownership graph traversal, not merely the recorded construction tree.
    reached={0}
    while True:
     nxt=reached|{j for i in reached for j in range(len(selected)) if owned[i]&selected[j]}
     if nxt==reached:break
     reached=nxt
    ck(len(reached)==len(selected)<=A.bit_count());ck(sum(x.bit_count() for x in owned)==A.bit_count())
 return {'functions':funcs,'fourier_targets':targets,'positive_disconnected':disconnected}
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'pilot';res={'moment':moment(),'structure':structure(2 if mode=='pilot' else 3),'family':[]}
 for w in ([1] if mode=='pilot' else [1,2]):
  res['family'].append(family(w));(RUN/'out'/f'{mode}.json').write_text(json.dumps(res,indent=2),encoding='utf-8')
 res.update(status='PASS',checks=checks,elapsed_seconds=time.monotonic()-start)
 (RUN/'out'/f'{mode}.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf-8');print(json.dumps(res))
