"""Summarize completed runs and plot observations against conjectured constants."""
import os
os.environ['MPLCONFIGDIR']=str(__import__('pathlib').Path(__file__).resolve().parents[1]/'data'/'matplotlib_cache')
os.environ['XDG_CACHE_HOME']=str(__import__('pathlib').Path(__file__).resolve().parents[1]/'data'/'cache')
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
import csv,json,math
from pathlib import Path
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1];mp.mp.dps=60
rs=[0.5,1.0,2.0,3.0]
constants={str(m):{str(r):str(4*mp.polylog(-mp.mpf(str(r)),mp.mpf(1)/m)/(m-1)) for r in rs}for m in [2,3]}
for m in [2,3]:
 assert mp.almosteq(mp.mpf(constants[str(m)]['1.0']),mp.mpf(4*m)/(m-1)**3)
 assert mp.almosteq(mp.mpf(constants[str(m)]['2.0']),mp.mpf(4*m*(m+1))/(m-1)**4)
 assert mp.almosteq(mp.mpf(constants[str(m)]['3.0']),mp.mpf(4*m*(m*m+4*m+1))/(m-1)**5)
 for r in rs:
  direct=4*mp.fsum(mp.mpf(k)**mp.mpf(str(r))*mp.mpf(m)**(-k)for k in range(1,1025))/(m-1)
  assert mp.almosteq(direct,mp.mpf(constants[str(m)][str(r)]))
(ROOT/'data'/'conjectured_constants.json').write_text(json.dumps(constants,indent=2))
summary=[];fig,axs=plt.subplots(2,3,figsize=(12,7))
for m,b in [(2,2),(2,5),(3,1),(3,3)]:
 paths=[ROOT/'data'/f'm{m}_b{b}_K{K}_native.csv'for K in [16384,32768]]
 datasets=[list(csv.DictReader(p.open()))for p in paths];a,z=datasets[0][-1],datasets[1][-1]
 row={'m':m,'b':b,'n':int(z['n']),'n2_q':float(z['n2_q']),
      'max_relative_cap_difference':max(abs(float(a[k])/float(z[k])-1)for k in a if k.startswith('n2_')),
      'conditional_TV_upper_estimate':float(z['conditional_TV_99']),
      'conditional_mean':float(z['conditional_moment_1.0'])}
 for r in rs:row['n2_moment_'+str(r)]=float(z['n2_moment_'+str(r)])
 summary.append(row);ns=[int(v['n'])for v in datasets[1]]
 label=f'initial support {{0,{b}}}'
 for col,r in enumerate([1.0,2.0]):
  target=float(constants[str(m)][str(r)])
  axs[m-2,col].semilogx(ns,[float(v['n2_moment_'+str(r)])/target for v in datasets[1]],'.-',label=label)
 axs[m-2,2].loglog(ns,[max(float(v['conditional_TV_99']),1e-18)for v in datasets[1]],'.-',label=label)
for i,m in enumerate([2,3]):
 for j in range(3):
  ax=axs[i,j];ax.set_xlabel('generation n');ax.grid(alpha=.25);ax.legend(fontsize=8)
  if j<2:
   ax.axhline(1,color='k',ls='--',lw=.8);ax.set_title(f'm={m}, moment r={j+1} / predicted constant');ax.set_ylabel(r'$n^2 E[X_n^r]/c(r,m)$')
  else:ax.set_title(f'm={m}, conditional geometric law');ax.set_ylabel('TV upper estimate (99 retained atoms)')
fig.suptitle('Critical fixed-offspring recursion: floating-point law iteration, K=32768')
fig.tight_layout();fig.savefig(ROOT/'data'/'moment_evidence.svg');fig.savefig(ROOT/'data'/'moment_evidence.png',dpi=140);plt.close(fig)
(ROOT/'data'/'summary.json').write_text(json.dumps(summary,indent=2))
for r in summary:print(r)
