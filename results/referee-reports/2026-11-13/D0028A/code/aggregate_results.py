#!/usr/bin/env python3
"""Aggregate all completed case artifacts, including the nondegenerate 3x3 torus."""
import csv,json,pathlib
R=pathlib.Path(__file__).resolve().parent.parent
base=json.loads((R/'data'/'verification.json').read_text())
if 'base_run' in base: base=base['base_run']
keys=['shape','model','boundary','q','n_sites','n_states','bp_fibers','graph_components',
      'exact_kernel_dimension','exact_rank','largest_fiber','absorbing_singletons',
      'exact_kernel_decomposition','exact_stationarity_residual','numeric_max_error',
      'nonproduct_fibers','elapsed_s']
results=[json.loads(p.read_text()) for p in sorted((R/'data').glob('*_q*-*.json'))]
with (R/'data'/'finite_summary.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for a in results:w.writerow({k:a[k] for k in keys})
out={'cases':len(results),'max_sites':max(a['n_sites'] for a in results),
     'max_states':max(a['n_states'] for a in results),
     'max_numeric_error':max(a['numeric_max_error'] for a in results),
     'all_exact_passed':all(a['exact_kernel_decomposition'] and a['exact_stationarity_residual']=='0' for a in results),
     'base_run':base,'extra_case_note':'3x3 FA2 torus, q=1/3, exact 512-state nullspace. Peak RSS was recorded only for the 56-case base run.'}
(R/'data'/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
