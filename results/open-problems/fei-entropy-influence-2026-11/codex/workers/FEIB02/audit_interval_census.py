import json
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps=100
old={(r['n'],r['objective']):r for r in json.loads(Path('certified_extrema.json').read_text())}
records=[];tight=True;largest_width=0
for n in range(1,25):
 row=json.loads(Path(f'census_interval_{n:02d}.json').read_text());q=row['scale']
 for name,a in row['maxima'].items():
  if a is None:continue
  lo,hi=a['lower_numerator'],a['upper_numerator'];ref=old[n,name]
  from symmetric import evaluate,mask_vector
  actual=evaluate(mask_vector(n,ref['extremizers_up_to_global_sign'][0]['mask']),110)[name];assert mp.mpf(lo)/q<=actual<=mp.mpf(hi)/q
  oldmask={x['mask'] for x in ref['extremizers_up_to_global_sign']}
  assert oldmask<=set(a['candidates']),(n,name,oldmask,a['candidates'])
  # Every possible maximizer, without floating-point discovery, is checked at 100 digits.
  from symmetric import evaluate,mask_vector
  vals=[evaluate(mask_vector(n,m),100)[name] for m in a['candidates']]
  assert abs(max(vals)-actual)<mp.mpf('1e-85')
  lround=(lo*10**10+q//2)//q;hround=(hi*10**10+q//2)//q
  tight=tight and lround==hround;largest_width=max(largest_width,(hi-lo)/q)
  records.append({'n':n,'objective':name,'lower':str(F(lo,q)),'upper':str(F(hi,q)),'rounds_to_10_decimals_rigorously':lround==hround,'candidates':a['candidates']})
Path('interval_extrema_audit.json').write_text(json.dumps(records,indent=2)+'\n')
print('every_possible_maximizer_from_integer_intervals_checked',True)
print('all_suprema_round_to_10_decimals_rigorously',tight)
print('largest_supremum_interval_width',largest_width)
