"""A096 stage20 v1. Exact Boolean/occupied-label/normalizer verifier."""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
start=time.perf_counter(); checks=0; nodes=0; leaves_n=0; proper=0
mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'; cap=55 if mode=='pilot' else 180
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
 if checks%1024==0 and time.perf_counter()-start>cap:raise TimeoutError(cap)
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def walsh(v):
 a=list(v); k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(i,i+k):a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return [F(x,len(v)) for x in a]
def delete(s,j):return (s&((1<<j)-1))|((s>>(j+1))<<j)
def restrict(v,j,t):
 return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(t<<j)] for x in range(len(v)//2)]
def law(v):return [x*x for x in walsh(v)]
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1]
def wrapper(v,sgn):return [a[c]+sgn*(1-a[c]**2)*v[t] for t in range(len(v)) for c in range(16)]
def iso(v,j):
 f=walsh(v)
 return all(f[s]*f[s|(1<<j)]==0 for s in range(len(v)) if not s&(1<<j))
def tree(v,coords,first,path=()):
 global nodes,leaves_n
 nodes+=1
 order=([first] if first in coords else [])+[c for c in coords if c!=first]
 # Keep the FULL signed wrapper isospectral too: seed singleton must be zero.
 eligible=[c for c in order if iso(v,coords.index(c)) and walsh(v)[1<<coords.index(c)]==0]
 if not eligible:
  leaves_n+=1;return [(F(1,2**len(path)),v,coords,path)]
 c=eligible[0]; j=coords.index(c); p=law(v)
 for t in (0,1):
  pc=law(restrict(v,j,t))
  for s in range(len(p)):
   if p[s]:ck(pc[delete(s,j)]==p[s])
  ck(sum(pc)==1)
 out=[]
 for t in (0,1):out+=tree(restrict(v,j,t),tuple(x for x in coords if x!=c),-1,path+((c,t),))
 return out
def maskmap(s,coords):
 return sum(((s>>c)&1)<<j for j,c in enumerate(coords))
seeds=list(range(256)) if mode=='main' else [0,1,126,150]
policies=0; nontrivial=0; ghost=0; penalty=0
for truth in seeds:
 v=[1-2*((truth>>x)&1) for x in range(8)]
 for first in range(3):
  ls=tree(v,(0,1,2),first); ck(sum(x[0] for x in ls)==1)
  if len(ls)>1:nontrivial+=1
  for sign in (-1,1):
   policies+=1; P=law(wrapper(v,sign)); support=[s for s,x in enumerate(P) if x]
   ck(sum(P)==1); ck(all(x in (-1,1) for x in wrapper(v,sign)))
   N=max(w.denominator for w,_,_,_ in ls); rows=[]
   for w,child,coords,path in ls:
    pc=law(wrapper(child,sign)); ck(sum(pc)==1)
    target=(sum((c+1)*(t+1) for c,t in path)+first)%len(pc)
    q=[F(7,8)*p+F(1,16*len(pc))+(F(1,16) if s==target else 0) for s,p in enumerate(pc)]
    ck(sum(q)==1); pull={}
    for s in support:
     z=(s&15)|(maskmap(s>>4,coords)<<4); ck(pc[z]==P[s]); ck(q[z]>0); pull[s]=q[z]
    ck(len(set((s&15)|(maskmap(s>>4,coords)<<4) for s in support))==len(support))
    ck(sum(pull.values())<=1)
    if sum(pull.values())<1:ghost+=1
    rows.append((w,pull))
   # G(S)^N is rational. Weighted AM-GM is checked without floating roots.
   asum=F(0)
   for s in support:
    product=F(1); am=F(0)
    for w,q in rows:
     product*=q[s]**int(w*N);am+=w*q[s]
    ck(product>0);ck(product<=am**N);asum+=am
    if product<am**N:penalty+=1
   ck(asum<=1)
# Independently exhaust the exact all-coordinate phase-null census n=0,1,2,3.
census={}
for n in range(4):
 allnull=nonflat=0
 for truth in range(1<<(1<<n)):
  v=[1-2*((truth>>x)&1) for x in range(1<<n)]
  if all(iso(v,j) for j in range(n)):
   allnull+=1; p=law(v)
   if sum(x>0 for x in p)>1:nonflat+=1
 census[str(n)]={'tables':1<<(1<<n),'all_coordinate_null':allnull,'nonflat':nonflat}
 if n<3:ck(nonflat==0)
ck(census['3']['nonflat']>0)
# A085 arbitrary-core depth: independently build literal parity blocks, all16 two-bit cores.
depth_cases=0
for truth in range(16):
 core=[1-2*((truth>>x)&1) for x in range(4)]; L=3
 v=[core[((x&7).bit_count()%2)|((((x>>3)&7).bit_count()%2)<<1)] for x in range(64)]
 pg=law(core);ph=law(v)
 ck(sum(pg)==sum(ph)==1)
 ck(sum(F(s.bit_count())*p for s,p in enumerate(ph))==L*sum(F(s.bit_count())*p for s,p in enumerate(pg)))
 ck(sorted(p for p in ph if p)==sorted(p for p in pg if p))
 for j in range(6):
  ck(iso(v,j))
  for t in (0,1):
   child=restrict(v,j,t)
   for k in range(5):ck(iso(child,k))
  depth_cases+=1
# Exact nonzero-normalizer witness, with no numerical logarithm used for the sign.
v=[-1 if x in (0,7) else 1 for x in range(8)];p=law(v); supp=[s for s,x in enumerate(p) if x]
ck(supp==[0,3,5,6]);ck(all(p[s]==F(1,4) for s in supp));ck(iso(v,0))
qp=[F(x,8) for x in (3,3,1,1)];qm=[F(x,8) for x in (1,1,3,3)]
ck(sum(qp)==sum(qm)==1)
ck(all(qp[k]*qm[k]==F(3,64) for k in range(4)))
ck(4>3)
for t in (0,1):ck(law(restrict(v,0,t))==[F(1,4)]*4)
save('NORMALIZER_WITNESS.json',{'actual_truth':v,'support':supp,'root_probability':'1/4','both_child_probability':'1/4','full_targets':['(3,3,1,1)/8','(1,1,3,3)/8'],'root_effective_KL':'0','Z':'sqrt(3)/2','complete_signed_debit_bits':'log2(4/3)/2','exact_sign_certificate':'4 > 3','target_necessity':'NOT claimed'})
result={'helper_version':'stage20-v1','mode':mode,'status':'PASS','seed_truth_tables':len(seeds),'full_wrapper_policies':policies,'nontrivial_seed_trees':nontrivial,'visited_seed_nodes':nodes,'retained_seed_leaves':leaves_n,'ghost_leaf_occurrences':ghost,'strict_AMGM_atom_occurrences':penalty,'A085_depth_cases':depth_cases,'phase_null_census':census,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh, Fraction, rational weighted-AMGM powers; no floating sign','peak_memory':'unmeasured; estimated below120MB'}
save('VALIDATION.json' if mode=='main' else 'PILOT.json',result);print(json.dumps(result))
