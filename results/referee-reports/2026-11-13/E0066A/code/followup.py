"""Extend only the two unresolved 1024-step numerical trajectories."""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import json
from pathlib import Path
import numpy as np
from experiments import simulate

operators=np.load('data/operators.npz')
rows=[]
for item in json.loads(Path('data/trajectory_details.json').read_text()):
    for i,period in enumerate(item['periods']):
        if period:continue
        periods,residuals,mass,major=simulate(operators[item['key']],
                                            [item['starts'][i]],steps=65536)
        row=dict(key=item['key'],start_index=i,steps=65536,
                 numerical_tail_period=periods[0],tail_residual=residuals[0],
                 max_mass_error=mass,max_majorisation_error=major)
        print(row)
        rows.append(row)
Path('data/followup.json').write_text(json.dumps(rows,indent=2)+'\n')
