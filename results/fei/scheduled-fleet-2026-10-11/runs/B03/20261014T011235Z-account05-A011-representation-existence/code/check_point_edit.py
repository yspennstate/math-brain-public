import pathlib,json,time,itertools,sys
from fractions import Fraction as F
from functools import lru_cache
R=pathlib.Path(__file__).resolve().parents[1]; start=time.monotonic(); assertions=0
def ck(x):
 global assertions
 assertions+=1
 assert x,assertions
def fw(table):
 v=list(table); k=1
 while k<len(v):
  for a in range(0,len(v),2*k):
   for j in range(a,a+k): v[j],v[j+k]=v[j]+v[j+k],v[j]-v[j+k]
  k*=2
 return tuple(F(z,len(v)) for z in v)
def influences(v,n): return tuple(F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v)) for j in range(n))
@lru_cache(None)
def factors(n):
 out={}; d=2
 while d*d<=n:
  while n%d==0: out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1: out[n]=out.get(n,0)+1
 return out
def plus(a,b,scale=F(1)):
 for k,v in b.items(): a[k]=a.get(k,0)+scale*v
 return {k:v for k,v in a.items() if v}
@lru_cache(None)
def logv(x):
 out={}
 for k,v in factors(x.numerator).items(): out[k]=F(v)
 for k,v in factors(x.denominator).items(): out[k]=out.get(k,0)-v
 return {k:v for k,v in out.items() if v}
@lru_cache(None)
def ce(p,q):
 out={}
 for x,y in zip(p,q):
  if x: ck(y>0);out=plus(out,logv(y),-x)
 return out
def entropy(p): return ce(p,p)
def ln_bounds(z):
 w=(z-1)/(z+1); term=w; acc=F(0)
 for j in range(40): acc+=2*term/(2*j+1);term*=w*w
 return acc,acc+2*term/(81*(1-w*w))
@lru_cache(None)
def log_bounds(z):
 z=F(z); k=0
 while z>=2:z/=2;k+=1
 while z<1:z*=2;k-=1
 lo,hi=ln_bounds(z);l2,u2=ln_bounds(F(2))
 return k+lo/u2,k+hi/l2
@lru_cache(None)
def bounds_cached(items):
 lo=hi=F(0)
 for k,v in items:
  a,b=log_bounds(k);lo+=v*(a if v>0 else b);hi+=v*(b if v>0 else a)
 return lo,hi
def bounds(vector): return bounds_cached(tuple(sorted(vector.items())))
def entropy_interval(atoms):
 lo=hi=F(0)
 for multiplicity,p in atoms:
  if not p: continue
  a,b=log_bounds(p); lo-=multiplicity*p*b;hi-=multiplicity*p*a
 return lo,hi
