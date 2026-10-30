"""Frozen stage22 exact prime-completion verification; Python stdlib only."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
import hashlib, json, time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
OUT.mkdir(exist_ok=True)
SPEC={'helper_version':'A043-prime-completion-v3','family':'all essential ternary Boolean cores, signed threshold selector completions; fixed rational product laws','domain':'all masks 0..255, all 8 threshold reflections for candidate selection; four selected masks at four selector laws, one actual dyadic-jump control','case_count':{'all_masks':256,'essential_cores':218,'spectral_cases':16,'dyadic_jump_cases':4},'symmetry':'none; every labeled essential core tested','arithmetic':'Python integers and Fraction; no logarithmic sign assertion','memory_estimate_mb':35,'max_runtime_seconds':55,'automatic_dimension_escalation':False}
(OUT/'frozen_spec.json').write_text(json.dumps(SPEC,indent=2)+'\n',encoding='utf-8')
START=time.perf_counter()
checks=0
def ck(x):
 global checks
 checks+=1
 assert x,checks
 assert time.perf_counter()-START<55,'frozen time cap'
def essential(a,n):
 return all(any(a[x]!=a[x^(1<<i)] for x in range(1<<n)) for i in range(n))
def rows(a,n,B):
 C=[i for i in range(n) if i not in B]
 return {tuple(a[sum(((u>>j)&1)<<i for j,i in enumerate(B))+sum(((v>>j)&1)<<i for j,i in enumerate(C))] for v in range(1<<len(C))) for u in range(1<<len(B))}
def prime(a,n):
 return essential(a,n) and all(len(rows(a,n,B))>=3 for k in range(2,n) for B in combinations(range(n),k))
def tab(mask,n): return tuple(1 if (mask>>x)&1 else -1 for x in range(1<<n))
def moments(a,p):
 n=len(p); v=[4*x*(1-x) for x in p]; mass={}; c={}
 # Direct physical expectation in the orthogonal centered basis.
 for S in range(1<<n):
  num=F(0); den=F(1)
  for i in range(n):
   if S>>i&1:den*=v[i]
  for x in range(1<<n):
   t=F(a[x])
   for i,pi in enumerate(p):
    bit=x>>i&1;t*=pi if bit else 1-pi
    if S>>i&1:t*=2*(bit-pi)
   num+=t
  c[S]=num/den;mass[S]=num*num/den
 ck(sum(mass.values())==1)
 return c,mass
def j(t):
 t=abs(t);k=0
 if not t:return 0
 while t<=F(1,2):t*=2;k+=1
 ck(F(1,2)<t<=1)
 return k
def jhi(c,P):return sum((P[S]*j(c[S]) for S in c if S.bit_count()>=2),F(0))
base=tuple(1 if x.bit_count()>=2 else -1 for x in range(8))
qset=[tuple(base[x^s] for x in range(8)) for s in range(8)]
ck(len(set(qset))==8)
for q in qset:ck(prime(q,3))
cert=[]; selected={}
for mask in range(256):
 a=tab(mask,3)
 if not essential(a,3):continue
 forbidden={a,tuple(-t for t in a)}|{tuple(a[x^(1<<i)] for x in range(8)) for i in range(3)}
 choices=[(s,q) for s,q in enumerate(qset) if q not in forbidden]
 ck(bool(choices));s,q=choices[0]
 g=a+q
 ck(essential(g,4))
 counts=[len(rows(g,4,B)) for k in range(2,4) for B in combinations(range(4),k)]
 ck(min(counts)>=3)
 # Independently create selector truth table, rather than concatenation.
 ck(g==tuple(a[x&7] if not (x&8) else base[(x&7)^s] for x in range(16)))
 cert.append({'core_mask':mask,'threshold_reflection':s,'proper_block_row_counts':counts})
 if mask in (1,23,150,254):selected[mask]=(a,q,g)
ck(len(cert)==218);ck(len(selected)==4)
spectral=[]
for mask,(a,q,g) in selected.items():
 p=[F(1,3),F(2,5),F(3,4)]
 ca,pa=moments(a,p);cb,pb=moments(q,p)
 for e in (F(1,2),F(1,8),F(1,64),F(1,1024)):
  cg,pg=moments(g,p+[e]);v=4*e*(1-e)
  for S in range(8):
   ck(cg[S]==(1-e)*ca[S]+e*cb[S])
   ck(cg[S|8]==(cb[S]-ca[S])/2)
   vs=F(1)
   for i in range(3):
    if S>>i&1:vs*=4*p[i]*(1-p[i])
   ck(pg[S|8]==e*(1-e)*vs*(cb[S]-ca[S])**2)
  ck(sum(pg[S|8] for S in range(8))==e*(1-e)*sum((pa[S]+pb[S]-2*ca[S]*cb[S]*(__import__('functools').reduce(lambda x,i:x*4*p[i]*(1-p[i]),[i for i in range(3) if S>>i&1],F(1)))) for S in range(8)))
  spectral.append({'mask':mask,'epsilon':str(e),'Delta':str(sum((S.bit_count()-1)*pg[S] for S in range(1,16))),'Jhi_over_ln4':str(jhi(cg,pg))})
# Actual prime completion has a discontinuous high-scale boundary.
a,q,g=selected[1];ck(q==base)
ca,pa=moments(a,[F(1,2)]*3);ck(jhi(ca,pa)==F(1,2))
for e in (F(1,8),F(1,64),F(1,1024),F(1,65536)):
 cg,pg=moments(g,[F(1,2)]*3+[e])
 ck(cg[7]==-(1+e)/4);ck(j(cg[7])==1)
 old=sum((pg[S]*j(cg[S]) for S in range(8) if S.bit_count()>=2),F(0))
 ck(old==(6*(1-e)**2+(1+e)**2)/16)
 ck(old<F(1,2))
 total=jhi(cg,pg)
 ck(total==(7+29*e-32*e*e)/16)
 ck((total<F(1,2)) if e<=F(1,64) else (total>F(1,2)))
# Scalar controls also check both directions of each dyadic boundary.
for k in (1,2,3,8):
 t=F(1,2**k);e=F(1,2**(k+4))
 ck(j(t)==k);ck(j(t+e)==k-1);ck(j(t-e)==k)
# Essentiality guard: dummy third input f = restriction q|x3=0.
q=base; f=tuple(q[x&3] for x in range(8));g=f+q
ck(not essential(f,3));ck(q!=f and q!=tuple(-t for t in f))
ck(all(q!=tuple(f[x^(1<<i)] for x in range(8)) for i in range(3)))
ck(len(rows(g,4,(2,3)))==2);ck(not prime(g,4))
result={'status':'PASS','assertions':checks,'cores':len(cert),'spectral_cases':len(spectral),'seconds':time.perf_counter()-START,'claim_scope':'finite exact verification; all-n implication is in PROOF.md','certificates':cert,'spectral':spectral}
(OUT/'exact_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ('status','assertions','cores','spectral_cases','seconds')}))
