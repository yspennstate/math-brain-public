from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, time, sys, hashlib
ROOT=Path(__file__).resolve().parents[1]
N=0
START=time.perf_counter()
def ok(v):
 global N
 assert v
 N+=1
 if N%256==0: assert time.perf_counter()-START<55, 'frozen runtime exceeded'
@lru_cache(None)
def factors(n):
 d={}; k=2
 while k*k<=n:
  while n%k==0:d[k]=d.get(k,0)+1;n//=k
  k+=1
 if n>1:d[n]=d.get(n,0)+1
 return d
def log(x):
 x=F(x); assert x>0
 d={p:F(k) for p,k in factors(x.numerator).items()}
 for p,k in factors(x.denominator).items():d[p]=d.get(p,F(0))-k
 return {p:k for p,k in d.items() if k}
def add(*terms):
 d={}
 for w,e in terms:
  for p,k in e.items():d[p]=d.get(p,F(0))+w*k
 return {p:k for p,k in d.items() if k}
def ce(p,q):
 return add(*[(-v,log(q[i])) for i,v in enumerate(p) if v])
def ent(p):return ce(p,p)
def kl(p,q):return add((1,ce(p,q)),(-1,ent(p)))
@lru_cache(maxsize=16)
def fw(v):
 a=list(v);s=1
 while s<len(a):
  for base in range(0,len(a),2*s):
   for j in range(base,base+s):u=a[j];v=a[j+s];a[j]=u+v;a[j+s]=u-v
  s*=2
 return tuple(F(x,len(a)) for x in a)
