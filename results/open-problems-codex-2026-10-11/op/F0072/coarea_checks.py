from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parent
def model(coords,d=2):
 idx={p:i for i,p in enumerate(coords)}; n=len(coords); adj=[0]*n
 for p,i in idx.items():
  for j in range(d):
   q=list(p);q[j]+=1;q=tuple(q)
   if q in idx:
    k=idx[q];adj[i]|=1<<k;adj[k]|=1<<i
 return adj,[2*d]*n,idx
def solve(adj,deg,wall_sets,root=None,means=False):
 n=len(adj);full=(1<<n)-1;cut=[0]*(1<<n);z=[F(0)]*(1<<n);z[0]=F(1)
 for mask in range(1,1<<n):
  bit=mask&-mask;v=bit.bit_length()-1;rest=mask^bit
  cut[mask]=cut[rest]+deg[v]-2*(adj[v]&rest).bit_count()
  assert cut[mask]>0
  s=F(0);bits=mask
  while bits:
   b=bits&-bits;bits^=b;s+=z[mask^b]
  z[mask]=s/cut[mask]
 def part(A,available=full):
  assert A&~available==0
  extra=available^A;s=F(0);sub=extra
  while True:
   pos=A|sub;s+=z[pos]*z[available^pos]
   if sub==0:break
   sub=(sub-1)&extra
  return s
 result=[]
 for A in wall_sets:
  Z=part(A);contacts={}
  for i in range(n):
   if A>>i&1:contacts[str(i)]=part(A^(1<<i),full^(1<<i))/Z
  result.append({'wall_mask':A,'Z':str(Z),'contacts':{i:str(x) for i,x in contacts.items()},'contact_sum':str(sum(contacts.values(),F(0))),'wall_cut':cut[A] if A else 0})
  assert sum(contacts.values(),F(0))<= (cut[A] if A else 0)
  if A==full:assert sum(contacts.values(),F(0))==cut[full]
 if root is not None:
  for row in result:
   if str(root) in row['contacts']:row['root_contact_float']=float(F(row['contacts'][str(root)]))
 # Fully exhaustive log-supermodularity checks for very small graphs only.
 if n<=6:
  for S in range(1<<n):
   for T in range(1<<n):assert z[S|T]*z[S&T]>=z[S]*z[T]
  print('Exhaustive z log-supermodularity passed',n,flush=True)
 if means:
  for row,A in zip(result,wall_sets):
   mm={}
   for i in range(n):
    if not(A>>i&1):continue
    moment=[F(0)]*(1<<n)
    for mask in range(1,1<<n):
     if not(mask>>i&1):continue
     s=z[mask];bits=mask^(1<<i)
     while bits:
      b=bits&-bits;bits^=b;s+=moment[mask^b]
     moment[mask]=s/cut[mask]
    total=F(0);extra=full^A;sub=extra
    while True:
     pos=A|sub;total+=moment[pos]*z[full^pos]
     if sub==0:break
     sub=(sub-1)&extra
    mm[str(i)]=str(total/F(row['Z']))
   row['wall_means']=mm
 return result
results=[];t=time.time()
# Three collinear Z^2 sites, zero boundary everywhere else.
adj,deg,idx=model([(-1,0),(0,0),(1,0)]);o=idx[(0,0)];left=idx[(-1,0)];right=idx[(1,0)]
C=1<<o;A=C|(1<<left);B=C|(1<<right);U=A|B
rows=solve(adj,deg,[C,A,B,U],root=o,means=True)
f=[F(x['contacts'][str(o)]) for x in rows]
assert f==[F(32,11),F(48,19),F(48,19),F(24,11)]
assert f[3]/f[0] < (f[1]/f[0])**2
results.append({'name':'three_site_lattice_reflection','coords':[[-1,0],[0,0],[1,0]],'rows':rows,'half_ratio':str(f[1]/f[0]),'union_ratio':str(f[3]/f[0]),'squared_half_ratio':str((f[1]/f[0])**2),'proposed_reflection_inequality':'FALSE'})
print('Three-site comparison:',json.dumps(results[-1]),flush=True)
(R/'coarea_checks.json').write_text(json.dumps(results,indent=2),encoding='utf8')
# 3x3 grounded square: mirrored half-boxes and a buffered two-site wall.
coords=[(x,y) for x in range(-1,2) for y in range(-1,2)]
adj,deg,idx=model(coords);o=idx[(0,0)];C=1<<o
A=sum(1<<idx[(x,y)] for x in [-1,0] for y in [-1,0,1]);B=sum(1<<idx[(x,y)] for x in [0,1] for y in [-1,0,1]);I=A&B
rows=solve(adj,deg,[C,I,A,B,A|B],root=o,means=True)
fI=F(rows[1]['contacts'][str(o)]);fA=F(rows[2]['contacts'][str(o)]);fU=F(rows[4]['contacts'][str(o)])
results.append({'name':'3x3_reflected_half_boxes','rows':rows,'half_ratio':str(fA/fI),'union_ratio':str(fU/fI),'squared_half_ratio':str((fA/fI)**2),'comparison_holds':fU/fI>=(fA/fI)**2})
print('3x3 comparison:',results[-1]['comparison_holds'],float(fA/fI),float(fU/fI),flush=True)
(R/'coarea_checks.json').write_text(json.dumps(results,indent=2),encoding='utf8')
# Buffered 4x4 square with a central 2x2 wall: all four wall corners are one
# lattice step away from the pinned exterior. Exact partition and contacts;
# only four moment vectors, bounded below 1 GB. No large-volume extrapolation.
coords=[(x,y) for x in range(4) for y in range(4)]
adj,deg,idx=model(coords);A=sum(1<<idx[(x,y)] for x in [1,2] for y in [1,2])
rows=solve(adj,deg,[A],means=True)
assert len(set(rows[0]['contacts'].values()))==1
assert len(set(rows[0]['wall_means'].values()))==1
results.append({'name':'4x4_buffered_central_2x2_wall','rows':rows,'corner_contact_float':float(F(next(iter(rows[0]['contacts'].values())))),'corner_mean_float':float(F(next(iter(rows[0]['wall_means'].values()))))})
(R/'coarea_checks.json').write_text(json.dumps(results,indent=2),encoding='utf8')
print('Buffered square:',results[-1]['corner_contact_float'],results[-1]['corner_mean_float'],flush=True)
print('Elapsed seconds',time.time()-t,flush=True)
