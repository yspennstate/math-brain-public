"""PROVED: exact Polya coefficient certificates for upper frame moments."""
exec(open('explore_upper_moments.py').read().split('unit=matrices')[0])
from time import monotonic
records=[]
for k,bound in [(F(3,2),F(27,25)),(F(2),F(7,5)),(F(2),F(11,8)),(F(3),F(81,40)),(F(4),F(107,40))]:
 poly=QQ(bound.numerator,bound.denominator)*t*t*n-QQ(k.numerator,k.denominator)*A*n-t*C
 for power in range(21):
  mats=matrices(poly)
  bad=sum(not psd(m) for m in mats.values())
  print('PROVED: tested k',k,'bound',bound,'power',power,'forms',len(mats),'NUMERICAL: unresolved',bad,flush=True)
  if not bad:
   records.append(dict(k=str(k),bound=str(bound),power=power));break
  poly*=sum(z)
with open('polya_upper_bounds.json','w') as fp:json.dump(records,fp,indent=2)