counts={'small':0,'references':0,'local_extremum':0,'bent_direct':0,'bent_compressed':0}; equal_cost={}; fixtures=[]
def case(h,m,y0,r,bent=False):
 ck(time.monotonic()-start<55)
 N=2**m; M=2**r;p=F(1,M);t=F(1,N)
 hs=list(h);hs[y0]=-hs[y0];hs=tuple(hs)
 a=fw(h);as_=fw(hs);ph=tuple(z*z for z in a);ps=tuple(z*z for z in as_)
 table=tuple((-h[y] if x==0 and y==y0 else h[y]) for y in range(N) for x in range(M))
 coeff=fw(table); law=tuple(z*z for z in coeff)
 for T in range(N):
  orient=h[y0]*(-1)**((T&y0).bit_count())
  ck(coeff[T*M]==a[T]-2*p*t*orient)
  for U in range(1,M):ck(coeff[T*M+U]==-2*p*t*orient)
 q=tuple((1-p)*ph[T]+p*ps[T] for T in range(N))
 ck(q==tuple(sum(law[T*M+U] for U in range(M)) for T in range(N)))
 Ih=sum(influences(h,m));Is=sum(influences(hs,m));If=influences(table,m+r)
 d=sum(h[y0]!=h[y0^(1<<j)] for j in range(m)); C=2*p*t*(m-d);E=2*p*t*d;Delta=C-E
 sel=2*r*p*t;V=4*p*(1-p)*t
 ck(sum(If[:r])==sel);ck(sum(If[r:])==Ih+Delta);ck(Is-Ih==2*t*(m-2*d))
 ck(sum(law[T*M+U] for T in range(N) for U in range(1,M))==V)
 B=plus(entropy(law).copy(),entropy(q),-1)
 ck(bounds(B)[1]<=m*V+4*sel)
 ck(m*V==2*(1-p)*Delta+4*(1-p)*E)
 if not d:
  counts['local_extremum']+=1;ck(Delta>=0);ck(bounds(B)[1]<=2*(1-p)*Delta+4*sel)
 js=plus(plus(entropy(q).copy(),entropy(ph),-(1-p)),entropy(ps),-p)
 kappa={}
 for T in range(N):
  if not q[T]:continue
  kp=((1-p)*ph[T]/q[T],p*ps[T]/q[T]);prior=(1-p,p)
  kappa=plus(kappa,plus(ce(kp,prior).copy(),entropy(kp),-1),q[T])
 ck(kappa==js)
 for ref in [(t,)*N,tuple(F(T+1,N*(N+1)//2) for T in range(N)),(t/2,)*N]:
  Q=tuple(ref[T]*(law[T*M+U]/q[T] if q[T] else F(U==0)) for T in range(N) for U in range(M))
  cost=ce(law,Q);avg=plus(ce(ph,ref).copy(),ce(ps,ref),p);avg=plus(avg,ce(ph,ref),-p)
  ck(sum(Q)==sum(ref));ck(cost==plus(avg.copy(),B))
  ck(plus(cost.copy(),entropy(law),-1)==plus(ce(q,ref).copy(),entropy(q),-1))
  if not bent:counts['references']+=1
 if bent:
  ck(d==y0.bit_count());ck(Ih==F(m,2));ck(all(x==t for x in ph))
  ck(m+bounds(B)[1]<=4*sum(If))
  key=(m,r)
  if key in equal_cost:ck(equal_cost[key]==B)
  else:equal_cost[key]=B
  if d==m//2 and r==1: ck(Delta==0);ck(bounds(B)[0]>=t*(m-1))
mode=sys.argv[1]
if mode=='small': ms=(1,2)
elif mode.startswith('n3-'): ms=(3,); shard=int(mode[3:]);ck(0<=shard<8)
elif mode=='bent': ms=()
else: raise ValueError(mode)
for m in ms:
 masks=range(32*shard,32*(shard+1)) if m==3 else range(2**(2**m))
 for mask in masks:
  h=tuple(1 if mask>>y&1 else -1 for y in range(2**m))
  for y0 in range(2**m):
   for r in (1,2,3):case(h,m,y0,r);counts['small']+=1
for m in ((2,4,6) if mode=='bent' else ()):
 h=tuple((-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(m//2)) for y in range(2**m))
 for weight in range(m+1):
  for r in (1,2,3):case(h,m,(1<<weight)-1,r,True);counts['bent_direct']+=1
for m in ((4,6,8,10,12,16,24,32) if mode=='bent' else ()):
 for r in (1,2,3,4):
  ck(time.monotonic()-start<55)
  t=F(1,2**m);b=F(1,2**(m//2));p=F(1,2**r);M=2**r;sel=2*r*p*t
  Ns=[(2**m+2**(m//2))//2,(2**m-2**(m//2))//2]
  qa=[t*(1-4*p*sg*b+4*p*t) for sg in (1,-1)]
  empty=[t*(sg-2*p*b)**2 for sg in (1,-1)];v=4*p*p*t*t
  ck(sum(Ns[k]*qa[k] for k in (0,1))==1)
  ck(all(empty[k]+(M-1)*v==qa[k] for k in (0,1)))
  hp=entropy_interval([(Ns[k],empty[k]) for k in (0,1)]+[(2**m*(M-1),v)])
  hq=entropy_interval(list(zip(Ns,qa)));B=(hp[0]-hq[1],hp[1]-hq[0]);V=4*p*(1-p)*t
  ck(B[1]<=m*V+4*sel)
  # Worst physical point degree m, retaining source edges lost by surgery.
  I_min=F(m,2)-2*m*p*t+sel
  ck(m+B[1]<=4*I_min)
  if r==1:
   ck(B[0]>=t*(m-1));chi=sum(Ns[k]*(qa[k]-t)**2/t for k in (0,1))
   ck(chi==4*t*(1-t));ck(hp[0]-m>t*(m-7))
   if m==16:
    ck(hp[0]-m>8*sel)
    fixtures.append({'m':m,'r':r,'edited_point_weight':m//2,'selector_I':str(sel),'data_increment':'0','true_H_minus_m_interval':[str(hp[0]-m),str(hp[1]-m)],'refuted_K':8,'any_A_positive_net_increment':True})
  counts['bent_compressed']+=1
if mode=='small': ck(counts['small']==216);ck(counts['references']==648)
elif mode.startswith('n3-'): ck(counts['small']==768);ck(counts['references']==2304)
else: ck(counts['bent_direct']==45);ck(counts['bent_compressed']==32)
out={'status':'PASS','helper_version':'A011-one-leaf-point-edit-v1.1','mode':mode,'counts':counts,'exact_assertions':assertions,'seconds':time.monotonic()-start,'memory':'100 MB estimate, peak not measured','neutral_countercertificate':fixtures,'scope':'Exact finite validation; all-parameter proofs in POINT_EDIT_TRANSFER.md'}
(R/'out'/('EXACT_'+mode+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='neutral_countercertificate'}))
