from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,time
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[0]/'20261012T010436Z-fleet05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
fw=ns['fw'];add=ns['ints_add'];grid=ns['grid'];factors=ns['factor'];SCALE=ns['SCALE'];ent=ns['ent'];logq=ns['logq']
checks=0;start=time.perf_counter()
def ck(v):
 global checks
 checks+=1;assert v;assert time.perf_counter()-start<120
def masslog(counts):
 z=defaultdict(int)
 for count in counts:
  if count:
   for p,e in factors(count).items():z[p]+=count*e
 return {p:c for p,c in z.items() if c}
def E(counts,power):
 ck(sum(counts)==1<<power)
 return add((power*(1<<power),{2:1}),(-1,masslog(counts)))
def Bpairs(pairs):
 return add((1,masslog([p+q for p,q in pairs])),(-1,masslog([p for p,q in pairs])),(-1,masslog([q for p,q in pairs])))
modules=[]
for mask in range(256):
 v=[1-2*((mask>>i)&1) for i in range(8)]
 a=fw(v[0::2]);b=fw(v[1::2]);pairs=[((p+q)**2,(p-q)**2) for p,q in zip(a,b)]
 P=[z for pair in pairs for z in pair];R=[sum(pair) for pair in pairs]
 modules.append((a,b,E(P,6),E(R,6),Bpairs(pairs),R))
fixtures=[]
for i,(a,b,H,HR,B,R1) in enumerate(modules):
 for j,(c,d,H2,HR2,B2,R2) in enumerate(modules):
  pairs=[((a[t]*c[u]+b[t]*d[u])**2,(a[t]*c[u]-b[t]*d[u])**2) for u in range(4) for t in range(4)]
  jointR=[sum(pair) for pair in pairs];HP=E([z for pair in pairs for z in pair],10);HRP=E(jointR,10);BP=Bpairs(pairs)
  TC=add((16,HR),(16,HR2),(-1,HRP))
  excess=add((1,HP),(-16,H),(-16,H2))
  ck(excess==add((1,BP),(-16,B),(-16,B2),(-1,TC)))
  ck(grid(TC)[0]>=0)
  # Compatible conditional lift using exact module data references has debt exactly TC.
  CE=add((1,BP),(16,HR),(16,HR2))
  ck(add((1,CE),(-1,HP))==TC)
  if (i,j) in ((0,255),(7,19),(23,171),(105,197)):
   total=F(0);actualCE={}
   for u in range(4):
    for t in range(4):
     index=4*u+t;p0,p1=pairs[index];r=jointR[index];refdata=F(R1[t]*R2[u],4096)
     for A,p in enumerate((p0,p1)):
      conditional=F(p,r) if r else F(1,2);q=conditional*refdata;total+=q
      if p:ck(q>0);actualCE=ns['add']((1,actualCE),(-F(p,1024),logq(q)))
   ck(total==1);ck(actualCE==ns['add']((F(1,1024),CE)))
   fixtures.append({'module_masks':[i,j],'normalization':'1','debt_prime_log_scaled':TC,'denominator':1024})
out={'status':'PASS','pairs':65536,'checks':checks,'elapsed_seconds':time.perf_counter()-start,'normalized_reference_fixtures':fixtures,'identity':'H(shared)=sum H(modules)+B_shared-sum B_j-TC(data); exact module-marginal conditional reference debt=TC'}
(ROOT/'out/ROW_IDENTITY_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','pairs','checks','elapsed_seconds')},indent=2))
