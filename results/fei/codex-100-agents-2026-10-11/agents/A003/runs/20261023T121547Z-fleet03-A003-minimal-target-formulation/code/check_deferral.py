"""Independent integer-Walsh certificate; frozen specification saved before execution."""
import json,time,sys,hashlib
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
started=time.monotonic(); limit=55; checks=nodes=edges=leaves=0
def ck(x):
 global checks
 checks+=1
 assert x
 if checks%1000==0 and time.monotonic()-started>limit: raise RuntimeError('55-second frozen runtime exceeded')
def walsh(v):
 a=list(v); k=1
 while k<len(a):
  for s in range(0,len(a),2*k):
   for j in range(s,s+k): a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return a
def inf(a,j): return F(sum(x*x for t,x in enumerate(a) if (t>>j)&1),len(a)**2)
def entropy_law(a): return sorted(F(x*x,len(a)**2) for x in a if x)
def lift(core,n,L):
 vals=[]
 for z in range(1<<(n*L)):
  y=sum((((z>>(j*L))&((1<<L)-1)).bit_count()%2)<<j for j in range(n))
  vals.append(core[y])
 return vals
def child(v,j,b):
 return [v[(t&((1<<j)-1))|((t>>j)<<(j+1))|(b<<j)] for t in range(len(v)//2)]
def visit(v,labels,baseinf,baselaw,L):
 global nodes,edges,leaves
 nodes+=1; a=walsh(v); sizes=[labels.count(j) for j in range(len(baseinf))]
 ck(entropy_law(a)==baselaw)
 ck(sum(inf(a,j) for j in range(len(labels)))==sum(sizes[j]*baseinf[j] for j in range(len(baseinf))))
 choices=[k for k,j in enumerate(labels) if sizes[j]>1]
 if not choices:
  leaves+=1; ck(len(labels)==len(baseinf)); return
 # Fixed block order, both outcomes exhaust the complete stopping tree.
 j=choices[0]; label=labels[j]; aa=[]
 for b in (0,1):
  vb=child(v,j,b); ac=walsh(vb); aa.append(ac)
  for t,x in enumerate(ac):
   lo=(t&((1<<j)-1))|((t>>j)<<(j+1)); hi=lo|(1<<j)
   ck(a[lo]*a[hi]==0)
   ck(F(x*x,len(ac)**2)==F(a[lo]**2+a[hi]**2,len(a)**2))
  visit(vb,labels[:j]+labels[j+1:],baseinf,baselaw,L)
 edges+=1; ck(inf(a,j)==baseinf[label]); ck(a[1<<j]==0)
 parentI=sum(inf(a,k) for k in range(len(labels)))
 meanI=sum(sum(inf(ac,k) for k in range(len(labels)-1)) for ac in aa)/2
 ck(parentI-meanI==baseinf[label])
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
ns=range(3) if mode=='pilot' else range(4)
tables=0
for n in ns:
 for mask in range(1<<(1<<n)):
  core=[1-2*((mask>>t)&1) for t in range(1<<n)]; ca=walsh(core)
  bi=[inf(ca,j) for j in range(n)]; bl=entropy_law(ca)
  for L in (2,3):
   tables+=1; v=lift(core,n,L); visit(v,[j for j in range(n) for _ in range(L)],bi,bl,L)
result={'status':'PASS','mode':mode,'assertions':checks,'lifted_tables':tables,'nodes':nodes,'query_nodes':edges,'terminal_nodes':leaves,'elapsed_seconds':time.monotonic()-started,'arithmetic':'integer Walsh and Fraction; entropy equality via identical exact positive probability multisets','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
