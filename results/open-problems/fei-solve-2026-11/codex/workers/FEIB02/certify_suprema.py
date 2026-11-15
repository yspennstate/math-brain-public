"""Exact maximizer ties and 100-place suprema from integer interval candidates.
Factor labels need not be prime: products are verified, and identical rational
logarithm coefficient maps suffice to prove equality.
"""
from fractions import Fraction as F
from math import comb,prod
from pathlib import Path
from functools import lru_cache
import json,time,argparse
from symmetric import integer_data,mask_vector,evaluate
parser=argparse.ArgumentParser();parser.add_argument('--verify-only',action='store_true');args=parser.parse_args()
start=time.monotonic();Q=1<<440;M=160
factorpath=Path('factorization_certificate.json')
factors=json.loads(factorpath.read_text()) if factorpath.exists() else {}
@lru_cache(None)
def factor(x):
 key=str(x)
 if key not in factors:
  assert not args.verify_only,('missing factorization',x)
  from sympy import factorint
  factors[key]=[[int(p),int(e)] for p,e in factorint(x).items()]
 pairs=factors[key];assert prod(p**e for p,e in pairs)==x
 return pairs

def expression(n,mask,objective):
 rows=integer_data(mask_vector(n,mask));mass=[comb(n,k)*a[0]**2 for k,a in enumerate(rows)]
 den=sum(k*w for k,w in enumerate(mass));den-=((1<<(2*n)) if '(I-1)' in objective else 0)
 assert den>0
 form={}
 def logadd(x,coef):
  if not coef:return
  for p,e in factor(x):form[p]=form.get(p,F(0))+F(coef*e,den)
 def constant(coef):form[2]=form.get(2,F(0))+F(coef,den)
 kind=objective.split('/')[0]
 for k,((ff,L,QQ,N),w) in enumerate(zip(rows,mass)):
  if not ff:continue
  ff=abs(ff)
  if kind=='A':constant(w*(n+k));logadd(QQ,-w)
  elif kind=='B':constant(w*(n-k));logadd(QQ,w);logadd(ff,-2*w)
  elif kind=='Gamma':logadd(L,w);logadd(ff,-w)
  elif kind=='P':constant(w*(n-k));logadd(N,-w)
  else:raise ValueError(kind)
 return {p:c for p,c in form.items() if c}

def ceildiv(a,b):return (a+b-1)//b
@lru_cache(None)
def ln_ratio(a,b):
 assert b<=a<=2*b
 if a==b:return 0,0
 yl=((a-b)*Q)//(a+b);yh=ceildiv((a-b)*Q,a+b)
 yl2=yl*yl//Q;yh2=ceildiv(yh*yh,Q)
 pl,ph=yl,yh;lo=hi=0
 for j in range(M):
  lo+=(2*pl)//(2*j+1);hi+=ceildiv(2*ph,2*j+1)
  pl=pl*yl2//Q;ph=ceildiv(ph*yh2,Q)
 # True y<=(1/3); finite-prefix power intervals may slightly exceed it.
 remainder=ceildiv(9*Q,4*(2*M+1)*3**(2*M+1))
 return lo,hi+remainder
ln2lo,ln2hi=ln_ratio(2,1)
@lru_cache(None)
def log2_bounds(p):
 e=p.bit_length()-1
 if p==1<<e:return e*Q,e*Q
 lo,hi=ln_ratio(p,1<<e)
 return e*Q+lo*Q//ln2hi,e*Q+ceildiv(hi*Q,ln2lo)

def decimal_round(x,places):
 s=10**places;z=(2*x.numerator*s+x.denominator)//(2*x.denominator)
 return str(z//s)+'.'+str(z%s).zfill(places)
records=[];count=0;maxwidth=F(0)
for n in range(1,25):
 row=json.loads(Path(f'census_interval_{n:02d}.json').read_text())
 for objective,entry in row['maxima'].items():
  if entry is None:continue
  masks=entry['candidates'];reference=expression(n,masks[0],objective)
  for mask in masks:
   assert expression(n,mask,objective)==reference,(n,objective,mask,'not an exact tie')
   count+=1
  lower=upper=F(0)
  for p,c in reference.items():
   a,b=log2_bounds(p)
   if c>0:lower+=c*a/Q;upper+=c*b/Q
   else:lower+=c*b/Q;upper+=c*a/Q
  ltext,htext=decimal_round(lower,100),decimal_round(upper,100)
  assert ltext==htext,(n,objective,'100-place rounding straddles')
  # Independent high-precision check, not used in the certificate.
  import mpmath as mp
  with mp.workdps(170):
   actual=evaluate(mask_vector(n,masks[0]),170)[objective]
   assert mp.mpf(lower.numerator)/lower.denominator<=actual<=mp.mpf(upper.numerator)/upper.denominator
  maxwidth=max(maxwidth,upper-lower)
  records.append({'n':n,'objective':objective,'value_100_decimals':ltext,'lower':str(lower),'upper':str(upper),'exact_ties_proved':True,'extremizers_up_to_global_sign':[{'mask':mask,'value_vector':''.join('+' if x>0 else '-' for x in mask_vector(n,mask))} for mask in masks],'log_expression':{str(p):str(c) for p,c in sorted(reference.items())}})
Path('suprema_certified.json').write_text(json.dumps(records,indent=2)+'\n')
if not args.verify_only:factorpath.write_text(json.dumps(factors,sort_keys=True,indent=2)+'\n')
print('suprema_certified_to_100_decimal_places',len(records))
print('all_interval_candidate_ties_proved_exactly',count)
print('verified_integer_factorizations',len(factors))
print('largest_final_interval_width',float(maxwidth))
print('wall_seconds',time.monotonic()-start)
