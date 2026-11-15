#!/usr/bin/env python3
"""Summarize raw approximation exponents without calling them dimensions."""
import csv,json,pathlib,statistics
root=pathlib.Path(__file__).resolve().parents[1]
j=json.loads((root/'data/simulation_summary.json').read_text())
summary=[]
for d in (4,5):
 for c in (.5,1.,2.):
  row={'d':d,'coefficient':c}
  for kind in ('exceptional_s_fit','selected_fiber_fit'):
   z=[f[kind]['slope'] for f in j['fits'] if f['d']==d and f['coefficient']==c and f[kind] is not None]
   row[kind]={'fitted_replicates':len(z),'median':statistics.median(z) if z else None,'minimum':min(z) if z else None,'maximum':max(z) if z else None}
  summary.append(row)
(root/'data/simulation_aggregate.json').write_text(json.dumps(summary,indent=2)+'\n')
for row in summary:
 def desc(k):
  z=row[k]
  if z['median'] is None:return 'no fit'
  return f"{z['fitted_replicates']}/4; {z['median']:.3f} [{z['minimum']:.3f}, {z['maximum']:.3f}]"
 print(f"| {row['d']} | {row['coefficient']:g} | {desc('exceptional_s_fit')} | {desc('selected_fiber_fit')} |")
