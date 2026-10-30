from pathlib import Path
from fractions import Fraction as F
import json,math,time
R=Path(__file__).resolve().parents[1]
def fw(t):
 a=list(t);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for k in range(j,j+h):u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
  h*=2
 return a
def orbit(mask):
 t=[1 if mask>>x&1 else -1 for x in range(8)]
 return {sum((t[x]*sign*(-1 if (x&j).bit_count()%2 else 1)>0)<<x for x in range(8)) for j in range(8) for sign in [-1,1]}
reps=sorted({min(orbit(mask)) for mask in range(256)})
spec={'helper_version':'A013-two-row-pilot-v1','family':'G=c(s), H=c(s)(1-2[1_(s=0) E0(V)+1_(s=1) E1(V)]); events arbitrary on same independent private cube; fresh selector','domain':{'phases':reps,'p_q_grid_denominator':32,'p_q':'0..32 independently'},'case_count':len(reps)*33**2,'symmetry':'Affine shared reindexing maps any distinct ordered pair to0,1; common character/sign multiplication permutes Fourier indices and keeps B,d; 16 character orbits of 256 phases. Physical shared influence is not replaced by affine-transformed influence.','arithmetic':'Exact integer Walsh coefficients, floating entropy for discovery only','memory_estimate_MB':70,'max_runtime_seconds':50,'finite_to_continuum':'No continuum inference from pilot'}
(R/'out/FROZEN_PILOT.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
start=time.perf_counter();best=(-1,None);patterns={}
def phi(a,b):
 if not a or not b:return 0.
 return (a+b)*math.log2(a+b)-a*math.log2(a)-b*math.log2(b)
for mask in reps:
 t=[1 if mask>>x&1 else -1 for x in range(8)];w=fw(t)
 pattern=tuple(tuple(sorted(F(w[T]*t[0],8) for T in range(8) if T&1==g)) for g in [0,1])+(t[0]*t[1],)
 patterns.setdefault(pattern,mask)
 for i in range(33):
  for j in range(33):
   p,q=i/32,j/32;d=(p+q)/8
   if not d:continue
   delta=(p*p+q*q)/8;b=2*(d-delta)
   for T in range(8):
    k=(p+q*t[0]*t[1]*(-1 if T&1 else 1))/8;a=w[T]*t[0]/8
    b+=phi((a-k)**2,k*k)
   ratio=b/d
   if ratio>best[0]:best=(ratio,{'mask':mask,'p':str(F(i,32)),'q':str(F(j,32)),'d':str(F(i+j,256))})
res={'status':'DISCOVERY_ONLY','case_count':len(reps)*33**2,'character_representatives':reps,'distinct_grouped_profiles':len(patterns),'maximum_float_B_over_d':best,'elapsed_seconds':time.perf_counter()-start,'profiles':[{'mask':mask,'groups':[[str(v) for v in group] for group in pattern[:2]],'relative_sign':pattern[2]} for pattern,mask in patterns.items()]}
(R/'out/PILOT_RESULTS.json').write_text(json.dumps(res,indent=2),encoding='utf-8');print(json.dumps(res))
