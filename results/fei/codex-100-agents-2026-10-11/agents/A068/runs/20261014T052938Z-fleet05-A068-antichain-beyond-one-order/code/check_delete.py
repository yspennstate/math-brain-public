import json,itertools,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from time import perf_counter
start=perf_counter();checks=0;pilot='--pilot' in sys.argv
def ck(b):
 global checks
 assert b
 checks+=1
 if checks%100000==0:assert perf_counter()-start<(55 if pilot else 170)
def fw(v):
 a=list(v);k=1
 while k<len(a):
  for i in range(0,len(a),2*k):
   for j in range(i,i+k):a[j],a[j+k]=a[j]+a[j+k],a[j]-a[j+k]
  k*=2
 return a
def edges(v):
 n=(len(v)-1).bit_length()
 return [sum(v[u]!=v[u^(1<<i)] for u in range(len(v)) if not u>>i&1) for i in range(n)]
def phase(f):
 return [(-1)**((f&1)^((f>>1&1)*(z&1))^((f>>2&1)*(z>>1&1))^((f>>3&1)*(z&1)*(z>>1&1))) for z in range(4)]
ph=[phase(f) for f in range(16)];pa=[fw(p) for p in ph];rank=[2 if f&8 else 0 for f in range(16)]
def primitive(y):
 t=(F(y)-1)/(F(y)+1)
 l=2*sum((t**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
 return l,l+2*t**41/(41*(1-t*t))
l2,u2=primitive(2)
@lru_cache(None)
def log2(v):
 v=F(v);k=0
 while v>=2:v/=2;k+=1
 while v<1:v*=2;k-=1
 lo,hi=primitive(v);lo=F(k)+lo/u2;hi=F(k)+hi/l2
 den=1<<72
 def floor(a):return (a*den).numerator//(a*den).denominator
 return F(floor(lo),den),F(-floor(-hi),den)
def entropy(a):
 den=len(a)**2;l=u=F(0)
 for v in a:
  if v:
   p=F(v*v,den);lo,hi=log2(1/p);l+=p*lo;u+=p*hi
 return l,u
def reference(a):
 n=(len(a)-1).bit_length();den=1<<(2*n)
 weights=[F(sum(a[s]**2 for s in range(1<<n) if s.bit_count()==k),den) for k in range(n+1)]
 raw=[F(1) for _ in a]
 for s in range(len(a)):
  for i in range(n):
   if s>>i&1:raw[s]/=(i+1)**2
 z=[sum((raw[s] for s in range(len(a)) if s.bit_count()==k),F(0)) for k in range(n+1)]
 r=[weights[s.bit_count()]*raw[s]/z[s.bit_count()] for s in range(len(a))]
 ck(sum(r)==1)
 l=u=F(0)
 for s,v in enumerate(a):
  if v:
   ck(r[s]>0);lo,hi=log2(1/r[s]);l+=F(v*v,den)*lo;u+=F(v*v,den)*hi
 return r,l,u
for f in range(16):
 values=[b*b for b in pa[f] if b]
 ck(len(values)==1<<rank[f])
 ck(all(b==16//(1<<rank[f]) for b in values))
 ck(rank[f]*16<=2*sum(i.bit_count()*b*b for i,b in enumerate(pa[f])))

profiles=[((3,2,2,1),1),((1,3,2,1),1),((2,2,2,1),1),((1,1),2),((4,4,1,1,1),0),((3,3,1,1,1),2)]
core_cert=[];constant_cases=0;row_admitted=0;row_not_admitted=0;first_nonproduct=None
parent_count=child_count=0;transcript=hashlib.sha256();strong_count=0
def product_test(v):
 total=sum(v)
 if not total:return True,None
 n=(len(v)-1).bit_length()
 marg=[sum(x for s,x in enumerate(v) if s>>i&1) for i in range(n)]
 def prod(xs):
  out=1
  for x in xs:out*=x
  return out
 isp=all(v[s]*total**(n-1)==prod(marg[i] if s>>i&1 else total-marg[i] for i in range(n)) for s in range(len(v)))
 nonfair=sum(0<x<total and 2*x!=total for x in marg)
 if isp and nonfair<=1:return True,None
 minor=None
 if not isp:
  for i in range(n):
   def insert(t,b):return (t&((1<<i)-1))|((t>>i)<<(i+1))|(b<<i)
   for a,b in itertools.combinations(range(1<<(n-1)),2):
    entries=[v[insert(a,0)],v[insert(b,0)],v[insert(a,1)],v[insert(b,1)]]
    det=entries[0]*entries[3]-entries[1]*entries[2]
    if det:
     minor=dict(coordinate=i,other_indices=[a,b],matrix=entries,determinant=det);break
   if minor:break
 return False,dict(squares=v,total=total,marginal_numerators=marg,product=isp,nonfair_varying_coordinates=nonfair,minor=minor)

for pi,(weights,theta) in enumerate(profiles):
 q=len(weights);nd=q-1;nparent=q+2;nchild=q+1
 h=[1 if sum(w*(-1)**(u>>i&1) for i,w in enumerate(weights))>=theta else -1 for u in range(1<<q)]
 old=fw(h);coreH=entropy(old);templates={}
 for eps in (1,-1):
  newweights=(weights[0]+eps*weights[1],)+weights[2:]
  active=sorted((i for i,w in enumerate(newweights) if w),key=lambda i:(-abs(newweights[i]),i))
  r=len(active)
  hc=[1 if sum(abs(newweights[i])*(-1)**(u>>j&1) for j,i in enumerate(active))>=theta else -1 for u in range(1<<r)]
  ac=fw(hc);ref,glo,ghi=reference(ac)
  ih=F(sum(s.bit_count()*b*b for s,b in enumerate(ac)),1<<(2*r))
  ck(ghi<=8*ih)
  ht=entropy(ac)
  templates[eps]=dict(active=active,newweights=newweights,core=hc,raw=ac,ref=ref,glo=glo,ghi=ghi,ih=ih,H=ht)
  core_cert.append(dict(profile=pi,weights=weights,theta=theta,tag_sign=eps,merged_weight=newweights[0],active_physical_data=active,compiled_ordered_abs_weights=[abs(newweights[i]) for i in active],compiled_raw_coefficients=ac,reference_masses=list(map(str,ref)),I_data=str(ih),entropy_interval=list(map(str,ht)),complete_data_reference_cost_interval=[str(glo),str(ghi)],margin_to_8I_lower=str(8*ih-ghi)))
 if q==5:tuples=[(f,8,6,3) for f in range(16)]
 else:tuples=itertools.product(range(16),repeat=q-1)
 if pilot:tuples=itertools.islice(tuples,2)
 for flags in tuples:
  origflags=(flags[0],flags[0])+tuple(flags[1:])
  values=[]
  for z in range(4):
   flips=sum((ph[origflags[i]][z]==-1)<<i for i in range(q))
   for u in range(1<<q):
    latent=u^(((u>>0)&1)<<1)
    # latent bit1=x1 xor tag; all other bits unchanged.
    values.append(h[latent^flips])
  parent=fw(values)
  parent_tag=sum(b*b for s,b in enumerate(parent) if s&2)
  old_d=sum(b*b for s,b in enumerate(old) if s&2)
  ck(parent_tag*(1<<(2*q))==old_d*(1<<(2*nparent)))
  ed=edges(values);ck(parent_tag==ed[1]*(1<<(nparent+1)))
  old_rank=0
  for s,b in enumerate(old):
   f=0
   for i in range(q):
    if s>>i&1:f^=origflags[i]
   old_rank+=b*b*rank[f]
  new_ranks=[]
  for eps in (1,-1):
   tmpl=templates[eps];active=tmpl['active'];ac=tmpl['raw'];r=len(active)
   out=[]
   for z in range(4):
    for u in range(1<<nd):
     source_u=(u&1)|((eps==-1)<<1)|((u>>1)<<2)
     out.append(values[(z<<q)|source_u])
   b=fw(out)
   for s in range(1<<nchild):
    data=s&((1<<nd)-1);zmask=s>>nd
    oldmask=(data&1)|((data>>1)<<2)|(zmask<<q)
    ck(2*b[s]==parent[oldmask]+eps*parent[oldmask|2])
   ff=[flags[i]^(tmpl['newweights'][i]<0) for i in active]
   phaseflags=[];rn=0
   for s in range(1<<r):
    f=0
    for j in range(r):
     if s>>j&1:f^=ff[j]
    phaseflags.append(f);rn+=ac[s]*ac[s]*rank[f]
    physical_s=sum(((s>>j)&1)<<i for j,i in enumerate(active))
    for t in range(4):
     ck(b[physical_s|(t<<nd)]==ac[s]*pa[f][t]*(1<<(nd-r)))
   unused=set(range(nd))-set(active)
   ck(all(not b[s] for s in range(len(b)) if any(s>>i&1 for i in unused)))
   for z in range(4):
    for u in range(1<<nd):
     t=sum((((u>>i)&1)^(ph[ff[j]][z]==-1))<<j for j,i in enumerate(active))
     ck(out[(z<<nd)|u]==tmpl['core'][t])
   den=1<<(2*nchild)
   ix=sum((s&((1<<nd)-1)).bit_count()*a*a for s,a in enumerate(b))
   iz=sum((s>>nd).bit_count()*a*a for s,a in enumerate(b))
   ck(sum(a*a for a in b)==den)
   ck(F(ix,den)==tmpl['ih'])
   ec=edges(out)
   ck(ix==sum(ec[:nd])*(1<<(nchild+1)))
   ck(iz==sum(ec[nd:])*(1<<(nchild+1)))
   ck(rn*den<=2*iz*(1<<(2*r)))
   ck(tmpl['ghi']+F(rn,1<<(2*r))<=F(8*ix+2*iz,den))
   # Each affine factor sums to1, already checked for all16 phases.
   ck(sum(tmpl['ref'])==1)
   if tmpl['ih']==0:
    ck(tmpl['ghi']==0 and iz==0 and b[0]**2==den)
    constant_cases+=1
   admitted=True
   for j in range(4):
    squares=[b[j|(t<<2)]**2 for t in range(1<<(nchild-2))]
    ok,certificate=product_test(squares)
    if not ok:
     admitted=False
     if first_nonproduct is None and not certificate['product']:
      first_nonproduct=dict(profile=pi,weights=weights,theta=theta,tag_sign=eps,control_flags=flags,physical_bit_order=['merged_x']+['data'+str(i+3) for i in range(q-2)]+['z0','z1'],address_coordinates=[0,1],address_frequency=j,row_certificate=certificate,actual_truth_table=out,raw_Fourier_coefficients=b)
   row_admitted+=admitted;row_not_admitted+=not admitted
   new_ranks.append(F(rn,1<<(2*r)))
   transcript.update(json.dumps([pi,list(flags),eps,b,ix,iz,rn],separators=(',',':')).encode())
   child_count+=1
  ck(F(old_rank,1<<(2*q))==sum(new_ranks)/2)
  if q==5:
   # Strong pair: data-only node decrement2 independently of control phases.
   hp=templates[1]['H'];hm=templates[-1]['H']
   dlo=coreH[0]-(hp[1]+hm[1])/2;dhi=coreH[1]-(hp[0]+hm[0])/2
   ck(dlo<=2<=dhi)
   ck(F(old_d,1<<(2*q))==F(1,2))
   strong_count+=1
  parent_count+=1
result=dict(status='PASS',helper_version=1,pilot=pilot,parent_cases=parent_count,child_cases=child_count,compiled_core_cases=len(core_cert),constant_output_cases=constant_cases,strong_pair_node_cases=strong_count,canonical_A079_admitted_cases=row_admitted,canonical_A079_not_admitted_cases=row_not_admitted,first_nonproduct_row=first_nonproduct,core_certificates=core_cert,exact_assertions=checks,runtime_seconds=perf_counter()-start,case_transcript_sha256=transcript.hexdigest(),arithmetic='Integer actual Boolean Walsh/edge/coherent restriction; Fraction references; outward20-term dyadic72 logs; exact phase-rank conservation and product minors',all_parameter_bridge='Analytic constant-relative-phase threshold recompile; arbitrary relative quadratic phase remains open')
run=Path(__file__).resolve().parents[1]
(run/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['core_certificates','first_nonproduct_row']}))

