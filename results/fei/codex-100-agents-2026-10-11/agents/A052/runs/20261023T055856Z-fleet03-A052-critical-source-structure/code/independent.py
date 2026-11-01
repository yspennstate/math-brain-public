from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];COUNT=0
def ck(t):
 global COUNT
 COUNT+=1
 if not t:raise AssertionError(COUNT)
def fac(v):
 out={};p=2
 while p*p<=v:
  while v%p==0:out[p]=out.get(p,0)+1;v//=p
  p+=1
 if v>1:out[v]=out.get(v,0)+1
 return out
def plus(*terms):
 out={}
 for d,c in terms:
  for k,v in d.items():out[k]=out.get(k,0)+v*c
 return {k:v for k,v in out.items() if v}
def rank(vs):
 rows=list(vs);r=0
 for j in reversed(range(max(rows,default=0).bit_length())):
  z=next((i for i in range(r,len(rows)) if rows[i]>>j&1),None)
  if z is None:continue
  rows[r],rows[z]=rows[z],rows[r]
  for i in range(r+1,len(rows)):
   if rows[i]>>j&1:rows[i]^=rows[r]
  r+=1
 return r
@lru_cache(None)
def prof(f):
 N=len(f);n=N.bit_length()-1
 coeff=[sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
 H={}
 for z in coeff:
  if not z:continue
  p=F(z*z,N*N);H=plus((H,1),(fac(p.numerator),-p),(fac(p.denominator),p))
 costs={v:F(sum(f[x]!=f[x^v] for x in range(N)),N) for v in range(1,N)}
 for v,w in costs.items():ck(w==F(sum(coeff[s]**2 for s in range(N) if (s&v).bit_count()%2),N*N))
 I=sum(costs[1<<j] for j in range(n));chosen=[];a=F(0)
 for v in sorted(costs,key=lambda z:(min(costs[z],1-costs[z]),z)):
  if rank(chosen+[v])>len(chosen):chosen.append(v);a+=min(costs[v],1-costs[v])
 ck(len(chosen)==n)
 return H,I,a
def branch(f,A,u):
 n=len(f).bit_length()-1;aa=[j for j in range(n) if A>>j&1];cc=[j for j in range(n) if not A>>j&1]
 return tuple(f[sum((u>>i&1)<<j for i,j in enumerate(aa))+sum((z>>i&1)<<j for i,j in enumerate(cc))] for z in range(1<<len(cc)))
def data(f,A):
 m=A.bit_count();q=F(1,1<<m);hs={};ia=F(0);aa=F(0)
 for u in range(1<<m):
  H,I,a=prof(branch(f,A,u));hs=plus((hs,1),(H,q));ia+=q*I;aa+=q*a
 H,I,_=prof(f)
 return H,I,plus((H,1),(hs,-1)),I-ia,ia-aa,plus(({2:F(15,4)*aa},1),(hs,-1))
@lru_cache(None)
def rank_signature(f,U):
 N=len(f);m={v:min(F(sum(f[x]!=f[x^v] for x in range(N)),N),F(sum(f[x]==f[x^v] for x in range(N)),N)) for v in range(1,N)}
 return tuple((t,rank([v for v in m if m[v]<=t]),rank([v for v in m if m[v]<=t]+[U])-1) for t in sorted(set([F(0),F(1,2)]+list(m.values()))))
def actual_transform(f,A,seed):
 n=len(f).bit_length()-1;aa=[j for j in range(n) if A>>j&1];cc=[j for j in range(n) if not A>>j&1]
 pa=list(reversed(aa)) if seed&1 else aa;pc=list(reversed(cc)) if seed&2 else cc;out=[]
 for y in range(1<<n):
  vals=[0]*n
  for i,j in enumerate(aa):vals[j]=(y>>pa[i]&1)^((seed>>(i+2))&1)
  for i,j in enumerate(cc):vals[j]=(y>>pc[i]&1)^((y>>aa[i%len(aa)]&1) if seed&4 else 0)^((seed>>(i+3))&1)
  x=sum(b<<j for j,b in enumerate(vals));d=(3*seed+1)%len(f)
  out.append(f[x]*(-1 if (d&y).bit_count()%2 else 1))
 return tuple(out)
def activated(k):
 out=[]
 for x in range(1<<(k+4)):
  a,b,c,z=[x>>j&1 for j in range(4)]
  out.append((-1 if (a*b+a*c+b*c+z*a)%2 else 1) if x>>4==0 else 1)
 return tuple(out)
def main():
 start=time.perf_counter();sources=[tuple(1-2*(t>>x&1) for x in range(8)) for t in [0x16,0x69,0x81]]+[activated(2),activated(3)];cases=0;rank_cases=0
 for f in sources:
  for A in [1,3]:
   old=data(f,A)
   for seed in range(8):
    ff=actual_transform(f,A,seed);new=data(ff,A);delta=new[1]-old[1]
    ck(old[0]==new[0]);ck(old[2]==new[2]);ck(old[5]==new[5]);ck(new[3]+new[4]-delta==old[3]+old[4]);cases+=1
    # Match every complete terminal by its entropy and full orbit minimum.
    terminal=lambda g:sorted((tuple(sorted(prof(branch(g,A,u))[0].items())),prof(branch(g,A,u))[2]) for u in range(1<<A.bit_count()))
    ck(terminal(f)==terminal(ff))
    m=A.bit_count();d=len(f).bit_length()-1-m
    # Match actual branch labels under P and b, and transport the OLD
    # booked subspace span(e0) by the inverse outside reversal R.
    for u in range(1<<m):
     v=sum((((u>>(m-1-i if seed&1 else i))&1)^((seed>>(i+2))&1))<<i for i in range(m))
     oldU=1;newU=1<<(d-1) if seed&2 else 1
     ck(rank_signature(branch(f,A,v),oldU)==rank_signature(branch(ff,A,u),newU));rank_cases+=1
    if time.perf_counter()-start>53:raise TimeoutError('frozen53s')
 # Scope adversary: exchange an irrelevant ORIGINAL queried bit with an
 # outside relevant bit. The physical partition changes; invariance fails.
 f=tuple(-1 if x>>1==0 else 1 for x in range(8))
 ff=tuple(f[((y&1)<<1)|((y>>1)&1)|(y&4)] for y in range(8))
 old=data(f,1);new=data(ff,1);delta=new[1]-old[1]
 ck(old[2]!=new[2]);ck(old[3]+old[4]!=new[3]+new[4]-delta)
 ck(old[2]=={} and new[2]=={2:F(2)})
 ck(old[3]+old[4]==0 and new[3]+new[4]-delta==1)
 out={'status':'PASS','sources':len(sources),'general_group_maps':cases,'rank_stratified_terminals':rank_cases,'checks':COUNT,'seconds':time.perf_counter()-start,'outside_group_guard':'changed partition: L0->2, compensated query+release0->1; blanket affine-invariance assertion FALSE','method':'direct character sums, physical edges for every direction, independent row-echelon rank and exact prime-log entropy; affine shifts, block permutations, shears and output characters'}
 (R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
