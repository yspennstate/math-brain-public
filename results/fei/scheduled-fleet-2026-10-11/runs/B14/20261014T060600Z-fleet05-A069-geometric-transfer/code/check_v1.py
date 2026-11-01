from pathlib import Path
from fractions import Fraction as R
import itertools,json,time,hashlib
RUN=Path(__file__).resolve().parents[1]
start=time.perf_counter();cases=checks=0
def ck(x):
 global checks
 checks+=1
 assert x,(cases,checks)
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for b in range(0,len(a),2*h):
   for j in range(b,b+h):
    x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
  h*=2
 return a
def inf(a):
 N=len(a);n=(N-1).bit_length()
 return [R(sum(a[j]!=a[j^(1<<i)] for j in range(N)),N) for i in range(n)]
def tab(j,k):return [1 if (j>>x)&1 else -1 for x in range(1<<k)]
weights=[R(1,4),R(1,4),R(1,16),R(7,20),R(7,80)]
def cells(m):
 return [[1],[2],[3],[d for d in range(1<<(m+2)) if d>>2 and not d&2],[d for d in range(1<<(m+2)) if d>>2 and d&2]]
for m in (1,2,3,5):
 cs=cells(m);ck(sum(weights)==1)
 ck(sorted(d for cell in cs for d in cell)==list(range(1,1<<(m+2))))
 for j,cell in enumerate(cs):
  if j>=3:
   exponent=2*sum(d.bit_count() for d in cell)-2*(j-3)*len(cell)
   ck(len(cell)**len(cell)<=2**exponent)
ck(20**5<2**8*7**5)
def fixture(m,k,hs,cstar=0,ustar=0,active=True):
 global cases
 d=m+2;D=1<<d;N=1<<(d+k);cs=cells(m)
 G=[hs[x&3][x>>d] for x in range(N)]
 q1=[-1 if (x&1)==cstar and ((x>>1)&1)==ustar else 1 for x in range(N)]
 q2=[-1 if active and (x&1)==cstar and ((x>>2)&((1<<m)-1))==0 else 1 for x in range(N)]
 source=[a*b for a,b in zip(G,q1)];mask=[a*b for a,b in zip(q1,q2)]
 F=[a*b for a,b in zip(source,mask)]
 ck(F==[a*b for a,b in zip(G,q2)])
 z=fw(F);zg=fw(source);ii=inf(F)
 corez=[fw(h) for h in hs]
 marginal=[]
 for t in range(1<<k):
  row=[z[s|(t<<d)]**2 for s in range(D)]
  marginal.append(sum(row))
  ck(sum(row)==sum(zg[s|(t<<d)]**2 for s in range(D)))
  ck(R(sum(row),N*N)==sum(R(a[t]**2,1<<(2*k)) for a in corez)/4)
  for cell in cs:
   ck(len({row[s] for s in cell})==1)
 tail=sum(v*v for j,v in enumerate(z) if j&(D-1))
 alpha=R(tail,N*N);tailZ=R(sum(v*v for j,v in enumerate(z) if (j&(D-1))>>2),N*N)
 ck(alpha<=sum(ii[:d]));ck(tailZ<=sum(ii[2:d]))
 RD=[R(0)]*D;RD[0]=1-alpha
 for w,cell in zip(weights,cs):
  for s in cell:RD[s]=alpha*w/len(cell)
 ck(sum(RD)==1)
 ck(all(RD[j&(D-1)]>0 for j,v in enumerate(z) if v))
 # Uniform supplied core reference is positive and normalized. Product Q is
 # identical across rows; actual core cross entropy is k, fully retained.
 ck(sum(RD[s]*R(1,1<<k) for t in range(1<<k) for s in range(D))==1)
 ck(sum(marginal)==N*N)
 for a in range(k):ck(ii[d+a]==sum(inf(h)[a] for h in hs)/4)
 # Exact c-phase and nonempty-Z factorization, independent of author code.
 hrow=fw([hs[cstar|(u<<1)][y] for y in range(1<<k) for u in (0,1)])
 for T in range(1<<k):
  for u in (0,1):
   for cell in cs[3+u:4+u]:
    for s in cell:
     expected=0 if not active else -(1<<(k+1))*hrow[u|(T<<1)]*(1 if not(s&1) or cstar==0 else -1)
     ck(z[s|(T<<d)]==expected)
 cases+=1
 if time.perf_counter()-start>55:
  (RUN/'out/PARTIAL.json').write_text(json.dumps({'status':'WALL_GUARD','completed_cases':cases,'checks':checks}))
  raise RuntimeError('frozen55s guard')
 return F,source,mask,ii
for k in (1,2):
 quadruples=list(itertools.product(range(4),repeat=4)) if k==1 else [(j%16,j//16,(5*j+3)%16,(7*j+1)%16) for j in range(256)]
 for m,cstar,ustar in itertools.product((1,2,3),(0,1),(0,1)):
  for codes in quadruples:fixture(m,k,[tab(code,k) for code in codes],cstar,ustar)
for codes in itertools.product(range(4),repeat=4):fixture(1,1,[tab(code,1) for code in codes],active=False)
# Exposed canceled-event family, nonconstant retained point core.
t=5;h=[-1 if y==0 else 1 for y in range(1<<t)]
F,g,q,ii=fixture(t,t,[h]*4)
Ig,Iq,If=sum(inf(g)),sum(inf(q)),sum(ii);delta=R(1,1<<t)
ck((Ig,Iq,If)==(1+2*t*delta,1+t*delta,(3*t+1)*delta))
ck(7*Ig+12*Iq>26*If)
exposed={'I_source':str(Ig),'I_mask':str(Iq),'I_final':str(If),'ancestral_ratio':str((7*Ig+12*Iq)/If)}
# Fully canceled output: retain actual y, alpha=0.
F,g,q,ii=fixture(1,1,[[-1,1]]*4,active=False);ck(sum(ii[:3])==0 and sum(ii[3:])==1)
# Nonfactorizing four core branches and one complete normalized core reference.
maj=[1 if y.bit_count()>=2 else -1 for y in range(8)];lit=[1 if y&1 else -1 for y in range(8)]
hs=[maj,lit,[-a for a in lit],[-a for a in maj]]
fixture(3,3,hs)
L=[1 if s==0 else 3 if s==1 else 5 for s in range(8)]
normalizer=sum(R(1,1<<ell) for ell in L);ck(normalizer==R(13,16))
for h in hs:
 zz=fw(h);gamma=sum(R(a*a,64)*ell for a,ell in zip(zz,L));ck(gamma==3*sum(inf(h)))
spec=json.loads((RUN/'FROZEN_SPEC.json').read_text());ck(cases==spec['case_count'])
result={'status':'PASS','cases':cases,'exact_assertions':checks,'elapsed_seconds':time.perf_counter()-start,'memory_estimate_MB':64,'arithmetic':'integer Walsh and Fraction; no entropy float comparisons','exposed_witness':exposed,'nonfactorizing_core_K':3,'coefficient_certificate':'20^5 < 2^8*7^5','spec_sha256':hashlib.sha256((RUN/'FROZEN_SPEC.json').read_bytes()).hexdigest()}
(RUN/'out').mkdir(exist_ok=True);(RUN/'out/CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
