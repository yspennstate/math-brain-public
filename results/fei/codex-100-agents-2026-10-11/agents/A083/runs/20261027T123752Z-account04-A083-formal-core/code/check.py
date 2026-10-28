from pathlib import Path
from fractions import Fraction as F
import json,time,math
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0;rows=[]
def ck(v):
 global checks
 assert v,checks
 checks+=1
def law(vals):
 N=len(vals)
 return [F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals))**2,N*N) for s in range(N)]
def marginal(p,keep):
 out={}
 for s,v in enumerate(p):out[s&keep]=out.get(s&keep,F(0))+v
 return out
def erase(p,i):
 out=[F(0)]*(len(p)//2)
 for s,v in enumerate(p):out[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=v
 return out
def log_product(p,q,scale):
 z=F(1)
 for x,y in zip(p,q):
  exponent=scale*x
  assert exponent.denominator==1
  if x: z*=(x/y)**int(exponent)
 return z
for n in (4,6,8):
 N=1<<n;e=F(1,1<<(4*n));half=N//2
 vals=[(-1)**sum(((x>>(2*j))&3)==0 for j in range(n//2)) for x in range(N)]
 p=law(vals);ck(p==[F(1,N)]*N)
 q=[F(1,N)*(1+(1-e)*(-1 if (s&(half-1)).bit_count()%2 else 1)) if s&half else F(1,N) for s in range(N)]
 ck(sum(q)==1 and min(q)>0 and q[0]==p[0])
 influences=[sum(v for s,v in enumerate(p) if s&(1<<i)) for i in range(n)]
 ck(influences==[F(1,2)]*n);ck(sum(influences)==F(n,2))
 masks=0
 for keep in range(N):
  if keep.bit_count()<=n-2:
   ck(marginal(p,keep)==marginal(q,keep));masks+=1
 rootprod=log_product(p,q,N)
 ck(rootprod==(1/(e*(2-e)))**(N//4))
 # Exact signs for n-1/4<D<n and tail d<1/4.
 ck(1<2-e<2);ck(F(3)<(3-e)*(1+e)<4)
 ratio=4/((3-e)*(1+e));ck(1<ratio<F(4,3));ck(ratio**2<2)
 tailprod=None;query_rows=[]
 for i in range(n):
  pp=erase(p,i);qq=erase(q,i);ck(pp==[F(2,N)]*half)
  projprod=log_product(pp,qq,half)
  if i<n-1:ck(pp==qq and projprod==1)
  else:
   expected=[F(2,N)+F(1,N)*(1-e)*(-1 if v.bit_count()%2 else 1) for v in range(half)]
   ck(qq==expected);ck(projprod==ratio**(N//4));tailprod=projprod
  # Exact exponential certificate of n-1/2<L_i<n.
  lossprod=rootprod/(projprod**2) # log2 divided by N
  ck(lossprod**2>F(1<<(2*N*n-N)))
  ck(lossprod<F(1<<(N*n)))
  child_influences=[]
  for bit in (0,1):
   childvals=[vals[(x&((1<<i)-1))|(bit<<i)|((x>>i)<<(i+1))] for x in range(half)]
   child=law(childvals)
   ck(set(child)=={F(0),F(4,N)})
   ck(sum(v for v in child if v)==1)
   Ic=sum(s.bit_count()*v for s,v in enumerate(child));ck(Ic==F(n,2)-bit);child_influences.append(Ic)
   # Dchild=1+d_i, exactly, via equal exponent scale N.
   ck(log_product(child,qq,N)==F(1<<N)*projprod**2)
   # CEchild=n-1+d_i, including the remaining tail mismatch.
   ceprod=math.prod(((1/y)**int(N*x) for x,y in zip(child,qq) if x),start=F(1))
   ck(ceprod==F(1<<(N*(n-1)))*projprod**2)
  ck(F(n,2)==F(1,2)+sum(child_influences)/2)
  query_rows.append({'i':i+1,'projected_divergence':'zero' if i<n-1 else 'positive; half log2(4/((3-e)(1+e)))'})
 ck(tailprod>1)
 ck(time.perf_counter()-start<50)
 rows.append({'n':n,'truth_table_count':N,'marginal_masks':masks,'queries':n,'children':2*n,'query_rows':query_rows})
out={'status':'PASS','exact_assertions':checks,'seconds':time.perf_counter()-start,'rows':rows,'arithmetic':'Fraction/integer Walsh and rational likelihood powers; no floating signs'}
(R/'out/CHECK_RESULT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
