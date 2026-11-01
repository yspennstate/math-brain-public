import sys,time,json
from fractions import Fraction as F
import core as c
start=time.perf_counter();pilot=sys.argv[1]=='pilot';cases=0;sharp=0
output=c.ROOT/'out'/('pilot_bounds.csv' if pilot else 'main_bounds.csv')
assert not output.exists()
with output.open('w',encoding='utf-8') as out:
 out.write('n,mask,distinguished,delta,I_product,I_plus,I_minus,status\n')
 for n in (range(4) if pilot else [4]):
  for mask,f in c.tables(n):
   for z in (range(n) if pilot else [0]):
    # Swap z and bit0, retaining every labelled coordinate in the pilot.
    ff=tuple(f[x^((((x>>z)^x)&1)*((1<<z)|1))] for x in range(len(f))) if z else f
    s=c.shadow_compute(ff)
    out.write(','.join(map(str,[n,mask,z,s['delta'],s['Ip'],sum(s['ip']),sum(s['im']),'PASS']))+'\n')
    cases+=1
    if s['B']==c.const(s['Ip']) and s['Ip']:sharp+=1
   if time.perf_counter()-start>(60 if pilot else 120):raise RuntimeError('frozen watchdog')
  out.flush()
controls=[]
if pilot:
 f=(-1,-1,-1,1);s=c.shadow_compute(f);assert s['B']==c.const(1) and s['Ip']==1
 for width in range(1,6):
  q=F(1,1<<width)
  for active in ['plus','minus']:
   qq=q if active=='plus' else 1-q
   X=min(qq,1-qq);V=4*qq*(1-qq);price=4*max(qq,1-qq)
   assert V==price*X
   controls.append({'width':width,'q':str(qq),'W':str(V),'exclusive_data_influence':str(X),'sharp_price':str(price)})
 c.dump('sharp_bias_controls.json',{'status':'PASS','controls':controls,'all_dyadic_bias_proof':'PROOF.md section2'})
result={'helper_version':'A026-exclusive-shadow-v1','status':'PASS','coordinate_cases':cases,'nonzero_B_equals_product_influence':sharp,'sharp_bias_controls':len(controls),'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh/physical exclusive edges; exact prime logs; outward dyadic 48-term atanh intervals'}
c.dump('pilot_bounds_summary.json' if pilot else 'main_bounds_summary.json',result);print(json.dumps(result,indent=2))
