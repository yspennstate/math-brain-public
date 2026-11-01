"""All-case fixed-point rational log certificate; floating ratios unused."""
import biased_grid as bg
from fractions import Fraction as F
import numpy as np,json,time
OUT=bg.OUT; start=time.perf_counter(); SCALE=1<<24
Q=1<<80
def ceildiv(a,b): return -((-a)//b)
def ln_fixed(a,b):
 # x=a/b in [1,2]; z=(a-b)/(a+b). Enclose every operation.
 if a==b: return 0,0
 zl=(a-b)*Q//(a+b); zh=ceildiv((a-b)*Q,a+b)
 z2l=zl*zl//Q; z2h=ceildiv(zh*zh,Q)
 tl,th=zl,zh; sl=sh=0
 for j in range(32):
  sl+=2*(tl//(2*j+1)); sh+=2*ceildiv(th,2*j+1)
  tl=tl*z2l//Q; th=ceildiv(th*z2h,Q)
 # Universal z<=1/3 tail, with exact integer upward rounding.
 sh+=ceildiv(2*Q*9,65*8*3**65)
 return sl,sh
l2,u2=ln_fixed(2,1)
low=np.zeros(1297,dtype=np.int64); high=low.copy()
for a in range(1,1297):
 k=a.bit_length()-1; l,u=ln_fixed(a,1<<k)
 low[a]=k*SCALE+l*SCALE//u2
 high[a]=k*SCALE+ceildiv(u*SCALE,l2)
 assert high[a]-low[a]<=1
assert low[1]==high[1]==0
records=[]; total=0; max_lower=F(0); max_upper=F(0); lower_witness=None; upper_witness=None
for n in [2,3,4]:
 masks,T=bg.prime_tables(n)
 for biasmask in range(1<<n):
  assert time.perf_counter()-start<50,'50 second certificate cap'
  A,ks,deg,D,_=bg.moments(n,T,biasmask)
  b=biasmask.bit_count(); L=D*D*3**b
  absA=np.abs(A); assert np.max(absA)<=1296
  weights=A*A*(3**(b-ks))
  assert np.all(weights.sum(axis=1)==L)
  delta=(weights[:,1:]*(deg[1:]-1)).sum(axis=1)
  assert np.all(delta>0)
  c=(2*(D.bit_length()-1)-2*ks)*SCALE
  hlow=(weights[:,1:]*(c[1:]+2*ks[1:]*low[3]-2*high[absA[:,1:]])).sum(axis=1)
  hupp=(weights[:,1:]*(c[1:]+2*ks[1:]*high[3]-2*low[absA[:,1:]])).sum(axis=1)
  # Search among finite exact interval ratios with integer cross-multiplication.
  # Floating quotient only selects a possible index; exact scan verifies it globally.
  jl=int(np.argmax(hlow/delta)); ju=int(np.argmax(hupp/delta))
  assert np.all(hlow.astype(object)*int(delta[jl])<=int(hlow[jl])*delta.astype(object))
  assert np.all(hupp.astype(object)*int(delta[ju])<=int(hupp[ju])*delta.astype(object))
  lo=F(int(hlow[jl]),SCALE*int(delta[jl])); hi=F(int(hupp[ju]),SCALE*int(delta[ju]))
  rec={'n':n,'biasmask':biasmask,'cases':len(masks),'lower':str(lo),'upper':str(hi),'lower_table':int(masks[jl]),'upper_table':int(masks[ju]),'parseval_checks':len(masks),'positive_deficit_checks':len(masks),'exact_ratio_max_checks':2*len(masks)}
  records.append(rec);total+=len(masks)
  if lo>max_lower: max_lower=lo;lower_witness=rec
  if hi>max_upper: max_upper=hi;upper_witness=rec
  data={'helper':'A043-rational-grid-certificate-v2','complete':False,'scale':SCALE,'atanh_terms':32,'ln_internal_scale':Q,'cases':total,'records':records,'maximum_lower':str(max_lower),'maximum_upper':str(max_upper),'lower_witness':lower_witness,'upper_witness':upper_witness}
  (OUT/'grid_certificate.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
data.update(complete=True,runtime_seconds=time.perf_counter()-start,maximum_interval_width=str(max_upper-max_lower))
(OUT/'grid_certificate.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
(OUT/'log_intervals.json').write_text(json.dumps({'scale':SCALE,'terms':32,'entries':[[int(low[a]),int(high[a])] for a in range(1297)]})+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2))
