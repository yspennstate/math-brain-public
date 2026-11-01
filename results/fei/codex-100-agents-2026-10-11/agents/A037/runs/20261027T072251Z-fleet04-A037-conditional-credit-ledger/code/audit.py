from pathlib import Path
from fractions import Fraction as Q
import time,json
start=time.monotonic();tests=0;nodes=0
root=Path(__file__).resolve().parents[1]
def test(b):
 global tests
 tests+=1
 assert b
 if time.monotonic()-start>55:raise TimeoutError('55s spec limit')
def walsh(f):
 a=list(f);step=1
 while step<len(a):
  for j in range(0,len(a),2*step):
   for k in range(j,j+step):a[k],a[k+step]=a[k]+a[k+step],a[k]-a[k+step]
  step*=2
 return [Q(v*v,len(a)**2) for v in a]
def expkl(p,q,mult):
 a=Q(1)
 for x,y in zip(p,q):
  if x:
   test(y>0);e=x*mult;test(e.denominator==1);a*=(x/y)**int(e)
 return a
def vacuum(p,q):
 if p[0]==1:return list(p)
 return [p[0]]+[(1-p[0])*x/(1-q[0]) for x in q[1:]]
def walk(f,q,den,reach=Q(1),depth=0):
 global nodes
 nodes+=1;p=walsh(f);qc=vacuum(p,q)
 release=expkl([p[0],1-p[0]],[q[0],1-q[0]],den*reach)
 test(expkl(p,q,den*reach)==release*expkl(p,qc,den*reach))
 if len(f)==1:return release*expkl(p,qc,den*reach)
 n=len(f).bit_length()-1;i=(n-1 if depth%2==0 else 0)
 def ins(s,b):return (s&((1<<i)-1))|((s>>i)<<(i+1))|(b<<i)
 m=len(f)//2
 children=[[f[ins(s,b)] for s in range(m)] for b in [0,1]]
 pc=[walsh(g) for g in children]
 R=[p[ins(s,0)]+p[ins(s,1)] for s in range(m)]
 Z=[qc[ins(s,0)]+qc[ins(s,1)] for s in range(m)]
 test(all(R[s]==(pc[0][s]+pc[1][s])/2 for s in range(m)))
 # Source-zero rows are sent deterministically by parity of history depth.
 joint=[[Z[s]*pc[b][s]/(2*R[s]) if R[s] else Z[s]*int(b==depth%2) for s in range(m)] for b in [0,1]]
 r=[sum(x) for x in joint];test(min(r)>0 and sum(r)==1)
 cq=[[x/r[b] for x in joint[b]] for b in [0,1]]
 erasure=expkl(p,qc,den*reach)/expkl(R,Z,den*reach)
 outcome=expkl([Q(1,2)]*2,r,den*reach)
 total=release*erasure*outcome
 for b in [0,1]:total*=walk(children[b],cq[b],den,reach/2,depth+1)
 test(total==expkl(p,q,den*reach))
 return total
trees=0
for n in [1,2,3]:
 N=1<<n
 for table in range(1<<N):
  f=[1-2*((table>>x)&1) for x in range(N)];p=walsh(f)
  for a in [0,N-1]:
   q=[x/3+Q(1,3*N)+Q(int(s==a),3) for s,x in enumerate(p)]
   walk(f,q,N*N);trees+=1
# Different representation of the new local counterexample sign over a rational grid.
positive=[]
for j in range(1,64):
 z=Q(1,2)-Q(j,128);t=Q(1,4)
 r=(1+t-2*z)/(2*(1-z))
 growth=(Q(1,4)/(r*(1-r)))**2/((t/z)*((1-t)/(1-z))**3)
 if growth>1:positive.append(j)
test(1 in positive)
result={'status':'PASS','trees':trees,'nodes':nodes,'assertions':tests,'positive_epsilon_numerators_over_128':positive,'runtime_seconds':time.monotonic()-start,'arithmetic':'rational products exp2(4^n * weighted KL), no imported peer/main helper'}
(root/'out/AUDIT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
