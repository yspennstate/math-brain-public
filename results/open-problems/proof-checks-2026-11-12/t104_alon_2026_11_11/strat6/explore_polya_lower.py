"""PROVED: exact Polya coefficient certificates for lower mixed moments."""
exec(open('explore_upper_moments.py').read().split('unit=matrices')[0])
records=[]
for k,bound in [(F(1),F(5,8)),(F(1),F(49,80)),(F(2),F(51,40)),(F(3),F(77,40))]:
 poly=QQ(bound.numerator,bound.denominator)*t*t*n-QQ(k.numerator,k.denominator)*A*n+t*C
 for power in range(25):
  mats=matrices(poly)
  bad=sum(not psd(m) for m in mats.values())
  print('PROVED: tested k',k,'bound',bound,'power',power,'forms',len(mats),'NUMERICAL: unresolved',bad,flush=True)
  if not bad:
   records.append(dict(k=str(k),bound=str(bound),power=power));break
  poly*=sum(z)
with open('polya_lower_bounds.json','w') as fp:json.dump(records,fp,indent=2)
