from fractions import Fraction as F
from functools import lru_cache
from collections import Counter,defaultdict
from pathlib import Path
import json,time,sys,hashlib

ROOT=Path(__file__).resolve().parents[1]
SCALE=1<<80
start=time.perf_counter(); checks=0
limit=60 if '--pilot' in sys.argv else 300
def ck(ok):
 global checks
 checks+=1
 assert ok
 if time.perf_counter()-start>limit: raise RuntimeError('Frozen runtime exceeded')
def fw(v):
 z=list(v); h=1
 while h<len(z):
  for i in range(0,len(z),2*h):
   for j in range(i,i+h):
    p,q=z[j],z[j+h];z[j],z[j+h]=p+q,p-q
  h*=2
 return z
def direct(v):
 return [sum(val*(1-2*((x&s).bit_count()%2)) for x,val in enumerate(v)) for s in range(len(v))]
@lru_cache(None)
def factor(k):
 z={};d=2
 while d*d<=k:
  while k%d==0:z[d]=z.get(d,0)+1;k//=d
  d+=1
 if k>1:z[k]=z.get(k,0)+1
 return z
def add(*terms):
 z=defaultdict(F)
 for w,v in terms:
  for p,c in v.items():z[p]+=w*c
 return {p:c for p,c in z.items() if c}
def logq(q):
 q=F(q)
 return add((1,factor(q.numerator)),(-1,factor(q.denominator)))
@lru_cache(None)
def ln(q):
 q=F(q);k=0
 while q>=2:q/=2;k+=1
 while q<1:q*=2;k-=1
 def ser(r):
  z=(r-1)/(r+1);zz=z*z;power=z;lo=F(0)
  for j in range(36):lo+=2*power/(2*j+1);power*=zz
  return lo,lo+2*power/(73*(1-zz))
 l,h=ser(q);l2,h2=ser(F(2))
 return (l+k*l2,h+k*h2) if k>=0 else (l+k*h2,h+k*l2)
@lru_cache(None)
def ln_grid(p):
 l,h=ln(F(p))
 return (l*SCALE).numerator//(l*SCALE).denominator,-((-h*SCALE).numerator//(-h*SCALE).denominator)
def grid(expr,constant=0):
 lo=hi=F(constant)*SCALE
 for p,c in expr.items():
  l,h=ln_grid(p)
  if c>=0:lo+=c*l;hi+=c*h
  else:lo+=c*h;hi+=c*l
 return lo,hi
def ent(ps):
 return add(*[(-p,logq(p)) for p in ps if p])
def entropy_scaled(w,n):
 # Natural entropy times 2^(2n); integer prime-log coefficients.
 z={2:2*n*(1<<(2*n))}
 for val,mult in Counter(abs(x) for x in w).items():
  if not val:continue
  for p,e in factor(val).items():z[p]=z.get(p,0)-2*e*val*val*mult
 return {p:c for p,c in z.items() if c}
def ints_add(*terms):
 z=defaultdict(int)
 for c,v in terms:
  for p,t in v.items():z[p]+=c*t
 return {p:c for p,c in z.items() if c}

@lru_cache(None)
def table(n,mask):
 v=tuple(1-2*((mask>>x)&1) for x in range(1<<n));w=tuple(fw(v))
 return v,w,entropy_scaled(w,n)
