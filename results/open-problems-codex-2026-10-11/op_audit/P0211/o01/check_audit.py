import itertools, math, json, pathlib
from fractions import Fraction as R
from collections import Counter, defaultdict
import numpy as np
import sympy as sp
ROOT=pathlib.Path(__file__).resolve().parent
out={}
n,k,a,b,l,r=sp.symbols('n k a b l r',positive=True)
def cert(birth,death,kill,h,z):
 return sp.factor(birth*(1-h.subs(z,z+1)/h)+death*(1-h.subs(z,z-1)/h)+kill)
h=1/((k+a)*(k+a+1))
upper=2*b*(n-k-1)/(k+a+2)+b+2*k*a/(n*(k+a-1))
single=b*(n-k-1)/(k+a+1)-k*(k-1)/(n*(k+a-1))+b+2*k/n
sector=b*(n-k-l)/(k+a+1)+l*b+(k-1)*((l-1)*k+l*a)/(n*(k+a-1))
stage2=b*(n-r-2)/(r+a+1)+b+r*(a-1)/(n*(r+a-1))
identities=[cert(b*(n-k-1),k*(k-1)/n,b+2*k/n,h,k)-upper,
 cert(b*(n-k-1),k*(k-1)/n,b+2*k/n,1/(k+a),k)-single,
 cert(b*(n-k-l),(k-1)*(k-l)/n,l*b+l*(k-1)/n,1/(k+a),k)-sector,
 cert(b*(n-r-2),r*r/n,b+r/n,1/(r+a),r)-stage2]
assert all(sp.simplify(x)==0 for x in identities)
out['symbolic_certificates']=['upper','count reciprocal','harmonic reciprocal','stage II reciprocal']

def part(S,n):
 cuts=[i for i in range(n) if S>>i&1]
 return tuple(sorted((cuts[(j+1)%len(cuts)]-cuts[j])%n or n for j in range(len(cuts))))
def transitions(p,n,beta):
 ans=defaultdict(R)
 for i in range(len(p)):
  for j in range(i+1,len(p)):
   q=tuple(sorted([p[t] for t in range(len(p)) if t not in (i,j)]+[p[i]+p[j]]))
   ans[q]+=R(2,n)
 for i,v in enumerate(p):
  for cut in range(1,v):
   q=tuple(sorted(list(p[:i]+p[i+1:])+[cut,v-cut]))
   ans[q]+=beta
 return ans
exact=[]
for N in range(2,10):
 beta=R(3,7)
 groups=defaultdict(list)
 for S in range(1,1<<N): groups[part(S,N)].append(S)
 for p,sets in groups.items():
  counts=Counter(p)
  assert len(sets)==R(N*math.factorial(len(p)-1),math.prod(math.factorial(v) for v in counts.values()))
  avg=defaultdict(R)
  for S in sets:
   K=S.bit_count()
   for i in range(N):
    if S>>i&1:
     if K==1: continue
     T=S^(1<<i); rate=R(K-1,N)
    else: T=S|(1<<i); rate=beta
    avg[part(T,N)]+=rate/len(sets)
  assert dict(avg)==dict(transitions(p,N,beta))
  for q,rate in transitions(p,N,beta).items():
   w=lambda p: (beta*N)**len(p)/math.prod(math.factorial(v) for v in Counter(p).values())
   assert w(p)*rate==w(q)*transitions(q,N,beta)[p]
 exact.append({'n':N,'partitions':len(groups),'subsets':(1<<N)-1})
out['exact_projection_and_detailed_balance']=exact

def bd(lo,hi,birth,death,kill):
 ks=list(range(lo,hi+1)); A=np.zeros((len(ks),len(ks)))
 for i,z in enumerate(ks):
  u,d,v=birth(z),death(z),kill(z)
  A[i,i]=u+d+v
  if i+1<len(ks): A[i,i+1]=-u
  if i>0: A[i,i-1]=-d
 return A
def sym(A):
 # Reversible similarity: offdiagonal is minus geometric mean of reverse rates.
 B=np.diag(np.diag(A))
 for i in range(len(A)):
  for j in range(i): B[i,j]=B[j,i]=-math.sqrt(max(0,A[i,j]*A[j,i]))
 return B
