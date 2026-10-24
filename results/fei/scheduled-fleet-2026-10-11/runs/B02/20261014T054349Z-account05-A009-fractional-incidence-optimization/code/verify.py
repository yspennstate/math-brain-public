import itertools, math, json, time
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]; checks=0; traces=0
def ck(x):
 global checks
 assert x; checks+=1
def setup(r,mask,ms):
 possible=list(itertools.combinations(range(r),2)); edges=[e for k,e in enumerate(possible) if mask>>k&1]
 deg=[sum(j in e for e in edges) for j in range(r)]; lam=[F(1,2*max(deg[u],deg[v])) for u,v in edges]; groups=[]; offset=r
 for i,m in enumerate(ms):
  leaves=tuple(range(offset,offset+m)); groups.append(leaves); offset+=m
  for j in leaves: edges.append((i,j)); lam.append(F(1,2*m))
 return edges,lam,groups,offset
def U(m,h,t):
 ell=F(1,2*m)
 if h==0: return (ell/32)**t
 if t==0: return F(1,64)
 return math.factorial(t)*ell**t/F(24*8**(t-1)*t*t*(t+1))
def choices(i,leaves,A,index):
 selected=tuple(j for j in leaves if j in A)
 if i not in A:
  yield tuple((index[(i,j)],(j,),()) for j in selected); return
 if not selected:
  for j in leaves: yield ((index[(i,j)],(i,),()),)
  return
 for paired in selected:
  rest=tuple(j for j in selected if j!=paired)
  for perm in itertools.permutations(rest):
   root=index[(i,paired)]; children=tuple(index[(i,j)] for j in perm)
   yield ((root,(i,paired),children),)+tuple((index[(i,j)],(j,),()) for j in rest)
def queue(r,mask,ms):
 global traces
 edges,lam,groups,n=setup(r,mask,ms); index={e:k for k,e in enumerate(edges)}
 p=[x/(4+x) for x in lam]; Z=1-math.prod(1-x for x in p); D=math.prod(1+x/4 for x in lam)-1
 total=F(0); cases=0
 for bits in range(1,1<<n):
  A={j for j in range(n) if bits>>j&1}; options=[list(choices(i,leaves,A,index)) for i,leaves in enumerate(groups)]; eventset=set(); mass=F(0)
  for combination in itertools.product(*options):
   visits=tuple(v for block in combination for v in block); owned={g:B for g,B,kids in visits}; children={g:kids for g,B,kids in visits}
   childset={g for kids in children.values() for g in kids}; roots=sorted(set(owned)-childset)
   ck(len(owned)==len(visits)); ck(set(j for B in owned.values() for j in B)==A)
   expected_arcs={(g,k) for g,kids in children.items() for k in kids}
   actual_arcs={(g,k) for g,B in owned.items() for k in owned if g!=k and set(B)&set(edges[k])}
   ck(expected_arcs==actual_arcs)
   prob=math.prod(p[g] if g in roots else 1-p[g] for g in range(len(edges)))/Z
   ck(prob==math.prod(lam[g]/4 for g in roots)/D)
   pending=roots[:]; record=[]; visited=set()
   while pending:
    g=pending.pop(0); ck(g not in visited); visited.add(g); B=owned[g]; kids=children[g]; s=len(B); c=len(kids)
    ck(set(B)<=set(edges[g])); ck(s in [1,2]); prob*=F(1,s*(s+1)*math.comb(2,s))
    prob*=F(1,(c+1)*(c+2)*math.comb(s+c-1,c))
    for k in kids:
     ck(len(set(B)&set(edges[k]))==1); prob*=lam[k]; pending.append(k)
    record.append((g,tuple(B),tuple(kids)))
   ck(visited==set(owned)); ck(tuple(record) not in eventset); eventset.add(tuple(record)); mass+=prob
  traces+=len(eventset); cases+=1
  expected=math.prod(U(len(leaves),int(i in A),sum(j in A for j in leaves)) for i,leaves in enumerate(groups))/D
  ck(mass==expected); ck(mass>0)
  bound=F(1,96**len(A))*math.prod(F(1,len(leaves)**sum(j in A for j in leaves)) for leaves in groups)/D
  ck(mass>=bound); total+=mass
 ck(total<=1)
 return {'r':r,'core_mask':mask,'private_counts':list(ms),'output_sets':cases,'output_subprobability':str(total)}
def broom(m):
 edges=[(0,j) for j in range(1,m+1)]+[(0,m+1),(m+1,m+2)]; n=m+3; size=1<<n
 vals=[1 if any((x>>u&1) and (x>>v&1) for u,v in edges) else -1 for x in range(size)]
 coeff=[sum(vals[x]*(-1 if (x&a).bit_count()%2 else 1) for x in range(size)) for a in range(size)]
 ck(sum(w*w for w in coeff)==size*size)
 I=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(size) for j in range(n)),size)
 ck(I==F(5,4)+F(m,2**(m+1))); ck(F(coeff[1<<(m+2)]**2,size*size)==F(1,16))
 tail=F(0)
 for a in range(size):
  if any(a>>j&1 for j in range(1,m+1)):
   if a>>(m+2)&1: ck(coeff[a]==0)
   else: ck(abs(coeff[a])==4)
   tail+=F(coeff[a]**2*a.bit_count(),size*size)
 ck(tail==F(m+2,2**(m+1))-F(1,4**m))
 # Source repair's exact core weights and full signed D.
 D=(1+F(1,8*m))**m*F(9,8)**2-1; ck(D<F(25,56)); ck(D<1)
 ck(F((m+7)*(m+2),2**(m+1))<=F(9,2))
 return {'m':m,'I':str(I),'singleton_z_P':'1/16','tail_degree':str(tail),'D_repair':str(D)}
start=time.perf_counter(); rows=[]
for r in range(1,4):
 for mask in range(1<<(r*(r-1)//2)):
  for ms in itertools.product([1,2],repeat=r): rows.append(queue(r,mask,ms))
rows.extend([queue(1,0,(3,)),queue(1,0,(4,))])
brooms=[broom(m) for m in range(2,7)]
result={'all_passed':True,'queue_functions':len(rows),'distinct_actual_traces':traces,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'queue_certificates':rows,'broom_review':brooms}
(ROOT/'out/VERIFY.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['queue_certificates','broom_review']}))
