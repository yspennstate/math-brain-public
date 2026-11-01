"""Independent coefficient and whole-tree check; imports no check.py or producer."""
from fractions import Fraction
from pathlib import Path
import json,time
F=Fraction
start=time.monotonic();checks=nodes=trees=empty_leaves=0
def test(a):
 global checks
 checks+=1
 assert a
 if checks%1000==0 and time.monotonic()-start>55:raise TimeoutError('55s')
def transform(values):
 a=[F(x,len(values)) for x in values];step=1
 while step<len(a):
  for base in range(0,len(a),2*step):
   for k in range(step):
    u,v=a[base+k],a[base+k+step];a[base+k]=u+v;a[base+k+step]=u-v
  step*=2
 return a
def project(j,i):
 return sum(1<<k for k,pos in enumerate(x for x in range(j.bit_length()+1) if x!=i) if j>>pos&1)
def visit(v,j,order,depth=0,stop=None):
 global nodes,empty_leaves
 nodes+=1;n=len(v).bit_length()-1;p=[x*x for x in transform(v)];a=1-p[j]
 B=(n-1)*a if j else F(0)
 if not order or (stop is not None and depth==stop):
  empty_leaves+=j==0
  test(sum(p)==1)
  # The atom partition has <=2^n other atoms, including n=0 and a=0.
  test(sum(t>0 for k,t in enumerate(p) if k!=j)<=2**n)
  return a,B,F(0)
 i=order[0];jc=project(j,i);next_order=[k-(k>i) for k in order[1:]]
 child=[]
 for y in range(2):
  vv=[z for k,z in enumerate(v) if (k//(1<<i))%2==y]
  child.append(visit(vv,jc,next_order,depth+1,stop))
 ac=sum(t[0] for t in child)/2;bt=sum(t[1] for t in child)/2;spent=sum(t[2] for t in child)/2
 cp=[1-transform([z for k,z in enumerate(v) if (k//(1<<i))%2==y])[jc]**2 for y in range(2)]
 test(sum(cp)/2==a-p[j^(1<<i)])
 test(ac<=a)
 # Upper charge used in the proof: a_child only until anchor absorption.
 local=sum(cp)/2 if jc else F(0)
 if not j:local=F(0)
 test(local+spent<=B-bt)
 return ac,bt,local+spent
for n in range(1,4):
 for code in range(1<<(1<<n)):
  v=[2*((code>>x)&1)-1 for x in range(1<<n)]
  for j in range(1,1<<n):
   anchor=[i for i in range(n) if j>>i&1];outside=[i for i in range(n) if not j>>i&1]
   for order,stop in [(anchor+outside,None),(outside+anchor,None),(list(range(n)),1)]:
    visit(v,j,order,stop=stop);trees+=1
# Exact majority coefficient and essential-coordinate obstruction, fixed small domain.
major=[]
for m in range(1,5):
 n=2*m+1;v=[1 if x.bit_count()<=m else -1 for x in range(1<<n)]
 a=transform(v);c=F(__import__('math').comb(2*m,m),4**m)
 test(a[0]==0);test(all(abs(x)<=c for x in a));test(c*c<=F(1,m+1))
 I=sum(F(s.bit_count())*x*x for s,x in enumerate(a));test(I==n*c)
 major.append({'n':n,'influence':str(I),'optimized_bank_over_I':str(n*(1-max(x*x for x in a[1:]))/I)})
# All-N algebraic boundary certificates without floating logs.
test(6**15<16*5**15)
for N in range(10,101):
 # At N10 the rational envelope equals 1/64; strictness comes from ell<4/15.
 test(F(6*N,2**N)*F(4,15)<=F(1,64))
 test(F(12*(3*N+2),2**N)<=F(3,8))
 test(F(N+1,2*N)<=1)
test(F(741,256)-F(1,64)>F(61,32));test(F(61,32)-F(1,4)==F(53,32))
result={'status':'PASS','trees':trees,'nodes':nodes,'assertions':checks,'empty_anchor_leaves':empty_leaves,'majority':major,'elapsed_seconds':time.monotonic()-start,'scope':'Independent FWHT moving-anchor bank telescopes and finite boundary cases; analytic source application is conditional on A036 original-source bounds'}
p=Path(__file__).resolve().parents[1]/'out/AUDIT.json';p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
