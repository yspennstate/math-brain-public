from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import prod
import argparse,json,hashlib,time
ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
start=time.monotonic();checks=0;faces=0;coefficients=0;parameter_cases=0;table_count=0
def ck(b):
 global checks
 assert b;checks+=1
 assert time.monotonic()-start<55
def fwht(values):
 a=values[:];h=1
 while h<len(a):
  for b in range(0,len(a),2*h):
   for i in range(b,b+h):
    x,y=a[i],a[i+h];a[i],a[i+h]=x+y,x-y
  h*=2
 return [Q(x,len(a)) for x in a]
for widths in ([[2,2]] if args.pilot else [[2,2],[2,3]]):
 r=len(widths);n0=sum(widths);n=2*n0;size=1<<n
 offset=0;blocks=[]
 for width in widths:blocks.append(set(range(offset,offset+width)));offset+=width
 U=[all(any(z>>i&1 for i in block) for block in blocks) for z in range(1<<n0)]
 V=[any(all(z>>i&1 for i in block) for block in blocks) for z in range(1<<n0)]
 a=Q(sum(U),1<<n0);b=Q(sum(V),1<<n0);ck(a+b==1)
 truth=[U[z&((1<<n0)-1)] and V[z>>n0] for z in range(size)]
 vals=[2*int(t)-1 for t in truth];hat=fwht(vals)
 hu=fwht([2*int(t)-1 for t in U]);hv=fwht([2*int(t)-1 for t in V])
 I0=Q(sum(sum(U[z]!=U[z^(1<<i)] for z in range(1<<n0)) for i in range(n0)),1<<n0)
 IF=Q(sum(sum(truth[z]!=truth[z^(1<<i)] for z in range(size)) for i in range(n)),size)
 ck(IF==I0)
 ck(sum(c*c for c in hat)==1)
 ck(sum(s.bit_count()*c*c for s,c in enumerate(hat))==IF)
 for mask,c in enumerate(hat):
  sx=mask&((1<<n0)-1);sy=mask>>n0
  if sx and not sy:ck(c*c==b*b*hu[sx]**2)
  elif sy and not sx:ck(c*c==a*a*hv[sy]**2)
  elif sx and sy:ck(c*c==hu[sx]**2*hv[sy]**2/4)
  else:ck(c==2*a*b-1)
  coefficients+=1
 # Independent complete prime classification via intersections of truth-point bitsets.
 allpoints=(1<<size)-1
 truth_bits=sum(1<<z for z,t in enumerate(truth) if t)
 masks={(i,s):sum(1<<z for z in range(size) if bool(z>>i&1)==(s==1)) for i in range(n) for s in [-1,1]}
 positive=set();negative=set()
 for signs in product([-1,0,1],repeat=n):
  points=allpoints
  for i,s in enumerate(signs):
   if s:points &= masks[i,s]
  if not points & (allpoints^truth_bits):positive.add(signs)
  if not points & truth_bits:negative.add(signs)
  faces+=1
 def minimal(implicants):
  return {s for s in implicants if all(tuple(0 if i==j else v for i,v in enumerate(s)) not in implicants for j,v in enumerate(s) if v)}
 pos=minimal(positive);neg=minimal(negative)
 transversal=[set(choice) for choice in product(*[sorted(block) for block in blocks])]
 pexpected={tuple(1 if i in tx or i-n0 in block else 0 for i in range(n)) for tx in transversal for block in blocks}
 nexpected={tuple(-1 if i in block else 0 for i in range(n)) for block in blocks}
 nexpected|={tuple(-1 if i-n0 in ty else 0 for i in range(n)) for ty in transversal}
 ck(pos==pexpected);ck(neg==nexpected)
 # Critical scope check: cheap opposite-side roots do not meet the hard target.
 for prime_set,target_blocks in [(pos,blocks),(neg,[{i+n0 for i in block} for block in blocks])]:
  for block in target_blocks:
   for signs in prime_set:
    support={i for i,s in enumerate(signs) if s}
    ck(len(support&block)<=1)
    if support&block:ck(len(support)>=r)
 table_count+=1
for w in ([4] if args.pilot else range(4,9)):
 r=2**w;pi=Q(1,2**r)
 for t in [0,r//2,r]:
  a=(1-Q(1,r))**(r-t)*(1-Q(1,2*r))**t;b=1-a
  I0=Q(0);lower=Q(0);Hupper=Q(1)
  for count,width,epsilon in [(r-t,w,Q(1,r)),(t,w+1,Q(1,2*r))]:
   if not count:continue
   p=1-epsilon;outside=a/p
   Ij=2*count*width*epsilon*outside
   I0+=Ij;lower+=Ij*outside*(r*(1-2*p/width)-3*pi)
   Hupper+=4*a*count*epsilon*(2*width+Q(3,2))
  ck(lower>Q(r,7)*I0)
  ck(b*b*lower>Q(r,112)*I0)
  ck(a*a*lower>Q(r,112)*I0)
  ck(Q(3,16)<a*b<=Q(1,4))
  ck(4*a*b*(1-a*b)>Q(39,64))
  ck(Hupper+2<8*I0)
  parameter_cases+=1
result={'status':'PASS','pilot':args.pilot,'assertions':checks,'truth_tables':table_count,
 'signed_faces_classified_for_both_polarities':faces,'spectral_coefficients':coefficients,
 'analytic_parameter_cases':parameter_cases,'seconds':time.monotonic()-start,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'arithmetic':'integer bitset faces and Walsh; Fraction; no tolerance',
 'scope':'Both global polarity choices separately; output-mass mixtures explicitly not refuted'}
(ROOT/'out'/('product_pilot.json' if args.pilot else 'product.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
