import json,pathlib,statistics
for name in ['numerics.json','numerics_extended.json']:
 x=json.loads(pathlib.Path(name).read_text());print(name)
 for n in sorted({v['n'] for v in x}):
  a=[v for v in x if v['n']==n];key='corr' if 'corr' in a[0] else 'horizontal_corr';vs=[v[key] for v in a]
  print(n,'reps',len(a),'mean corr',statistics.mean(vs),'sd',statistics.stdev(vs))
  if 'rank_n_excess' in a[0]:print('mean opt/rank',[statistics.mean(v[k] for v in a) for k in ['opt_n_excess','rank_n_excess']])
print('rank two-point', (1.09**.5+9.09**.5)/2, 'cross two-point',(4.16**.5+4.04**.5)/2)
