import json
from fractions import Fraction as F
from functools import lru_cache
import transitive as base

def ceil_fraction(v):return -((-v.numerator)//v.denominator)
def ln_norm(v,d):
 a=v-d;b=v+d;total=0
 for k in range(base.M):
  power=2*k+1
  total+=(2*base.Q*pow(a,power))//((2*k+1)*pow(b,power))
 z=F(a,b)
 tail=2*z**(2*base.M+1)/((2*base.M+1)*(1-z*z))
 return F(total,base.Q),F(total+base.M+ceil_fraction(base.Q*tail),base.Q)
LN2=ln_norm(2,1)
@lru_cache(None)
def logint(v):
 assert v>0
 k=v.bit_length()-1;lo,hi=ln_norm(v,1<<k)
 lower=base.Q*(F(k)+lo/LN2[1])
 upper=base.Q*(F(k)+hi/LN2[0])
 return F(lower.numerator//lower.denominator,base.Q),F(ceil_fraction(upper),base.Q)

if __name__=='__main__':
 base.ln_norm=ln_norm;base.LN2=LN2;base.logint=logint
 base.main()
 for name in ['transitive_certificates.json','transitive_summary.json']:
  p=base.ROOT/'out'/name
  result=json.loads(p.read_text(encoding='utf-8'))
  result['helper_version']='A026-transitive-true-erasure-v2'
  result['rounding']='All logarithm intervals outward-rounded to denominator 2^140'
  p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print('Final output helper_version: A026-transitive-true-erasure-v2')
