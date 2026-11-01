from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time,hashlib
R=Path(__file__).resolve().parents[1]; O=R/'out';O.mkdir(exist_ok=True)
spec={'helper_version':'A082-stage22-v2','family':'Actual products of disjoint AND2 signs; finite cardinality reference laws', 'domain':'even n=2..32 root certificates; Boolean FWHT n=2,4,6; compression n=2..8 at x=1/4,1/2,3/4,2, all deletion sizes; two actual AND2 physical children', 'case_count':'16 roots, 3 actual Boolean tables, 168 compression/deletion profiles, two physical children', 'symmetry':'Cardinality permutation symmetry proved algebraically; FWHT uses all labelled inputs', 'arithmetic':'integers and Fraction only; 64 rational bisections, no floating signs','memory_estimate_mb':70,'max_runtime_seconds':55,'pilot':'v1 whole-domain PASS483; v2 corrects advertised profile count140 to168 and adds physical-branch negative control; no escalation'}
(O/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
t0=time.monotonic(); checks=0
def ck(b):
 global checks
 assert b
 checks+=1
def z(n,x):return (1+x)**n-1+2**n*x**n
def poly(n,x):
 m=2**n
 return sum(F(comb(n,j)*(m+1 if j==n else 1)*(2*(m-1)*j-n*m))*x**(j-1) for j in range(1,n+1))
def direct(n,x):
 m=2**n
 return 2*(m-1)*x*(n*(1+x)**(n-1)+m*n*x**(n-1))-n*m*z(n,x)
roots=[]
for n in range(2,33,2):
 m=2**n
 for x in [F(1,m+1),F(1,2),F(1)]:ck(poly(n,x)*x==direct(n,x))
 if n==2:
  ck(poly(n,F(1,5))==0);roots.append({'n':n,'exact_root':'1/5','minimum_atom_witnesses':0});continue
 ck(poly(n,F(1,2))<0<poly(n,F(1)))
 signs=[2*(m-1)*j-n*m for j in range(1,n+1)]
 ck(all(s<0 for s in signs[:n//2]) and all(s>0 for s in signs[n//2:]))
 lo,hi=F(1,2),F(1)
 for _ in range(64):
  mid=(lo+hi)/2
  if poly(n,mid)<0:lo=mid
  else:hi=mid
 ck(poly(n,lo)<0<=poly(n,hi));ck(lo>F(1,m+1))
 roots.append({'n':n,'root_interval':[str(lo),str(hi)],'minimum_atom_witnesses':m-n,'sign_change_index':n//2+1})
# Independent actual Boolean construction; no assumed spectrum.
for n in [2,4,6]:
 a=[-1 if sum(((v>>(2*j))&3)==3 for j in range(n//2))%2 else 1 for v in range(2**n)]
 stride=1
 while stride<len(a):
  for i in range(0,len(a),2*stride):
   for j in range(i,i+stride):a[j],a[j+stride]=a[j]+a[j+stride],a[j]-a[j+stride]
  stride*=2
 ck(all(v*v==2**n for v in a))
 p=[F(v*v,4**n) for v in a]
 ck(sum(p)==1);ck(sum(p[s]*s.bit_count() for s in range(2**n))==F(n,2))
profiles=0
for n in range(2,9):
 m=2**n
 for x in [F(1,4),F(1,2),F(3,4),F(2)]:
  zz=z(n,x);a=F(1,m);b=F(m-1,m)*((1+x)**n-1)/zz;c=F(m-1)*x**n/zz
  ck(a+b+c==1 and min(a,b,c)>0)
  u=[a if s==0 else F(m-1,m)*(m+1 if s==m-1 else 1)*x**s.bit_count()/zz for s in range(m)]
  ck(sum(u)==1)
  for k in range(n+1):
   d=n-k;profiles+=1
   marg=[F(0)]*(2**d)
   for s in range(m):marg[s & (2**d-1)]+=u[s]
   if d==0:ck(marg==[F(1)]);continue
   den=(1+x)**n-1
   al=((1+x)**k-1)/den
   be=(1+x)**k*((1+x)**d-1)/den
   ck(al+be==1 and al>=0 and be>0)
   pred=[a+b*al if s==0 else b*be*x**s.bit_count()/((1+x)**d-1)+(c if s==2**d-1 else 0) for s in range(2**d)]
   ck(marg==pred)
# Boundary: n=2 exact root makes the calibrated law exactly uniform.
n=2;x=F(1,5);zz=z(n,x)
ck([F(1,4)]+[F(3,4)*(5 if s==3 else 1)*x**s.bit_count()/zz for s in range(1,4)]==[F(1,4)]*4)
# Actual AND2: coordinate deletion is not a branch spectrum.
for bit in [0,1]:
 truth=[-1 if (bit==1 and y==1) else 1 for y in [0,1]]
 child=[F((truth[0]+truth[1])**2,4),F((truth[0]-truth[1])**2,4)]
 ck(child==([F(1),F(0)] if bit==0 else [F(0),F(1)]))
 ck(child!=[F(1,2),F(1,2)])
out={'status':'PASS','assertions':checks,'root_cases':len(roots),'compression_profiles':profiles,'roots':roots,'elapsed_seconds':time.monotonic()-t0,'arithmetic':'exact Fraction/integer, no floating conclusions','formal_status':'not Lean checked; independent review of new compression pending'}
(O/'CERTIFICATE.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='roots'}))
