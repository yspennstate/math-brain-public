from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
import itertools,json,time,sys
RUN=Path(__file__).resolve().parents[1]; START=time.monotonic(); CHECKS=0
def need(v,s):
 global CHECKS
 CHECKS+=1
 if not v: raise AssertionError(s)
 if CHECKS%4096==0 and time.monotonic()-START>55: raise TimeoutError('frozen 55s cap')
def walsh(v):
 a=list(v);s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for i in range(j,j+s):a[i],a[i+s]=a[i]+a[i+s],a[i]-a[i+s]
  s*=2
 return a
def degree(v):
 a=list(v)
 for i in range(len(v).bit_length()-1):
  for x in range(len(v)):
   if x>>i&1:a[x]^=a[x^(1<<i)]
 return max([x.bit_count() for x,b in enumerate(a) if b]+[0])
@lru_cache(None)
def ln_interval(x):
 z=(x-1)/(x+1);z2=z*z;p=z;s=Q(0)
 for j in range(14):s+=2*p/(2*j+1);p*=z2
 return s,s+2*p/(29*(1-z2))
@lru_cache(None)
def log_interval(x):
 e=0
 while x<1:x*=2;e-=1
 while x>=2:x/=2;e+=1
 lo,hi=ln_interval(x);a,b=ln_interval(Q(2))
 return e+lo/b,e+hi/a
@lru_cache(None)
def atom_upper(p):
 if not p:return Q(0)
 return p*log_interval(1/p)[1]
def row(v,k,check_anf=False):
 N=len(v);n=N.bit_length()-1;mu_n=sum(x*x for x in v)
 if not mu_n:return (Q(0),Q(0),Q(0),Q(0))
 a=[int(x!=0) for x in v];b=[int(x==-1) for x in v]
 if check_anf:
  need(degree(a)<=k,'support degree');need(degree(b)<=k+2,'negative bit degree')
 W=walsh(v);counts=Counter(w*w for w in W if w)
 need(sum(s*c for s,c in counts.items())==N*mu_n,'row Parseval')
 E_num=[]
 for i in range(n):
  r=sum((v[x]-v[x^(1<<i)])**2 for x in range(N));E_num.append(r)
  if r:need(r*(1<<(k+1))>=4*N,'absolute influence gap')
  need(r*N==4*sum(w*w for s,w in enumerate(W) if s>>i&1),'physical/Walsh energy')
  if check_anf and r:
   da=[a[x]^a[x^(1<<i)] for x in range(N)]
   if any(da):
    need(k>=1 and degree(da)<=k-1,'support derivative degree')
    need(sum(da)*(1<<(k-1))>=N,'support derivative minimum weight')
   else:
    db=[b[x]^b[x^(1<<i)] for x in range(N)]
    need(degree(db)<=k+1,'negative derivative degree')
    need(r==4*sum(db),'exact invariant-support derivative')
 E=Q(sum(E_num),4*N);mu=Q(mu_n,N)
 Hfull=sum(c*atom_upper(Q(s,N*N)) for s,c in counts.items())
 Hcond=sum(c*mu*atom_upper(Q(s,N*mu_n)) for s,c in counts.items())
 mass=atom_upper(mu)
 need(mass<=2*E,'mass entropy same energy')
 need(Hcond<=Q(2*k+5,2)*E,'conditional complete row inequality')
 need(Hfull<=Q(2*k+9,2)*E,'full complete row inequality')
 return E,Hfull,Hcond,mu
def ternary():
 total=0;minimum={}
 for n in range(4):
  N=1<<n
  for v in itertools.product((-1,0,1),repeat=N):
   a=[int(x!=0) for x in v];b=[int(x==-1) for x in v]
   k=max(degree(a),degree(b)-2,0)
   row(v,k,True);total+=1
  minimum[str(n)]=3**N
 return {'ternary_rows':total,'by_n':minimum}
def restrictions(n,upto=None):
 for state in itertools.product((-1,0,1),repeat=n):
  if upto is None or sum(t!=-1 for t in state)<=upto:yield state
def assignment(state,z):
 result=0;j=0
 for i,v in enumerate(state):
  if v==-1:v=z>>j&1;j+=1
  result|=v<<i
 return result
