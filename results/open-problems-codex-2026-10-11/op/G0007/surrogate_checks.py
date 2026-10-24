import math,json,pathlib
out=[]
for d in [3,5,7,20]:
 b=d-1; c=1/b; A=2*d/(d-2)
 def theta(p):
  if p<=c:return 0.
  lo=0.;hi=1.
  # positive root: divided equation is decreasing and avoids the root u=0.
  def g(u):return sum(math.comb(b,k)*(-1)**(k+1)*p**k*u**(k-1) for k in range(1,b+1))-1
  for _ in range(100):
   mid=(lo+hi)/2
   if g(mid)>0:lo=mid
   else:hi=mid
  u=(lo+hi)/2
  return p*(-math.expm1(d*math.log1p(-p*u)))
 vals=[{'h':h,'ratio':theta(c+h)/h} for h in [1e-3,1e-4,1e-5]]
 assert abs(vals[-1]['ratio']/A-1)<.003
 out.append({'d':d,'predicted_site_slope':A,'finite_difference_checks':vals,'slope_ratio_colors':(d-2)**2})
pathlib.Path('surrogate_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
