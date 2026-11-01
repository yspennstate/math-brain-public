"""Independent direct-character/physical-edge audit; no other-agent imports."""
from pathlib import Path
from fractions import Fraction as F
import json, time, hashlib
R=Path(__file__).resolve().parents[1]
PR=(2,3,5,7,11,13,17,19,23,29,31)
checks=0
def check(x):
 global checks
 assert x
 checks+=1
def rank(vs):
 b={}
 for v in vs:
  while v:
   j=v.bit_length()-1
   if j in b: v^=b[j]
   else: b[j]=v; break
 return len(b)
def profile(f):
 N=len(f); n=N.bit_length()-1
 W=[sum(f[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
 h=[0]*len(PR); h[0]=2*n*N*N
 for w in W:
  z=abs(w)
  if not z: continue
  for j,p in enumerate(PR):
   while z%p==0: h[j]-=2*w*w; z//=p
  check(z==1)
 check(sum(w*w for w in W)==N*N)
 c=[F(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(N)]
 check(sum(c[1<<i] for i in range(n))==F(sum(s.bit_count()*w*w for s,w in enumerate(W)),N*N))
 chosen=[]; a=F(0)
 for v in sorted(range(1,N),key=lambda v:(min(c[v],1-c[v]),v)):
  if rank(chosen+[v])>len(chosen): chosen.append(v); a+=min(c[v],1-c[v])
 check(len(chosen)==n)
 return h,a,W,c
def nonpositive(v):
 a=b=1
 for p,e in zip(PR,v):
  if e>0:a*=p**e
  elif e<0:b*=p**(-e)
 return a<=b
def run():
 start=time.perf_counter(); N=32; n=5; f=tuple(-1 if x==0 else 1 for x in range(N)); hf,af,wf,cf=profile(f)
 check(af==F(5,16)); cases=0; byrank={}; witnesses=[]
 for mask in range(256):
  vals=[(mask>>x)&1 for x in range(8)]; anf=vals[:]
  for j in range(3):
   for x in range(8):
    if x>>j&1: anf[x]^=anf[x^(1<<j)]
  deg=max([x.bit_count() for x in range(8) if anf[x]]+[0])
  p=tuple(-1 if vals[x&7] else 1 for x in range(N)); hp,ap,wp,cp=profile(p)
  support=[s for s,w in enumerate(wp) if w]; r=rank([s^support[0] for s in support])
  kernel=[v for v in range(N) if len({p[x]*p[x^v] for x in range(N)})==1]
  check(len(kernel)==2**(n-r)); check(rank(kernel)==n-r)
  g=tuple(a*b for a,b in zip(f,p)); hg,ag,wg,cg=profile(g)
  for d,K in [(3,10)]+([(2,4)] if deg<=2 else []):
   gamma=F(1,2**(d-1))-F(1,8); margin=K*gamma-1
   check(ag-af>=r*gamma)
   v=[hg[j]-hf[j] for j in range(len(PR))]; v[0]-=r*N*N
   check(nonpositive(v))
   v=[hg[j]-hf[j] for j in range(len(PR))]; v[0]+=int((-K*(ag-af)+r*margin)*N*N)
   check(nonpositive(v))
   if r==0: check(hg==hf and ag==af)
   cases+=1; byrank[str(r)]=byrank.get(str(r),0)+1
  if r and len(witnesses)<3: witnesses.append({'mask':mask,'rank':r,'affine_influence':str(ag)})
 # Missing-rarity guard: quadratic phase times itself is constant.
 p=tuple(-1 if ((x&1) and (x&2)) else 1 for x in range(N))
 check(profile(tuple(a*a for a in p))[1]<profile(p)[1])
 # Missing raw affine minimization guard: a character can remove a character.
 chi=tuple(-1 if x&1 else 1 for x in range(N))
 shifted=tuple(a*b for a,b in zip(f,chi)); hs,aa,ww,cc=profile(shifted)
 check(aa==af); check(sum(cc[1<<i] for i in range(n))>sum(cf[1<<i] for i in range(n)))
 out={'status':'PASS','cases':cases,'checks':checks,'rank_counts':byrank,'witnesses':witnesses,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh, Fraction physical costs, exact integer prime-product entropy comparisons','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (R/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8'); print(json.dumps(out))
if __name__=='__main__':run()