def fixture(ny,limited=False):
 total=0;ranks=Counter();witness=None
 for xs in restrictions(3):
  xf=[i for i,t in enumerate(xs) if t==-1]
  for ys in restrictions(ny,2 if limited else None):
   nf=ys.count(-1);N=1<<nf;rows={};cells=Counter()
   for z in range(N):
    y=assignment(ys,z);t=0
    while t<7 and y>>t&1:t+=1
    cells[t]+=1;label=sum(((t>>i)&1)<<j for j,i in enumerate(xf))
    fixed=sum((t>>i&1)*v for i,v in enumerate(xs) if v!=-1)&1
    q=int(t==7 and ny==9 and y>>7&1 and y>>8&1)
    v=rows.setdefault(label,[0]*N);v[z]=1-2*(q^fixed)
   k=max(nf-(c.bit_length()-1) for c in cells.values())
   need(all(c&(c-1)==0 for c in cells.values()),'restricted affine cells')
   need(k<=7 and k<=len(cells)-1,'codim and dyadic partition count')
   ledger=[row(v,k,False) for v in rows.values()]
   E=sum(a[0] for a in ledger);H=sum(a[1] for a in ledger);HC=sum(a[2] for a in ledger)
   need(sum(a[3] for a in ledger)==1,'Boolean partition normalization')
   need(H<=Q(23,2)*E,'full eight-cell theorem')
   need(HC<=Q(19,2)*E,'full conditional eight-cell theorem')
   ranks[len(xf)]+=1;total+=1
   if ny==9 and xs==(-1,0,0) and ys==(-1,)*9:
    witness={'row_masses':[str(a[3]) for a in ledger],'energy':str(E),'full_entropy_upper':str(H),'conditional_entropy_upper':str(HC),'cell_sizes':dict(cells)}
    need(sorted(a[3] for a in ledger)==[Q(43,128),Q(85,128)],'genuine four-cell masses')
    need(all(a[3].numerator.bit_count()==4 for a in ledger),'no two-cell coarsening')
 return {'states':total,'by_free_X':dict(ranks),'proper_four_cell_witness':witness}
def masses():
 profiles={}
 def visit(left,previous,parts,m):
  if not left:
   need(max(parts,default=0)<=len(parts)-1,'dyadic cover exponent bound')
   profiles[m]+=1;return
  if len(parts)==m:return
  for exponent in range(previous,m):
   mass=Q(1,1<<exponent)
   if mass<=left:visit(left-mass,exponent,parts+[exponent],m)
 for m in range(1,9):profiles[m]=0;visit(Q(1),0,[],m)
 # Sharp degree9 tensor guard at eight cells, independent ANF check.
 bits=[int((y&127)==127 and y>>7&1 and y>>8&1) for y in range(512)]
 need(degree(bits)==9,'sharp admitted degree9 phase')
 # Direct character sums verify a nonaffine proper support independently of FWT.
 support=[int(next((j for j in range(7) if not(y>>j&1)),7)%2==0) for y in range(128)]
 W=[sum(v*(1-2*((s&y).bit_count()&1)) for y,v in enumerate(support)) for s in range(128)]
 need(W==walsh(support),'direct proper-support character certificate')
 need(sum(support)==85,'proper support cardinality')
 return {'dyadic_profiles_up_to_m':profiles,'sharp_tensor_degree':9,'direct_support_mass':'85/128'}
def direct():
 for k in range(8):
  n=k+2;N=1<<n
  v=[(1-2*int(y>>k&1 and y>>(k+1)&1)) if (y&((1<<k)-1))==((1<<k)-1) else 0 for y in range(N)]
  for i in range(n):
   p=Q(sum((v[y]-v[y^(1<<i)])**2 for y in range(N)),4*N)
   need(p==Q(1,1<<(k+1)),'absolute gap sharp for every coordinate')
  row(v,k,True)
 for xs in restrictions(3):
  xf=[i for i,t in enumerate(xs) if t==-1];r=len(xf);N=512;rows={};values=[]
  for y in range(N):
   t=next((j for j in range(7) if not(y>>j&1)),7)
   label=sum((t>>i&1)<<j for j,i in enumerate(xf))
   fixed=sum((t>>i&1)*v for i,v in enumerate(xs) if v!=-1)&1
   q=int(t==7 and y>>7&1 and y>>8&1)
   rows.setdefault(label,[0]*N)[y]=1-2*(fixed^q)
  for y in range(N):
   t=next((j for j in range(7) if not(y>>j&1)),7)
   q=int(t==7 and y>>7&1 and y>>8&1)
   for x in range(1<<r):
    fullx=assignment(xs,x)
    values.append(1-2*(q^((fullx&t).bit_count()&1)))
  W=walsh(values);Ws={j:walsh(v) for j,v in rows.items()}
  scale=1<<r
  for s,w in enumerate(W):
   j=s&(scale-1);t=s>>r
   need(w==scale*(Ws[j][t] if j in Ws else 0),'direct full-F Walsh/row factor')
  Efull=Q(sum((s>>r).bit_count()*w*w for s,w in enumerate(W)),len(values)**2)
  Erows=sum(row(v,7,False)[0] for v in rows.values())
  need(Efull==Erows,'direct full-F original IY ledger')
  need(sum(w*w for w in W)==len(values)**2,'direct full-F Boolean Parseval')
 return {'full_F_X_restrictions':27,'gap_sharp_rows':8}
mode=sys.argv[1]
result={'helper':'A034-stage19-check-v1','mode':mode}
if mode=='ternary':result.update(ternary())
elif mode=='fixture7':result.update(fixture(7))
elif mode=='fixture9':result.update(fixture(9,True))
elif mode=='masses':result.update(masses())
elif mode=='direct':result.update(direct())
else:raise ValueError(mode)
result.update(assertions=CHECKS,seconds=time.monotonic()-START,status='PASS')
out=RUN/'out';out.mkdir(exist_ok=True)
(out/(mode+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k not in ('proper_four_cell_witness',)}))