def prob(v):return tuple(x*x for x in fw(v))
def truth(mask,n):return tuple(-1 if mask>>i&1 else 1 for i in range(1<<n))
def restr(v,i,b):
 return tuple(v[(s&((1<<i)-1))|((s>>i)<<(i+1))|(b<<i)] for s in range(len(v)//2))
def influence(v):
 n=(len(v)-1).bit_length()
 return sum(F(sum(v[s]!=v[s^(1<<i)] for s in range(len(v))),len(v)) for i in range(n))
def prod(bits):
 out=[F(1)]
 for p in bits:out=[x*(1-p) for x in out]+[x*p for x in out]
 return out
def mixture_identity(p,components,weights):
 L=len(p);M=len(weights)
 q=[sum(weights[j]*components[j][0][s]*components[j][1][t] for j in range(M)) for t in range(L) for s in range(L)]
 diag=[p[s] if s==t else F(0) for t in range(L) for s in range(L)]
 if any(p[s] and not q[s*(L+1)] for s in range(L)):return
 joint=[[p[s]*weights[j]*components[j][0][s]*components[j][1][s]/q[s*(L+1)] if p[s] else F(0) for s in range(L)] for j in range(M)]
 v=[sum(row) for row in joint]; hc={}; hjs={}; cond={}
 for j,row in enumerate(joint):
  if not v[j]:continue
  pj=[x/v[j] for x in row]
  hc=add((1,hc),(v[j],ent(pj)))
  cond=add((1,cond),(v[j],kl(pj,components[j][0])),(v[j],kl(pj,components[j][1])))
 for s,x in enumerate(p):
  if x:hjs=add((1,hjs),(x,ent([joint[j][s]/x for j in range(M)])))
 D=kl(diag,q)
 ok(D==add((1,hc),(1,kl(v,weights)),(1,cond)))
 residual=add((1,kl(v,[F(1,M)]*M)),(1,hjs),(1,kl(v,weights)),(1,cond))
 ok(add((1,D),(-1,ent(p)),(1,log(M)))==residual)
 return D
A=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
B=tuple(1-x*x for x in A);AA=fw(A);BB=fw(B);beta=F(3,8)
def wrapper(h,sigma):return tuple(A[u]+sigma*B[u]*h[s] for s in range(len(h)) for u in range(16))
def reference(q):
 out=[F(0)]*(16*(1+len(q)))
 # Actual tags are supplied explicitly by the caller: use sparse dictionary instead.
 return out
def coherent(pseed):
 q={u:AA[u]**2 for u in range(16) if AA[u]}
 for s,x in enumerate(pseed):
  if s and x:
   for u in range(16):
    if BB[u]:q[u+16*s]=BB[u]**2*x
 return q
def sparse_ce(p,q):return add(*[(-x,log(q[s])) for s,x in enumerate(p) if x])
def seed(g,duplicated):
 n=(len(g)-1).bit_length();w=2*n if duplicated else n
 core=[]
 for s in range(1<<w):
  t=(s&((1<<n)-1))^((s>>n) if duplicated else 0)
  core.append(g[t])
 return tuple((-1 if (s&7).bit_count()%2 else 1)*core[s>>3] for s in range((1<<w)*8))
def full_case(g,duplicated):
 h=seed(g,duplicated);ph=prob(h);pg=prob(g);n=(len(g)-1).bit_length()
 ok(ent(ph)==ent(pg));ok(influence(h)==3+(2 if duplicated else 1)*influence(g))
 for sigma in [-1,1]:
  G=wrapper(h,sigma);p=prob(G);q=coherent(ph)
  ok(all(x in [-1,1] for x in G));ok(sum(q.values())==1);ok(all(q.get(i,F(0))==x for i,x in enumerate(p)))
  ok(influence(G)==F(23,8)+(F(3,4) if duplicated else beta)*influence(g))
  cp=[]
  for bit in [0,1]:
   child=restr(G,4,bit);pchild=prob(child);cp.append(pchild)
   sh=restr(h,0,bit);ps=prob(sh)
   qc=coherent(ps)
   ok(all(qc.get(i,F(0))==x for i,x in enumerate(pchild)));ok(ent(pchild)==ent(p))
   ok(len(set(child))==2)
   # Genuine full normalized target: uniform replacement on all retained core labels.
   nc=(len(sh)-1).bit_length()-2
   qs=[F(0)]*len(sh)
   for s in range(1<<nc):qs[3+4*s]=F(1,1<<nc)
   target=coherent(qs)
   ok(sum(target.values())==1)
   bill=add((1,sparse_ce(pchild,target)),(-1,ent(p)))
   ok(bill==add((beta,kl(ps,qs))))
  cg=fw(G)
  ok(cp[0]==cp[1]);ok(all(not(cg[s]*cg[s^(1<<4)] ) for s in range(len(G)) if not(s&(1<<4))))
def det(a):
 a=[list(row) for row in a];out=F(1)
 for j in range(len(a)):
  k=next(i for i in range(j,len(a)) if a[i][j])
  if k!=j:a[j],a[k]=a[k],a[j];out=-out
  v=a[j][j];out*=v
  for i in range(j+1,len(a)):
   t=a[i][j]/v
   for k in range(j,len(a)):a[i][k]-=t*a[j][k]
 return out
def a032():
 v=truth(1,3);p=prob(v)
 ok(p[0]==F(9,16) and all(x==F(1,16) for x in p[1:]));ok(influence(v)==F(3,4))
 tau=kl(p,prod([F(1,4)]*3));ok(tau=={2:F(2),3:F(-9,8)})
 ok(3**3<2**5 and 3**9>2**14)
 for r in [1,2,3]:
  size=1<<r
  mat=[[F(1,16)**r*9**sum(not(i>>k&1) and not(j>>k&1) for k in range(r)) for j in range(size)] for i in range(size)]
  ok(det(mat)==F(1,32)**(r*2**(r-1)))
 full_case(v,False)
def a096(p):
 supp=[i for i,x in enumerate(p) if x]
 if len(supp)<2:return 0
 event=set(supp[::2]);mu=2*sum(p[i] for i in event)-1;t=F(1,3)
 q=[]
 for sign,ghost in [(1,F(1,8)),(-1,F(1,16))]:
  q.append([x*(1+sign*t*(1 if i in event else -1))/(1+sign*t*mu)*(1-ghost) for i,x in enumerate(p)]+[ghost])
  ok(sum(q[-1])==1)
 Z2=(1-t*t)/(1-t*t*mu*mu)*F(7,8)*F(15,16)
 ok(all(q[0][i]*q[1][i]==p[i]*p[i]*Z2 for i in supp))
 debit=add((F(1,2),ce(list(p)+[F(0)],q[0])),(F(1,2),ce(list(p)+[F(0)],q[1])),(-1,ent(p)))
 ok(debit==add((F(-1,2),log(Z2))))
 ok(0<Z2<1)
 return 1
def run(mode):
 global START
 START=time.perf_counter();pilot=mode=='pilot'
 fixtures=[(n,m) for n in range(3) for m in range(1<<(1<<n))]
 fixtures+= [(3,m) for m in [1,3,7,23,105,126,150,254]]
 if pilot:fixtures=fixtures[:4]+[(2,1)]
 norms=0;post=0;full=0
 for n,m in fixtures:
  g=truth(m,n);p=prob(g);L=len(p)
  full_case(g,True);full+=1
  norms+=a096(p)
  for M in [1,2,3,4]:
   comps=[(prod([F(1+((i+j)%3),4) for i in range(n)]),prod([F(1+((2*i+j+1)%3),4) for i in range(n)])) for j in range(M)]
   mixture_identity(p,comps,[F(1,M)]*M);post+=1
 # Sharp actual Boolean bent2 reference classes.
 g=truth(1,2);p=prob(g);ok(p==tuple([F(1,4)]*4))
 for k in [0,1,2]:
  M=1<<k;comps=[]
  for j in range(M):
   a=prod([F(j>>i&1) if i<k else F(1,2) for i in range(2)])
   comps.append((a,a))
  D=mixture_identity(p,comps,[F(1,M)]*M)
  ok(D=={2:F(2-k)} if k<2 else D=={})
 a032()
 result={'status':'PASS','mode':mode,'assertions':N,'full_boolean_duplicated_cores':full,'posterior_cases':post+3,'geometric_ghost_cases':norms,'both_controller_signs':True,'both_complete_children':True,'runtime_seconds':time.perf_counter()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'integer Walsh, rational probabilities, canonical prime-log rational identities; analytic KL/log-sum nonnegativity','formal_proof':False}
 (ROOT/'out').mkdir(exist_ok=True)
 (ROOT/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':run(sys.argv[1])
