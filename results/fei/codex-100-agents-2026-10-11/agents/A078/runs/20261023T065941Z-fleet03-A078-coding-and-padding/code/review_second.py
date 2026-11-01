from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out'
spec={'helper_version':'independent rational binomial identities1','family':'A077 even biased cofactor after first restriction of odd central majority','domain':'even n4..128','case_count':63,'symmetry':'symmetric level multiplicities exactly retained','arithmetic':'Fraction, integer binomials; no logarithms or floating point','memory_estimate_MB':2,'max_runtime_seconds':55}
(O/'FROZEN_REVIEW.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
checks=0
for n in range(4,129,2):
 alpha=F(comb(n,n//2),2**n);A=[F(0)]*(n+2)
 for l in range(n//2+1):A[2*l+1]=(-1)**l*alpha*F(comb(n//2,l),comb(n,2*l))
 beta=[A[k+1] if k%2==0 else A[k] for k in range(n+1)]
 L=2*sum((comb(n-1,k)*abs(beta[k]*beta[k+1]) for k in range(n)),F(0))
 Ie=sum((comb(n-1,k)*A[k+1]**2 for k in range(0,n,2)),F(0))
 assert L==4*Ie;checks+=1
 assert Ie<=alpha;checks+=1
 assert 8*F(1,2**(n//2))+16*F(1,2**n)<=8*alpha;checks+=1
result={'status':'PASS','scope':'A077-SECOND-MAJORITY-SHARED@1 sections1-2 only; not independent review of own private/account contributions','exact_assertions':checks,'even_n_cases':63,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'REVIEW_SECOND.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
