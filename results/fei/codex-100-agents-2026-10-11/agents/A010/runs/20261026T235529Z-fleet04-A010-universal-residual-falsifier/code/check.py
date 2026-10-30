from pathlib import Path
from fractions import Fraction as F
import json, time, sys, hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
OUT.mkdir(exist_ok=True)
PILOT='--pilot' in sys.argv
SPEC={'helper_version':'A010-independent-union-v1','family':'f=2 product_X OR(z0,z1,private pair) product_Y OR(z1,z2,private pair)-1', 'domain':[[1,1]] if PILOT else [[1,1],[1,2],[2,1],[2,2],[2,3],[3,2]],'case_count':1 if PILOT else 6,'symmetry':'none; swapped cases explicitly included','arithmetic':'integer Walsh, integer union DP, Fraction; ceiling logarithm upper certificate','memory_estimate_mb':90,'max_runtime_seconds':55,'scalar_domain':'all integer r,s from 4 through 64; induction covers larger values analytically'}
(ROOT/('PILOT_SPEC.json' if PILOT else 'FROZEN_SPEC.json')).write_text(json.dumps(SPEC,indent=2),encoding='utf-8')
start=time.perf_counter();checks=0
def ck(b):
 global checks
 checks+=1
 assert b
 if time.perf_counter()-start>55: raise RuntimeError('frozen deadline')
def fw(a):
 a=a[:];h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):a[k],a[k+h]=a[k]+a[k+h],a[k]-a[k+h]
  h*=2
 return a
def supports(r,s):
 return [3|(3<<(3+2*j)) for j in range(r)]+[6|(3<<(3+2*(r+j))) for j in range(s)]
def masks(v):
 a=[];u=v
 while u:a.append(u);u=(u-1)&v
 return a
def physical(r,s):
 ss=supports(r,s);n=3+2*(r+s);N=1<<n
 f=[1 if all(x&u for u in ss) else -1 for x in range(N)]
 a=fw(f);ck(sum(v*v for v in a)==N*N)
 inv=fw(a);ck(all(v==N*w for v,w in zip(inv,f)))
 specI=F(sum(v*v*k.bit_count() for k,v in enumerate(a)),N*N)
 edgeI=F(sum(f[x]!=f[x^(1<<j)] for x in range(N) for j in range(n)),N)
 ck(specI==edgeI)
 ax=F(3,4)**r;by=F(3,4)**s
 formula=F(5,4)-(ax+by)/4-3*ax*by/4+(r*ax*(1+by)+s*by*(1+ax))/6
 ck(specI==formula)
 mx=F(sum(v*v for k,v in enumerate(a) if k&sum(3<<(3+2*j) for j in range(r))),N*N)
 my=F(sum(v*v for k,v in enumerate(a) if k&sum(3<<(3+2*(r+j)) for j in range(s))),N*N)
 ck(mx==(1+by)*ax*(1-ax)/2);ck(my==(1+ax)*by*(1-by)/2)
 return ss,a,N,specI,mx,my
def law(r,s,ss):
 # Integer polynomial DP of the product mask law and its K-weighted law.
 mass={0:1};occ={0:0};den=1
 for j,u in enumerate(ss):
  size=r if j<r else s;D=30*size;p=D-15
  mm={};oo={}
  for x,v in mass.items():
   mm[x]=mm.get(x,0)+p*v;oo[x]=oo.get(x,0)+p*occ[x]
   for z in masks(u):
    k=x|z;mm[k]=mm.get(k,0)+v;oo[k]=oo.get(k,0)+occ[x]+v
  mass,occ=mm,oo;den*=D
 ck(sum(mass.values())==den);ck(sum(occ.values())==den);ck(occ[0]==0)
 return occ,den
def ceilcost(num,den):
 ck(num>0)
 k=max(0,(den//num).bit_length())
 while k and (num<<(k-1))>=den:k-=1
 ck((num<<k)>=den)
 return k
rows=[]
for r,s in SPEC['domain']:
 ss,a,N,I,mx,my=physical(r,s);q,D=law(r,s,ss)
 upper=sum(F(v*v,N*N)*ceilcost(q[k],D) for k,v in enumerate(a) if k and v)
 ck(upper<34*I)
 # Sectorwise witness bound for the same globally feasible source.
 for k,num in q.items():
  if not k:continue
  px=bool(k&sum(3<<(3+2*j) for j in range(r)))
  py=bool(k&sum(3<<(3+2*(r+j)) for j in range(s)))
  bound=(30*r)**r if px else 60
  bound*=((30*s)**s if py else 60)
  ck(num*bound>=D)
 rows.append({'r':r,'s':s,'truth_inputs':N,'I':str(I),'M_X':str(mx),'M_Y':str(my),'ceiling_cost_upper':str(upper),'normalized_reference':True})
if not PILOT:
 for r in range(4,257):
  a=F(3,4)**r;ck(a<F(1,3));ck(r*a<=F(81,64));ck(r*r*a<7)
  if r>=7:ck(3*(r+1)**2<=4*r*r)
 for r in range(4,65):
  for s in range(4,65):
   a=F(3,4)**r;b=F(3,4)**s
   I=F(5,4)-(a+b)/4-3*a*b/4+(r*a*(1+b)+s*b*(1+a))/6
   ck(I>F(5,4));mx=(1+b)*a*(1-a)/2;my=(1+a)*b*(1-b)/2
   upper=12+r*(5+r)*mx+s*(5+s)*my
   ck(upper<F(1429,48));ck(upper<24*I)
result={'status':'PASS','checks':checks,'rows':rows,'scalar_pairs':0 if PILOT else 3721,'seconds':time.perf_counter()-start,'proof_level':'exact finite certificates; all-parameter proof in REVIEW_AND_EXTENSION.md','spec':SPEC}
(OUT/('PILOT.json' if PILOT else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
