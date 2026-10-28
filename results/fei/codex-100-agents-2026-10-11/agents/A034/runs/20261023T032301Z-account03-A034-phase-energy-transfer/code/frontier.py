from pathlib import Path
from fractions import Fraction as Q
import itertools,json,time
RUN=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def w(v):
 a=list(v);k=1
 while k<len(a):
  for j in range(0,len(a),2*k):
   for i in range(j,j+k):a[i],a[i+k]=a[i]+a[i+k],a[i]-a[i+k]
  k*=2
 return a
# On this frozen domain each row has four signs and raw entries0,2,4.
# Hence the normalized FULL Boolean Fourier squares are dyadic powers,
# and entropy is EXACTLY rational with no transcendental comparison.
def ent(raw):
 total=Q(0)
 for r in raw:
  if not r:continue
  q=Q(r*r,256)
  if q.numerator&(q.numerator-1):raise AssertionError('unexpected nondyadic atom')
  total+=q*(q.denominator.bit_length()-q.numerator.bit_length())
 return total
cases=0;nonaffine=0;worst=Q(0);best=None
for pts in itertools.combinations(range(8),4):
 S=set(pts);V={x^min(S) for x in S};affine=all(x^y in V for x in V for y in V)
 nonaffine+=not affine
 for sign in range(256):
  vals=[]
  for y in range(8):
   z=1-2*(sign>>y&1)
   vals.extend([z,z if y in S else -z])
  raw=w(vals);H=ent(raw)
  Iy=Q(sum(vals[z]!=vals[z^(1<<i)] for z in range(16) for i in range(1,4)),16)
  Iy2=Q(sum((s>>1).bit_count()*v*v for s,v in enumerate(raw)),256)
  assert Iy==Iy2
  checks+=1
  assert H<=4*Iy
  checks+=1
  ratio=H/Iy if Iy else Q(0)
  if ratio>worst:worst=ratio;best={'support':pts,'data_phase_mask':sign,'truth':vals,'raw_walsh':raw,'H':str(H),'IY':str(Iy),'affine_support':affine}
  cases+=1
  if cases%1024==0 and time.monotonic()-start>20:raise TimeoutError('frozen20s cap')
out={'status':'PASS','cases':cases,'checks':checks,'nonaffine_supports':nonaffine,'maximum_H_over_IY':str(worst),'maximizer':best,'runtime_seconds':time.monotonic()-start,'scope':'complete finite domain only; no arbitrary-dimension proper-four-cell theorem'}
(RUN/'out'/'frontier_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
