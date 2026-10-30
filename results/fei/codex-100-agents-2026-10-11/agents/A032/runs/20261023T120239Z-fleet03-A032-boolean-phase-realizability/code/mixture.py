from arith import *
from pathlib import Path
import json,time
root=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0;rows=[];minors=[]
def ck(x):
 global checks
 checks+=1;assert x,checks;assert time.perf_counter()-t0<55
def norm(v):ck(sum(v)==1);ck(all(x>=0 for x in v))
def determinant(m):
 m=[list(row) for row in m];ans=Q(1)
 for i in range(len(m)):
  pivot=next((j for j in range(i,len(m)) if m[j][i]),None)
  if pivot is None:return Q(0)
  if pivot!=i:m[pivot],m[i]=m[i],m[pivot];ans=-ans
  p=m[i][i];ans*=p
  for k in range(i,len(m)):m[i][k]/=p
  for j in range(i+1,len(m)):
   p=m[j][i]
   for k in range(i,len(m)):m[j][k]-=p*m[i][k]
 return ans
tau={2:Q(2),3:-Q(9,8)}
for r in [1,2]:
 n=3*r;N=1<<n
 p=[Q(1) for _ in range(N)]
 for s in range(N):
  for b in range(r):p[s]*=Q(9,16) if not((s>>(3*b))&7) else Q(1,16)
 norm(p)
 # Selected flattening minor: one row bit and two column bits per block.
 mat=[]
 for row in range(1<<r):
  line=[]
  for col in range(1<<r):
   label=sum((((row>>b)&1)|(((col>>b)&1)<<1))<<(3*b) for b in range(r))
   line.append(p[label])
  mat.append(line)
 det=determinant(mat);ck(det==Q(1,32)**(r*(1<<(r-1))))
 minors.append({'blocks':r,'matrix':mat,'determinant':det,'rank':1<<r})
 # Exact2^r product-mixture representation of the actual law.
 mix=[]
 for s in range(N):
  val=Q(0)
  for z in range(1<<r):
   prod=Q(1,1<<r)
   for b in range(r):prod*=Q(1,8) if z&(1<<b) else (1 if not((s>>(3*b))&7) else 0)
   val+=prod
  mix.append(val)
 ck(mix==p)
 pmarg=[influence(p,i) for i in range(n)];ck(pmarg==[Q(1,4)]*n)
 tc=add(*[(1,H([u,1-u])) for u in pmarg],(-1,H(p)));ck(tc==add((r,tau)))
 for M in [1,2,3]:
  comps=[]
  for z in range(M):
   u=[Q(1+((i+2*z)%3),4) for i in range(n)];q=[]
   for s in range(N):
    v=Q(1)
    for i,a in enumerate(u):v*=a if s&(1<<i) else 1-a
    q.append(v)
   norm(q);comps.append(q)
  q=[sum(v)/M for v in zip(*comps)];norm(q)
  joint=[[p[x]*comps[z][x]/(M*q[x]) for x in range(N)] for z in range(M)]
  pz=[sum(v) for v in joint];norm(pz);ck([sum(v) for v in zip(*joint)]==p)
  cond=[ [v/pz[z] for v in joint[z]] for z in range(M)]
  hmarg=[];Hcond={};TCcond={};product_residual={};blockMI=[];bitMI=[]
  for z in range(M):
   px=cond[z];norm(px);Hcond=add((1,Hcond),(pz[z],H(px)));localH={}
   for i in range(n):
    u=influence(px,i);localH=add((1,localH),(1,H([u,1-u])))
    target=Q(1+((i+2*z)%3),4)
    product_residual=add((1,product_residual),(pz[z],D([u,1-u],[target,1-target])))
   TCcond=add((1,TCcond),(pz[z],add((1,localH),(-1,H(px)))))
  for i in range(n):
   entropycond=add(*[(pz[z],H([influence(cond[z],i),1-influence(cond[z],i)])) for z in range(M)])
   bitMI.append(add((1,H([pmarg[i],1-pmarg[i]])),(-1,entropycond)))
  for b in range(r):
   blockmarg=[sum(p[x] for x in range(N) if ((x>>(3*b))&7)==s) for s in range(8)]
   bhcond={}
   for z in range(M):
    bp=[sum(cond[z][x] for x in range(N) if ((x>>(3*b))&7)==s) for s in range(8)]
    bhcond=add((1,bhcond),(pz[z],H(bp)))
   blockMI.append(add((1,H(blockmarg)),(-1,bhcond)))
  Iall=add((1,H(p)),(-1,Hcond))
  ck(TCcond==add((1,tc),*[(-1,v) for v in bitMI],(1,Iall)))
  ck(D(p,q)==add((1,TCcond),(1,D(pz,[Q(1,M)]*M)),(1,product_residual)))
  # Independently certify every mutual information as exact KL of its joint law.
  fulljoint=[v for row in joint for v in row];prodjoint=[pz[z]*p[x] for z in range(M) for x in range(N)]
  ck(Iall==D(fulljoint,prodjoint))
  rows.append({'blocks':r,'components':M,'KL':D(p,q),'TC_conditional':TCcond,'total_mutual_information':Iall,'block_MI':blockMI,'bit_MI':bitMI,'product_residual':product_residual,'mixture_weight_KL':D(pz,[Q(1,M)]*M),'posterior':joint})
ck(len(rows)==6);ck(3**3<2**5)
result={'PASS':True,'checks':checks,'seconds':time.perf_counter()-t0,'posterior_decompositions':6,'exact_rank_minors':minors,'decompositions':rows,'formal_status':'NOT_CLAIMED'}
(root/'out/mixture.json').write_text(json.dumps(enc(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['exact_rank_minors','decompositions']}))
