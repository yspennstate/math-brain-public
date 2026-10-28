import itertools,json,time
from pathlib import Path
B=Path(__file__).resolve().parents[1]
(B/'out'/'INDEPENDENT_SPEC.json').write_text(json.dumps({'helper_version':'A055 basis enumeration v1','family':'all ordered labelled two-bit Boolean products','domain':'256 products on four bits; every unordered GF2 basis (840)','case_count':215040,'symmetry':'basis permutations removed since sums are invariant','arithmetic':'integer directional disagreement counts and direct character sums','memory_estimate_MB':30,'maximum_runtime_seconds':55},indent=2),encoding='utf-8')
s=time.perf_counter();checks=0
def ck(v):
 global checks
 assert v;checks+=1
 assert time.perf_counter()-s<55
def rank(v):
 piv={}
 for x in v:
  while x:
   j=x.bit_length()-1
   if j in piv:x^=piv[j]
   else:piv[j]=x;break
 return len(piv)
bases=[b for b in itertools.combinations(range(1,16),4) if rank(b)==4];ck(len(bases)==840)
tables=[tuple(1 if (v>>x)&1 else -1 for x in range(4)) for v in range(16)]
def costs(t):
 N=len(t);return [min(sum(t[x]!=t[x^v] for x in range(N)),sum(t[x]==t[x^v] for x in range(N))) for v in range(N)]
def walsh(t):return [sum(t[x]*(-1 if (x&u).bit_count()%2 else 1) for x in range(len(t))) for u in range(len(t))]
for a,b in itertools.product(tables,repeat=2):
 t=tuple(a[x&3]*b[x>>2] for x in range(16));c=costs(t)
 aa=min(sum(costs(a)[v] for v in base) for base in itertools.combinations(range(1,4),2))
 bb=min(sum(costs(b)[v] for v in base) for base in itertools.combinations(range(1,4),2))
 target=4*(aa+bb);best=1000
 for basis in bases:
  z=sum(c[v] for v in basis);ck(z>=target);best=min(best,z)
 ck(best==target)
 ck(walsh(t)==[x*y for y in walsh(b) for x in walsh(a)])
 # The direction-cost maximum inequality is the sublevel-rank premise.
 ca,cb=costs(a),costs(b)
 for v in range(16):ck(c[v]>=4*max(ca[v&3],cb[v>>2]))
r={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-s,'products':256,'unordered_bases_per_product':840,'basis_comparisons':215040}
(B/'out'/'INDEPENDENT.json').write_text(json.dumps(r,indent=2),encoding='utf-8');print(json.dumps(r))