spectra=[]
for N in range(2,9):
 for beta in [1e-7,1/N,0.0625,2,1e3]:
  states=list(range(1,1<<N)); idx={S:i for i,S in enumerate(states)}
  A=np.zeros((len(states),len(states)))
  for S in states:
   K=S.bit_count(); row=idx[S]
   for i in range(N):
    T=S^(1<<i)
    if not T: continue
    rate=(K-1)/N if S>>i&1 else beta
    A[row,idx[T]]=-rate; A[row,row]+=rate
  ev=np.linalg.eigvalsh(sym(A))
  radial=list(np.linalg.eigvalsh(sym(bd(1,N,lambda k:beta*(N-k),lambda k:k*(k-1)/N,lambda k:0))))
  for L in range(1,N//2+1):
   Ar=bd(L,N-L,lambda k:beta*(N-k-L),lambda k:(k-1)*(k-L)/N,lambda k:L*beta+L*(k-1)/N)
   radial.extend(list(np.linalg.eigvalsh(sym(Ar)))*(math.comb(N,L)-math.comb(N,L-1)))
  error=float(np.max(np.abs(ev-np.sort(radial))))
  assert error<1e-8
  # Independent polymer generator, not a sector-spectrum surrogate.
  parts=sorted(set(part(S,N) for S in states)); ix={p:i for i,p in enumerate(parts)}
  M=np.zeros((len(parts),len(parts)))
  for p in parts:
   for q,rate in transitions(p,N,beta).items():
    M[ix[p],ix[q]]-=float(rate); M[ix[p],ix[p]]+=float(rate)
  gap=float(np.linalg.eigvalsh(sym(M))[1]); s=beta+math.sqrt(beta)+1/N
  assert gap>=s/6-1e-9 and gap<=4*s+1e-9 and gap>=beta+2/N-1e-9
  spectra.append({'n':N,'beta':beta,'gap_M':gap,'sector_error':error})
out['spectra']=spectra

# Exact up/down commutator and harmonic dimensions, including the middle layer.
for N in range(2,9):
 layers=[[S for S in range(1<<N) if S.bit_count()==j] for j in range(N+1)]
 Us=[]
 for j in range(N):
  Us.append(sp.Matrix([[int((S&T)==S) for S in layers[j]] for T in layers[j+1]]))
 for j in range(N+1):
  size=len(layers[j]); zero=sp.zeros(size)
  DU=Us[j].T*Us[j] if j<N else zero
  UD=Us[j-1]*Us[j-1].T if j>0 else zero
  assert DU-UD==(N-2*j)*sp.eye(size)
 for L in range(1,N//2+1):
  assert len(layers[L])-Us[L-1].T.rank()==math.comb(N,L)-math.comb(N,L-1)
out['exact_boolean_algebra']='commutators and harmonic dimensions for n=2..8'

# Rational grid: beta=(a/n)^2 avoids floating point in all certificate inequalities.
minimum=R(100)
points=0
for N in [8,9,16,31,64,100,251]:
 for t in range(9):
  aa=R(2)+R(t,8)*(R(N,4)-2); bb=(aa/N)**2
  for K in range(1,N):
   c=single.subs({n:N,k:K,a:aa,b:bb})
   assert c>=aa/(5*N)
  for L in range(1,N//2+1):
   for K in range(L,N-L+1):
    # Evaluate exact certificate independently of sympy substitution for speed.
    c=bb*(N-K-L)/(K+aa+1)+L*bb+R(K-1,N)*((L-1)*K+L*aa)/(K+aa-1)
    assert c>=aa/(5*N)
    minimum=min(minimum,c/(aa/N)); points+=1
  for rr in range(N-1):
   c=bb*(N-rr-2)/(rr+aa+1)+bb+R(rr,N)*(aa-1)/(rr+aa-1)
   assert c>=aa/(5*N)
out['rational_certificate_grid']={'points':points,'minimum_sector_ratio':float(minimum)}
(ROOT/'check_results.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({key:(len(val) if isinstance(val,list) else val) for key,val in out.items()},indent=2))