def singleton(v,w,E,n,i,lookup=True):
 L=1<<n;den=L*L
 idx=[x for x in range(L) if not(x&(1<<i))]
 g=[v[x] for x in idx];h=[v[x|(1<<i)] for x in idx]
 if lookup:
  gm=sum((t<0)<<j for j,t in enumerate(g));hm=sum((t<0)<<j for j,t in enumerate(h))
  Eg=table(n-1,gm)[2];Eh=table(n-1,hm)[2]
 else:Eg=entropy_scaled(fw(g),n-1);Eh=entropy_scaled(fw(h),n-1)
 delta=ints_add((1,E),(-2,Eg),(-2,Eh))
 Q=sum(val*val for s,val in enumerate(w) if s&(1<<i))
 R=sum((s.bit_count()-1)*val*val for s,val in enumerate(w) if s&(1<<i))
 D=[(p-q)//2 for p,q in zip(g,h)]
 ck(Q==sum(p!=q for p,q in zip(g,h))*den//len(g))
 physical=sum((D[x]-D[x^(1<<j)])**2 for x in range(len(D)) for j in range(n-1))
 ck(R==physical*den//(4*len(D)))
 margin=ints_add((2*R,{2:1}),(-1,delta))
 lo,hi=grid(margin,3*Q)
 ck(lo>=0)
 return lo,hi,Q,R,delta

def pilot():
 nodes=blocks=0;minmargin=None
 for n in range(4):
  for mask in range(1<<(1<<n)):
   v,w,E=table(n,mask);den=1<<(2*n)
   ck(list(w)==direct(v))
   for i in range(n):
    singleton(v,w,E,n,i);nodes+=1
   for a in range(n+1):
    N=1<<a;D=1<<(n-a)
    eb=[]
    for b in range(N):eb.append(entropy_scaled(fw([v[b+N*y] for y in range(D)]),n-a))
    delta=add((F(1,den),E),*[(-F(N,den),e) for e in eb])
    Q=sum(val*val*(s&(N-1)).bit_count() for s,val in enumerate(w));q=F(Q,den)
    ck(grid(delta)[0]>=0)
    if a:
     t=q/a
     binary=ent([t,1-t])
     m1=add((a,{2:F(1)}),(a,binary),(-1,delta))
     m2=add((a,binary),(-1,delta))
     ck(grid(m1)[0]>=0);ck(grid(m2,2*q)[0]>=0)
     if q:
      crude=add((q,logq(F(a)/q)),(-1,delta))
      ck(grid(crude,3*q)[0]>=0)
     else:ck(not delta)
    else:ck(not delta and q==0)
    blocks+=1
 ck(nodes==804 and blocks==1082)
 return {'blocks':blocks,'singleton_nodes':nodes,'status':'PASS'}

def census():
 n=4;nodes=0;zeros=0;best=None;bestw=None
 # Cache only 256 smaller tables; never cache the full four-bit domain.
 for mask in range(65536):
  v=[1-2*((mask>>x)&1) for x in range(16)];w=fw(v);E=entropy_scaled(w,4)
  ck(w==direct(v))
  for i in range(4):
   lo,hi,Q,R,delta=singleton(v,w,E,4,i);nodes+=1
   if not Q:zeros+=1;continue
   # Ratio enclosure Delta / ((3/ln2)d+2I(D)) = delta_nat / (3d+2 ln2 I(D)).
   dl,dh=grid(delta);l2,h2=ln_grid(2)
   ub=F(dh,3*Q*SCALE+2*R*l2)
   if best is None or ub>best:best=ub;bestw={'mask':mask,'coordinate':i,'I_numerator':Q,'derivative_energy_numerator':R,'denominator':256,'delta_prime_log_numerator':delta}
 ck(nodes==262144)
 # A rational published upper cap for this finite census, proved by the interval upper ratio.
 ck(best<F(81,100))
 return {'status':'PASS','tables':65536,'nodes':nodes,'zero_influence_nodes':zeros,'ratio_upper_bound':str(best),'certified_rational_cap':'81/100','max_interval_witness':bestw}

def bent():
 cases=[]
 for m in range(2,41,2):
  u=F(1,1<<(m//2));d=u*u;weights=[(1+e*u)/2 for e in (1,-1)]
  Delta={2:m*d}
  for e,we in zip((1,-1),weights):
   Delta=add((1,Delta),(-2*we*(1-e*u)**2,logq(1-e*u)))
   z=abs(1-2*e*u)
   if z:Delta=add((1,Delta),(we*z*z,logq(z)))
  # Independent histogram computation, no closed-form simplification.
  den=1<<(2*m);C=1<<(m//2)
  hp=add(*[(F((1<<m)+e*C,2),ent([F((e*C-1)**2,den),F(1,den)])) for e in (1,-1)])
  hg={2:F(m)}
  hgp=add(*[(F((1<<m)+e*C,2),ent([F((e*C-2)**2,den)])) for e in (1,-1)])
  ck(Delta==add((1,hp),(-F(1,2),hg),(-F(1,2),hgp)))
  upper=add((1,ent([d,1-d])),(-1,Delta))
  gl,gh=grid(upper,2*d);ck(gl>0)
  if m in (2,4,6,8):
   b=[(-1)**sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2)) for y in range(1<<m)]
   bp=b.copy();bp[0]*=-1
   v=[z for p,q in zip(b,bp) for z in (p,q)];ww=fw(v)
   ck(ent([F(z*z,1<<(2*(m+1))) for z in ww])==hp)
   ck(sum(F(z*z,1<<(2*(m+1))) for s,z in enumerate(ww) if s&1)==d)
  cases.append({'m':m,'delta':str(d),'sharp_gap_over_delta_squared_interval':[str(gl/(SCALE*d*d)),str(gh/(SCALE*d*d))]})
 coeff={1:F(3)}
 def c(k):return F(-1) if k==1 else F(3,2) if k==2 else F(-2,k*(k-1)*(k-2))
 for j in range(2,7):
  def weighted(lam):return c(2*j)*lam**(2*j)+c(2*j-1)*lam**(2*j-1)
  coeff[j]=-2*weighted(1)+weighted(2)
 ck(coeff[2]==F(-19,6));ck(coeff[3]==F(-61,30));ck(F(-1,2)-coeff[2]==F(8,3))
 tensors=[]
 for m,t in ((2,2),(2,3),(4,2)):
  b=[(-1)**sum(((y>>j)&1)*((y>>(j+1))&1) for j in range(0,m,2)) for y in range(1<<m)]
  bp=b.copy();bp[0]*=-1;base=[z for p,q in zip(b,bp) for z in (p,q)]
  v=[1]
  for _ in range(t):v=[p*q for p in base for q in v]
  n=(m+1)*t;w=fw(v)
  ck(ent([F(z*z,1<<(2*n)) for z in w])==add((t,ent([F(z*z,1<<(2*(m+1))) for z in fw(base)]))))
  mask=sum(1<<(j*(m+1)) for j in range(t))
  ck(sum(F(z*z,1<<(2*n))*(s&mask).bit_count() for s,z in enumerate(w))==F(t,1<<m))
  tensors.append({'m':m,'t':t,'status':'PASS'})
 return {'status':'PASS','histogram_cases':cases,'natural_entropy_coefficients_after_m_delta':{str(j):str(c) for j,c in coeff.items()},'tensors':tensors}

result={'helper_version':'A018-independent-lead-review-v2','grid_scale':str(SCALE),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if '--pilot' in sys.argv:result['pilot']=pilot();name='PILOT.json'
else:
 result['census']=census()
 (ROOT/'out/CENSUS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
 result['bent']=bent();name='CHECK.json'
result['assertions']=checks;result['elapsed_seconds']=time.perf_counter()-start
(ROOT/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({'status':'PASS','file':name,'assertions':checks,'elapsed_seconds':result['elapsed_seconds']},indent=2))
