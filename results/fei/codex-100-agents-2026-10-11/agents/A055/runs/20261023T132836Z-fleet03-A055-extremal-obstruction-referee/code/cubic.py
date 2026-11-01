from exact import Q,fw,entropy,add,mul,sgn,put,enc
from functools import lru_cache
from collections import Counter
from pathlib import Path
import time,sys,json,hashlib,itertools
R=Path(__file__).resolve().parents[1];pilot='--pilot' in sys.argv
spec={'helper_version':'A055 rare-root cubic-phase orbit guard v1; own exact.py unchanged','family':'all degree<=3 phases on4bits modulo output affine characters; whole-activated Q times point2 root; original-pair branch-controlled characters','domain':'main1024 phase classes on4bits;48 embedded3-bit nonlinear phase classes,48 explicit output-character copies,40 original-pair two-sign comparisons at K6,k6,n12;pilot16 phase classes on3bits,16 embedded phases and16 character copies at n10','case_count':'main1024 phase classes and136 physical root competitors;pilot16 phase classes and32 root competitors','symmetry':'ONLY output affine-character quotient: all H,a,centered costs and spectral affine rank unchanged under output characters;2^(n+1) orbit size per representative; explicit character-copy controls included','arithmetic':'integer Walsh and physical derivatives, exact minimum independent parity basis, Fraction and prime-log entropy with64-term rational atanh bounds','memory_estimate_MB':200,'maximum_runtime_seconds':120,'pilot_max_seconds':55,'helper_sha256':hashlib.sha256((R/'code/exact.py').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if not (R/'out/FROZEN_SPEC.json').exists():put('FROZEN_SPEC.json',spec)
start=time.perf_counter();checks=0;limit=55 if pilot else 120
def ck(x):
 global checks
 assert x
 checks+=1
 assert time.perf_counter()-start<limit,'frozen cap'
def rank(vs):
 piv={}
 for v in vs:
  while v:
   j=v.bit_length()-1
   if j in piv:v^=piv[j]
   else:piv[j]=v;break
 return len(piv)
@lru_cache(None)
def hh(x):return entropy([x])
@lru_cache(None)
def st(v):
 N=len(v);n=N.bit_length()-1;W=fw(v);counts=Counter(abs(w) for w in W if w)
 H={}
 for w,c in counts.items():H=add(H,hh(Q(w,N)),c)
 B=fw([w*w for w in W]);cost=tuple(min(N*N-b,N*N+b) for b in B)
 piv={};basis=[];num=0
 for c,s in sorted((cost[s],s) for s in range(1,N)):
  x=s
  while x:
   j=x.bit_length()-1
   if j in piv:x^=piv[j]
   else:piv[j]=x;basis.append(s);num+=c;break
  if len(basis)==n:break
 ck(len(basis)==n)
 a=Q(num,2*N*N)
 I=Q(sum(v[x]!=v[x^(1<<j)] for x in range(N) for j in range(n)),N)
 ck(a<=I)
 supp=[s for s,w in enumerate(W) if w];r=rank([s^supp[0] for s in supp])
 ck(rank([s for s in range(N) if cost[s]==0])==n-r)
 return H,I,a,r,cost,tuple(basis)
def phase(n,mask):
 monos=[sum(1<<j for j in js) for d in [2,3] for js in itertools.combinations(range(n),d)]
 return tuple((-1)**sum((x&m)==m for j,m in enumerate(monos) if mask&(1<<j)) for x in range(1<<n))
phase_n=3 if pilot else 4;phase_count=1<<(sum(1 for d in [2,3] for _ in itertools.combinations(range(phase_n),d)))
for mask in range(phase_count):
 P=phase(phase_n,mask);H,I,a,r,cost,basis=st(P);N=len(P)
 ck(sgn(add({2:Q(r)},H,-1))>=0);ck(a>=Q(r,4))
 for v in range(1,N):
  direct=Q(sum(P[x]!=P[x^v] for x in range(N)),N);m=min(direct,1-direct)
  ck(m==Q(cost[v],2*N*N));ck(m==0 or m>=Q(1,4))
 if mask%256==0:put('CHECKPOINT_PHASE.json',{'phase_classes':mask+1,'assertions':checks})
def root(seed):
 nd=4+(len(seed).bit_length()-1);out=[]
 for x in range(1<<(nd+6)):
  a,b,c,z=[(x>>j)&1 for j in range(4)]
  out.append(seed[(x>>4)&(len(seed)-1)]*(-1)**(a*b+a*c+b*c+z*a) if x>>nd==0 else 1)
 return tuple(out)
f=root([1] if pilot else[-1,1,1,1]);N=len(f);n=N.bit_length()-1
H0,I0,a0,r0,c0,_=st(f);delta=Q(f.count(-1),N);gamma=Q(1,4)-4*delta;K=Q(6)
ck(I0==a0);ck(delta<=Q(1,64));ck(K*gamma>1)
ck(all(Q(c,2*N*N)<=2*delta for c in c0))
products=0;rank_profile=Counter()
def check_product(P):
 global products
 hp,ip,ap,rp,cp,_=st(P);ck(all(c==0 or Q(c,2*N*N)>=Q(1,4) for c in cp))
 g=tuple(x*y for x,y in zip(f,P));hg,ig,ag,rg,cg,bg=st(g)
 ck(sgn(add(add(H0,{2:rp}),hg,-1))>=0)
 active=0
 for v in bg:
  if cp[v]:
   active+=1;ck(Q(cg[v]-c0[v],2*N*N)>=gamma)
  else:ck(cg[v]==c0[v])
 ck(active>=rp);ck(ag>=a0+rp*gamma)
 Ddiff=add(add(hg,H0,-1),{2:-K*(ag-a0)})
 ck(sgn(add({2:-rp*(K*gamma-1)},Ddiff,-1))>=0)
 ck(sgn(Ddiff)<=0)
 products+=1;rank_profile[rp]+=1
 return g,hg,ig,ag
triples=[(0,1,2)] if pilot else[(0,1,2),(6,7,8),(0,4,6)]
for js in triples:
 for mask in range(16):
  small=phase(3,mask)
  P=tuple(small[sum(((x>>j)&1)<<i for i,j in enumerate(js))] for x in range(N))
  g,hg,ig,ag=check_product(P)
  # Global input-coordinate parity is an output character; inspect its full reset cost.
  pc=tuple(P[x]*(-1)**(x.bit_count()%2) for x in range(N))
  gc,hc,ic,ac=check_product(pc)
  ck(hc==hg and ac==ag)
 put('CHECKPOINT_PRODUCTS.json',{'completed_triples':list(js),'products':products,'assertions':checks})
alignment=0
if not pilot:
 children=[tuple(f[(y<<2)|b] for y in range(N//4)) for b in range(4)]
 for branch in range(4):
  h=children[branch]
  for v in [0,1<<2,1<<3,1<<4,1<<6]:
   vv=v>>2
   Bv=sum(1-2*Q(sum(h[y]!=h[y^(1<<j)] for y in range(len(h))),len(h)) for j in range(n-2) if vv&(1<<j))
   C0=sum(Q(sum(children[branch^(1<<j)][y]*h[y] for y in range(len(h))),len(h)) for j in range(2))
   Cv=sum(Q(sum(children[branch^(1<<j)][y]*h[y]*(-1)**((vv&y).bit_count()%2) for y in range(len(h))),len(h)) for j in range(2))
   for sign in [-1,1]:
    P=tuple(sign*(-1)**((v&x).bit_count()%2) if x&3==branch else 1 for x in range(N))
    g,Hg,Ig,ag=check_product(P)
    bill=(Bv+C0-sign*Cv)/4
    ck(Ig-I0==bill)
    ck(sgn(add(add(Hg,H0,-1),{2:-K*bill}))<=0)
    alignment+=1
put('PILOT.json' if pilot else'CHECK.json',{'status':'PASS','pilot':pilot,'assertions':checks,'phase_classes':phase_count,'phase_dimension':phase_n,'physical_products':products,'original_pair_sign_comparisons':alignment,'root_dimension':n,'root_negative_mass':str(delta),'gamma':str(gamma),'K':str(K),'strict_margin_per_affine_rank':str(K*gamma-1),'rank_profile':dict(rank_profile),'elapsed_seconds':time.perf_counter()-start,'distinct_complete_tables':st.cache_info().currsize,'symmetry':'output affine characters only; explicit character-copy controls included'})
print(json.dumps({'status':'PASS','assertions':checks,'phase_classes':phase_count,'products':products,'alignment':alignment,'seconds':time.perf_counter()-start}))
