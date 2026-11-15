"""Summarize complete roots, keeping intermediate levels and phase claims apart."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict
import csv,hashlib,json,math
import numpy as np
BASE=Path(__file__).resolve().parent
script=BASE/'simulate_depth_dependent_excursions.py'
digest=hashlib.sha256(script.read_bytes()).hexdigest()
directory=BASE/'computations'/f'c29_log_caps_M4000_src{digest[:10]}'
rows=[]
for source in sorted(directory.glob('p*_H*_rep*/root_summary.json')):
    record=json.loads(source.read_text(encoding='utf-8'))
    assert record['absolute_level']==0
    with np.load(source.parent/'population.npz',allow_pickle=False) as stored:
        assert int(stored['absolute_level'])==0
        values=stored['values'][:,0]
    assert len(values)==record['samples']
    record['q90_R1']=float(np.quantile(values,.9))
    record['mean_se_conditional_only']=float(np.std(values,ddof=1)/math.sqrt(len(values)))
    record['q95_R1']=float(np.quantile(values,.95))
    record['population_file']=str(source.parent/'population.npz')
    record['population_sha256']=hashlib.sha256((source.parent/'population.npz').read_bytes()).hexdigest()
    rows.append(record)
grouped=defaultdict(list)
for row in rows:
    grouped[(row['p'],row['horizon'])].append(row)
groups=[]
for (p,horizon),members in sorted(grouped.items()):
    result={'p':p,'horizon':horizon,'complete_replicates':len(members),'samples_per_rep':members[0]['samples']}
    if p=='1/4':
        result['exact_law_all_active_mean_upper_bound']=(horizon+2)/3
        result['normalized_mean_estimate']=float(np.mean([x['mean_R1'] for x in members]))/horizon
    for key in ('mean_R1','median_R1','q90_R1','q95_R1','pgf_half_R1'):
        vals=np.array([x[key] for x in members])
        result[key]={'mean_of_reps':float(np.mean(vals)),
                     'sd_between_reps':float(np.std(vals,ddof=1)) if len(vals)>1 else None,
                     'range':[float(np.min(vals)),float(np.max(vals))]}
    for cutoff in ('20','40','80'):
        vals=np.array([x['tails'][cutoff]['estimate'] for x in members])
        result[f'P_R1_ge_{cutoff}']={'mean_of_reps':float(np.mean(vals)),
                                   'sd_between_reps':float(np.std(vals,ddof=1)) if len(vals)>1 else None}
    groups.append(result)
now=datetime.now(timezone.utc).isoformat()
summary={'at':now,'source_sha256':digest,'completed_jobs':len(rows),'requested_jobs':24,
         'model_threshold':'UNRESOLVED','status':'numerical evidence',
         'error_bar_meaning':'Sample SD between independent full empirical-population runs; each root file also has conditional parent-sampling SE. Neither includes a bound on inherited bias or gives certified true-law coverage.',
         'groups':groups,'roots':rows}
(BASE/'C29_CURRENT_RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
with (BASE/'C29_ROOT_RESULTS.csv').open('w',encoding='utf-8',newline='') as stream:
    writer=csv.writer(stream)
    writer.writerow(['p','horizon','replicate','samples','mean_R1','median_R1','q90_R1','pgf_half_R1','pgf_conditional_SE','P_R1_ge20','P_R1_ge40','P_R1_ge80'])
    for r in rows:
        writer.writerow([r['p'],r['horizon'],r['replicate'],r['samples'],r['mean_R1'],r['median_R1'],r['q90_R1'],r['pgf_half_R1'],r['pgf_se_conditional_only'],r['tails']['20']['estimate'],r['tails']['40']['estimate'],r['tails']['80']['estimate']])
print(json.dumps({'completed':len(rows),'threshold':'UNRESOLVED','groups':groups}))
