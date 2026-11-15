"""Standalone research figure; data are the saved census and dense threshold outputs."""
import json,math,os
from pathlib import Path
for _thread_env in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:os.environ[_thread_env]='1'
os.environ['XDG_CACHE_HOME']=str(Path('localcache').resolve())
Path('localcache/fontconfig').mkdir(parents=True,exist_ok=True)
os.environ['MPLCONFIGDIR']=str(Path('mplconfig').resolve())
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
rows=[json.loads(Path(f'census_{n:02d}.json').read_text()) for n in range(1,25)]
dense=[json.loads(x) for x in Path('thresholds_dense.jsonl').read_text().splitlines()]
fig,axs=plt.subplots(1,3,figsize=(14,4.2),constrained_layout=True)
for ax,key,bound,limit in zip(axs,['A/I','B/I','Gamma/I'],[3.3252155,3.459354,1.6],[3,2/math.log(2),1/math.log(2)]):
 ax.plot([r['n'] for r in dense],[r['maxima'][key]['value'] for r in dense],color='#386cb0',lw=1.4,label='All thresholds')
 ax.scatter([r['n'] for r in rows],[r['maxima'][key]['value'] for r in rows],s=18,color='#222222',zorder=3,label='All symmetric functions')
 if key!='A/I':
  xs=[];ys=[]
  for n in [24,32,64,128,256,512,1000,1024,2000]:
   p=Path(f'hill_{n:04d}.json')
   if p.exists():
    v=max(s['final'][key] for s in json.loads(p.read_text())['searches'])
    if key=='Gamma/I' and n==2000 and Path('gamma_refinement_2000.json').exists():v=max(v,json.loads(Path('gamma_refinement_2000.json').read_text())['best'][key])
    xs.append(n);ys.append(v)
  ax.scatter(xs,ys,marker='x',s=27,color='#e08214',zorder=4,label='Value-vector search')
 ax.axhline(bound,color='#b2182b',lw=1,ls='--',label='Proved upper bound')
 ax.axhline(limit,color='#1b7837',lw=1,ls=':',label='Proved limiting lower bound')
 ax.set_xscale('log');ax.set_xlim(1,2000);ax.set_ylim(bottom=0)
 ax.set_xlabel('Number of variables n');ax.set_title(key.replace('Gamma','Γ'))
 ax.grid(alpha=.17,which='both');ax.spines[['top','right']].set_visible(False)
axs[0].set_ylabel('Bits per unit total influence')
handles,labels=axs[1].get_legend_handles_labels();fig.legend(handles,labels,loc='outside lower center',ncol=3,fontsize=8)
fig.savefig('functional_ratios.png',dpi=180);fig.savefig('functional_ratios.pdf')
print('Figure uses',len(dense),'threshold dimensions and census dimensions 1..24.')
