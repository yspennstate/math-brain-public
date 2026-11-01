"""Maximum-weight upper sets using the Boolean order polytope (integral vertices)."""
import itertools,json,time,pathlib
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
ROOT=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(360012)
def perms(n):return list(itertools.permutations(range(n)))
def comp(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):return tuple(a.index(i) for i in range(len(a)))
def group(name):
 if name=='S3':return perms(3),comp,inverse
 if name=='D4':
  els=list(itertools.product(range(4),range(2)))
  def mul(a,b):return ((a[0]+(-1)**a[1]*b[0])%4,(a[1]+b[1])%2)
  def inv(a):return ((-(-1)**a[1]*a[0])%4,a[1])
  return els,mul,inv
 if name=='C6':return list(range(6)),lambda a,b:(a+b)%6,lambda a:-a%6
 raise ValueError(name)
def setup(n):
 rows=[];cols=[];data=[];r=0
 for s in range(1<<n):
  for i in range(n):
   if not(s>>i&1):rows.extend([r,r]);cols.extend([s,s|(1<<i)]);data.extend([1.,-1.]);r+=1
 return coo_matrix((data,(rows,cols)),shape=(r,1<<n)).tocsr()
def law(Q):
 n=len(Q);d=np.empty(1<<n)
 for s in range(1<<n):
  ix=[i for i in range(n) if s>>i&1];d[s]=np.linalg.det(Q[np.ix_(ix,ix)]).real if ix else 1.
 # Inclusion probabilities -> exact-set probabilities by Boolean Mobius inversion.
 for i in range(n):
  for s in range(1<<n):
   if not(s>>i&1):d[s]-=d[s|(1<<i)]
 return d
def check(Q,A):
 n=len(Q);ev=np.linalg.eigvalsh(Q);p=float(np.exp(np.log(ev).mean()));mu=law(Q)
 nu=np.array([p**s.bit_count()*(1-p)**(n-s.bit_count()) for s in range(1<<n)])
 c=mu-nu;lp=linprog(c,A_ub=A,b_ub=np.zeros(A.shape[0]),bounds=(0,1),method='highs')
 if not lp.success:raise RuntimeError(lp.message)
 witness=[s for s,v in enumerate(lp.x) if v>.5];delta=float(c[ witness ].sum())
 return {'density':p,'minimum_upper_set_gap':float(lp.fun),'rounded_gap':delta,'witness':witness,'normalization_error':float(abs(mu.sum()-1)),'minimum_atom':float(mu.min()),'eigenvalues':ev.tolist()}
records=[];t=time.monotonic()
for name,N in [('C6',30),('S3',100),('D4',60)]:
 els,mul,inv=group(name);n=len(els);A=setup(n)
 for trial in range(N):
  raw=rng.normal(size=n)+1j*rng.normal(size=n);index={g:i for i,g in enumerate(els)}
  B=np.array([[raw[index[mul(inv(g),h)]] for h in els] for g in els]);H=(B+B.conj().T)/2
  e,U=np.linalg.eigh(H);z=(e-e.min())/(e.max()-e.min())
  if trial%3==0:z=.001+.998*z
  elif trial%3==1:z=.05+.9*z
  else:z=.15+.7*z
  Q=(U*z)@U.conj().T
  a=check(Q,A);b=check(np.eye(n)-Q,A)
  rec={'group':name,'trial':trial,'lower':a,'complement_lower':b}
  records.append(rec)
  if min(a['rounded_gap'],b['rounded_gap']) < -1e-8:
   rec['Q_real']=Q.real.tolist();rec['Q_imag']=Q.imag.tolist();print('COUNTEREXAMPLE_CANDIDATE',json.dumps(rec));break
 ROOT.joinpath('finite_results.json').write_text(json.dumps(records,indent=2),encoding='utf8')
 print(name,'trials',N,'seconds',time.monotonic()-t,'worst_gap',min(min(r['lower']['rounded_gap'],r['complement_lower']['rounded_gap']) for r in records),flush=True)
print('total kernels',len(records),'comparisons',2*len(records))
