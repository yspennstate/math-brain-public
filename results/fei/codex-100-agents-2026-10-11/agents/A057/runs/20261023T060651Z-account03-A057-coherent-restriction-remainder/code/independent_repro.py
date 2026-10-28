from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import time,json,sys
ROOT=Path(__file__).resolve().parents[1];start=time.monotonic();full='--full' in sys.argv
counts={'assertions':0,'exposed_states':0,'exterior_edges':0,'mixed_tree_edges':0,'positive_internal_debits':0}
def ck(x):
 assert x;counts['assertions']+=1
 if time.monotonic()-start>(180 if full else 55):raise RuntimeError('frozen cap')
def mix(*terms):
 out={}
 for w,exp in terms:
  for p,a in exp.items():out[p]=out.get(p,F(0))+w*a
 return {p:v for p,v in out.items() if v}
@lru_cache(None)
def factor(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d+=1
 if n>1:out[n]=1
 return out
def ph(p):
 if not p:return {}
 out={}
 for q,k in factor(p.denominator).items():out[q]=p*k
 for q,k in factor(p.numerator).items():out[q]=out.get(q,F(0))-p*k
 return {q:k for q,k in out.items() if k}
@lru_cache(maxsize=4096)
def H(table):
 N=len(table);out={}
 for s in range(N):
  amplitude=sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(table))
  if amplitude:out=mix((1,out),(1,ph(F(amplitude*amplitude,N*N))))
 return out
@lru_cache(None)
def ln_bounds(q):
 z=(q-1)/(q+1);su=F(0)
 for j in range(48):su+=2*z**(2*j+1)/(2*j+1)
 error=2*abs(z)**97/(97*(1-z*z))
 return su-error,su+error
@lru_cache(None)
def logs(p):
 if p==2:return F(1),F(1)
 k=p.bit_length()-1;a,b=ln_bounds(F(p,1<<k));l,h=ln_bounds(F(2))
 return k+a/h,k+b/l
def positive(exp):
 lower=F(0)
 for p,v in exp.items():
  l,h=logs(p);lower+=v*(l if v>=0 else h)
 return lower>=0
def restrict(table,fix):
 n=len(table).bit_length()-1;rem=[i for i in range(n) if i not in fix];out=[]
 for r in range(1<<len(rem)):
  x=sum(v<<i for i,v in fix.items())+sum(((r>>j)&1)<<i for j,i in enumerate(rem));out.append(table[x])
 return tuple(out),rem
def inf(table,i):
 return F(sum(table[x]!=table[x+(1<<i)] for x in range(len(table)) if not x>>i&1),len(table)//2)
def graph(code):return [(0,1),(2,3)]+[e for j,e in enumerate([(0,2),(0,3),(1,2),(1,3)]) if code>>j&1]
def sign(z,edges):return (-1)**sum(((z>>i)&1)*((z>>j)&1) for i,j in edges)
def pair_account(table,rem):
 E=F(0)
 for pair in [(0,1),(2,3)]:
  left=[x for x in pair if x in rem]
  if len(left)==2:E+=4*sum(inf(table,rem.index(x)) for x in left)
  elif len(left)==1:E+=2
 return E
for code in ([0,3,5,15] if full else [0]):
 edges=graph(code)
 for gt in ([6,8,15] if full else [6]):
  g=tuple(1 if gt>>y&1 else -1 for y in range(4));V=1-F(sum(g),4)**2
  table=tuple(g[y] if z==0 else sign(z,edges) for y in range(4) for z in range(16))
  for zz in product([None,0,1],repeat=4):
   fix={i:v for i,v in enumerate(zz) if v is not None};v,rem=restrict(table,fix);E=pair_account(v,rem)
   t=F(1,1<<sum(x is None for x in zz)) if 1 not in zz else F(0);counts['exposed_states']+=1
   for i in [x for x in rem if x<4]:
    child=[];Ec=[];tc=[]
    for bit in [0,1]:
     ff=dict(fix);ff[i]=bit;vc,rc=restrict(table,ff);child.append(H(vc));Ec.append(pair_account(vc,rc));tc.append(2*t if bit==0 else F(0))
    D=mix((1,H(v)),(-F(1,2),child[0]),(-F(1,2),child[1]));dE=E-sum(Ec)/2
    ck(dE>=2);ck(positive(mix((1,{2:dE}),(-1,D))))
    ck(mix((V,ph(t)),(-V/2,ph(tc[0])),(-V/2,ph(tc[1])))==({2:t*V} if t*V else {}));counts['exterior_edges']+=1
if full:
 # Actual fine-core g=A*y+(1-A)*1, where A indicates internal bit0 equals0.
 g=tuple((1 if y>>1&1 else -1) if not y&1 else 1 for y in range(4))
 table=tuple(g[(x>>4)&3] if not x>>6&1 else (g[(x>>4)&3] if not x&15 else sign(x&15,graph(0))) for x in range(128))
 def potential(fix):
  vals,rem=restrict(table,fix);gy,gr=restrict(g,{i-4:v for i,v in fix.items() if i in [4,5]})
  mu=F(sum(gy),len(gy));var=1-mu*mu
  x=fix.get(6);mask=all(fix.get(i,0)==0 for i in range(4));density=F(1,1<<sum(i not in fix for i in range(4))) if mask else F(0)
  t=F(17,32) if x is None else F(1) if x==0 else density
  p=F(1,2) if 4 not in fix else F(fix[4]==0)
  core=(1 if fix[5] else -1,) if 5 in fix else (-1,1);muc=F(sum(core),len(core));Vc=1-muc*muc
  U=mix((t*p,mix((1,H(core)),(-1,ph(muc*muc)))));R=mix((Vc,ph(t*p)))
  ctrl=sum(inf(gy,j) for j,i in enumerate(gr) if i==0);data=sum(inf(gy,j) for j,i in enumerate(gr) if i==1)
  Q=t*(21*ctrl+5*data)
  S={2:6*inf(vals,rem.index(6))} if x is None else mix((var,ph(t)))
  E=4*sum(inf(vals,rem.index(i)) for i in rem if i<4) if x is None else F(0) if x==0 else pair_account(vals,rem)
  return vals,mix((1,U),(1,R),(1,S),(1,{2:Q+E}))
 order=[4,6,0,5,1,2,3]
 def walk(fix,depth):
  if depth==len(order):return
  i=order[depth];vals,P=potential(fix);cs=[];pcs=[]
  for bit in [0,1]:
   ff=dict(fix);ff[i]=bit;vc,pc=potential(ff);cs.append(H(vc));pcs.append(pc)
  D=mix((1,H(vals)),(-F(1,2),cs[0]),(-F(1,2),cs[1]))
  ck(positive(mix((1,P),(-F(1,2),pcs[0]),(-F(1,2),pcs[1]),(-1,D))))
  counts['mixed_tree_edges']+=1
  if i in [4,5] and positive(mix((1,D),(-1,{2:F(1,1000)}))):counts['positive_internal_debits']+=1
  for bit in [0,1]:
   ff=dict(fix);ff[i]=bit;walk(ff,depth+1)
 walk({},0)
 for m in range(4,259,2):
  c=F(1,1<<m);ck(m*c/2<=F(1,8));ck(F(17,8)<=F(17,3)*F(3,8))
out={'status':'PASS','full':full,**counts,'seconds':time.monotonic()-start,'arithmetic':'independent direct-character entropy and independent48-term log bounds'}
(ROOT/'out'/('independent.json' if full else 'independent_pilot.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
