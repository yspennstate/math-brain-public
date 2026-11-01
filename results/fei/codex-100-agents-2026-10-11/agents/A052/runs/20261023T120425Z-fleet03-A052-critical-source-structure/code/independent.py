from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
R=Path(__file__).resolve().parents[1];COUNT=0;START=time.perf_counter();PR=(2,3,5,7)
def ck(t):
 global COUNT
 COUNT+=1
 if not t:raise AssertionError(COUNT)
def table(n,t):return tuple(1-2*(t>>x&1) for x in range(1<<n))
def direct(f):return tuple(sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(f)) for s in range(len(f)))
def prime_product_sign(v):
 a=b=1
 for p,z in zip(PR,v):
  if z>0:a*=p**z
  elif z<0:b*=p**(-z)
 return (a>b)-(a<b)
def rank(vs):
 span={0};r=0
 for v in vs:
  if v not in span:span|={x^v for x in list(span)};r+=1
 return r
@lru_cache(None)
def prof(f):
 N=len(f);n=N.bit_length()-1;W=direct(f);H=[2*n*N*N,0,0,0]
 for w in W:
  for j,p in enumerate(PR):
   z=abs(w);v=0
   while z and z%p==0:z//=p;v+=1
   H[j]-=2*w*w*v
 I=F(sum(sum(f[x]!=f[x^(1<<j)] for x in range(N)) for j in range(n)),N)
 ck(I==F(sum(s.bit_count()*w*w for s,w in enumerate(W)),N*N))
 costs={v:min(F(sum(f[x]!=f[x^v] for x in range(N)),N),F(sum(f[x]==f[x^v] for x in range(N)),N)) for v in range(1,N)}
 basis=[];a=F(0)
 for v in sorted(costs,key=lambda v:(costs[v],v)):
  if rank(basis+[v])>len(basis):basis.append(v);a+=costs[v]
 ck(len(basis)==n)
 return tuple(H),I,a
def split(f,i):
 lo=(1<<i)-1
 return [tuple(f[(x&lo)|((x>>i)<<(i+1))|(s<<i)] for x in range(len(f)//2)) for s in [0,1]]
def select(g,h,i):
 out=[]
 for x in range(2*len(g)):
  z=(x&((1<<i)-1))|((x>>(i+1))<<i);out.append(h[z] if x>>i&1 else g[z])
 return tuple(out)
def delta_D(f,g,K):
 p,q=prof(f),prof(g);N=len(f);di=(q[1]-p[1])*N*N;ck(di.denominator==1)
 return (q[0][0]-p[0][0]-K*int(di),)+tuple(q[0][j]-p[0][j] for j in range(1,4))
def check_source(f,K,stationary):
 n=len(f).bit_length()-1;cases=0
 for i in range(n):
  g,h=split(f,i);M=len(h);c0=F(sum(a*b for a,b in zip(g,h)),M)
  for v in range(M):
   hh=tuple(a*(-1 if (x&v).bit_count()%2 else 1) for x,a in enumerate(h));cv=F(sum(a*b for a,b in zip(g,hh)),M)
   di=prof(hh)[1]-prof(h)[1]
   for s in [-1,1]:
    nh=tuple(s*a for a in hh);ff=select(g,nh,i);p,q=prof(f),prof(ff)
    ck(prof(nh)[0]==prof(h)[0]);ck(prof(nh)[2]==prof(h)[2])
    ck(q[1]-p[1]==(di+c0-s*cv)/2)
    # Full child bank, including all signs and zero coefficients.
    oldbank=K*(prof(g)[2]+prof(h)[2])/2
    newbank=K*(prof(g)[2]+prof(nh)[2])/2
    ck(oldbank==newbank)
    if stationary:ck(prime_product_sign(delta_D(f,ff,K))<=0)
    cases+=1
  if stationary:ck(c0>=0)
  if time.perf_counter()-START>53:raise TimeoutError('frozen53s')
 return cases
def main():
 d=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'));sources={}
 for row in d['critical_sources']+d['phase_class_representatives']:sources[(row['n'],row['table'],row['K'])]=True
 cases=0
 for (n,t,K) in sources:cases+=check_source(table(n,t),K,True)
 guard=d['minimal_dimension_only_guard']
 if guard:
  f=table(guard['n'],guard['table']);g=table(guard['n'],guard['competitor_table'])
  ck(prime_product_sign(delta_D(f,g,guard['K']))>0)
  p=prof(f);dv=(p[0][0]-guard['K']*int(p[1]*len(f)**2),)+p[0][1:];ck(prime_product_sign(dv)>0)
 # Restriction ratio criticality alone does not grant quadratic-phase
 # optimality: a physical character has ratio0 like all its descendants,
 # but this actual two-bit phase gives entropy2 and SAME influence1.
 f=(1,1,-1,-1);g=(1,1,-1,1);ck(prof(f)[1]==prof(g)[1]==1);ck(prof(f)[0]==(0,0,0,0));ck(prof(g)[0]==(32,0,0,0));ck(prime_product_sign(delta_D(f,g,3))>0)
 bent=[]
 for m in [2,4]:
  h=tuple((-1)**(sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))%2) for x in range(1<<m))
  g=tuple(a*(-1 if x&1 else 1) for x,a in enumerate(h));f=select(g,h,m);ff=select(g,g,m)
  ck(prof(f)[0]==prof(ff)[0]);ck(prof(f)[1]-prof(ff)[1]==F(1,2));ck(prime_product_sign(delta_D(f,ff,3))>0)
  # Sharp bent-product equality case: g is constant and h is bent.
  const=tuple(1 for _ in h);f=select(const,h,m);cc=[F(sum(a*(-1 if (x&v).bit_count()%2 else 1) for x,a in enumerate(h)),len(h)) for v in range(len(h))]
  ck(cc[0]==max(map(abs,cc))==F(1,1<<(m//2)));ck(sum(c*c for c in cc)==1)
  q=F(sum(a!=b for a,b in zip(const,h)),len(h));ck(q==(1-F(1,1<<(m//2)))/2)
  for v in range(len(h)):
   hv=tuple(a*(-1 if (x&v).bit_count()%2 else 1) for x,a in enumerate(h));ck(prof(select(const,hv,m))[0]==prof(f)[0])
  bent.append({'m':m,'C0':str(cc[0]),'query_influence':str(q),'strict_nonstationary_gain_K3':'3/2'})
 out={'status':'PASS','checks':COUNT,'stationary_sources':len(sources),'actual_stationary_competitors':cases,'bent_controls':bent,'minimal_dimension_guard_replayed':bool(guard),'seconds':time.perf_counter()-START,'arithmetic':'direct characters; physical edges; independent set-span rank; exact integer-product sign certificates, no logarithm approximation or imported main helper'}
 (R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps(out))
if __name__=='__main__':main()
