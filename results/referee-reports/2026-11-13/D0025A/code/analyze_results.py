#!/usr/bin/env python3
import os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];os.chdir(ROOT)
os.environ['MPLCONFIGDIR']=str(ROOT/'data/.mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data/.cache')
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:os.environ[k]='1'
import csv,json,statistics
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
rows=list(csv.DictReader(open('data/ring_currents.csv')))
for r in rows:
 for k in r:
  if k!='init':r[k]=float(r[k])
assert len(rows)==94
assert all(r['nice']>=10 for r in rows)
assert all(0<=r['current']<=1 for r in rows)
assert all(r['min_bond_current']<=r['current']<=r['max_bond_current'] for r in rows)
summary={'records':len(rows),'sizes':sorted({int(r['n']) for r in rows}),'K_values':[1,2],'nice_values':sorted({int(r['nice']) for r in rows}),'r':.3,'p':.2,'mu':1/.3-(.2/.3+.8),'K1_theorem_plateau_height':.075,'K1_guaranteed_interval':[.36,.64],'long_central':{},'initialization_check':{}}
fig,axes=plt.subplots(1,2,figsize=(11,4.3),layout='constrained')
colors={2000:'#286f9f',10000:'#c67927',100000:'#466f47'}
for K,ax in zip([1,2],axes):
 for n in [2000,10000,100000]:
  available=[r for r in rows if r['n']==n and r['K']==K and r['env_seed']==125 and r['r']==.3 and r['init']=='random']
  # Use longest recorded run at a repeated density, exposing all run lengths in CSV.
  best={}
  for r in available:
   if r['rho'] not in best or r['measure']>best[r['rho']]['measure']:best[r['rho']]=r
  selected=sorted(best.values(),key=lambda r:r['rho'])
  ax.plot([r['rho'] for r in selected],[r['current'] for r in selected],'-o',ms=4,color=colors[n],label=f'n={n:,}')
 phase=[r for r in rows if r['K']==K and r['init']=='phase'][0]
 ax.plot(phase['rho'],phase['current'],'s',mfc='none',mec='#9b4154',ms=7,label='phase initial state, n=100,000')
 if K==1:
  ax.axhline(.075,color='black',ls='--',lw=1,label='infinite-system plateau r/4')
  ax.axvspan(.36,.64,alpha=.08,color='black')
 else:
  control=[r for r in rows if r['K']==2 and r['r']==1 and r['rho']==1][0]
  summary['K2_homogeneous_ring_center_current']=control['current']
  ax.axhline(.3*control['current'],color='black',ls=':',lw=1,label='r × homogeneous-ring center estimate')
 ax.set(xlabel=r'Density $\rho$',ylabel='Current per bond per unit time',title=f'Site disorder, K={K}',xlim=(0,K),ylim=(0,.19))
 ax.grid(alpha=.2);ax.legend(fontsize=7,loc='best')
 central=[r for r in rows if r['K']==K and r['n']==2000 and r['burn']==100000]
 summary['long_central'][str(K)]=[{k:r[k] for k in ['rho','current','block_sd','min_bond_current','max_bond_current']} for r in central]
 summary['initialization_check'][str(K)]=[{k:r[k] for k in ['rho','burn','measure','init','current','block_sd']} for r in rows if r['K']==K and r['n']==100000 and r['rho']==K/2]
fig.savefig('data/current_density.svg')
with open('data/summary.json','w') as f:json.dump(summary,f,indent=2)
with open('data/summary_tables.md','w') as f:
 f.write('| K | density | current | block SD | bond-current range |\n|---|---|---|---|---|\n')
 for K,rs in summary['long_central'].items():
  for r in rs:f.write(f"| {K} | {r['rho']:.2f} | {r['current']:.8f} | {r['block_sd']:.6f} | {r['min_bond_current']:.6f}–{r['max_bond_current']:.6f} |\n")
 f.write('\n| K | burn | measurement | initial state | center current |\n|---|---|---|---|---|\n')
 for K,rs in summary['initialization_check'].items():
  for r in rs:f.write(f"| {K} | {r['burn']:.0f} | {r['measure']:.0f} | {r['init']} | {r['current']:.8f} |\n")
print(json.dumps({k:summary[k] for k in ['records','sizes','nice_values','mu','K1_guaranteed_interval','K2_homogeneous_ring_center_current']},indent=2))
