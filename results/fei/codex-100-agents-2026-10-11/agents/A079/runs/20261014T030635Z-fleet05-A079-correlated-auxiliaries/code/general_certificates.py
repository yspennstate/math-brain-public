import json,time,math,hashlib
from pathlib import Path
from fractions import Fraction as Q
root=Path(__file__).resolve().parents[1]
spec={'helper_version':'A079-general-one-nonfair-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'Integer height-two one-coordinate rows and symbolic Gibbs energy identities','domain':'All25 physical pairs in{-2,-1,0,1,2}^2; all1024 positive integer magnitude pairs a,b<=32 screened for coprimality; m=1..10 and64 fixed rational q values for symbolic identities; five integer log comparisons','case_count':1694,'symmetry':'None; coprimality is an explicit hypothesis filter','arithmetic':'integer gcd/parity/power comparisons; Fraction polynomial identities in a symbolic log variable','memory_estimate':'under10MB','maximum_runtime_seconds':60}
(root/'out'/'FROZEN_GENERAL_EXTENSION.json').write_text(json.dumps(spec,indent=2)+'\n')
start=time.monotonic();assertions=0;coprime=0;nonfair=0
def ck(x):
 global assertions
 assertions+=1;assert x;assert time.monotonic()-start<60
for u in range(-2,3):
 for v in range(-2,3):
  a,b=abs(u+v),abs(u-v)
  if a and b and a!=b:ck(sorted([Q(a,math.gcd(a,b)),Q(b,math.gcd(a,b))])==[1,3]);nonfair+=1
for a in range(1,33):
 for b in range(1,33):
  if math.gcd(a,b)!=1:continue
  coprime+=1;n=a*a+b*b
  while n%2==0:n//=2
  ck((n==1)==(a==b==1))
for m in range(1,11):
 for j in range(64):
  q=Q(j,128)
  ck(Q(5,2)*(Q(m,2)+q)-(m+Q(5,2)*q+Q(1,4))==Q(m-1,4))
  # Kall=6+2l; difference has coefficients m-1 and m-1+2q.
  ck(3*m+6*q-(2*m+6*q+1)==m-1)
  ck(m+2*q-1==m-1+2*q)
ck(121<128);ck(3**5<2**8);ck(3**12>2**19);ck(5**3<2**7);ck(5**10>2**23)
out={'status':'PASS','assertions':assertions,'one_bit_pairs':25,'nonfair_one_bit_pairs':nonfair,'coprime_pairs':coprime,'symbolic_m_q_cases':640,'seconds':time.monotonic()-start,'bridge':'Gibbs/KL inequality proved analytically in DERIVATION; finite scalar examples validate symbolic residuals, not the continuum theorem by themselves','independent_review':False}
(root/'out'/'general_extension_validation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
