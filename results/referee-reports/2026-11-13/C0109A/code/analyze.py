import csv,json,math
from pathlib import Path
import numpy as np
from scipy import stats
rows=list(csv.DictReader(Path('data/simulations.csv').open()))
for r in rows:
 for k in r:r[k]=float(r[k])
result=[]
for eps in sorted(set(r['eps'] for r in rows)):
 group=[r for r in rows if r['eps']==eps]
 sizes=sorted(set(int(r['n']) for r in group))
 item={'eps':eps,'sizes':sizes,'replicates':len(group)//len(sizes)}
 for metric in ['dK','radial_discrepancy']:
  med=np.array([np.median([r[metric] for r in group if r['n']==n]) for n in sizes])
  fit=stats.linregress(np.log(sizes),np.log(med))
  fit_tail=stats.linregress(np.log(sizes[-3:]),np.log(med[-3:]))
  item[metric]={'medians':med.tolist(),'fitted_delta':-fit.slope,'tail3_delta':-fit_tail.slope,'r_squared':fit.rvalue**2,'log_slope_stderr':fit.stderr}
 item['largest_n_sample_variance']=[r['sample_variance'] for r in group if r['n']==sizes[-1]]
 result.append(item)
Path('data/fits.json').write_text(json.dumps(result,indent=2))
summary={'matrices':len(rows),'max_n':max(r['n'] for r in rows),'total_compute_seconds':sum(r['seconds'] for r in rows),'peak_rss_mb':max(r['rss_mb'] for r in rows),'epsilon_results':result}
Path('data/summary.json').write_text(json.dumps(summary,indent=2))
print('eps  delta_dK  tail3_dK  delta_radial  tail3_radial  median_dK_2048')
for x in result:
 print(x['eps'],*[round(x[k][f],5) for k,f in [('dK','fitted_delta'),('dK','tail3_delta'),('radial_discrepancy','fitted_delta'),('radial_discrepancy','tail3_delta')]],round(x['dK']['medians'][-1],6))
print('matrices',len(rows),'peak_MiB',summary['peak_rss_mb'],'seconds',summary['total_compute_seconds'])
