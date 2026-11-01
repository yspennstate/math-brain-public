import math,json,hashlib

def walsh(vals):
 a=list(map(float,vals)); N=len(a); h=1
 while h<N:
  for i in range(0,N,2*h):
   for j in range(i,i+h):
    x,y=a[j],a[j+h]; a[j]=x+y; a[j+h]=x-y
  h*=2
 return [x/N for x in a]
def mu(vals): return [x*x for x in walsh(vals)]
def pc(x): return x.bit_count()
def M(vals,z): return sum(w*z**pc(s) for s,w in enumerate(mu(vals)))
def P(vals,z):
 return sum(pc(s)*w for s,w in enumerate(mu(vals))) if z==1 else (1-M(vals,z))/(1-z)
def inf(vals,i): return sum(w for s,w in enumerate(mu(vals)) if (s>>i)&1)
def act(vals,i,z): return sum(w*z**(pc(s)-1) for s,w in enumerate(mu(vals)) if (s>>i)&1)
def restrict(vals,fixed):
 n=(len(vals)).bit_length()-1; free=[i for i in range(n) if i not in fixed]; out=[]
 for y in range(1<<len(free)):
  x=0
  for i,b in fixed.items(): x|=b<<i
  for k,i in enumerate(free): x|=((y>>k)&1)<<i
  out.append(vals[x])
 return out
def bdrop(vals,A,z):
 av=0.0
 for y in range(1<<len(A)):
  fixed={i:(y>>k)&1 for k,i in enumerate(sorted(A))}
  av+=P(restrict(vals,fixed),z)/(1<<len(A))
 return P(vals,z)-av
def bformula(vals,A,z):
 mask=sum(1<<i for i in A); out=0.0
 for s,w in enumerate(mu(vals)):
  a=pc(s&mask); b=pc(s&~mask)
  if a:
   phi=(1-z**a)/(1-z)
   out+=w*z**b*phi
 return out
def bern(vals,t,z):
 n=(len(vals)).bit_length()-1; out=0
 for mask in range(1<<n):
  A={i for i in range(n) if mask>>i&1}; k=pc(mask)
  out+=t**k*(1-t)**(n-k)*bdrop(vals,A,z)
 return out
def bern_formula(vals,t,z): return (M(vals,z+t*(1-z))-M(vals,z))/(1-z)
def tree(vals,w=1.0):
 n=(len(vals)).bit_length()-1
 if n==0:return 0.0
 z=1-1/n
 return w*act(vals,0,z)+tree(restrict(vals,{0:0}),w/2)+tree(restrict(vals,{0:1}),w/2)
def parity(n): return [1 if pc(x)%2==0 else -1 for x in range(1<<n)]
def aand(n): return [1 if x==(1<<n)-1 else -1 for x in range(1<<n)]
def maj(n): return [1 if pc(x)>n//2 else -1 for x in range(1<<n)]
maxbe=maxbr=maxv=0.0; minrat=9.0; cases=0
for n in range(1,5):
 fs=[parity(n),aand(n),[1 if ((x*1103515245+12345)&7)<4 else -1 for x in range(1<<n)]]
 if n%2: fs.append(maj(n))
 for vals in fs:
  z=.37
  for mask in range(1<<n):
   A={i for i in range(n) if mask>>i&1}; maxbe=max(maxbe,abs(bdrop(vals,A,z)-bformula(vals,A,z))); cases+=1
  for t in [.2,.5,.73]: maxbr=max(maxbr,abs(bern(vals,t,z)-bern_formula(vals,t,z)))
  zd=1-1/n; root=P(vals,zd); maxv=max(maxv,tree(vals)-root)
  for i in range(n):
   p=inf(vals,i)
   if p>1e-14:minrat=min(minrat,act(vals,i,zd)/p)
tab=[]
for m in [1,2,3,5,10,20,50,100,1000]:
 z=1-1/(3*m); Mg=.75*z+.25*z**3; rr=.5*(1+z*z)*Mg**(m-1); tab.append([m,z,rr])
out={'block_cases':cases,'max_block_identity_abs_error':maxbe,'max_bernoulli_identity_abs_error':maxbr,'max_adaptive_tree_spent_minus_root':maxv,'min_activation_ratio':minrat,'majority3_table':tab,'majority3_limit':math.exp(-.5)}
print(json.dumps(out,indent=2))
