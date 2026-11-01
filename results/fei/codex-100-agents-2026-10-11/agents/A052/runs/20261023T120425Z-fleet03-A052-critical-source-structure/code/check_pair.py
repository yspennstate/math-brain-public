from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
import json,time,sys
R=Path(__file__).resolve().parents[1];START=time.perf_counter();COUNT=0;PR=(2,3,5,7)
def ck(t):
 global COUNT
 COUNT+=1
 if not t:raise AssertionError(COUNT)
def table(n,t):return tuple(1-2*(t>>x&1) for x in range(1<<n))
def direct(f):return tuple(sum(a*(-1 if (x&s).bit_count()%2 else 1) for x,a in enumerate(f)) for s in range(len(f)))
def sign(v):
 p=q=1
 for a,b in zip(PR,v):
  if b>0:p*=a**b
  elif b<0:q*=a**(-b)
 return (p>q)-(p<q)
def rank(vs):
 s={0};r=0
 for v in vs:
  if v not in s:s|={a^v for a in list(s)};r+=1
 return r
@lru_cache(None)
def profile(f):
 N=len(f);n=N.bit_length()-1;W=direct(f);H=[2*n*N*N,0,0,0]
 for w in W:
  for j,p in enumerate(PR):
   z=abs(w);e=0
   while z and z%p==0:e+=1;z//=p
   H[j]-=2*w*w*e
 I=F(sum(sum(f[x]!=f[x^(1<<j)] for x in range(N)) for j in range(n)),N)
 ck(I==F(sum(s.bit_count()*w*w for s,w in enumerate(W)),N*N))
 costs={v:min(F(sum(f[x]!=f[x^v] for x in range(N)),N),F(sum(f[x]==f[x^v] for x in range(N)),N)) for v in range(1,N)}
 basis=[];a=F(0)
 for v in sorted(costs,key=lambda x:(costs[x],x)):
  if rank(basis+[v])>len(basis):basis.append(v);a+=costs[v]
 return H,I,a,W
def positions(A,n):return [j for j in range(n) if A>>j&1],[j for j in range(n) if not A>>j&1]
def emb(x,ps):return sum((x>>i&1)<<j for i,j in enumerate(ps))
def branches(f,A):
 aa,cc=positions(A,len(f).bit_length()-1)
 return [tuple(f[emb(u,aa)|emb(x,cc)] for x in range(1<<len(cc))) for u in range(4)]
def glue(gs,A,n):
 aa,cc=positions(A,n);f=[0]*(1<<n)
 for u,g in enumerate(gs):
  for x,a in enumerate(g):f[emb(u,aa)|emb(x,cc)]=a
 return tuple(f)
def case(f,A,r,v,s,stationary):
 n=len(f).bit_length()-1;N=len(f);gs=branches(f,A);M=N//4;h=gs[r];p=profile(f)
 nv=tuple(s*a*(-1 if (x&v).bit_count()%2 else 1) for x,a in enumerate(h));new=gs[:];new[r]=nv;ff=glue(new,A,n);q=profile(ff)
 C0=sum(F(sum(a*b for a,b in zip(gs[r^(1<<j)],h)),M) for j in range(2))
 Cv=sum(F(sum(gs[r^(1<<j)][x]*h[x]*(-1 if (x&v).bit_count()%2 else 1) for x in range(M)),M) for j in range(2))
 B=profile(nv)[1]-profile(h)[1]
 ck(q[1]-p[1]==(B+C0-s*Cv)/4)
 ck(profile(nv)[0]==profile(h)[0]);ck(profile(nv)[2]==profile(h)[2])
 # Every original mixed Fourier row, including both interference signs.
 aa,cc=positions(A,n);ws=[direct(g) for g in gs]
 for T in range(M):
  for W in range(4):
   z=sum((-1 if (W&u).bit_count()%2 else 1)*(s*ws[u][T^v] if u==r else ws[u][T]) for u in range(4))
   ck(q[3][emb(T,cc)|emb(W,aa)]==z)
 if stationary:
  di=(q[1]-p[1])*N*N;ck(di.denominator==1)
  d=[q[0][j]-p[0][j] for j in range(4)];d[0]-=3*int(di);ck(sign(d)<=0)
 return ff
def main():
 pilot='--pilot' in sys.argv;nsources=16 if pilot else 256;cases=0
 for t in range(nsources):
  f=table(3,t)
  for A in [3,5,6]:
   for r in range(4):
    for v in range(2):
     for s in [-1,1]:case(f,A,r,v,s,False);cases+=1
  if time.perf_counter()-START>53:raise TimeoutError('frozen53s')
 # The full existing65536 census certifies each quadratic-class maximum.
 # Group those exact maxima by degree4 ANF coefficient (truth parity).
 src=json.loads((R/'out/CHECK.json').read_text(encoding='utf-8'));winners={}
 for row in src['phase_class_representatives']:
  c=row['table'].bit_count()%2
  if c not in winners or sign([a-b for a,b in zip(row['D_scaled_prime_log'],winners[c]['D_scaled_prime_log'])])>0:winners[c]=row
 ck(len(winners)==2);critical_cases=0
 for c,row in winners.items():
  f=table(4,row['table'])
  for A in [3,5,6,9,10,12]:
   for r in range(4):
    for v in range(4):
     for s in [-1,1]:case(f,A,r,v,s,True);critical_cases+=1
  if time.perf_counter()-START>53:raise TimeoutError('frozen53s')
 f=table(3,0);ff=case(f,3,0,0,-1,False);ck(profile(f)[0]!=profile(ff)[0]);ck(profile(ff)[0]==[128,0,0,0])
 out={'status':'PASS','pilot':pilot,'checks':COUNT,'generic_three_bit_sources':nsources,'generic_original_pair_competitors':cases,'cubic_phase_classes':2,'cubic_phase_representatives':list(winners.values()),'stationary_original_pair_competitors':critical_cases,'sign_entropy_guard':'one branch sign changes full root entropy0 to2; pair entropy must retain s','seconds':time.perf_counter()-START,'arithmetic':'own direct characters and every physical query/outside edge; exact prime products; independent set-span child minima; all mixed T,W retained'}
 (R/'out'/('PAIR_PILOT.json' if pilot else 'PAIR.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='');print(json.dumps({k:v for k,v in out.items() if k!='cubic_phase_representatives'}))
if __name__=='__main__':main()
