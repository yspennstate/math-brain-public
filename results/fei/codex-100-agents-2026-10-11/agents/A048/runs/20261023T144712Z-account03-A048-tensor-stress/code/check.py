from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, hashlib

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parents[2]
SOURCE=ROOT/'A036/runs/20261023T135330Z-account03-A036-reference-law-divergence'
count=0
def ok(v):
 global count
 assert v
 count+=1
def save(name,obj):
 (BASE/'out').mkdir(exist_ok=True)
 (BASE/'out'/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8')

def spec(t):
 a=list(t); step=1
 while step<len(a):
  for b in range(0,len(a),2*step):
   for j in range(b,b+step):
    u,v=a[j],a[j+step]; a[j],a[j+step]=u+v,u-v
  step*=2
 return [F(x,len(a)) for x in a]
def delete(s,i): return (s&((1<<i)-1))|((s>>(i+1))<<i)
def insert(s,i,y):return (s&((1<<i)-1))|(y<<i)|((s>>i)<<(i+1))
def child(t,i,y):return [t[insert(x,i,y)] for x in range(len(t)//2)]
def anchor(p,j):
 q=[F(5,6)*x for x in p];q[0]=p[0];q[j]+=F(1,6)*(1-p[0]);return q
@lru_cache(None)
def factors(a):
 out=[];d=2
 while d*d<=a:
  if a%d==0:
   k=0
   while a%d==0:a//=d;k+=1
   out.append((d,k))
  d+=1
 if a>1:out.append((a,1))
 return tuple(out)
def plus(a,b,c=F(1)):
 out=dict(a)
 for p,x in b.items():
  out[p]=out.get(p,F(0))+c*x
  if not out[p]:del out[p]
 return out
def kl(p,q):
 out={}
 for a,b in zip(p,q):
  if not a:continue
  ok(b>0);r=a/b
  for v,sign in [(r.numerator,1),(r.denominator,-1)]:
   for prime,k in factors(v):out[prime]=out.get(prime,F(0))+sign*k*a
 return {k:v for k,v in out.items() if v}

def main():
 start=time.perf_counter(); roots=edges=ghosts=0; hist={}
 for n in (1,2,3):
  dim=1<<n
  for bits in range(1<<dim):
   t=[1 if bits>>x&1 else -1 for x in range(dim)]
   a=spec(t);p=[x*x for x in a];ok(sum(p)==1)
   for j in range(1,dim):
    roots+=1;q=anchor(p,j);ok(sum(q)==1 and q[0]==p[0]);ok(all(y>=F(5,6)*x for x,y in zip(p,q)))
    ghosts+=int(p[j]==0 and q[j]>0);K=kl(p,q)
    # Every non-anchor nonempty row is exactly beta*P; anchor contribution is nonpositive.
    ok(q[j]>=p[j]);ok(all(q[s]==F(5,6)*p[s] for s in range(1,dim) if s!=j))
    for i in range(n):
     if j>>i&1:continue
     edges+=1;d=dim//2;jc=delete(j,i); pb=[F(0)]*d;qb=[F(0)]*d
     for s in range(dim):pb[delete(s,i)]+=p[s];qb[delete(s,i)]+=q[s]
     aa=[spec(child(t,i,y)) for y in (0,1)];pp=[[x*x for x in v] for v in aa]
     kernel=[[pp[y][s]/(2*pb[s]) if pb[s] else F(1,2) for s in range(d)] for y in (0,1)]
     ok(all(kernel[0][s]+kernel[1][s]==1 for s in range(d)))
     rr=[sum(qb[s]*kernel[y][s] for s in range(d)) for y in (0,1)]
     ok(sum(rr)==1 and min(rr)>=F(5,12))
     inherited=[[qb[s]*kernel[y][s]/rr[y] for s in range(d)] for y in (0,1)]
     for y in (0,1):
      ok(sum(inherited[y])==1 and sum(pp[y])==1)
      ok(all(not pp[y][s] or inherited[y][s]>0 for s in range(d)))
      ok(pp[y][jc]==(a[j]+(1 if y==0 else -1)*a[j|(1<<i)])**2)
     ki=[kl(pp[y],inherited[y]) for y in (0,1)]
     avg=plus({},{},F(0))
     for v in ki:avg=plus(avg,v,F(1,2))
     erased=plus(K,kl(pb,qb),F(-1));outcome=kl([F(1,2)]*2,rr)
     ok(not plus(plus(plus(K,erased,F(-1)),outcome,F(-1)),avg,F(-1)))
     fresh=[kl(pp[y],anchor(pp[y],jc)) for y in (0,1)]
     sigma=plus(plus({},fresh[0],F(1,2)),fresh[1],F(1,2));sigma=plus(sigma,avg,F(-1))
     # Alternate signed-reset expression from full chain, exactly equal in prime-log form.
     alternative=plus(plus(plus(plus({},fresh[0],F(1,2)),fresh[1],F(1,2)),K,F(-1)),erased)
     alternative=plus(alternative,outcome);ok(sigma==alternative)
     r=n-j.bit_count();aroot=1-p[j];achild=sum(1-v[jc] for v in pp)/2;b=a[j|(1<<i)]**2
     ok(achild==aroot-b);ok(r*aroot-(r-1)*achild==aroot+(r-1)*b);ok(r*aroot-(r-1)*achild>=achild)
  hist[n]={'tables':1<<dim}
 ok(roots==1844 and edges==2336 and ghosts>0)
 endpoints=[]
 for N in (10,12,20):
  delta=F(1,1<<N);bill=6*N*delta*F(4,15)
  ok(bill<=F(1,64));ok(12*delta*(3*N+2)<=F(3,8));ok(12*delta<=F(3,256))
  ok(F(741,256)-F(1,64)-F(1,4)==F(673,256))
  endpoints.append({'N':N,'inclusive_bill_upper':str(bill),'reserve_strict_lower':'673/256'})
 ok(6**15<16*5**15)
 claims=json.loads((SOURCE/'CLAIMS.json').read_text(encoding='utf-8'))
 c=next(x for x in claims if x['claim_id']=='A036-CHARACTER-ANCHORED-NORMALIZED-DIVERGENCE-BANK')
 ok(hashlib.sha256(c['exact_statement'].encode()).hexdigest()==c['statement_sha256'])
 result={'status':'PASS','assertions':count,'roots':roots,'physical_edges':edges,'reference_only_anchor_roots':ghosts,'endpoints':endpoints,'seconds':time.perf_counter()-start,'source_claim_sha256':c['statement_sha256'],'arithmetic':'exact Fraction and prime-log linear forms; analytic inequalities in PROOF.md'}
 save('CHECK.json',result);print(json.dumps(result))
if __name__=='__main__':main()
