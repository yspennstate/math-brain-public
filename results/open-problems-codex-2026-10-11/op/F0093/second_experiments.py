import numpy as np,json,time,math
from pathlib import Path
from itertools import permutations
EPS=.25
out=Path('second_experiments.jsonl');out.write_text('',encoding='utf8')
def entropy(P):
 z=P[P>0];return float(-(z*np.log(z)).sum())
def kl(P,Q):
 z=P>0
 assert np.all(Q[z]>0)
 return float((P[z]*np.log(P[z]/Q[z])).sum())
def save(row):
 with out.open('a',encoding='utf8') as f:f.write(json.dumps(row)+'\n')
 print(row,flush=True)
def line(n):
 W=2*n+1;P=np.zeros((W,W));P[n,n]=1;seq=[P.copy()]
 def step(P,e):
  A=np.zeros_like(P)
  for i in [-1,1]:
   for j in [-1,1]:A+=(e/4+(1-e)/2*(i==j))*np.roll(P,(i,j),(0,1))
  return A
 for i in range(n):P=step(P,EPS);seq.append(P.copy())
 # The whole history at n=128 uses about 68 MB.
 h=[entropy(p) for p in seq]
 assert max(np.diff(np.diff(h)))<1e-10
 for k in sorted({1,2,int(math.log(n)),n//4,n}):
  R=np.zeros_like(P);R[n,n]=1
  for i in range(n):R=step(R,1 if i<k else EPS)
  tv=.5*np.abs(R-P).sum();D=kl(R,P);bound=(h[n]-h[n-k])/EPS**k
  assert D<=bound+1e-8
  save({'model':'Z','n':n,'k':k,'tv_block_change':float(tv),'KL_block_change':D,'KL_bound':bound,'original_tv_from_product':float(.5*np.abs(P-P.sum(1)[:,None]*P.sum(0)[None,:]).sum()),'hybrid_tv_from_product':float(.5*np.abs(R-R.sum(1)[:,None]*R.sum(0)[None,:]).sum()),'max_mass_error':float(max(abs(p.sum()-1) for p in seq))})
for n in [16,32,64,128]:line(n)
# Build the level-3 Grigorchuk quotient from its actual tree action.
def gen(g,depth,x):
 if depth==0:return x
 bit=x>>(depth-1);tail=x&((1<<(depth-1))-1)
 if g=='1':return x
 if g=='a':return ((1-bit)<<(depth-1))+tail
 child={'b':('a','c'),'c':('a','d'),'d':('1','b')}[g][bit]
 return (bit<<(depth-1))+gen(child,depth-1,tail)
S=[tuple(gen(g,3,x) for x in range(8)) for g in 'abcd'];id=tuple(range(8))
def mul(a,b):return tuple(a[b[i]] for i in range(len(a)))
Q=[id];index={id:0}
for g in Q:
 for s in S:
  z=mul(g,s)
  if z not in index:index[z]=len(Q);Q.append(z)
q=len(Q);assert q==128
for s in S:assert mul(s,s)==id
assert mul(S[1],S[2])==S[3]
right=np.array([[index[mul(g,s)] for s in S] for g in Q]);inv=np.argsort(right,axis=0)
def qstep(P,e):
 A=np.zeros_like(P)
 for i in range(4):
  for j in range(4):A+=(e/16+(1-e)/4*(i==j))*P[np.ix_(inv[:,i],inv[:,j])]
 return A
n=60;P=np.zeros((q,q));P[0,0]=1;seq=[P.copy()]
for i in range(n):P=qstep(P,EPS);seq.append(P.copy())
h=[entropy(p) for p in seq];assert max(np.diff(np.diff(h)))<1e-10
for k in [1,3,6,15,60]:
 for i in sorted({0,(n-k)//2,n-k}):
  R=np.zeros_like(P);R[0,0]=1
  for t in range(n):R=qstep(R,1 if i<=t<i+k else EPS)
  m=k+max(i,n-i-k);bound=(h[m]-h[m-k])/EPS**k
  # A4 proves the TV bound after left convolution/inversion, not a KL claim at this point.
  tv=float(.5*np.abs(R-P).sum());assert tv<=math.sqrt(max(0,bound)/2)+1e-8
  save({'model':'Grigorchuk level3 quotient','order':q,'n':n,'k':k,'block_start':i,'tv_block_change':tv,'TV_bound':math.sqrt(max(0,bound)/2),'original_tv_from_product':float(.5*np.abs(P-P.sum(1)[:,None]*P.sum(0)[None,:]).sum()),'mass':float(R.sum())})
print('Completed deterministic checks.',flush=True)
