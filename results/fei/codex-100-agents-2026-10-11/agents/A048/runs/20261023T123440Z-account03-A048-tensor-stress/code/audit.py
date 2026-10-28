"""Independent audit: no imports of producer or interval helper."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib
B=Path(__file__).resolve().parents[1]
raw=(B/'out/PHASE_CERTIFICATE.json').read_bytes();phase=json.loads(raw)
for m in range(15):
 for r in range(3):
  aa=F(sum((-1)**j*comb(m,j) for j in range(m+1) if j%3==r),2**m)
  rr=F(sum(comb(m,j) for j in range(m+1) if j%3==r),2**m)
  assert aa==F(phase['alt_vectors'][m][r]) and rr==F(phase['rho_vectors'][m][r])
for i in range(3):
 for j in range(3):
  entry=F(sum((-1)**s*comb(6,s) for s in range(7) if (j+s)%3==i),64)
  assert entry==F(phase['T6'][i][j])==-F(27,64)*(F(i==j)-F(1,3))
for m in range(2,9):
 ds=[]
 for r in range(3):
  x,y=map(F,(phase['alt_vectors'][m-1][r],phase['alt_vectors'][m-1][(r-1)%3]))
  assert x*x+y*y>0;ds.append((x*x-y*y)/(x*x+y*y))
 assert sum(d!=0 for d in ds)==2
 assert all(d==0 or abs(d)>=F(3,5) for d in ds)
 if m%2==0:assert all(F(x) for x in phase['alt_vectors'][m])
for t in range(2,15):assert min(map(F,phase['rho_vectors'][t]))>=F(1,4)
m=4;k=4;r=0;size=2**(m+k);delta=F(1,2**k)
values=[]
for x in range(size):
 t=x%(2**m);z=x//(2**m);val=-1 if z&1 else 1
 if z in (2,3):val=-val
 if z==0 and t.bit_count()%3==r:val=-val
 values.append(val)
for mask in range(size):
 S=mask%(2**m);U=mask//(2**m);s=S.bit_count()
 qt=F(sum((-1)**j*comb(s,j)*comb(m-s,l) for j in range(s+1) for l in range(m-s+1) if (j+l)%3==r),2**m)
 gh=F(U==1)-2*delta*((-1)**((U&2).bit_count())-(-1)**((U&3).bit_count()))
 expected=(gh if S==0 else 0)-2*delta*qt
 literal=F(sum(value*(-1)**((x&mask).bit_count()) for x,value in enumerate(values)),size)
 assert literal==expected
account=json.loads((B/'out/ACCOUNT_CERTIFICATE.json').read_text(encoding='utf8'))
N=account['tail_bits'];assert N==account['z_bits']==65536
assert account['original_F_dimension']==2*N+3 and account['reset_blocks']==N//2-1
assert 6**15<16*5**15
bill=F(N-4,4608)-F(1,15)
assert bill==F(account['cumulative_global_sigma_strict_lower'])==F(9059,640)
assert bill-8==F(account['signed_net_shortfall_strict_lower'])==F(3939,640)
assert 4+F(253,256)-(3+(F(3,8)+F(4,15))/4)>F(3,2)
assert 2+F(229,256)==F(741,256)>0
for row in account['sparse_tensor_cases']:
 T=row['T'];l=row['activation_controls'];alpha=F(row['alpha'])
 assert alpha==F(1,4*T*T) and T&(T-1)==0
 assert alpha*(T*F(3939,640)-4*(l+1))==F(row['remaining_deficit_strict_lower'])>0
 assert alpha*(l+1+2*T)==F(row['influence_upper'])
result={'status':'PASS','phase_artifact_sha256':hashlib.sha256(raw).hexdigest(),'binomial_phase_entries_recomputed':45,'matrix_entries_recomputed':9,'literal_actual_cube_coefficients_recomputed':256,'account_N':N,'strict_deficit_lower':str(bill-8),'sparse_cases_recomputed':len(account['sparse_tensor_cases']),'independence':'Binomial counts instead of recurrence; convolution instead of matrix powers; literal character sums instead of Walsh; no producer/helper imports'}
(B/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result))
