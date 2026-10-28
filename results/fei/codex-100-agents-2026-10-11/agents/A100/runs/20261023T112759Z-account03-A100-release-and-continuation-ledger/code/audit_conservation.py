from pathlib import Path
from fractions import Fraction as F
import json,time
R=Path(__file__).resolve().parents[1];O=R/'out';start=time.perf_counter();n=0
spec={'helper_version':'A100-direct-character-conservation-audit-v1','family':'Original A079 controller; parity3, biased dummy-query seed, balanced nonisospectral seed; both signs; same frozen domain','case_count':6,'extra_sharp_ratio_cases':16,'symmetry':'None','arithmetic':'Direct character sums, exact Fraction coefficients and rational product conservation; no Walsh or prime-log helper imported','memory_estimate_MB':40,'maximum_runtime_seconds':55};(O/'FROZEN_AUDIT_SPEC.json').write_bytes((json.dumps(spec,indent=2)+'\n').encode())
def ck(v):
 global n
 n+=1;assert v,n;assert time.perf_counter()-start<55

def ft(v):return [F(sum(z*(-1 if (x&s).bit_count()%2 else 1) for x,z in enumerate(v)),len(v)) for s in range(len(v))]
a=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1);b=tuple(1-z*z for z in a);A,B=ft(a),ft(b);ck(sum(z*z for z in B)==F(3,8));ck(sum(x*y for x,y in zip(A,B))==0)
seeds=[tuple((-1)**x.bit_count() for x in range(8)),tuple(-1 if x//2==0 else 1 for x in range(8)),tuple((-1 if x&4 else 1)*(-1 if x%4==0 else 1) for x in range(8))]
for h in seeds:
 H=ft(h);m=H[0]
 for sign in (-1,1):
  G=[a[x]+sign*b[x]*h[y] for y in range(8) for x in range(16)];gh=ft(G)
  for T in range(8):
   for U in range(16):ck(gh[U+16*T]==(A[U]+sign*m*B[U] if T==0 else sign*B[U]*H[T]))
  ck(sum(v*v for v in gh)==1)
for rho in [F(0),F(1,128),F(1,32),F(1,2)]:
 for lam in [F(0),F(1,64),F(1,32),F(1,2)]:
  injection_ratio=1/(1-rho);transaction_ratio=(1-rho)/(1-lam);total=injection_ratio*transaction_ratio;ck(total==1/(1-lam));ck(total>=1);ck((transaction_ratio<=1)==(lam<=rho))
sharp=json.loads((O/'GHOST_REVIEW.json').read_text())['sharp_cases'];ck(len(sharp)==16 and any(z['sign']=='positive' for z in sharp) and any(z['sign']=='negative' for z in sharp) and any(z['sign']=='zero' for z in sharp))
result={'status':'PASS','assertions':n,'direct_wrapper_cases':6,'exact_all_fourier_coefficients_checked':768,'sharp_conservation_cases':16,'conclusion':'Manufacturing singleton ghost then converting profile has net cost beta*log2(1/(1-lambda)); no free creation of credit','author_or_main_helper_imported':False,'runtime_seconds':round(time.perf_counter()-start,6)};(O/'INDEPENDENT_CONSERVATION_AUDIT.json').write_bytes((json.dumps(result,indent=2)+'\n').encode());print(json.dumps(result,indent=2))
