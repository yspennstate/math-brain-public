import json,time,hashlib
from pathlib import Path
from fractions import Fraction as Q
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'A019-excess-independent-v1','family':'A018 equal five-private-bit point defects sharing one bit','domain':'one actual eleven-bit Boolean parent and two six-bit modules','case_count':1,'symmetry':'none','arithmetic':'integer Walsh and exact integer comparison; entropy represented by rational prime-log coefficients','memory_estimate_MB':30,'maximum_runtime_seconds':60}
(R/'out/EXCESS_SPEC.json').write_text(json.dumps(spec,indent=2));start=time.monotonic()
def fw(a):
 if len(a)==1:return a
 h=len(a)//2;l=fw(a[:h]);r=fw(a[h:]);return [x+y for x,y in zip(l,r)]+[x-y for x,y in zip(l,r)]
def factors(k):
 out={};p=2
 while p*p<=k:
  while k%p==0:out[p]=out.get(p,0)+1;k//=p
  p+=1
 if k>1:out[k]=out.get(k,0)+1
 return out
def hform(tt):
 N=len(tt);out={2:Q(2*(N.bit_length()-1))}
 for k in fw(tt):
  if k:
   for p,v in factors(abs(k)).items():out[p]=out.get(p,Q(0))-Q(2*k*k*v,N*N)
 return out
module=[-1 if x==0 else 1 for x in range(64)]
parent=[(-1 if z==0 and x==0 else 1)*(-1 if z==0 and y==0 else 1) for y in range(32) for x in range(32) for z in range(2)]
hp=hform(parent);hm=hform(module)
coef={p:131072*(hp.get(p,0)-2*hm.get(p,0)) for p in set(hp)|set(hm)}
expected={2:-262144,31:491071,13:-231361,37:-231361,3:-27900,5:-27900}
assert coef==expected
lhs=31**491071;rhs=481**231361*15**27900*2**262144;assert lhs>rhs
out={'status':'FINITE_BOOLEAN_WITNESS_INDEPENDENTLY_HOLDS','claim':'A018-SHARED-POINT-COLLISION-EXCESS@1','scope':'eleven-bit positive entropy excess only; asymptotic and full reference theorem not independently reviewed here','entropy_prime_log_coefficients':{str(k):int(v) for k,v in coef.items()},'positive_integer_comparison':True,'seconds':time.monotonic()-start,'lhs_bits':lhs.bit_length(),'rhs_bits':rhs.bit_length(),'lhs_sha256':hashlib.sha256(lhs.to_bytes((lhs.bit_length()+7)//8,'big')).hexdigest(),'rhs_sha256':hashlib.sha256(rhs.to_bytes((rhs.bit_length()+7)//8,'big')).hexdigest()}
(R/'out/EXCESS_REVIEW.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
